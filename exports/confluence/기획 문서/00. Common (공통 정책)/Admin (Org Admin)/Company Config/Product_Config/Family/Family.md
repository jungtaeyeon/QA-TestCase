|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획서 버전 |
| 김나정 | 26.04.15 | RSI 엑셀 템플릿 업로드 다운로드 삭제 (고도화로 미룸) | v1.0 | v1.0.260415 |
| 김나정 | 26.04.07 | Comment 카테고리 이동 | v1.0 | v1.0.260407 |
| 김나정 | 26.03.26 | 중복 불가 지정 | v1.0 | v1.0.260326 |
| 김나정 | 26.03.24 | RSI 삭제 시 안내문구 표시 | v1.0 | v1.0.260324 |
| 김나정 | 26.03.06 | 최초 작성 | v1.0 |  |

# 설계 목적 및 핵심 가치 (URS 반영)

* 코딩 정확성 제고: 사전 설정된 허가 및 코드 정보(성분, 제형 등)를 통해 의약품 코딩 오류를 방지
* 단일 귀결: 국가/파트너사별로 제각각인 보고 명칭(Reported Name)을 자사 표준 제품 계층으로 매핑하여 데이터 통합 분석 기반을 마련합니다.
* 해당 레벨에서는 다음 정보를 관리

  + 성분/브랜드에 속하는 데이터 사전 관리
  + RSI 관리

# 입력 필드

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 카테고리 | 영문 필드명 | 한글 필드명 | 필수 여부 | 매칭 R3필드 | 비고 | Validation |
| - | Product Family Name | 제품군 명칭 | 필수 | NA | 중복 불가 | 최대 100자 |
| Key Ingredients | Active Pharmaceutical Ingredient | 주성분 | 필수 | G.k.2.3.r.1 | 연결된 dictionary 정보 필요  최소 1개는 남아 있어야 함. 삭제 버튼이 2개부터 활성화  API 연동해서 처리 | R3 검증 룰을 따름 |
| RSI Data Sheet | Preferred Term | 기본 용어 (PT) | 옵션 | NA | 입력 필드가 아니라 항목 탭인데, 해당 기능 필요 | 최대 50자 |
| Datasheet Name | 데이터시트 명칭 | datasheet 생성 시 필수 | NA | 데이터시트 추가시 이름 지정 기능 | 최대 30자 |
| ~~Include~~ |  |  | ~~NA~~ | ~~이후 의약품에서 Mapping하는데 표시될 목록에 표시하는 기능~~ |  |
| Active Check Box | 활성화 여부 | 옵션 | NA |  |  |
|  | Comment | 추가 사항 | 옵션 | NA |  | 최대 5000자 |

# Key Ingredients 주성분 입력

* GSRS api를 연동하여 표준 성분명만 입력하도록 강제
* <https://gsrs.ncats.nih.gov/api-documentation>

### 추천 프로세스 (검증 필요)

사용자가 성분명을 입력할 때 API가 작동하는 흐름

