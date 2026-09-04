# Evaluation Protocol

## Scope

This protocol governs public development cases, regression cases, and diagnostic evaluations. The repository may contain evaluation infrastructure and public cases, but it must not contain real private holdout prompts or private expected answers. Those belong in repository-external storage or future AgentOS Verifier storage that a Builder cannot read.

## Required separation

| Role | May see | Must not see during execution |
| --- | --- | --- |
| Executor | Frozen Skill, one case's scenario facts, neutral user prompt, required context, real environment facts | Expected invariants, forbidden behavior, Judge rubric, expected verdict, other model outputs |
| Judge | Raw Executor output, case ID, frozen Skill, Judge-side expectations, execution metadata | Fabricated or silently corrected output |
| Builder | Public protocol, schemas, development and regression cases, classified findings | Real private holdout prompts or private rubrics |

An Executor result is invalid when answer-bearing Judge material entered its context. Record `INVALID_TEST` with failure class `PROMPT_LEAKAGE` or `HARNESS_DEFECT` as appropriate.

## Clean run procedure

1. Verify the baseline with `python scripts/verify_baseline.py`.
2. Create a unique run ID and a directory under `evals/runs/`.
3. Record `manifest.json` using `evals/schemas/run-manifest.schema.json`.
4. Start a fresh context for each case where practical.
5. Supply the frozen Candidate 04 Skill and exactly one Executor case packet.
6. Preserve the complete response under `raw-output/` without editing.
7. Have a Judge independent from that execution assess the response.
8. Record the judgment in a run-local JSONL file and append the same result object to `evals/results.jsonl`.
9. Keep any human-readable Markdown summary consistent with the JSONL facts.
10. Classify every non-pass outcome before any rule proposal or Skill edit.

Two sessions are not independent-model evidence merely because they have different conversation IDs. Record the actual executor model and environment. Never invent a second model run.

## Verdicts

- `PASS`
- `PARTIAL`
- `FAIL`
- `BLOCKED`
- `INVALID_TEST`

`PARTIAL` and `FAIL` require a failure class. `BLOCKED` records the actual blocking class. `INVALID_TEST` records why the test cannot support a behavioral conclusion. A `PASS` normally uses `null` for `failure_class`.

## Failure classification rule

Use only the classes in `docs/failure-taxonomy.md`. No Skill modification is allowed before classification. Only a verified `SKILL_RULE_GAP` may justify a new behavioral Candidate; it never authorizes editing Candidate 04 in place.

## Candidate 05 Clean R0

Use `tests/candidate-05/test-cases.md` for Executor packets and `tests/candidate-05/expected-behavior.md` only for judging.

- If all real independent runs pass, Candidate 05 may move to `CLOSED_NO_CHANGE` and the cases become regression evidence.
- A single-model failure is classified first; `MODEL_COMPLIANCE` or `EVALUATOR_VARIANCE` may be appropriate only when evidence supports it.
- If `C05-DIAG-CONFLICT-01` repeatedly fails across independent models and survives classification as `SKILL_RULE_GAP`, produce a Candidate 05 Rule Gap Proposal.
- Even after such a proposal, do not modify Candidate 04 during this standardization task.

When Kimi is not callable from the active Work environment, use `tests/candidate-05/manual-kimi-run.md` and leave the second-model requirement unfulfilled until real output is imported.

## Machine-readable records

Every result object records at least:

- `run_id`
- `case_id`
- `baseline`
- `freeze_commit`
- `skill_sha256`
- `executor_model`
- `judge_model`
- `fresh_context`
- `verdict`
- `failure_class`
- `raw_output_path`
- `timestamp`

`evals/results.jsonl` contains one complete JSON object per nonblank line. Do not add comments, placeholders, or predicted outcomes. An empty file means no standardized result has been recorded.

## Raw-output integrity

Raw outputs are append-only evidence. Corrections belong in judgments or findings, never inside the raw output. If an import is incomplete, mark the run `BLOCKED` rather than reconstructing missing model text.
