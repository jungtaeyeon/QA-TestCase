|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.24 | 추가 검증룰, 비고 추가 입력 | v1.0 | v1.0.260424 |
| 김나정 | 26.04.07 | 최초작성\_필드 정보 입력 | v1.0 | v1.0.260407 |

# 1. 개요

---

**목적**: Case Edit 화면 중 '사망 정보(Death)' 섹션의 필드 구성, 코딩 연동 및 유효성 검증 규칙을 정의. 보고된 사망원인과 부검에 의한 사망원인을 구분하여 구조화된 데이터 입력을 지원.

* **페이지 위치**: Safety > Tracker > Case Edit > Patient > Death

**핵심 설계 방향**:

* **두 가지 사망원인 구분**: 보고된 사망원인(D.9.2.r — Reported) / 부검에 의한 사망원인(D.9.4.r — Autopsy-determined)을 별도 반복 그룹으로 관리.
* **연관 쌍 검증**: MedDRA Version ↔ Code, Code → Free text의 연관 필수 검증.
* **MedDRA 코딩 연동**: License 유효 시 팝업 입력, Expire 시 자유기재 전환.

# 2. 출력 정보

---

## 2.1 필드 데이터

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Date of Death | 사망일 | 옵션 | D.9.1 |  |  |
|  | Was Autopsy Done? | 부검 여부 | 조건부 필수 | D.9.3 |  | * Option 값:​ 영어 병기    + Yes 예​   + No 아니오​ |
| 연관 | MedDRA Version for Reported Cause(s) of Death | 사망원인의 MedDRA 버전 | 조건부 필수 | D.9.2.r.1a |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Reported Cause(s) of Death (MedDRA code) | 사망원인의 MedDRA 코드 | 조건부 필수 | D.9.2.r.1b |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Reported Cause(s) of Death (MedDRA Term) | 보고된 사망원인 MedDRA 용어​ | 조건부 필수 | 자체 필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.9.2.r.1b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
|  | Reported Cause(s) of Death (free text) | 사망원인 설명 | 조건부 필수 | D.9.2.r.2 |  |  |
| 연관 | MedDRA Version for Autopsy-determined Cause(s) of Death | 사망원인의 MedDRA 버전 | 조건부 필수 | D.9.4.r.1a |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Autopsy-determined Cause(s) of Death (MedDRA code) | 사망원인의 MedDRA 코드 | 조건부 필수 | D.9.4.r.1b |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Autopsy-determined Cause(s) of Death (MedDRA Term | 부검에 의한 사망원인 MedDRA 용어​ | 조건부 필수 | 자체 필드 | * 입력: MedDRA 팝업 & License Expire경우 자유기재​ * 값: D.9.4.r.1b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
|  | Autopsy-determined Cause(s) of Death (free text) | 사망원인 설명 | 조건부 필수 | D.9.4.r.2 |  |  |

## 2.4 제안 구조

```
Death (사망 정보)
│
├── Death Overview
│   ├── Date of Death [D.9.1]
│   └── Was Autopsy Done? [D.9.3]
│
├── Reported Cause(s) of Death [D.9.2.r] ── 반복 그룹
│   ├── MedDRA Version [D.9.2.r.1a]  ─┐
│   ├── MedDRA Code [D.9.2.r.1b]      ├─ 연관
│   ├── MedDRA Term (자체 필드)       ─┘
│   └── Free Text [D.9.2.r.2]
│
└── Autopsy-determined Cause(s) of Death [D.9.4.r] ── 반복 그룹
    ├── MedDRA Version [D.9.4.r.1a]  ─┐
    ├── MedDRA Code [D.9.4.r.1b]      ├─ 연관
    ├── MedDRA Term (자체 필드)       ─┘
    └── Free Text [D.9.4.r.2]
```

# 3. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | MedDRA 코딩 팝업 | D.9.2.r.1, D.9.4.r.1의 Version+Code+Term을 MedDRA 팝업에서 입력. License Expire 시 자유기재 전환 | 코딩 필드 클릭 시 |
| 2 | D.9.1 → D.9.3 조건부 필수 | 사망일(D.9.1) 입력 시 부검 여부(D.9.3) 필수 활성화 | D.9.1 값 입력 시 |
| 3 | 연관 쌍 상호 필수 | Version ↔ Code 연관 쌍 (2개 쌍), Code → Free text (2개 쌍) | 저장/Validation 시 |

# 4. 정책

---

## 4.1 MedDRA 팝업 & License Expire 공통 규칙

사망원인 MedDRA 코드/용어를 사용하는 필드(D.9.2.r.1a/b, D.9.4.r.1a/b 및 각 자체필드 Term)에 공통 적용:

| 조건 | 동작 |
| --- | --- |
| MedDRA License 유효 | MedDRA 팝업을 통해 코드·버전·용어 입력 |
| MedDRA License Expire | Free text(자유기재)로 전환. Term 필드는 비필수, 250자 이하 검증 |

# 5. 요구사항

---

| 요구사항 | 기획 방향 | 의도 | 분류 |
| --- | --- | --- | --- |
| 사망 정보 구조화 입력 | 사망일, 부검 여부, 보고된/부검 사망원인 분리 | 사망 사례의 규제 보고 요건 충족 | Requirement |

# 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
