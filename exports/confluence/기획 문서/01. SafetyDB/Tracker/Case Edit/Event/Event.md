|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.28 |  | v1.0 | v1.0.260428 |
| 김나정 | 26.03.23 | 최초 작성 | v1.0 | v1.0.260323 |

## 1. 개요

---

* **목적**: Case Edit 화면 중 '약물이상반응/이상사례(Event)' 섹션(ICH E2B R3 E.i)의 필드 구성, 중대성(Seriousness) 기준, MedDRA 코딩 및 교차 섹션 연동 로직을 정의.
* **페이지 위치**: Safety > Tracker > Case Edit > Event

**핵심 설계 방향**:

* **Seriousness Criteria**: 6개 중대성 항목(E.i.3.2a~f)은 모두 필수이며, 미선택 시 NI 자동 입력.

* **Intake 데이터 연동**: Seriousness 정보가 Manual Intake에서 입력된 경우 자동 입력. NA 선택 시 모든 항목 체크 해제.
* **교차 섹션 연동**: Reporter 자격(C.2.r.4) → E.i.8 활성화, Seriousness Death(E.i.3.2a) → Death 섹션(D.9), Outcome Fatal(E.i.7=5) → Death 섹션.

# 2. 출력 정보

---

## 2.1 Reported Term (보고 용어) — E.i 반복 그룹

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Reaction / Event as Reported by the Primary Source for Translation | 원보고자가 보고한 약물이상반응/이상사례 | 옵션 | E.i.1.2 |  | 입력   * Intake & Triage 에서 입력한 Reported Term에 대해 각각 탭으로 생성하고 해당 필드에 입력한다 |
|  | Reaction / Event as Reported by the Primary Source in Native Language | 원보고자가 보고한 약물이상반응/이상사례(현지 언어) | 옵션 | E.i.1.1a |  |  |
|  | Reaction / Event as Reported by the Primary Source Language | 원보고자의 현지언어 | 조건부 필수 | E.i.1.1b |  |  |
|  | MedDRA Version for Reaction / Event | 약물이상반응/이상사례 MedDRA 버전 | 필수 | E.i.2.1a |  | 입력   * MedDRA 팝업 & License Expire경우 자유기재 |
|  | Reaction / Event (MedDRA code) | 약물이상반응/이상사례 MedDRA 코드 | 필수 | E.i.2.1b |  | 입력   * MedDRA 팝업 & License Expire경우 자유기재 |
|  | Reaction / Event (MedDRA Term) | 약물이상반응/이상사례 MedDRA 용어​ | 필수 | 자체 필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: E.i.2.1b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하 | 입력   * MedDRA 팝업 & License Expire경우 자유기재​ |
|  | Term Highlighted by the Reporter | 원보고자가 강조한 용어 | 옵션 | E.i.3.1 |  | * 옵션 값: 영문 병기    + 1=Yes, highlighted by the reporter, NOT serious​   + 2=No, not highlighted by the reporter, NOT serious​   + 3=Yes, highlighted by the reporter, SERIOUS​   + 4=No, not highlighted by the reporter, SERIOUS |
|  | special Situation | 특별 상황​ | 옵션 | 자체 필드 |  | * Option 값:​    + 1=Lack of efficacy​   + 2=Medication errors or Potential medication errors​   + 3=Overdose​   + 4=Misuse​   + 5=Abuse​   + 6=Counterfeit​   + 7=Reports from Lawsuits​   + 8=Off-label use​   + 9=Drug Addiction and withdrawal syndrome​   + 10=Unexpected beneficial effect​   + 11=Drug Interactions​   + 12=Disease Progression related to the use of the product​   + 13=Suspected transmission of infectious agents via a medicinal product (STIAMP)​   + 14=Occupation exposure​   + 15=Pregnancy ​   + 16= Breast feeding​   + 17=Other |
|  | Results in Death | 사망 | 필수 | E.i.3.2a |  | 처리   * Checkbox 선택 안 한 경우 XML필드에 자동 NI 입력 |
|  | Life Threatening | 생명의 위협 | 필수 | E.i.3.2b |  | 처리   * Checkbox 선택 안 한 경우 XML필드에 자동 NI 입력 * 디자인: Null Flavor에서 NI값밖에 없으므로 True/NI 둘 중 하나 선택 |
| 묶음 | Caused / Prolonged Hospitalisation | 입원 또는 입원기간의 연장 | 필수 | E.i.3.2c |  | 처리   * 해당 항목을 선택하면 아래에 추가 입력 필드(입원 시작일, 입원 종료일)가 자동으로 확장되며, 항목 우측의 버튼을 클릭 시 추가 입력 필드를 축소 및 확장을 할 수 있다 * Checkbox 선택 안 한 경우 XML필드에 자동 NI 입력 * 디자인: Null Flavor에서 NI값밖에 없으므로 True/NI 둘 중 하나 선택 |
| Hospitalization Start | 입원 시작일​ | 옵션 | 자체 필드 |  | 입력   * 입원 또는 입원 기간의 연장이 입력된 경우 활성화​ * 입원 종료일 보다 미래 날짜 입력 불가​ * 최소 일 (Day)까지 입력 |
| Hospitalization End | 입원 종료일​ | 옵션 | 자체 필드 |  | 입력   * 입원 또는 입원 기간의 연장이 입력된 경우 활성화​ * 입원 시작일 보다 보다 과거 날짜 입력 불가​ * 최소 일 (Day)까지 입력 |
|  | Disabling / Incapacitating | 중대한 불구나 기능저하 | 필수 | E.i.3.2d |  | 처리   * Checkbox 선택 안 한 경우 XML필드에 자동 NI 입력 * 디자인: Null Flavor에서 NI값밖에 없으므로 True/NI 둘 중 하나 선택 |
|  | Congenital Anomaly / Birth Defect | 선천적 기형 초래 | 필수 | E.i.3.2e |  | 처리   * Checkbox 선택 안 한 경우 XML필드에 자동 NI 입력 * 디자인: Null Flavor에서 NI값밖에 없으므로 True/NI 둘 중 하나 선택 |
| 묶음 | Other Medically Important Condition | 기타 의학적으로 중요한 상황​ | 필수 | E.i.3.2f |  | 처리   * 해당 항목을 선택하면 아래에 추가 입력 필드(기타 의학적으로 중요한 상황 설명)이 자동으로 확장되며, 항목 우측의 버튼을 클릭 시 추가 입력 필드를 축소 및 확장을 할 수 있다. ​ * Checkbox 선택 안 한 경우 XML필드에 자동 NI 입력 * 디자인: Null Flavor에서 NI값밖에 없으므로 True/NI 둘 중 하나 선택 |
| Other Medically Important Condition Additioanl Info | 기타 의학적으로 중요한 상황 설명​ | 옵션 | 자체 필드 |  | 입력   * 자유기재, 500자 이하​ * 기타 의학적으로 중요한 상황이 입력된 경우 활성화 |
|  | Severity | 중증도​ | 옵션 | 자체 필드 |  | * Option 값:​    + 1=Severe​   + 2=Moderate​   + 3=Mild​   + 4=Unknown |
|  | CTCAE | CTCAE | 옵션 | 자체 필드 |  | * Option 값: ​    + 1=Grade 1​   + 2= Grade 2​   + 3= Grade 3​   + 4= Grade 4​   + 5= Grade 5​   + 6= UNK |
|  | Date of Start of Reaction / Event | 발현일 | 조건부 필수 | E.i.4 |  | MFDS: 임상시험국내와 치료목적 사용승인의 경우 필수값 |
|  | Date of End of Reaction / Event | 종료일 | 조건부 필수 | E.i.5 |  | MFDS: 임상시험국내와 치료목적 사용승인의 경우 필수값 |
|  | Duration of Reaction / Event (number) | 지속 기간 | 조건부 필수 | E.i.6a |  |  |
|  | Duration of Reaction / Event (unit) | 지속 기간(단위) | 조건부 필수 | E.i.6b |  | 제한된 UCUM 코드   * Option 값: ​    + 10.a=연대​   + a=연​   + mo=월​   + wk=주​   + d=일​   + h=시간​   + min=분​   + s=초 |
|  | Outcome of Reaction / Event at the Time of Last Observation | 최종 관찰 결과 | 필수 | E.i.7 |  | * Option 값:​ 영어 병기    + 1=recovered/resolved ​   + 2=recovering/resolving ​   + 3=not recovered/not resolved/ongoing   + 4=recovered/resolved with sequelae ​   + 5=fatal ​   + 0=unknown |
|  | Medical Confirmation by Healthcare Professional | 의료전문가 확인 여부 | 옵션 | E.i.8 | C.2.r.4 Qualification 원보고자의 자격 에서 4=Lawyer 또는 5=Consumer or other non health professional를 선택한 경우에만 활성화(의약전문가가 직접 보고하는 경우에는 이 항목을 입력하지 않는다.)​ | * Option 값: ​영어 병기    + True​   + False |
|  | Identification of the Country Where the Reaction / Event Occurred | \발현당시 환자가 있던 국가 | 옵션 | E.i.9 |  |  |

