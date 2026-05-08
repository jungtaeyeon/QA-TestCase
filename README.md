# SafetyDB QA Workflow

> SafetyDB 기획서를 기반으로 시나리오, 테스트케이스(TC), 리뷰, 업데이트를 관리하는 에이전트 사용 가이드입니다.

---

## 개요

이 저장소는 아래 흐름을 지원합니다.

1. 기획서 QA 분석서 생성
2. 테스트 시나리오 생성
3. TC CSV 생성
4. Figma 기반 UI TC 추가
5. TC 리뷰
6. 기획 변경 시 TC 업데이트
7. 필요 시 Testiny 업로드

모든 TC 규칙의 단일 정본은 [`tc-writing-rules`](/Users/heesu/Desktop/QA-Testcase/.github/skills/tc-writing-rules/SKILL.md)입니다.

---

## 폴더 구조

```text
SafetyDB/
├── Safety1.0/
│   ├── plan/                  # 기획서
│   └── TC/                    # 생성된 TC CSV
├── agent_output/
│   ├── analysis/              # QA 분석서 HTML
│   ├── scenario/              # 시나리오 산출물
│   ├── review/                # 리뷰 결과 / Figma 반영 리포트
│   └── changelog/             # TC 변경 이력
└── .github/
    ├── agents/
    └── skills/
```

주요 산출물 경로:

- QA 분석서: `agent_output/analysis/{기획서명}-QA분석.html`
- 시나리오: `agent_output/scenario/{기획서명}_시나리오.md`
- TC CSV: `TC/{기획서명}_TC.csv`
- 리뷰 결과: `agent_output/review/{TC파일명}_review.md`, `agent_output/review/{TC파일명}_review_actions.csv`
- 변경 이력: `agent_output/changelog/{날짜}_{대상}_변경내역.md`

---

## 에이전트

현재 저장소에 있는 에이전트만 정리합니다.

| 에이전트 | 역할 | 대표 산출물 |
|---------|------|------------|
| `Plan-Translator` | 기획서를 QA 분석서 HTML로 변환 | `agent_output/analysis/...` |
| `TC Generator` | 시나리오 생성, TC 생성, Figma 기반 TC 추가 | `agent_output/scenario/...`, `TC/...` |
| `TC-Reviewer` | TC Lint/커버리지/버그 발견력 리뷰 | `agent_output/review/...` |
| `TC-Update` | 기획/디자인 변경 반영, 변경 이력 정리 | `TC/...`, `agent_output/changelog/...` |
| `Doublecheck` | AI 산출물 검증 | 별도 검증 리포트/대화 |
| `Devils Advocate` | 아이디어/설계 리스크 스트레스 테스트 | 대화 중심 |

---

## 스킬

현재 저장소에 있는 스킬만 정리합니다.

| 스킬 | 역할 |
|------|------|
| `tc-writing-rules` | TC CSV 스키마, 필드 명세, 열거값, Lint, 작성 원칙의 단일 정본 |
| `scenario-guidelines` | 시나리오 도출 규칙, `Major > Minor` 분류, 산출물 형식 |
| `figma-tc` | Figma 디자인과 기존 TC를 비교해 UI TC를 추가/수정 |
| `testiny-upload` | Testiny 업로드 절차 및 필드 매핑 |
| `tooluniverse-pharmacovigilance` | PV 도메인 용어, 역할, 업무 맥락 |

---

## 기본 흐름

### 1. QA 분석서 생성

- 에이전트: `Plan-Translator`
- 입력: `plan/`의 기획서
- 출력: `agent_output/analysis/{기획서명}-QA분석.html`

예시:

```text
@Plan-Translator plan/Product_Config-0325.md 분석해줘
```

### 2. 시나리오 생성

- 에이전트: `TC Generator`
- 스킬: `scenario-guidelines`
- 출력: `agent_output/scenario/{기획서명}_시나리오.md`

예시:

```text
@TC Generator Sender 기획서 기반으로 시나리오 생성해줘
```

### 3. TC 생성

- 에이전트: `TC Generator`
- 기준 스킬: `tc-writing-rules`
- 출력: `TC/{기획서명}_TC.csv`

예시:

```text
@TC Generator Sender 기획서 기반으로 TC 생성해줘
```

### 4. Figma 기반 TC 추가

- 에이전트: `TC Generator`
- 스킬: `figma-tc`, `tc-writing-rules`
- 출력: 기존 TC CSV 반영 + `agent_output/review/{기획서명}_figma_tc_report.md`

예시:

```text
@TC Generator https://figma.com/design/xxx/yyy?node-id=1-2 디자인 기반으로 Sender TC에 UI TC 추가해줘
```

### 5. TC 리뷰

- 에이전트: `TC-Reviewer`
- 기준 스킬: `tc-writing-rules`
- 출력: `agent_output/review/{TC파일명}_review.md`, `agent_output/review/{TC파일명}_review_actions.csv`

