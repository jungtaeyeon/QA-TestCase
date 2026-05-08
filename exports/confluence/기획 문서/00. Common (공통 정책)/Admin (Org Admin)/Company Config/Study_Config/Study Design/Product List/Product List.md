|  |  |  |  |
| --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 |
| 김나정 | 26.03.11 | 최초 작성 | v1.0 |

# 입력 필드

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 카테고리 | 필드 영문명 | 필드 국문명 | 필수 여부 | 매칭 R3필드 | 비고 | Validation |
|  | Study Drug Name | 임상 의약품명 | 필수 | N/A | 1. WHODrug으로 추가했을 경우, WHODrug 팝업창에서 Trade Name 입력 2. Product List에서 추가 시 Licenses의 Trade Name 입력 | 최대 250자 |
|  | Product Type | 의약품 유형 | 필수 | N/A | 1. 아래 다섯가지의 값 중 선택 2. Investigational Product 3. Comparator 4. Placebo 5. No Study Drug Given 6. Additional Study Drug | - |

# Study 전용 'Product List' 운영 로직

Study Design 그리드에 직접 매핑하기 전, '완충 지대' 역할을 하는 페이지

* Product List는 Study Design에 종속된 리스트로, 해당 Project 하위의 데이터에만 매핑됨
* 데이터 소싱: Product Master Level 3 (Licenses) 전체 리스트 중, 현재 임상 시험에 투여되는 약물들만 선택하여 'Study 전용 리스트'를 구축

  + Product Master Level 3 (Licenses)를 연동하는 시간 기준으로 해당 정보를 가지고 있음
* Licenses에서 연동되지 않을 경우 WHODrug 제품 코드로 제품 입력

### Additional Study Drug 불러올 경우

* Product List 연동 (P3. Product List):

  + 제품 유형(Type) 선택 시 'Additional Study Drug'를 선택하면, 해당 행에 "해당 타입은 맹검 처리되지 않습니다."이라는 안내 툴팁 또는 배지를 노출

### 최신 정보 업데이트

* Product List 상단에 'Update'버튼으로 연동된 Product Master의 Licenses 최신 정보로 동기화할 수 있음

  + Update 버튼 누르지 않으면 연동된 Product Master의 Licenses가 변경되더라도 최신 정보로 동기화하지 않음

# 와이어프레임

![](https://t37003623.p.clickup-attachments.com/t37003623/c8cad810-39c0-4894-8d68-c944a25429f9/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | 1. WHODrug 팝업을 사용해 Product List에 추가 | 1. 클릭 시 WHODrug 검색 팝업 추가 2. 검색 후 Study drug name에 Trade Name입력 |
| 2 | 1. Product 마스터 연동을 통해 Product List 추가 | 1. 클릭 시 Product Maseter Level 3(Licenses)리스트 팝업이 노출 2. 선택 시 Study Drug Name에 해당 라이선스의 Trade Name이 표시 |
| 3 | 1. 해당 의약품이 임상 시험 내에서 수행하는 역할(시험약, 대조약 등)을 정의 | 1. 클릭 시 드롭다운으로 선택 2. Investigational Product 3. Comparator 4. Placebo 5. No Study Drug Given 6. Additional Study Drug |
