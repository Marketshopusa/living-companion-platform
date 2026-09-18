# ADR-002 — Legal / trust policy pack (draft framework)

- **ID:** 002
- **Title:** Establish draft legal and trust policy pack without locking counsel decisions
- **Status:** proposed
- **Date:** 2026-09-18
- **Deciders:** Primary Engineering Agent proposal; **human legal counsel + product owner required** to accept

## Context

After Gate 1 (Companion Core identity contracts), the repository still lacked user-facing Privacy Policy, Terms, Acceptable Use, AI disclosure, age/safety, and anti-fraud notices. Root [PRIVACY.md](../../PRIVACY.md) and [SECURITY.md](../../SECURITY.md) are engineering baselines only. Master-spec Points 47–49 and Section A require privacy, security, age/safety, and untrusted-LLM posture from architecture start. [DECISIONS.md](../../DECISIONS.md) still lists open legal items (age method, retention, Telegram terms, training on user data, jurisdiction).

The operator asked to structure policies now—AI disclosure, privacy, and protections against fraud/lawsuits—while other stack decisions remain open. No prior app privacy text was found in-repo to import.

## Decision (proposed)

1. Add `docs/legal/` as the canonical **draft** location for user-facing and operator-facing policies.
2. Keep every document bannered `DRAFT — PENDING HUMAN LEGAL COUNSEL` until a human accepts this ADR (or a successor) and fills placeholders (`[OPERATOR_LEGAL_NAME]`, `[JURISDICTION]`, `[AGE_GATE_METHOD]`, `[RETENTION_DEFAULT]`, contacts, etc.).
3. Require AI disclosure to be surfaced before first AI interaction when any client ships.
4. Default posture remains: **do not train foundation models on user data** unless a later ADR changes it.
5. Do **not** mark Points 47 / 48 / 49 PASS merely because drafts exist; implementation gates remain separate.
6. Do **not** invent jurisdiction, age-verification vendor, or retention periods in this ADR.

## Consequences

Positive:

- Clear place for privacy, terms, AUP, AI notice, age/safety, anti-fraud, DSAR, cookies, vendor checklist.
- Reduces silent omission of AI-generated-content notices and fraud warnings.
- Engineers and agents have linkable policy text without forking into apps prematurely.

Negative / follow-up:

- Drafts are **not** legal advice and must not be published as final without counsel.
- Placeholders must be completed before production launch.
- Open DECISIONS items 7, 11, 12 (and jurisdiction) remain blocking for production adult features, Telegram, and hard retention/delete SLAs.

## Alternatives considered

- Wait until Points 47–49 implementation — rejected: disclosure and AUP scaffolding are cheap governance and reduce later scramble.
- Silently fill US/EU jurisdiction and age vendor — rejected: violates “no silent legal lock” rule.
- Copy a third-party app’s policies verbatim — rejected: no in-repo source text; licensing/fit risk.

## Spec references

- Section A (ADR for irreversible privacy/security/legal choices; untrusted LLM; no minors sexualization)
- Points 47 (security), 48 (privacy), 49 (age and safety)
- Point 53 (consent-gated analytics)
- [AGENTS.md](../../AGENTS.md) stop conditions for legal/privacy locks
- [DECISIONS.md](../../DECISIONS.md) open items 7, 11, 12
