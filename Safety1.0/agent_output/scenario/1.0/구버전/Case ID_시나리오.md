# Case ID 테스트 시나리오

## 개요
- 기획서: `plan/Case ID - iVigilance Square - Confluence_20260424.md`
- RTM 버전: v1 (design-validator 완료)
- 작성 기준일: 2026-04-27
- 기능 범위: ICSR Case ID 생성 규칙 설정, 번호 채번 정책, 만료 경고, Import 식별자 처리, Case/Report Level 식별자 노출
- 제외 범위: AI Convert 적용(추후 예정), Tracker/Case Edit 별도 캔버스 검증 항목(OOS — 본 RTM에 포함하되 Figma 검증은 별도)
- Figma 캔버스: ICSR Config > Case ID (node-id=18831-28173), 대상 프레임 `Case ID Rule/W1440` (18831-28629)

### 주요 용어
| 용어 | 정의 |
|------|------|
| Case ID | ICSR 케이스의 `[설정된 번호 조합]` 부분. Tracker·Case Edit에서는 이 값만 표시 |
| C.1.1 | E2B R3 보고자 관리번호. `[국가코드]-[조직 식별자]-[설정된 번호 조합]` 형식. Initial 케이스 생성 시 부여 |
| C.1.8.1 | E2B R3 고유식별 보고자 관리번호. 중복 체크·Follow-up 연결 기준 |
| Initial | 최초 생성 케이스 (Follow-up 아닌 케이스) |
| Follow-up | 기존 케이스에 추가 정보로 이어지는 후속 보고서 |
| Import | XML 파일을 통해 케이스를 시스템에 인입하는 기능 |
| Zero-padding | 일련번호 앞자리에 '0'을 채우는 방식 (예: 5자리 설정 → 00001) |
| Destination | 보고처. C.1.1의 국가코드는 Destination 확정 시점에 결정됨 |

---

## 기능 분해

| 화면/업무 흐름 | 기능 영역 | 세부 동작 | 관련 근거 |
|--------------|----------|----------|---------|
| Case ID 설정 화면 | 기본 구조 정책 | 설정 가능한 모든 텍스트는 영문·숫자만 허용, 대소문자 구분 | §개요 및 정책 |
| Case ID 설정 화면 | 기본 구조 정책 | 삭제된 케이스의 일련번호 재사용 절대 금지 | §개요 및 정책 |
| Case ID 설정 화면 | 조직 식별자 설정 | 텍스트 직접 입력 (최소 1자, 최대 10자, 영숫자) | §기본 구조 및 국가 코드 로직 |
| Case ID 설정 화면 | 국가코드 결정 | 4단계 우선순위 자동 결정 (Reporter Primary → Reporter First → Event Country Primary → Event Country First → KR 기본값) | §기본 구조 및 국가 코드 로직 |
| Case ID 설정 화면 | Year 설정 | 라디오버튼 선택 (2-digit YY / 4-digit YYYY / N/A), 선택 시 리셋 정책 자동 결정 | §Year |
| Case ID 설정 화면 | Year 설정 | 툴팁 제공 — 연도/연월/N/A 선택별 초기화 정책 안내 | §Year |
| Case ID 설정 화면 | Type of Report 설정 | 체크 시 케이스 Type 값에 따라 구분자 자동 추가 (SP/RS/OT/UN) | §Type of Report |
| Case ID 설정 화면 | Product Abbreviation 설정 | Product Config 약어 참조, 없으면 UNK, Suspect 자사 제품 2개 이상 시 첫 번째 | §Product Abbreviation |
| Case ID 설정 화면 | 자유 텍스트 설정 | 칩 추가 → Custom Text 블록 활성화 → 영숫자 입력 (최소 1자, 최대 6자) | §자유 텍스트 추가 |
| Case ID 설정 화면 | 일련번호 자릿수 설정 | 드롭다운 선택 (3~9자리), Zero-padding 적용 | §일련번호 자릿수 설정 |
| Case ID 설정 화면 | 일련번호 자릿수 설정 | 자릿수 변경 시 이후 생성 케이스부터 적용 | §일련번호 자릿수 설정 |
| Case ID 설정 화면 | 시작 번호 설정 | 시작점 지정 (기본값 1, 숫자 N 입력 시 N부터 카운팅) | §시작 번호 설정 |
| Case ID 설정 화면 | 시작 번호 설정 | 상한 제한: 최대 생성 가능 숫자 - 400 초과 불가 | §시작 번호 설정 제한 정책 |
| Case ID 설정 화면 | 최후 번호 검증 | 동일 조합 내 이미 생성된 최후 번호보다 커야 함 | §최후 번호 검증 규칙 |
| Case ID 설정 화면 | 포맷 설정(D&D) | 칩 추가/삭제/순서 변경 → Preview 실시간 반영 | §포맷 설정 및 인터랙션 |
| Case ID 설정 화면 | 포맷 설정(D&D) | 활성화 조건: Year 연도 선택 또는 Type of Report 체크 시만 활성화 | §포맷 설정 및 인터랙션 |
| Case ID 설정 화면 | 포맷 설정(D&D) | 칩 X 클릭 시 하단 영역 비활성화, 이전 설정값 유지 | §포맷 설정 및 인터랙션 |
| Case ID 설정 화면 | Preview | 스크롤 시에도 상단 고정 | §와이어프레임 #1 |
| 케이스 생성 (Case 화면) | Case ID 만료 임박 팝업 | 남은 번호 ≤ 100일 때 팝업 노출 (Case ID 부여 시점) | §Case ID 만료 임박 알림 |
| 케이스 생성 (Case 화면) | Case ID 만료 임박 팝업 | 팝업 내용: 현재 마지막 Case ID + 자동 확장 안내 + New Case ID 예시 | §Case ID 만료 임박 알림 |
| 케이스 생성 (Case 화면) | Case ID 만료 임박 팝업 | 닫기 로직: Confirm → 다음 로그인 재노출 / Do not show again + Confirm → 미노출 | §사용자 인터랙션 및 제어 |
| 케이스 생성 (Case 화면) | Case ID 만료 임박 팝업 | 자동 미노출: 새 자릿수 체계로 넘어간 경우 기존 팝업 중단 | §사용자 인터랙션 및 제어 |
| 케이스 생성 시스템 | 자릿수 자동 확장 | 최대 자릿수 초과 시 1자리 추가, 1XXXXX 형식으로 시작 | §Case ID 자릿수 자동 확장 |
| Import 기능 | Import Option A | C.1.1 신규 부여 + C.1.8.1 파일 내 값 유지 | §Import 설정 |
| Import 기능 | Import Option B | C.1.1, C.1.8.1 모두 파일 내 값 사용 | §Import 설정 |
| Import 기능 | C.1.8.1 Null Sync | C.1.8.1 Null인 경우 C.1.1 값을 C.1.8.1에 복사 | §C.1.1, C.1.8.1 동일 입력 설정 |
| Case Edit 화면 | C.1.1 수정 제한 | 기본 수정 불가, 수정 버튼 클릭 → 경고 얼럿 → Confirm(Sync 해제)/Cancel | §C.1.1 동작 설정 |
| Case Edit 화면 | Approval 이후 수정 불가 | C.1.1, C.1.8.1 수정 버튼 비표시 + 안내 문구 노출 | §C.1.1 변경 시점 |
| Tracker / Case 화면 | Case Level 식별자 노출 | 일련번호만 표시 (국가코드·조직 식별자 미표시) | §Case vs Report 식별자 노출 사양 |
| ICSR 보고서 화면 | Report Level 식별자 노출 | 국가-조직-일련번호 형식으로 C.1.1, C.1.8.1 표시 | §Case vs Report 식별자 노출 사양 |

