# Audit Log, Activity Log, Audit Trail

관련 이슈:

[IS-1257](https://selta.atlassian.net/browse/IS-1257?src=confmacro)

# 변경 이력

|  |  |  |  |
| --- | --- | --- | --- |
| 날짜 | 작성자 | 변경 내용 | 버전 |
| 2026-04-29 | 김병환 | Org User 개념 도입   * 3.2, 5.1 에 참고 추가 * Aud-06 수정 * 역할 관련 오딧 수정    + 6.1 역할 변경 이벤트 분리   + 6.2.2 역할 변경 이벤트 분리   + 초대 발송 로그에 org/app 역할 병기 |  |
| 2026-04-22 | 김병환 | External User, Viewer 관련 사항 고도화에 하게 되어 관련 내용 수정   * 규칙 부분은 수정하지 않고, 실제 구현 및 관련 설명에서 수정 * AUD-15 에 External User, Viewer 관련 내용 삭제하고 고도화 요구사항 섹션에 해당 내용 작성 * 기존 미결로 된 부분과 고도화 통합 |  |
| 2026-04-13 | 김병환 | Tenant → Org로 교체 |  |
| 2026-04-09 | 김병환 | 6.2.1, 6.2.2에 있는 계정/로그인/멀티태넌트 정책 외의 로그를 6.2.3으로 옮기고 워크플로우 유닛에서 사용자 배정, 라이선스의 시스템 체크 부분을 추가    6에 원칙 추가  Company Config, ICSR Config의 오딧 로그 추가(6.2.4~7) |  |
| 2026-04-08 | 김병환 | Org Admin -> Org Admin으로 수정   * 고객 UI에서는 Org 대신 Org, Organization 으로 수정     Org Audit Log 추가   * 사용자 유닛에 할당/해제 |  |
| 2026-03-30 | 김병환 | Master Admin /Org Admin 권한 구조 변경 관련 내용 수정  5.1 주석, 6.1.2 역할변경, Workspace 할당, App 접근 권한 변경 수정 , 6.2.2 역할 변경, Workspace 할당, App 접근 권한 변경 수정 |  |
| 2026-03-29 | 김병환 | Master Admin /Org Admin 권한 구조 변경 관련 내용 수정  5.1 주석, 6.1.2 역할변경, Workspace 할당, App 접근 권한 변경 수정 , 6.2.2 역할 변경, Workspace 할당, App 접근 권한 변경 수정    Backoffice 정책 변경에 따른 오딧 로그 수정  2.1 / 3.1.1 / 3.2 / 4 / 5.1 / 6.1.1 / 6.1.2 / 6.2.2 / 7.2 / 8 |  |
| 2026-03-23 | 김병환 | 구조 변경 및 전체 내용 업데이트 |  |
| 2026-03-19 | 김병환 | 2번 설명 관련 내용 추가: 양쪽 기록에 대한 조건 추가  3번에서 필요 없는 부분 삭제  미결, 추후고려 사항 추가  5번 화면 흐름 Activity Log -> Audit Log > Audit Trail 순으로 조정 | v1.1 |
| 2026-03-18 | 김병환 | 최초 작성 | v1.0 |

# 일정 구분: 추가로 최우선에서 개발되는 기능에 대해서는 로그로 찍혀야 함.( [IS-1242](https://selta.atlassian.net/browse/IS-1242?src=confmacro) 참고)

|  |  |  |  |
| --- | --- | --- | --- |
| 에픽 | 기능 | 상세 | 일정 |
| 멀티 태넌트 구조 및 계정 권한 | \*Audit | \*기존 넵튠과 거의 유사(차이는 멀티태넌트 정책이 들어가서 태넌트/워크스페이스 단위로 오딧 조회) / 조회나 보여주는 정책은 기존 넵튠에서 백엔드 팀이 설계한 정책 반영 | Release1 |
| 멀티 태넌트 구조 및 계정 권한 |  | \*Audit 데이터 보존 정책 반영 | Release1 |

# 1 Policy

## 1.1 목적

플랫폼 내 발생하는 모든 행위를 목적에 따라 3종류의 로그로 구분하여 체계적으로 기록·관리함으로써, 감사 추적성을 확보하고 규제 대응 능력을 보장한다.

## 1.2 기대효과

- 규제 기관 감사 요청 시 즉각적인 이력 제출 가능

- 관리자 행위의 책임 추적성 확보

- 케이스(ICSR) 필드 변경 이력의 완전한 보존 (Audit Trail)

- 로그 위변조 방지를 통한 데이터 무결성 보장

전체 구성은 다음과 같다.

![](https://selta.atlassian.net/wiki/download/attachments/25296917/att_0_for_25296917.png?api=v2)

로그는 목적과 발생 영역에 따라 3종으로 구분한다. 각 로그는 독립적으로 관리되며, 동일 행위가 중복 기록되지 않도록 분류 기준을 엄격히 적용하되, 어려 군데 기록이 필요한 경우는 다음과 같다

① 동일 행위를 행위자(본인/관리자)에 따라 다른 로그에 기록하는 경우(6.2.1 참고)

* 관리자가 하는 경우 Admin 내에서 이루어지기 때문에 Audit Log에 기록
* 본인이 하는 경우 Admin 밖에서 이루어지기 때문에 Activity Log에 기록

② Backoffice Admin의 행위가 고객의 계정·권한·설정을 변경하는 경우: 고객의 계정·권한·설정 상태가 변경된 사실 자체가 Audit Log의 기록 대상이라고 판단(6.1.2 참고)

* 지정한 로그에 한하여 Backoffice Activity Log와 고객 Org Audit Log에 동시 기록.

# 2 Log Classification

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 로그 유형 | 정의 | 발생 영역 | 접근 권한 | 비고 |
| Activity Log | 어드민 영역 밖에서 발생하는 행위 기록 | 로그인/로그아웃, Workspace 전환 등 일반 행위 | 일반 사용자 접근 가능 | 해당 분류는 백오피스에서도 동일하게 적용하여 Backoffice Admin 바깥의 행위는 Backoffice Activity Log에 기록 |
| Audit Log | 어드민 영역 내에서 발생하는 행위 기록 | 계정·권한·설정 변경, 어플리케이션 설정 등 | Admin 권한 사용자만 접근 가능 | 해당 분류는 백오피스에서도 동일하게 적용하여 Backoffice Admin 내부의 행위는 Backoffice Audit Log에 기록 |
| Audit Trail\* | Safety DB 전용 케이스 변경 이력 | ICSR 필드별 변경 전/후 값 기록 | 일반 사용자 접근 가능 |  |

\*Audit Trail은 해당 문서에서 다루지 않고, 다른 기획에서 정해질 예정(미결)

## 2.1 로그 컬럼 구성과 필터 여부\*

|  |  |  |  |
| --- | --- | --- | --- |
| 컬럼 | 정의 | 비고 | 필터 제공 여부 |
| No | 단순 개수를 확인하는 숫자 |  |  |
| Org | 해당 로그가 어떤 Org에서의 행위로 발생 했는지 구분하기 위한 값: Org명 표시 | 해당 항목은 백오피스에서 고객의 로그를 볼때만 필요한 컬럼, 고객이 보는 화면에는 해당 컬럼 미노출 | O  1차에서는 필터 미제공: Org1개만 있음 |
| Workspace | 해당 로그가 어떤 Org>워크스페이스에서의 행위로 발생 했는지 구분하기 위한 값: Workspace 명 표시 | 해당 항목은 백오피스에서 고객의 로그를 볼때만 필요한 컬럼, 고객이 보는 화면에는 해당 컬럼 미노출 | O |
| App | 해당 로그가 어떤 Org>워크스페이스>앱에서의 행위로 발생했는지 구분하기 위한 값: App명 표시 | 해당 항목은 백오피스에서 고객의 로그를 볼때만 필요한 컬럼, 고객이 보는 화면에는 해당 컬럼 미노출 | O |
| Date | 행위로 로그가 생성된 시점 | 추후 시간대 고려 필요(미결) | O |
| Category | 해당 로그의 분류: 분류는 로그 기획시 정리되어 해당 값이 표시 |  | O |
| Task | 발생한 행위와 그에 따른 변경 사항 표시 |  |  |
| Author | 발생한 행위를 일으킨 사람/시스템 | 시스템이 행위를 한 경우: System | O |
| User | 발생한 행위에 영향을 받은 사용자 | 없는 경우 비울 수 있음 | O |

\*해당 구성은 아래에 기술될 Activity Log, Audit Log에만 반영, Audit Trail에 대한 기획은 아직 확인 안됨

# 3 Core Recording Rules

## 3.1 로그 분류 규칙 (기능이 추가되거나 업데이트 되면서 계속 업데이트 필요)

2가지 분류 규칙에 따라서 로그가 분류 되어 기록 및 조회 가능

### 3.1.1 Admin 메뉴 내부, Admin 메뉴 외부 관점

로그는 어드민 메뉴 내부 또는 외부 활동에 따라 각기 다른 페이지에서 조회 가능

#### Activity Log에 기록되는 것:

* 로그인 성공 / 실패 (실패 시 사유 포함)
* 로그아웃 (직접 / 세션 만료 / 강제)
* Workspace 전환.
* 현재 기획이 추가됨에 따라 기록되는 것은 더 늘어날 수 있음(미결)

#### Audit Log에 기록되는 것:

* 계정 생성 / 수정 / 비활성화 / 권한 변경
* 사용자 초대 / 재발송 / 수락
* Org / Workspace / Application 생성·수정·폐쇄
* Connected Service(라이선스) 등록·변경
* 워크플로우 설정
* Company Config(Product, Study 정보), ICSR Config(Sender, Default Rule)
* 현재 기획이 추가됨에 따라 기록되는 것은 더 늘어날 수 있음(미결)

### 3.1.2 Org, Workspace, App 관점

로그는 어떤 영역에서 행위를 하느냐에 따라서 각기 다른 페이지에서 조회 가능

#### Org/Master Admin만 접근 가능한 페이지에서 행위(ex Org Home)

* Org Activity Log와 Org Audit Log에 기록

#### App 단위에서의 활동

* App Activity Log와 App Audit Log에 기록

#### 예외사항

* Org/Master Admin을 포함하여 App 접근 권한을 가진 App User, App Admin, External User의 로그인/아웃 기록도 App 단위가 아닌 Org Activity Log에서만 기록

  + 이 부분은 현재 기술적인 사항으로 예외적인 동작

### 3.1.3 기타

#### Activity Log + Audit Log 양쪽에 기록 되는 것:

* 관리자가 하는 행위가 일반 사용자가 하는 행위와 겹치는 것들은 같은 메시지이나 Author가 관리자가 되어 Audit Log와 Activity Log에 기록됨

  + 사용자의 정보를 어드민에서 변경했고, 이를 User가 알아야 하기 때문

    - 대상 로그: 개인 정보 변경, 비밀번호 재설정

#### 기록하지 않는 것:

* 읽기/조회 이벤트는 Activity Log, Audit Log, Audit Trail 어디에도 기록하지 않는다.

#### Audit Trail에 기록되는 것:

* 케이스(ICSR) 필드별 수정 이력 (변경 전/후 값 포함)

  + 케이스 필드별 수정 이력은 오직 Audit Trail에만 기록

## 3.2 역할·행위별 기록 위치

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 행위 주체 | 행위 유형 | 기록 위치 | Author | 비고 |
| Master Admin / Org Admin | 어드민 내 활동 | Org Audit Log | 본인 ID |  |
| Master Admin / Org Admin | 어드민 외 활동 (로그인 등) | Org Activity Log | 본인 ID |  |
| App Admin | 케이스 수정 | 해당 App Audit Trail | 본인 ID |  |
| App Admin | 어드민 활동 | 해당 App Audit Log | 본인 ID |  |
| App Admin | 어드민 외 활동 | 해당 App Activity Log | 본인 ID |  |
| 모든 계정 | 로그인/로그아웃 | Org Activity Log | 본인 ID | 더 있을지는 확인 필요(미결) |
| Backoffice Admin | Backoffice Admin 내부 행위: 백오피스 계정 초대 및 관리 | Backoffice Audit Log | 행위자 ID\* |  |
| Backoffice Admin/Operator | Backoffice Admin 외부 행위: 계약정보 관리 및 기타 행위 | Backoffice Activity Log | 행위자 ID\* |  |

참고: App Admin / App User는 Org 레벨에서 Org User에 해당

\*Backoffice Admin 또는 Operator의 행위로 고객 설정이 변경되는 경우, 고객/Backoffice Log의 Author에는 해당 행위자의 ID로 기록한다.

# 4 Retention / Integrity / Export Principles

## Viewing / Query Limits

화면 동작 관련

* 필터는 2.1 확인하여 적용

  + 필터당 일단은 조건 1개씩만 설정 가능
* 화면 조회: 기본 최근 2주(14일) 결과만 표시
* 기간 검색: 최대 1년(365일) 지원
* 한번에 로딩 할 수 있는 최대 로그건수 : 최대 10만 건, 페이지당 30건

  + 만약 1년 치 조회 시 10만 건이 넘는경우, 10만건 규칙이 우선되어 10만건만 조회

## Export

Export

* 감사 로그 추출은 CSV 형식으로 제공하며, 감사 로그 화면에서 제공된 컬럼을 포함한다.
* Export 시 한번에 최대 1년만 가능하며 , 1년 내에서 로그 건수가 10만 건을 초과하는 경우,10만건만 Export 처리

  + 1년 초과 건에 대해서는 고객사가 회사에 문의하여 받을 수 있음.
* Export 시 조회 기간 미설정하는 경우, 현재 기준으로 30일치만 Export (10만 건 제한 적용하여 10만건 넘는 경우 10만건만 Export)

## Integrity

기술적 요구사항

* 무결성 보장

  + 감사 로그는 수정 및 삭제 불가 (Append-only 구조)
  + 위변조 방지 필요

## Retention

* 보존

  + 고객사의 모든 로그는 계약 기간 중에는 전체 보존한다.
  + 고객사의 모든 로그는 고객사 계약이 종료 되면 60일간 보존 후 완전 삭제 한다.
  + 백오피스 로그는 계속 보관

# 5 Access Scope

## 5.1. 역할별 조회 권한

|  |  |  |  |
| --- | --- | --- | --- |
| 역할 | Audit Trail | Activity Log | Audit Log |
| Backoffice Admin | 백오피스에서 전체 Org 조회 가능 | 백오피스에서 전체 Org 조회 가능 | 백오피스에서 전체 Org 조회 가능 |
| Master Admin / Org Admin | 해당 Org 조회 가능\* | 해당 Org 조회 가능\* | 해당 Org 조회 가능\* |
| App Admin | 담당 App 조회 가능 | 담당 App 조회 가능 | 담당 App 조회 가능 |
| App User / External User | 접근 가능한 App 조회 가능 | 접근 가능한 App 조회 가능 | X |
| Viewer\*\* | 해당 Org 조회 가능 | 해당 Org 조회 가능 | 해당 Org 조회 가능 |

참고: App Admin / App User는 Org 레벨에서 Org User에 해당

\*Master Admin / Org Admin은 Org 레벨 로그는 직접 조회 가능. App 레벨 로그는 해당 App에 직접 접근하여 조회.

\*\*Viewer는 감사 목적 Readonly 역할. 기본은 Org 레벨 전체 접근으로 만약 특정 Workspace/App 단위 감사가 필요한 경우 Master Admin/Org Admin으로 설정으로 범위 지정 해주면 그 때 접근하여 조회

# 6 Event Catalog

Audit Log, Activity Log와 Backoffice Activity/Audit Log에 기록될 전체 항목은 다음과 같다.

원칙: 모든 로그는 행위 단위로 1건씩 기록한다. 하나의 사용자 액션이 복수의 데이터 변경을 유발하는 경우(예: 템플릿 업로드, 일괄 설정 변경), 각 변경 건이 개별 행으로 기록된다.

### 6.1 백오피스 전용 로그

#### 6.1.1 Backoffice Audit Log (BOF 계정 관리)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 분류 | Task | 표시 문구 | 정책 | Author | 고객 Org Audit Log 동시기록 |
| BOF 계정 | 계정 생성 | Backoffice account created: [이메일] [역할] | Backoffice 계정 생성 시 | 행위자 ID | – |
| BOF 계정 | 역할 변경 | Backoffice role changed: [이메일] [변경 전] → [변경 후] | Admin ↔ Operator 역할 변경 시 | 행위자 ID | – |
| BOF 계정 | 계정 비활성화 | Backoffice account deactivated: [이메일] | 계정 비활성화 시 | 행위자 ID | – |
| BOF 계정 | 계정 재활성화 | Backoffice account activated: [이메일] | 계정 재활성화 시 | 행위자 ID | – |
| BOF 계정 | 계정 잠금 해제 | Backoffice account unlocked: [이메일] | 잠금 해제 시 | 행위자 ID | – |
| BOF MFA 설정(추후 고려) | MFA 설정 변경 | Backoffice MFA setting changed: [활성화/비활성화] | Backoffice 전체 MFA 설정 변경 시 | 행위자 ID | – |
| Log | CSV 추출 | Backoffice Audit log exported: [추출 기간] | Backoffice Audit Log 추출 | 행위자 ID | - |

#### 6.1.2 Backoffice Activity Log

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 분류 | Task | 표시 문구 | 정책 | Author | 고객 Org Audit Log 동시기록\* |
| 계약 | 계약 생성 | Contract created: [고객사명] [시작일~종료일] | 계약 생성 시 | 행위자 ID | O |
| 계약 | 계약 정보 수정(정정) | Contract corrected: [항목] [변경 전] → [변경 후] | 종이 계약서와 시스템 입력값 불일치 정정 시. 항목별 행 기록 | 행위자 ID | O |
| 계약 | 구성 변경 신규 계약(NEW) | Contract created (config change): [고객사명] [변경 내용] | Workspace/App 구성 변경으로 신규 계약 생성 시 | 행위자 ID | O |
| 계약 | 계약 종료 | Org terminated: [고객사명] [데이터 삭제 예정일] | 계약 종료(Terminate) 처리 시 | 행위자 ID | O |
| 계약 | 계약 연장(RENEW) | Contract renewed: [고객사명] [기존 종료일] → [신규 종료일] | 계약 연장(RENEW) 처리 시 | 행위자 ID | O |
| 계약 | 계약 복원 (종료→활성) | Org restored from terminated: [고객사명] [사유] | Terminated → Active 복원 시 (60일 내 한정) | 행위자 ID | O |
| 계약 | 계약 종료 알림 발송 | Contract expiry notification sent: [고객사명] [D-N일] [성공/실패] | D-90/30/7/1일 자동 발송 시. 실패도 기록 | 시스템 | – |
| 계약 | 계약 체결 안내 발송 | Contract confirmation sent: [고객사명] [성공/실패] | 계약 생성·연장·추가 완료 시. 실패도 기록 | 시스템 | – |
| 계약 | 복원 사후 통지 발송 | Restoration notification sent: [고객사명] [성공/실패] | 복원 후 통지 발송 시. 실패도 기록 | 시스템 | – |
| Org | Org 생성 | Org created: [Org명] | 계약 생성 시 자동 기록 | 행위자 ID | O |
| Org | Org 이름 수정 | Org name changed: [변경 전] → [변경 후] | Org 이름 수정 시 | 행위자 ID | O |
| Workspace | Workspace 생성 | Workspace created: [Workspace명] in [Org명] | Workspace 생성 시 | 행위자 ID | O |
| Workspace | Workspace 이름 수정 | Workspace name changed: [변경 전] → [변경 후] | Workspace 이름 수정 시 | 행위자 ID | O |
| Workspace | Workspace 폐쇄 | Workspace closed: [Workspace명] in [Org명] | Workspace 폐쇄 처리 시 | 행위자 ID | O |
| Workspace | App 활성화 | App activated: [앱명] in [Workspace명] | Workspace 내 App 활성화 시 | 행위자 ID | O |
| Workspace | App 비활성화 | App deactivated: [앱명] in [Workspace명] | Workspace 내 App 비활성화 시 | 행위자 ID | O |
| Workspace | App 할당 | App assigned: [변경 전 앱], [WS명] → [변경 후 앱], [WS명] | 계약 생성/변경 시 Workspace에 App 배정 시 | 행위자 ID | O |
| 고객 사용자 | 초대 발송 | User invitation sent: [이메일] in [Org명] | Master Admin 초대 발송 시 | 행위자 ID | O |
| 고객 사용자 | 초대 재발송 | User invitation resent: [이메일] in [Org명] | 초대 링크 만료/분실 재발송 시. 이전 링크 파기 포함 | 행위자 ID | O |
| 고객 사용자 | 초대 수락 | User invitation accepted: [이메일] in [Org명] | 초대 링크를 통해 계정 활성화 시 | 본인 ID | O |
| 고객 사용자 | Org 역할 변경 | Org role changed: [이메일] [변경 전 역할] → [변경 후 역할] | 어드민에 의해 역할 변경 시. | 행위자 ID | O |
| 고객 사용자 | App 역할 변경 | App role changed: [이메일] [변경 전 역할] → [변경 후 역할] | 어드민에 의해 역할 변경 시. | 행위자 ID | O |
| 고객 사용자 | Workspace 할당 | Workspace assigned: [이메일] → [Workspace명] | Workspace 할당 시. | 행위자 ID | O |
| 고객 사용자 | Workspace 해제 | Workspace unassigned: [이메일] from [Workspace명] | Workspace 접근 해제 시 | 행위자 ID | O |
| 고객 사용자 | App 접근 권한 변경 | App access changed: [이메일] [앱명] [on/off] | App 접근 권한 변경 시. | 행위자 ID | O |
| 고객 사용자 | 계정 정보 수정 | User profile updated: [이메일] [변경 항목] [변경 전] → [변경 후] | 이름 등 계정 기본 정보 수정 시 | 행위자 ID | O |
| 고객 사용자 | 계정 비활성화 | User account deactivated: [이메일] | 어드민에 의해 계정 비활성화 시 | 행위자 ID | O |
| 고객 사용자 | 계정 재활성화 | User account activated: [이메일] | 비활성화 → 활성화 시 | 행위자 ID | O |
| 고객 사용자 | 계정 잠금 해제 | User account unlocked: [이메일] | 잠금 해제 시 | 행위자 ID | O |
| 고객 사용자 | 비밀번호 재설정 발송 | Password reset email sent: [이메일] | 비밀번호 재설정 이메일 발송 시 | 행위자 ID | O |
| Break-Glass | 접근 시작 | Break-Glass access started: [Org명] [사유] | 접근 시작 시. 사유 입력 필수 | 본인 ID | O |
| Break-Glass | 접근 중 행위 | 행위에 대해서는 기존에 노출해야 할 로그를 노출하고, 행위자 아이디에 백오피스 아이디 표시 | 접근 기간 내 모든 데이터 수정 행위 자동 기록 | 행위자 ID | O |
| Break-Glass | 접근 종료 | Break-Glass access ended: [Org명] | 관련 업무 완료 후 접속 종료 시 | 본인 ID | O |
| Break-Glass (추후) | 접근 요청 | Break-Glass access requested: [Org명] [사유] | Backoffice Admin이 고객 데이터 접근 요청 시 | 행위자 ID | O |
| Break-Glass (추후) | 접근 승인 | Break-Glass access approved: [Org명] [승인자] | 승인/거부 정책은 추후 정의 (현재 미결) | 승인자 ID | O |
| Break-Glass (추후) | 접근 거부 | Break-Glass access denied: [Org명] [거부자] | 승인/거부 정책은 추후 정의 (현재 미결) | 거부자 ID | O |
| Break-Glass (추후) | 직권 접근 | Break-Glass access granted without approval: [Org명] | 10분 내 미응답 직권 접근 시. '승인 미확보 긴급 접근' 표기 | 시스템 | O |
| Break-Glass (추후) | 사후 통지 발송 | Break-Glass post-access notification sent: [Org명] | 접근 완료 후 Org Admin 전원 통지 시 | 시스템 | – |
| 앱 설정 | 매뉴얼 링크 변경 | App manual link updated: [앱명] [변경 전 URL] → [변경 후 URL] | 앱 매뉴얼 링크 수정 시 | 행위자 ID | – |
| 앱 설정 | CS 링크 변경 | App CS link updated: [앱명] [변경 전 URL] → [변경 후 URL] | 앱 CS 링크 수정 시 | 행위자 ID | – |
| 앱 설정 | 버전 정보 변경 | App version updated: [앱명] [변경 전] → [변경 후] | 앱 버전 정보 수정 시 | 행위자 ID | – |
| Log | CSV 추출 | Backoffice Activity log exported: [추출 기간] | Backoffice Activity Log CSV Export 시 | 행위자 ID | – |
| Log | CSV 추출 | Activity log exported: [추출 기간] | Backoffice에서 고객사 Activity Log 추출 | 행위자 ID |  |
| Log | CSV 추출 | Audit log exported: [추출 기간] | Backoffice에서 고객사 Audit Log 추출 | 행위자 ID |  |
| Log | CSV 추출 | Audit Trail exported: [추출 기간] | Backoffice에서 고객사 Audit Trail 추출 | 행위자 ID |  |
| 인증 | 로그인 성공 | Backoffice logged in: [이메일] | 로그인 성공 시 | 본인 ID | – |
| 인증 | 로그인 실패 | Failed Backoffice login attempt: [이메일] [사유] | 로그인 실패 시. 사유 포함 | 본인 ID | – |
| 인증 | 로그아웃 | Logged out: [이메일] | 명시적 로그아웃 시 | 본인 ID | – |
| 인증 | 세션 만료 | Logged out due to session timeout: [이메일] | 시간 초과 강제 로그아웃 시 | 본인 ID | – |
| 인증 | 강제 로그아웃 | Forced logout: [이메일] [사유] | 계정 비활성화·권한 변경 등에 의한 강제 종료 시 | 시스템 | – |
| 계약 | 계약 취소(CANCELLED) | Contract cancelled: [고객사명] | SCHEDULED 상태 계약 취소 시 | 행위자 ID | O |
| 계약 | 계약 만료(EXPIRED) | Contract expired: [고객사명] | 종료일 도래에 의한 자동 만료 시 | 시스템 | O |
| 계약 | 미래 계약 발효(SCHEDULED→ACTIVE) | Contract activated (scheduled): [고객사명] | 시작일 도래에 의한 자동 발효 시 | 시스템 | O |
| Org | Pre-Active → Active 전환 | Org activated: [Org명] | Contract ACTIVE 전환에 의한 Org 상태 변경 시 | 시스템 | – |
| Org | Active → Pre-Active 전환 | Org deactivated to pre-active: [Org명] | 모든 ACTIVE Contract EXPIRED + SCHEDULED 존재 시 | 시스템 | – |
| 인증 | 로그인 차단 (Org 비활성) | Login blocked: [이메일] [Org명] [Org 상태] | Pre-Active/Terminated 상태에서 고객 로그인 시도 시 | 시스템 | – |
| Workspace | Workspace 완전 폐쇄 | Workspace permanently closed: [Workspace명] in [Org명] | 데이터 이관 완료 후 완전 폐쇄 시 | 행위자 ID | O |
| 공지사항 | 공지사항 작성 | Notice created: [제목] | 공지사항 작성 시 | 행위자 ID | – |
| 공지사항 | 공지사항 노출 설정 변경 | Notice visibility changed: [제목] [노출/미노출] | 노출/미노출 토글 변경 시 | 행위자 ID | – |
| 공지사항 | 공지사항 삭제 | Notice deleted: [제목] | 공지사항 삭제 시 | 행위자 ID | – |

### 6.2 고객사 로그

#### 6.2.1 계정·로그인 관련 로그 (Org Activity Log / Org Audit Log)

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 위치 | 분류 | Task | 표시 문구 | 정책 | Author | User | 비고 | 일정 |
| Org Activity Log | 인증 | 로그인 성공 | User logged in: [이메일] | 로그인 성공 시 | 본인 ID | 본인 ID |  | 최우선 |
| Org Activity Log | 인증 | 로그인 실패 | Failed login attempt: [이메일] | 로그인 실패 시. | 본인 ID | – |  | 최우선 |
| Org Activity Log | 인증 | 로그아웃 | User logged out: [이메일] | 사용자 직접 로그아웃 시 | 본인 ID | 본인 ID |  | 최우선 |
| Org Activity Log | 인증 | 세션 만료 | Session timed out: [이메일] | 60분 세션 만료 후 자동 로그아웃 시 | 본인 ID | 본인 ID |  | 최우선 |
| Org Activity Log | 인증 | 강제 로그아웃 | Forced logout: [이메일] [사유] | 계정 비활성화·권한 변경·MFA 정책 변경 등에 의한 강제 종료 시. 사유 포함 | 시스템 | 적용 ID |  | 최우선 |
| Org Activity Log | MFA | MFA 인증 성공 | MFA verified: [이메일] | MFA 코드 인증 성공 시 | 본인 ID | 본인 ID |  | 최우선 |
| Org Activity Log | MFA | MFA 인증 실패 | MFA verification failed: [이메일] (n/5) | MFA 코드 오입력 시. 카운트 포함 | 본인 ID | – |  | 최우선 |
| Org Activity Log | MFA | MFA 잠금 | Account locked due to MFA failure: [이메일] | MFA 5회 초과로 계정 Locked 전환 시 | 시스템 | 적용 ID |  | 최우선 |
| Org Activity Log | MFA | MFA 코드 재발급 | MFA code resent: [이메일] | Resend Code 클릭 성공 시 | 본인 ID | 본인 ID |  | 최우선 |
| Org Activity Log | 비밀번호 | 비밀번호 변경 완료 | Password changed: [이메일] | 비밀번호 재설정 링크를 통해 변경 완료 시. 기존 세션 강제 종료 포함 | 본인 ID | 본인 ID |  | 최우선 |
| Org Activity Log | 비밀번호 | 180일 만료 감지 | Password expiry enforced: [이메일] | 180일 경과 후 첫 로그인 시 만료 화면 강제 표시 시 | 시스템 | 본인 ID |  |  |
| Org Activity Log | 비밀번호 | 유예 카운트 사용 | Password change deferred: [이메일] (n/5) | '나중에 변경' 클릭 시. 카운트 포함 | 본인 ID | 본인 ID |  |  |
| Org Activity Log | 계정 | 계정 잠금 | Account locked: [이메일] [사유] | 비밀번호/MFA 5회 실패 누적으로 자동 Locked 전환 시. 사유 포함 | 시스템 | 적용 ID |  | 최우선 |
| Org Audit Log | 계정 | 계정 초대 발송 | User invitation sent: [이메일] [Org역할][App역할] in [Org명] | 관리자가 신규 계정 초대 발송 시 | 행위자 ID | – |  | 최우선 |
| Org Audit Log | 계정 | 초대 재발송 | User invitation resent: [이메일] [Org역할][App역할] in [Org명] | 초대 링크 만료/분실 재발송 시. 이전 링크 파기 포함 | 행위자 ID | – |  | 최우선 |
| Org Audit Log | 계정 | 초대 수락 | User invitation accepted: [이메일] [Org역할][App역할] in [Org명] | 초대 링크 클릭·수락 완료 시 | 본인 ID | – |  | 최우선 |
| Org Audit Log | 계정 | 최초 계정 설정 완료 | Account setup completed: [이메일] | 초대받은 사용자가 이름/비밀번호 최초 설정 완료 시. 계정 Active 전환 | 본인 ID | 본인 ID |  | 최우선 |
| Org Audit Log | 계정 | 계정 비활성화 | User account deactivated: [이메일] | 관리자에 의해 계정 Inactive 처리 시. 활성 세션 강제 종료 포함 | 행위자 ID | 적용 ID |  | 최우선 |
| Org Audit Log | 계정 | 계정 재활성화 | User account activated: [이메일] | Inactive → Active 전환 시 | 행위자 ID | 적용 ID |  | 최우선 |
| Activity Log,  Audit Log | 계정 | 계정 잠금 해제 | User account unlocked: [이메일] | 관리자 해제 또는 본인 비밀번호 재설정 완료 시 | 행위자 ID | 적용 ID | 관리자 해제→Audit Log  본인 재설정→Activity Log | 최우선 |
| Org Audit Log | MFA | MFA 설정 변경 | Org MFA setting changed: [Org명] [활성화/비활성화] | Org 단위 MFA 설정 변경 시. 전체 세션 강제 종료 트리거 | 행위자 ID | – | 어드민 행위→Audit Log | 최우선 |
| Activity Log,  Audit Log | 프로파일 | 이름 변경 | User name changed: [이메일] [변경 전] → [변경 후] | 이름 변경 완료 시 | 행위자 ID | 적용 ID | 본인 수정→Activity Log  관리자 수정→Audit Log | 최우선 |
| Activity Log,  Audit Log | 비밀번호 | 비밀번호 재설정 이메일 발송 | Password reset email sent: [이메일] | 비밀번호 재설정 이메일 발송 시 | 행위자 ID | 본인 ID | 본인 요청→Activity Log  관리자 발송→Audit Log | 최우선 |

#### 6.2.2 멀티Org 정책에서 파생되는 로그

해당 로그들은 Org Audit Log, Org Activity Log에 기록된다.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 위치 | 분류 | Task | 표시 문구 | 정책 | Author | User | 일정 |
| Org Audit Log | 역할·권한 | Org 역할 변경 | Org role changed: [이메일] [변경 전] → [변경 후] | 관리자에 의해 역할 변경 시. 즉시 적용. | 행위자 ID | 적용 ID | 고라이브 |
| Org Audit Log | 역할·권한 | App 역할 변경 | App role changed: [이메일] [변경 전] → [변경 후] | 관리자에 의해 역할 변경 시. 즉시 적용. | 행위자 ID | 적용 ID | 고라이브 |
| Org Audit Log | 역할·권한 | Workspace 할당 | Workspace assigned: [이메일] → [Workspace명] | Workspace 접근 권한 부여 시. | 행위자 ID | 적용 ID | 고라이브 |
| Org Audit Log | 역할·권한 | Workspace 해제 | Workspace unassigned: [이메일] from [Workspace명] | Workspace 접근 권한 해제 시. (크로스 테넌트 관련은 추후 고려) | 행위자 ID | 적용 ID | 고라이브 |
| Org Audit Log | 역할·권한 | App 접근 권한 변경 | App access changed: [이메일] [앱명] [허용/차단] | App 접근 권한 on/off 변경 시. | 행위자 ID | 적용 ID | 고라이브 |

#### 6.2.3 계정, 로그인 /멀티Org 정책 이외 고객사 로그

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 위치 | 분류 | Task | 표시 문구 | 정책 | Author | User | 일정 |
| Org Audit Log | Workflow | UNIT에 사용자 배정 | Workflow [UNIT명]: [배정된 사용자 ID 1,2...] assigned | 워크플로우의 유닛에 사용자가 배정 | 행위자 ID | 적용 ID | 고도화 |
| Org Audit Log | Workflow | UNIT에 사용자 배정 해제 | Workflow [UNIT명]: [배정된 사용자 ID 1,2...] unassigned | 워크플로우의 유닛에 사용자 배정 해제 | 행위자 ID | 적용 ID | 고도화 |
| Org Audit Log | Connected Service | 라이선스 등록 | License registered: [WHODrug/MedDRA] [번호] | 라이선스 번호 신규 등록 시 | 행위자 ID | – | 고라이브 |
| Org Audit Log | Connected Service | 라이선스 변경 | License updated: [WHODrug/MedDRA] [변경 전] → [변경 후] | 라이선스 번호 변경 시 | 행위자 ID | – | 고라이브 |
| Org Audit Log | Connected Service | 라이선스 Active 상태 확인 | License active check: [WHODrug/MedDRA] | 등록 후 매주 월요일에 시스템이 체크 | 시스템 |  | 고라이브 |
| Org Audit Log | Connected Service | 라이선스 Expired 상태 확인 | License expired check: [WHODrug/MedDRA] | 등록 후 매주 월요일에 시스템이 체크 | 시스템 |  | 고라이브 |
| Org Audit Log | Audit Log | CSV 추출 | Audit log exported: [조회 범위] [기간] | CSV Export 실행 시 | 행위자 ID | – | ? |
| Org Activity Log | Activity Log | CSV 추출 (Activity Log) | Activity log exported: [조회 범위] [기간] | CSV Export 실행 시 | 행위자 ID | – | ? |

## 6.2.4 Product Config > Family

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 위치 | 분류 | Task | 표시 문구 | 정책 | Author | User | 일정 |
| Org Audit Log | Product | Family 생성 | Family created: [Family명] | Family 신규 생성 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | Family 정보 수정 | Family updated: [Family명] [항목] [변경 전] → [변경 후] | Family 정보 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | Family 삭제 | Family deleted: [Family명] | Family 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI 그룹 생성 | RSI group created: [Family명] [Datasheet명] | RSI 그룹 신규 생성 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI 그룹 수정 | RSI group updated: [Family명] [Datasheet명] [항목] [변경 전] → [변경 후] | Datasheet Name, Effective Date, Active 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI 그룹 삭제 | RSI group deleted: [Family명] [Datasheet명] | RSI 그룹 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI Term 추가 | RSI term added: [Datasheet명] [MedDRA Code] | MedDRA Browser에서 Term 선택 추가 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI Term 수정 | RSI term modified: [Datasheet명] [항목] [변경 전] → [변경 후] | 기존 Term 수정 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI Term 삭제 | RSI term removed: [Datasheet명] [MedDRA Code] | Term 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI Template 업로드 | RSI template uploaded: [Datasheet명] [파일명] [N건] | 엑셀 템플릿 일괄 업로드 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | Product 생성 | Product created: [Product명] | Product 신규 생성 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | Product 정보 수정 | Product updated: [Product명] [항목] [변경 전] → [변경 후] | Product 정보 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | Product 삭제 | Product deleted: [Product명] | Product 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | License 생성 | License created: [Trade Name] | License 신규 생성 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | License 정보 수정 | License updated: [Trade Name] [항목] [변경 전] → [변경 후] | License 정보 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | License 삭제 | License deleted: [Trade Name] | License 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Product | RSI Datasheet 매핑 | RSI datasheet mapped: [Trade Name] [Datasheet명] | License에 RSI 그룹 연결 시 | 행위자 ID | – | 최우선 |

## 6.2.5 Product Config > Study Config (Study Design 포함)

**참고:** Study Design은 하나의 화면에서 Arm 추가, Period 추가, Treatment 연결 등을 개별적으로 수행할 수 있다. 단, 로그는 Save 단위가 아닌 각 행위 단위로 기록한다.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 위치 | 분류 | Task | 표시 문구 | 정책 | Author | User | 일정 |
| Org Audit Log | Study | Project 생성 | Project created: [Project ID] | Project 신규 생성 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Project 정보 수정 | Project updated: [Project ID] [항목] [변경 전] → [변경 후] | Project 정보 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Project 삭제 | Project deleted: [Project ID] | Project 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Study 생성 | Study created: [Study Name] | Study 신규 생성 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Study 정보 수정 | Study updated: [Study Name] [항목] [변경 전] → [변경 후] | Study 정보 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Study 삭제 | Study deleted: [Study Name] | Study 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Study Status 변경 | Study status changed: [Study Name] [변경 전] → [변경 후] | Ongoing/Close 변경 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | 맹검 일괄 해제 | Study unblinded: [Study Name] | Study Close 확정 시 시스템 자동 수행 | 시스템 | – | 고도화 |
| Org Audit Log | Study | Part 생성 | Part created: [Study Name] [Part Title] | Part 추가 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Part 수정 | Part updated: [Study Name] [Part Title] [항목] [변경 전] → [변경 후] | Part 정보 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Part 삭제 | Part deleted: [Study Name] [Part Title] | Part 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Arm 추가 | Arm added: [Part Title] [Arm Title] | Arm 행 추가 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Arm 수정 | Arm updated: [Part Title] [Arm Title] [항목] [변경 전] → [변경 후] | Arm Type, Blinded 등 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Arm 삭제 | Arm deleted: [Part Title] [Arm Title] | Arm 행 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Period 추가 | Period added: [Part Title] [Period명] | Period 열 추가 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Period 삭제 | Period deleted: [Part Title] [Period명] | Period 열 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Treatment 생성 | Treatment created: [Part Title] [Treatment명] | Treatment 신규 생성 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Treatment 수정 | Treatment updated: [Part Title] [Treatment명] [항목] [변경 전] → [변경 후] | Treatment 이름/제품 구성 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Treatment 삭제 | Treatment deleted: [Part Title] [Treatment명] | Treatment 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Product List 제품 추가 | Product list added: [Study Name] [Study Drug Name] | Product Master 연동 또는 WHODrug으로 추가 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Product List 제품 삭제 | Product list removed: [Study Name] [Study Drug Name] | Product List에서 제품 삭제 시 | 행위자 ID | – | 최우선 |
| Org Audit Log | Study | Product List 동기화 | Product list updated: [Study Name] | Update 버튼으로 최신 정보 동기화 시 | 행위자 ID | – | 최우선 |

## 6.2.6 ICSR Config > Sender

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 위치 | 분류 | Task | 표시 문구 | 정책 | Author | User | 일정 |
| Org Audit Log | Sender | Sender 정보 수정 | Sender updated: [항목] [변경 전] → [변경 후] | Sender 필드 정보 변경 시. 항목별 행 기록 | 행위자 ID | – | 고라이브 |
| Org Audit Log | Sender | Batch Sender ID 추가 | Batch Sender ID added: [규제기관] | 규제기관별 ID 신규 등록 시 | 행위자 ID | – | 고라이브 |
| Org Audit Log | Sender | Batch Sender ID 수정 | Batch Sender ID updated: [규제기관] [항목] [변경 전] → [변경 후] | Batch Sender ID 변경 시. 항목별 행 기록 | 행위자 ID | – | 고라이브 |
| Org Audit Log | Sender | Batch Sender ID 삭제 | Batch Sender ID deleted: [규제기관] | Batch Sender ID 삭제 시 | 행위자 ID | – | 고라이브 |

## 6.2.7 ICSR Config > Default Rule

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 위치 | 분류 | Task | 표시 문구 | 정책 | Author | User | 일정 |
| Org Audit Log | Default Rule | Case ID 생성 규칙 수정 | Case ID Rule updated: [항목] [변경 전] → [변경 후] | Case ID(C.1.1) 생성 규칙 변경 시. 항목별 행 기록 | 행위자 ID | – | 최우선 |
| Org Audit Log | Default Rule | Import 시 식별자 처리 방식 변경 | Import ID handling updated: [변경 전] → [변경 후] | Import를 통한 케이스 생성 시 C.1.1/C.1.8.1 값 처리 방식(A/B) 변경 시 | 행위자 ID | – | 최우선 |

# 7 UI / Export / Viewing Flow

## 7.1 고객사 화면에서 조회하는 로그

### 7.1.1 Activity Log 조회 흐름

① GNB [Activity Log] 클릭 → Activity Log 목록 화면

② 필터 설정하여 조회: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 선택 → [검색]

③[CSV Export] 버튼 클릭 → 조회 기간 기준 전체 건수 다운로드

### 7.1.2 Audit Log 조회 흐름

① GNB [Admin > Audit Log] 클릭 → Audit Log 목록 화면

② 필터 설정하여 조회: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 선택 → [검색]

③[CSV Export] 버튼 클릭 → 조회 기간 기준 전체 건수 다운로드

### 7.1.3 Audit Trail

별도 기획 진행 중. 이 문서에서는 다루지 않음.

## 7.2 백오피스에서 화면에서 조회하는 로그

### 7.2.1 고객사 로그 조회 흐름

Backoffice에서 해당 Org의 Audit Trail, Activity Log, Audit Log를 조회 할 수 있다.

① GNB [Log] → 고객사 로그 클릭 → 필터 확인(결과가 처음 부터 나오지 않음)

② 필터 설정: 날짜 범위 / 고객사명 / Org / Workspace / App / 조회 할 로그 종류 선택(Audit Trail, Activity Log, Audit Log)→ [검색]

③ [CSV Export] 버튼 클릭 → 조회 기간 기준 전체 건수 다운로드

### 7.2.2 백오피스 자체 로그 조회 흐름

Backoffice에서 백오피스 자체 로그를 조회 할 수 있다.

### 7.2.2.1 Backoffice Activity Log 조회 흐름

① GNB [Log] → Backoffice Activity Log 클릭 → Activity Log 목록 화면

② 필터 설정하여 조회: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 선택 → [검색]

③[CSV Export] 버튼 클릭 → 조회 기간 기준 전체 건수 다운로드

### 7.2.2.2 Audit Log 조회 흐름

① GNB [Admin > Audit Log] 클릭 → Audit Log 목록 화면

② 필터 설정하여 조회: 날짜 범위 / 카테고리 / 행위자 / 대상 계정 선택 → [검색]

③[CSV Export] 버튼 클릭 → 조회 기간 기준 전체 건수 다운로드

Backoffice 자체 로그는 2개 탭으로 구분하여 조회한다.

# 8 Requirement Summary

|  |  |  |  |
| --- | --- | --- | --- |
| ID | 요구사항 | 대상 | 우선순위 |
| AUD-01 | 로그인 성공·실패(사유 포함), 로그아웃, 세션 만료, 강제 로그아웃 이벤트를 Org Activity Log에 기록 (App 단위 Activity Log에는 별도 기록하지 않음) | Activity Log | 필수 |
| AUD-02 | MFA 인증 성공·실패·잠금·코드 재발급 이벤트 기록 | Activity Log | 필수 |
| AUD-03 | 비밀번호 변경 완료·180일 만료 감지·유예 카운트 이벤트 기록 | Activity Log | 필수 |
| AUD-04 | 계정 초대·재발송·수락·최초설정·비활성화·재활성화·잠금해제 이벤트 기록 | Audit Log | 필수 |
| AUD-05 | MFA 설정 변경 (Org 단위) 이벤트 기록 | Audit Log | 필수 |
| AUD-06 | 역할·권한 변경 (Org 역할 변경, App 역할 변경, Workspace 할당·해제, App 접근 권한) 이벤트 기록 | Audit Log | 필수 |
| AUD-07 | Org / Workspace / App 생성·수정·폐쇄 이벤트 기록 | Audit Log | 필수 |
| AUD-08 | Backoffice Activity Log: 계약·Org·Workspace·앱·고객사용자·Break-Glass·앱설정·인증 전체 운영 행위 기록 | Backoffice Activity Log | 필수 |
| AUD-09 | Backoffice Audit Log: BOF 계정 생성·역할변경·비활성화·재활성화·잠금해제 기록 | Backoffice Audit Log | 필수 |
| AUD-10 | Backoffice Admin/Operator 행위로 고객 설정이 변경되는 경우 고객 Audit Log에 Author = Backoffice Admin ID 또는 Backoffice Operator ID로 동시 기록 | Audit Log | 필수 |
| AUD-11 | 모든 로그 수정·삭제 API 미제공 (Append-only 구조). 위변조 방지 조치 적용 | 전체 | 필수 |
| AUD-12 | 고객사 로그 보존: 계약 기간 중 전체 보존 + 계약 종료 후 60일 후 완전 삭제. Backoffice 로그 보존 기간: 계속 보관 | 전체 | 필수 |
| AUD-13 | 화면 조회: 기본 최근 2주, 최대 1년, 최대 10만 건(페이지당 30건). 1년 내 10만 건 초과 시 10만 건만 조회 | 전체 | 필수 |
| AUD-14 | Export: CSV 형식, 최대 1년치, 10만 건 초과 시 10만 건만 추출. 기간 미설정 시 30일치(10만 건 제한 적용) | 전체 | 필수 |
| AUD-15 | 조회 권한: Backoffice Admin — 전체 Org.    Master Admin·Org Admin — 해당 Org.    App Admin — 담당 App.    App User — 접근 가능한 App | 전체 | 필수 |

# 9 고도화 요구사항

## 9.1 External User, Viewer

* AUD-15: External User 조회 권한 — 접근 가능한 App (AUD-15 이월)
* AUD-15: Viewer 조회 권한 — 해당 Org (AUD-15 이월)

## 9.2. 기타 미결사항, 추후 논의 사항

## 확인 필요: 로그인/로그아웃 이외에 Org Activity Log에 기록될 다른 권한의 로그

* 계정의 로그인/로그아웃은 역할에 따라 나눠서 로그에 찍을 수 없고 Org레벨에서 찍어야 한다고 개발팀 피드백 받음.
* 이거 이외에 더 없는지 확인 필요

## 기획 완료 후 확인 예정: 추가되는 워크스페이스 관련 오딧 로그

* 기준 정보 관련 기획 완료 후 동작 확인 하여 추가 작성

## 기획 완료 후 추가 예정: 어드민 관련 오딧 로그

* 어드민 기획 완료 후 해당 로그 추가 예정

## 추후 고려: 로그 조회시 Org필터 추가 필요

* 현재는 Org1개여서 필터는 미고려
* 향후 Org여러개 일시 필터 추가 필요

## 추후 고려: 로그의 시간대 고려 필요

* 로그의 생성 시간대가 한국 시간 뿐만 아니라 다른 지역대 시간 등에 대한 고려 필요할 수 있음
* 당장 급한 것은 아님.

## 추후 고려: Case Audit Trail

* 현재는 비어 있고, 추후 나정님 기획 시 연결 예정

## 추후 고려: 백오피스 사용 계정의 MFA 적용

* 혹시나 해서.....일단은 나중 추후 고려한다고 판단

## 추후 고려: Break-Glass 관련 오딧

* 수준은 이미 확정되어 추후로 표시된 로그는 추후 고려 예정

## 추후 고려: 고객시 요청으로 오딧로그 추출

오딧 로그가 너무 커서 고객사에서 회사에 요청하여 내부의 사람이 수동으로 오딧 로그 추출시 해당 활동도 고객사의 오딧로그에 기록해야 하나?

* 있으면 좋을것 같지만, 시스템 바깥의 활동을 시스템에 어떻게 오딧 로그 남길지도 기획 필요
* 당장고려할것은아니라고판단, 추후 고려 필요
