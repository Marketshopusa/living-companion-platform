# Security

Baseline from [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md) sections A, G, Points 39/47/49. This is policy for the repository, not a claim that controls are implemented.

## Non-negotiables

- No secrets in source control.
- LLM output is untrusted data. It must not execute shell, arbitrary code, SQL, payments, account changes, destructive operations, privileged APIs, or unrestricted tools.
- Canonical authorization is server-side. Clients cannot grant themselves entitlements or memory access.
- Tenant isolation: User A memory, media, relationship, and sessions must never be readable as User B.
- Companion isolation: memories of one Companion must not mix with another.

## Threat model (spec)

Account takeover; broken authorization; cross-user memory leakage; prompt injection; malicious tool input; webhook replay/spoofing; insecure local storage; secret leakage; supply-chain compromise; media access abuse; entitlement abuse; denial of service.

## Required controls (to be implemented in later gates)

- Authentication and session/device revocation
- Authorization on every memory, companion, and media read
- Rate limiting
- Webhook signature verification and idempotency (Telegram and billing, when those exist)
- Structured audit events without dumping private content
- Abuse reporting and blocking
- Age gating architecture; no minors or minor-like sexualization; no unauthorized real-person voice/face cloning
- Supply-chain: lockfiles and reviewed dependencies once a stack is chosen

## Gate 0 controls that exist now

- `.gitignore` for secrets and key material
- `.env.example` with no credentials
- CI baseline check rejects tracked secret-like filenames
- No product APIs yet (attack surface is documentation + git only)

## Incident posture

Do not log secrets or unrestricted conversation content. Future diagnostics: ERROR / WARNING / INFO / PERFORMANCE / SECURITY with redaction (Point 57).