---

## 관점 매핑 요약

| 기능 영역 | Functional | Business | Data | Non-Functional | Flow | 비고 |
|----------|-----------|---------|------|---------------|------|------|
| 기본 구조 정책 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 영문숫자 제한, ID 재사용 방지 |
| 조직 식별자 설정 | 적용 | 미적용 | 적용 | 미적용 | 미적용 | 입력 유효성(BVA) |
| 국가코드 결정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 4단계 우선순위 |
| Year 설정 | 적용 | 적용 | 적용 | 미적용 | 적용 | 리셋 정책, 디자인이슈(ISSUE-001) |
| Type of Report 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | SP/RS/OT/UN 매핑 |
| Product Abbreviation 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 외부 참조, UNK fallback |
| 자유 텍스트 설정 | 적용 | 미적용 | 적용 | 미적용 | 미적용 | 입력 유효성, 디자인이슈(ISSUE-005) |
| 일련번호 자릿수 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 경계값, 적용 시점 |
| 시작 번호 설정 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 상한 제한, 최후 번호 검증 |
| 포맷 설정(D&D) | 적용 | 미적용 | 미적용 | 미적용 | 미적용 | 활성화 조건, Preview 실시간 반영 |
| Case ID 만료 임박 팝업 | 적용 | 적용 | 미적용 | 미적용 | 적용 | 디자인이슈(ISSUE-009 Critical) |
| 자릿수 자동 확장 | 적용 | 적용 | 적용 | 미적용 | 적용 | 서비스 연속성 |
| Import Option A/B | 적용 | 적용 | 적용 | 미적용 | 미적용 | 식별자 정합성 |
| C.1.8.1 Null Sync | 적용 | 적용 | 적용 | 미적용 | 미적용 | 식별자 보호 |
| C.1.1 수정 제한 | 적용 | 적용 | 적용 | 미적용 | 적용 | Sync 해제 흐름 |
| Approval 이후 수정 불가 | 적용 | 적용 | 적용 | 미적용 | 적용 | 상태 기반 제한, 규제 준수 |
| Case Level 식별자 노출 | 적용 | 적용 | 적용 | 미적용 | 미적용 | OOS(Tracker/Case Edit) |
| Report Level 식별자 노출 | 적용 | 적용 | 적용 | 미적용 | 미적용 | C.1.1/C.1.8.1 형식 |

