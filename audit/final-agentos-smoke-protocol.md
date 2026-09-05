# Final AgentOS Fresh-Context Smoke Protocol

Status: `NOT_EXECUTED`

This protocol must be run against the intended final release commit after repository-local remediation and external evaluation evidence are complete. This file is preparation only and is not smoke-test evidence.

## Required isolation

- Use a genuinely fresh Agent context that has not read this project conversation or prior smoke output.
- Give the Agent only the repository at the inspected commit and the exact input below.
- Do not provide expected answers, `STANDARDIZATION-REPORT.md` conclusions, or prior Agent output outside what the repository itself contains.
- Do not claim freshness when the platform cannot establish it; record the limitation.
- The Agent must not modify the repository.

## Exact raw Agent input

```text
Inspect this repository without modifying any file. Based only on repository evidence, report:

1. the current formal behavioral baseline, lifecycle status, and project role;
2. the canonical runtime Skill, frozen source, freeze provenance commit, and SHA-256;
3. the current diagnostic and whether it is accepted or baseline behavior;
4. the next required action;
5. the frozen scope and forbidden mutations;
6. the exact repository validation commands;
7. the status of Candidate 05 Clean R0, including how many independent execution environments are actually complete;
8. the relationship between the original Windows R0, the reconstructed leaky note, and the active Clean R0;
9. all current release blockers and evidence limitations.

Then create a Candidate 05 Clean R0 execution plan without modifying the formal Skill or repository. Do not claim that any planned execution occurred.
```

## Evidence to preserve

Store a completed run under `audit/agentos-smoke/<run-id>/` with:

- `input.md`: the exact raw Agent input above;
- `output.md`: the complete unedited first Agent response;
- `metadata.yaml`: timestamp, inspected full commit hash, Agent provider/model, session/context identifier when exposed, freshness evidence, environment, and operator;
- any export or screenshot reference used to support fresh-context provenance.

The metadata must record `NOT_EXPOSED` plus an explanation when a provider does not expose an exact model or session identifier. It must never invent an identifier.

## Acceptance checks

The result passes only if the Agent derives the repository facts correctly, distinguishes all three Candidate 05 artifact roles, identifies the real remaining blockers, supplies the exact four validation commands, keeps Candidate 04 untouched, and does not claim unperformed work.

Afterward, independently compare the raw output with current repository state and record the verdict without editing the raw response.
