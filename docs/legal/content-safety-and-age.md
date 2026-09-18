# Content safety and age controls / Seguridad de contenido y edad

**Status:** `DRAFT — PENDING HUMAN LEGAL COUNSEL`  
**Product:** `[PRODUCT_NAME]` · **Operator:** `[OPERATOR_LEGAL_NAME]`  
**Effective date (when approved):** `[EFFECTIVE_DATE]`  
**Age method (open decision):** `[AGE_GATE_METHOD]`  
**Safety contact:** `[CONTACT_SAFETY]`

Aligns with master-spec **Point 49**. Implementation of verification vendors is **not** locked (see [DECISIONS.md](../../DECISIONS.md) item 7).

---

## 1. Age eligibility

- Adult conversational features (including intimate/romantic roleplay when enabled) require users to be adults under applicable law.
- `[AGE_GATE_METHOD]` must be chosen by human counsel (self-attestation, payment instrument, third-party age vendor, government ID, etc.). Until chosen, **do not ship adult features**.
- We do not knowingly allow accounts for children below the legal adult age for the product’s adult mode.

## 2. Absolute prohibitions (design + policy)

- No sexualization of minors.
- No characters that appear to be minors in sexual contexts.
- No CSAM creation, storage, or distribution.
- No unauthorized real-person face/voice cloning.
- Safety classifier / policy layer is a shared platform service (Point 49 engineering expansion), not a per-client fork.

## 3. Consent and boundaries

- Users may set content boundaries and revoke consent for sensitive modalities (voice, camera, screen, location).
- Companions must respect interrupt and “stop” semantics for embodied/voice features when implemented.
- Adult content is opt-in where the product offers it; default safe mode for new accounts until age gate PASSes.

## 4. Reporting and blocking

Users must be able to:

- report abusive content or behavior;
- block another user or stop a Companion session;
- request human review for high-severity reports.

Contact: `[CONTACT_SAFETY]`. Preserve enough forensic metadata for investigation without dumping unnecessary private content into logs (see [SECURITY.md](../../SECURITY.md)).

## 5. Illegal and abusive content

We prohibit content that is illegal or listed in [acceptable-use-policy.md](acceptable-use-policy.md). We may remove content and suspend accounts.

## 6. What is still open

Human ADR still required for:

- exact age verification method and vendor;
- adult-content legal policy per jurisdiction;
- retention of report evidence;
- Telegram channel-specific terms (open decision 11).

---

## Español (resumen)

Las funciones adultas solo para mayores de edad, con método `[AGE_GATE_METHOD]` aún **no decidido**. Prohibido sexualizar menores o personajes con apariencia de menor, CSAM, y clonar rostro/voz de personas reales sin autorización. Debe existir reporte, bloqueo y modo seguro por defecto. No publicar funciones adultas hasta ADR legal.
