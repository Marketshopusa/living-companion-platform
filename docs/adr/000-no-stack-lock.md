# ADR-000 — No irreversible stack lock in Gate 0

- **ID:** 000
- **Title:** No irreversible stack lock in Gate 0
- **Status:** accepted (Gate 0 governance)
- **Date:** 2026-09-13
- **Deciders:** Primary Engineering Agent proposal; human review via repository

## Context

[MASTER_BUILD_SPECIFICATION.md](../../MASTER_BUILD_SPECIFICATION.md) requires technologies to be selected by benchmark and recorded in ADRs. Gate 0 is repository governance only. Locking language, 3D runtime, database, auth, or paid AI providers now would be an irreversible convenience choice, especially under a $0 development constraint.

## Decision

Gate 0 does **not** select:

- backend or client languages
- 3D engine
- database or event bus
- authentication vendor
- realtime transport
- paid LLM / STT / TTS / vision / cloud GPU

Development remains local. Provider interfaces will be designed later so adapters can be swapped.

Open questions stay in [DECISIONS.md](../../DECISIONS.md).

## Consequences

- Gate 1+ may introduce a stack only with a new ADR and human approval.
- Empty `core/`, `backend/`, and `apps/` trees are intentional.
- CI in Gate 0 checks documents and layout, not product tests.

## Alternatives considered

Picking a popular stack immediately — rejected as a silent lock and a cost/vendor risk.

## Spec references

Section B (repo baseline), Section E (provider abstraction), Section O (first builder command), V3 AE (foundation before platforms), global $0 cost constraint.
