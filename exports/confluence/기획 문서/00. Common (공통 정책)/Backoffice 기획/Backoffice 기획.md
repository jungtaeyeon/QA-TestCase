# 변경사항

|  |  |  |  |
| --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 |
| 김병환 | 26-04-29 | Org User 개념 도입   * 오딧 로그 사용자 초대 수정 * bof-u-01, bof-u-02, bof-u-03 수정 * 3.2 강등 케이스 수정 * 용어 정리    + 온보딩 5, 7 단계 수정   + 온보딩 ⑦ 수정   + App 접근 권한 결정 3단계 부분 수정   + 3.1, 3.2 수중 |  |
| 김병환 | 26-04-22 | External User, Viewer 관련 사항 고도화에 하게 되어 관련 내용 수정   * 규칙 부분은 수정하지 않고, 실제 구현 및 관련 설명에서 수정 * BOF-U-02, BOF-LMT-01, BOF-LMT-04, BOF-LMT-05 에서 External User, Viewer 제거 하고 해당 내용 고도화 섹션에 추가 * 11.2에 고도화 관련 섹션 추가하고 미결 사항과 합쳐서 정리 |  |
| 김병환 | 26-04-20 | MFA 설정 변경 시 세션 강제 종료 → 다음 로그인 부터 변경으로 수정 - BOF-BAC-08 |  |
| 김병환 | 26-04-17 | 잠금 해제 구조 변경 - 3.4 수정: 계정 잠금 해제는 비밀번호 재설정으로 한다고 수정 - 8.2: 계정 잠금 해제 부분 삭제 |  |
| 김병환 | 26-04-13 | Tenant → Org로 교체  Org 생성시 제약사, CRO 선택하는 것 삭제 |  |
| 김병환 | 26.04.08 | Tenant Admin -> Org Admin으로 수정   * 고객 UI에서는 Tenant 대신 Org, Organization 으로 수정 |  |
| 김병환 | 26.03.31 | 태넌트 생성시 제약사, CRO 선택하는 과정 추가 |  |
| 김병환 | 26.03.31 | 계약 RENEW 정책 구체화  1.1.2, 1.1.11, 1.1.15, BOF-C-12 수정    계약 Correct 화면 흐름 구체화  1.1.11, BOF-C-06    1.1.8.2 계약 Correct 시에는 메일 보내지 않는 다는 것 구체화 |  |
| 김병환 | 26.03.30 | Master Admin/Tenant Admin 권한 구조 수정 원복: Master Admin/Tenant Admin도 명시적으로 권한을 받아야 워크스페이스/앱에 접근 가능    계정 한도 계산 방식 변경  0.6, 3.2, 10.3 BOF-U-02, 10.7 BOF-LMT-03 |  |
| 김병환 | 26.03.29 | Master Admin/Tenant Admin 권한 구조 수정  0.6, 3.2, 10.3 BOF-U-02, 10.7 BOF-LMT-03    백오피스 오딧 로그 수정 |  |
| 김병환 | 26.03.28 | 개발팀 기획 사항 바탕으로 전체적으로 문서 수정 |  |

# 0. 개요

## 0.1 목적

본 문서는 iVigilance Square 플랫폼의 Backoffice 서비스 운영 정책, 화면 흐름, 개발 요구사항을 정의한다.

Backoffice는 셀타스퀘어 내부 운영자(Backoffice Admin / Operator)가 사용하는 운영 도구로, 고객사 계약 관리·Org 관리·전체 사용자 관리·앱 설정을 담당한다.

## 0.2 GNB(전체 메뉴) 구조

Backoffice의 전체 메뉴 구조는 다음과 같다.

| GNB 메뉴 | 주요 기능 |
| --- | --- |
| 계약 관리 | 계약 목록 조회·생성·정정·연장·종료 |
| Org 관리 | Org 목록·상세 조회, Workspace 관리, App 활성화 설정, 사용자 초대 |
| 사용자 관리 | 전체 사용자 목록·생성·수정·비활성화·잠금 해제 |
| 앱 설정 | 앱별 링크 관리, 버전 관리 |
| Log | 고객사 로그 조회 (Audit Trail·Activity Log·Audit Log), Backoffice Activity Log 조회 |
| 공지사항 작성 | 공지사항 작성, 작성된 공지사항 확인, 작성된 공지사항의 노출/미노출 설정, 작성된 공지사항의 관리(삭제) |
| Admin | Backoffice 내부 계정(Admin/Operator) 관리 + Backoffice Audit Log 조회. Backoffice Admin 전용 |

## 0.3 온보딩 플로우 (계약 → 서비스 시작)

계약 체결 후 고객이 서비스를 사용하기까지의 전체 흐름은 다음과 같다.

| 단계 | 수행 주체 | 내용 | Org 상태 |
| --- | --- | --- | --- |
| 1 | Backoffice Admin | Org 생성: 고객사명 입력 → Org 이름·Main Workspace 이름 자동완성 후 확정 → 저장 → Org 및 Main Workspace 생성 | — (상태 미부여. 최초 Contract 생성 시 Pre-Active 부여) |
| 2 | Backoffice Admin | 계약 생성: 기존 Org 선택 → 계약 정보 입력 → 저장 → Contract 생성 (시작일이 미래이면 SCHEDULED) | 시작일이 미래이면 Pre-Active / 현재·과거이면 Active |
| 3 | Backoffice Admin | Workspace별 Application 활성화 설정 | 2단계 결과에 따름 (Pre-Active 또는 Active) |
| 4 | Backoffice Admin | Master Admin 계정 직접 생성 후 초대 메일 발송 | 2단계 결과에 따름 (Pre-Active 또는 Active) |
| — | 시스템 | Contract 시작일 도래 → SCHEDULED에서 ACTIVE로 전환 → Org Pre-Active에서 Active로 자동 전환 | → Active |
| 5 | Master Admin | 로그인 후 Org Admin, Org User 등 사용자 초대 및 Org 역할/App 역할 설정 | Active |
| 6 | Backoffice Admin | 필요 시) 추가 Workspace: 고객사가 세일즈에 요청 → 관련 계약 완료 → Backoffice Admin이 NEW Contract 생성(1.1.16) → Workspace 자동 생성 | Active |
| 7 | Master Admin / Org Admin / Org User(App Admin 권한 보유 시) | Org 및 활성화된 Application 내 세부 설정 수행 | Active |

|  |
| --- |
| 📋 온보딩 흐름 |
| ① [Org 관리] → [+ 새 Org] 클릭 → 고객사명 입력 → Org 이름·Main Workspace 이름 자동완성 후 확정 → [저장] → Org 및 Main Workspace 생성 |
| ② [계약 관리] → [+ 새 계약] 클릭 → 계약 생성화면 |
| ③ 기존 Org 목록에서 Org 선택 |
| ④ 계약 기간, 앱 목록, 앱별 사용량, 계약 금액, 세일즈 담당자 이름/이메일, 원본 계약서 링크 입력 → [저장] → Contract 생성 → 계약 상세 화면으로 이동 |
| — ※ 계약 시작일이 미래인 경우 Org는 Pre-Active 상태이다. 이 기간에 1~4단계 설정 작업은 Backoffice에서 수행 가능하지만, 고객 로그인은 불가하다. 계약 시작일 도래 시 Contract가 ACTIVE로 전환되고 Org도 Active가 되어, 5단계부터 진행 가능하다. |
| ⑤ [Org 관리] → 해당 Org 클릭 → [Workspace 탭] → Main Workspace 행 클릭 → [App 활성화 설정] → 앱 ON/OFF 토글 후 [저장] |
| ⑥ [Org 관리] → Org 상세 → [사용자 탭] → [Master Admin 초대] → 이메일·이름 입력 → [초대 발송] |
| → 초대 메일 발송, 계정 상태: Invitation |
| ⑦ 이후 단계는 Master Admin이 iVigilance Square에서 Org Admin, Org User 등을 초대하고 역할 및 권한을 설정하여 진행 |
| ⑧ (필요 시) 추가 Workspace: 별도 종이 계약 완료 → [계약 관리] → [+ 새 계약] → 추가 Workspace 포함 NEW Contract 생성(1.1.16 참고) → Org 관리에서 App 활성화 설정 |

## 0.4 Org / Workspace 이름 규칙

| 규칙 | 내용 |
| --- | --- |
| 최대 글자 수 | 20자 이내 (공백 포함) |
| 자동 생성 | Org 생성 시: 고객사명 입력값이 Org 이름·Main Workspace 이름 필드에 동일값으로 자동완성됨. 각각 독립적으로 수정 가능.    계약 생성 시: 기존 Org를 선택하며, Org 이름은 자동 표시됨. |
| 사후 수정 | Backoffice에서 생성 후 수정 가능 |
| 이름 수집 시점 | 계약 생성 전 고객사로부터 미리 수집. 세일즈 단계에서 확보 후 계약 입력 시 기입, 확보 되어 있지 않으면 디폴트 값 자동 입력 |

## 0.5 운영 기준

* Org는 서비스 이용 단위이다.
* Org 이름은 Backoffice Admin이 지정하며, Org 생성 시 고객사명을 초기값으로 자동완성한다. 이후 화면 표시 목적에 따라 수정 가능하다.
* Org 이름은 시스템 전체에서 유니크해야 한다. 중복 시 저장 불가 + 오류 메시지 표시. *(현재 1 고객사 = 1 Org 구조 기준. 멀티 Org 도입 시 추후 별도 정책 재정의 필요)*
* Contract는 Org에 연결되어 생성된다.
* 동일 Org 내 동일 앱에 대해 유효기간이 겹치는 계약은 저장이 차단된다. 종료된 과거 계약 이력(EXPIRED/SUPERSEDED/CANCELLED)은 차단 기준에 포함하지 않는다.
* Org 데이터는 고객이 서비스 내에서 생성·조회하는 실제 운영 데이터(예: Safety DB 데이터 등)를 의미하며, 계약 정보, Org 기본 정보, Backoffice 관리 정보는 이에 포함되지 않는다.

## 0.6 App 접근 권한 결정 구조

사용자가 특정 App에 최종적으로 접근하려면 아래 3단계 조건이 모두 충족되어야 한다. 하나라도 충족되지 않으면 접근 불가.

**고객 로그인 전제조건**

고객(Master Admin / Org Admin / App Admin / App User 등)이 iVigilance Square에 로그인하려면 Org 상태가 Active여야 한다. Pre-Active / Terminated 상태에서는 로그인 차단 + 안내 메시지 표시.

※ Backoffice Admin 및 Operator는 위 조건과 무관하게 Backoffice에 로그인 가능하다. Org가 Pre-Active 상태인 기간에도 App 활성화, Master Admin 초대 등 설정 작업을 수행할 수 있다.

| 단계 | 조건 | 관리 주체 | 관련 섹션 |
| --- | --- | --- | --- |
| 1단계 | 해당 App을 포함한 Contract 버전이 현재 시점에 유효(ACTIVE) | Backoffice Admin (계약 생성 시 설정) | 1.1.2 계약 정보 구성, BOF-C-01 |
| 2단계 | Workspace에서 App 활성화 | Backoffice Admin | 2.6 Workspace별 App 활성화 설정, BOF-T-02 |
| 3단계 | 사용자에게 App 접근 권한 부여 | Backoffice Admin / Master Admin / Org Admin (Org User는 부여 불가) | 3.2 사용자 정보 수정, BOF-U-02 |

※ 3단계 중 하나라도 미충족 시 해당 App 접근 불가. 2단계(Workspace 활성화) 여부와 무관하게 3단계 권한이 부여되어 있더라도 2단계가 비활성이면 접근 불가.

# 1. 계약 관리

## 1.1 정책

### 1.1.1 목적

* 종이 계약서를 기반으로 고객사의 Contract 조건을 시스템에 등록하고, 그 조건에 따라 Org의 생성·확장·종료를 관리한다.
* 모든 계약 변경(연장, 정정, 신규)은 기존 Contract를 수정하지 않고 항상 새 Contract 버전을 생성한다(append-only versioning). 하나의 Org에 여러 Contract 버전이 누적된다.
* 각 Contract 버전은 적용 기간, 허용 범위(App 구성), 사용 조건의 스냅샷을 정의하며, 생성 후 계약 조건(content)은 불변이다. 상태(status) 전이만 허용된다.
* 계약 변경 시 사용자가 액션 유형(NEW / RENEW / CORRECT)을 선택하며, 이 분류는 업무 메타데이터로서 저장 방식을 바꾸지 않는다. 어떤 액션이든 결과는 항상 새 Contract 버전 생성이다.
* Org의 운영 상태(Pre-Active / Active / Terminated)는 Contract 버전 상태와 분리된다. Contract status는 Org status를 직접 소유하거나 전이시키지 않는다. Org 상태 판단은 Contract 조건의 영향을 받을 수 있지만, 운영 책임은 Org 정책이 가진다.

  + 시작일이 도래하지 않은 계약(SCHEDULED 상태)은 현행 계약 판단에 포함되지 않는다.
* 계약 등록과 계약 발효는 분리된다. 계약은 미래 시작일로 등록 가능하며(SCHEDULED), 이 기간 Org는 Pre-Active 상태이다. 시작일 도래 시 Contract가 ACTIVE로 전환되고, Org도 Active로 전환되어 고객 로그인이 가능해진다.
* Org가 Pre-Active인 기간에도 Backoffice Admin은 App 활성화, Master Admin 초대 등 사전 설정 작업을 수행할 수 있다.
* 현재 Org 상태 판단에 반영되는 유효 계약 조건은 현행 계약 조건으로 조회 가능하며, 이전 Contract 버전은 계약 이력으로 조회 가능하다.

  + 현행 계약은 현재 시점에 ACTIVE 상태인 Contract 버전(들)의 집합을 의미하며 단일 Contract 버전을 의미하지 않는다.
  + 과거 계약은 SUPERSEDED 또는 EXPIRED 상태인 Contract 버전이며, 읽기 전용 이력으로 조회한다.
  + 미래 계약은 SCHEDULED 상태인 Contract 버전이며, 현행 계약에는 포함되지 않는다.
  + 현재/과거/미래 구분은 별도 저장 방식이 아니라 상태 및 유효기간 해석의 결과이다.
  + 계약 조회 화면에서 표시되는 계약 정보는 단일 Contract가 아닌, 현재 시점 기준 ACTIVE 상태인 조건을 함께 표시한다.

### 1.1.2 계약 정보 구성

| 항목 | 필수 여부 | 비고 |
| --- | --- | --- |
| 고객사명 | 필수 | 계약서 기준 고객사명을 입력한다. 입력값 기준으로 기존 Org 매칭 목록을 표시한다. 계약 정보에 기록되며, Org 검색/식별에 사용된다. |
| Org | 필수 | 기존 Org 목록에서 선택한다. Org가 존재하지 않는 경우 먼저 Org 관리에서 Org를 생성해야 한다. 선택 시 해당 Org 이름이 고객사명 필드에 자동완성됨. Org 명 수정이 필요한 경우 Org 관리에서 별도 수정 |
| 계약 시작일 | 필수 | 날짜 선택. 유효성 규칙은 1.1.3 참고 |
| 계약 종료일 | 필수 | 날짜 선택. 유효성 규칙은 1.1.3 참고 |
| 계약 금액 | 필수 | 계약 단위 금액 정보(통화 포함) |
| Main Workspace 이름 | 필수 | Org 생성 시 자동 생성된 Main Workspace 이름이 읽기 전용으로 표시된다. 이름 수정이 필요한 경우 Org 관리 > Workspace 상세(2.4)에서 별도 수정한다. 최대 20자(공백 포함). |
| 계약 앱 목록 | 필수 | 전체 앱 목록을 체크박스로 표시. 포함할 앱을 선택한다. 현재는 Safety DB 1개. 최소 1개 이상 선택 필수 — 하나도 선택하지 않으면 저장 불가 + 인라인 오류 메시지 표시 ('앱은 최소 1개 이상이어야 합니다.') |
| 앱의 Workspace 배정 | 필수 | 계약 앱 목록에서 선택한 앱만 후보로 표시된다. 각 앱을 사용할 Workspace에 배정한다. 최초 계약 시 Main Workspace가 기본 선택. 추가 Workspace가 존재하는 경우 추가 Workspace까지 선택 가능. 동일 Workspace 내 같은 앱은 중복 배정 불가. 신규 계약(NEW)으로 앱이 추가되는 경우에도 사용할 Workspace를 지정한다 |
| 앱별 사용량 정보 | 필수 | 계약 앱 목록에서 선택한 앱별로 사용량 입력란 표시. 숫자만 입력 가능, 최소 1 이상. 예: Safety DB 이니셜 케이스 수 1,000건. 초과 시에도 서비스 사용 가능. 초과 여부는 계약 상세 화면(앱 사용량 탭)에서 시각적으로 표시 |
| 앱 구성 변경 시 처리 | — | 한 Contract 버전 내 모든 앱은 동일한 계약 기간(시작일/종료일)을 가진다. 앱별 독립적인 계약 기간 설정은 허용하지 않는다. 앱 구성(추가/제거)이 변경되는 경우 기존 계약의 연장이 아닌 신규 계약(action\_type = NEW)으로 처리한다. |
| 세일즈 담당자 이름 | 필수 | 한국어 또는 영문 입력. 최대 50자(공백 포함). 계약 종료 알림 수신 대상 |
| 세일즈 담당자 이메일 | 필수 | 이메일 형식 검증 적용. 계약 종료 D-90/30/7/1일 알림 수신 |
| 원본 계약서 | 필수 | 원본 계약서 외부 저장소 링크. URL 형식 검증 적용 |
| 추가 Workspace 여부 | 선택 | 추가 Workspace 포함 계약 시 수량 입력. 별도 사용 기간은 입력하지 않으며, 해당 Workspace는 이 Contract의 시작일/종료일을 그대로 따른다. |
| 메모 | 선택 | 최대 1,000자(공백 포함) |

