# SafetyDB QA Harness

PV(Pharmacovigilance) 도메인 전용 QA 자동화 파이프라인입니다.
기획서 입력부터 Testiny 등록까지 7개의 전문 에이전트가 순차·병렬로 작동하며, `qa-orchestrator` 스킬이 전체를 조율합니다.

---

## 에이전트 팀

| # | 에이전트 | 역할 | 핵심 산출물 |
|---|---------|------|------------|
| 01 | `plan-analyst` | 기획서 → QA 분석 HTML + **RTM v0** (기획 품질 이슈 포함) | `analysis/*-QA분석.html` |
| 02 | `design-validator` *(선택)* | 기획서 + Figma → 디자인 이슈 리포트 + **RTM v1** | `review/*_design_qa_report.html` |
| 03 | `scenario-writer` | RTM v0(또는 v1) → 시나리오 + **RTM v2** | `scenario/*_시나리오.md` |
| 04 | `tc-writer` | RTM v2 → TC CSV + **RTM v3** | `TC/*_TC.csv` |
| 05 | `tc-reviewer` | TC + RTM v3 → PASS/FAIL 판정 + **RTM v4** | `review/*_review.md` |
| 06 | `tc-uploader` | Figma TC 동기화 + Testiny 등록 | Testiny 등록 완료 |
| 07 | `qa-guardian` | 어느 단계에서나 AI 결과 검증 | `review/*_guardian_report.md` |

> `TC-Update`, `doublecheck`, `devils-advocate`는 기존 에이전트를 그대로 유지합니다.

---

## 파이프라인 흐름

```
[기획서 입력]
      ↓
  01 plan-analyst ──────────── RTM v0 ─── ⏸ 사용자 확인 (기획 품질 이슈)
      ↓                    ↘
  02 design-validator(선택) ─ RTM v1 ─── ⏸ 사용자 확인 (디자인 이슈)
      ↓  (건너뛰면 RTM v0 그대로)
  03 scenario-writer ──────── RTM v2 ─── ⏸ 사용자 확인 (시나리오 + 확인 필요 사항)
      ↓
  04 tc-writer ──────────────── RTM v3 ── ⏸ 사용자 확인 (TC 검토)
      ↓
  05 tc-reviewer ──────────────RTM v4
      ├── FAIL ──→ 04 tc-writer (재작업 피드백)
      └── PASS ──→ 06 tc-uploader
```

> **⏸ 사용자 확인**: 각 에이전트는 완료 후 자동으로 다음 단계를 실행하지 않습니다.
> 사용자가 산출물을 검토하고 명시적으로 다음 에이전트 실행을 지시해야 합니다.

---

## 공유 아티팩트 (RTM 버전 흐름)

RTM(Requirements Traceability Matrix)은 파이프라인 전체에서 공유되는 상태 파일입니다.
각 에이전트는 RTM을 읽고 자신의 산출물을 반영하여 다음 버전으로 넘깁니다.

| RTM 버전 | 생성/갱신 주체 | 추가 내용 |
|---------|--------------|---------|
| **v0** | plan-analyst | 기능 목록, 요구사항 ID, 기획 품질 이슈 |
| **v1** | design-validator *(선택)* | 디자인 이슈 태그 (Missing/Mismatch 등) — 건너뛰면 v0 그대로 유지 |
| **v2** | scenario-writer | 시나리오 ID 매핑, 관점 태그 |
| **v3** | tc-writer | TC ID 범위, type별 분포 |
| **v4** | tc-reviewer | 리뷰 결론 (PASS/FAIL), 액션 항목 |

**RTM 저장 경로**: `Safety1.0/agent_output/rtm/{기획서명}_RTM.md`

---

## 전체 산출물 위치

