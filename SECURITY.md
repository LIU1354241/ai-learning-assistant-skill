# Security Policy

## Reporting a vulnerability

Do not disclose secrets, private learner data, private holdout prompts, or exploit details in a public issue. Use the repository owner's private security-reporting channel. Include the affected file or commit, impact, reproduction conditions, and a minimal remediation direction.

## Scope

Security-sensitive findings include:

- exposed tokens, credentials, cookies, or private keys;
- unauthorized learner-memory access or mutation;
- prompt or evaluation data that exposes a real private holdout;
- unsafe tool, permission, or execution boundaries;
- supply-chain changes to CI or executable scripts.

Behavioral quality disagreements without a security impact belong in normal Candidate evaluation.

## Handling

Do not rewrite history or rotate credentials based only on a suspected pattern match. Verify the finding first. If a real secret is confirmed, stop publication, rotate or revoke it through the owning service, then obtain explicit owner approval before any history rewrite.
