|  |  |  |  |
| --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 |
| 김용성 | 2026.04.16 | - |  |
|  |  |  |  |

## 1. 개요

---

* **목적**: SafetyDB 플랫폼에서 XML Import 작업(Task) 단위의 이력을 조회하고, 각 Task 내 케이스별 변환 진행 상태를 모니터링하는 화면. Import 완료 후 케이스 처리 결과를 신속히 파악하고, 실패 케이스 원인 확인 및 후속 조치를 지원한다.
* **페이지 위치**: Safety > Data Hub > History
* **페이지 성격**: 모니터링 전용 (조회/확인 목적). 직접적인 데이터 수정이나 재처리 기능은 제공하지 않는다.

|  |  |
| --- | --- |
| 구분 | 내용 |
| 데이터 범위 | 워크스페이스 내 전체 XML Import Task 및 하위 케이스 |
| 접근 대상 역할 | 워크스페이스 내 전체 사용자 (본인 외 타 사용자 Task 포함 조회 가능) |
| 화면 구조 | 단일 페이지 내 Task(작업 단위) > Case(케이스 단위) 2-depth 구조 |

## 2. 정책

---

### 2.1 Task 상태 정책

Task의 전체 상태는 하위 케이스들의 변환 상태를 집계하여 결정한다.

|  |  |  |
| --- | --- | --- |
| 상태 | 조건 | 설명 |
| Converting | 하위 케이스 중 하나라도 변환 진행 중 | 작업이 아직 완료되지 않은 상태 |
| Success | 모든 케이스 변환 완료 | 전체 작업 성공 완료 |
| Fail | 하나라도 실패한 경우 | 부분 실패 포함. 상태별 케이스 수로 부분 실패 여부 구분 |

진행 중 케이스가 남아있으면 실패 케이스 유무와 무관하게 Converting을 유지하고, 모든 케이스 처리가 종료된 후 실패 존재 시 Fail로 전환한다.

### 2.2 케이스 식별자 정책

