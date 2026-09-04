# Baseline Audit — 2026-09-05

## Scope

This audit records the repository state before the AgentOS-readiness standardization began. All Phase 0 commands were run before creating `chore/ai-learning-agentos-readiness` and before editing tracked files.

## Phase 0 checkpoint

| Check | Recorded result |
| --- | --- |
| `git status --short` | Clean; no output. |
| `git branch --show-current` | `main` |
| `git rev-parse HEAD` | `164c4d99d06841001ede1d06e6335bc105c5c3bc` |
| `git rev-parse origin/main` | `164c4d99d06841001ede1d06e6335bc105c5c3bc` |
| `git cat-file -t 164c4d9` | `commit` |
| `git diff --check` | PASS; no output. |
| Remote | `origin` = `https://github.com/LIU1354241/ai-learning-assistant-skill.git` |

The ten-entry history at the checkpoint was:

```text
164c4d9 (HEAD -> main, origin/main, origin/HEAD) feat: freeze v0.6 Candidate 04 failure-aware degradation
7fae2a1 docs: add Chinese README
8c1c503 Revise README for clarity and project status
9c354a0 docs: add Apache 2.0 license
f75a406 feat: freeze v0.6 Candidate 03 question representation
afdf70f chore: ignore local skill test snapshots
10e08a2 feat: release AI Learning Assistant Skill v0.3 Stable
96e5644 Create v0.1 AI learning assistant skill
```

`git show --stat 164c4d9` confirmed that the freeze provenance commit added the Candidate 04 formal source, test record, R1/R2/R3 sources, and the Candidate 04 test evidence. It changed 16 files with 5,913 insertions.

## Required files at the checkpoint

| File | State | Size |
| --- | --- | ---: |
| `LICENSE` | Present | 11,355 bytes |
| `README.md` | Present | 1,597 bytes |
| `README.zh-CN.md` | Present | 2,712 bytes |
| `docs/design-notes.md` | Present | 2,723 bytes |
| `docs/evolution-log.md` | Present | 2,142 bytes |

The inspected `LICENSE` is the Apache License, Version 2.0. No license replacement is required or permitted by this standardization.

## Canonical Skill finding

Both requested Git snapshots were inspected:

- `git show HEAD:SKILL.md`
- `git show 164c4d9:SKILL.md`

They were identical because `HEAD` was the freeze commit, but the root `SKILL.md` remained the obsolete short runtime entry rather than the newly frozen Candidate 04 source.

Pre-promotion hashes:

| Artifact | SHA-256 |
| --- | --- |
| Root `SKILL.md` | `c74f259fdc160a9bb5813505635eabc35102c75cd23fe800705dfe5bb7753bf7` |
| Frozen Candidate 04 source | `c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa` |

`git diff --no-index --numstat SKILL.md SKILL-v0.6-candidate-04-failure-aware-degradation.md` recorded `1141` insertions and `58` deletions, and `cmp` returned non-zero. The root entry was therefore stale.

## Promotion

The frozen source was promoted byte-for-byte to `SKILL.md`. No Candidate 04 rule was edited or rewritten.

Post-promotion invariant:

```text
SHA256(SKILL.md)
= SHA256(SKILL-v0.6-candidate-04-failure-aware-degradation.md)
= c41bd7d50fdbecf4fc9b16aabd613f16f0fdc8bf5a01c7d3f32e2b4aeaac37fa
```

Exact tracked file changed by promotion: `SKILL.md` only. The frozen source and frozen evidence files were not changed.

## Candidate 05 starting-state limitation

The authoritative remote checkpoint did not contain `tests/candidate-05/`. The user's Windows repository was expected to contain untracked Candidate 05 files, but that local drive is not mounted in this Work environment. This clone did not delete or overwrite those local files. Their exact bytes were unavailable at the start of standardization and must not be represented as recovered verbatim evidence.
