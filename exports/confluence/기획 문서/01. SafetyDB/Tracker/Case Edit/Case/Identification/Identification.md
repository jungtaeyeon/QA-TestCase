|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.23 | 필드별 룰, 비고, 로직 추가 | v1.0 | v1.0.260423 |
| 김나정 | 26.04.03 | 최초 작성 | v1.0 | v1.0.260403 |

# 1. 개요

---

* **목적**: ICSR(개별 사례 안전성 보고서)의 식별 및 관리 정보를 입력하고, 규제기관 보고를 위한 기초 데이터를 생성함.
* **핵심 로직**:

  + 자동 식별자 생성: 보고자 관리번호(C.1.1), 고유식별 보고자관리번호(C.1.8.1)의 경우 승인(Approval) 전까지는 예상값(Preview)을 노출하고, 승인 시점에 값을 확정함(수정 불가).
  + 인지일 정합성: 최초 인지일(C.1.4)과 최신 정보 인지일(C.1.5) 간의 선후 관계 검증.
  + 조건부 활성화: 보고 구분 및 국가 코드에 따른 하위 필드 제어.
* **페이지 위치**: Tracker>Case Edit>Case>Identification

# 2. 출력 정보

---

## 2.1 상세 필드 명세

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증 룰 | 비고 |
|  | Case ID | Case ID | 필수 | 자체 필드 |  | * Console> ICSR Configuration>Case ID에서 설정한 값 중 [국가코드]와 [조직 식별자]를 제외한 정보를 입력함 * Read Only 로 표시, 수정 불가 |
|  | Sender’s (case) Safety Report Unique Identifier | 보고자관리번호 | 필수 | C.1.1 |  | * Read Only 로 표시, 수정 불가 * Initial: 현재 입력된 사례 정보를 기준으로 예상되는 값을 Preview, Approval 전까지 사례 정보를 기준으로 [국가 코드]를, Configuration 값을 기준으로 [조직 식별자]를 업데이트 ​    + Approval 완료 상태인 경우: 해당 시점의 최신 사례 정보를 기준으로 값을 확정​하고 고정 * FU: Initial에서 값이 확정된 경우에는 동일하게 확정, 미확정된 경우에는 동일하게 예상값을 표시만 하기.​ |
|  | Worldwide Unique Case Identification | 고유식별 보고자관리번호 | 필수 | C.1.8.1 |  | * Read Only 로 표시, 수정 불가 * Import, Convert등으로 기 보고 사례를 생성하여 C.1.8.1 값이 이미 있는 경우 :​    + 이 경우에는 고정 값으로 변경되지 않는다.​ * 자사 최초 수집 건으로 C.1.8.1 값이 없는 경우 :​    + Initial: 현재 입력된 사례 정보를 기준으로 예상되는 값을 Preview, Approval 전까지 사례 정보를 기준으로 국가를, Configuration 값을 기준으로 조직을 업데이트 ​      - Approval 완료 상태인 경우: 해당 시점의 최신 사례 정보를 기준으로 값을 확정​하고 고정   + FU: Initial에서 값이 확정된 경우에는 동일하게 확정, 미확정된 경우에는 동일하게 예상값을 표시만 하기. |
|  | Date Report Was First Received from Source | 최초 발생인지일 | 필수 | C.1.4 | 가장 최근의 발생인지일(C.1.5) 필드와 같거나 이전 날짜인지 검증​ | 1. 최초 보고된 Case인 경우 (Intake&Triage로 입력) ▶ 새로 입력한 값을 C.1.5 (Date of Most Recent Information for This Report;가장 최근의 발생인지일)와 C.1.4 (Date Report Was First Received from Source;최초 발생인지일)에 동일하게 입력​ 2. FU 보고된 Case인 경우 (FU report로 입력) ▶이전 버전 값 유지 & 수정 불가능 |
|  | Date of Most Recent Information for This Report | 가장 최근의 발생인지일 | 필수 | C.1.5 | FU 보고서 생성시 Amendment 또는 Nullification 선택했는지 (C.1.11.2: True) 검증​ | 1. 최초 보고된 Case인 경우 (Manual Intake로 입력) ▶ 새로 입력한 값을 C.1.5 (Date of Most Recent Information for This Report;가장 최근의 발생인지일)와 C.1.4 (Date Report Was First Received from Source;최초 발생인지일)에 동일하게 입력​ 2. FU 보고된 Case인 경우 (FU report로 입력) ▶ FU 보고서 생성시 Amendment 또는 Nullification 선택했는지 (C.1.11.1: Value=1 또는 2) 검증 ​     1. Follow-up 선택 ▶ 새로 입력한 값을 C.1.5 (Date of Most Recent Information for This Report;가장 최근의 발생인지일)에 업데이트. ​    2. Amendment or Nullification 선택 (C.1.11.1: Value=1 또는 2) ▶ 이전 버전 값 유지 & 수정 불가능​ |
|  | Type of Report | 보고 구분 | 필수 | C.1.3 | '시험/연구에서 보고 Report from study​'를 선택한 경우에는 Study ID 필드를 활성화 | * 필드 활성 조건: NA​ * 입력: Intake & Triage에서 입력한 값 그대로 입력 후 수정가능​ * Option 값:​    + 자발적 보고 Spontaneous Report​   + 시험/연구에서 보고 Report from study​   + 기타 other​   + 정보 이용불가(불명) Not available to sender (unknown)​ |
|  | Does This Case Fulfil the Local Criteria for an Expedited Report? | 신속보고 여부 | 필수 | C.1.7 |  | * 필드 활성 조건: C.3.4.5 Sender’s Country Code 의 값이 ​KR일 때​    + AE type = SUSAR (임상 & 치료목적) 일 때는 값을 True (False인 경우에는 보고대상이 아님)​   + AE type = SADR (시판후) 일 때는 값을 True​   + 나머지는 값을 False​ * KR이 아닐 때 ▶ 직접 입력​ * Option 값: ​    + Yes 예 true​   + No 아니오 false​ |
|  | Follow Up Number | 추적보고 번호 | 옵션 | 자체 필드 | * Max length: 4​ | * Tracker에 있는 follow-up No인데, 이전에는 중간에 계약되어서 내가 받은게 최초가 아닐때, 기록하는 용도를 겸하고 있었기 때문에 수동 입력으로만 가능 (정보성 필드) |
|  | Report Nullification / Amendment | 보고 무효화/수정 | 옵션 | C.1.11.1 |  | * Intake&Triage를 통해 Case 생성하는 경우 (DB에 해당 Case ID 최초 생성하는 경우) ▶ 비활성​ * FU Report 생성시 ▶ 해당 정보가 Amendement면 Value=2, Nullification이면 Value=1, Follow-up이면 Value 없음으로 처리한다. |
|  | Reason for Nullification / Amendment | 보고 무효화/수정 이유 | 옵션 | C.1.11.2 |  | * Free text + 언어 추가 입력 필드​ |
|  | Are Additional Documents Available? | 추가 자료 여부 | 필수 | C.1.6.1 |  | * 필드 활성 조건: NA​ * 입력: C.1.6.1.Selta.1 /C.1.6.1.r.1/ C.1.6.1.r.2 앞의 세가지 field (화면의 1. Additional Documents) 중 하나라도 값이 있으면 True로 자동 입력한다. ​ * Option값: false, true​    + true일 경우 C.1.6.1.r.1의 묶음 세션이 활성화 |
| 묶어서 한 행으로 표시. +선택시 묶어서 추가 | Documents Held by Sender | 자료 설명 | 옵션 | C.1.6.1.r.1 |  | * Table 컬럼 내 공간이 부족한 경우에는 줄임표 (…)으로 표시​ |
| Document Type | 자료 구분 | 옵션 | C.1.6.1.r.1에 연결 필드 |  | * Option 값:​    + 1=Clinical records (CRF)​   + 2=Hospital records​   + 3=Medical certificate​   + 4=Autopsy reports​   + 5=ECG strips​   + 6=Chest X-ray​   + 7=Photographs​   + 8=CIOMS​   + 9=SAE Report​   + 10=Email​   + 11=Pregnancy Report​   + 12=QC Report ​   + 13=Other​ |
| Included Documents | 첨부 문서 | 옵션 | C.1.6.1.r.2 |  | * 허용 파일 양식: Application/PDF, image/jpeg, application/DICOM, text/plain Representation: e.g.B64 Compression: e.g.DF​ * 파일명으로 표시 |
|  | First Sender of This Case | 최초 보고자 규제당국 여부 | 필수 | C.1.8.2 |  |  |
|  | Other Case Identifiers in Previous Transmissions | 이전 전송에서의 기타 보고자관리번호 유무 | 옵션 | C.1.9.1 |  | * 행을 하나라도 생성하여 입력한 경우에는 XML에서 필드에 True를 입력 (아래 C.1.9.1.r.1 & C.1.9.1.r.2에 대해 r>=1이면 True)​ * 하나도 입력하지 않은 경우에는 NI 자동으로 입력​ * True 선택 시 C.1.9.1.r.1, C.1.9.1.r.2가 활성화 |
| 묶어서 한 행으로 표시. +버튼으로 추가 | Source(s) of the Case Identifier | 자료원 | 옵션 | C.1.9.1.r.1 |  | C.1.9.r.1과 C.1.9.1.r.2묶어서 +버튼으로 행 추가 가능 |
| Case Identifier(s) | 보고자관리번호 | 옵션 | C.1.9.1.r.2 |  | C.1.9.r.1과 C.1.9.1.r.2묶어서 +버튼으로 행 추가 가능   * 처리: 파트너사 재보고시 (Import, AI Convert[고도화 예정]를 통해 생성) 해당 파일의 C.1.1에 입력된 정보를 C.1.9.1.r.2로 추가 (r+1) 입력​ |
|  | eport FU No from the previous sender | 이전 전송에서의 추적보고 연번​ | 옵션 | 자체 필드 |  | * Reconciliation Module에서 검증 시 사용 (Light ver 범위 제외)​ * 고도화 때 예정 |
|  | Type of the Report Link 참조 보고 유형 | 참조 보고 유형 | 옵션 | 자체 필드 |  | * Option 값:​    + 1=mother/parent-child pair where both had events/reactions,.   + 2=siblings with common exposure.   + 3=several reports involving the same patient.   + 4=an ICSR previously sent via paper without a conformant E2B Worldwide Unique Case​ Identification Number.   + 5=several similar reports from same reporter (cluster).​   + 6=other​ |
| Identification Number of the Report Which Is Linked to This Report | 참조보고의 보고자관리번호 | 옵션 | C.1.10.r |  | * 추가 검증 룰: ​    + 조건부 필수 (셀타)​   + ‘Type of the Report Link 참조 보고 유형’ 필드를 선택한 경우에는 필수 입력​ |

