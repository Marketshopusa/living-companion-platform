# Contributing

## Before you write product code

1. Read [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md) (V3 is authoritative on embodiment and sequencing).
2. Read [AGENTS.md](AGENTS.md), [BUILD_PLAN.md](BUILD_PLAN.md), and [DECISIONS.md](DECISIONS.md).
3. Confirm the current gate is `IN_PROGRESS` or you are opening the next approved gate.
4. Do not skip gates because “it can be done later.”

## Workflow

1. Branch from `main`.
2. Own a file set; do not collide with another agent on the same files.
3. Implement only the current gate’s scope.
4. Add or update tests and [docs/evidence/](docs/evidence/) for that gate.
5. Run [scripts/check-baseline.ps1](scripts/check-baseline.ps1) (Windows) or the CI workflow locally equivalent.
6. Update [BUILD_PLAN.md](BUILD_PLAN.md) with status, evidence path, and commit SHA **after** tests pass.
7. Open a pull request. Do not force-push `main`.

## Definition of Done (every point)

Code (when required), configuration, documentation, automated tests where applicable, manual procedure, evidence, defect list/resolution, acceptance criteria.

## Secrets

Never commit `.env`, keys, tokens, or credentials. Use `.env.example` with empty placeholders only.

## Assets

Production assets need provenance and license metadata. Do not copy proprietary characters, models, voices, prompts, or designs.

## Human approval

Irreversible architecture, cost, privacy, security, legal/licensing, or product decisions need an ADR and a human sign-off. See [DECISIONS.md](DECISIONS.md).
