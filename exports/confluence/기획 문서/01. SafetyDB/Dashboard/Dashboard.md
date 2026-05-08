# 변경사항

|  |  |  |  |
| --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 |
|  | 26.03.10 | Guest -> External User 수정  Viewer 추가: 범위가 미정임 |  |
| 김병환 | 26.03.06 | 마스터 URS 참고하여 전체적으로 재정리 | v1.0 |
| 김병환 | 26.02.27 | URS와 기본요구사항을 참고하여 문서 정리 완료 | v1.0 |

# **0. 기본 요구사항**

본 문서는 Safety DB를 단일 데이터 원천으로 하는 Status 대시보드와 QC 대시보드의 운영 정책, 개발 요구사항, 데이터 요건을 정의한다.

* Status 대시보드: 현재 DB에 입력된 케이스 상태 확인
* QC 대시보드: Submission / Exchange Compliance 등 완료한 업무의 품질 검토 결과 조회

# **1. 공통 정책**

## **1.1 목적**

본 문서는 대시보드의 운영 정책, 개발 요구사항, 데이터 요건을 정의한다.

대시보드는 Safety DB에 저장된 데이터를 읽어서 시각화하는 것을 기본 원칙으로 한다.

## **1.2 대시보드 진입점**

|  |  |
| --- | --- |
| **접속 레벨** | **진입 위치** |
| **Tenant** | Tenant Home 내 Dashboard 메뉴 |
| **Workspace** | Workspace Home 내 Dashboard 메뉴 |
| **App** | App 내 좌측 GNB 메뉴 |

### **화면 흐름**

|  |
| --- |
| **📋 대시보드 진입 흐름**  케이스 A: Tenant 레벨 진입    Tenant Home → GNB [Dashboard] 클릭 → Tenant 레벨 대시보드 표시    (전체 Workspace × App 합산 데이터 표시, Master Admin / Tenant Admin 전용)    케이스 B: Workspace 레벨 진입    Workspace Home → GNB [Dashboard] 클릭 → Workspace 레벨 대시보드 표시    (해당 Workspace 산하 App 데이터만, Master Admin / Tenant Admin 전용)    케이스 C: App 레벨 진입    App 화면 → 좌측 GNB [Dashboard] 클릭 → App 레벨 대시보드 표시    (해당 App 데이터만, App Admin / App User / External User 접근 가능)    ⚠ Backoffice Admin은 고객사 대시보드 접근 불가 → 별도 운영 모니터링 화면 이용 |

## **1.3 데이터 원천 및 갱신**

|  |  |  |
| --- | --- | --- |
| **레이어** | **구성요소** | **비고** |
| **원천** | Safety DB | 모든 집계 수치의 단일 데이터 원천 |
| 갱신 방식 | 1시간 주기 배치 |  |
| 최종 업데이트 일시 | 대시보드 배치가 마지막으로 실행된 시각 표시 | 마지막 업데이트: 2025-10-15 09:00 (KST) |

## 1.4 대시 보드 종류와 목적

|  |  |
| --- | --- |
| **대시보드 종류** | **의미** |
| Status | 현재 DB에 입력되어 있는 케이스들의 상태를 확인   1. 현재 시간 중심 2. 실시간성 중요 |
| QC | 완료한 업무의 퀄리티를 검토하기 위한 결과를 조회   1. 보고가 완료 된 케이스수를 확인 |

## **1.5 월 귀속 기준**

|  |  |  |
| --- | --- | --- |
| **대시보드 종류** | **월 귀속 기준** | **의미** |
| Status | **수집 시점** | Safety DB에 케이스가 수집된 시점 기준 |
| QC | **보고 완료 시점** | 규제기관 제출 또는 파트너사 교환 완료 시점 기준 |

## **1.6 멀티테넌트 데이터 스코프**

