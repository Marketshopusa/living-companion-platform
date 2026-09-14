# Architecture (provisional)

**Status:** Gate 0 baseline. This document describes intended architecture from [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md). It is **not** an irreversible stack lock. See [docs/adr/000-no-stack-lock.md](docs/adr/000-no-stack-lock.md) and [DECISIONS.md](DECISIONS.md).

## Category

Living Companion Platform: persistent embodied companions. Clients do not own canonical identity, memory, relationship, emotion, outfit, room, or world state.

## System context

```text
iOS / Android / Windows / macOS / Web / Telegram
        |  versioned APIs, realtime, capability negotiation
        v
Companion Core (canonical) + World & Life Engine
        |  AI gateway (untrusted model I/O)
        v
LLM / embeddings / STT / TTS / vision / moderation adapters
```

Agency path (mandatory):

`LLM intent → structured action proposal → server validation → authorization → policy/safety → execution → result → state update`

## Companion Core

- **Mind:** identity, structured personality, tenant-isolated user model, memory (episodic / semantic / relational / preference / temporal), reasoning/context budgets, relationship (state machine + dimensions), blended emotion with decay, safety, versioned AI configuration.
- **Body (canonical state + client runtime):** persistent visual identity, semantic animation (intent in, approved graphs out), physical state, licensed voice identity.
- **Life:** room/scene, outfit, activities, routines, journal (never user-fact), future events, bounded goals.

## Canonical vs client-local

**Server-authoritative:** Companion identity, memory, relationship, personality, emotion, physical state, outfit, current room/scene/activity/action, world snapshot, user presence, future events, autonomous goals, safety, entitlements, AI configuration, devices/sessions, audit events.

**Client-ephemeral:** camera, LOD, input devices, partial transcripts, playback buffers, UI layout, FPS. On reconnect, server revision wins.

## World & Life Engine

Coordinates date/time/timezone, location context, permissioned weather, lighting, ambient audio, rooms, objects, interaction points, physical/emotional state, outfit, presence, routines, events, goals, interruptions. Rooms are functional systems (navmesh, objects, actions), not backgrounds.

## Action, navigation, objects, wardrobe

- **Action:** structured operation with preconditions, navigation, object interaction, animation plan, emotion overlay, duration, priority, interruptibility, cancel, completion, follow-up. Interruptible by default.
- **Navigation:** navmesh, obstacles, doors, furniture-aware targets — no teleport-as-default for living behavior. Logical position is canonical; geometric following is runtime.
- **Objects:** `object_id`, state, interaction_points, supported_actions, animation mappings, availability, ownership, visibility. Add objects without forking Core.
- **Wardrobe:** garment metadata, transactional outfit changes, explicit vs inferred preference memory. Reference wardrobe before a large catalog.

## Reference-first

Do not scale to 10 female + 5 male companions until the Reference Companion + Reference Home + Reference Wardrobe + action/object/life stack PASSes as one system.

`REFERENCE → VALIDATE → ABSTRACT → TEMPLATE → VARIATIONS → SCALE`

## Cross-platform

Same Companion across iOS, Android, Windows, macOS, Web, Telegram. Telegram is a constrained adapter (text/voice messages), not a second brain. Desktop fullscreen / windowed / floating / overlay / minimal are presentation modes.

## AI providers

Core must not import vendor SDKs into domain logic. Adapters live under `ai/` (not started). Development default: local stubs at $0.

## Security / privacy sketch

Tenant isolation, authn/z, rate limits, no secrets in source, webhook authenticity, prompt-injection resistance, tool allowlists, deny-by-default camera/mic/screen, age gating architecture (legal method is an open decision). See [SECURITY.md](SECURITY.md) and [PRIVACY.md](PRIVACY.md).

## Not decided here

Language, 3D engine, database, auth vendor, realtime transport, paid AI providers. Those require human ADRs.
