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

## Gate 1 — Companion Core identity contracts

### Scope

- Versioned Companion identity schema (immutable vs mutable) in `core/contracts/identity/v1/`.
- Persist a fictional test Companion with a unique `companion_id` independent of any device.
- Two simulated clients read the same ID and receive the same canonical identity.
- Cross-tenant read returns `forbidden`. Unknown id within tenant returns `not_found`.
- No UI, avatar, paid LLM, wardrobe, or world. No identity models under `apps/`.

### Automated

From repository root:

1. `git diff -- MASTER_BUILD_SPECIFICATION.md` (must be empty).
2. `scripts/check-baseline.ps1` or `scripts/check-baseline.sh`.
3. `scripts/check-identity-contracts.ps1` or `scripts/check-identity-contracts.sh` (pytest under `tests/identity`).

### Manual

1. Confirm two simulated clients share Core and are not competing stores.
2. Confirm `apps/` has no identity implementation.
3. Confirm LLM text is not accepted as an identity command.

### Evidence

`docs/evidence/gate-1/` and `docs/evidence/point-01/` (identity-contract slice only; Point 01 is not fully PASSed).

### PASS

Automated tests green; isolation and dual-client cases recorded; master spec unmodified; [BUILD_PLAN.md](BUILD_PLAN.md) Gate 1 PASS. Does **not** PASS Points 02–05.

## Later gates

Points 00–70 and V3 combined tests (bedtime, morning, cooking, movie, 30–60 minute reality, seven-day, cross-platform) are not in Gate 0. Track them in [BUILD_PLAN.md](BUILD_PLAN.md) as `NOT_STARTED`.
