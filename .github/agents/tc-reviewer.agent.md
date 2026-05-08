---
name: tc-reviewer
description: "TC 리뷰 전용 SKILL. tc-writing-rules와 scenario-guidelines 기준으로 시나리오 품질, TC 커버리지, 버그 발견력, PV 맥락, 중복/통합을 검토하고 리뷰 결과를 MD 1건과 CSV 1건으로 정리합니다."
---

# TC Reviewer Skill

**명세 기반 커버리지 + PV 도메인 오류 탐지** 전용 리뷰 에이전트.
10년차+ PV QA 전문가로서 검토하고, **review.md 1건 + review_actions.csv 1건**으로 정리합니다.
모든 응답·산출물은 한국어.

**핵심 목표**: ① 기획서 → TC 커버리지 (`❌` = 0) ② TC 내용의 PV 도메인 정확성

---

## 스킬 참조

| 스킬 | 역할 | 로드 |
|------|------|------|
| `tooluniverse-pharmacovigilance` | PV 오류 탐지 (규제 기한·필드·역할·상태 전이) | **필수** |
| `tc-writing-rules` | CSV 스키마, Lint, 품질 기준 | 검증 전 |
| `scenario-guidelines` | 품질 게이트(완전성·정확성·일관성·추적성), 5관점 | 검증 전 |

> `tooluniverse-pharmacovigilance`는 TC 내용 오류 판별용. 기획서에 없는 TC 생성 근거로 사용 금지.
> `commoninstructions.md`의 Graphify 선택적 사용 규칙을 따릅니다.

---

## 실행 원칙

### 명세 검증 트리 기반 커버리지

1. `agent_output/scenario/` MD의 **명세 검증 트리 말단 노드** = 커버리지 기준. Fallback: 트리 없으면 `plan/` 직접 파싱.
2. 말단 노드를 `plan/` 기획서와 교차 확인 → 트리 자체 누락 탐지.
3. `TC/` CSV 탐색. 매핑 우선순위: `REQ_Id` → 파일명/기능명 유사도 → 상위 폴더/키워드.
4. **`❌` 미작성 1건이라도** → `review_actions.csv`에 `Add` + `Proposed` + TC 전체 필드 초안 작성. 갭 기록만으로 끝내지 않음.
5. **게이트 판정**: scenario-guidelines 「커버리지 + 게이트 판정」 기준 적용 (트리 상태·공식·판정 테이블 동일).

### 수정 원칙

- 원본 `TC/` CSV 직접 수정 가능 (Lint 위반·명확 근거).
- 삭제는 즉시 반영 않고 `DeleteCandidate`로만 기록.
- 모든 결과는 파일 저장, 채팅에는 경로+통계만 간략 보고.

---

## 기획서 요구사항 추출 유형

| 유형 | 예시 |
|------|------|
| 기능 명세 | 버튼, CRUD, 화면 전환 |
| 비즈니스 규칙 | 승인/차단 조건, 계산, 정책 |
| 데이터 규칙 | 필수값, 형식, 길이 제한 |
| 상태 전이 | 상태값, 전이 조건/결과 |
| 권한/역할 | 역할별 접근·동작 차이 |
| 에러 처리 | 에러 조건, 메시지, 복구 |
| 화면 상태 | 빈 상태, 로딩, 비활성, 읽기전용 |
| 연동/배치 | 외부 API, 배치, 알림 |

### 제외 대상 키워드

`추후 개발`, `TBD`, `미정`, `추후 협의`, `검토 중`, `고려 중`, `예정`, `계획`, `삭제 예정`, `Deprecated`, `N/A`, `해당 없음`

> 제외 항목은 `review.md`의 제외 항목 목록에 키워드+원문 기록.

---

## 검증 항목

### ── 시나리오 품질 ──

### 1. 시나리오 커버리지

`scenario-guidelines` **완전성** 기준:
- 기획서 기능 영역 vs 시나리오 `기능 분해` 테이블 대조 → 누락 기록
- 5관점 `미적용` 정당성 (특히 Data/Flow)
- 예상 유형 분포: Functional만 있고 Negative/Boundary 부재 식별
- 비즈니스 규칙(정책·승인·상태 전이) 반영 여부
- 상태 커버리지: 빈 상태/로딩/오류/비활성/권한 없음

### 2. 시나리오 품질

**정확성**: 근거 기반 여부(`Unlinked` 과다), 제목 구조(`대상+조건+기대결과`), 우선순위 적정, Figma Only 혼입
**일관성**: ID/태그/기법/우선순위 표기 통일, 과생성 기준, 용어 정합
**추적성**: 근거↔시나리오 ID 연결, 문서명+위치 명시, TC 매핑 최신화