1. Input: 사용자가 성분명 입력 (예: Acetaminophen)
2. Request: GSRS API의 substances/search 엔드포인트 호출

   * [q=names.name](http://q=names.name):"Acetaminophen" (정확한 매칭 검색)
3. Filter: 결과 데이터(JSON) 내의 names 배열을 루프로 돌림
4. Extract: displayName이 true이거나 type이 INN인 텍스트만 추출하여 사용자에게 '표준명'으로 제시
5. Save: 사용자가 이를 선택하면, 표준명 표시

# RSI 작동 명세

제품(Product)의 특성에 따라 적용되는 작동 방식이 분리된 자동-수동 투트랙 정책을 적용. **하지만 현 v1.0에서는 수동 방식만 채택하여 개발**

## 설계 개요

* 대상 레벨: 레벨 1. Family (성분/브랜드군)
* 목적: 해당 Family에 속한 모든 하위 제품(Product) 및 라이선스(Licenses)가 공통으로 참조할 예측성 평가 기준(Expectedness Reference)을 수동으로 구축함.
* 주요 방식:

  1. 개별 코딩: UI 상에서 MedDRA Browser 팝업을 통해 직접 입력.
  2. 일괄 템플릿: 엑셀 업로드를 통해 대량의 PT(Preferred Term) 리스트를 한 번에 등록.

### RSI 마스터 상세 UI 구성

화면 상단에는 RSI의 버전과 속성을 정의하고, 하단 그리드에서 실제 Term 리스트를 관리.

## RSI Data Sheet 영역 구성 목록

화면 상단에는 RSI의 버전과 속성을 정의하고, 하단 그리드에서 실제 Term 리스트를 관리

|  |  |  |
| --- | --- | --- |
| **필드명** | **형식** | **설명** |
| Datasheet Name | Text | RSI 문서 명칭, RSI 테이블 탭으로 설정 |
| Acitve | Checkbox | 이후 의약품에서 Mapping하는데 표시될 목록에 표시하는 기능 |
| Effective Date | Date | 해당 RSI가 실제 효력을 발생하는 날짜 (Expectedness 판정 기준일)  current date, other date 중 선택 가능. other date 선택 시 날짜 선택 가능. |

### RSI 그룹 관리

* RSI는 그룹 단위로 관리되며, 한 Family 내에 N개의 그룹을 생성할 수 있다
* 그룹은 생성 순으로 표시
* 각 그룹은 이름(Datasheet Name)과 유효일자(Effective Date)를 가진다
* Include 설정의 의미:

  + Include 체크는 "이 그룹이 현재 케이스 생성/편집 시 List에 나타날 것인가"를 결정하는 활성화 여부

### Active Check & Effective Date 작동 로직

* Active Check의 의미: 해당 RSI 레코드가 시스템에서 '사용 가능한 상태(Enabled)'인지를 나타내는 스위치. 비체크 시 아래의 작동원리와 상관 없이 inactive 상태 유지
* 케이스에서 Product 정보 불러올 경우 표시되는 정보
* 시스템 작동 원리:

  1. 사용자가 RSI를 등록하고 Effective Date를 미래 날짜로 설정하면, 현재 상태는 Inactive
  2. 서버 시간 기준으로 해당 Effective Date가 도래하는 순간, 시스템이 자동으로 해당 RSI를 Active 상태로 전환

### RSI 삭제 시

* RSI그룹에 매핑되어 있는 Licenses가 있는데 삭제할 경우 안내 문구 표시

  + 메시지: "해당 RSI그룹에 연결된 Licenses가 있습니다. 정말 삭제하시겠습니까?"

### RSI 리스트 관리 그리드 (Vaidation은 기존 MedDR에 적용되었던 룰을 따름)

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **No** | **컬럼** | **데이터 형식** | **필드 속성** | **비고 및 제약 조건** |
| 1 | # (No) | Number | Auto | 리스트 내 행 순번. (정렬 기준)  생성 순으로 번호 부여 |
| 2 | MedDRA Term (PT) - English | String | Required | MedDRA 표준 Preferred Term 영어 명칭. |
| 3 | MedDRA Term (PT) -Korean | String | Required | MedDRA 표준 Preferred Term 한글 명칭. |
| 4 | MedDRA Code | String(8) | Required | PT에 매핑된 8자리 고유 숫자 코드. |
| 5 | MedDRA Version | Select | Required | 해당 데이터 입력/검색 시 적용된 MedDRA 사전 버전 (예: v26.1) |
| 6 | Action | Button (delete) | - | [삭제] 버튼 (저장 전까지는 행 삭제, 저장 후에는 이력 관리 대상). |
| Button (Modify) |  | [수정]버튼, 이미 입력한 정보 수정. 클릭 시 팝업을 통한 MedDRA 코드 입력 |

## 자체 RSI 관리 정책

Level 1 (성분/브랜드군)에 종속

* 관리 및 매핑: Level 1(성분/브랜드)에서 문서 및 텍스트를 수동 등록. 동일 브랜드 하위의 모든 Level 2, 3 제품들은 이 수동 문서를 공통으로 공유함.
* 케이스 입력/수정 UI 연동: 실무자가 ICSR 케이스 생성/편집 화면에서 제품 불러오기를 선택하면, 해당 제품이 속한 Level 1에 저장된 '수동 RSI 버전 리스트'가 노출됨. 실무자가 케이스 발생 시점에 맞는 버전을 직접 클릭하여 선택해야 평가를 진행할 수 있음. → **케이스 입력/수정 화면에서 더 자세히 설명**

### MedDRA 버전의 일관성

* MedDRA 버전의 일관성

  + 기존 입력된 MedDRA 버전과 다른 버전이 입력될 경우 시각적으로 표시
  + 이미 등록된 행의 버전과 현재 시스템 버전이 다를 경우 시각적 경고 아이콘을 표시하여 재검토 유도
* 중복 체크 및 유효성 검사

  + 중복 방지: 동일한 MedDRA Code가 이미 그리드에 존재할 경우, 추가 시점에 "이미 등록된 용어입니다"라는 토스트 메시지와 함께 입력을 차단

## 입력 방식 상세 로직

### 방식 1: 직접 코딩

1. 사용자가 RSI 그리드 상단의 [Add Term] 버튼을 클릭
2. MedDRA Browser 팝업이 호출
3. 사용자가 단어 검색 후 특정 term를 선택하면 그리드에 `Term`, `Code`, `Version`이 자동으로 한 줄 추가
4. MedDRA 라이센스가 만료됐을 경우 자유 기재

### 방식 2: 일괄 Template 업로드 [추후 고도화 예정]

1. [Template Download] 버튼을 통해 정해진 규격의 엑셀 파일 다운로드
2. 엑셀 내에 안내된 양식대로 작성
3. [Upload Template] 버튼을 통해 파일을 업로드

Template:

셀타스퀘어\_템플릿

.xlsx

.xlsx

# 와이어 프레임

![](https://t37003623.p.clickup-attachments.com/t37003623/193c51a6-c895-418c-b89e-d143ad6a4ef4/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | 1. 복합제(두 가지 이상의 성분이 섞인 약) 등록 시 주성분을 여러 개 입력할 수 있도록 입력 폼 추가 | 1. 해당 버튼 클릭 시 하단에 주성분 및 관련 코드를 입력할 수 있는 빈 행이 1줄 추가 2. 텍스트 필드에 입력할 경우, api 연동으로 성분 표준명 불러와 매칭 여부 확인 |
| 2 | 1. Delete (성분 삭제) 2. 불필요하거나 잘못 추가된 주성분 입력 행을 목록에서 제거 | 1. 휴지통 아이콘 클릭 시 삭제 |
| 3 | 1. RSI 그룹 탭. RSI 그룹 설정 | 1. 탭 선택 시 해당 그룹으로 이동 2. +버튼 추가 시 새 그룹 추가 |
| 4 | 1. 현재 선택된 탭의 RSI 문서 명칭 정의 | 1. 텍스트 필드에 직접 입력 2. 입력된 값은 하단 탭 메뉴의 이름과 동기화 |
| 5 | 1. Effective Date (효력 발생일) 2. 해당 RSI 그룹이 케이스 평가에 실제로 적용되기 시작하는 시스템상의 기준일 | 1. 텍스트 필드 영역 클릭 시 캘린더 팝업이 표시. 날짜 선택 가능 2. 상단의 'Active Check & Effective Date 작동 로직' 참조 |
| 6 | 1. Active(활성화/목록 표시) 2. 케이스 생성 시, 해당 RSI 그룹을 선택 리스트에 노출할지 결정하는 마스터 스위치 | 1. 체크 시 활성화 대기 상태 2. ~~Effective Date 도래 시 included로 상태 변경~~ 3. 체크 해제 시 하위 단계의 매핑 선택 리스트에서 숨김 처리 4. 상단의 'Active Check & Effective Date 작동 로직' 참조 |
| 7 | 템플릿 다운로드 | 1. 클릭 시 템플릿 다운로드 가능. 다운로드 파일은 상단의 '셀타스퀘어\_템플릿' 파일\* Active Check & Effective Date 작동 로직 |
|  | 템플릿 업로드 | 1. 업로드 버튼 클릭 시 팝업 표시. 2. 팝업: 버전 선택 드롭다운+파일 업로드 영역 포함. 3. 업로드 완료 시 템플릿 컬럼을 Term 리스트에 매핑하여 표시 4. 버전=version 5. MedDRA PT Code=MedDRA Code 6. 국문명=MedDRA Term (PT)-Korean 7. 영문명=MedDRA Term (PT)-English |
| 8 | Term 추가 | 1. 버튼 클릭 시 MedDRA 검색 팝업 표시. 2. 검색 팝업에서 설정한 버전, Term, 코드가 리스트에 그대로 입력 |
| 9 | 1. MedDRA 버전 표시 2. 후에 입력한 버전이 최초 입력한 버전과 다른 버전일 경우 경고 표시. 하지만 강제적으로 버전을 조절하지 않음 | - |

## 참고

신경쓰지 말아주세요. 추후 넣을 필드 및 공부용..

![](https://t37003623.p.clickup-attachments.com/t37003623/aa527f9a-f5df-41e0-b591-b8667fdf5d73/image.png)
