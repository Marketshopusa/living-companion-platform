# Companion identity contracts v1

Language-neutral JSON Schema (Draft 2020-12). Python (ADR-001) validates and persists these documents; Python types are **not** the source of truth.

`identity_schema_version` is `1`. A later additive contract must live under `v2/`.

## Isolation error shape

| Situation | `code` |
| --- | --- |
| Authenticated principal, different `tenant_id` than the Companion | `forbidden` |
| Unknown `companion_id` **within** the principal’s tenant | `not_found` |

Do not mix these.

## Immutability

| Field | Mutable after create |
| --- | --- |
| `companion_id` | No |
| `tenant_id` | No |
| `owner_user_id` | No (transfer out of scope) |
| `created_at` | No |
| `identity_schema_version` | No (fixed per contract directory) |
| `display_name` | Yes (versioned config) |
| `age_presentation` | Yes |
| `gender_presentation` | Yes |
| `personality` | Yes |
| `configuration` | Yes |
| `status` | Yes (`active` \| `disabled` \| `archived`) |
| `config_revision` | Server-incremented on successful mutable writes |
| `updated_at` | Server-set |
| `metadata` | Yes (allowlisted keys only) |

Id format: UUID string, lowercase. Schema choice, not a vendor lock.

## Canonical JSON

- UTF-8
- RFC 3339 timestamps in UTC with `Z`
- Object keys sorted lexicographically at every level
- Separators `,` and `:` with no extra whitespace
- No `NaN` / `Infinity`
- `additionalProperties: false` on all v1 objects

## Out of v1 (non-authoritative; do not persist here)

`VOICE`, `APPEARANCE`, `MEMORY`, `RELATIONSHIP`, `CURRENT_STATE`, outfit, room, world. No `device_id`. No LLM payload command type.

## Commands

Only `CreateCompanion`, `GetCompanion`, `UpdateCompanionConfiguration`, `SetCompanionStatus`. Extra properties are rejected.
