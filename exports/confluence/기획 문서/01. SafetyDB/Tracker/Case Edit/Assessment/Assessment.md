|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김용성 | 26.04.27 | 비고 및 추가 기획 | v1.0 | v1.0.260428 |
| 김나정 | 26.04.08 | 최초 작성 | v1.0 | v1.0.260408 |

# 1. 개요

---

* **목적**: Case Edit 화면 중 '인과성 평가(Assessment)' 섹션(ICH E2B R3 G.k.9.i)의 필드 구성, 자동 계산 로직, 평가 방법별 결과 분기, 예측가능성 판정을 정의.
* **페이지 위치**: Safety > Tracker > Case Edit > Assessment

**핵심 설계 방향**:

* **Drug-Event 매트릭스**: k(의약품) × i(이상반응) 조합별로 자동 생성. 사용자가 평가 대상을 선택하여 개별 평가 입력.
* **시간 간격 자동 계산**: 투여 시작일/종료일과 이상반응 발현일의 차이를 자동 계산.
* **평가 방법별 결과 분기**: Method of Assessment 선택 값에 따라 Result of Assessment 옵션이 동적으로 변경.
* **MFDS 자동 입력**: 보고 유형(임상/시판후) 및 원보고자 국가에 따라 MFDS 평가 방법이 자동 결정.

## 2. 출력 정보

---