### 1.1.3 계약 날짜 유효성 규칙

| 규칙 | 내용 |
| --- | --- |
| 시작일 ≤ 종료일 | 시작일은 종료일과 같거나 이전이어야 함. 시작일이 종료일보다 뒤일 수 없음 |
| 종료일 ≥ 시작일 | 종료일은 시작일과 같거나 이후여야 함. 종료일이 시작일보다 앞설 수 없음 |
| 유효성 검사 시점 | 계약 생성 및 수정 시 저장 전 실시간 검증. 위반 시 저장 불가 + 인라인 오류 메시지 표시 |
| 계약 연장 시 | 새 종료일은 기존 시작일 이후여야 함. 동일 조건 적용 |
| 앱과 태넌트의 시작일, 종료일 | 한 Contract 내 모든 앱은 동일한 계약 기간을 가진다. 앱별 독립 기간 설정 불가 |
| 동일 앱 유효기간 중복 금지 | 같은 Org 내 같은 앱이 서로 다른 계약 계보에서 동시에 유효해지는 계약은 저장 불가. 같은 버전 체인 내부의 후속 버전 전이는 허용. 미래 예약 계약(SCHEDULED) 자체의 존재는 허용하되, 활성화 시 cross-chain 동시 유효가 발생하도록 등록되는 경우 저장 시점에 차단 |

### 1.1.4 Org상태

Org 상태는 단일 Contract가 아닌, 해당 Org에 적용된 여러 App 계약 조건의 유효 상태를 종합하여 계산된다.

*※ 아래 Org 상태는 운영 상태이며, Contract 버전 상태(SCHEDULED/ACTIVE/SUPERSEDED/EXPIRED/CANCELLED)와 별개의 축이다. Contract 상태 모델은 1.1.6 참고.*

| 상태 | 설명 | 전환 방법 | 비고 |
| --- | --- | --- | --- |
| Pre-Active | 계약이 등록되었지만 ACTIVE Contract가 아직 없는 상태 | 미래 시작일 계약 등록 시(Contract SCHEDULED) / 모든 ACTIVE Contract가 EXPIRED되었지만 SCHEDULED Contract가 남아 있는 경우 | 고객 로그인 불가. Backoffice에서 App 활성화, Master Admin 초대 등 사전 설정 작업 가능 |
| Active | ACTIVE 상태 Contract가 1개 이상 존재하여 서비스 접근이 가능한 상태 | Contract SCHEDULED → ACTIVE 전환 시 시스템 자동 | 정상 사용 가능, 고객 로그인 가능, 백오피스 조회 가능 |
| Terminated | 계약 만료(Contract EXPIRED)에 따른 시스템 자동 전환 또는 Backoffice Admin 수동 전환 | 시스템 자동 / Backoffice Admin 수동 | 고객 로그인 불가, 60일 후 데이터 삭제 |

\* Terminated(보존 기간 만료 전/후) 상태에서는 Org 내부 운영 데이터(앱 데이터 등)는 Backoffice Admin도 조회할 수 없다.

\* 단, 계약 정보, Org 기본 정보, 상태 변경 및 복원을 위한 관리 정보는 Backoffice에서 조회 가능하다.

\* Pre-Active 상태에서는 고객(Master Admin 포함)이 로그인할 수 없다. Backoffice Admin만 Backoffice에서 해당 Org의 설정 작업(App 활성화, Master Admin 초대 등)을 수행할 수 있다.

### 1.1.5 Org상태 전환 규칙

| 현재 상태 | 전환 가능 상태 | 트리거 | 처리 방식 |
| --- | --- | --- | --- |
| — (상태 미부여) | Pre-Active | 최초 Contract 생성 시 | 시스템 자동 |
| Pre-Active | Active | Contract SCHEDULED → ACTIVE 전환 시 | 시스템 자동 (배치/스케줄러) |
| Active | Terminated | ①모든 ACTIVE Contract가 EXPIRED 시 ②Backoffice Admin 수동 | ①시스템 자동 ②수동 |
| Active | Pre-Active | 모든 ACTIVE Contract가 EXPIRED되었지만 SCHEDULED Contract가 존재하는 경우 | 시스템 자동 |
| Terminated | Active | Backoffice Admin 수동 복원 (60일 내 한정) | 수동 |

*※ Terminated → Active 복원은 단일 Backoffice Admin이 처리 가능. 다중 승인 불필요. 복원 행위는 감사 로그에 별도 카테고리로 기록.*

### 1.1.6 계약 버전 상태 (Contract Version Status)

계약 히스토리를 안정적으로 관리하기 위해, 모든 Contract 버전은 아래 상태 중 하나를 가진다.

이 상태 모델은 Contract 상태 모델이며, Org 운영 상태(Active/Terminated)와 분리된다.

예외: Org에 연결된 모든 ACTIVE Contract가 EXPIRED되면, SCHEDULED Contract 존재 여부에 따라 Org는 Pre-Active 또는 Terminated로 자동 전환된다(하단 "Contract 상태와 Org 상태의 관계" 참고). Org가 Pre-Active 상태일 때 연결된 계약이 ACTIVE가 되면, Org 상태는 자동으로 Active로 전환된다. Terminated 상태에서는 Contract가 ACTIVE로 전이되더라도 Org 상태가 자동 전환되지 않는다(수동 복원 필요 — 1.1.5 참고).

| 상태 | 설명 | 현행 계약 포함 여부 |
| --- | --- | --- |
| SCHEDULED | 미래 시작일을 가진 예약 계약. 저장 완료되었지만 효력 미시작 | 미포함 |
| ACTIVE | 현재 시점 기준 효력이 있는 계약 버전 | 포함 |
| SUPERSEDED | 더 최신 버전에 의해 대체된 상태. 읽기 전용 이력 | 미포함 |
| EXPIRED | 유효기간이 종료된 상태. 읽기 전용 이력 | 미포함 |
| CANCELLED | 발효 전에 취소된 계약 버전. 효력 없음. 이력 보존용 | 미포함 |

**상태 해석 원칙**

* 상태는 Contract 버전의 라이프사이클 관리를 위한 값이다. 계약 조건 자체를 수정하는 값이 아니다.
* 현재/과거/미래 구분은 상태와 유효기간을 함께 해석한 결과이다.
* 계약 버전은 어떤 상태가 되더라도 물리적으로 덮어쓰거나 삭제하지 않는다.
* ACTIVE 계약의 중도 해지/취소는 현재 Contract 상태 모델 범위에 포함하지 않으며, 해당 시나리오는 Org 정책 및 감사 로그 영역에서 다룬다.

**상태 전이 규칙**

| 현재 상태 | 다음 상태 | 트리거 | 처리 방식 |
| --- | --- | --- | --- |
| 생성 시점 | SCHEDULED | 미래 시작일 계약 저장 | 동기 |
| 생성 시점 | ACTIVE | 즉시 발효 계약 저장 | 동기 |
| SCHEDULED | ACTIVE | 시작일 도래 | 배치/스케줄러 |
| SCHEDULED | SUPERSEDED | 발효 전 수정으로 새 버전 생성 | 동기 |
| SCHEDULED | CANCELLED | 발효 전 취소 | 동기 |
| ACTIVE | SUPERSEDED | 같은 체인의 후속 버전이 ACTIVE로 전이 | 동기 또는 배치 |
| ACTIVE | EXPIRED | 종료일 도래 | 배치/스케줄러 |

*※ SCHEDULED→ACTIVE 전이 시, 해당 계약이 기존 ACTIVE와 같은 버전 체인에 속하고 대체 관계이면 선행 ACTIVE를 함께 SUPERSEDED 처리한다. 단, 만료 후 연속 RENEW인 경우 선행 계약은 SUPERSEDED가 아닌 EXPIRED로 처리한다.*

**배치/스케줄러 원칙**

* SCHEDULED→ACTIVE, ACTIVE→EXPIRED 전이는 반드시 배치 또는 스케줄러가 처리한다.
* 사용자 액션 기반 전이(생성, 수정, 교체, 취소)는 동기 처리한다.

**Contract 상태와 Org 상태의 관계**

* Contract status는 Org status를 직접 전이시키지 않는다.
* Org 상태 판단은 Contract 조건의 영향을 받을 수 있지만, Org 상태의 운영 책임은 Org 정책이 가진다.
* Org에 연결된 모든 ACTIVE Contract가 EXPIRED로 전이되면:

  + SCHEDULED Contract가 존재하는 경우 → Org Pre-Active로 전환
  + SCHEDULED Contract도 없는 경우 → Org Terminated로 전환
  + 이는 Contract가 Org를 직접 전이시키는 것이 아니라, "유효한 Contract가 없는 Org"에 대한 시스템 정책이다.

### 1.1.7 Contract 내 App/Workspace 계약기간 관리

**기간 원칙**

* 한 Contract 버전 내 모든 앱은 동일한 계약 기간(시작일/종료일)을 가진다.
* 앱별 독립적인 계약 기간 설정은 허용하지 않는다.
* Workspace도 동일한 원칙을 따른다. Workspace별 독립 시작일/종료일은 허용하지 않는다.
* 한 Contract 내 모든 App과 Workspace는 동일한 계약 기간을 가진다.
* App 또는 Workspace 구성 변경(추가/제거)이 필요한 경우 신규 계약(action\_type = NEW)으로 처리한다.

접근 가능 여부와 동작

* 앱은 소속 Contract 버전이 ACTIVE 상태이고, Org 상태가 Active일 때만 접근 가능하다.
* Contract가 EXPIRED 상태로 전이되면 해당 Contract에 포함된 모든 앱은 접근 불가가 된다. 데이터는 60일간 보존 후 삭제된다.
* 추가 Workspace를 포함한 Contract가 EXPIRED되면 해당 Workspace는 자동 폐쇄 대상이 된다(2.7 참고).
* Org가 Terminated 상태가 되면 Contract 상태와 무관하게 모든 앱 접근이 불가하다.
* 앱은 Workspace 내 활성화 설정(0.6 2단계)과 사용자 권한 부여(0.6 3단계)가 모두 충족되어야 접근 가능하다

**권한/라이선스 계산**

* 권한과 라이선스 판단은 앱 단위로 수행한다.
* 계약은 상업적/업무적 단위로 관리하고, 접근 가능 여부 계산은 앱 단위로 분리한다.

### 1.1.8 계약 알림 정책

계약 관련 주요 이벤트 발생 시 아래 정책에 따라 이메일 알림을 발송한다

공통 정책

* 수신 대상: 역할 그룹 기준 전체 발송. 구성원 변경 시 자동 반영.
* 알림 발송 실패 처리: 실패 정의 = SMTP 오류, 주소 오류, 서버 거부 등 미전달 전체. 재시도: 1시간 간격, 최대 3회. 최종 실패 시 Backoffice Admin 인앱 알림 + 감사 로그 기록.
* 세일즈 담당자 이메일은 계약 정보에 입력되어 있는 이메일 사용

#### 1.1.8.1 종료 사전 알림

계약 종료일 기준으로 아래 시점에 Master Admin과 세일즈 담당자, 백오피스 어드민/오퍼레이터에게 알림 이메일을 자동 발송한다.

사전 알림 범위는 계약 종료일 정보가 있는 것들 전체를 대상으로 한다.

| 발송 시점 | 수신 대상 | 비고 |
| --- | --- | --- |
| 종료 D-90일 | Master Admin, 세일즈 담당자, Backoffice Admin, Backoffice Operator | 갱신 검토 시작 안내 |
| 종료 D-30일 | Master Admin, 세일즈 담당자, Backoffice Admin, Backoffice Operator | 갱신 요청 안내 |
| 종료 D-7일 | Master Admin, 세일즈 담당자, Backoffice Admin, Backoffice Operator | 긴급 갱신 안내 |
| 종료 D-1일 | Master Admin, 세일즈 담당자, Backoffice Admin, Backoffice Operator | 최종 경고. 내일 서비스 종료 예정 안내 |

**종료 사전 알림 템플릿**

제목: [iVigilance Square] {고객사명} 계약 종료 D-{N}일 안내

안녕하세요, {고객사명} 관리자님.

iVigilance Square 서비스 계약 종료가 {N}일 남았습니다.

■ 종료 예정 계약

* 종료일: {YYYY-MM-DD}
* 대상:

  + {Org전체 계약} (해당 시)
  + 앱: {앱명1}, {앱명2} (해당 시)
  + Workspace: {Workspace명1}, {Workspace명2} (해당 시)
* Org종료 예정 메일 일때: 계약 종료 후 해당 계약 범위(Org 전체 또는 개별 App)의 데이터는 60일간 보존합니다.
* 워크스페이스와 앱 종료 예정 메일 일때: 해당 Contract에 포함된 Workspace(APP)는 계약 종료에 따라 함께 종료 대상이 되며, 데이터 처리는 Workspace(APP) 폐쇄 절차에 따릅니다. (담당 세일즈에게 문의하세요.)
* 삭제 예정일: {YYYY-MM-DD}

  + 보존 기간 이후 데이터는 복구 불가능하게 완전 삭제 됩니다.

계약 갱신이 필요하신 경우 담당 세일즈에게 연락해 주시기 바랍니다.

감사합니다.

셀타스퀘어 드림

**템플릿 관련 참고**

* Org종료일때와 워크스페이스/앱 종료일 때 안내 문구에 차이 있음
* 삭제 예정일은 Org종료와 앱 종료일때만 추가하여 발송

#### 1.1.8.2 계약 체결 안내

계약이 새로 맺어지거나 변경되는 경우, 계약이 생성되거나 변경되어 신규 Contract가 생성된 시점에 Master Admin과 세일즈 담당자, 백오피스 어드민/오퍼레이터에게 알림 이메일을 자동 발송한다.

| 발송 시점 | 수신 대상 | 비고 |
| --- | --- | --- |
| 신규 계약 생성 | Master Admin(지정된 경우), 세일즈 담당자, Backoffice Admin, Backoffice Operator | 신규 계약 생성 안내. 최초 계약 시 Master Admin 미지정 상태이면 MA 제외하고 발송 |
| 계약 연장 | Master Admin(지정된 경우), 세일즈 담당자, Backoffice Admin, Backoffice Operator | 갱신된 계약 내용 안내    계약이 종료된 상태에서 60일 내 계약 연장시에도 계약 연장으로 적용하여 같은 메일 전송 |

**체결 안내 템플릿**

제목: [iVigilance Square] {고객사명} 계약 {신규 생성 / 연장 / 변경} 안내

안녕하세요, {고객사명} 관리자님.

iVigilance Square 서비스 계약이 {신규 생성 / 연장 / 변경}되었습니다.

■ 계약 정보

- 고객사: {고객사명}

- 계약 기간: {신규 계약 {시작일} ~ {종료일}}

- 계약 앱: {앱 목록}

- 변경 내용:

{변경된 정보명1: 변경된 정보1}

서비스 이용 중 문의사항이 있으시면 담당 세일즈에게 연락해 주시기 바랍니다.

감사합니다.

셀타스퀘어 드림

※ 계약 정정(CORRECT)은 시스템 입력값 정정 목적이므로 체결 안내 메일 발송 대상이 아니다.

#### 1.1.8.3 복원 후 사후 통지

| 발송 시점 | 수신 대상 | 비고 |
| --- | --- | --- |
| Terminated → Active 단순 복원 | Master Admin, 세일즈 담당자, Backoffice Admin, Backoffice Operator | 서비스 재개 안내(실수 복원) |

제목: [iVigilance Square] {고객사명} 서비스 재개 안내

안녕하세요, {고객사명} 관리자님.

iVigilance Square 서비스가 재개되었습니다.

■ 재개 정보

- 고객사: {고객사명}

- 재개 일시: {YYYY-MM-DD HH:MM} (KST)

서비스 이용 중 문의사항이 있으시면 담당 세일즈에게 연락해 주시기 바랍니다.

감사합니다.

셀타스퀘어 드림

### 1.1.9 계약 생성

#### 정책

* 종이 계약서 내용을 시스템에 입력하여 계약을 생성한다.
* 계약 생성은 기존 Org를 선택하여 진행한다. Org가 존재하지 않는 경우 먼저 Org 관리에서 Org를 생성해야 한다.

  + 선택된 Org에 현재 적용 중인 계약이 존재하는 경우 경고를 표시하고 기존 계약을 확인하도록 안내한다.
  + 동일 Org 내 동일 앱에 대해 유효기간이 겹치는 경우 저장을 차단한다. (단, 같은 버전 체인 내부의 후속 버전 전이는 예외. 1.1.3 참고)
