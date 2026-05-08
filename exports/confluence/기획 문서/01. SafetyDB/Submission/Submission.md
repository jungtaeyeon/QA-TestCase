# Submission (보고 실행 및 배포)

| **이름** | **날짜** | **변경 사항** | **제품 버전** |
| --- | --- | --- | --- |
| 김병환 | 2026-04-29 | 배치 재생성 케이스여도, 보고 상태는 <https://selta.atlassian.net/wiki/spaces/IS/whiteboard/44367917?atl_f=PAGETREE> 문서 기준Drafting(보고), MA(ICSR Process)으로 이동   * 배치만 재성성하는 것은 고도화에서 진행   Triage가 완료 되연 보고 기준으로 Drafting 단계가 되는데 이때 부터 Submission List 노출  보고 단계에 Ready to Submit 인데, ICSR Processing 단계가 Approval, 상태가 Approved가 아니면 보고 불가 → 에러 발생  보고 시 오류가 발생한 경우에는 Drafting 단계로 전환 |  |
| 김병환 | 2026-04-28 | 실제 MFDS ACK 파일 추가 검증 결과, AE + CR 조합 확인. 케이스 오류 시 배치 레벨 AE와 케이스 레벨 CR이 함께 수신됨.   * ACK.A.5에 CR 발생 케이스 ID 목록 포함 (예: I:케이스번호) 되는 것 확인 * 위에 따라 AE + CR 시 CR 대응(C: Lock 해제 → Entry)이 우선이며 배치 생성 팝업 불필요.    **성공&오류 별 대응 정책의 표1, 표2** 에 해당 내용 반영. |  |
| 김병환 | 2026-04-28 | N.1.5 / N.2.r.4 / C.1.2 구조 확인 결과, 배치 생성 시 N.1.5만 세팅하고 N.2.r.4/C.1.2는 건드리지 않는 것으로 변경. C.1.2는 케이스별 ICSR 버전 타임스탬프로 케이스 내용 변경 시에만 갱신되어야 함. 배치 재생성은 케이스 변경이 아니므로 갱신 불필요.  신규 배치 생성(AE/AR 오류 대응) 시에도 N.1.5만 새로 세팅 |  |
| 김병환 | 2026-04-28 | **수정 1 — 3.3 오류별 대응 정책표 전체 재구성**   * 단일 표 → 4개 표 분리 (배치 레벨 / 케이스 레벨 / CR 상세 / 타임아웃) * CR 대응: B(신규 배치 생성) → C(Lock 해제 → Entry, 시스템 자동 처리, 팝업 없음) * R/P/C/N은 CR의 ACK.B.r.7 상세 사유로 명시 * 구조 설명 추가   **수정 2 — 3.3 배치 상태에 따른 Result 값 표**   * ASIS: `ACK Error: AE/AR/CR/R/P/C/N` * TOBE: `배치 오류: AE / AR. 케이스 오류: CR (상세: R/P/C/N)`   **수정 3 — 3.3 보고 시 배치 상태 정의 — Failed 행**   * ASIS: `배치 내 일부 케이스만 오류인 경우도 배치 Status는 Failed로 처리(실제 규제기관에서 Failed로 올것으로 보이나 일단 작성 했습니다.)` * TOBE: `배치 레벨 오류(AE/AR) 시 Failed. 배치 정상(AA)이나 일부 케이스 CR 수신 시에도 Failed. CR 케이스는 시스템 자동으로 Lock 해제 → Entry, 정상 케이스(CA)는 이미 접수 완료 상태`   **수정 4 — 3.3 배치 생성과 정보 업데이트**   * ASIS: N.2.r.4/C.1.2와 N.1.5를 별도 행으로 분리, N.1.5는 `Queued→Transmitting 전환 직전 시간` * TOBE: `N.1.5, N.2.r.4, C.1.2: 배치 생성 시점의 타임스탬프를 동일하게 세팅` (한 행으로 통합)   **수정 5 — 5.2 Submitting Monitoring 필드 — Acknowledge**   * ASIS: `ACK.A.3 Date of Batch Transmission` * TOBE: `ACK.M.4 Acknowledgement Date of Batch Transmission`   **수정 6 — 5.2 Submitting Monitoring 필드 — Ack Comment**   * ASIS: `ACK Comment 필드 전달값`, 케이스 ❌ * TOBE: `배치 행: ACK.A.5 값이 있으면 ACK Error 표시. 케이스 행: ACK.B.r.7 값이 있으면 ACK Error 표시. 상세 내용은 ACK 파일 다운로드로 확인`, 케이스 ✅   **수정 7 — 5.2 Submitting Monitoring 필드 — Result 비고**   * ASIS: `개별 케이스와 배치 모두에 관련 결과 표시` * TOBE: `배치 행: AE / AR / Timeout. 케이스 행: CA / CR + 상세코드(R/P/C/N). 배치 Failed 시 중복 제거 후 나열 (예: CR: R, C)`   **수정 8 — 5.2 Submitting Monitoring 필드 — Submission date 비고**   * ASIS: `케이스 단위: 해당 케이스가 속한 배치의 N.1.5 동일 값 표시` * TOBE: `N.1.5 = 배치 생성 시점 타임스탬프 자동 세팅. 케이스 단위: 해당 배치의 N.1.5 동일 값 표시`   **수정 9 — 4. 요구사항 — F-13**   * ASIS: `Batch 오류(AE/AR) 및 ICSR 중대 오류(CR) 시 신규 배치 생성` * TOBE: `Batch 오류(AE/AR) 시 신규 배치 생성. 기존 케이스 데이터 미변경`   **수정 10 — 4. 요구사항 — 오류 대응 C**   * ASIS: `필수값 누락(R), 조건부 필수(P), 코드 오류(C), nullFlavor(N) → Lock 해제` * TOBE: `ICSR 오류(CR) 수신 시 Lock 해제. CR 상세 사유: 필수값 누락(R), 조건부 필수(P), 코드 오류(C), nullFlavor(N)` |  |
| 김병환 | 2026-04-17 | 피드백 받은 부분 수준 |  |
| Claude (PX Expert Q&A 기반) | 2026-04-10 | 최초 작성 (Rough Draft) |  |
| Claude (plan-linter) | 2026-04-10 | 표준화 및 보강 |  |