|  |  |  |
| --- | --- | --- |
| **접속 레벨** | **집계 범위** | **접근 가능 역할** |
| **Tenant** | 전체 Workspace × App 합산  (Workspace별 Breakdown 해서도 볼 수 있어야 함) | Master Admin, Tenant Admin |
| **Workspace** | 해당 Workspace 산하 App 데이터만 | Master Admin, Tenant Admin |
| **Application** | 해당 App 데이터만 | App Admin, App User, External User |

*※ App Admin / App User / External User의 Workspace 접근은 App 진입을 위한 경로이므로, Workspace 대시보드(Workspace 내 전체 App 집계)는 Master Admin / Tenant Admin 전용으로 정의한다.*

### **1.6.1 데이터 격리**

* Backoffice Admin은 고객사의 PV 업무 지표(대시보드) 접근 불가. 별도 운영 모니터링 화면 이용.
* 타 Tenant 데이터 접근 불가.
* 최초 계약 시 생성된 Workspace 이외, 추가로 생성되어 Study와 관련 Product 일부만 접근하는 워크스페이스의 경우, Tenant와 격리 되어 해당 정보를 확인 할 수 없음

### **1.6.2 역할별 데이터 노출 범위**

|  |  |  |
| --- | --- | --- |
| **역할 (Role)** | **접근 가능 범위** | **대시보드 내 제약** |
| **Backoffice Admin** | 해당 없음 | 대시보드 접근 불가. 별도 운영 모니터링 화면 이용. |
| **Master Admin** | 소속 Tenant 전체 | Tenant/Workspace/App 레벨 모두 접근. Breakdown 조회 가능. |
| **Tenant Admin** | 소속 Tenant 전체 | Tenant/Workspace/App 레벨 모두 접근. Breakdown 조회 가능. |
| **App Admin** | 소속 App | App 레벨 대시보드만. |
| **App User** | 소속 App | App 레벨 대시보드만. |
| External User | 접근 허용된 App | App 레벨 대시보드만. |
|  |  |  |

## **1.7 주차(Week) 및 공휴일 산출 기준**

주차 산출: ISO 8601 기준 — 월요일 시작, 목요일 포함 주가 1주차

공휴일: 필터링 시 공휴일을 확인할 수 있도록 필요 - 이 부분은 구현 어떻게 할지 개발팀 확인 필요

## **1.8 파라미터 수정 권한**

파라미터(연도·월·날짜 범위 등) 수정 권한은 레벨별로 다르게 적용한다.

|  |  |  |
| --- | --- | --- |
| **접속 레벨** | **역할** | **파라미터 수정** |
| **Tenant** | Master Admin / Tenant Admin | 가능/일회적 변경 |
| **Workspace** | Master Admin / Tenant Admin | 가능/일회성 변경 |
| **App** | App Admin | 가능/일회성 변경 |
| **App** | App User / External USer | 가능/일회성 변경 |

* Backoffice Admin은 고객사의 PV 업무 지표(대시보드) 접근 불가. 별도 운영 모니터링 화면 이용.

## **1.9 공통 동작 정책**

* 파라미터 변경 시 모든 패널 자동 갱신
* 데이터 미발생: NA / 값 0: 0 으로 구분 표기
* 차트의 특정 항목이나 그래프 클릭 시 관련 상세 데이터로 이동 (차트 인터랙션)
* 대시보드 최근 업데이트 시간 표시 (Status / QC 공통)

## **1.10 Export**

* 대시보드 자료를 PDF / EXCEL로 Export 가능해야 한다.
* PDF: 현재 보고 있는 화면을 PDF 형식으로 Export
* EXCEL: 현재 보고 있는 화면 내 수치들을 EXCEL 형식으로 Export

  + Export 시 대시보드 종류·업데이트 일시·Export 시간이 문서 내에 표시되어야 함
* 해당 URL로 외부 공유 불가

### **화면 흐름**