* 계약 생성 완료 시 계약 체결 안내 이메일을 발송한다. (1.1.8.2 참고)
* 고객사명은 계약서 기준 입력값으로 저장되며, 이후 Org 이름이 변경되더라도 기존 계약과의 연결 판단에는 영향을 주지 않는다.
* 계약 생성 시 action\_type = NEW이며, previous\_contract\_id = NULL이다 (새 계약 계보의 시작점).
* 시작일이 현재 또는 과거이면 Contract 상태 = ACTIVE, 시작일이 미래이면 Contract 상태 = SCHEDULED로 생성된다.
* 시작일이 미래인 경우 Contract는 SCHEDULED 상태로 생성되며, 해당 Org에 ACTIVE Contract가 없으면 Org 상태는 Pre-Active가 된다. 이 기간 동안:

  + 고객 로그인: 불가 (Org Pre-Active)
  + Backoffice 설정 작업: 가능 (App 활성화, Master Admin 초대 등)
  + 시작일 도래 시 배치/스케줄러가 Contract를 ACTIVE로 전환하고, Org도 Active로 전환하여 고객 로그인 가능

#### 화면 흐름

|  |
| --- |
| 📋 계약 생성 흐름 |
| ① GNB [계약 관리] 클릭 → 계약 목록 화면 |
| ② [+ 새 계약] 버튼 클릭 → 계약 생성 화면 |
| ③ 기존 Org 목록에서 Org 선택 → 선택된 Org에 현재 적용 중인 계약 존재 여부 확인 |
| ④ 계약 정보 입력 (1.1.2 계약 정보 구성 참고):  (자동 표시) 고객사명 — Org 선택 시 자동완성  (읽기 전용) Main Workspace 이름  (필수) 계약 시작일 / 종료일  (필수) 계약 앱 목록 — 전체 앱 목록에서 체크박스로 선택. 최소 1개 필수  (필수) 앱의 Workspace 배정 — 선택한 앱별로 사용할 Workspace 지정. Main Workspace 기본 선택  (필수) 앱별 사용량 — 선택한 앱별 숫자 입력 (최소 1)  (필수) 계약 금액 (통화 포함)  (필수) 세일즈 담당자 이름 / 이메일  (필수) 원본 계약서 링크(URL)  (선택) 추가 Workspace 여부 및 수량  (선택) 메모 |
| ⑤ 유효기간 중복 검증 → 동일 Org 내 동일 앱 기준으로 겹치는 경우 저장 차단 + 메시지("동일 앱의 계약 기간이 중복됩니다. 기존 계약을 확인해 주세요.") 표시 |
| ⑥ [저장] 버튼 클릭 → Contract 생성 → 계약 상세 화면으로 이동. Org 상태: 시작일이 현재/과거이면 Active / 미래이면서 해당 Org에 다른 ACTIVE Contract가 없는 경우 Pre-Active / 미래이면서 다른 ACTIVE Contract가 있으면 기존 상태 유지 |

### 1.1.10 계약 조회

#### 정책

* 계약 목록: 전체 계약 조회. 고객사명·Org 상태·계약 기간 기준 검색·필터링 가능
* 단건 조회 탭 구성: 계약 기본 정보 / 앱 사용량 / 계약 이력

  + 계약 기본 정보: 현재 시점 기준 ACTIVE 상태인 Contract 버전의 조건을 표시. SCHEDULED 상태의 미래 계약이 있는 경우 별도 표시. SUPERSEDED / EXPIRED / CANCELLED 버전은 계약 이력 탭에서 조회
  + 앱 사용량

    - 앱 사용량 탭: 계약 시 입력한 사용량(계약 값) 대비 현재 실제 사용량을 나란히 표시

      * 예: Safety DB 이니셜 케이스 — 계약: 1,000건 / 현재: 1,250건
      * 초과 시 해당 행에 시각적 강조 표시 (색상 또는 아이콘). 서비스 차단은 없음
  + 계약 이력: NEW(신규), RENEW(연장), CORRECT(정정)으로 분류하여 버전별 생성 일시, 생성자, 상태를 확인. 각 이력 클릭 시 해당 시점 계약 상세 조회 가능(읽기 전용). 계약 이력은 버전 이력이며, 상세 변경 내용(before/after)은 감사 로그에서 확인

**Contract 상태 UI 표시 규칙**

| 표시 위치 | 표시 방식 |
| --- | --- |
| 계약 목록 | 각 행에 Contract 상태 배지 표시. 상태 필터로 조회 가능 (ACTIVE / SCHEDULED / EXPIRED / SUPERSEDED / CANCELLED) |
| 계약 상세 — 계약 정보 탭 | 상단에 현재 Contract 상태 배지 표시. SCHEDULED 미래 계약이 있으면 별도 영역에 예약 계약 정보 표시 |
| 계약 상세 — 계약 이력 탭 | 각 버전 행에 상태 배지 표시. 분류(NEW/RENEW/CORRECT) 배지와 상태 배지 병렬 표시 |
| Org 상세 | Org 상태 배지 표시 (Pre-Active / Active / Terminated) |

*※ 배지 색상은 디자인 시스템에서 정의. 상태 간 시각적 구분이 명확해야 한다.*

#### 화면 흐름

|  |
| --- |
| 📋 계약 조회 흐름 |
| ① GNB [계약 관리] → 계약 목록 화면 |
| 검색창에 고객사명 입력, 또는 상태 필터 선택 |
| ② 목록에서 계약 행 클릭 → 계약 상세 화면 |
| [계약 정보 탭]: 기본 계약 내용 확인 |
| [앱 사용량 탭]: 앱별 계약 사용량 vs 현재 사용량 비교 표시 (초과 시 강조) |
| [계약 이력 탭]: NEW(신규), RENEW(연장), CORRECT(정정)으로 분류하여 버전별 생성 일시, 생성자, 상태 확인. 각 이력 클릭 시 해당 시점 계약 상세 조회 가능(읽기 전용). 상세 변경 내용은 감사 로그에서 확인 |

**계약 상세 화면 액션 버튼 노출 조건**

| 버튼 | 노출 조건 |
| --- | --- |
| [계약 연장] | Org Active 상태, 또는 Terminated 60일 내 |
| [계약 정정] | Contract가 ACTIVE 또는 SCHEDULED 상태 |
| [계약 취소] | Contract가 SCHEDULED 상태일 때만 |
| [계약 종료] | Org Active 상태일 때만 |
| [계약 복원] | Org Terminated 상태 + 60일 내 |

### 1.1.11 계약 변경

### 정책

* 계약 변경은 기존 계약 조건이 바뀌는 경우를 의미하며, 사용자가 변경 유형을 먼저 선택한 후 해당 유형에 맞는 화면에서 처리한다.
* 계약 변경 액션 유형은 3가지로 구분한다:

|  |  |  |  |
| --- | --- | --- | --- |
| 액션 유형 | 의미 | 저장 방식 | previous\_contract\_id |
| NEW | 신규 계약. 새 계약 계보의 시작점 | 새 Contract 버전 생성 | 반드시 NULL |
| RENEW | 기존 계약의 연장/후속 버전. 앱 구성은 유지하고 기간 및 조건(금액·사용량·세일즈 담당자·원본 계약서)을 갱신 | 새 Contract 버전 생성 | 필수 (기존 계약 참조) |
| CORRECT | 기존 계약의 정정. 종이 계약서와 시스템 입력값 불일치 시 정정 용도 | 새 Contract 버전 생성 | 필수 (기존 계약 참조) |

* 모든 액션 유형의 결과는 항상 새 Contract 버전 생성이다. 기존 계약 버전은 절대 덮어쓰지 않는다.
* 분류는 업무 메타데이터이며, 저장 방식을 바꾸지 않는다.

**앱 구성 변경과 액션 유형의 관계**

* 앱 구성(추가/제거)이 하나라도 변경되면 action\_type은 NEW이다.
* RENEW는 App/Workspace 구성 변경 없이 계약 기간을 연장하는 후속 Contract version이며, 연장 시점의 금액·앱별 사용량·세일즈 담당자·원본 계약서 링크는 새로 입력 또는 갱신할 수 있다.
* 기존 "계약 추가"(Workspace 추가, App 추가)는 앱/Workspace 구성이 변경되므로 action\_type = NEW로 분류한다.

**분류 판단 기준 (경계 케이스)**

| 변경 내용 | 분류 | 근거 |
| --- | --- | --- |
| 기간 연장 ± 금액·사용량 변경 (앱 구성 동일) | RENEW | 구성 유지 + 기간 연장 + 조건 갱신 |
| 앱 추가 또는 제거 | NEW | 구성 변경 → 새 계약 계보 |
| Workspace 추가 | NEW | 구성 변경 |
| 사용량만 변경 (기간·구성 동일) | CORRECT | 종이 계약서와 시스템 입력값 불일치 정정 |
| 금액만 변경 (기간·구성 동일) | CORRECT | 입력값 정정 |
| 기간 + 앱 구성 동시 변경 | NEW | 구성 변경 포함 시 항상 NEW |
| 시작일이 다른 앱 추가 | NEW (별도 Contract) | 동일 Contract 내 앱별 독립 시작일 불허 |

*※ RENEW는 구성 유지 + 기간 연장 + 상업 조건 갱신에 한정. 판단이 모호한 경우 NEW로 처리한다.*

*※ RENEW에서 금액·사용량 변경은 기간 연장에 수반되는 조건 갱신이다. 기간 변경 없이 금액·사용량만 변경하는 경우는 입력값 정정(CORRECT)이다.*

*※ 세부 DTO 허용/금지 필드 매트릭스는 미결 항목 4번 참고.*

**DTO 및 서버 검증 원칙**

* 액션 유형별로 DTO를 분리한다.
* 사용자가 선택한 액션 유형에 따라 입력 가능한 필드를 제한한다.
* DTO 형식만 맞더라도 아래 경우는 서버가 거절한다:

  + RENEW인데 앱 구성 변경이 포함된 경우
  + CORRECT인데 신규 계약 수준의 변경이 발생한 경우
* 세부 허용/금지 필드 매트릭스는 별도 정의 필요 (11.2 미결 항목 참고)

**NEW의 버전 체인 원칙**

* NEW는 기존 계약과 버전 계보(version lineage)로 연결하지 않는다 (previous\_contract\_id = NULL).
* 기존 계약과의 관계는 Org\_id, action\_type, change\_reason, 감사 로그로 추적한다.

**변경 이력 기록**

* 계약 이력 = 버전 이력 (어떤 버전이 언제, 어떤 분류로 생성되었는지)
* 감사 로그 = 행위 이력 (누가, 언제, 어떤 사유로, 어떤 변경을 했는지. before/after 포함)
* 두 역할을 분리한다.

**수정 불가 항목**

* 고객사명은 어떤 액션 유형에서도 수정 불가

### 화면 흐름: 계약 정정(CORRECT

|  |
| --- |
| 📋 계약 연장(RENEW): 1.1.15 확인 |
| 📋 신규 계약(NEW) Workspace/App 구성 변경: 1.1.16 확인 |
|  |
| 📋 계약 정정(CORRECT) 흐름 |
| ① 계약 상세 화면 → [계약 정정] 버튼 클릭 → 정정 입력 폼 |
| (조회 전용) 고객사명, 계약 앱 목록, Workspace/App 구성, 계약 시작일, 종료일 |
| (프리필 + 수정 가능) 계약 금액, 앱별 사용량, 세일즈 담당자 이름/이메일, 원본 계약서 링크, 메모 |
| ② 사유 입력 필수 |
| ③ [저장] 클릭 → 새 Contract 버전 생성 (action\_type = CORRECT, previous\_contract\_id = 기존 계약 ID) |
| → 기존 계약 버전은 SUPERSEDED 상태로 전환 |
| → 감사 로그 기록 (변경 전/후 값 포함) |
| → 계약 상세 화면으로 복귀 |
|  |
| [계약 이력 확인] |
| ③ 계약 상세 화면 → [계약 이력 탭] → Contract 버전 목록 확인 |
| - 표시 컬럼: 분류(action\_type) / 버전 생성 일시 / 생성자 / 상태 / 사유 |
| > 값이 없는 경우는 '-' 로 표시 |
| 계약 내용의 상세 변경 사항은 Audit Log에서 확인 |

### 화면 흐름: 계약 취소(CANCELLED)

|  |
| --- |
| 📋 계약 취소 흐름 |
| ① 계약 상세 화면 → [계약 취소] 버튼 클릭 (Contract가 SCHEDULED 상태일 때만 노출) |
| ② 사유 입력 모달 표시 → 취소 사유 입력 (필수) |
| ③ 확인 모달: '발효 전 계약을 취소합니다. 취소된 계약은 효력이 발생하지 않으며 이력으로만 보존됩니다. 계속하시겠습니까?' |
| ④ [확인] 클릭 → Contract 상태 CANCELLED 전환 |
| → 계약 이력 탭에서 CANCELLED 상태로 조회 가능 (읽기 전용) |
| → 감사 로그 기록 |

### 1.1.12 계약 이력 조회

### 정책

* 계약 상세 화면 내 [계약 이력 탭]에서 Contract 버전 이력 조회 가능

  + 분류: NEW(신규), RENEW(연장), CORRECT(정정)
  + 표시 항목: 분류(action\_type) / 버전 생성 일시 / 생성자 / 상태(ACTIVE/SUPERSEDED/EXPIRED/CANCELLED)
  + 과거 버전 클릭 시 해당 시점의 계약 상세 조회 (읽기 전용)
* 계약 이력은 버전 이력이다. 상세 변경 내용(before/after)은 감사 로그에서 확인한다.

### 1.1.14 계약 종료(Org Terminated)

### 정책

* 계약 종료(Org Terminated)는 Contract 조건 또는 고객 요청에 따라 Org 상태가 Terminated로 전환되는 것을 의미한다
* Org가 Terminated 상태로 전환되면 즉시 고객 접근이 차단되고 서비스가 중단된다.
* Org Terminated 전환 케이스:

  + 계약 만료: 모든 ACTIVE Contract가 EXPIRED되고 SCHEDULED Contract도 없는 경우 시스템 자동 전환
  + 중도 해지: 계약 기간 중 고객 요청 또는 운영 판단에 의해 Backoffice Admin이 수동 전환. Contract 자체는 상태 모델 변경 없이 ACTIVE를 유지하며, 종료일 도래 시 EXPIRED로 자동 전이
* Org가 Terminated 상태가 된 이후에는 다음과 같은 처리가 가능하다:
* 종료 후 60일 이내:

  + 데이터 추출: 세일즈 담당자를 통해 요청 후 내부에서 제공
  + 단순 복원: Org 상태를 Terminated → Active로 복원 (사유 입력 필수)
  + 계약 연장: Org 상태를 Active로 전환한 후 신규 Contract를 생성하여 계약 연장 처리
* 종료 후 60일 경과:

  + 모든 데이터 자동 삭제
  + Org 복원 불가

### 화면 흐름

|  |
| --- |
| 📋 계약 종료 흐름 |
| ① 계약 상세 화면 → [계약 종료] 버튼 클릭 |
| ② 확인 모달: '종료 후 60일 뒤 데이터가 삭제됩니다. 계속하시겠습니까?' |
| ③ [확인] 클릭 → Org 상태 Terminated 전환 |
| → 데이터 보존 기간 60일 카운트 시작 |
| → 계약 상세 화면에 종료일 및 데이터 삭제 예정일 표시 |
| → 감사 로그 기록 |
|  |
| [60일 내 복원 — 단순 복원] |
| ④ 계약 상세 화면 → [계약 복원] 버튼 클릭 (60일 경과 후 버튼 미노출 + API 차단) |
| ⑤ 사유 입력 모달 표시 → 사유 입력 (200자) |
| ⑥ [확인] 클릭 → Org Active 전환 + 하위 계정 접근 복구 + Workspace App 활성화 설정 자동 복구 |
| → 복원 사후 통지 이메일 발송 (1.1.8.3, BOF-C-16 참고) |
| → 잔여 D-day 알림 재개 (이미 경과된 D-day는 복원 즉시 발송 안함) |
| → 감사 로그 기록 |
|  |
| [60일 내 계약 연장] |
| ① 계약 상세 화면 → [계약 연장] 버튼 클릭 (Org Terminated + 60일 내일 때 노출) |
| ② 사유 입력 모달 표시 → 복원 사유 입력 (200자) |
| ③ [확인] 클릭 → Org Active 전환 + 하위 계정 접근 복구 + Workspace App 활성화 설정 자동 복구 |
| → 감사 로그에 Org 복원 기록 |
| ④ 복원 완료 후 1.1.15 RENEW 입력 화면으로 자동 이동 → 이후 1.1.15 과정에 따라 진행 |
| → 계약 연장 완료 시 계약 체결 안내 이메일 발송 (1.1.8.2 참고) |

### 1.1.15 계약 연장(RENEW)

### 정책

* 계약 연장: 기존 Contract의 App/Workspace 구성을 유지한 채 계약 기간을 연장하는 후속 Contract version. 연장 시점의 금액·앱별 사용량·세일즈 담당자·원본 계약서 링크는 새 Contract version에 새로 기록한다.

  + 계약 연장은 기존 계약 수정이 아니라 신규 계약 생성 방식으로 처리한다.
