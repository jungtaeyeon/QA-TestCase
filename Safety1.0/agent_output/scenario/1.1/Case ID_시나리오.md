# Case ID 테스트 시나리오

> **기반 RTM**: v0 (기획자 답변 반영 2026-04-28)
> **기획서**: `plan/00. Common (공통 정책)/Admin (Org Admin)/ICSR Config/Case ID/Case ID.md` (v1.0.250427)
> **작성일**: 2026-05-06 | **작성 에이전트**: scenario-writer | **최종 업데이트**: 2026-05-06 (기획자 보류 답변 반영 — 확인 필요 #1~#3 전원 해소)

---

## 개요

- **기능 범위**: Case ID Configuration 화면의 Case ID 번호 조합 설정 (접근 권한, 조직 식별자, 국가 코드, Year/Type of Report/Product Abbreviation/자유 텍스트/일련번호/포맷 설정), 만료 임박 알림 팝업, 자릿수 자동 확장, Import 설정, ICSR 식별자 관리 사양(C.1.1 / C.1.8.1)
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

- **[대분류] Case ID Configuration 접근 권한**
  - [중분류] 역할별 접근 허용/차단
    - Master Admin 접근 가능 [SC-CASEID-001] ✅
    - Org Admin 접근 가능 [SC-CASEID-001] ✅
    - 권한 없는 역할 접근 차단 [SC-CASEID-002] ✅

- **[대분류] 기본 구조 및 조직 식별자**
  - [중분류] 조직 식별자 입력
    - 유효 입력 (1~10글자, 영문/숫자) 및 Case ID 반영 [SC-CASEID-003] ✅
    - 길이 경계값 위반 (0글자, 11글자 이상) [SC-CASEID-004] ✅ (에러 메시지: [메시지 확인 필요])
    - 허용 문자 위반 (특수문자, 한글 등) [SC-CASEID-005] ✅ (에러 메시지: [메시지 확인 필요])
  - [중분류] 국가 코드 결정 로직
    - Reporter's Country Code (Primary) 우선 [SC-CASEID-006] ✅
    - Reporter's Country Code (First) — Primary 없을 때 [SC-CASEID-006] ✅
    - Country Where Reaction Occurred (Primary) [SC-CASEID-006] ✅
    - Country Where Reaction Occurred (First) [SC-CASEID-006] ✅
    - 기본값 KR [SC-CASEID-006] ✅

- **[대분류] 번호 조합 설정**
  - [중분류] Year 설정
    - 2-digit year 선택 및 매년 초 리셋 [SC-CASEID-007] ✅
    - 4-digit year 선택 및 매년 초 리셋 [SC-CASEID-008] ✅
    - N/A 선택 및 누적 증가 [SC-CASEID-009] ✅
    - 툴팁 문구 표시 (기획자 답변 CONFLICT-001 반영) [SC-CASEID-010] ✅
    - Year=N/A 선택 시 포맷 설정 영역 비활성화 (Year 칩 미추가 → 활성화 조건 미충족) [SC-CASEID-025] ✅
  - [중분류] Type of Report
    - 구분자 자동 추가 (SP/RS/OT/UN) [SC-CASEID-011] ✅
    - 표시 문구 노출 [SC-CASEID-011] ✅
    - Type of Report 미선택 시 구분자 미추가 [SC-CASEID-011] ✅
  - [중분류] Product Abbreviation
    - PRD Chip 포함 + 제품 있는 케이스 → 약어 표시 [SC-CASEID-012] ✅
    - PRD Chip 포함 + 제품 없는 케이스 → UNK 표시 [SC-CASEID-013] ✅
    - Suspect 자사 제품 2개 이상 → 첫 번째 약어 [SC-CASEID-013] ✅
  - [중분류] 자유 텍스트
    - 체크박스 선택 및 텍스트 입력 후 Case ID 반영 [SC-CASEID-014] ✅
    - 드래그 앤 드롭 위치 배치 [SC-CASEID-014] ✅
    - 길이/문자 유효성 검증 (최대 6글자, 영문/숫자) [SC-CASEID-015] ✅ (에러 메시지: [메시지 확인 필요])

- **[대분류] 일련번호 자릿수 설정**
  - [중분류] 자릿수 선택 및 Zero-padding
    - 자릿수 선택(3~9) 및 Zero-padding 적용 [SC-CASEID-016] ✅
    - 자릿수 경계값 (최솟값 3, 최댓값 9) [SC-CASEID-016] ✅
  - [중분류] 자릿수 중간 변경
    - 이후 케이스 적용 [SC-CASEID-017] ✅
    - 기존 케이스 표시 유지 (CONFIRM-002) [SC-CASEID-017] ✅

- **[대분류] 시작 번호 설정**
  - [중분류] 시작 번호 입력
    - 시작 번호 N 설정 및 즉시 적용 [SC-CASEID-018] ✅
    - 미입력 시 강제로 1 기입 (MISSING-002) [SC-CASEID-019] ✅
    - 최대값-400 초과 입력 불가 (오류 미노출, MISSING-002) [SC-CASEID-020] ✅
  - [중분류] 최후 번호 검증
    - 시작 번호 > 이미 생성된 최후 번호 강제 [SC-CASEID-021] ✅

- **[대분류] 포맷 설정 (Drag & Drop)**
  - [중분류] 활성화 조건
    - Year(2/4-digit) 선택 시 활성화 [SC-CASEID-022] ✅
    - Type of Report 체크 시 활성화 [SC-CASEID-022] ✅
    - 활성화 조건 미충족 시 비활성화 [SC-CASEID-022] ✅
  - [중분류] 칩 추가/삭제
    - 칩 추가 시 하단 설정 영역 활성화 [SC-CASEID-023] ✅
    - X 클릭 시 칩 삭제 및 비활성화 (이전 설정 유지) [SC-CASEID-023] ✅
  - [중분류] 순서 변경 및 Preview
    - 드래그로 순서 변경 및 Preview 실시간 반영 [SC-CASEID-024] ✅

- **[대분류] Case ID 만료 임박 알림**
  - [중분류] 팝업 노출 조건
    - 남은 번호 100개 이하 시 팝업 노출 [SC-CASEID-026] ✅
    - 팝업 노출 시점: Case ID 최종 부여 순간 [SC-CASEID-026] ✅
    - 남은 번호 101개 이상 시 팝업 미노출 [SC-CASEID-026] ✅
  - [중분류] 팝업 내용
    - 현재 마지막 Case ID, 최대값, 새 Case ID 표시 [SC-CASEID-027] ✅
  - [중분류] 사용자 인터랙션
    - Confirm 클릭 → 닫힘, 다음 로그인 재노출 [SC-CASEID-028] ✅
    - 세션 만료 후 재접속 = 다음 로그인 (CONFIRM-004) [SC-CASEID-028] ✅
    - Do not show again → 팝업 영구 미노출 [SC-CASEID-029] ✅
    - 새 자릿수 체계 전환 시 기존 팝업 자동 중단 [SC-CASEID-030] ✅
    - Do not show again + 자동 확장 → 설정 초기화 팝업 재노출 (CONFIRM-003) [SC-CASEID-031] ✅

- **[대분류] Case ID 자릿수 자동 확장**
  - [중분류] 확장 동작
    - 최대 자릿수 초과 시 한 자리 자동 확장 [SC-CASEID-032] ✅
    - 확장 후 1XXXXX 형식으로 번호 시작 [SC-CASEID-032] ✅

- **[대분류] Import 설정**
  - [중분류] 옵션 A (기본값)
    - C.1.1 신규 부여, C.1.8.1 파일 내 값 유지 [SC-CASEID-033] ✅
    - 파일 내 C.1.8.1 없는 경우 — 발생 불가 케이스 (C.1.8.1 Null 케이스 없음) [SC-CASEID-037] ➖
  - [중분류] 옵션 B
    - C.1.1, C.1.8.1 모두 파일 내 값 사용 [SC-CASEID-034] ✅
    - 중복 C.1.1 에러 반환 (CONFIRM-001) [SC-CASEID-035] ✅
  - [중분류] 적용 범위
    - Import 기능 케이스 생성 시에만 적용 [SC-CASEID-036] ✅

- **[대분류] C.1.1, C.1.8.1 동일 입력**
  - [중분류] C.1.8.1 Null 처리
    - C.1.8.1 없을 때 C.1.1 값 자동 복사 [SC-CASEID-038] ✅

- **[대분류] ICSR 식별자 노출 사양**
  - [중분류] Case Level
    - Tracker List, Case Edit — 일련번호 형식 노출 [SC-CASEID-039] ✅
  - [중분류] Report Level
    - C.1.1, C.1.8.1 — 국가-조직-일련번호 형식 노출 [SC-CASEID-040] ✅

- **[대분류] 생성 유형별 식별자 부여 로직**
  - [중분류] 매뉴얼 케이스 생성
    - C.1.1 = C.1.8.1, Destination 확정 시 국가코드 결정 [SC-CASEID-041] ✅
  - [중분류] Import 케이스
    - C.1.1 신규 부여, C.1.8.1 파일 내 값 유지 [SC-CASEID-042] ✅

- **[대분류] 식별자 수정 및 변경 정책**
  - [중분류] 수정 불가
    - 시스템 부여 즉시 수동 수정 불가 [SC-CASEID-043] ✅
    - Approval 이후 C.1.1, C.1.8.1 수정 불가 및 UI 안내 [SC-CASEID-044] ✅
    - C.1.8.1 변경 불가 — 시스템 UI 고지 없음 (CONFIRM-005) [SC-CASEID-045] ✅

- **[대분류] ID 재사용 방지**
  - [중분류] 재사용 금지
    - 케이스 삭제 후 일련번호 재사용 불가 [SC-CASEID-046] ✅

- **[대분류] C.1.4 필수값 처리** *(기획자 답변 MISSING-003)*
  - [중분류] Case 생성
    - C.1.4 Null 상태에서 케이스 생성 불가 [SC-CASEID-047] ✅
  - [중분류] Case 편집
    - C.1.4 Null 상태로 저장 불가 [SC-CASEID-048] ✅

---

### 커버리지 요약

| 대분류 | 전체 | ✅ 연결 | ⏸️ 보류 | ➖ 제외 | ❌ 미작성 | 처리율 | 완료율 |
|--------|------|--------|---------|-------|---------|-------|-------|
| Configuration 접근 권한 | 3 | 3 | 0 | 0 | 0 | 100% | 100% |
| 기본 구조 및 조직 식별자 | 7 | 7 | 0 | 0 | 0 | 100% | 100% |
| 번호 조합 설정 | 14 | 14 | 0 | 0 | 0 | 100% | 100% |
| 일련번호 자릿수 설정 | 4 | 4 | 0 | 0 | 0 | 100% | 100% |
| 시작 번호 설정 | 4 | 4 | 0 | 0 | 0 | 100% | 100% |
| 포맷 설정 | 7 | 7 | 0 | 0 | 0 | 100% | 100% |
| 만료 임박 알림 | 8 | 8 | 0 | 0 | 0 | 100% | 100% |
| 자릿수 자동 확장 | 2 | 2 | 0 | 0 | 0 | 100% | 100% |
| Import 설정 | 5 | 4 | 0 | 1 | 0 | 100% | 100% |
| C.1.1, C.1.8.1 동일 입력 | 1 | 1 | 0 | 0 | 0 | 100% | 100% |
| ICSR 식별자 노출 사양 | 2 | 2 | 0 | 0 | 0 | 100% | 100% |
| 생성 유형별 식별자 부여 | 2 | 2 | 0 | 0 | 0 | 100% | 100% |
| 식별자 수정 및 변경 정책 | 3 | 3 | 0 | 0 | 0 | 100% | 100% |
| ID 재사용 방지 | 1 | 1 | 0 | 0 | 0 | 100% | 100% |
| C.1.4 필수값 처리 | 2 | 2 | 0 | 0 | 0 | 100% | 100% |
| **합계** | **65** | **64** | **0** | **1** | **0** | **100%** | **100%** |

> - 게이트 판정: ✅ **PASS** — `❌` 0건, `⏸️` 0건 (모든 보류 항목 해소)
> - TC 작성 완료 후 `tc-writing-rules` Step 5에서 TC 커버리지 테이블 추가 예정

### REQ 매핑율

| 지표 | 값 |
|------|-----|
| 전체 REQ 수 | 64건 (기존 55 + 신규 9) |
| 제외 REQ 수 | 1건 (REQ-EX-001) |
| 매핑 대상 REQ 수 | 63건 |
| 시나리오 매핑 완료 | 63건 |
| 미매핑 (사유 기록) | 0건 |
| **REQ 매핑율** | **63 / 63 × 100 = 100%** |

---

## 시나리오 목록

| ID | 우선순위 | 관점 | 기법 | 시나리오 제목 | 검증 목적 | 근거 | 관련 REQ |
|----|---------|------|------|--------------|----------|------|---------|
| SC-CASEID-001 | Critical | Business | 결정테이블 | Master Admin / Org Admin은 Case ID Configuration 화면에 접근하고 설정을 저장할 수 있다 | 허가된 역할의 접근 및 설정 저장 가능 여부 확인 | 기획자 답변 MISSING-001 | REQ-056 |
| SC-CASEID-002 | Critical | Business | 결정테이블 | 권한 없는 역할은 Case ID Configuration 화면에 접근할 수 없다 | 비인가 역할의 접근 차단 여부 확인 | 기획자 답변 MISSING-001 | REQ-056 |
| SC-CASEID-003 | High | Functional | 유스케이스 | 유효한 조직 식별자를 입력하면 Case ID 기본 구조에 반영된다 | [국가]-[조직 식별자]-[번호 조합] 구조 정상 반영 확인 | 기획서 § 기본 구조 및 국가코드 로직 | REQ-005, REQ-011 |
| SC-CASEID-004 | High | Data | 경계값분석 | 조직 식별자 길이 경계값 위반 시 입력이 제한된다 | 0글자(미입력), 11글자 이상 입력 시 거부 동작 확인 | 기획서 § 기본 구조 및 국가코드 로직; REQ-011 | REQ-003, REQ-011 |
| SC-CASEID-005 | High | Data | 동등분할 | 조직 식별자에 허용되지 않는 문자(특수문자, 한글 등) 입력 시 제한된다 | 영문/숫자 외 문자 입력 차단 확인 | 기획서 § 기본 구조; REQ-011 | REQ-003, REQ-011 |
| SC-CASEID-006 | Critical | Business | 결정테이블 | 케이스 생성 시 국가 코드 결정 우선순위(①→②→③→④→기본값 KR)에 따라 Case ID 접두사가 결정된다 | 국가 코드 우선순위 로직 각 분기 검증 | 기획서 § 기본 구조 및 국가코드 로직 | REQ-006, REQ-007, REQ-008, REQ-009, REQ-010 |
| SC-CASEID-007 | High | Business | 유스케이스 | Year 2-digit 설정 시 Case ID에 C.1.4 연도 뒤 2자리(YY)가 포함되고 매년 1월 1일 00:00:00에 일련번호가 리셋된다 | 2-digit year 표기 및 연초 리셋 동작 확인 | 기획서 § Year (연도 표시 및 리셋 정책) | REQ-012 |
| SC-CASEID-008 | High | Business | 유스케이스 | Year 4-digit 설정 시 Case ID에 C.1.4 연도 전체 4자리(YYYY)가 포함되고 매년 1월 1일 00:00:00에 일련번호가 리셋된다 | 4-digit year 표기 및 연초 리셋 동작 확인 | 기획서 § Year (연도 표시 및 리셋 정책) | REQ-013 |
| SC-CASEID-009 | High | Functional | 유스케이스 | Year N/A 설정 시 연도가 미표기되고 일련번호가 초기화 없이 누적 증가한다 | N/A 선택 시 누적 채번 동작 확인 | 기획서 § Year (연도 표시 및 리셋 정책) | REQ-014 |
| SC-CASEID-010 | Medium | Functional | 유스케이스 | Year 설정란 옆 툴팁이 기획자 수정 완료된 올바른 문구로 표시된다 | 툴팁 문구에 삭제된 "연월 선택" 표현이 없고 현행 정책을 정확히 안내하는지 확인 | 기획자 답변 CONFLICT-001; 기획서 § Year | REQ-015 |
| SC-CASEID-011 | High | Business | 결정테이블 | Type of Report 체크 시 케이스의 Type of Report 값에 따라 구분자(SP/RS/OT/UN)가 Case ID에 자동 추가된다 | 4가지 유형별 구분자 추가 및 미선택 시 미추가 확인 | 기획서 § Type of Report (보고 구분) 추가 | REQ-016, REQ-017 |
| SC-CASEID-012 | High | Business | 유스케이스 | PRD Chip이 포함된 설정에서 제품 있는 케이스 생성 시 Product Config에 등록된 제품 약어가 Case ID에 표시된다 | Product Abbreviation 정상 참조 및 표시 확인 | 기획서 § Product Abbreviation 추가; 기획자 답변 MISSING-005 | REQ-018, REQ-020 |
| SC-CASEID-013 | High | Business | 결정테이블 | PRD Chip 포함 설정에서 제품 없는 케이스는 UNK가 표시되고, Suspect 자사 제품 2개 이상이면 첫 번째 자사제품 약어가 표시된다 | 제품 없음/복수 제품 분기 처리 확인 | 기획서 § Product Abbreviation 추가; 기획자 답변 MISSING-005 | REQ-019, REQ-021 |
| SC-CASEID-014 | High | Functional | 유스케이스 | 자유 텍스트를 체크 후 입력하고 원하는 위치에 배치하면 해당 텍스트가 Case ID에 포함된다 | 자유 텍스트 선택→입력→드래그 배치→Case ID 반영 플로우 확인 | 기획서 § 자유 텍스트 추가 | REQ-022, REQ-024 |
| SC-CASEID-015 | High | Data | 경계값분석 | 자유 텍스트 유효성 위반(7글자 이상 또는 허용 외 문자) 시 입력이 제한된다 | 최대 6글자 초과, 영문/숫자 외 문자 차단 확인 | 기획서 § 자유 텍스트 추가; REQ-023 | REQ-003, REQ-023 |
| SC-CASEID-016 | High | Functional | 경계값분석 | 일련번호 자릿수를 선택하면 해당 자릿수만큼 Zero-padding이 적용된 번호가 생성된다 | 자릿수 3(최솟값) ~ 9(최댓값) 각 선택 시 정상 Zero-padding 확인 | 기획서 § 일련번호 자릿수 설정 | REQ-025, REQ-026 |
| SC-CASEID-017 | High | Business | 상태전이 | 일련번호 자릿수를 중간에 변경하면 이후 생성 케이스에만 새 자릿수가 적용되고 기존 케이스는 생성 당시 자릿수를 유지한다 | 자릿수 변경의 소급 미적용 및 이후 적용 확인 | 기획서 § 일련번호 자릿수 설정; 기획자 답변 CONFIRM-002 | REQ-027, REQ-060 |
| SC-CASEID-018 | High | Functional | 유스케이스 | 시작 번호 N을 설정하고 저장하면 이후 생성되는 첫 번째 케이스의 일련번호가 N으로 시작한다 | 시작 번호 설정 및 즉시 적용 확인 | 기획서 § 시작 번호 설정 | REQ-028, REQ-029, REQ-030 |
| SC-CASEID-019 | Medium | Data | 오류추정 | 시작 번호 입력란을 비우고 포커스를 벗어나면 시스템이 강제로 1을 기입한다 | 미입력 시 기본값 1 강제 기입 동작 확인 | 기획자 답변 MISSING-002; REQ-028 | REQ-028, REQ-057 |
| SC-CASEID-020 | High | Business | 경계값분석 | 시작 번호를 [최대 생성 가능 숫자 - 400]을 초과하여 입력하면 입력이 차단된다 (오류 문구 미노출) | 임계치 초과 입력 불가 및 오류 문구 미노출 확인 | 기획서 § 시작 번호 설정 제한 정책; 기획자 답변 MISSING-002 | REQ-032, REQ-058 |
| SC-CASEID-021 | High | Business | 결정테이블 | 시작 번호가 해당 조합에서 이미 생성된 최후 번호보다 크지 않으면 생성이 거부된다 | 최후 번호 검증 규칙 적용 확인 | 기획서 § 최후 번호 검증 규칙 | REQ-031 |
| SC-CASEID-022 | High | Functional | 결정테이블 | Year(2/4-digit) 선택 또는 Type of Report 체크 시에만 포맷 설정(Drag & Drop) 영역이 활성화된다 | 활성화 조건 충족/미충족 각 분기 확인 | 기획서 § 포맷 설정 및 인터랙션 | REQ-033 |
| SC-CASEID-023 | High | Functional | 유스케이스 | 칩을 추가하면 하단 해당 설정 영역이 활성화되고, X를 클릭해 칩을 삭제하면 비활성화되지만 이전 설정값은 유지된다 | 칩 추가/삭제와 하단 설정 영역 연동 및 설정 유지 확인 | 기획서 § 포맷 설정 및 인터랙션 | REQ-034, REQ-035, REQ-037 |
| SC-CASEID-024 | Medium | Functional | 유스케이스 | 칩을 드래그하여 순서를 변경하면 상단 Case ID Preview에 실시간으로 반영된다 | 드래그 앤 드롭 순서 변경 및 Preview 실시간 반영 확인 | 기획서 § 포맷 설정 및 인터랙션 | REQ-036 |
| SC-CASEID-025 | High | Functional | 유스케이스 | Year=N/A 설정 시 포맷 설정 영역(Drag & Drop)이 활성화되지 않는다 | Year=N/A는 Year 칩을 추가하지 않은 상태이므로 활성화 조건(2/4-digit 또는 Type of Report 체크) 미충족 → 포맷 설정 영역 비활성화 확인 | 기획자 답변 (2026-05-06) | REQ-033, REQ-034 |
| SC-CASEID-026 | High | Business | 경계값분석 | 케이스에 Case ID가 최종 부여되는 시점에 남은 번호가 100개 이하이면 만료 임박 팝업이 즉시 노출된다 | 100개 이하(노출) / 101개 이상(미노출) 경계 확인 | 기획서 § Case ID 만료 임박 알림 | REQ-038, REQ-039 |
| SC-CASEID-027 | Medium | Functional | 유스케이스 | 만료 임박 팝업에 현재 마지막 Case ID, 최대 자릿수 최대값, 확장 후 새 Case ID 정보가 표시된다 | 팝업 내용 정확성 확인 | 기획서 § Case ID 만료 임박 알림 | REQ-040 |
| SC-CASEID-028 | High | Business | 상태전이 | [Confirm] 클릭 시 팝업이 닫히고, 해당 사용자의 다음 로그인(세션 만료 후 재접속 포함) 시 팝업이 재노출된다 | Confirm 닫기 후 재노출 로직 및 세션 만료 포함 여부 확인 | 기획서 § 사용자 인터랙션 및 제어; 기획자 답변 CONFIRM-004 | REQ-041, REQ-062 |
| SC-CASEID-029 | High | Business | 상태전이 | [Do not show again] 체크 후 [Confirm] 클릭 시 해당 사용자에게 만료 임박 팝업이 더 이상 노출되지 않는다 | 영구 미노출 설정 동작 확인 | 기획서 § 사용자 인터랙션 및 제어 | REQ-042 |
| SC-CASEID-030 | Medium | Business | 상태전이 | 일련번호가 완전히 초과되어 새로운 자릿수 체계(1XXXXX...)로 전환되면 기존 만료 임박 팝업이 자동으로 중단된다 | 새 자릿수 체계 전환 후 기존 팝업 미노출 확인 | 기획서 § 사용자 인터랙션 및 제어 | REQ-043 |
| SC-CASEID-031 | High | Business | 상태전이 | [Do not show again]을 설정한 사용자가 자릿수 자동 확장으로 새 자릿수 체계로 전환되면 설정이 초기화되어 새 체계에 대한 팝업이 재노출된다 | 자동 확장 이후 Do not show again 초기화 및 팝업 재노출 확인 | 기획자 답변 CONFIRM-003 | REQ-042, REQ-061 |
| SC-CASEID-032 | Critical | Business | 상태전이 | 설정된 최대 자릿수를 초과하는 번호가 필요할 때 자릿수가 한 자리 자동 확장되어 1XXXXX 형식으로 번호가 이어진다 | 서비스 중단 없이 자릿수 자동 확장 동작 확인 | 기획서 § Case ID 자릿수 자동 확장 | REQ-044 |
| SC-CASEID-033 | Critical | Business | 유스케이스 | Import 기본값(옵션 A) 선택 시 C.1.1은 시스템 규칙에 따라 신규 부여되고 C.1.8.1은 파일 내 데이터가 유지된다 | Import 옵션 A 동작 확인 | 기획서 § Import 설정 | REQ-045, REQ-047 |
| SC-CASEID-034 | Critical | Business | 유스케이스 | Import 옵션 B 선택 시 C.1.1, C.1.8.1 모두 파일 내 값 그대로 사용된다 | Import 옵션 B 동작 확인 | 기획서 § Import 설정 | REQ-046 |
| SC-CASEID-035 | Critical | Business | 오류추정 | Import 옵션 B 선택 후 파일 내 C.1.1이 시스템 기존 케이스와 중복될 경우 에러가 반환되고 Import가 실패한다 | 중복 C.1.1 에러 반환 및 오류 메시지 표시 확인 | 기획자 답변 CONFIRM-001 | REQ-046, REQ-059 |
| SC-CASEID-036 | High | Business | 결정테이블 | Import 설정은 Import 기능으로 케이스를 생성할 때만 적용되며, 매뉴얼 생성에는 적용되지 않는다 | Import 설정 적용 범위 한정 확인 | 기획서 § Import 설정 — 적용 범위 | REQ-047 |
| SC-CASEID-037 | - | - | - | ➖ N/A — Import 파일 내 C.1.8.1 Null 케이스 없음 | C.1.8.1이 Null인 케이스는 존재하지 않으므로 테스트 대상에서 제외 | 기획자 답변 (2026-05-06) | REQ-045, REQ-048 |
| SC-CASEID-038 | High | Business | 결정테이블 | C.1.8.1이 Null인 경우 C.1.1 값이 C.1.8.1에 자동으로 복사된다 | C.1.8.1 Null 시 C.1.1 복사 동작 확인 | 기획서 § C.1.1, C.1.8.1 동일 입력 설정 | REQ-048 |
| SC-CASEID-039 | High | Functional | 유스케이스 | Tracker List 및 Case Edit의 Case ID 필드에 일련번호 형식으로 식별자가 노출된다 | Case Level 노출 형식(일련번호) 확인 | 기획서 § Case vs Report Identifier 노출 사양 | REQ-001, REQ-002, REQ-049 |
| SC-CASEID-040 | High | Functional | 유스케이스 | ICSR 보고서(C.1.1, C.1.8.1)에 국가-조직-일련번호 형식으로 식별자가 노출된다 | Report Level 노출 형식(국가-조직-일련번호) 확인 | 기획서 § Case vs Report Identifier 노출 사양 | REQ-050 |
| SC-CASEID-041 | Critical | Business | 유스케이스 | 매뉴얼 케이스 생성 시 C.1.1과 C.1.8.1이 동일하며, Destination 확정 시 국가코드가 결정되어 [국가]-[회사]-[일련번호] 조합이 기입된다 | 매뉴얼 케이스 식별자 부여 로직 확인 | 기획서 § 매뉴얼 케이스 생성 (Initial) | REQ-001, REQ-051 |
| SC-CASEID-042 | Critical | Business | 유스케이스 | Import 케이스 생성 시 C.1.1은 Destination 확정 시 신규 부여되고, C.1.8.1은 파일 내 기존 값이 유지된다 | Import 케이스 식별자 부여 로직 확인 | 기획서 § 데이터 인입 (Import) | REQ-001, REQ-052 |
| SC-CASEID-043 | Critical | Business | 도메인리스크 | 시스템이 부여한 식별자는 사용자가 수동으로 수정할 수 없다 | 식별자 편집 불가 (사용자 편집 권한 없음) 확인 | 기획서 § 식별자 수정 및 변경 정책 | REQ-053 |
| SC-CASEID-044 | Critical | Business | 상태전이 | Approval 상태 이후 C.1.1, C.1.8.1 수정 불가 — 수정 버튼 비표시 및 안내 문구가 표시된다 | Approval 이후 C.1.1/C.1.8.1 잠금 및 UI 안내 확인 | 기획서 § 식별자 수정 및 변경 정책 | REQ-054, REQ-055 |
| SC-CASEID-045 | Medium | Business | 유스케이스 | C.1.8.1 변경 불가 정책은 시스템 UI에 별도 표시 없이 운영 정책 문서/교육으로만 고지된다 | 시스템 UI에 C.1.8.1 변경 불가 안내 미표시 확인 | 기획자 답변 CONFIRM-005 | REQ-055 |
| SC-CASEID-046 | Critical | Business | 도메인리스크 | 케이스가 삭제되더라도 해당 케이스에 부여된 일련번호는 이후 새 케이스에 재사용되지 않는다 | ID 재사용 방지 정책 확인 | 기획서 § 개요 및 정책 | REQ-004 |
| SC-CASEID-047 | High | Business | 유스케이스 | Case 생성 시 C.1.4(최초 발생인지일)는 필수값이므로 C.1.4 없이 케이스 생성을 시도하면 거부된다 | C.1.4 Null 케이스 생성 불가 확인 | 기획자 답변 MISSING-003 | REQ-063 |
| SC-CASEID-048 | High | Business | 유스케이스 | Case 편집 중 C.1.4를 제거한 상태로 저장하면 저장이 거부된다 | Case 편집 시 C.1.4 Null 저장 불가 확인 | 기획자 답변 MISSING-003 | REQ-064 |

> **기획자 답변 반영 (2026-05-06)**: SC-CASEID-025 ✅ 확정 (Year=N/A → 포맷 설정 비활성화), SC-CASEID-037 ➖ N/A (C.1.8.1 Null 케이스 없음 → 제외), SC-CASEID-004/005/015 에러 메시지 "[메시지 확인 필요]"로 TC 작성.
> **보류 항목 없음** — 확인 필요 사항 #1~#3 전원 해소, 게이트 판정 ✅ PASS.

---

## TC 매핑 상태

| 시나리오 ID | 시나리오 제목 (요약) | TC ID 범위 | TC 작성 상태 |
|------------|---------------------|-----------|-------------|
| SC-CASEID-001 | Master Admin/Org Admin 접근 허용 | - | ⏳ 대기 |
| SC-CASEID-002 | 비인가 역할 접근 차단 | - | ⏳ 대기 |
| SC-CASEID-003 | 유효 조직 식별자 입력 및 Case ID 반영 | - | ⏳ 대기 |
| SC-CASEID-004 | 조직 식별자 길이 경계값 위반 | - | ⏳ 대기 |
| SC-CASEID-005 | 조직 식별자 허용 문자 위반 | - | ⏳ 대기 |
| SC-CASEID-006 | 국가 코드 우선순위 결정 로직 | - | ⏳ 대기 |
| SC-CASEID-007 | Year 2-digit 설정 및 연초 리셋 | - | ⏳ 대기 |
| SC-CASEID-008 | Year 4-digit 설정 및 연초 리셋 | - | ⏳ 대기 |
| SC-CASEID-009 | Year N/A 설정 및 누적 증가 | - | ⏳ 대기 |
| SC-CASEID-010 | Year 설정란 툴팁 문구 확인 | - | ⏳ 대기 |
| SC-CASEID-011 | Type of Report 구분자 자동 추가 | - | ⏳ 대기 |
| SC-CASEID-012 | PRD Chip + 제품 있는 케이스 약어 표시 | - | ⏳ 대기 |
| SC-CASEID-013 | PRD Chip + 제품 없는 케이스 UNK / Suspect 복수 | - | ⏳ 대기 |
| SC-CASEID-014 | 자유 텍스트 선택·입력·배치 및 Case ID 반영 | - | ⏳ 대기 |
| SC-CASEID-015 | 자유 텍스트 유효성 위반 | - | ⏳ 대기 |
| SC-CASEID-016 | 일련번호 자릿수 선택 및 Zero-padding | - | ⏳ 대기 |
| SC-CASEID-017 | 자릿수 중간 변경 — 이후 적용, 기존 유지 | - | ⏳ 대기 |
| SC-CASEID-018 | 시작 번호 설정 및 즉시 적용 | - | ⏳ 대기 |
| SC-CASEID-019 | 시작 번호 미입력 시 강제 1 기입 | - | ⏳ 대기 |
| SC-CASEID-020 | 시작 번호 최대값-400 초과 입력 불가 | - | ⏳ 대기 |
| SC-CASEID-021 | 최후 번호 검증 — 시작 번호 > 최후 번호 | - | ⏳ 대기 |
| SC-CASEID-022 | 포맷 설정 영역 활성화/비활성화 조건 | - | ⏳ 대기 |
| SC-CASEID-023 | 칩 추가/삭제 및 하단 설정 연동 | - | ⏳ 대기 |
| SC-CASEID-024 | 칩 드래그 순서 변경 및 Preview 실시간 반영 | - | ⏳ 대기 |
| SC-CASEID-025 | Year=N/A 시 포맷 설정 영역 비활성화 | - | ⏳ 대기 |
| SC-CASEID-026 | 만료 임박 팝업 노출 조건 (100개 이하) | - | ⏳ 대기 |
| SC-CASEID-027 | 만료 임박 팝업 내용 검증 | - | ⏳ 대기 |
| SC-CASEID-028 | Confirm 클릭 후 닫힘 및 다음 로그인 재노출 | - | ⏳ 대기 |
| SC-CASEID-029 | Do not show again — 영구 미노출 | - | ⏳ 대기 |
| SC-CASEID-030 | 새 자릿수 체계 전환 시 기존 팝업 자동 중단 | - | ⏳ 대기 |
| SC-CASEID-031 | Do not show again + 자동 확장 → 설정 초기화 재노출 | - | ⏳ 대기 |
| SC-CASEID-032 | 최대 자릿수 초과 시 자릿수 자동 확장 | - | ⏳ 대기 |
| SC-CASEID-033 | Import 옵션 A — C.1.1 신규, C.1.8.1 파일 내 유지 | - | ⏳ 대기 |
| SC-CASEID-034 | Import 옵션 B — C.1.1, C.1.8.1 파일 내 사용 | - | ⏳ 대기 |
| SC-CASEID-035 | Import 옵션 B 중복 C.1.1 에러 반환 | - | ⏳ 대기 |
| SC-CASEID-036 | Import 설정 적용 범위 (Import 케이스 생성 시에만) | - | ⏳ 대기 |
| SC-CASEID-037 | ➖ N/A — C.1.8.1 Null 케이스 없음 (제외) | - | ➖ TC 제외 |
| SC-CASEID-038 | C.1.8.1 Null 시 C.1.1 값 자동 복사 | - | ⏳ 대기 |
| SC-CASEID-039 | Case Level — 일련번호 형식 노출 | - | ⏳ 대기 |
| SC-CASEID-040 | Report Level — 국가-조직-일련번호 형식 노출 | - | ⏳ 대기 |
| SC-CASEID-041 | 매뉴얼 케이스 C.1.1=C.1.8.1, Destination 확정 시 국가코드 결정 | - | ⏳ 대기 |
| SC-CASEID-042 | Import 케이스 C.1.1 신규 부여, C.1.8.1 파일 내 유지 | - | ⏳ 대기 |
| SC-CASEID-043 | 시스템 부여 식별자 수동 수정 불가 | - | ⏳ 대기 |
| SC-CASEID-044 | Approval 이후 C.1.1/C.1.8.1 수정 불가 및 UI 안내 | - | ⏳ 대기 |
| SC-CASEID-045 | C.1.8.1 변경 불가 — 시스템 UI 미표시 확인 | - | ⏳ 대기 |
| SC-CASEID-046 | 케이스 삭제 후 일련번호 재사용 불가 | - | ⏳ 대기 |
| SC-CASEID-047 | Case 생성 시 C.1.4 필수값 (Null 생성 불가) | - | ⏳ 대기 |
| SC-CASEID-048 | Case 편집 시 C.1.4 Null 저장 불가 | - | ⏳ 대기 |

---

## 확인 필요 사항

| # | 질문 | 관련 시나리오/요구사항 | 처리 결과 | 상태 |
|---|------|-------------------|----------|------|
| 1 | 조직 식별자(길이/문자 위반) 및 자유 텍스트(길이/문자 위반) Validation 실패 시 에러 메시지 문구 미정의 | SC-CASEID-004, SC-CASEID-005, SC-CASEID-015 / REQ-003, REQ-011, REQ-023 | TC 에러 메시지 필드에 "[메시지 확인 필요]"로 작성. TC 작성 가능. | ✅ 확인 완료 |
| 2 | Year=N/A 선택 시 포맷 설정 영역(Drag & Drop) 활성화 여부 | SC-CASEID-025 / REQ-033, REQ-034 | Year=N/A는 Year 칩을 Drag & Drop으로 추가하지 않은 상태 → 활성화 조건 미충족 → 포맷 설정 비활성화. SC-CASEID-025 ✅ 확정. | ✅ 확인 완료 |
| 3 | Import 옵션 A 선택 상태에서 파일 내 C.1.8.1이 Null인 경우 처리 방식 | SC-CASEID-037 / REQ-045, REQ-048 | C.1.8.1 Null 케이스 자체가 없음 → 테스트 대상 외. SC-CASEID-037 ➖ N/A 제외. | ✅ 확인 완료 |

---

## 리뷰 이력

| 일자 | 참석자 | 주요 결정 사항 |
|-----|-------|--------------|
| 2026-05-06 | scenario-writer | RTM v0 기반 초안 작성. 기획자 확인 요청 답변 파일(2026-04-28) 반영 — CONFLICT-001/002, MISSING-001~005, EXPR-001~003, CONFIRM-001~005 해결 처리. 미해결 2건(확인 필요 #2, #3) TC 작성 보류. 조직 식별자/자유 텍스트 에러 메시지(확인 필요 #1)는 TC 작성 가능, 에러 문구 검증만 참고용 처리. 신규 REQ 9건(REQ-056~REQ-064) 추가. |
| 2026-05-06 | 기획자 보류 답변 반영 | 확인 필요 사항 #1~#3 전원 해소. #1: 에러 메시지 "[메시지 확인 필요]"로 처리 (SC-CASEID-004/005/015 ✅). #2: Year=N/A = Year 칩 미추가 → 포맷 설정 비활성화 확정 (SC-CASEID-025 ✅). #3: C.1.8.1 Null 케이스 없음 → SC-CASEID-037 ➖ N/A 제외. 게이트 판정 ✅ PASS 상향. |

---

## 참고 사항

### Validation 요약

| 필드 | 유효 범위 | 위반 시 동작 | 에러 메시지 |
|------|---------|------------|-----------|
| 조직 식별자 | 1~10글자, 영문/숫자 | 입력 제한 | **[메시지 확인 필요]** |
| 자유 텍스트 | 1~6글자, 영문/숫자 | 입력 제한 | **[메시지 확인 필요]** |
| 시작 번호 — 미입력 | - | 강제 1 기입 (오류 미노출) | 없음 |
| 시작 번호 — 최대값-400 초과 | - | 입력 불가 (오류 미노출) | 없음 |
| Import 옵션 B — 중복 C.1.1 | - | Import 실패 | 오류 메시지 표시 (문구 미정의) |

### 신규 추가 REQ 목록 (기획자 답변 기반)

| REQ_Id | 내용 | 출처 |
|--------|------|------|
| REQ-056 | Case ID Configuration 접근 권한: Master Admin / Org Admin만 접근 가능 | 기획자 답변 MISSING-001 |
| REQ-057 | 시작 번호 미입력 시 강제로 1 기입 | 기획자 답변 MISSING-002 |
| REQ-058 | 시작 번호 최대값-400 초과 입력 불가 (오류 미노출) | 기획자 답변 MISSING-002 |
| REQ-059 | Import 옵션 B — 중복 C.1.1 시 에러 반환 (Import 실패, 오류 메시지 표시) | 기획자 답변 CONFIRM-001 |
| REQ-060 | 자릿수 중간 변경 후 기존 케이스는 생성 당시 자릿수 그대로 표시 | 기획자 답변 CONFIRM-002 |
| REQ-061 | [Do not show again] 설정 후 자릿수 자동 확장 시 설정 초기화, 새 체계 팝업 재노출 | 기획자 답변 CONFIRM-003 |
| REQ-062 | 세션 만료 후 재접속도 "다음 로그인"으로 간주 → 팝업 재노출 | 기획자 답변 CONFIRM-004 |
| REQ-063 | C.1.4(최초 발생인지일)는 Case 생성 시 필수값 (Null 케이스 생성 불가) | 기획자 답변 MISSING-003 |
| REQ-064 | Case 편집 시 C.1.4 Null 상태로 저장 불가 | 기획자 답변 MISSING-003 |
