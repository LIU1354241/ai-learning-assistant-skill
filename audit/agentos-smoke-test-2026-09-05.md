# AgentOS Fresh-Context Smoke Test — 2026-09-05

## Protocol

A fresh Agent context with no prior conversation was asked to inspect the repository without modifying files and report:

- current formal baseline;
- baseline status and role;
- current diagnostic;
- whether Candidate 05 is baseline behavior;
- next action;
- frozen scope;
- exact validation commands;
- any repository-derived confidence limitation.

It was then asked to create a Candidate 05 Clean R0 execution plan without modifying the formal Skill or repository.

## First response

The fresh Agent correctly reported:

- Candidate 04 as the formal baseline;
- `FROZEN / CURRENT_BASELINE`;
- canonical `SKILL.md`, frozen source, freeze commit, and exact SHA-256;
- Candidate 05 — Learner Evidence Conflict as `DIAGNOSTIC / CURRENT_DIAGNOSTIC`;
- Candidate 05 is not accepted, validated, or baseline behavior;
- the next action is Clean R0 evaluation and finding classification;
- Candidate 04 source, behavior, canonical byte identity, and manifest-recorded evidence are frozen;
- Candidate 06 and direct Candidate 05 promotion are forbidden;
- the exact four validation commands from `AGENTS.md`.

It also independently identified the missing original Windows R0 bytes, unavailable exact model IDs, missing second-model run, and then-unrecorded independent verdict as limitations. It reported that no frozen file had changed.

Verdict: `PASS` for repository state discovery.

## Second response: execution plan

The same Agent produced a plan that:

1. verifies the frozen baseline and stops on mismatch;
2. separates Executor inputs from Judge-side material;
3. uses one fresh context per case and records real metadata;
4. preserves complete raw output without repair;
5. requires independent judgment and synchronized JSONL records;
6. classifies every non-pass before any Skill decision;
7. uses the manual Kimi protocol when direct access is unavailable and never invents a run;
8. stops on leakage, contamination, incomplete capture, missing metadata, or unavailable capability;
9. permits `CLOSED_NO_CHANGE` after sufficient passing independent runs, while allowing a Candidate 05 proposal only for a reproducible, independently judged `SKILL_RULE_GAP` that survives alternative-cause analysis.

It explicitly kept Candidate 04 untouched and did not claim that execution occurred.

Verdict: `PASS` for repository-derived Clean R0 planning.

## Limitation

This smoke test proves repository readability in one Codex Work Agent environment. It does not prove behavior in Kimi, another independent model, or a future AgentOS runtime.
