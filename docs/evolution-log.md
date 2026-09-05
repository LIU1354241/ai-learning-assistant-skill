# Evolution Log

This log explains why the project changed. Test tables and raw outputs remain in their evidence files.

## Provenance note

The current Git history preserves v0.1/v0.3 snapshots and formal Candidate 03/04 artifacts. It does not contain the original Candidate 01 or Candidate 02 source and test files. Their lifecycle entries are preserved as `SUPERSEDED` with `was_frozen: true`, but missing rationale or test details are not reconstructed as fact.

Candidate 03's freeze record identifies its immediate frozen baseline as “02F Truth + Completion” and records that baseline's SHA-256. That proves Candidate 02F existed in the evaluation lineage, but it does not recover the missing Candidate 02A–02F history.

The final repository and reachable-history search found no authoritative Candidate 01/02 source or test artifacts. The explicit boundary is recorded in `project/history-provenance-gaps.yaml`. Authoritative evidence may be imported later without rewriting existing history; until then, no missing rationale or test sequence is claimed.

## v0.1 — Initial behavioral boundary (2026-08-24)

The first version reframed the project from a general answer prompt into a learning assistant. It established truthfulness, learner context, priority setting, capability building, adaptive depth, execution transparency, explicit exceptions, and a memory boundary. The goal was to convert recurring learning friction into executable Agent behavior without creating a curriculum engine or automatic profile store.

## v0.2 — Learner adaptation

The early rules were not sufficiently explicit about adapting explanations to role, goal, and current level. v0.2 strengthened those dimensions, connected abstract concepts to examples, and introduced optional visualization guidance. The change revised existing rules instead of growing an unlimited rule list.

## v0.3 Stable — Control response weight (2026-08-24)

v0.2 exposed a second risk: helpful modules could accumulate into a heavy response regardless of the actual question. v0.3 stabilized eight core rules, used identity/goal/level/stage as relevant context, and replaced a fixed long format with a light default plus triggered modules. It also kept Skill, Memory, and Workflow responsibilities separate.

The repository history preserves v0.3 at commit `10e08a2`.

## Candidate 01 — Historical baseline, source evidence missing

Candidate 01 is recorded as a former frozen baseline and is now `SUPERSEDED`. The current repository does not preserve its source, problem statement, behavioral delta, or test record. Standardization therefore does not claim why it changed or how it was validated. This is an explicit provenance gap, not a reconstructed history; see `project/history-provenance-gaps.yaml`.

## Candidate 02 / 02F — Truth and completion lineage

Candidate 02 is recorded as a former frozen baseline and is now `SUPERSEDED`. The Candidate 03 freeze record proves that its immediate predecessor was `02F Truth + Completion`, with recorded SHA-256 `f601e4ac00ef8c8c07cd77261355f73da9a1ba63a5b243918241cee194cb4219`.

The inherited Candidate 03 source contains truth boundaries, topic-scoped learner evidence, lightweight verification, source handling, request completion, transfer boundaries, and execution transparency. However, because Candidate 02 source and tests are absent, this repository cannot assign each inherited behavior to a particular 02A–02F step or claim a verified reason/test sequence. That history remains intentionally unresolved rather than inferred and is recorded in `project/history-provenance-gaps.yaml`.

## Candidate 03 — Question → Information Need → Representation

Candidate 03 addressed a representation-selection problem: a generic instruction to “consider a diagram” was not enough to ensure that architecture overviews appeared before detail, while flows, states, comparisons, and explicit deltas needed different forms.

It introduced a selection chain from the user's question to the information need and then to the smallest useful representation. The Hard Overview Gate required an overview before detail when the user needed a system map, while Visual Truth prevented invented nodes or relationships. It also preserved completion and explicit-delta behavior rather than allowing visualization to override them.

The freeze review recorded cross-model evidence, a targeted scope diff against frozen 02F, preservation checks, and formal hashes. Candidate 03 froze at commit `f75a406`, then became `SUPERSEDED` when Candidate 04 froze.

## Candidate 04 — Failure-Aware Degradation

Candidate 04 began because tool or evidence failure could produce two opposite mistakes: abandoning an entire task when only one optional capability failed, or continuing with unsupported certainty when a required source was unavailable.

### R1

R1 introduced failure-aware degradation: stop only the affected part when evidence, permission, safety, or scope is required; otherwise continue with output narrowed to what remaining evidence supports. It also required that an unavailable capability not be assumed recovered without evidence.

### R2

Cross-model review found a stable confirmation failure: when retrieval was unavailable, models could name a concrete remembered candidate as the main answer and append an “unverified” label. The label did not prevent the candidate from being remembered as confirmed. R2 made the confirmation boundary more explicit and added targeted retests.

### R3

R3 refined the boundary so a user who explicitly requests an unverified candidate can still receive one, clearly labeled, while ordinary confirmation requests do not receive unsupported candidates as the conclusion. This avoided turning truthfulness into blanket refusal and added an Agent-transparency guard.

The durable Kimi targeted retest recorded 4/4 PASS. Final cross-model evidence also recorded model compatibility differences: some models followed the rule and others still leaked a candidate. Those failures did not automatically become new rules because the existing rule was explicit, the behavior was not a new cross-model rule gap, and repeating synonymous constraints risked prompt growth and regressions.

The final review found no unresolved Candidate-04-specific rule defect and recommended freezing R3. Commit `164c4d9` is the freeze provenance. The formal source SHA-256 is `c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa`.

## Candidate 05 — Learner Evidence Conflict diagnostic

Candidate 05 is not an accepted rule set. It is a `DIAGNOSTIC` hypothesis that Candidate 04 may not define sufficiently clear behavior when old and new learner capability evidence conflict.

Four original focuses were reclassified as Candidate 04 regressions because the frozen baseline already covers self-report strength, single-failure limits, topic isolation, transfer boundaries, and scope. Only the old/new evidence conflict remains a genuinely new diagnostic.

The original R0 leaked expected behavior into Executor prompts and is classified `INVALID_TEST` / `PROMPT_LEAKAGE`. The next valid step is Clean R0 execution in real independent environments, followed by classification. No failure may produce a Skill edit until a verified `SKILL_RULE_GAP` passes the Promotion Gate.