| 아티팩트 | 경로 |
|---------|------|
| RTM | `Safety1.0/agent_output/rtm/{기획서명}_RTM.md` |
| QA 분석 HTML | `Safety1.0/agent_output/analysis/{기능명}-QA분석.html` |
| 시나리오 MD | `Safety1.0/agent_output/scenario/{기획서명}_시나리오.md` |
| TC CSV | `TC/{기획서명}_TC.csv` |
| 리뷰 결과 | `Safety1.0/agent_output/review/{기획서명}_review.md` |
| 디자인 QA | `Safety1.0/agent_output/review/{기획서명}_design_qa_report.html` |
| 변경 이력 | `Safety1.0/agent_output/changelog/{날짜}_{대상}_변경내역.md` |

---

## 모든 에이전트 공통 전제 조건

다음은 에이전트 실행 전 **예외 없이** 적용되는 전제 조건입니다.

1. **PV 도메인 참조**: PV 용어 해석, 역할 맥락, 규제 판단이 필요한 시점에 `tooluniverse-pharmacovigilance` 스킬을 참조합니다. 매 실행마다 강제 로드하지 않으며, 필요할 때 꺼내쓰는 참조 도구입니다.
2. **RTM 확인**: 자신의 선행 RTM 버전이 존재하는지 확인한 뒤 실행합니다. 없으면 선행 에이전트 실행을 안내합니다.
3. **기획서 기반 원칙**: `plan/` 폴더의 기획서에 명시된 내용만 사용합니다. 임의 확장 금지.
4. **한국어 출력**: 모든 산출물은 한국어로 작성합니다.
5. **파일 저장 우선**: 결과는 파일로 저장하고, 채팅에는 파일 경로와 요약만 보고합니다.
6. **확인 필요 사항 표면화**: 기획서만으로 판단하기 어렵거나 해석이 갈리는 항목은 임의로 결정하지 않고, 산출물에 `확인 필요 사항` 섹션으로 분리하여 사용자 검토를 요청합니다.

---

## Figma 탐색 규칙 (design-validator 전용)

1. **지정 캔버스만 탐색**: URL의 `node-id`가 가리키는 페이지 안에서만 탐색합니다. 다른 페이지로 확장 금지.
2. **미반영 처리**: 지정 캔버스에 해당 기능이 없으면 "캔버스에 미반영"으로 기록하고 진행합니다.
3. **URL 미제공 시**: 사용자에게 Figma URL을 요청합니다. 임의 탐색 금지.

---

## 관련 스킬

| 스킬 | 용도 |
|------|------|
| `qa-orchestrator` | 파이프라인 전체 조율, 에이전트 간 핸드오프 계약, 에러 처리 |
| `rtm-manager` | RTM 공유 상태 생성·조회·갱신 규칙 |
| `tooluniverse-pharmacovigilance` | PV 도메인 전문 지식 (PV 용어/역할/규제 판단 필요 시 참조) |
| `scenario-guidelines` | 시나리오 도출 6단계 프로세스 |
| `tc-writing-rules` | TC 작성 기준, CSV 스키마, Lint 규칙 |
| `figma-tc` | Figma 3-way 비교 및 TC 동기화 |
| `testiny-upload` | Testiny 업로드 절차 및 필드 매핑 |

---

## 빠른 시작

```
# 전체 파이프라인 실행
"qa-orchestrator 스킬 사용해서 plan/.../feature.md 전체 파이프라인 실행해줘"

# 특정 단계만 실행
"plan-analyst로 plan/.../feature.md 분석해줘"
"scenario-writer로 RTM v0 기반 시나리오 작성해줘"

# 디자인 검증 (병렬 실행 가능)
"design-validator로 plan/.../feature.md https://figma.com/design/... 비교해줘"
```

## graphify (필수 — 모든 파일 탐색 전 우선 참조)

이 프로젝트는 `graphify-out/`에 knowledge graph가 있습니다.

**규칙 (예외 없이 적용):**
- **파일 탐색(Glob/Grep/Read) 전 반드시** `graphify-out/GRAPH_REPORT.md`를 먼저 읽어 god nodes와 community 구조를 파악합니다.
- `graphify-out/wiki/index.md`가 존재하면 raw 파일 대신 wiki를 우선 탐색합니다.
- 코드 파일을 수정한 후에는 `.venv/bin/graphify update .`를 실행해 그래프를 최신 상태로 유지합니다.
