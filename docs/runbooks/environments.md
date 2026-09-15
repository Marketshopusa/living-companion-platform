# Environments

| Name | Purpose | Status |
| --- | --- | --- |
| `local` | Developer machine, $0, no paid APIs; identity store is in-process or gitignored JSON files | **Active** |
| `staging` | Shared non-production (future) | Not created |
| `prod` | Production (future) | Not created |

No cloud accounts, GPU providers, or paid subscriptions. Gate 1 does not provision a database.

Copy `.env.example` to `.env` locally when needed. Never commit `.env`. Identity file stores used in tests write to pytest temp dirs, not the repo.
