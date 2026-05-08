|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.30 | RA Due 계산 및 필터링 정책 수정 | v1.0 | v1.0.260430 |
| 김나정 | 26.03.30 | 최초 작성 | v1.0 | v1.0.260327 |
|  |  |  |  |  |

## 1. 개요

---

* **목적**: 이상사례(AE) 사례의 인입부터 종결까지 단일 화면에서 관리하는 통합 Tracker 화면 구축. 실무자가 [식별 ➔ 우선순위 판단 ➔ 즉각 액션]으로 이어지는 Tabulated Dashboard를 통해 PV 업무를 수행할 수 있도록 한다.
* **페이지 위치**: Safety > Tracker (추정 — 원본에 IA 경로 명시 없음)
* **기대 효과**:

  + 도구 학습 비용 절감 및 프로세스 누락 방지
  + 실무자 스스로 업무 우선순위를 조정하는 Self-Service Analysis 환경 제공
  + 감사 시 즉각적인 데이터 추출을 통한 감사 대응 준비 확보

## 2. 정책

---

### 2.1 사례 생애주기 관리

별도의 메뉴 이동 없이 그리드 내에서 사례의 전체 과정을 제어 가능하다.

| 기능 | 설명 |
| --- | --- |
| 신규 생성 (Intake) | Manual 생성 버튼 제공 |
| 데이터 인입 | XML Import 및 AI 기반의 Convert(Extraction) 지원 |
| 후속 보고 (Follow-up) | 기존 사례 선택 후 FU 생성 시 Case Edit으로 자동 연결 (기존 데이터 로드) |
| 관리 액션 | 수정, 삭제(Void/Nullify), 보관(Archive) 기능 제공 [추후 예정] |

### 2.2 워크로드 및 담당자 관리

| 조건 | 동작 |
| --- | --- |
| 최초 케이스 생성 시 | 생성한 사람이 담당자(Assignee) 컬럼에 자동 표시 |
| 관리자 재배정 [추후 고도화] | 시스템 로직에 의해 자동 배정된 담당자를 관리자가 필요 시 수동 재배정 가능 |

### 2.3 권한 제어 [추후 개발]

| 역할 | 권한 |
| --- | --- |
| 일반 사용자 | 본인에게 할당된 사례의 편집 권한만 보유 |
| 관리자 (Admin) | 타인의 담당자를 수동으로 변경 가능 |

### 2.4 데이터 그리드 제어 (Filter & Export)

| 기능 | 설명 |
| --- | --- |
| 다중 필터링 | 그리드 내 컬럼에 대해 검색 및 필터링 지원 |
| 데이터 내보내기 | 필터링된 결과 그대로 Excel 추출 [추후 개발] |

### 2.5 보고 출처 분류 (Source Type Classification Logic)

