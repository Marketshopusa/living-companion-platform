# ADR-001 — Core language for Gate 1 identity contracts

- **ID:** 001
- **Title:** Core language for Gate 1 identity contracts
- **Status:** accepted
- **Date:** 2026-09-14
- **Deciders:** Primary Engineering Agent proposal; **human accepted** on 2026-09-14.

## Context

[ADR-000](000-no-stack-lock.md) forbids a silent stack lock. Gate 1 (Companion Core identity contracts) still needs an executable runtime so schema validation, deterministic serialization, isolation tests, and local persistence can PASS. [MASTER_BUILD_SPECIFICATION.md](../../MASTER_BUILD_SPECIFICATION.md) requires technologies to be selected by benchmark and recorded in ADRs, canonical Companion identity in Core/backend (not in a client), $0 local development until spend is approved, and replaceable adapters rather than vendor SDKs in domain logic.

Language/runtime for Core remains an open item in [DECISIONS.md](../../DECISIONS.md). This document proposes a **narrow** choice for implementing Gate 1 identity contracts only. Canonical identity remains defined at a **language-neutral contract boundary** (versioned JSON Schema). Python is a Core test/runtime for those contracts, not the identity model itself, and not a platform-wide language lock.

## Decision

**Accepted:** implement Gate 1 Companion Core identity **validation, domain logic, tests, and local persistence adapters** with:

- **Python 3.x** (current maintained 3.x on the developer machine and CI; no paid interpreter)
- **pytest** for deterministic automated tests
- **JSON Schema** as the canonical, language-neutral identity contract (immutable vs mutable fields, commands, errors)
- **JSON Schema validation** in Python against those schemas before persist
- **Standard-library-first** implementation (`json`, `pathlib`, `datetime`, `uuid`, `unittest.mock` / pytest fixtures). Add a dependency only if JSON Schema validation cannot be done with an already-available, $0, OSI-licensed library recorded in the lockfile; prefer the smallest validator, no vendor cloud SDK
- **Local in-memory** repository as the default persistence port
- **Optional JSON-file** persistence for restart/recovery tests (gitignored or test temp dirs)
- **No paid services**
- **No database** (no PostgreSQL, SQLite-as-product-DB requirement, or hosted DB)
- **No cloud dependency**
- **No vendor SDK requirement** (no LLM, STT/TTS, 3D, auth, or cloud SDKs)

Clients (including simulated Gate 1 clients) consume the **JSON contracts**, not Python types as the source of truth. A future Core in another language may implement the same schemas without changing `companion_id` or identity semantics.

## This ADR does NOT lock

This accepted ADR still does **not** select or freeze:

- mobile platform language (iOS/Android)
- desktop platform language (Windows/macOS native)
- web frontend language
- 3D engine
- AI provider (LLM, embeddings, STT, TTS, vision, moderation)
- database or event bus
- cloud provider or cloud infrastructure
- realtime transport (WebSocket, WebRTC, other)
- authentication provider (OIDC or otherwise)

Those remain open in [DECISIONS.md](../../DECISIONS.md) and require their own ADRs.

## Why this is appropriate for Gate 1

Gate 1 must prove a unique `companion_id`, device-independent identity, two simulated clients reading the same canonical snapshot, cross-tenant deny, validation, versioning, and deterministic serde — not a production mesh, UI, or data platform.

Python 3.x plus pytest and JSON Schema fit that slice: local, $0, no cloud account, strong test runners, and first-class JSON. Standard-library-first keeps Companion Core free of vendor SDKs. In-memory and optional JSON-file persistence satisfy “identity lives in Core/backend, not in one app” without deciding a canonical database (open decision). JSON Schema keeps the architecture **language-neutral at the contract boundary**: iOS, Android, Windows, macOS, Web, and Telegram must not grow duplicate identity models; they would later bind to the same schemas.

This is a Gate 1 **implementation vehicle**, not a declaration that the Living Companion Platform is a Python product.

## Consequences

Positive:

- Gate 1 can be tested without paid CI extras, databases, or cloud.
- Contracts stay portable; Core Python code is an adapter to schemas.
- Aligns with ADR-000: later stacks still need new ADRs.

Negative / follow-up:

- Status is **accepted**. Gate 1 identity modules may use this runtime. Replacing it requires a new ADR.
- Because this ADR is accepted, `core/` and `backend/` identity code may be Python; that is reversible only with a new ADR and a port of the same JSON Schema.
- Gate 0 baseline scripts that forbid all product source under `core/`/`backend/` will need a later, separate change when Gate 1 is built — **not** part of this ADR file.

## Alternatives considered

- **Language-neutral schemas only, no runtime** — rejected for Gate 1 PASS: automated identity tests and persistence proof would be missing.
- **TypeScript/Node as Core** — viable $0 alternative; not proposed here to avoid implying a web-frontend lock. May be chosen if this ADR is rejected.
- **Go/Rust** — strong for later services; heavier for Gate 1 schema-and-test slice; not proposed.
- **Picking PostgreSQL, SQLite, or a cloud DB now** — rejected; database remains an open human decision.
- **Implementing identity inside `apps/`** — rejected; clients are not Companion brains.

## Spec references

- Section A (canonical Core state, untrusted LLM, no secrets, ADR for irreversible choices, $0 until approved)
- Section B (exact technologies via ADR)
- Section F (Companion entity minima: id, timestamps, versioning, ownership/tenant)
- Point 01 (Companion Core identity independent of device; identity not owned by one client)
- Point 03 engineering expansion (canonical schema; immutable identity vs versioned mutable configuration; separate identity from presentation/state/relationship)
- [ACCEPTANCE_TESTS.md](../../ACCEPTANCE_TESTS.md) Gate 1 (simulated clients, cross-tenant deny, no UI/avatar/paid LLM)
- V3 AE (Foundation → Companion Core → Identity before platforms and production systems)
- [ADR-000](000-no-stack-lock.md)
