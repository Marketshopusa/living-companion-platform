# Backend

Gate 1: local Companion identity persistence adapters only.

- `backend/identity/memory_store.py` — in-memory repository
- `backend/identity/file_store.py` — JSON files, one document per `companion_id`

No HTTP API, no database, no cloud. Canonical authorization stays in Core policy.
