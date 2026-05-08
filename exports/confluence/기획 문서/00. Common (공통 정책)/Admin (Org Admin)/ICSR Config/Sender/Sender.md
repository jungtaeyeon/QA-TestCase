|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 2026.03.20 | Batch Sender Identifier 하위에 필드 소속되는 것으로 수정 | v1.0 | v1.0.260320 |
| 김나정 | 2026.03.17 | Workspace Sender 추가 및 일부 수정 | v1.0 |  |
| 김나정 | 2026.03.09 | 추후 개발 삭제, 와이어프레임 기능 명세 구체화 | v1.0 |  |
| 김나정 | 2026.02.19 | 최초 작성 | v1.0 |  |

# 개요

* 목적: 모든 보고서의 발신자 정보를 일관성 있게 유지하고, 특히 국가별로 상이한 Sender ID(N.1.3)를 체계적으로 관리하여 보고 정합성을 극대화함.
* 기대효과:

  + 국가별 규제기관 대응력 강화
  + 반복적인 대량 입력 작업의 자동화

# 판매 및 운영 전략

* 국내 시장 (KR): 당사의 CRO 서비스 경쟁력 보호를 위해 제약사 중심으로 제품을 판매하며, 고객사당 단일 Sender 정보만 사용하도록 제한함.
* 해외 시장 (Global): 제약사 및 CRO 업체 대상 판매를 허용하며, 해외 CRO가 다수의 위탁사(Client) 정보를 관리할 수 있도록 프로젝트별 독립적 Sender 설정 기능을 제공함.
* 현재는 국내 시장만 타깃으로 하여 해외시장은 고려하지 않음. 다만 확장적으로 설계 필요. CRO는 타겟으로 하여 테넌트 정보 계승 유무는 설정 가능해야 함

# 시스템 설정 및 상속 로직

### 계층별 설정 규칙

1. Tenant Level: 전체 시스템의 기준이 되는 마스터 Sender 정보(최대 1개)를 설정함.
2. Workspace Level: 테넌트의 국가 속성에 따라 상속 정책이 자동 결정됨.

|  |  |  |
| --- | --- | --- |
| **구분** | **국내** | **국외** |
| Target | 제약사 | 제약사, CRO |
| 상속 옵션 | Tenant 정보 강제 계승 (Mandatory) | 상위 계승 vs 자체 설정 선택 가능 (Optional) |
| 변경 권한 | Workspace 단위 수정 불가 (Read-only) | 권한에 따라 Workspace별 독립 설정 가능 |
| 비즈니스 목적 | 1 고객사 = 1 Sender 정체성 유지 | CRO 업체의 멀티 고객사 대행 업무 지원 |

# ICSR 필드별 매핑

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ICSR 필드명 한글** | ICSR 필드명 영어 | **속성** | **비고** | **연결 R3 ID** |
| 배치 보고자 ID | Batch Sender Identifier | Required | 1. 각 국가(규제기관)마다 부여받는 식별자가 다르므로, 국가별로 1:1 매핑하여 관리 2. 설정 규칙: Tenant 내에서 국가별로 유니크한 ID 1개 등록 (예: KR:MFDS+ID, US:FDA+ID 등). 3. 동일한 국가 및 ID가 설정되지 않도록 밸리데이션 수행 4. 워크스페이스당 보고자 ID 한 개 | N.1.3 |
| 보고자 구분 | Sender Type | Required | 1. 발신자 유형 코드 매핑 2. 제약회사로 설정했을 경우 보고자 구분은 1을 디폴트로 고정 | C.3.1 |
| 보고자의 조직 | Sender’s Organisation | Conditional | C.3.1이 '7(Patient)'이 아닐 경우 필수 | C.3.2 |
| 보고자의 부서 | Sender’s Department | Optional |  | C.3.3.1 |
| 보고자의 직위 | Title | Optional |  | C.3.3.2 |
| 보고자의 이름 | Given Name | Optional |  | C.3.3.3 |
| 보고자의 중간 이름 | Middle Name | Optional |  | C.3.3.4 |
| 보고자의 성 | Family Name | Optional |  | C.3.3.5 |
| 보고자의 주소(상세주소) | Street Address | Optional |  | C.3.4.1 |
| 보고자의 주소(도로명과 번호) | City | Optional |  | C.3.4.2 |
| 보고자의 주소(특별시,광역시,도 등) | State or Province | Optional |  | C.3.4.3 |
| 보고자의 주소(우편번호) |  | Optional |  | C.3.4.4 |
| 보고자의 주소(국가코드) | Country Code | Optional |  | C.3.4.5 |
| 보고자의 전화번호 | Telephone | Optional |  | C.3.4.6 |
| 보고자의 팩스번호 | Fax | Optional |  | C.3.4.7 |
| 보고자의 이메일 | E-mail | Optional |  | C.3.4.8 |