### 2.1 Assessed Reaction (평가 대상 선택) — G.k.9.i

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Reaction(s) / Event(s) Assessed | 평가 대상 | 옵션 | G.k.9.i.1 | 1. E.i의 약물이상반응/이상사례 ID 입력된 값인지 검증 | * 입력    + 자동 생성 필드 (사용자 직접 입력 불가)      - k=의약품 개수     - i=이상반응 개수   + 각 의약품마다 E.i.2.1b의 MedDRA 코드에 입력된 모든 코드(증상)에 대해 각 코드마다 하나의 Option으로 자동 생성되어서 사용자가 이 중에서 골라서 평가를 생성해서 입력이 가능하도록 함. |
| 연관 | Time Interval between Beginning of Drug Administration and Start of Reaction / Event (number) | 투여 후 발현까지의 시간 간격 | 조건부 필수 | G.k.9.i.3.1a |  | * 자동 계산    + 조건1. G.k.4.r.4 (투여 시작일) 항목, E.i.4 (이상반응 발현일) 항목이 최소 CCYYMMDD 수준이고, 동일한 수준으로 모두 입력완료​   + 계산: E.i.4 - G.k.4.r.4 (Minimum 입력된 날짜 단위 기준으로 계산되어야 한다.)​ |
| Time Interval between Beginning of Drug Administration and Start of Reaction / Event (unit) | 투여 후 발현까지의 시간 간격(단위) | 조건부 필수 | G.k.9.i.3.1b |  | * 입력    + Option 값: ​      - 10.a=연대​     - a=연​     - mo=월​     - wk=주​     - d=일​     - h=시간​     - min=분​     - s=초​ |
| 연관 | Time Interval between Last Dose of Drug and Start of Reaction / Event (number) | Time Interval between Last Dose of Drug and Start of Reaction / Event (number) | 조건부 필수 | G.k.9.i.3.2a |  | * 자동 계산    + 조건: G.k.4.r.5 (투여 종료일) 항목, E.i.4 (이상반응 발현일) 항목이 CCYYMMDD 수준, 동일하게 모두 입력완료​   + 계산: E.i.4 - G.k.4.r.5 (Minimum 입력된 날짜 단위 기준으로 계산되어야 한다.)​ |
| Time Interval between Last Dose of Drug and Start of Reaction / Event (unit) | 최종 투여 후 발현까지의 시간 간격(단위) | 조건부 필수 | G.k.9.i.3.2b |  | * 입력    + Option 값      - 10.a=연대     - a=연     - mo=월     - wk=주     - d=일     - h=시간     - min=분     - s=초 |
|  | Did Reaction Recur on Re-administration? | 재투여 및 재발현 여부 | 옵션 | G.k.9.i.4 |  | * 입력    + Option 값: 한글 영어 병기      - 1=yes - yes (rechallenge was done, reaction reccurred)     - 2=yes - no (rechallenge was done, reaction did not recur)     - 3=yes - unk (rechallenge was done, outcome unknown)     - 4=no - n/a (no rechallenge was done, recurrance is not applicable) |
|  | Result of Assessment | 평가 결과 | 옵션 | G.k.9.i.2.r.3 |  | * 입력    + Free text * Manual Intake에서 입력한 값 가져오기 |
| 관련 | KRCT Result of Assessment | KRCT 평가 결과 | 조건부 필수 | G.k.9.i.2.r.3.KR.2 |  | * 입력    + Option 값: 영어 병기      - 1=Related     - 2=Not related * Manual Intake에서 입력한 값 가져오기 * 관련성 있음/관련성 없음 옵션 중 ‘관련성 있음’ 선택 시 인과성 여부 필드의 ‘Related’에 매핑, ‘관련성 없음’ 선택 시 ‘Not Related’에 매핑 |
| WHO-UMC Result of Assessment | WHO-UMC 평가 결과 | 옵션 | G.k.9.i.2.r.3.KR.1 |  | * 입력    + Option 값: 영어 병기      - 1=Certain ​     - 2=Probable​     - 3=Possible ​     - 4=Unlikely​     - 5=Conditional/unclassified​     - 6=Unassessable/unclassifiable * Manual Intake에서 입력한 값 가져오기 * 확실함(Certain) 상당히확실함(Probable) 가능함(Possible) 가능성적음(Unlikely) 평가곤란(Conditional/unclassified) 평가불가(Unassessable/unclassifiable)의 선택지 중 가능성 적음 선택 시 ‘인과성 여부' 필드의 ‘Not Related’에 매핑, 그 외 선택 시 'Related’에 매핑 |
| Reporting Criteria | 인과성 여부 | 필수 | 자체 필드 |  | * 옵션:    + Related/Unknown   + Not Related * Manual Intake에서 입력한 값 가져오기 * 관련성 있음/관련성 없음 옵션 중 ‘관련성 있음’ 선택 시 인과성 여부 필드의 ‘Related’에 매핑, ‘관련성 없음’ 선택 시 ‘Not Related’에 매핑 |
|  | Source of Assessment | 평가 정보원 | 옵션 | G.k.9.i.2.r.1 | 1. 입력값이 60자 이하인지 검증​ | * 입력    + 기본 제공 Option 값:      - Investigator     - Sponsor     - NCA     - MAH     - Health Care professional     - Non-Health Care professional     - Free text   + Creative Dropdown으로 추가 옵션 기재 가능 |
|  | Method of Assessment | 평가 방법 | 옵션 | G.k.9.i.2.r.2 | 1. 입력값이 60자 이하인지 검증​ | * 입력    + 원래 자유기재 필드이나 Selta에서 dropdown으 값 제공   + Option 값:      - 1=Global introspection (Expert judgement)     - 2=Algorithm Method     - 3= WHO-UMC     - 4=Naranjo     - 5=Jones     - 6=Begaud (French method)     - 7=Kramer (Yale)     - 8=Adverse Drug Reaction Advisory committee     - 9=Liverpool     - 10=Koh     - 11=Hsu     - 12=Drug interaction probability scale     - 13=Probabilistic Method (logistic method)     - 14=Bayesian (BARDI)     - 15= Other: free text |
|  | MFDS Method of Assessment | 평가 방법 | 옵션 | G.k.9.i.2.r.2.KR.1 | * 비필수로 입력값이 있는 경우 검증    + 1) 임상시험(CT)의 경우 (C.1.3에서 Value=2 이면서, C.5.4에서 Value=1 인 경우) "2"만 허용   + 2) 치료목적사용(CU)의 경우 (C.1.3에서 Value=2 이면서, C.5.4에서 Value=2 인 경우) "2"만 허용   + 3) N.2.r.3 항목값이 국내(KR)의 경우 "1"만 허용   + 4) N.2.r.3 항목값이 국외(FR)의 경우 입력 허용하지 않음   + 5) N.2.r.3 항목값이 임상시험국외(CF)의 경우 입력 허용하지 않음​ * 임상시험과 치료목적 사용승인의 경우 필수값으로 검증 | * 입력    + Option 값: ​      - 1=WHO-UMC​     - 2=KRCT   + 우선순위      1. 원보고자의 국가코드가 KR이 아닌 경우 ▶ 해당 필드 비활성 & 입력 불가​     2. C.1.3에서 Value=2 이면서, C.5.4에서 Value=1 또는 2 인 경우 ▶ 해당 필드 값 2로 자동 입력​     3. 나머지 경우 ▶ 해당 필드 값 1로 자동 입력 |
|  | Event Expectedness | 예측가능성 | 조건부 필수 | 자체 필드 | 1. 조건부필수​ 2. C.5.4에 1 또는 2가 입력된 경우에는 필수​ | * Option 값: ​    + 1=Expected​   + 2=Unexpected​ * 자동화:    + Configuration> Master>Product에서 RSI값이 있다면 비교해서 자동 입력​ * 처리:    + Drug Tab 중 Characterization of Drug이 Suspect이거나 interacting인 Tab 모두에 값이 하나도 없는 경우 (예. Intake & Triage만 입력된 상태)이거나 Tab 중 하나라도 Drug-Event가 Unexpected이면 보고서 전체를 Unexpected로 처리하며 AE Type 분류 |
|  | Reference Safety Information​ | 미정 | 옵션 | 자체 필드 | 1. 비필수로 입력값이 있는 경우 검증 | * 입력    + Option 값: ​      - 1= Investigational Brochure​     - 2= Product leaflet​     - 3= Package Insert ​     - 4= SmPC |

