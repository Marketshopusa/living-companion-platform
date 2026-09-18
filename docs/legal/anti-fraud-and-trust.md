# Anti-fraud and trust & safety / Antifraude y confianza

**Status:** `DRAFT — PENDING HUMAN LEGAL COUNSEL`  
**Product:** `[PRODUCT_NAME]` · **Operator:** `[OPERATOR_LEGAL_NAME]`  
**Effective date (when approved):** `[EFFECTIVE_DATE]`  
**Abuse / fraud desk:** `[CONTACT_SAFETY]`

Goal: reduce scams, impersonation, deepfake deception, and social-engineering risk around an AI companion product.

---

## 1. Product promises we must not make

- We do **not** claim Companions are human.
- We do **not** claim AI advice is professional counsel.
- We do **not** ask users (via official channels) for passwords, seed phrases, one-time codes, or wire transfers.
- Official staff will never demand payment outside documented billing flows.

## 2. User-facing fraud warnings (ship with AI disclosure)

Display durable guidance such as:

- AI may hallucinate; verify important facts independently.
- Never send money, gifts, or credentials because a Companion “asked.”
- Romance/scam patterns: urgent secrecy, off-platform payment, crypto, gift cards → report and stop.
- Deepfake risk: AI voice/face may sound/look real; treat media as synthetic unless proven otherwise.

## 3. Impersonation controls

- Brand the product clearly; reserve official domains and app-store listings.
- Prohibit Companion configurations that impersonate banks, governments, or living private individuals for deception.
- Watermark or label AI media where feasible ([ai-disclosure.md](ai-disclosure.md)).
- Domain / phishing: publish canonical URLs once production exists; warn about lookalikes.

## 4. Account and entitlement abuse

- Server-side authorization only.
- Rate limits, device/session revocation, anomaly detection (Point 47).
- Webhook signature verification for Telegram/billing when those integrations exist.
- No client-side entitlement grants.

## 5. Prompt injection and tool abuse

LLM output is untrusted. It must not execute shell, SQL, payments, account changes, or privileged APIs without:

`intent → structured proposal → validation → authorization → policy → execution → result → state update`

## 6. Operator response

On credible fraud reports we may: freeze sessions, revoke devices, preserve logs needed for investigation, notify affected users when appropriate, and cooperate with lawful process.

## 7. Transparency

Public status of this program remains draft until counsel and security owners accept ADR-002 and fill contacts/jurisdiction.

---

## Español (resumen)

El Companion **no** es humano ni asesor profesional. Nunca envíes dinero ni contraseñas porque la IA lo “pida”. Cuidado con estafas románticas y deepfakes. La autorización es siempre en servidor; la salida del modelo no ejecuta acciones privilegiadas sola. Reporta fraude a `[CONTACT_SAFETY]`.
