# Multi-Org 구조 및 계정 권한 정책

관련 이슈:

[IS-1261](https://selta.atlassian.net/browse/IS-1261?src=confmacro)

> **본 문서는 Multi-Org 구조의 Source of Truth다.**

> 계정 운영 상세 → / Backoffice 운영 상세 → BOF / 감사 로그 수집·조회 상세 →

> 하위 문서는 본 문서의 원칙을 따른다. 충돌 시 구조·상태·경계는 MT 우선, 운영 흐름·화면은 해당 하위 문서 우선.

---

## 변경사항

|  |  |  |  |
| --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 |
| 김병환 | 26.04.29 | 지라 이슈에 있는 업무 우선순위와 동기화  Org user 개념 반영   * 7.1 역할 정의에 org user 추가하고 나머지 정리    + external user는 신분에 가까워서 역할 정의에서는 제외하고 따로 작성   + viewer가 org 레벨에 가까워서 app-> org로 수정 * 권한 매트릭스 org 레벨에서 app admin과 app user를 org user로 통합 |  |
| 김병환 | 26.04.29 | 권한매트릭에서 사용자 잠금해제 할 수 있다고 된 부분 삭제   * 잠금해제는 본인만이 비밀번해 재설정으로 가능하여 해당 기능은 기획에서 제거 했기 때문에 매트릭스에서도 삭제 |  |
| 김병환 | 26.04.20 | External User, Viewer 관련 사항 고도화에 하게 되어 관련 내용 수정   * 규칙 부분은 수정하지 않고, 실제 구현 및 관련 설명에서 수정  * 10.2, 10.4, 12 미결 부분 수정, 권한 매트릭스에서 External User, Viewer 제거 * 11 고도화 섹션 추가하여 관련 내용 작성하고 미결 사항과 통합 정리 |  |
| 김병환 | 26.04.20 | 계정 한도 계산 부분 반영 - 7.2 |  |
| 김병환 | 26.04.17 | 멀티 Org 관련 내용 수정 - 10.4 관련 내용 |  |
| 김병환 | 26.04.14 | 일정 구분 추가 |  |
| 김병환 | 26.04.13 | Tenant → Org로 수정 |  |
| 김병환 | 26.04.08 | Tenant Admin -> Org Admin으로 수정   1. 고객 UI에서는 Tenant 대신 Org, Organization 으로 수정 |  |
| 김병환 | 26.03.31 | 10.4 Cross-tenant 초대 도입 시 부여 가능한 역할에 Viewer 추가. |  |
| 김병환 | 26.03.30 | 권한 매트릭스 추가 |  |
| 김병환 | 26.03.30 | Master Admin/Tenant Admin 권한 구조 수정 원복: Master Admin/Tenant Admin도 명시적으로 권한을 받아야 워크스페이스/앱에 접근 가능    2.3, 4.1, 4.2, 5.3, 7.1, 10.0    계정 한도 계산 방식 변경 |  |
| 김병환 | 26.03.29 | Master Admin/Tenant Admin 권한 구조 수정  2.3, 4.1, 4.2, 5.3, 7.1, 10.5 수정    Suspended 상태 제거, Pre-Active 상태 추가 및 관련 동작 수정  1, 10.1, 9 ONB-03/04, 6.1, 6.2, 6.3, 6, 3.2 |  |
| 김병환 | 26.03.23 | 문서 재구조화. MT 범위를 구조·상태·경계·원칙으로 재정의. 계정 운영 상세 ACC 위임, Backoffice 운영 상세 BOF 위임, 감사 로그 화면·조회 상세 AUD 위임. 리뷰 댓글 반영 |  |
| 김병환 | 26.03.19 | 구조 리팩토링: 0 개요 신설, 4(역할)→2·7(관계)→3 이동, 5+6 통합, UI 화면 흐름 최소화(BOF/ACC 참조), 5.1/10 중복 수치 상호 참조 정리, 인라인 미결 항목 11로 통합 |  |
| 김병환 | 26.03.17 | 백오피스 문서 교차검토 반영 및 전면 보완. ISO-04→ISO-05 ID 분리, 감사 로그 3분리 구조 도입, App Admin 5명 확정, D+60 삭제 처리, Break-Glass 정책 정비 외 다수 |  |
| 김병환 | 26.03.12 | 1.1 상세화, 3.2 상세화, 리뷰 의견 추가, ISO-04 추가 |  |
| 김병환 | 26.03.11 | 데이터 보존 정책 수정, 7.3, 8.1 섹션 수정 | v1.0 |
| 김병환 | 26.03.10 | Viewer 역할/권한 명확화, 9.2 보존 기간 변경 | v1.0 |
| 김병환 | 26.03.05 | 화면 흐름 추가, audit log 관련 정보 추가, Workspace 전환 UX 반영 | v1.0 |
| 김병환 | 26.03.03 | App Admin 최소 계정수 변경 (1명 → 0명) | v1.0 |
| 김병환 | 26.02.26 | 내용 수정 | v1.0 |
| 김병환 | 26.02.24 | 전체적으로 재작성 | v1.0 |
| 김나정 | 26.02.11 | 최초작성 | v1.0 |

---

# 일정 구분

[IS-1250](https://selta.atlassian.net/browse/IS-1250?src=confmacro)
참고

|  |  |  |  |
| --- | --- | --- | --- |
| 에픽 | 기능 | 상세 | 일정 |
| 멀티 태넌트 구조 및 계정 권한 | \*태넌트 생성 | \*계약 시 1개 태넌트, 1개 Main Workspace, 계약에 따라 설정된 App 생성 | Relase2 (Go-live) |
| 멀티 태넌트 구조 및 계정 권한 | \*태넌트 관리 | \*태넌트 생성, 비활성화 처리 | Relase2 (Go-live) |
| 멀티 태넌트 구조 및 계정 권한 | \*워크스페이스 관리 | \*필요에 따라 태넌트 내 추가 워크스페이스 생성, 비활성화 처리, 패쇄 처리 | Relase2 (Go-live) |
| 멀티 태넌트 구조 및 계정 권한 | \*추가 생성 된 워크스페이스의 데이터 격리 | \*Main Workspace가 아닌 추가로 생성된 워크스페이스는 태넌트 데이터와 분리되어서 관리되고, 워스페이스가 비활성화 처리 시 해당 데이터는 태넌트에 통합 | Relase2 (Go-live) |
| 멀티 태넌트 구조 및 계정 권한 | \*태넌트에 계약에 따른 정책 반영 | \*계약에서 태넌트와 워크스페이스, 어플리케이션이 결정되면 해당 세팅에 따라 태넌트/워크스페이스/어플리케이션 활성화, 계약 종료에 따른 태넌트/워크스페이스/어플리케이션 비활성화 및 관련 정책 반영 | Relase2 (Go-live) |
| 멀티 태넌트 구조 및 계정 권한 | \*셀타스퀘어의 고객사 접근 시 권한 획득 | \*고객사의 승인 하에 고객사 페이지 접근 | Relase2 (Go-live) |
| 멀티 태넌트 구조 및 계정 권한 | \*사용자 권한/역할 생성 | \*사용자에게 역할(admin, user)과 권한(workspace 접근), App 사용 권한을 부여 할 수 있다. | Release1 |
| 멀티 태넌트 구조 및 계정 권한 | \*Audit | \*기존 넵튠과 거의 유사(차이는 멀티태넌트 정책이 들어가서 태넌트/워크스페이스 단위로 오딧 조회) / 조회나 보여주는 정책은 기존 넵튠에서 백엔드 팀이 설계한 정책 반영 | Release1 → 해당 기능은  [IS-1240](https://selta.atlassian.net/browse/IS-1240?src=confmacro) 에서 진행 |
| 멀티 태넌트 구조 및 계정 권한 | \*Audit | \*Audit 데이터 보존 정책 반영 | Release1 → 해당 기능은  [IS-1240](https://selta.atlassian.net/browse/IS-1240?src=confmacro) 에서 진행 |

---

# 1 Policy

* Org는 유일한 운영 주체다.
* Org만 시스템 상태를 가진다.
* Org 상태는 Pre-Active / Active / Terminated 로 정의한다.
* Contract는 운영 주체가 아니다. Contract는 행동하지 않는다.
* Contract는 Org 상태 전이 조건, 적용 기간, 허용 범위, 이력 기록만 정의한다.
* Backoffice는 Contract 조건을 기준으로 Org를 생성하고 관리한다.
* Org 하위의 Workspace와 Application은 Org 운영 범위 안에서만 존재한다.
* 최종 접근 가능 여부는 Contract 조건, Workspace 활성화, 사용자 권한의 교집합으로만 결정한다.
* Backoffice Admin은 고객 데이터에 대한 직접 접근 권한을 보유하지 않는다. 운영 목적 접근이 불가피한 경우 8 Break-Glass 원칙으로만 허용한다.
* Org 사용자 및 접근 권한은 Backoffice Admin, Master Admin, Org Admin이 관리한다.

---

# 2 Core Structure

## 2.1 System Levels

|  |  |  |
| --- | --- | --- |
| 레벨 | 정의 | 소유·관리 주체 |
| Backoffice | Org 생성·관리 및 Contract 조건 관리 영역 | Backoffice Admin, Backoffice Operator |
| Org | 고객사의 최상위 운영 단위 | Backoffice Admin 생성 / Master Admin·Org Admin 운영 |
| Workspace | Org 내부의 업무 및 데이터 범위 제한 단위 | Backoffice Admin 생성 / Master Admin·Org Admin 관리 |
| Application | Workspace에서 활성화되어 사용되는 기능 단위 | Backoffice Admin 활성화 / Master Admin·Org Admin 접근 제어 / App Admin 내부 설정 |

## 2.2 Structural Relationships

* Org : Workspace = 1 : N
* Workspace : Application = N : N 구조이나, 실제 관리 단위는 `Workspace별 App 활성화 설정`이다.
* Org 생성 시 Main Workspace 1개를 자동 생성한다.
* Additional Workspace는 Contract 조건 안에서만 추가할 수 있다.

## 2.3 Operational Ownership

|  |  |  |
| --- | --- | --- |
| 항목 | 생성 주체 | 관리 주체 |
| Org | Backoffice Admin | 상태 관리: Backoffice Admin / 이름·내부 정책: Master Admin, Org Admin |
| Workspace | Backoffice Admin | Master Admin, Org Admin |
| Workspace 데이터 선택 설정 | Backoffice Admin이 Workspace 생성 후 Master Admin·Org Admin이 설정 시작 | Master Admin, Org Admin |
| Workspace별 App 활성화·비활성화 | Backoffice Admin | Backoffice Admin |
| App 내부 설정 | — | App Admin, Master Admin, Org Admin |
| Master Admin 계정 | Backoffice Admin | Backoffice Admin |
| Org 사용자 및 접근 권한 | — | Master Admin, Org Admin, Backoffice Admin |

## 2.4 Workspace Definition

* Workspace는 독립 시스템이 아니다.
* Workspace는 Org 데이터의 전체 복사본이 아니다.
* Workspace는 Org 내부 데이터 범위 제한 레이어다.
* Main Workspace는 Org 전체 데이터셋에 접근할 수 있다.
* Main Workspace는 독립적으로 폐쇄할 수 없다. Org가 Terminated 되는 경우에만 폐쇄한다.
* Additional Workspace는 Backoffice Admin이 생성한다. 생성 이후 Workspace 데이터 선택 설정(예: 스터디·프로덕트 범위)은 Master Admin 또는 Org Admin이 수행한다.
* Additional Workspace는 Org 데이터 중 선택된 부분집합에만 접근할 수 있다.

---

# 3 Data Scope

## 3.1 Org Data

Org에 귀속되는 데이터:

* 사용자 계정, 역할, 계정 상태, Workspace 할당, App 접근 권한
* Org 기준 정보 및 설정
* Org Workflow 설정
* Connected Service 설정 및 라이선스 등록 정보
* Org 범위의 Application 데이터
* Org 범위의 Audit Trail, Activity Log, Audit Log

## 3.2 Non-Org Data

Org 데이터 접근 제한 정책이 적용되지 않는 데이터:

* Contract 조건, 적용 기간, 이력 기록
* Backoffice 운영 로그, 처리 이력

Org 상태가 Pre-Active 또는 Terminated인 경우에도 Contract 정보와 Backoffice 관리 데이터는 조회할 수 있다.

## 3.3 Data Isolation

* 모든 데이터는 Org 식별자를 기준으로 논리적으로 분리한다.
* 권한 부여 없이 다른 Org 데이터에 접근할 수 없다.
* Cross-Org 접근 및 데이터 이동은 현재 범위에서 미적용이다. (→ 미결 #1, #10, #11)

## 3.4 Workspace Data Selection

**기준 정보:**

* Main Workspace는 Org 전체 기준 데이터를 사용한다.
* Additional Workspace는 Org 기준 데이터 중 선택된 범위만 사용한다. 선택은 복제가 아니라 범위 제한이다.

**Safety DB 데이터:**

* Case ID는 Org 내부에서 전역 고유해야 한다.
* Workspace 간 중복 Case ID가 존재하면 데이터 병합을 차단한다.

**Workspace 간 데이터 통합:**

* Additional Workspace 데이터는 해당 Workspace가 폐쇄된 경우에만 Main Workspace로 통합할 수 있다.
* Org 레벨 상위 조회(대시보드, 트래커 등)는 통합 이후에만 해당 데이터를 포함한다.

## 3.5 App 간 데이터 이동

같은 Workspace 내 App 간 데이터 이동 가능 여부는 App 특성에 따라 조정 가능한 구조로 처리한다. (→ ISO-03)

---

# 4 Access Control

## 4.1 Three-Condition Gate

|  |  |  |
| --- | --- | --- |
| 게이트 | 결정 주체 | 결정 내용 |
| Contract 조건 | Backoffice Admin | Org에 허용된 Workspace 수, App 범위, 사용 기간 정의 |
| Workspace 활성화 | Backoffice Admin | 허용된 App을 어떤 Workspace에서 활성화할지 설정 |
| 사용자 권한 | Master Admin, Org Admin, Backoffice Admin | 사용자별 Workspace 접근 권한 및 App 접근 권한 부여 |

세 조건 중 하나라도 충족되지 않으면 접근을 거부한다.

Master Admin 및 Org Admin도 Org 운영 권한과 실제 Workspace/App 접근 권한은 구분하며, App 접근을 위해서는 다른 사용자와 동일하게 사용자별 권한 부여가 필요하다.

## 4.2 Role Boundaries

* 사용자별 App 접근 권한 설정은 Backoffice Admin, Master Admin, Org Admin이 수행한다.
* App Admin은 App 내부 설정만 수행한다. 사용자 접근 제어는 수행하지 않는다.
* Master Admin 및 Org Admin은 Org 사용자와 권한을 관리할 수 있지만, Workspace 접근 / App 접근 / App 내부 설정 권한은 다른 사용자와 동일하게 명시적으로 부여하여 사용한다. 필요 시 본인 계정에도 직접 부여할 수 있다.
* 사용자 초대와 접근 제어는 Org 레벨에서만 수행한다. Workspace에서 사용자를 직접 초대할 수 없다. 단 Master Admin 최초 초대와 운영 목적 예외 처리는 Backoffice에서 수행 한다.

## 4.3 Access Recheck

* Workspace 전환 시점에 대상 Workspace 접근 권한과 App 접근 권한을 다시 확인한다.
* 재확인 시 권한이 없으면 이동을 거부한다.
* 접근 가능한 Workspace가 1개인 경우 Workspace 전환 메뉴를 노출하지 않는다. (미결: 홈/네이게이션 정책 문서에서 결정 예정)

---

# 5 Workspace Model

## 5.1 생성 및 수량 한도

* Org 생성 시 Main Workspace 1개를 자동 생성한다.
* Additional Workspace는 Contract 조건에 따라 Backoffice Admin이 생성한다.
* Org당 Workspace 기본 수: 1개 / 최대: 100개

## 5.2 Workspace App 모델

* Workspace당 활성화 가능한 App 수는 Contract 조건에 따른다.
* 최소 1개, 최대 10개의 App을 Workspace에서 활성화할 수 있다.
* 같은 Workspace 안에서 동일한 App을 여러 개 사용할 수 없다.
* Workspace별 App 활성화 주체는 Backoffice Admin이다.

## 5.3 운영 원칙

* 사용자는 여러 Workspace에 접근할 수 있다.
* 사용자는 Workspace마다 다른 역할을 가질 수 있다.
* 권한은 사용자 자체가 아니라 `Org–Workspace–App 관계`에 귀속된다.
* Workspace 전환 및 진입 UX 상세는 NAV (Customer Solution) 참조.

---

# 6 Lifecycle

Org만 시스템 상태를 가진다. Contract는 상태를 가지지 않는다.

|  |  |  |
| --- | --- | --- |
| Org 상태 | 진입 조건 | 결과 |
| Pre-Active | 계약이 등록되었지만 Org 사용 시작 전이거나, 현재 유효한 Contract 조건이 없고 미래 Contract 조건만 남아 있는 경우 | 고객 로그인 차단, 데이터 유지, Backoffice 사전 설정 가능 |
| Active | Contract 조건이 Org 사용을 허용하는 경우 | 정상 사용 가능 |
| Terminated | Contract 조건이 더 이상 Org 사용을 허용하지 않는 경우 | 접근 차단, 데이터 보존 후 삭제 |

## 6.1 Activation

* Backoffice Admin이 Contract 정보를 기준으로 Org를 생성한다.
* Org 생성과 동시에 Main Workspace 1개를 자동 생성한다.
* 최초 Contract 시작일이 미래이면 Org는 Pre-Active 상태가 되고, 현재 또는 과거이면 Active 상태가 된다.
* Backoffice Admin이 Workspace별 Application 활성화 설정을 수행한다.
* Backoffice Admin이 Master Admin 계정을 직접 생성하고 초대 메일을 발송한다.
* Pre-Active 상태에서는 고객 로그인이 불가하지만, Backoffice에서 App 활성화, Master Admin 초대 등 사전 설정 작업은 수행할 수 있다.
* Org 사용 가능 시점이 도래하면 Org는 Active 상태로 전이된다.
* 구체적인 온보딩 처리 흐름은 BOF 참조.

## 6.2 Continuation and Expansion

* Contract 조건이 계속 사용을 허용하는 동안 Org는 Active를 유지한다.
* Contract 조건이 확장되면 Org는 Active를 유지한 상태에서 Additional Workspace 또는 App 범위를 추가할 수 있다.
* 현재 유효한 Contract 조건이 종료되었더라도, 미래에 시작될 Contract 조건이 남아 있으면 Org는 Pre-Active로 전이된다.
* 현재 범위에서는 Additional Org 생성 정책을 정의하지 않는다. (→ 미결 #8)

## 6.3 Termination

* Contract 조건이 Org 사용을 더 이상 허용하지 않으면 Org는 Terminated 상태로 전이된다.
* 운영 판단에 의해 Org 종료가 필요한 경우에도 Org는 Terminated 상태로 전이될 수 있다.
* Org가 Terminated가 되면 해당 Org의 모든 계정은 자동으로 접근 차단 처리된다.
* Org가 Terminated가 되면 모든 활성 세션을 강제 종료하고 로그인이 불가능해진다.
* Org 데이터는 Terminated 시점부터 D+60까지 보존하며, D+60 시점에 hard delete 처리한다.
* Master Admin 계정은 Org가 Terminated 되기 전에는 비활성화할 수 없다.
* 구체적인 오프보딩 처리 흐름은 BOF 참조.

## 6.4 Workspace 폐쇄 및 App 비활성화

* Additional Workspace는 Contract 조건 만료 또는 고객사 요청에 따라 폐쇄할 수 있다. 처리는 Backoffice Admin이 수행한다.
* Main Workspace는 독립적으로 폐쇄할 수 없다.
* Workspace가 폐쇄되면 해당 Workspace의 App은 비활성화된다.
* Workspace 폐쇄 후 데이터 보관은 D+60 정책을 따른다.

## 6.5 App 비활성화

* App 단위 계약이 종료된 되면, 해당 App 데이터는 종료 시점 기준으로 D+60일 보존 후 삭제 된다.
* Org, Workspace 계약이 유효하더라도 종료된 App 데이터는 별도로 삭제된다.

---

# 7 Role & Limit Summary

## 7.1 역할 정의

|  |  |  |
| --- | --- | --- |
| 영역 | 역할 | 개념 |
| Backoffice | Backoffice Admin | Org 생성, Contract 관리, Workspace 생성, App 활성화, Master Admin 생성, 운영 로그 조회를 수행한다. |
| Backoffice | Backoffice Operator | 운영 범위의 Backoffice 업무를 수행한다. |
| Org | Master Admin | Org 최고 관리자. Org 설정, 사용자 관리, 접근 권한 관리를 수행한다. 필요 시 본인에게도 Workspace/App/App Admin 권한을 명시적으로 부여하여 작업할 수 있다. 계약 종료 전 비활성화 불가. |
| Org | Org Admin | Master Admin 위임 범위에서 Org 운영을 수행한다. 필요 시 본인에게도 Workspace/App/App Admin 권한을 명시적으로 부여하여 작업할 수 있다. Master Admin 설정을 변경할 수 없다. |
| Org | Org User | Org 내 일반 사용자. Org 홈에서 관리자 메뉴에 접근할 수 없다. App 레벨에서 App Admin 또는 App User 권한을 부여받아 App을 사용한다. |
| Org | Viewer | 조회 전용. 생성·수정·삭제 불가. 기본은 Org 단위 접근, 필요 시 Workspace·App 지정. |
| App | App Admin | 특정 Workspace의 특정 App 내부 설정만 관리한다. 사용자 접근 제어 권한 없음. |
| App | App User | 일반 사용자. |

* 특수 신분: External User

  + 외부에서 Safety DB App User로 초대시 설정 가능, 추가시 비용 발생

역할 편집 권한, 초대 규칙, 강등 처리 상세는 Account 문서 참조.

## 7.2 계정 및 구조 한도

|  |  |
| --- | --- |
| 항목 | 한도 |
| Active, Locked 계정 / Org | 최대 200명 |
| Master Admin / Org | 최소 1명, 최대 1명 |
| Org Admin / Org | 최소 0명, 최대 3명 |
| App Admin / Workspace–App | 최소 0명, 최대 5명 |
| External User / Org | 최대 50명 (Active, Locked 계정 수 내 포함) |
| Viewer / Org | 최소 0명, 최대 5명 (Active, Locked 계정 수 미포함) |
| Workspace / Org | 기본 1개, 최대 100개 |
| App / Workspace | 최소 1개, 최대 10개 |

참고

* 계정 수 한도는 Active, Locked 계정 기준으로 계산한다.
* 계정의 한도 계산에서 Inactive / Invitation 상태 계정은 제한 카운트에 포함되지 않는다

# 8 Audit & Exception Principles

## 8.1 로그 3분류

|  |  |
| --- | --- |
| 로그 유형 | 기록 범위 |
| Audit Trail | Safety DB Case 필드 변경 (before / after) |
| Activity Log | 비관리자 행위 (로그인, 로그아웃, Workspace 전환 등) |
| Audit Log | 관리자 행위 (계정·권한·설정 변경) |

## 8.2 핵심 원칙

* Case 수정은 Audit Trail에만 기록한다. Activity Log에 중복 기록하지 않는다.
* 읽기·조회 이벤트는 기록하지 않는다.
* 감사 로그는 Append-only 구조로 관리한다. 수정 API와 삭제 API는 제공하지 않는다.

## 8.3 보존 원칙

* Org 데이터 로그는 Org Active 전체 기간 동안 보존한다.
* Org 데이터 로그는 Org Terminated 후 D+60 시점에 삭제한다.
* Backoffice 운영 행위 로그 보존 기간은 내부 정책 결정 후 반영한다. (→ 미결 #4)
* 보존 기간 변경은 신규 기록부터 적용한다. 변경 이전 기록은 기존 기간을 유지한다.

감사 로그 수집 이벤트 상세, 조회 접근 범위, 화면·Export 규칙은 참조.

## 8.4 Break-Glass 원칙

* Backoffice Admin의 고객 데이터 직접 접근은 기본 차단한다.
* 운영 목적 접근이 불가피한 경우 Break-Glass로만 허용한다.
* 접근 사유 입력은 필수다. 사유 없이 요청을 진행할 수 없다.
* Break-Glass 접근 중 모든 행위는 Backoffice Audit Log와 해당 Org 감사 로그에 동일하게 자동 기록한다.

Break-Glass 승인 플로우, 시간 제한, 사후 통지 등 운영 상세는 BOF 참조.

Phase 2 상세 정책은 미결. (→ 미결 #4 연관)

---

# 9 Requirement Summary

|  |  |  |
| --- | --- | --- |
| ID | 정책 (한 줄) | 상세 참조 |
| ISO-01 | 개별 Org 간 데이터 격리 처리 | — |
| ISO-02 | Org 내 Workspace 간 데이터 격리 처리 | — |
| ISO-03 | Workspace 내 App 간 데이터 이동은 App 특성별 조정 가능 구조로 처리 | — |
| ISO-04 | Break-Glass: 사유 입력 필수, 즉시 허용, Backoffice·Org 양쪽 로그 기록 | → 8, BOF |
| ONB-01 | Org 생성 시 Main Workspace 1개 자동 생성 | → BOF |
| ONB-02 | Master Admin 계정은 Backoffice Admin이 직접 생성 후 초대 메일 발송 | → BOF |
| ONB-03 | Org가 Pre-Active 또는 Terminated 상태로 전환될 때 하위 모든 계정 일괄 접근 차단 | → BOF |
| ONB-04 | Org가 Pre-Active 또는 Terminated 상태로 전환될 때 활성 세션 전체 강제 종료 | → BOF |
| ONB-05 | 계약 종료 후 보존 기간 내 Backoffice Admin의 고객 데이터 추출 기능 제공 | → BOF |
| ONB-06 | Master Admin 계정은 계약 종료 전 비활성화 불가 처리 | → BOF |
| SES-01 | 복수 Workspace 접근 권한 사용자는 App 사용 중 Workspace 전환 가능 | → NAV (Customer Solution) |
| SES-02 | Workspace 전환은 Soft Switch 방식 (세션 유지 + 신규 세션 발급) | → NAV (Customer Solution) |
| SES-03 | Workspace 진입 후 역할별 분기 처리 | → NAV (Customer Solution) |
| LFC-01 | 초대는 Org 레벨 (Master Admin / Org Admin) 에서만 수행 | → ACC |
| LFC-02 | 초대 링크 유효기간 7일, 만료 시 링크 무효화 | → ACC |
| LFC-03 | 초대 재발송 시 이전 링크 즉시 파기 | → ACC |
| LFC-04 | 계정 삭제 미제공, 비활성화로 대체 | → ACC |
| LFC-05 | 비활성화 계정의 데이터 및 이력 보존 | → ACC |
| AUD-01~09 | 감사 로그 수집 원칙 및 보존·무결성 규칙 | → 8, AUD |
| AUD-10~12 | 감사 로그 조회 범위, 화면, Export 규칙 | → AUD |
| LMT-01~07 | 사용량 한도 초과 시 차단 처리 | → 7.2 수치 참조, 처리 상세 BOF·ACC |
| ROLE-01~05 | 권한 변경 즉시 적용, 이력 기록, 강등 처리 | → ACC |
| LIC-01~03 | WHODrug·MedDRA 라이선스 등록·검증·자동 업데이트 | → Org Admin 문서 (추후 작성) |
| TRF-01~07 | Org 간 데이터 이동 요청·승인·처리 | → 미결 #1 |

---

# 10 Edge Cases

## 10.1 State vs Access 충돌

* Org가 Pre-Active 또는 Terminated이면 기존 Workspace 접근 권한과 App 접근 권한이 남아 있어도 접근을 허용하지 않는다.
* Contract 조건이 App 허용 범위를 정의해도 Workspace 활성화가 없으면 접근을 허용하지 않는다.
* Workspace 활성화가 있어도 사용자 권한이 없으면 접근을 허용하지 않는다.
* Workspace 전환 시점 재검증에서 대상 Workspace 또는 App 권한이 없으면 이동을 거부한다.

## 10.2 Workspace vs User 충돌

* 사용자는 여러 Workspace에 접근할 수 있다.
* 사용자는 Workspace별로 서로 다른 역할을 가질 수 있다.
* Workspace는 사용자를 직접 초대하지 않는다. 초대는 Org 레벨에서만 수행한다.

## 10.3 Data Merge 충돌

* Additional Workspace 데이터는 Org 데이터의 복제가 아니다.
* Additional Workspace 데이터의 Main Workspace 통합은 해당 Workspace가 폐쇄된 경우에만 허용한다.
* Workspace 내부 App 간 데이터 이동은 App 특성별 규칙에 따라 조정 가능해야 한다.
* Workspace는 유지되고 특정 App만 비활성화되는 경우의 데이터 처리 방식은 미결이다. (→ 미결 #5)

## 10.4 Cross-Org Edge Cases (고도화 대상)

* 고도화 섹션 참조

## 10.5 Audit Visibility Edge Cases

* Phase 1에서는 Org, Workspace, App 각 레벨에서 해당 레벨 로그만 조회한다.
* Org 레벨에서 하위 Workspace·App 로그 통합 조회는 현재 미적용이다. (→ 미결 #6)
* Master Admin 또는 Org Admin이 App 로그를 조회하려면 해당 App 접근 권한을 직접 보유해야 한다.
* 향후 통합 조회 기능 추가를 위한 기반 설계는 현재 단계에서 고려해야 한다.

---

# 11 고도화 요구사항

본 섹션은 고도화 단계에 구현 예정인 요구사항들을 기록한다. 본문에서 제외된 내용 중 고도화 시점에 반영이 필요한 항목들이 포함된다.

## 11.1 External User 관련

* External User는 Safety DB 외 다른 App 접근 권한을 받을 수 없다. (10.2 이월)
* Cross-Org 초대 도입 시 신규 계정을 만들지 않고 기존 계정에 대상 Org 접근 권한을 추가하는 방식으로 처리한다. (10.4 이월)
* Cross-Org 초대 도입 시 부여 가능한 역할은 External User, Viewer만 허용한다. (10.4 이월)
* Cross-Org 초대 도입 시 로그인 분기, Workspace 선택 목록 구성, 세션 전환 UX는 별도 정합성 재정의가 필요하다. (10.4 이월)

  + External User가 여러 조직에 초대 되는 경우, 같은 이메일로 초대 될 수 있어야 함
  + 로그인 시 조직을 선택 할 수 있어야 함.
  + 초대 시 External User 구분 할 수 있는 기능 필요.
  + MFA 있는 조직에 초대된 경우, 로그인 시. 조직 선택 후 해당 조직의 정책에 맞게 MFA 코드 입력 필요
  + 조직 전환은 신규 세션 발급 필요

    - 동작 자체는 어떤게 할지 논의 필요: 데이터 섞이지 않고 구분된다면 단방향 처리 필요.
* 권한 매트릭스 3개(Org/WS/Application 레벨)에서 External User 열 정의. (본문 매트릭스 이월)

## 11.2 Viewer 관련

* Viewer는 조회만 가능하다. 생성·수정·삭제는 수행하지 않는다. (10.2 이월)
* 감사 목적으로 외부인이 사용하는 것으로 해당 계정은 Master Admin/Org Admin 초대하고, 감사가 종료되면 수동으로 비활성화 처리 한다. (10.2 이월)
* 권한 매트릭스 3개(Org/WS/Application 레벨)에서 Viewer 열 정의. (본문 매트릭스 이월)

  + 매트릭스 주의사항: "Viewer는 `O`인 항목도 조회 전용으로 해석"한다.

### 감사(Audit) 목적 외부인 초대 (10.4 이월)

* 감사인이 iVigilance Square를 사용 중(타 Org 소속)인 경우: 크로스테넌트 초대 — 기존 계정에 Viewer 역할 부여
* 감사인이 iVigilance Square를 사용하지 않는 경우: 유효한 이메일 주소로 신규 계정 초대 — Viewer 역할 부여. 1인 1계정 원칙 적용
* 두 경우 모두 감사 종료 후 초대 주체(MA/TA)가 해당 Viewer 계정을 수동 비활성화한다.

# 11.3 기타 미결 사항

|  |  |  |  |
| --- | --- | --- | --- |
| # | 항목 | 출처 | 상태 |
| 1 | Org 간 이동 가능 데이터 범위 정의 및 전송 상세 정책 구체화 | 3.3, TRF-01~07 | 고도화 |
| 2 | 크로스 테넌트 구현 시 로그인 분기 정합성: Workspace 선택 목록 구성 방식, 세션 전환 UX 재정의 필요 | 10.4, SES-02 | 고도화 |
| 4 | Backoffice Audit Log 보존 기간: 내부 정책 결정 후 반영 | 8.3 | 급하지 않음 |
| 5 | Workspace 유지 상태에서 특정 App만 비활성화 시 데이터 처리 방식 | 10.3 | 고도화 |
| **6** | Org 레벨 하위 Workspace·App 로그 통합 조회: Phase 1 미적용, 기반 설계는 현재 고려 | 10.5 | 논의 필요 |
| 7 | App Admin 역할 개발 우선순위 | — | 고도화 |
| 8 | Additional Org 생성(다중 Org) 지원 범위: 현재 미적용 | 6.2 | 고도화 |
| 9 | Cross-Org 초대 시 부여 가능 역할 External User, Viewer 제한: 적용 시기 미정 | 10.4 | 고도화 |
| 10 | Cross-Org 초대 플로우 상세 정책 및 초대 링크 유효기간 정합성 | 10.4, LFC-02 | 고도화 |
| 11 | 타 Org 접근 제한 정책 구체적 방안 | 3.3 | 고도화 |
| 12 | Workspace 이름 변경 권한을 MA/TA에게 허용할지 여부   * 현재 Backoffice Admin 전용 |  | 고도화 |

# 참고: 권한 매트릭스 (통합 참조표)

> **목적**: 역할별 기능 접근 권한을 한눈에 확인하기 위한 통합 참조표

> **표기**`O` = 가능`X` = 불가`O(권한 부여 시)` = 해당 범위 권한이 부여된 경우 가능`O(Break-Glass)` = Break-Glass 시에만 가능

> **주의**Viewer는 `O`인 항목도 **조회 전용**으로 해석한다.세부 정책 충돌 시 각 정책 문서 본문이 우선한다.Backoffice 내부 권한(Admin/Operator 역할별 메뉴 접근, 로그 조회 등)은 `(NEW) Backoffice` 8.2 화면별 역할 권한 매트릭스 참고.

---

## Org 레벨 권한

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 기능 | Backoffice Admin | Backoffice Operator | Master Admin | Org Admin | Org User(App Admin, App User) |
| Org 생성 | O | X | X | X | X |
| Org 상태 변경 | O | X | X | X | X |
| Org 이름 변경 | O | X | X | X | X |
| 계약 정보 관리 | O | X | X | X | X |
| 계약 정보 조회 | O | O | O | O | X |
| Org 기본 정보 조회 | O | O | O | O | X |
| 사용자 초대/생성 | O | X | O | O\* | X |
| 역할 / Workspace / App 권한 수정 | O | X | O | O\* | X |
| 계정 비활성화 / 재활성화 | O | O | O | O\* | X |
| 비밀번호 재설정 메일 발송 | O | O | O | O | X |
| 라이센스(Meddra, Whodrug) 관리 | X | X | O | O | X |
| Company Config관리 | X | X | O | O | X |
| ICSR Config 관리 | X | X | O | O | X |
| MFA 설정 | O | X | O | O | X |

**각주**

* `Org Admin*` : Master Admin 관련 설정 변경은 제외

**참고**

* `(NEW) Backoffice` 3.2, 3.3, 3.4, 8.2
* `(NEW) Account (+Login, Password)` 1.2, 2.4, 3.3.1, 3.4.1, 4.5, 8.1, 8.5

---

## Workspace 레벨 권한

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 기능 | Backoffice Admin | Backoffice Operator | Master Admin | Org Admin | App Admin | App User |
| Workspace 상세 조회 (Backoffice) | O | O | X | X | X | X |
| Workspace 접근 (서비스 내부) | O(Break-Glass) | X | O(권한 부여 시) | O(권한 부여 시) | O(권한 부여 시) | O(권한 부여 시) |
| Workspace 이름 변경 | O | X | X | X | X | X |
| Workspace 내 App 활성/비활성 | O | X | X | X | X | X |
| 추가 Workspace 폐쇄 | O | X | X | X | X | X |
| 추가 Workspace 완전 폐쇄 | O | X | X | X | X | X |

**각주**

* `O(Break-Glass)` : 일반 접근은 불가하고, Break-Glass 시 대상 Org 범위 내 접근 가능
* `O(권한 부여 시)` : 해당 사용자에게 Workspace 접근 권한이 부여된 경우만 가능

**참고**

* Workspace 접근을 제외한 나머지 활동들은 백오피스 계약에서 이뤄지는 활동이고 현재 기준(3월 31일)으로 어드민 기획 시 일부 기능이 어드민에서 가능하게 수정 될 수 있습니다.
* `(NEW) Backoffice` 0.4, 0.6, 2.4, 2.6, 2.7, 6.2
* `(NEW) Account (+Login, Password)` 2.3, 2.4

---

## Application 레벨 권한

사용자가 App에 접근하려면 아래 3단계가 모두 충족되어야 한다.

1. 계약에 App 포함
2. Workspace에서 App 활성화
3. 사용자에게 App 접근 권한 부여

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 기능 | Backoffice Admin | Backoffice Operator | Master Admin | Org Admin | App Admin | App User |
| 사용자별 App 접근 권한 설정 | O | X | O | O\* | X | X |
| Application 사용 | O(Break-Glass) | X | O(권한 부여 시) | O(권한 부여 시) | O(권한 부여 시) | O(권한 부여 시) |
| Default Values 설정 조회 | O(Break-Glass) | X | O(권한 부여 시) | O(권한 부여 시) | O(권한 부여 시) | O(권한 부여 시) |
| App Audit Log / Activity Log 조회 | O(Break-Glass) | X | O(권한 부여 시) | O(권한 부여 시) | O(권한 부여 시) | X |

**각주**

* `Org Admin*` : Master Admin 관련 설정 변경은 제외
* `O(Break-Glass)` : 일반 접근은 불가하고, Break-Glass 시 대상 Org 범위 내 App 접근 가능
* `O(권한 부여 시)` : 해당 Workspace-App 접근 권한이 부여된 경우만 가능

**참고**

* `(NEW) Backoffice` 0.6, 2.6, 5.1, 5.2, 6.2
* `(NEW) Account (+Login, Password)` 2.2, 2.4, 4.5, 8.1, 8.5

---

## 해석 원칙

* Master Admin / Org Admin도 Workspace·App 접근 권한이 **자동으로 생기지 않는다**. 권한이 부여된 범위만 접근 가능하다.
* Backoffice Admin은 고객 서비스 내부를 상시 사용하는 역할이 아니며, 고객 데이터 직접 접근은 **Break-Glass 예외**로만 허용된다.
* Backoffice Operator는 **비활성화 / 잠금 해제 / 비밀번호 재설정 메일 발송**은 가능하지만, **역할·권한 부여·변경은 불가**하다.
* Workspace 이름 변경, Workspace 내 App 활성/비활성, 추가 Workspace 폐쇄/완전 폐쇄는 현재 문서 기준으로 **Backoffice Admin 전용**이다.

**참고**

* `(NEW) Backoffice` 0.6, 2.4, 2.6, 2.7, 6.2, 8.2
* `(NEW) Account (+Login, Password)` 2.2, 2.4, 3.3.1, 3.4.1, 4.5, 8.1, 8.5

---

## 미결
