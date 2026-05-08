# Case ID 테스트 시나리오

> **기반 RTM**: v0 (기획자 답변 v1.2 반영 2026-05-07)
> **기획서**: `exports/confluence/기획 문서/00. Common (공통 정책)/Admin (Org Admin)/ICSR Config/Case ID/Case ID.md` (v1.0.250430)
> **작성일**: 2026-05-07 | **작성 에이전트**: scenario-writer

---

## 개요

- **기능 범위**: Case ID Configuration 화면의 Case ID 번호 조합 설정 (조직 식별자, 국가코드, Year/Type of Report/Product Abbreviation/자유 텍스트/일련번호/포맷 설정), 만료 임박 알림 팝업, 자릿수 자동 확장, Import 설정, ICSR 식별자 관리 사양(C.1.1 / C.1.8.1)
- **제외 범위**: AI Convert에 Import 설정 적용 (추후 개발 예정 — REQ-EX-001)
- **주요 용어**:
  - **Case ID**: `[설정된 번호 조합]` — Tracker 및 Case Edit에 표시되는 식별자
  - **C.1.1**: 보고자 관리번호 (Report Level, ICSR 보고서에 기입)
  - **C.1.8.1**: 고유식별 보고자 관리번호
  - **C.1.4**: 최초 발생인지일 (Year 설정의 참조 필드)
  - **Destination**: 보고처 (국가코드 결정 시점 기준)
  - **Zero-padding**: 선택 자릿수만큼 번호 앞에 '0' 채움

---

## 명세 검증 트리

### 트리 구조

- **[대분류] 기본 구조 및 조직 식별자**
  - [중분류] 조직 식별자 입력
    - 유효 입력(1~10자, 영문/숫자, 대소문자 구분) 시 Case ID 반영 [SC-CASEID-001] ✅
    - 길이 경계값 위반(0자·11자 이상) 시 오류 처리 [SC-CASEID-002] ✅
    - 허용 문자 외(특수문자·한글 등) 입력 시 차단 [SC-CASEID-003] ✅
  - [중분류] 국가코드 결정 로직
    - 4단계 우선순위 로직(Reporter Primary→First→Event Country Primary→First→KR) [SC-CASEID-004] ✅
  - [중분류] Case ID 자동 부여 및 표시
    - 케이스 생성 시 자동 부여, Case Edit·Tracker에 번호 조합 표시 [SC-CASEID-005] ✅
  - [중분류] ID 재사용 방지
    - 삭제된 케이스 일련번호 이후 신규 케이스에 재사용 금지 [SC-CASEID-006] ✅

- **[대분류] 번호 조합 구성 요소 설정**
  - [중분류] Year 설정
    - 2-digit(YY) 설정, 매년 1월 1일 00:00:00 리셋 [SC-CASEID-007] ✅
    - 4-digit(YYYY) 설정, 매년 1월 1일 00:00:00 리셋 [SC-CASEID-008] ✅
    - N/A 설정, 연도 미표기 누적 증가 [SC-CASEID-009] ✅
    - Year 툴팁 문구 표시 [SC-CASEID-010] ✅
    - Year 설정 변경 시 이후 케이스만 적용, 기존 케이스 불변 [SC-CASEID-011] ✅
  - [중분류] Type of Report 설정
    - 4개 코드 매핑 정확성(SP/RS/OT/UN) [SC-CASEID-012] ✅
    - Null/미입력 케이스에서 UN 기본 적용 [SC-CASEID-013] ✅
    - 체크 시 표시 문구 노출 확인 [SC-CASEID-014] ✅
  - [중분류] Product Abbreviation 설정
    - 약어 참조 및 미등록 시 UNK 표시 [SC-CASEID-015] ✅
    - 활성화 조건(제품 불러오기 포함 케이스만) [SC-CASEID-016] ✅
    - Suspect 자사 제품 2개 이상 시 첫 번째 약어 표시 [SC-CASEID-017] ✅
    - Product Config 약어 삭제 시 기존 케이스 불변, 신규·Import만 반영 [SC-CASEID-018] ✅
  - [중분류] 자유 텍스트 설정
    - 유효 입력(영문/숫자, 최대 6글자) 및 드래그앤드롭 배치 [SC-CASEID-019] ✅
    - 허용 문자 외·최대 길이(7글자 이상) 초과 시 차단 [SC-CASEID-020] ✅
    - 최솟값(0글자 허용 여부) 및 빈값 저장 처리 [SC-CASEID-021] ⏸️ (기획자 확인 필요 — MISSING-010)
  - [중분류] 일련번호 자릿수 설정
    - 3~9자리 선택 시 Zero-padding 적용 [SC-CASEID-022] ✅
    - 자릿수 변경 시 이후 케이스만 적용, 기존 케이스 소급 없음 [SC-CASEID-023] ✅
  - [중분류] 일련번호 시작점 설정
    - 시작 번호 기본값 1, 빈값 커서아웃 시 강제 1 기입 [SC-CASEID-024] ✅
    - 사용자 지정 시작 번호로 카운팅, 저장 후 첫 케이스 즉시 적용 [SC-CASEID-025] ✅
    - 최후 번호 검증(이미 생성된 최후 번호보다 커야 함) [SC-CASEID-026] ✅
    - 시작 번호 제한([최대 생성 가능 숫자 - 400] 초과 불가) [SC-CASEID-027] ✅

