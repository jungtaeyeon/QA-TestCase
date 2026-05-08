|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.23 | 추가 검증룰 및 비고 사항 추가 | v1.0 | v1.0.260423 |
| 김나정 | 26.04.06 | 최초작성\_필드 정보 입력 | v1.0 | v1.0.260406 |

# 1. 개요

---

* **목적**: 문헌 보고 사례의 근거 자료 관리 및 임상시험/연구 정보의 체계적 데이터 바인딩을 통한 보고서 정합성 확보.
* **페이지 위치**: Tracker > Case Edit > Case > Source
* **핵심 설계 방향**:

  + **시험/연구 정보**: Study ID를 마스터 키로 사용하여 `Study Configuration` 정보와 실시간 연동 [Release 2에서 적용].
  + **조건부 활성화**: 보고 구분(C.1.3) 값에 따른 섹션 제어 로직 적용.

# 2. 출력 정보

---

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 연관 묶음 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
|  | Literature Reference(s) | 문헌 제목 | 옵션 | C.4.r.1 |  |  |
|  | Included Documents | 첨부 문서 | 옵션 | C.4.r.2 |  | * 허용 파일 형식: Application/PDF, image/jpeg, application/DICOM, text/plain Representation: e.g.B64 Compression: e.g.DF​ |
|  | Study ID | 시험/연구 ID | 조건부 필수 | 자체 필드 | * 활성 조건: 만약 C.1.3 Type of Report보고 구분 입력 값이 2가 아닌 경우라면 해당 필드 비활성화 | * 입력: Intake&Triage 에서 입력한 정보 그대로 입력하고, 수정가능. 수정시에는 Study 불러오기 클릭하면 검색창 팝업되어 재 입력 가능, 직접 수정 불가(read only)​​ [Release2에서 적용] * 처리: Org Home>Study Configuration> Study ID에 저장된 Study 정보를 연동하여 C.5.4, C.5.4.KR.1까지 자동으로 입력, 직접 수정 불가(read only)​ [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Part Information | 파트 정보 |  | 자체 필드 |  | * Study ID 정보 기입하지 않았을 경우 비활성화 * Org Home>Study Configuration에서 불러온 정보값을 입력 [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Period Information | 기간 정보 |  | 자체 필드 |  | * Study ID 정보 기입하지 않았을 경우 비활성화 * Org Home>Study Configuration에서 불러온 정보값을 입력 [Release2에서 적용] * 현재는 자유 입력으로 기재 * 다중 선택이 가능하므로, 다중 표시 |
|  | Sponsor Study Number | 시험/연구 계획서 번호 (승인받은 임상시험의 경우 임상시험 일련번호 기재 or 임상시험 계획번호 기재) | 조건부 필수 | C.5.3 | 1. 조건부 필수​ 2. 보고 구분(C.1.3)에서 Value=2 이면서, 연구 구분(C.5.4)에서 Value=1 or Value=2 인 경우에만 필수, 연구 구분(C.5.4)에서 Value=3 일 때는 입력은 가능, 필수 검증 안함​ | * Org Home>Study Configuration의 ‘Sponsor Study Number’값을 입력 [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Study Name | 시험/연구 계획서 제목 | 조건부 필수 | C.5.2 |  | * Org Home>Study Configuration에서 Study ID 의 value를 key로 찾은 Study 정보 에서 동일한 필드명 가져와서 입력​ [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Study Type Where Reaction(s) / Event(s) Were Observed | 연구 구분 | 옵션 | C.5.4 |  | * Org Home>Study Configuration에서 Study ID 의 value를 key로 찾은 Study 정보 에서 ‘Study Type’필드 값 가져와서 입력​ [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Other Studies Type | 기타 시험 상세구분 | 옵션 | C.5.4.KR.1 |  | * Org Home>Study Configuration에서 Study ID 의 value를 key로 찾은 Study 정보 에서 'Other Studies Type' 필드 값 가져와서 입력​ [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Study Registration Number | 시험/연구 등록 번호 | 조건부 필수 | C.5.1.r.1 |  | * Org Home>Study Configuration에서 Study ID 의 value를 key로 찾은 Study 정보 에서 ‘Study Registration Number’ 필드 값 가져와서 입력​ [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Study Registration Country | 시험/연구 등록 국가 | 옵션 | C.5.1.r.2 |  | * Org Home>Study Configuration에서 Study ID 의 value를 key로 찾은 Study 정보 에서 ‘Study Registration Country’ 필드 값 가져와서 입력​ [Release2에서 적용] * 현재는 자유 입력으로 기재 |
|  | Unblinding | 맹검 해제 | 조건부 필수 | 자체 필드 |  | * [Release2에서 적용], 현재는 비가시화 |
|  | Date of unblinding | 눈가림 해제일 | 조건부 필수 | 자체 필드 |  | * [Release2에서 적용], 현재는 비가시화 |
|  | Arm | 군 정보 | 조건부 필수: unblinding 필드 값이 1이 아닌 경우 Arm을 필수 입력 | 자체 필드 |  | * [Release2에서 적용], 현재는 비가시화 |

### 2.3 Blinding (Release 2 전용) — 현재 비가시화

| 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 추가 검증룰 | 비고 |
| --- | --- | --- | --- | --- | --- |
| Unblinding | 맹검 해제 | 조건부 필수 | 자체 필드 | — | [Release 2에서 적용], 현재 비가시화 |
| Date of unblinding | 눈가림 해제일 | 조건부 필수 | 자체 필드 | — | [Release 2에서 적용], 현재 비가시화 |
| Arm | 군 정보 | 조건부 필수: Unblinding 필드 값이 1이 아닌 경우 Arm 필수 입력 | 자체 필드 | — | [Release 2에서 적용], 현재 비가시화 |

## 2.4 제안 구조

```
Source
├── Literature (문헌 정보)
│   ├── Literature Reference(s) [C.4.r.1]
│   └── Included Documents [C.4.r.2]
│
└── Study Information (시험/연구 정보) ─── C.1.3 = 2일 때만 활성화
    ├── Study ID (마스터 키) ──→ Study Configuration 연동 [R2]
    │   ├── Part Information
    │   └── Period Information (다중 선택)
    ├── Sponsor Study Number [C.5.3]
    ├── Study Name [C.5.2]
    ├── Study Type [C.5.4]
    │   └── Other Studies Type [C.5.4.KR.1]
    ├── Study Registration Number [C.5.1.r.1]
    ├── Study Registration Country [C.5.1.r.2]
    └── Blinding (Release 2 전용)
        ├── Unblinding
        ├── Date of unblinding
        └── Arm
```

# 3. 기능 설명

---

> 원문에 정의 없음

# 4. 정책

---

## 4.1 섹션 활성화 로직 (C.1.3 종속성)

보고 구분 필드(C.1.3)의 입력 값에 따라 시험/연구 정보 섹션의 가시성을 제어한다.

| 조건 | 동작 |
| --- | --- |
| C.1.3 입력 값이 2 (Report from Study) | 시험/연구 정보 섹션 전체 활성화 |
| C.1.3 입력 값이 2가 아닌 경우 | 시험/연구 정보 섹션 전체 비활성화. 불필요한 데이터 입력 방지 및 보고 유형별 데이터 정합성 유지 |

## 4.2 조건부 필수 검증 규칙 (Sponsor Study Number — C.5.3)

| C.1.3 값 | C.5.4 값 | Sponsor Study Number 필수 여부 |
| --- | --- | --- |
| 2 (Report from Study) | 1 (Clinical Trial) | 필수 |
| 2 (Report from Study) | 2 (Individual Patient Use) | 필수 |
| 2 (Report from Study) | 3 (Other Studies) | 입력 가능, 필수 검증 안 함 |
| 2가 아님 | — | 비활성화 (입력 불가) |

# 5. 요구사항

---

> 원문에 정의 없음

# 6. 프로토타입 / 와이어프레임

---

> 기획자 추가 예정 — 기획안 초안 확정 후 프로토타입을 별도 제작하여 첨부합니다.
