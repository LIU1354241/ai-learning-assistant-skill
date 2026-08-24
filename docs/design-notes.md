# Design Notes

## Design goal

Turn recurring learning problems into a small set of instructions an AI Agent can execute consistently. The first version favors clear boundaries over feature count.

## From pain points to Agent behavior

| User pain point | Design response | Expected Agent behavior |
| --- | --- | --- |
| “I do not know where I am in the learning process.” | Understand the user before answering. | Infer or ask about level, goal, and stage before choosing depth. |
| “Everything looks important.” | Make priority explicit. | Separate learn now, learn later, and not needed yet. |
| “I can remember terms but not why they matter.” | Explain need and value. | Connect a concept to the problem it solves and when it becomes useful. |
| “AI gives me answers, but I cannot decide alone.” | Optimize for capability. | Show reasoning and end with a small practice or judgment task. |
| “Explanations are too shallow or too advanced.” | Adapt depth. | Change terminology, examples, pace, and detail to fit the learner. |
| “AI tools make changes I cannot understand.” | Require collaboration transparency. | Report what was done, why, and what problem it solved. |
| “AI may confidently invent information.” | Put truth first and self-check. | Verify when possible; otherwise label uncertainty and never fabricate support. |

## Why two modes

Learning and execution have different success conditions. Learning Mode succeeds when the user understands and can make a better next judgment. Execution Mode succeeds when the requested outcome is produced within scope and the work remains understandable. Keeping only these two modes avoids a large taxonomy while covering the main interaction patterns.

## Why exceptions are explicit

The default teaching behavior is not always appropriate. An exam question may need a fast answer; an urgent bug may need containment before explanation; deep research needs more evidence; missing information requires a refusal to guess. Exceptions prevent a good default from becoming a rigid rule. They change response speed or depth, not the truthfulness requirement.

## Memory boundary

The Skill defines behavior, not storage. It may recognize stable learning goals, stage, active projects, durable preferences, recurring blockers, and regular tools as potentially useful context. Whether anything is stored must be decided by the user and the host memory system.

## Non-goals for v0.1

- Diagnose the user or model a personality profile.
- Build a curriculum engine or scoring system.
- Save personal data automatically.
- Require OpenViking, Codex, Kimi Code, or any specific Agent runtime.
- Add rules for every possible learning situation.
