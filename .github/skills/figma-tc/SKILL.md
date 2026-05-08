---
name: figma-tc
description: PV 도메인 Figma 디자인, 기획서, 기존 TC를 3-way 비교하여 누락/변경/추가 사항을 모두 식별하고 tooluniverse-pharmacovigilance를 활용해 PV 맥락으로 TC를 생성·수정·정리하는 절차를 정의합니다. USE FOR: Figma 디자인 TC 추가, UI TC, 변경점 분석, TC 동기화, 기획-디자인 불일치 점검
---

# Figma 디자인 기반 TC 동기화 가이드

> **목적**: Figma 디자인과 기획서, 기존 TC CSV를 3-way 비교하여 **Missing · Changed · Added · Removed Candidate · Mismatch**를 식별하고, TC를 생성/수정/정리합니다.
> **TC 작성 규칙**: `tc-writing-rules` 스킬의 스키마·열거값·Lint를 준수합니다.
> **시나리오 연계**: `scenario-guidelines` 스킬의 시나리오 산출물(예상 유형, 5관점, TC 매핑 상태)을 활용합니다.
> **PV 전제**: 모든 테스트 대상은 PV 도메인으로 간주하며, Figma에서 읽힌 UI 요소도 `tooluniverse-pharmacovigilance`를 통해 PV 업무 맥락과 규제 리스크 관점에서 해석합니다.

## 기획서 참조 (필수)

> **`common.instructions.md`의 Graphify 선택적 사용 규칙을 따릅니다.**
> `plan/` 대상 기획서를 `view` / `read_file`로 읽고, 자료 2종 이상 또는 기획서 2건 이상이면 `graphify query`/`explain`/`path`로 교차 분석합니다.
> Figma 분석 결과와 `graphify query`/`explain`/`path` 결과를 비교하여 `[Figma Only]`, `[Mismatch]`를 판단합니다.

이 스킬은 세 파트로 구성됩니다.
- **Part A. 공통 규칙** — 시나리오 생성과 TC 추가 모두에 적용
- **Part B. 시나리오 지침** — Figma를 입력 소스로 시나리오 도출 시 적용
- **Part C. TC 지침** — Figma 기반 TC 추가/수정 시 적용

---

## Part A. 공통 규칙

> 시나리오 생성(기능 1)과 TC 추가(기능 3) 모두에 적용합니다.

### A-1. 핵심 원칙

1. Figma 분석은 **구조화된 정보 기반**으로 수행합니다. `get_screenshot`만으로 TC/시나리오를 생성하지 않습니다.
2. **기획서에 없더라도 Figma에 명확히 존재하는 기능/상태/문구/인터랙션은 반드시 검증 범위에 포함**합니다. 단, 기획 근거가 없으면 `[Figma Only]`로 명시합니다.
3. 단순 장식 요소나 기능 의도가 불명확한 것은 검증 대상으로 단정하지 않습니다.
4. 기획서와 충돌하는 경우에는 충돌 사실을 반드시 기록합니다.
5. 디자인의 시각적 표현뿐 아니라 **상태, 조건, 인터랙션, 문구, 제약, 권한 차이**까지 검증 범위에 포함합니다.
6. Figma에서 확인한 필드/상태/문구가 PV 업무 용어, 규제 필드, 보고/승인 흐름과 연결되는지 반드시 확인합니다.

---

### A-2. 도구 사용 기준

| 우선순위 | 도구 | 용도 |
|----------|------|------|
| 1차 | `get_design_context` | 화면 구조, 컴포넌트 구성, 상태 분기, 계층 관계, 주요 텍스트/속성 파악 |
| 2차 | `get_metadata` | 노드명, 컴포넌트명, variant, frame 구조 보강 |
| 보조 | `get_variable_defs` | 상태값, 토큰, variant 규칙, 조건 분기 해석 |
| 보조 | `get_screenshot` | 구조화 정보만으로 시각 차이를 판단하기 어려운 경우에만 사용 |

**금지**: `get_screenshot`만 보고 TC/시나리오 생성, 기획/디자인/기존 TC 중 하나만 보고 결론

---

## Part B. 시나리오 지침

> Figma가 시나리오 도출의 **입력 소스**로 사용될 때 적용합니다 (tc-generator 기능 1 + Figma URL 동반 시).

1. **Part A의 도구(A-2)**로 Figma에서 아래 항목을 추출합니다.
   - 화면 단위 기능, 컴포넌트 상태(empty/loading/error/disabled)
   - 문구/placeholder/tooltip/validation message
   - 권한별·조건별 노출 차이, 인터랙션, 내비게이션 경로
   - PV 필드명, 코드값, 상태명, 보고/승인 액션 등 도메인 의미가 있는 UI 요소
