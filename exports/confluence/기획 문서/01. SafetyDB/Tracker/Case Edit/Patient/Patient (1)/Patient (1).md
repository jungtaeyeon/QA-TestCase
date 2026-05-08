|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.06 | 최초작성\_필드 정보 입력 | v1.0 | v1.0.260406 |
|  |  |  |  |  |

# 1. 개요

---

* **목적**: Case Edit 화면 중 '환자 정보(Patient Characteristics)' 섹션의 필드 구성, 데이터 유형, 유효성 검증 규칙 및 연관 필드 간 제어 로직을 정의.
* **페이지 위치**: Safety > Tracker > Case Edit > Patient > Patient

# 2. 출력 정보

---

## 2.1 필드 데이터

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Patient (name or initials) | 이름(이니셜) | 필수 | D.1 |  | * Manual Intake에서 입력한 정보를 그대로 입력​ |
|  | Patient Medical Record Number(s) and Source(s) of the Record Number (GP Medical Record Number) | 1차 의료기관 진료기록번호 | 옵션 | D.1.1.1 |  |  |
|  | Patient Medical Record Number(s) and Source(s) of the Record Number (Specialist Record Number) | 2, 3차 의료기관 진료기록번호 | 옵션 | D.1.1.2 |  |  |
|  | Patient Medical Record Number(s) and Source(s) of the Record Number (Hospital Record Number) | 병원 진료기록번호 | 옵션 | D.1.1.3 |  |  |
|  | Patient Medical Record Number(s) and Source(s) of the Record Number (Investigation Number) | 임상시험대상자 식별번호 | 조건부 필수 | D.1.1.4 |  |  |
|  | Date of Birth | 생년월일 | * D.2.1, D.2.2, D.2.2.1, D.2.3 항목중 1항목만 입력 | D.2.1 | MFDS에서는 D.2.1, D.2.2, D.2.2.1, D.2.3 항목 중 1항목만 입력하도록 하고 있음. ​  ▶ 2개 이상 값이 입력되었다면 보고서 출력 또는 Reporting시 Destination이 MFDS인 경우에는 다음의 우선 순위에 따라 XML보고서에 출력: D.2.1→ D.2.2 → D.2.2.1 → D.2.3​ |  |
|  | Patient Age Group (as per reporter) | 환자의 연령대 | D.2.1, D.2.2, D.2.2.1, D.2.3 항목중 1항목만 입력 | D.2.3 | MFDS에서는 D.2.1, D.2.2, D.2.2.1, D.2.3 항목 중 1항목만 입력하도록 하고 있음. ​  ▶ 2개 이상 값이 입력되었다면 보고서 출력 또는 Reporting시 Destination이 MFDS인 경우에는 다음의 우선 순위에 따라 XML보고서에 출력: D.2.1→ D.2.2 → D.2.2.1 → D.2.3​ | * Option 값: ​영문 병기    + 0=Foetus​   + 1=Neonate (Preterm and Term newborns)​   + 2=Infant​   + 3=Child​   + 4=Adolescent​   + 5=Adult​   + 6=Elderly |
| 연관 | Age at Time of Onset of Reaction / Event (number) | 발현 당시 연령 | * D.2.1, D.2.2, D.2.2.1, D.2.3 항목중 1항목만 입력 | D.2.2a | MFDS에서는 D.2.1, D.2.2, D.2.2.1, D.2.3 항목 중 1항목만 입력하도록 하고 있음. ​  ▶ 2개 이상 값이 입력되었다면 보고서 출력 또는 Reporting시 Destination이 MFDS인 경우에는 다음의 우선 순위에 따라 XML보고서에 출력: D.2.1→ D.2.2 → D.2.2.1 → D.2.3​ |  |
| Age at Time of Onset of Reaction / Event (unit) | 발현 당시 연령(단위) | * D.2.1, D.2.2, D.2.2.1, D.2.3 항목중 1항목만 입력 | D.2.2b | MFDS에서는 D.2.1, D.2.2, D.2.2.1, D.2.3 항목 중 1항목만 입력하도록 하고 있음. ​  ▶ 2개 이상 값이 입력되었다면 보고서 출력 또는 Reporting시 Destination이 MFDS인 경우에는 다음의 우선 순위에 따라 XML보고서에 출력: D.2.1→ D.2.2 → D.2.2.1 → D.2.3​ | * 허용 값:Year, Month, Week, Day, Hour and Decade​ |
| 연관 | Gestation Period When Reaction / Event Was Observed in the Foetus (number) | 발현 당시의 임신기간 | * D.2.1, D.2.2, D.2.2.1, D.2.3 항목중 1항목만 입력 | D.2.2.1a | MFDS에서는 D.2.1, D.2.2, D.2.2.1, D.2.3 항목 중 1항목만 입력하도록 하고 있음. ​  ▶ 2개 이상 값이 입력되었다면 보고서 출력 또는 Reporting시 Destination이 MFDS인 경우에는 다음의 우선 순위에 따라 XML보고서에 출력: D.2.1→ D.2.2 → D.2.2.1 → D.2.3​ |  |
| Gestation Period When Reaction/Event Was Observed in the Foetus (unit) | 발현 당시의 임신기간(단위) | D.2.1, D.2.2, D.2.2.1, D.2.3 항목중 1항목만 입력  제한된 UCUM코드 | D.2.2.1b | MFDS에서는 D.2.1, D.2.2, D.2.2.1, D.2.3 항목 중 1항목만 입력하도록 하고 있음. ​  ▶ 2개 이상 값이 입력되었다면 보고서 출력 또는 Reporting시 Destination이 MFDS인 경우에는 다음의 우선 순위에 따라 XML보고서에 출력: D.2.1→ D.2.2 → D.2.2.1 → D.2.3​ | * 허용치: Month, Week, Day and {Trimester}​ |
|  | Sex | 성별 | 조건부 필수 | D.5 |  | * Option 값:​ 영문 병기    + 1=Male​   + 2=Female​ |
|  | Last Menstrual Period Date | 최종월경일 | 옵션 | D.6 |  | 처리: D.5의 value=1 (성별이 남자)인 경우, 해당 항목 비활성화 |
|  | Body Weight (kg) | 체중(kg) | 옵션 | D.3 |  |  |
|  | Height (cm) | 신장(cm) | 옵션 | D.4 |  |  |

