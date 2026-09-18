# Living Companion Platform

Persistent, embodied AI companions with identity, personality, memory, relationships, emotions, voice, body, wardrobe, environments, objects, actions, routines, bounded autonomy, and cross-device continuity.

This is **not** a chatbot, a chatbot with an avatar, a mobile-only app, a static 3D character, or a library of scripted clips.

## Governing specification

[MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md) is the product and engineering source of truth. The **V3 Consolidated Product Directive** in that file is authoritative when earlier sections conflict on sequencing, embodiment, or Reference-first development.

Do not edit `MASTER_BUILD_SPECIFICATION.md` to “simplify” requirements.

## Current status

**Gate 1 (Companion Core identity contracts)** is implemented: versioned JSON Schema identity in Companion Core, local in-memory/file persistence, simulated clients, tenant isolation tests. No UI, 3D, or paid providers. See [BUILD_PLAN.md](BUILD_PLAN.md).

**Legal / trust pack (draft):** [docs/legal/](docs/legal/README.md) — privacy, terms, acceptable use, AI disclosure, age/safety, anti-fraud. Pending human legal counsel ([ADR-002](docs/adr/002-legal-policy-pack-draft.md)). Not a Points 47–49 PASS.

See [BUILD_PLAN.md](BUILD_PLAN.md) for gate status.

## Repository layout

```text
apps/             # Future clients: iOS, Android, Windows, macOS, Web, Telegram
core/             # Companion Core — identity contracts (Gate 1); other domains later
backend/          # Local identity persistence port (memory/file); no cloud DB
ai/               # Provider adapters and AI configuration — not started
integrations/     # External channel adapters — not started
cms/              # Character / AI / asset CMS — not started
assets/           # Versioned licensed assets — not started
infrastructure/   # Deploy/env definitions — not started
scripts/          # Repo checks and tooling
tests/            # Gate 1 identity tests
docs/adr/         # Architecture decision records
docs/evidence/    # Gate evidence
docs/evaluations/ # AI evaluation artifacts
docs/runbooks/    # Operations notes
```

## Environments

Development starts at **$0** and **local-only**. See [docs/runbooks/environments.md](docs/runbooks/environments.md).

## Documentation

| Document | Role |
| --- | --- |
| [PRODUCT_SPEC.md](PRODUCT_SPEC.md) | Pointer to the master spec (does not fork requirements) |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Provisional architecture (not a silent lock) |
| [DECISIONS.md](DECISIONS.md) | Open decisions requiring human approval |
| [ACCEPTANCE_TESTS.md](ACCEPTANCE_TESTS.md) | Gate procedures |
| [SECURITY.md](SECURITY.md) | Security baseline |
| [PRIVACY.md](PRIVACY.md) | Privacy baseline |
| [docs/legal/](docs/legal/README.md) | Draft user-facing legal / AI / anti-fraud policies |
| [AGENTS.md](AGENTS.md) | Multi-agent working rules |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |

## Rules that never slip

- Canonical Companion state lives in Companion Core / backend, not in one client.
- LLM output is untrusted. It cannot execute privileged operations.
- `NOT_STARTED → IN_PROGRESS → TESTING → PASS`. Failure is `FAIL → FIX → RETEST → PASS`.
- Build one Reference Companion (and Reference Home / Wardrobe / Life) before scaling to 15 characters.