|  |  |  |
| --- | --- | --- |
| 변환 결과 | 식별자 | 설명 |
| 성공 | C.1.8.1 (Case Safety Report Unique ID) | 시스템에서 생성된 케이스 ID |
| 실패 | C.1.1 (Sender's Safety Report Unique ID) | 원본 XML의 Sender 식별자로 대체 |

### 2.3 케이스 변환 단계 정책

변환은 다음 5단계를 순차적으로 거친다. 스텝 인디케이터(Step Indicator)로 시각화하여 현재 단계 및 실패 단계를 표시한다.

```
Start → Duplicate Check → Follow-up Check → Configuration Applied → AE Type Categorized
```

각 단계의 시스템 내 상태값 정의는 XML Import 페이지 기획 완료 후 기획 회의 내에서 별도 논의 예정

### 2.4 접근 권한 정책

워크스페이스 내 전체 사용자가 전체 Import 이력을 조회할 수 있다. 본인이 수행하지 않은 타 사용자의 Task도 조회 가능하다.

### 2.5 필터링 정책

Task 레벨에서 3가지 필터를 제공한다. 케이스 레벨 필터는 모니터링 성격상 제공하지 않는다.

|  |  |  |
| --- | --- | --- |
| 필터 항목 | 기준 필드 | 비고 |
| Task 상태 | Status | Converting / Success / Fail |
| Import한 사용자 | Performer | 이름 기재 |
| Import 일시 | Started At | 날짜 단위 기간 검색 (Date Range) |
| Task 유형 | Type | Import / Export |

검색 정책: File Name 컬럼에 대해 부분 일치 검색을 지원하며, 대소문자를 구분하지 않는다. Performer 컬럼에도 검색을 지원한다.

### 2.6 Case 바로가기 정책

변환 성공한 케이스에 한해 Case 페이지로의 바로가기 링크를 제공한다. 실패 케이스에는 링크를 제공하지 않는다.

### 2.7 Task 정렬 정책

Task 테이블의 기본 정렬은 Started At 기준 내림차순(최신 순)으로 한다. 그 외 정렬은 제공하지 않는다.

### 2.8 데이터 수정/삭제 권한 정책

본 페이지는 모니터링 전용이므로, 어떤 역할이든 Task/Case 데이터의 수정, 삭제, 재처리(retry) 기능을 제공하지 않는다. URS 48의 Pending Case Management 등 사용자 개입이 필요한 기능은 본 페이지 범위 밖이다.

### 2.9 원본 XML 보관 기간 정책

타 데이터 정책과 동일하게, 계약기간 동안 보관 및 계약 종료 60일 이후에 파기한다.

### 2.10 Converting 태스크 정책

변환중인 태스크에 대해서는 Case 리스트를 제공하지 않고, ‘변환 진행 중입니다.’ 라는 안내 문구를 제공한다.

## 3. 요구사항

---

|  |  |  |  |
| --- | --- | --- | --- |
| 요구사항 | 기획 방향 | 의도 | 분류 |
| Task 목록 조회 | 테이블 형태로 Import Task 나열, 워크스페이스 내 전체 Import Task 공개 | 태스크 단위 모니터링 가능하도록 | Requirement |
| Task 상태 표시 | Converting / Success / Fail 3가지 상태로 표기 | 한눈에 전체 작업 완료 여부 파악 | Requirement |
| 상태별 케이스 수 표시 | Task 로우에서 성공/실패/진행 중 케이스 수 표시 | Fail 상태에서도 부분 성공 여부를 별도 상태 없이 파악 가능하게 | Enhancement |
| Task row 확장 | 클릭 시 row 확장, 하위 케이스 목록 표시 | Task > Case List 2-depth 구조 | Requirement |
| 케이스 변환 단계 스텝 인디케이터 | Start → Duplicate Check → Follow-up Check → Configuration Applied → AE Type Categorized | 케이스 단위 진행 상태 시각화 | Requirement |
| 케이스 식별자 표시 | 성공: C.1.8.1 / 실패: C.1.1 | 실패 케이스도 원본 XML과 대조 가능하도록 | Requirement |
| Tracker 바로가기 | 변환 성공한 케이스에 한해 Tracker 링크 제공 | 후속 작업으로 빠르게 이동 가능하도록 | Requirement |
| 원본 파일 재다운로드 | Task 단위로 원본 XML 파일 다운로드 버튼 제공 | Import한 원본 파일 재확인 가능하도록 | Requirement |
| Task 레벨 필터링 | Task 상태 / Import한 사용자 / Import 일시(Date Range) 기준 필터 제공 | 대량 이력 중 원하는 Task 빠르게 탐색 | Requirement |
| 에러 파일 출력 | 변환 실패한 케이스에 한해 에러 로그 txt 파일 제공 | 에러 원인을 사용자가 인지할 수 있도록 | Enhancement |

## 4. 출력 정보

---

### 4.1 Task 테이블

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 필드명 | 표시 여부 | 설명 | 옵션 | 비고 |
| No. | Y | Import 작업 순번 | — | Audit Trail Index와 규격 통일. |
| File Name | Y | Import된 원본 XML 파일명 | 필터: Y, 검색: Y (부분 일치, 대소문자 무관) |  |
| Total Cases | Y | Task 내 전체 케이스 수 | — | 실패 시 공란 처리 |
| 상태별 케이스 수 | Y | 성공 N / 실패 N / 진행 중 N | — | 표기할 수 있는 최적 UI 논의 필요 |
| Status | Y | Task 처리 상태 | 필터: Y | Converting / Success / Fail |
| Source | Y | 원본 XML 파일 재다운로드 | — |  |
| Started At | Y | 처리 시작 시각 (YYYY/MM/DD hh:mm:ss) | 필터: Y (기간 검색) | 사용자가 업로드 요청 → 시스템 처리 시작 시각 |
| Performer | Y | 작업 수행 사용자 | 필터: Y, 검색: Y | User name 표시 |

### 4.2 케이스 목록 (Task row 확장 시)

|  |  |  |  |
| --- | --- | --- | --- |
| 필드명 | 표시 여부 | 설명 | 비고 |
| Case 식별자 | Y | 성공: C.1.8.1 / 실패: C.1.1 | 실패 시 원본 XML Sender 식별자로 대체 |
| 최초 인지일 (C.1.4) | Y | XML Import 페이지에서 사용자가 입력한 값 | 케이스별로 상이할 수 있음 |
| 변환 단계 (Step Indicator) | Y | Start → Duplicate Check → Follow-up Check → Configuration Applied → AE Type Categorized | 현재 단계 및 실패 단계 시각화 |
| 에러 로그 다운로드 | 조건부 | 실패 케이스에 한해 상세 에러 로그 파일 다운로드 링크 제공 | 실패 사유 텍스트로 부족한 상세 정보가 필요할 때 사용 |
| Tracker 바로가기 | 조건부 | 성공 케이스에 한해 링크 제공 |  |

## 5. 기능 설명

---

|  |  |  |  |
| --- | --- | --- | --- |
| # | 기능명 | 설명 | 액션 |
| 1 | Summary Card 조회 | 워크스페이스 전체 기준 Total Imports / Success / Fail / Converting 수치를 페이지 상단 카드 형태로 표시. 필터 적용과 무관하게 고정값 유지 | 페이지 진입 시 자동 로드 |
| 2 | Task 테이블 조회 | 워크스페이스 내 전체 Import Task를 테이블 형태로 나열 | 페이지 진입 시 자동 로드 |
| 3 | Task 필터링 | Task 상태 / Performer / Started At(Date Range) 기준 필터 | 필터 UI 조작 |
| 4 | Task 검색 | File Name, Performer 부분 일치 검색 | 검색 입력 |
| 5 | Task row 확장 | Task 로우 클릭 시 하위 케이스 목록 표시 | 로우 클릭 (expand/collapse) |
| 6 | 케이스 변환 단계 확인 | Step Indicator로 변환 진행/완료/실패 단계 시각화 | 확장된 케이스 목록에서 확인 |
| 7 | Tracker 바로가기 | 성공 케이스의 Case 페이지 이동 | 링크 클릭 |
| 8 | 원본 XML 다운로드 | Task 단위 원본 XML 파일 재다운로드 | Source 컬럼 다운로드 버튼 클릭 |
| 9 | 케이스 에러 로그 다운로드 | 실패 케이스별 상세 에러 로그 파일 다운로드 | 케이스 row의 에러 로그 다운로드 링크 클릭 |

## 5-1. 제안 구조

---

```
Safety > Data Hub > Import History
│
├── [Summary Card] Total Imports / Success / Fail / Converting
│   └── 워크스페이스 전체 기준 고정값 (필터 적용과 무관)
│
├── [필터] Task 상태 / Import한 사용자 / Import 일시
│
└── Task 테이블
    ├── Task Row #1 (collapsed)
    │   └── [확장 시] Case 목록
    │       ├── Case #1 — Step Indicator — Tracker 링크
    │       ├── Case #2 — Step Indicator — 실패 사유 — 에러 로그 다운로드
    │       └── ...
    ├── Task Row #2
    └── ...
```

## 6. 프로토타입 / 와이어프레임

---

![image-20260416-090000.png](https://selta.atlassian.net/wiki/download/attachments/23888176/image-20260416-090000.png?api=v2)

<https://uncomputably-unannunciable-alleen.ngrok-free.dev/data_hub>

## 7. 엣지케이스 및 예외 처리

---

|  |  |  |  |
| --- | --- | --- | --- |
| # | 케이스 | 발생 조건 | 처리 방식 |
| EC-01 | XML 파일 내 유효 케이스 0건 | 유효한 케이스가 없는 XML 업로드 | Task 생성 여부 및 처리 방식 확인 필요 (미결) - Import 기획 시 논의 예정 |
| EC-02 | 동일 파일 중복 Import | 동일한 XML 파일 재업로드 시 | Duplicate Check 단계에서 전량 차단 가능. 사용자 안내 방식 논의 필요 (미결) - |
| EC-03 | Import History 데이터 없음 | 워크스페이스에서 XML Import를 한 번도 수행하지 않은 경우 | 빈 상태(Empty State) 화면    Main: "Import 이력이 없습니다."  Sub: "XML 파일을 Import하면 여기에서 작업 현황을 확인할 수 있습니다." |
| EC-04 | Task 내 대량 케이스 | 하나의 Task에 케이스 수가 매우 많은 경우 row 확장 시 | 최대 제한 없음 |
| EC-05 | 변환 단계 장시간 정체 | 특정 단계에서 변환이 비정상적으로 오래 걸리는 경우 | 추후 XML Import 기획 완료 후 논의 예정 |

## 8. 레퍼런스 자료

---

> 개발 시 참고하면 좋을 문서를 첨부합니다.

[xml\_import\_history\_useca…](/wiki/spaces/IS/pages/23888176/Import%2BHistory?preview=%2F23888176%2F33423403%2Fxml_import_history_usecase.md)
