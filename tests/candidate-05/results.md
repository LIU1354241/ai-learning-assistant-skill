# Candidate 05 Clean R0 Results

Status: `TWO_EXECUTOR_ENVIRONMENTS_COMPLETE`

## Run summaries

### Codex Work

Run: `c05-r0-clean-20260905-codex-work`

Five clean cases ran in separate fresh Codex Work Agent contexts. A role-separated fresh Judge recorded 5/5 `PASS`. Exact model and session/context identifiers were not exposed, so that run's Judge separation is recorded but cannot be independently demonstrated from platform identifiers.

### External Kimi

Run: `c05-r0-clean-20260905-kimi-external`

The user ran each case in a separate new Kimi conversation. OpenAI / GPT-5.6 Sol judged each case in a fresh Judge conversation, using a different provider and account from the Executor. Exact Kimi model/version and Executor/Judge session identifiers were not exposed.

| Case ID | Codex Work | External Kimi | Kimi failure class |
| --- | --- | --- | --- |
| `REG-C04-EVIDENCE-01` | `PASS` | `PARTIAL` | `MODEL_COMPLIANCE` |
| `REG-C04-EVIDENCE-02` | `PASS` | `PASS` | `null` |
| `REG-C04-TRANSFER-01` | `PASS` | `PASS` | `null` |
| `C05-DIAG-CONFLICT-01` | `PASS` | `PARTIAL` | `MODEL_COMPLIANCE` |
| `REG-C04-SCOPE-01` | `PASS` | `PASS` | `null` |

External Kimi summary: 3 `PASS`, 2 `PARTIAL / MODEL_COMPLIANCE`, 0 `FAIL`, and 0 `SKILL_RULE_GAP`.

## Evaluation conclusion

The acceptance requirement for at least two independent Executor environments is satisfied by the completed Codex Work and external Kimi runs. This is distinct from Judge independence: the external Kimi judgments were produced by OpenAI / GPT-5.6 Sol using a different provider, different account, and fresh Judge conversation per case; exact session identifiers remain `NOT_EXPOSED`.

Candidate 05 remains `DIAGNOSTIC`. The two Kimi non-pass outcomes are classified as `MODEL_COMPLIANCE`, and neither reproduced as a non-pass in the Codex Work execution. Because not all independent runs passed, `CLOSED_NO_CHANGE` is not established. Because no `SKILL_RULE_GAP` exists, the Promotion Gate does not permit a rule proposal.

The original leaky R0 remains `INVALID_TEST / PROMPT_LEAKAGE`; it is historical evidence and was not used as Clean R0 Executor input.
