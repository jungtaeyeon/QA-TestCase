# Case ID 테스트 시나리오

## 개요
- 기획서:
  - Org Level: `Safety1.0/plan/1.0/기획 문서/00. Common (공통 정책)/Admin (Org Admin)/ICSR Config/Case ID/Case ID.md`
  - App Level: `Safety1.0/plan/1.0/기획 문서/01. SafetyDB/Configuration/Case ID (Safety Config)/Case ID (Safety Config).md`
- Figma:
  - `https://www.figma.com/design/UwDGzHxNEV9q5u3IIzmkjo/iVigilance-Square?node-id=18831-28173&m=dev`
  - Node: `18831:28173` (`ICSR Config>Case ID`)
- 참고 정책:
  - `Safety1.0/plan/1.0/기획 문서/00. Common (공통 정책)/Account (+Login, Password)/Account (+Login, Password).md`
  - `Safety1.0/plan/1.0/기획 문서/00. Common (공통 정책)/Audit Log, Activity Log, Audit Trail/Audit Log, Activity Log, Audit Trail.md`
- 작성 기준일: 2026-04-27
- 기준 버전: Case ID 기획서 v1.0.250417, 최신 변경일 2026-04-17
- 기능 범위:
  - Org Level Case ID Configuration 설정 및 저장
  - App Level Case ID 설정값 Read-only 조회
  - Case ID, 보고자 관리번호(C.1.1), 고유식별 보고자 관리번호(C.1.8.1) 생성 및 표시 정책
  - 국가코드, 조직 식별자, 번호 조합, 일련번호, 시작 번호, 만료 경고, 자동 자릿수 확장
  - Import 시 C.1.1/C.1.8.1 유지 정책
  - Case Edit에서 C.1.1 수동 수정 전환 및 Approval 이후 수정 제한
  - Figma 확인 기준 화면 UI 상태: Preview 보조 정보, Add Segment 중복 방지, 설정 변경 안내 배너, 만료 임박 모달 문구
- 제외 범위:
  - AI Convert 적용 상세: v1.0 대상에서 제외
  - 실제 Case 생성 화면의 입력 UI 상세: Case ID 부여 결과와 식별자 전파만 검증
  - 중복/후속 판별 로직의 상세 비교 알고리즘: C.1.8.1이 기준 식별자로 사용되는 연계 영향만 검증
- 주요 용어:
  - Case ID: `[국가코드]-[조직 식별자]-[설정된 번호 조합]` 중 `[설정된 번호 조합]`을 의미하며 Case Edit 및 Tracker의 Case ID에 표시됨
  - Report ID: ICSR 보고서의 C.1.1/C.1.8.1에 표시되는 `국가-조직-일련번호` 형식
  - C.1.1: Sender's Safety Report Unique Identifier, 보고자 관리번호
  - C.1.8.1: Worldwide Unique Case Identification, 고유식별 보고자 관리번호
  - Org Level: Org > Admin > ICSR Config > Case ID 설정 영역
  - App Level: Workspace > Application > Admin > ICSR Config > Case ID 조회 영역

---

## Figma 디자인 대조 요약

| 분류 | Figma 확인 내용 | 시나리오 반영 |
|---|---|---|
| 일치 | 국가코드 자동 필드는 disabled 상태이며, 조직 식별자는 영문/숫자 최대 10자로 표시된다. | SC-CID-008 보강 |
| 일치 | 일련번호 칩은 `일련번호(필수)`로 표시되고, Year/Report Type/Product Abbreviation/Custom Text는 선택형 세그먼트로 표시된다. | SC-CID-015 보강 |
| 추가 | Add Segment 영역에 `클릭 혹은 드래그 앤 드롭하여 추가하세요.` 문구와 선택형 세그먼트 추가 버튼이 표시되며, 이미 추가된 세그먼트는 disabled 상태로 보인다. | SC-CID-041 신규 |
| 추가 | Preview 영역에 리셋 주기와 `연간 최대 처리: 99,999건 (5자리 기준)` 정보가 표시된다. | SC-CID-040 신규, CN-CID-06 확인 완료: `매년 1월 1일` 기준 |
| 추가 | 상단 안내 배너에 `설정을 변경하면 이후 생성되는 케이스부터 적용됩니다. 기존 케이스는 변경되지 않습니다.` 문구가 표시된다. | SC-CID-042 신규 |
| 일치 | Import 옵션 A가 선택 상태이며 `권장` 배지가 표시된다. | SC-CID-025 보강 |
| 변경 반영 | 만료 임박 모달의 체크박스 문구는 `오늘 하루 보지 않기`로 적용한다. | SC-CID-033, SC-CID-043 반영, CN-CID-05 확인 완료 |

---

## 계층 구조

```text
Org Level (Org > Admin > ICSR Config > Case ID)
├── Master Admin: 설정 조회/수정 가능
├── Org Admin: 설정 조회/수정 가능
├── App Admin/App User/External User/Viewer: Org Level 설정 접근 차단
└── 저장된 Case ID 생성 규칙
    │
    ▼
App Level (Workspace > Application > Admin > ICSR Config > Case ID)
├── 권한 부여된 사용자: Org Level 설정값 Read-only 조회
└── 수정/저장 UI 미제공
```

---

## 공통 사전 조건

| 영역 | 기준 | 근거 |
|---|---|---|
| 계정 권한 | Master Admin / Org Admin만 Org Level 설정 수정 가능 | Account.md §2.2, §2.4 |
| 계정 상태 | Active 계정만 접근 가능, Inactive/Locked는 서비스 접근 또는 조작 차단 | Account.md §1.3, §3.4 |
| 세션 | 로그인 후 60분 세션, 만료 5분 전 팝업, 미응답 시 자동 로그아웃 | Account.md §5.1 |
| App Level | Org Admin의 Case ID 설정 정보를 그대로 Read-only 표시 | Case ID (Safety Config).md §제약사의 경우 |
| 식별자 무결성 | 부여된 식별자는 수정 불가 원칙, C.1.8.1은 중복 체크 및 후속 보고 연결 기준 | Case ID.md §ICSR 식별자 관리 사양서 |

---

## 명세 검증 트리

### 트리 구조

- [대분류] Case ID 설정 접근 및 계층
  - [중분류] Org Level 권한
    - Master Admin/Org Admin은 Case ID 설정 화면에 접근하여 수정할 수 있다 [SC-CID-001] ✅
    - App Admin/App User/External User/Viewer는 Org Level Case ID 설정 접근이 차단된다 [SC-CID-002] ✅
    - Inactive/Locked/Invitation 상태 계정은 Case ID 설정 조작이 차단된다 [SC-CID-003] ✅
    - Case ID 설정 중 세션 만료 시 저장되지 않은 변경사항 처리가 정책대로 동작한다 [SC-CID-004] ✅
  - [중분류] App Level 조회
    - App Level Case ID 화면은 Org Level 설정값을 Read-only로 표시한다 [SC-CID-005] ✅
