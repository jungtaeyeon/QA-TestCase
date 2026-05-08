|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.23 | 추가 검증룰 및 비고 사항 작성 | v1.0 | v1.0.260423 |
| 김나정 | 26.04.06 | 최초작성\_필드 정보 입력 | v1.0 | v1.0.260406 |

# 개요

* Case Edit 화면 중 '원보고자 정보(Primary Source)' 섹션의 기능 및 로직을 정의

  + **데이터 연동**: Manual Intake 단계에서 입력된 '원보고자의 주소(상세주소)' 및 '국가코드' 정보가 자동으로 연동되어 사용자 재입력을 최소화
  + **조건부 유효성 검사**
  + **동적 UI 제어**: 보고자의 자격(Qualification) 선택에 따라 하위 필드 및 관련 의료 전문가 확인 필드(E.i.8)를 실시간으로 활성화/비활성화
* 페이지 위치: Tracker>Case Edit>Case>Reporter

# 섹션별 상세 필드 명세

# 1. 개요

---

* **목적**: Case Edit 화면 중 '원보고자 정보(Primary Source)' 섹션의 기능 및 로직 정의.
* **페이지 위치**: Tracker > Case Edit > Case > Reporter
* **핵심 설계 방향**:

  + **데이터 연동**: Manual Intake 단계에서 입력된 '원보고자의 주소(상세주소)' 및 '국가코드' 정보가 자동으로 연동되어 사용자 재입력을 최소화.
  + **동적 UI 제어**: 보고자의 자격(Qualification) 선택에 따라 하위 필드 및 관련 의료 전문가 확인 필드(E.i.8)를 실시간으로 활성화/비활성화.

# 2. 출력 정보

---

## 2.1 출력 정보 데이터

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Reporter’s Title | 원보고자의 직위 | 옵션 | C.2.r.1.1 |  |  |
|  | Reporter’s Organisation | 원보고자의 조직 | 조건부 필수 | C.2.r.2.1 |  |  |
|  | Reporter’s Department | 원보고자의 부서 | 옵션 | C.2.r.2.2 |  |  |
|  | Reporter’s Given Name | 원보고자의 이름 | 조건부 필수 | C.2.r.1.2 |  |  |
|  | Reporter’s Middle Name | 원보고자의 중간 이름 | 옵션 | C.2.r.1.3 |  |  |
|  | Reporter’s Family Name | 원보고자의 성 | 옵션 | C.2.r.1.4 |  |  |
|  | Reporter’s Street | 원보고자의 주소(상세주소) | 조건부 필수 C.2.r.2.3, C.2.r.2.4, C.2.r.2.5 중 1개 | C.2.r.2.3 |  | * Manual Intake에서 입력한 값 있을 경우 입력된 상태 |
|  | Reporter’s City | 원보고자의 주소(도로명과 번호) | 조건부 필수 C.2.r.2.3, C.2.r.2.4, C.2.r.2.5 중 1개 | C.2.r.2.4 |  |  |
|  | Reporter’s State or Province | 원보고자의 주소(특별시, 광역시, 도 등) | 조건부 필수 C.2.r.2.3, C.2.r.2.4, C.2.r.2.5 중 1개 | C.2.r.2.5 |  |  |
|  | Reporter’s Postcode | 원보고자의 주소(우편번호) | 옵션 | C.2.r.2.6 |  |  |
|  | Reporter’s Telephone | 원보고자의 전화번호 | 옵션 | C.2.r.2.7 |  |  |
|  | Reporter’s Country Code | 원보고자의 국가코드 | 조건부 필수 | C.2.r.3 |  | * Manual Intake에서 입력한 값 입력된 상태 |
|  | Primary Source for Regulatory Purposes | 규제 목적 상 원보고자 | 조건부 필수 | C.2.r.5 |  | * 처리: Check시 XML필드에 1입력 (1= primary)​ |
|  | Qualification | 원보고자의 자격 | 필수 | C.2.r.4 |  | * 처리: 값을 4 또는 5 선택한 경우에만 E.i.8 Medical Confirmation by Healthcare Professional 의료전문가 확인 여부 필드를 활성화 * Option 값:​ 한글과 병기    + 1=Physician​   + 2=Pharmacist​   + 3=Other health professional​   + 4=Lawyer​   + 5=Consumer or other non health professional​ |
|  | Other Health Professional Type | 기타 의료전문가 구분 | 옵션 | C.2.r.4.KR.1 |  | * 처리: Qualification 원보고자의 자격 (C.2.r.4) 필드 항목이 "3＂이 아닌 경우에는 필드 비활성​ * Option값:​ 한글과 병기    + 1=Nurse ​   + 2=Other |

