# Candidate 05 Clean R0 Results

Status: `ONE_ENVIRONMENT_COMPLETE`

Run `c05-r0-clean-20260905-codex-work` executed all five clean cases in separate fresh Codex Work Agent contexts. A separate fresh Judge that did not produce the outputs recorded 5/5 `PASS`.

| Case ID | Verdict |
| --- | --- |
| `REG-C04-EVIDENCE-01` | `PASS` |
| `REG-C04-EVIDENCE-02` | `PASS` |
| `REG-C04-TRANSFER-01` | `PASS` |
| `C05-DIAG-CONFLICT-01` | `PASS` |
| `REG-C04-SCOPE-01` | `PASS` |

The exact Executor/Judge model identifier was not exposed. This is one Codex Work execution environment with independent context and Judge role, not two independent model environments. Kimi and another independent model run remain pending. Candidate 05 therefore remains `DIAGNOSTIC`; this run alone does not permit `CLOSED_NO_CHANGE`.

The original leaky R0 is classified `INVALID_TEST` / `PROMPT_LEAKAGE`; that is a test-design classification, not a claim that a clean model execution occurred.