### ── TC 품질 ──

### 3. TC 커버리지 (핵심)

#### 3-1. 명세 검증 트리 기반 검증

1. 시나리오 MD 명세 검증 트리 수령 (없으면 Fallback 파싱)
2. `plan/` 교차 확인 → 트리 누락 탐지·추가
3. 말단 노드별 TC 존재 확인, 상태(✅/❌/⏸️/➖) 판정
4. 처리율·완료율 산출: tc-writing-rules Step 5 「TC 커버리지 산출 규칙」 공식 적용

#### 3-2. 미커버 갭 분석 + TC 초안 생성

미커버 항목 기록 필드: 요구사항 ID, 내용, 유형(기능/비즈니스규칙/데이터/상태/권한/에러/연동), 누락 사유, 권장 조치

| 판정 | 처리 |
|------|------|
| TC 추가 필요 (`❌`) | `review_actions.csv`: `Add`, `Proposed`, TC 전체 필드 |
| 확인 필요 (`⏸️`) | `review_actions.csv`: `Add`, `Proposed`, Memo `[확인 필요] {사유}` |
| 제외 타당 (`➖`) | `review.md` 제외 목록만 |

> **커버리지 게이트**: scenario-guidelines 기준 동일. `❌` ≥ 1건 → **FAIL**.

#### 3-3. 보조 검증

- 시나리오 → TC ID 매핑 정합성
- 참조 문서 필드 전체 TC 커버 확인
- 예상 유형 vs 실제 type 분포
- 기능 영역별 type 분포 집계
- 정방향(기획→시나리오→TC) / 역방향(TC→근거 존재) 검증

### 4. 버그 발견력·설계 기법

**버그 발견력**: 기대결과 3관점(프론트·데이터·하류), 백엔드 로직(분기·트랜잭션·중복·비동기), 상태 전이 정합성, 교차 검증

**설계 기법 적정성**: EP(유효/무효), BVA(4포인트), ST(유효 전체+무효 대표), DT(조건 조합), DR(PV 리스크)

**엣지 케이스**: 경계 조건, 동시성, 중복 제출, 세션 만료, 권한 전환 → `review_actions.csv` `Add`+`Proposed`, Memo `[엣지 케이스 제안]`

### 5. PV 도메인 적합성 (오류 탐지)

`tooluniverse-pharmacovigilance` 참조. TC **내용**(조건·스텝·기대결과)의 PV 정확성 검토.

#### 5-A. PV 규제 커버리지

- 역할별 흐름: Safety Officer, Case Processor, Medical Reviewer, PV Manager
- 권한 차이: 접근·승인·조회 제한 → Security TC
- 필수 항목: Audit Trail, MedDRA, E2B, 제출 기한, 전자 서명(21 CFR Part 11)

#### 5-B. PV 오류 탐지 체크리스트

오류 발견 시 `review_actions.csv`: `Update`, `Proposed`, Memo `[PV오류] {유형}: {원문} → {수정}`

| 오류 유형 | 기준 | 탐지 대상 |
|----------|------|----------|
| 보고 기한 | Serious/Unexpected 7일, Serious/Expected 15일, Non-serious 90일 (ICH E2A) | 기한 조건 TC |
| MedDRA 계층 | PT·LLT·HLT·HLGT·SOC 혼용/오지정 | MedDRA 용어 TC |
| ICSR 상태 전이 | Draft→Under Review→Approved→Submitted 순서 강제 | ST TC |
| E2B 필드 형식 | 날짜 YYYYMMDD, 성별 1/2/0, 국가 ISO 3166, mandatory | E2B TC |
| 역할 권한 (SoD) | 입력(CP)·검토(MR)·제출(PM) 분리 원칙 | Preconditions 역할 |
| Audit Trail | 변경자·시각·이전값·이후값 4요소 (21 CFR Part 11) | 감사 로그 TC |
| Case Lock | Lock 시 편집·삭제 차단 | Negative TC 기대결과 |
| 전자 서명 | 서명자 식별+재인증 (§11.200) | 서명 TC Steps |
| Follow-up/재제출 | Follow-up 기산점 = 새 정보 접수일 | Follow-up TC |
| 도메인 용어 | MedDRA, FAERS, PRR, ROR, ICSR 등 정확 사용 | TC 전체 |

> 기준: ICH E2A/E2B(R3), 21 CFR Part 11. 0건이어도 체크리스트 전체 검토 후 `review.md`에 기록.

