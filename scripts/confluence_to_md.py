#!/usr/bin/env python3
"""Confluence 트리를 마크다운으로 내려받는다.

- URL / page-id / folder-id 중 하나를 받아 그 아래 트리 전체를 재귀 다운로드
- 접근 불가(403/404)한 페이지·폴더는 스킵하고 진행
- 현재(`status == "current"`) 상태의 자식만 저장 (archived/draft/trashed 제외)
- 저장 파일엔 메타데이터(YAML frontmatter) 없이 본문 마크다운만 기록

Auth:
- CONF_EMAIL + CONF_TOKEN (Atlassian Cloud basic)
- 또는 CONF_BEARER_TOKEN
"""

from __future__ import annotations

import argparse
import io
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Optional
from urllib.parse import urlparse

if TYPE_CHECKING:
    import requests 


DEFAULT_ENV_PATH = ".env"
DEFAULT_OUT_DIR = "exports/confluence"


@dataclass
class ExportStats:
    pages_saved: int = 0
    pages_skipped: int = 0
    folders_created: int = 0
    folders_skipped: int = 0


# ---------- env & args ----------

def load_dotenv_if_present(file_path: str = DEFAULT_ENV_PATH) -> None:
    """`.env`로 환경변수를 덮어쓴다 (파일이 진실의 원천)."""
    path = Path(file_path)
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key:
            os.environ[key] = value


def sanitize_file_name(value: str) -> str:
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value).strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned[:120] or "confluence-export"


def parse_root_from_url(raw_url: str) -> Optional[tuple[str, str]]:
    parsed = urlparse(raw_url)
    m = re.search(r"/pages/(\d+)", parsed.path)
    if m:
        return ("page", m.group(1))
    m = re.search(r"/folder/(\d+)", parsed.path)
    if m:
        return ("folder", m.group(1))
    m = re.search(r"(?:^|&)pageId=(\d+)(?:&|$)", parsed.query)
    if m:
        return ("page", m.group(1))
    return None


def resolve_root(args: argparse.Namespace) -> tuple[str, str]:
    if args.folder_id:
        return ("folder", args.folder_id)
    if args.page_id:
        return ("page", args.page_id)
    if args.url:
        root = parse_root_from_url(args.url)
        if root:
            return root
        raise SystemExit("URL에서 page/folder id를 찾지 못했습니다. --page-id 또는 --folder-id로 직접 지정해 주세요.")
    raise SystemExit("--page-id, --folder-id, 또는 --url 중 하나는 필요합니다.")


def resolve_base_url(args: argparse.Namespace) -> str:
    base_url = args.base_url or os.environ.get("CONF_BASE_URL")
    if not base_url and args.url:
        parsed = urlparse(args.url)
        if parsed.scheme and parsed.netloc:
            return f"{parsed.scheme}://{parsed.netloc}"
    if not base_url:
        raise SystemExit("CONF_BASE_URL이 필요합니다. 예: https://your-domain.atlassian.net")
    return base_url.rstrip("/")


# ---------- HTTP ----------

def build_session() -> "requests.Session":
    import requests

    bearer = os.environ.get("CONF_BEARER_TOKEN")
    email = os.environ.get("CONF_EMAIL")
    token = os.environ.get("CONF_TOKEN")

    session = requests.Session()
    session.headers.update({"Accept": "application/json"})

    if bearer:
        session.headers["Authorization"] = f"Bearer {bearer}"
    elif email and token:
        session.auth = (email, token)
    else:
        raise SystemExit("인증 정보가 없습니다. CONF_EMAIL + CONF_TOKEN 또는 CONF_BEARER_TOKEN을 설정해 주세요.")

    return session


def get_json_with_response(session, url: str, *, params: Optional[dict] = None, timeout: int = 30):
    response = session.get(url, params=params, timeout=timeout, allow_redirects=False)
    if 300 <= response.status_code < 400:
        raise SystemExit(
            f"Confluence API 리다이렉트: status={response.status_code}, "
            f"location={response.headers.get('Location') or '(empty)'}"
        )
    response.raise_for_status()
    if "json" not in response.headers.get("Content-Type", "").lower():
        raise SystemExit(f"JSON이 아닌 응답: {response.url}\nbody: {response.text[:400]}")
    return response, response.json()