## 2.2 제안 구조

```
Patient (환자 정보)
├── Patient Identification (식별)
│   ├── Patient (name or initials) [D.1] ─── Manual Intake 연동
│   ├── GP Medical Record Number [D.1.1.1]
│   ├── Specialist Record Number [D.1.1.2]
│   ├── Hospital Record Number [D.1.1.3]
│   └── Investigation Number [D.1.1.4]
│
├── Age / Date of Birth ─── 그룹 내 1항목만 입력 (MFDS)
│   ├── Date of Birth [D.2.1]
│   ├── Patient Age Group [D.2.3]
│   ├── Age at Onset [D.2.2a] + Unit [D.2.2b]   ── 연관 쌍
│   └── Gestation Period [D.2.2.1a] + Unit [D.2.2.1b] ── 연관 쌍
│
└── Demographics (신체/인구학적)
    ├── Sex [D.5]
    ├── Last Menstrual Period Date [D.6] ── D.5=1이면 비활성화
    ├── Body Weight (kg) [D.3]
    └── Height (cm) [D.4]
```

# 3. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | Intake 데이터 연동 | Manual Intake에서 입력된 D.1(이름/이니셜) 정보가 자동 입력된 상태로 표시 | 자동 |
| 2 | D.5 → D.6 동적 제어 | D.5에서 1(Male)을 선택한 경우 D.6(최종월경일) 필드 비활성화 | D.5 값 변경 시 |
| 3 | 연령 상호 배타 검증 | MFDS 보고 시 D.2.1, D.2.2, D.2.2.1, D.2.3 중 1개만 XML 출력. 다수 입력 시 우선순위 적용 | 보고서 생성/Validation 시 |
| 4 | D.2.2a ↔ D.2.2b 연관 쌍 검증 | 한쪽 값이 입력되면 다른 쪽도 필수 | 저장/Validation 시 |
| 5 | D.2.2.1a ↔ D.2.2.1b 연관 쌍 검증 | 한쪽 값이 입력되면 다른 쪽도 필수 | 저장/Validation 시 |

# 4. 정책

---

## 4.1 연령 그룹 배타적 입력 규칙 (MFDS)

D.2.1(Date of Birth), D.2.2(Age at Onset), D.2.2.1(Gestation Period), D.2.3(Age Group) 중 1항목만 입력하도록 제한한다.

| 조건 | 동작 |
| --- | --- |
| 2개 이상 값이 입력된 상태에서 Destination이 MFDS | XML 보고서 출력 시 우선순위 적용: D.2.1 → D.2.2 → D.2.2.1 → D.2.3 |

## 4.2 동적 UI 제어 — Sex(D.5) 종속

| 조건 | 동작 |
| --- | --- |
| D.5 = 1 (Male) | Last Menstrual Period Date (D.6) 비활성화 |
| D.5 = 2 (Female) 또는 미입력 | Last Menstrual Period Date (D.6) 활성화 |

# 5. 요구사항

---

| 요구사항 | 기획 방향 | 의도 | 분류 |
| --- | --- | --- | --- |
| 환자 식별 정보 입력 | D.1 + 진료기록번호 4종 + 임상시험대상자번호 | Valid ICSR의 4대 요소 중 하나인 환자 식별 확보 | Requirement |
| 연령 정보 입력 및 상호 배타 | 4가지 연령 정보 그룹, MFDS 시 우선순위 출력 | 규제기관별 연령 보고 요건 충족 | Requirement |
| 성별 기반 동적 제어 | D.5 → D.6 비활성화 | 불필요 필드 입력 방지 | Requirement |

# 6. 프로토타입 / 와이어프레임