2. 추출한 항목을 입력 소스로 삼아 **`scenario-guidelines` 스킬의 Step 0~6**에 따라 시나리오를 도출합니다.
   - Figma 추출 항목은 Step 0-2(범위/용어 정리)과 Step 1(명세 검증 트리 작성)의 입력 재료로 사용합니다.
   - 이후 Step 2~6(5관점·설계기법·우선순위·품질 게이트·리뷰 기준)은 `scenario-guidelines`를 그대로 따릅니다.
   - 이때 `tooluniverse-pharmacovigilance`를 활용해 Figma 항목이 PV 도메인에서 어떤 검증 의미를 가지는지 해석합니다.
3. 기획서에 없고 Figma에만 존재하는 항목은 시나리오 title에 **`[Figma Only]`** 태그를 붙입니다.
4. 기획서와 Figma가 충돌하는 항목은 시나리오의 `확인 필요 사항`에 **`[Mismatch]`** 태그로 기록합니다.

---

## Part C. TC 지침

> Figma 기반 TC 추가/수정 시 적용합니다 (tc-generator 기능 3).

### C-1. 실행 절차

#### Step 1. 시나리오·기존 TC·기획서 범위 확인
1. `agent_output/scenario/`에서 해당 기획서의 시나리오 산출물을 읽습니다.
   - 시나리오 리뷰가 완료되었는지 확인 (`리뷰 이력` 테이블)
   - 시나리오 ID(`SC-XXX-NNN`) → TC ID(`TC-XXX-NNN-nnn`) 매핑 관계 확인
   - 각 시나리오의 **예상 유형**과 **관점 태그** 확인
   - **유형별 분포** 테이블로 전체 커버리지 현황 파악
2. `TC/` 폴더에서 해당 기획서의 기존 TC CSV를 읽습니다.
3. 기획서를 참조하여 기존 TC가 커버하는 기능 범위를 파악합니다.

#### Step 2. Figma 구조화 분석
`get_design_context` → `get_metadata` → 필요 시 `get_variable_defs` → 마지막에만 `get_screenshot` 순서로 분석하여 아래를 추출합니다.

- 화면 단위 기능, 컴포넌트 종류와 상태, interaction 요소
- 문구/placeholder/tooltip/validation message
- empty/loading/error/disabled state
- 권한별/조건별 노출 차이, 디자인 annotation 규칙
- 화면 구조 변경, 컴포넌트 variant 변경, 내비게이션 경로, 데이터 표시 규칙

#### Step 3. 기존 TC 커버리지 매핑 및 중복 대조
기존 TC CSV를 읽고 각 TC가 커버하는 기능·시나리오·상태·조건·권한·기대결과를 매핑합니다. 이후 Step 5에서 신규 TC 후보와 대조할 기준으로 사용합니다.

중복으로 보이는 TC라도 바로 삭제하지 말고, Figma/기획과 다시 대조합니다.

#### Step 4. 3-way 비교 수행
기획서 / Figma / 기존 TC를 비교하여 모든 항목을 아래 다섯 가지로 분류합니다.

- `Missing`: 기획 또는 디자인에 있으나 TC에 없음
- `Changed`: 기존 TC는 있으나 조건/문구/상태/동작이 바뀜
- `Added`: Figma에 신규 기능/UI/상태가 추가됨
- `Removed Candidate`: 기존 TC는 있으나 기획/디자인에서 제거된 것으로 보임
- `Mismatch`: 기획과 디자인이 상충함

#### Step 5. 중복 검증 및 TC 생성/수정

신규 TC 후보마다 Step 3에서 매핑한 기존 TC와 대조하여 중복 여부를 판정합니다.

**중복 판정 기준** — 다음 조건 중 **2개 이상** 일치하면 중복

1. **검증 대상 동일**: 같은 화면/컴포넌트/기능을 검증
2. **검증 조건 동일**: 같은 선행조건, 입력값, 상태를 전제
3. **검증 포인트 동일**: 같은 기대결과를 확인

**처리 규칙**

| 상황 | 처리 |
|------|------|
| 완전 중복 | 신규 TC 생성하지 않음. 리포트에 "기존 TC 커버" 기록 |
| 부분 중복 | 기존 TC에 스텝/기대결과 추가하여 확장 |
| 유사하지만 조건 상이 | 별도 TC 생성. `Memo`에 관련 TC Id 참조 기록 |
| `Missing` / `Added` | 새 TC 생성 |
| `Changed` | 기존 TC 행을 직접 수정 |
| `Removed Candidate` | 삭제하지 않고 리포트에 기록 |
| `Mismatch` | 검증 가능한 범위로 TC 반영, `확인 필요`로 표기 |

**TC type 결정**: `tc-writing-rules` Step 3의 설계 기법 → type 매핑에 따라 결정합니다.
- 에러 메시지·필수값 표시·버튼 활성/비활성 → `Functional` 또는 `Negative`
- 경계값 → `Boundary`
- 권한 차이 → `Security`
- 응답성·접근성·레이아웃 등 순수 품질 속성 → `Performance`

