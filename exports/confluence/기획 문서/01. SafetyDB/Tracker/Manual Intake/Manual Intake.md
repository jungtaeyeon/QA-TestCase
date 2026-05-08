|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획서 버전 |
| 김나정 | 26.04.28 | Case ID Config 설정 안되어있을 경우 안내창 표시 기획 추가 | v1.0 | v1.0.260428 |
| 김나정 | 26.04.23 | 5. 제안 구조 수정 (기획 변경x) | v1.0 | v1.0.260423 |
| 김나정 | 26.04.10 | 최초 작성 | v1.0 | v1.0.260410 |

# 1. 개요

---

* **목적**: 자동 처리가 불가능한 이상사례에 대해 사용자가 수동으로 최초 사례(Initial Case)를 생성하는 경로를 제공한다. 유효한 ICSR의 4대 요소(보고자·환자·약물·이상사례)를 즉시 확인하고, 수동 입력 단계에서 중대성과 인과성을 판단하여 신속보고(Expedited) 대상을 빠르게 식별한다. 스마트 인터페이스를 통해 입력 오류를 최소화하고 공수를 절감한다.
* **페이지 위치**: Safety > Tracker > Manual Intake
* **핵심 가치**

  + **유효성 검증**: 4대 요소 충족 여부를 입력 즉시 확인
  + **신속 분류**: 입력 시점에 중대성·인과성을 판정하여 Expedited 여부 조기 식별
  + **지능형 입력**: Product Master 연동 기반 부분 일치 제안으로 입력 오류 최소화

# 2. 정책

---

## 2.1 필수/조건부 필수 필드 정책

Manual Intake 화면의 필드는 E2B(R3) 필수 항목과 비즈니스 필수 항목으로 구분하여 관리한다. 필수값이 미입력된 상태에서는 케이스 저장을 허용하지 않는다.

| 상태 | 필드 성격 | 시스템 동작 |
| --- | --- | --- |
| 필수 | 모든 케이스에서 반드시 입력 | 미입력 시 저장 차단, 해당 필드 하이라이트 |
| 조건부 필수 | 특정 조건 충족 시 필수로 전환 | 조건 미충족 시 비활성화, 충족 시 필수 표시 전환 |
| 선택 | 입력 불필요 | 저장 차단 없음 |

## 2.2 조건부 필드 활성화 규칙

보고 구분(C.1.3) 값에 따라 시험 정보 관련 필드의 활성화 여부가 결정된다.

| 보고 구분(C.1.3) 값 | 시험/연구 계획서 번호(C.5.3) | 임상시험대상자 식별번호(D.1.1.4) |
| --- | --- | --- |
| 2 (Report from study) | 활성화 및 필수 | 필수 |
| 1 / 3 / 4 외 값 | 비활성화 | 비활성화 |

## 2.3 의심의약품 이중화 데이터 관리 로직

Product Master에서 부분 정보만 선택된 경우, 공식 코딩 데이터와 식별용 메타데이터를 이중화하여 저장한다.

| 데이터 종류 | 저장 위치 | 활용처 |
| --- | --- | --- |
| 보고서 코딩 데이터 | ICSR 표준 필드 (성분 정보만 코딩) | 최종 생성 ICSR 보고서 및 케이스 출력물 |
| 내부 식별 메타데이터 | 별도 "식별용 메타데이터" 필드 (제형/용량) | 규제기관 보고 대상 분류(Reporting Triage) 로직의 비교 연산 |

## 2.4 제품 정보 조합별 매핑 규칙

사용자가 제공한 정보 완성도에 따라 시스템이 제안하는 매핑 방식이 달라진다.

### 2.4.1 Product Master 검색 키워드 매핑

검색창에 입력된 값은 Product Master의 계층별 필드와 매칭된다.

| 검색 키워드 | Product Master 검색 대상 필드 |
| --- | --- |
| 성분 | Family 계층의 "Product Family Name", "Active Pharmaceutical Ingredient" |
| 제품 | Products 계층 "Product Name" |
| 라이센스 | Licenses 계층의 “Trade Name” |

### 2.4.2 제품 검색 실시간 쿼리 조건

| 조건 | 동작 |
| --- | --- |
| 검색창 입력 길이 2자 미만 | 쿼리 미실행 |
| 검색창 입력 길이 2자 이상 | 실시간 쿼리 실행, 부분 일치 모든 Master 데이터 리스팅 |

## 2.5 중복 체크 정책

