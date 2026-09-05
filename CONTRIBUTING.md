# Contributing

## Start with project state

Read, in order:

1. `STATUS.md`
2. `project/project-state.yaml`
3. `project/baseline-manifest.json`
4. `AGENTS.md`
5. the current Candidate manifest

## Before a change

- Open a focused issue or proposal describing the observed behavior and evidence.
- Classify failures using `docs/failure-taxonomy.md`.
- Do not edit the current frozen Skill or frozen evidence.
- Keep Executor prompts separate from Judge expectations.
- Keep private holdout material outside the repository.

Only a verified `SKILL_RULE_GAP` may justify a new behavioral Candidate. Model compliance or evaluator variance alone is not a rule-change reason.

## Validation

Run:

```bash
python scripts/validate_repo.py
python scripts/verify_baseline.py
python scripts/lint_eval_prompts.py
git diff --check
```

Prompt-lint warnings require human review but are not automatic test failures. Include real commands and results in the change report; do not claim unavailable model runs.

## Commits and pull requests

- Keep commits logically scoped.
- Explain behavioral impact, evidence, and unverified items.
- Do not combine lifecycle states in one status string; use separate role or historical fields.
- Do not change the Apache-2.0 license without explicit owner authorization.
