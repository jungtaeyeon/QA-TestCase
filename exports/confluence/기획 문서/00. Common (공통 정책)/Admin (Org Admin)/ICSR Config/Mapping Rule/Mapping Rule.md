|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.03.25 | 최초 작성 | v1.0 | v1.0.260325 |
|  |  |  |  |  |

# 프로토타이핑

[링크](https://seltaglobal.sharepoint.com/sites/RDDivision/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype%2FICSR%20Config%5FMapping%20Rule%2Dv1%2Ehtml&parent=%2Fsites%2FRDDivision%2FShared%20Documents%2F01%2E%20DEV%2F%E2%97%88Prototype)

# 평과 결과 매핑 설정

## 개요 및 목적

* 목적: 케이스 내 'Result of Assessment' 필드(G.k.9.i.2.r.3)의 특정 텍스트를 인식하여, 식약처 보고서 변환 시 해당 이상사례(AE)를 '관련 있음(Related)으로 자동 분류하기 위함.
* 활용: 변환 시스템의 AE Type 자동 분류 엔진에서 매핑 데이터를 참조함.
* 선택적으로 설정할 수 있는 룰

## 상세 동작 및 시스템 로직

|  |  |  |
| --- | --- | --- |
| **구분** | **상세 명세** | **비고** |
| 대상 필드 | Result of Assessment (평가 결과) | E2B(R3) 기준 G.k.9.i.2.r.3 필드 |
| 판단 기준 | 설정된 텍스트가 대상 필드 내에 포함되어 있을 경우 | 'Related'로 판정 |
| 결과 활용 | 식약처 보고서 생성 시 AE Type 분류의 근거로 사용 | 보고 자동화 로직 |
| 디폴트 상태 | 비어 있음 (Empty) | 최초 설정 필요 |

## 사용자 입력 규칙

* 입력 형식

  + 영문 입력 시 대소문자를 구분하지 않음
* 기존의 단일 텍스트 필드 대신, '1 키워드 = 1 필드' 구조를 채택하여 오입력을 방지

  + 입력 컴포넌트: 독립된 텍스트 필드 행으로 구성
  + 행 추가 (+Add): 버튼 클릭 시 새로운 입력 필드가 하단에 추가됩니다.
  + 행 삭제 (삭제 아이콘): 각 텍스트 필드 우측의 삭제 버튼을 통해 특정 키워드를 리스트에서 즉시 제외

# 와이어프레임

![](https://t37003623.p.clickup-attachments.com/t37003623/aff03dd8-6c3e-4269-af08-f6259218028a/image.png)![](https://t37003623.p.clickup-attachments.com/t37003623/3112b46b-11b1-4a23-8ea2-5892b7924e82/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | 1. 평가 결과 매핑 필드 2. 케이스 변환 및 생성 시 '관련 있음(Related)'으로 판정할 단어 또는 문구를 입력하는 개별 행 | 1. 텍스트 입력: 특정 키워드를 입력하여 매핑 리스트를 구성함. 2. 저장 제한(Validation): 3. 텍스트 필드 행이 생성되었으나 내용이 비어 있는 경우, 상단의 SAVE 버튼이 자동으로 비활성화되어 저장이 차단됨. |