## 2.2 제안 구조

> 원문에 정의 없음

# 3. 기능 설명

---

> 원문에 정의 없음 (필드별 동작은 2.1 상세 필드 명세의 비고 및 4. 정책을 참조)

# 4. 정책

---

## 4.1 Case ID, 보고자 관리번호, 고유식별 보고자관리번호 정의 — 필드 구성 정의

| 필드명 | 데이터 구성 요소 |
| --- | --- |
| Case ID | * [국가코드], [조직 식별자]를 제외한 순수 넘버 |
| 보고자 관리번호 (C.1.1) | * [국가코드] + [조직 식별자] + [리포트 넘버] 전체 포함 |
| 고유식별 보고자관리번호 (C.1.8.1) | * 자발보고(Manual Intake): C.1.1과 동일하게 생성<br>- Import: 원본 파일에 기재된 C.1.8.1 값 |

## 4.2 사례의 식별자 (Primary Key)

### 4.2.1 자발보고 (Manual Intake)

* 식별자: [국가코드], [조직 식별자]를 제외한 번호 (Case ID와 동일)
* 로직:

  + 시스템 정책에 따라 생성된 번호가 사례의 정체성을 결정
  + 이 번호가 사례 묶음의 절대적인 기준이 됨
  + C.1.1과 C.1.8.1은 이 식별자를 기반으로 [국가코드]와 [조직 식별자]가 포함된 필드 데이터로 존재

