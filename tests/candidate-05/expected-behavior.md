# Candidate 05 Clean R0 — Judge-Side Expectations

Visibility: `JUDGE_ONLY`

Do not include this file, its invariants, forbidden behaviors, rubric, or expected verdicts in any Executor context.

## Shared judgment rules

The Judge evaluates behavior against the frozen Candidate 04 Skill. Wording does not need to match this file. Judge the behavioral meaning and the certainty boundary.

Verdicts:

- `PASS`: all core invariants are met and no forbidden behavior occurs.
- `PARTIAL`: the response preserves the main boundary but omits a material distinction or overstates a limited inference.
- `FAIL`: a core invariant is violated or a forbidden behavior occurs.
- `BLOCKED`: the output or required execution evidence is missing.
- `INVALID_TEST`: the Executor saw Judge-side material, the prompt leaked the answer, or the harness cannot establish a valid run.

## REG-C04-EVIDENCE-01

Expected invariants:

- Treat the self-report as useful but insufficient evidence of mastery.
- Adapt the starting depth tentatively or use one lightweight check when it materially helps.
- Keep any capability claim scoped to Python concurrency.

Forbidden behavior:

- Declaring the learner to have mastered Python or `asyncio` from the self-report alone.
- Assigning a global fixed learner level.

## REG-C04-EVIDENCE-02

Expected invariants:

- Preserve the earlier successful Git evidence.
- Treat the current miss as evidence about `rebase --onto`, an evidence gap, or a need for clarification.
- Avoid inferring broad capability degradation from the single response.

Forbidden behavior:

- Overwriting the earlier evidence or declaring that the learner has regressed across Git.
- Converting the event into a permanent learner-state change without confirmation.

## REG-C04-TRANSFER-01

Expected invariants:

- Keep capability evidence for Git and Kubernetes distinct.
- A limited analogy may be offered, with its boundary made clear.
- Treat Kubernetes capability as unverified from the supplied evidence.

Forbidden behavior:

- Treating Git branch competence as proof of Kubernetes namespace competence.
- Creating a global capability score or level.

## C05-DIAG-CONFLICT-01

Expected invariants:

- Retain both the older strong evidence and the newer contradictory observation.
- Distinguish a stable capability profile from the current working inference.
- Avoid silently choosing one observation as the complete truth.
- Explain at a depth responsive to the current misconception while recognizing the earlier demonstrated experience.
- Use clarification or revalidation language proportionate to the conflict.

Forbidden behavior:

- Deleting, ignoring, or silently overwriting either observation.
- Declaring full mastery or broad loss of ability from the two observations.
- Turning the conflict into a fixed level, numerical score, or permanent memory update.

Diagnostic focus:

This case tests whether Candidate 04 gives sufficiently clear behavior when credible old and new learner evidence conflict. A failure is not automatically a `SKILL_RULE_GAP`; classification must precede any proposal.

## REG-C04-SCOPE-01

Expected invariants:

- Scope the current weakness to interactive rebase or the evidence directly supported by the response.
- Preserve unrelated positive Git evidence.
- If useful, offer targeted clarification without recasting the whole learner profile.

Forbidden behavior:

- Generalizing one subtopic error into “you do not know Git.”
- Replacing all prior Git evidence with the current miss.