**run_type 결정**: `tc-writing-rules` 섹션 4.4의 결정 트리에 따라 `Automation`, `Manual`, `Both`를 지정합니다.

**시나리오 예상 유형과의 정합성**: 신규/수정 TC의 type이 시나리오의 예상 유형과 일치하는지 확인합니다. 분화가 발생하면 `Memo`에 분화 사유를 기록합니다.

**설계 기법 기록**: 신규/수정 TC의 도출 근거가 된 설계 기법을 `Memo`에 태그로 기록합니다 (예: `[EP]`, `[BVA]`, `[ST]`).

#### Step 5-1. PV 도메인 보강

TC 초안 완성 후 아래 관점으로 보강합니다:
- **용어 정확성**: TC 내 PV 용어가 표준(MedDRA, E2B, ICH)과 일치하는지 확인
- **규제 필드 커버리지**: Figma에 표시된 Required/Conditional 필드가 모두 TC에 포함되었는지 확인
- **코드 체계 검증**: 국가코드, MedDRA PT, Sender Type 등 코드값 관련 TC 존재 확인
- **하류 영향**: Figma 변경이 ICSR 보고서 생성 등 하류 기능에 미치는 영향 TC 확인
- **PV 체크포인트 태그**: `tc-writing-rules` 섹션 2의 PV 체크포인트 해당 여부 확인 후 `Memo`에 태그 기록

#### Step 6. 품질 검증

**6-1. Lint 검증**: `tc-writing-rules` 섹션 4의 Lint 규칙 전체 통과 확인
**6-2. 커버리지 검증**:
- 시나리오 예상 유형 대비 실제 TC type 분포 비교
- 참조 문서(개별 항목 검증 룰 등) 대상 필드 전체 TC 커버 확인
- 기능 영역별 Functional/Negative/Boundary/Security/Performance 최소 커버리지 확인
- Smoke TC가 전체의 10~20% 범위 내인지 확인

**6-3. 기대결과 3관점 확인**:
- 프론트(화면·메시지) + 데이터(DB/API 변경) + 하류 영향(목록·로그·알림)

#### Step 7. 시나리오 역추적 및 결과 저장

**시나리오 역추적** (`tc-writing-rules` Step 5 준수):
- 시나리오 산출물의 `TC 매핑 상태` 테이블에 실제 TC ID 범위와 TC 작성 상태를 기입
- 예상 유형 대비 분화 발생 시 `예상 유형` 열에 실제값 병기
- Figma 분석 중 발견된 신규 확인 필요 사항은 시나리오의 `확인 필요 사항`에 추가

**TC CSV 저장**:
- `Changed`는 기존 행 직접 수정, `Missing`/`Added`는 새 행 추가
- 저장 경로: `TC/{기획서명}_TC.csv`

**변경 리포트 저장**:
- 채팅 출력 금지, 반드시 Markdown 파일로 생성
- 저장 경로: `agent_output/review/{기획서명}_figma_tc_report.md`

리포트 필수 섹션:

```markdown
## 변경 요약
(신규 추가 / 수정 / 확장(중복 병합) / 중복 제외 / 삭제 후보 / 확인 필요 각 N건)

## 신규 추가 TC
## 수정된 TC
## 기존 TC 확장 (중복 병합)
## 중복으로 제외된 TC 후보
## 삭제 후보 TC
## 확인 필요 사항


## 설계 기법 적용 요약
| 설계 기법 | 적용 대상 | TC ID 범위 |
|----------|----------|-----------|

## 시나리오-TC 매핑 (신규/수정분)
| 시나리오 ID | 예상 유형 | 실제 TC type |  TC ID | 분화 사유 |
|------------|----------|-------------|-------|----------|

## 커버리지 매트릭스
| 기능 영역 | Functional | Negative | Boundary | Security | Performance | 합계 |
|----------|-----------|---------|---------|---------|-----------|-----|
```

---

### C-2. 변경 TC 수정 규칙

기존 TC가 존재하더라도 아래 항목이 달라졌으면 `Changed`로 분류하고 기존 TC 행을 직접 수정합니다.

버튼/문구 텍스트, 노출 조건, 기본값, 기대 결과, 상태 전이, 입력 제한, 권한 정책, 화면 이동 결과

### C-3. 삭제 후보 규칙

기존 TC가 아래 조건이면 `Removed Candidate`로 분류합니다. 즉시 삭제하지 말고 리포트에 먼저 기록합니다.

- 기획서에서 제거됨
- Figma에서도 제거됨
- 대체 플로우로 통합됨
- UI 명칭/구조가 바뀌어 기존 TC 그대로는 유효하지 않음