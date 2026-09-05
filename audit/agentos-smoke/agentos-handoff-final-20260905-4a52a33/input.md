This is a fresh AgentOS handoff smoke test.

Do not use or assume any prior conversation history.

The repository itself is the only authoritative project context.

Do not modify any files.
Do not commit.
Do not push.
Do not create a tag.

The current shell directory may not be the repository root.

First locate the accessible Git repository named:

ai-learning-assistant-skill

You may inspect the current workspace/filesystem only to locate the
repository root.

Do not use prior conversation history to determine project state.

Once located, cd into the repository root and run:

git branch --show-current
git rev-parse HEAD
git status --short

Expected checkpoint:

branch:
chore/ai-learning-agentos-readiness

HEAD:
4a52a333a83ed8ba41195c82eabc2e40b27db797

If:
- the repository cannot be located;
- the branch differs;
- the HEAD differs;

STOP and report the exact mismatch.

If the repository and checkpoint match, continue.

Read the repository according to its own Agent instructions and answer,
using repository evidence only:

1. What is the current formal behavioral baseline?
2. What is its lifecycle status and project role?
3. What is the current diagnostic Candidate?
4. Is Candidate 05 part of the formal baseline?
5. What is the current next action?
6. Which files or behavior are frozen and must not be modified?
7. What repository validation commands should an Agent run?
8. What is the current Candidate 05 evaluation outcome?
9. Is there any verified SKILL_RULE_GAP?
10. Is the repository currently READY for final release/tagging?

Then create a concise execution plan for:

Candidate 05 Clean R0

without modifying the formal Skill.

Important:

- Do not infer project facts from conversation history.
- Use repository files only after locating the repository.
- Distinguish verified facts from unavailable information.
- Do not modify Candidate 04.
- Do not promote Candidate 05.
- Do not execute the plan.

At the end also report:

repository_path:
branch:
HEAD:
working_tree_clean:
files_read:
validation_commands_found:
