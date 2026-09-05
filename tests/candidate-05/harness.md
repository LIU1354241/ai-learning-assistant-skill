# Candidate 05 Clean R0 Harness

## Separation rule

An Executor receives only:

1. the byte-verified frozen Candidate 04 Skill;
2. one case from `test-cases.md` containing scenario facts, neutral user prompt, and required context;
3. minimal system facts needed to describe the available environment.

The Executor never receives `expected-behavior.md`, a forbidden-behavior list, a Judge rubric, an expected verdict, earlier outputs, or another case in the same context.

## Execution protocol

1. Run `python scripts/verify_baseline.py` and record the Skill SHA.
2. Create a fresh context for each case where the environment permits it.
3. Load `SKILL.md` as the behavioral instruction without altering it.
4. Supply exactly one clean case packet.
5. Save the complete raw response without corrections.
6. Record model, environment, timestamp, context freshness, and tool availability in the run manifest.
7. Give the raw output and `expected-behavior.md` to a Judge that did not produce that output.
8. Record the verdict and failure class in both the run record and `evals/results.jsonl`.
9. If a failure occurs, complete failure classification before proposing or editing any Skill.

## Independence

Two labels or sessions from the same underlying model do not automatically establish independent-model reproduction. Record the real provider/model/environment. Never invent a second run.

## Kimi manual path

When Kimi is not callable from the active environment, use `manual-kimi-run.md`. Its packets contain no Judge material. Import returned raw outputs without editing and record the actual Kimi model shown by that environment.

## Original R0

`test-cases-r0-leaky.md` is a reconstructed historical invalid-test note and is excluded from all execution. The recovered Windows originals are preserved under `history/windows-main-164c4d9-untracked/` as `INVALID_TEST / PROMPT_LEAKAGE` evidence and are also excluded from execution.