|  |
| --- |
| **📋 Export 흐름 (공통)**  ① 대시보드 화면 우측 상단 [Export] 버튼 클릭  ② Export 형식 선택: [PDF] / [EXCEL]     PDF: 현재 화면 레이아웃 그대로 PDF 생성     EXCEL: 현재 화면 내 수치 데이터를 시트로 변환  ③ 생성된 파일 다운로드     파일 내 메타 정보 포함: 대시보드 종류 / 마지막 업데이트 일시 / Export 시각    ⚠ 외부 URL 공유 기능 미제공 |

## **1.11 (제안) 공통 UI 원칙: 디자인에 따라 변경 될 수 있음**

* 동작

  + 파라미터 변경 시 모든 패널 자동 갱신
  + 데이터 미발생: NA / 값 0: 0 으로 구분 표기
  + 차트 인터랙션 요구사항

    - 차트의 특정 항목이나 그래프 클릭 시 관련 상세 데이터로 이동

* 디자인(제안 입니다)

|  |  |
| --- | --- |
| **상태** | **색상** |
| 정상 / 100% 달성 | 초록 |
| 경고 / 임계값 미달 | 빨강 |
| 데이터 없음 (NA) | 회색 |
| 중증(Serious) 관련 | 남색 계열 |
| Death / 고위험 | 분홍·적색 계열 |

# **2. Status 대시보드**

### 공통: 대시보드 최근 업데이트 시간 표시

### 필터: 규제기관 / 파트너사 / 의약품 / 성분 / Workspace / 기준시점

* 여러개 선택

  + 규제기관, 파트너사, 의약품, 성분은 필터 별로 최대 3개 까지만 다중 선택
  + Workspace는 1개씩만 선택
* 기준 시점

  + 현재 년월 자동 적용
  + 미래 년월 선택 불가
* 필터 변경시 전체 대시보드 업데이트

### **집계 단위 토글**

* 월별 / 분기별: 디폴트는 월별
* 최근 12개월 / 올해: 디폴트는 최근 12개월
* 분기별 고를 시 기간 필터(최근 12개월/올해)는 비활성화 처리
* [조회] 버튼 클릭 시 전체 갱신

### **화면 흐름**

|  |
| --- |
| **📋 Status 대시보드 공통 파라미터 조작 흐름**  ① 대시보드 진입 → [Status] 탭 자동 표시  ② 공통 필터 설정: 규제기관 / 파트너사 / 의약품 / 성분) / Workspace / 기준시점  ③ 집계 단위 토글 선택 — 1단계: 월별 or 분기별     1단계 월별 선택 시: 2단계(최근 12개월 / 올해) 표시     1단계 분기별 선택 시: 2단계 영역 비활성화  ④ [조회] 버튼 클릭 → 전체 섹션 일괄 갱신 (Summary 카드 + 차트 ① ② ③) |

## **2.1 Summary 카드**

필터 조건 기준으로 집계된 핵심 지표를 카드 형태로 표시.

카드 4종: 전체 ICSR 건수 / SUSAR 건수 / Serious 비율(%) / 누적 총계

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-S-SUM-01 | 공통 필터 및 집계 단위 토글 조건에 따라 Summary 카드 4종 표시. | 필수 |
| DR-S-SUM-02 | 카드 ①: 전체 ICSR 건수 — 해당 기간 내 Safety DB 수집 건 합계. | 필수 |
| DR-S-SUM-03 | 카드 ②: SUSAR 건수 — 해당 기간 내 SUSAR로 분류된 건 합계. | 필수 |
| DR-S-SUM-04 | 카드 ③: Serious 비율(%) — Serious / 전체 ICSR × 100. | 필수 |
| DR-S-SUM-05 | 카드 ④: 누적 총계 — 전체 기간 기준 Safety DB 수집 건 누적 합계. | 필수 |

### **화면 흐름**

|  |
| --- |
| **📋 Summary 카드 조회 흐름**  ① [조회] 버튼 클릭 → Summary 카드 4종 갱신  ② 카드 ①: 전체 ICSR 건수 표시  ③ 카드 ②: SUSAR 건수 표시  ④ 카드 ③: Serious 비율(%) 표시  ⑤ 카드 ④: 누적 총계 표시  ⚠ 데이터 미발생: NA / 값 0: 0 으로 구분 표기 |

