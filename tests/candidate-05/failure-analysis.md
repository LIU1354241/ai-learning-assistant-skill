# Candidate 05 Failure Analysis

Status: `CLASSIFIED_MODEL_COMPLIANCE_FINDINGS`

Three real Executor environments have completed Candidate 05 evaluation runs. The Codex Work and Claude Haiku 4.5 runs each passed all five cases. The external Kimi run produced three `PASS` and two `PARTIAL / MODEL_COMPLIANCE` judgments. There were no `FAIL` or `SKILL_RULE_GAP` findings.

## C05-MC-001

- Run: `c05-r0-clean-20260905-kimi-external`
- Case: `REG-C04-EVIDENCE-01`
- Verdict: `PARTIAL`
- Failure class: `MODEL_COMPLIANCE`
- Expected behavior: preserve the self-report as tentative evidence and use a lightweight check when it would materially establish topic-specific capability; preserve appropriate certainty in technical claims.
- Actual behavior: the response avoided a mastery claim and adapted its teaching depth, but deferred learner verification to a later optional clarification and included technical claims stated too strongly.
- Why it matters: the response taught the topic but did not sufficiently validate the learner's topic-specific capability evidence.
- Existing-rule check: Candidate 04 already specifies topic-scoped evidence, the limits of self-report, controlled lightweight verification, and truth/uncertainty boundaries.
- Alternative causes: `SKILL_RULE_GAP` is excluded because the relevant behavior is already explicit; `PROMPT_LEAKAGE`, `HARNESS_DEFECT`, and `CONTEXT_MISSING` are not supported by the preserved clean packet and provenance.
- Reproduction: not reproduced as a non-pass in either the Codex Work or Claude Haiku 4.5 run; both judged the same case `PASS`.
- Disposition: retain as model-compatibility evidence; no Skill change or Candidate 05 rule proposal.

## C05-MC-002

- Run: `c05-r0-clean-20260905-kimi-external`
- Case: `C05-DIAG-CONFLICT-01`
- Verdict: `PARTIAL`
- Failure class: `MODEL_COMPLIANCE`
- Expected behavior: preserve both old and new evidence, scope the conflict, and use explicit clarification or revalidation language proportional to the contradiction.
- Actual behavior: the response preserved both observations and scoped the misconception, but treated the earlier local demo as a decisive counterexample instead of clearly marking the older evidence as needing revalidation.
- Why it matters: the learner-state conclusion is somewhat more settled than Candidate 04's certainty boundary permits for conflicting evidence.
- Existing-rule check: Candidate 04 already distinguishes stable evidence from current working inference and expressly permits clarification or revalidation when evidence conflicts.
- Alternative causes: `SKILL_RULE_GAP` is excluded because the relevant behavior is already explicit; `PROMPT_LEAKAGE`, `HARNESS_DEFECT`, and `CONTEXT_MISSING` are not supported by the preserved clean packet and provenance.
- Reproduction: not reproduced as a non-pass in either the Codex Work or Claude Haiku 4.5 run; both judged the same primary diagnostic case `PASS`.
- Disposition: retain as model-compatibility evidence; no Skill change or Candidate 05 rule proposal.

## Lifecycle effect

Candidate 05 remains `DIAGNOSTIC`. The evidence does not support `CLOSED_NO_CHANGE` because not all real independent Executor runs passed: the valid Kimi run retains two `PARTIAL / MODEL_COMPLIANCE` outcomes. It does not support `PROPOSED` because no verified `SKILL_RULE_GAP` exists. The Claude 5/5 `PASS` run strengthens compatibility evidence without erasing the Kimi findings. Candidate 04 remains unchanged.
