|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.24 | 추가 검증룰, 비고 사항 추가 | v1.0 | v1.0.260424 |
| 김나정 | 26.04.06 | 최초작성\_필드 정보 입력 | v1.0 | v1.0.260406 |

# 1. 개요

---

* **목적**: Case Edit 화면 중 '검사 결과(Test/Results)' 섹션(ICH E2B R3 F.r)의 필드 구성, MedDRA 코딩, 검사 결과 입력 및 XML 변환 로직을 정의.
* **페이지 위치**: Safety > Tracker > Case Edit > Patient > Test

**핵심 설계 방향**:

* **한정기호 분리 입력**: 숫자값(F.r.3.2)과 한정기호(qualifier)를 분리하여 입력 편의성 및 Data 완결성 확보. XML 출력 시 결합.
* **단위 동기화**: F.r.3.3(결과 단위) 입력 시 F.r.4(정상 하한), F.r.5(정상 상한)의 단위를 동일하게 자동 입력.

## 2. 출력 정보

---

### 2.1 필드 데이터

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Test Date | 검사 날짜 | 조건부 필수 | F.r.1 |  |  |
|  | Test Name (free text) | 검사명 설명 | 조건부 필수 | F.r.2.1 |  |  |
| 연관 | MedDRA Version for Test Name | 검사명의 MedDRA 버전 | 조건부 필수 | F.r.2.2a | * 추가 검증 룰​    + MFDS: MedDRA SOC "Investigations"에 해당하는 LLT코드만 입력​ | * MedDRA 검색 창을 통해 입력    + 라이센스 없을 시 수동 입력   + 수동입력 시 드롭다운 |
| Test Name (MedDRA code) | 검사명의 MedDRA 코드 | 조건부 필수 | F.r.2.2b | * 추가 검증 룰​    + MFDS: MedDRA SOC "Investigations"에 해당하는 LLT코드만 입력​ | * MedDRA 검색 창을 통해 입력    + 라이센스 없을 시 수동 입력 |
| Test Name (MedDRA Term) ​ | 검사명의 MedDRA 용어 | 조건부 필수 | 자체 필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: F.r.2.2b.에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * MedDRA 검색 창을 통해 입력    + 라이센스 없을 시 수동 입력 |
| 연관 | Test Result (code) | 검사 결과 | 조건부 필수 | F.r.3.1 |  | * Option 값:​ 영어 병기    + 1=Positive​   + 2=Negative​   + 3=Borderline​   + 4=Inconclusive |
| 연관 | Test Result (value / qualifier) | 검사 결과 값 | 조건부 필수 | F.r.3.2 |  | * XML 예시 (ICH ICSR Technical Information참고)​    + 한정기호 없을 때 (e.g., “10 mg/dl”) `​` <value xsi:type="IVL\_PQ" >`​` <center value="10" unit="mg/dl" /></value>​   + 초과 (e.g. “ > 10 mg/dl”)`​` <value xsi:type="IVL\_PQ" >`​` <low value="10" unit="mg/dl" inclusive="false"/>`​` <high nullFlavor="PINF"/></value>​   + 미만 (e.g. “ < 10 mg/dl”)`​` <value xsi:type="IVL\_PQ" >`​` <low nullFlavor="NINF"/>`​` <high value="10" unit="mg/dl" inclusive="false"/>`​` </value>​   + 이상 (e.g. “ >= 10 mg/dl”) `​` <value xsi:type="IVL\_PQ" >`​` <low value="10" unit="mg/dl" inclusive="true"/>`​` <high nullFlavor="PINF"/></value​   + 이하(e.g. “ <= 10 mg/dl”)`​` <value xsi:type="IVL\_PQ" >`​` <low nullFlavor="NINF"/>`​` <high value="10" unit="mg/dl" inclusive="true"/>`​` </value> |
| Test Result (unit) | 검사 결과(단위) | 조건부 필수 | F.r.3.3 |  | * 처리:​    + F.r.4 .Normal Low Value 정상범위 하한값의 단위를 동일하게 자동 입력   + F.r.5 Normal High Value 정상범위 상한값의 단위를 동일하게 자동 입력 |
| Test Result (qualifier) | 검사 결과 값 | 조건부 필수 | 자체 필드 | * 기본 검증 룰​    + 조건부필수값으로 F.r.2 항목에 입력값이 있고, F.r.3.1와 F.r.3.4 항목에 값이 입력되지 않은 경우 항목 여부 검증​ | * Option 값: ​    + > (초과)​   + < (미만)​   + >= (이상)​   + =< (이하)​ * 활성화: F.r.3.2 값이 입력된 경우에만 활성화​ * 처리: XML보고서에서 F.r.3.2 Test Result (value / qualifier) 검사 결과 값에 같이 입력 (상세 예시는 F.r.3.2 항목 참고) |
|  | Normal Low Value | 정상범위 하한값 | 옵션 | F.r.4 |  |  |
|  | Normal High Value | 정상범위 상한값 | 옵션 | F.r.5 |  |  |
|  | Result Unstructured Data (free text) | 검사 결과 설명 | 조건부 필수 | F.r.3.4 |  |  |
|  | Comments (free text) | 비고 | 옵션 | F.r.6 |  |  |
|  | More Information Available | 추가 정보 여부 | 옵션 | F.r.7 |  | * Option 값: ​영어 병기    + Yes 예​   + No 아니오​ * 연관된 C.1.6.1이 1. 아무 것도 없을 때만 에러를 띄울지, 아니면 2. 필드 자체에 i로 파일이 첨부될 때, 입력하는 필드라고 알려줄지, 그것도 아니라면 3. 해당 필드로 바로가기나 이런 것으로 동작을 유지할지 (기존 방법)을 결정 필요 |