## **2.2 차트 ① AE Type 분포**

AE Type별 ICSR 건수를 2-Way 스택 막대 차트와 누적 합계 추이선으로 표시.

**차트 구성**

* 형태: 2-Way 스택 막대 + Accumulated Total 점선 (이중 Y축)

* 왼쪽 Y축: 해당 기간 건수 / 오른쪽 Y축: Accumulated Total

* 세그먼트 5종: Death / SUSAR / SADR / SAE / ADR / AE / Unclassifiable(AE Type 분류 불가)

* 월 귀속 기준: Safety DB 수집 시점

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-S-AE-01 | 공통 필터 및 집계 단위 토글 기준으로 AE Type별 건수 집계. | 필수 |
| DR-S-AE-02 | 2-Way 스택 막대 차트 표시. 세그먼트: Death / SUSAR / SADR / SAE / ADR / AE / Unclassifiable(AE type 분류 불가). | 필수 |
| DR-S-AE-03 | Accumulated Total 점선(오른쪽 Y축) 표시. 누적 합계 = 전체 AE Type 합산 누적. | 필수 |
| DR-S-AE-04 | 월 귀속 기준: Safety DB 수집 시점. | 필수 |
| DR-S-AE-05 | 차트 항목 클릭 시 해당 케이스 상세 목록으로 드릴다운. (미결정: 동작 방식 별도 정의) | 필수 |

### **화면 흐름**

|  |
| --- |
| **📋 차트 ① AE Type 분포 조회 흐름**  ① [조회] 버튼 클릭 → 차트 ① 갱신  ② 기간 내 AE Type별 건수를 스택 막대 차트로 표시  ③ Accumulated Total 점선(오른쪽 Y축) 함께 표시  ④ 스택 세그먼트: Death / SUSAR / SADR / SAE / 기타(ADR+AE+Not AE 합산)  ⑤ 차트 항목 클릭 → 해당 케이스 상세 목록으로 이동 (드릴다운 방식 미결정)  ⚠ 데이터 미발생: NA / 값 0: 0 으로 구분 표기 |

## **2.3 차트 ② Source별 유입경로**

Source Type별 ICSR 유입 건수를 2-Way 스택 막대 차트와 누적 합계 추이선으로 표시.

**차트 구성**

* 형태: 2-Way 스택 막대 + Accumulated Total 점선 (이중 Y축)

* 왼쪽 Y축: 해당 기간 건수 / 오른쪽 Y축: Accumulated Total

* 세그먼트 5종: SP / CT / PMS / LS / UNK

* Accumulated Total = 전체 Source 합산 누적

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-S-SRC-01 | 공통 필터 및 집계 단위 토글 기준으로 Source Type별 건수 집계. | 필수 |
| DR-S-SRC-02 | 2-Way 스택 막대 차트 표시. 세그먼트: SP / CT / PMS / LS / UNK. | 필수 |
| DR-S-SRC-03 | Accumulated Total 점선(오른쪽 Y축) 표시. 누적 합계 = 전체 Source 합산 누적. | 필수 |
| DR-S-SRC-04 | 차트 항목 클릭 시 해당 케이스 상세 목록으로 드릴다운. (미결정: 동작 방식 별도 정의) | 필수 |

**화면 흐름**

|  |
| --- |
| **📋 차트 ② Source별 유입경로 조회 흐름**  ① [조회] 버튼 클릭 → 차트 ② 갱신  ② 기간 내 Source Type별 건수를 스택 막대 차트로 표시  ③ Accumulated Total 점선(오른쪽 Y축) 함께 표시 (전체 Source 합산 누적)  ④ 스택 세그먼트: SP / CT / PMS / LS / UNK  ⑤ 차트 항목 클릭 → 해당 케이스 상세 목록으로 이동 (드릴다운 방식 미결정)  ⚠ 데이터 미발생: NA / 값 0: 0 으로 구분 표기 |

