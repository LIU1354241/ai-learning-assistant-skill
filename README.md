# AI Learning Assistant Skill

**English** | [简体中文](README.zh-CN.md)

> A truth-first behavioral Skill for evidence-aware learning, representation selection, learner-state boundaries, and transparent Agent execution.

## Current state

| Field | Value |
| --- | --- |
| Current stable version | `v0.6` |
| Current behavioral baseline | Candidate 04 — Failure-Aware Degradation |
| Baseline status | `FROZEN` |
| Baseline role | `CURRENT_BASELINE` |
| Freeze provenance | `164c4d9` |
| Canonical runtime Skill | `SKILL.md` |
| Current diagnostic | Candidate 05 — Learner Evidence Conflict |
| Candidate 05 status | `DIAGNOSTIC` |

Candidate 05 is not accepted, validated, or part of baseline behavior. It has no behavioral rule file. Its next action is a clean R0 evaluation followed by failure classification.

For the machine-readable and Agent-facing source of truth, start with [STATUS.md](STATUS.md), then follow [AGENTS.md](AGENTS.md).

## What the Skill does

The Skill helps an Agent:

- distinguish verified facts, supported inference, and unverified information;
- adapt to learner evidence without inventing a global ability level;
- choose prose, steps, tables, flows, or overview diagrams from the information need;
- preserve truth boundaries when tools or evidence fail;
- separate completed execution, verification, and unresolved work;
- stop when the user's request is complete instead of adding automatic calls to action.

## Usage

Use `SKILL.md` as the runtime instruction entry. It is intentionally byte-identical to the frozen Candidate 04 source recorded in `project/baseline-manifest.json`.

Before relying on the Skill in another Agent environment, run:

```bash
python scripts/validate_repo.py
python scripts/verify_baseline.py
python scripts/lint_eval_prompts.py
git diff --check
```

Then make `SKILL.md` available to the Agent as its Skill instruction. Runtime integration is host-specific; this repository defines behavior and governance, not a particular Agent installer.

## Candidate lifecycle

Candidate status and project role are separate. The legal progression and terminal states are defined in `docs/candidate-lifecycle.md`. A diagnostic can close with `CLOSED_NO_CHANGE`; a Candidate number does not imply that a new rule will be accepted.

No observed failure may trigger a Skill edit until the failure is classified. Only a verified `SKILL_RULE_GAP` may justify a new behavioral Candidate, and a new Candidate must not rewrite the current frozen source in place.

## Evaluation system

- Executor-facing development cases contain only scenario facts, neutral prompts, and required context.
- Expected invariants, forbidden behavior, and Judge rubrics remain Judge-side.
- Raw outputs and real model/environment metadata are preserved for every recorded run.
- Human-readable Markdown and `evals/results.jsonl` must describe the same facts.
- Private holdouts are stored outside this repository or in future AgentOS Verifier storage.

See `docs/evaluation-protocol.md`, `docs/failure-taxonomy.md`, and `evals/schemas/`.

## AgentOS relationship

This repository is prepared as a governed handoff unit for future Liu AgentOS work. `STATUS.md`, manifests, lifecycle rules, schemas, and validation commands let a fresh Agent discover the formal baseline and mutation boundaries without conversation history.

No AgentOS runtime, private Verifier store, or automatic multi-model runner is implemented here. Standardization is project governance, not a new Skill feature.

## Repository map

- `SKILL.md` — canonical runtime entry.
- `STATUS.md` — current human-readable state.
- `AGENTS.md` — read order, frozen scope, mutation limits, and verification.
- `project/` — baseline and Candidate state manifests.
- `docs/` — design history, lifecycle, evaluation, and failure classification.
- `tests/` — public development, regression, and diagnostic evidence.
- `evals/` — schemas, public run records, and machine-readable results.
- `scripts/` — zero-dependency repository checks.

## License

Licensed under the [Apache License 2.0](LICENSE) (`Apache-2.0`).
