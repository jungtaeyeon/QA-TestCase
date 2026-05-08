# RTM — Case ID
> 버전: v3 | 생성: 2026-05-06 | 갱신: 2026-05-07 | 갱신 에이전트: tc-writer | 파이프라인 상태: TC 작성 완료, 리뷰 대기

## 메타데이터
- 기획서 경로: `exports/confluence/기획 문서/00. Common (공통 정책)/Admin (Org Admin)/ICSR Config/Case ID/Case ID.md`
- 기획서 최신 버전: v1.0.250430 (작성: 김나정)
- 참조 상위 기획서: 없음 (상위 경로 MD 없음)
- 기획 품질 이슈: 충돌 3건 / 표현 불일치 2건 / 누락 13건 / 확인 필요 3건
- 총 요구사항 수: 57건 (REQ-001~REQ-057)
- 제외 항목 수: 2건 (REQ-EX-001 TBD, REQ-046 N/A — Null 케이스 없음)
- 검증 대상 요구사항: 56건
- TC 작성 보류 요구사항: 1건 (REQ-025, MISSING-010 미해결)
- 기획자 답변 v1.2 반영: CONFLICT-001/002/003, MISSING-002/003/004/005/006/007/008/009/012, CONFIRM-001/002 해결 (13건)
- TC 작성 완료: 97건 (Smoke 12건, E2E 13건) | TC 보류: 1건 (REQ-025, MISSING-010 미해결)
- TC 파일 경로: `TC/1.2/Case ID_TC.csv`

---

## 요구사항 목록