[중복 로직](https://selta.atlassian.net/wiki/spaces/IS/pages/31162383) 의 로직을 따름

## 2.6 케이스 생성 정책

* 신규 케이스로 생성할 경우 생성 시점에 Case ID 부여
* 케이스 생성 시점에 보고 출처 분류 > AE Type 분류 > 보고 기한 설정(RA due)의 로직을 시행함.

  + 해당 사항을 기준으로 Submission에 보고 리스트업
* 케이스 생성 시점 케이스 생성 사용자를 Owner로 지정
* 생성 완료 시 toast 알림창 표시

  + 알림창 내에 생성된 Case Edit 화면으로 바로가기 버튼 표시

## 2.7 필요 조건 적용 정책

### 2.7.1 Case ID Configuration을 진행하지 않은 경우

* Case ID Configuration에서 [조직자 이름]을 설정하지 않은 경우:

  + ‘Organisation Home에서 Case ID Configuration을 먼저 진행해주세요. Case ID 생성 규칙이 설정되지 않으면 케이스 생성이 불가합니다.’ 안내문구 팝업 표시.
  + 버튼은 ‘OK’하나.

# 3. 출력 정보

---

## 3.1 Manual Intake 상세 데이터 명세

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **카테고리** | **국문 필드명** | 영문 필드명 | **E2B(R3) 매핑** | **필수/조건부 상세 규칙** | 비고 |
| **보고 관리** | 보고 구분 | Type of Report | C.1.3 | [필수] |  |
|  | 시험/연구 계획서 번호 (승인받은 임상시험의 경우 임상시험 일련번호 기재 or 임상시험 계획번호 기재) | Sponsor Study Number | C.5.3 | [조건부 필수] C.1.3이 '2(Study)'인 경우 활성화 및 필수 | 임상 정보 불러오기는 release2에서 업데이트 예정 |
|  | 최초 발생인지일 | Date Report Was First Received from Source | C.1.4 | [필수] |  |
|  | 가장 최근의 발생인지일 (Day0) | Date of Most Recent Information for This Report | C.1.5 | [필수] |  |
| **환자 정보** | 이름(이니셜) | Patient (name or initials) | D.1 | [필수] |  |
|  | 임상시험대상자 식별번호 | Patient Medical Record Number(s) and Source(s) of the Record Number (Investigation Number) | D.1.1.4 | [조건부 필수] C.1.3이 '2(Study)'인 경우 필수 |  |
|  | 생년월일 | Date of Birth | D.2.1 | [선택] |  |
|  | 발현 당시 연령 | Age at Time of Onset of Reaction / Event (number) | D.2.2a | [선택] |  |
|  | 발현 당시 연령(단위) | Age at Time of Onset of Reaction / Event (unit) | D.2.2b | [선택] | D.2.2a와 묶음 |
|  | 성별 | Sex | D.5 | [선택] |  |
| **원보고자** | 원보고자의 국가코드 | Reporter’s Country Code | C.2.r.3 | [필수] |  |
|  | 원보고자의 자격 | Qualification | C.2.r.4 | [선택] |  |
| **이상사례** | 원보고자가 보고한 약물이상반응/이상사례 | Reaction / Event as Reported by the Primary Source for Translation | E.i.1.2 | [필수] |  |
|  | 약물이상반응/이상사례 MedDRA Term | Reaction / Event (MedDRA code) Term | E.i.2.1b | [필수] | * 용어(Term)로 화면 표시, 코드 입력하면 코드, 버전, 용어 데이터 전부 가지고 있음 * 팝업으로 MedDRA Term, Code 검색 가능 * 라이센스 만료 시 자유 입력으로 가능 |
| **의심의약품** | 원보고자가 보고한 의약품명 | Medicinal Product Name as Reported by the Primary Source | G.k.2.2 | [필수] |  |
|  | 의약품 코딩 정보 |  | Product Config | [필수] | Product Master 연동 매핑된 정보 (Family-Product Family Name/Products-Product Name/Licenses-Trade Name)이 매핑되었다는 정보 표시 |
| **중대성 평가** | 사망 | Results in Death | E.i.3.2a | [필수] | E.i.3.2a~f는 true 아니면 NI 둘 중 하나 선택하도록 UX/UI 부탁 |
|  | 생명의 위협 | Life Threatening | E.i.3.2b | [필수] |  |
|  | 입원 또는 입원기간의 연장 | Caused / Prolonged Hospitalisation | E.i.3.2c | [필수] |  |
|  | 입원 시작일​ | Hospitalization Start | 자체 필드 | [옵션] | 입원 또는 입원기간의 연장 필드와 연관 [Date/Tme]형식으로 입력 |
|  | 입원 종료일​ | Hospitalization End | 자체 필드 | [옵션] | 입원 또는 입원기간의 연장 필드와 연관 [Date/Tme]형식으로 입력 |
|  | 중대한 불구나 기능저하 | Disabling / Incapacitating | E.i.3.2d | [필수] |  |
|  | 선천적 기형 초래 | Congenital Anomaly / Birth Defect | E.i.3.2e | [필수] |  |
|  | 기타 의학적으로 중요한 상황 | Other Medically Important Condition | E.i.3.2f | [필수] |  |
|  | 기타 의학적으로 중요한 상황 설명 | Other Medically Important Condition Additioanl Info | 자체 필드 | [옵션] | 기타 의학적으로 중요한 상황 필드와 연관 |
| 인과성 | KRCT 평가 결과 | KRCT Result of Assessment | G.k.9.i.2.r.3.KR.2 | [선택] | * 국내외 임상/치료목적 사용승인 건 기록 * WHO-UMC 평가 결과(G.k.9.i.2.r.3.KR.1)필드에 입력 시 해당 필드 비활성화 * 관령성 있음/관련성 없음 옵션 중 ‘관련성 있음’ 선택 시 인과성 여부 필드의 ‘Related’에 매핑, ‘관련성 없음’ 선택 시 ‘Not Related’에 매핑 |
|  | WHO-UMC 평가 결과 | WHO-UMC Result of Assessment | G.k.9.i.2.r.3.KR.1 | [선택] | * 자발보고 및 시판 후 조사 건 기록 * KRCT 평가 결과(G.k.9.i.2.r.3.KR.2)필드에 입력 시 해당 필드 비활성화 * 확실함(Certain) 상당히확실함(Probable) 가능함(Possible) 가능성적음(Unlikely) 평가곤란(Conditional/unclassified) 평가불가(Unassessable/unclassifiable)의 선택지 중 가능성 적음 선택 시 ‘인과성 여부' 필드의 ‘Not Related’에 매핑, 그 외 선택 시 'Related’에 매핑 |
|  | 인과성 여부 | Reporting Criteria | 자체 필드 | [필수] | 옵션:   * Related/Unknown * Not Related   AE Type 판별에 사용되는 값 |
|  | 평가 결과 | Result of Assessment | G.k.9.i.2.r.3 | [선택] | 해외 파트너사나 국외 문헌 건 기록 |

## 3.2 Product Configuration List 모달 화면 구성

| 영역 | 구성 요소 | 설명 |
| --- | --- | --- |
| 상단 | 통합 검색창 | 제품명·성분명·제형·용량 등 입력. 2자 이상 입력 시 실시간 쿼리 실행 |
| 중앙 | Hierarchical Tree View | 검색어 기반 필터링 결과를 3-Level 계층(성분 → 프로덕트 → 제형+용량+성분의 조합 → 라이선스)으로 표시 |
| 하단 | [취소] / [적용] 버튼 | [적용] 클릭 시 Intake 화면 의심의약품 섹션에 코딩 정보 반영 및 케이스에 코딩 |

# 4. 기능 설명

---

## 4-1. 의약품 코딩 및 마스터 연동 시스템

### 제품 정보 조회 인터페이스

사용자가 마스터 데이터를 호출하고 선택하는 과정에 대한 상세 사양

* 트리거 : Manual Intake 화면 내 '의심의약품' 섹션의 [제품 정보 불러오기] 버튼 클릭.
* 컴포넌트: Product Configuration List 모달(Modal) 팝업.
* 지능형 검색:

  + 동작: 검색창에 제품명 최소 2자 이상 입력 시 실시간 쿼리 실행.
  + 매칭: 입력된 텍스트가 포함된 모든 마스터 데이터를 리스팅

### 의약품 코딩 및 조합 로직

사용자가 입력한 정보의 완성도에 따라 시스템이 제안하는 지능형 매핑 로직

### 검색 키워드

| 검색 키워드 | Product Master 검색 대상 필드 | 비고 |
| --- | --- | --- |
| 성분 | Family 계층의 "Product Family Name", "Active Pharmaceutical Ingredient" | Pharmaceutical Ingredient 항목이 복수일 경우, “/”로 이어서 하나의 개체로 처리 |
| 제품 | Products 계층 "Product Name" |  |
| 라이센스 | Licenses 계층의 “Trade Name” |  |

### 제품 검색 모달

#### **화면 구성 요소**

* 상단: 검색 범위 선택+검색어 입력
* 중앙: 계층형 제품 리스트 (Hierarchical Tree View) - 검색어에 따라 필터링된 결과 노출.
* 하단: 취소, 적용 버튼. 적용 버튼 클릭 시 Intake 화면에 코딩 및 케이스에 코딩

### 모달 UI 및 인터랙션 사양

#### 2분할 레이아웃 (2-Pane Layout)

* 좌측 영역 (Search Results): 검색 범위와 키워드에 매칭되는 항목을 리스트 형태로 나열합니다.
* 우측 영역 (Context Tree): 좌측에서 선택한 항목을 중심으로 최상위 성분(L1)부터 최하위 라이선스(Lic)까지의 전체 계층 구조를 트리 형태로 표시합니다.

#### PhPID 계층형 선택 로직

트리 내에서 특정 제품(L4 수준) 노드가 활성화되면, 해당 노드 바로 하단에 정밀도 선택 칩이 표시

* 선택 가능한 옵션 (예시: 타이레놀 325mg 검색 시):

  1. L2 (성분 + 용량): Acetaminophen + 325mg
  2. L3 (성분 + 제형): Acetaminophen + Tablet
  3. L4 (성분 + 제형 + 용량): Acetaminophen + Tablet + 325mg
* 인터랙션: 사용자는 위 칩 중 하나를 클릭하여 현재 코딩할 데이터의 계층을 결정. 예를 들어 성분과 제형만 확실히 알고 있다면 L3 칩을 클릭하여 적용합니다.

#### **좌측 영역: 검색 결과 리스트**

* **동작**: 선택된 범위(Scope) 내에서 키워드와 부분 일치(Partial Match)하는 항목을 플랫(Flat)한 리스트로 나열함.
* **정보**: 항목명, 하위 정보 요약(성분/제형 등), 허가 국가(License일 경우) 등을 간략히 표시함.

#### **우측 영역: 계층형 컨텍스트 트리 (Context Tree)**

* 동작: 좌측에서 항목 선택 시, 해당 항목을 포함한 전체 계층 구조를 트리 형태로 시각화함.
* 계층 구조: [L1 성분] → [프로덕트] → [L2/L3/L4] / [License 허가정보] 순으로 구성됨

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **하위 계층 묶음** | **선택 레벨** | **코딩 구성 요소** | **공식 보고서 코딩** | **내부 식별 메타데이터** |
|  | L1 | 성분 | 성분 (L1 수준 코딩) | Family 계층의 정보만 포함 |
| 묶어서 프로덕트 하위 | L2 | 성분 + 용량 | 성분 + 용량 (L2 수준 코딩) | Family+Product 계층의 정보만 포함, 제형 정보 제외 |
|  | L3 | 성분 + 제형 | 성분 + 제형 (L3 수준 코딩) | Family+Product 계층의 정보만 포함, 용량 정보 제외 |
|  | L4 | 성분 + 제형 + 용량 | 성분 + 제형 + 용량 (L4 수준 전체 코딩) | Family+Product 계층의 정보만 포함, 전체 정보 포함 |
| 묶어서 프로덕트 하위 | Lic | 허가 제품명 + 국가 | Trade Name + License 허가 국가 | Family+Product+Licenses 국가 매핑 정보 포함 |

### 개발 가이드

* DB에 실제 L2나 L3 마스터 데이터가 개별적으로 존재하지 않더라도, L4 정보를 바탕으로 시스템이 실시간으로 L2(성분+용량) 및 L3(성분+제형) 조합을 생성하여 클라이언트에 전달해야 함
* 사용자가 L3를 선택하고 적용했을 때, 서버에는 해당 케이스의 약물 정보로 '성분'과 '제형' 데이터만 바인딩하고 '용량' 데이터는 Null 또는 공백으로 처리하는 로직이 필요

### 디자인 및 프론트 가이드

* 검색 시 선택한 항목 (성분, 제품, 허가 제품)에 따라 우측에 보여주는 트리 접기 다르게

# 5. 제안 구조 (참고)

---

```
Manual Intake
├── 보고 관리 섹션
│   ├── 보고 구분 (C.1.3) [필수]
│   ├── 시험/연구 계획서 번호 (C.5.3) [조건부 필수 - C.1.3=2]
│   └── 인지일 (C.1.5) [필수]
├── 환자 정보 섹션
│   ├── 이름/이니셜 (D.1) [필수]
│   ├── 임상시험대상자 식별번호 (D.1.1.4) [조건부 필수 - C.1.3=2]
│   ├── 연령 (D.2.2a/b) [선택]
│   └── 성별 (D.5) [선택]
├── 원보고자 섹션
│   ├── 원보고자 국가 (C.2.r.3) [필수]
│   └── 원보고자 자격 (C.2.r.4) [선택]
├── 이상사례 섹션
│   ├── 보고자가 보고한 이상사례 (E.i.1.2) [필수]
│   └── 약물이상반응/이상사례 MedDRA 코드 (E.i.2.1b) [필수]
├── 의심의약품 섹션
│   ├── 원보고자가 보고한 의약품명 (G.k.2.2) [필수]
│   └── 의약품 코딩 정보 [필수] ────► Product Configuration List Modal
│                                      ├── 통합 검색창 (2자 이상)
│                                      ├── Hierarchical Tree View (3-Level)
│                                      │   ├── Level 1. 성분 (Family)
│                                      │   ├── Level 2. 제형+용량 (Products)
│                                      │   └── Level 3. 라이선스 (Licenses)
│                                      └── 취소 / 적용 버튼
└── 평가 및 인과성 섹션
    ├── 중대성 (E.i.3.2a-f) [필수, 6개 체크박스]
    ├── 인과성_임상(CT/CU) (G.k.9.i.2.r.3.KR.2) [필수]
    ├── 인과성_시판 후(KR) (G.k.9.i.2.r.3.KR.1) [필수]
    └── 인과성_국외(FR/CU) (G.k.9.i.2.r.3) [선택]
```

# 6. 프로토타입 / 와이어프레임

---

## 프로토타입

<https://seltaglobal.sharepoint.com/sites/RDDivision/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype%2FTracker%5FManualintake%5Fv3%2Ehtml&parent=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype>

피드백 시 프로토타입에서 해당 사항 무시 부탁드립니다.

1. 필드명, 필드 드롭다운 시 표시되는 옵션, Validation 등은 MFDS의 제공 옵션대로 표시해주세요

## 와이어프레임

### Intake 화면

![image-20260421-024112.png](https://selta.atlassian.net/wiki/download/attachments/23789589/image-20260421-024112.png?api=v2)

### 제품 불러오기 검색 모달

![image-20260421-063721.png](https://selta.atlassian.net/wiki/download/attachments/23789589/image-20260421-063721.png?api=v2)

| **#** | **기능 설명** | **액션** |
| --- | --- | --- |
| 1 | 제품 불러오기에서 불러온 레벨의 값이 표시 | - |
| 2 | 중대성 평가 입력의 경우 Null Flavor가 NI 밖에 없으므로 True와 NI만 표시 |  |
| 3 | 인과성 평가 영역  선택에 따라 활성화 비활성화 필요. | 꼭 상단의 필드 설명 표에서 비고 확인해서 개발/디자인 부탁드립니다. |
| 4 | 검색 시 검색 영역 선택하는 드롭다운 | 클릭 시 드롭다운하여 선택  옵션:   * 성분 * 제품 * 허가제품 |
| 5 | 검색한 결과값이 표시되는 영역  4번에서 선택한 영역에 해당하는 값이 표시   * 성분: 성분명 * 제품: 성분 · 제형 · 용량 / Family 부제 * 허가제품: Trade Name + 국가코드 칩 / 성분,제형,용량 부제 | 클릭 시 해당하는 값의 하위 트리가 우측에 표시  프로토타입 확인 부탁 |
| 6 | 검색한 결과값의 트리가 표시되는 영역  5번에서 나온 결과값에 해당하는 트리가 표시된다   * 성분을 선택하고 검색했을 경우: 나머지 계층은 접혀있고 성분만 표시된다 * 제품을 선택하고 검색했을 경우: 나머지 계층은 접혀있고 제품명+L2~L4까지가 표시된다. * 허가 제품을 선택하고 검색했을 경우: 나머지 계청은 접혀있고 제품명+Trade Name, 국가가 표시된다. | 클릭 시   * 해당 트리의 값이 선택 * 화살표 누르면 접기/펴기 가능 |
