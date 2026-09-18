# Legal / trust policy pack — evidence

Date: 2026-09-18

Workstream: Governance side track (ADR-002 proposed)

Result: DRAFT pack added; **not** Points 47–49 PASS; **not** counsel-approved

## What was added

- `docs/legal/` — privacy, terms, AUP, AI disclosure (EN+ES short notices), content safety/age, anti-fraud, DSAR, cookies, vendor checklist
- `docs/adr/002-legal-policy-pack-draft.md` — status `proposed`
- Links from `PRIVACY.md`, `SECURITY.md`, `README.md`, `DECISIONS.md`, `BUILD_PLAN.md`, `CONTRIBUTING.md`
- Baseline scripts require core legal files

## Explicit non-claims

- No jurisdiction, age-verification vendor, or retention period locked
- No production UI shipping these as final policies
- No subprocessors approved
- Points 47 / 48 / 49 remain `NOT_STARTED` in BUILD_PLAN

## Validation

See `check-baseline.txt` in this folder.

## Next human actions

1. Review and accept or revise ADR-002
2. Fill placeholders: operator name, contacts, jurisdiction, age method, retention
3. Counsel edit before any public/product link
