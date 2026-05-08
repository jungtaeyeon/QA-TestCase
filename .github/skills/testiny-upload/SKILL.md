---
name: testiny-upload
description: PV 도메인 TC를 Testiny MCP로 업로드하는 절차와 CSV-Testiny 필드 매핑을 정의합니다. tooluniverse-pharmacovigilance를 활용해 PV 용어·리스크 맥락이 보존되는지 확인합니다. USE FOR: Testiny 업로드, TC 등록, 필드 매핑, 폴더 매칭
---

# Testiny 업로드 가이드

> **목적**: TC CSV를 Testiny에 업로드하는 절차와 필드 매핑 규칙을 관리합니다.
> **CSV 스키마**: `tc-writing-rules` 스킬의 §2를 정본으로 합니다.
> **시나리오 연계**: 업로드 완료 후 `scenario-guidelines` 산출물의 TC 매핑 상태를 업데이트합니다.
> **트리거**: 사용자가 `업로드` 또는 `testiny`를 요청했을 때 실행
> **PV 전제**: 모든 테스트 대상은 PV 도메인으로 간주하며, 업로드 전 `tooluniverse-pharmacovigilance`를 사용해 PV 용어·규제 리스크·역할 맥락이 TC에 보존되었는지 확인합니다.

## 기획서 참조 (필수)

> **`common.instructions.md`의 Graphify 선택적 사용 규칙을 따릅니다.**
> `plan/` 대상 기획서를 `view` / `read_file`로 읽고, 자료 2종 이상 또는 기획서 2건 이상이면 `graphify query`/`explain`/`path`로 교차 분석합니다.

---

## 1. 업로드 절차

### Step 1. 사전 검증
업로드 전 TC CSV가 `tc-writing-rules` 품질 기준을 충족하는지 확인합니다.
- Lint 규칙 전체 통과 여부 (섹션 4 참조)
- 시나리오 역추적 완료 여부 (`TC 매핑 상태` 테이블 기입 확인)
- PV 용어, 역할/권한, 규제/업무 리스크 관련 TC가 누락 없이 포함되었는지 확인
- 미통과 시 업로드를 중단하고 사용자에게 보정 안내

### Step 2. 프로젝트 및 폴더 매칭
1. Testiny MCP `listProjects`로 대상 프로젝트를 확인합니다.
2. `listTestCaseFolders`로 기존 폴더 구조를 조회합니다.
3. CSV의 `folder_name` 기준으로 Testiny 폴더를 매칭합니다.
   - 매칭되는 폴더가 없으면 사용자에게 새 폴더 생성 여부를 확인합니다.

### Step 3. TC 등록
각 TC를 `createTestCase`로 등록합니다. 필드 매핑은 섹션 2 참조.

### Step 4. 등록 결과 검증
1. 등록 결과를 요약합니다 (총 등록 수, 폴더별 등록 수, 실패 건).
2. 실패 건이 있으면 원인을 분류합니다 (필드 형식 오류, 폴더 미매칭, API 오류 등).
3. 등록된 TC 수와 CSV TC 수의 정합성을 확인합니다.
4. 업로드된 TC의 제목, Preconditions, Expected Results, REQ_Id에 PV 도메인 용어와 근거 추적 정보가 손실 없이 유지되었는지 확인합니다.

### Step 5. 시나리오 역추적 확인
업로드 완료 후 시나리오 산출물의 `TC 매핑 상태`가 최신인지 확인합니다.
- TC 작성 상태를 `미작성` → `업로드 완료`로 갱신
- 업로드 실패 건은 `업로드 실패`로 표시하고 사유 기록

---

## 2. 업로드 필드 매핑

> **CSV 헤더는 영문이 정본입니다.** 기존 한글 헤더를 가진 CSV를 처리할 때는 아래 한글 별칭으로 동등 매핑합니다. 신규 CSV는 반드시 영문 헤더를 사용합니다.

| CSV 컬럼 (정본) | 한글 별칭 | Testiny 필드 | 비고 |
|----------------|----------|-------------|------|
| `folder_name` | — | Test Case Folder | 폴더 매칭/생성. 3~6단계 `>` 구분 |
| `Testcase_Id` | — | External ID | `TC-[약어]-[시나리오순번]-[TC순번]` 형식 |
| `title` | — | Title | 필수. 50자 이하 |
| `Preconditions` | `사전 조건` | Precondition | |
| `Test Steps` | `테스트 스텝` | Steps | |
| `Expected Results` | `예상 결과` | Expected Result | |
| `Priority` | — | Priority | `Critical` / `High` / `Medium` / `Low` |
| `type` | — | Custom Field 또는 Tag | `Functional` / `Negative` / `Boundary` / `Security` / `Performance` |
| `test scope` | — | Custom Field 또는 Tag | `Regression`, `Integration`, `Smoke`, `E2E` (복수 시 쉼표 구분. Smoke·E2E 단독 불가) |
| `run_type` | — | Custom Field 또는 Tag | `Automation` / `Manual` / `Both` |
| `Memo` | — | Description 또는 Custom Field | 플로우 맥락, 암묵적 요구사항 태그, 설계 기법 태그 등 |
| `REQ_Id` | — | Custom Field 또는 Linked Requirement | `{ID} ({문서명} {위치})` 또는 `{문서명} {위치}` 형식. 복수 시 쉼표 연결 |

> `type`, `test scope`, `run_type`, `Memo`, `REQ_Id`는 Testiny 프로젝트 설정에 따라 Custom Field 또는 Tag로 매핑합니다. 프로젝트에 해당 필드가 없으면 사용자에게 생성 여부를 확인합니다.

---

## 3. 업데이트 (TC-Update 용)

기존 TC를 수정·삭제·추가할 때의 Testiny 연동 절차입니다.

### 기존 TC 조회 및 비교
- Testiny MCP `listTestCases`로 현재 등록된 TC를 조회합니다.
- 로컬 `TC/` CSV와 Testiny 데이터를 `Testcase_Id` 기준으로 비교하여 동기화 상태를 확인합니다.
  - 로컬에만 있는 TC / Testiny에만 있는 TC / 내용이 다른 TC를 식별합니다.

### 업데이트 실행
사용자가 변경 목록을 승인한 후 Testiny에 반영합니다.
- 수정: `updateTestCase`로 변경된 필드만 업데이트
- 추가: `createTestCase`로 신규 등록
- 삭제: 즉시 삭제하지 않고 사용자 승인 후 처리. 삭제 대상은 리포트에 기록

### 업데이트 후 검증
- 등록/수정/삭제 결과를 요약합니다.
- 시나리오 산출물의 `TC 매핑 상태`를 갱신합니다.