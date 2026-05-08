|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.04.23 | 데이터 Bottom-up 계승 구조 폐기 | v1.0 | v1.0.260423 |
| 김나정 | 26.04.22 | Bottom-up data에 대한 추가 설명 | v1.0 | v1.0.260422 |
| 김나정 | 26.04.21 | Family, Products, Licenses 최소/최대 생성 갯수 추가 | v1.0 | v1.0.260421 |
| 김나정 | 26.04.17 | 라이센스 계층 설명 수정, 필수 계층 추가 | v1.0 | v1.0.260417 |
| 김나정 | 26.03.23 | 삭제 로직 추가 | v1.0 | v1.0.260323 |
| 김나정 | 26.03.19 | 오기재 수정 (MedDRA > MFDS 코드) | v1.0 | v1.0.260319 |
| 김나정 | 26.03.18 | 검색 기능 추가, UX/UI 욜구사항 추가 | v1.0 | v1.0.260318 |
| 김나정 | 26.02.20 | 최초 작성 | v1.0 |  |

# 개요 및 설계 아키텍처

### 설계 목적

* ICSR 프로세싱을 위한 자사 제품 마스터 데이터를 3단계 Hierarchy로 구축함.
* 케이스 입력 시 사전 설정된 제품 마스터 정보가 ICSR Case 필드에 자동 바인딩되며, 최종 규제기관 보고서(XML) 생성 시 해당 값들이 E2B(R3) 규격에 맞춰 자동 매핑되어 출력됨.
* 단일 귀결: 국가/파트너사별로 제각각인 보고 명칭을 자사 표준 제품 계층으로 매핑하여 데이터 통합 분석 기반을 마련

### 주요 기능

* 보고서상 제품명(Verbatim) ↔ 자사 표준 제품 계층 매핑
* RSI MedDRA 코딩 및 템플릿 업데이트 지원.

# 3단계 하이라키 및 ICSR-E2B(R3) 매핑 명세서