## **2.4 차트 ③ Domestic/Foreign 현황**

국내·해외 ICSR 발생 현황 및 누적 추이를 병렬 막대 차트와 이중 선 차트로 표시.

**차트 구성**

* 형태: Grouped 막대(스택 아님, 병렬 배치) + 이중선 (오른쪽 Y축)

* 막대: Domestic(파랑) / Foreign(초록) 병렬 배치

* 이중선(오른쪽 Y축): 국내 누적 실선 + 해외 누적 점선

**KPI 카드 4종: 국내 건수 / 해외 건수 / 국내 누적 / 해외 누적**

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-S-DF-01 | 공통 필터 및 집계 단위 토글 기준으로 Domestic/Foreign별 건수 집계.   1. 국내가 아니면 나미저는 국외로 분류2 | 필수 |
| DR-S-DF-02 | Grouped 막대 차트 표시. Domestic(파랑) / Foreign(초록) 병렬 배치. | 필수 |
| DR-S-DF-03 | 이중선(오른쪽 Y축) 표시. 국내 누적 실선 + 해외 누적 점선. | 필수 |
| DR-S-DF-04 | KPI 카드 4종 표시: 국내 건수 / 해외 건수 / 국내 누적 / 해외 누적. | 필수 |
| DR-S-DF-05 | 차트 항목 클릭 시 해당 케이스 상세 목록으로 드릴다운. (미결정: 동작 방식 별도 정의) | 필수 |

### **화면 흐름**

|  |
| --- |
| **📋 차트 ③ Domestic/Foreign 현황 조회 흐름**  ① [조회] 버튼 클릭 → 차트 ③ 갱신  ② 기간 내 Domestic / Foreign 건수를 Grouped 막대 차트로 표시  ③ 국내 누적 실선 + 해외 누적 점선(오른쪽 Y축) 함께 표시  ④ KPI 카드: 국내 건수 / 해외 건수 / 국내 누적 / 해외 누적 표시  ⑤ 차트 항목 클릭 → 해당 케이스 상세 목록으로 이동 (드릴다운 방식 미결정)  ⚠ 데이터 미발생: NA / 값 0: 0 으로 구분 표기 |

# **3. QC 대시보드**

### 공통: 대시보드 최근 업데이트 시간 표시

### 필터: 규제기관 / 파트너사 / 의약품 / Workspace / 기준시점

* 여러개 선택

  + 규제기관, 파트너사, 의약품은 최대 3개 까지만 다중 선택
  + Workspace는 1개씩만 선택
* 기준 시점

  + 현재 년월 자동 적용
  + 미래 년월 선택 불가
* 필터 변경시 전체 대시보드 업데이트

### **집계 단위 토글**

* 월별 / 분기별: 디폴트는 월별
* 최근 12개월 / 올해: 디폴트는 최근 12개월
* 분기별 고를 시 기간 필터(최근 12개월/올해)는 비활성화 처리
* [조회] 버튼 클릭 시 전체 갱신

### **공통 표시 방식: 각 섹션은 2-Way 차트 + 값 테이블을 병행 제공한다.**

* 2-Way 차트: Period Volume(막대) + Accumulated Total(선)이 항상 나란히 배치 (토글 아님)
* 값 테이블: 행 = 신속보고(Expedited)/정기보고(Periodic) 또는 Serious/Non-Serious 구분 × On time/Late/Missing 건수+비율. 열 = 12개월 + 합계

기준 시점 기본값: 현재 월 자동 적용. 미래 월 선택 불가. 변경 시 4개 섹션 일괄 갱신.

공통 값 표기 규칙: 값 0 = 빨간 숫자 강조 / 값 없음 = 회색 “-” / N/A = 이탤릭 회색 (분모 0)

## **3.1 Regulatory Authority Submission Compliance**