프로토타입: [submission\_prototype\_v4.…](/wiki/spaces/IS/pages/23068729/Submission?preview=%2F23068729%2F46956604%2Fsubmission_prototype_v4.html)

## 1. 개요

* **목적**: Validation을 통과한 ICSR을 선정하고, 선정된 ICSR을 배치단위로 규제기관에 법적 기한 내 전송하고, 전송 결과를 추적·증빙하여 보고를 완료 한다.
* **페이지 위치**: Safety > Submission

  + 하위: Submission List / Submission Monitoring

## 2. 전체 흐름

1. RA Triage가 완료 된 케이스의 Submission 상태가 ‘Drafting’으로 변경 된다.
2. 사용자는 Submission List 페이지에서 내가 보고할 케이스를 선택한다.
3. 보고할 케이스를 선택하고 보고를 진행한다
4. 보고는 배치 단위로 묶여서 진행 된다.

   1. 보고가 진행되는 동안 보고 진행 케이스는 수정이 불가능하게 된다.
5. Submission Monitoring에서 보고 진행 상황 및 완료 여부 확인

   1. 보고가 정상적으로 문제 없이 완료되면 해당 케이스의 Workflow 단계가 ‘Completion’으로 변경
   2. 보고가 완료 되면 (성공/실패 상관 없이) ACK 파일을 받을 수 있다.
   3. 보고 시 문제가 있으면 오류에 따른 처리 방법이 수행

## 3. 정책

### 3.1 기능 범위 정책

| **구분** | **내용** |
| --- | --- |
| 프로세스 시작점 | Workflow 단계 ‘RA Triage'가 완료되어, Submission 상태가 ‘Drafting’이 된 케이스를 대상 |
| 데이터 범위 | Initial 및 Follow-up 포함 모든 ICSR |
| 보고 채널 | MFDS 단일이고 향후 다른 규제기관으로 확장 |
| 접근 권한 | 따로 없음. |

### 3.2 Submission List — 보고 할 케이스 집계 및 배치 실행 정책

#### 보고 대상 집계 기준

| **조건** | **동작** |
| --- | --- |
| 워크플로우 상태 | Workflow 단계 ‘RA Triage'가 완료되어, Submission 상태가 ‘Drafting’이 된 케이스를 자동 집계   * List에서는 해당 케이스들의 Submission Statis를 표시 * Workflow와 Workflow Status는 가지고 있는 값 그대로 표시 |
| Expedited 보고(신속), Periodic 보고(정기) 분리 | Submission List 내 페이지 구분 필요   * Expedited (디폴트): 해당 페이지 들어올 때 먼저 보이는 화면    + Workflow 단계 ‘RA Triage'가 완료되어, Submission 상태가 ‘Drafting’이 된 케이스 중, RA 값이 있고, 신속보고 여부에 체크가 되어 있는 것만 노출 * Periodic: Workflow 단계 ‘RA Triage’ 가 완료되어, Submission 상태가 ‘Drafting’이 된 케이스 증, RA 값이 있고, 신속보고 여부에 체크가 되어 있지 않은 것만 노출 |

#### Submission List 동작