- [대분류] Case ID 구성 규칙
  - [중분류] 기본 표시 및 국가/조직 접두부
    - Preview는 국가-조직-번호 조합을 하이픈 형식으로 실시간 표시한다 [SC-CID-006] ✅
    - 국가코드는 Reporter Country Primary/First, Reaction Country Primary/First, 기본 KR 순으로 결정된다 [SC-CID-007] ✅
    - 조직 식별자는 1~10자 영문/숫자만 허용하고 대소문자를 구분한다 [SC-CID-008] ✅
  - [중분류] 번호 구성 요소
    - Year 선택값은 2-digit/4-digit/N/A에 따라 표시 및 리셋 정책을 결정한다 [SC-CID-009] ✅
    - Year 영역 툴팁은 리셋 정책 안내 문구를 표시한다 [SC-CID-010] ✅
    - Type of Report 체크 시 보고 구분 코드가 Case ID에 자동 추가된다 [SC-CID-011] ✅
    - Product Abbreviation은 제품 불러오기 및 약어 존재 여부에 따라 약어 또는 UNK로 표시된다 [SC-CID-012] ✅
    - Suspect이자 자사 제품이 2개 이상이면 첫 번째 자사 제품 약어를 사용한다 [SC-CID-013] ✅
    - Free Text 선택 시 1~6자 영문/숫자 Custom Text를 설정할 수 있다 [SC-CID-014] ✅
    - 선택형 Format chip 추가/삭제 시 하단 설정 영역 활성화와 이전 설정값 유지가 동작하고, 일련번호 칩은 삭제할 수 없다 [SC-CID-015] ✅
    - Drag & Drop 순서 변경은 Case ID Preview에 즉시 반영된다 [SC-CID-016] ✅
    - Preview 보조 정보는 일련번호 리셋 주기와 연간 최대 처리 건수를 표시한다 [SC-CID-040] ✅
    - Add Segment 영역은 선택형 세그먼트의 중복 추가를 방지하는 disabled 상태를 표시한다 [SC-CID-041] ✅
    - 설정 변경 안내 배너는 변경사항이 이후 생성 케이스부터 적용되고 기존 케이스는 변경되지 않음을 고지한다 [SC-CID-042] ✅
- [대분류] 일련번호 정책
  - [중분류] 자릿수 및 시작 번호
    - 일련번호 자릿수 3~9 선택 시 zero-padding이 적용된다 [SC-CID-017] ✅
    - Start From 기본값 1 및 입력값 N이 저장 후 첫 케이스부터 적용된다 [SC-CID-018] ✅
    - 동일 조합 내 생성 이력이 있으면 최후 번호보다 큰 번호부터 생성된다 [SC-CID-019] ✅
    - Start From은 최대 생성 가능 숫자 - 400을 초과할 수 없다 [SC-CID-020] ✅
    - 한 번 부여된 일련번호는 케이스 삭제 후에도 재사용되지 않는다 [SC-CID-021] ✅
    - 자릿수 변경은 저장 후 생성되는 케이스부터 적용된다 [SC-CID-022] ✅
  - [중분류] 만료 경고 및 자동 확장
    - 남은 번호가 100개 이하가 되면 Case ID 부여 시점에 경고 팝업이 표시된다 [SC-CID-031] ✅
    - 오늘 하루 보지 않기 미선택 후 확인한 사용자는 다음 로그인 시 경고 팝업을 다시 본다 [SC-CID-032] ✅
    - 오늘 하루 보지 않기 선택 후 확인 시 해당 사용자에게 경고 팝업이 당일 다시 노출되지 않는다 [SC-CID-033] ✅
    - 만료 임박 모달은 확인 버튼, 닫기 아이콘, 오늘 하루 보지 않기 체크박스를 제공한다 [SC-CID-043] ✅
    - 최대 자릿수를 초과하면 한 자리 확장된 번호가 자동 부여된다 [SC-CID-034] ✅
    - 확장 번호 체계로 넘어간 후 기존 만료 임박 팝업은 자동 미노출된다 [SC-CID-035] ✅
- [대분류] Case/Report 식별자 생성 및 전파
  - [중분류] Manual 생성
    - Manual Initial 케이스 생성 시 설정된 규칙에 따라 Case ID가 순차 부여된다 [SC-CID-023] ✅
    - Manual Initial 보고서는 C.1.1과 C.1.8.1이 동일하게 생성된다 [SC-CID-024] ✅
  - [중분류] Import 식별자 처리
    - Import 옵션 A는 C.1.1을 신규 부여하고 C.1.8.1 파일값을 유지한다 [SC-CID-025] ✅
    - Import 옵션 B는 C.1.1과 C.1.8.1 파일값을 모두 유지한다 [SC-CID-026] ✅
    - C.1.8.1이 Null인 경우 C.1.1 값을 C.1.8.1에 복사한다 [SC-CID-027] ✅
    - Import에서는 C.1.8.1 기존값이 Sync 대상이 아니며 유지된다 [SC-CID-028] ✅
  - [중분류] 표시 및 식별 기준
    - Case Level은 일련번호, Report Level은 국가-조직-일련번호 형식으로 표시된다 [SC-CID-029] ✅
    - C.1.8.1은 화면 직접 노출 없이 내부 중복 체크 및 후속 보고 연결 기준으로 사용된다 [SC-CID-030] ✅
- [대분류] Case Edit 식별자 수정 제한
  - [중분류] C.1.1 수정 전환
    - C.1.1 수정 버튼 클릭 시 수동 변경 경고 알럿이 표시되고 Confirm/Cancel 분기가 동작한다 [SC-CID-036] ✅
    - Approval 상태 이후 C.1.1/C.1.8.1 수정 UI는 제공되지 않는다 [SC-CID-037] ✅
    - Manual 생성 건의 C.1.8.1은 변경할 수 없다 [SC-CID-038] ✅
- [대분류] 감사 추적
  - [중분류] Org Audit Log
    - Case ID 생성 규칙 및 Import 식별자 처리 방식 변경 시 Org Audit Log가 항목 단위로 기록된다 [SC-CID-039] ✅
  - [중분류] AI Convert 적용
    - AI Convert에 동일 정책 적용 [CID-EX-001] ➖ (문서에 추후 적용 예정으로 표시)

### 커버리지 요약

| 대분류 | 전체 | ✅ 연결 | ⏸️ 보류 | ➖ 제외 | ❌ 미작성 | 처리율 | 완료율 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Case ID 설정 접근 및 계층 | 5 | 5 | 0 | 0 | 0 | 100% | 100% |
| Case ID 구성 규칙 | 14 | 14 | 0 | 0 | 0 | 100% | 100% |
| 일련번호 정책 | 12 | 12 | 0 | 0 | 0 | 100% | 100% |
| Case/Report 식별자 생성 및 전파 | 8 | 8 | 0 | 0 | 0 | 100% | 100% |
| Case Edit 식별자 수정 제한 | 3 | 3 | 0 | 0 | 0 | 100% | 100% |
| 감사 추적 | 2 | 1 | 0 | 1 | 0 | 100% | 100% |
| **합계** | **44** | **43** | **0** | **1** | **0** | **100%** | **100%** |

> 게이트 판정: ✅ PASS. `❌ 미작성` 및 `⏸️ 보류` 노드 0건. `➖ 제외` 1건은 AI Convert 추후 적용 항목이다.