보고 완료 시점 기준 월 귀속. 제출 의무 케이스 중 실제 제출 완료 비율을 Expedited, Periodic으로 나눠 월별 표시.

**정의**

* Expedited: 전체 보고 케이스 중 due date가 7일, 15일인 것
* Periodic: 보고 건 중 due date가 다음과 같은 것(분기 종료 후 1개월 내, • 정기 보고서 (PBRER)의 제출일이 속한 분기의 종료 후 1개월 이내, 결과보고서 (CSR) 완료일이 속한 분기종료 후 1개월 내)
* 보고 완료율 = (월에 보고한 건 / 해당 월에 보고해야 하는 건) × 100

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-Q-SC-01 | Report Year·Month 파라미터. 모든 QC 패널에 자동 반영. | 필수 |
| DR-Q-SC-02 | 현재 년/월 기준 최근 1년간의 보고 완료율을 Expedited, Periodic으로 분류하여 월별 표시 | 필수 |
| DR-Q-SC-03 | 현재 년/월의 보고 완료율을 Expedited, Periodic으로 구분하여 표시. 포함되는 케이스 수도 함께 표시. | 필수 |
| DR-Q-SC-04 | 12개월 간의 보고 완료율을 Expedited, Periodic으로 분류하여 표시 | 필수 |
| DR-Q-SC-05 | 현재 년도의 보고 완료율을 Expedited, Periodic으로 구분하여 표시 | 필수 |

### **화면 흐름**

|  |
| --- |
| **📋 Submission Compliance 조회 흐름 (DR-Q-SC)**  ① [QC] 탭 → Regulatory Authority Submission Compliance 섹션  ② Report Year / Month 드롭다운 선택 → 모든 QC 패널 자동 갱신  ③ 최근 1년 월별 보고 완료율 테이블 표시 (Expedited / Periodic 행 구분)  ④ 현재 년/월 보고 완료율 + 케이스 수 표시  ⑤ 12개월 합산 완료율 + 현재 년도 완료율 표시  ⑦ 차트 항목 클릭 → 해당 케이스 상세 목록으로 이동 |

## **3.2 Regulatory Authority Submission Timeline Compliance**

보고 완료 시점 기준 월 귀속. 기한 내 제출 완료 비율 월별 표시.

* Due Date 내 보고한 건 / 해당 월 보고건 중 Due Date 내 보고한 건 × 100

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-Q-STC-01 | 3.1과 동일한 구조와 데이터 표시 | 필수 |
| DR-Q-STC-02 | 데이터 차이: 3.2는 전체 보고에서 Due date 내에 보고한 건만 표시 (On Time / Late 판정 기준) | 필수 |

### **화면 흐름**

|  |
| --- |
| **📋 Submission Timeline Compliance 조회 흐름 (DR-Q-STC)**  ① [QC] 탭 → Regulatory Authority Submission Timeline Compliance 섹션  ② Report Year / Month 드롭다운 선택 (DR-Q-SC-01과 공통 파라미터 자동 반영)  ③ Submission Compliance(3.1)와 동일 구조로 표시     차이: Due date 내 보고한 건만 카운트 → On Time 비율 표시 |

## **3.3 SDEA Partner Exchange Compliance**

교환 완료 시점 기준 월 귀속. 실제 파트너사에 제공해야 하는 것 중에서 제공했는지 여부 표시.

* 파트너사 제공 완료율 = (파트너사 제공 건 / 월에 파트너사에 제공해야 할 것) × 100

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-Q-EC-01 | Report Year·Month 파라미터. 모든 QC 패널에 자동 반영. | 필수 |
| DR-Q-EC-02 | 현재 년/월 기준 최근 1년간의 파트너사 제공 완료율을 Serious, Non-Serious로 분류하여 월별 표시 | 필수 |
| DR-Q-EC-03 | 현재 년/월의 파트너사 제공 완료율을 Serious, Non-Serious로 구분하여 표시. 포함되는 케이스 수도 함께 표시. | 필수 |
| DR-Q-EC-04 | 12개월 간의 파트너사 제공 완료율을 Serious, Non-Serious로 분류하여 표시 | 필수 |
| DR-Q-EC-05 | 현재 년도의 파트너사 제공 완료율을 Serious, Non-Serious로 구분하여 표시 | 필수 |