| REQ_Id | 요구사항 내용 | 유형 | 출처(섹션) | 제외여부 | 시나리오 ID | TC ID 범위 | 상태 |
|--------|------------|------|----------|---------|-----------|----------|------|
| REQ-001 | Case ID는 케이스 생성 시 자동 부여됨 (Configuration 설정 기반 순차 일련번호) | 기능명세 | Case ID의 개념 | - | SC-CASEID-005 | - | TC 작성 완료 |
| REQ-002 | Case ID = [설정된 번호 조합] 부분만 해당. Case Edit의 Case ID 필드 및 Tracker의 Case ID 컬럼에 표시 | 기능명세 | Case ID의 개념 | - | SC-CASEID-005, SC-CASEID-044 | - | TC 작성 완료 |
| REQ-003 | 모든 텍스트 입력은 영문 및 숫자만 허용, 대소문자 구분 | 데이터 규칙 | 개요 및 정책 | - | SC-CASEID-001, SC-CASEID-003, SC-CASEID-020 | - | TC 작성 완료 |
| REQ-004 | ID 재사용 방지: 삭제된 케이스의 일련번호도 절대 재사용 금지 | 비즈니스 규칙 | 개요 및 정책 | - | SC-CASEID-006 | - | TC 작성 완료 |
| REQ-005 | 기본 구조: `[국가코드]-[조직 식별자]-[설정된 번호 조합]` | 기능명세 | 기본 구조 및 국가코드 로직 | - | SC-CASEID-005 | - | TC 작성 완료 |
| REQ-006 | 국가코드 1순위: Reporter's Country Code (Primary) | 비즈니스 규칙 | 기본 구조 및 국가코드 로직 | - | SC-CASEID-004 | - | TC 작성 완료 |
| REQ-007 | 국가코드 2순위: Reporter's Country Code (First) — Primary 없을 경우 | 비즈니스 규칙 | 기본 구조 및 국가코드 로직 | - | SC-CASEID-004 | - | TC 작성 완료 |
| REQ-008 | 국가코드 3순위: Identification of Country Where Reaction Occurred (Primary) — 위 정보 없을 시 | 비즈니스 규칙 | 기본 구조 및 국가코드 로직 | - | SC-CASEID-004 | - | TC 작성 완료 |
| REQ-009 | 국가코드 3-1: Event Country Occurred (First) — 3번 조건 내부 세부처리 [✅ CONFIRM-001 해결: 4단계 유지] | 비즈니스 규칙 | 기본 구조 및 국가코드 로직 | - | SC-CASEID-004 | - | TC 작성 완료 |
| REQ-010 | 국가코드 기본값: 모든 조건 미충족 시 'KR' | 비즈니스 규칙 | 기본 구조 및 국가코드 로직 | - | SC-CASEID-004 | - | TC 작성 완료 |
| REQ-011 | 조직 식별자: 사용자 직접 입력, 최소 1자~최대 10자, 영어(대소문자 구분)+숫자 | 데이터 규칙 | 기본 구조 및 국가코드 로직 | - | SC-CASEID-001, SC-CASEID-002, SC-CASEID-003 | - | TC 작성 완료 |
| REQ-012 | Year 2-digit: C.1.4 연도 뒤 두 자리(YY) 표기, 매년 1월 1일 00:00:00 리셋 | 기능명세 | 번호 조합 > Year | - | SC-CASEID-007 | - | TC 작성 완료 |
| REQ-013 | Year 4-digit: C.1.4 연도 전체 네 자리(YYYY) 표기, 매년 1월 1일 00:00:00 리셋 | 기능명세 | 번호 조합 > Year | - | SC-CASEID-008 | - | TC 작성 완료 |
| REQ-014 | Year N/A: 연도 미표기, 초기화 없이 누적 증가 | 기능명세 | 번호 조합 > Year | - | SC-CASEID-009 | - | TC 작성 완료 |
| REQ-015 | 연도 설정 툴팁: "연도 선택 시 매년 초 '00001' 초기화 / N/A 선택 시(Chip 미추가 시) 누적" (26.04.30 문구 수정 완료) | 화면 상태 | 번호 조합 > Year | - | SC-CASEID-010 | - | TC 작성 완료 |
| REQ-016 | Year 설정 변경 시 이후 케이스부터 새 설정 적용, 기존 케이스 불변 [✅ MISSING-002 해결] | 비즈니스 규칙 | 번호 조합 > Year | - | SC-CASEID-011 | - | TC 작성 완료 |
| REQ-017 | Type of Report 체크 시 케이스 값에 따라 구분자 자동 추가 (Spontaneous→SP / Report from Study→RS / Other→OT / Not Available→UN) | 비즈니스 규칙 | 번호 조합 > Type of Report | - | SC-CASEID-012 | - | TC 작성 완료 |
| REQ-018 | Type of Report 체크 시 표시 문구: "체크 시 케이스의 Type of Report 값에 따라 구분자가 Case ID에 자동 추가됩니다." | 화면 상태 | 번호 조합 > Type of Report | - | SC-CASEID-014 | - | TC 작성 완료 |
| REQ-019 | Type of Report 미입력/Null 케이스에서 UN 기본 적용 [✅ MISSING-003 해결] | 비즈니스 규칙 | 번호 조합 > Type of Report | - | SC-CASEID-013 | - | TC 작성 완료 |
| REQ-020 | Product Abbreviation: Admin Product Config에 등록된 약어 참조, 없으면 UNK 표시 | 기능명세 | 번호 조합 > Product Abbreviation | - | SC-CASEID-015 | - | TC 작성 완료 |
| REQ-021 | Product Abbreviation 활성화 조건: 케이스에 '제품 불러오기'로 제품 포함 시만 활성화 | 비즈니스 규칙 | 번호 조합 > Product Abbreviation | - | SC-CASEID-016 | - | TC 작성 완료 |
| REQ-022 | Suspect 자사 제품 2개 이상 시 입력 순서 기준 첫 번째 약어 표시 [✅ CONFIRM-002 해결] | 비즈니스 규칙 | 번호 조합 > Product Abbreviation | - | SC-CASEID-017 | - | TC 작성 완료 |
| REQ-023 | Product Config 약어 삭제/변경 시 기존 Case ID 불변, 신규/Import 케이스에만 반영 [✅ MISSING-012 해결] | 비즈니스 규칙 | 번호 조합 > Product Abbreviation | - | SC-CASEID-018 | - | TC 작성 완료 |
| REQ-024 | 자유 텍스트: 체크박스 선택, 라디오 버튼으로 텍스트 블록 추가, 영문+숫자, 최대 6글자 | 기능명세 | 번호 조합 > 자유 텍스트 | - | SC-CASEID-019, SC-CASEID-020 | - | TC 작성 완료 |
| REQ-025 | 자유 텍스트 최솟값 및 빈값 저장 처리 [⏸ MISSING-010 미해결 — 기획자 확인 필요] | 데이터 규칙 | 번호 조합 > 자유 텍스트 | - | SC-CASEID-021 | - | TC보류 |
| REQ-026 | 자유 텍스트: 드래그 앤 드롭으로 원하는 위치에 배치 가능 | 기능명세 | 번호 조합 > 자유 텍스트 | - | SC-CASEID-019 | - | TC 작성 완료 |
| REQ-027 | 일련번호 자릿수: 3, 4, 5, 6, 7, 8, 9 중 선택 (최대 9자리), Zero-padding 적용 | 기능명세 | 일련번호 자릿수 설정 | - | SC-CASEID-022 | - | TC 작성 완료 |
| REQ-028 | 일련번호 자릿수 변경 시 이후 생성 케이스부터 적용 (기존 케이스 소급 없음) | 비즈니스 규칙 | 일련번호 자릿수 설정 | - | SC-CASEID-023 | - | TC 작성 완료 |
| REQ-029 | 시작 번호 기본값: 1 / 빈값 커서아웃 시 강제 1 기입 | 기능명세 | 일련번호 및 카운팅 시작점 설정 | - | SC-CASEID-024 | - | TC 작성 완료 |
| REQ-030 | 시작 번호: 사용자 입력 시 해당 번호부터 카운팅 시작, 설정 저장 후 첫 케이스부터 즉시 적용 | 기능명세 | 일련번호 및 카운팅 시작점 설정 | - | SC-CASEID-025 | - | TC 작성 완료 |
| REQ-031 | 최후 번호 검증: 이미 생성된 최후 번호보다 커야 함 (동일 조합 이력 기준) | 비즈니스 규칙 | 최후 번호 검증 규칙 | - | SC-CASEID-026 | - | TC 작성 완료 |
| REQ-032 | 시작 번호 설정 제한: [최대 생성 가능 숫자 - 400] 초과 불가 [⚠ CONFIRM-003 — 전제값 보류 유지, TC 가능] | 비즈니스 규칙 | 시작 번호 설정 제한 정책 | - | SC-CASEID-027 | - | TC 작성 완료 |
| REQ-033 | 포맷 설정 Drag&Drop 영역 활성화 조건 — 칩 추가 시 해당 칩 설정 영역 활성화 [✅ MISSING-004 해결] | 기능명세 | 포맷 설정 및 Drag & Drop | - | SC-CASEID-028 | - | TC 작성 완료 |
| REQ-034 | Chip 구성: YY/YYYY(Year), ######(일련번호), TR(보고 구분), PRD(제품 약어), TXT(자유 텍스트) | 기능명세 | 포맷 설정 및 Drag & Drop | - | SC-CASEID-029 | - | TC 작성 완료 |
| REQ-035 | 칩 드래그 앤 드롭으로 좌우 순서 변경, Preview에 실시간 반영 | 기능명세 | 포맷 설정 및 Drag & Drop | - | SC-CASEID-030 | - | TC 작성 완료 |
| REQ-036 | 칩 x 클릭 시 제거, 하단 설정 영역 비활성화 / 이전 설정값 세션 내에서만 유지 [✅ MISSING-005 해결] | 기능명세 | 포맷 설정 및 Drag & Drop | - | SC-CASEID-031 | - | TC 작성 완료 |
| REQ-037 | 만료 임박 알림: 남은 번호 100개 이하 시, Case ID 최종 부여 순간에 팝업 노출 | 기능명세 | Case ID 만료 경고 | - | SC-CASEID-032 | - | TC 작성 완료 |
| REQ-038 | 팝업 노출 위치: Configuration 화면 아님. Manual Intake/Import 케이스 생성 완료 시점. 모든 화면에서 노출. | 기능명세 | Case ID 만료 경고 | - | SC-CASEID-033 | - | TC 작성 완료 |
| REQ-039 | 팝업 내용: 현재 마지막 Case ID, 최대값, 자릿수 확장 후 첫 번째 New Case ID 표시 [✅ MISSING-007 해결] | 화면 상태 | Case ID 만료 경고 | - | SC-CASEID-034 | - | TC 작성 완료 |
| REQ-040 | 팝업 닫기 — Confirm 클릭: 팝업 닫힘, 해당 사용자의 다음 로그인 시 재노출 | 기능명세 | Case ID 만료 경고 | - | SC-CASEID-035 | - | TC 작성 완료 |
| REQ-041 | 팝업 닫기 — "오늘 하루 보지 않기" 체크 + Confirm: 24시간 미노출 | 기능명세 | Case ID 만료 경고 | - | SC-CASEID-036 | - | TC 작성 완료 |
| REQ-042 | 하루 억압 중 자릿수 초과 전환 시 별도 알림 없이 24시간 내 팝업 재노출 가능 [✅ MISSING-008 해결] | 비즈니스 규칙 | Case ID 만료 경고 | - | SC-CASEID-037 | - | TC 작성 완료 |
| REQ-043 | 팝업 자동 미노출: 새로운 자릿수 체계(1XXXXX...)로 넘어간 경우 기존 팝업 중단 | 비즈니스 규칙 | Case ID 만료 경고 | - | SC-CASEID-038 | - | TC 작성 완료 |
| REQ-044 | 자릿수 자동 확장: 최대 자릿수 초과 시 한 자리 자동 추가, 1XXXXX 형식으로 시작 (예: 99999→100000) | 비즈니스 규칙 | Case ID 자릿수 자동 확장 | - | SC-CASEID-039 | - | TC 작성 완료 |
| REQ-045 | Import 옵션 A(기본값): C.1.1 신규 부여, C.1.8.1 파일 내 값 유지 | 기능명세 | Import 설정 | - | SC-CASEID-040 | - | TC 작성 완료 |
| REQ-046 | Import 옵션 A + C.1.8.1 Null 케이스 없음 [✅ MISSING-009 해결 — N/A 처리] | 비즈니스 규칙 | Import 설정 | N/A | - | - | N/A 제외 (기획자: Null 케이스 없음) |
| REQ-047 | Import 옵션 B: C.1.1, C.1.8.1 모두 파일 내 값 유지 / C.1.1 중복 시 에러 반환 [✅ CONFLICT-001 해결] | 기능명세 | Import 설정 | - | SC-CASEID-041 | - | TC 작성 완료 |
| REQ-048 | Import 적용 범위: Import 기능을 통한 케이스 생성 시에만 적용 | 비즈니스 규칙 | Import 설정 | - | SC-CASEID-042 | - | TC 작성 완료 |
| REQ-049 | C.1.8.1이 없을 때(Null) C.1.1 값을 C.1.8.1에 자동 복사 (기존 값 있으면 미적용) | 비즈니스 규칙 | C.1.1, C.1.8.1 동일 입력 설정 | - | SC-CASEID-043 | - | TC 작성 완료 |
| REQ-050 | Case Level(Tracker, Case Edit): 일련번호 형식만 표시 (예: 202604ST001) | 기능명세 | ICSR 식별자 관리 사양서 | - | SC-CASEID-044 | - | TC 작성 완료 |
| REQ-051 | Report Level(C.1.1, C.1.8.1): [국가]-[조직]-[일련번호] 형식 표시 (예: KR-SELTA-202604ST001) | 기능명세 | ICSR 식별자 관리 사양서 | - | SC-CASEID-044 | - | TC 작성 완료 |
| REQ-052 | 매뉴얼 케이스: C.1.1 = C.1.8.1, Destination 확정 시 국가코드 결정 및 부여 | 비즈니스 규칙 | 생성 유형별 식별자 부여 로직 | - | SC-CASEID-045 | - | TC 작성 완료 |
| REQ-053 | Destination 미확정 상태에서 C.1.1 공란 표시 [✅ MISSING-006 해결 — 잠정] | 비즈니스 규칙 | 생성 유형별 식별자 부여 로직 | - | SC-CASEID-046 | - | TC 작성 완료 |
| REQ-054 | Import 케이스: C.1.1은 보고처 확정 시 신규 부여(Import 옵션 A = Initial 사례), C.1.8.1은 파일 내 기존 값 유지 [✅ CONFLICT-002 해결] | 비즈니스 규칙 | 생성 유형별 식별자 부여 로직 | - | SC-CASEID-047 | - | TC 작성 완료 |
| REQ-055 | 식별자 수정 불가 정책 — 부여 즉시 어떤 상태에서도 수정 불가 [✅ CONFLICT-003 해결] | 비즈니스 규칙 | 식별자 수정 및 변경 정책 | - | SC-CASEID-048 | - | TC 작성 완료 |
| REQ-056 | C.1.1 Approval 이후 변경 불가: 수정 버튼 비표시 + 안내 문구 표시 | 비즈니스 규칙 | 식별자 수정 및 변경 정책 | - | SC-CASEID-049 | - | TC 작성 완료 |
| REQ-057 | C.1.8.1 Approval 이후 변경 불가 (동일 안내 문구) + 매뉴얼 고지 방식 | 비즈니스 규칙 | 식별자 수정 및 변경 정책 | - | SC-CASEID-049 | - | TC 작성 완료 |
| REQ-EX-001 | Convert 기능에도 Import 설정 적용 (추후 적용 예정) | 기능명세 | Import 설정 | TBD | - | - | 제외 |