---

## 시나리오 목록

| ID | 우선순위 | 관점 | 기법 | 시나리오 제목 | 검증 목적 | 근거 | 비고 |
|---|---|---|---|---|---|---|---|
| SC-CID-001 | Critical | Business | 결정테이블 | Master Admin/Org Admin이 Org Level Case ID 설정에 접근하면 수정 가능한 상태로 표시된다 | 설정 가능 역할의 접근 및 수정 권한 검증 | Case ID.md §와이어프레임, Account.md §2.2, §2.4 | 상위 계정 정책 필수 |
| SC-CID-002 | High | Business | 결정테이블 | App Admin 이하 역할이 Org Level Case ID 설정에 접근하려 하면 메뉴 미노출 또는 접근 차단된다 | 하위 역할의 Org Level 설정 변경 차단 검증 | Account.md §2.2, §2.4, Sender_시나리오 권한 패턴 | 권한 공통 회귀 |
| SC-CID-003 | High | Business | 상태전이 | Inactive/Locked/Invitation 상태 계정은 Case ID 설정 조회 또는 저장을 수행할 수 없다 | 계정 상태 기반 접근 차단 검증 | Account.md §1.3, §3.4 | 계정 정책 확인 필수 |
| SC-CID-004 | Medium | Non-Functional | 비기능요구사항 | Case ID 설정 편집 중 세션이 만료되면 정책에 따라 자동 로그아웃되고 미저장 변경사항이 저장되지 않는다 | 장시간 설정 작업 중 세션 만료 영향 검증 | Account.md §5.1 | 저장 전/후 분기 TC 필요 |
| SC-CID-005 | High | Functional | 유스케이스 | App Level Case ID 화면은 Org Level 설정 정보를 Read-only로 표시하고 수정 UI를 제공하지 않는다 | Safety Config 조회 전용 정책 검증 | Case ID (Safety Config).md §제약사의 경우 | App Level 포함 |
| SC-CID-006 | High | Functional | 유스케이스 | Case ID Preview는 국가-조직-번호 조합과 하이픈을 실시간으로 표시한다 | Preview 표시 형식 및 고정 영역 검증 | Case ID.md §기본 구조, §와이어프레임 #1, Figma `Breadcrumb & Preview` | Tracker 안내 문구 포함 |
| SC-CID-007 | Critical | Business | 결정테이블 | 케이스 정보의 국가코드가 우선순위에 따라 Case ID 접두사로 결정된다 | 국가코드 결정 우선순위 검증 | Case ID.md §국가 코드 로직 | Primary/First/기본 KR 분기 |
| SC-CID-008 | High | Data | 경계값분석 | 조직 식별자는 1~10자 영문/숫자만 허용하고 대소문자를 구분하여 Preview에 반영된다 | 조직 식별자 입력 Validation 검증 | Case ID.md §조직 식별자 입력, §와이어프레임 #2 | |
| SC-CID-009 | Critical | Business | 결정테이블 | Year 설정이 2-digit/4-digit/N/A에 따라 표시 형식과 일련번호 리셋 정책을 결정한다 | 연도 표시 및 연 단위/누적 채번 정책 검증 | Case ID.md §Year | 확인 완료: 현재 선택지는 3종 |
| SC-CID-010 | Low | Functional | 유스케이스 | Year 설정 툴팁을 열면 2-digit/4-digit 선택 시 연 단위 리셋, N/A 선택 시 누적 증가 안내가 표시된다 | 사용자 안내 문구 노출 검증 | Case ID.md §Year 툴팁 | Year+Month 삭제 기준 반영 |
| SC-CID-011 | High | Business | 결정테이블 | Type of Report 체크 시 케이스의 보고 구분값에 따라 SP/RS/OT/UN 코드가 자동 추가된다 | 보고 구분 코드 매핑 검증 | Case ID.md §Type of Report | |
| SC-CID-012 | High | Data | 결정테이블 | 제품 불러오기로 제품 정보가 포함되면 Product Abbreviation이 활성화되고 값이 없으면 UNK가 표시된다 | 제품 약어 데이터 참조 및 fallback 검증 | Case ID.md §Product Abbreviation | PRD 칩 별도 선택/삭제 가능 |
| SC-CID-013 | High | Data | 결정테이블 | Suspect이자 자사 제품이 2개 이상이면 첫 번째 순서의 자사 제품 약어가 표시된다 | 다중 제품 선택 시 대표 약어 결정 검증 | Case ID.md §Product Abbreviation | Product Config 연계 |
| SC-CID-014 | Medium | Data | 경계값분석 | Free Text 선택 시 Custom Text는 1~6자 영문/숫자만 입력 가능하다 | 자유 텍스트 Validation 검증 | Case ID.md §자유 텍스트 | |
| SC-CID-015 | Medium | Functional | 상태전이 | Year/TR/PRD/TXT 등 선택형 Format chip 추가/삭제 시 하단 설정 영역이 활성/비활성 전환되고, 일련번호 칩은 삭제할 수 없다 | Chip 상태 전이 및 설정값 보존 검증 | Case ID.md §포맷 설정, §와이어프레임 #3, Figma `Segment Builder` | Figma: 일련번호(필수) 칩 고정 |
| SC-CID-016 | High | Functional | 유스케이스 | Format chip을 Drag & Drop으로 재정렬하면 Preview의 번호 조합 순서가 즉시 변경된다 | 구성 요소 순서 변경과 Preview 동기화 검증 | Case ID.md §포맷 설정 및 인터랙션 | |
| SC-CID-017 | High | Data | 경계값분석 | 일련번호 자릿수 3~9 선택 시 선택한 길이만큼 zero-padding이 적용된다 | serial number 표시 길이 검증 | Case ID.md §일련번호 자릿수 설정 | 확인 완료: UI 허용 범위 3~9 |
| SC-CID-018 | High | Business | 경계값분석 | Start From 기본값은 1이고 N 입력 후 저장하면 첫 생성 케이스가 N부터 채번된다 | 시작 번호 적용 시점 검증 | Case ID.md §시작 번호 설정 | |
| SC-CID-019 | Critical | Business | 결정테이블 | 동일 조합 내 생성 이력이 있으면 Start From보다 최후 생성 번호가 우선되어 다음 번호가 생성된다 | 최후 번호 검증 규칙 검증 | Case ID.md §최후 번호 검증 규칙 | 중복 방지 핵심 |
| SC-CID-020 | High | Data | 경계값분석 | Start From은 최대 생성 가능 숫자 - 400을 초과하여 설정할 수 없다 | 번호 고갈 방지 제한 검증 | Case ID.md §시작 번호 설정 제한 정책 | |
| SC-CID-021 | Critical | Data | 데이터생명주기분석 | 부여된 일련번호는 케이스가 삭제되어도 재사용되지 않는다 | 식별자 재사용 방지 및 감사성 검증 | Case ID.md §필수 룰, §ID 재사용 방지 | PV 식별자 무결성 |
| SC-CID-022 | Medium | Flow | 상태전이 | 일련번호 자릿수를 변경하면 이후 생성되는 케이스부터 변경된 자릿수가 적용된다 | 설정 변경 적용 시점 검증 | Case ID.md §일련번호 자릿수 설정 | 기존 케이스 영향 없음 |
| SC-CID-023 | Critical | Flow | 유스케이스 | Manual Initial 케이스 생성 시 Configuration 설정에 따른 Case ID가 순차 부여된다 | Manual 생성의 Case ID 부여 흐름 검증 | Case ID.md §생성 유형별 식별자 부여 로직 | [E2E] |
| SC-CID-024 | Critical | Data | 데이터생명주기분석 | Manual Initial 보고서에서 C.1.1과 C.1.8.1이 동일한 Report ID로 생성된다 | Manual 생성 식별자 동기화 검증 | Case ID.md §매뉴얼 케이스 생성 | 규제 보고 식별자 |
| SC-CID-025 | Critical | Business | 결정테이블 | Import 옵션 A 선택 시 C.1.1은 신규 부여되고 C.1.8.1은 파일 내 값을 유지한다 | 기본 Import 처리 방식 검증 | Case ID.md §Import 설정 옵션 A, Figma `Import Settings Card` | Default, Figma 권장 배지 |
| SC-CID-026 | High | Business | 결정테이블 | Import 옵션 B 선택 시 C.1.1과 C.1.8.1 모두 파일 내 값을 유지한다 | Migration 목적 유지 옵션 검증 | Case ID.md §Import 설정 옵션 B | |
| SC-CID-027 | High | Data | 결정테이블 | C.1.8.1 값이 Null이면 C.1.1 값을 C.1.8.1에 복사한다 | 고유식별자 보완 Sync 검증 | Case ID.md §C.1.1, C.1.8.1 동일 입력 설정 | |
| SC-CID-028 | Critical | Data | 데이터생명주기분석 | Import로 인입된 C.1.8.1 기존값은 Sync 대상이 아니며 유지된다 | 기존 고유식별자 보호 검증 | Case ID.md §값 유지 선택 및 동기화 | 후속/중복 연결 영향 |
| SC-CID-029 | High | Functional | 동등분할 | Case Level은 일련번호만, Report Level은 국가-조직-일련번호 형식으로 표시된다 | 화면 성격별 식별자 노출 형식 검증 | Case ID.md §Case vs Report 식별자 노출 사양 | Tracker/Case/ICSR |
| SC-CID-030 | Critical | Business | 도메인리스크 | C.1.8.1은 화면에 직접 노출되지 않아도 내부 중복 체크 및 후속 보고 연결 기준으로 유지된다 | PV 중복/후속 보고 식별 기준 검증 | Case ID.md §Case vs Report 식별자 노출 사양, §생성 유형별 식별자 부여 로직 | 도메인 리스크 |
| SC-CID-031 | High | Flow | 경계값분석 | Case ID 부여 후 남은 번호가 100개 이하가 되면 모든 사용자에게 만료 임박 팝업이 표시된다 | 번호 고갈 사전 경고 검증 | Case ID.md §Case ID 만료 임박 알림 | 팝업은 생성 시점 |
| SC-CID-032 | Medium | Functional | 상태전이 | 만료 임박 팝업에서 오늘 하루 보지 않기를 선택하지 않고 확인하면 해당 사용자의 다음 로그인 시 팝업이 다시 표시된다 | 팝업 닫기 상태 전이 검증 | Case ID.md §사용자 인터랙션 및 제어, Figma `Modal` | Figma 확인 버튼 문구: `확인` |
| SC-CID-033 | Medium | Functional | 상태전이 | 오늘 하루 보지 않기 선택 후 확인하면 해당 사용자에게 팝업이 당일 다시 표시되지 않는다 | 사용자별 당일 미노출 설정 검증 | Case ID.md §사용자 인터랙션 및 제어, Figma `Modal` | CN-CID-05 확인 완료 |
| SC-CID-034 | Critical | Business | 경계값분석 | 설정된 최대 자릿수를 초과하면 한 자리 확장된 번호가 자동으로 부여된다 | 서비스 중단 없는 자동 확장 검증 | Case ID.md §Case ID 자릿수 자동 확장 | 99999 다음 100000 |
| SC-CID-035 | High | Flow | 상태전이 | 확장 번호 체계로 넘어간 후 기존 만료 임박 팝업은 자동으로 노출되지 않는다 | 확장 이후 팝업 종료 조건 검증 | Case ID.md §사용자 인터랙션 및 제어, §자릿수 확장 | |
| SC-CID-036 | High | Business | 결정테이블 | Case Edit에서 C.1.1 수정 버튼 클릭 시 경고 알럿이 표시되고 Confirm 시 Sync가 끊기며 Cancel 시 연결 상태가 유지된다 | C.1.1 수동 수정 전환 분기 검증 | Case ID.md §Case Edit에서 동작 | |
| SC-CID-037 | Critical | Business | 상태전이 | Approval 상태 이후 C.1.1/C.1.8.1 수정 버튼은 표시되지 않고 수정 불가 안내 문구가 표시된다 | 승인 이후 식별자 변경 차단 검증 | Case ID.md §C.1.1 변경 시점 | 규제 식별자 보호 |
| SC-CID-038 | Critical | Business | 도메인리스크 | Manual 생성 건의 C.1.8.1은 사용자가 변경할 수 없다 | 고유식별 보고자 관리번호 불변성 검증 | Case ID.md §Manual에 C.1.8.1 변경 불가 | 교육/매뉴얼 고지 포함 |
| SC-CID-039 | High | Non-Functional | 데이터생명주기분석 | Case ID 생성 규칙 또는 Import 식별자 처리 방식 변경 시 Org Audit Log에 행위자와 변경 전/후 값이 기록된다 | 감사 추적성 검증 | Audit Log.md §6.2.4 Default Rule | 상위 정책 반영 |
| SC-CID-040 | Medium | Functional | 유스케이스 | [Figma Only] Preview 보조 정보가 일련번호 리셋 주기와 연간 최대 처리 건수를 표시한다 | 사용자가 현재 채번 주기와 처리 한도를 Preview에서 인지할 수 있는지 검증 | Figma `Period Info` | CN-CID-06 확인 완료: `매년 1월 1일` |
| SC-CID-041 | Medium | Functional | 상태전이 | [Figma Only] Add Segment 영역에서 이미 추가된 선택형 세그먼트는 중복 추가할 수 없는 disabled 상태로 표시된다 | 세그먼트 중복 추가 방지와 선택 가능 상태 검증 | Figma `Add Segment Area`, `Add Item` | Year/TR/PRD/TXT 추가 버튼 |
| SC-CID-042 | Medium | Functional | 유스케이스 | [Figma Only] Case ID 설정 화면 상단에 이후 생성 케이스부터 적용 및 기존 케이스 미변경 안내가 표시된다 | 설정 변경 적용 시점 안내 문구 노출 검증 | Figma `Notice Banner` | SC-CID-022와 정책 연계 |
| SC-CID-043 | Medium | Functional | 상태전이 | [Figma] 만료 임박 모달의 오늘 하루 보지 않기 체크박스와 확인 버튼이 표시된다 | 사용자의 팝업 재노출 제어 UI 및 당일 미노출 정책 검증 | Case ID.md §사용자 인터랙션 및 제어, Figma `Modal` | CN-CID-05 확인 완료 |

