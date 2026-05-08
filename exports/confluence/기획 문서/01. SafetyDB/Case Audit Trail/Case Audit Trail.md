|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 홍수정 | 26.04.06 | 컬럼명 수정  Follow-up No → FU No | v1.0 | v1.0.260406 |
| 김나정 | 26.03.23 | 최초 작성 | v1.0 | v1.0.260323 |

# 프로토타이핑

<https://seltaglobal.sharepoint.com/sites/RDDivision/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype%2FCaseAuditTrail%2Dv2%2Ehtml&parent=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype>

# 설계 개요

* 목적: 데이터 변경의 전 과정을 기록하여 추적성(Traceability)을 확보하고, QC 활동의 근거 데이터를 제공함.
* 핵심 컨셉: [Case ➔ Report ➔ Save Point]로 이어지는 구조.
* 기획서에 기재된 내용 중 AI 관련 내용은 이번 버전에 고려하지 않는데 [추후 적용]

# 관리 체계

* Level 1 (Case ID): 선택 시 해당 케이스 전체 기간의 모든 로그 노출.
* Level 2 (Report Type): Initial, Follow-up 1, Follow-up 2 등을 구분.
* Level 3 (Save Point): 각 리포트 내에서 '저장'이 발생한 시점(YYYY-MM-DD HH:MM:SS)별로 리스팅.

## 맹검 데이터 처리

* 동작: 맹검된 Case의 Audit Log 조회 시, Study Drug 관련 필드 등의 New/Old Value를 `********`로 마스킹 처리함.
* 주의: 로그 자체는 남기되 내용만 가려, 데이터가 수정되었다는 사실은 알 수 있게 함.

# 데이터 내보내기

* 형식: Excel 포맷 지원.
* 범위: 현재 사용자가 선택한 필터링, 기간 등을 적용하여 전체 audit trail 내보내기 가능.
* 포함 정보: 누가, 언제 추출했는지에 대한 워터마크 포함.

# Case Audit Trail 페이지

### Case Audit Trail 그리드 컬럼

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 카테고리 | 컬럼 출력명 | 필드 데이터 매핑 | 상세 규칙 및 로직 | 컬럼 정렬 및 필터링 |
| Audit Trail Page | Case ID | C.1.1 | 해당 로그가 속한 케이스의 고유 번호 | 정렬 |
|  | Category |  | Option   1. Case 2. Workflow Action (추후) 3. User Context (추후) | 필터링 |
|  | FU No |  | Follow-up 차수 (Initial = 0, Follow-up = 1, 2...) | 정렬, 필터링 |
|  | Action |  | 1. Add 2. Edit 3. Delete | 필터링 |
|  | Time Stamp |  | 반영된 일시. | 정렬 |
|  | Performer |  | 사용자 | 필터링 |
|  | Details |  | Modal 표시 버튼 | - |
|  |  |  |  |  |
| Modal | FU No |  | Follow-up 차수 (Initial = 0, Follow-up = 1, 2...) | 정렬, 필터링 |
|  | Revision Sequence |  | 동일 케이스 안에서 버전 표시  저장 포인트마다 시퀀스가 늘어남 | 필터링 |
|  | Time Stamp |  | 반영된 일시. | 정렬 |
|  | Classification |  | 그가 발생한 구체적인 기술적/업무적 맥락 | 필터링 |
|  | Element |  | 변경의 대상이 되는 데이터 항목 | - |
|  | Action |  | NEW, EDIT, DELETE 등 액션 종류 | 필터링 |
|  | Previous Value |  | 변경 전 데이터. 최초 생성 시 `-` 표기 | - |
|  | Current Value |  | 변경 후 데이터 | - |
|  | Performer |  | 수행자. Case audit list와 동일하게 표시 | 필터링 |

## Performer (수행자)

|  |  |  |
| --- | --- | --- |
| **분류** | **대상 액션 및 필드** | **상세 로직** |
| User Name | 수동/반자동 조작 | 1. Performer가 System으로 정해진 것 외에 모든 사항의 행위자 |
| System: 고정 | 자동 계산/부여 | 1. AE type 2. RA Triage 3. FU No 4. CASE ID 부여 5. Report 생성시에 추가되는 C.1.1/C.1.8.1 |
| [추후] AI | 지능형 자동 입력 | 1. [추후] AI Convert 기능을 통한 데이터 자동 입력 시 |

