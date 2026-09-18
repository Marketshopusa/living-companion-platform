# Security

Baseline from [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md) sections A, G, Points 39/47/49. This is policy for the repository, not a claim that controls are implemented.

**Trust & abuse draft pack:** [docs/legal/anti-fraud-and-trust.md](docs/legal/anti-fraud-and-trust.md), [acceptable-use-policy.md](docs/legal/acceptable-use-policy.md), [content-safety-and-age.md](docs/legal/content-safety-and-age.md). Status: `DRAFT — PENDING HUMAN LEGAL COUNSEL` ([ADR-002](docs/adr/002-legal-policy-pack-draft.md)).

## Non-negotiables

- No secrets in source control.
- LLM output is untrusted data. It must not execute shell, arbitrary code, SQL, payments, account changes, destructive operations, privileged APIs, or unrestricted tools.
- Canonical authorization is server-side. Clients cannot grant themselves entitlements or memory access.
- Tenant isolation: User A memory, media, relationship, and sessions must never be readable as User B.
- Companion isolation: memories of one Companion must not mix with another.
- Official channels never solicit passwords, seed phrases, OTP codes, or off-platform payments via Companion chat.

## Threat model (spec)

Account takeover; broken authorization; cross-user memory leakage; prompt injection; malicious tool input; webhook replay/spoofing; insecure local storage; secret leakage; supply-chain compromise; media access abuse; entitlement abuse; denial of service; social-engineering / romance scams mediated by AI output; unauthorized real-person voice/face cloning; phishing sites impersonating the product.

## Required controls (to be implemented in later gates)

- Authentication and session/device revocation
- Authorization on every memory, companion, and media read
- Rate limiting
- Webhook signature verification and idempotency (Telegram and billing, when those exist)
- Structured audit events without dumping private content
- Abuse reporting and blocking
- Age gating architecture; no minors or minor-like sexualization; no unauthorized real-person voice/face cloning
- AI disclosure and synthetic-media labeling where feasible
- Supply-chain: lockfiles and reviewed dependencies once a stack is chosen
- Fraud desk process and user-facing warnings ([docs/legal/anti-fraud-and-trust.md](docs/legal/anti-fraud-and-trust.md))

## Gate 1 controls that exist now

- JSON Schema validation before persist (`additionalProperties: false`)
- Server-side `IdentityAccessPolicy`; cross-tenant reads are `forbidden`
- No LLM identity mutation path (unstructured payloads rejected)
- Companion documents isolated by `companion_id`
- Simulated principals only (not OIDC)

## Gate 0 controls that exist now

- `.gitignore` for secrets and key material
- `.env.example` with no credentials
- CI baseline check rejects tracked secret-like filenames
- No product APIs yet beyond in-process identity commands (no HTTP surface)

## Incident posture

Do not log secrets or unrestricted conversation content. Future diagnostics: ERROR / WARNING / INFO / PERFORMANCE / SECURITY with redaction (Point 57). Suspected fraud or account takeover: preserve minimal forensic metadata and contact `[CONTACT_SAFETY]` / `[CONTACT_LEGAL]` once those placeholders are filled in the legal pack.
