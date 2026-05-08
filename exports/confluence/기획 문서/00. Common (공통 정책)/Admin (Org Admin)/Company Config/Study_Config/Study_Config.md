|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.02.25 | 최초 작성 | v1.0 | v1.0.260318 |

# 설계 목적

* 임상 데이터 표준화: 복잡한 임상 시험 설계(Study Design)를 7단계 하이라키로 구조화하여 데이터 정합성 확보
* ICSR 자동화 연동: 설정된 Study 정보가 케이스 입력 시 자동 바인딩되어 E2B(R3) 보고서 생성 시간 단축
* Product Master 연결: 최종 단계에서 앞서 기획한 3단계 제품 마스터와 연결하여 데이터 흐름 완성

![](https://t37003623.p.clickup-attachments.com/t37003623/b6fd4abe-14fa-4fca-944c-5ad7d84e769d/Study%20%E1%84%92%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A1%E1%84%8F%E1%85%B5-Study%20Hierarchy.drawio.png)

# Study 데이터 하이라키 (7 Layers)

임상 시험의 단위를 가장 작은 구성 요소인 '치료(Treatment)'와 '제품(Product)'까지 세분화

1. Project: 최상위 과제 단위 (예: 고형암 치료제 개발 프로그램)
2. Study: 개별 임상 시험 번호 (예: Protocol No. CLN-001)
3. Part: 임상 단계 또는 구분
4. Arm: 피험자 군 (예: 대조군, 시험군 1, 시험군 2)
5. Period: 시간적 구분
6. Treatment: 투약 요법 (예: A약 10mg + B약 5mg 병용)
7. Product: 실제 투여되는 제품 (Product Master와 매핑)

# 페이지 아키텍쳐

|  |  |  |
| --- | --- | --- |
| **페이지** | **구성 계층** | **주요 기능 및 액션** |
| P1. Project | Project | 과제 코드 명명 |
| P2. Study | Study | 임상 프로토콜 번호 등록, 국가 정보 설정 |
| P3. Study Design | Part + Arm + Period + Treatment | 핵심 설계 페이지: 환자가 어떤 단계(Part)에서 어떤 군(Arm)에 속해 어떤 시기(Period)에 어떤 치료(Treatment)를 받는지 시각적으로 구성 |
| P4. Product | Product | 매핑 페이지: 설정된 Treatment에 사용되는 실제 의약품을 Product의 Level 3(Licenses) 리스트에서 호출하여 연결. |

# Reporting 자동화 연동

* Study 정보 입력 시 국가 정보 및 임상 코드 입력 필요. 이상사례 발생 시 시스템이 "어느 국가의 어떤 규정에 맞춰 보고해야 하는지"를 자동으로 판별
* Product Master에서 관리하는 Level 3 License 정보가 변경될 경우, 해당 라이선스를 참조하고 있는 모든 Study 내 제품 정보에 즉시 반영

# Study 검색

공통 검색창에서 검색 가능

* Project ID, Sponsor Study Number, Study Name, Part Title, Arm Title을 검색하면 해당 사항으로 검색 결과 표시

# UX/UI 요구사항

* 리스트에 보이는 이름

  + Project=[Project ID]
  + Study=[Study Name]
  + Study Design=[Part Title]

# 프로토타이핑 파일

[study-config-prototype\_f…](/wiki/spaces/IS/pages/23888111/Study_Config?preview=%2F23888111%2F23888118%2Fstudy-config-prototype_f.html)

![](https://t37003623.p.clickup-attachments.com/t37003623/bb7a2ee6-0d8f-47e3-a1b1-36ab674cf225/image.png)
