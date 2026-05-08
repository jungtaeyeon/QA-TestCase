# confluence_to_md.py

Confluence 페이지·폴더 트리를 마크다운으로 내려받는 스크립트.

- URL / page-id / folder-id 중 하나를 주면 **그 아래 트리 전체**를 재귀 다운로드
- 접근 불가(403/404)한 항목은 **스킵**하고 진행
- `status == "current"`인 페이지·폴더만 저장 (archived/draft/trashed 제외)
- 저장 파일엔 **메타데이터 없이** 본문 마크다운만 기록

## 의존성

```bash
pip install markitdown requests
```

## 환경 변수 (`.env`)

프로젝트 루트의 `.env` 파일에 다음을 설정:

```dotenv
CONF_BASE_URL=https://<workspace>.atlassian.net
CONF_EMAIL=you@example.com
CONF_TOKEN=<Atlassian API token>
```

### API 토큰 발급

- https://id.atlassian.com/manage-profile/security/api-tokens
- **Classic API token** (스코프 없음) 을 사용하면 간단합니다 — 계정 권한을 그대로 상속
- **Scoped token** 쓸 거면 최소 다음 스코프 필요:
  - `read:page:confluence`
  - `read:content-details:confluence`
  - `read:space:confluence`
  - `read:folder:confluence`
  - `read:hierarchical-content:confluence`

### Bearer 토큰 방식

`CONF_EMAIL` + `CONF_TOKEN` 대신 `CONF_BEARER_TOKEN` 하나만으로도 인증 가능.

## 기본 사용법

프로젝트 루트에서 실행. (`.env`가 현재 디렉터리 기준이므로)

### 1. URL로 전체 트리 다운로드 — 권장

```bash
python scripts/confluence_to_md.py \
  --url "https://selta.atlassian.net/wiki/spaces/IS/folder/23167000" \
  --out-dir ./exports/confluence
```

페이지 URL도 동일하게 동작 (해당 페이지 + 모든 하위 페이지):

```bash
python scripts/confluence_to_md.py \
  --url "https://selta.atlassian.net/wiki/spaces/IS/pages/23920679/01.+SafetyDB" \
  --out-dir ./exports/confluence
```

### 2. ID로 직접 지정

```bash
# 폴더
python scripts/confluence_to_md.py --folder-id 23167000 --out-dir ./exports/confluence

# 페이지
python scripts/confluence_to_md.py --page-id 23920679 --out-dir ./exports/confluence
```

### 3. 깊이 제한

```bash
python scripts/confluence_to_md.py \
  --url "https://selta.atlassian.net/wiki/spaces/IS/folder/23167000" \
  --out-dir ./exports/confluence \
  --max-depth 2
```

- `0` = 루트만
- `1` = 루트 + 직접 자식까지
- `2` = 손자까지
- 미지정 = 전체

## CLI 옵션

| 옵션 | 설명 |
|---|---|
| `--url` | Confluence page 또는 folder URL (아래 트리 전체) |
| `--page-id` | 페이지 ID 직접 지정 |
| `--folder-id` | 폴더 ID 직접 지정 |
| `--base-url` | Confluence base URL (기본: `$CONF_BASE_URL`) |
| `--out-dir` | 출력 디렉터리 (기본: `exports/confluence`) |
| `--env-file` | `.env` 경로 (기본: `.env`) |
| `--max-depth` | 최대 깊이 제한 (0 이상) |

## 결과 디렉터리 구조

```
exports/confluence/
└── <루트 제목>/
    ├── <루트 제목>.md          ← 루트가 페이지면 본문
    ├── <자식 페이지>/
    │   ├── <자식 페이지>.md
    │   └── <손자 페이지>/
    │       └── <손자 페이지>.md
    └── <자식 폴더>/
        └── <폴더 안 페이지>/
            └── <폴더 안 페이지>.md
```

- 각 페이지는 자기 이름의 디렉터리 + 그 안의 `제목.md` 1개로 저장
- 폴더는 빈 디렉터리로만 존재 (자식이 있으면 그 안에 채워짐)
- 파일 내용은 **본문 마크다운만** — YAML frontmatter/제목/링크 등 메타데이터 없음

## 재실행 / 업데이트

- 같은 `--out-dir`로 다시 실행하면 **기존 디렉터리를 재사용**하고 같은 제목의 `.md` 파일을 덮어씁니다
- `(id)` 접미사가 붙은 폴더가 생기지 않도록, 이름이 같은 형제가 실제로 있을 때만 구분 접미사가 붙습니다
- 삭제된 페이지의 마크다운 파일은 자동으로 지워지지 않습니다. 깔끔하게 새로 받으려면:

```bash
rm -rf ./exports/confluence
python scripts/confluence_to_md.py --url "..." --out-dir ./exports/confluence
```

## 실행 로그

시작 시 진단 한 줄:
```
[conf] base_url=https://selta.atlassian.net auth=basic email=hspark@seltasquare.com token=ATATT3xF...DC2F46B9 (len=192)
```
- `token=...` 로 실제 사용 토큰 식별 (앞 8자 + 뒷 8자)

처리 중 발생하는 로그:
- `[skip] page id=23560277 (status=404)` — 접근 불가로 스킵
- `[skip] page id=xxx 본문 없음` — API가 body를 주지 않음
- `[skip] folder id=xxx status=archived` — 현재 상태가 아님

마지막에 통계:
```
saved_root: exports/confluence/01. Information Security
pages_saved: 42
pages_skipped: 3
folders_created: 7
folders_skipped: 0
```
