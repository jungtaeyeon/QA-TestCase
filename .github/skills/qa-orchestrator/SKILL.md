# QA Orchestrator Skill

파이프라인 전체를 조율하는 오케스트레이터 스킬입니다.
이 스킬을 호출하면 에이전트 팀의 실행 순서, 핸드오프 계약, 에러 처리 전략을 확인하고 파이프라인을 시작합니다.

---

## 파이프라인 아키텍처

**패턴**: Pipeline + Producer-Reviewer 하이브리드

```
[기획서 입력]
      ↓
  01 plan-analyst ──────────────── RTM v0 생성
      ↓
  02 scenario-writer ───────────── RTM v1 (시나리오 첨부)
      ↓                ↘ [병렬 실행 가능]
  03 tc-writer      04 design-validator ── RTM v3 (디자인 이슈 태그)
      ↓                ↙
  05 tc-reviewer ──── RTM v2 기반 검증
      ├── FAIL ──→ 03 tc-writer (피드백 루프, 최대 3회)
      └── PASS ──→ RTM v4 생성
             ↓
  06 tc-uploader ───────────────── Testiny 등록 완료
```

---

## 실행 모드

이 스킬을 로드한 뒤 실행 모드를 선택합니다.

### Full Mode (전체 파이프라인)
기획서 → Testiny 등록까지 전체 실행.
```
"qa-orchestrator full mode로 plan/.../feature.md 실행해줘"
"qa-orchestrator 전체 파이프라인으로 {기획서 경로} 처리해줘"
```

### Quick Mode (핵심 산출물만)
기획서 → TC 생성까지만. Figma 동기화 및 Testiny 업로드 제외.
```
"qa-orchestrator quick mode로 시나리오 + TC만 만들어줘"
```

### Single Mode (특정 에이전트 단독)
특정 단계만 실행.
```
"qa-orchestrator single: plan-analyst 실행"
"qa-orchestrator single: tc-reviewer 실행"
```

---

## 에이전트 핸드오프 계약

각 에이전트는 다음 조건이 충족된 경우에만 실행됩니다.

| 에이전트 | 선행 조건 | 산출물 (다음 에이전트에게 전달) |
|---------|---------|------------------------------|
| **01 plan-analyst** | 기획서 파일 존재 | RTM v0, QA 분석 HTML |
| **02 scenario-writer** | RTM v0 존재 | RTM v1, 시나리오 MD |
| **03 tc-writer** | RTM v1 존재, 시나리오 MD 존재 | RTM v2, TC CSV |
| **04 design-validator** | RTM v1 이상, Figma URL | RTM v3, 디자인 QA HTML |
| **05 tc-reviewer** | RTM v2 존재, TC CSV 존재 | RTM v4 (PASS 시), review_actions.csv |
| **06 tc-uploader** | RTM v4 존재 (PASS 판정) | Testiny 등록 완료 |

> **중요**: 선행 조건이 충족되지 않은 에이전트는 실행하지 않고 사용자에게 안내합니다.

---

## 전제 조건 주입 (모든 에이전트 실행 전 필수)

파이프라인의 어느 단계에서도 다음 전제 조건을 **항상** 적용합니다.

```
1. rtm-manager 스킬 확인 (RTM 상태 관리 규칙)
2. 기획서 기반 원칙 (plan/ 폴더 기획서 외 임의 확장 금지)
3. 한국어 출력
4. 파일 저장 우선
5. 확인 필요 사항은 임의 결정 없이 사용자에게 표면화
```

> `tooluniverse-pharmacovigilance`는 각 에이전트가 PV 도메인 판단이 필요한 시점에 자율적으로 참조합니다. 파이프라인 레벨에서 강제 로드하지 않습니다.

---

## 에러 처리 전략

| 상황 | 대응 |
|------|------|
| RTM 파일 없음 | 선행 에이전트 실행 안내 후 중단 |
| tc-reviewer FAIL (1~2회) | review_actions.csv를 tc-writer에게 전달하여 재작업 |
| tc-reviewer FAIL (3회 이상) | 자동 루프 중단 + 사용자에게 수동 개입 요청 |
| Figma URL 접근 실패 | Figma 단계를 건너뛰고 Testiny 업로드 진행 |
| Testiny 업로드 실패 | 실패 TC 목록과 원인을 보고하고 재시도 안내 |

---

## 파이프라인 상태 추적

오케스트레이터는 실행 중 현재 상태를 파악하기 위해 RTM 버전을 확인합니다:

| RTM 버전 | 파이프라인 상태 |
|---------|--------------|
| 파일 없음 | 파이프라인 미시작 |
| v0 | plan-analyst 완료 |
| v1 | scenario-writer 완료 |
| v2 | tc-writer 완료 |
| v3 | design-validator 완료 |
| v4 | tc-reviewer PASS |
| v4 + Testiny 등록 완료 | 파이프라인 종료 |

현재 RTM 버전을 확인하면 어느 단계부터 재개해야 하는지 파악할 수 있습니다.

---

## 파이프라인 시작 체크리스트

이 스킬을 로드한 뒤 다음을 순서대로 확인합니다:

- [ ] 기획서 파일 경로 확인
- [ ] Figma URL 제공 여부 확인 (없으면 Quick Mode 권장)
- [ ] RTM 현재 상태 확인 (이어서 실행할지 처음부터 실행할지 결정)
- [ ] 실행 모드 선택 (full / quick / single)
- [ ] tooluniverse-pharmacovigilance 스킬 로드 (필수)
- [ ] 파이프라인 시작