## 2.4 제안 구조

```
Test (검사 정보) [F.r] ── 반복 그룹
│
├── Test Identification
│   ├── Test Date [F.r.1]
│   ├── Test Name (free text) [F.r.2.1]
│   ├── MedDRA Version for Test Name [F.r.2.2a] ─┐
│   ├── Test Name MedDRA Code [F.r.2.2b]          ├─ 연관
│   └── Test Name MedDRA Term (자체 필드)         ─┘
│
├── Test Result
│   ├── Test Result (code) [F.r.3.1]       ─┐
│   ├── Test Result (value) [F.r.3.2]       │
│   ├── Test Result (unit) [F.r.3.3]        ├─ 연관
│   │   ├──→ 자동: Normal Low Value 단위
│   │   └──→ 자동: Normal High Value 단위
│   └── Test Result (qualifier) (자체 필드) ─┘
│       └──→ F.r.3.2 입력 시에만 활성화
│
└── Normal Range & Free Text
    ├── Normal Low Value [F.r.4]
    ├── Normal High Value [F.r.5]
    ├── Result Unstructured Data [F.r.3.4]
    ├── Comments [F.r.6]
    └── More Information Available [F.r.7] ──→ C.1.6.1 연관 (미확정)
```

## 3. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | MedDRA 코딩 팝업 | F.r.2.2a/2.2b/Term을 MedDRA 팝업에서 입력. MFDS 시 SOC "Investigations" LLT만 허용 | 코딩 필드 클릭 |
| 2 | 검사 결과 삼원 검증 | F.r.2(검사명) 입력 시 F.r.3.1(코드) / F.r.3.2(수치)+qualifier / F.r.3.4(텍스트) 중 최소 1개 필수 | 저장/Validation |
| 3 | 한정기호 분리 입력 | F.r.3.2에 숫자만, qualifier에 한정기호(>, <, >=, =<)를 분리 입력. XML 출력 시 IVL\_PQ 형식으로 결합 | 저장 및 XML 생성 시 |
| 4 | 단위 자동 동기화 | F.r.3.3(단위) 입력 시 F.r.4(정상 하한)와 F.r.5(정상 상한)의 단위를 동일하게 자동 입력 | F.r.3.3 값 변경 시 |
| 5 | F.r.7 → C.1.6.1 연동 | F.r.7=Yes 선택 시 C.1.6.1(추가 자료 여부) 확인. C.1.6.1이 False이면 해당 필드로 바로가기하여 작성 강제 | F.r.7 값 Yes로 변경 시 |

# 4. 정책

---

## 4.1 MedDRA 팝업 & License Expire 공통 규칙

검사명 MedDRA 필드(F.r.2.2a/b 및 자체필드 Term)에 적용:

| 조건 | 동작 |
| --- | --- |
| MedDRA License 유효 | MedDRA 팝업을 통해 코드·버전·용어 입력 |
| MedDRA License Expire | Free text(자유기재)로 전환. Term 필드는 비필수, 250자 이하 검증. 버전은 드롭다운으로 수동 입력 |

## 4.2 XML 한정기호 처리 (Test Result — F.r.3.2)

Test Result (value / qualifier)의 XML 출력 형식 (ICH ICSR Technical Information 참고):

| 한정기호 | 예시 | XML 구조 요약 |
| --- | --- | --- |
| 없음 | 10 mg/dl | `<center value="10" unit="mg/dl" />` |
| >(초과) | >10 mg/dl | `<low value="10" inclusive="false"/>`, `<high nullFlavor="PINF"/>` |
| < (미만) | < 10 mg/dl | `<low nullFlavor="NINF"/>`, `<high value="10" inclusive="false"/>` |
| >= (이상) | >= 10 mg/dl | `<low value="10" inclusive="true"/>`, `<high nullFlavor="PINF"/>` |
| =< (이하) | =< 10 mg/dl | `<low nullFlavor="NINF"/>`, `<high value="10" inclusive="true"/>` |

## 4.3 동적 UI 제어 — Test Result (qualifier) 활성화

| 조건 | 동작 |
| --- | --- |
| F.r.3.2 (Test Result value) 값 입력됨 | Test Result (qualifier) 활성화 |
| F.r.3.2 미입력 | Test Result (qualifier) 비활성화 |

## 4.4 자동 단위 동기화 — Test Result (unit)

| 조건 | 동작 |
| --- | --- |
| F.r.3.3 (Test Result unit) 입력됨 | F.r.4 Normal Low Value 및 F.r.5 Normal High Value의 단위를 동일 값으로 자동 입력 |

## 4.5 조건부 필수 — Test Result (qualifier)

| 조건 | 동작 |
| --- | --- |
| F.r.2에 입력값 있음 AND F.r.3.1, F.r.3.4 모두 미입력 | Test Result (qualifier) 필수 검증 |

## 4.6 MFDS 전용 검증 — MedDRA SOC 제한

| 조건 | 동작 |
| --- | --- |
| Destination이 MFDS | MedDRA SOC "Investigations"에 해당하는 LLT 코드만 입력 허용 |

# 5. 요구사항

---

> 원문에 정의 없음

## 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