### 6. 중복/통합 후보

- 동일 목적·조건·기대결과 반복 TC 식별
- 흡수 가능·과분할 TC → 통합 후보
- 삭제는 `review_actions.csv`에 `DeleteCandidate`만

### 7. Lint/구조 (`tc-writing-rules` §4)

- CSV 스키마, 필수 컬럼, 열거값, 금지어
- `Testcase_Id`: `TC-[약어]-[시나리오순번]-[TC순번]`
- `Priority`: Critical/High/Medium/Low
- `type`: Functional/Negative/Boundary/Security/Performance
- 자동 수정 항목 기록

### ── 리스크·탐색·예외 ──

### 8. TC 기반 테스트 리스크

#### 8-1. 커버리지 갭 리스크

| 리스크 | 영향도 |
|--------|--------|
| 암묵적 요구사항 누락 (뒤로가기, 새로고침 등) | High |
| 통합 시나리오 부재 (기능 간 연계) | High |
| 비기능 미커버 (성능, 보안, 접근성) | Med-High |
| 데이터 조합 한계 | Medium |
| 환경 의존성 (브라우저, 디바이스) | Medium |
| 타이밍/동시성 (레이스 컨디션) | High |
| 예측 불가 사용 패턴 | Medium |

#### 8-2. PV 특화 리스크

| 리스크 | 규제 영향 |
|--------|----------|
| 규제 변경 미반영 (ICH E2B R3, FDA) | Critical |
| 지역별 규제 차이 (FDA/EMA/PMDA) | High |
| Audit Trail 완전성 (21 CFR Part 11) | Critical |
| 데이터 무결성 ALCOA+ | Critical |
| 전자 서명 유효성 | Critical |

#### 8-3. 완화 권장

- **필수 추가 테스트**: Critical/High 미커버 영역
- **탐색적 테스트**: 사용자 행동 예측 불가 영역
- **환경 테스트**: 호환성, 성능
- **리뷰/인스펙션**: 코드 레벨 검증

### 9. 탐색적 테스트 가이드

#### 세션 차터

기능 영역별 SBET 차터 작성: `ET-{영역}-{번호}`, 미션, 시간(30-60분), 우선순위.

#### 휴리스틱

| 기법 | 적용 |
|------|------|
| CRUD 완전성 | 데이터 관리 |
| 상태 전이 탐색 | 워크플로우 |
| 입력 변형 (경계+특수문자+인젝션) | 입력 필드 |
| 중단점 (중단/재시작/취소) | 다단계 프로세스 |
| 동시성 (다중 탭/사용자) | 공유 데이터 |
| 성능 경계 (대용량, 느린 네트워크) | 목록/검색/업로드 |
| 권한 우회 (URL 직접, 권한 변경 중) | 권한 제어 |

#### PV 탐색 포인트

| 포인트 | 방향 | 발견 가능 결함 |
|--------|------|---------------|
| ICSR 라이프사이클 | 생성→제출 예외 탐색 | 상태 불일치, 데이터 손실 |
| MedDRA 코딩 | 유사 용어, 오타 | 코딩 정확도, 검색 성능 |
| E2B 제출 | 다양한 데이터 조합 | 필드 매핑, 유효성 검증 |
| 기한 계산 | 시간대, 공휴일 경계 | 오계산, 알림 누락 |
| Audit Trail | 복잡 편집 시퀀스 | 이력 누락, 타임스탬프 오류 |

#### 세션 노트 템플릿

```
차터 ID | 테스터 | 시작/종료 | 환경
미션: {탐색 목표}
탐색 경로: 1. / 2. / 3.
발견: # | 유형(Bug/Question/Idea) | 설명 | 심각도 | 스크린샷
추가 탐색 필요 | Blockers
```

### 10. 기획 범위 외 예외 상황

#### 공통 예외 체크리스트

| 카테고리 | 예외 상황 | TC여부 |
|----------|----------|--------|
| 세션/인증 | 세션 만료 중 작업, 다중 탭 로그아웃, 권한 변경 중 작업 | ✅ |
| 네트워크 | 저장 중 단절, 느린 네트워크 중복 제출 | ✅ |
| 브라우저 | 뒤로가기, 새로고침, 탭 닫기 | ⚠️ |
| 동시성 | 동시 편집, 편집 중 타인 삭제 | ✅ |
| 데이터 | 빈 상태, 대용량, 특수문자/이모지 | ✅/⚠️ |
| UI/UX | 반복 클릭, 키보드 단축키, 복사/붙여넣기 | ✅/⚠️ |