### **화면 흐름**

|  |
| --- |
| **📋 Partner Exchange Compliance 조회 흐름 (DR-Q-EC)**  ① [QC] 탭 → SDEA Partner Exchange Compliance 섹션  ② Report Year / Month 드롭다운 선택 (QC 공통 파라미터 자동 반영)  ③ 최근 1년 월별 파트너사 제공 완료율 테이블 표시 (Serious / Non-Serious 행 구분)  ④ 현재 년/월 완료율 + 케이스 수 표시  ⑤ 12개월 합산 완료율 + 현재 년도 완료율 표시 |

## **3.4 SDEA Partner Exchange Timeline Compliance**

교환 완료 시점 기준 월 귀속. 파트너와 약속된 기한 내 제공한 것만 표시.

* 정해진 기간 내 파트너사에 제공한 건 / 해당 월 내에 파트너사에게 제공해야 하는 건 × 100

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-Q-ETC-01 | 3.3과 동일한 구조 | 필수 |
| DR-Q-ETC-02 | 3.3과의 차이: 파트너사와 약속한 기간 내 전달했는지의 비율 표시. 나머지는 DR-Q-EC와 동일한 구성. | 필수 |

### **화면 흐름**

|  |
| --- |
| **📋 Partner Exchange Timeline Compliance 조회 흐름 (DR-Q-ETC)**  ① [QC] 탭 → SDEA Partner Exchange Timeline Compliance 섹션  ② Report Year / Month 드롭다운 선택 (QC 공통 파라미터 자동 반영)  ③ Partner Exchange Compliance(3.3)와 동일 구조로 표시     차이: 파트너사와 약속된 기한 내 전달한 건만 카운트 |

# **4. Safety DB 공통 필수 데이터 요건**

|  |  |  |
| --- | --- | --- |
| **데이터 항목** | **활용 지표** | **비고** |
| 케이스 고유 ID | 전체 | 중복 집계 방지 |
| 케이스 수집 시점 | DR-S-W, DR-S-M, DR-S-A, DR-S-I | Status 대시보드 월 귀속 기준 |
| 발생 국가 (Domestic/Foreign) | DR-S-W, DR-S-M, DR-S-A | - |
| AE Type | DR-S-W, DR-S-M, DR-S-A | Death·SUSAR·SADR·SAE·ADR·AE·Not AE |
| Source Type | DR-S-M, DR-S-A, DR-S-I | Safety DB에서 정해진 대로 추가됨 |
| Seriousness | DR-S-M, DR-S-A, DR-S-I, DR-Q-EC, DR-Q-ETC | Serious·Non-Serious |
| Reporting Type | DR-S-I, DR-Q-SC, DR-Q-STC | Expedited·Periodic 등 |
| 규제기관 제출 완료 시점 | DR-Q-SC, DR-Q-STC | QC 월 귀속 기준 |
| 규제기관 제출 기한일 | DR-Q-STC | On Time·Late 판정 |
| SDEA 파트너 교환 완료 시점 | DR-Q-EC, DR-Q-ETC | QC 월 귀속 기준 |
| SDEA 파트너 교환 기한일 | DR-Q-ETC | - |
| 파트너사명 | DR-Q-EC, DR-Q-ETC | - |
| SDEA 교환 의무 여부 | DR-Q-EC, DR-Q-ETC | 비대상 제외 |

# **5. Audit Log 기록 항목**

## **5.1 개요**

* 대시보드 관련 주요 행위(파라미터 변경, Export, 접근 등)는 Audit Log에 기록된다.
* Append-only 구조. 수정/삭제 불가.
* 모든 로그는 발생 일시(UTC), 행위 IP, Tenant명, Workspace명(해당 시) 포함.

