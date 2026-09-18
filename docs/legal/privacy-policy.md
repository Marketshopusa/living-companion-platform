# Privacy policy / Política de privacidad

**Status:** `DRAFT — PENDING HUMAN LEGAL COUNSEL`  
**Product:** `[PRODUCT_NAME]` · **Operator:** `[OPERATOR_LEGAL_NAME]`  
**Effective date (when approved):** `[EFFECTIVE_DATE]`  
**Privacy contact:** `[CONTACT_PRIVACY]`

This draft aligns with master-spec Points 05 / 42 / 48 / 53 and root [PRIVACY.md](../../PRIVACY.md). It is **not** a completed compliance program.

---

## 1. Who we are

`[OPERATOR_LEGAL_NAME]` (“we”, “us”) operates `[PRODUCT_NAME]`, a Living Companion Platform that may use artificial intelligence. See [ai-disclosure.md](ai-disclosure.md).

## 2. Scope

This notice covers personal data processed when you use our apps, web, desktop, Telegram, or related services (when those surfaces exist). Local-only development builds may process data only on your device; production processing may involve servers and vetted vendors listed in [vendor-and-subprocessors.md](vendor-and-subprocessors.md).

## 3. Data classes

We classify data as: `PUBLIC` / `OPERATIONAL` / `PERSONAL` / `SENSITIVE` / `SECRET`.

Examples:

| Class | Examples |
| --- | --- |
| OPERATIONAL | Fictional Companion configuration, schema versions, feature flags |
| PERSONAL | Account identifiers, `tenant_id` / `owner_user_id`, contact email, device ids |
| SENSITIVE | Voice recordings, camera/screen captures, precise location, health-like content you choose to share |
| SECRET | Passwords, tokens, API keys (never logged in cleartext) |

## 4. What we collect (when features exist)

Only what a shipped feature requires (minimization):

- **Account / identity:** email or auth subject, tenant membership, session/device metadata.
- **Companion configuration:** name, personality settings you choose, preferences.
- **Conversation content:** text, transcripts, and (if enabled) voice audio for STT/TTS.
- **Memory artifacts:** structured memories you create or that the system proposes and you accept/correct.
- **Sensor permissions (deny-by-default):** microphone, camera, screen, location — only after explicit permission.
- **Diagnostics:** crash and performance telemetry with redaction; not full private chat dumps.
- **Payments / entitlements:** billing tokens via payment processor (we should not store full card numbers).
- **Support / abuse reports:** content you submit to `[CONTACT_SAFETY]` / `[CONTACT_PRIVACY]`.

We do **not** intend to collect data from children under the age gate. See [content-safety-and-age.md](content-safety-and-age.md).

## 5. Why we process data

- Provide and secure the Companion Core experience (identity, sync, continuity).
- Operate AI features you enable (conversation, voice, moderation).
- Enforce [acceptable-use-policy.md](acceptable-use-policy.md) and prevent fraud/abuse.
- Comply with law and respond to lawful requests.
- Improve reliability (consent-gated analytics; separated from raw conversation content where required).

## 6. AI processing

AI systems may process prompts, context windows, voice features, and moderation signals. LLM output is **untrusted** and cannot alone authorize privileged actions.

**Training:** default recommendation is **do not train foundation models on user data** unless a human-approved ADR, updated notice, and required consent say otherwise.

## 7. Sharing

We may share data with:

- infrastructure and AI subprocessors under contract (see vendor list when production);
- payment processors;
- authorities when legally required;
- successors in a corporate transaction under continued protections.

We do **not** sell personal data for advertising as a business model in this draft posture. Any advertising stack would need a separate ADR and notice update.

## 8. Retention

Retention periods are an **open human decision** (`[RETENTION_DEFAULT]`). Until decided:

- prefer ephemeral processing for voice/vision;
- Gate 1 identity supports `archived` status only (not hard-delete yet);
- deletion/export hooks are required by the product spec before Points 48 PASS.

## 9. Your controls (when implemented)

You should be able to control: memory, voice, camera, screen, data, and history; and request access, correction, export, and deletion as required by applicable law. Process: [data-subject-requests.md](data-subject-requests.md).

## 10. Security

See [SECURITY.md](../../SECURITY.md) and [anti-fraud-and-trust.md](anti-fraud-and-trust.md). No method is perfect; report suspected incidents to `[CONTACT_LEGAL]`.

## 11. International transfers

If data leaves your country, we will describe transfer mechanisms (SCCs, adequacy, etc.) once jurisdiction and vendors are chosen. **Not locked.**

## 12. Children

Service not directed to users below `[AGE_GATE_METHOD]` threshold. No sexualization of minors or minor-like characters. See Point 49 and [content-safety-and-age.md](content-safety-and-age.md).

## 13. Changes

Material changes will update `[EFFECTIVE_DATE]` and, where required, seek fresh consent.

## 14. Contact

Privacy: `[CONTACT_PRIVACY]` · Legal: `[CONTACT_LEGAL]`

---

## Resumen en español

`[PRODUCT_NAME]` puede procesar datos de cuenta, configuración del Companion, conversaciones, voz/cámara (solo con permiso), memorias y diagnósticos. Usamos IA; el contenido puede ser generado o mediado por IA. Por defecto **no** entrenamos modelos con tus datos salvo decisión humana explícita. Puedes (cuando exista la función) controlar memoria, voz, cámara, pantalla, datos e historial, y solicitar acceso/exportación/eliminación. Contacto: `[CONTACT_PRIVACY]`. Este texto es **borrador** hasta revisión legal.
