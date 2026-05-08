# Default Rule 테스트 시나리오

## 개요
- 기획서: [default-rule.md](../../plan/1.0/0414/00-common(공통정책)/configuration/icsr-config/default-rule.md)
- 작성 기준일: 2026-04-15
- 기능 범위: ICSR(개별 사례 안전성 보고서)의 Case ID 생성 규칙 설정 및 관리
- 제외 범위: 와이어프레임, 추후 개발 예정 기능 (Convert 적용 등)
- 참조 상위 기획: [multi-org.md](계정 권한 정책), [home-navigation.md](네비게이션 정책), [org-admin-app-admin.md](관리자 권한)

### 주요 용어
| 용어 | 정의 |
|-----|------|
| Case ID | ICSR 케이스의 고유 식별 번호. `[국가코드]-[조직 식별자]-[설정된 번호 조합]` 형식 |
| C.1.1 (보고자 관리번호) | ICSR E2B R3 필드. Report Level에서 국가-조직-일련번호 형식으로 표시 |
| C.1.8.1 (고유식별 보고자 관리번호) | ICSR E2B R3 필드. 케이스 식별 및 중복 체크의 기준 |
| 일련번호 | Case ID 내 순차적으로 부여되는 숫자 부분 |
| Zero-padding | 일련번호 앞자리에 '0'을 채우는 방식 |
| Type of Report | 보고 유형 (Spontaneous, Report from Study, Other, Not Available) |
| Product Abbreviation | Admin > Product Config에 등록된 제품 약어 |
| Import | 외부 파일을 통해 케이스를 시스템에 인입하는 기능 |

---

## 기능 분해

| 화면/업무 흐름 | 기능 영역 | 세부 동작 | 관련 근거 |
|--------------|----------|----------|----------|
| Default Rule 설정 | 조직 식별자 설정 | 조직 식별자 텍스트 입력 (1-10글자, 영어/숫자만) | 기획서 §기본 구조 및 국가 코드 로직 |
| Default Rule 설정 | 국가 코드 결정 | 케이스 생성 시 우선순위에 따른 국가 코드 자동 결정 | 기획서 §기본 구조 및 국가 코드 로직 |
| Default Rule 설정 | 연도 설정 (Year) | 5가지 연도 포맷 중 선택 및 리셋 정책 적용 | 기획서 §Year (연도 표시 및 리셋 정책) |
| Default Rule 설정 | Type of Report 설정 | 보고 구분 코드 자동 추가 체크 및 매핑 (SP/RS/OT/UN) | 기획서 §Type of Report |
| Default Rule 설정 | Product Abbreviation 설정 | 제품 약어 참조 설정 체크 | 기획서 §Product Abbreviation 추가 |
| Default Rule 설정 | 자유 텍스트 설정 | 사용자 정의 텍스트 블록 추가 (최대 6글자) | 기획서 §자유 텍스트 추가 |
| Default Rule 설정 | 일련번호 자릿수 설정 | 3-9자리 중 선택 | 기획서 §일련번호 자릿수 설정 |
| Default Rule 설정 | 시작 번호 설정 | 일련번호 시작점 지정 | 기획서 §시작 번호 설정 |
| Default Rule 설정 | 포맷 순서 설정 | Drag & Drop으로 구성 요소 순서 변경 | 기획서 §포맷 설정 및 인터랙션 |
| Default Rule 설정 | Preview 실시간 반영 | 설정 변경 시 상단 Preview에 즉시 반영 | 기획서 §포맷 설정 및 인터랙션 |
| Case ID 부여 | 자동 채번 | 케이스 생성 시 설정에 따른 Case ID 자동 부여 | 기획서 §개요 및 정책, §생성 유형별 식별자 부여 로직 |
| Case ID 부여 | ID 재사용 방지 | 삭제된 케이스의 일련번호 재사용 금지 | 기획서 §개요 및 정책 |
| Case ID 부여 | 연/월 기준 리셋 | 연도/연월 설정에 따른 주기적 번호 초기화 | 기획서 §Year |
| Case ID 만료 관리 | 만료 임박 알림 | 남은 번호 200개 이하 시 팝업 알림 | 기획서 §Case ID 만료 임박 알림 |
| Case ID 만료 관리 | 자릿수 자동 확장 | 최대치 초과 시 자동 자릿수 확장 | 기획서 §Case ID 자릿수 자동 확장 |
| Import 설정 | C.1.1/C.1.8.1 처리 방식 | Import 시 식별자 유지/신규 부여 옵션 선택 | 기획서 §Import 설정 |
| Case Edit | C.1.1 수정 제한 | 기본 수정 불가, 수동 변경 시 Sync 해제 경고 | 기획서 §C.1.1 동작 설정 |
| Case Edit | Approval 후 수정 불가 | Approval 상태 이후 C.1.1, C.1.8.1 수정 차단 | 기획서 §C.1.1 변경 시점 |
| 식별자 노출 | Case Level 노출 | Tracker List, Case에서 일련번호만 표시 | 기획서 §Case vs Report 식별자 노출 사양 |
| 식별자 노출 | Report Level 노출 | ICSR 보고서에서 국가-조직-일련번호 표시 | 기획서 §Case vs Report 식별자 노출 사양 |