- **[대분류] 포맷 설정 (Drag & Drop)**
  - 칩 추가 시 해당 칩 설정 영역 활성화 [SC-CASEID-028] ✅
  - Chip 구성 요소(YY/YYYY/######/TR/PRD/TXT) 표시 및 선택 [SC-CASEID-029] ✅
  - 칩 드래그앤드롭 순서 변경, Preview 실시간 반영 [SC-CASEID-030] ✅
  - 칩 x 클릭 시 제거, 설정값 세션 내에서만 유지(새로고침 시 초기화) [SC-CASEID-031] ✅

- **[대분류] Case ID 만료 경고 및 자동 확장**
  - [중분류] 만료 임박 알림 팝업
    - 남은 번호 100개 이하 시 케이스 생성 완료 시점에 팝업 노출 [SC-CASEID-032] ✅
    - 팝업 노출 위치(Manual Intake/Import 완료 시, 모든 화면) [SC-CASEID-033] ✅
    - 팝업 내용(현재 마지막 Case ID, 최대값, New Case ID) [SC-CASEID-034] ✅
    - Confirm 클릭 시 팝업 닫힘, 다음 로그인 시 재노출 [SC-CASEID-035] ✅
    - "오늘 하루 보지 않기" + Confirm 시 24시간 미노출 [SC-CASEID-036] ✅
    - 24시간 억압 중 자릿수 초과 전환 시 별도 알림 없이 팝업 재노출 가능 [SC-CASEID-037] ✅
    - 새 자릿수 체계(1XXXXX...) 전환 후 기존 팝업 자동 미노출 [SC-CASEID-038] ✅
  - [중분류] 자릿수 자동 확장
    - 최대 자릿수 초과 시 한 자리 자동 추가(99999→100000) [SC-CASEID-039] ✅

- **[대분류] Import 설정 및 식별자 동기화**
  - Import 옵션 A: C.1.1 신규 부여, C.1.8.1 파일값 유지 [SC-CASEID-040] ✅
  - Import 옵션 A + C.1.8.1 Null 케이스 ➖ (기획자 답변: Null 케이스 없음 — REQ-046)
  - Import 옵션 B: C.1.1/C.1.8.1 파일값 유지, C.1.1 중복 시 에러 반환 [SC-CASEID-041] ✅
  - Import 적용 범위(Import 기능을 통한 케이스 생성 시에만) [SC-CASEID-042] ✅
  - C.1.8.1 Null 시 C.1.1 자동 복사, 기존 값 있으면 미적용 [SC-CASEID-043] ✅

- **[대분류] ICSR 식별자 관리 사양서**
  - [중분류] Case vs Report Level 노출
    - Case Level 일련번호 표시 / Report Level 국가-조직-일련번호 표시 [SC-CASEID-044] ✅
  - [중분류] 생성 유형별 식별자 부여
    - 매뉴얼 케이스: C.1.1 = C.1.8.1, Destination 확정 시 국가코드 결정 [SC-CASEID-045] ✅
    - Destination 미확정 상태에서 C.1.1 공란 표시 [SC-CASEID-046] ✅
    - Import 케이스: C.1.1 Destination 확정 시 신규 부여(옵션A = Initial), C.1.8.1 파일값 유지 [SC-CASEID-047] ✅
  - [중분류] 식별자 수정 및 변경 정책
    - 식별자 부여 즉시 어떤 상태에서도 수동 수정 절대 불가 [SC-CASEID-048] ✅
    - Approval 이후 C.1.1/C.1.8.1 수정 버튼 비표시, 안내 문구 표시 [SC-CASEID-049] ✅

---

### 커버리지 요약

| 대분류 | 전체 | ✅ 연결 | ⏸️ 보류 | ➖ 제외 | ❌ 미작성 | 처리율 | 완료율 |
|-------|------|--------|--------|-------|---------|-------|-------|
| 기본 구조 및 조직 식별자 | 6 | 6 | 0 | 0 | 0 | 100% | 100% |
| 번호 조합 구성 요소 설정 | 21 | 20 | 1 | 0 | 0 | 100% | 100% |
| 포맷 설정 | 4 | 4 | 0 | 0 | 0 | 100% | 100% |
| Case ID 만료 경고 및 자동 확장 | 8 | 8 | 0 | 0 | 0 | 100% | 100% |
| Import 설정 및 식별자 동기화 | 5 | 4 | 0 | 1 | 0 | 100% | 100% |
| ICSR 식별자 관리 사양서 | 6 | 6 | 0 | 0 | 0 | 100% | 100% |
| **합계** | **50** | **48** | **1** | **1** | **0** | **100%** | **100%** |

> 처리율 = (✅ + ⏸️) / (전체 − ➖) × 100 = 49/49 = **100%**
> 완료율 = ✅ / (전체 − ➖ − ⏸️) × 100 = 48/48 = **100%**

**게이트 판정: ⚠️ 조건부 PASS** — ❌ 0건, ⏸️ 1건(SC-CASEID-021, MISSING-010 미해결)

---

### REQ 매핑율

| 지표 | 값 |
|------|-----|
| 전체 REQ 수 | 57건 (REQ-001~REQ-057) + 제외 1건 (REQ-EX-001) |
| 제외 REQ 수 | 2건 (REQ-EX-001 TBD, REQ-046 N/A — Null 케이스 없음) |
| 매핑 대상 REQ 수 | 56건 |
| 시나리오 매핑 완료 | 56건 (✅ 55건 + ⏸️ 1건) |
| 미매핑 (사유 기록) | 0건 |
| **REQ 매핑율** | **56/56 × 100 = 100%** |

---

## 시나리오 목록

| ID | 우선순위 | 관점 | 기법 | 시나리오 제목 | 검증 목적 | 근거 | 관련 REQ | 비고 |
|----|---------|------|------|--------------|----------|------|---------|------|
| SC-CASEID-001 | High | Data | 경계값분석 | 조직 식별자 유효 입력(1~10자, 영문/숫자, 대소문자 구분) 시 Case ID에 정상 반영된다 | 유효 범위 입력값이 Case ID에 정확히 반영되는지 검증 | 기획서 §기본 구조 및 국가 코드 로직 | REQ-011, REQ-003 | |
| SC-CASEID-002 | Medium | Data | 경계값분석 | 조직 식별자 길이 경계값 위반(0자·11자 이상) 시 오류가 발생한다 | 최소(1자)·최대(10자) 경계 외 입력 오류 처리 검증 | 기획서 §기본 구조 및 국가 코드 로직 | REQ-011 | |
| SC-CASEID-003 | Medium | Data | 동등분할 | 조직 식별자에 허용 문자 외(특수문자·한글 등) 입력 시 입력이 차단된다 | 영문/숫자 외 문자 차단 정책 검증 | 기획서 §개요 및 정책, §기본 구조 | REQ-003, REQ-011 | |
| SC-CASEID-004 | Critical | Business | 결정테이블 | 국가코드 결정 4단계 우선순위 로직이 순서대로 적용된다 | Reporter Primary→First→Event Country Primary→First→KR 순서 정확성 검증 | 기획서 §기본 구조 및 국가 코드 로직 | REQ-006, REQ-007, REQ-008, REQ-009, REQ-010 | |
| SC-CASEID-005 | High | Functional | 유스케이스 | 케이스 생성 시 Case ID가 자동 부여되어 Case Edit·Tracker에 번호 조합만 표시된다 | 자동 채번 기능 및 표시 위치 검증 | 기획서 §Case ID의 개념 | REQ-001, REQ-002, REQ-005 | |
| SC-CASEID-006 | High | Business | 도메인리스크 | 삭제된 케이스의 일련번호가 이후 신규 케이스에 재사용되지 않는다 | ID 재사용 방지 정책 검증 (ICSR 규제 요건) | 기획서 §개요 및 정책 | REQ-004 | |
| SC-CASEID-007 | High | Functional | 동등분할 | Year 2-digit 설정 시 C.1.4 연도 뒤 두 자리(YY) 형식으로 표기되고 매년 1월 1일 00:00:00에 일련번호가 리셋된다 | 2-digit 표기 및 연간 리셋 동작 검증 | 기획서 §Year (연도 표시 및 리셋 정책) | REQ-012 | |
| SC-CASEID-008 | High | Functional | 동등분할 | Year 4-digit 설정 시 C.1.4 연도 전체 네 자리(YYYY) 형식으로 표기되고 매년 1월 1일 00:00:00에 일련번호가 리셋된다 | 4-digit 표기 및 연간 리셋 동작 검증 | 기획서 §Year (연도 표시 및 리셋 정책) | REQ-013 | |
| SC-CASEID-009 | High | Functional | 동등분할 | Year N/A 설정 시 연도가 포함되지 않고 초기화 없이 일련번호가 누적 증가한다 | 연도 미표기 및 전체 누적 채번 동작 검증 | 기획서 §Year (연도 표시 및 리셋 정책) | REQ-014 | |
| SC-CASEID-010 | Low | Functional | 유스케이스 | Year 설정란 옆 툴팁 클릭 시 "연도 선택 시 매년 초 00001 초기화, N/A 선택 시 누적" 안내 문구가 표시된다 | 툴팁 문구 정확성 검증 | 기획서 §Year (연도 표시 및 리셋 정책) | REQ-015 | |
| SC-CASEID-011 | High | Business | 데이터생명주기분석 | Year 설정 변경 이후 생성된 케이스부터 새 설정이 적용되고, 기존 케이스의 Case ID는 변경되지 않는다 | 설정 변경의 소급 적용 방지 검증 | 기획서 §Year / 기획자 답변 MISSING-002 | REQ-016 | |
| SC-CASEID-012 | High | Business | 결정테이블 | 케이스 Type of Report 값에 따라 올바른 구분자(Spontaneous→SP, Report from Study→RS, Other→OT, Not Available→UN)가 Case ID에 자동 추가된다 | 4개 코드 매핑 정확성 검증 | 기획서 §Type of Report (보고 구분) 추가 | REQ-017 | |
| SC-CASEID-013 | Medium | Business | 오류추정 | Type of Report 미입력 또는 Null 케이스에서 UN이 기본 구분자로 적용된다 | Null 케이스 폴백 처리 검증 | 기획자 답변 MISSING-003 | REQ-019 | |
| SC-CASEID-014 | Low | Functional | 유스케이스 | Type of Report 칩 추가 시 "체크 시 케이스의 Type of Report 값에 따라 구분자가 Case ID에 자동 추가됩니다." 문구가 표시된다 | 표시 문구 정확성 검증 | 기획서 §Type of Report (보고 구분) 추가 | REQ-018 | |
| SC-CASEID-015 | High | Business | 동등분할 | PRD 칩 활성화 시 Admin Product Config에 등록된 약어가 참조되며, 미등록 시 UNK가 표시된다 | 약어 참조 정확성 및 UNK fallback 검증 | 기획서 §Product Abbreviation 추가 | REQ-020 | |
| SC-CASEID-016 | Medium | Business | 결정테이블 | PRD 칩은 케이스에 '제품 불러오기'를 통해 제품 정보가 포함된 경우에만 활성화된다 | 활성화 조건 검증 | 기획서 §Product Abbreviation 추가 | REQ-021 | |
| SC-CASEID-017 | Medium | Business | 동등분할 | Suspect 자사 제품이 2개 이상인 경우 입력 순서 기준 첫 번째 제품의 약어가 Case ID에 표시된다 | 다중 제품 시 첫 번째 약어 선택 기준 검증 | 기획서 §Product Abbreviation 추가 / 기획자 답변 CONFIRM-002 | REQ-022 | |
| SC-CASEID-018 | High | Business | 데이터생명주기분석 | Product Config 약어 삭제/변경 후 기존 케이스 Case ID는 불변이며, 신규·Import 케이스에만 변경 내용이 반영된다 | 약어 변경의 기존 데이터 불변 원칙 검증 | 기획자 답변 MISSING-012 | REQ-023 | |
| SC-CASEID-019 | Medium | Functional | 유스케이스 | 자유 텍스트 유효 입력(영문/숫자, 최대 6글자) 후 드래그앤드롭으로 원하는 위치에 배치하면 Case ID에 반영된다 | 자유 텍스트 입력 및 배치 기능 검증 | 기획서 §자유 텍스트 추가 | REQ-024, REQ-026 | |
| SC-CASEID-020 | Medium | Data | 경계값분석 | 자유 텍스트에 허용 문자 외 입력 또는 7글자 이상 입력 시 차단된다 | 허용 문자 위반 및 최대 길이 초과 차단 검증 | 기획서 §자유 텍스트 추가 | REQ-003, REQ-024 | |
| SC-CASEID-021 | Medium | Data | 경계값분석 | 자유 텍스트 미입력 상태로 저장 시 처리 방식이 기획서에 정의된 정책에 따른다 | 최솟값(0글자 허용 여부) 및 빈값 저장 처리 정책 검증 | 기획자 답변 MISSING-010 미해결 | REQ-025 | ⏸️ TC보류 |
| SC-CASEID-022 | High | Functional | 경계값분석 | 일련번호 자릿수를 3~9자리 중 선택하면 해당 자릿수만큼 Zero-padding이 적용된다 | 자릿수별 Zero-padding 정확성 검증 | 기획서 §일련번호 자릿수 설정 | REQ-027 | |
| SC-CASEID-023 | High | Business | 데이터생명주기분석 | 일련번호 자릿수 변경 후 이후 생성 케이스부터 새 자릿수가 적용되고, 기존 케이스는 변경되지 않는다 | 자릿수 변경 소급 적용 방지 검증 | 기획서 §일련번호 자릿수 설정 | REQ-028 | |
| SC-CASEID-024 | Medium | Functional | 유스케이스 | 시작 번호 필드의 기본값이 1이며, 빈값 상태에서 커서아웃 시 강제로 1이 기입된다 | 기본값 자동 설정 동작 검증 | 기획서 §시작 번호 설정 | REQ-029 | |
| SC-CASEID-025 | High | Business | 유스케이스 | 사용자가 지정한 시작 번호부터 카운팅이 시작되며, 설정 저장 후 생성되는 첫 번째 케이스에 즉시 적용된다 | 사용자 지정 시작점 설정 및 즉시 적용 검증 | 기획서 §시작 번호 설정 | REQ-030 | |
| SC-CASEID-026 | High | Business | 경계값분석 | Case ID 생성 시 동일 조합 이력에서 이미 생성된 최후 번호보다 큰 번호부터 생성된다 | 최후 번호 검증 규칙 정확성 검증 | 기획서 §최후 번호 검증 규칙 | REQ-031 | |
| SC-CASEID-027 | High | Business | 경계값분석 | 시작 번호를 [최대 생성 가능 숫자 - 400]을 초과하여 설정하면 차단된다 | 시작 번호 설정 상한 임계치 검증 | 기획서 §시작 번호 설정 제한 정책 / 기획자 답변 CONFIRM-003(보류) | REQ-032 | [확인 필요] |
| SC-CASEID-028 | High | Functional | 결정테이블 | 포맷 설정 영역에서 칩을 추가하면 해당 칩의 하단 설정 영역이 활성화된다 | 칩별 설정 영역 활성화 조건 검증 | 기획서 §포맷 설정 및 인터랙션 / 기획자 답변 MISSING-004 | REQ-033 | |
| SC-CASEID-029 | Medium | Functional | 동등분할 | 포맷 설정 영역에 YY/YYYY/######/TR/PRD/TXT Chip 구성 요소가 표시되고 선택 가능하다 | Chip 구성 요소 전체 표시 및 동작 검증 | 기획서 §포맷 설정 및 인터랙션 | REQ-034 | |
| SC-CASEID-030 | Medium | Functional | 유스케이스 | 포맷 설정 영역에서 칩을 드래그앤드롭으로 순서 변경하면 상단 Case ID Preview에 실시간으로 반영된다 | Drag&Drop 순서 변경 및 Preview 실시간 반영 검증 | 기획서 §포맷 설정 및 인터랙션 | REQ-035 | |
| SC-CASEID-031 | Medium | Functional | 유스케이스 | 칩 x 클릭 시 칩이 제거되고 설정 영역이 비활성화되며, 이전 설정값은 세션 내에서만 유지되고 새로고침 시 초기화된다 | 칩 제거 및 설정값 세션 유지 범위 검증 | 기획서 §포맷 설정 및 인터랙션 / 기획자 답변 MISSING-005 | REQ-036 | |
| SC-CASEID-032 | High | Business | 경계값분석 | 남은 번호가 100개 이하가 되는 시점에 Case ID가 최종 부여된 순간 만료 임박 팝업이 노출된다 | 팝업 노출 임계치(100개) 및 시점 정확성 검증 | 기획서 §Case ID 만료 임박 알림 | REQ-037 | |
| SC-CASEID-033 | High | Functional | 유스케이스 | 만료 임박 팝업이 Case ID Configuration 화면이 아닌 Manual Intake·Import 케이스 생성 완료 시점에, 어떤 화면에서도 노출된다 | 팝업 노출 위치 정확성 검증 | 기획서 §ID 팝업 표시 시점 | REQ-038 | |
| SC-CASEID-034 | High | Functional | 유스케이스 | 만료 임박 팝업에 현재 마지막으로 부여된 Case ID, 최대값, 자릿수 확장 후 첫 번째 New Case ID가 정확히 표시된다 | 팝업 내용 정확성 검증 | 기획서 §팝업 노출 조건 / 기획자 답변 MISSING-007 | REQ-039 | |
| SC-CASEID-035 | Medium | Functional | 상태전이 | Confirm 클릭 시 팝업이 닫히며, 해당 사용자의 다음 로그인 시 팝업이 다시 노출된다 | Confirm 클릭 후 팝업 상태 전이 검증 | 기획서 §사용자 인터랙션 및 제어 | REQ-040 | |
| SC-CASEID-036 | Medium | Business | 상태전이 | "오늘 하루 보지 않기" 체크 후 Confirm 클릭 시 24시간 동안 팝업이 노출되지 않는다 | 24시간 억압 기능 검증 | 기획서 §사용자 인터랙션 및 제어 | REQ-041 | |
| SC-CASEID-037 | Medium | Business | 오류추정 | "오늘 하루 보지 않기" 24시간 억압 기간 중 자릿수가 초과되어 자동 확장으로 전환될 경우 별도 알림 없이 24시간 내 팝업이 재노출될 수 있다 | 억압 중 자릿수 초과 전환 시 처리 검증 | 기획자 답변 MISSING-008 | REQ-042 | |
| SC-CASEID-038 | Medium | Business | 상태전이 | 일련번호가 완전히 초과되어 새로운 자릿수 체계(1XXXXX... 형식)로 전환된 경우 기존 만료 임박 팝업이 자동으로 미노출된다 | 번호 체계 전환 후 팝업 자동 중단 검증 | 기획서 §사용자 인터랙션 및 제어 | REQ-043 | |
| SC-CASEID-039 | High | Business | 상태전이 | 설정된 최대 자릿수를 초과하는 케이스 생성 시 자릿수가 한 자리 자동 추가되어 번호가 연속으로 부여된다(예: 99999→100000) | 자릿수 자동 확장 동작 및 연속성 검증 | 기획서 §Case ID 자릿수 자동 확장 | REQ-044 | |
| SC-CASEID-040 | High | Business | 유스케이스 | Import 옵션 A 선택 시 C.1.1은 시스템 규칙에 따라 신규 부여되고 C.1.8.1은 파일 내 값이 유지된다 | Import 옵션 A 처리 방식 정확성 검증 | 기획서 §Import 설정 | REQ-045 | |
| SC-CASEID-041 | Critical | Business | 결정테이블 | Import 옵션 B 선택 시 C.1.1·C.1.8.1 모두 파일값이 유지되며, C.1.1 중복 발생 시 에러가 반환된다 | 옵션 B 처리 및 중복 C.1.1 에러 반환 검증 | 기획자 답변 CONFLICT-001 | REQ-047 | |
| SC-CASEID-042 | Medium | Business | 동등분할 | Import 설정(옵션 A/B)은 Import 기능을 통해 생성된 케이스에만 적용된다 | Import 적용 범위 경계 검증 | 기획서 §Import 설정 | REQ-048 | |
| SC-CASEID-043 | High | Business | 결정테이블 | C.1.8.1이 Null인 경우 C.1.1 값이 C.1.8.1에 자동 복사되며, C.1.8.1에 기존 값이 있는 경우에는 복사가 적용되지 않는다 | C.1.8.1 자동 복사 조건 검증 | 기획서 §C.1.8.1이 없을 때 C.1.1 값을 그대로 사용 | REQ-049 | |
| SC-CASEID-044 | High | Functional | 유스케이스 | Case Level(Tracker, Case Edit)에는 일련번호 형식만 표시되고, Report Level(C.1.1, C.1.8.1)에는 [국가]-[조직]-[일련번호] 형식으로 표시된다 | 노출 레벨별 식별자 형식 정확성 검증 | 기획서 §Case vs Report Identifier 노출 사양 | REQ-050, REQ-051 | |
| SC-CASEID-045 | High | Flow | 데이터생명주기분석 | 매뉴얼 케이스 생성 시 C.1.1과 C.1.8.1이 동일하게 부여되며, Destination 확정 시점에 국가코드가 결정되어 [국가]-[조직]-[일련번호] 형식으로 기입된다 | 매뉴얼 케이스 식별자 부여 흐름 검증 | 기획서 §매뉴얼 케이스 생성 (Initial) | REQ-052 | |
| SC-CASEID-046 | Medium | Business | 도메인리스크 | Destination이 미확정된 Draft 케이스에서 C.1.1 필드가 공란으로 표시된다 | Destination 미확정 시 C.1.1 표시 방식 검증 | 기획자 답변 MISSING-006 (잠정) | REQ-053 | [확인 필요] |
| SC-CASEID-047 | High | Flow | 데이터생명주기분석 | Import 케이스(옵션 A)에서 C.1.1은 Destination 확정 시 신규 부여(= Initial 사례)되고, C.1.8.1은 파일 내 기존 값이 유지된다 | Import 케이스 식별자 부여 로직 검증 | 기획서 §데이터 인입 / 기획자 답변 CONFLICT-002 | REQ-054 | |
| SC-CASEID-048 | Critical | Non-Functional | 도메인리스크 | 식별자(C.1.1/C.1.8.1)가 부여된 이후 어떤 상태에서도 사용자가 수동으로 수정할 수 없다 | 식별자 불변 원칙(ICSR 데이터 무결성) 검증 | 기획서 §식별자 수정 및 변경 정책 / 기획자 답변 CONFLICT-003 | REQ-055 | |
| SC-CASEID-049 | Critical | Non-Functional | 상태전이 | Approval 상태 이후 C.1.1·C.1.8.1 필드에서 수정 버튼이 비표시되고 "Approval 상태 이후로는 … 수정이 불가합니다." 안내 문구가 표시된다 | Approval 후 UI 수정 불가 처리 및 문구 정확성 검증 | 기획서 §C.1.1 변경 시점 | REQ-056, REQ-057 | |

---

## TC 매핑 상태

| 시나리오 ID | 시나리오 제목 요약 | TC ID 범위 | TC 작성 상태 |
|------------|----------------|-----------|-------------|
| SC-CASEID-001 | 조직 식별자 유효 입력 → Case ID 반영 | TC-CASEID-001-001~003 | ✅ 완료 |
| SC-CASEID-002 | 조직 식별자 길이 경계값 위반 오류 | TC-CASEID-002-001~002 | ✅ 완료 |
| SC-CASEID-003 | 조직 식별자 허용 문자 외 차단 | TC-CASEID-003-001~002 | ✅ 완료 |
| SC-CASEID-004 | 국가코드 4단계 우선순위 로직 | TC-CASEID-004-001~005 | ✅ 완료 |
| SC-CASEID-005 | Case ID 자동 부여 및 표시 위치 | TC-CASEID-005-001~003 | ✅ 완료 |
| SC-CASEID-006 | ID 재사용 방지 | TC-CASEID-006-001~002 | ✅ 완료 |
| SC-CASEID-007 | Year 2-digit 설정 및 연간 리셋 | TC-CASEID-007-001~002 | ✅ 완료 |
| SC-CASEID-008 | Year 4-digit 설정 및 연간 리셋 | TC-CASEID-008-001~002 | ✅ 완료 |
| SC-CASEID-009 | Year N/A 설정, 누적 증가 | TC-CASEID-009-001 | ✅ 완료 |
| SC-CASEID-010 | Year 툴팁 문구 표시 | TC-CASEID-010-001 | ✅ 완료 |
| SC-CASEID-011 | Year 설정 변경 소급 없음 | TC-CASEID-011-001~002 | ✅ 완료 |
| SC-CASEID-012 | Type of Report 4개 코드 매핑 | TC-CASEID-012-001~004 | ✅ 완료 |
| SC-CASEID-013 | Type of Report Null → UN 기본 적용 | TC-CASEID-013-001 | ✅ 완료 |
| SC-CASEID-014 | Type of Report 표시 문구 | TC-CASEID-014-001 | ✅ 완료 |
| SC-CASEID-015 | Product Abbreviation 약어 참조·UNK fallback | TC-CASEID-015-001~002 | ✅ 완료 |
| SC-CASEID-016 | Product Abbreviation 활성화 조건 | TC-CASEID-016-001~002 | ✅ 완료 |
| SC-CASEID-017 | Suspect 제품 2개 이상 → 첫 번째 약어 | TC-CASEID-017-001 | ✅ 완료 |
| SC-CASEID-018 | Product Config 약어 삭제 → 기존 케이스 불변 | TC-CASEID-018-001~002 | ✅ 완료 |
| SC-CASEID-019 | 자유 텍스트 유효 입력·드래그앤드롭 배치 | TC-CASEID-019-001~002 | ✅ 완료 |
| SC-CASEID-020 | 자유 텍스트 허용 문자 위반·최대 길이 초과 차단 | TC-CASEID-020-001~002 | ✅ 완료 |
| SC-CASEID-021 | 자유 텍스트 최솟값·빈값 저장 처리 | - | ⏸️ TC 작성 보류 (MISSING-010 미해결) |
| SC-CASEID-022 | 일련번호 자릿수 선택·Zero-padding | TC-CASEID-022-001~002 | ✅ 완료 |
| SC-CASEID-023 | 자릿수 변경 소급 없음 | TC-CASEID-023-001~002 | ✅ 완료 |
| SC-CASEID-024 | 시작 번호 기본값 1·강제 기입 | TC-CASEID-024-001~002 | ✅ 완료 |
| SC-CASEID-025 | 사용자 지정 시작 번호·즉시 적용 | TC-CASEID-025-001~002 | ✅ 완료 |
| SC-CASEID-026 | 최후 번호 검증 | TC-CASEID-026-001~002 | ✅ 완료 |
| SC-CASEID-027 | 시작 번호 설정 제한([최대-400]) | TC-CASEID-027-001~002 | ✅ 완료 |
| SC-CASEID-028 | 포맷 설정 칩 추가 → 설정 영역 활성화 | TC-CASEID-028-001~002 | ✅ 완료 |
| SC-CASEID-029 | Chip 구성 요소 표시·선택 | TC-CASEID-029-001 | ✅ 완료 |
| SC-CASEID-030 | 칩 드래그앤드롭·Preview 실시간 반영 | TC-CASEID-030-001 | ✅ 완료 |
| SC-CASEID-031 | 칩 x 클릭 제거·설정값 세션 유지 | TC-CASEID-031-001~003 | ✅ 완료 |
| SC-CASEID-032 | 만료 임박 팝업 노출 임계치 | TC-CASEID-032-001~002 | ✅ 완료 |
| SC-CASEID-033 | 만료 팝업 노출 위치 | TC-CASEID-033-001~003 | ✅ 완료 |
| SC-CASEID-034 | 만료 팝업 내용 표시 | TC-CASEID-034-001 | ✅ 완료 |
| SC-CASEID-035 | Confirm 클릭 닫힘·다음 로그인 재노출 | TC-CASEID-035-001~002 | ✅ 완료 |
| SC-CASEID-036 | 오늘 하루 보지 않기·24시간 미노출 | TC-CASEID-036-001~002 | ✅ 완료 |
| SC-CASEID-037 | 24시간 억압 중 자릿수 초과·팝업 재노출 | TC-CASEID-037-001~002 | ✅ 완료 |
| SC-CASEID-038 | 새 자릿수 체계 전환 후 팝업 자동 미노출 | TC-CASEID-038-001 | ✅ 완료 |
| SC-CASEID-039 | 자릿수 자동 확장(99999→100000) | TC-CASEID-039-001~002 | ✅ 완료 |
| SC-CASEID-040 | Import 옵션 A: C.1.1 신규·C.1.8.1 유지 | TC-CASEID-040-001~002 | ✅ 완료 |
| SC-CASEID-041 | Import 옵션 B: 파일값 유지·중복 에러 | TC-CASEID-041-001~002 | ✅ 완료 |
| SC-CASEID-042 | Import 적용 범위 | TC-CASEID-042-001~002 | ✅ 완료 |
| SC-CASEID-043 | C.1.8.1 Null → C.1.1 자동 복사 | TC-CASEID-043-001~002 | ✅ 완료 |
| SC-CASEID-044 | Case Level·Report Level 식별자 형식 표시 | TC-CASEID-044-001~002 | ✅ 완료 |
| SC-CASEID-045 | 매뉴얼 케이스 C.1.1=C.1.8.1·국가코드 결정 | TC-CASEID-045-001~002 | ✅ 완료 |
| SC-CASEID-046 | Destination 미확정 → C.1.1 공란 | TC-CASEID-046-001 | ✅ 완료 |
| SC-CASEID-047 | Import 케이스 식별자 부여 로직 | TC-CASEID-047-001~002 | ✅ 완료 |
| SC-CASEID-048 | 식별자 부여 즉시 수정 절대 불가 | TC-CASEID-048-001~003 | ✅ 완료 |
| SC-CASEID-049 | Approval 이후 수정 버튼 비표시·안내 문구 | TC-CASEID-049-001~003 | ✅ 완료 |

---

## TC 커버리지

| 대분류 | 전체 | ✅ TC 연결 | ⏸️ 보류 | ➖ 제외 | ❌ 미작성 | 처리율 | 완료율 |
|-------|------|----------|--------|-------|---------|-------|-------|
| 기본 구조 및 조직 식별자 | 6 | 6 | 0 | 0 | 0 | 100% | 100% |
| 번호 조합 구성 요소 설정 | 21 | 20 | 1 | 0 | 0 | 100% | 100% |
| 포맷 설정 | 4 | 4 | 0 | 0 | 0 | 100% | 100% |
| Case ID 만료 경고 및 자동 확장 | 8 | 8 | 0 | 0 | 0 | 100% | 100% |
| Import 설정 및 식별자 동기화 | 5 | 4 | 0 | 1 | 0 | 100% | 100% |
| ICSR 식별자 관리 사양서 | 6 | 6 | 0 | 0 | 0 | 100% | 100% |
| **합계** | **50** | **48** | **1** | **1** | **0** | **100%** | **100%** |

> TC 명세 처리율 = (✅ + ⏸️) / (전체 − ➖) × 100 = 49/49 = **100%**
> TC 작성 완료율 = ✅ / (전체 − ➖ − ⏸️) × 100 = 48/48 = **100%**

**TC 게이트 판정: ⚠️ 조건부 PASS** — ❌ 0건, ⏸️ 1건 (SC-CASEID-021, MISSING-010 미해결)

> TC 통계: 총 97건 | Smoke 12건(12.4%) | E2E 13건(13.4%) | Functional 49건 | Negative 22건 | Boundary 16건

---

## 확인 필요 사항

| # | 질문 | 관련 시나리오/REQ | 영향도 | 상태 |
|---|------|----------------|--------|------|
| 1 | 자유 텍스트 최솟값: 0글자 허용 여부 및 빈값(공백·미입력) 저장 시 처리 방식(오류 반환·저장 허용 등)이 미정의됨 | SC-CASEID-021 / REQ-025 | TC 작성 보류 | ⏸️ 미해결 |
| 2 | "최대 생성 가능 숫자" 기준값: 현재 설정 자릿수 최대값(예: 5자리=99999)인지, 자동 확장 고려 전체 한계값인지 미확정. 자릿수 변경 시 재계산 여부도 불명확 | SC-CASEID-027 / REQ-032 | TC 작성 가능, 전제 조건값 보류 | ⚠️ 보류 유지 |
| 3 | Destination 미확정 상태 C.1.1 공란 표시: 기획자 답변에 "확인 필요" 플래그 포함 — 잠정 처리 후 최종 확인 권장 | SC-CASEID-046 / REQ-053 | 잠정 처리 (참고용) | ⚠️ 잠정 답변 확인 요청 |

---

## 리뷰 이력

| 일자 | 참석자 | 주요 결정 사항 |
|-----|-------|--------------|
| 2026-05-07 | scenario-writer (자동) | 기획자 답변 v1.2 반영 — 13건 해결, MISSING-010 1건 TC보류 유지, 총 49개 시나리오 도출 |

---

## 참고 사항

### Validation 요약

| 필드 | 규칙 |
|------|------|
| 조직 식별자 | 최소 1자 ~ 최대 10자, 영문/숫자, 대소문자 구분 |
| 자유 텍스트 | 최대 6글자, 영문/숫자 (최솟값 미확정 — 확인 필요 #1) |
| 시작 번호 | 기본값 1 / [최대 생성 가능 숫자 - 400] 이하 (기준값 보류 — 확인 필요 #2) |

### 상태 전이 요약 (식별자 수정 정책)

```
[케이스 생성]
    ↓ Destination 확정 시
[C.1.1/C.1.8.1 부여] ← 부여 즉시 수동 수정 절대 불가 (어떤 상태에서도)
    ↓
[Draft → Submitted → Approval]
    ↓ Approval 이후
[수정 버튼 비표시 + 안내 문구 표시]
```

> Destination 미확정 상태: C.1.1 공란 → 확정 후 부여 (SC-CASEID-046 참조)