def get_json(session, url: str, *, params: Optional[dict] = None, timeout: int = 30) -> dict:
    _, payload = get_json_with_response(session, url, params=params, timeout=timeout)
    return payload


def parse_next_link(link_header: Optional[str]) -> Optional[str]:
    from requests.utils import parse_header_links

    if not link_header:
        return None
    for link in parse_header_links(link_header.rstrip(">").replace(">,", ",<")):
        if link.get("rel") == "next" and link.get("url"):
            return link["url"]
    return None


# ---------- Confluence fetchers ----------

def _fetch_page_v1(session, base_url: str, page_id: str) -> dict:
    return get_json(
        session,
        f"{base_url}/wiki/rest/api/content/{page_id}",
        params={"expand": "body.export_view"},
    )


def fetch_page(session, base_url: str, page_id: str) -> dict:
    """v2 우선, 본문이 비면 v1으로 보강. 실패 시 예외 전파."""
    import requests

    try:
        payload = get_json(
            session,
            f"{base_url}/wiki/api/v2/pages/{page_id}",
            params={"body-format": "export_view"},
        )
        body_html = payload.get("body", {}).get("export_view", {}).get("value", "")
        if not body_html:
            try:
                v1 = _fetch_page_v1(session, base_url, page_id)
                v1_html = v1.get("body", {}).get("export_view", {}).get("value", "")
                if v1_html:
                    return {
                        "id": v1.get("id", page_id),
                        "title": v1.get("title", ""),
                        "status": v1.get("status", "current"),
                        "body_html": v1_html,
                    }
            except requests.HTTPError:
                pass
        return {
            "id": payload.get("id", page_id),
            "title": payload.get("title", ""),
            "status": payload.get("status", "current"),
            "body_html": body_html,
        }
    except requests.HTTPError as error:
        response = error.response
        if response is not None and response.status_code in {403, 404}:
            try:
                v1 = _fetch_page_v1(session, base_url, page_id)
                return {
                    "id": v1.get("id", page_id),
                    "title": v1.get("title", ""),
                    "status": v1.get("status", "current"),
                    "body_html": v1.get("body", {}).get("export_view", {}).get("value", ""),
                }
            except requests.HTTPError:
                raise error
        raise


def fetch_folder(session, base_url: str, folder_id: str) -> dict:
    """폴더 메타만 조회. 단건 GET이 404면 최소 객체로 폴백."""
    import requests

    try:
        payload = get_json(session, f"{base_url}/wiki/api/v2/folders/{folder_id}")
        return {
            "id": folder_id,
            "title": payload.get("title", f"folder-{folder_id}"),
            "status": payload.get("status", "current"),
        }
    except requests.HTTPError as error:
        response = error.response
        if response is not None and response.status_code == 404:
            return {"id": folder_id, "title": f"folder-{folder_id}", "status": "current"}
        raise


def list_direct_children(session, base_url: str, parent_type: str, parent_id: str) -> list[dict]:
    """현재(current) 상태의 page/folder 자식만 반환."""
    if parent_type == "page":
        next_url = f"{base_url}/wiki/api/v2/pages/{parent_id}/direct-children?limit=100"
    elif parent_type == "folder":
        next_url = f"{base_url}/wiki/api/v2/folders/{parent_id}/direct-children?limit=100"
    else:
        return []

    children: list[dict] = []
    while next_url:
        response, payload = get_json_with_response(session, next_url)
        for item in payload.get("results", []):
            if item.get("status", "current") != "current":
                continue
            if str(item.get("type", "")).lower() not in {"page", "folder"}:
                continue
            children.append(item)
        next_url = parse_next_link(response.headers.get("Link"))
    return children


# ---------- Markdown export ----------

def convert_html_to_markdown(html: str) -> str:
    from markitdown import MarkItDown
    from markitdown import StreamInfo

    md = MarkItDown()
    # Confluence API already returns Unicode text. Passing it through a temp
    # .html file lets MarkItDown guess a charset again, which can mis-detect
    # Korean-heavy pages like "Case ID" as Cyrillic encodings.
    return md.convert_stream(
        io.BytesIO(html.encode("utf-8")),
        stream_info=StreamInfo(
            mimetype="text/html",
            extension=".html",
            charset="utf-8",
        ),
    ).text_content