---

## 관점 매핑 요약

| 기능 영역 | Functional | Business | Data | Non-Functional | Flow | 비고 |
|----------|-----------|----------|------|----------------|------|------|
| 조직 식별자 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 입력 유효성, 저장 |
| 국가 코드 결정 | 적용 | 적용 | 적용 | 미적용 | 적용 | 우선순위 로직, 기본값 |
| 연도 설정 (Year) | 적용 | 적용 | 적용 | 미적용 | 적용 | 리셋 정책 영향 |
| Type of Report 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 코드 매핑 정합성 |
| Product Abbreviation 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 외부 데이터 참조 |
| 자유 텍스트 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 입력 유효성 |
| 일련번호 자릿수 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 경계값 |
| 시작 번호 설정 | 적용 | 적용 | 적용 | 미적용 | 적용 | 기존 번호 영향 |
| 포맷 순서 설정 | 적용 | 미적용 | 적용 | 미적용 | 미적용 | UI 인터랙션 |
| Preview 실시간 반영 | 적용 | 미적용 | 미적용 | 미적용 | 미적용 | 실시간 UI |
| 자동 채번 | 적용 | 적용 | 적용 | 미적용 | 적용 | 핵심 비즈니스 로직 |
| ID 재사용 방지 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 데이터 무결성 |
| 연/월 기준 리셋 | 적용 | 적용 | 적용 | 미적용 | 적용 | 시간 기반 전이 |
| 만료 임박 알림 | 적용 | 적용 | 미적용 | 미적용 | 미적용 | 사용자 알림 |
| 자릿수 자동 확장 | 적용 | 적용 | 적용 | 미적용 | 적용 | 서비스 연속성 |
| Import C.1.1/C.1.8.1 처리 | 적용 | 적용 | 적용 | 미적용 | 적용 | 식별자 정합성 |
| C.1.1 수정 제한 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 데이터 보호 |
| Approval 후 수정 불가 | 적용 | 적용 | 적용 | 미적용 | 적용 | 상태 기반 제한 |
| 식별자 노출 (Case/Report) | 적용 | 적용 | 적용 | 미적용 | 미적용 | 화면별 표시 규칙 |

---

## 시나리오 목록