* 계약 연장이 되면 직전의 계약정보는 이전 계약 정보로 남고 계약 이력 조회시 이전 계약으로 조회 가능

  + 연장 후 이전 계약 정보는 수정 불가
* 계약이 연장되면 Org 상태는 Active 유지한다. 연장 이력은 감사 로그에 기록
* 연장 계약은 현재 시점에 등록하더라도 미래 시작일과 종료일을 가질 수 있으며, 시작일 도래 시점 부터 적용 된다.
* 계약 연장 완료 시 계약 체결 안내 이메일 발송(1.1.8.2 참고)
* 계약 연장 시 action\_type = RENEW이며, previous\_contract\_id = 기존 계약 ID이다.
* RENEW는 앱 구성이 유지되는 경우에만 사용 가능하다. 앱 구성 변경이 포함되면 NEW로 처리한다.
* 새 Contract version 발효 시점부터 해당 version의 앱별 사용량 기준이 적용된다. 발효 이전 Contract 기간의 사용량 집계는 이전 version 기준으로 확정된다. 집계 로직 상세(초기화 주기 등)는 앱별 정책을 따른다.

*※ Terminated 상태에서의 재계약은 1.1.14의 복원 절차 완료 후 진행한다. 1.1.15의 RENEW 흐름은 Org가 Active인 상태를 전제한다.*

**RENEW의 시작일/종료일 관계별 처리**

| 케이스 | 조건 | 기존 계약 처리 | 새 계약 상태 |
| --- | --- | --- | --- |
| 만료 후 연속 | 새 시작일 ≥ 기존 종료일 | 종료일까지 ACTIVE → EXPIRED | SCHEDULED → 시작일 도래 시 ACTIVE |
| 겹치지만 미발효 | 새 시작일 < 기존 종료일, 아직 미래 | 현재 ACTIVE 유지 | SCHEDULED → 시작일 도래 시 기존 SUPERSEDED + 새 ACTIVE |
| 겹치고 이미 발효 | 새 시작일 ≤ 현재 | 즉시 SUPERSEDED | 즉시 ACTIVE |

**미래 계약(SCHEDULED) 처리 원칙**

* 미래 시작일 계약은 저장 가능하며 SCHEDULED 상태로 생성된다.
* SCHEDULED 계약은 현행 계약이 아니며 예약된 계약으로 취급한다.
* 미래 계약을 수정해야 하는 경우, 기존 레코드를 직접 수정하지 않고 새 미래 계약 버전을 생성한다. 기존 미래 계약은 SUPERSEDED 처리.
* 미래 계약을 취소해야 하는 경우 CANCELLED 상태로 전환한다. 실제 효력은 발생하지 않았지만 이력 보존을 위해 삭제하지 않는다.

### 화면 흐름

|  |
| --- |
| 📋 계약 연장 흐름 |
| ① 계약 상세 화면 → [계약 연장] 버튼 클릭 |
| ② 계약 연장 입력 화면:  (조회 전용) 고객사명, Org, 기존 계약 시작일, 기존 종료일, 기존 앱 목록, 기존 Workspace/App 구성, 기존 계약 금액, 기존 앱별 사용량, 세일즈 담당자 이름, 세일즈 담당자 이메일  (필수) 새 계약 시작일  (필수) 새 계약 종료일  (필수) 새 계약 금액  (필수) 새 앱별 사용량  (필수) 새 세일즈 담당자 이름  (필수) 새 세일즈 담당자 이메일  (필수) 새 원본 계약서 링크(URL)  (선택) 새 메모    ※ RENEW는 기간 변경 전용이다. Workspace/App 구성 변경이 필요한 경우 신규 계약(NEW, 1.1.16)으로 처리한다. |
| ③ 정보 수정 후 [확인] 클릭 → 새 Contract 버전 생성 (action\_type = RENEW, previous\_contract\_id = 기존 계약 ID) + Org 상태 Active 유지 |
| → 시작일이 미래이면 SCHEDULED, 현재/과거이면 즉시 ACTIVE (기존 버전은 상태 전이 규칙에 따라 처리) |
| → 계약 상세 화면 갱신된 종료일 표시 |
| -> 직전 Contract 버전은 이전 계약 정보로 보존되며, 계약 이력 조회 시 과거 버전으로 확인 가능 |

### 1.1.16 신규 계약(NEW): 기존 계약의 Workspace/App 구성 변경 처리

### 정책

* 기존 계약의 Workspace 또는 App 구성이 변경되는 모든 경우(추가/제거)는 기존 계약의 연장이 아니라 신규 계약(action\_type = NEW)으로 처리한다.
* NEW 계약은 새 계약 계보를 시작하며, 기존 계약과 버전 체인을 공유하지 않는다 (previous\_contract\_id = NULL).
* 동일 Org 내 동일 앱에 대해 유효기간이 겹치는 NEW 계약은 등록할 수 없다. 새 NEW 계약을 등록하려면 기존 계약의 동일 앱을 먼저 종료하거나 정리하여 중복 기간이 발생하지 않도록 해야 한다.

**Workspace 추가**

* 추가 Workspace는 별도 종이 계약 후 처리
* Backoffice Admin이 생성하며, 기준 정보 범위는 Master/Org Admin이 설정
* 기준 정보 범위는 스터디 1개 단위, 해당 스터디에 속한 프로덕트 복수 선택 가능
* 계약 생성 완료 시 계약 체결 안내 이메일 발송(1.1.8.2 참고)

**App 추가**

* 계약 기간 중 신규 App 추가는 별도 종이 계약 후 처리 (세일즈 담당자 → Backoffice Admin으로 정보 전달)
* 계약 생성 완료 시 계약 체결 안내 이메일 발송(1.1.8.2 참고)

### 화면 흐름

|  |
| --- |
| 📋 Workspace/App 구성 변경 시 신규 계약 생성 흐름 |
| ① GNB [계약 관리] → 계약 목록 화면. 해당 Org의 기존 계약 확인 → Workspace 또는 App 추가가 필요한 경우 [+ 새 계약] 버튼 클릭 → 계약 생성 화면 |
| ② 기존 Org 선택 |
| ③ 계약 정보 입력:  (조회 전용) 고객사명, Org 기존 계약 시작일, Org 기존 계약 종료일 — 운영자 참고용  (필수) 새 Contract 시작일 / 종료일  (필수) 계약 앱 목록 — 전체 앱 목록에서 체크박스로 선택. 최소 1개 필수  (필수) 앱의 Workspace 배정  (Workspace 추가 시) 새 Workspace 이름 입력 (동일 Org 내 유니크).  ※ 기준 정보 범위(Study/Product)는 계약 생성 시점에는 입력하지 않으며, Workspace 생성 후 고객사 Admin이 후속 설정한다  ※ 추가 Workspace는 별도 사용 기간을 입력하지 않으며, 해당 신규 Contract 기간을 그대로 따른다.  (필수) 앱별 사용량  (필수) 계약 금액 (통화 포함)  (필수) 세일즈 담당자 이름 / 이메일  (필수) 원본 계약서 링크 (URL)  (선택) 메모 |
| ④ 동일 Org·동일 앱 유효기간 중복 검증 → 중복 시 저장 차단 |
| ⑤ [저장] 클릭 → 신규 Contract 버전 생성 (action\_type = NEW, previous\_contract\_id = NULL)  → 필요한 Workspace/App 리소스 생성. App 활성화는 Org 관리 > Workspace별 App 활성화 설정(2.6)에서 별도 수행  → 계약 체결 안내 이메일 발송 (1.1.8.2 참고) |

# 2. Org 관리

## 2.1 Org 생성

### 정책

* Org 생성은 계약 생성과 분리된 별도 기능이다. Org를 먼저 생성한 후 계약을 연결한다.
* 고객사명을 입력하면 Org 이름·Main Workspace 이름이 동일값으로 자동완성된다. 각각 독립적으로 수정 가능.
* 저장 시 Org 및 Main Workspace가 함께 생성된다.
* Org 이름은 시스템 전체에서 유니크해야 한다. 중복 시 저장 불가 + 오류 메시지 표시.

### 화면 흐름

|  |
| --- |
| 📋 Org 생성 흐름 |
| ① GNB [Org 관리] → [+ 새 Org] 버튼 클릭 |
| ② 고객사명 입력 → Org 이름·Main Workspace 이름 자동완성 (각각 수정 가능) |
| ③ [저장] 클릭 → Org 및 Main Workspace 생성   * 고객사명 미입력, 고객사 분류 없이 저장 불가 |
| → Org 상세 화면으로 이동 |

## 2.2 Org 목록 조회

### 정책

•  고객사명·Org 상태·계약 기간 기준 검색 및 필터링

•  목록에서 각 Org의 기본 정보(고객사명, Org 상태, Workspace 수, 계약된 앱 수) 확인

### 화면 흐름

|  |
| --- |
| 📋 Org 목록 조회 흐름 |
| ① GNB [Org 관리] 클릭 → Org 목록 화면 |
| ② 검색창에 고객사명 입력 또는 필터 선택 → 목록 갱신 |
| ③ Org 행 클릭 → Org 상세 화면 |

## 2.3 Org 상세 조회 및 정보 수정

### 정책

* 상세 탭 구성: 기본 정보 / Workspace / 사용자 / 계약 정보
* 수정 가능 항목: Org 이름, 내부 정책 등 기본 정보 (계약 관련 수정은 계약 관리에서 처리)

  + Org 이름: 디폴트 값은 계약 시 작성한 고객사명이며, 표시 목적에 따라 수정 가능
  + Org 이름은 동일 고객 여부 판단 기준으로 사용하지 않는다.
  + Org 이름을 수정하더라도 계약 시 입력된 고객사명은 변경되지 않는다.

### 화면 흐름

|  |
| --- |
| 📋 Org 정보 수정 흐름 |
| ① Org 상세 화면 → [기본 정보 탭] |
| ② [수정] 버튼 클릭 → 인라인 수정 모드 전환 (Org Terminated 상태에서는 읽기 전용) |
| ③ 항목 수정 후 [저장] → 변경 완료 |

### 탭 구조와 상세 섹션

**① 기본 정보 탭**

| 항목 | 설명 |
| --- | --- |
| 고객사명 | 계약 시 입력한 고객사명 (읽기 전용. 수정은 계약 관리에서 처리) |
| Org 이름 | 수정 가능 (최대 20자). 디폴트 값은 고객사명. 수정해도 계약상 고객사명은 변경되지 않음 |
| Org 상태 배지 | Pre-Active / Active / Terminated / Terminated (삭제 완료) |
| 생성일 | Org 생성 일시 |
| Workspace 수 | 해당 Org 내 Workspace 수 |
| 계정 수 | 해당 Org 소속 사용자 수 |
| 계약된 앱 수 | 현재 유효 계약에 포함된 앱 수 |

**② Workspace 탭**

해당 Org 내 Workspace 목록을 표시한다. 행 클릭 시 Workspace 상세 화면(2.4)으로 진입.

| 항목 | 설명 |
| --- | --- |
| Workspace 이름 | Main / 추가 구분 표시 |
| 활성화된 앱 수 | ON 상태 앱 수 |
| 상태 | 활성 / 폐쇄 |

액션: 행 클릭 → Workspace 상세(2.4)에서 App 활성화(2.6), 폐쇄(2.7) 처리. 추가 Workspace는 NEW Contract 생성(1.1.16) 시 자동 생성된다.

**③ 사용자 탭**

해당 Org 소속 사용자 목록을 조회하고 Master Admin을 초대하는 용도이다. 사용자 권한 수정·계정 비활성화 등 관리 작업은 GNB 사용자 관리에서 처리한다.

| 항목 | 설명 |
| --- | --- |
| 이름 | 사용자 이름 |
| 이메일 | 사용자 이메일 |
| 역할 | Master Admin / Org Admin / App Admin / App User 등 |
| 계정 상태 | Active / Inactive / Locked / Invitation |
| 최종 로그인 일시 | — |

액션: [Master Admin 초대] (2.9 참고). 그 외 사용자 관련 액션은 이 탭에서 제공하지 않는다.

### Org 상태별 화면 동작

Org 상세 화면에서 상태에 따라 표시되는 정보와 허용되는 액션이 달라진다.

| 기능 | Pre-Active | Active | Terminated (60일 내) | Terminated (60일 경과) |
| --- | --- | --- | --- | --- |
| 기본 정보 탭 조회 | ✓ | ✓ | ✓ | ✓ |
| 기본 정보 수정(Org 이름 수정) | ✓ | ✓ | (읽기 전용) | (읽기 전용) |
| Workspace 탭 조회 | ✓ | ✓ | (읽기 전용) | (읽기 전용) |
| Workspace 이름 수정 | ✓ | ✓ | (읽기 전용) | (읽기 전용) |
| App 활성화 설정 변경 | ✓ | ✓ | (읽기 전용) | (읽기 전용) |
| Workspace 폐쇄/완전 폐쇄 | (읽기 전용) | ✓ (추가 Workspace 만) | (읽기 전용)   * Org가 Terminated 되면 추가 Workspace 데이터가 자동으로 Main Workspace 병합되어야 한다. | (읽기 전용) |
| 사용자 탭 조회 | ✓ | ✓ | (읽기 전용) | (읽기 전용) |
| Master Admin 초대 | ✓ | ✓ | (읽기 전용) | (읽기 전용) |
| 계약 정보 탭 조회 | ✓ | ✓ | ✓ | ✓ |
| Break-Glass 접근 (Admin only) | (읽기 전용) | ✓ (고객 데이터 직접 접근은 Break-Glass 경유만 가능 — 6.1 참고) | ✓ (60일 내) | (읽기 전용) |
| 상태 배지 표시 | Pre-Active | Active | Terminated | Terminated (삭제 완료) |

*※ Pre-Active 상태에서는 Master Admin 초대와 App 활성화 설정은 가능하다. 추가 Workspace는 NEW Contract 생성(1.1.16)으로만 가능하다.*

*※ 읽기 전용: 탭/화면은 접근 가능하나 수정·생성·삭제 등 액션이 비활성화된다. API 레벨에서도 차단.*

*※ Terminated 60일 경과 시 Workspace/사용자 탭은 접근 가능하나 데이터가 없는 빈 상태로 표시된다.*

## 2.4 Workspace 상세 조회

### 정책

* Org 상세 화면의 [Workspace 탭]에서 Workspace 행 클릭 시 Workspace 상세 화면으로 진입한다.
* Workspace 상세 화면에서 표시되는 정보는 아래와 같다.

**공통 표시 항목 (Main Workspace / 추가 Workspace 공통)**

| 항목 | 설명 |
| --- | --- |
| Workspace 이름 | 수정 가능 (동일 Org 내 유니크 강제) |
| App 목록 | 계약에서 허용된 앱 전체 목록 표시. 활성화된 앱은 ON, 비활성화된 앱은 OFF로 표시. Backoffice Admin이 토글로 설정 |

**추가 Workspace 전용 표시 항목**

| 항목 | 설명 |
| --- | --- |
| 생성일 | Workspace 생성 일시 |
| 계약 기간 | 해당 Workspace가 포함된 Contract의 시작일 ~ 종료일. Workspace 자체의 독립 계약기간은 없다. |
| 기준 정보: Study | 해당 Workspace에 설정된 스터디 정보 |
| 기준 정보: Product | 해당 스터디에 속한 프로덕트 목록 |

**액션 버튼**

| 버튼 | 조건 | 설명 |
| --- | --- | --- |
| [수정] | 공통 | Workspace 이름 수정 모드 전환 |
| [Workspace 폐쇄] | 추가 Workspace만 | Workspace 비활성화 처리. Main Workspace는 Org 종료 시에만 처리 |
| [Workspace 완전 폐쇄] | 추가 Workspace가 폐쇄 상태인 경우 (수동 폐쇄 또는 계약 종료로 인한 자동 폐쇄 포함) | 데이터 이관 완료 확인 후 완전 폐쇄 처리. 계약 종료로 폐쇄된 추가 Workspace도 반드시 이 버튼을 눌러야 완전 폐쇄된다. 상세 절차는 2.7 참고 |

*※ Main Workspace는 폐쇄/완전 폐쇄 버튼이 표시되지 않는다. Main Workspace는 Org 종료 시에만 폐쇄된다.*

### 화면 흐름

|  |
| --- |
| 📋 Workspace 상세 진입 흐름 |
| ① Org 상세 화면 → [Workspace 탭] |
| ② 대상 Workspace 행 클릭 → Workspace 상세 화면 |
| → Workspace 이름, App 목록(ON/OFF), 액션 버튼 표시 |
| → 추가 Workspace인 경우 생성일, 계약 기간, 기준 정보(Study/Product) 추가 표시 |

## 2.5 추가 Workspace 생성

추가 Workspace는 NEW Contract 생성(1.1.16) 시 자동 생성된다. Org 관리 화면에서 별도 생성하는 기능은 제공하지 않는다.

* Workspace 이름은 NEW Contract 생성 시 입력하며, 동일 Org 내 유니크 강제.
* 기준 정보 범위(Study/Product)는 Workspace 생성 후 고객사 Admin이 후속 설정한다.

## 2.6 Workspace별 App 활성화 설정

### 정책

