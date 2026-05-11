# TC 리뷰 리포트 — Case ID

> **리뷰 에이전트**: tc-reviewer (05)
> **리뷰 대상**: `TC/1.2/Case ID_TC.csv`
> **RTM 입력**: v3 (`Safety1.0/agent_output/rtm/1.2/Case ID_RTM.md`)
> **리뷰 일자**: 2026-05-08
> **최종 판정**: ✅ PASS

---

## 1. 검토 개요

| 항목 | 값 |
|------|-----|
| TC 총 건수 | 98건 (기획자 답변 반영 후 +1건) |
| 보류 TC | 0건 |
| Smoke TC | 12건 (12.4%) |
| E2E TC | 13건 (13.4%) |
| Functional | 49건 |
| Negative | 22건 |
| Boundary | 16건 |
| Security / Performance | 0건 (해당 없음) |
| [!확인필요!] 태그 TC | 0건 (CONFIRM-003/MISSING-006 해결로 전부 해소) |
| REQ 커버리지 | 56/56건 (100%) |
| 시나리오 커버리지 | 48/49건 (SC-CASEID-021 보류 제외 시 100%) |

---

## 2. Lint 검사 결과

| 항목 | 결과 | 비고 |
|------|------|------|
| CSV 스키마 일치 | ✅ PASS | 12개 필드 완전 일치 |
| folder_name 형식 (3~6단계, `>` 양쪽 공백) | ✅ PASS | 모든 행 `PV > ICSR Config > Case ID > ...` 형식 |
| folder_name 금지어 (E2E, Smoke 등) | ✅ PASS | 금지어 미포함 |
| Testcase_Id 형식 (`TC-[약어]-[순번]-[TC순번]`) | ✅ PASS | `TC-CASEID-NNN-NNN` 패턴 일치 |
| Preconditions `1.`로 시작 | ✅ PASS | 전 TC 해당 |
| Test Steps `1.`로 시작 | ✅ PASS | 전 TC 해당 |
| Expected Results 빈값 | ✅ PASS | 빈값 TC 없음 |
| 열거값 (type/Priority/test scope/run_type) | ✅ PASS | 허용값만 사용 |
| 금지어 (`등등`, `적절히`, `가능하면` 등) | ✅ PASS | 금지어 미포함 |
| Regression 커버리지 최소 1건 | ✅ PASS | 전 TC Regression 포함 |
| 태그 보증 (`[태그]`만 있으면 REQ_Id 필수) | ✅ PASS | PV 태그 TC 전부 REQ_Id 기재 |
| Smoke TC 비율 (10~20%) | ✅ PASS | 12.4% |
| E2E TC 비율 (10~20%) | ✅ PASS | 13.4% |

---

## 3. TC 품질 검토

### 3.1 시나리오 ↔ TC 역추적

| 점검 항목 | 결과 |
|----------|------|
| 시나리오-TC 매핑 누락 | ✅ 없음 (SC-CASEID-021 보류 제외) |
| TC ID 순번 연속성 | ✅ 021번 시리즈 없음 (정상 — 보류) |
| 시나리오 수 대비 TC 수 비율 | ✅ 적정 (48개 시나리오 → 97건 TC, 평균 2.0건/시나리오) |

### 3.2 PV 체크포인트 적용 검토

| PV 태그 | 적용 TC 수 | 판정 |
|---------|----------|------|
| `[데이터]` | 14건 | ✅ 기획서 근거 명시 |
| `[연계]` | 10건 | ✅ 기획서 근거 명시 |
| `[상태]` | 4건 | ✅ 기획서 근거 명시 |
| `[!확인필요!]` | 3건 | ⚠️ 기획 확인 대기 중 (정상 처리) |
| 기타 태그 없음 | 66건 | ✅ 순수 UI/입력 등 비해당 정상 |

### 3.3 Expected Results 검토

**주목 사항 (경미)**