## 로그 분리 원칙

단일 저장 시점(Save Point)에 여러 액션이 동시에 발생하더라도, 수행자(Performer)가 다를 경우 반드시 별개의 로그 행(Row)으로 분리하여 기록

* 원칙: 1개 저장 시점(Timestamp) 내에 `User`, `System` 액션이 혼재할 경우, 각각 독립된 행으로 생성함.
* 시나리오 예시 (Case FU 생성 시):

  + 사용자가 [Save] 클릭 ➔ 사용자 명의의 `CASE_CREATE` 로그 생성.
  + 동시에 시스템이 일련번호와 차수를 부여 ➔ System 명의의 `FU Info`로그 생성.
  + 결과: Audit Trail List에는 동일한 시간에 두 개의 행이 나란히 표시됨.

## 리스트 정렬 및 구분 우선순위

감사 로그 그리드(Main Page) 및 모달 리스트의 정렬 순서

1. 1순위: Time Stamp (최신순) - 언제 일어난 일인가?
2. 2순위: Performer (행위자별) - 누가/무엇이 수행했는가? (`User` > `System` 순)

# Audit Log에 기록되어야 할 세부 액션 정의

## 감사 로그 분류 데이터

감사 로그는 단순히 "누가 고쳤다"를 넘어 "어떤 맥락에서(Classification) 무엇을(Element) 어떻게(Action) 했는가"를 추적

|  |  |  |  |
| --- | --- | --- | --- |
| **분류 수준** | **명칭** | **설명** | **예시** |
| Level 1 | Category | 업무의 큰 범주 | 1. Case 2. Workflow Action (추후) 3. User Context (추후) |
| Level 2 | Classification | 로그가 발생한 구체적인 기술적/업무적 맥락 | Field Section 표시 |
| Level 3 | Action | 데이터에 가해진 실제 동작 | NEW (생성), EDIT (수정), DELETE (삭제) |
| Level 4 | Element | 변경의 대상이 되는 데이터 항목 | Patient Name, AE Term, Case Status 등 |

## 카테고리

구조:

* Category (대분류): "어떤 업무 범주인가?"
* Classification (중분류/소분류): "어떤 분류에 속하는가?"
* Action (동작): "데이터에 무슨 동작을 했나?">New, Edit, Delete
* Element (요소)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 시나리오 | Category | Action | Classification | Element | Value (Previous & Current) | Performer | 비고 |
| 1. 직접 사례 생성 2. 자동 사례 생성 3. 수동 사례 삭제 | Case | 1. NEW 2. NEW 3. DELETE | Case Lifecycle | CASE ID | Tracker List 에 표시되는 Case ID (일련번호) | 1. System (고정) 2. System (고정) 3. 행위자 유저 이름 |  |
| 사례 정보 입력 (AI) | NEW | Field Section | 1. 필드 title | 해당 필드 입력값 | 1. AI (추후 적용) | 추후 적용 |
| 사례 정보 입력 (Import) | NEW | Field Section | 1. 필드 title | 해당 필드 입력값 | 1. 행위자 유저 이름 |  |
| 사례 정보 입력 (수동) | NEW, EDIT, DELETE | Field Section | 1. 필드 title | 해당 필드 입력값 | 1. 행위자 유저 이름 |  |
| 사례 정보 입력 (FU) | NEW | Field Section | 1. 필드 title | 해당 필드 입력값 | 1. 행위자 유저 이름 |  |
| 사례 업데이트에 따른 정보 업데이트 | 1. NEW, EDIT 2. NEW, EDIT 3. NEW, EDIT 4. NEW 5. NEW | System Logic | 1. Reporting Due 2. AE Type 3. FU Info 4. Check Result 5. Check Result | 1. Tracker List\_RA 2. Tracker List\_AE Type 3. Tracker List\_FU No 4. 케이스 생성 시 판별 여부 (중복 시 Duplication) 5. 케이스 생성 시 판별 여부 (후속 시 Duplication Follow-up) | 1. System (고정) 2. System (고정) 3. System (고정) 4. 행위자 유저 이름 5. 행위자 유저 이름 | Check Result의 경우, 케이스 생성 시 중복, 후속 판별 여부 표시 |
| 1. 상태 변경 2. 담당자 자동 지정 (최초) 3. 담당자 변경 4. 담당자 이관 | Workflow Action | 1. EDIT 2. NEW 3. EDIT 4. EDIT | 1. Forward/Backward 2. Auto-assign 3. Assignee Change 4. Ownership Handover | 1. Case Status 2. Assignee 3. Assignee 4. Owner |  |  | 추후 적용 |
| 1. 사례 의견 | User Context | 1. NEW, EDIT, DELETE | 1. Comment | 1. 필드 title |  |  | 추후 적용 |

