# AI Learning Assistant Standardization

Work: `AI Learning Standardization — AgentOS Readiness v0.1`

Date: `2026-09-05`

## Verdict

Verdict: `NEEDS_FIX`

Current baseline: Candidate 04

Baseline status: `FROZEN`

Baseline role: `CURRENT_BASELINE`

Canonical Skill: `SKILL.md`

Frozen source: `SKILL-v0.6-candidate-04-failure-aware-degradation.md`

Freeze commit: `164c4d9`

Baseline SHA-256: `c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa`

Current diagnostic: Candidate 05 — Learner Evidence Conflict

Candidate 05 outcome: `DIAGNOSTIC`

Critical unresolved findings: `0 P0`

AgentOS readiness: `NOT_READY`

The repository's structural and frozen-baseline checks pass. The overall verdict remains `NEEDS_FIX` because the external second-model run, hosted CI result, and final post-reconciliation fresh-Agent smoke test are still pending. Candidate 01/02 authoritative artifacts remain unavailable, but the absence is now explicitly recorded without invented rationale or tests. The exact original untracked Candidate 05 R0 bytes have been imported as immutable historical evidence.

No release tag was created.

## What changed

### Baseline and canonical state

- Recorded the actual clean starting state at `HEAD == origin/main == 164c4d99d06841001ede1d06e6335bc105c5c3bc`.
- Proved that the old root `SKILL.md` SHA (`c74f259f...`) differed from the frozen source SHA.
- Promoted the frozen Candidate 04 source to `SKILL.md` byte-for-byte.
- Added `project/baseline-manifest.json` with separate freeze commit, canonical Skill, frozen source, frozen SHA, Apache-2.0 license, and recorded evidence hashes.
- Verified every recorded Candidate 04 evidence file both in the working tree and against the freeze commit.

### Project and Agent governance

- Added `STATUS.md`, `AGENTS.md`, `project/project-state.yaml`, and `project/candidate-index.yaml`.
- Separated lifecycle status, project role, and `was_frozen` history.
- Added legal lifecycle states, terminal states, and the Candidate Promotion Gate.
- Defined read order, frozen scope, allowed mutations, forbidden actions, verification commands, and reporting rules.

### Candidate 05 test cleanup

- Kept Candidate 05 as `DIAGNOSTIC / CURRENT_DIAGNOSTIC` with `baseline_change_allowed: false` and no rule file.
- Preserved the reconstructed historical leakage note without falsely claiming it was the original, then imported the recovered Windows originals byte-for-byte as immutable `INVALID_TEST / PROMPT_LEAKAGE` evidence.
- Created neutral Executor cases and a separate Judge-only expectations file.
- Preserved all old ID mappings:
  - `C05-01` → `REG-C04-EVIDENCE-01`
  - `C05-02` → `REG-C04-EVIDENCE-02`
  - `C05-03` → `REG-C04-TRANSFER-01`
  - `C05-04` → `C05-DIAG-CONFLICT-01`
  - `C05-05` → `REG-C04-SCOPE-01`
- Added exact manual Kimi packets and an import protocol.

### Evaluation and validation infrastructure

- Added the evaluation protocol and failure taxonomy.
- Added JSON schemas, run directories, raw-output storage, run-local judgments, and global JSONL results.
- Added zero-dependency scripts to validate repository state, verify frozen evidence, and warn on prompt leakage.
- Added GitHub Actions validation.
- Added checks for required files, legal states, baseline/diagnostic boundaries, duplicate case IDs, JSONL integrity, run-local/global consistency, raw-output existence, manifest consistency, absolute local paths, private holdout paths, and Apache-2.0 references.

### Documentation and hygiene

- Synchronized English and Chinese READMEs to v0.6 / Candidate 04 / Candidate 05 diagnostic state.
- Rewrote the evolution log around reasons and decision boundaries rather than copying test tables.
- Added `CONTRIBUTING.md`, `SECURITY.md`, `.gitattributes`, and `.editorconfig`.
- Extended `.gitignore` for repository-external private evaluation material and common local artifacts.
- Did not replace or modify the Apache-2.0 `LICENSE`.

### Phase 2 acceptance and Phase 3A preparation

- Phase 2 recorded `47 PASS / 3 FAIL / 9 PENDING`, with `0 P0`.
- A final Git-tree and reachable-history search found no authoritative Candidate 01/02 source or test artifacts; `project/history-provenance-gaps.yaml` now records the explicit boundary without reconstructing history.
- Prepared separated Kimi Executor and Judge packets under `evals/packages/candidate-05-kimi-clean-r0/`; no Kimi output is claimed.
- Strengthened run/result provenance for model identity, exposed session/context identifiers, fresh-context evidence, Executor/Judge separation, and raw input/output paths.
- Prepared `audit/final-agentos-smoke-protocol.md`; it is marked `NOT_EXECUTED` and is not final smoke evidence.

## Candidate 05 Clean R0 status

Run: `c05-r0-clean-20260905-codex-work`

- Five cases ran in five separate fresh Agent contexts.
- Each Executor received the frozen Skill and one clean case only.
- Complete raw outputs were preserved.
- A separate fresh Judge that did not produce the outputs recorded independent judgments.
- Result: 5/5 `PASS`, including `C05-DIAG-CONFLICT-01`.
- Exact Executor/Judge model identifiers were not exposed by the environment.
- This is one Codex Work environment, not two independent model environments.
- Kimi was not callable from this Work container; its real run is awaiting manual execution and import.