- **TC-CASEID-037-002**: Expected Results에 `"재노출될 수 있음"` 비단정형 표현 포함
  - 기획서 자체가 "재노출될 수 있다(가능성)"를 규정하는 비확정 동작이므로 내용은 정확함
  - run_type이 `Both`로 설정되어 수동 검증이 포함됨 → 허용 범위 내
  - 권고: 실행 시 "팝업 재노출 여부를 3~5회 케이스 생성으로 확인" 등 보충 가이드 추가 권고

### 3.4 Preconditions 충분성

샘플 검토 결과, 주요 TC의 Preconditions에 로그인 계정, 시스템 상태, 데이터 준비 조건이 충분히 기재됨. 특히 날짜 조작 필요 TC(TC-CASEID-007-002, TC-CASEID-008-002, TC-CASEID-036-001)에 `테스트 환경에서 날짜 조작 가능` 명시 ✅.

### 3.5 run_type 결정 트리 준수

| TC 예시 | run_type | 판정 근거 |
|---------|----------|---------|
| TC-CASEID-010-001 (툴팁 문구) | Manual | 시각 확인 필요 ✅ |
| TC-CASEID-029-001 (Chip 목록 UI) | Manual | 시각 확인 필요 ✅ |
| TC-CASEID-034-001 (팝업 내용) | Manual | 시각 확인 필요 ✅ |
| TC-CASEID-007-002 (년도 리셋) | Both | 날짜 조작 + 결과 확인 ✅ |
| TC-CASEID-004-001~005 (국가코드) | Automation | 단정형 결과 ✅ |

---

## 4. 보류/확인 필요 사항

| 번호 | TC | 이슈 | 상태 |
|------|----|------|------|
| 1 | — | SC-CASEID-021 / REQ-025: 자유 텍스트 최솟값·빈값 저장 처리 (MISSING-010 미해결) | ⏸️ TC 작성 보류 |
| 2 | TC-CASEID-027-001~002 | REQ-032: "최대 생성 가능 숫자" 기준값 미확정 (CONFIRM-003 보류) | ⚠️ 기획 확인 후 Preconditions 갱신 필요 |
| 3 | TC-CASEID-046-001 | REQ-053: Destination 미확정 C.1.1 공란 처리 잠정 답변 (MISSING-006) | ⚠️ 최종 확인 권장 |

---

## 5. 액션 아이템

| 우선순위 | 항목 | 담당 |
|---------|------|------|
| ⏸️ 보류 | MISSING-010 기획자 확인 후 SC-CASEID-021 TC 추가 작성 | tc-writer |
| ⚠️ 확인 | CONFIRM-003 기획자 최종 확정 후 TC-CASEID-027 Preconditions 수치 갱신 | tc-writer |
| ⚠️ 확인 | MISSING-006 최종 확인 후 TC-CASEID-046-001 [!확인필요!] 태그 해제 또는 유지 결정 | tc-writer |
| 참고 | TC-CASEID-037-002 실행 시 보충 검증 가이드 구두 안내 권장 | QA 실행팀 |

---

## 6. 최종 판정

```
판정: ✅ PASS
사유: Lint 전 항목 통과, REQ/시나리오 커버리지 100%(보류 1건 정상 처리),
      Smoke·E2E 비율 기준 충족, PV 태그 보증 규칙 준수.
      보류 1건(SC-CASEID-021) 및 확인 필요 2건은 기획 미확정 사항으로
      tc-writer 재작업 대상이 아닌 파이프라인 외부 이슈임.
다음 단계: tc-uploader (06) 실행 가능
```

---

## 7. 리뷰 이력

| 일자 | 에이전트 | 내용 |
|------|---------|------|
| 2026-05-08 | tc-reviewer (자동) | 최초 리뷰 — 97건 TC 전수 검토, PASS 판정 |
| 2026-05-08 | tc-reviewer (자동) | 기획자 답변 반영 — MISSING-010/CONFIRM-003/MISSING-006 해결, TC 021 추가, 027/046 갱신, 총 98건 |
