# Vendors and subprocessors / Proveedores y subencargados

**Status:** `DRAFT — PENDING HUMAN LEGAL COUNSEL`  
**Product:** `[PRODUCT_NAME]` · **Operator:** `[OPERATOR_LEGAL_NAME]`  
**Effective date (when approved):** `[EFFECTIVE_DATE]`  
**Privacy contact:** `[CONTACT_PRIVACY]`

Until production vendors are approved, development remains **local / $0 stubs** ([docs/runbooks/environments.md](../runbooks/environments.md)).

---

## 1. Current production subprocessors

| Vendor | Purpose | Data categories | Region | DPA / terms reviewed | Status |
| --- | --- | --- | --- | --- | --- |
| _None approved_ | — | — | — | — | Empty by design |

Update this table before any paid or cloud provider processes personal data.

## 2. Review checklist (required before onboarding)

- [ ] Business need documented; no “convenience-only” paid spend without ADR  
- [ ] Data categories and minimization reviewed  
- [ ] Training-on-customer-data: **off** unless ADR + notice + consent  
- [ ] Subprocessor list and breach notification terms acceptable  
- [ ] Encryption in transit; encryption at rest where offered  
- [ ] Retention / deletion API or process documented  
- [ ] Region / transfer mechanism recorded  
- [ ] Prompt-injection / logging risks assessed for AI vendors  
- [ ] Security contact and incident SLA noted  
- [ ] Added to this table **before** production traffic  

## 3. AI provider special rules

- Treat model output as untrusted ([SECURITY.md](../../SECURITY.md)).  
- Do not send secrets or unnecessary sensitive data in prompts.  
- Prefer ephemeral voice/vision processing.  
- Document whether vendor stores prompts and for how long.

## 4. Telegram / messaging channels

Bot ownership and data-processing terms remain an **open decision** ([DECISIONS.md](../../DECISIONS.md) item 11). Do not launch a production bot until that ADR exists.

---

## Español (resumen)

Hoy **no** hay subencargados de producción aprobados. Antes de usar un proveedor cloud/IA hay que completar el checklist, ADR de coste, y actualizar esta tabla. Telegram requiere decisión humana previa.