### 2.8 제안 구조

```
Assessment (Drug-Event 평가) [G.k.9.i]
│
├── Assessed Reaction
│   └── Reaction(s)/Event(s) Assessed [G.k.9.i.1] ── 자동 생성 (E.i.2.1b 연동)
│
├── Time Interval ── 자동 계산 (Read-Only)
│   ├── Start→Onset (number) [G.k.9.i.3.1a] ─┐ 연관
│   ├── Start→Onset (unit) [G.k.9.i.3.1b]    ─┘
│   ├── LastDose→Onset (number) [G.k.9.i.3.2a] ─┐ 연관
│   └── LastDose→Onset (unit) [G.k.9.i.3.2b]    ─┘
│
├── Rechallenge
│   └── Did Reaction Recur on Re-administration? [G.k.9.i.4]
│
├── Causality Assessment [G.k.9.i.2.r] ── 반복 그룹
│   ├── Source of Assessment [G.k.9.i.2.r.1]
│   ├── Method of Assessment [G.k.9.i.2.r.2]
│   └── Result of Assessment [G.k.9.i.2.r.3] ── Manual Intake 연동
│
├── WHO-UMC & Reporting Criteria
│   ├── WHO-UMC Result [G.k.9.i.2.r.3.KR.1] ── Unlikely→Not Related, 나머지→Related
│   ├── Result of Assessment [G.k.9.i.2.r.3] ── Manual Intake 연동
│   └── Reporting Criteria (자체 필드) ── 필수, Manual Intake 연동
│
├── MFDS Assessment
│   ├── MFDS Method [G.k.9.i.2.r.2.KR.1] ── 자동 입력/비활성 로직
│   └── KRCT Result [G.k.9.i.2.r.3.KR.2]
│
└── Expectedness & RSI
    ├── Event Expectedness (자체 필드) ── RSI 자동 비교
    └── Reference Safety Information (자체 필드)
```

## 3. 기능 설명

---

> 원문에 정의 없음

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | Drug-Event 매트릭스 자동 생성 | E.i.2.1b MedDRA 코드별로 평가 Option 자동 생성 | 자동 |
| 2 | 시간 간격 자동 계산 | G.k.4.r.4/G.k.4.r.5와 E.i.4 간 차이를 CCYYMMDD 수준에서 자동 계산 | 자동 |
| 3 | MFDS 평가 방법 자동 입력 | 원보고자 국가, 보고 유형에 따라 KR.1 값 자동 결정 | 자동 |
| 4 | RSI 기반 Expectedness 자동 입력 | Configuration > Master > Product의 RSI 정보와 비교하여 Expected/Unexpected 자동 판정 | 자동 |
| 5 | Unexpected 처리 | Drug Tab 중 Suspect/Interacting인 Tab에서 하나라도 Unexpected이면 보고서 전체를 Unexpected로 분류 | AE Type 분류 시 |
| 6 | Intake Causality 연동 | Intake에서 Reported Causality 입력 시 Assessment 1행 자동 생성 (Source=Qualification, Method=Global introspection, Causality=Intake 값) | 자동 |