---

## 기능 분해

| 화면/업무 흐름 | 기능 영역 | 세부 동작 | 관련 근거 |
|---|---|---|---|
| Org Level Case ID | 접근 권한 | Master Admin/Org Admin 수정 가능, 하위 역할 접근 차단 | Account.md §2.2, §2.4 |
| Org Level Case ID | 계정 상태 | Active만 조작 가능, Inactive/Locked/Invitation 차단 | Account.md §1.3, §3.4 |
| App Level Case ID | Read-only 조회 | Org Level 설정값 그대로 표시, 수정 UI 미제공 | Case ID (Safety Config).md |
| Preview | 표시 형식 | 국가-조직-번호 조합, 하이픈, 상단 고정, 실시간 반영 | Case ID.md §기본 구조, §와이어프레임 |
| Preview | 보조 정보 | Tracker의 Case ID는 국가코드와 조직 식별자를 제외한다는 안내, 리셋 주기, 연간 최대 처리 건수 표시 | Figma `Breadcrumb & Preview` |
| 국가코드 | 접두사 결정 | Reporter Country Primary/First → Reaction Country Primary/First → KR | Case ID.md §국가 코드 로직 |
| 조직 식별자 | 입력 규칙 | 1~10자, 영문/숫자, 대소문자 구분 | Case ID.md §조직 식별자 입력 |
| 번호 구성 | Year | 2-digit/4-digit/N/A, 연 단위 리셋 또는 누적 | Case ID.md §Year |
| 번호 구성 | Type of Report | Spontaneous/Study/Other/Unknown 코드 매핑 | Case ID.md §Type of Report |
| 번호 구성 | Product Abbreviation | Product Config 약어 참조, 미존재 시 UNK, 다중 자사제품 첫 번째 | Case ID.md §Product Abbreviation |
| 번호 구성 | Free Text | 1~6자 영문/숫자 Custom Text | Case ID.md §자유 텍스트 |
| 포맷 설정 | Chip/Drag & Drop | Year/TR/PRD/TXT 등 선택형 칩 추가/삭제, 일련번호 칩 고정, 설정 영역 활성화, Preview 순서 반영 | Case ID.md §포맷 설정 |
| 포맷 설정 | Add Segment | 선택형 세그먼트 추가 버튼, 이미 추가된 항목 disabled 상태, 클릭 또는 Drag & Drop 추가 안내 | Figma `Add Segment Area` |
| 설정 안내 | Notice Banner | 설정 변경은 이후 생성 케이스부터 적용되고 기존 케이스는 변경되지 않음 | Figma `Notice Banner`, Case ID.md §일련번호 자릿수 설정 |
| 일련번호 | 자릿수/Start From | 3~9 자릿수 zero-padding, 기본값 1, 저장 후 첫 케이스부터 적용 | Case ID.md §일련번호 및 시작점 |
| 일련번호 | 최후 번호/재사용 방지 | 동일 조합 생성 이력 기준, 삭제 후 재사용 금지 | Case ID.md §최후 번호 검증, §ID 재사용 방지 |
| 만료 경고 | 팝업 | 남은 번호 100개 이하, Case ID 최종 부여 순간 노출 | Case ID.md §만료 임박 알림 |
| 자동 확장 | 번호 확장 | 최대값 초과 시 한 자리 확장, 기존 팝업 중단 | Case ID.md §자동 자릿수 확장 |
| Manual 생성 | C.1.1/C.1.8.1 | C.1.1과 C.1.8.1 동일, Destination 확정 시 국가 코드 결정 | Case ID.md §매뉴얼 케이스 생성 |
| Import | 식별자 유지 | 옵션 A/B, C.1.8.1 기존값 보호, Null 시 C.1.1 복사 | Case ID.md §Import 설정 |
| Import | 기본 옵션 UI | 옵션 A 선택 상태와 `권장` 배지 표시 | Figma `Import Settings Card` |
| Case Edit | 수정 제한 | C.1.1 수동 수정 경고, Approval 이후 수정 불가, C.1.8.1 변경 불가 | Case ID.md §Case Edit에서 동작 |
| 만료 경고 | 모달 제어 | 확인 버튼, 닫기 아이콘, 재노출 제어 체크박스 문구 검증 | Figma `Modal`, Case ID.md §사용자 인터랙션 및 제어 |
| 감사 로그 | 변경 기록 | Case ID Rule/Import ID handling 변경 항목별 기록 | Audit Log.md §6.2.4 |