![](https://t37003623.p.clickup-attachments.com/t37003623/0c5a74e4-766e-4a45-9654-11350b9ee6cf/Study%20%E1%84%92%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A1%E1%84%8F%E1%85%B5-Product%20hierarchy.drawio%20(1).png)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **계층 (Level)** | 페이지 명 | **구성 요소** | **관리 및 매핑 로직** | 필수 사항 | 최소/최대 개수 |
| Level 1. 성분/브랜드군 | Family | 성분명, 브랜드명, 성분코드, RSI | 글로벌 통합 분석의 최상위 기준점 | 필수 | 최소 1/최대 1000 |
| Level 2. 제형, 용량, 모델 | Products | Dosage Form, Strength, Model | 제품의 물리적 규격과 세부 모델 정보를 한 화면에서 그룹화하여 관리합니다. | 필수 | Family 하위의 개수로 측정 최소 1/ 최대 1000 |
| Level 3. 국가별 License | Licenses | 허가국, 허가번호, 품목기준코드 | 시판약의 경우 허가 단위를 생성. 임상약은 허가 번호를 입력하지 않아도 됨 | 필수 | Prdocuts 하위의 개수로 측정 최소 1/최대 500 |

# Product 검색

공통 검색창에서 검색 가능

* Product Family Name, Product Name, Trade Name을 검색하면 해당 사항으로 검색 결과 표시

# UX/UI 요구사항

* 리스트에 보이는 이름

  + Family=[Product Family Name]
  + Products=[Product Name]
  + Licenses=[Trade Name]

# RSI 연동 정책 및 작동 명세

제품(Product)의 특성에 따라 적용되는 계층과 작동 방식이 완전히 분리된 투트랙(Two-Track) 정책을 적용. (추후 적용)

## 전역 환경 설정 (추후 적용)

RSI 작동 방식과 스케줄을 개별 제품마다 설정하는 번거로움을 없애기 위해, Product Master 화면 최상단에서 일괄 제어.

### RSI 모드 일괄 제어 토글 (추후 적용)

* 위치: Product 메인 화면 최상단.
* 기능: 전체 시스템의 기본 RSI 작동 방식을 결정하는 `[수동] / [자동]` 토글 스위치.

# Family, Product, License 삭제 로직

* 하위에 묶여있는 계층이 있다면 상위 개념은 삭제될 수 없음 (ex. Family 하위에 Products, Licenses가 존재한다면 Family는 삭제 불가. Products 하위에 Licenses가 존재한다면 Products 는 삭제 불가)

  + Family 하위에 Products/Licenses 있는데 삭제 버튼 클릭할 경우 메시지 표시

    - Family에 Products가 존재하면 삭제가 불가능합니다. 포함된 Products를 모두 삭제한 후 다시 시도해 주세요." 문구 표시 (Confirm 버튼만)
  + Products하위에 Licenses가 있는데 삭제 버튼 클릭할 경우 메시지 표시

    - Products에 Licenses가 존재하면 삭제가 불가능합니다. 포함된 Licenses를 모두 삭제한 후 다시 시도해 주세요." 문구 표시 (Confirm 버튼만)

# ~~WHODrug, MFDS 코드와 계층의 연결성 (폐기)~~

* ~~Licenses 단계에서 국가 코드 적용이 필요하기 때문에 WHODrug, MFDS 코드를 제일 하위 단계에서 세팅 필요~~

### ~~설계 원칙: Bottom-Up 데이터 동기화~~

* ~~기본 전략: 국가별 규제 요건이 반영되는 Level 3. License를 표준 코드(WHODrug/MFDS)의 소스 오브 트루스(Source of Truth)로 설정~~
* ~~상속 로직: 하위(Licenses)에서 확정된 데이터는 상위(Product, Family) 계층으로 자동 업데이트되어 전 계층의 데이터 일관성을 유지~~

### ~~시나리오별 작동 명세~~

|  |  |  |
| --- | --- | --- |
| **~~구분~~** | **~~Case A: 라이선스 정식 연결~~** | **~~Case B: 라이선스 미연결~~** |
| ~~작동 조건~~ | ~~Tenant 단위에서 정식 라이선스 계약/연결 시~~ | ~~라이선스 미연결 또는 자체 관리 제품일 때~~ |
| ~~데이터 입력~~ | ~~팝업을 통해 WHODrug/MFDS 전체 데이터 호출 및 저장~~ | ~~필수 관리 필드에 한해 사용자가 직접 입력~~ |
| ~~데이터 범위~~ | ~~WHODrug/MFDS 제공 데이터 전체 (MPID, 성분, 용량 등 모든 필드)~~ | ~~시스템 운영에 필요한 최소 필드 (코드 및 명칭 등)~~ |
| ~~상향 전파~~ | ~~저장 즉시 상위 Product 및 Family 필드에 자동 반영~~ | ~~입력된 값만 상,하위 계층으로 복사 저장~~ |
| ~~케이스 연동~~ | ~~케이스 생성 시 WHODrug의 모든 상세 정보가 ICSR로 이전~~ | ~~마스터에 저장된 최소 정보만 케이스로 이전~~ |

### ~~국가별 데이터 충돌 해결~~

~~1:N 매핑(하나의 Product 하위에 여러 License 존재) 시 데이터 혼선을 방지하기 위한 정책~~

|  |  |  |  |
| --- | --- | --- | --- |
| **~~구분~~** | **~~관리 레벨~~** | **~~데이터 처리 로직~~** | ~~비고~~ |
| ~~국가별 특화 데이터~~ | ~~Level 3~~ | ~~허가번호, 품목기준코드, 로컬 성분코드(WHODrug\_Country, MFDS 등)는 해당 레벨에만 귀속되며 상위로 올라가지 않음~~ |  |
| ~~글로벌 공통 데이터~~ | ~~Level 1, 2 (Shared)~~ | ~~WHODrug Drug Code, 성분명 등 국가와 무관한 공통 정보만 상위 계층으로 상속~~ |  |
| ~~데이터 일관성 유지~~ | ~~System Logic~~ | ~~Level 3(Licenses)에서 가장 마지막으로 업데이트된 데이터를 기준으로 상위 Level 2, 1의 공통 필드를 갱신~~   1. ~~특정 License에서 코드를 변경하여 상위 계층에 반영할 때, 기존에 저장되어 있던 값과 매핑된 정보가 다를 경우 경고 팝업을 노출~~ 2. ~~팝업 메시지: "다른 성분에 대한 WHODrug 정보가 Family, Products에 연결되어 있습니다. 현재 정보로 덮어쓰시겠습니까?"~~ | ~~Bottom-up 필드가 변경되어 올라가는 기준 시간은 해당 필드의 저장 시간~~ |

### ~~계층별 수정 권한 및 가시성 제어~~

~~상위 계층에서 하위 데이터가 임의로 수정되어 데이터 정합성이 깨지는 것을 방지~~

* ~~가시성 정책 :~~

  + ~~상향 상속된 필드 중 상위 계층 운영에 불필요한 필드는 화면에서 비가시화 처리~~
  + ~~전역 분석이나 참조를 위해 노출이 필요한 핵심 필드(예: WHODrug Code, 성분명)는 Level1, Level2 화면에 표시하되 Read-only 상태를 유지~~
* ~~수정 권한:~~

  + ~~Product 및 Family 화면에서 상속된 필드는 직접 수정이 불가능~~

    - ~~라이센스가 연결되어 있지 않은 경우만 직접 수정 가능~~
  + ~~데이터 수정이 필요한 경우, 반드시 해당 데이터의 원천인 Level 3. Licenses 화면으로 이동하여 수정해야 하며, 변경 사항은 상위로 즉시 재전파~~

#### 미결사항 (변경가능성 있음)

* 아래의 의약품에 관련 Identifier의 경우, IDMP에서 관리하는데, 아직 국내에서 활용하지 않음.

|  |  |  |
| --- | --- | --- |
| D.8.r.2a | MPID Version Date/Number | 의약품식별자(MPID) 버전 |
| D.8.r.2b | Medicinal Product Identifier (MPID) | 의약품식별자(MPID) |
| D.8.r.3a | PhPID Version Date/Number | 제제식별자(PhPID) 버전 |
| D.8.r.3b | Pharmaceutical Product Identifier (PhPID) | 제제식별자(PhPID) |

|  |  |  |
| --- | --- | --- |
| D.10.8.r.2a | MPID Version Date/Number | 의약품식별자(MPID) 버전 |
| D.10.8.r.2b | Medicinal Product Identifier (MPID) | 의약품식별자(MPID) |
| D.10.8.r.3a | PhPID Version Date/Number | 제제식별자(PhPID) 버전 |
| D.10.8.r.3b | Pharmaceutical Product Identifier (PhPID) | 제제식별자(PhPID) |

|  |  |  |
| --- | --- | --- |
| G.k.2.1.1a | MPID Version Date/Number | 의약품식별자(MPID) 버전 |
| G.k.2.1.1b | Medicinal Product Identifier (MPID) | 의약품식별자(MPID) |
| G.k.2.1.2a | PhPID Version Date/Number | 제제식별자(PhPID) 버전 |
| G.k.2.1.2b | Pharmaceutical Product Identifier (PhPID) | 제제식별자(PhPID) |

|  |  |  |
| --- | --- | --- |
| G.k.2.3.r.2a | Substance/Specified Substance TermID Version Date/Number | 성분명/특정성분명 버전 |
| G.k.2.3.r.2b | Substance/Specified Substance TermID | 성분명/특정성분명 코드 |

* WHODURG과 연결되어 있을 것으로 예상되나, 아직 실 활용하지 않고, WHODRUG에서 제공하는 방식도 명확하지 않아서 우선은 License 수준에서 별도 작성하도록 해 두었음.

![](https://t37003623.p.clickup-attachments.com/t37003623/afd50385-1890-49a6-88fc-997303b48485/image.png)![](https://t37003623.p.clickup-attachments.com/t37003623/ef6af837-c3a8-45d5-8291-88e9e9b23a7e/image.png)

* Medicinal Product Identifier (MPID)

* > 제품의 License 수준에서의 ID

* Pharmaceutical Product Identifier (PhPID)>Level4까지 정보를 포함할 수 있음.

  + Level1> 성분 수준의 ID
  + Level2> 약물 수준의 ID (정보 일부만 존재하는 경우)
  + Level3> 약물 수준의 ID (정보 일부만 존재하는 경우)
  + Level4> 약물 수준의 ID
* Substance/Specified Substance TermID

* > 성분 수준의 ID

![](https://t37003623.p.clickup-attachments.com/t37003623/d11e2be8-8e32-420f-a3c3-f38d6b2e47eb/image.png)![](https://t37003623.p.clickup-attachments.com/t37003623/505dd498-bf13-4f54-b35e-5a32f37a4707/image.png)