## 4. 정책

---

### 4.1 Time Interval 자동 계산 규칙

| 필드 | 계산식 | 조건 |
| --- | --- | --- |
| G.k.9.i.3.1a (투여 시작→발현) | E.i.4 − G.k.4.r.4 | 양쪽 모두 최소 CCYYMMDD 수준, 동일 수준 입력 완료 |
| G.k.9.i.3.2a (최종 투여→발현) | E.i.4 − G.k.4.r.5 | 양쪽 모두 CCYYMMDD 수준, 동일하게 입력 완료 |

> Minimum 입력 날짜 단위 기준으로 계산.

### 4.2 MFDS Method of Assessment 자동 입력 및 비활성 로직

**우선순위 적용 순서:**

| 순서 | 조건 | 동작 |
| --- | --- | --- |
| 1 | 원보고자 국가코드 ≠ KR | 비활성, 입력 불가 |
| 2 | C.1.3=2 AND (C.5.4=1 또는 C.5.4=2) | 값 "2" (KRCT) 자동 입력 |
| 3 | 나머지 경우 | 값 "1" (WHO-UMC) 자동 입력 |

**검증룰 (입력값이 있는 경우):**

| 조건 | 허용 값 |
| --- | --- |
| CT: C.1.3=2, C.5.4=1 | "2" (KRCT)만 허용 |
| CU: C.1.3=2, C.5.4=2 | "2" (KRCT)만 허용 |
| N.2.r.3=KR (국내) | "1" (WHO-UMC)만 허용 |
| N.2.r.3=FR (국외) | 입력 불가 |
| N.2.r.3=CF (임상시험국외) | 입력 불가 |

### 4.3 WHO-UMC Result → Reporting Criteria 자동 매핑

| WHO-UMC 선택 값 | Reporting Criteria 매핑 |
| --- | --- |
| 4=Unlikely (가능성 적음) | Not Related |
| 1=Certain, 2=Probable, 3=Possible, 5=Conditional/unclassified, 6=Unassessable/unclassifiable | Related |

### 4.4 Reporting Criteria 직접 입력 매핑

| 선택 값 | 매핑 |
| --- | --- |
| 관련성 있음 | Related/Unknown |
| 관련성 없음 | Not Related |

> Manual Intake에서 입력한 값 가져오기.

### 4.5 Event Expectedness 조건부 필수 및 자동화

| 조건 | 동작 |
| --- | --- |
| C.5.4=1 또는 C.5.4=2 | Event Expectedness 필수 |
| Configuration > Master > Product에 RSI 값 존재 | RSI 비교하여 자동 입력 |
| Drug Tab 중 Suspect/Interacting Tab 모두 값 없음 또는 하나라도 Unexpected | 보고서 전체를 Unexpected로 처리, AE Type 분류 |

### 4.6 평가 대상 자동 생성 규칙

| 조건 | 동작 |
| --- | --- |
| 의약품별 E.i.2.1b MedDRA 코드 입력됨 | 각 코드마다 하나의 Option으로 자동 생성 → 사용자가 선택하여 평가 생성 |

### 4.7 Manual Intake 연동 필드

| 대상 필드 | 연동 동작 |
| --- | --- |
| Result of Assessment (G.k.9.i.2.r.3) | Manual Intake에서 입력한 값 가져오기 |
| WHO-UMC Result (G.k.9.i.2.r.3.KR.1) | Manual Intake에서 입력한 값 가져오기 |
| Reporting Criteria (자체 필드) | Manual Intake에서 입력한 값 가져오기 |

## 5. 요구사항

---

> 원문에 정의 없음

## 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
