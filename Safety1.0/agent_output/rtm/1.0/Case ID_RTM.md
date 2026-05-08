# RTM — Case ID
> 버전: v3 | 최초 생성: 2026-04-28 | 기획자 답변 반영: 2026-05-04 | 시나리오 매핑: 2026-05-04 | TC 작성: 2026-05-04 | 갱신 에이전트: tc-writer | 파이프라인 상태: 리뷰 대기

## 메타데이터
- 기획서 경로: `plan/00. Common (공통 정책)/Admin (Org Admin)/ICSR Config/Case ID/Case ID.md`
- 참조 상위 기획서: `plan/00. Common (공통 정책)/Admin (Org Admin)/ICSR Config/ICSR Config.md` (내용 없음)
- 기획서 최신 버전: v1.0.250427 (작성자: 김나정)
- 분석 소스: 기획서 본문 텍스트 (와이어프레임 섹션 제외)
- 기획자 답변 반영일: 2026-05-04
- 시나리오 파일: `Safety1.0/agent_output/scenario/Case ID_시나리오.md`
- TC 파일: `TC/Case ID_TC.csv`
- 기획 품질 이슈 원본: 충돌 2건 / 표현 불일치 3건 / 누락 5건 / 확인 필요 5건
- 기획 품질 이슈 반영 후: **충돌 2건 해결** / **표현 불일치 3건 현행 유지** / **누락 5건 해결** / **확인 필요 5건 해결** / 잔여 미확인 1건
- 총 요구사항 수: 55건 (기존 51건 + 기획자 답변 기반 신규 4건)
- 제외 항목 수: 1건
- 검증 대상 요구사항: 55건
- TC 작성 보류: **0건**
- 총 TC 수: **104건** (보류 0건, [!확인필요!] 0건, 에러 문구 참고 3건)
- type 분포: Functional 55 / Negative 30 / Boundary 12 / Security 0 / Performance 0
- Smoke: 20건 / E2E: 7건 / Integration: 11건
- 잔여 미확인: 1건 (MISSING-002 중 조직 식별자·자유 텍스트 validation 에러 메시지 — 참고용, TC 작성 비차단)
- 총 시나리오: 36건 (SC-CASEID-001 ~ SC-CASEID-036)
- REQ 매핑율: 55/55 = 100%

---

## 요구사항 목록

