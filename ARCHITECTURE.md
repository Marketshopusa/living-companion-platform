# Architecture (provisional)

**Status:** Gate 1 identity contracts. This document describes intended architecture from [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md). It is **not** an irreversible platform lock. See [docs/adr/000-no-stack-lock.md](docs/adr/000-no-stack-lock.md), [docs/adr/001-core-language-for-identity-contracts.md](docs/adr/001-core-language-for-identity-contracts.md), and [DECISIONS.md](DECISIONS.md).

## Category

Living Companion Platform: persistent embodied companions. Clients do not own canonical identity, memory, relationship, emotion, outfit, room, or world state.

## System context

```text
iOS / Android / Windows / macOS / Web / Telegram  (not implemented)
        |  versioned contracts (JSON Schema v1 identity)
        v
Companion Core identity (canonical) — in-process + local file port
        |  AI gateway (untrusted model I/O) — not started
        v
LLM / embeddings / STT / TTS / vision / moderation adapters — not started
```

Agency path (mandatory for later privileged actions):

`LLM intent → structured action proposal → server validation → authorization → policy/safety → execution → result → state update`

Identity writes do **not** use that path. There is no LLM command type. Only `CreateCompanion`, `GetCompanion`, `UpdateCompanionConfiguration`, and `SetCompanionStatus` after schema + policy validation.

## Companion Core

Gate 1 implemented: canonical Companion identity (`companion_id`, tenant/owner boundary, declarative personality configuration, allowlisted preferences, lifecycle status, versioning). Contracts live under `core/contracts/identity/v1/`. Python (ADR-001) is the Gate 1 runtime adapter, not a duplicate identity model.

Intended later:

- **Mind:** structured personality engine, tenant-isolated user model, memory, reasoning/context budgets, relationship, blended emotion, safety, versioned AI configuration.
- **Body (canonical state + client runtime):** persistent visual identity, semantic animation, physical state, licensed voice identity.
- **Life:** room/scene, outfit, activities, routines, journal (never user-fact), future events, bounded goals.

## Canonical vs client-local

**Server-authoritative (Gate 1):** Companion identity documents in Core/backend repositories. Simulated clients share one Core; they do not persist a competing store.

**Server-authoritative (later):** memory, relationship, personality engine state, emotion, physical state, outfit, current room/scene/activity/action, world snapshot, user presence, future events, autonomous goals, safety, entitlements, AI configuration, devices/sessions, audit events.

**Client-ephemeral:** camera, LOD, input devices, partial transcripts, playback buffers, UI layout, FPS. On reconnect, server revision wins. No shipping clients yet.

## World & Life Engine

Not started. Identity schema v1 excludes room, outfit, world, and current state.

Intended later: date/time/timezone, location context, permissioned weather, lighting, ambient audio, rooms, objects, interaction points, physical/emotional state, outfit, presence, routines, events, goals, interruptions. Rooms are functional systems, not backgrounds.

## Action, navigation, objects, wardrobe

Not started. Intended: interruptible actions, navmesh, object interaction without forking Core, reference wardrobe before a large catalog.

## Reference-first

Do not scale to 10 female + 5 male companions until the Reference Companion + Reference Home + Reference Wardrobe + action/object/life stack PASSes as one system.

`REFERENCE → VALIDATE → ABSTRACT → TEMPLATE → VARIATIONS → SCALE`

## Cross-platform

Same Companion across iOS, Android, Windows, macOS, Web, Telegram. Telegram is a constrained adapter, not a second brain. Gate 1 uses simulated clients only.

## AI providers

Core must not import vendor SDKs into domain logic. Adapters live under `ai/` (not started). Development default: local stubs at $0.

## Security / privacy sketch

Tenant isolation (Gate 1 identity reads), authn/z later, rate limits, no secrets in source. See [SECURITY.md](SECURITY.md) and [PRIVACY.md](PRIVACY.md).

## Not decided here

3D engine, database, auth vendor, realtime transport, paid AI providers, client languages. ADR-001 locks **only** the Gate 1 Core identity runtime (Python 3.x, pytest, JSON Schema, memory/file persistence).
