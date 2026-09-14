# Agent working agreement

The **repository** is the source of truth. Chat is not the project-management system.

## Required reading (every session)

1. This file (`AGENTS.md`)
2. [BUILD_PLAN.md](BUILD_PLAN.md)
3. [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md) (including V3)
4. Relevant ADRs under [docs/adr/](docs/adr/)
5. Current gate evidence under [docs/evidence/](docs/evidence/)
6. Open items in [DECISIONS.md](DECISIONS.md)

## Roles

### Primary Engineering Agent (Cursor)

- Architecture
- Companion Core / backend
- Primary implementation
- Integration, debugging, release preparation

### Secondary Audit / Test / Documentation Agent (Antigravity or equivalent)

- Independent tasks
- UI/UX (when in scope)
- Test generation
- Audits and documentation
- Technical spikes
- Regression verification

**Never let both agents edit the same files at the same time.** Use branches and pull requests. If both must touch one area, one agent owns the files until merge.

## Traceability

Every meaningful change must map:

`requirement → task → implementation → test → evidence → gate → commit`

## Gates

- Status: `NOT_STARTED → IN_PROGRESS → TESTING → PASS`
- Failure: `FAIL → FIX → RETEST → PASS`
- Compilation is not acceptance
- Do not start the next point through a failed gate
- Do not modify `MASTER_BUILD_SPECIFICATION.md`

## LLM security

Treat every model output as untrusted. Models must not execute shell, SQL, payments, account changes, or privileged APIs. Path:

`intent → structured proposal → validation → authorization → policy → execution → result → state update`

## Canonical state

Clients (iOS, Android, Windows, macOS, Web, Telegram) are presentation surfaces. They must not become competing Companion brains.

## Cost

Assume $0 until a human ADR approves spend. No paid services “for convenience.”

## Stop conditions

Stop for unresolvable failures or decisions listed in [DECISIONS.md](DECISIONS.md). Do not silently lock stack, legal, privacy, or licensing choices.
