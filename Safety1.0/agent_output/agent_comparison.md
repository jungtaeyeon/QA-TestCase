# 에이전트 비교: 구버전 vs 신규 파이프라인 (01~07)

> 작성일: 2026-05-07  
> 목적: 기존 단일 에이전트 방식과 새로 구축한 7-step 파이프라인의 차이를 구조·방법론·산출물 측면에서 비교

---

## 1. 에이전트 구성 변화 (한눈에 보기)

| 역할 | 구버전 에이전트 | 신규 에이전트 |
|------|--------------|-------------|
| 기획서 분석 | `plan-translator` | `01-plan-analyst` |
| 디자인 검증 | `design-qa` | `02-design-validator` |
| 시나리오 생성 | `tc-generator` (기능 1) | `03-scenario-writer` |
| TC 작성 | `tc-generator` (기능 2) | `04-tc-writer` |
| TC 리뷰 | `tc-reviewer` | `05-tc-reviewer` |
| 업로드 | `tc-generator` (기능 4) | `06-tc-uploader` |
| AI 결과 검증 | 없음 | `07-qa-guardian` (신규) |

**핵심 변화**: `tc-generator` 1개가 시나리오·TC·Figma·업로드를 모두 담당하던 구조 → 각 역할이 독립 에이전트로 분리됨.

---

## 2. 파이프라인 구조 차이

### 구버전 — 에이전트 간 상태 공유 없음

```
[사용자 요청]
    ↓
plan-translator → HTML (단일 산출물)
    ↓ (별도 실행)
tc-generator → 시나리오 + TC + 업로드 (에이전트 내부 순차 처리)
    ↓ (별도 실행)
tc-reviewer → review.md + review_actions.csv
```

- 에이전트 간 **공유 상태 파일 없음** — 각 에이전트가 기획서를 독립적으로 읽음
- 앞 에이전트의 산출물을 다음 에이전트가 참조하는 규약이 없음
- FAIL 시 재작업 루프 없음 (tc-reviewer가 갭을 기록해도 자동 연결 안 됨)

### 신규 파이프라인 — RTM을 중심으로 상태 연결

```
[기획서 입력]
      ↓
01 plan-analyst ──── RTM v0 ──→ ⏸ 사용자 확인
      ↓
02 design-validator ─ RTM v1 → ⏸ 사용자 확인  (선택)
      ↓
03 scenario-writer ── RTM v2 → ⏸ 사용자 확인
      ↓
04 tc-writer ───────── RTM v3 → ⏸ 사용자 확인
      ↓
05 tc-reviewer ──────── RTM v4
      ├── FAIL → 04 tc-writer 재작업 루프
      └── PASS → 06 tc-uploader
```

- RTM(v0→v4)이 파이프라인 전체의 **공유 상태 파일** 역할
- 각 에이전트는 선행 RTM 버전 존재 여부를 실행 전 체크
- FAIL 시 `review_actions.csv`를 통한 **자동 재작업 루프** 구축

---

## 3. 기획서 분석 에이전트 비교: plan-translator vs 01-plan-analyst

### 3-1. 분석 방법론

| 항목 | plan-translator | 01-plan-analyst |
|------|----------------|----------------|
| 분석 방식 | 유저 스토리 + 시나리오 기반 서술 | **9차원 매트릭스** × 엔티티 전수 순회 |
| 엔티티 추출 | 없음 (섹션 기반 서술) | Step 1에서 타입별 엔티티 목록 명시적 추출 |
| 이슈 분류 | 없음 | 충돌/표현불일치/누락/확인필요 4종 |
| 이슈 에스컬레이션 | 없음 | **Tier 1/2/3** — 기획자 전달 대상 자동 필터링 |
| 자기검증 | 없음 | **Step 5 검증 체크리스트** (매트릭스 빈칸, 커버리지, 분류 정합성 등 5항목) |
| 와이어프레임 | 참조 허용 | **완전 금지** (기획서 텍스트 본문만 분석 소스) |

#### 9차원 매트릭스 (01-plan-analyst 신규)

| # | 차원 | 검사 질문 |
|---|------|---------|
| ① | 정의 완전성 | 값·동작이 완전히 정의되어 있는가? |
| ② | 조건 명확성 | 조건·분기가 모호하지 않은가? |
| ③ | 에러 처리 | 실패 시 동작·메시지가 정의되어 있는가? |
| ④ | 권한 분기 | 역할별 접근·동작 차이가 정의되어 있는가? |
| ⑤ | 상태 전이 | 전이 조건과 결과 상태가 명확한가? |
| ⑥ | 교차 일관성 | 다른 문서/섹션과 동일한가? |
| ⑦ | 데이터 형식/범위 | 타입, 길이, 허용값, 기본값이 정의되어 있는가? |
| ⑧ | UI 피드백 | 각 상태에서 사용자에게 무엇이 보이는가? |
| ⑨ | 도메인 규제 | PV 규정과 충돌하지 않는가? |

