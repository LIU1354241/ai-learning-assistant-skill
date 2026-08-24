# AI Learning Assistant Skill

`ai-learning-assistant-skill` is a stable behavior contract for a long-term AI learning assistant. It is designed to help a learner understand their current stage, choose priorities, see why knowledge matters, build judgment, and collaborate responsibly with AI tools.

The project exists because a useful learning assistant should do more than answer questions. A correct answer can solve the current prompt while leaving the learner unsure what to study, why it matters, or how to decide next time. This Skill turns those recurring needs into a small set of executable Agent rules.

## What it learns from i-have-adhd

The project learns a design idea from `i-have-adhd`: start from real human friction and behavioral patterns, then translate them into concrete guidance an AI Agent can follow. It does not copy that project's content, assume that every learner has ADHD, or reproduce its implementation. The reusable lesson is the path from **human need → behavioral rule → boundary → testable response**.

## Relationship to OpenViking, Memory, and Agents

- **The Skill** defines how the assistant should reason and respond.
- **The Agent**—such as Codex, Kimi Code, or another executor—performs the task under those rules.
- **Workflow** coordinates task steps and checks without redefining learner data.
- **Memory** may provide durable learner context, but this Skill does not store data. It only says which stable facts may be worth remembering with user consent.
- **OpenViking** can be explored as one possible context and memory infrastructure. This repository is independent from it and has no required integration.

The design keeps these responsibilities separate: behavior belongs to the Skill, action belongs to the Agent, sequencing belongs to Workflow, and persistence belongs to an explicitly governed Memory system.

## Repository contents

- `SKILL.md` — concise instructions read by an AI Agent.
- `docs/design-notes.md` — the reasoning from learner pain points to Skill behavior.
- `docs/evolution-log.md` — version history and design changes.
- `examples/usage-examples.md` — sample prompts and expected behavior.

## v0.3 Stable

- Learner matching now uses identity, goal, level, and stage.
- Responses use a lightweight default structure plus triggered modules instead of a fixed long format.
- Learning behavior focuses on building judgment, not only delivering knowledge.
- Skill, Memory, and Workflow remain separate responsibilities.

Version 0.3 keeps eight core rules, two modes, explicit exceptions, a self-check, and a narrow memory policy. It adds no scripts, external service dependency, automatic memory, or connection to other projects.