| **조건** | **동작** |
| --- | --- |
| 목록 내 케이스 개수 및 정렬 기준 | 페이지당 25개 케이스 노출  페이지 내 케이스 정렬 기준   1. Due Date(RA) 가장 임박한 것 우선 2. 동일 Due Date인 경우, Case ID 오름 차순(이전에 등록된 것 먼저 노출) |
| 검색 필터 | CASE ID 키워드 검색  Case Owner 필터 (다중 선택, 최대 5개)  Workflow 필터 (다중 선택, 최대 5개)  Workflow Status 필터 (다중 선택, 최대 5개)  Submission Status 필터 (다중 선택, 최대 5개)  Destination 필터 (다중 선택, 최대 5개) |
| 페이지 내 버튼: Submit | Submit   * 목록에서 케이스 선택 후 해당 버튼 클릭 하면 확인 팝업 노출 후 보고 진행 * 팝업 메시지    + 타이틀: 배치 생성 확인   + 내용: 선택한 N건의 케이스로 배치를 생성하고 MFDS에 보고를 진행하시겠습니까?   + 버튼: 취소, 보고 진행 * 동시에 25건만 생성 가능    + 다른 페이지로 넘어가면 선택된것 초기화 됨. |
| 보고 시 배치 생성 | 목록에서 케이스를 1개 이상 선택 후 Submit 클릭 시 배치 생성하여 보고 진행  케이스 여러개 선택 시 동일 Receiver인 케이스만 유효한 배치로 묶음. 상이한 Receiver 혼재 시 자동 차단   [IS-1678](https://selta.atlassian.net/browse/IS-1678?src=confmacro)   * 현재는 리시버가 1군데여서, MFDS 이외 리시버 추가 시(다른 규제기관, 파트너사) 해당 로직 추가 필요 → 고도화 이슈   Submission Status가 Ready to Submit 이고 Workflow가 Approval, Workflow Status가 Approved 인것만 배치 생성 가능, 나머지 케이스를 선택하여 배치 생성 시에는 에러   * 에러 메시지: Submission Status가 Ready to Submit 이고 Workflow가 Approval, Workflow Status가 Approved 일때만 보고 할 수 있습니다. |
| 보고 시 화면 동작 | 보고가 시작되는 케이스는 Submission List에서 제외   * 이미 배치 상태가 "Queued"인 경우, 케이스 재선택 시 시스템에서 배치를 생성하지 않고 차단 |

### 3.3 Submission Monitoring — 보고 진행 및 결과 확인

#### 해당 페이지 설계 시 고려

| **조건** | **동작** |
| --- | --- |
| 보고 이력, 보고를 진행한 파일과 ACK 파일 | 계약 종료 시점 까지 보관 필요 / 계약 중 해당 데이터 변조 및 삭제 불가 |

#### 조회 대상 집계

| **조건** | **동작** |
| --- | --- |
| 보고 진행 중, 보고 완료, 보고 실패 건 | Submission List 페이지에서 보고를 진행한 배치와 그 케이스를 조회 할 있고 배치의 상태도 함께 조회 가능 |
| 신속 보고, 정기 보고 분리 | 필터를 통해서 보고 진행 및 결과 확인 시 신속 보고 또는 정기 보고 인지 분리하여 조회 가능 |

#### **Submission Status 정의**

| **상태** | **설명** |
| --- | --- |
| Drafting | RA Triage가 완료된 상태 |
| Ready to RP | ICSR Processing에서 승인이 완료 된 상태 |
| Submitting | 보고 진행 중 상태  보고 진행 중 상태는 내부적으로는 해당 단계로 동작한다.  Queued - 전송대기: 배치 생성 완료, 게이트웨이 전송 전  Transmitting - 전송중: MFDS AS2로 전송 시작됨  Waiting ACK - 전송 완료: MFDS ACK 응답 대기 중  Received ACK - ACK 정상 수신 |
| Submitted | 보고가 완료된 상태  보고 성공, 보고가 되었으나 문제가 있는 경우, 보고가 되었으나 ACK 파일을 못받은 경우에 대해서는 Result에서 표시 |

#### 배치 상태에 따른 Result 값

| **상태** | **Result 표시 여부** | **표시 할 Result 값** |
| --- | --- | --- |
| Ready to Submit | X | - |
| Submitting | X | 보고가 정상적으로 진행되는 경우  Queued, Transmitting, Waiting ACK, Received ACK 표시   * 단계로 변경되는 경우 그 단계 맞춰서 Result에 표시     보고 자체가 1시간 이상 진행되지 않은 경우   * 배치 행에 표시: Submission Timeout |
| Submitted | O | Receive ACK.이면서 보고에 문제 없는 경우(=ACK 파일에 에러 코드 없음)   * ACK Accept   Receive ACK.이면서 보고에 문제 있는 경우(=ACK 파일에 에러 코드 있음   * 배치 행에 표시: AE/AR * 케이스 행에 표시: CR (상세: R/P/C/N)     Waiting ACK 상태에서 48시간 내 ACK를 받지 못한 경우   * 배치 행에 표시: ACK Timeout |

#### Submission Monitoring 동작

| **조건** | **동작** |
| --- | --- |
| 목록 내 케이스 개수 및 정렬 기준 | 페이지당 25개 케이스 노출  페이지 내 배치 정렬 기준: 배치 생성일시 역순 |
| 리프레시 기능 | 해당 페이지 리프레시 지원하는 버튼 추가 |
| 검색 필터 | CASE ID 키워드 검색  Reporter 필터 (다중 선택, 최대 5개)  Status 필터 (다중 선택, 최대 5개)  Result 필터 (다중 선택, 최대 5개)  Destination 필터 (다중 선택, 최대 5개)  신속보고/정기보고 구분 필터 |
| 상태/결과 변환 | <https://selta.atlassian.net/wiki/spaces/IS/pages/23068729/Submission#Submission-Status-%EC%A0%95%EC%9D%98> 와 <https://selta.atlassian.net/wiki/spaces/IS/pages/23068729/Submission#%EB%B0%B0%EC%B9%98-%EC%83%81%ED%83%9C%EC%97%90-%EB%94%B0%EB%A5%B8-Result-%EA%B0%92> 맞춰 표시   * 변경 된 것은 화면에 바로 반영은 안되고 리프레시 해야 함. |
| 상태 변환에 따른 단계별 흐름 표시 | 각 단계별 흐름을 배치별로 화면에 표시(Wizard UI 형식)   * 기본으로는 <https://selta.atlassian.net/wiki/spaces/IS/pages/23068729/Submission#Submission-Status-%EC%A0%95%EC%9D%98> 내 Submitting 에 있는 흐름을 표시    + 흐름 표시      - 진행 하지 않음: 흐름 표시 영역에 아무것도 표시 하지 않음     - 진행 중, 진행 완료: 구분하여 표시     - 해당 상태에서 문제가 있는 경우: 따로 표시 |
| ACK 파일 다운로드 | 보고가 정상적으로 완료 된 것은 해당 배치와 관련된 ACK 또는 ACK Comment가 등록되고, ACK의 파일의 경우, 사용자는 해당 파일을 다운로드 가능 |
| 배치 파일 내 케이스 조회 | 배치 파일에 포함되어 있는 케이스를 조회 할 수 있어야 한다.  배치 파일 클릭 시 해당 배치 파일에 포함된 케이스의 ID와 해당 케이스의 보고 시간, 결과, 정시 보고 여부를 확인 필요 - 보고 시간과 결과는 기존 배치와 동일하게 하되, 특정 케이스의 문제가 있는 경우 해당 케이스의 상태는 따로 표시 - 정시 보고 여부는 아래의 조건에 따라 판단  - ACK 수신 시점이 Due Date 이전이거나 동일한 날: On-Time 으로 표시  - ACK 수신 시점이 Due Date 이후: Late로 표시 |
| 완료에 따른 처리 | 아래의 오류에 따라 특정 단계로 전환 후 고객이 직접 오류 대응 |
| 전송 중 무결성 보장 | 보고가 시작된 케이스는 보고가 끝나기 전까지 수정 불가  보고가 시작된 케이스는 Submission List에서 제외 |

#### 배치 생성과 정보 업데이트

| **조건** | **동작** |
| --- | --- |
| 배치 생성 | Submission List에서 케이스를 선택하여 Submit 클릭 시 배치 생성 |
| 배치 생성 시 정보 업데이트 | N.1.5: 배치 생성 시점의 타임스탬프를 동일하게 세팅 |
| 단순 재전송 (Submission Timeout, ACK Timeout) 시 배치 생성 | XML 내 모든 timestamp(N.1.5/N.2.r.4/C.1.2) 유지하고 그대로 재송신 |
| 신규 배치 생성 (AE/AR/CR 오류 대응) | 새 Batch Number 발급 → N.1.5만 새로 갱신 |

#### **성공&오류 별 대응 정책**

출처와 내용은 ICH Guideline과 국내외 시판 후 의약품 이상사례 보고 시스템 사용자 매뉴얼 v.3.1 (2025년 11월 버전)

[1\_ICH\_ICSR\_Implementatio…](/wiki/spaces/IS/pages/23068729/Submission?preview=%2F23068729%2F48529444%2F1_ICH_ICSR_Implementation_Guide_v5_03.pdf)[국내·외 시판 후 의약ᄑ…](/wiki/spaces/IS/pages/23068729/Submission?preview=%2F23068729%2F29950035%2F%E1%84%80%E1%85%AE%E1%86%A8%E1%84%82%E1%85%A2%C2%B7%E1%84%8B%E1%85%AC+%E1%84%89%E1%85%B5%E1%84%91%E1%85%A1%E1%86%AB+%E1%84%92%E1%85%AE+%E1%84%8B%E1%85%B4%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A1%E1%86%BC%E1%84%89%E1%85%A1%E1%84%85%E1%85%A8%E1%84%87%E1%85%A9%E1%84%80%E1%85%A9%E1%84%89%E1%85%B5%E1%84%89%E1%85%B3%E1%84%90%E1%85%A6%E1%86%B7+%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%8C%E1%85%A1+%E1%84%86%E1%85%A2%E1%84%82%E1%85%B2%E1%84%8B%E1%85%A5%E1%86%AF%28%E1%84%8B%E1%85%B4%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%91%E1%85%AE%E1%86%B7%E1%84%8B%E1%85%A1%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%82%E1%85%A1%E1%84%85%E1%85%A1%29_v3.1+%281%29.pdf)

##### 오류 구분 체계

* 배치 레벨 (ACK.A.4): 배치 메타데이터(N.1.1~N.1.5) 검증 결과. AA.AE/AR 해당.

  + 오류 상세: ACK.A.5 (Batch Validation Error, 선택사항)
* 케이스 레벨 (ACK.B.r.6): 배치 정상(AA) 수신 시 개별 ICSR 검증 결과. CA/CR 해당.

  + 해당 오류의 경우 배치 내 일부 케이스만 CR이고 나머지는 CA(정상접수완료) 일 수 있음
  + 오류 상세: ACK.B.r.7 (Error/Warning Message or Comment)
* 타임아웃: MFDS ACK 코드가 아닌 시스템 자체 정의 상태.
* 오류 상세 정보 표시: 배치 행 Ack Comment에 ACK.A.5 값, 케이스 행 Ack Comment에 ACK.B.r.7 값 표시

###### 표 1) 배치 레벨 오류 (ACK.A.4 - Transmission Acknowledgement Code)

* 배치 메타데이터(N.1.1~N.1.5) 검증 결과. MFDS가 배치 XML을 수신하여 검증 후 응답하는 코드.
* 배치 레벨에서의 오류 시 배치 신규 생성하는 것은 고도화에서 진행

| **ACK.A.4** | **의미** | 시스템 처리 방식 | 오류 버튼 클릭 시 팝업 |
| --- | --- | --- | --- |
| AA | 접수통지 승인. 추가 대응 없음 | Receive ACK 상태로 변경 | - |
| AE | 접수통지 오류. 상세정보 추가 제공되고 대응 필요 | AE 단독(CR 없음), AE + CR 으로 오는 케이스 모두 Submission 상태 ‘Drafting’으로 변경, 이후 사용자가 ICSR Processing Workflow 단계 재진행 필요 | AE 단독, AE + CR으로 오는 케이스 모두 시스템이 자동으로 Workflow 단계 및 상태 변경. |
| AR | 접수통지 거절. 전체 파일 재전송 필요 | 문제가 있는 케이스 모두 Submission 상태 ‘Drafting’으로 변경, 이후 사용자가 ICSR Processing Workflow 단계 재진행 필요 | 시스템이 자동으로 Workflow 단계 및 상태변경. |

###### 표 2) 케이스 레벨 오류 (ACK.B.r.6 - Acknowledgemant Code for a ICSR Message)

* 배치 AE 수신 시 배치 내 개별 ICSR에 대한 검증 결과. AE + CR 조합으로 수신되며, ACK.A.5에 CR 발생 케이스 ID 목록이 포함됨. 배치 내 일부 케이스만 CR이고 나머지는 CA(정상 접수 완료)일 수 있음.

| **ACK.B.r.6** | 의미 | 시스템 처리 방식 | 오류 버튼 클릭 시 팝업 |
| --- | --- | --- | --- |
| CA | 데이터 전송 완료. 해당 ICSR 정상 접수 | - | - |
| CR | 데이터 전송 실패. 해당 ICSR에 치명적 오류, 접수 불가. 상세 사유는 ACK.B.r.7에 R/P/C/N 코드로 포함 | 문제가 있는 케이스 모두 Submission 상태 ‘Drafting’으로 변경, 이후 사용자가 ICSR Processing Workflow 단계 재진행 필요 | 시스템이 자동으로 Workflow 단계 및 상태변경. |

###### 표 3) CR 상세 사유 코드(ACK.B.r.7, MFDS 정의)

* CR이 발생한 ICSR의 ACK.B.r.7 필드에 아래 형식으로 오류 항목이 명시됨.

| **코드** | 의미 | **ACK 파일 내 표시 형식** |
| --- | --- | --- |
| R | 필수 값 누락 | R:항목ID (예: R:C.1.2) |
| P | 조건부 필수 값 누락 | P:항목ID (예: P:D.10.2b) |
| C | 코드 모록에 없는 값 (MedDRA, 의약품코드, 국가코드 등) | C:항목ID (예: C:D.10.6) |
| N | null을 허용하지 않는 항목에 nullFlavor 사용 또는 허용하지 않는 nullFlavor 플래그 사용 | N:항목ID (예: N:C.2.r.3) |

###### 표 4) 타임아웃 (시스템 자체 정의, ACK 코드 아님)

| 종류 | 오류 유형 | 시스템 처리 방식 | 오류 버튼 클릭 시 팝업 |
| --- | --- | --- | --- |
| 타임아웃 | 전송 후 게이트웨이 응답 없음 (네트워크 장애, 게이트웨이 일시 오류) | A: 단순 재전송 — 배치 재생성 없이 기존에 만든 배치 그대로 즉시 재전송 | 타이틀: 오류 대응 - 타임아웃  내용: ACK 응답이 수신되지 않았습니다. 기존 배치를 그대로 재전송합니다.  버튼: 취소, 재전송   * 재전송: 보고하려던 파일 그대로 다시 보고 진행    + 기존 행의 정보들 업데이트 |
| 보고 결과를 48시간 내 받지 못한 경우 | 보고 전달 후 48시간 내 피드백(실패/성공 여부, ACK 파일 수령) 받지 못한 경우 | A: 단순 재전송 — 배치 재생성 없이 기존에 만든 배치 그대로 즉시 재전송 | 타이틀: 오류 대응 - 타임아웃  내용: ACK 응답이 수신되지 않았습니다. 기존 배치를 그대로 재전송합니다.  버튼: 취소, 재전송   * 재전송: 보고하려던 파일 그대로 다시 보고 진행    + 기존 행의 정보들 업데이트 |

## 4. 요구사항

| 요구사항 | 기획 방향 | 의도 |
| --- | --- | --- |
| Submission List 화면 신규 구성 | Tracker와 분리된 보고 전용 작업 화면. Submission 상태 케이스 자동 집계 | 보고 실행과 케이스 처리 역할 분리 |
| 신속/정기 보고 탭 분리 | Submission List 내 신속 보고(디폴트)·정기 보고 페이지 분리.  신속보고   * Workflow 단계 ‘RA Triage'가 완료되어, Submission 상태가 ‘Drafting’이 된 케이스 중, RA 값이 있고, 신속보고 여부에 체크가 되어 있는 것만 노출   정기보고   * Workflow 단계 ‘RA Triage’ 가 완료되어, Submission 상태가 ‘Drafting’이 된 케이스 증, RA 값이 있고, 신속보고 여부에 체크가 되어 있지 않은 것만 노출 | 보고 유형별 작업 영역 구분 |
| Submission List 정렬 — Due Date 임박순, 동일 시 Case ID 오름차순 | 목록 자동 정렬 | 기한 누락 방지 |
| Submission List 검색·필터 | Case ID 키워드 검색 + Case Owner/Status/Destination 다중 선택 필터 (각 최대 5개) | 보고 대상 탐색 |
| 배치(Batch) 생성 및 E2B 전송 | 단일/다중 케이스 선택 → 배치 생성 → MFDS AS2 게이트웨이 전송 | MFDS 보고 처리 |
| 전송 전 자동 차단 | 동일 Receiver 케이스만 유효 배치로 묶음. 상이한 Receiver 혼재 시 자동 차단. 전송 중 케이스 재선택 차단 | 유효한 배치만 생성, 사용자 인터럽트 최소화 |
| 전송 중 System Freeze | 보고 진행 중 해당 케이스 수정 불가. 보고 시작 케이스는 Submission List에서 제외 | 전송 데이터 무결성 보장 |
| Submission Monitoring 화면 신규 구성 | 배치 단위 실시간 상태 표시 + Expandable Row로 케이스 상세 드릴다운 | 보고 중 상태 가시성 확보 |
| ACK 자동 매핑 | 수신 ACK를 배치·케이스에 자동 매핑, 성공/실패 즉시 반영 | 수동 대조 작업 제거 |
| 오류 대응 — 단순 재전송 (A) | 타임아웃 오류 시 배치 재생성 없이 기존 배치 즉시 재전송 | 전송 오류 복구 비용 최소화 |
| 오류 대응 — 신규 배치 생성 (B) | Batch 오류(AE/AR) 시 신규 배치 생성. 기존 케이스 데이터 미변경 | 데이터 오류 대응 완결성  goek |
| 오류 대응 — Lock 해제·수정 흐름 (C) | ICSR 오류(CR) 수신 시 Lock 해제. CR 상세 사유: 필수값 누락(R), 조건부 필수(P), 코드 오류(C), nullFlavor(N) → 케이스 모두 Submission 상태 ‘Drafting’으로 변경, 이후 사용자가 ICSR Processing Workflow 단계 재진행 필요 | 데이터 수정 후 재보고 경로 |
| Submission Log (보고 이력 전수 목록) | 전송 파일(XML) + ACK 파일 계약 종료까지 보관. 변조·삭제 불가 | GxP Audit Trail 요건 충족 |
| On-time / Late 자동 판정 | ACK 수신 시점과 Due Date 비교하여 자동 표시   * ACK 수신 시점이 Due Date 이전이거나 동일한 날: On-Time 으로 표시 * ACK 수신 시점이 Due Date 이후: Late로 표시 | 준수율 지표 자동 산출 |

## 5. 출력 정보

### 5.1 Submission List 필드

| **필드명** | **설명** | **필터/검색** | **비고** |
| --- | --- | --- | --- |
| CASE ID | 케이스 고유 식별자. FU 여부 표시(FU Info) | 검색(Y) / 필터(Y) | C.1.1 |
| Case Owner | 케이스 담당자 이름 | 필터(Y, 최대 5개) | 등록된 이름 표시 |
| Workflow | 현재 케이스 워크플로우 단계 표시 | 필터(Y, 최대 5개) | ex Approval |
| Workflow Status | 해당 워크플로우의 상태 표시 | 필터(Y, 최대 5개) | ex. In Progrss, Approved |
| Submission Status | 보고 상태 표시 | 필터(Y, 최대 5개) | Submission Status 기준 ‘Drafting’ 단계 부터 표시 |
| Destination | 보고 수신처. 현재 MFDS 고정 | 필터(Y, 최대 5개) | 규제기관명 표시: MFDS |
| Due Date | AE Type 기반 Triage 산출 보고 기한 |  | YYYY-MM-DD 형식 |
| Deadline | AE Type 기반 Triage 산출 보고 기한 |  | D-남은일 형식, 당일인 경우 D-0, 지난 경우 Late로 표시 |

### 5.2 Submitting Monitoring 필드

| **필드명** | **배치 단위 표시** | **케이스 단위 표시** | **설명** | **비고** |
| --- | --- | --- | --- | --- |
| Category | ✅ | ❌ | 해당 배치가 신속/정기 인지 구분   * 신속, 정기로 구분 |  |
| Batch No / CASE ID | 배치 번호 표시 | CASE ID 표시 | 배치 행이면 Batch No, 케이스 행이면 Case ID | — |
| Reporter | ✅ | ❌ | 보고 실행한 사람 이름 | 케이스 행 미표시 |
| Status | ✅ | ❌ | <https://selta.atlassian.net/wiki/spaces/IS/pages/23068729/Submission#Submission-Status-%EC%A0%95%EC%9D%98> 에 정의 된 값 표시 | 케이스 행 미표시 |
| Destination | ✅ | ❌ | 보고 수신처 | 향후 Receiver별 동적 값 |
| Submission date | ✅ | ✅ | N.1.5 = 배치 생성 시점 타임스탬프 자동 세팅. | 케이스 단위: 해당 배치의 N.1.5 동일 값 표시 |
| Result | ✅ | ✅ | <https://selta.atlassian.net/wiki/spaces/IS/pages/23068729/Submission#%EB%B0%B0%EC%B9%98-%EC%83%81%ED%83%9C%EC%97%90-%EB%94%B0%EB%A5%B8-Result-%EA%B0%92> 표시  케이스 행에 에러를 표시할 때 에러 여러가지인 경우 중복 제거 후 나열 (예: CR: R, C) | 개별 케이스와 배치 모두에 관련 결과 표시 |
| Acknowledge | ✅ | ❌ | ACK 내 ACK가 전송된 시간(ACK.M.4 Acknowledgement Date of Batch Transmission)을 표시하며, 규제당국으로부터 ACK를 받았을 때 표시 | 배치 단위만 표시 |
| On-time / Late | ❌ | ✅ | ACK 수신 시점 vs Due Date 비교 결과  해당 값은 케이스 값을 펼쳐서 볼때 Acknowledge 자리에서 해당 값 노출 | On Time / Late |
| Ack Comment | ✅ | ❌ | 배치 행: ACK.A.5 값이 있으면 ACK Error 표시. | 케이스 행 미표시 |
| File | ✅ | ❌ | 전송한 XML 파일 클릭 시 다운로드 | 케이스 행 미표시 |
| ACK | ✅ | ❌ | 전달받은 ACK 파일. 클릭 시 다운로드 | 케이스 행 미표시 |

### 5.3 Submitting Monitoring 내 흐름 표시

* <https://selta.atlassian.net/wiki/spaces/IS/pages/23068729/Submission#Submission-Monitoring-%EB%8F%99%EC%9E%91> 내 ‘상태 변환에 따른 단계별 흐름 표시’ 적용

## 6. 기능 설명

| # | 기능명 | 설명 | 액션 |
| --- | --- | --- | --- |
| F-01 | Submission List 자동 집계 | Submission 상태가 ‘Drafting’ 케이스를 자동으로 목록에 표시. 신속 보고·정기 보고 페이지 분리 노출 | 시스템 자동 |
| F-02 | Submission List 정렬 | Due Date 임박순 우선 정렬. 동일 Due Date 시 Case ID 오름차순. 페이지당 25건 | 시스템 자동 |
| F-03 | Submission List 검색·필터 | Case ID 키워드 검색 + Case Owner/Status/Destination 다중 선택 필터 (각 최대 5개) | 사용자 실행 |
| F-04 | 배치 생성 및 전송 | 케이스 선택 → 배치 생성 → MFDS AS2 전송. 상이한 Receiver 혼재 시 자동 차단 | 사용자 실행 |
| F-05 | 전송 중 System Freeze | 보고 시작 케이스 수정 불가 + Submission List에서 제외. 전송 중 케이스 재선택 시 배치 생성 차단 | 시스템 자동 |
| F-06 | 배치 단위 흐름 모니터링 | Queued → Transmitting → Waiting ACK → Receive ACK / Failed 상태 전환. 리프레시 시 화면 반영 | 시스템 자동 |
| F-07 | Submission Monitoring 정렬·필터 | 페이지당 25건, 배치 생성일시 역순 정렬. Case ID/Reporter/Workflow/Destination/신속·정기 구분 필터 | 사용자 실행 |
| F-08 | 케이스 드릴다운 (Expandable Row) | Submission Monitoring에서 배치 행 클릭 시 포함 케이스 ID, 보고 시간, 결과, 정시 보고 여부 표시 | 사용자 실행 |
| F-09 | ACK 자동 매핑 | MFDS ACK 수신 시 배치·케이스에 자동 매핑, 상태 즉시 반영 | 시스템 자동 |
| F-10 | ACK 파일 다운로드 | Submission Monitoring 배치 행의 ACK 필드 클릭 시 ACK 파일 다운로드 | 사용자 실행 |
| F-11 | On-time / Late 자동 판정 | 케이스 행에서 ACK 수신 시점과 Due Date 비교 결과 표시. 이전 또는 동일 → On-Time, 초과 → Late | 시스템 자동 |
| F-12 | 오류 대응 — 단순 재전송 (A) | 타임아웃 오류 시 배치 재생성 없이 기존 배치 즉시 재전송 | 사용자 실행 |
| F-14 | 오류 대응 — Lock 해제·수정 흐름 (B) | ICSR 오류(CR) 수신 시 Lock 해제. CR 상세 사유: 필수값 누락(R), 조건부 필수(P), 코드 오류(C), nullFlavor(N) → 케이스 모두 Submission 상태 ‘Drafting’으로 변경, 이후 사용자가 ICSR Processing Workflow 단계 재진행 필요 | 시스템 자동/사용자 실행 |
| F-15 | 보고 이력·파일 영구 보관 | 전송 파일(XML) + ACK 파일 계약 종료까지 보관. 변조·삭제 불가 | 시스템 자동 |

## 7. 제안 구조 (IA)

Safety

└── Submission

    ├── Submission List          ← 보고 대상 케이스 선정

    ├── Submission Monitoring     ← 배치 전송 상태 추적

## 8. 엣지케이스 및 예외 처리

| **#** | **케이스** | **발생 조건** | **처리 방식** |
| --- | --- | --- | --- |
| EC-01 | 중복 배치 생성 시도 | 이미 "전송 중"인 케이스를 다시 선택하여 배치 생성 요청 | 시스템 차단. 에러 메시지 표시 -> 전송 중인 것은 취합시 미노출 필요 -> 누군가 동시작업으로 동시에 선택할 수 있어서 처단 필요? |

## 9. 추후 고도화

* 수동 보고 처리

  [IS-1680](https://selta.atlassian.net/browse/IS-1680?src=confmacro)

  + 추후 고도화 시점에서 다시 논의 예정, 현재는 Workflow 단계 ‘Approval’이면서 해당 상태가 ‘Approved’ 이고 RA 값이 없는 것을 보고하는 것이 목적

    - 보고시 Verified → Ready to Submit으로의 승인이 없는데 보고 진행할 경우: 승인 안했는데 보고 진행할건지 확인+왜 진행하는지 사유 작성 = audit에 필요
* 엣지 케이스 고려

  + Receiver 설정이 안된 케이스가 보고를 할 수 있는 상태 올라왔을때 처리

    - 자동취합에서는 이슈가 없을 수 있으나 수동으로 보고 처리 시에는 고려 필요
  + 전송 후 일정 시간 내 ACK 미수신 시 처리 방법

    - 현재 48시간으로 단순히 정했으나 주말이나 일요일 껴 있는 경우 이슈 있음.
    - 수동 처리나 근무일 고려 등 필요
* 오류 대응: 신규 배치 생성

  + Batch 오류(AE/AR) 시 신규 배치 생성. 기존 케이스 데이터 미변경: 고도화에서 진행 (

    [IS-1679](https://selta.atlassian.net/browse/IS-1679?src=confmacro)
    )