## 2.2 제안 구조

```
Reporter (원보고자 정보)
├── Reporter Identity (신원)
│   ├── Reporter's Title [C.2.r.1.1]
│   ├── Reporter's Given Name [C.2.r.1.2]
│   ├── Reporter's Middle Name [C.2.r.1.3]
│   └── Reporter's Family Name [C.2.r.1.4]
│
├── Reporter Organisation (소속)
│   ├── Reporter's Organisation [C.2.r.2.1]
│   └── Reporter's Department [C.2.r.2.2]
│
├── Reporter Address (주소) ─── Manual Intake 연동
│   ├── Reporter's Street [C.2.r.2.3]     ┐
│   ├── Reporter's City [C.2.r.2.4]       ├─ 3개 중 1개 이상 필수
│   ├── Reporter's State or Province [C.2.r.2.5] ┘
│   ├── Reporter's Postcode [C.2.r.2.6]
│   ├── Reporter's Telephone [C.2.r.2.7]
│   └── Reporter's Country Code [C.2.r.3]
│
└── Qualification & Regulatory (자격 및 규제)
    ├── Primary Source for Regulatory Purposes [C.2.r.5]
    ├── Qualification [C.2.r.4] ──→ 4 or 5 선택 시 E.i.8 활성화
    └── Other Health Professional Type [C.2.r.4.KR.1] ──→ C.2.r.4=3일 때만 활성화
```

# 3. 기능 설명

---

> 원문에 정의 없음

# 4. 정책

---

## 4.1 데이터 연동 (Manual Intake → Reporter)

| 대상 필드 | 연동 동작 |
| --- | --- |
| Reporter's Street (C.2.r.2.3) | Manual Intake에서 입력한 값이 있을 경우 자동 입력된 상태 |
| Reporter's Country Code (C.2.r.3) | Manual Intake에서 입력한 값 자동 입력된 상태 |

## 4.2 동적 UI 제어 — Qualification(C.2.r.4) 종속

| 조건 | 동작 |
| --- | --- |
| Reporter’s City (C.2.r.4) = 4 (Lawyer) 또는 5 (Consumer or other non health professional) | E.i.8 Medical Confirmation by Healthcare Professional 필드 활성화 |
| Reporter’s City(C.2.r.4) = 3 (Other health professional) | Other Health Professional Type (C.2.r.4.KR.1) 필드 활성화 |
| Reporter’s City(C.2.r.4) ≠ 3 | Other Health Professional Type (C.2.r.4.KR.1) 필드 비활성화 |

## 4.3 조건부 필수 — 주소 그룹

| 조건 | 동작 |
| --- | --- |
| C.2.r.2.3, C.2.r.2.4, C.2.r.2.5 중 최소 1개 입력 | 조건부 필수 충족 |

## 4.4 Primary Source 체크 처리

| 조건 | 동작 |
| --- | --- |
| Primary Source for Regulatory Purposes (C.2.r.5) 체크 | XML 필드에 값 1 입력 (1 = primary) |

# 5. 요구사항

---

> 원문에 정의 없음

# 6. 프로토타입 / 와이어프레임
