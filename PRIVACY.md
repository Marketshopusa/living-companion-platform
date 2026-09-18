# Privacy

Baseline from [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md) sections G, Points 05/42/48/53. Not a completed compliance program.

**User-facing draft pack:** [docs/legal/](docs/legal/README.md) (Privacy Policy, AI disclosure, DSAR, cookies, vendors). Status: `DRAFT — PENDING HUMAN LEGAL COUNSEL` ([ADR-002](docs/adr/002-legal-policy-pack-draft.md)).

## Data classes

`PUBLIC / OPERATIONAL / PERSONAL / SENSITIVE / SECRET`

## Principles

- Minimization: collect only what a gate requires.
- Deny-by-default for microphone, camera, screen, and location.
- Vision and voice retention are configurable; prefer ephemeral processing.
- Users must be able to control memory, voice, camera, screen, data, and history (when those features exist).
- Deletion and export hooks are required by the spec; retention periods are **not** decided (see [DECISIONS.md](DECISIONS.md)).
- Journal / inner life of the Companion must never be presented as a user fact.
- Explicit clothing/memory preferences vs inferred: inferred has lower confidence and must be correctable.
- Analytics (when added) must be consent-gated and separated from conversation content.
- Default recommendation until approved otherwise: **do not train models on user data**.
- AI-mediated features require the [AI disclosure](docs/legal/ai-disclosure.md) before first interaction when a client ships.

## Isolation tests (Gate 1+)

Gate 1: Tenant B cannot read Tenant A Companion identity. Companion A fields do not appear on Companion B. User Model / memory isolation remains later.

## AI providers

When adapters exist, vendor processing terms must be reviewed using [docs/legal/vendor-and-subprocessors.md](docs/legal/vendor-and-subprocessors.md). Local stubs are the Gate 0 / early-dev default ($0).

## Gate 1

Identity documents classify fictional Companion config as `OPERATIONAL` and `owner_user_id` / `tenant_id` as `PERSONAL`. No `SECRET` in fixtures. Retention/hard-delete is not implemented (`archived` status only). No training data collection.