* Workspace별로 사용할 앱을 활성화/비활성화 설정
* 활성화 가능한 앱 목록은 계약에서 허용된 앱 범위 내이며, 해당 App을 포함한 Contract 버전이 유효(ACTIVE)한 경우에만 선택 가능
* Workspace 내 같은 앱을 여러 개 사용할 수 없음
* 앱은 최대 10개까지 활성화 가능
* Workspace 내 App 활성/비활성 설정 권한: Backoffice Admin 전용
* Org가 Terminated 상태에서는 App 활성화 설정 변경 불가.(읽기전용)

### 화면 흐름: App 활성화 설정

|  |
| --- |
| 📋 App 활성화 설정 흐름 |
| ① Org 상세 화면 → [Workspace 탭] |
| ② 대상 Workspace 행 클릭 → Workspace 상세 화면 |
| ③ [App 활성화] 섹션에서 앱별 ON/OFF 토글 설정 |
| - 계약에서 허용된 앱만 선택 가능 (미계약 앱은 비활성화 표시) |
| ④ [저장] 클릭 → 설정 즉시 반영 |

### 화면흐름: Workspace 이름 수정

|  |
| --- |
| 📋 Workspace 이름 수정 흐름 |
| ① [Org 관리] → 해당 Org 클릭 → [Workspace 탭] |
| ② 수정할 Workspace 행 클릭 → Workspace 상세 화면 |
| ③ [수정] 버튼 클릭 → Workspace 이름 필드 편집 모드 전환 |
| ④ 이름 수정 후 [저장] → 동일 Org 내 중복 여부 검증 |
| → 중복 시: 저장 불가 + 오류 메시지("동일 Org 내 이미 사용 중인 이름입니다.") 표시 |
| → 중복 아닐 시: 저장 완료 + 즉시 반영 |

## 2.7 Workspace 폐쇄

### 정책

* 세 가지 방식으로 폐쇄가 트리거된다 (A-1, A-2, B)

  + 케이스 A

    - 케이스 A-1: Org 전체 계약 종료로 Terminated 시 하위 Workspace 일괄 자동 폐쇄. 추가 Workspace가 있는 경우 해당 데이터가 Main Workspace에 정상 병합되었는지 확인 후 고객에게 데이터를 반출한다.
    - A-2: 추가 Workspace를 포함한 Contract가 EXPIRED되고, 후속 ACTIVE/SCHEDULED Contract에 동일 Workspace 구성이 승계되지 않는 경우 해당 Workspace만 시스템 자동 폐쇄. Org 및 Main Workspace는 영향 없음
  + 케이스 B: 고객 요청 중간 폐쇄 - 고객이 세일즈 담당자에게 폐쇄 요청 → 세일즈 담당자가 Backoffice Admin에게 이메일로 전달 → Backoffice Admin이 확인 후 처리
* Main Workspace는 Org 계약 종료 시에만 폐쇄 처리됨

#### 정책: 추가 Workspace의 폐쇄 절차 (케이스 A-2, B 공통)

* 폐쇄 처리 시 해당 Workspace 내 계정은 해당 Workspace 범위에서 비활성화
* 폐쇄된 Workspace는 데이터 이관이 완전하게 완료 되었다고 확인이 되기 전 까지는 Master/Org Admin이 조회 가능
* 폐쇄된 Workspace의 데이터는 이관이 완료 되면 상위 Org에서 조회 가능

  + 조회 가능한 데이터의 의미

    - 기본적으로 태넌트에서는 Main Workspace에 있는 데이터를 조회 가능

      * 추후 기획되는 홈에서 Org홈의 메뉴에 트래커와 대시보드를 추가 할 예정이고, 이 트래커와 대시보드에서는 메인 Workspace에 있는 앱의 정보를 조회 가능.
    - 추가로 생성한 워크스페이스가 폐쇄되는 경우, 해당 정보는 Main Workspace에 결합되어 태넌트에서 해당 정보를 조회 가능
    - (해당 케이스는 Safety DB에 한정해서 현재 논의가 되었고 다른 앱의 경우 추후 별도 확정한다.)
* 이관이 완벽하게 된 경우에 완전 폐쇄 버튼 클릭하여 폐쇄 처리

### 화면 흐름(케이스 B)

|  |
| --- |
| 📋 Workspace 폐쇄 흐름 |
| ① 고객이 세일즈 담당자에게 Workspace 폐쇄 요청 (전화/이메일) |
| ② 세일즈 담당자가 Backoffice Admin에게 이메일로 폐쇄 요청 내용 전달 |
| ③ Backoffice Admin이 GNB [Org 관리] → 해당 Org 클릭 → [Workspace 탭] |
| ④ 폐쇄 대상 Workspace 행 클릭 → Workspace 상세 화면 |
| ⑤ [Workspace 폐쇄] 버튼 클릭 → 확인 모달 표시: '해당 워크스페이스를 정말로 폐쇄 하시겠습니까?' |
| ⑥ [확인] 클릭 → Workspace 비활성화 처리 완료 |
| -> 비활성화 처리 된 Workspace 데이터가 제대로 이관 되었는지 Master/Org Admin은 확인하고 문제 없는 경우 고객사가 운영사에 요청하여 [Workspace 완전 폐쇄] 버튼 클릭하여 폐쇄 처리  -> 완전 폐쇄 버튼은 폐쇄 버튼 누르기 전 까지는 비활성화 |

## 2.8 Org 종료

### 정책

* Org 종료는 계약 종료 또는 고객사 요청에 따른 종료로 Org가 Terminated 상태로 전환 되는 것을 의미한다.

  + 예: 계약 기간 종료에 따라 Org 상태가 Terminated로 전환
* Org가 Terminated 상태로 전환되면 하위 모든 계정 접근이 즉시 차단되고 활성 세션이 강제 종료된다.
* Terminated 상태에서도 계약 정보 및 상태 확인을 위한 Backoffice 관리 정보는 조회 가능하다.
* Org 내부 운영 데이터는 60일간 보존 후 자동 삭제된다.
* 멀티 테넌트 도입 이후 특정 Org를 수동으로 상태 전환하는 정책은 추후 별도 정의한다.

### 화면 흐름

|  |
| --- |
| 📋 Org 종료 후 Org 관리 화면 변화 |
| ① 계약 종료 처리 완료 (1.1.14 참고) → Org 상태 Terminated 전환 |
| ② GNB [Org 관리] → Org 목록 화면 → 해당 Org 상태 배지 Terminated 표시 |
| ③ Org 상세 진입 → 기본 정보 탭 / 계약 정보 탭 조회 가능 |
| → Workspace 탭, 사용자 탭 조회 가능(읽기 전용) |
| → 데이터 삭제 예정일 표시 |
| ④ 60일 내: [계약 복원] 버튼 노출 → 복원 흐름은 1.1.14 참고 |
| ⑤ 60일 경과: 데이터 자동 삭제 → Terminated (삭제 완료) 상태로 변경 |

### 화면 흐름: 태넌트가 여러개 있을 때 특정 태넌트를 수동으로 Terminated 처리(추후 반영)

|  |
| --- |
| 📋 Org가 여러개 있을때 특정 Org 종료 상태 전환 흐름(추후 반영) |
| ① Org 상세 화면 → [Org 비활성화] 버튼 클릭 |
| ② 확인 모달: '비활성화 시 하위 모든 계정이 접근 차단됩니다. 계속하시겠습니까?' |
| ③ [확인] 클릭 → Org Terminated + 하위 계정 일괄 비활성화 + 세션 강제 종료 |
| → Org 목록에서 해당 Org 상태 Terminated 표시 |

## 2.9 Org 내 Master Admin 초대

### 정책

•  Backoffice Admin만 Master Admin 계정 생성 및 초대 가능

•  생성 시 이메일, 이름 입력 후 초대 메일 자동 발송 (계정 상태: Invitation)

•  이메일 중복 검증 적용

•  초대 링크 유효기간: 7일. 만료 시 Backoffice Admin이 재발송 가능

•  재발송 시 이전 링크 즉시 파기, 신규 링크만 유효

• Org가 Pre-Active 상태인 기간에도 Master Admin 초대는 가능하다. 단, 초대받은 Master Admin이 실제 로그인하려면 Org가 Active 상태여야 한다.

• Org가 Terminated 상태에서는 Master Admin 초대 불가.(읽기 전용)

### 화면 흐름

|  |
| --- |
| 📋 Master Admin 초대 / 재발송 흐름 |
| [최초 초대] |
| ① Org 상세 화면 → [사용자 탭] |
| ② [Master Admin 초대] 버튼 클릭 → 초대 폼 모달 표시 (Terminated 상태에서는 읽기 전용) |
| ③ 이메일 주소 입력 → 실시간 중복 검증 |
| ④ 이름 입력 후 [초대 발송] 클릭 |
| → 초대 메일 자동 발송 + 사용자 목록에 Invitation 상태로 추가 |
|  |
| [초대 재발송 - 링크 만료 또는 분실 시] |
| ⑤ 사용자 목록에서 Invitation 상태 계정 확인 → [재발송] 버튼 클릭 |
| ⑥ 확인 모달 → [확인] → 이전 링크 파기 + 신규 초대 메일 발송 |

# 3. 전체 사용자 관리

Backoffice에서 Neptune 플랫폼 전체 사용자를 통합 조회 및 관리한다.

## 3.1 사용자 목록 조회

### 정책

• 이름, 이메일, 고객사, Org 역할, App 역할, 계정 상태, 최종 로그인 일시 표시

• 계정 상태(Active / Inactive / Locked / Invitation)·고객사 기준 필터링 및 이름·이메일·고객사 기반 검색

### 화면 흐름

|  |
| --- |
| 📋 사용자 목록 조회 흐름 |
| ① GNB [사용자 관리] 클릭 → 전체 사용자 목록 화면 |
| ② 검색창에 이름, 이메일, 고객사 입력, 또는 계정 상태(Active / Inactive / Locked / Invitation)·고객사 필터 선택 → 목록 갱신 |
| 사용자 행 클릭 → 사용자 상세 화면 |

## 3.2 사용자 정보 수정

### 정책

•  부여/수정 가능 항목: 이름, Org 역할, 워크스페이스/앱 접근 권한, App 역할

•  앱 접근 권한 부여 시 해당 Workspace에서 해당 App이 활성화되어 있어야 함. 비활성 App은 권한 부여 UI에서 선택 불가 처리

•  이메일(계정 ID)은 수정 불가

•  비밀번호 재설정: 재설정 메일 발송만 가능, 직접 입력 UI 미제공

• 역할 변경, 앱 접근 권한 부여·변경은 Backoffice Admin 전용이다. Operator는 수행할 수 없다 (8.2 권한 매트릭스 참고).

• Org가 Pre-Active / Terminated 상태에서는 사용자 권한 수정 불가. (읽기 전용)

• Master Admin 또는 Org Admin도 Workspace 할당 및 App 접근 권한을 명시적으로 설정한다. 필요 시 본인 계정에 대해서도 동일하게 설정할 수 있다.

### 화면 흐름

|  |
| --- |
| 📋 사용자 정보 수정 흐름 |
| ① 사용자 상세 화면 → [수정] 버튼 클릭 → 수정 모드 전환 (Org가 Pre-Active / Terminated 상태에서는 읽기 전용) |
| ② 이름 / Org 역할 / Workspace / 앱 접근 권한 / App 역할 수정 |
| ③ [저장] 클릭 → 변경 즉시 적용 + 대상 사용자 세션에 즉시 반영 |
| ※ 권한 변경 시 케이스별 처리: |
| - Org Admin → Org User 강등 (Org 역할 변경): 전용 화면 접속 중이면 안내 팝업("역할이 변경되어 해당 화면에 접근할 수 없습니다. 홈으로 이동합니다.") 표시 후 홈 이동 |
| - App Admin → App User 변경 (App 역할 변경): 어드민 화면 접속 중이면 안내 팝업("역할이 변경되어 관리자 화면에 접근할 수 없습니다. 홈으로 이동합니다.") 표시 후 홈 이동 |
| - 그 외 화면(앱 내 작업 중 등): 별도 안내 없이 권한 변경만 처리 |
|  |
| [비밀번호 재설정] |
| ① 사용자 상세 화면 → [비밀번호 재설정] 버튼 클릭 |
| ② 확인 모달 → [확인] 클릭 → 사용자 이메일로 재설정 링크 발송 |

## 3.3 계정 비활성화 / 재활성화

### 정책

• Backoffice Admin 및 Operator 모두 수행 가능하다 (8.2 권한 매트릭스 참고).

•  비활성화: 처리 즉시 해당 계정의 모든 활성 세션 강제 종료

•  Master Admin 계정은 계약 종료 후에만 비활성화 처리 가능

•  계정 삭제는 지원하지 않으며 비활성화로 대체

•  비활성화된 계정은 목록에서 유지, 재활성화 가능

### 화면 흐름

|  |
| --- |
| 📋 계정 비활성화 흐름 |
| ① 사용자 상세 화면 → [비활성화] 버튼 클릭 |
| (Master Admin인 경우 계약 종료 전 버튼 비활성화 처리) |
| ② 확인 모달: '비활성화 시 모든 세션이 즉시 종료됩니다. 계속하시겠습니까?' |
| ③ [확인] 클릭 → 계정 비활성화 + 활성 세션 강제 종료 |
|  |
| [재활성화] |
| ① Inactive 상태 계정 상세 화면 → [재활성화] 버튼 클릭 → Active 전환 |

## 3.4 계정 잠금 해제

### 정책

•  계정 잠금 해제는 본인 비밀번호 재설정으로만 해제

•  잠금 해제 권한 상세는 Account 정책 문서 LCK-05 참조

### 화면 흐름

|  |
| --- |
| 📋 계정 잠금 해제 흐름 |
| 잠금 해제는 본인 비밀번호 재설정으로 해제 |

# 4. 앱 설정

## 4.1 앱 내 링크 관리

### 정책

•  앱 내에서 제공되는 외부 링크를 Backoffice에서 관리

•  관리 링크 종류: 매뉴얼 링크, CS(고객 지원) 링크

•  앱별로 독립적으로 관리. 변경 즉시 앱 내 반영

### 화면 흐름

|  |
| --- |
| 📋 링크 관리 흐름 |
| ① GNB [앱 설정] 클릭 → 앱 목록 화면 |
| ② 설정할 앱 클릭 → 앱 상세 설정 화면 |
| ③ [링크 관리 탭] → 매뉴얼 링크 / CS 링크 URL 입력 또는 수정 |
| ④ [저장] 클릭 → 변경 즉시 앱 내 반영 |

# 5. Log 조회

## 5.1 Log 체계 개요

Backoffice에서 조회 가능한 로그는 아래 3가지로 구분된다. 로그 분류 규칙, 컬럼 구성, 보존/무결성/Export 원칙의 상세는 AUD(Audit Log/Activity Log/Audit Trail) 정책 문서를 참조한다.

| 조회 메뉴 | 조회 대상 | 접근 권한 |
| --- | --- | --- |
| GNB [Log] → 고객사 로그 | 고객사 Org의 Audit Trail·Activity Log·Audit Log 통합 | Admin / Operator |
| GNB [Log] → Backoffice Activity Log | Backoffice Admin/Operator의 운영 행위 기록 (계약·Org·Workspace·사용자·앱설정·Break-Glass·알림 등) | Admin / Operator |
| GNB [Admin] → Backoffice Audit Log | Backoffice 내부 계정 관리 행위 기록 (BOF 계정 생성·역할 변경·비활성화 등) | Admin 전용 |

**공통 조회 규칙**

* 화면 기본 최근 2주, 최대 1년. 최대 10만 건(페이지당 30건)
* 로그 행 클릭 시 상세 정보 모달 또는 사이드 패널 표시. 변경 전/후 값 포함
* CSV Export: 조회 기간 기준 최대 1년치 전체 건수 다운로드 (화면 10만 건 제한 적용). 기간 미설정 시 30일치 Export
* Append-only 구조. 수정/삭제 불가

## 5.2 고객사 로그 조회 (GNB [Log])

### 정책

* Backoffice Admin 및 Operator 접근 가능
* 고객사의 Audit Trail, Activity Log, Audit Log를 통합 조회
* 진입 시 결과 미표시. 고객사(Org)와 로그 종류를 선택한 후 [검색]으로 조회
* 날짜 범위 미지정 시 최근 2주 기록 조회
* 필터: 날짜 범위 / 고객사명(Org) / Workspace / App / 로그 종류(Audit Trail, Activity Log, Audit Log) / 카테고리 / 행위자 / 대상 계정

### 화면 흐름

|  |
| --- |
| 📋 고객사 로그 조회 흐름 |
| ① GNB [Log] → [고객사 로그] 진입 → 조회 화면 (초기 결과 미표시) |
| ② 고객사(Org) 선택 + 로그 종류 선택 (Audit Trail / Activity Log / Audit Log) |
| ③ 추가 필터 설정: 날짜 범위 / Workspace / App / 카테고리 / 행위자 / 대상 계정 → [검색] |
| ④ 로그 목록 표시. 로그 행 클릭 → 상세 정보 모달 (변경 전/후 값 포함) |
| ⑤ [CSV Export] 클릭 → 조회 기간 기준 전체 건수 다운로드 |

## 5.3 Backoffice Activity Log 조회 (GNB [Log])

### 정책