→ **엔티티 타입에 따라 MUST/IF-APPLICABLE 차원이 구분됨** — 무작위 검사가 아닌 구조적 순회

### 3-2. 산출물 비교

| 산출물 | plan-translator | 01-plan-analyst |
|--------|----------------|----------------|
| QA 분석 HTML | `{기능명}-QA분석.html` (1종) | `{기능명}-QA확인용.html` (1종) |
| 기획자 전달 문서 | 없음 | `{기능명}-기획자확인요청.md` (Tier-1 이슈만) |
| RTM | `{기획서명}_RTM.md` (v0) | `{기획서명}_RTM.md` (v0, 이슈 Tier 포함) |

### 3-3. HTML 레이아웃 구조

| 항목 | plan-translator | 01-plan-analyst |
|------|----------------|----------------|
| 레이아웃 | **3-panel** (좌 사이드바 + 중앙 QA 분석 + 우 원문 패널) | **2-panel** (좌 사이드바 + 메인 콘텐츠) |
| 우측 패널 | 기획서 원문 + ref 배지 연결 | 없음 |
| 주요 컨텐츠 구조 | 테스트 목표, 유저 스토리, 엣지 케이스, 검증 포인트 매트릭스 | 이슈 카운트 카드, 기획 충돌/누락/확인 항목, QA 테스트 포인트, RTM 미리보기 |
| Auto-glossary | 있음 (PV 용어 툴팁) | 없음 |
| ref 배지 | 있음 (원문-분석 교차 클릭) | 없음 |
| 템플릿 파일 | 없음 (inline 생성) | `.github/templates/plan-analyst/` 참조 |

**요약**: plan-translator는 QA가 즉시 읽으며 원문을 교차 참조하는 **"분석 뷰어"** 중심, plan-analyst는 이슈 분류·에스컬레이션에 초점을 둔 **"품질 게이트 도구"** 중심

---

## 4. 디자인 검증 비교: design-qa vs 02-design-validator

| 항목 | design-qa | 02-design-validator |
|------|-----------|-------------------|
| 파이프라인 통합 | 독립 실행 (RTM 연결 없음) | RTM v1 생성 → scenario-writer에 전달 |
| 이슈 분류 | 누락/불일치/명세미반영/디자인전용 4종 | 동일 분류 유지 |
| 산출물 | HTML 리포트 1종 | HTML 리포트 + **RTM v1** (디자인 이슈 태그 반영) |
| 선택 실행 | 항상 실행 가능 | ⏸ 건너뛰면 RTM v0 그대로 유지 |
| 후행 에이전트 영향 | 없음 | 03-scenario-writer가 RTM v1의 🔴/🟠 태그를 시나리오에 반영 |

---

## 5. 시나리오 생성 비교: tc-generator(기능1) vs 03-scenario-writer

| 항목 | tc-generator 기능 1 | 03-scenario-writer |
|------|--------------------|--------------------|
| 트리거 조건 | 키워드 라우팅 (`시나리오`, `scenario`) | RTM v0/v1 존재 확인 후 실행 |
| RTM 선행 확인 | 없음 | **필수** (RTM 없으면 단독 실행 모드로 전환) |
| 기획자 답변 파일 반영 | 없음 | RTM `확인 필요 사항` 해결 상태 반영 |
| 디자인 이슈 반영 | Figma URL 입력 시만 | RTM v1의 태그 자동 반영 |
| 산출물 | 시나리오 MD | 시나리오 MD + **RTM v2 갱신** |
| RTM REQ 매핑율 | 없음 | `### REQ 매핑율` 표 필수 포함 |

---

## 6. TC 작성 비교: tc-generator(기능2) vs 04-tc-writer

| 항목 | tc-generator 기능 2 | 04-tc-writer |
|------|--------------------|-----------| 
| 트리거 조건 | 키워드 라우팅 | RTM v2 존재 확인 후 실행 |
| RTM 선행 확인 | 없음 | **필수** (v1 이하이면 scenario-writer 먼저 안내) |
| TC 보류 처리 | 시나리오 미해결 항목 보류 | `확인 필요` 태그 → `[!확인필요!]` 동기화 + 보류 |
| Figma 처리 | 기능 3으로 직접 처리 | 06-tc-uploader에 위임 |
| 산출물 | TC CSV + 시나리오 MD 갱신 | TC CSV + **RTM v3 갱신** |
| 재작업 루프 | 없음 | tc-reviewer FAIL 시 `review_actions.csv` 수신 → 재반영 절차 정의 |

---

## 7. TC 리뷰 비교: tc-reviewer vs 05-tc-reviewer