---

## 시나리오 목록

| ID | 우선순위 | 관점 태그 | 도출 기법 | 시나리오 제목 | 검증 목적 | 근거 | 비고 |
|----|---------|----------|----------|------------|----------|------|------|
| SC-CID-001 | High | Functional, Data | BVA | 조직 식별자 입력 시 유효성 검증이 동작한다 | 최소 1자~최대 10자, 영숫자만 허용, 경계값 및 무효 문자 차단 검증 | REQ-003 (§기본 구조 및 국가 코드 로직) | |
| SC-CID-002 | High | Business, Data | DT | 국가코드가 4단계 우선순위에 따라 올바르게 결정된다 | Reporter Primary → Reporter First → Event Country Primary → Event Country First → KR 기본값 순서 검증 | REQ-002 (§기본 구조 및 국가 코드 로직) | |
| SC-CID-003 | High | Functional, Business | DT | Year 설정 옵션 선택 시 Case ID 포맷과 리셋 정책이 올바르게 결정된다 | 2-digit(YY)/4-digit(YYYY)/N/A 선택별 포맷 반영 및 리셋 정책 검증 | REQ-004, REQ-005 (§Year) | [디자인이슈] ISSUE-001 Critical: Figma에 N/A 옵션 누락 — N/A 옵션 구현 여부 확인 후 TC 설계 |
| SC-CID-004 | Medium | Functional | EP | Year 설정 툴팁이 올바른 내용으로 표시된다 | 툴팁 호버 시 연도/연월/N/A 각 초기화 정책 안내 문구 정확성 검증 | REQ-006 (§Year) | [디자인이슈] ISSUE-002 Major: Figma 툴팁 문구 "미선택 시"로 변경·월 초기화 문구 삭제 → 기획서 문구와 불일치 |
| SC-CID-005 | High | Business, Data | DT | Type of Report 체크 시 케이스 Type 값에 따라 구분자가 Case ID에 올바르게 추가된다 | Spontaneous→SP, Report from Study→RS, Other→OT, Not Available→UN 매핑 정확성 검증 | REQ-007 (§Type of Report) | |
| SC-CID-006 | Medium | Business, Data | EP | Product Abbreviation이 Product Config 약어를 올바르게 참조하고 예외 조건이 처리된다 | 약어 없을 시 UNK 표시, Suspect 자사 제품 2개 이상 시 첫 번째 약어 사용 | REQ-008 (§Product Abbreviation) | |
| SC-CID-007 | Medium | Functional, Data | BVA | 자유 텍스트 칩 추가 및 텍스트 입력 시 유효성 검증이 동작한다 | 최소 1자~최대 6자, 영숫자만 허용, 경계값 검증 | REQ-009 (§자유 텍스트 추가) | [디자인이슈] ISSUE-005 Major: Figma는 칩+Text Input 방식, 기획서는 체크박스/라디오 혼용 → UI 컴포넌트 확정 필요 / ISSUE-006 Minor: helper 문구에 최소 1자 미표기 |
| SC-CID-008 | High | Functional, Business | BVA | 일련번호 자릿수 드롭다운 선택이 Zero-padding에 정확히 반영된다 | 선택 가능 범위(3~9자리) 및 Zero-padding 정확성 검증, 자릿수 변경 시 이후 케이스부터 적용 | REQ-010, REQ-011 (§일련번호 자릿수 설정) | [디자인이슈] ISSUE-003 Major: Figma 기본값 5자리, 드롭다운 옵션 3~9 vs 5~9 불확실 — [확인 필요] |
| SC-CID-009 | High | Business, Data | DT, BVA | 시작 번호 설정이 올바르게 적용되고 상한 및 최후 번호 검증이 동작한다 | 시작 번호 N 입력 시 N부터 카운팅, 상한(최대-400) 초과 차단, 최후 번호보다 커야 하는 검증 | REQ-012, REQ-013, REQ-014 (§시작 번호 설정, §시작 번호 설정 제한 정책, §최후 번호 검증 규칙) | [디자인이슈] ISSUE-004 Minor: 상한 및 최후 번호 검증 UI(에러/경고) Figma 미반영 |
| SC-CID-010 | Medium | Functional | UC | 포맷 설정 영역에서 칩 추가/삭제/순서 변경 시 Preview에 실시간 반영된다 | 칩 D&D 조작, X 클릭 시 비활성화(값 유지), 활성화 조건 검증 | REQ-015, REQ-016, REQ-017 (§포맷 설정 및 인터랙션) | |
| SC-CID-011 | Low | Functional | EP | Preview 영역이 스크롤 시에도 상단 고정된다 | 긴 설정 화면에서 스크롤 시 Preview sticky 동작 유지 | REQ-018 (§와이어프레임 #1) | |
| SC-CID-012 | Critical | Business, Data | DT, DR | 남은 번호가 100개 이하일 때 Case ID 부여 시점에 만료 임박 팝업이 올바르게 노출된다 | 팝업 노출 조건(임계치 100개), 팝업 내용(현재 마지막 Case ID + 자동 확장 안내 + New Case ID 예시), 노출 시점(Case ID 부여 순간) 검증 | REQ-019, REQ-020 (§팝업 노출 조건, §Case ID 만료 임박 알림) | [디자인이슈] ISSUE-009 Critical: 본 캔버스(ICSR Config > Case ID)에 팝업 미반영 — Case 생성 화면 Figma URL 확보 후 별도 검증 필요 |
| SC-CID-013 | High | Functional, Business | ST | 만료 임박 팝업에서 사용자 인터랙션이 올바르게 처리된다 | Confirm → 다음 로그인 재노출 / Do not show again + Confirm → 영구 미노출 / 새 자릿수 체계 전환 시 기존 팝업 자동 중단 | REQ-021, REQ-022 (§사용자 인터랙션 및 제어) | [확인 필요] Do not show again의 적용 범위가 사용자별인지 시스템 전체인지 미명시 |
| SC-CID-014 | Critical | Business, Data | ST, DR | 일련번호가 최대치 초과 시 자릿수가 자동으로 1자리 확장되고 서비스가 중단되지 않는다 | 5자리 99999 이후 100000(6자리)으로 자동 전환, 서비스 중단 없이 번호 연속 부여 검증 | REQ-023 (§Case ID 자릿수 자동 확장) | 규제/업무 연속성(PV 케이스 채번 중단 시 보고 지연 위험) |
| SC-CID-015 | High | Business, Data | DT | Import Option A 적용 시 C.1.1은 신규 부여되고 C.1.8.1은 파일 내 값이 유지된다 | Import 후 C.1.1 신규 부여 확인, C.1.8.1 파일 내 원본값 보존 확인 | REQ-024 (§Import 설정) | [디자인이슈] ISSUE-008 Info: Figma에 '권장' 배지 추가 — 기획서 표기 보완 필요(기능 영향 없음) |
| SC-CID-016 | High | Business, Data | DT | Import Option B 적용 시 C.1.1, C.1.8.1 모두 파일 내 값이 그대로 사용된다 | Import 후 C.1.1, C.1.8.1 모두 파일 내 원본값 보존 확인 | REQ-025 (§Import 설정) | |
| SC-CID-017 | High | Business, Data | DT | C.1.8.1이 Null인 경우 C.1.1 값이 C.1.8.1에 올바르게 복사된다 | C.1.8.1 Null 케이스에서 C.1.1 값 Sync 확인, 기존 C.1.8.1 값이 있을 시 덮어쓰지 않음을 확인 | REQ-026 (§C.1.1, C.1.8.1 동일 입력 설정) | |
| SC-CID-018 | Critical | Business, Data | DR | Case ID가 한 번 부여되면 수동 수정이 절대 불가하다 | 시스템 부여 직후 사용자 편집 UI 미노출, 직접 편집 시도 차단 검증 | REQ-029 (§식별자 수정 및 변경 정책) | PV 데이터 무결성(C.1.1 임의 변경 시 규제 추적성 훼손 위험) |
| SC-CID-019 | High | Functional, Business | UC, DR | Case Edit에서 C.1.1 수정 버튼 클릭 시 경고 얼럿이 표시되고 Confirm/Cancel 분기가 올바르게 동작한다 | 수정 버튼 → 경고 얼럿 → Confirm 시 Sync 해제 + 수동 수정 가능 / Cancel 시 원래 상태 유지 | REQ-030 (§C.1.1 동작 설정) | OOS (Case Edit 캔버스 별도 검증 필요) |
| SC-CID-020 | Critical | Business, Flow | ST, DR | Approval 상태 이후 C.1.1, C.1.8.1 수정이 차단되고 안내 문구가 표시된다 | Approval 이후 수정 버튼 비표시, 안내 문구 정확성 검증 | REQ-031 (§C.1.1 변경 시점) | OOS (Case Edit 캔버스 별도 검증 필요) / PV 규제 준수(Approval 이후 식별자 변경 시 규제 위반 위험) |
| SC-CID-021 | High | Functional, Business | EP | Case Level 화면에서 Case ID가 일련번호 형식으로만 표시된다 | Tracker, Case Edit에서 [설정된 번호 조합]만 표시, 국가코드·조직 식별자 미포함 확인 | REQ-027 (§Case vs Report 식별자 노출 사양) | OOS (Tracker/Case Edit 캔버스 별도 검증 필요) |
| SC-CID-022 | High | Functional, Business | EP | Report Level(ICSR 보고서)에서 C.1.1, C.1.8.1이 [국가]-[조직]-[일련번호] 형식으로 표시된다 | ICSR 보고서 내 C.1.1, C.1.8.1 표시 형식 정확성 검증 | REQ-028 (§Case vs Report 식별자 노출 사양) | |
| SC-CID-023 | Critical | Data | DLA | 케이스 삭제 후에도 해당 일련번호가 이후 케이스에 재사용되지 않는다 | 삭제된 케이스의 번호가 다음 채번 시 건너뛰어짐을 확인 | REQ-001 (§개요 및 정책) | ID 재사용 방지 — PV 케이스 고유성 훼손 위험 |
| SC-CID-024 | Medium | Business, Data | EG | 동시에 여러 케이스 생성 시에도 일련번호가 중복 없이 순차 부여된다 | 병렬 처리(최대 30개) 시에도 번호 고유성 및 순차성 유지 | §팝업 노출 조건(최대 30개 병렬 처리 언급) | 동시성 리스크 |
| SC-CID-025 | Medium | Data, Business | DLA | 자릿수 설정 변경 후 변경 전 케이스에는 영향이 없고 변경 후 신규 케이스부터 새 설정이 적용된다 | 변경 전 케이스 Case ID 불변 확인, 변경 후 신규 케이스에 새 자릿수 적용 확인 | REQ-011 (§일련번호 자릿수 설정) | |

---

## 요구사항 추적 매트릭스 (RTM)

| 요구사항 ID | 요구사항 내용 | 유형 | 제외 여부 | 연관 시나리오 ID | TC ID 범위 | 상태 |
|------------|-------------|------|---------|----------------|-----------|------|
| REQ-001 | Case ID 기본 구조: [국가코드]-[조직 식별자]-[설정된 번호 조합] / ID 재사용 방지 | 데이터규칙 | - | SC-CID-023 | - | ⏳ 시나리오 완료 |
| REQ-002 | 국가코드 결정 우선순위 (Reporter Primary → Reporter First → Event Country Primary → Event Country First → KR) | 비즈니스규칙 | - | SC-CID-002 | - | ⏳ 시나리오 완료 |
| REQ-003 | 조직 식별자 입력 (1-10자, 영숫자, 대소문자 구분) | 기능명세 | - | SC-CID-001 | - | ⏳ 시나리오 완료 |
| REQ-004 | Year 설정 라디오 버튼 (2-digit YY / 4-digit YYYY / N/A 선택) | 기능명세 | - | SC-CID-003 | - | ⏳ 시나리오 완료 |
| REQ-005 | Year 선택 시 일련번호 리셋 정책 (연단위 매년 1월 1일 00:00:00 리셋 / N/A 누적) | 비즈니스규칙 | - | SC-CID-003 | - | ⏳ 시나리오 완료 |
| REQ-006 | Year 설정란 툴팁 제공 | 기능명세 | - | SC-CID-004 | - | ⏳ 시나리오 완료 |
| REQ-007 | Type of Report 체크박스 — 구분자 자동 추가 (SP/RS/OT/UN) | 비즈니스규칙 | - | SC-CID-005 | - | ⏳ 시나리오 완료 |
| REQ-008 | Product Abbreviation 자동 참조 (Product Config, 없으면 UNK, Suspect 자사 2개 이상 시 첫 번째) | 비즈니스규칙 | - | SC-CID-006 | - | ⏳ 시나리오 완료 |
| REQ-009 | 자유 텍스트 추가 (칩 방식, 1-6자, 영숫자) | 기능명세 | - | SC-CID-007 | - | ⏳ 시나리오 완료 |
| REQ-010 | 일련번호 자릿수 설정 드롭다운 (3~9자리, Zero-padding) | 기능명세 | - | SC-CID-008 | - | ⏳ 시나리오 완료 |
| REQ-011 | 자릿수 변경 시 이후 생성 케이스부터 적용 | 비즈니스규칙 | - | SC-CID-008, SC-CID-025 | - | ⏳ 시나리오 완료 |
| REQ-012 | 시작 번호 설정 (기본값 1, 숫자 N 입력 시 N부터 카운팅) | 기능명세 | - | SC-CID-009 | - | ⏳ 시나리오 완료 |
| REQ-013 | 시작 번호 상한 제한: 최대 생성 가능 숫자 - 400 초과 불가 | 비즈니스규칙 | - | SC-CID-009 | - | ⏳ 시나리오 완료 |
| REQ-014 | 최후 번호 검증: 동일 조합 내 이미 생성된 최대 번호보다 커야 함 | 비즈니스규칙 | - | SC-CID-009 | - | ⏳ 시나리오 완료 |
| REQ-015 | 포맷 설정 Drag & Drop (칩 순서 변경 → Preview 실시간 반영) | 기능명세 | - | SC-CID-010 | - | ⏳ 시나리오 완료 |
| REQ-016 | 포맷 설정 활성화 조건: Year 연도 선택 또는 Type of Report 체크 시만 활성화 | 비즈니스규칙 | - | SC-CID-010 | - | ⏳ 시나리오 완료 |
| REQ-017 | 칩 삭제(X) 시 하단 영역 비활성화, 이전 설정값 유지 | 기능명세 | - | SC-CID-010 | - | ⏳ 시나리오 완료 |
| REQ-018 | Preview 상단 고정 (스크롤 시에도 Preview 유지) | 기능명세 | - | SC-CID-011 | - | ⏳ 시나리오 완료 |
| REQ-019 | Case ID 만료 임박 팝업 (남은 번호 ≤ 100, Case ID 부여 시점에 즉시 노출) | 기능명세 | - | SC-CID-012 | - | ⏳ 시나리오 완료 |
| REQ-020 | 팝업 내용: 현재 마지막 Case ID + 자동 확장 안내 + New Case ID 예시 | 기능명세 | - | SC-CID-012 | - | ⏳ 시나리오 완료 |
| REQ-021 | 팝업 닫기 로직: Confirm → 다음 로그인 재노출 / Do not show again + Confirm → 미노출 | 기능명세 | - | SC-CID-013 | - | ⏳ 시나리오 완료 |
| REQ-022 | 팝업 자동 미노출: 새 자릿수 체계(1XXXXX...)로 넘어간 경우 기존 팝업 중단 | 비즈니스규칙 | - | SC-CID-013 | - | ⏳ 시나리오 완료 |
| REQ-023 | Case ID 자릿수 자동 확장: 최대 자릿수 초과 시 1자리 추가, 1XXXXX 형식으로 시작 | 비즈니스규칙 | - | SC-CID-014 | - | ⏳ 시나리오 완료 |
| REQ-024 | Import Option A: C.1.8.1 유지 + C.1.1 신규 부여 (Default) | 비즈니스규칙 | - | SC-CID-015 | - | ⏳ 시나리오 완료 |
| REQ-025 | Import Option B: C.1.1, C.1.8.1 모두 파일 내 값 유지 | 비즈니스규칙 | - | SC-CID-016 | - | ⏳ 시나리오 완료 |
| REQ-026 | C.1.8.1 없을 때 C.1.1 값을 C.1.8.1에 복사 | 비즈니스규칙 | - | SC-CID-017 | - | ⏳ 시나리오 완료 |
| REQ-027 | Case Level 식별자 표시 형식: 일련번호만 (Tracker, Case Edit) | 데이터규칙 | - | SC-CID-021 | - | ⏳ 시나리오 완료 |
| REQ-028 | Report Level 식별자 표시 형식: 국가-조직-일련번호 (C.1.1, C.1.8.1) | 데이터규칙 | - | SC-CID-022 | - | ⏳ 시나리오 완료 |
| REQ-029 | 식별자 수정 불가: 시스템 부여 즉시 수동 수정 절대 불가 | 기능명세 | - | SC-CID-018 | - | ⏳ 시나리오 완료 |
| REQ-030 | C.1.1 수동 수정 해지: 수정 버튼 → 얼럿 → Confirm(수정 허용+Sync 해제) / Cancel | 기능명세 | - | SC-CID-019 | - | ⏳ 시나리오 완료 |
| REQ-031 | C.1.1 Approval 이후 수정 불가 (수정 버튼 비표시, 안내 문구 노출) | 상태전이 | - | SC-CID-020 | - | ⏳ 시나리오 완료 |
| REQ-EX-001 | AI Convert 적용 (추후 예정) | 기능명세 | ➖ (추후 예정) | - | - | ➖ 제외 |

> **상태 값**: `✅ TC 완료` / `⏳ 시나리오 완료` / `❌ 미작성` / `➖ 제외`
> `TC ID 범위`는 TC 작성 완료 후 기입합니다.

---

## TC 매핑 상태

| 시나리오 ID | 시나리오 제목 | TC 유형 | TC ID 범위 | TC 작성 상태 |
|------------|-------------|--------|-----------|------------|
| SC-CID-001 | 조직 식별자 입력 시 유효성 검증이 동작한다 | Functional, Boundary, Negative | - | ⏳ 대기 |
| SC-CID-002 | 국가코드가 4단계 우선순위에 따라 올바르게 결정된다 | Functional | - | ⏳ 대기 |
| SC-CID-003 | Year 설정 옵션 선택 시 Case ID 포맷과 리셋 정책이 올바르게 결정된다 | Functional | - | ⏳ 대기 |
| SC-CID-004 | Year 설정 툴팁이 올바른 내용으로 표시된다 | Functional | - | ⏳ 대기 |
| SC-CID-005 | Type of Report 체크 시 케이스 Type 값에 따라 구분자가 Case ID에 올바르게 추가된다 | Functional | - | ⏳ 대기 |
| SC-CID-006 | Product Abbreviation이 Product Config 약어를 올바르게 참조하고 예외 조건이 처리된다 | Functional | - | ⏳ 대기 |
| SC-CID-007 | 자유 텍스트 칩 추가 및 텍스트 입력 시 유효성 검증이 동작한다 | Functional, Boundary, Negative | - | ⏳ 대기 |
| SC-CID-008 | 일련번호 자릿수 드롭다운 선택이 Zero-padding에 정확히 반영된다 | Functional, Boundary | - | ⏳ 대기 |
| SC-CID-009 | 시작 번호 설정이 올바르게 적용되고 상한 및 최후 번호 검증이 동작한다 | Functional, Boundary, Negative | - | ⏳ 대기 |
| SC-CID-010 | 포맷 설정 영역에서 칩 추가/삭제/순서 변경 시 Preview에 실시간 반영된다 | Functional | - | ⏳ 대기 |
| SC-CID-011 | Preview 영역이 스크롤 시에도 상단 고정된다 | Functional | - | ⏳ 대기 |
| SC-CID-012 | 남은 번호가 100개 이하일 때 Case ID 부여 시점에 만료 임박 팝업이 올바르게 노출된다 | Functional | - | ⏳ 대기 |
| SC-CID-013 | 만료 임박 팝업에서 사용자 인터랙션이 올바르게 처리된다 | Functional | - | ⏳ 대기 |
| SC-CID-014 | 일련번호가 최대치 초과 시 자릿수가 자동으로 1자리 확장되고 서비스가 중단되지 않는다 | Functional | - | ⏳ 대기 |
| SC-CID-015 | Import Option A 적용 시 C.1.1은 신규 부여되고 C.1.8.1은 파일 내 값이 유지된다 | Functional | - | ⏳ 대기 |
| SC-CID-016 | Import Option B 적용 시 C.1.1, C.1.8.1 모두 파일 내 값이 그대로 사용된다 | Functional | - | ⏳ 대기 |
| SC-CID-017 | C.1.8.1이 Null인 경우 C.1.1 값이 C.1.8.1에 올바르게 복사된다 | Functional | - | ⏳ 대기 |
| SC-CID-018 | Case ID가 한 번 부여되면 수동 수정이 절대 불가하다 | Functional, Security | - | ⏳ 대기 |
| SC-CID-019 | Case Edit에서 C.1.1 수정 버튼 클릭 시 경고 얼럿이 표시되고 Confirm/Cancel 분기가 올바르게 동작한다 | Functional | - | ⏳ 대기 |
| SC-CID-020 | Approval 상태 이후 C.1.1, C.1.8.1 수정이 차단되고 안내 문구가 표시된다 | Functional | - | ⏳ 대기 |
| SC-CID-021 | Case Level 화면에서 Case ID가 일련번호 형식으로만 표시된다 | Functional | - | ⏳ 대기 |
| SC-CID-022 | Report Level(ICSR 보고서)에서 C.1.1, C.1.8.1이 [국가]-[조직]-[일련번호] 형식으로 표시된다 | Functional | - | ⏳ 대기 |
| SC-CID-023 | 케이스 삭제 후에도 해당 일련번호가 이후 케이스에 재사용되지 않는다 | Functional | - | ⏳ 대기 |
| SC-CID-024 | 동시에 여러 케이스 생성 시에도 일련번호가 중복 없이 순차 부여된다 | Functional, Performance | - | ⏳ 대기 |
| SC-CID-025 | 자릿수 설정 변경 후 변경 전 케이스에는 영향이 없고 변경 후 신규 케이스부터 새 설정이 적용된다 | Functional | - | ⏳ 대기 |

> TC ID 범위는 TC 작성 완료 후 기입합니다.

---

## 확인 필요 사항

| No | 관련 시나리오 | 질문 내용 | 상태 |
|----|------------|---------|------|
| 1 | SC-CID-003 | [MISMATCH-001] 기획서 본문 "라디오 버튼으로 5가지 중 한가지 선택"이나 Year 표에는 3가지(2-digit, 4-digit, N/A)만 명시. 나머지 2가지 옵션은 무엇인가? Figma도 YY/YYYY 2가지만 노출(N/A 미반영). 기획서 표 기준 3가지로 확정 시 본문 문구 수정 필요 | 미확인 |
| 2 | SC-CID-008 | [MISMATCH-002] 기획서 §자릿수 설정 "3, 4, 5, 6, 7, 8, 9" vs 와이어프레임 area 5 "5, 6, 7, 8, 9". 드롭다운 최소값은 3인가 5인가? TC 경계값 설계에 직접 영향 | 미확인 |
| 3 | SC-CID-007 | [MISMATCH-003] 자유 텍스트 UI: 기획서 §자유 텍스트 line1 "체크박스 형태" vs line2 "라디오 버튼". Figma는 칩(D&D)+Text Input 방식. 실제 UI 컴포넌트 확정 필요 | 미확인 |
| 4 | SC-CID-013 | [MISSING-001] 만료 팝업 "Do not show again"의 적용 범위가 사용자별(개인 설정)인지 시스템 전체인지 불명확. TC 개인화 동작 설계에 영향 | 미확인 |
| 5 | SC-CID-009 | [CONFIRM-001] 시작 번호 상한 "최대 생성 가능 숫자 - 400"의 기준이 현재 자릿수 기준인지, 자동 확장 포함 전체 기준인지? (5자리 시 99999-400=99599 인지 여부) | 미확인 |
| 6 | SC-CID-023 | [CONFIRM-002] ID 재사용 방지 범위: 삭제된 케이스뿐 아니라 추후 예정인 Void/Nullify 처리 케이스의 번호도 포함되는가? 현재 기획 범위에서는 삭제만 해당하는 것으로 간주하여 시나리오 작성 | 미확인 |
| 7 | SC-CID-004 | [ISSUE-002 연계] Figma 툴팁 문구가 "N/A 선택 시"→"미선택 시"로 변경되고 월 초기화 문구가 삭제됨. 기획서 문구 기준으로 TC 작성할지, Figma 문구 기준으로 변경할지 결정 필요 | 미확인 |
| 8 | SC-CID-012, SC-CID-013 | [ISSUE-009 연계] 만료 임박 팝업이 본 캔버스(ICSR Config > Case ID)에 미반영. Case 생성 화면 Figma URL 확보 후 해당 시나리오에 대한 Figma 검증을 별도로 진행해야 함 | 미확인 |

---

## 리뷰 이력

| 일자 | 참석자 | 주요 결정 사항 |
|------|-------|--------------|
| 2026-04-27 | AI (scenario-writer) | 초안 작성 완료. 팀 리뷰 대기. |

---

## 참고 사항

### 디자인 이슈 시나리오 반영 요약

| 이슈 ID | 심각도 | 연관 시나리오 | TC 영향 | 처리 방향 |
|---------|-------|------------|--------|---------|
| ISSUE-001 | Critical | SC-CID-003 | N/A 옵션 TC 케이스 설계 전 확정 필요 | N/A 추가 또는 정책 삭제 결정 후 TC 반영 |
| ISSUE-002 | Major | SC-CID-004 | 기대값(툴팁 문구) 확정 후 TC 작성 | 기획서/Figma 중 기준 문구 결정 필요 |
| ISSUE-003 | Major | SC-CID-008 | 드롭다운 옵션 범위 확정 전 경계값 TC 보류 | 3~9 또는 5~9 확정 후 TC 반영 |
| ISSUE-004 | Minor | SC-CID-009 | 에러/경고 피드백 UI 확정 후 TC 작성 가능 | 참고용 — TC 작성 우선 진행 |
| ISSUE-005 | Major | SC-CID-007 | UI 컴포넌트(체크박스/라디오/칩) 확정 전 인터랙션 TC 설계 보류 | UI 확정 후 반영 |
| ISSUE-006 | Minor | SC-CID-007 | helper 문구 검증 TC 추가 가능 | 참고용 |
| ISSUE-007 | Info | - | 기획서에 없는 디자인 요소 — TC 대상 아님 | 기획서 보완 권장 |
| ISSUE-008 | Info | SC-CID-015 | '권장' 배지 노출 TC 추가 가능 | 기획서 보완 후 결정 |
| ISSUE-009 | Critical | SC-CID-012, SC-CID-013 | Case 생성 화면 Figma URL 확보 후 별도 검증 | 시나리오는 기획서 기반으로 작성 완료 |

### 상태 전이 다이어그램

```
C.1.1/C.1.8.1 수정 가능 여부 (케이스 워크플로우):

┌──────────┐    ┌──────────┐    ┌──────────┐
│  Draft   │ →  │In Review │ →  │ Approval │
│ (수정가능) │    │ (수정가능) │    │ (수정불가) │
└──────────┘    └──────────┘    └──────────┘
                                      │
                        수정 버튼 비표시 + 안내 문구 노출

일련번호 리셋 정책 (Year 설정별):

2-digit / 4-digit Year:
  [연간 누적] ──(매년 1월 1일 00:00:00)──→ [일련번호 00001로 리셋]

N/A:
  [전체 누적] ──(리셋 없음)──→ [계속 누적]

자릿수 자동 확장:
  [5자리: 00001~99999] ──(99999 초과)──→ [6자리: 100000~999999 (1XXXXX 형식)]
```

### 입력 필드 Validation 요약

| 필드 | 최소 | 최대 | 허용 문자 | 필수 여부 |
|------|-----|-----|---------|---------|
| 조직 식별자 | 1자 | 10자 | 영어(대소문자 구분), 숫자 | 필수 |
| 자유 텍스트 | 1자 | 6자 | 영어, 숫자 | 선택(칩 추가 시) |
| 일련번호 자릿수 | 3 (또는 5, 확인 필요) | 9 | 드롭다운 선택 | 필수 |
| 시작 번호 | 1 | 최대 생성 가능 숫자 - 400 | 숫자 | 기본값 1 |
