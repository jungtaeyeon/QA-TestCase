|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 이름 | 날짜 | 변경 사항 | 제품 버전 | 기획 버전 |
| 김나정 | 26.03.31 | 삭제 로직 수정 | v1.0 | v1.0.260331 |
| 김나정 | 26.03.11 | 최초 작성 | v1.0 | v1.0.260319 |

# 입력 필드

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 카테고리 | 반복필드 | 필드 영문명 | 필드 국문명 | 필수 여부 | R3값 매핑 | 비고 | Validation |
| Study Identification |  | Project ID | 프로젝트 ID | 필수 | N/A | Project에서 입력한 값 가져옴. Read Only | - |
|  | Sponsor Study Number | 시험/연구 계획서 번호 | 필수 | C.5.3 | 국가별 승인번호는 여러개 생길 수 있기 때문에 여기는 1개만 있는 관리번호여야 함. | R3 검증 룰을 따름 |
|  | Study Name | 시험/연구 계획서 제목 | 필수 | C.5.2 | 1. `+ Add Title` 클릭 시 새로운 과제명 입력 행 생성 2. 좌측 드롭다운에서 국가 선택 후 우측에 과제명 입력 3. 다국가 임상의 경우 보고서 국가에 맞는 언어 명칭이 자동으로 리포트(C.5.2)에 기재됨 (국가는 Regional 과 묶여서 Report에 기재) | R3 검증 룰을 따름 |
|  | Study Acronym | 연구 이름 (약어) | 옵션 | N/A | Blind용 명칭 생성시, CASE ID 부여, 누적된 데이터 분석하여 Dashboard등 생성 등에서 필요 | 최대 50자 |
| Study Details |  | Study Type | 연구 구분 | 필수 | C.5.4 | 동일한 방식으로 할지 고려 필요 (Arugs의 경우, 1개의 필드로 되어 있음) regional(KR) 관련 세부 설정 필드 필요할지도 -> 우선 MFDS 필드에 맞춰서 3개. 추후 Regional Rule에 따라 바뀔 가능성 있음 | 현재는 MFDS R3 검증 룰을 따름 |
|  |  | Non-Interventional Study | 비중재적 연구 여부 | 옵션 | N/A | 보고에는 필요 X | 최대 20자 |
|  | 묶어서 반복필드 | Target Disease Indication | 주요 적응증 | 옵션 | G.k.7.r.1 | MedDRA coding필요함.  반복 입력 가능해야 함.  나중에 Sync에서 쓸 일이 있을 것 같아서 미리 공유해 두면 좋을 것 같음. 그리고 임상 입력시에도 편할거 같음. IP의 적응증으로 자동 입력시 편할 것같음. 임상은 보고자가 보고한 적응증이라도 다 똑같음. | R3 검증 룰을 따름 |
|  | MedDRA version for indication | 적응증의 MedDRA 버전 | 옵션 | G.k.7.r.2a | MedDRA 코딩 팝업을 사용해 MedDRA 코딩  MedDRA 라이센스 연결되어 있지 않을 경우 자유 기재. 버전은 드롭다운  선택한 메드라 코드와 term이 해당 필드에 자동입력 | 최대 5글자 |
|  | MedDRA term- Korean | MedDRA term- 한국어 | 옵션 | N/A | 제한 없음 |
|  | MedDRA term- English | MedDRA term- 영어 | 옵션 | N/A | 제한 없음 |
|  | MedDRA code | 적응증의 MedDRA 코드 | 옵션 | G.k.7.r.2b | 최대 15글자 |
| Study Registration | 묶어서 반복필드 | Study Registration Country | 시험/연구 등록 국가 | 필수 | C.5.1.r.2 |  | R3 검증 룰을 따름 |
| Reference Type | 임상 참조 번호 유형 | 옵션 | N/A | (정보성) 임상시험 승인된 번호 종류 아래 예 참고  FDA IND Number US (미국) 의약품 임상시험 승인 번호  IDE Number US (미국) 의료기기(Device) 임상시험용 승인 번호  jRCT Number JP (일본) 일본 임상시험 정보 시스템 등록 번호  NCT Number Global (<http://ClinicalTrials.gov> ) 미국 및 글로벌 공용 임상 등록 번호  NMPA IND Number CN (중국) 중국 약감국 승인 번호  WHO/UTN Number Global (WHO) 세계보건기구 부여 고유 식별 번호  MFDS (KCT) KR (한국) 한국 식약처(CRIS) 등록 번호  EudraCT number (유럽) 임상시험 승인 번호  언젠가 고도화: 식약처의 경우, 아래 2군데서 검증을 함.  일련번호=2.16.840.1.113883.3.989.2.1.3.5  계획서번호=2.16.840.1.113883.3.989.5.1.10.2.5 | - |
| Study Registration Number | 시험/연구 등록 번호 | 필수 | C.5.1.r.1 | Reference Type에 묶임 | R3 검증 룰을 따름 |
| Message Receiver Identifier | ICSR 수신자 ID | 필수 | N.2.r.3 |  | R3 검증 룰을 따름 |
| Other Studies Type | 기타 시험 상세구분 | 선택적 필수 | C.5.4.KR.1 | 등록 국가를 KR로 선택할 경우 표시 | R3 검증 룰을 따름 |
| Blind |  | Study is eligible for Unblinding (체크박스) | 시험 맹검 해제 허용 여부 | 필수 | N/A |  | - |
| Study Status |  | Study Status | 임상 상태 | 필수 | N/A | ongoing/close 두가지 선택지로 선택  close 선택 시 blind 일괄 해지 | - |

# Study 추가, 저장, 삭제

* [+add study] 클릭 시 project 하위에 study 추가 가능
* [save] 클릭 시 기재된 정보 저장
* [delete] 하위에 해당 프로젝트에 소속된 Study Design이 있을 경우 삭제 불가

  + 소속 하위 데이터 존재할 때 버튼 클릭 시 Project에 Study Design이 존재하면 삭제가 불가능합니다. 포함된 Study Design을 모두 삭제한 후 다시 시도해 주세요." 문구 표시 (Confirm 버튼만)

# Study Registration

* 케이스(Case) 생성 시, 본 단계에서 설정한 값이 보고서의 '연구 정보' 섹션에 자동으로 바인딩되는 핵심 로직
* Reporting Source of Truth: 케이스에서 리포트 생성 시, 시스템은 해당 케이스에 연동된 Study의 Registration 필드 값을 우선적으로 참조
* 데이터 매핑:

  + Study Registration Country: E2B(R3) 필드 C.5.1.r.2로 매핑되어 보고 국가를 확정
  + Study Registration Number: E2B(R3) 필드 C.5.1.r.1로 매핑되어 승인 번호를 출력
  + Message Receiver Identifier: E2B(R3) 필드 N.2.r.3로 매핑되어 보고서 송신 대상을 특정

# 와이어프레임

![](https://t37003623.p.clickup-attachments.com/t37003623/5fdcec25-c523-4141-86c9-5cf0f560f0d5/image.png)

|  |  |  |
| --- | --- | --- |
| # | 기능 설명 | 액션 |
| 1 | 1. 이미 설정한 Project ID가 그대로 반영 2. Read only | - |
| 2 | 1. ICSR 보고용 연구 유형(C.5.4)을 정의 2. 케이스에 불러오기 할 경우 C.5.4에 매핑 | 1. 클릭 시 드롭다운으로 선택지 표시 2. 1=Clinical trials 임상시험 3. 2=Individual patient use(e.g. 'compassionate use' or 'named patient basis') 개별 환자 사용(예: 치료목적 사용승인) 4. 3=Other studies (e.g. pharmacoepidemiology, pharmacoeconomics, intensive monitoring) 기타 시험(예: 약물역학, 약물경제학, 집중 모니터링) 5. 선택지 클릭하면 값 입력. |
| 3 | 해당 연구의 개입/비개입 여부를 설정 | 1. 클릭 시 드롭다운으로 선택지 표시 2. Yes 3. No |
| 4 | 연구 대상이 되는 질환을 MedDRA 표준 코드로 관리 | 1. `+ Add Indication` 클릭 시 새로운 입력 행이 하단에 생성 2. Target Disease Indication 필드에는 free text 입력 3. MedDRA veirsion, MedDRA Term (Koreanm, English), MEdDRA Code는 MedDRA 라이센스 연결되어 있을 경우 팝업을 통해 입력 4. MedDRA라이센스 연결되어 있지 않을 경우 자유 기재로 입력. 버전은 드롭다운으로 입력 |
| 5 | IND, NCT 등 등록 번호의 종류를 정의 | 1. 클릭 시 드롭다운하여 선택지 표시 2. DA IND Number US (미국) 의약품 임상시험 승인 번호 3. IDE Number US (미국) 의료기기(Device) 임상시험용 승인 번호 4. jRCT Number JP (일본) 일본 임상시험 정보 시스템 등록 번호 5. NCT Number Global ([ClinicalTrials.gov](http://clinicaltrials.gov/)) 미국 및 글로벌 공용 임상 등록 번호 6. NMPA IND Number CN (중국) 중국 약감국 승인 번호 7. WHO/UTN Number Global (WHO) 세계보건기구 부여 고유 식별 번호 8. MFDS (KCT) KR (한국) 한국 식약처(CRIS) 등록 번호 9. EudraCT number (유럽) 임상시험 승인 번호 10. 기타 11. 기타 선택 시 free text필드가 옆에 표시. 자유기재 |
| 6 | 임상 라이센스를 얻은 국가 선택 및 관련 정보 입력 | 1. 6클릭 시 드롭다운으로 국가 선택 가능 2. 선택한 국가가 표시 3. 6에서 KR 선택 시 6-1표시 4. 6-1 클릭 시 드롭다운 표시 (영어와 병기) 5. 1=재심사 보고 사용성적조사 6. 2=재심사 보고 시판 후 임상연구 7. 3=재심사 보고 특별조사 8. 4=기타 |
| 7 | 1. 임상 시험 진행 여부 관리 2. 디폴트=ongoing | 1. ongoing 선택 시 2. 해당 임상이 ongoing 상태로 변환 3. close 선택 시 4. close 선택시 얼럿 메시지: "Study를 종료하면 새로운 Case를 생성할 수 없습니다." 5. Confirm 클릭 시 해당 임상 하위의 맹검 오픈 가능상태로 전환 6. Cancel 클릭 시 ongoing 상태로 유지 7. 해당 임상을 close 상태로 변환 8. blinded 처리되었던 arm에 속한 Product 오픈 가능 상태 (케이스에서) 9. Case Intake&Triage에서 과제 정보 불러올 수 없도록 조치 (리스트에 보이지 않음) 10. Unblind필드(R3 필드x)에 Open 옵션 선택 가능하도록 변경 |

# 참고

신경쓰지 말아주세요. 추후 넣을 필드 및 공부용..

![](https://t37003623.p.clickup-attachments.com/t37003623/8c2d8da6-e5fa-4e44-9bf1-34c4fbb2dc37/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202026-03-18%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%207.23.58.png)![](https://t37003623.p.clickup-attachments.com/t37003623/8d1459f2-60c4-4477-a5ab-21911e6d44d1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202026-03-18%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%207.24.11.png)![](https://t37003623.p.clickup-attachments.com/t37003623/a343bde9-818a-4065-b34f-001887bdec03/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202026-03-18%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%207.24.19.png)
