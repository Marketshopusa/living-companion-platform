# Decisions

Irreversible architecture, cost, privacy, security, legal/licensing, and product choices require a human-approved ADR. **Nothing below is silently decided.**

## Locked in Gate 0

| ID | Decision |
| --- | --- |
| [ADR-000](docs/adr/000-no-stack-lock.md) | Gate 0 does not lock language, 3D runtime, database, auth, realtime transport, or paid providers. |

## Locked in Gate 1

| ID | Decision |
| --- | --- |
| [ADR-001](docs/adr/001-core-language-for-identity-contracts.md) | Gate 1 Core identity runtime: Python 3.x, pytest, JSON Schema, stdlib-first, in-memory + optional JSON file. Does **not** lock client languages, 3D, AI, database, cloud, realtime, or auth provider. |

## Proposed (not accepted)

| ID | Decision |
| --- | --- |
| [ADR-002](docs/adr/002-legal-policy-pack-draft.md) | Draft legal/trust pack under `docs/legal/` (privacy, terms, AUP, AI disclosure, age/safety, anti-fraud, DSAR, cookies, vendors). **Does not** lock jurisdiction, age method, retention, Telegram terms, or training-on-user-data. Requires human legal counsel before publish. |

## Open — require human approval

1. Language/runtime for **clients** and any Core beyond Gate 1 identity (monorepo vs polyglot). Gate 1 Core identity runtime is ADR-001 only.
2. Real-time 3D engine (Unity, Unreal, Godot, custom, WebGPU, other).
3. Canonical database and event bus.
4. Authentication standard (e.g. OIDC) and MFA timeline. Gate 1 isolation uses **simulated principals**, not production accounts.
5. Realtime transport (WebSocket, WebRTC, other).
6. Local-first vs cloud LLM / STT / TTS for development after stubs.
7. Age verification method and adult-content legal policy (required by spec Point 49; **not implemented in Gate 0 or Gate 1**). Draft posture only: [docs/legal/content-safety-and-age.md](docs/legal/content-safety-and-age.md).
8. Whether accounts/auth are pulled before full clients (recommended for isolation tests) despite V3 listing Accounts under Production Systems. **Gate 1: simulated principals are sufficient for cross-tenant deny tests.**
9. Point 02 “all clients now” vs V3 platforms-later: **Gate 1 uses contract simulators**; real devices later.
10. Asset creation: in-house vs licensed; placeholder-vs-production policy.
11. Telegram bot ownership and data-processing terms. Draft checklist: [docs/legal/vendor-and-subprocessors.md](docs/legal/vendor-and-subprocessors.md).
12. Retention periods, export format, and whether user data is ever used for training (default recommendation: **never train on user data** unless approved). Gate 1 `archived` is a status only. Draft DSAR/privacy: [docs/legal/](docs/legal/README.md).
13. **Governing law / venue** (`[JURISDICTION]`) and operator legal entity / contact emails for publishing Terms and Privacy.
14. Human acceptance of [ADR-002](docs/adr/002-legal-policy-pack-draft.md) and counsel review before any production UI links these policies as final.

## Contradictions recorded (not resolved here)

- Strict 70-point order vs V3 AE expanded sequence — **V3 wins** for embodiment/reference/world/action; 70-point text remains the functional checklist.
- Point 02 multi-client acceptance vs clients not existing until later — see open item 9.
- Accounts at Point 39 / V3 production-systems vs need for tenant isolation from Gate 1 — see open item 8.
- Hyperrealistic persistent 3D vs $0 development budget — production body is blocked until tools, artists, and licenses are approved.