---

## 관점 매핑 요약

| 기능 영역 | Functional | Business | Data | Non-Functional | Flow | 비고 |
|---|---|---|---|---|---|---|
| 권한/계정 상태 | 적용 | 적용 | 미적용 | 적용 | 적용 | Account 정책 필수 |
| App Level Read-only | 적용 | 적용 | 미적용 | 미적용 | 미적용 | Safety Config 연계 |
| Preview/포맷 설정 | 적용 | 적용 | 적용 | 미적용 | 적용 | Drag & Drop, Add Segment disabled 상태 포함 |
| 국가/조직 식별자 | 적용 | 적용 | 적용 | 미적용 | 미적용 | 접두부 정합성 |
| 번호 구성 요소 | 적용 | 적용 | 적용 | 미적용 | 미적용 | Year/TR/PRD/TXT/Serial |
| 일련번호 정책 | 미적용 | 적용 | 적용 | 미적용 | 적용 | 시작점/최후 번호/재사용 방지 |
| 만료 경고/자동 확장 | 적용 | 적용 | 적용 | 미적용 | 적용 | 경계값, 상태 전이, 모달 재노출 문구 포함 |
| Manual/Import 식별자 | 적용 | 적용 | 적용 | 미적용 | 적용 | C.1.1/C.1.8.1 |
| Case Edit 수정 제한 | 적용 | 적용 | 적용 | 미적용 | 적용 | Approval 이후 불변성 |
| 감사 로그 | 적용 | 적용 | 적용 | 적용 | 미적용 | Org Audit Log |

---

## 요구사항 추적 매트릭스 (RTM)

