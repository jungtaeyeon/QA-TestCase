|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.24 | 추가 검증룰, 비고 사항 추가 | v1.0 | v1.0.260424 |
| 김나정 | 26.04.06 | 최초작성\_필드 정보 입력 | v1.0 | v1.0.260406 |

# 1. 개요

---

* **목적**: 태아/신생아 사례에서 환자(아이)의 부모 정보, 부모의 과거 병력 및 부모의 병용약 정보를 구조적으로 입력. ICH E2B R3 D.10 섹션에 해당.
* **페이지 위치**: Safety > Tracker > Case Edit > Patient > Parent

# 2. 출력 정보

---

## 2.1 필드 데이터

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Parent Identification | 부모이름(이니셜) | 옵션 | D.10.1 |  |  |
|  | Sex of Parent | 부모의 성별 | 조건부 필수 | D.10.6 |  | * Option 값:​영문 병기    + 1=Male​   + 2=Female |
|  | Date of Birth of Parent | 부모의 생년월일 | 옵션 | D.10.2.1 |  |  |
| 연관 | Age of Parent (number) | 부모의 연령(숫자) | 조건부 필수 | D.10.2.2a |  |  |
| Age of Parent (unit) | 부모의 연령(단위) | 조건부 필수 | D.10.2.2b |  | * Option 값:​    + 10.a=연대​   + a=연 |
|  | Body Weight (kg) of Parent | 부모의 체중(kg) | 옵션 | D.10.4 |  |  |
|  | Height (cm) of Parent | 부모의 신장(cm) | 옵션 | D.10.5 |  |  |
|  | Last Menstrual Period Date of Parent | 부모(어머니)의 최종 월경일 | 옵션 | D.10.3 |  |  |
|  | Relevant Medical History type of Parent | 부모의 병력 구분​ | 옵션 | 자체 필드 |  | * Option 값: ​    + 1= Diseases​   + 2= Conditions​   + 3= Surgical procedures​   + 4= Psychological trauma​   + 5= Risk factors​   + 6=Other​ |
|  | Relevant Medical History Term of Parent reported from primary sources | 원보고자가 보고한 부모의 병력​ | 옵션 | 자체 필드 | 250자 이하​ |  |
| 연관 | MedDRA Version for Medical History | 과거 병력 MedDRA 버전 | 조건부 필수 | D.10.7.1.r.1a |  | * MedDRA 팝업    + License Expire경우 자유기재​ |
| Medical History (disease / surgical procedure / etc.) (MedDRA code) | 과거 병력 MedDRA 코드 | 조건부 필수 | D.10.7.1.r.1b |  | * MedDRA 팝업    + License Expire경우 자유기재​ |
| Medical History (disease / surgical procedure / etc.) (MedDRA Term) | 과거 병력 MedDRA 용어​ | 조건부 필수 | 자체 필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.10.7.1.r.1b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * MedDRA 팝업    + License Expire경우 자유기재​ |
|  | Start Date | 시작일 | 옵션 | D.10.7.1.r.2 |  |  |
|  | Continuing | 지속여부 | 옵션 | D.10.7.1.r.3 |  | * Option 값:​ 영어 병기    + Yes 예 ​   + No 아니오​ * 처리: 해당 field 값이 True이면 D.10.7.1.r.4 필드 값은 삭제하고 비활성​ |
|  | End Date | 종료일 | 옵션 | D.10.7.1.r.4 |  |  |
|  | Comments | 비고 | 옵션 | D.10.7.1.r.5 |  |  |
|  | Text for Relevant Medical History and Concurrent Conditions of Parent | 과거 병력 설명 | 옵션 | D.10.7.2 |  |  |
|  | Name of Drug as Reported | 의약품명 | 옵션 | D.10.8.r.1 |  |  |
| 연관 | medicinal product version | 의약품 코드 버전 | 조건부 필수 | D.10.8.r.1.KR.1a |  |  |
| medicinal product ID | 의약품 코드 | 조건부 필수 | D.10.8.r.1.KR.1b |  |  |
| 연관 | MPID Version Date/Number | 의약품식별자(MPID) 버전 | 옵션 | D.10.8.r.2a |  | IDMP 확정 후 사용​ |
| Medicinal Product Identifier (MPID) | 의약품식별자(MPID) | 옵션 | D.10.8.r.2b |  | IDMP 확정 후 사용​ |
| 연관 | PhPID Version Date/Number | 제제식별자(PhPID) 버전 | 옵션 | D.10.8.r.3a |  | IDMP 확정 후 사용​ |
| Pharmaceutical Product Identifier (PhPID) | 제제식별자(PhPID) | 옵션 | D.10.8.r.3b |  | IDMP 확정 후 사용​ |
|  | Start Date | 시작일 | 옵션 | D.10.8.r.4 |  |  |
|  | End Date | 종료일 | 옵션 | D.10.8.r.5 |  |  |
| 연관 | MedDRA Version for Indication | 적응증의 MedDRA 버전 | 조건부 필수 | D.10.8.r.6a |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Indication (MedDRA code) | 적응증의 MedDRA 코드 | 조건부 필수 | D.10.8.r.6b |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Indication (MedDRA Term) | 적응증의 MedDRA 용어​ | 조건부 필수 | 자체 필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.10.8.r.6b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| 연관 | MedDRA Version for Reaction | 약물이상반응의 MedDRA 버전 | 조건부 필수 | D.10.8.r.7a |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Reactions (MedDRA code) | 약물이상반응의 MedDRA 코드 | 조건부 필수 | D.10.8.r.7b |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Reactions (MedDRA Term) | 약물이상반응의 MedDRA 용어​ | 조건부 필수 | 자체 필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.10.8.r.7b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |

## 2.5 제안 구조

```
Parent (부모 정보)
│
├── Parent Demographics (인적/신체)
│   ├── Parent Identification [D.10.1]
│   ├── Sex of Parent [D.10.6]
│   ├── Date of Birth of Parent [D.10.2.1]
│   ├── Age of Parent (number) [D.10.2.2a] ─┐ 연관
│   ├── Age of Parent (unit) [D.10.2.2b]    ─┘
│   ├── Body Weight (kg) [D.10.4]
│   ├── Height (cm) [D.10.5]
│   └── Last Menstrual Period Date [D.10.3]
│
├── Parent Medical History [D.10.7.1.r] ── 반복 그룹
│   ├── Medical History type (자체 필드)
│   ├── Medical History Term (자체 필드, 250자)
│   ├── MedDRA Version [D.10.7.1.r.1a]  ─┐
│   ├── MedDRA Code [D.10.7.1.r.1b]      ├─ 연관
│   ├── MedDRA Term (자체 필드)           ─┘
│   ├── Start Date [D.10.7.1.r.2]
│   ├── Continuing [D.10.7.1.r.3] ──→ True 시 End Date 삭제·비활성
│   ├── End Date [D.10.7.1.r.4]
│   └── Comments [D.10.7.1.r.5]
│
├── Parent Medical History Free Text [D.10.7.2]
│
└── Parent Drug [D.10.8.r] ── 반복 그룹
    ├── Name of Drug as Reported [D.10.8.r.1]
    ├── medicinal product version [D.10.8.r.1.KR.1a] ─┐ 연관
    ├── medicinal product ID [D.10.8.r.1.KR.1b]       ─┘
    ├── MPID Version [D.10.8.r.2a] ─┐ 연관 (IDMP 확정 후)
    ├── MPID [D.10.8.r.2b]          ─┘
    ├── PhPID Version [D.10.8.r.3a] ─┐ 연관 (IDMP 확정 후)
    ├── PhPID [D.10.8.r.3b]          ─┘
    ├── Start Date [D.10.8.r.4]
    ├── End Date [D.10.8.r.5]
    ├── Indication MedDRA Version [D.10.8.r.6a] ─┐
    ├── Indication MedDRA Code [D.10.8.r.6b]     ├─ 연관
    ├── Indication MedDRA Term (자체 필드)        ─┘
    ├── Reaction MedDRA Version [D.10.8.r.7a] ─┐
    ├── Reaction MedDRA Code [D.10.8.r.7b]     ├─ 연관
    └── Reaction MedDRA Term (자체 필드)        ─┘
```

# 3. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | MedDRA 코딩 팝업 | D.10.7.1.r.1, D.10.8.r.6, D.10.8.r.7의 Version+Code+Term | 코딩 필드 클릭 |
| 2 | WHODrug/MFDS Drug 코딩 팝업 | D.10.8.r.1.KR.1a/1b | 코딩 필드 클릭 |
| 3 | Continuing → End Date 비활성 | D.10.7.1.r.3(Continuing)=Yes 시 D.10.7.1.r.4(End Date) 삭제+비활성 | Continuing 변경 시 |
| 4 | 연관 쌍 상호 필수 | Version ↔ Code 쌍, D.10.2.2a ↔ D.10.2.2b | 저장/Validation |

# 4. 정책

---

## 4.1 MedDRA 팝업 & License Expire 공통 규칙

MedDRA 코드/용어를 사용하는 필드(D.10.7.1.r.1a/b, D.10.8.r.6a/b, D.10.8.r.7a/b 및 각 자체필드 Term)에 공통 적용:

| 조건 | 동작 |
| --- | --- |
| MedDRA License 유효 | MedDRA 팝업을 통해 코드·버전·용어 입력 |
| MedDRA License Expire | Free text(자유기재)로 전환. Term 필드는 비필수, 250자 이하 검증 |

## 4.2 동적 UI 제어 — Continuing(D.10.7.1.r.3) 종속

| 조건 | 동작 |
| --- | --- |
| Continuing = True (Yes) | End Date(D.10.7.1.r.4) 값 비활성화 |
| Continuing = False (No) 또는 미입력 | End Date 활성화 |

### 4.3 IDMP 미확정 필드

MPID(D.10.8.r.2a/b), PhPID(D.10.8.r.3a/b) 필드는 IDMP 확정 후 사용 예정.

## 5. 요구사항

---

> 원문에 정의 없음

## 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