---

## 제외 항목 목록

| REQ_Id | 원문 | 제외 사유 |
|--------|------|---------|
| REQ-EX-001 | "추후 Convert에도 적용 예정" | 추후 개발 예정 — 현재 TC 작성 불가 |
| REQ-046 | Import 옵션 A + C.1.8.1 Null 케이스 처리 | N/A — 기획자 답변: "Null 케이스 없음" |

---

## 확인 필요 사항 (TC 작성 보류 우선)

| No | 이슈 ID | 질문 내용 | 관련 REQ | TC 영향 | 상태 |
|----|---------|---------|---------|--------|------|
| 1 | CONFLICT-001 | Import 옵션 B 선택 시 C.1.1 중복 발생 처리 방식 | REQ-047 | TC 작성 완료 | ✅ 해결: 에러 반환(Import 실패, 오류 메시지) → SC-CASEID-041 |
| 2 | CONFLICT-002 | "Initial 사례" 정의 — 수동 생성 한정 vs Import 포함 | REQ-054 | TC 작성 완료 | ✅ 해결: Import 옵션 A 사용 시 신규 부여 = Initial 사례 → SC-CASEID-047 |
| 3 | CONFLICT-003 | C.1.1/C.1.8.1 수정 불가 시점 | REQ-055 | TC 작성 완료 | ✅ 해결: 부여 즉시 어떤 상태에서도 수정 불가 → SC-CASEID-048 |
| 4 | MISSING-002 | Year 설정 변경 시 기존 케이스 번호 처리 방식 | REQ-016 | TC 작성 완료 | ✅ 해결: 이후 케이스부터 새 설정 적용, 기존 케이스 불변 → SC-CASEID-011 |
| 5 | MISSING-003 | Type of Report Null 케이스에서 구분자 폴백 처리 | REQ-019 | TC 작성 완료 | ✅ 해결: UN 기본 적용 → SC-CASEID-013 |
| 6 | MISSING-004 | PRD/TXT 칩만 추가 시 포맷 설정 영역 활성화 여부 | REQ-033 | TC 작성 완료 | ✅ 해결: 추가된 칩에 대해 활성화 → SC-CASEID-028 |
| 7 | MISSING-005 | 칩 비활성화 후 이전 설정값 저장 범위 (세션 vs DB) | REQ-036 | TC 작성 완료 | ✅ 해결: 세션 내에서만 유지, 새로고침 시 초기화 → SC-CASEID-031 |
| 8 | MISSING-006 | Destination 미확정 상태 C.1.1 표시 방식 | REQ-053 | TC 작성 완료 | ✅ 해결(잠정): 공란으로 표시 → SC-CASEID-046 |
| 9 | MISSING-007 | 만료 팝업 New Case ID 산출 방식 | REQ-039 | TC 작성 완료 | ✅ 해결: 자릿수 확장 후 첫 번째 번호 (99999→100000) → SC-CASEID-034 |
| 10 | MISSING-008 | 하루 보지 않기 후 자릿수 초과 전환 시 사용자 인지 방법 | REQ-042 | TC 작성 완료 | ✅ 해결: 별도 알림 없이 24시간 내 팝업 재노출 가능 → SC-CASEID-037 |
| 11 | MISSING-009 | Import 옵션 A + C.1.8.1 Null 시 자동 복사 규칙 적용 여부 | REQ-046 | N/A 제외 | ✅ 해결: Null 케이스 없음 → REQ-046 N/A |
| 12 | MISSING-010 | 자유 텍스트 최솟값 및 빈값 저장 처리 | REQ-025 | TC 작성 보류 | ⏸ 미해결: 기획자 "확인 필요" → SC-CASEID-021 보류 |
| 13 | MISSING-012 | Product Config 약어 삭제 시 기존 Case ID 처리 | REQ-023 | TC 작성 완료 | ✅ 해결: 기존 케이스 불변, 신규/Import만 반영 → SC-CASEID-018 |
| 14 | CONFIRM-001 | 국가코드 우선순위 3-1번 계층 구조 | REQ-009 | TC 작성 완료 | ✅ 해결: 3번 조건 내부 세부처리, 4단계 유지 → SC-CASEID-004 |
| 15 | CONFIRM-002 | Suspect 자사 제품 "첫 번째 순서" 기준 | REQ-022 | TC 작성 완료 | ✅ 해결: "첫 번째 순서"로 명시(입력 순서) → SC-CASEID-017 |
| 16 | CONFIRM-003 | "최대 생성 가능 숫자" 기준값 정의 | REQ-032 | TC 가능, 전제값 보류 | ⚠️ 보류 유지: TC 작성 가능하나 전제 조건값 확인 필요 → SC-CASEID-027 |