* Backoffice Admin 및 Operator 접근 가능
* Backoffice Admin/Operator의 Admin 메뉴 외부 운영 행위 기록을 조회 (계약·Org·Workspace·사용자·앱설정·Break-Glass·알림·인증 등)
* 필터: 날짜 범위 / 카테고리 / 행위자 / 대상 계정

### 화면 흐름

|  |
| --- |
| 📋 Backoffice Activity Log 조회 흐름 |
| ① GNB [Log] → [Backoffice Activity Log] 진입 → 최근 2주 로그 자동 표시 |
| ② 필터 설정: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 → [검색] → 목록 갱신 |
| ③ 로그 행 클릭 → 상세 정보 모달 표시 |
| ④ [CSV Export] 클릭 → 조회 기간 기준 전체 건수 다운로드 |

## 5.4 Backoffice Audit Log 조회 (GNB [Admin] → [Audit Log])

### 정책

* Backoffice Admin 전용. Operator 접근 불가
* Backoffice Admin 메뉴 내부 행위 기록을 조회 (BOF 계정 생성·역할 변경·비활성화·재활성화·잠금 해제 등)
* 필터: 날짜 범위 / 카테고리 / 행위자 / 대상 계정

### 화면 흐름

|  |
| --- |
| 📋 Backoffice Audit Log 조회 흐름 |
| ① GNB [Admin] → [Audit Log] 진입 → 최근 2주 로그 자동 표시 |
| ② 필터 설정: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 → [검색] → 목록 갱신 |
| ③ 로그 행 클릭 → 상세 정보 모달 표시 |
| ④ [CSV Export] 클릭 → 조회 기간 기준 전체 건수 다운로드 |

## 5.5 기록 항목 전체 정의

Backoffice에서 기록되는 전체 항목은 다음과 같다. 기록 위치는 AUD 정책 3.2 기준.

| 기록 위치 | 분류 | Task | 표시 문구 | 정책 | Author |
| --- | --- | --- | --- | --- | --- |
| BOF Activity Log | 계약 | 계약 생성(NEW) | Contract created: [고객사명] [시작일~종료일] | 계약 생성 시 | 행위자 ID |
| BOF Activity Log | 계약 | 계약 정정(CORRECT) | Contract corrected: [항목] [변경 전 값] → [변경 후 값] | 계약 정정 시. 항목별 행 기록 | 행위자 ID |
| BOF Activity Log | 계약 | 계약 연장(RENEW) | Contract renewed: [고객사명] [기존 종료일] → [신규 종료일] | 계약 연장 시 | 행위자 ID |
| BOF Activity Log | 계약 | 구성 변경 신규 계약(NEW) | Contract created (config change): [고객사명] [변경 내용] | Workspace/App 구성 변경으로 신규 계약 생성 시 | 행위자 ID |
| BOF Activity Log | 계약 | 계약 취소(CANCELLED) | Contract cancelled: [고객사명] | SCHEDULED 상태 계약 취소 시 | 행위자 ID |
| BOF Activity Log | 계약 | 계약 만료(EXPIRED) | Contract expired: [고객사명] | 종료일 도래에 의한 자동 만료 시 | 시스템 |
| BOF Activity Log | 계약 | 미래 계약 발효(SCHEDULED→ACTIVE) | Contract activated (scheduled): [고객사명] | 시작일 도래에 의한 자동 발효 시 | 시스템 |
| BOF Activity Log + 고객 Audit Log | Org | Org 생성 | Org created: [Org명] | Org 생성 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Org | Org 이름 수정 | Org name changed: [변경 전] → [변경 후] | Org 이름 수정 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Org | Org 종료(Terminated) | Org terminated: [고객사명] [데이터 삭제 예정일] | Org Terminated 전환 시 | 행위자 ID / 시스템 |
| BOF Activity Log + 고객 Audit Log | Org | Org 복원(종료→활성) | Org restored from terminated: [고객사명] [사유] | Terminated → Active 복원 시 (60일 내 한정) | 행위자 ID |
| BOF Activity Log | Org | Org Pre-Active → Active 전환 | Org activated: [Org명] | Contract ACTIVE 전환에 의한 Org 상태 변경 시 | 시스템 |
| BOF Activity Log | Org | Org Active → Pre-Active 전환 | Org deactivated to pre-active: [Org명] | 모든 ACTIVE Contract EXPIRED + SCHEDULED 존재 시 | 시스템 |
| BOF Activity Log | 인증 | 로그인 차단 (Org 비활성) | Login blocked: [이메일] [Org명] [Org 상태] | Pre-Active/Terminated 상태에서 로그인 시도 시 | 시스템 |
| BOF Activity Log | 알림 | 계약 종료 사전 알림 발송 | Contract expiry notification sent: [고객사명] [D-N일] [성공/실패] | D-90/30/7/1일 자동 발송 시 | 시스템 |
| BOF Activity Log | 알림 | 계약 체결 안내 발송 | Contract confirmation sent: [고객사명] [성공/실패] | 신규 계약/연장/변경 완료 시 | 시스템 |
| BOF Activity Log | 알림 | 복원 사후 통지 발송 | Restoration notification sent: [고객사명] [성공/실패] | Terminated → Active 복원 시 | 시스템 |
| BOF Activity Log + 고객 Audit Log | Workspace | Workspace 생성 | Workspace created: [Workspace명] in [Org명] | Workspace 생성 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Workspace | Workspace 이름 수정 | Workspace renamed: [변경 전] → [변경 후] | Workspace 이름 수정 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Workspace | App 활성화 설정 변경 | App activation changed: [Workspace명] [앱명] [ON/OFF] | App 활성화/비활성화 토글 변경 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Workspace | Workspace 폐쇄 | Workspace closed: [Workspace명] in [Org명] | Workspace 폐쇄 처리 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Workspace | Workspace 완전 폐쇄 | Workspace permanently closed: [Workspace명] in [Org명] | 데이터 이관 완료 후 완전 폐쇄 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | 사용자 | 사용자 생성/초대 | User invited: [이름] [이메일] [Org 역할][App 역할] | 사용자 초대 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | 사용자 | 사용자 정보 수정 | User updated: [항목] [변경 전] → [변경 후] | 이름, 역할, Workspace, 앱 접근 권한 변경 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | 사용자 | 계정 비활성화 | User deactivated: [이름] [이메일] | 계정 비활성화 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | 사용자 | 계정 재활성화 | User reactivated: [이름] [이메일] | 계정 재활성화 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | 사용자 | 계정 잠금 해제 | User unlocked: [이름] [이메일] | 잠금 해제 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | 사용자 | 비밀번호 재설정 메일 발송 | Password reset sent: [이메일] | 재설정 메일 발송 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | 사용자 | 초대 재발송 | Invitation resent: [이메일] | 초대 링크 재발송 시 (기존 링크 파기) | 행위자 ID |
| BOF Activity Log | 인증 | 로그인 성공 | Backoffice logged in: [이메일] | 로그인 성공 시 | 본인 ID |
| BOF Activity Log | 인증 | 로그인 실패 | Failed Backoffice login attempt: [이메일] [사유] | 로그인 실패 시 | 본인 ID |
| BOF Activity Log | 인증 | 로그아웃 | Logged out: [이메일] | 명시적 로그아웃 시 | 본인 ID |
| BOF Activity Log | 인증 | 세션 만료 | Logged out due to session timeout: [이메일] | 시간 초과 강제 로그아웃 시 | 본인 ID |
| BOF Activity Log | 인증 | 강제 로그아웃 | Forced logout: [이메일] [사유] | 계정 비활성화·권한 변경 등에 의한 강제 종료 시 | 시스템 |
| BOF Activity Log | 인증 | 로그인 실패 잠금 | Account locked: [이메일] [실패 횟수] | 로그인 실패 5회 시 자동 잠금 | 시스템 |
| BOF Activity Log + 고객 Audit Log | Break-Glass | Break-Glass 접근 시작 | Break-Glass access started: [Org명] [사유] | Break-Glass 접근 시작 시 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Break-Glass | Break-Glass 접근 중 행위 | 행위에 대해서는 기존에 노출해야 할 로그를 노출하고, 행위자 ID에 Backoffice ID 표시 | 접근 기간 내 모든 데이터 수정 행위 자동 기록 | 행위자 ID |
| BOF Activity Log + 고객 Audit Log | Break-Glass | Break-Glass 접근 종료 | Break-Glass access ended: [Org명] | 로그아웃 시 세션 종료 | 행위자 ID |
| BOF Activity Log | 앱 설정 | 앱 링크 수정 | App link updated: [앱명] [매뉴얼/CS] [URL] | 매뉴얼/CS 링크 수정 시 | 행위자 ID |
| BOF Audit Log | 계정 관리 | Backoffice 계정 생성 | Backoffice account created: [이름] [이메일] [역할] | Backoffice 계정 초대 시 | 행위자 ID |
| BOF Audit Log | 계정 관리 | Backoffice 역할 변경 | Backoffice role changed: [이름] [변경 전] → [변경 후] | 역할 변경 시 | 행위자 ID |
| BOF Audit Log | 계정 관리 | Backoffice 계정 비활성화 | Backoffice account deactivated: [이름] [이메일] | 비활성화 시 | 행위자 ID |
| BOF Audit Log | 계정 관리 | Backoffice 계정 재활성화 | Backoffice account activated: [이름] [이메일] | 재활성화 시 | 행위자 ID |
| BOF Audit Log | 계정 관리 | Backoffice 계정 잠금 해제 | Backoffice account unlocked: [이름] [이메일] | 잠금 해제 시 | 행위자 ID |
| BOF Activity Log | 공지사항 | 공지사항 작성 | Notice created: [제목] | 공지사항 작성 시 | 행위자 ID |
| BOF Activity Log | 공지사항 | 공지사항 노출 설정 변경 | Notice visibility changed: [제목] [노출/미노출] | 노출/미노출 토글 변경 시 | 행위자 ID |
| BOF Activity Log | 공지사항 | 공지사항 삭제 | Notice deleted: [제목] | 공지사항 삭제 시 (Admin 전용) | 행위자 ID |
| BOF Audit Log | Log | CSV 추출 | Backoffice Audit log exported: [추출 기간] | Backoffice Audit Log 추출 | 행위자 ID |
| BOF Activity Log | Log | CSV 추출 | Backoffice Activity log exported: [추출 기간] | Backoffice Activity Log 추출 | 행위자 ID |
| BOF Activity Log | Log | CSV 추출 | Activity log exported: [추출 기간] | Backoffice에서 고객사 Activity Log 추출 | 행위자 ID |
| BOF Activity Log | Log | CSV 추출 | Audit log exported: [추출 기간] | Backoffice에서 고객사 Audit Log 추출 | 행위자 ID |
| BOF Activity Log | Log | CSV 추출 | Audit Trail exported: [추출 기간] | Backoffice에서 고객사 Audit Trail 추출 | 행위자 ID |

*※ "BOF Activity Log + 고객 Audit Log"는 Backoffice의 행위로 고객 설정이 변경되는 경우, Backoffice Activity Log와 해당 고객사의 Org Audit Log에 동시 기록됨을 의미한다. 고객 Audit Log의 Author에는 Backoffice Admin 또는 Backoffice Operator로 기록한다 (AUD 3.2 참고).*

# 6. Break-Glass 접근 정책

## 6.1 목적

Backoffice Admin은 원칙적으로 고객 데이터에 직접 접근할 수 없다. 운영 목적의 긴급 접근이 필요한 경우, Break-Glass 절차를 통해서만 접근이 허용되며 모든 행위는 Backoffice Activity Log 및 해당 Org의 Audit Log에 동일하게 기록 된다.

Break-Glass 접근 정책은 2단계로 설계된다.

* **1차 정책 (v1 적용):** 접근 사유 입력 후 즉시 접근 허용. 접근 중 모든 행위는 Backoffice Activity Log 와 고객사 Org Audit Log에 자동 기록.
* **2차 정책 (추후 고려):** 고객사 Org Admin의 사전 승인이 필요한 플로우. 거부 즉시 차단, 미응답 10분 경과 시 직권 접근 허용. 고객사에 사후 통지 이메일 전송

## 6.2 정책

**[1차 정책 — v1 적용]**

* 접근 사유 입력 필수. 입력 없이 요청 진행 불가
* 사유 입력 후 즉시 접근 허용.
* Break-Glass 접근이 시작되면, 대상 Org 범위 내 모든 Workspace와 App에 접근 가능하다.
* 시간 제한은 없다.
* 세션은 로그아웃 시 종료된다.
* 접근 시 모든 행위 Backoffice Activity Log 및 해당 Org 감사 로그에 동일하게 자동 기록

**[2차 정책 — 추후 수준 논의 및 고려 필요]**

* 접근 사유 입력 필수
* 해당 Org의 Org Admin 전원에게 동시에 승인 요청 발송 (이메일 + 인앱 알림)
* 한 명이라도 승인하면 접근 허용

  + 한 명이라도 승인하지 않으면 접근 불가 처리?
* 미승인 접근/사후 통보: 아무도 승인하지 않고 10분 경과 시 Backoffice Admin 직권으로 접근 허용 → 감사 로그에 '승인 미확보 긴급 접근'으로 기록
* 접속 제한 정책 필요한가?

  + 한번 접근 시 NN분만 사용
  + 하루 접근 횟수 제한
* 접근 시 모든 행위 Backoffice Activity Log 및 해당 Org 감사 로그에 동일하게 자동 기록. 승인 여부(승인/거부/미응답) 별도 기록
* 접근 완료 후 해당 Org의 Org Admin 전원에게 사후 통지 이메일 발송

## 6.3 화면 흐름

|  |
| --- |
| 📋 Break-Glass 접근 흐름 (1차 — v1) |
| ① Backoffice Admin이 고객 데이터 접근 필요 판단 |
| ② 해당 Org 상세 화면 → [긴급 접근] 버튼 클릭 |
| ③ 사유 입력 모달 표시 → 접근 사유 입력 (필수). 입력 없이 진행 불가 |
| ④ [확인] 클릭 → 사유 저장 + 즉시 접근 허용 + 감사 로그 기록 시작 |
| ⑤ 접근 완료 → 로그아웃 시 세션 종료 |

|  |
| --- |
| 📋 Break-Glass 접근 흐름 (2차 — 추후 고려 및 수준 논의 필요) |
| ① Backoffice Admin이 고객 데이터 접근 필요 판단 |
| ② 해당 Org 상세 화면 → [긴급 접근 요청] 버튼 클릭 |
| ③ 접근 사유 입력 폼 → [요청 발송] 클릭 |
| → 해당 Org의 Org Admin 전원에게 승인 요청 메일 + 인앱 알림 발송 |
| ④-A 승인자 발생 → 즉시 접근 허용 (1시간) + 감사 로그 기록 |
| ④-B 10분 내 미응답 → Backoffice Admin 직권 접근 허용 (1시간) |
| → 감사 로그에 '승인 미확보 긴급 접근' 기록 |
| ⑤ 접근 완료 후 Org Admin 전원에게 사후 통지 이메일 발송 |

## 6.4 사후 통지 이메일 템플릿(추후 고려)

| 항목 | 내용 |
| --- | --- |
| 제목 | [iVigilance Square] Backoffice 관리자의 데이터 접근 완료 안내 - {Org명} |
| 수신 | 해당 Org의 Org Admin 전원 |

안녕하세요, 관리자님.
셀타스퀘어 Backoffice 관리자가 운영 목적으로 귀사의 데이터에 접근하였음을 안내드립니다.
■ 접근 정보
- 접근 일시: {YYYY-MM-DD HH:MM} (KST)
- 접근자: {Backoffice Admin 이름} ({이메일})
- 접근 Org: {Org명}
- 접근 사유: {입력된 사유}
모든 접근 행위는 감사 로그에 기록되어 있으며, Audit Log 메뉴에서 확인하실 수 있습니다.
문의사항이 있으시면 담당 세일즈에게 연락해 주시기 바랍니다.
감사합니다.
셀타스퀘어 드림

# 7. 사용량 제한 정책

**계정**

| 항목 | 한도 |
| --- | --- |
| Active 계정 / Org | 최대 200명 |
| Master Admin / Org | 최소 1명, 최대 1명 |
| Org Admin / Org | 최소 0명, 최대 3명 |
| App Admin / Workspace–App | 최소 0명, 최대 5명 |
| External User / Org | 최대 50명 (Active 계정 수 내 포함) |
| Viewer / Org | 최소 0명, 최대 5명 (Active 계정 수 미포함) |
| Workspace / Org | 기본 1개, 최대 100개 |
| App / Workspace | 최소 1개, 최대 10개 |

참고

* 계정 수 한도는 Active, Locked 계정 기준으로 계산한다.
* Inactive / Invitation  상태 계정은 한도 카운트에 포함되지 않는다.

**앱 사용량**

* 앱 사용량은 계약 시 설정
* 현재 기준으로 *Safety DB의 경우 앱 사용량(이니셜 케이스 수) 초과 시에도 서비스 사용 가능.*

# 8. Backoffice Admin

## 8.1 목적

Backoffice는 셀타스퀘어 내부 직원 여러 명이 접근하는 운영 도구다. 접근 권한을 역할로 구분하고 계정 생성·수정·비활성화를 관리한다.

## 8.2 Backoffice 계정의 역할 정의