def resolve_directory(
    parent_dir: Path,
    title: str,
    entity_id: str,
    used_names: dict[Path, set[str]],
) -> Path:
    """부모 디렉터리 아래에 이 엔티티가 쓸 디렉터리 경로를 결정.

    - 기존에 같은 이름 디렉터리가 있어도(재실행) 그대로 재사용 → 파일이 덮어써진다.
    - 같은 실행 안에서 형제가 같은 제목이면 `(id)` 접미사로 구분한다.
    """
    base_name = sanitize_file_name(title)
    siblings = used_names.setdefault(parent_dir, set())
    if base_name not in siblings:
        siblings.add(base_name)
        return parent_dir / base_name
    # 이번 실행 안에서 형제 충돌 → ID 접미사로 구분
    fallback = f"{base_name} ({entity_id})"
    siblings.add(fallback)
    return parent_dir / fallback


def resolve_page_markdown_path(page_dir: Path, title: str, page_id: str) -> Path:
    """페이지 디렉터리 안에 저장할 마크다운 파일 경로를 결정한다."""
    file_name = sanitize_file_name(title or f"page-{page_id}")
    return page_dir / f"{file_name}.md"


def export_tree(
    session,
    base_url: str,
    root_type: str,
    root_id: str,
    parent_dir: Path,
    stats: ExportStats,
    max_depth: Optional[int],
    used_names: Optional[dict[Path, set[str]]] = None,
    depth: int = 0,
) -> Optional[Path]:
    import requests

    if used_names is None:
        used_names = {}

    # 1) 루트 처리 (page면 본문 저장, folder면 디렉터리만)
    if root_type == "page":
        try:
            page = fetch_page(session, base_url, root_id)
        except requests.HTTPError as error:
            status = error.response.status_code if error.response is not None else "?"
            print(f"[skip] page id={root_id} (status={status})", file=sys.stderr)
            stats.pages_skipped += 1
            return None

        if page.get("status", "current") != "current":
            print(f"[skip] page id={root_id} status={page.get('status')}", file=sys.stderr)
            stats.pages_skipped += 1
            return None

        title = page.get("title") or f"page-{root_id}"
        root_dir = resolve_directory(parent_dir, title, root_id, used_names)
        root_dir.mkdir(parents=True, exist_ok=True)

        html = page.get("body_html", "")
        if html:
            markdown = convert_html_to_markdown(html).strip() + "\n"
            markdown_path = resolve_page_markdown_path(root_dir, title, root_id)
            markdown_path.write_text(markdown, encoding="utf-8")
            stats.pages_saved += 1
        else:
            print(f"[skip] page id={root_id} 본문 없음", file=sys.stderr)
            stats.pages_skipped += 1

    elif root_type == "folder":
        try:
            folder = fetch_folder(session, base_url, root_id)
        except requests.HTTPError as error:
            status = error.response.status_code if error.response is not None else "?"
            print(f"[skip] folder id={root_id} (status={status})", file=sys.stderr)
            stats.folders_skipped += 1
            return None

        if folder.get("status", "current") != "current":
            print(f"[skip] folder id={root_id} status={folder.get('status')}", file=sys.stderr)
            stats.folders_skipped += 1
            return None

        title = folder.get("title") or f"folder-{root_id}"
        root_dir = resolve_directory(parent_dir, title, root_id, used_names)
        root_dir.mkdir(parents=True, exist_ok=True)
        stats.folders_created += 1

    else:
        raise SystemExit(f"지원하지 않는 루트 타입: {root_type}")

    # 2) 깊이 제한
    if max_depth is not None and depth >= max_depth:
        return root_dir

    # 3) 자식 재귀
    try:
        children = list_direct_children(session, base_url, root_type, root_id)
    except requests.HTTPError as error:
        status = error.response.status_code if error.response is not None else "?"
        print(f"[skip] {root_type} id={root_id} 자식 목록 실패 (status={status})", file=sys.stderr)
        return root_dir

    for child in children:
        child_id = str(child.get("id", "")).strip()
        child_type = str(child.get("type", "")).lower()
        if not child_id or child_type not in {"page", "folder"}:
            continue
        export_tree(
            session=session,
            base_url=base_url,
            root_type=child_type,
            root_id=child_id,
            parent_dir=root_dir,
            stats=stats,
            max_depth=max_depth,
            used_names=used_names,
            depth=depth + 1,
        )

    return root_dir


