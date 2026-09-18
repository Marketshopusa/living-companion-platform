# Data subject requests / Solicitudes de derechos sobre datos

**Status:** `DRAFT — PENDING HUMAN LEGAL COUNSEL`  
**Product:** `[PRODUCT_NAME]` · **Operator:** `[OPERATOR_LEGAL_NAME]`  
**Privacy contact:** `[CONTACT_PRIVACY]`  
**Effective date (when approved):** `[EFFECTIVE_DATE]`

Supports Point 48 (user control of memory, voice, camera, screen, data, history; deletion per applicable law).

---

## 1. Rights we intend to support (where law requires)

- **Access** — what personal data we hold about you.
- **Correction** — fix inaccurate personal data.
- **Export / portability** — machine-readable export where required (`[export format — open decision]`).
- **Deletion** — erase or anonymize when required (hard-delete vs `archived` — implementation pending; Gate 1 only has `archived`).
- **Restriction / objection** — limit certain processing where applicable.
- **Withdraw consent** — for optional modalities (mic, camera, analytics).

## 2. How to submit

Email `[CONTACT_PRIVACY]` from the address on your account (or other verified channel once accounts exist). Include:

1. Full name / account identifier  
2. Request type (access, export, delete, correct, other)  
3. Relevant Companion / tenant ids if known  
4. Whether the request includes voice/media  

We may request additional verification to prevent fraudulent deletion/takeover.

## 3. Target timelines

Unless mandatory law sets otherwise, aim to acknowledge within **7 days** and complete within **30 days**, with permitted extensions communicated in writing. **Not a legal guarantee until counsel sets SLAs.**

## 4. Limits

We may retain data when required for security, fraud prevention, legal claims, or law. Companion “journal / inner life” fiction is not a user fact store; user personal data remains separable.

## 5. Agents / engineering note

Do not implement irreversible mass-delete without authorization checks. Prefer soft-delete → hard-delete with audit. Export format and retention remain open in [DECISIONS.md](../../DECISIONS.md).

---

## Español (resumen)

Puedes pedir acceso, corrección, exportación, eliminación y retirar consentimientos escribiendo a `[CONTACT_PRIVACY]`. Verificaremos identidad para evitar fraudes. Gate 1 aún no tiene borrado duro (solo `archived`). Plazos orientativos 7 / 30 días hasta que abogados fijen SLAs.