| 항목 | tc-reviewer (구버전) | 05-tc-reviewer (신규) |
|------|--------------------|--------------------|
| 에이전트 성격 | 독립 실행 SKILL | **파이프라인 Step 05** |
| 선행 조건 | 없음 | RTM v3 존재 필수 |
| 검증 내용 | 동일 (10개 PV 오류 유형, 커버리지, Lint 등) | 구버전 검증 항목 **전부 + 추가 검증** |
| 추가 검증 항목 | - | TC 매핑 정합성 (ID 범위 대조), PV 태그 보증 검증 (`[!확인필요!]` 동기화 확인) |
| FAIL 처리 | 갭 기록만 (연결 없음) | **FAIL → tc-writer 재작업 루프** 자동 연결 |
| RTM 갱신 | 없음 | PASS 시 **RTM v4 생성** (`리뷰 PASS` 상태 반영) |
| PASS 판정 기준 | review.md 내 기록 | 명시적 PASS/FAIL 판정 → 파이프라인 분기 |

---

## 8. 신규 추가: 07-qa-guardian

구버전에 없던 에이전트. 어느 단계에서나 AI 결과물의 품질을 독립 검증하는 역할.

| 항목 | 내용 |
|------|------|
| 실행 시점 | 어느 단계에서나 호출 가능 |
| 역할 | 다른 에이전트 산출물(HTML, 시나리오, TC, RTM)의 품질을 독립적으로 검증 |
| 산출물 | `review/{기획서명}_guardian_report.md` |

---

## 9. RTM 도입 전/후 비교

| 관점 | 구버전 (RTM 없음) | 신규 (RTM v0~v4) |
|------|----------------|----------------|
| 요구사항 추적 | 기획서를 각 에이전트가 개별 파싱 | 전 에이전트가 공유 RTM 참조 |
| 이슈 이력 | 에이전트별 산출물에 분산 | RTM `확인 필요 사항` 섹션에 통합 기록 |
| 파이프라인 상태 | 알 수 없음 | RTM 첫 줄로 현재 단계 즉시 파악 |
| TC 커버리지 추적 | 개별 CSV로만 | RTM `REQ_Id ↔ TC ID 범위` 연결로 역추적 가능 |
| 기획자 답변 반영 | 수동 | 기획자확인요청.md → 답변 → RTM 업데이트 → 다음 에이전트 |

---

## 10. 전체 차이 요약

| 관점 | 구버전 | 신규 파이프라인 |
|------|--------|--------------|
| 에이전트 수 | 4개 (`plan-translator`, `design-qa`, `tc-generator`, `tc-reviewer`) | 7개 (01~07) |
| 핵심 아키텍처 | 독립 에이전트, 상태 공유 없음 | RTM 공유 상태 기반 파이프라인 |
| 기획 분석 방법 | 유저 스토리 서술 | 9차원 매트릭스 × 엔티티 전수 순회 |
| 이슈 에스컬레이션 | 없음 | Tier 1(기획자) / Tier 2(QA 내부) / Tier 3(무시) |
| 와이어프레임 처리 | 허용 | **완전 금지** |
| HTML 구조 | 3-panel (원문 패널 포함) | 2-panel (이슈 카드 중심) |
| 자기검증 | 없음 | plan-analyst Step 5 체크리스트 |
| 재작업 루프 | 없음 | tc-reviewer FAIL → tc-writer 자동 연결 |
| 사용자 확인 단계 | 없음 (자동 진행) | 각 에이전트 완료 후 **명시적 ⏸ 확인** 필수 |
| AI 결과 독립 검증 | 없음 | 07-qa-guardian |
| 기획자 소통 채널 | 없음 | 기획자확인요청.md (Tier-1 이슈만 필터링) |

---

## 11. 실제 산출물 비교 (Case ID 기준)

> `Safety1.0/agent_output/` 기준

| 산출물 | 구버전 경로 | 신규 경로 |
|--------|-----------|---------|
| 기획 분석 HTML | `analysis/1.0/CaseID/Case ID-기획파악용.html` | `analysis/1.2/CaseID-QA확인용.html` |
| 기획자 확인 요청 | 없음 | `analysis/1.0/CaseID/Case ID-기획자확인요청.md` |
| 시나리오 MD | `scenario/1.0/구버전/Case ID_시나리오.md` | `scenario/1.2/Case ID_시나리오.md` |
| TC CSV | `TC/1.0/Case ID_TC.csv` | `TC/1.2/Case ID_TC.csv` |
| RTM | 없음 | `rtm/1.2/Case ID_RTM.md` (v3 기준 57 REQ 추적) |
| 리뷰 MD | `review/1.0/1.1/Case_ID_review.md` | `review/1.1/Case ID_review.md` |

→ 구버전 대비 **기획자확인요청.md + RTM**이 신규 추가된 핵심 산출물

---

*비교 기준 파일: `.github/agents/plan-translator.agent.md`, `01-plan-analyst.agent.md`, `02-design-validator.agent.md`, `03-scenario-writer.agent.md`, `04-tc-writer.agent.md`, `05-tc-reviewer.agent.md`, `tc-generator.agent.md`, `design-qa.agent.md`, `tc-reviewer.agent.md`*