[보고 출처 분류](https://selta.atlassian.net/wiki/spaces/IS/pages/29622314) 로직 참조

### 2.6 AE Type 분류 (이상사례 구분 로직)

[AE Type 분류](https://selta.atlassian.net/wiki/spaces/IS/pages/29982809/AE%2BType) 로직 참조

### 2.7 MFDS 보고 대상 및 기한 설정 (MFDS Reporting Triage Logic)

[보고 기한 설정](https://selta.atlassian.net/wiki/spaces/IS/pages/30441502) 로직 참조

### 3. 요구사항

---

| 요구사항 | 기획 방향 | 의도 | 분류 |
| --- | --- | --- | --- |
| 사례 인입~종결 통합 관리 | 단일 Tracker 그리드에서 Intake, FU, Edit, Void/Archive 수행 | 도구 학습 비용 절감, 프로세스 누락 방지 | Requirement |
| 자동 AE Type 분류 | 중대성/인과성/예측성 판정 로직 기반 자동 분류 | 실무자 Self-Service Analysis 환경 제공 | Requirement |
| 규제기관 보고 기한 자동 산정 | Source Type + AE Type 기반 MFDS 보고 매트릭스 적용 | 보고 기한 누락 방지, 감사 대응 | Requirement |
| 다중 필터링 및 검색 | Case ID 검색, Date Range, Global Filter 제공 | 워크로드 파악 및 우선순위 관리 | Requirement |
| 담당자 자동 배정 | 생성자 자동 배정 | 업무 분배 최적화 | Requirement |
| 의약품 정보 매칭 | 성분/브랜드/제형 Partial Match 기반 세부 분류 | 정밀한 보고 출처 분류 | Enhancement (추후) |
| 권한 제어 | 역할 기반 편집/재배정 권한 분리 | 데이터 무결성 보장 | Enhancement (추후) |
| Excel 내보내기 | 필터링 결과 그대로 Excel 추출 | 감사 대응 | Enhancement (추후) |

## 4. 출력 정보

---

### 4.1 Tracker 그리드

| 컬럼명 | 필드 데이터 매핑 | 설명 | 비고 | 컬럼 헤더 정렬/필터링 |
| --- | --- | --- | --- | --- |
| Case ID | C.1.1의 리포트넘버 | 사례 고유 식별자 |  |  |
| Worldwide Unique Case Identification | C.1.8.1 | 고유식별 보고자관리번호 |  |  |
| Day0 | C.1.5 | 최근 인지일 |  | 정렬 |
| FU No | NA | 후속보고 순번. 수정/무효화 시 Amend/Null 표시, 후속보고 순번은 그대로 동일하게 부여 | Follow-up Sequencing Logic 적용 | 필터링  옵션: Null, Amend |
| Country | C.2.r.3 (누락시 E.i.9) | 발생 국가. 누락 시 E.i.9 발현 당시 환자 소재 국가 대체 출력 |  | 필터링  옵션: KR, US |
| Report Type | C.1.3 | 보고 구분. C.1.3이 2(Study)인 경우 계획서 번호 대신 출력 |  | 필터링  옵션: Spontaneous / Study / Other / Unknown |
| Reported Product | G.k.2.2 | 원보고자가 보고한 의약품명 |  |  |
| Product | NA | 내부 DRUG Key로 코딩된 품목명 출력 |  | 필터링 옵션: Product Configuration의 Drug Key가 옵션으로 표시 |
| Reported AE | E.i.1.2 | 이상사례명 |  |  |
| MedDRA coded Term | E.i.2.1b | MedDRA 코딩 용어 (영어) | 펼치기/접기 UI 제공 (추후) |  |
| AE Type | NA | AE type Classification Logic에 따른 자동 분류 값 |  | 필터링  옵션: SUSAR (사망/치명적), SUSAR (기타), SADR, ADR, AE, Unclassifiable |
| RA Due | NA | 보고 기한 상태 (Day-N / D-Day / Missing / On Time / Overdue / NA) | •보고 대상이 아닌 경우: NA  •보고 대상인 경우: Today와 D-Day 를 비교   * Today < D-Day (Due Date 미만) ▶ Day-N로 남은 일수 표시 * Today = D-Day (Due Date 동일) ▶ D-Day 표시 * Today > D-Day (Due Date 초과) ▶ Overdue(D+N) : 보고 여부 X or UNK   보고 완료시 계산   * Submission Date <= D-Day ▶ On Time: 보고 기한 내 보고 완료 (보고 여부 O & 보고 기한 준수 O) * Submission Date > D-Day ▶ Late: 보고 기한 초과하여 보고 완료 (보고 여부 O & 보고 기한 준수 X) | * 필터링 옵션:    + Day-N   + D-day   + Overdue   + On time   + Late   + NA * Day-N 선택 시 Day-1부터 해당하는 케이스 전부 표시 |
| Status | NA | 처리 상태 | * Entry * QC * MA * Approval * submission (보고 대상이어야만 생김) * Completion * Archived [추후] | 필터링  옵션: Entry / QC / MA / Approval / Approved / Submission / Close |
| Assignee | NA | 담당자 | * 사용자 이름 | 필터링  옵션: 사용자 이름 |
| Owner | NA | 생성자 (케이스 최초 생성 User) | * 사용자 이름 | 필터링 옵션: 사용자 이름 |

## 5. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | 신규 사례 생성 | Manual 생성 버튼으로 새 사례 Intake | Create |
| 2 | XML Import | XML 파일 기반 데이터 인입  Data-hub의 XML Import 화면으로 이동 | Import |
| 3 | Follow-up 생성 | 기존 사례 선택 후 FU 생성, Case Edit 자동 연결  트래커 케이스 ID 우클릭하여 Follow-Up 선택하면 Follow-up 생성 페이지(case-edit)에서 생성 가능 | Create FU |
| 4 | 사례 수정 | 기존 사례 데이터 편집 | Edit |
| 5 | 필터링 | Date Range, Global Filter | Filter |
| 6 | 검색 | Case ID 및 Worldwide Unique Case Identification 검색 | Search |

## 5-1. 제안 구조

---

```
Tracker Page
├── [Header] 검색 & 필터 영역
│   ├── Case ID 검색 (Input Box)
│   ├── Date Range (RA Due)
│   └── Date Range (Calendar Picker: Day0)
├── [Actions] 사례 관리 액션
│   ├── + New Case
│   │   ├── Manual Intake
│   │   └── XML Import
│   └── Follow-up (Tracker 리스트에서 추가)
└── [Grid] 데이터 그리드
    ├── Case ID | Day0 | FU No | Country | Report Type | Product Name | ...
    └── ... (AE Term | MedDRA | AE Type | RA Due | Status | Assignee)
```

## 6. 프로토타입 / 와이어프레임

---

## 프로토타입

<https://seltaglobal.sharepoint.com/sites/RDDivision/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype%2FTracker%5Fv3%2Ehtml&parent=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype>

## 와이어프레임

![image-20260415-075111.png](https://selta.atlassian.net/wiki/download/attachments/23494726/image-20260415-075111.png?api=v2)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | Product 명 필터링 | * 필터링 클릭 시 Product Configuration에 저장된 Licenses의 [Trade Name]값을 표시 * 검색을 통해 Trade Name 검색 가능 |
