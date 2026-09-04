# Candidate Lifecycle

## Purpose

Candidates are evidence-governed changes to the behavioral Skill. A Candidate number is not proof that a rule change is needed. Diagnostic work begins with a hypothesis and may close without changing the baseline.

Lifecycle status and project role are separate fields. Use one lifecycle status only; retain historical facts such as `was_frozen: true` separately.

## Legal lifecycle states

| Status | Meaning | May become baseline? |
| --- | --- | --- |
| `DIAGNOSTIC` | A hypothesis is being tested; no rule change is authorized. | No |
| `PROPOSED` | A classified rule-gap proposal exists. | No |
| `EXPERIMENTAL` | A scoped candidate rule set is under behavioral test. | No |
| `VALIDATED` | Required tests passed and evidence is recorded. | Not yet |
| `ACCEPTED` | The validated candidate was approved for formalization. | Pending freeze |
| `FROZEN` | Immutable formal source and evidence are recorded. | Yes, when role is `CURRENT_BASELINE` |
| `SUPERSEDED` | A former candidate is no longer current. | No |

## Terminal or non-promotion states

| Status | Meaning |
| --- | --- |
| `REJECTED` | Evidence does not support the proposal or its risk is unacceptable. |
| `CLOSED_NO_CHANGE` | The diagnostic was resolved by the existing baseline; no new rules are required. |
| `BLOCKED` | Required evidence, execution capability, or decision authority is unavailable. |

`BLOCKED` may return to the prior active state when the blocker is resolved. `REJECTED` and `CLOSED_NO_CHANGE` require a new evidence-backed diagnostic to reopen.

## Typical path

```text
DIAGNOSTIC → PROPOSED → EXPERIMENTAL → VALIDATED → ACCEPTED → FROZEN
```

Any active state may move to `REJECTED` or `BLOCKED`. A diagnostic may move directly to `CLOSED_NO_CHANGE`. A frozen candidate may later move to `SUPERSEDED`; record `was_frozen: true` rather than combining lifecycle strings.

## Promotion Gate

Before `DIAGNOSTIC` can become `PROPOSED`:

1. Executor input contains only scenario facts, a neutral user prompt, and necessary context.
2. Expected invariants, forbidden behavior, expected verdicts, and the Judge rubric were not visible to the Executor.
3. Complete raw outputs and model, environment, date, context-isolation, and Skill-hash metadata are preserved.
4. A Judge independent from the producing execution reviews the output.
5. Every failure is assigned a failure class using `docs/failure-taxonomy.md`.
6. The failure reproduces sufficiently to distinguish a rule gap from model or evaluator variance.
7. At least one verified `SKILL_RULE_GAP` remains after alternative causes are excluded.

Before `PROPOSED` can advance further, the proposed behavioral delta must be minimal, have explicit regressions, and avoid editing the current frozen source in place.

No observed failure may trigger a Skill edit until failure classification is complete. Only a verified `SKILL_RULE_GAP` may justify a new behavioral Candidate.

## Current project application

- Candidate 01: `SUPERSEDED`; `was_frozen: true`.
- Candidate 02: `SUPERSEDED`; `was_frozen: true`.
- Candidate 03: `SUPERSEDED`; `was_frozen: true`.
- Candidate 04: `FROZEN`; role `CURRENT_BASELINE`.
- Candidate 05: `DIAGNOSTIC`; role `CURRENT_DIAGNOSTIC`.
