# Agent Operating Contract

This repository is a governed behavioral Skill project. Repository state, evidence, and runtime behavior must not be inferred from conversation history.

## Minimum read order

1. `STATUS.md`
2. `project/project-state.yaml`
3. `project/baseline-manifest.json`
4. The constraints in this `AGENTS.md`
5. The current Candidate manifest
6. Task-relevant tests and history
7. `docs/evolution-log.md` only when deeper historical context is needed

The current Candidate manifest is `tests/candidate-05/manifest.yaml`.

## Frozen scope

- Candidate 04 is `FROZEN` and has role `CURRENT_BASELINE`.
- `SKILL-v0.6-candidate-04-failure-aware-degradation.md` is the frozen source.
- `SKILL.md` is the canonical runtime entry and must remain byte-identical to the frozen source while Candidate 04 is current.
- Every file and SHA listed in `project/baseline-manifest.json` under `frozen_evidence` is immutable evidence.
- Freeze provenance is commit `164c4d9`; repository `HEAD` is not required to remain at that commit.

## Allowed mutations

Within an authorized task, an Agent may update project governance, documentation, public evaluation infrastructure, development or regression cases, schemas, and validation scripts. It may record real evaluation outputs and classifications. It may propose a new Candidate only after the Promotion Gate is satisfied.

## Forbidden actions

- Do not change Candidate 04 behavior or rewrite its frozen source.
- Do not edit, delete, or replace frozen evidence.
- Do not create Candidate 06 as part of standardization.
- Do not promote Candidate 05 directly or treat it as baseline behavior.
- Do not modify any Skill after an observed failure until failure classification is complete.
- Do not treat `MODEL_COMPLIANCE`, `PROMPT_LEAKAGE`, `HARNESS_DEFECT`, `EVALUATOR_VARIANCE`, `TOOL_OR_ENVIRONMENT`, `CONTEXT_MISSING`, or `UNKNOWN` as a rule-gap finding.
- Do not store real private holdout prompts in this repository. Use repository-external storage or AgentOS Verifier storage.
- Do not invent model runs, judgments, raw outputs, or verification results.
- Do not force push, rewrite history, change repository visibility, or change the Apache-2.0 license.

## Candidate Promotion Gate

A behavioral Candidate may advance only when all of the following are true:

1. The test is valid and the Executor did not see expected behavior or Judge rubric.
2. The failure is reproducible with complete raw outputs and execution metadata.
3. Independent judgment classifies the failure as `SKILL_RULE_GAP`.
4. Evidence shows the gap is not model compliance, evaluator variance, missing context, harness behavior, or tool/environment failure.
5. The proposed change is minimal, scoped, and has explicit regression coverage.
6. Validation passes and the promotion decision is recorded without altering the current frozen baseline in place.

No observed failure may trigger a Skill edit before this classification and gate review.

## Verification commands

Run from the repository root:

```bash
python scripts/validate_repo.py
python scripts/verify_baseline.py
python scripts/lint_eval_prompts.py
git diff --check
```

Warnings from `lint_eval_prompts.py` require review but are not automatic failures.

## Reporting requirements

After each phase report:

1. what changed;
2. what was verified;
3. unresolved findings;
4. `git status --short`;
5. whether any frozen file changed.

Separate completed verification from inference and unverified requirements. Preserve complete raw model output for every real evaluation. Do not mark a release ready while any P0 finding remains, and do not create a release tag until all required validation passes and the intended release commit is known.

