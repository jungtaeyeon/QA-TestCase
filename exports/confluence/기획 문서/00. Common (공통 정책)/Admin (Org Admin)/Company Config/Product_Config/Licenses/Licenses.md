|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획서 버전 |
| 김나정 | 26.04.22 | 데이터 Bottom Up 역전파 삭제 | v1.0 | v1.0.260422 |
| 김나정 | 26.03.26 | Trade Name 중복 불가 기재 | v1.0 | v1.0.260326 |
| 김나정 | 26.03.19 | Product Identifier type 화면 기획 변경  Substance Term ID Bottom-up 로직 추가, 필수/옵션 필드 추가 기재 | v1.0 | v1.0.260319 |
| 김나정 | 26.03.18 | WHODrug bottom-up 기준 기재 (기획변경 X) | v1.0 | v1.0.260318 |
| 김나정 | 26.03.06 | 최초 작성 | v1.0 |  |

# 입력 필드

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 카테고리 | 필드 영문 | 필드 국문 | 필수 여부 | 매칭 R3필드 | 비고 | Validation |
| - | Trade Name | 제품 허가명 | 필수 | N/A | 중복 불가 | 최대 100자 |
| - | Award Date | 허가 승인일 | 옵션 | N/A | calendar 선택 | - |
| - | Withdrawn Date | 허가 취하/취소일 | 옵션 | N/A | calendar 선택 | - |
| - | Market Authorization Holder | 품목 허가권자 (MAH) | 조건부 필수 (라이선스 유형이 Marketed Device / Marketed Drug / Marketed Vaccine 일때) | G.k.3.3 | 추후 Filtering에 활용하여야 함 | R3 검증 룰을 따름 |
| - | Biologic / Vaccine (체크박스) | 바이오의약품 / 백신 | 옵션 | N/A |  | - |
| - | Not in Tradename Lookup / Not Auto-Scheduled (체크박스) | 제품명 조회/자동 스케줄 제외 | 옵션 | N/A | 개발 중이거나 허가되었지만, 실제로 이상사례 발생 사례가 없는 경우, 목록에서 제외 가능 | - |
| - | Biosimilar (체크박스) | 바이오시밀러 | 옵션 | N/A |  | - |
| - | Authorization Country | 허가 국가 | 조건부 필수 (라이선스 유형이 시판 후 일때) | G.k.3.2 |  | R3 검증 룰을 따름 |
| - | License Type | 라이선스 유형 | 필수 | N/A | 드롭다운 선택 (와이어프레임 참조) | - |
| - | Datasheet Name (드롭다운 매핑) | 데이터시트 명칭 (RSI 매핑) | 옵션 | N/A | 매핑 | - |
| - | WHO Medicinal Product ID | WHO 의약품 식별번호 (MPID) | 옵션 | 보고 Destination이 시판 후 국외(FR)보고인 경우 (MFDS-O-FR)인 경우, G.k.2.1.KR.1b로 입력 | G.k.2.1.KR.1a 버전 정보 별도 필요 | R3 검증 룰을 따름 |
| - | MFDS Code (Regional) | 식약처 성분코드 (지역) | 옵션 | G.k.2.3.r.1.KR.1b/G.k.2.3.r.1.KR.1a | MFDS-KR일 때 매핑  Licenses 국가코드가 KR일때 MFDS 입력 필드 활성화 | R3 검증 룰을 따름 |
| - | License # | 허가 번호 / 품목기준코드 | 조건부 필수 (라이선스 유형이 시판 후 일때) | MFDS일때, G.k.2.1.KR.1b (타국가 License인 경우, G.k.3.1와 같이 다른 필드일 수 있음) | MFDS일때, G.k.2.1.KR.1b  Level 3단위로 남음 | R3 검증 룰을 따름 |
| - | Product Identifier Type | 제품 식별자 유형 | 옵션 | N/A | 어떤 종류의 ID에 Mapping할지이기 때문에 해당 필드 자체는 R3에 연결되지 않음.  드롭다운으로 선택 (와이어프레임 참조) | - |
| - | Product Identifier | 제품 식별자 | 옵션 | G.k.2.1.1b (MPID)  G.k.2.1.2b (PhPID)  G.k.2.3.r.2b (Substance Term ID) | type에 따라 필드가 다름 | R3 검증 룰을 따름 |
| Product Name / Dosage Form / Strength | Product Name | 기본 제품명 | N/A | N/A | Products에서 승계 Read Only | - |
| - | Brand Information | 브랜드 정보 | 필수 | N/A | 크리에이터블 드롭다운 (와이어프레임 참조) | 추후 Filtering에 활용하여야 하므로 필수 |

# Regional 정보 입력

## 지역 성분코드 입력

