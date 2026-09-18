# Cookies and similar technologies / Cookies y tecnologías similares

**Status:** `DRAFT — PENDING HUMAN LEGAL COUNSEL`  
**Product:** `[PRODUCT_NAME]` · **Operator:** `[OPERATOR_LEGAL_NAME]`  
**Effective date (when approved):** `[EFFECTIVE_DATE]`

Applies when Web (and similar) clients ship. Native apps may use local storage / SDKs with analogous notice.

---

## 1. Categories

| Category | Purpose | Consent posture (draft) |
| --- | --- | --- |
| Strictly necessary | Auth session, security, load balancing, fraud prevention | Required for service |
| Preferences | Language, UI settings | Prefer consent or conspicuous control |
| Analytics | Aggregated product metrics (no raw chat dumps) | Consent-gated (Point 53) |
| Marketing | Not in default $0 architecture | Requires separate ADR + notice |

## 2. Local storage

Clients may store ephemeral UI state, tokens in secure storage, and caches. Canonical Companion identity/memory remains server-side when online sync exists; clients must not become competing brains ([ARCHITECTURE.md](../../ARCHITECTURE.md)).

## 3. Controls

When Web ships: cookie banner / preference center linking this notice and [privacy-policy.md](privacy-policy.md). Deny-by-default for non-essential tags.

## 4. Open items

Exact cookie inventory, CMP vendor, and retention for analytics IDs require human approval before production Web launch.

---

## Español (resumen)

Cookies necesarias para sesión/seguridad; analítica solo con consentimiento y separada del contenido de chat; marketing no por defecto. Inventario exacto pendiente de aprobación humana antes del launch web.