## 2.2 제안 구조

```
Event (약물이상반응/이상사례) [E.i] ── 반복 그룹 (Intake 탭 단위)
│
├── Reported Term
│   ├── Reaction/Event for Translation [E.i.1.2] ── Intake 연동
│   ├── Reaction/Event in Native Language [E.i.1.1a]
│   └── Native Language [E.i.1.1b]
│
├── MedDRA Coding
│   ├── MedDRA Version [E.i.2.1a]
│   ├── MedDRA Code [E.i.2.1b]
│   └── MedDRA Term (자체 필드)
│
├── Reporter Highlight & Special Situation
│   ├── Term Highlighted by Reporter [E.i.3.1]
│   └── Special Situation (자체 필드)
│
├── Seriousness Criteria [E.i.3.2] ── 공통: 미선택 시 NI 자동 입력
│   ├── Results in Death [E.i.3.2a]
│   ├── Life Threatening [E.i.3.2b]
│   ├── Caused/Prolonged Hospitalisation [E.i.3.2c] ── 묶음
│   │   ├── Hospitalization Start (자체 필드)
│   │   └── Hospitalization End (자체 필드)
│   ├── Disabling/Incapacitating [E.i.3.2d]
│   ├── Congenital Anomaly/Birth Defect [E.i.3.2e]
│   └── Other Medically Important Condition [E.i.3.2f] ── 묶음
│       └── Additional Info (자체 필드, 500자)
│
├── Severity & Grading
│   ├── Severity (자체 필드)
│   └── CTCAE (자체 필드)
│
├── Reaction/Event Timeline
│   ├── Date of Start [E.i.4]
│   ├── Date of End [E.i.5]
│   ├── Duration (number) [E.i.6a]
│   └── Duration (unit) [E.i.6b]
│
└── Outcome & Confirmation
    ├── Outcome [E.i.7]
    ├── Medical Confirmation [E.i.8] ── C.2.r.4=4 or 5일 때만 활성화
    └── Country [E.i.9]
```