Candidate 05 therefore remains `DIAGNOSTIC`. The single available passing environment does not yet justify `CLOSED_NO_CHANGE`, and no Candidate 05 proposal or rule file was created.

## AgentOS smoke test

A fresh Agent with no prior conversation correctly derived from the repository:

- Candidate 04 / `FROZEN` / `CURRENT_BASELINE`;
- Candidate 05 / `DIAGNOSTIC` / not formal behavior;
- the current next action;
- the frozen scope;
- all four validation commands;
- the missing original R0, exact model IDs, and second-model evidence limitations.

It then produced a compliant Clean R0 execution plan without changing the formal Skill or any file. Smoke-test result: `PASS` for repository discovery and planning in the available Codex Work environment.

That smoke test predates the Candidate 05 provenance reconciliation and final remediation preparation, and it preserves a summary rather than raw session evidence. A final rerun against the intended release commit remains pending under `audit/final-agentos-smoke-protocol.md`; no final smoke result is claimed.

## Validation results

| Command | Result |
| --- | --- |
| `python scripts/validate_repo.py` | `PASS` — structural state, Candidate rules, JSONL/run consistency, paths, and Apache-2.0 checks passed. |
| `python scripts/verify_baseline.py` | `PASS` — canonical Skill, frozen source, freeze commit, and every recorded evidence SHA passed. |
| `python scripts/lint_eval_prompts.py` | `PASS` — no suspicious leakage phrase in the canonical Candidate 05 Executor inputs. |
| `python -m py_compile scripts/validate_repo.py scripts/verify_baseline.py scripts/lint_eval_prompts.py` | `PASS` |
| `python -m json.tool` on both schemas and the run manifest | `PASS` |
| Skill Creator `quick_validate.py .` | `PASS` — `Skill is valid!` |
| `git diff --check` | `PASS` |

GitHub-hosted CI was configured but was not claimed as observed before the final branch push.

## Repository hygiene and security review

Checked current files and every reachable Git blob for:

- PEM private-key headers;
- AWS access-key identifiers;
- GitHub token prefixes;
- OpenAI-style secret keys;
- obvious long credential assignments to API key, client secret, access token, or password fields.

Result: `0` matches in current content and `0` matches in reachable Git history.

Also checked:

- unnecessary Windows absolute paths: none in repository text;
- in-repository private holdout paths: none;
- license content/reference: Apache-2.0;
- Git author email exposure.

Author emails visible in history:

- `2251718565@qq.com`
- `codex@local`
- `codex@openai.com`

No history rewrite was performed because no real secret was found and no approval for history rewriting was given.

Not checked or not available:

- full entropy-based secret scanning;
- provider-side credential validity or revocation state;
- GitHub branch protection, repository visibility, or Advanced Security settings;
- a completed hosted CI run;
- security of a future AgentOS runtime or external Verifier store.

## Unresolved findings

### P0

None.

### P1

1. **C05-EVAL-001 — Second independent model pending.** Run the separated Kimi package and import real raw inputs, outputs, provenance, and independently produced judgments.
2. **CI-OBS-001 — Hosted CI pending.** The current branch has not been pushed and no hosted workflow result exists for the intended final commit.
3. **AGENTOS-SMOKE-002 — Final smoke pending.** Run the prepared protocol in a demonstrably fresh context against the intended final commit and preserve raw input/output plus context provenance.

### P2

1. **MODEL-META-001 — Exact Codex Work model IDs not exposed.** The real environment is recorded without inventing identifiers.
2. **EVAL-PROV-001 — Existing Work session identifiers unavailable.** The run records role separation and fresh contexts, but the platform exposed no session IDs or exports that independently prove those assertions.
3. **HISTORY-PROV-001 — Candidate 01/02 authoritative history unavailable.** The gap is explicitly recorded in `project/history-provenance-gaps.yaml`; the owner may later provide authoritative evidence.
4. **SECURITY-SCAN-LIMIT-001 — Secret review is pattern-based.** Full entropy scanning and provider-side credential validation were not performed.
5. **PRIVACY-001 — Author emails are public in history.** This is disclosed; no rewrite was performed.

## Frozen-file integrity

- Frozen Candidate 04 source changed: `NO`.
- Frozen Candidate 04 evidence changed: `NO`.
- Canonical `SKILL.md` changed: `YES`, solely by byte-for-byte promotion from the frozen source.
- Candidate 04 behavior changed: `NO`.
- Candidate 05 rule file created: `NO`.
- Candidate 06 created: `NO`.
- Apache-2.0 license changed: `NO`.

## Git provenance before Phase 3A

1. `6f617b0` — `chore: establish frozen baseline and project state`
2. `9f4b7ce` — `test: clean Candidate 05 diagnostics and formalize candidate lifecycle`
3. `2885cec` — `docs: sync v0.6 documentation and open-source governance`
4. `0e645dc` — `feat: add machine-readable evaluation records and repository validation`
5. `3b7fdf8` — `test: record Candidate 05 clean R0 and AgentOS smoke evidence`
6. `9478b02` — `docs: record AgentOS readiness standardization outcome`
7. `e56386f` — `test: preserve original Candidate 05 R0 provenance`

Phase 3A is recorded by the commit containing this report update with message `chore: prepare final acceptance remediation`; its exact hash is reported after commit creation because a commit cannot embed its own stable hash.

## Release decision

Do not create `v0.6.0-agent-ready` yet. The intended release commit is not accepted while P1 evidence gaps remain. Candidate 04 remains the frozen formal baseline, and future repository `HEAD` is not required to equal its freeze provenance commit.