| REQ_Id | 요구사항 내용 | 유형 | 출처(섹션) | 제외여부 | 시나리오 ID | TC ID 범위 | 상태 |
|--------|------------|------|----------|---------|-----------|----------|------|
| REQ-001 | Case ID는 케이스 생성 시 자동으로 부여됨 | 기능명세 | Case ID의 개념 | - | SC-CASEID-031 | TC-CASEID-031-001 ~ 031-003 | TC 작성 완료 |
| REQ-002 | Case ID 구조: `[국가코드]-[조직 식별자]-[설정된 번호 조합]` 중 [설정된 번호 조합] 부분 | 기능명세 | Case ID의 개념 | - | SC-CASEID-031 | TC-CASEID-031-001 ~ 031-003 | TC 작성 완료 |
| REQ-003 | Case ID는 Case Edit의 Case ID 필드에 표시됨 | 기능명세 | Case ID의 개념 | - | SC-CASEID-031 | TC-CASEID-031-001 ~ 031-002 | TC 작성 완료 |
| REQ-004 | Case ID는 Tracker의 Case ID 필드에 표시됨 | 기능명세 | Case ID의 개념 | - | SC-CASEID-029, SC-CASEID-031 | TC-CASEID-029-001, 031-001 ~ 031-003 | TC 작성 완료 |
| REQ-005 | 국가코드 결정 우선순위: ① Reporter's Country Code (Primary) → ② Reporter's Country Code (First) → ③ Country Where Reaction/Event Occurred (Primary) → ④ Country Where Reaction/Event Occurred (First) → ⑤ 기본값 'KR' | 비즈니스 규칙 | 기본 구조 및 국가 코드 로직 | - | SC-CASEID-028 | TC-CASEID-028-001 ~ 028-005 | TC 작성 완료 |
| REQ-006 | 조직 식별자: 최소 1글자 ~ 최대 10글자, 영어/숫자만 입력 가능 (대소문자 구분) | 데이터 규칙 | 기본 구조 및 국가 코드 로직 | - | SC-CASEID-003, SC-CASEID-004 | TC-CASEID-003-001 ~ 003-004, 004-001 ~ 004-004 | TC 작성 완료 |
| REQ-007 | 설정 가능한 모든 텍스트는 영문 및 숫자만 가능하며 대소문자 구분하여 입력 가능 | 데이터 규칙 | 개요 및 정책 | - | SC-CASEID-003, SC-CASEID-004, SC-CASEID-011 | TC-CASEID-003-001 ~ 003-004, 004-003 ~ 004-004, 011-003 ~ 011-004 | TC 작성 완료 |
| REQ-008 | ID 재사용 방지: 한 번 부여된 일련번호는 해당 케이스가 삭제되더라도 재사용 불가 | 비즈니스 규칙 | 개요 및 정책 | - | SC-CASEID-033 | TC-CASEID-033-001 ~ 033-002 | TC 작성 완료 |
| REQ-009 | Year - 2-digit year(YY): C.1.4(최초 발생인지일) 연도 뒤 두 자리 표기, 매년 1월 1일 00:00:00 리셋 | 기능명세 | Year (연도 표시 및 리셋 정책) | - | SC-CASEID-005 | TC-CASEID-005-001, 005-004 | TC 작성 완료 |
| REQ-010 | Year - 4-digit year(YYYY): C.1.4(최초 발생인지일) 연도 전체 네 자리 표기, 매년 1월 1일 00:00:00 리셋 | 기능명세 | Year (연도 표시 및 리셋 정책) | - | SC-CASEID-005 | TC-CASEID-005-002, 005-004 | TC 작성 완료 |
| REQ-011 | Year - N/A: 연도 미표기, 초기화 없이 누적 증가 | 기능명세 | Year (연도 표시 및 리셋 정책) | - | SC-CASEID-005 | TC-CASEID-005-003 | TC 작성 완료 |
| REQ-012 | Year 설정란 옆 툴팁 표시 (기획자 수정 완료): "연도 선택 시 매년 초에 일련번호가 '00001'로 초기화됩니다. N/A 선택 시(Chip을 추가하지 않았을 경우) 초기화 없이 번호가 계속 누적됩니다." *(CONFLICT-001 해결)* | 화면 상태 | Year (연도 표시 및 리셋 정책) | - | SC-CASEID-006 | TC-CASEID-006-001 ~ 006-002 | TC 작성 완료 |
| REQ-013 | Type of Report 체크 시 케이스의 Type of Report 값에 따라 구분자 자동 추가: Spontaneous→SP, Report from Study→RS, Other→OT, Not Available to Sender(Unknown)→UN | 비즈니스 규칙 | Type of Report (보고 구분) 추가 | - | SC-CASEID-007 | TC-CASEID-007-001 ~ 007-005 | TC 작성 완료 |
| REQ-014 | Product Abbreviation: PRD Chip 포함 설정 기준 — 케이스에 제품이 있을 경우 Product Config에 등록된 약어 표시, 제품이 없는 케이스는 UNK 표시 *(MISSING-005 해결)* | 비즈니스 규칙 | Product Abbreviation 추가 | - | SC-CASEID-008 | TC-CASEID-008-001 ~ 008-003 | TC 작성 완료 |
| REQ-015 | Product Abbreviation: 케이스 생성 시 '제품 불러오기'로 제품 정보가 포함된 경우 약어 표시, 제품 없는 케이스는 UNK로 대체 *(MISSING-005 해결)* | 비즈니스 규칙 | Product Abbreviation 추가 | - | SC-CASEID-008 | TC-CASEID-008-001 ~ 008-002 | TC 작성 완료 |
| REQ-016 | Product Abbreviation: Suspect이자 자사 제품이 두 개 이상인 경우 첫 번째 순서 자사 제품 약어 표시 | 비즈니스 규칙 | Product Abbreviation 추가 | - | SC-CASEID-009 | TC-CASEID-009-001 ~ 009-002 | TC 작성 완료 |
| REQ-017 | 자유 텍스트: 체크박스 형태로 선택 가능, 선택 시 [Custom Text] 블록 제공, 라디오 버튼으로 텍스트 블록 추가 | 기능명세 | 자유 텍스트 추가 | - | SC-CASEID-010 | TC-CASEID-010-001 ~ 010-003 | TC 작성 완료 |
| REQ-018 | 자유 텍스트: 영문/숫자만 입력 가능, 최대 6글자 | 데이터 규칙 | 자유 텍스트 추가 | - | SC-CASEID-011 | TC-CASEID-011-001 ~ 011-004 | TC 작성 완료 |
| REQ-019 | 일련번호 자릿수: 3, 4, 5, 6, 7, 8, 9 중 선택 (최대 9자리) | 기능명세 | 일련번호 자릿수 설정 | - | SC-CASEID-012 | TC-CASEID-012-001 ~ 012-003 | TC 작성 완료 |
| REQ-020 | 일련번호 Zero-padding: 선택한 자릿수만큼 번호 앞에 '0' 채움 | 기능명세 | 일련번호 자릿수 설정 | - | SC-CASEID-012 | TC-CASEID-012-001 ~ 012-003 | TC 작성 완료 |
| REQ-021 | 자릿수 중간 변경 시 이후 생성되는 케이스부터 적용 (기존 케이스 소급 없음 → REQ-054 참조) | 비즈니스 규칙 | 일련번호 자릿수 설정 | - | SC-CASEID-013 | TC-CASEID-013-001 ~ 013-003 | TC 작성 완료 |
| REQ-022 | 시작 번호 설정: 기본값 1, 사용자가 N 입력 시 N부터 카운팅 시작; 값 삭제 후 커서 아웃 시 강제로 1 기입 *(MISSING-002 부분 해결)* | 기능명세 | 시작 번호 설정 | - | SC-CASEID-014 | TC-CASEID-014-001 ~ 014-003 | TC 작성 완료 |
| REQ-023 | 시작 번호 설정: 저장 후 생성되는 첫 번째 케이스부터 즉시 적용 | 비즈니스 규칙 | 시작 번호 설정 | - | SC-CASEID-014 | TC-CASEID-014-003 | TC 작성 완료 |
| REQ-024 | 최후 번호 검증: 시작 번호는 해당 조합에서 이미 생성된 가장 최후 번호보다 커야 함 | 비즈니스 규칙 | 최후 번호 검증 규칙 | - | SC-CASEID-016 | TC-CASEID-016-001 ~ 016-003 | TC 작성 완료 |
| REQ-025 | 시작 번호 제한: [최대 생성 가능 숫자 - 400]을 초과하여 입력 불가 처리 (오류 문구 미노출) *(MISSING-002 부분 해결)* | 비즈니스 규칙 | 시작 번호 설정 제한 정책 | - | SC-CASEID-015 | TC-CASEID-015-001 ~ 015-002 | TC 작성 완료 |
| REQ-026 | 포맷 설정 Drag & Drop: Chip 드래그로 좌우 순서 변경, Preview 실시간 반영 | 기능명세 | 포맷 설정 및 인터랙션 (Drag & Drop) | - | SC-CASEID-018 | TC-CASEID-018-001 ~ 018-002 | TC 작성 완료 |
| REQ-027 | 포맷 설정 영역 활성화 조건: Year를 2-digit 또는 4-digit으로 선택하거나 Type of Report 체크 시에만 해당 설정 영역 활성화 | 기능명세 | 포맷 설정 및 인터랙션 (Drag & Drop) | - | SC-CASEID-019 | TC-CASEID-019-001 ~ 019-003 | TC 작성 완료 |
| REQ-028 | Chip 구성: Year(연/월), ####(일련번호), TR(보고 구분), PRD(제품 약어), TXT(자유 텍스트) | 기능명세 | 포맷 설정 및 인터랙션 (Drag & Drop) | - | SC-CASEID-017 | TC-CASEID-017-001 | TC 작성 완료 |
| REQ-029 | Chip 추가 시 하단 해당 설정 영역 활성화; X 누르면 chip 삭제, 하단 영역 비활성화 (이전 설정값 유지) | 기능명세 | 포맷 설정 및 인터랙션 (Drag & Drop) | - | SC-CASEID-017 | TC-CASEID-017-001 ~ 017-003 | TC 작성 완료 |
| REQ-030 | Case ID 만료 임박 알림 팝업: 남은 번호가 100개 이하일 때 팝업 노출 | 기능명세 | Case ID 만료 임박 알림 | - | SC-CASEID-020 | TC-CASEID-020-001, 020-003 | TC 작성 완료 |
| REQ-031 | 팝업 노출 시점: 케이스에 Case ID가 최종적으로 부여된 순간 (Case ID configuration 화면이 아님) | 기능명세 | ID 팝업 표시 시점 | - | SC-CASEID-020 | TC-CASEID-020-001 ~ 020-002 | TC 작성 완료 |
| REQ-032 | 팝업 내용: 현재 마지막 Case ID, 최대 자릿수 최대값, 확장 후 첫 번호(New Case ID_1), 두 번째 번호(New Case ID_2) 포함 | 기능명세 | Case ID 만료 임박 알림 | - | SC-CASEID-020 | TC-CASEID-020-002 | TC 작성 완료 |
| REQ-033 | 팝업 닫기 — [Confirm] 클릭: 닫히지만 해당 사용자 다음 로그인 시 재노출; "다음 로그인"에 세션 만료 후 재접속도 포함 *(CONFIRM-004 해결)* | 기능명세 | 사용자 인터랙션 및 제어 | - | SC-CASEID-021 | TC-CASEID-021-001 ~ 021-003 | TC 작성 완료 |
| REQ-034 | 팝업 닫기 — [Do not show again] 체크 후 [Confirm]: 해당 팝업 더 이상 노출 안 함 (단, 자동 자릿수 확장 시 초기화 → REQ-055 참조) | 기능명세 | 사용자 인터랙션 및 제어 | - | SC-CASEID-022 | TC-CASEID-022-001 ~ 022-002 | TC 작성 완료 |
| REQ-035 | 팝업 자동 미노출: 일련번호 완전 초과 후 새로운 자릿수 체계(1XXXXX...)로 넘어간 경우 기존 팝업 노출 중단 | 비즈니스 규칙 | 사용자 인터랙션 및 제어 | - | SC-CASEID-024 | TC-CASEID-024-003 | TC 작성 완료 |
| REQ-036 | 자동 자릿수 확장: 최대 자릿수 초과 시 자릿수 +1, '1XXXXX' 형식으로 번호 시작 (예: 5자리 99999 → 6자리 100000); 확장 발생 시 모달만 노출, 별도 외부 알림 없음 *(MISSING-004 해결)* | 비즈니스 규칙 | Case ID 자릿수 자동 확장 | - | SC-CASEID-024 | TC-CASEID-024-001 ~ 024-003 | TC 작성 완료 |
| REQ-037 | Import 설정 옵션 A(기본값): C.1.1 신규 부여 + C.1.8.1 파일 내 값 유지 | 비즈니스 규칙 | Import 설정 — C.1.1/C.1.8.1 값 처리 방식 | - | SC-CASEID-025 | TC-CASEID-025-001 ~ 025-003 | TC 작성 완료 |
| REQ-038 | Import 설정 옵션 B: C.1.1, C.1.8.1 모두 파일 내 값 그대로 사용; 파일 내 C.1.1이 시스템 내 기존 케이스와 중복될 경우 에러 반환 (Import 실패, 오류 메시지 표시) *(CONFIRM-001 해결)* | 비즈니스 규칙 | Import 설정 — C.1.1/C.1.8.1 값 처리 방식 | - | SC-CASEID-026, SC-CASEID-027 | TC-CASEID-026-001 ~ 026-002, 027-001 ~ 027-002 | TC 작성 완료 |
| REQ-039 | Import 설정 적용 범위: Import 기능으로 케이스 생성 시에만 적용 | 비즈니스 규칙 | Import 설정 — C.1.1/C.1.8.1 값 처리 방식 | - | SC-CASEID-025, SC-CASEID-026 | TC-CASEID-025-001 ~ 025-002, 026-001 ~ 026-002 | TC 작성 완료 |
| REQ-040 | C.1.8.1 없을 때 C.1.1 복사: C.1.8.1이 Null이면 C.1.1 값을 C.1.8.1에 복사 | 비즈니스 규칙 | C.1.1, C.1.8.1 동일 입력 설정 | - | SC-CASEID-030 | TC-CASEID-030-001 ~ 030-002 | TC 작성 완료 |
| REQ-041 | Case Level 식별자 노출: Tracker List, Case의 Case ID → 일련번호만 표시 | 기능명세 | Case vs Report Identifier 노출 사양 | - | SC-CASEID-029 | TC-CASEID-029-001 ~ 029-002 | TC 작성 완료 |
| REQ-042 | Report Level 식별자 노출: ICSR 보고서(C.1.1, C.1.8.1) → 국가-조직-일련번호 표시 | 기능명세 | Case vs Report Identifier 노출 사양 | - | SC-CASEID-029 | TC-CASEID-029-003 | TC 작성 완료 |
| REQ-043 | 매뉴얼 케이스 생성 — Case ID: Configuration 설정에 따른 순차적 일련번호 부여, 중복 체크 및 Follow-up 연결 기준 | 기능명세 | 매뉴얼 케이스 생성 (Initial) | - | SC-CASEID-031 | TC-CASEID-031-001 ~ 031-003 | TC 작성 완료 |
| REQ-044 | 매뉴얼 케이스 생성 — C.1.1과 C.1.8.1 동일; Destination 확정 시 국가코드 결정, [국가]-[회사]-[일련번호] 조합 생성 | 비즈니스 규칙 | 매뉴얼 케이스 생성 (Initial) | - | SC-CASEID-031 | TC-CASEID-031-002 ~ 031-003 | TC 작성 완료 |
| REQ-045 | Import/AI Convert — Case ID: Configuration 설정에 따른 순차적 일련번호 부여 | 기능명세 | 데이터 인입 (Import / AI Convert) | - | SC-CASEID-032 | TC-CASEID-032-001 | TC 작성 완료 |
| REQ-046 | Import/AI Convert — 식별자: 파일 내 C.1.8.1 값 기반 생성, 중복 체크 및 Follow-up 연결 기준 | 비즈니스 규칙 | 데이터 인입 (Import / AI Convert) | - | SC-CASEID-032 | TC-CASEID-032-002 | TC 작성 완료 |
| REQ-047 | Import/AI Convert — C.1.1: Destination 확정 시 국가코드 결정, [국가]-[회사]-[일련번호] 조합 생성 | 비즈니스 규칙 | 데이터 인입 (Import / AI Convert) | - | SC-CASEID-032 | TC-CASEID-032-003 | TC 작성 완료 |
| REQ-048 | Import/AI Convert — C.1.8.1: 파일 내 기존 값 유지 | 비즈니스 규칙 | 데이터 인입 (Import / AI Convert) | - | SC-CASEID-032 | TC-CASEID-032-002 | TC 작성 완료 |
| REQ-049 | 식별자 수정 불가: 시스템 부여 즉시 수동 수정 절대 불가 (사용자 편집 권한 없음) | 비즈니스 규칙 | 식별자 수정 및 변경 정책 | - | SC-CASEID-034 | TC-CASEID-034-001 ~ 034-002 | TC 작성 완료 |
| REQ-050 | C.1.1 Approval 이후 변경 불가: UI 수정 버튼 비표시, 안내 문구 표시 ("Approval 상태 이후로는 보고자 관리번호(C.1.1)과 고유식별 보고자 관리번호(C.1.8.1) 수정이 불가합니다.") | 비즈니스 규칙 | 식별자 수정 및 변경 정책 | - | SC-CASEID-035 | TC-CASEID-035-001 ~ 035-003 | TC 작성 완료 |
| REQ-051 | C.1.8.1 변경 불가 — 운영 정책 문서/교육으로만 고지, 시스템 UI에 별도 표시 없음 *(CONFIRM-005 해결)* | 비즈니스 규칙 | Manual에 C.1.8.1 변경 불가 및 규제 관련 명시 | - | SC-CASEID-034 | TC-CASEID-034-003 | TC 작성 완료 |
| REQ-052 | Case ID Configuration 화면 접근 권한: Master Admin 및 Org Admin만 접근 가능 *(MISSING-001 해결 — 신규)* | 비즈니스 규칙 | 접근 권한 | - | SC-CASEID-001, SC-CASEID-002 | TC-CASEID-001-001 ~ 001-002, 002-001 ~ 002-002 | TC 작성 완료 |
| REQ-053 | C.1.4(최초 발생인지일)는 케이스 생성 시 필수값 (Null 불가); 케이스 편집 시에도 C.1.4 Null 상태로 저장 불가 *(MISSING-003 해결 — 신규)* | 비즈니스 규칙 | Year — C.1.4 필수값 처리 | - | SC-CASEID-036 | TC-CASEID-036-001 ~ 036-003 | TC 작성 완료 |
| REQ-054 | 자릿수 중간 변경 시 기존 생성 케이스의 Case ID는 생성 당시 자릿수 그대로 표시, 소급 변경 없음 *(CONFIRM-002 해결 — 신규)* | 비즈니스 규칙 | 일련번호 자릿수 설정 | - | SC-CASEID-013 | TC-CASEID-013-002 ~ 013-003 | TC 작성 완료 |
| REQ-055 | [Do not show again] 체크 후 자동 자릿수 확장으로 새 자릿수 체계 전환 시 해당 설정 초기화, 새 체계에 대한 만료 임박 팝업 재노출 *(CONFIRM-003 해결 — 신규)* | 비즈니스 규칙 | 사용자 인터랙션 및 제어 | - | SC-CASEID-023 | TC-CASEID-023-001 ~ 023-002 | TC 작성 완료 |
| REQ-EX-001 | AI Convert에 Import 설정 적용 — 추후 개발 예정 | 기능명세 | Import 설정 — 적용 범위 | TBD | - | - | 제외 |