# 3. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | 탭 기반 다중 Event | Event 여러개일 때 Tab으로 구분하여 생성 | Tab을 +버튼으로 추가 |
| 2 | Seriousness Checkbox + NI 자동 | 6개 Seriousness 항목 미선택 시 XML에 NI 자동 입력 | 저장 |
| 3 | Seriousness Intake 연동 | Manual Intake에서 Seriousness 입력 시 자동 입력. | 자동 |
| 4 | 입원 정보 확장/축소 | E.i.3.2c 선택 시 입원 시작일/종료일/Ongoing 필드 확장. | E.i.3.2c 체크 시 |
| 5 | Other Med Important 확장/축소 | E.i.3.2f 선택 시 추가 설명 필드 확장 | E.i.3.2f 체크 시 |
| 6 | C.2.r.4 → E.i.8 동적 제어 | Reporter 자격이 4(Lawyer) 또는 5(Consumer) 시 E.i.8 활성화 | C.2.r.4 변경 시 (교차 섹션) |
| 7 | Completion Check: Death | E.i.3.2a=True 시 D.9 Death 섹션 입력 필요 | Completion Check 실행 시 |

# 4. 정책

---

## 4.1 MedDRA 팝업 & License Expire 공통 규칙

MedDRA 코드/용어를 사용하는 필드(E.i.2.1a/b 및 자체필드 Term)에 적용:

| 조건 | 동작 |
| --- | --- |
| MedDRA License 유효 | MedDRA 팝업을 통해 코드·버전·용어 입력 |
| MedDRA License Expire | Free text(자유기재)로 전환. Term 필드는 비필수, 250자 이하 검증 |

## 4.2 Seriousness Criteria 공통 처리 (E.i.3.2a~f)

| 조건 | 동작 |
| --- | --- |
| 체크박스 선택 | XML 필드에 True 입력 |
| 체크박스 미선택 | XML 필드에 자동으로 NI(No Information) 입력 |

> 디자인 참고: Null Flavor에서 NI 값만 존재하므로 True/NI 둘 중 하나 선택 방식.

## 4.3 묶음 확장/축소 — Hospitalisation(E.i.3.2c)

| 조건 | 동작 |
| --- | --- |
| E.i.3.2c 선택 | Hospitalization Start, Hospitalization End 필드 자동 확장(활성화) |
| E.i.3.2c 미선택 | 하위 필드 비활성화 |

추가 검증:

* Hospitalization Start ≤ Hospitalization End (역전 불가)
* 최소 일(Day) 단위까지 입력 필수

## 4.4 묶음 확장/축소 — Other Medically Important(E.i.3.2f)

| 조건 | 동작 |
| --- | --- |
| E.i.3.2f 선택 | Additional Info 필드 자동 확장(활성화), 자유기재 500자 이하 |
| E.i.3.2f 미선택 | 하위 필드 비활성화 |

## 4.5 교차 참조 — Medical Confirmation(E.i.8) ↔ Reporter Qualification(C.2.r.4)

| 조건 | 동작 |
| --- | --- |
| C.2.r.4 = 4 (Lawyer) 또는 5 (Consumer or other non health professional) | E.i.8 활성화 |
| C.2.r.4 = 1, 2, 3 (의약전문가) | E.i.8 비활성화 (의약전문가가 직접 보고하는 경우 입력 불요) |

## 4.6 MFDS 조건부 필수 — 발현일/종료일

| 조건 | 동작 |
| --- | --- |
| 보고 유형이 임상시험국내 또는 치료목적 사용승인 | E.i.4(발현일), E.i.5(종료일) 필수 |

## 4.7 Intake 연동 — Reported Term 탭 생성

| 조건 | 동작 |
| --- | --- |
| Intake & Triage에서 Reported Term 입력 | 각 Term에 대해 탭 생성, E.i.1.2 필드에 자동 입력 |

# 5. 요구사항

---

> 원문에 정의 없음

# 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