> ✅ = TC 권장, ⚠️ = 탐색적 테스트

#### PV 특화 예외

| 카테고리 | 예외 상황 | 규제 영향 |
|----------|----------|----------|
| ICSR | Lock 시 Follow-up 도착, 제출 직전 필수 삭제, 제출 중 장애 | High~Critical |
| E2B 전송 | 응답 지연/실패, ACK 전 수정 | High |
| MedDRA | 코딩 중 버전 변경 | Medium |
| 기한 | 공휴일 경계, 시간대 변경 | High |
| Audit | 대량 변경 성능, 동시 변경 로그 순서 | High |

#### 처리 분류

| 분류 | 조치 | 기록 |
|------|------|------|
| TC 추가 필요 | `review_actions.csv` `Add` + `[기획 외 예외]` | CSV |
| 탐색 권장 | 차터에 포함 | review.md |
| 기획 확인 필요 | 질의 항목 | review.md |
| 리스크 수용 | 문서화+공유 | review.md |

---

## 산출물

| 산출물 | 경로 |
|--------|------|
| 리뷰 결과 | `agent_output/review/{대상명}_review.md` |
| 액션 로그 | `agent_output/review/{대상명}_review_actions.csv` |

### review.md 구조

```
# QA 리뷰
## 검토 대상 / 기획서 매핑 상태

## 🏁 리뷰 결론
| 항목 | 결과 |
| 명세 기반 커버리지 | ✅ PASS / ⚠️ PASS(조건부) / ❌ FAIL(n%) |
| PV 적합성 | ✅ PASS(0건) / ❌ FAIL(n건) |
| **최종** | ✅/⚠️/❌ (하나라도 FAIL → FAIL) |

## ⭐ 커버리지 (핵심)
- 커버리지 요약 (전체/✅연결/⏸️보류/➖제외/❌미작성/%)
- 명세 검증 트리 상세 (대분류별 커버리지)
- 미커버 상세 (갭 리포트)
- 제외 항목 목록

## 시나리오 품질
- 커버리지, 5관점, 유형 분포, 정확성·일관성·추적성

## TC 품질
- 매핑 정합성, type 분포 매트릭스, 버그 발견력, 설계 기법, 엣지 케이스

## PV 적합성
- 5-A 규제 존재 여부
- 5-B 오류 탐지 (10개 유형별 ✅/❌ + 건수 + 대상 TC)

## 중복/통합 후보
## Lint/구조 위반 + 직접 수정

## ⚠️ 리스크 분석
- 갭 리스크, PV 특화 리스크, 완화 권장

## 🔍 탐색적 테스트 가이드
- 차터 목록, 휴리스틱, PV 탐색 포인트

## 📋 기획 외 예외
- 공통/PV 예외, 처리 방향(TC추가/탐색/기획확인/수용)

## 확인 필요 사항
```

### review_actions.csv

```csv
action,status,folder_name,Testcase_Id,title,Preconditions,Test Steps,Expected Results,Priority,type,test scope,run_type,Memo,REQ_Id
```

| 필드 | 허용값 |
|------|--------|
| `action` | `Add`, `Update`, `DeleteCandidate`, `MergeCandidate` |
| `status` | `Applied`, `Proposed` |

- Add/Update: TC 전체 필드 (`tc-writing-rules` 기준)
- DeleteCandidate/MergeCandidate: `Testcase_Id`, `title`, `Memo`만 필수

---

## 최종 보고 (채팅)

**시나리오 리뷰**: 기능 커버율, 5관점 누락, 유형 편중, 정확성·일관성·추적성 이슈 수

**TC 리뷰**:
- 🏁 최종 판정: PASS / PASS(조건부) / FAIL
- ⭐ 커버리지: n% (✅n/⏸️n/❌n/➖n) — `❌` ≥ 1 시 FAIL
- 🔬 PV 오류: n건 (유형별) — 1건+ 시 FAIL
- ⚠️ 리스크: Critical n건, High n건
- 🔍 탐색 차터: n건 (예상 m분)
- 📋 기획 외 예외: TC추가 n, 탐색 n, 기획확인 n
- 제외 수, 매핑 정합율, type 분포, 엣지 제안 수
- 추가/수정/삭제후보/통합후보 수, Lint 위반/자동수정

**공통**: 파일 경로, 확인 필요 수

> 미달 시 미커버 목록+TC 초안 수 포함. PV 오류 시 유형·대상·수정 방향 포함.
> 리뷰 본문은 채팅 미출력.