## 반복 필드 식별(Index) 가이드

### Classification (세션/블록 단위 식별)

데이터가 속한 ICSR 표준의 상위 태그(Parent Tags)를 기준으로 인덱스를 생성.

* 일반 반복 필드: `명칭 + 숫자` 조합으로 표시

  + 예: Product 1, Event 2
  + 개발 참고: E2B R3의 I(E.i) 또는 K(G.k) 등 반복되는 상위 노드의 순번을 매핑
* 복합 관계 필드 (Causality 등): 연관된 두 개 이상의 블록을 조합하여 표시

  + 예: Product 1 Event 1 (1번 약물과 1번 이상사례의 인과성 평가 세션임을 명시)

### Element (세부 필드 단위 식별)

특정 세션(Classification) 안에서도 다시 반복되는 세부 항목들을 구분

* 필드 내 반복: `필드명 + 숫자` 조합으로 표시

  + 예: Indication (MedDRA code) 1, Dosage Regimen 2
  + 개발 참고: 한 제품 내 여러 적응증이 있는 경우처럼, 하위 반복 태그(R(r) 등)의 순번을 매핑

## Case Audit Trail 상단 필터 및 검색 사양

|  |  |  |  |
| --- | --- | --- | --- |
| **구분** | **컴포넌트 타입** | **검색 대상 및 로직** | **비고** |
| 데이터 검색 | 검색 | 특정 키워드를 직접 입력하여 데이터 내에서 검색  (시간이 모자랄 경우 Case ID, Performer 만이라도 검색) | Main Key 검색 |
| Date Range | 기간 선택 필터 (Calendar) | 로그가 발생한 시작일 ~ 종료일 기간을 설정함. | Time Stamp 기준 |
| Search | 실행 버튼 | 설정된 모든 필터 조건을 결합하여 하단 리스트를 새로고침함. |  |
| Reset | Reset 버튼 | 모든 필터를 초기화하고 전체 리스트로 돌아가는 버튼을 제공 |  |

#### 기간 설정 규칙

* 기본값: 최근 1년 기간을 디폴트로 자동 설정하여 초기 로딩 부하를 방지
* 시간 기준: 설정된 날짜의 시작일 00:00:00 ~ 종료일 23:59:59까지의 로그를 포함

## Modal 상세 데이터 매핑

### 모달 UI 상단: Revision/Save Point 리스트

|  |  |  |
| --- | --- | --- |
| **컬럼명** | **출력 데이터 값 (Value)** | **상세 로직** |
| Check Box | 선택 여부 | 하단 상세 그리드와 연동 (디폴트는 최신 Revision 선택) |
| FU info | 0 (Initial), 1F, 2F... | 해당 케이스의 Follow-up 차수 정보 표시 |
| Revision Sequence | 1, 2, 3... | 동일 FU 내에서 [저장]이 발생한 순차적 번호 |
| User | 수정한 사용자 이름 | Performer 데이터 |
| Date | YYYY-MM-DD HH:mm:ss | 서버 기준 저장 완료 시점 (Time Stamp) |

### 감사 로그 모달 상세 조회 로직

#### 기본 정책

* 다중 선택 허용: 사용자는 상단 리스트에서 개수에 제한 없이 Revision Sequence를 체크 가능
* 실시간 합산 노출:

  + 1개 선택 시: 해당 시퀀스(저장 시점)에 발생한 변경 필드만 하단에 노출.
  + N개 선택 시: 선택된 모든 시퀀스에서 발생한 변경 필드들을 하나의 통합 리스트로 합쳐서 노출.
