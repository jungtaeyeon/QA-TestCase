# Graph Report - /Users/taeyeon/vscode/QA-Testcase  (2026-04-22)

## Corpus Check
- 2 files · ~26,479 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 50 nodes · 102 edges · 9 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]

## God Nodes (most connected - your core abstractions)
1. `exportPageTree()` - 10 edges
2. `export_tree()` - 8 edges
3. `main()` - 8 edges
4. `exportWholeDoc()` - 8 edges
5. `buildMarkdownSections()` - 7 edges
6. `main()` - 7 edges
7. `get_json()` - 5 edges
8. `fetch_page()` - 5 edges
9. `list_direct_children()` - 5 edges
10. `extractTitle()` - 5 edges

## Surprising Connections (you probably didn't know these)
- `get_json()` --calls--> `get_json_with_response()`  [EXTRACTED]
  /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py → /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py  _Bridges community 4 → community 5_
- `fetch_folder()` --calls--> `get_json()`  [EXTRACTED]
  /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py → /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py  _Bridges community 5 → community 6_
- `export_tree()` --calls--> `list_direct_children()`  [EXTRACTED]
  /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py → /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py  _Bridges community 4 → community 6_
- `export_tree()` --calls--> `resolve_directory()`  [EXTRACTED]
  /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py → /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py  _Bridges community 3 → community 6_
- `main()` --calls--> `export_tree()`  [EXTRACTED]
  /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py → /Users/taeyeon/vscode/QA-Testcase/scripts/confluence_to_md.py  _Bridges community 6 → community 0_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.36
Nodes (9): build_session(), ExportStats, load_dotenv_if_present(), main(), parse_args(), parse_root_from_url(), `.env`로 환경변수를 덮어쓴다 (파일이 진실의 원천)., resolve_base_url() (+1 more)

### Community 1 - "Community 1"
Cohesion: 0.36
Nodes (10): apiGet(), buildMarkdownSections(), buildSectionHeading(), collectPageNodes(), exportPageTree(), exportWholeDoc(), extractMarkdown(), extractTitle() (+2 more)

### Community 2 - "Community 2"
Cohesion: 0.42
Nodes (8): exportOne(), fail(), loadDotEnvIfPresent(), loadUrlsFromFile(), main(), parseCliArgs(), parseClickUpDocUrl(), printUsage()

### Community 3 - "Community 3"
Cohesion: 0.4
Nodes (5): 부모 디렉터리 아래에 이 엔티티가 쓸 디렉터리 경로를 결정.      - 기존에 같은 이름 디렉터리가 있어도(재실행) 그대로 재사용 → 파일이, 페이지 디렉터리 안에 저장할 마크다운 파일 경로를 결정한다., resolve_directory(), resolve_page_markdown_path(), sanitize_file_name()

### Community 4 - "Community 4"
Cohesion: 0.5
Nodes (4): get_json_with_response(), list_direct_children(), parse_next_link(), 현재(current) 상태의 page/folder 자식만 반환.

### Community 5 - "Community 5"
Cohesion: 0.67
Nodes (4): fetch_page(), _fetch_page_v1(), get_json(), v2 우선, 본문이 비면 v1으로 보강. 실패 시 예외 전파.

### Community 6 - "Community 6"
Cohesion: 0.5
Nodes (4): convert_html_to_markdown(), export_tree(), fetch_folder(), 폴더 메타만 조회. 단건 GET이 404면 최소 객체로 폴백.

### Community 7 - "Community 7"
Cohesion: 1.0
Nodes (2): buildDefaultOutputPath(), sanitizeFileName()

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (2): ensureMarkdownExtension(), writeMarkdown()

## Knowledge Gaps
- **6 isolated node(s):** ``.env`로 환경변수를 덮어쓴다 (파일이 진실의 원천).`, `v2 우선, 본문이 비면 v1으로 보강. 실패 시 예외 전파.`, `폴더 메타만 조회. 단건 GET이 404면 최소 객체로 폴백.`, `현재(current) 상태의 page/folder 자식만 반환.`, `부모 디렉터리 아래에 이 엔티티가 쓸 디렉터리 경로를 결정.      - 기존에 같은 이름 디렉터리가 있어도(재실행) 그대로 재사용 → 파일이` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 7`** (2 nodes): `buildDefaultOutputPath()`, `sanitizeFileName()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 8`** (2 nodes): `ensureMarkdownExtension()`, `writeMarkdown()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `export_tree()` connect `Community 6` to `Community 0`, `Community 3`, `Community 4`, `Community 5`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Why does `list_direct_children()` connect `Community 4` to `Community 0`, `Community 6`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `fetch_page()` connect `Community 5` to `Community 0`, `Community 6`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **What connects ``.env`로 환경변수를 덮어쓴다 (파일이 진실의 원천).`, `v2 우선, 본문이 비면 v1으로 보강. 실패 시 예외 전파.`, `폴더 메타만 조회. 단건 GET이 404면 최소 객체로 폴백.` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._