---

## 제외 항목 목록

| REQ_Id | 원문 | 제외 사유 |
|--------|------|---------|
| REQ-EX-001 | "해당 설정은 오직 'Import' 기능을 통해 케이스가 생성될 때만 적용되는 로직 (추후 Convert에도 적용 예정)" | 추후 개발 예정 (TBD) — 현 버전 범위 외 |

---

## 확인 필요 사항 (기획자 답변 반영 완료)

> 전체 15건 / **14건 해결** / **1건 부분 해결** / **TC 작성 보류 0건**

| No | 이슈 | 관련 REQ | TC 영향 | 기획자 답변 요약 | 상태 |
|----|------|---------|--------|----------------|------|
| 1 | [CONFLICT-001] 툴팁에 삭제된 "연월 선택" 문구 잔류 | REQ-012 | 보류 해제 | 툴팁 수정 완료 ("연월 선택 시" 문구 삭제) | ✅ 해결됨 |
| 2 | [CONFLICT-002] Case Level 식별자 예시 자릿수 불일치 (3자리 vs 5자리) | REQ-019, REQ-041 | 참고용 | 의도적 예시 (선택값 3~9자리 시연), 기획서 수정 불필요 | ✅ 해결됨 |
| 3 | [MISSING-001] Case ID Configuration 접근 가능 역할 미정의 | REQ-052 | 보류 해제 | Master Admin / Org Admin 접근 가능 | ✅ 해결됨 |
| 4 | [MISSING-002] Validation 실패 시 에러 메시지 문구 미정의 | REQ-006, REQ-018, REQ-022, REQ-025 | 참고용 | 시작 번호: 미입력→강제 1 / 최대값 초과→입력 불가(오류 미노출) 확인; **조직 식별자·자유 텍스트 에러 메시지 미답변 (잔여)** | ⚠️ 부분 해결 |
| 5 | [MISSING-003] C.1.4 Null일 때 Year 처리 로직 미정의 | REQ-053 | 보류 해제 | C.1.4는 Case 생성 시 필수값 (Null 없음); 편집 시 Null 저장 불가 TC 필요 | ✅ 해결됨 |
| 6 | [MISSING-004] 자동 자릿수 확장 발생 시 Admin 알림 방식 미정의 | REQ-036 | 참고용 | 모달만 노출, 별도 외부 알림 없음 | ✅ 해결됨 |
| 7 | [MISSING-005] PRD Chip 포함 설정 + 케이스 내 제품 없을 때 동작 불명확 | REQ-014, REQ-015 | 참고용 | 제품 있는 케이스: 약어 노출 / 제품 없는 케이스: UNK | ✅ 해결됨 |
| 8 | [EXPR-001] 자유 텍스트 / Free Text / Custom Text 혼용 | REQ-017, REQ-018 | 참고용 | 현행 유지 (수정X); TC 작성 시 혼용 표현 허용 | ✅ 현행 유지 확인 |
| 9 | [EXPR-002] 조직 식별자 vs 조직명 혼용 | REQ-006 | 참고용 | 현행 유지 (수정X) | ✅ 현행 유지 확인 |
| 10 | [EXPR-003] 보고 구분 vs Type of Report 혼용 | REQ-013 | 참고용 | 현행 유지 (수정X) | ✅ 현행 유지 확인 |
| 11 | [CONFIRM-001] Import 옵션 B 선택 시 중복 C.1.1 처리 방법 | REQ-038 | 보류 해제 | 에러 반환 (Import 실패, 오류 메시지 표시) | ✅ 해결됨 |
| 12 | [CONFIRM-002] 자릿수 중간 변경 시 기존 케이스 Tracker 표시 방식 | REQ-054 | 참고용 | 기존 케이스는 생성 당시 자릿수 그대로 표시, 변경 없음 | ✅ 해결됨 |
| 13 | [CONFIRM-003] Do not show again 후 자릿수 확장 시 팝업 재노출 여부 | REQ-055 | 보류 해제 | 설정 초기화 → 새 체계에 대한 팝업 재노출 | ✅ 해결됨 |
| 14 | [CONFIRM-004] "다음 로그인" — 세션 만료/재접속 포함 여부 | REQ-033 | 참고용 | 세션 만료 후 재접속도 "다음 로그인"으로 간주 → 팝업 재노출 | ✅ 해결됨 |
| 15 | [CONFIRM-005] C.1.8.1 변경 불가 시스템 UI 고지 여부 | REQ-051 | 참고용 | 운영 정책 문서/교육으로만 고지, 시스템 UI 별도 표시 없음 | ✅ 해결됨 |