| 요구사항 ID | 요구사항 내용 | 유형 | 제외 여부 | 연관 시나리오 ID | TC ID 범위 | 상태 |
|---|---|---|---|---|---|---|
| CID-REQ-001 | Master Admin/Org Admin은 Org Level Case ID 설정을 수정할 수 있다 | 권한/역할 | - | SC-CID-001 | TC-CID-001-001~TC-CID-001-002 | ✅ TC 작성 완료 |
| CID-REQ-002 | 하위 역할은 Org Level Case ID 설정 접근 또는 수정이 차단된다 | 권한/역할 | - | SC-CID-002 | TC-CID-002-001~TC-CID-002-002 | ✅ TC 작성 완료 |
| CID-REQ-003 | Inactive/Locked/Invitation 계정은 Case ID 설정 조작이 차단된다 | 권한/역할 | - | SC-CID-003 | TC-CID-003-001 | ✅ TC 작성 완료 |
| CID-REQ-004 | 60분 세션 정책이 Case ID 설정 화면에도 적용된다 | 상태 전이 | - | SC-CID-004 | TC-CID-004-001 | ✅ TC 작성 완료 |
| CID-REQ-005 | App Level은 Org Level Case ID 설정값을 Read-only로 표시한다 | 화면 상태 | - | SC-CID-005 | TC-CID-005-001 | ✅ TC 작성 완료 |
| CID-REQ-006 | Preview는 국가-조직-번호 조합을 하이픈 형식으로 표시한다 | 화면 상태 | - | SC-CID-006 | TC-CID-006-001 | ✅ TC 작성 완료 |
| CID-REQ-007 | 국가코드는 문서의 우선순위에 따라 자동 결정된다 | 비즈니스 규칙 | - | SC-CID-007 | TC-CID-007-001 | ✅ TC 작성 완료 |
| CID-REQ-008 | 조직 식별자는 1~10자 영문/숫자만 허용한다 | 데이터 규칙 | - | SC-CID-008 | TC-CID-008-001~TC-CID-008-003 | ✅ TC 작성 완료 |
| CID-REQ-009 | Year 선택은 표시 형식과 번호 리셋 정책을 함께 결정한다 | 비즈니스 규칙 | - | SC-CID-009, SC-CID-010 | TC-CID-009-001~TC-CID-010-001 | ✅ TC 작성 완료 |
| CID-REQ-010 | Type of Report 값에 따라 SP/RS/OT/UN 코드가 추가된다 | 비즈니스 규칙 | - | SC-CID-011 | TC-CID-011-001 | ✅ TC 작성 완료 |
| CID-REQ-011 | Product Abbreviation은 Product Config 약어를 참조하고 없으면 UNK로 표시한다 | 데이터 규칙 | - | SC-CID-012, SC-CID-013 | TC-CID-012-001~TC-CID-013-001 | ✅ TC 작성 완료 |
| CID-REQ-012 | Free Text는 1~6자 영문/숫자만 허용한다 | 데이터 규칙 | - | SC-CID-014 | TC-CID-014-001~TC-CID-014-002 | ✅ TC 작성 완료 |
| CID-REQ-013 | 선택형 Format chip 추가/삭제와 Drag & Drop은 Preview에 반영되며 일련번호 칩은 삭제할 수 없다 | 기능 동작 | - | SC-CID-015, SC-CID-016 | TC-CID-015-001~TC-CID-016-001 | ✅ TC 작성 완료 |
| CID-REQ-014 | 일련번호 자릿수 3~9 선택 시 zero-padding이 적용된다 | 데이터 규칙 | - | SC-CID-017 | TC-CID-017-001~TC-CID-017-002 | ✅ TC 작성 완료 |
| CID-REQ-015 | Start From은 저장 후 첫 케이스부터 적용된다 | 비즈니스 규칙 | - | SC-CID-018 | TC-CID-018-001 | ✅ TC 작성 완료 |
| CID-REQ-016 | 생성 이력이 있으면 동일 조합 내 최후 번호보다 큰 번호로 생성된다 | 비즈니스 규칙 | - | SC-CID-019 | TC-CID-019-001 | ✅ TC 작성 완료 |
| CID-REQ-017 | Start From은 최대 생성 가능 숫자 - 400을 초과할 수 없다 | 데이터 규칙 | - | SC-CID-020 | TC-CID-020-001~TC-CID-020-002 | ✅ TC 작성 완료 |
| CID-REQ-018 | 한 번 부여된 번호는 삭제 후에도 재사용되지 않는다 | 데이터 규칙 | - | SC-CID-021 | TC-CID-021-001 | ✅ TC 작성 완료 |
| CID-REQ-019 | 자릿수 변경은 이후 생성 케이스부터 적용된다 | 상태 전이 | - | SC-CID-022 | TC-CID-022-001 | ✅ TC 작성 완료 |
| CID-REQ-020 | Manual Initial 케이스 생성 시 설정 규칙에 따라 Case ID가 순차 부여된다 | 연동/배치 | - | SC-CID-023 | TC-CID-023-001 | ✅ TC 작성 완료 |
| CID-REQ-021 | Manual Initial 보고서에서 C.1.1과 C.1.8.1은 동일하게 생성된다 | 데이터 규칙 | - | SC-CID-024 | TC-CID-024-001 | ✅ TC 작성 완료 |
| CID-REQ-022 | Import 옵션 A는 C.1.1 신규 부여, C.1.8.1 파일값 유지를 수행한다 | 비즈니스 규칙 | - | SC-CID-025 | TC-CID-025-001 | ✅ TC 작성 완료 |
| CID-REQ-023 | Import 옵션 B는 C.1.1/C.1.8.1 파일값 모두 유지를 수행한다 | 비즈니스 규칙 | - | SC-CID-026 | TC-CID-026-001 | ✅ TC 작성 완료 |
| CID-REQ-024 | C.1.8.1 Null 시 C.1.1 값을 C.1.8.1에 복사한다 | 데이터 규칙 | - | SC-CID-027 | TC-CID-027-001 | ✅ TC 작성 완료 |
| CID-REQ-025 | Import 인입 C.1.8.1 기존값은 Sync 대상이 아니며 유지된다 | 데이터 규칙 | - | SC-CID-028 | TC-CID-028-001 | ✅ TC 작성 완료 |
| CID-REQ-026 | Case Level과 Report Level은 서로 다른 표시 형식을 사용한다 | 화면 상태 | - | SC-CID-029 | TC-CID-029-001 | ✅ TC 작성 완료 |
| CID-REQ-027 | C.1.8.1은 내부 중복 체크 및 후속 보고 연결 기준으로 사용된다 | 비즈니스 규칙 | - | SC-CID-030 | TC-CID-030-001 | ✅ TC 작성 완료 |
| CID-REQ-028 | 남은 번호가 100개 이하가 되면 Case ID 부여 시점에 팝업이 노출된다 | 상태 전이 | - | SC-CID-031 | TC-CID-031-001~TC-CID-031-002 | ✅ TC 작성 완료 |
| CID-REQ-029 | 오늘 하루 보지 않기를 선택하지 않고 확인한 사용자는 다음 로그인 시 팝업을 다시 본다 | 상태 전이 | - | SC-CID-032 | TC-CID-032-001 | ✅ TC 작성 완료 |
| CID-REQ-030 | 오늘 하루 보지 않기 선택 후 확인 시 팝업이 당일 다시 노출되지 않는다 | 상태 전이 | - | SC-CID-033 | TC-CID-033-001 | ✅ TC 작성 완료 |
| CID-REQ-031 | 최대 자릿수를 초과하면 한 자리 확장된 번호가 자동 부여된다 | 비즈니스 규칙 | - | SC-CID-034 | TC-CID-034-001 | ✅ TC 작성 완료 |
| CID-REQ-032 | 자동 확장 후 기존 만료 임박 팝업은 중단된다 | 상태 전이 | - | SC-CID-035 | TC-CID-035-001 | ✅ TC 작성 완료 |
| CID-REQ-033 | C.1.1 수동 수정 전환 시 경고 알럿 및 Confirm/Cancel 분기가 동작한다 | 기능 동작 | - | SC-CID-036 | TC-CID-036-001~TC-CID-036-002 | ✅ TC 작성 완료 |
| CID-REQ-034 | Approval 상태 이후 C.1.1/C.1.8.1 수정은 불가하다 | 비즈니스 규칙 | - | SC-CID-037 | TC-CID-037-001 | ✅ TC 작성 완료 |
| CID-REQ-035 | Manual 생성 건의 C.1.8.1은 변경할 수 없다 | 비즈니스 규칙 | - | SC-CID-038 | TC-CID-038-001 | ✅ TC 작성 완료 |
| CID-REQ-036 | Case ID Rule 및 Import ID handling 변경은 Org Audit Log에 기록된다 | 연동/배치 | - | SC-CID-039 | TC-CID-039-001 | ✅ TC 작성 완료 |
| CID-REQ-037 | [Figma Only] Preview 보조 정보는 리셋 주기와 연간 최대 처리 건수를 표시한다 | 화면 상태 | - | SC-CID-040 | TC-CID-040-001 | ✅ TC 작성 완료 |
| CID-REQ-038 | [Figma Only] Add Segment 영역은 선택형 세그먼트 중복 추가를 방지한다 | 기능 동작 | - | SC-CID-041 | TC-CID-041-001 | ✅ TC 작성 완료 |
| CID-REQ-039 | [Figma Only] 설정 변경 안내 배너는 이후 생성 케이스부터 적용 및 기존 케이스 미변경을 고지한다 | 화면 상태 | - | SC-CID-042 | TC-CID-042-001 | ✅ TC 작성 완료 |
| CID-REQ-040 | [Figma] 만료 임박 모달은 오늘 하루 보지 않기 체크박스와 확인 버튼을 제공한다 | 상태 전이 | - | SC-CID-043 | TC-CID-033-001 | ✅ TC 작성 완료 |
| CID-EX-001 | AI Convert에 Import 식별자 정책 적용 | 연동/배치 | ➖ 추후 적용 | - | - | ➖ 제외 |

