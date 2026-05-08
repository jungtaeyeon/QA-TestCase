# Case ID Figma TC 동기화 리포트

## 변경 요약

| 구분 | 건수 | 내용 |
|---|---:|---|
| 신규 추가 | 3 | SC-CID-040~042 Figma 신규 시나리오 TC 추가 |
| 수정 | 0 | 없음 |
| 확장(중복 병합) | 0 | 없음 |
| 중복 제외 | 1 | SC-CID-043은 TC-CID-033-001에서 당일 미노출 정책으로 커버 |
| 삭제 후보 | 0 | 없음 |
| 확인 필요 | 0 | CN-CID-05, CN-CID-06 확인 완료 |

## 신규 추가 TC

| TC ID | 시나리오 | 제목 | 분류 |
|---|---|---|---|
| TC-CID-040-001 | SC-CID-040 | [Figma Only] Preview 보조 정보 노출 검증 | Added |
| TC-CID-041-001 | SC-CID-041 | [Figma Only] Add Segment 중복 추가 차단 검증 | Added |
| TC-CID-042-001 | SC-CID-042 | [Figma Only] 설정 변경 안내 배너 노출 검증 | Added |

## 수정된 TC

없음.

## 기존 TC 확장 (중복 병합)

없음.

## 중복으로 제외된 TC 후보

| 후보 | 제외 사유 | 커버 TC |
|---|---|---|
| SC-CID-043 만료 임박 모달 오늘 하루 보지 않기 UI 별도 TC | TC-CID-033-001이 동일 모달의 체크박스, 확인 버튼, 당일 미노출 정책을 검증함 | TC-CID-033-001 |

## 삭제 후보 TC

없음.

## 확인 필요 사항

없음. CN-CID-05는 `오늘 하루 보지 않기`, CN-CID-06은 `매년 1월 1일` 기준으로 확인 완료됨.

## 설계 기법 적용 요약

| 설계 기법 | 적용 대상 | TC ID 범위 |
|---|---|---|
| 유스케이스 | Preview 보조 정보 표시, Notice Banner 표시 및 적용 시점 안내 | TC-CID-040-001, TC-CID-042-001 |
| 상태전이 | Add Segment 선택형 세그먼트 추가 가능/disabled 상태 전환 | TC-CID-041-001 |

## 시나리오-TC 매핑 (신규/수정분)

| 시나리오 ID | 예상 유형 | 실제 TC type | TC ID | 분화 사유 |
|---|---|---|---|---|
| SC-CID-040 | Functional | Functional | TC-CID-040-001 | 분화 없음 |
| SC-CID-041 | Functional | Functional | TC-CID-041-001 | 분화 없음 |
| SC-CID-042 | Functional | Functional | TC-CID-042-001 | 분화 없음 |
| SC-CID-043 | Functional | Functional | TC-CID-033-001 | 기존 만료 경고 사용자 제어 TC에서 커버 |

## 커버리지 매트릭스

| 기능 영역 | Functional | Negative | Boundary | Security | Performance | 합계 |
|---|---:|---:|---:|---:|---:|---:|
| Preview 보조 정보 | 1 | 0 | 0 | 0 | 0 | 1 |
| Add Segment 상태 | 1 | 0 | 0 | 0 | 0 | 1 |
| Notice Banner | 1 | 0 | 0 | 0 | 0 | 1 |
| 만료 임박 모달 | 1 | 0 | 0 | 0 | 0 | 1 |
| **합계** | **4** | **0** | **0** | **0** | **0** | **4** |

## 검증 메모

- Figma-only 항목은 title과 Memo에 `[Figma Only]`로 표기함.
- 신규 TC의 Expected Results는 화면 표시, 데이터 영향, 하류 영향 관점을 포함함.
- 기존 TC-CID-033-001은 CN-CID-05 확인 결과에 따라 `오늘 하루 보지 않기` 당일 미노출 정책을 이미 검증하므로 별도 중복 TC를 생성하지 않음.