* 정렬 규칙: 합산된 리스트는 기본적으로 [Date(최신순)]로 정렬

|  |  |  |  |
| --- | --- | --- | --- |
| **구분** | **사용자 액션** | **시스템 반응** | **비고** |
| 개별 체크/해제 | 상단 리스트 특정 행의 [체크박스] 클릭 | 1. 해당 행의 선택 상태를 Toggle. 2. 하단 그리드에 해당 시퀀스의 데이터를 추가하거나 제거(Add/Remove). | 실시간 반응 |
| 전체 선택/해제 | (필요 시) 헤더의 [전체 선택 체크박스] 클릭 | 1. 현재 리스트에 보이는 모든 시퀀스의 데이터를 하단 그리드에 통합 로드. | 대량 데이터 QC용 |
| 하단 그리드 업데이트 | 다중 시퀀스 데이터 수신 시 | 1. 선택된 모든 `Revision Sequence ID`에 해당하는 필드 변경 로그를 쿼리. 2. 중복 없이 시간 역순(최신순)으로 전체 리스트 재구성. | Revision Seq 컬럼으로 시점 구분 |

### 모달 UI 하단: 필드별 변경 상세

#### Case Audit 모달 (Follow-up 및 데이터 수정 시)

|  |  |  |  |
| --- | --- | --- | --- |
| **컬럼명** | **출력되는 값의 형태** | **예시 (Case Changed / F/U 발생 시)** | 비고 |
| FU No | 현재 케이스의 차수 | 1F (Follow-up 1차 수정 중임을 의미) |  |
| Revision Sequence | 해당 차수 내 저장 순번 | 3 (1F 리포트의 3번째 저장 시점) |  |
| Time Stamp | 일시 | 2026-03-24 14:00:00 |  |
| Classification | 수정된 데이터의 섹션 | Event, Drug, Patient 등.. |  |
| Element | 타겟이 되는 데이터 | Field Name, AE type.. |  |
| Previous Value | 수정되기 전의 기존 데이터 | Dizziness, 10mg |  |
| Current Value | 수정 후 업데이트된 데이터 | Syncope, 20mg |  |
| Performer | 수행자 | 김나정, System |  |

# 와이어프레임

### Case Audit Trail 페이지

![](https://t37003623.p.clickup-attachments.com/t37003623/51c720f4-f5b6-4aa8-bd0b-38bb2f0c884c/image.png)

### Case Audit Trail 모달

![](https://t37003623.p.clickup-attachments.com/t37003623/335a6de9-7ea1-482a-b9c0-2a204a4f4a88/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | 1. 현재 조회 중인 감사 로그 데이터를 엑셀 파일로 추출함. | 1. 클릭 시 설정된 필터 조건(기간, 사용자 등)이 적용된 전체 리스트를 다운로드함. 2. 파일에는 추출자 정보와 일시가 포함된 워터마크가 삽입됨. |
| 2 | 1. 특정 액션에 대한 이벤트 상세 내용을 확인하는 모달을 호출함. 2. 호출 기준은 케이스 ID | 1. 클릭 시 Audit Trail Detail 모달이 팝업됨. 2. 선택한 행의 `Case ID`, `FU No` 정보가 모달로 전달 |
| 3 | 1. 현재 모달에서 상세 내용을 조회 중인 케이스의 고유 번호를 표시함. (일련번호만 있는 케이스 ID를 표시함) | 1. - |
| 4 | 1. 저장 시점의 Save Point를 표시함 2. 표시 정보: Follow-up No, 시퀀스 넘버(리비전 넘버), 저장 일시, 저장한 사람 3. 디폴트로 save point 중 최신것만 선택되어 있음 4. 최신 순으로 정렬 5. 참고: 맹검된 데이터는 `********`로 마스킹되어 표시됨. | 1. 전체 시퀀스 체크 시 모든 `Revision Sequence`가 선택되며, 그리드에 모든 시퀀스의 변경 사항이 통합되어 리스트업됨. 2. 이력 리스트 정렬은 최신순(Date)을 따름. 3. 개별 체크: 해당 시점의 변경 사항만 우측에 노출. 4. 다중 체크: 선택된 여러 시퀀스의 데이터를 실시간으로 합산하여 우측에 노출. |