---

## TC 매핑 상태

| 시나리오 ID | 시나리오 제목 | 예상 TC 유형 | TC ID 범위 | TC 작성 상태 |
|---|---|---|---|---|
| SC-CID-001 | Master Admin/Org Admin Case ID 설정 수정 가능 | Functional/Security | TC-CID-001-001~TC-CID-001-002 | ✅ 작성 완료 |
| SC-CID-002 | 하위 역할 Org Level 접근 차단 | Security/Negative | TC-CID-002-001~TC-CID-002-002 | ✅ 작성 완료 |
| SC-CID-003 | 비정상 계정 상태 접근 차단 | Security/Negative | TC-CID-003-001 | ✅ 작성 완료 |
| SC-CID-004 | 설정 중 세션 만료 처리 | Non-Functional/Regression | TC-CID-004-001 | ✅ 작성 완료 |
| SC-CID-005 | App Level Read-only 조회 | Functional/Regression | TC-CID-005-001 | ✅ 작성 완료 |
| SC-CID-006 | Preview 하이픈 형식 실시간 표시 | Functional | TC-CID-006-001 | ✅ 작성 완료 |
| SC-CID-007 | 국가코드 우선순위 결정 | Functional/Business | TC-CID-007-001 | ✅ 작성 완료 |
| SC-CID-008 | 조직 식별자 Validation | Boundary/Negative | TC-CID-008-001~TC-CID-008-003 | ✅ 작성 완료 |
| SC-CID-009 | Year 표시 및 리셋 정책 | Functional/Business | TC-CID-009-001~TC-CID-009-002 | ✅ 작성 완료 |
| SC-CID-010 | Year 툴팁 문구 | Functional | TC-CID-010-001 | ✅ 작성 완료 |
| SC-CID-011 | Type of Report 코드 매핑 | Functional/Business | TC-CID-011-001 | ✅ 작성 완료 |
| SC-CID-012 | Product Abbreviation 활성화 및 UNK fallback | Functional/Data | TC-CID-012-001 | ✅ 작성 완료 |
| SC-CID-013 | 다중 자사 제품 첫 번째 약어 선택 | Functional/Data | TC-CID-013-001 | ✅ 작성 완료 |
| SC-CID-014 | Free Text Validation | Boundary/Negative | TC-CID-014-001~TC-CID-014-002 | ✅ 작성 완료 |
| SC-CID-015 | 선택형 Chip 추가/삭제 및 일련번호 칩 고정 | Functional | TC-CID-015-001~TC-CID-015-002 | ✅ 작성 완료 |
| SC-CID-016 | Drag & Drop Preview 반영 | Functional | TC-CID-016-001 | ✅ 작성 완료 |
| SC-CID-017 | Serial digit zero-padding | Boundary | TC-CID-017-001~TC-CID-017-002 | ✅ 작성 완료 |
| SC-CID-018 | Start From 기본값 및 적용 | Functional/Boundary | TC-CID-018-001 | ✅ 작성 완료 |
| SC-CID-019 | 최후 번호 우선 생성 | Business/Regression | TC-CID-019-001 | ✅ 작성 완료 |
| SC-CID-020 | Start From 최대값 제한 | Boundary/Negative | TC-CID-020-001~TC-CID-020-002 | ✅ 작성 완료 |
| SC-CID-021 | 삭제 후 번호 미재사용 | Data/Regression | TC-CID-021-001 | ✅ 작성 완료 |
| SC-CID-022 | 자릿수 변경 이후 생성건 적용 | Functional/Regression | TC-CID-022-001 | ✅ 작성 완료 |
| SC-CID-023 | Manual Initial Case ID 순차 부여 | E2E/Regression | TC-CID-023-001 | ✅ 작성 완료 |
| SC-CID-024 | Manual C.1.1/C.1.8.1 동일 생성 | Data/Regression | TC-CID-024-001 | ✅ 작성 완료 |
| SC-CID-025 | Import 옵션 A 처리 | Functional/Data | TC-CID-025-001 | ✅ 작성 완료 |
| SC-CID-026 | Import 옵션 B 처리 | Functional/Data | TC-CID-026-001 | ✅ 작성 완료 |
| SC-CID-027 | C.1.8.1 Null 시 C.1.1 복사 | Data/Negative | TC-CID-027-001 | ✅ 작성 완료 |
| SC-CID-028 | Import C.1.8.1 기존값 유지 | Data/Regression | TC-CID-028-001 | ✅ 작성 완료 |
| SC-CID-029 | Case Level/Report Level 표시 형식 | Functional | TC-CID-029-001 | ✅ 작성 완료 |
| SC-CID-030 | C.1.8.1 내부 식별 기준 | Data/Integration | TC-CID-030-001 | ✅ 작성 완료 |
| SC-CID-031 | 남은 번호 100개 이하 팝업 | Boundary/Functional | TC-CID-031-001~TC-CID-031-002 | ✅ 작성 완료 |
| SC-CID-032 | 확인 후 다음 로그인 재노출 | Functional | TC-CID-032-001 | ✅ 작성 완료 |
| SC-CID-033 | 오늘 하루 보지 않기 당일 미노출 | Functional | TC-CID-033-001 | ✅ 작성 완료 |
| SC-CID-034 | 최대 자릿수 초과 자동 확장 | Boundary/Regression | TC-CID-034-001 | ✅ 작성 완료 |
| SC-CID-035 | 확장 후 기존 팝업 중단 | Functional/Regression | TC-CID-035-001 | ✅ 작성 완료 |
| SC-CID-036 | C.1.1 수동 수정 경고 분기 | Functional/Business | TC-CID-036-001~TC-CID-036-002 | ✅ 작성 완료 |
| SC-CID-037 | Approval 이후 식별자 수정 불가 | Business/Regression | TC-CID-037-001 | ✅ 작성 완료 |
| SC-CID-038 | Manual C.1.8.1 변경 불가 | Business/Security | TC-CID-038-001 | ✅ 작성 완료 |
| SC-CID-039 | Case ID 설정 변경 Audit Log 기록 | Non-Functional/Integration | TC-CID-039-001 | ✅ 작성 완료 |
| SC-CID-040 | [Figma Only] Preview 리셋 주기 및 연간 최대 처리 건수 표시 | Functional | TC-CID-040-001 | ✅ 작성 완료 |
| SC-CID-041 | [Figma Only] Add Segment 중복 추가 방지 | Functional | TC-CID-041-001 | ✅ 작성 완료 |
| SC-CID-042 | [Figma Only] 설정 변경 안내 배너 | Functional | TC-CID-042-001 | ✅ 작성 완료 |
| SC-CID-043 | [Figma] 만료 임박 모달 오늘 하루 보지 않기 UI | Functional | TC-CID-033-001 | ✅ 작성 완료 |

