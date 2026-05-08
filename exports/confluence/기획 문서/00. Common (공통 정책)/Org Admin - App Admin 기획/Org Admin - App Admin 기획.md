# Org Admin / App Admin 정책 문서

|  |  |  |  |
| --- | --- | --- | --- |
| 작성자 | 작성일 | 변경 사항 | 버전 |
| 김병환 | 2026.04.29 | Org User 개념 적용   * 역할(Role)" 단일 표기 → Org 역할 / App 역할 분리    + 2.2, 2.4, 2.5, 2.7, UM-01, UM-10, UM-12, UM-40, TA-UM-03 * 역할 변경 → 분리    + UM-42, UM-43 * 흐름 재기술    + 2.11     초대 가능 Org 역할은 초대 주체의 권한보다 낮은 역할로 제한 한다는 규칙 삭제   * 불필요한 로직이라고 판단    + UM-12 수정     Account 기획 문서와 차이가 있어서 수정   * UM-13, UM-14, UM-23, UM-50, UM-01, UM-20, UM-21, UM-41, UM-44, UM-45, UM-51, UM-52, UM-53, UM-55 수정 * UM-15를 맞추고, UM-16 추가 |  |
| 김병환 | 2026.04.22 | External User, Viewer 관련 사항 고도화에 하게 되어 관련 내용 수정   * 규칙 부분은 수정하지 않고, 실제 구현 및 관련 설명에서 수정 * AP-01 에 Viewer 관련 내용 삭제하고 고도화 요구사항 섹션에 해당 내용 작성 * 고도화 섹션 신설하고 미결과 통합 정리 |  |
| 김병환 | 2026.04.20 | 관리자 잠금 해제 기능 제거 반영 (1, 2.1, 2.11,2.12 UM-05~07 재편). 2.5 한도 계산 기준 Locked 제외 문구 수정.  MFA 설졍 변경 시 세션 초기화가 아닌 다음 로그인시 부터 적용으로 수정(2.8, 2.11, 2.12) |  |
| 김병환 | 2026.04.14 | 계정 한도 계산 상태에 Locked 추가  어카운트 부분 비활성화 관련 내용 추가 |  |
| 김병환 | 2026.04.13 | Tenant → Org로 교체 |  |
| 김병환 | 2026.04.09 | 워크플로우 unit 배정 방식 수정    3.3 라이선스 상태와 상태 체크 동작 수정 |  |
| 김병환 | 2026.04.08 |  | 최초 작성 |

# 일정 구분

