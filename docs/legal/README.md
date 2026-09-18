# Legal and trust policy pack

**Status:** `DRAFT — PENDING HUMAN LEGAL COUNSEL`

This directory holds **user-facing and operator-facing** policy scaffolds for the Living Companion Platform. It does **not** claim GDPR/CCPA certification, counsel approval, or production readiness.

Engineering baselines remain:

- [PRIVACY.md](../../PRIVACY.md) — data-class and minimization rules for builders
- [SECURITY.md](../../SECURITY.md) — security non-negotiables for builders

## Why this pack exists

Gate 1 closed identity contracts only. Product surface (UI, accounts, voice, vision, billing) is not shipping yet. Still, the master spec (Points 47–49, Section A/G) requires privacy, security, age/safety, and AI-trust posture **from architecture start**. Structuring policies now reduces later legal and fraud risk without locking jurisdiction, retention numbers, or age-verification vendors (see [DECISIONS.md](../../DECISIONS.md)).

## Documents

| File | Purpose |
| --- | --- |
| [privacy-policy.md](privacy-policy.md) | Privacy notice (what we collect, rights, AI processing) |
| [terms-of-service.md](terms-of-service.md) | Terms of use, disclaimers, liability limits |
| [acceptable-use-policy.md](acceptable-use-policy.md) | Prohibited uses (fraud, crime, abuse, minors) |
| [ai-disclosure.md](ai-disclosure.md) | Clear notice that content/behavior is AI-generated / AI-mediated |
| [content-safety-and-age.md](content-safety-and-age.md) | Age gating, adult content, no-minors, likeness cloning |
| [anti-fraud-and-trust.md](anti-fraud-and-trust.md) | Impersonation, scams, deepfakes, social-engineering defenses |
| [data-subject-requests.md](data-subject-requests.md) | Access / export / delete / correct request process |
| [cookie-and-similar-technologies.md](cookie-and-similar-technologies.md) | Cookies / local storage / SDK notice (web later) |
| [vendor-and-subprocessors.md](vendor-and-subprocessors.md) | Subprocessor / AI-vendor review checklist |

## Placeholders (must be filled before publish)

Replace every token before presenting these as live policies:

| Token | Meaning |
| --- | --- |
| `[OPERATOR_LEGAL_NAME]` | Legal entity that operates the product |
| `[PRODUCT_NAME]` | Public product name |
| `[CONTACT_PRIVACY]` | Privacy contact email |
| `[CONTACT_LEGAL]` | Legal / abuse contact email |
| `[CONTACT_SAFETY]` | Safety / report abuse contact |
| `[JURISDICTION]` | Governing law / venue (human decision) |
| `[EFFECTIVE_DATE]` | Effective date when counsel approves |
| `[RETENTION_DEFAULT]` | Default retention period (open decision) |
| `[AGE_GATE_METHOD]` | Age verification method (open decision) |

## Rules for agents and engineers

1. Do **not** mark Points 47 / 48 / 49 as PASS because these drafts exist.
2. Do **not** remove the `DRAFT` banner or claim counsel approval.
3. Do **not** silently fill jurisdiction, retention, training-on-user-data, or age method — those need ADR + human sign-off.
4. When a UI ships, surface [ai-disclosure.md](ai-disclosure.md) before first AI interaction and keep it reachable from settings/footer.
5. Prefer linking these files over copying conflicting text into apps.

## Related ADR

[ADR-002](../adr/002-legal-policy-pack-draft.md) — proposed framework for this pack.