| ID | 우선순위 | 관점 태그 | 도출 기법 | 시나리오 제목 | 검증 목적 | 근거 | 비고 | 예상 TC 유형 |
|----|---------|----------|----------|-------------|----------|------|------|-------------|
| SC-DFR-001 | Critical | Business, Data | DT, DR | Default Rule 설정 화면에 올바른 권한을 가진 사용자만 접근할 수 있다 | Master Admin/Org Admin만 Configuration > ICSR Config > Default Rule에 접근 가능한지 검증 | multi-org.md §4.2 Role Boundaries, org-admin-app-admin.md §1 | 계정 정책 연계 | Functional |
| SC-DFR-002 | High | Functional, Data | EP, BVA | 조직 식별자 입력 시 유효성 검증이 동작한다 | 1-10글자, 영어/숫자만 허용, 경계값 검증 | 기획서 §기본 구조 및 국가 코드 로직 | | Functional, Boundary, Negative |
| SC-DFR-003 | High | Business, Data | DT | 국가 코드가 우선순위에 따라 올바르게 결정된다 | 4단계 우선순위 로직 (Reporter's Country Primary > First > Event Occurred Primary > First > KR 기본값) | 기획서 §기본 구조 및 국가 코드 로직 | | Functional |
| SC-DFR-004 | High | Functional, Business | DT | 연도 설정 옵션에 따라 Case ID 포맷과 리셋 정책이 올바르게 적용된다 | 5가지 연도 옵션 (2-digit, 4-digit, Year-Month Short/Full, N/A) 및 각 리셋 정책 검증 | 기획서 §Year | | Functional |
| SC-DFR-005 | High | Business, Data | DT, EP | Type of Report 설정에 따라 보고 구분 코드가 올바르게 매핑된다 | Spontaneous→SP, Report from Study→RS, Other→OT, Not Available→UN 매핑 정확성 | 기획서 §Type of Report | | Functional |
| SC-DFR-006 | Medium | Functional, Data | EP | Product Abbreviation 설정 시 제품 약어가 올바르게 참조된다 | Product Config에서 약어 참조, 값 없을 시 UNK 표시, 복수 자사제품 시 첫 번째 사용 | 기획서 §Product Abbreviation 추가 | | Functional |
| SC-DFR-007 | Medium | Functional, Data | EP, BVA | 자유 텍스트 입력 시 유효성 검증이 동작한다 | 1-6글자, 영어/숫자만 허용 | 기획서 §자유 텍스트 추가 | | Functional, Boundary, Negative |
| SC-DFR-008 | High | Functional, Business | BVA | 일련번호 자릿수 설정이 올바르게 적용된다 | 3-9자리 선택 및 Zero-padding 적용 검증 | 기획서 §일련번호 자릿수 설정 | | Functional, Boundary |
| SC-DFR-009 | Medium | Business, Data | EP, BVA | 시작 번호 설정이 올바르게 적용된다 | 시작 번호 입력 및 첫 번째 Case ID 생성 검증, 자릿수와 조합 | 기획서 §시작 번호 설정 | | Functional |
| SC-DFR-010 | Medium | Functional | UC | 포맷 순서 드래그 앤 드롭이 정상 동작한다 | 칩 추가/제거, 순서 변경, Preview 실시간 반영 | 기획서 §포맷 설정 및 인터랙션 | | Functional |
| SC-DFR-011 | Critical | Business, Data | DT, DR | 케이스 생성 시 설정된 Default Rule에 따라 Case ID가 올바르게 자동 부여된다 | Manual 케이스 생성 시 C.1.1, C.1.8.1 동일하게 부여, 국가코드-조직-일련번호 형식 | 기획서 §매뉴얼 케이스 생성 | 핵심 비즈니스 플로우 | Functional |
| SC-DFR-012 | Critical | Business, Data | DT, DLA | 케이스 삭제 후에도 해당 일련번호가 재사용되지 않는다 | 삭제된 케이스의 번호 재사용 금지 정책 검증 | 기획서 §개요 및 정책 | 데이터 무결성 | Functional |
| SC-DFR-013 | High | Business, Flow | ST | 연도/연월 설정에 따라 일련번호가 올바르게 리셋된다 | 연 단위(매년 1월 1일)/월 단위(매월 1일) 리셋, N/A 시 누적 | 기획서 §Year | 시간 기반 상태 전이 | Functional |
| SC-DFR-014 | High | Business, Functional | DT | 일련번호 만료 임박 시 팝업 알림이 올바르게 표시된다 | 남은 번호 200개 이하일 때 팝업 노출, 현재 Case ID, 최대값, 확장 후 예시 표시 | 기획서 §Case ID 만료 임박 알림 | | Functional |
| SC-DFR-015 | High | Business, Data | ST | 사용자가 만료 알림 팝업에서 올바르게 상호작용할 수 있다 | Confirm 클릭 시 닫힘/재로그인 시 재노출, Do not show again 체크 시 영구 미노출, 자릿수 변경 후 미노출 | 기획서 §사용자 인터랙션 및 제어 | | Functional |
| SC-DFR-016 | Critical | Business, Data | ST, DR | 일련번호가 최대치에 도달하면 자릿수가 자동 확장된다 | 5자리 99999 초과 시 100000(6자리) 자동 전환, 서비스 중단 없음 | 기획서 §Case ID 자릿수 자동 확장 | 서비스 연속성 보장 | Functional |
| SC-DFR-017 | High | Business, Data | DT | Import 시 C.1.8.1만 유지 옵션이 올바르게 동작한다 | C.1.1 신규 부여, C.1.8.1 파일 내 값 유지 | 기획서 §Import 설정 옵션 A | | Functional |
| SC-DFR-018 | High | Business, Data | DT | Import 시 C.1.1, C.1.8.1 모두 유지 옵션이 올바르게 동작한다 | C.1.1, C.1.8.1 모두 파일 내 값 사용 | 기획서 §Import 설정 옵션 B | | Functional |
| SC-DFR-019 | High | Business, Data | DT | C.1.8.1이 없을 때 C.1.1 값 Sync 설정이 올바르게 동작한다 | C.1.8.1이 Null인 경우 C.1.1 값 복사 | 기획서 §C.1.1, C.1.8.1 동일 입력 설정 | | Functional |
| SC-DFR-020 | High | Functional, Business | UC, DR | Case Edit에서 C.1.1 수정 시 경고 후 Sync 해제가 올바르게 동작한다 | 수정 버튼 → 경고 얼럿 → Confirm/Cancel 동작 검증 | 기획서 §C.1.1 동작 설정 | | Functional |
| SC-DFR-021 | Critical | Business, Flow | ST, DR | Approval 상태 이후 C.1.1, C.1.8.1 수정이 차단된다 | Approval 이후 수정 버튼 미표시, 안내 문구 표시 | 기획서 §C.1.1 변경 시점 | 규제 준수 | Functional |
| SC-DFR-022 | High | Functional, Business | EP | Case Level과 Report Level에서 식별자가 올바른 형식으로 노출된다 | Tracker/Case에서 일련번호, ICSR 보고서에서 국가-조직-일련번호 형식 | 기획서 §Case vs Report 식별자 노출 사양 | | Functional |
| SC-DFR-023 | High | Data, Business | DLA | Default Rule 설정 변경이 저장 후 새로 생성되는 케이스에만 적용된다 | 설정 변경 전 케이스 영향 없음, 변경 후 케이스만 새 규칙 적용 | 기획서 §일련번호 자릿수 설정, §시작 번호 설정 | | Functional |
| SC-DFR-024 | Medium | Functional | EP | Preview 영역이 상단 고정되어 스크롤 시에도 유지된다 | Preview 영역 상단 sticky 동작 | 기획서 §포맷 설정 및 인터랙션 | UI 동작 | Functional |
| SC-DFR-025 | Medium | Functional, Business | EP | 칩 활성화/비활성화 시 해당 설정 영역이 올바르게 토글된다 | 칩 추가 시 하단 영역 활성화, X 클릭 시 비활성화(값 유지) | 기획서 §포맷 설정 및 인터랙션 | | Functional |
| SC-DFR-026 | High | Data | DLA, DR | 설정 저장 시 감사 로그가 올바르게 기록된다 | Default Rule 설정 변경 내역이 Audit Log에 기록 | multi-org.md §3.1 Org Data | 감사추적성 | Functional |
| SC-DFR-027 | Medium | Business | EP | 연도 설정 영역의 툴팁이 올바르게 표시된다 | 툴팁 호버 시 리셋 정책 안내 메시지 표시 | 기획서 §Year | | Functional |
| SC-DFR-028 | High | Business, Data | DT | C.1.1이 Initial 사례에만 자동 부여되고 Follow-up에는 부여되지 않는다 | Initial 케이스에만 C.1.1 부여, Follow-up은 기존 값 유지 | 기획서 §C.1.1 변경 시점 | | Functional |
| SC-DFR-029 | Medium | Functional, Business | EP | Import 설정 옵션 변경 시 해당 설정만 저장된다 | 옵션 A/B 선택 변경 및 저장 동작 | 기획서 §Import 설정 | | Functional |
| SC-DFR-030 | High | Business, Data | DT, DR | 동시에 여러 케이스 생성 시에도 일련번호가 중복 없이 순차 부여된다 | 병렬 처리(최대 30개) 시에도 번호 고유성 유지 | 기획서 §팝업 노출 조건 | 동시성 | Functional |

---

## 요구사항 추적 매트릭스 (RTM)

| 요구사항 ID | 요구사항 내용 | 유형 | 제외 여부 | 연관 시나리오 ID | TC ID 범위 | 상태 |
|------------|-------------|------|---------|----------------|-----------|------|
| REQ-DFR-001 | 설정 가능한 모든 텍스트는 영문 및 숫자만 가능하며 대소문자 구분 | 데이터 규칙 | - | SC-DFR-002, SC-DFR-007 | - | ⏳ 시나리오 완료 |
| REQ-DFR-002 | ID 재사용 방지: 삭제된 케이스 번호 재사용 금지 | 비즈니스 규칙 | - | SC-DFR-012 | - | ⏳ 시나리오 완료 |
| REQ-DFR-003 | 국가 코드 우선순위: Reporter's Country > Event Occurred Country > KR 기본값 | 비즈니스 규칙 | - | SC-DFR-003 | - | ⏳ 시나리오 완료 |
| REQ-DFR-004 | 조직 식별자 1-10글자 영어/숫자만 입력 가능 | 데이터 규칙 | - | SC-DFR-002 | - | ⏳ 시나리오 완료 |
| REQ-DFR-005 | Year 5가지 옵션 및 각 리셋 정책 | 기능 명세 | - | SC-DFR-004, SC-DFR-013 | - | ⏳ 시나리오 완료 |
| REQ-DFR-006 | Type of Report 코드 매핑 (SP/RS/OT/UN) | 비즈니스 규칙 | - | SC-DFR-005 | - | ⏳ 시나리오 완료 |
| REQ-DFR-007 | Product Abbreviation Product Config 참조, 없으면 UNK | 데이터 규칙 | - | SC-DFR-006 | - | ⏳ 시나리오 완료 |
| REQ-DFR-008 | 자유 텍스트 1-6글자 영어/숫자만 | 데이터 규칙 | - | SC-DFR-007 | - | ⏳ 시나리오 완료 |
| REQ-DFR-009 | 일련번호 자릿수 3-9자리 선택 가능 | 기능 명세 | - | SC-DFR-008 | - | ⏳ 시나리오 완료 |
| REQ-DFR-010 | 시작 번호 설정 가능, 디폴트 1 | 기능 명세 | - | SC-DFR-009 | - | ⏳ 시나리오 완료 |
| REQ-DFR-011 | 포맷 Drag & Drop 및 Preview 실시간 반영 | 기능 명세 | - | SC-DFR-010, SC-DFR-024, SC-DFR-025 | - | ⏳ 시나리오 완료 |
| REQ-DFR-012 | Case ID 만료 임박 알림 (200개 이하) | 기능 명세 | - | SC-DFR-014, SC-DFR-015 | - | ⏳ 시나리오 완료 |
| REQ-DFR-013 | 자릿수 자동 확장 (서비스 중단 없이) | 비즈니스 규칙 | - | SC-DFR-016 | - | ⏳ 시나리오 완료 |
| REQ-DFR-014 | Import 설정 옵션 A: C.1.8.1만 유지 | 기능 명세 | - | SC-DFR-017 | - | ⏳ 시나리오 완료 |
| REQ-DFR-015 | Import 설정 옵션 B: C.1.1, C.1.8.1 모두 유지 | 기능 명세 | - | SC-DFR-018 | - | ⏳ 시나리오 완료 |
| REQ-DFR-016 | C.1.8.1 Null 시 C.1.1 값 복사 (Sync 설정) | 비즈니스 규칙 | - | SC-DFR-019 | - | ⏳ 시나리오 완료 |
| REQ-DFR-017 | C.1.1 수정 시 경고 후 Sync 해제 | 기능 명세 | - | SC-DFR-020 | - | ⏳ 시나리오 완료 |
| REQ-DFR-018 | Approval 상태 이후 C.1.1, C.1.8.1 수정 불가 | 비즈니스 규칙 | - | SC-DFR-021 | - | ⏳ 시나리오 완료 |
| REQ-DFR-019 | Case Level 일련번호만, Report Level 국가-조직-일련번호 | 화면 상태 | - | SC-DFR-022 | - | ⏳ 시나리오 완료 |
| REQ-DFR-020 | Initial 사례에만 C.1.1 부여 | 비즈니스 규칙 | - | SC-DFR-028 | - | ⏳ 시나리오 완료 |
| REQ-DFR-021 | 병렬 처리(최대 30개) 시에도 번호 중복 방지 | 비즈니스 규칙 | - | SC-DFR-030 | - | ⏳ 시나리오 완료 |
| REQ-DFR-022 | 권한: Master Admin, Org Admin만 설정 가능 | 권한/역할 | - | SC-DFR-001 | - | ⏳ 시나리오 완료 |
| REQ-DFR-023 | 설정 변경 감사 로그 기록 | 비즈니스 규칙 | - | SC-DFR-026 | - | ⏳ 시나리오 완료 |
| REQ-DFR-024 | 케이스 생성 시 C.1.1 자동 부여 (Manual) | 기능 명세 | - | SC-DFR-011 | - | ⏳ 시나리오 완료 |
| REQ-DFR-025 | 설정 변경은 이후 생성 케이스에만 적용 | 비즈니스 규칙 | - | SC-DFR-023 | - | ⏳ 시나리오 완료 |
| REQ-DFR-026 | Convert 적용 | 기능 명세 | ➖ (추후 개발) | - | - | ➖ 제외 |

> **상태 값**: `✅ TC 완료` / `⏳ 시나리오 완료` / `❌ 미작성` / `➖ 제외`

---

## 확인 필요 사항

| No | 관련 시나리오 | 질문 내용 | 상태 |
|----|-------------|----------|------|
| 1 | SC-DFR-001 | Default Rule 설정 화면 접근 권한이 App Admin에게도 부여되는지, 아니면 Master/Org Admin만 가능한지 명확한 확인 필요 (기획서에 명시적 언급 없음) | 미확인 |
| 2 | SC-DFR-003 | 국가 코드가 결정되는 정확한 시점 - 케이스 '생성' 시점인지, Destination(보고처) '확정' 시점인지 명확화 필요 (기획서 내 "케이스 생성 시점"과 "Destination 확정 시점" 문구 혼용) | 미확인 |
| 3 | SC-DFR-013 | 연도/연월 리셋 시점이 KST 기준인지, UTC 기준인지 명시 필요 (기획서에 "1월 1일 00:00:00" 언급하나 타임존 미명시) | 미확인 |
| 4 | SC-DFR-016 | 자릿수 자동 확장 시 Admin에게 별도 알림이 발송되는지 확인 필요 | 미확인 |
| 5 | SC-DFR-026 | Audit Log에 기록되는 Default Rule 설정 변경 항목의 세부 범위 (모든 필드 변경 vs 주요 항목만) | 미확인 |
| 6 | - | 자유 텍스트가 비활성화된 상태에서 이전 설정값이 유지되는 경우, 재활성화 시 해당 값이 그대로 사용되는지 기본값으로 리셋되는지 확인 필요 | 미확인 |

---

## 리뷰 이력

| 일자 | 참석자 | 주요 결정 사항 |
|-----|-------|--------------|
| 2026-04-15 | AI (초안) | 초안 작성 완료. 팀 리뷰 대기 |

---

## 참고 사항

### 상위 기획서 연계 사항

| 상위 기획서 | 연계 내용 | 적용 시나리오 |
|-----------|----------|-------------|
| multi-org.md | Master Admin, Org Admin 역할 정의 및 권한 범위 | SC-DFR-001 |
| multi-org.md | Org Data 범위 정의 (Audit Trail, Activity Log) | SC-DFR-026 |
| org-admin-app-admin.md | Org Admin 메뉴 접근 권한 및 설정 주체 정의 | SC-DFR-001 |
| home-navigation.md | Org 홈 > Admin 메뉴 접근 경로 | SC-DFR-001 |

### 상태 전이 다이어그램

```
케이스 워크플로우 상태에 따른 C.1.1/C.1.8.1 수정 가능 여부:

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Draft     │ →  │  In Review  │ →  │  Approval   │
│  (수정가능)  │    │  (수정가능)  │    │ (수정불가)   │
└─────────────┘    └─────────────┘    └─────────────┘
                                            │
                            수정 버튼 미표시 + 안내 문구

일련번호 리셋 상태 전이 (Year 설정별):

2-digit/4-digit Year:
  [연간 누적] ──(매년 1월 1일 00:00:00)──→ [00001로 리셋]

Year-Month (Short/Full):
  [월간 누적] ──(매월 1일 00:00:00)──→ [00001로 리셋]

N/A:
  [전체 누적] ──(리셋 없음)──→ [계속 누적]
```

### Case ID 구조 예시

```
기본 구조: [국가코드]-[조직 식별자]-[설정된 번호 조합]

예시 1: KR-SELTA-2600001SP
- 국가코드: KR (한국)
- 조직 식별자: SELTA
- 연도: 26 (2-digit)
- 일련번호: 00001 (5자리)
- 보고구분: SP (Spontaneous)

예시 2: KR-SELTA-202604ST001
- 국가코드: KR
- 조직 식별자: SELTA
- 연월: 202604 (Year-Month Full)
- 자유텍스트: ST
- 일련번호: 001 (3자리)
```

### 입력 필드 Validation 요약

| 필드 | 최소 | 최대 | 허용 문자 | 필수 여부 |
|-----|-----|-----|---------|---------|
| 조직 식별자 | 1자 | 10자 | 영어(대소문자), 숫자 | 필수 |
| 자유 텍스트 | 1자 | 6자 | 영어, 숫자 | 선택 |
| 일련번호 자릿수 | 3 | 9 | - | 필수 |
| 시작 번호 | 1 | 자릿수 최대값 | 숫자 | 디폴트 1 |

---

## TC 매핑 상태

| 시나리오 ID | TC 작성 상태 | TC 수 | 비고 |
|-----------|------------|-------|------|
| SC-DFR-001 | 미작성 | - | |
| SC-DFR-002 | 미작성 | - | |
| SC-DFR-003 | 미작성 | - | |
| SC-DFR-004 | 미작성 | - | |
| SC-DFR-005 | 미작성 | - | |
| SC-DFR-006 | 미작성 | - | |
| SC-DFR-007 | 미작성 | - | |
| SC-DFR-008 | 미작성 | - | |
| SC-DFR-009 | 미작성 | - | |
| SC-DFR-010 | 미작성 | - | |
| SC-DFR-011 | 미작성 | - | |
| SC-DFR-012 | 미작성 | - | |
| SC-DFR-013 | 미작성 | - | |
| SC-DFR-014 | 미작성 | - | |
| SC-DFR-015 | 미작성 | - | |
| SC-DFR-016 | 미작성 | - | |
| SC-DFR-017 | 미작성 | - | |
| SC-DFR-018 | 미작성 | - | |
| SC-DFR-019 | 미작성 | - | |
| SC-DFR-020 | 미작성 | - | |
| SC-DFR-021 | 미작성 | - | |
| SC-DFR-022 | 미작성 | - | |
| SC-DFR-023 | 미작성 | - | |
| SC-DFR-024 | 미작성 | - | |
| SC-DFR-025 | 미작성 | - | |
| SC-DFR-026 | 미작성 | - | |
| SC-DFR-027 | 미작성 | - | |
| SC-DFR-028 | 미작성 | - | |
| SC-DFR-029 | 미작성 | - | |
| SC-DFR-030 | 미작성 | - | |