| 역할 | 설명 및 접근 범위 |
| --- | --- |
| Backoffice Admin | 모든 기능 접근 가능. 계약 생성·수정·종료, Org 관리, 전체 사용자 관리, 앱 설정, Audit Log, Break-Glass 접근 포함. Backoffice 계정 관리(생성·수정·비활성화) 가능 |
| Backoffice Operator | 계약 정보 및 Org 정보: 조회만 가능 (생성·수정·종료·연장 불가). 사용자 계정 운영(비활성화, 잠금 해제, 비밀번호 재설정), 앱 설정, Audit Log, 공지사항은 가능. Break-Glass 접근 및 사용자 역할/권한 부여·변경은 불가. Backoffice 계정 관리 불가 |

*\* 역할 추가 필요 여부는 운영 규모에 따라 추후 검토. 현재는 Admin / Operator 2단계로 운영.*

**화면별 역할 권한 매트릭스**

| GNB 메뉴 | 기능 | Admin | Operator |
| --- | --- | --- | --- |
| 계약 관리 | 계약 목록 조회 | ✓ | ✓ |
| 계약 관리 | 계약 상세 조회 (정보/사용량/이력 탭) | ✓ | ✓ |
| 계약 관리 | 계약 생성 (NEW) | ✓ | ✗ |
| 계약 관리 | 계약 연장 (RENEW) | ✓ | ✗ |
| 계약 관리 | 계약 정정 (CORRECT) | ✓ | ✗ |
| 계약 관리 | 계약 취소 (CANCELLED) | ✓ | ✗ |
| 계약 관리 | 계약 종료 / 복원 | ✓ | ✗ |
| Org 관리 | Org 목록 조회 | ✓ | ✓ |
| Org 관리 | Org 생성 | ✓ | ✗ |
| Org 관리 | Org 상세 조회 | ✓ | ✓ |
| Org 관리 | Org 정보 수정 (이름) | ✓ | ✗ |
| Org 관리 | Workspace App 활성화 설정 | ✓ | ✗ |
| Org 관리 | Workspace 폐쇄 / 완전 폐쇄 | ✓ | ✗ |
| Org 관리 | Workspace 상세 조회 | ✓ | ✓ |
| Org 관리 | Workspace 정보 수정 (이름) | ✓ | ✗ |
| Org 관리 | Master Admin 초대 | ✓ | ✗ |
| 사용자 관리 | 사용자 목록 조회 | ✓ | ✓ |
| 사용자 관리 | 사용자 정보 수정 (역할/권한) | ✓ | ✗ |
| 사용자 관리 | 계정 비활성화 / 재활성화 | ✓ | ✓ |
| 사용자 관리 | 비밀번호 재설정 메일 발송 | ✓ | ✓ |
| 앱 설정 | 링크 관리 (매뉴얼/CS) | ✓ | ✓ |
| 앱 설정 | 버전 정보 조회 | ✓ | ✓ |
| Log | 고객사 로그 조회 (Audit Trail·Activity Log·Audit Log) | ✓ | ✓ |
| Log | Backoffice Activity Log 조회 | ✓ | ✓ |
| Admin | Backoffice Audit Log 조회 | ✓ | ✗ |
| Org 관리 | 긴급 접근 | ✓ | ✗ |
| 공지사항 | 작성 / 목록 조회 / 노출 설정 | ✓ | ✓ |
| 공지사항 | 삭제 | ✓ | ✗ |
| Admin | Backoffice 계정 생성/수정/비활성화 | ✓ | ✗ |
| Admin | Backoffice 계정 목록 조회 | ✓ | ✗ (메뉴 미노출) |

*※ Operator에게 권한 없는 기능의 버튼/메뉴는 UI에서 미노출 처리한다. API 레벨에서도 차단한다.*

## 8.3 Backoffice 계정 정책

•  Backoffice 계정 ID는 이메일 주소 사용. 생성 후 변경 불가

•  계정 생성은 Backoffice Admin만 가능

•  비밀번호 생성 규칙은 [Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) 와 동일하게 적용. 복잡도만 동일하게 적용하고, 변경주기나 재설정은 미지원

•  MFA: Backoffice 내의 MFA는 추후 적용

•  계정 삭제 미지원. 비활성화로 대체

•  Backoffice Admin 계정은 최소 1명 이상 Active 상태 유지 필요 (전원 비활성화 불가)

## 8.4 Backoffice 사용자 관리 화면

### 기능

* Backoffice 계정 목록 조회: 이름, 이메일, 역할, 계정 상태, 최종 로그인 일시 표시
* 계정 생성: 이메일, 이름, 역할(Admin/Operator) 입력 후 초대 메일 발송
* 계정 정보 수정: 이름, 역할 수정 가능. 이메일 수정 불가
* 계정 비활성화 / 활성화
* 참고: 백오피스의 계정 초대 및 생성, 정보 수정, 비활성화 등의 동작은 계정 정책과 동일하게 처리 한다.

  + 단 마스터 계정 초대는 동작은 동일하나 메일 정보는 다르게 한다.

### 화면 흐름

|  |
| --- |
| 📋 Backoffice 계정 관리 흐름 |
| [계정 목록 조회] |
| ① Backoffice GNB [Admin] 클릭 → Backoffice 사용자 목록 화면 |
| ② 상태 필터(Active/Inactive/Locked/Invitation) 또는 검색으로 필터링 |
|  |
| [계정 생성] |
| ① [+ 계정 추가] 버튼 클릭 → 생성 폼 (이메일, 이름, 역할 선택) |
| ② [초대 발송] 클릭 → 초대 메일 발송 (계정 상태: Invitation) |
|  |
| [역할 변경] |
| ① 계정 행 클릭 → 상세 화면 → [수정] → 역할 변경 후 [저장] |
| → 변경 즉시 적용. 해당 계정이 접근 불가 메뉴에 있을 경우 홈으로 이동 처리 |
|  |
| [비활성화] |
| ① 계정 상세 → [비활성화] 클릭 → 확인 모달 → [확인] |
| → 마지막 Admin 계정인 경우 비활성화 버튼 disabled 처리 |

## 8.5 Backoffice 로그인

•  로그인 URL은 iVigilance Square와 별도 도메인으로 분리

•  로그인 방식: 이메일 + 비밀번호 (Account 정책 문서 7.1 LGN01~07 동일 적용)

•  MFA: Backoffice 단위로 활성화 시 로그인 후 이메일 6자리 코드 인증

•  로그인 실패 5회 시 계정 자동 Locked. Backoffice Admin이 해제 가능

• Backoffice 로그인은 Org 상태와 무관하다. Org가 Pre-Active 상태인 기간에도 Backoffice Admin/Operator는 로그인하여 설정 작업을 수행할 수 있다.

• iVigilance Square(고객 측) 로그인은 Org Active 상태에서만 허용되며, Backoffice와 별도로 제어된다.

## 9. 공지사항 관리

### 9.1 목적

Backoffice Admin / Operator가 플랫폼 공지사항을 작성·관리하고, 고객사 사용자에게 노출 여부를 제어할 수 있는 기능을 제공한다.

### 9.2 권한

| 기능 | Backoffice Admin | Backoffice Operator |
| --- | --- | --- |
| 공지사항 작성 | ✓ | ✓ |
| 공지사항 목록 조회 | ✓ | ✓ |
| 노출/미노출 설정 | ✓ | ✓ |
| 공지사항 삭제 | ✓ | ✗ |

### 9.3 정책

* 공지사항 목록은 최신 작성순(내림차순) 정렬. 백오피스 화면에 최대 10개 노출
* 노출/미노출 설정은 토글 방식으로 작성이 완료 된 글에 한하여 설정 가능하고, 토글 변경에 따른 노출은 즉시 반영
* 공지사항 작성 시 파일 첨부 지원, 이미지 첨부 시 작성 화면에 노출, 파일 첨부 시 본문에 파일명 노출
* 삭제는 Backoffice Admin 전용. Operator에게는 삭제 버튼 미노출 처리
* 삭제된 공지사항은 복구 불가

### 9.4 화면 흐름

|  |
| --- |
| 📋 공지사항 작성 흐름 |
| ① GNB [공지사항 작성] 클릭 → 공지사항 목록 화면 |
| ② [+ 공지사항 작성] 버튼 클릭 → 작성 폼 (제목, 내용 입력) |
| ③ [저장] 클릭 → 목록 최상단에 추가 (기본 노출 상태) |

|  |
| --- |
| 📋 노출/미노출 설정 흐름 |
| ① 공지사항 목록 화면 → 노출할 공지사항 클릭 |
| ② 공지사항 본문에 있는 토글 전환 → 즉시 반영 (별도 저장 버튼 없음) |

|  |
| --- |
| 📋 공지사항 삭제 흐름 |
| ① 공지사항 목록 화면 → 대상 공지사항 행 클릭 또는 [삭제] 버튼 클릭 (Admin 전용 노출) |
| ② 확인 모달: '삭제된 공지사항은 복구되지 않습니다. 계속하시겠습니까?' |
| ③ [확인] 클릭 → 공지사항 삭제 완료 → 목록에서 제거 |

# 10. 개발 요구사항

## 10.1 계약 관리

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-C-01 | 계약 생성: 기존 Org를 선택한 후 계약 기간, 앱 목록, 앱별 사용량, 추가 Workspace 여부 및 수량, 계약 금액, 세일즈 담당자 이름/이메일, 원본 계약서 링크 입력 후 저장 시 Contract 생성. 추가 Workspace는 해당 Contract의 계약 기간을 따르며 별도 기간 입력 없음.    Org가 존재하지 않는 경우 먼저 Org 관리에서 생성 필요(BOF-T-01 참고). 계약 생성 완료 시 계약 체결 안내 이메일 발송(1.1.8.2 참고). 계약 생성 시 action\_type = NEW, previous\_contract\_id = NULL. 시작일이 현재/과거이면 ACTIVE, 미래이면 SCHEDULED 상태로 생성 | 필수 |
| BOF-C-02 | 계약 생성 시 동일 Org에 대해 현재 적용 중인 계약 존재 여부를 확인하고 경고를 표시한다. 동일 Org 내 동일 앱에 대해 유효기간이 겹치는 계약은 저장 시점에 차단한다. 같은 버전 체인 내부의 후속 버전 전이는 예외 | 필수 |
| BOF-C-03 | 계약 목록 조회: 고객사명·Org 상태·계약 기간 기준 필터링 및 검색. 비활성화된 계약 포함하여 전체 조회 가능 | 필수 |
| BOF-C-04 | 계약 단건 조회: 계약 기본 정보 / 앱별 사용량(계약값 vs 실제값 비교, 초과 시 시각적 강조) / 계약 이력 | 필수 |
| BOF-C-05 | 계약 이력 탭: NEW(신규)·RENEW(연장)·CORRECT(정정) 분류별 버전 이력 표시. 표시 컬럼: 분류(action\_type) / 버전 생성 일시 / 생성자 / 상태. 값 없는 경우 '-' 표시. 상세 변경 내용은 Audit Log에서 확인 | 필수 |
| BOF-C-06 | 계약 정정(CORRECT): 종이 계약서와 시스템 입력값 불일치 시 정정 용도.    수정 불가(조회 전용): 고객사명, 계약 앱 목록, Workspace/App 구성, 계약 시작일, 종료일.  수정 가능(기존값 프리필): 계약 금액, 앱별 사용량, 세일즈 담당자 이름/이메일, 원본 계약서 링크, 메모. 정정 사유 입력 필수.    저장 시 새 Contract 버전 생성(action\_type = CORRECT, previous\_contract\_id = 기존 계약 ID). 기존 버전은 SUPERSEDED 처리. 변경 전/후 값 감사 로그 기록 | 필수 |
| BOF-C-07 | 계약 날짜 유효성 검증: 시작일 ≤ 종료일. 계약 생성/정정/연장 시 저장 전 검증. 추가 검증: 동일 Org 내 동일 앱에 대해 서로 다른 계약 계보에서 유효기간이 겹치는 경우 저장 차단. 위반 시 저장 불가 + 인라인 오류 메시지 | 필수 |
| BOF-C-09 | 계약 종료(Terminate): 종료 즉시 고객사 접근 차단. 데이터 보존 기간(60일) 시작. 계약 상세에 삭제 예정일 표시. 모든 종료(수동/자동) 시 감사 로그 기록 | 필수 |
| BOF-C-10 | 계약 복원(Terminated → Active): 2가지 시나리오    Backoffice Admin이 수동으로 처리. 종료 후 60일 내에만 가능. 사유 입력 필수. 복원 사후 통지 이메일 발송 (BOF-C-16 참고)    계약 연장 처리: 계약 종료 후 60일 이내 고객이 재계약 요청하는 경우, 계약을 복원하고 계약 연장 처리 가능. 계약 연장 처리 시 완료 후 계약 체결 안내 이메일 발송 (BOF-C-15 참고)    아무것도 하지 않는 경우: 60일 경과 후 버튼 미노출 + API 차단 | 필수 |
| BOF-C-12 | 계약 연장(RENEW): 앱 구성은 유지하고 기간을 연장하는 신규 Contract 버전 생성. 계약 금액·앱별 사용량, 세일즈 담당자, 원본 계약서 링크는 신규 입력(계약 금액, 앱별 사용량, 세일즈 담당자는 기존값을 조회 전용으로 표시)    action\_type = RENEW, previous\_contract\_id = 기존 계약 ID. 시작일/종료일 관계에 따라 3가지 케이스(만료 후 연속 / 겹치지만 미발효 / 겹치고 이미 발효) 처리. 직전 계약 버전은 상태 전이 규칙에 따라 SUPERSEDED 또는 EXPIRED 처리. 계약 이력 탭에서 읽기 전용 조회 가능. 앱 구성 변경이 포함되면 RENEW가 아닌 NEW로 처리.    계약 연장 완료 시 계약 체결 안내 이메일 발송 (1.1.8.2 참고)    Org 상태 Active 유지. 날짜 유효성 검증 동일 적용. 감사 로그 기록    새 Contract version 발효 시점부터 해당 version의 사용량 기준 적용. | 필수 |
| BOF-C-13 | 계약 종료 사전 알림(1.1.8.1 참고): D-90/30/7/1일에 Master Admin , 세일즈 담당자, Backoffice Admin/Operator 전체 이메일 자동 발송. 발송 실패 시 재시도 처리(1시간 간격, 최대 3회). 최종 실패 시 발송 이력 감사 로그 기록 | 필수 |
| BOF-C-14 | 추가 Workspace는 NEW Contract에 포함된 경우에만 생성 가능하며, 생성된 Workspace의 접근 가능한 기준 정보(Default Value: 스터디 1개 선택, 해당 스터디에 속한 프로덕트 복수 선택 가능) 범위 설정 및 저장을 지원한다. 상세 설정 방식은 추후 확정 | 필수 |
| BOF-C-15 | 계약 체결 안내 이메일: 신규 계약 생성(NEW)·계약 연장(RENEW)·재계약 완료 시 Master Admin, 세일즈 담당자, Backoffice Admin/Operator에게 자동 발송. 이메일 본문에 변경된 계약 내용(기간, 앱 구성 등) 포함. 발송 실패 시 1.1.8.1과 동일한 재시도 처리 적용 | 필수 |
| BOF-C-16 | 복원 사후 통지 이메일(1.1.8.3 참고): Terminated → Active 단순 복원 완료 시 Master Admin, 세일즈 담당자, Backoffice Admin/Operator에게 자동 발송. 발송 실패 시 1.1.8.1과 동일한 재시도 처리 적용 | 필수 |
| BOF-C-17 | Contract 상태 자동 전이: SCHEDULED→ACTIVE(시작일 도래), ACTIVE→EXPIRED(종료일 도래) 전이는 배치/스케줄러가 자동 처리. SCHEDULED→ACTIVE 전이 시 같은 버전 체인의 기존 ACTIVE가 대체 관계이면 SUPERSEDED 처리. 만료 후 연속 RENEW는 기존 계약 EXPIRED 처리. 동일 배치 내 후속 처리로 Org 상태 전환도 수행: SCHEDULED→ACTIVE 시 Org Pre-Active→Active, 모든 ACTIVE가 EXPIRED 시 SCHEDULED 유무에 따라 Org Pre-Active 또는 Terminated 전환 | 필수 |
| BOF-C-18 | 미래 계약 취소: SCHEDULED 상태 계약의 취소 기능. 취소 시 CANCELLED 상태로 전환. 효력 미발생 이력으로 보존. 취소 사유 입력 필수. 감사 로그 기록 | 필수 |
| BOF-C-19 | 액션 유형별 DTO 분리: NEW/RENEW/CORRECT 별로 입력 가능 필드를 제한하는 DTO 분리. 서버에서 의미 검증 추가 수행 (RENEW인데 앱 구성 변경 포함 → 거절, CORRECT인데 신규 수준 변경 → 거절). 세부 필드 매트릭스는 별도 정의(11.2 참고) | 필수 |
| BOF-C-20 | 버전 계보 검증: action\_type = NEW이면서 previous\_contract\_id ≠ NULL이면 저장 불가. action\_type = RENEW 또는 CORRECT이면서 previous\_contract\_id = NULL이면 저장 불가 | 필수 |
| BOF-C-21 | 고객 로그인 게이트: iVigilance Square 로그인 시 Org 상태가 Active인지 검증. Pre-Active / Terminated 상태이면 로그인 차단 + 상태별 안내 메시지 표시. Backoffice 로그인에는 적용하지 않음. 안내 메시지: Pre-Active="서비스 준비 중입니다. 계약 시작일 이후 로그인 가능합니다." / Terminated="계약이 종료되었습니다. 재계약이 필요한 경우 담당자에게 문의하세요." | 필수 |