[IS-1240](https://selta.atlassian.net/browse/IS-1240?src=confmacro)
참고

|  |  |  |  |
| --- | --- | --- | --- |
| 에픽 | 기능 | 상세 | 일정 |
| 로그인 및 계정 정책 | \*Admin > User Management | 아래에 언급된 사용자 관리와 동일  위치는 Org Admin | Release1 |
| 관리자 화면(Admin) | 사용자 관리 | \*기본: 태넌트/워크스페이스/앱별 사용자 조회, (필요에 따라) 계정 비활성화/활성화 | Release1 |
| 태넌트 어드민만 지원: 사용자 생성(초대), 비활성화/활성화, MFA 설정 | Release1 |
| \*전체적인 화면 구성과 동작은 넵튠에 준하여 구성하되, 멀티태넌트 정책에 따른 화면이나 역할 부여 정도만 달라질 예정 |  |
| ~~\*계약 정보 조회~~ | ~~\*태넌트 어드민만 지원: 백오피스 어드민에서 설정 된 계약 정보 조회~~ | 고도화 → 계약 정보 조회에 대해서는 일단 계획 없음 |
| ~~\*계약 문의 할 수 있는 채널 구축(ex. 현재 CS 처럼)~~ | 고도화 → 일단 계획 없음 |
| 외부 라이선스 관리(Whodrug, MedDRA) | \*태넌트 어드민만 지원 | Relase2 (Go-live) |
| Whodrug, MedDRA: 기존 넵튠과 동일 | Relase2 (Go-live) |
| \*필요에 따라 AI 기능이 add-on 경우, 해당 메뉴에서 on/off 관리 | 고도화 |
| 워크플로우 설정 | \*태넌트 어드민만 지원: 워크플로우는 고정, 해당 워크플로우에 담당자와 due 설정 | 위에 참조 → Org Admin/ App Admin에서 진행   * 현재는 워크플로우 관련 설정 할 것은 다 고도화에서 처리. |
| 기준 정보 관리 | \*태넌트 어드민만 지원: 나정님이 기획 중인 Default Setting이 어드민에 추가 | 위에 참조 → Org Admin/ App Admin에서 진행   * 기준 정보를 설정하는 것이 있어서 Org Admin에는 해당 기능 추가, App Admin에서는 조회만 할 수 있게 추가 |
| 사용량 관리 | \*태넌트 어드민만 지원 | 고도화 |
| \*현재 사용량과 남은 사용량 조회(ex. Safety db: 이니셜 케이스 수) | 고도화 |
| \*애플리케이션별 관리 화면 | \*해당 어플리케이션의 admin에 추가(ex. Safety db: 관련 룰 설정) | Release1   * C.1.1 생성 자체는 최우선으로 진행됨에 따라 Org Admin에는 해당 기능 추가, App Admin에서 조회 할 수 있게 추가 |

---

# Part 1: Org Admin

## 1. 개요

Org Admin은 Org 내 플랫폼 운영 전반을 관리하는 메뉴이다. 설정 주체는 Master Admin / Org Admin이다.

| 메뉴 | 설명 | **일정** |
| --- | --- | --- |
| 사용자 관리 | 계정 CRUD, 초대, MFA, 접근 권한 조회 | 고라이브 |
| 라이선스 관리 | MedDRA / WHODrug 라이선스 등록 및 상태 관리 | 고라이브 |
| 사용량 조회 | 계정, 앱, 워크스페이스 사용 현황 및 한도 조회 | 고도화 |
| 오딧 로그 | 관리자 작업 이력 조회 | 최우선 |
| 워크플로우 설정 | 워크플로우 모델 조회 및 Unit 사용자 할당 - 고도화시에는 워크플로우의 기능 및 상태 권한 조합을 커스텀, 유닛 설정 및 할당 지원 예정 | 고도화 |
| 기준 정보 설정 | Product, Sender, Receiver, Study 등 기준 정보 관리 | 최우선 |
| ICSR 설정 | ICSR 케이스 관련 설정 관리 | 최우선 |
| 공지사항 | Org 내 공지사항 작성 및 노출 관리 | 고도화 |

# 2. 사용자 관리

## 2.1 개요

사용자 계정의 생성(초대), 조회, 수정, 활성화/비활성화, MFA 설정을 수행하는 메뉴이다.

*※ 계정 생명주기, 인증 정책, 비밀번호 정책의 원본 정의는* [Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) *에 있다. 본 섹션은 Org Admin 화면 관점에서 필요한 정책을 기술하며,* [Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) *와 연동된다.*

## 2.2 초대 기반 계정 등록

계정은 관리자의 초대를 통해서만 생성되며, 자가 가입(Self-signup)은 지원하지 않는다.

* 최초 Master Admin: Backoffice Admin이 관련 정보 입력하고 Backoffice에서 Master Admin 대상자를 초대
* 이후 계정 생성/초대 가능 주체: Master Admin, Org Admin (Org User(App Admin, App User) 이하는 초대 불가)
* Org Admin은 Master Admin이 기존 계정에 Org Admin 역할을 부여하여 생성됨
* 초대 재발송 가능 주체: Master Admin / Org Admin만 가능

## 2.3 계정 상태 정의

계정 상태는 4가지로 구분되며, 조건에 따라 자동 또는 수동으로 전환된다.

| 상태 | 정의 및 전환 조건 |
| --- | --- |
| Invitation | 초대 메일 발송 후 비밀번호 미설정 상태. 관리자 초대 시 자동 부여. |
| Active | 정상 사용 가능 상태. 비밀번호 최초 설정 완료 시 자동 전환. |
| Inactive | 관리자에 의해 접근이 차단된 상태. 상위 관리자가 수동 변경. |
| Locked | 로그인/MFA 실패 누적으로 시스템이 자동 차단. 5회 연속 실패 시 자동 전환. |

* Locked 상태는 Inactive와 독립적으로 관리되며, 잠금 해제 후 Active로 복귀한다.
* Master Admin 계정은 Inactive 전환이 불가하며, 계약 종료 시 Backoffice에서만 처리 가능하다.

## 2.4 초대 흐름

1. 관리자가 초대 대상 이메일 입력 및 Org 역할 지정
2. 시스템이 초대 메일 발송 (계정 상태: Invitation)
3. 초대받은 사용자가 메일 내 링크 클릭 후 최초 정보 및 비밀번호 설정
4. 설정 완료 즉시 계정 상태 Active 전환, 초대 링크 즉시 파기

* 초대 링크 유효기간: 발송 후 7일. 기간 내 미수락 시 자동 만료.
* 재발송 시 이전 링크 자동 파기, 최신 링크만 유효.

## 2.5 역할 선택 및 한도

계정 생성 시 선택 가능 Org 역할: Org Admin / Org User / Viewer

Org User 선택 시 External User 초대 가능(사용자는 App User 역할만, Safety DB 접근만 가능)

App 레벨 역할(App Admin / App User)은 Workspace/app 접근 권한 설정 시 지정한다. (참고: [Multi-Org 구조 및 관련 정책](https://selta.atlassian.net/wiki/spaces/IS/pages/23101464/Multi-Org#7.2-%EA%B3%84%EC%A0%95-%EB%B0%8F-%EA%B5%AC%EC%A1%B0-%ED%95%9C%EB%8F%84) )

*참고: External User, Viewer 역할은 고도화에서 추가될 예정이어서 현재 구현에서는 반영하지 않는다.*

| 역할 | 최대 | 한도 초과 시 처리 |
| --- | --- | --- |
| Master Admin | 1 | Backoffice에서 지정 (Org Admin 화면에서 생성 불가) |
| Org Admin | 3 | 역할 선택 비활성화 + 한도 초과 안내 |
| App Admin | Workspace-App당 5 | 해당 Workspace-App에 대한 추가 할당 차단 + 안내 |
| App User | - | 전체 한도(200명) 내 |
| External User | 50 | 역할 선택 비활성화 |
| Viewer | 5 | 역할 선택 비활성화 |

* 전체 Active, Locked 상태 계정 한도: 200명 (Viewer 미포함).
* 한도 계산 기준: Active, Locked 상태 계정만. Inactive / Invitation 제외.
* 전체 한도 도달 시 계정 생성 버튼 비활성화 + 한도 초과 안내 표시.

## 2.6 사용자 접근 권한 설정

사용자에게 접근 가능한 Workspace와 해당 Workspace 내 App을 설정한다. 설정 주체는 Master Admin / Org Admin이다 (App Admin은 불가).

* 계정 생성 시 또는 계정 정보 수정 시 설정 가능
* Workspace 선택 → 해당 Workspace 내 활성화된 App 목록에서 접근 허용할 App 선택
* 복수 Workspace 배정 가능. 각 Workspace별로 App을 개별 설정
* Workspace에 배정되었더라도 App이 하나도 선택되지 않으면 해당 Workspace 내 App 접근 불가
* Backoffice에서 비활성화된 App은 목록에 표시하지 않음

## 2.7 사용자 접근 권한 조회

사용자 목록에서 개별 사용자 선택 시 다음 정보를 표시한다.

* 부여된 Org 역할: 해당 사용자의 Org 역할 (Org Admin / Org User)
* 접근 가능 Workspace: Workspace 이름 기준으로 나열
* 접근 가능 App: 각 Workspace 하위에 시스템에 등록된 앱 이름 및 App 역할(App Admin / App User) 기준으로 나열
* 표시 순서: Workspace → 해당 Workspace 내 App(App 역할) 순서로 계층적 표시

## 2.8 MFA 정책

* MFA는 Org 단위로 활성화/비활성화하며, 개인별 On/Off는 지원하지 않는다.
* 최초 Org 생성 시, 디폴트는 Off 상태.
* 설정 가능 주체: Backoffice Admin, Master Admin, Org Admin.
* 인증 수단: 이메일 기반 6자리 코드(숫자). 유효기간 10분.
* 코드 재발급: 30초 쿨다운 적용. 30초 내 재발급 시도 시 안내 팝업 표시.
* 코드 파기: 새 코드 발급 시 이전 코드 즉시 파기.
* 잠금 처리: MFA 5회 연속 실패 시 계정 자동 Locked 전환.

|  |
| --- |
| 정책: MFA 정책 변경은 다음 로그인부터 적용된다. 기존 활성 세션은 영향받지 않으며, 변경 시점은 Audit Log에 기록된다 |

## 2.9 계정 잠금 및 해제

* 비밀번호 입력 5회 연속 실패, 비밀번호 인증 성공 이후 MFA 5회 연속 실패 시 계정 자동 Locked 전환 (Invitation 상태 제외).
* 잠금 발생 시 해당 계정으로 로그인 화면에서 안내 메시지 표시.
* 사용자 본인 비밀번호 재설정 완료 시 잠금 자동 해제.

## 2.10 계정 비활성화

* 계정의 비활성화 조건

  + 대상 계정이 특정 케이스의 Owner 혹은 Assignee이 아닌 경우
  + 대상 계정이 특정 케이스의 Owner 혹은 Assignee 이나, 상태가 ‘Close’ 또는 ‘Archive’ 인 경우가 아닌 경우
  + 위의 경우가 아닌 경우에는 계정을 비활성화 할 수 없음

    - 위 상황에서 계정 비활성화 시 에러 메시지 표시: “해당 계정은 진행 중인 케이스의 Owner 또는 Assignee로 지정되어 있어 비활성화할 수 없습니다. 케이스를 Close 또는 Archive 처리하거나, 다른 담당자에게 재배정한 후 다시 시도해 주세요.”
* 계정의 비활성화 시 모든 활성 세션 즉시 강제 종료.
* 하위 권한 Admin이 상위 권한 계정의 비활성화 시도 시 차단.
* Master Admin 계정의 비활성화 버튼은 비활성(disabled) 처리.
* 비활성화된 계정은 목록에서 표시 유지 (삭제 없음). 비활성화 일시 및 처리자 표시.
* 재활성화 버튼 제공. 클릭 시 확인 모달 후 Active 전환.

## 2.11 화면 흐름

|  |
| --- |
| 📋 계정 초대 흐름 |
| ① Org Admin > [사용자 관리] → [+ 계정 생성] 버튼 클릭 |
| ② 이메일, Org 역할 선택 (Org Admin / Org User) → 이메일 실시간 중복 검증 |
| ③ WS·App 접근 권한 설정 (Org Admin: 선택사항 / Org User: 필수) |
| ④ [초대 발송] 클릭 → 시스템 초대 메일 발송 (계정 상태: Invitation) |
| ⑤ 사용자가 초대 메일 링크 클릭 → 최초 계정 설정 화면(이름/비밀번호 입력) |
| ⑥ 설정 완료 → 초대 링크 즉시 파기 + 계정 상태 Active 전환 |
| ⚠ 7일 내 미수락 시 링크 자동 만료 → 관리자가 Invitation 상태 계정 행에서 재발송 처리 |

|  |
| --- |
| 📋 접근 권한 설정 흐름 |
| ① 계정 생성 또는 계정 정보 수정 화면 진입 |
| ② Workspace 목록에서 접근 허용할 Workspace 선택 (복수 선택 가능) |
| ③ 선택한 Workspace별로 활성화된 App 목록 표시 → 접근 허용할 App 선택 |
| ④ [저장] → 접근 권한 즉시 반영 |

|  |
| --- |
| 📋 계정 비활성화 흐름 |
| ① 사용자 관리 목록 → 대상 계정 행의 활성화 토글 클릭 |
| ② 확인 모달: '이 계정을 비활성화하시겠습니까? 비활성화 시 로그인이 불가합니다.' |
| ③ [비활성화] 클릭 → 계정 상태 Inactive 전환 + 활성 세션 강제 종료 |

|  |
| --- |
| 📋 MFA 설정 변경 흐름 |
| ① 사용자 관리 화면 |
| ② MFA Setting On/Off 토글 전환 |
| ③ Off 변경 시: 'MFA를 비활성화하면 계정 보안이 약화될 수 있습니다. 계속하시겠습니까?' |
| ④ On 변경 시: 'MFA 보안 로그인을 활성화하시겠습니까?' |
| ⑤ [확인] 클릭 → MFA 설정 변경 (다음 로그인부터 적용) |

|  |
| --- |
| 📋 계정 정보 수정 흐름 |
| ① 사용자 관리 목록 → 대상 계정 행의 편집 아이콘 클릭 → 계정 정보 수정 모달 표시 |
| ② 수정 가능 항목: 이름, Org 역할, 접근 가능 Workspace, App 할당/해제, App 역할(App Admin / App User) |
| ③ 이메일(계정 ID)은 읽기 전용 표시 |
| ④ [저장] 클릭 → 변경 사항 저장 + 변경 확인 팝업 표시 |

## 2.12 개발 요구사항

### 계정 목록 ([Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) 참고)

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| UM-01 | 이름, 이메일, 접근 가능 Org, 접근 가능 Workspace, 접근 가능 App, Org 역할, App 역할, 계정 상태, 최종 로그인 일시, 생성 일시, 비활성화 시 비활성화 일시 컬럼 표시 | 필수 | Admin-User |
| UM-02 | 계정 상태별 필터링: Active / Inactive / Locked / Invitation | 필수 | Admin-User |
| UM-03 | 이름 또는 이메일 기반 검색 기능 | 필수 | Admin-User |
| UM-04 | 계정 한도 현황 표시: 현재 Active, Locked계정 수 / 최대 허용 수 | 필수 | Admin-User |
| UM-05 | Inactive 계정 행에 재활성화 버튼 제공 | 필수 | Admin-User |
| UM-06 | Invitation 상태 계정 행에 초대 재발송 버튼 제공. 주체: Master Admin, Org Admin | 필수 | Admin-User |

### 계정 생성 ([Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) 참고

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| UM-10 | 계정 생성(사용자 초대) 버튼 → 이메일, 이름, Org 역할 선택, Workspace/App 접근 권한 및 App 역할 설정 폼 제공 | 필수 | Admin-User |
| UM-11 | 이메일 입력 시 시스템 전체 범위 실시간 중복 검증.    중복 확인 시 인라인 오류 메시지 표시: '이미 사용 중인 이메일입니다.' 사용 가능 시 확인 표시(✓). | 필수 | Admin-User |
| UM-12 | 역할 선택: Org Admin / Org User    Org Admin 최대 3명 한도 초과 시 Org Admin 역할 선택 비활성화 처리 및 한도 초과 안내 표시.    App Admin은 Workspace-App별 최대 5명까지 할당 가능하며, 한도 초과 시 해당 Workspace-App에 대한 추가 할당을 차단하고 안내 표시. | 필수 | Admin-User |
| UM-13 | 계정 한도 도달 시 생성 버튼 비활성화 및 '계정 한도에 도달했습니다.' 안내 표시 (전체 Active, Locked 200명 한도) | 필수 | Admin-User |
| UM-14 | 생성 완료 시 초대 메일 자동 발송 (계정 상태: Invitation). 성공 팝업: '입력한 이메일 주소로 초대 링크가 발송되었습니다. | 필수 | Admin-User |
| UM-15 | 이메일 형식 검증. 오류 시: '유효하지 않은 이메일 형식입니다.' | 필수 | Admin-User |
| UM-16 | 현재 Active 계정 수가 한도의 80% 이상일 경우 경고 배너 표시 | 추후 고 | Admin-User |

### 초대 메일 ([Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) 참고)

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| UM-20 | 계정 초대 이메일  발신자: Seltasquare.  제목: [iVigilance Square] 계정 설정 안내  본문:  안녕하세요, [user name] 님, 셀타스퉤어 입니다. 아래 링크를 클릭하여 개인정보 및 비밀번호를 설정해주세요.  [비밀번호 설정 규칙]   * 4자 이상 연속된 숫자를 사용할 수 없습니다. * 4자 이상 연속 반복되는 문자를 사용할 수 없습니다. * 영문 대문자/소문자/숫자/특수문자 중 3종류 이상을 조합하여 9~20자로 설정해야 합니다. * 직전 비밀번호를 재사용 할 수 없습니다.   버튼: '계정 설정' (계정 최초 설정 화면 링크).    링크 유효기간: 7일. 재발송 시 이전 링크 즉시 파기, 신규 링크만 유효. 링크로 비밀번호 설정 완료 시 해당 링크 즉시 파기. | 필수 | Admin-User |
| UM-21 | 초대 링크 유효기간 7일. 초대 링크 만료 시 관리자가 User Management 화면에서 Invitation 상태 계정을 확인 후 수동으로 재발송 처리. | 필수 | Admin-User |
| UM-22 | Active 계정에 초대 메일 재발송 불가 (UI 차단) | 필수 | Admin-User |
| UM-23 | 재발송 시 이전 링크 즉시 파기, 신규 링크만 유효. 재발송 완료 시 안내 메시지: '등록된 이메일 주소로 초대 메일이 발송되었습니다. | 필수 | Admin-User |
| TA-UM-01 | 30초 이내 재발송 시: '인증 코드는 30초마다 한 번 요청할 수 있습니다. 잠시 후 다시 시도해 주세요.' | 필수 | Admin-User |

### 계정 정보 수정 ([Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) 참고)

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| UM-40 | 수정 가능 항목: 이름, Org 역할, 접근 가능한 Org, Workspace, Workspace에 따른 App 할당/해제, App 역할(App Admin / App User). 권한에 따라 수정 가능 항목 제한 적용 | 필수 | Admin-User |
| UM-41 | 이메일(계정 ID) 필드는 읽기 전용 표시. 수정 UI 미제공. | 필수 | Admin-User |
| UM-42 | Org 역할(Role) 또는 App 역할 변경 시 확인 모달 표시: '역할 변경은 즉시 적용됩니다.' 안내 후 변경 처리. 어드민 또는 상위 권한 전용 화면 접속 중이면 변경 즉시 팝업 후 홈 이동 (ACC-12 참조). | 필수 | Admin-User |
| UM-43 | 하위 권한 Admin이 동등 또는 상위 권한 계정의 Org 역할 변경 시도 시 차단. App 역할 변경은 Master Admin / Org Admin만 가능.  역할 하향은 즉시 적용되며, 강등 대상 계정이 변경된 권한으로 접근 불가한 화면에 있는 경우 팝업 표시 후 Org 홈 이동 (상세 케이스는 ACC-12 참조). | 필수 | Admin-User |
| UM-44 | 비밀번호 재설정: '재설정 메일 발송' 버튼만 제공. 관리자가 직접 비밀번호를 입력하는 UI 미제공. | 필수 | Admin-User |
| UM-45 | App 접근 권한 수정: Master Admin / Org Admin만 가능. App Admin은 수정 불가. | 필수 | Admin-User |
| TA-UM-02 (Account 문서 > PRF-13과 동일) | 이름 필드: 2~30자, 한글/영문/숫자/공백/특수문자(, . -) 허용 | 필수 | Admin-User |
| TA-UM-03 | 접근 권한 표시: Org 역할 + Workspace(이름) → App(이름, App 역할) 계층적 표시 | 필수 | Admin-User |
| TA-UM-04 | 접근 권한 설정: Workspace 목록에서 접근 허용할 Workspace 선택 (복수 선택 가능). 선택한 Workspace별로 활성화된 App 목록 표시 → 접근 허용할 App 선택. Backoffice에서 비활성화된 App은 목록 미표시. | 필수 | Admin-User |
| TA-UM-05 | Workspace 배정 시 App 미선택 상태면 해당 Workspace 내 App 접근 불가. 저장 시 접근 권한 즉시 반영. | 필수 | Admin-User |

### 계정 비활성화 ([Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) 참고)

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| UM-50 | 계정 비활성화 버튼 제공. 클릭 시 확인 모달: '이 계정을 비활성화하시겠습니까? 비활성화 시 해당 계정의 모든 세션이 즉시 종료되며, 로그인이 불가합니다.'  계정 비활성화 조건   * 계정의 비활성화 조건    + 대상 계정이 특정 케이스의 Owner 혹은 Assignee이 아닌 경우   + 대상 계정이 특정 케이스의 Owner 혹은 Assignee 이나, 상태가 ‘Close’ 또는 ‘Archive’ 인 경우가 아닌 경우   + 위의 경우가 아닌 경우에는 계정을 비활성화 할 수 없음      - 위 상황에서 계정 비활성화 시 에러 메시지 표시: “해당 계정은 진행 중인 케이스의 Owner 또는 Assignee로 지정되어 있어 비활성화할 수 없습니다. 케이스를 Close 또는 Archive 처리하거나, 다른 담당자에게 재배정한 후 다시 시도해 주세요.” | 필수 | Admin-User |
| UM-51 | 비활성화 처리 즉시 해당 계정의 활성 세션 강제 종료 | 필수 | Admin-User |
| UM-52 | 하위 권한 Admin이 상위 권한 계정의 비활성화 시도 시 차단 및 안내 메시지 표시 | 필수 | Admin-User |
| UM-53 | Master Admin 계정의 비활성화 버튼은 고객이 사용하는 어드민에서는 disabled 처리 | 필수 | Admin-User |
| UM-54 | 비활성화 계정 목록 유지 + 비활성화 일시/처리자 표시 | 필수 | Admin-User |
| UM-55 | 비활성화 계정의 재활성화 버튼 제공. 클릭 시 확인 모달 후 Active 전환. | 필수 | Admin-User |

### MFA 설정 (신규)

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| TA-MFA-01 | MFA On/Off 토글. Org 생성 시 기본값 Off. | 필수 | Admin-User |
| TA-MFA-02 | MFA 설정 안내 문구 및 해제 시 보안 경고 표시 | 필수 | Admin-User |
| TA-MFA-03 | Off 변경 시: 'MFA를 비활성화하면 계정 보안이 약화될 수 있습니다. 계속하시겠습니까?' | 필수 | Admin-User |
| TA-MFA-04 | On 변경 시: 'MFA 보안 로그인을 활성화하시겠습니까?' | 필수 | Admin-User |
| TA-MFA-05 | MFA 변경 즉시 Audit Log 기록. 다음 로그인 부터 적용 | 필수 | Admin-User |

# 3. 라이선스 설정

## 3.1 개요

Org에서 사용하는 외부 의약품 코딩 서비스(MedDRA, WHODrug)의 라이선스 등록 및 상태를 관리하는 메뉴이다.

## 3.2 MedDRA

* MedDRA ID 입력 및 검증: 보유 중인 MedDRA ID를 입력하고 Verify 버튼으로 유효성 검증. 숫자만 입력 가능. 빈값 허용.

  + 숫자 외 입력 시: '입력한 ID가 유효하지 않습니다. 확인 후 다시 시도해 주세요.'
  + 빈값 상태에서 Verify 시 Status / Last Verified는 '-' 표시
* 상태

  + Status / Last Verified: Verify 완료 시 Active 또는 Expired 표시.
  + Expired 처리: Expired 시 기존 선택 버전 유지. 재입력·재검증으로 갱신.
  + 매주 월요일에 자동 체크하여 Active/Expired 갱신.
* Version: 라이선스 입력 시 현재 최신 MedDRA 버전을 디폴트로 자동 입력. 다른 버전 사용 시 드롭다운에서 직접 선택. 지원 버전: 29.0, 28.1, 28.0, 27.1, 27.0, 26.1, 26.0, 25.1, 25.0, 24.1, 24.0, 23.1, 23.0. 라이선스를 빈값으로 하면 버전 초기화 및 선택 불가.
* 라이선스 적용 범위: 같은 조직 내 사용자. 라이선스 있으면 자동변환 시 MedDRA 코드 자동 입력 + 수동 입력 시 코드 선택 가능. 없으면 해당 기능 사용 불가.

## 3.3 WHODrug

* WHODrug License No. 입력 및 검증: 보유 중인 WHODrug License No.를 입력하고 Verify 버튼으로 유효성 검증. 숫자만 입력 가능. 빈값 허용.

  + 숫자 외 입력 시: '입력한 ID가 유효하지 않습니다. 확인 후 다시 시도해 주세요.'
  + 빈값 상태에서 Verify 시 Status / Last Verified는 '-' 표시
* 상태

  + Status / Last Verified: Verify 완료 시 Active 또는 Expired 표시.
  + Expired 처리: Expired 시 기존 선택 버전 유지. 재입력·재검증으로 갱신.
  + 매주 월요일에 자동 체크하여 Active/Expired 갱신.
* Version: 라이선스 입력 시 현재 최신 WHODrug 버전이 자동 적용된다. 별도 버전 선택 기능 없음. 라이선스를 빈값으로 하면 버전 표시 없음.
* 라이선스 적용 범위: 같은 조직 내 사용자. 라이선스 있으면 자동변환 시 WHODrug 코드 자동 입력 + 자동변환을 위한 코드 설정 + 수동 입력 시 코드 선택 가능. 없으면 해당 기능 사용 불가.

## 3.4 저장

* 변경 사항이 있는 경우에만 Save 버튼 활성화.
* Verify 미완료 시 저장 불가. 에러: '라이선스 번호가 검증되지 않았습니다. 저장할 수 없습니다.'

## 3.5 화면 흐름

|  |
| --- |
| 📋 라이선스 등록 흐름 |
| ① [라이선스 설정] 메뉴 진입 → MedDRA / WHODrug 라이선스 화면 표시 |
| ② MedDRA ID 또는 WHODrug License No. 입력 |
| ③ [Verify] 클릭 → 외부 시스템 검증 호출 |
| ④ 검증 성공: Status(Active/Expired) + Last Verified 표시. Version 자동 선택. |
| ⚠ 검증 실패: '입력한 ID가 유효하지 않습니다. 확인 후 다시 시도해 주세요.' |

|  |
| --- |
| 📋 Meddra 라이선스 버전 변경 흐름(Whodrug은 최신 버전 1개로 고정) |
| ① Version 드롭다운 클릭 → 지원 버전 목록 표시 |
| ② 원하는 버전 선택 |
| ③ [Save] 클릭 → 변경 저장 |
| ⚠ Verify 미완료 상태에서 Save 시: '라이선스 번호가 검증되지 않았습니다. 저장할 수 없습니다.' |

## 3.6 개발 요구사항

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| TA-LIC-01 | MedDRA ID 입력 필드 + Verify 버튼. 숫자만 입력. 빈값 허용. | 필수 | Admin-License |
| TA-LIC-02 | 검증 성공 시 Status(Active/Expired), Last Verified 표시 | 필수 | Admin-License |
| TA-LIC-03 | 검증 실패: '입력한 ID가 유효하지 않습니다. 확인 후 다시 시도해 주세요.' | 필수 | Admin-License |
| TA-LIC-04 | 다른 조직 등록 ID: '이 ID는 [회사명]에 등록되어 있습니다. 해당 조직의 구성원이십니까?' | 필수 | Admin-License |
| TA-LIC-05 | MedDRA Version 드롭다운. 최신 버전 자동 선택. 빈값 시 초기화. | 필수 | Admin-License |
| TA-LIC-06 | WHODrug License No. + Verify. MedDRA와 동일 로직. | 필수 | Admin-License |
| TA-LIC-07 | WHODrug Version: 최신 버전 자동 선택. | 필수 | Admin-License |
| TA-LIC-08 | Save: 변경 시만 활성. Verify 미완료 시 차단 + '라이선스 번호가 검증되지 않았습니다.' | 필수 | Admin-License |
| TA-LIC-09 | 1주일 주기 자동 유효성 체크. Last Verified 갱신. | 필수 | Admin-License |

# 4. 사용량 조회

## 4.1 개요

Org 내 계정, App, Workspace의 사용 현황 및 한도를 조회하는 메뉴이다. 조회 전용이며 설정 변경은 불가하다.

## 4.2 계정 사용량

### 화면: 요약 카드

* 전체 Active 계정: N / 200 (프로그레스 바 또는 게이지). Viewer 미포함, 별도 표시.

### 화면: 역할별 현황 테이블

| 역할 | 현재 | 최대 |
| --- | --- | --- |
| Master Admin | N | 1 |
| Org Admin | N | 3 |
| App Admin | N | Workspace-App당 5 |
| App User | N | - |
| External User | N | 50 |
| Viewer | N | 5 |

* Master Admin은 Backoffice에서 지정. App Admin은 하단 Workspace 개설 현황에서 상세 확인.
* 전체 한도(200명)에 Viewer 미포함. Active, Locked 계정만 카운트.

## 4.3 앱 사용량

### 화면: 워크스페이스 별 앱 사용량

| Workspace | App | 계약 사용량 | 현재 사용량 | 초기화 시점 | 상태 |
| --- | --- | --- | --- | --- | --- |
| WS-Main | Safety DB | 1,000건 | 872건 | 2025.01.01 | 정상 |
| WS-Main | LITUS | 500건 | 512건 | 2025.01.01 | 초과 |
| WS-02 | Safety DB | 500건 | 230건 | 2025.06.01 | 정상 |

* 초과 시에도 서비스 사용 가능하나 시각적으로 구분. App 활성화 변경은 Backoffice Admin만 가능.

## 4.4 워크스페이스 개설 현황

### 화면: 워크스페이스 현황

| Workspace 이름 | 활성화 App 수 | App Admin 수 | 상태 |
| --- | --- | --- | --- |
| WS-Main | 3 / 10 | 2 | Active |
| WS-02 | 1 / 10 | 1 | Active |

* 현재 Workspace 수: N / 100 로 표시
* Workspace 추가는 Backoffice를 통한 계약 변경으로 처리 (안내 문구 표시)

## 4.5 화면 흐름

|  |
| --- |
| 📋 사용량 조회 흐름 |
| ① [사용량 조회] 메뉴 진입 → 계정 사용량 / 앱 사용량 / 워크스페이스 개설 현황 표시 |
| ② 계정 사용량: 요약 카드 + 역할별 현황 테이블 확인 |
| ③ 앱 사용량: Workspace-App별 계약/현재/초기화 시점/상태 확인 |
| ④ 워크스페이스: 현재 수 / 최대 + 목록 테이블 확인 |
| ※ 조회 전용. 설정 변경 불가. 한도 조정은 Backoffice를 통한 계약 변경 필요. |

## 4.6 개발 요구사항 ( ([Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword) 참고)

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| AP-01 | 역할별 계정 현황 + 전체 한도 표시 (Active, Locked 200명 기준 | 필수 | Admin-Usage |
| AP-02 | Workspace 수 현황 (N / 100). Workspace별 App Admin 현황. | 필수 | Admin-Usage |
| TA-USG-01 | Workspace-App별 사용량: 계약/현재/초기화 시점/상태. 초과 시 시각적 강조. | 필수 | Admin-Usage |
| AP-03 | 한도 80% 이상 경고 + 초과 시 '계약 변경이 필요합니다' 안내 | 추후 고려 | Admin-Usage |
| AP-04 | 한도 조정은 Backoffice를 통한 계약 변경으로 처리된다는 안내 문구 제공 | 추후 고려 | Admin-Usage |

# 5. 오딧 로그

## 5.1 개요

Org 내 관리자 작업 이력을 조회하는 메뉴이다. 상세 정책 및 로그 항목은 [Audit Log, Activity Log, Audit Trail](https://selta.atlassian.net/wiki/spaces/IS/pages/25296917/Audit%2BLog%2BActivity%2BLog%2BAudit%2BTrail) 를 참조한다.

# 6. 워크플로우

해당 기능은 고도화에 상세 내용이 추가 될 예정.

# 7. 기준 정보 설정

## 7.1 개요

Org 내 ICSR 처리에 필요한 기준 정보(Product, Sender, Receiver, Study 등)를 관리하는 메뉴이다. 상세는 별도 [Company Config](https://selta.atlassian.net/wiki/spaces/IS/pages/23527439/Company%2BConfig) 를 참조한다.

* Org Admin에서는 Company Config로 설정 할 수 있어야 한다.

# 8. ICSR 설정

## 8.1 개요

ICSR 케이스 관련 설정을 관리하는 메뉴이다. 상세는 별도 [ICSR Config](https://selta.atlassian.net/wiki/spaces/IS/pages/22904852/ICSR%2BConfig) 를 참조한다.

* Org Admin에서는 ICSR Config로 설정 할 수 있어야 한다.

# 9. 공지사항

## 9.1 개요

Master Admin / Org Admin이 Org 내 Workspace 사용자에게 공지사항을 작성·관리하고, 노출 여부를 제어하는 메뉴이다.

## 9.2 권한

| 기능 | Master Admin | Org Admin |
| --- | --- | --- |
| 공지사항 작성 | ✓ | ✓ |
| 공지사항 목록 조회 | ✓ | ✓ |
| 노출/미노출 설정 | ✓ | ✓ |
| 공지사항 삭제 | ✓ | ✓ |

## 9.3 정책

* 공지사항 목록은 최신 작성순(내림차순) 정렬. 최대 10개 노출.
* 노출/미노출 설정은 토글 방식. 작성 완료 글에 한하여 설정 가능. 변경 즉시 반영.
* 파일 첨부 지원. 이미지: 작성 화면 인라인 표시, 일반 파일: 파일명 표시.
* 삭제된 공지사항은 복구 불가.

## 9.4 화면 흐름

|  |
| --- |
| 📋 공지사항 작성 흐름 |
| ① [공지사항] 메뉴 진입 → 공지사항 목록 화면 |
| ② [+ 공지사항 작성] 버튼 → 작성 폼 (제목, 내용), 노출할 워크스페이스 선택 |
| ③ [저장] → 목록 최상단 추가 (기본 노출 상태) |

|  |
| --- |
| 📋 공지사항 삭제 흐름 |
| ① 대상 공지사항 행 [삭제] 클릭 |
| ② 확인 모달: '삭제된 공지사항은 복구되지 않습니다. 계속하시겠습니까?' |
| ③ [확인] → 삭제 완료 |

## 9.5 개발 요구사항

| ID | 요구사항 | 우선순위 | 화면 ID |
| --- | --- | --- | --- |
| TA-NTC-01 | 공지사항 목록: 최신순, 최대 10개 노출 | 필수 | Admin-Notice |
| TA-NTC-02 | 작성 폼: 제목, 내용, 파일 첨부, 노출할 워크스페이스 선택 | 필수 | Admin-Notice |
| TA-NTC-03 | 노출/미노출 토글. 변경 즉시 반영. | 필수 | Admin-Notice |
| TA-NTC-04 | 삭제: 확인 모달 후 처리. 복구 불가. | 필수 | Admin-Notice |

# Part 2: App Admin

# 10. 개요

App Admin은 Workspace-App 단위의 운영 설정을 조회하는 메뉴이다. Org Admin에서 설정된 내용을 App 범위 내에서 확인할 수 있다. 설정 변경 권한은 없으며 조회 전용이다.

| 메뉴 | 설명 | **일정** |
| --- | --- | --- |
| 기준 정보 조회 | Org 레벨 기준 정보를 App 범위에서 조회 | 최우선 |
| ICSR 설정 조회 | Org 레벨 ICSR 설정을 App 범위에서 조회 | 최우선 |
| Audit Log | Workspace-App 범위 관리자 작업 이력 조회 | 최우선 |

# 11. 기준 정보 조회

Org 레벨에서 설정된 기준 정보를 해당 App 범위 내에서 조회한다. 상세는 별도 [Company Config](https://selta.atlassian.net/wiki/spaces/IS/pages/23527439/Company%2BConfig) 를 참조한다.

* App Admin에서는 설정되어 있는 Company Config 정보를 조회만 할 수 있다.
* 실제 App에서는 설정된 Company Config를 케이스 입력 시 활용 할 수 있다.

# 12. ICSR 설정 조회

Org 레벨에서 설정된 ICSR 설정을 해당 App 범위 내에서 조회한다. 상세는 별도 [ICSR Config](https://selta.atlassian.net/wiki/spaces/IS/pages/22904852/ICSR%2BConfig) 를 참조한다.

* App Admin에서는 설정되어 있는 ICSR Config 정보를 조회만 할 수 있다.
* 실제 App에서는 설정된 ICSR Config를 케이스 입력 시 활용 할 수 있다.

# 13. Audit Log

해당 Workspace-App 범위의 관리자 작업 이력을 조회한다. 상세 정책 및 로그 항목은 [Audit Log, Activity Log, Audit Trail](https://selta.atlassian.net/wiki/spaces/IS/pages/25296917/Audit%2BLog%2BActivity%2BLog%2BAudit%2BTrail) 를 참조한다.

# 14. 고도화 요구사항

## 14.1 External User, Viewer

* External User, Viewer는 고도화 시점에서 초대 가능

  + 상세 내용은 [Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword#9.1-External-User) , [Account (+Login, Password)](https://selta.atlassian.net/wiki/spaces/IS/pages/23822337/Account%2BLogin%2BPassword#9.2-Viewer) 참고
* Viewer

  + AP-01: Viewer는 전체 한도(200명)에 미포함, 별도 표시 (AP-01 이월)