* 각 나라의 성분코드를 입력하는 Regional 공간으로, 현재 버전에서는 한국 식약처(MFDS) 규제기관 코드만 제공
* 추후 +버튼을 통해 지역 추가 가능 (현재는 제공하지 않음)
* 글로벌 성분코드와는 분리되어 별도로 입력
* 사내 타 시스템(ivi, wave)에 이미 구현된 성분코드 검색 api 호출

  + 필드 클릭 시 MFDS 전용 성분코드 팝업창을 띄워 검색 및 입력

# Level 3. License - RSI 매핑

|  |  |
| --- | --- |
| **항목** | **상세 기능 명세** |
| 기능명 | RSI 데이터시트 매핑 |
| 기능 설명 | 해당 라이선스(국가/품목)에 적용할 안전성 참조 정보(RSI)를 설정  여기서 매핑된 RSI는 추후 Case 생성 및 편집 단계에서 이상사례의 '기재 여부(Expectedness/Listedness)'를 판별하는 기준값으로 활용 |
| 데이터 소스 | Level 1 (Family)의 'RSI Management' 섹션에서 생성된 RSI 그룹 리스트를 실시간으로 참조 |
| 사용자 액션 | 1. `Datasheet Name` 드롭다운 필드를 클릭  2. 상위 Family에서 정의된 RSI 그룹 네임 목록을 확인  3. 해당 국가 허가사항에 맞는 RSI 그룹을 선택 |
| 시스템 로직 | RSI 그룹 선택 시, 해당 그룹 내에 등록된 모든 MedDRA Term(PT), 코드, 버전 정보가 해당 License의 제품 정보와 연결 |

# 와이어프레임

![](https://t37003623.p.clickup-attachments.com/t37003623/2fce233d-1617-47a2-b4ee-63215865c4f6/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | 1. 권한을 가지고 있는 제조사를 표시 2. Products의 Manufacturer와 동일 리스트로 관리 | 1. 클릭 시 크리에이터블 드롭다운 표시 2. 해당 드롭다운 리스트는 Manufacturer의 리스트와 동일하게 관리됨 3. 드롭다운에 새로운 리스트 추가 시 Manufacturer에도 동일하게 추가 |
| 2 | 1. 라이선스를 부여받은 국가를 설정 | 1. 드롭다운 시 국가 코드 설정 |
| 3 | 1. 라이센스 타입 설정 | 1. 클릭 시 드롭다운 리스트 표시 2. 리스트: Investigational Device / Investigational Drug / Investigational Vaccine / Marketed Device / Marketed Drug / Marketed Vaccine |
| 4 | 1. 국가 설정(1번)에 따라 해당 국가 규제기관의 성분 코드를 입력 2. 현재는 MFDS 규제기관만 제공하므로 KR 선택시에만 표시 3. 그외 국가 선택 시 해당 필드 표시되지 않음 | 1. 필드 클릭 시 MFDS 성분 검색 팝업 호출 2. 팝업에서 선택한 코드가 해당 필드에 입력 3. 라이센스 연결되지 않을 경우 자유 기재 |
| 5 | 1. 국제 표준 제품 식별 ID를 입력 | 1. 클릭 시 WHODrug 검색 팝업이 노출 2. 검색 결과에 국가코드 표시 필요 |
| 6 | 1. 상위 Level 1(Family)에서 기획된 RSI 그룹 중 하나를 선택하여 매핑 2. Level 1 에서 생성된 RSI 그룹 네임이 리스트로 표시 3. 추후 케이스 생성/편집 시 해당 RSI 정보는 expectedness/Listedness 판별하는 정보값으로 활용 | 1. 클릭 시 이미 설정한 RSI 그룹 목록 표시 2. RSI 선택 시 해당 RSI의 증상이 Licenses의 제품 정보로 매핑 |
| 7 | 1. MPID 입력 | 1. 프리텍스트 입력 |
| 8 | 1. PhPID 입력 | 1. 프리텍스트 입력 |
| 9 | 1. subbstance Term ID 입력 | 1. 프리텍스트 입력 |
| 10 | 1. 상위 레벨(1, 2)에서 이미 정의된 제품의 핵심 물리적 정보 표시 2. 각 정보 매핑 3. Product Name=2레벨의 Product Name 4. Dosage Formulation=2레벨의 Dosage Formulation 5. Strength=레벨 2의 Strength 6. Unit=레벨2의 Unit | - |

# 참고

![](https://t37003623.p.clickup-attachments.com/t37003623/7dcceb80-a2d7-4441-8cf9-faf11e9edbdd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202026-03-12%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%209.55.21.png)![](https://t37003623.p.clickup-attachments.com/t37003623/8e240c67-a4a9-4d39-b394-f595f774a179/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202026-03-12%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%209.55.37.png)
