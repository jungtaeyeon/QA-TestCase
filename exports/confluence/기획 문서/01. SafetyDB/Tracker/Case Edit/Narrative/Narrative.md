|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.28 | 최초 작성 | v1.0 | v1.0.260328 |
|  |  |  |  |  |

# 1. 개요

---

* **목적**: Case Edit 화면 중 '사례 설명(Narrative)' 섹션(ICH E2B R3 H)의 필드 구성을 정의. 사례의 임상 경과, 치료 조치, 결과 및 추가 정보를 자유 텍스트로 기술하고, 보고자의 진단명을 MedDRA 코딩하며, 다국어 번역 및 현지 언어 보고를 지원.
* **페이지 위치**: Safety > Tracker > Case Edit > Narrative

**핵심 설계 방향**:

* **사례 설명(H.1)**: 필수 필드. 임상 경과의 핵심 기술 영역.
* **Sender's Diagnosis(H.3.r)**: MedDRA 코딩을 통한 진단명/증후군 재분류. LLT + SOC 이중 용어 표시.

# 2. 출력 정보

---

## 2.1 필드 데이터

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Case Narrative Including Clinical Course, Therapeutic Measures, Outcome and Additional Relevant Information | 사례 설명 | 필수 | H.1 |  |  |
|  | Reporter's Comments | 원보고자의 의견 | 옵션 | H.2 |  |  |
| 연관 | MedDRA Version for Sender's Diagnosis / Syndrome and / or Reclassification of Reaction / Event | 진단명 MedDRA 버전 | 조건부 필수 | H.3.r.1a |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Sender's Diagnosis / Syndrome and / or Reclassification of Reaction / Event (MedDRA code) | 진단명 MedDRA 코드 | 조건부 필수 | H.3.r.1b |  | * 입력: MedDRA 팝업    + License Expire경우 자유기재​ |
| Sender's Diagnosis / Syndrome and / or Reclassification of Reaction / Event (MedDRA LLT Term) | 진단명 MedDRA LLT 용어​ | 옵션 | 자체 필드 | * 값: H.3.r.1b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업> LLT 용어    + License Expire경우 자유기재 |
| Sender's Diagnosis / Syndrome and / or Reclassification of Reaction / Event (MedDRA SOC Term) | 진단명 MedDRA SOC 용어​ | 옵션 | 자체 필드 | * 값: H.3.r.1b 에 입력된 코드의 영문 Term​ * License Expire시 비필수/ 250자 이하​ | * 입력: MedDRA 팝업> SOC 용어    + License Expire경우 자유기재 |
|  | Sender's Comments | 보고자의 의견 | 옵션 | H.4 |  |  |
|  | Case Summary and Reporter’s Comments Language | 원보고자의 현지언어 | 조건부 필수 | H.5.r.1b |  |  |
|  | Case Summary and Reporter’s Comments Text | 원보고자의 의견 | 옵션 | H.5.r.1a |  |  |

## 2.2 제안 구조

```
Narrative (사례 설명)
│
├── Case Narrative
│   ├── Case Narrative [H.1] ── 필수
│   └── Reporter's Comments [H.2]
│
├── Sender's Diagnosis [H.3.r] ── 반복 그룹
│   ├── MedDRA Version [H.3.r.1a]    ─┐
│   ├── MedDRA Code [H.3.r.1b]        │
│   ├── MedDRA LLT Term (자체 필드)   ├─ 연관
│   └── MedDRA SOC Term (자체 필드)   ─┘
│
└── Sender's Comments & Localization
    ├── Sender's Comments [H.4]
    ├── Comments Language [H.5.r.1b]
    └── Comments Text [H.5.r.1a]
```

# 3. 기능 설명

---

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| 1 | MedDRA 코딩 팝업 | H.3.r.1a/1b/LLT Term/SOC Term을 MedDRA 팝업에서 입력 | 코딩 필드 클릭 |
| 2 | LLT + SOC 이중 표시 | H.3.r.1b 코드에서 LLT Term과 SOC Term을 동시에 자동 표시 | 자동 |

## 4. 정책

---

### 4.1 MedDRA 팝업 & License Expire 공통 규칙

진단명 MedDRA 필드(H.3.r.1a/b 및 자체필드 LLT Term, SOC Term)에 적용:

| 조건 | 동작 |
| --- | --- |
| MedDRA License 유효 | MedDRA 팝업을 통해 코드·버전·LLT 용어·SOC 용어 입력 |
| MedDRA License Expire | Free text(자유기재)로 전환. Term 필드들은 비필수, 250자 이하 검증 |

## 5. 요구사항

---

> 원문에 정의 없음

## 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