# ---------- CLI ----------

def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Confluence 트리를 마크다운으로 내려받기")
    parser.add_argument("--url", help="Confluence page/folder URL — 이 아래 전체 트리 다운로드")
    parser.add_argument("--page-id", help="Confluence page ID")
    parser.add_argument("--folder-id", help="Confluence folder ID")
    parser.add_argument("--base-url", help="Confluence base URL (예: https://your-domain.atlassian.net)")
    parser.add_argument("--out-dir", default=DEFAULT_OUT_DIR, help=f"출력 디렉터리 (기본: {DEFAULT_OUT_DIR})")
    parser.add_argument("--env-file", default=DEFAULT_ENV_PATH, help=f".env 경로 (기본: {DEFAULT_ENV_PATH})")
    parser.add_argument("--max-depth", type=int, help="최대 깊이 (0=루트만)")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    load_dotenv_if_present(args.env_file)

    root_type, root_id = resolve_root(args)
    base_url = resolve_base_url(args)

    if args.max_depth is not None and args.max_depth < 0:
        raise SystemExit("--max-depth는 0 이상이어야 합니다.")

    session = build_session()

    # 진단 라인: 어떤 자격증명으로 어디에 접속 중인지
    email = os.environ.get("CONF_EMAIL", "")
    token = os.environ.get("CONF_TOKEN", "")
    bearer = os.environ.get("CONF_BEARER_TOKEN", "")
    cred = bearer or token or ""
    auth_kind = "bearer" if bearer else ("basic" if (email and token) else "none")
    cred_prefix = cred[:8] if cred else "-"
    cred_suffix = cred[-8:] if len(cred) >= 8 else "-"
    print(
        f"[conf] base_url={base_url} auth={auth_kind} email={email or '-'} "
        f"token={cred_prefix}...{cred_suffix} (len={len(cred)})",
        file=sys.stderr,
    )

    stats = ExportStats()
    exported_root = export_tree(
        session=session,
        base_url=base_url,
        root_type=root_type,
        root_id=root_id,
        parent_dir=Path(args.out_dir),
        stats=stats,
        max_depth=args.max_depth,
    )

    print(f"saved_root: {exported_root}")
    print(f"pages_saved: {stats.pages_saved}")
    print(f"pages_skipped: {stats.pages_skipped}")
    print(f"folders_created: {stats.folders_created}")
    print(f"folders_skipped: {stats.folders_skipped}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except ModuleNotFoundError as error:
        missing = error.name or "(unknown)"
        print(
            f"[ModuleNotFoundError] 누락 모듈: {missing}\n"
            f"  실행한 Python: {sys.executable}\n"
            f"  - markitdown / requests 자체가 없으면: `pip install markitdown requests`\n"
            f"  - 위 패키지는 설치돼 있는데 다른 모듈이 누락된 거라면 해당 모듈을 설치하세요: `pip install {missing}`\n"
            f"  - venv를 쓰고 있다면 venv 활성화 후 같은 인터프리터에 설치했는지 확인하세요.",
            file=sys.stderr,
        )
        raise SystemExit(1) from error
    except Exception as error:
        try:
            import requests
        except ModuleNotFoundError:
            raise
        if isinstance(error, requests.HTTPError):
            response = error.response
            if response is not None:
                req_url = getattr(response.request, "url", "(unknown)")
                print(
                    f"Confluence API error: {response.status_code} {response.reason}\n"
                    f"  request: GET {req_url}\n"
                    f"  body: {response.text}",
                    file=sys.stderr,
                )
            else:
                print(f"HTTP error: {error}", file=sys.stderr)
            raise SystemExit(1) from error
        raise
    except KeyboardInterrupt:
        print("Interrupted.", file=sys.stderr)
        raise SystemExit(130)
