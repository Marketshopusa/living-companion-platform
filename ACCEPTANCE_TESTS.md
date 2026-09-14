# Acceptance tests

Completion means **IMPLEMENTED + TESTED + EVIDENCE + GATE PASS**, not “files exist” without a check.

Evidence is stored under `docs/evidence/<gate-or-point>/`.

## Gate 0 — Repository governance

### Scope

Repository baseline only. No Companion Core, UI, 3D, or paid providers.

### Automated

Run `scripts/check-baseline.ps1` (Windows) or `scripts/check-baseline.sh` (CI/Unix).

Must pass:

1. Required governance files exist (see script list).
2. Section B directories exist.
3. `MASTER_BUILD_SPECIFICATION.md` exists and is not required to change.
4. No tracked `.env`, `credentials.json`, or `*.pem` product secrets.
5. ADR-000 exists.

### Manual

1. Confirm `git status` shows no accidental secret files.
2. Confirm this file, [BUILD_PLAN.md](BUILD_PLAN.md), and [ARCHITECTURE.md](ARCHITECTURE.md) describe Gate 0 as governance-only.
3. Confirm no product implementation under `core/`, `backend/`, `apps/*` beyond `.gitkeep` / placeholders.

### Evidence

`docs/evidence/gate-0/` must contain:

- `inventory.txt` — file listing
- `git.txt` — branch, remote, SHAs
- `check-baseline.txt` — script output
- `notes.md` — PASS/FAIL and defects

### PASS

All automated checks green; manual checks recorded; master spec unmodified; [BUILD_PLAN.md](BUILD_PLAN.md) updated.

## Gate 1 — Companion Core identity contracts (do not start until Gate 0 PASS + human approval)

### Scope (future)

- Versioned Companion identity schema (immutable vs mutable).
- Persist a fictional test Companion with a unique ID independent of any device.
- Two simulated clients read the same ID and receive the same identity.
- Cross-tenant read denied.
- No UI, avatar, paid LLM, wardrobe, or world.

### Evidence (future)

`docs/evidence/point-01/`

## Later gates

Points 00–70 and V3 combined tests (bedtime, morning, cooking, movie, 30–60 minute reality, seven-day, cross-platform) are not in Gate 0. Track them in [BUILD_PLAN.md](BUILD_PLAN.md) as `NOT_STARTED`.