### 4.2.2 인입 데이터 (Import — 파일 내 C.1.8.1 존재 시)

* 식별자: 고유식별 보고자관리번호 (C.1.8.1)
* 로직:

  + 파일 내에 이미 존재하는 C.1.8.1이 곧 고유 식별 번호
  + 이 번호가 사례 묶음의 절대적인 기준이 되며, 인입 즉시 확정되어 수정 불가

## 4.3 핵심 제어 및 정합성 룰

식별자의 일관성을 유지하기 위해 시스템적으로 강제되는 철칙.

### 4.3.1 수동 수정 및 중복 차단

* 수정 불가: Case ID, C.1.1, C.1.8.1 필드 모두 사용자가 수동으로 타이핑하여 수정 불가

## 4.4 보고자관리번호(C.1.1)와 고유식별 보고자관리번호(C.1.8.1) 정책

### **자발보고의 경우**

* C.1.1과 C.1.8.1이 동일한 정책으로 관리된다.

### **Import의 경우**

* C.1.1이 해당 정책으로 관리.
* C.1.8.1은 원본 파일에서 채번, 고정값으로 수정되지 않음.

| 단계 | 처리 및 확정 로직 | 비고 |
| --- | --- | --- |
| Initial (Entry ~ Approval) | 국가 코드 및 조직 식별자, Report Number를 기준으로 실시간 Preview 반영. |  |
| Approved | 해당 시점의 최신 정보를 기준으로 값 확정. | 확정 이후 고정 |
| 승인 취소 | 승인 취소 시 정보 수정에 따라 식별자 변경 가능. | 파트너사 통지 후 취소/변경에 따른 책임은 사용자에게 있음. |
| Follow-up | * 최초 보고(Initial)에서 확정된 값을 그대로 계승 * 묶인 케이스 중 하나라도 Approved 상태가 있을 경우, 해당 값으로 고정하여 모든 케이스가 동일하게 적용. * Approved 이전 상태인 경우 FU 그룹의 예상값을 공유하여 표시. | FU 묶음에서 동기화되어 적용 |

## 4.5 인지일 선후 관계 검증

* **Rule**: C.1.4이 C.1.5보다 앞설 경우
* 사용자가 C.1.5를 C.1.4보다 이전 날짜로 입력할 경우, 저장을 차단하고 "최초 인지일은 가장 최근 인지일보다 늦을 수 없습니다"라는 에러 메시지를 노출함.

# 5. 요구사항

---

> 원문에 정의 없음

# 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