예시:

```text
@TC-Reviewer Sender_TC.csv 리뷰해줘
```

### 6. TC 업데이트

- 에이전트: `TC-Update`
- 용도: 기획/디자인 변경 반영, 기존 TC 수정, 변경 이력 기록
- 출력: `TC/{기획서명}_TC.csv`, `agent_output/changelog/{날짜}_{대상}_변경내역.md`

예시:

```text
@TC-Update Sender 기획서가 변경됐어. 기존 TC 업데이트해줘
```

### 7. Testiny 업로드

- 에이전트: `TC Generator` 또는 `TC-Update`
- 스킬: `testiny-upload`
- 트리거: 사용자가 `업로드` 또는 `testiny`를 요청한 경우

예시:

```text
@TC Generator Sender TC testiny에 업로드해줘
```

---

## TC CSV 기준

정본은 [`tc-writing-rules`](/Users/heesu/Desktop/QA-Testcase/.github/skills/tc-writing-rules/SKILL.md)입니다. README에는 핵심만 요약합니다.

### CSV 헤더

```csv
folder_name,Testcase_Id,title,Preconditions,Test Steps,Expected Results,Priority,type,test scope,run_type,Notes,REQ_Id
```

- 영문 헤더가 정본입니다.
- 기존 한글 헤더는 업로드 시 별칭으로만 동등 처리합니다.

### 핵심 규칙

- `folder_name`: `A > B > C` ~ `A > B > C > D > E`
- `Testcase_Id`: `^[A-Z][A-Z0-9]*(-[A-Z][A-Z0-9]*)*-\d{3}$`
- `REQ_Id`: `^REQ_[a-z][a-z0-9]*(_[a-z][a-z0-9]*)*_\d+$`
- `Preconditions`, `Test Steps`: `1.`로 시작하는 번호 목록
- `test scope` 허용값:
  - `Regression`
  - `Integration`
  - `Regression,Smoke`
  - `Regression,E2E`
  - `Regression,E2E,Smoke`
  - `Integration,Smoke`
- `E2E` 단독 사용 금지
- `Smoke` 단독 사용 금지

### Testiny 필드 매핑

| CSV 컬럼 | 한글 별칭 | Testiny 필드 |
|----------|----------|-------------|
| `folder_name` | — | Test Case Folder |
| `Testcase_Id` | — | External ID |
| `title` | — | Title |
| `Preconditions` | `사전 조건` | Precondition |
| `Test Steps` | `테스트 스텝` | Steps |
| `Expected Results` | `예상 결과` | Expected Result |
| `Priority` | — | Priority |

---

## 빠른 시작

### 전체 흐름

```text
@Plan-Translator Sender 기획서 분석해줘
@TC Generator Sender 기획서 기반으로 시나리오 생성해줘
@TC Generator Sender 기획서 기반으로 TC 생성해줘
@TC-Reviewer Sender_TC.csv 리뷰해줘
```

---

## ClickUp Doc Export

ClickUp Doc 링크를 Markdown으로 저장할 수 있는 간단한 스크립트를 제공합니다.

```text
export CLICKUP_API_TOKEN=your_token
# 또는 .env 에 CLICKUP_API_TOKEN=your_token 추가
# 또는 .env 에 CLICKUP_API_KEY=your_token 추가
node scripts/clickup-doc-to-md.mjs "링크"
node scripts/clickup-doc-to-md.mjs "링크" "./저장폴더명/저장파일명.md"
node scripts/clickup-doc-to-md.mjs "링크" "링크"
node scripts/clickup-doc-to-md.mjs --input ./clickup-links.txt --out-dir ./exports/clickup
```

- `docs/...` 와 `v/dc/...` 형식의 ClickUp Doc 링크를 모두 지원합니다.
- 페이지 링크를 넣으면 해당 페이지와 하위 페이지를 함께 `.md`로 저장합니다.
- 여러 링크를 한 번에 넣으면 각각 별도 `.md` 파일로 일괄 저장합니다.

### Figma 반영 포함

```text
@TC Generator Sender 기획서 기반으로 TC 생성해줘
@TC Generator https://figma.com/design/xxx/... Sender TC에 UI TC 추가해줘
@TC-Reviewer Sender_TC.csv 리뷰해줘
```

### 변경 반영

```text
@TC-Update Sender 기획서가 변경됐어. 기존 TC 업데이트해줘
```

### 보조 검증

```text
@Doublecheck 생성된 TC 설명 검증해줘
@Devils Advocate 이 시나리오 설계의 약점을 찾아줘
```

---

## 참고

- 기획서에 없는 기능, 로직, 조건, 데이터는 만들지 않습니다.
- PV 도메인 문서라면 `tooluniverse-pharmacovigilance`를 함께 참조합니다.
- 상세 규칙 변경은 README가 아니라 `tc-writing-rules`에서 관리합니다.
