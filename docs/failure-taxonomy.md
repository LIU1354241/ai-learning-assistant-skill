# Failure Taxonomy

Classify a non-pass result before considering a Skill change.

| Failure class | Meaning | Rule-change implication |
| --- | --- | --- |
| `SKILL_RULE_GAP` | The frozen rules lack or contradict behavior needed for the valid case, and alternative causes have been excluded with reproducible evidence. | May justify a new Candidate proposal; never an in-place baseline edit. |
| `MODEL_COMPLIANCE` | The rule is sufficiently explicit, but a model does not follow it reliably. | Do not change the Skill automatically. Record model compatibility evidence. |
| `PROMPT_LEAKAGE` | Executor input reveals expected behavior, forbidden behavior, rubric, or verdict. | Invalidate and clean the test. |
| `HARNESS_DEFECT` | Context construction, isolation, capture, fixture, or execution plumbing makes the result unreliable. | Fix the harness and rerun. |
| `EVALUATOR_VARIANCE` | Judges disagree or a verdict depends on unsupported interpretation. | Reconcile or add independent judgment before concluding. |
| `TOOL_OR_ENVIRONMENT` | Required tools, files, permissions, network, runtime, or model access are unavailable or faulty. | Fix or record the environment; do not infer behavior. |
| `CONTEXT_MISSING` | Required case facts or instructions were absent from the valid Executor packet. | Repair the case/context and rerun. |
| `UNKNOWN` | Available evidence cannot yet support a more specific class. | Block rule changes and gather evidence. |

## Classification standard

A `SKILL_RULE_GAP` classification requires all of the following:

- valid neutral test input;
- verified frozen Skill hash;
- complete raw output and execution metadata;
- independent judgment;
- evidence that the expected behavior is not already clearly required;
- reproduction sufficient to rule out ordinary model or evaluator variance;
- a scoped explanation of why the gap belongs to the Skill.

When evidence is insufficient, use `UNKNOWN`, `BLOCKED`, or the most accurate non-rule class. Classification certainty must not be inflated to advance a Candidate.
