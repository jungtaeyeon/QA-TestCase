|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.24 | 추가 검증룰, 비고 사항 추가 | v1.0 | v1.0.260406 |
| 김나정 | 26.04.06 | 최초작성\_필드 정보 입력 | v1.0 | v1.0.260406 |

## 1. 개요

---

페이지 위치: Tracker > Case Edit > Patient > Medical History

## 2. 출력 정보

---

## 2.1 필드 데이터

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
| 연관 | Relevant Medical History as Reported by the Primary Source | 원보고자가 보고한 과거 병력​ | 옵션 | 자체필드 | * 추가 검증 룰​    + 비필수로 항목값이 입력된 경우 검증​   + 입력값이 250자 이하인지 검증​ | * 기본 검증 룰: NA​ |
| Type of Condition | 병력 구분​ | 옵션 | 자체필드 | * 추가 검증 룰​    + 비필수로 항목값이 입력된 경우 검증​ | * Option 값:​ 영어만 표기    + 1= Diseases​   + 2= Conditions​   + 3= Surgical procedures​   + 4= Psychological trauma​   + 5= Risk factors​   + 6=Other​ * 기본 검증 룰: NA​ |
| MedDRA Version for Medical History | 과거 병력 MedDRA 버전 | 조건부 필수 | D.7.1.r.1a |  | * 입력: MedDRA 팝업    + License Expire 경우 자유기재​ |
| Medical History (disease / surgical procedure / etc.) (MedDRA code) | 과거 병력 MedDRA 코드 | 조건부 필수 | D.7.1.r.1b |  | * 입력: MedDRA 팝업    + License Expire 경우 자유기재​ |
| Medical History (disease / surgical procedure / etc.) (MedDRA Term) | 과거 병력 MedDRA 용어​ | 조건부 필수 | 자체필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.7.1.r.1b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ |  |
|  | Start Date | 시작일 | 옵션 | D.7.1.r.2 |  |  |
|  | Continuing | 지속여부 | 옵션 | D.7.1.r.3 |  | * Option 값:​ 영문 병기    + Yes 예​   + No 아니오​ |
|  | End Date | 종료일 | 옵션 | D.7.1.r.4 |  |  |
|  | Comments | 비고 | 옵션 | D.7.1.r.5 |  |  |
|  | Family History | 가족력 | 옵션 | D.7.1.r.6 |  |  |
|  | Text for Relevant Medical History and Concurrent Conditions (not including reaction / event) | 과거 병력 상세내용 | 조건부 필수 | D.7.2 |  | 만약 D.7.1, D.7.2에서 아무런 내용을 작성할 것이 없다면, MFDS에서 보고시 “None”을 출력 |
| 연관 | Concomitant Therapies | 병용요법 | 옵션 | D.7.3 |  | 직접 입력 또는 자동 처리: Concomitant Therapy Type 필드와 Text for Concomitant Therapy 필드에 정보가 입력되면 XML의 D.7.3의 Value를 True로 한다 |
| Concomitant Therapy Type | 병용요법 구분​ | 옵션 | - |  |  |
| Text for Concomitant Therapy | 병용요법 상세​ | 옵션 | - |  |  |
|  | Name of Drug as Reported | 의약품명 | 조건부 필수 | D.8.r.1 |  |  |
| 연관 | medicinal product version | 의약품 코드 버전 | 조건부 필수 | D.8.r.1.KR.1a |  | * 입력: WHODrug/ MFDS Drug 팝업으로 입력 & License Expire뒤에는 Free text로 검증​ * 드롭다운으로 버전 선택 |
| medicinal product ID | 의약품 코드 | 조건부 필수 | D.8.r.1.KR.1b |  | * 입력: WHODrug/ MFDS Drug 팝업으로 입력 & License Expire뒤에는 Free text로 검증​ |
|  | MPID Version Date/Number | 의약품식별자(MPID) 버전 | 조건부 필수 | D.8.r.2a |  | * IDMP 확정 후 사용​ |
|  | Medicinal Product Identifier (MPID) | 의약품식별자(MPID) | 조건부 필수 | D.8.r.2b |  | * IDMP 확정 후 사용​ |
| 연관 | PhPID Version Date/Number | 제제식별자(PhPID) 버전 | 조건부 필수 | D.8.r.3a |  | IDMP 확정 후 사용​ |
| Pharmaceutical Product Identifier (PhPID) | 제제식별자(PhPID) | 조건부 필수 | D.8.r.3b |  | IDMP 확정 후 사용​ |
|  | Start Date | 시작일 | 옵션 | D.8.r.4 |  |  |
|  | End Date | 종료일 | 옵션 | D.8.r.5 |  |  |
|  | MedDRA Version for Indication | 적응증의 MedDRA 버전 | 조건부 필수 | D.8.r.6b |  | * 입력: MedDRA 팝업    + License Expire 경우 자유기재​ * 버전 기재시 드롭다운 |
| Indication (MedDRA code) | 적응증의 MedDRA 코드 | 조건부 필수 | D.8.r.6a |  | * 입력: MedDRA 팝업    + License Expire 시 자유기재 |
| ndication (MedDRA Term) | 적응증의 MedDRA 용어​ | 조건부 필수 | 자체필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.8.r.6b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업    + License Expire 경우 자유기재​ |
| 연관 | MedDRA Version for Reaction | 약물이상반응의 MedDRA 버전 | 조건부 필수 | D.8.r.7a |  | * 입력: MedDRA 팝업    + License Expire 경우 자유기재​ |
| Reaction (MedDRA code) | 약물이상반응의 MedDRA 코드 | 조건부 필수 | D.8.r.7b |  | * 입력: MedDRA 팝업    + License Expire 경우 자유기재​ |
| Reaction (MedDRA Term) | 약물이상반응의 MedDRA 용어​ | 조건부 필수 | 자체필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.8.r.7b에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업    + License Expire 경우 자유기재​ |