### 배치 보고자 ID 추가시 (추후)

* 국가 규제기관에 따른 배치 보고자 ID 추가 시 Add버튼을 클릭하여 추가
* 규제기관(MFDS, FDA, EMA) 선택 후 text field에 배치 보고자 ID 기재

  + 규제기관 선택 시 이미 한 번 설정한 규제기관 코드는 표시되지 않음
  + 드롭다운시 순서는 MFDS, FDA, EMA
  + 현재 버전에서는 MFDS만 표시, 추후 FDA, EMA 추가 시 표시 예정

## Validation 확인

[Connect your account to see a preview](https://seltaglobal.sharepoint.com/%3Ax%3A/r/sites/RDDivision/_layouts/15/Doc.aspx?sourcedoc=%7B24542AC4-CE17-42EF-9EDB-924935E5454D%7D&file=%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%86%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%87%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%B3%E1%86%BC%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%89%E1%85%A1%E1%84%85%E1%85%A8%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A7%E1%86%AF%20%E1%84%92%E1%85%A1%E1%86%BC%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%8C%E1%85%B3%E1%86%BC%20%E1%84%85%E1%85%AE%E1%86%AF.xlsx&action=default&mobileredirect=true)

[Connect](https://seltaglobal.sharepoint.com/%3Ax%3A/r/sites/RDDivision/_layouts/15/Doc.aspx?sourcedoc=%7B24542AC4-CE17-42EF-9EDB-924935E5454D%7D&file=%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%86%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%87%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%B3%E1%86%BC%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%89%E1%85%A1%E1%84%85%E1%85%A8%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A7%E1%86%AF%20%E1%84%92%E1%85%A1%E1%86%BC%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%8C%E1%85%B3%E1%86%BC%20%E1%84%85%E1%85%AE%E1%86%AF.xlsx&action=default&mobileredirect=true)

[SharePoint](https://seltaglobal.sharepoint.com/%3Ax%3A/r/sites/RDDivision/_layouts/15/Doc.aspx?sourcedoc=%7B24542AC4-CE17-42EF-9EDB-924935E5454D%7D&file=%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%86%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%87%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%B3%E1%86%BC%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%89%E1%85%A1%E1%84%85%E1%85%A8%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A7%E1%86%AF%20%E1%84%92%E1%85%A1%E1%86%BC%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%8C%E1%85%B3%E1%86%BC%20%E1%84%85%E1%85%AE%E1%86%AF.xlsx&action=default&mobileredirect=true)

[seltaglobal.sharepoint.com/:x:/r/sites/RDDivision/\_layouts/15/Doc.aspx?sourcedoc=%7B24542AC4-CE17-42EF-9EDB-924935E5454D%7D&file=%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%86%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%87%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%B3%E1%86%BC%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%89%E1%85%A1%E1%84%85%E1%85%A8%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A7%E1%86%AF%20%E1%84%92%E1%85%A1%E1%86%BC%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%8C%E1%85%B3%E1%86%BC%20%E1%84%85%E1%85%AE%E1%86%AF.xlsx&action=default&mobileredirect=true](https://seltaglobal.sharepoint.com/%3Ax%3A/r/sites/RDDivision/_layouts/15/Doc.aspx?sourcedoc=%7B24542AC4-CE17-42EF-9EDB-924935E5454D%7D&file=%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%86%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%87%E1%85%A1%E1%86%AB%E1%84%8B%E1%85%B3%E1%86%BC%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%89%E1%85%A1%E1%84%85%E1%85%A8%20%E1%84%80%E1%85%A2%E1%84%87%E1%85%A7%E1%86%AF%20%E1%84%92%E1%85%A1%E1%86%BC%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%8C%E1%85%B3%E1%86%BC%20%E1%84%85%E1%85%AE%E1%86%AF.xlsx&action=default&mobileredirect=true)

* 해당 링크에서 '항목 검증룰' 확인 필요

# Batch Sender Identifier 하위 그룹으로 필드 데이터 관리 필요

* Batch Sender Identifier에 따라 contact point가 다르므로 각 Batch Sender Identifier에 모든 필드를 종속시켜 그룹화하여 관리해야 함

  + Batch Sender Identifier가 추가될때마다 하위 그룹 필드 데이터를 관리해야 함

    - 멀티 레코드 관리: `+ Add Identifier` 버튼을 통해 미국(FDA), 한국(MFDS) 등 국가별 보고 정보를 독립적으로 추가 및 관리 가능
    - Batch Sender Identifier를 클릭하면 하위 그룹 필드 데이터가 표시 (ex FDA 선택 시 영어로 입력된 데이터가 표시)
  + Batch Sender Identifier를 제외한 다른 필드들의 데이터 복사 붙여넣기 가능 필요

    - 화면 상단에 복사 버튼을 넣어 필드 전체 복사 및 붙여넣기 가능하도록

# 와이어프레임

![](https://t37003623.p.clickup-attachments.com/t37003623/3bfe9bd3-efe4-45c3-b4b4-3f16b3a9a31c/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 [고도화 예정] | 1. 국내 제약사의 경우 표시되지 않음. 자도으로 테넌트 정보 계승 2. 디폴트: on 3. 테넌트\_Admin\_Conpany Config에서는 표시되지 않음 | 1. 클릭 시 on/off 설정 가능 2. on으로 설정할 경우: 테넌트의 sender 정보를 계승하고 sender date 전부 read-only 표시 3. off에서 변경 시: 저장한 모든 정보가 삭제됩니다. 변경하시겠습니까? 얼럿 표시 필요 (버튼: cancel, confirm) 4. off로 설정할 경우: on 상태의 값을 그대로 text-field에 넣고 수정 가능으로 변경 |
| 2 [고도화 예정] | 1. 상속 안내 문구 2. 국내 제약사의 경우 표시되지 않음. 자동으로 테넌트 정보 계승 3. 테넌트\_Admin\_Conpany Config에서는 표시되지 않음 | - |
| 3 | 1. Batch sender ID 등록 2. 규제기관별 ID 1:1 설정 3. 디폴트: Regulatory Authority=MFDS로 선택된 한개의 입력 창 표시 4. Regulatory Authority는 드롭다운으로 규제기관 선택 가능 5. 현재는 MFDS만 등록 가능 | 1. Add Idenfier클릭 시 ID 입력 란 추가 2. 규제기관(Regulatory Authority) 드롭 다운 클릭 시 규제기관 선택 가능 3. 이미 선택한 규제기관은 표시되지 않음 4. MFDS선택 시 텍스트필드에 'MFDS-'가 디폴트로 표시 |
| 4 | 1. Batch Sender ID에 따라 소속이 바뀜 | 1. Batch Sender ID 클릭 시 소속된 필드값이 표시됨 |

* Tenant에서의 sender정보는 빈칸으로 표시

  + Save 버튼 클릭 후 저장된 값이 있을 경우 페이지에 저장된 값이 표시

# 요구사항

## UX/UI

### Sender 설정 관리 화면 (Admin Console)

* 필드명에 R3 필드 기재하지 말고 ICSR 필드명만 기재, 한영 병기 기재
* 국가별 Sender ID: [국가 - Sender ID]를 1:1로 매핑하여 추가/수정하는 리스트 제공.
* 국내 제약사인 워크스페이스의 Sender의 경우 Read-only 표시
* 상속 토글 (Inheritance Toggle):

  + 국내(KR) 제약사: '상위 계승' 상태로 고정 및 비가시화(보이지 않음).
  + 국외(Global): 토글 On/Off 선택권을 부여하여 프로젝트별 개별 설정 지원.
* C.3.2 조건부 필수 UI:

  + 실시간 반영: C.3.1 값이 '7(Patient)'로 선택되는 즉시 C.3.2 필드의 필수 표시가 사라지며, 유효성 검사 대상에서 제외됨.

## 개발 설계

* 배치 보고자 ID: 국가별 유니크함 보장.
* 국내 제약사인 워크스페이스의 Sender의 경우 Read-only 표시