## 10.2 Org 관리

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-T-01 | Org 생성 기능: Backoffice Admin이 Org 관리 화면에서 Org를 생성한다. 고객사명 입력 → Org 이름·Main Workspace 이름 자동완성(각각 수정 가능) → 저장 시 Org 및 Main Workspace 생성. Org 이름은 시스템 전체에서 유니크해야 한다. 중복 시 저장 불가 + 인라인 오류 메시지 표시. (멀티 Org 도입 시 재정의 필요). 계약 생성은 반드시 기존 Org를 선택하여 진행하며, 계약 생성 화면에서 Org를 새로 만들 수 없다 | 필수 |
| BOF-T-02 | Workspace별 App 활성화/비활성화 설정: Backoffice Admin 전용. 계약에서 허용된 앱 범위 내에서만 설정 가능 | 필수 |
| BOF-T-03 | 추가 Workspace는 NEW Contract 생성(1.1.16) 시 자동 생성된다. 별도 생성 화면은 제공하지 않는다. 생성 이후 해당 Workspace의 기준 정보 접근 범위(스터디 1개 단위로 설정하고, 해당 스터디에 속한 프로덕트는 복수 선택 가능)는 고객사 Admin이 직접 설정 가능해야 한다. Workspace 이름은 동일 Org 내 유니크 강제 | 필수 |
| BOF-T-04 | Org 목록 조회: 고객사명·Org 상태·계약 기간 기준 검색 및 필터링 | 필수 |
| BOF-T-05 | Org 단건 조회: 기본 정보 / Workspace / 사용자 / 계약 정보 탭 구분 표시 | 필수 |
| BOF-T-06 | Org 정보 수정: 이름(최대 20자, 공백 포함) 등 기본 정보 수정 가능 | 필수 |
| BOF-T-07 | Workspace 폐쇄:  케이스 A-1(Org 전체 종료) Org Terminated 시 하위 Workspace 일괄 자동 폐쇄.  케이스 A-2(추가 WS 소속 Contract 종료) 추가 Workspace를 포함한 Contract가 EXPIRED되고 후속 승계가 없으면 해당 Workspace만 자동 폐쇄. Workspace는 소속 Contract 기간 만료 기준 적용    케이스 B(고객 요청에 따른 중간 폐쇄): Backoffice Admin이 세일즈 담당자로부터 이메일 요청 수신 후 수동 처리.    Main Workspace는 Org 종료 시에만 처리 | 필수 |
| BOF-T-08 | Org 상태 전환(Terminated): 처리 즉시 하위 모든 계정 비활성화 및 활성 세션 강제 종료. Terminated(보존 기간 만료) Org는 Backoffice에서도 데이터 조회 불가 처리 | 필수 |
| BOF-T-09 | Master Admin 계정 생성 및 초대 메일 발송 기능 (Backoffice Admin 전용). 초대 링크 유효기간 7일 | 필수 |
| BOF-T-10 | Master Admin 초대 재발송 기능: 기존 링크 즉시 파기 후 신규 링크 발송. Backoffice Admin 전용 | 필수 |
| BOF-T-11 | Org 내 사용자 목록 조회 기능 제공 | 필수 |

## 10.3 전체 사용자 관리

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-U-01 | 전체 사용자 목록 조회: 이름·이메일·Org·Org 역할·App 역할·계정 상태 기반 검색 및 필터링 | 필수 |
| BOF-U-02 | 사용자 정보 수정(부여 포함): 이름, Org 역할, Workspace 할당/해제, 앱 접근 권한 및 App 역할(App Admin / App User) 부여/수정. Backoffice Admin 전용 (Operator 수행 불가). 이메일 수정 불가. 앱 접근 권한 부여 시 해당 Workspace에서 해당 App이 활성화되어 있어야 함(비활성 App은 선택 불가 처리). | 필수 |
| BOF-U-03 | 역할 변경은 변경 즉시 적용. 대상 사용자의 활성 세션에 즉시 반영. 권한 하향 시 케이스별 처리:  ① Org Admin → Org User 강등 시 전용 화면 접속 중이면 안내 팝업("역할이 변경되어 해당 화면에 접근할 수 없습니다. 홈으로 이동합니다.") 후 홈 이동  ② App Admin → App User 변경 시 어드민 화면 접속 중이면 안내 팝업("역할이 변경되어 관리자 화면에 접근할 수 없습니다. 홈으로 이동합니다.") 후 홈 이동  ③ 그 외 화면(앱 내 작업 중 등)은 별도 안내 없이 처리" | 필수 |
| BOF-U-04 | 비밀번호 재설정 메일 발송 기능 제공. 직접 비밀번호 입력 UI 미제공 | 필수 |
| BOF-U-05 | 계정 비활성화: 처리 즉시 활성 세션 강제 종료. Master Admin은 계약 종료 후에만 처리 가능 (UI disabled + API 차단) | 필수 |
| BOF-U-06 | 계정 재활성화 기능 제공 | 필수 |
| BOF-U-07 | 계정 잠금 해제: Backoffice Admin 및 Operator는 Master Admin 포함 전체 계정 잠금 해제 가능 | 필수 |
| BOF-U-08 | 계정 삭제 기능 미제공, 비활성화로 대체 (UI 및 API 수준 삭제 차단) | 필수 |

## 10.4 앱 설정

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-A-01 | 앱별 매뉴얼 링크 URL 등록 및 수정 기능. 변경 즉시 앱 내 반영 | 필수 |
| BOF-A-02 | 앱별 CS 링크 URL 등록 및 수정 기능. 변경 즉시 앱 내 반영 | 필수 |
| BOF-A-03 | 앱별 현재 버전 정보 조회 기능 | 필수 |

## 10.5 Log 조회

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-AL-01 | 고객사 로그 통합 조회 화면 제공 (GNB [Log] → 고객사 로그). Admin 및 Operator 접근 가능. 고객사의 Audit Trail·Activity Log·Audit Log를 통합 조회. 진입 시 결과 미표시 → 고객사(Org)와 로그 종류 선택 후 [검색]으로 조회 | 필수 |
| BOF-AL-02 | 고객사 로그 필터: 날짜 범위 / 고객사명(Org) / Workspace / App / 로그 종류(Audit Trail, Activity Log, Audit Log) / 카테고리 / 행위자 / 대상 계정. 화면 기본 최근 2주, 최대 1년. 최대 10만 건(페이지당 30건) | 필수 |
| BOF-AL-03 | 로그 행 클릭 시 상세 정보 모달 또는 사이드 패널 표시. 변경 전/후 값 포함. 전체 로그 공통 | 필수 |
| BOF-AL-04 | CSV Export: 조회 기간 기준 최대 1년치 전체 건수 다운로드 (화면 10만 건 제한 적용). 기간 미설정 시 30일치. 전체 로그 공통 | 필수 |
| BOF-AL-05 | 5.5 기록 항목 전체 정의에 명시된 모든 이벤트 기록. Append-only 구조, 수정/삭제 불가 | 필수 |
| BOF-AL-06 | 모든 계약 알림 발송(종료 사전 알림, 계약 체결 안내, 복원 사후 통지) 성공/실패 여부 감사 로그 기록 | 필수 |
| BOF-AL-07 | Backoffice Activity Log 조회 화면 제공 (GNB [Log] → Backoffice Activity Log). Admin 및 Operator 접근 가능. 필터: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 | 필수 |
| BOF-AL-08 | Backoffice Audit Log 조회 화면 제공 (GNB [Admin] → Audit Log). Admin 전용, Operator 접근 불가. 필터: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 | 필수 |

## 10.6 Break-Glass

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-BG-01 | Backoffice Admin의 고객 데이터 직접 접근 차단. 운영 목적 접근 시 Break-Glass 승인 플로우 적용 -> 1차: 사유 입력 후 즉시 접근 허용. 시간 제한 없음. 로그아웃 시 세션 종료. | 필수 |
| BOF-BG-02 | 접근 사유 입력 필수. 입력 없이 요청 발송 불가 | 필수 |
| BOF-BG-03 | 해당 Org의 Org Admin전원에게 동시 승인 요청 발송 (이메일 + 인앱 알림) | 추후 고려 |
| BOF-BG-04 | 한 명이라도 승인 시 즉시 접근 허용. | 추후 고려 |
| BOF-BG-05 | 10분 내 미응답 시 Backoffice Admin 직권 접근 허용. 감사 로그에 '승인 미확보 긴급 접근' 기록 | 추후 고려 |
| BOF-BG-06 | 접근 시 모든 행위 감사 로그 자동 기록. | 필수 |
| BOF-BG-07 | 접근 완료 후 해당 Org의 Org Admin 전원에게 사후 통지 이메일 발송 | 추후 고려 |

## 10.7 사용량 제한

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-LMT-01 | Org 내 Active 상태 계정 수 200명 한도 초과 시 계정 생성/초대 차단. | 필수 |
| BOF-LMT-02 | Org Admin 최대 3명 Active 계정 한도 초과 시 추가 불가 처리 | 필수 |
| BOF-LMT-03 | Workspace 내 App당 App Admin 최대 5명 Active 계정 한도 초과 시 추가 불가 처리 | 필수 |
| BOF-LMT-06 | 사용량 80% 이상 도달 시 Backoffice 화면에서 경고 표시 | 고도화 |

## 10.8 Backoffice Admin

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-BAC-01 | Backoffice 계정 역할 2종 관리: Admin(전체 권한) / Operator(계약·Org 조회 전용. 사용자 계정 운영·앱 설정·Audit Log·공지사항 가능. Break-Glass 및 사용자 역할/권한 부여 불가). 역할별 메뉴 접근 제어. Backoffice 계정 관리는 Admin 전용 | 필수 |
| BOF-BAC-02 | Backoffice 계정 목록 조회: 이름, 이메일, 역할, 상태, 최종 로그인 일시 표시. Backoffice Admin 전용 | 필수 |
| BOF-BAC-03 | Backoffice 계정 생성: 이메일 중복 검증 후 초대 메일 발송. Backoffice Admin만 가능 | 필수 |
| BOF-BAC-04 | Backoffice 계정 역할 변경 즉시 적용. 접근 불가 메뉴 접속 중일 경우 홈으로 이동 처리 | 필수 |
| BOF-BAC-05 | Backoffice 계정 비활성화 기능 제공. 마지막 Backoffice Admin 계정은 비활성화 불가 (UI disabled + API 차단) | 필수 |
| BOF-BAC-06 | Backoffice 계정 잠금 해제: Backoffice Admin이 처리 | 필수 |
| BOF-BAC-07 | Backoffice 계정 삭제 미제공, 비활성화로 대체 | 필수 |
| BOF-BAC-08 | Backoffice MFA 활성화/비활성화 설정: Backoffice Admin 전용. 변경 시 다음 로그인 부터 적용, 변경 시 Audit Log 기록 | 추후 고려 |

### 10.9 공지사항 관리

| ID | 요구사항 | 우선순위 |
| --- | --- | --- |
| BOF-NTC-01 | 공지사항 작성 기능 제공. 제목·내용 입력 후 저장. , 파일 첨부 지원, Backoffice Admin / Operator 모두 가능 | 필수 |
| BOF-NTC-02 | 공지사항 목록 조회: 최신 작성순 정렬, 최대 10개 노출 | 필수 |
| BOF-NTC-03 | 공지사항 노출/미노출 토글 설정. 변경 즉시 반영 | 필수 |
| BOF-NTC-04 | 공지사항 삭제: Backoffice Admin 전용. Operator에게는 삭제 버튼 미노출 처리 | 필수 |

# 11. 1 참고: 앱별 사용량 관련 정책

App 별로는 사용량이 있으며, 해당 사용량은 계약시 정의 되거나 고객이 계약 후 사용량을 구매하여 사용한다.

### Safety DB

* 계약 기간 내 이니셜 케이스 등록 가능 수

  + Safety DB 이니셜 케이스 사용량은 1년 단위 집계, 매년 초기화 후 재카운트.

    - ex. 2년 계약, 이니셜 케이스 200으로 계약 시, 첫해 1년에 150 케이스 등록 한 경우, 2년차가 되면 다시 200으로 초기화 되어 재 카운트
* *사용량은 제약으로 동작하지 않으며, 초과해도 서비스 사용이 가능하다. 단, 초과 여부는 계약 상세 화면(앱 사용량 탭)에서 항상 확인 가능하도록 표시한다.*

\* ex. 2년 계약, 이니셜 케이스 200으로 계약 시, 첫해에 250개 이니셜 케이스 등록 가능

\* 50개에 대해서는 1년 후에 50개 비용 따로 받을 예정

\* 그래서 50개가 초과되었다는 것은 알 수 있어야 함.

### Tabulator

* 계약 기간 내 변환 할 수 있는 크레딧

  + 따로 제약은 없고 고객이 필요할 때 마다 충전
  + 대신 충전건에 대해서는 계약 기간 동안은 계속 유지
  + 계약이 종료되고 나서 환불은 불가
* 해당 방식에 대해서 플랫픔으로 들어와서 앱으로 변할때는 다시 재논의 필요

  + 현재는 충전은 세일즈 통해서 비용 납부하면 내부에서 백오피스 통해서 크레딧 넣어 주고 있음.

### Litus

* 사용 가능한 인터벌에 따른 비용 납입

\* 계약 기간 내 사용 가능한 텀 그룹 수

* 현재는 설정하고 나서의 비용은 일시불로 받고 있음
* 해당 방식에 대해서 플랫픔으로 들어와서 앱으로 변할때는 다시 재논의 필요

### 기타

* Sync는 대용량, 벌크 변환이고 Safety DB에 붙어서 동작하기 때문에 Sync만을 위한 특별한 사용량 정책은 없을것으로 판단되나 이 부분은 실제 기획시 재확인 필요.

# 11.2 고도화 요구사항

## **11.1 External User 관련**

* BOF-U-02: 사용자 정보 수정 시 External User 역할 변경 시 Safety DB 외 앱 접근 권한 자동 해제 (BOF-U-02 이월)
* BOF-LMT-01: External User 50명 상한 별도 차단 (BOF-LMT-01 이월)
* BOF-LMT-05: External User의 앱 접근은 Safety DB로 한정. 타 앱 접근 권한 부여 불가 처리 (BOF-LMT-05 이월)

## 11.2 Viewer 관련

* BOF-LMT-04: Viewer 계정은 전체 Active 계정 수에 포함하지 않으며, 최대 5명까지 생성 가능 (BOF-LMT-04 이월)

## 11.3 기타 고려가 필요한 부분

* Org 생성 후 계약 미연결 시 방치 정리 정책

  + Org만 생성하고 계약을 연결하지 않은 채 방치된 경우의 정리 정책 정의 필요 (자동 삭제 기간, 알림 여부 등). 계약 연결 전 Org는 상태 미부여 상태이며, 최초 Contract 생성 시 Pre-Active가 부여된다
* 멀티테넌트 도입 시 특정 Org 수동 종료 정책

  + 현재 1 고객사 = 1 Org 구조에서는 계약 종료로 Terminated 처리. 멀티테넌트 도입 이후 특정 Org만 수동으로 Terminated 전환하는 정책 및 화면 흐름 별도 정의 필요. 2.8 화면 흐름(추후 반영) 참고

### 확정된 이전 미결 항목

|  |  |  |  |
| --- | --- | --- | --- |
| No | 항목 | 확정 내용 | 확정일 |
| — | 추가 Workspace Default Value 설정 방식 | 스터디 1개 단위 설정, 프로덕트 복수 선택. BOF-C-14, BOF-T-03에 반영 완료 | 2026-03 |
| — | Backoffice Audit Log 보존 기간 | 계속 보관 | 2026-03 |
| — | 연장/정정/신규 분류 기준 상세 | 디시전 3.3 기준 반영. 1.1.11에 경계 케이스 테이블 추가 | 2026-03-26 |
| — | 계약 목록/상세/이력 화면 상태 구분 UI | 상태 배지 + 필터. 1.1.10에 규칙 추가. 색상은 디자인 시스템 | 2026-03-26 |
| — | ACTIVE 계약의 중도 해지/취소 정책 | Org Terminated 수동 처리. Contract 상태 변경 없음. 1.1.14에 반영 | 2026-03-26 |
| — | 고객 로그인 차단 안내 메시지 | 상태별 3종 확정. BOF-C-21에 반영 | 2026-03-26 |
| — | Contract EXPIRED → Org 전환 배치 | BOF-C-17과 동일 배치 내 후속 처리 | 2026-03-26 |
|  | Workspace에 별도 계약 기간이 있는지 여부 | 독립 기간 없음. Workspace는 소속 Contract의 계약 기간을 따른다. Workspace별 독립 시작일/종료일 미제공. 구성 변경 시 NEW Contract로 처리 (App 계약기간 원칙과 동일) | 2026-03-27 |