## 2.2 제안 구조

```
Medical History (과거 병력 및 병용약물)
│
├── Relevant Medical History [D.7.1.r] ── 반복 그룹
│   ├── Reported Medical History (자체필드) ─┐
│   ├── Type of Condition (자체필드)         ├─ 연관
│   ├── MedDRA Version [D.7.1.r.1a]        │
│   ├── MedDRA Code [D.7.1.r.1b]           │
│   └── MedDRA Term (자체필드)              ─┘
│   ├── Start Date [D.7.1.r.2]
│   ├── Continuing [D.7.1.r.3]
│   ├── End Date [D.7.1.r.4]
│   ├── Comments [D.7.1.r.5]
│   └── Family History [D.7.1.r.6]
│
├── Medical History Free Text [D.7.2]
│
├── Concomitant Therapies [D.7.3] ── 자동 True 설정
│   ├── Concomitant Therapy Type
│   └── Text for Concomitant Therapy
│
└── Concomitant Drug [D.8.r] ── 반복 그룹
    ├── Name of Drug as Reported [D.8.r.1]
    ├── medicinal product version [D.8.r.1.KR.1a] ─┐ 연관
    ├── medicinal product ID [D.8.r.1.KR.1b]       ─┘
    ├── MPID Version [D.8.r.2a]
    ├── MPID [D.8.r.2b]
    ├── PhPID Version [D.8.r.3a] ─┐ 연관
    ├── PhPID [D.8.r.3b]          ─┘
    ├── Start Date [D.8.r.4]
    ├── End Date [D.8.r.5]
    ├── Indication MedDRA Version [D.8.r.6b]
    ├── Indication MedDRA Code [D.8.r.6a]
    ├── Indication MedDRA Term (자체필드)
    ├── Reaction MedDRA Version [D.8.r.7a] ─┐ 연관
    ├── Reaction MedDRA Code [D.8.r.7b]     │
    └── Reaction MedDRA Term (자체필드)     ─┘
```

# 3. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | MedDRA 코딩 팝업 | D.7.1.r.1, D.8.r.6, D.8.r.7의 Version+Code+Term을 MedDRA 팝업에서 입력. License Expire 시 자유기재 전환 | 코딩 필드 클릭 시 |
| 2 | WHODrug/MFDS Drug 코딩 팝업 | D.8.r.1.KR.1a/1b를 WHODrug 또는 MFDS Drug 팝업에서 입력. License Expire 시 자유기재 전환 | 코딩 필드 클릭 시 |
| 3 | D.7.3 자동 True 처리 | Concomitant Therapy Type 또는 Text에 정보 입력 시 D.7.3을 자동으로 True로 설정 | 하위 필드 입력 시 자동 |
| 4 | D.7.2 조건부 필수 | D.7.1 그룹에 아무 값도 없을 경우 D.7.2 필수 검증 활성화 | 저장/Validation 시 |
| 5 | 연관 쌍 상호 필수 | Version ↔ Code 필드 쌍에서 한쪽 입력 시 다른 쪽 필수 (총 5개 쌍) | 저장/Validation 시 |

# 4. 정책

---

## 4.1 MedDRA 팝업 & License Expire 공통 규칙

MedDRA 코드/용어를 사용하는 필드(D.7.1.r.1a/b, D.8.r.6a/b, D.8.r.7a/b 및 각 자체필드 Term)에 공통 적용:

| 조건 | 동작 |
| --- | --- |
| MedDRA License 유효 | MedDRA 팝업을 통해 코드·버전·용어 입력 |
| MedDRA License Expire | Free text(자유기재)로 전환. Term 필드는 비필수, 250자 이하 검증 |

## 4.2 WHODrug / MFDS Drug 팝업 & License Expire 규칙

의약품 코드 관련 필드(D.8.r.1.KR.1a, D.8.r.1.KR.1b)에 적용:

| 조건 | 동작 |
| --- | --- |
| License 유효 | WHODrug/MFDS Drug 팝업으로 입력 |
| License Expire | Free text로 전환하여 검증 |

## 4.3 Concomitant Therapies 자동 True 처리

| 조건 | 동작 |
| --- | --- |
| Concomitant Therapy Type 또는 Text for Concomitant Therapy에 정보 입력 | XML D.7.3 Value를 True로 설정 |

## 4.4 MFDS 보고 시 "None" 출력

| 조건 | 동작 |
| --- | --- |
| D.7.1, D.7.2 모두 내용 없음 & Destination이 MFDS | 보고 시 "None" 출력 |

## 4.5 IDMP 미확정 필드

MPID(D.8.r.2a/b), PhPID(D.8.r.3a/b) 필드는 IDMP 확정 후 사용 예정.

# 5. 요구사항

---

> 원문에 정의 없음

# 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