## **5.2 기록 항목 전체 정의**

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **분류** | **Task** | **표시 문구** | **정책** | **Author** | **User** |
| 대시보드 접근 | 대시보드 진입 | Dashboard accessed: [레벨] [Tenant명/Workspace명/App명] | 대시보드 화면 진입 시. 레벨(Tenant/Workspace/App) 및 대상 표기. | 본인 ID | 본인 ID |
| 파라미터 | 파라미터 변경 | Dashboard parameter changed: [대시보드 종류] [파라미터명] [변경 전] → [변경 후] | Year·Month·날짜 범위·Product 등 파라미터 변경 시. 일회적 변경으로 저장 없음. | 본인 ID | - |
| Export | PDF Export | Dashboard exported (PDF): [대시보드 종류] [레벨] | PDF Export 실행 시. 대시보드 종류 및 접근 레벨 포함. | 본인 ID | 본인 ID |
| Export | EXCEL Export | Dashboard exported (Excel): [대시보드 종류] [레벨] | EXCEL Export 실행 시. | 본인 ID | 본인 ID |

* *Author: 행위를 발생시킨 주체. User: 행위의 적용 대상. 대시보드 접근·Export는 행위자 본인이 대상이므로 동일 값 기록.*

* *파라미터 변경은 일회성 조회 변경이므로 저장 이벤트 없이 변경 시점 기록만 남긴다.*

# **6. 개발 요구사항 종합**

## **6.1 공통**

|  |  |  |
| --- | --- | --- |
| **ID** | **요구사항** | **우선순위** |
| DR-CMN-01 | 대시보드 최근 업데이트 시간 표시 (배치 마지막 실행 시각 기준) | 필수 |
| DR-CMN-02 | 파라미터 변경 시 모든 패널 자동 갱신 | 필수 |
| DR-CMN-03 | 데이터 미발생: NA / 값 0: 0 으로 구분 표기 | 필수 |
| DR-CMN-04 | 차트 항목/그래프 클릭 시 관련 상세 데이터로 이동 (드릴다운) | 필수 |
| DR-CMN-05 | PDF Export: 현재 보고 있는 화면을 PDF 형식으로 Export. 파일 내 대시보드 종류·업데이트 일시·Export 시각 포함. | 필수 |
| DR-CMN-06 | EXCEL Export: 현재 화면 내 수치들을 EXCEL 형식으로 Export. 파일 내 메타 정보 포함. | 필수 |
| DR-CMN-07 | 외부 URL 공유 기능 미제공 | 필수 |
| DR-CMN-08 | Backoffice Admin은 고객사 대시보드 접근 불가. UI 레벨 및 API 레벨 차단. | 필수 |
| DR-CMN-09 | Workspace 데이터 격리: 추가로 생성된 Workspace 데이터는 Tenant Dashboard에 미포함. 해당 워크스페이스가 패쇄되어야 Dashboard에 정보 포함 됨. | 필수 |
| DR-CMN-10 | Workspace 대시보드는 Master Admin / Tenant Admin 전용. App Admin 이하는 App 레벨 대시보드만 접근 가능. | 필수 |

# **5. 미결사항**

* 인터랙티브 드릴다운: 캘린더에서 해당 케이스를 어떻게 필터링 해서 보낼지?

  + 현재 생각은 클릭 시 트래커에 필터링 결과를 조회할 수 있는 방식이 좋을듯 한데, 아직 트래커 기획이 미정이어서 확인 안됨

# **6. 참고 프로토타입? 스토리보드**

[status-dashboard-storybo…](/wiki/spaces/IS/pages/23560264/Dashboard?preview=%2F23560264%2F23822392%2Fstatus-dashboard-storyboard-v2_5.html)

[qc-dashboard-storyboard-…](/wiki/spaces/IS/pages/23560264/Dashboard?preview=%2F23560264%2F23068743%2Fqc-dashboard-storyboard-v2.html)
