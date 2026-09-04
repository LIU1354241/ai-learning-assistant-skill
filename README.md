# AI Learning Assistant Skill

**English** | [简体中文](README.zh-CN.md)

> A truth-first AI learning assistant skill for evidence-aware teaching, representation selection, learner-state handling, and reliable Agent execution.

`ai-learning-assistant-skill` is a behavioral contract for building long-term AI learning assistants.

The project focuses on a simple idea:

> **A useful learning assistant should not only answer correctly. It should also know what is verified, what is inferred, what the learner actually needs, and when an Agent should stop, continue, or ask for evidence.**

## Core Principles

- **Truth First** — never turn guesses, simplifications, or unverified information into facts.
- **Shortest Effective Answer** — answer the real question first and expand only when useful.
- **Evidence-Aware Learning** — learner capability is based on evidence, not labels or assumptions.
- **Question → Information Need → Representation** — choose diagrams, flows, tables, steps, or plain text based on what the user actually needs to understand.
- **Visual Truth** — diagrams must not invent nodes, relationships, states, or changes.
- **Agent Transparency** — execution should clearly separate what was done, what was verified, and what remains unverified.

## Project Status

This project is under active development.

Stable and experimental candidates are developed through behavioral testing, red-team cases, regression checks, and cross-model evaluation.

## License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.
