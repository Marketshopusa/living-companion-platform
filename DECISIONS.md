# Decisions

Irreversible architecture, cost, privacy, security, legal/licensing, and product choices require a human-approved ADR. **Nothing below is silently decided.**

## Locked in Gate 0

| ID | Decision |
| --- | --- |
| [ADR-000](docs/adr/000-no-stack-lock.md) | Gate 0 does not lock language, 3D runtime, database, auth, realtime transport, or paid providers. |

## Open — require human approval

1. Language/runtime for Core/backend and clients (monorepo vs polyglot).
2. Real-time 3D engine (Unity, Unreal, Godot, custom, WebGPU, other).
3. Canonical database and event bus.
4. Authentication standard (e.g. OIDC) and MFA timeline.
5. Realtime transport (WebSocket, WebRTC, other).
6. Local-first vs cloud LLM / STT / TTS for development after stubs.
7. Age verification method and adult-content legal policy (required by spec Point 49; **not implemented in Gate 0**).
8. Whether accounts/auth are pulled before full clients (recommended for isolation tests) despite V3 listing Accounts under Production Systems.
9. Point 02 “all clients now” vs V3 platforms-later: contract simulators at Gate 1 vs real devices later.
10. Asset creation: in-house vs licensed; placeholder-vs-production policy.
11. Telegram bot ownership and data-processing terms.
12. Retention periods, export format, and whether user data is ever used for training (default recommendation: **never train on user data** unless approved).

## Contradictions recorded (not resolved here)

- Strict 70-point order vs V3 AE expanded sequence — **V3 wins** for embodiment/reference/world/action; 70-point text remains the functional checklist.
- Point 02 multi-client acceptance vs clients not existing until later — see open item 9.
- Accounts at Point 39 / V3 production-systems vs need for tenant isolation from Gate 1 — see open item 8.
- Hyperrealistic persistent 3D vs $0 development budget — production body is blocked until tools, artists, and licenses are approved.
