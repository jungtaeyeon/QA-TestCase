|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.07 | blinding 명칭 수정 | v1.0 | v1.0.260407 |
| 김나정 | 26.03.19 | 최초 작성 | v1.0 | v1.0.260319 |

# 입력 필드

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 카테고리 | 필드 영문명 | 필드 국문명 | 필수 여부 | 매칭 R3필드 | 비고 | Validation |
| Part | Part Title | 파트 명칭 | 필수 | N/A | 1. 번호로 자동 부여 (ex part1, part2) |  |
|  | Blinding | 연구/맹검 유형 | 필수 | N/A | Open-Label, Single Blind, Double Blind |  |
| Arm | Arm Title | 군 명칭 | 필수 | N/A | 1. Part 번호-Arm type & Arm 행 번호(자동 부여):​ 2. 추가된 행에 Arm Type으로 구분해서 자동생성 (예. Part01-Experimental Arm 01​ |  |
|  | Primary License | 대표 라이선스 (주요 제품) | 옵션 | N/A | 보고할 제품 선택  리스트는 Product list에 있는 제품 하위 Licenses에서 불러와서 표시 |  |
|  | arm Type | 군 구분 (암 유형) | 옵션 | N/A | 1. Experimental arm (시험군) 2. Active comparator arm (활성대조군) 3. Placebo comparator arm (위약대조군) 4. Sham comparator arm (유사처치군) 5. Standard of Care arm (표준치료군) 6. Reference arm (참조군) 7. No intervention arm (비투여군) 8. Observation arm (관찰군) |  |
|  | Blinded (체크박스) | 맹검 여부 | 옵션 | G.k.2.5 (맹검 시 true로 체크) | Study Type에서 Not Blinded 선택 시 비활성화 |  |
| Treatment | Treatment No | Treatment 번호 | 필수 | N/A | 연동, Part&Arm에서 승계. Part&Arm에서 없는 Product 표시되지 않음 |  |
|  | Products | 관련 의약품 | 필수 | N/A | Product List에서 입력한 Products 중 선택하여 연결 |  |

# 그리드 매트릭스

이 페이지는 7단계 하이라키 중 중간 4개 계층(Part, Arm, Period, Treatment)을 하나의 매트릭스로 통합하여 관리

* 행 = Arm (피험자 군): 시험군(Experimental), 대조군(Comparator) 등 환자 그룹을 정의
* 열 = Period (시간적 구분): Day 1-7, Cycle 1 등 임상의 시간 흐름을 정의
* 셀 = Treatment (투약 요법): 특정 군이 특정 시기에 받는 치료(약물 조합)를 배치

# 맹검(Blind) 및 해제(Unblinding) 메커니즘

* Blinded 설정: Study Design 그리드의 각 Arm(행)별로 Blinded 체크박스를 제공. 이 체크 여부는 G.k.2.5 필드값(맹검 시 true)의 기초 데이터
* Case 레벨 Unblinding:

  + 추후 Case 입력 시 SUSAR(예상치 못한 중대한 이상반응) 등이 발생할 경우, 해당 특정 케이스에 대해서만 맹검을 해제하여 상세 평가를 진행
* Study Status 연동: 전체 임상이 `Close` 상태가 되면 blinded 처리되었던 arm에 속한 Product 오픈 가능 상태로 전환

# Study 전용 'Product List' 운영 로직

Study Design 그리드에 직접 매핑하기 전, '완충 지대' 역할을 하는 페이지

* Product List는 Study Design에 종속된 리스트로, 해당 Project 하위의 데이터에만 매핑됨
* 데이터 소싱: Product Master Level 3 (Licenses) 전체 리스트 중, 현재 임상 시험에 투여되는 약물들만 선택하여 'Study 전용 리스트'를 구축합니다.
* Licenses에서 연동되지 않을 경우 WHODrug 제품 코드로 제품 입력
* Product List와 동기화:

  + Product List에서 'Update'버튼 클릭할 경우 연계된 최신 정보로 업데이트, 해당 정보가 그대로 Study Design에 반영
* Design 연동: Study Design의 `Study Drug` 셀에서는 이 페이지에서 미리 확정해둔 약물 리스트만 드롭다운으로 노출하여 오입력을 방지

## Additional Study Drug 맹검 예외 및 시각적 표시 로직

![](https://t37003623.p.clickup-attachments.com/t37003623/3f39bc56-f761-40da-b99c-9396ef42b1ba/image.png)

### ARM 단위로 Additioanl Study Drug 설정

* ARM 전체에 Additional Study Drug를 설정하고, 맹검 제외대상 안내문구 표시

#### 맹검 예외 작동 원리 (Unblinding Logic)

* 기본 원칙: Arm(행) 단위의 'Additional Study Drug'인 제품은 무조건 맹검 대상에서 제외
* Case 연동:

  + 케이스 입력 시, 맹검된 Arm이라 하더라도 Additional Study Drug로 분류된 제품은 제품명이 즉시 노출된 상태로 바인딩
  + 이는 연구자의 눈가림 해제(Unblinding) 절차 없이도 상시 확인 가능해야 하는 정보임을 의미

### 시각적 표시 가이드

사용자가 설계 단계에서 어떤 약물이 맹검 예외인지 직관적으로 알 수 있도록 UI 요소를 추가

* 그리드 내 표시 (P3. Study Design):

  + 아이콘 부착: 해당 제품 옆에 '열람 가능'을 상징하는 눈 모양 아이콘 또는 'Unblinded' 태그를 고정 표시

# Arm, Period, Treatment 그룹 작동 명세

## 계층별 정의 및 기능

|  |  |  |
| --- | --- | --- |
| **계층 (Level)** | **기능 및 작동 명세** | **자동화 및 제약 조건** |
| Part (L3) | 상위 개념: Arm, Period, Treatment를 포함하는 상위 설계 단위 | 1. 이름 부여: 'Part#' 형식으로 자동 부여(중복 불가)되며 수정 가능 2. 맹검 제어: 설정한 Blinding 에 따라 하위 Blinded 체크박스 활성화 여부가 결정 (예: Not Blinded 선택 시 비활성화) |
| Arm (L4) | 피험자 군 설정: 특정 치료를 받는 환자 그룹을 정의 | 1. 명칭 조합: [Part 번호]-[Arm Type]-[행 번호]를 조합해 자동 생성 (예: Part 01-Experimental Arm 01) 2. 맹검 설정: Arm 단위로 맹검 여부(Blinded)를 개별 설정 가능 3. Arm 한개만 맹검 설정(Blinded)할 경우 저장시 메시지 표시: "한 개의 arm만 맹검 설정(Blinded)되었습니다. 이대로 저장하시겠습니까?" (Confirm/cancel 버튼) |
| Period (L5) | 시간적 구분: Arm의 행에 추가되어 임상의 단계적 흐름을 구성하며 하위에 Treatment를 포함 | 1. 확장성: Period 1개당 하나의 Arm 셀에 하나의 Treatment를 설정하며, Period는 최대 5개까지 추가 가능 |
| Treatment (L6) | 투약 요법: 특정 군(Arm)이 특정 시기(Period)에 받는 실제 처방(약물 조합)을 배치 | 1. 복사/붙여넣기: 하위 Product 정보를 포함하여 다른 Period 열로 복사가 가능 |

### Treatment 의약품 연동 및 매핑 로직

* 최초 생성 상태: Treatment가 처음 생성될 때는 하위에 어떠한 Product도 연결되지 않은 빈 상태로 노출
* Product 호출: Treatment 그룹 내의 `+` 버튼을 클릭하면, 앞서 Product List 페이지에서 세팅한 제품 목록이 드롭다운으로 노출
* 데이터 바인딩: 선택된 제품은 Drug Name으로 표시되며, 해당 제품의 `Product Type`(시험약, 대조약 등) 속성을 함께 상속받음

### Treatment 명칭 및 중복 정책

* 중복 허용: 동일한 Study 내에서 동일한 이름의 Treatment(예: Treatment2)가 존재할 수 있음.
* 이름 기반 데이터 바인딩: Treatment의 이름이 동일하면, 그 하위에 연결된 의약품 리스트(Product List) 정보는 반드시 동일해야 함

  + 복사 붙여넣기로 연결된 Treatment 중 한곳이라도 이름 및 정보를 변경하면 다른 Treatment의 이름 및 정보가 동시에 같이 반영됨

|  |  |  |
| --- | --- | --- |
| **구분** | **작동 명세 및 인터랙션** | **비고** |
| 신규 생성 | 새로운 Treatment 명칭 입력 시, 하위에 제품이 연결되지 않은 상태로 생성 | 고유 명칭일 경우 |
| 중복 명칭 입력 | 이미 존재하는 Treatment 이름을 입력할 경우, 시스템은 해당 이름에 저장된 제품 리스트를 즉시 호출하여 해당 셀에 바인딩 | 자동 데이터 동기화 |
| 데이터 일괄 업데이트 | 여러 곳에 배치된 'Treatment2' 중 하나의 셀에서 제품 구성을 수정하면, 동일한 이름을 가진 모든 셀의 'Treatment2' 정보가 실시간으로 일괄 업데이트 | 정보의 동일성 유지 |
| 복사 및 붙여넣기 | 특정 Treatment를 복사하여 다른 셀에 붙여넣을 경우, 이름과 하위 제품 정보가 그대로 복제 | 편리한 그리드 설계 |

### 시각적 표시 및 유효성 검사

유효성 검사:

* 이름은 같지만 제품 구성을 다르게 하려는 시도는 시스템적으로 차단

# 와이어프레임

![](https://t37003623.p.clickup-attachments.com/t37003623/1944ae0b-20d3-44a3-8fa9-abd568e99725/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | Study Type 선택 | 1. 클릭 시 드롭다운으로 선택 2. Single Blind 3. Double Blind 4. Open-Label 5. Open-Label 선택 시 6번 비활성화 |
| 2 | + Arm (Row) 추가 | 1. 클릭 시 그리드 하단에 새로운 피험자 군(Arm) 행이 추가 2. 추가된 행의 `Arm Title`은 Part 번호, Arm Type, 행 번호를 조합하여 자동으로 생성 (예: Part 01-Experimental Arm 01). |
| 3 | + Period (Col) 추가 | 1. 클릭 시 그리드 우측에 새로운 시간적 구분(Period) 컬럼이 생성 |
| 4 | 군 유형 설정 | 1. 클릭 시 드롭다운하여 arm type 추가 2. Experimental arm (시험군) 3. Active comparator arm (활성대조군) 4. Placebo comparator arm (위약대조군) 5. Sham comparator arm (유사처치군) 6. Standard of Care arm (표준치료군) 7. Reference arm (참조군) 8. No intervention arm (비투여군) 9. Observation arm (관찰군) |
| 5 | Treatment 설정 | 1. Treatment 생성 시 자동으로 Treatment#으로 이름 생성 2. 이름 클릭 시 Treatment 이름 변경 가능 3. Copy 버튼으로 Treatment 복사 가능, 다른 treatmen영역에 그대로 붙여넣기 가능 (이름, 연결 product까지 동일) 4. Delete 버튼으로 Treatment 단위로 삭제 가능 5. Product List에 등록된 제품을 Treatment에 연결 가능. 클릭 시 Product List 팝업으로 표시 |
| 6 | 맹검 여부 설정 | 1. 각 Arm(행)별로 맹검 여부를 설정 2. 체크 시 G.k.2.5 필드값이 'true'로 저장 3. 상위 Study Type이 'Not Blinded'일 경우 이 체크박스는 비활성화 |
| 7 | Part Management | 1. 하단 탭을 통해 PART I, PART II 등 part에 해당하는 페이지 조회 가능 2. `+ Add Part` 클릭 시 새로운 파트가 생성되며 `Part Title`은 번호에 따라 'part1', 'part2' 등으로 자동 부여 3. 추가되는 Part는 사이드바 영역의 part에 표시 |

# 참고

신경쓰지 말아주세요. 추후 넣을 필드 및 공부용..

![](https://t37003623.p.clickup-attachments.com/t37003623/0ec0a839-7034-401e-b03b-2f131b910211/image.png)![](https://t37003623.p.clickup-attachments.com/t37003623/8635ae29-48cc-4630-aa51-84d7cb05cee8/image.png)