### TC 커버리지 요약

| 구분 | 수 |
|---|---:|
| 작성 TC | 53 |
| 매핑 완료 시나리오 | 43/43 |
| Figma 신규 TC 미작성 | 0 |
| Figma 확인 필요 보류 | 0 |
| Smoke TC | 7 |
| E2E TC | 6 |
| 미해소 확인 필요 사항 | 0 |

| type | 수 |
|---|---:|
| Functional | 34 |
| Boundary | 12 |
| Security | 5 |
| Negative | 1 |
| Performance | 1 |

---

## 확인 필요 사항

| No | 관련 시나리오 | 질문 내용 | 상태 |
|---|---|---|---|
| CN-CID-01 | SC-CID-009, SC-CID-010 | Year 선택지는 2-digit/4-digit/N/A 3종이다. 기존 5가지/연월 문구는 Year+Month 조합 삭제 전 잔존 문구로 보고 v1.0 TC에서는 3종 기준으로 검증한다. | 확인 완료 |
| CN-CID-02 | SC-CID-017 | 일련번호 자릿수의 실제 UI 허용 범위는 3~9이다. | 확인 완료 |
| CN-CID-03 | SC-CID-012, SC-CID-015 | PRD 칩도 별도 선택/삭제 가능하며, 일련번호 칩만 삭제 불가한 고정 칩으로 검증한다. | 확인 완료 |
| CN-CID-04 | SC-CID-025~028 | v1.0 대상에서 Convert는 제외한다. Import 식별자 처리 TC에 Convert 케이스를 포함하지 않는다. | 확인 완료 |
| CN-CID-05 | SC-CID-032, SC-CID-033, SC-CID-043 | 만료 임박 모달의 재노출 제어는 `오늘 하루 보지 않기`로 적용한다. 체크 후 확인 시 해당 사용자에게 당일 팝업을 다시 노출하지 않고, 다음 날짜에는 만료 임박 조건이 유지되면 다시 노출될 수 있다. | 확인 완료 |
| CN-CID-06 | SC-CID-010, SC-CID-040 | Preview Period Info의 리셋 주기 문구는 `매년 1월 1일`로 적용한다. | 확인 완료 |

---

## 리뷰 이력

| 일자 | 참석자 | 주요 결정 사항 |
|---|---|---|
| 2026-04-27 | Codex | Case ID 기획서, 상위 Account 정책, Safety Config read-only 정책을 반영하여 시나리오 초안 생성 |
| 2026-04-27 | 사용자 확인 | Year 선택지 3종, 일련번호 자릿수 3~9, PRD 칩 선택/삭제 가능 및 일련번호 칩 삭제 불가, v1.0 Convert 제외를 확정 |
| 2026-04-27 | Codex | Case ID TC 50건 작성, 39개 시나리오 전체 매핑 및 커버리지 요약 갱신 |
| 2026-04-27 | Codex | Figma `ICSR Config>Case ID` 노드 확인 후 Preview 보조 정보, Add Segment disabled 상태, 설정 안내 배너, 만료 임박 모달 문구를 시나리오에 반영 |
| 2026-04-27 | 사용자 확인 | CN-CID-05는 `오늘 하루 보지 않기`, CN-CID-06은 `매년 1월 1일` 기준으로 적용 확정 |
| 2026-04-27 | Codex | Figma 신규 시나리오 SC-CID-040~042에 대한 TC 3건 추가 및 매핑 완료 |

---

## 참고 사항

### 식별자 표시 요약

| 구분 | 표시 위치 | 표시 형식 | 예시 |
|---|---|---|---|
| Case Level | Tracker List, Case의 Case ID | 일련번호 | `202604ST001` |
| Report Level | ICSR 보고서 C.1.1/C.1.8.1 | 국가-조직-일련번호 | `KR-SELTA-202604ST001` |

### 국가코드 결정 우선순위

| 순위 | 기준 |
|---:|---|
| 1 | Reporter's Country Code Primary |
| 2 | Reporter's Country Code First |
| 3 | Identification of the Country Where the Reaction / Event Occurred Primary |
| 4 | Identification of the Country Where the Reaction / Event Occurred First |
| 5 | 기본값 KR |

### Type of Report 코드 매핑

| Type of Report | Case ID 코드 |
|---|---|
| Spontaneous | SP |
| Report from Study | RS |
| Other | OT |
| Not Available to Sender(Unknown) | UN |

### Import 식별자 처리 옵션

| 옵션 | C.1.1 | C.1.8.1 | 비고 |
|---|---|---|---|
| A. C.1.8.1만 유지 | 시스템 규칙에 따라 신규 부여 | 파일 내 값 유지 | Default |
| B. C.1.1, C.1.8.1 유지 | 파일 내 값 유지 | 파일 내 값 유지 | Migration 목적 |

### PV 도메인 리스크

- C.1.1/C.1.8.1은 ICSR 제출 및 중복/후속 보고 연결에 직접 영향을 주므로, 번호 재사용·수동 수정·Import 유지 옵션의 결함은 규제 보고 식별자 오염으로 이어질 수 있다.
- C.1.8.1은 화면 직접 노출 여부와 무관하게 내부 식별 기준으로 유지되어야 하며, Import 시 기존 값을 보호해야 후속 보고 연결이 깨지지 않는다.
- Case ID 생성 규칙 변경은 기존 케이스 식별자를 소급 변경하지 않고 이후 생성 건에만 적용되는지 회귀 검증이 필요하다.
