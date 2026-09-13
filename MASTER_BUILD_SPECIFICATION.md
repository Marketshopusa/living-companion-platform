# MASTER BUILD SPECIFICATION — AI COMPANION ECOSYSTEM
## Production Engineering Edition v2.0

**This is the upgraded master order derived from the supplied original specification.**
The original numbered scope is preserved and each point is expanded with engineering, testing, evidence, security, privacy, cost, and multi-agent requirements.

---

# A. ABSOLUTE PROJECT RULES

1. Execute strictly sequentially: `NOT_STARTED → IN_PROGRESS → TESTING → PASS`.
2. Failure is always `FAILED → FIX → RETEST → PASS`; never continue through a failed gate.
3. Compilation is not acceptance.
4. Every PASS requires code/configuration/docs/tests/manual evidence/defect resolution/acceptance evidence.
5. Canonical Companion, user, memory, relationship, safety, entitlement, and configuration state lives in the backend/Core, not in one client.
6. LLM output is untrusted data. It cannot execute arbitrary code, shell, SQL, privileged actions, payments, account changes, or external tools without validated server-side authorization.
7. No secrets in source code.
8. Every production behavior must be reproducible from code, schema, configuration, AI configuration/model version, and asset version.
9. Do not copy proprietary code, assets, characters, branding, private prompts, private models, or protected designs.
10. All production assets and voices require documented provenance/licensing.
11. Major irreversible architecture, cost, privacy, security, legal/licensing, or product decisions require human approval and an ADR.
12. The repository is the source of truth; chat is not the project-management system.

---

# B. REQUIRED REPOSITORY BASELINE

```text
/
├── MASTER_BUILD_SPECIFICATION.md
├── BUILD_PLAN.md
├── ACCEPTANCE_TESTS.md
├── ARCHITECTURE.md
├── PRODUCT_SPEC.md
├── DECISIONS.md
├── SECURITY.md
├── PRIVACY.md
├── CONTRIBUTING.md
├── AGENTS.md
├── README.md
├── apps/
├── core/
├── backend/
├── ai/
├── integrations/
├── cms/
├── assets/
├── infrastructure/
├── scripts/
├── tests/
└── docs/
    ├── adr/
    ├── evidence/
    ├── evaluations/
    └── runbooks/
```

Exact technologies must be selected by benchmark and recorded in ADRs.

---

# C. BUILD ORCHESTRATOR

`BUILD_PLAN.md` must track every point with:

- status;
- dependencies;
- agent/owner;
- branch;
- commit SHA;
- tests;
- evidence path;
- blocker;
- timestamp.

After PASS:

1. update `BUILD_PLAN.md`;
2. commit;
3. run regression tests;
4. create checkpoint tag when applicable;
5. begin the next point automatically.

The builder must not ask the human to paste the next point.

---

# D. CURSOR + ANTIGRAVITY COLLABORATION CONTRACT

**GitHub is the shared source of truth.**

Default role split:

### Cursor — Primary Engineering Agent
- architecture;
- core/backend;
- primary implementation;
- integration;
- refactoring;
- debugging;
- release preparation.

### Antigravity — Parallel/Verification Agent
- independent tasks;
- UI/UX;
- test generation;
- audits;
- documentation;
- technical spikes;
- regression verification.

**Never let both agents edit the same files simultaneously.**

Use branches and pull requests. If both touch the same area, one owns the files and the other works independently until a PR/merge/review.

Every agent session must read:
1. `AGENTS.md`
2. `BUILD_PLAN.md`
3. `MASTER_BUILD_SPECIFICATION.md`
4. relevant ADRs
5. current point evidence.

---

# E. AI PROVIDER ABSTRACTION

Create provider interfaces for:
- LLM/reasoning;
- embeddings/retrieval;
- STT;
- TTS;
- vision;
- safety/moderation;
- optional search/tools.

Provider adapters must be replaceable. Track safe operational metadata such as provider, model, config version, latency, success/failure, and cost metrics where available.

---

# F. CANONICAL DATA MODEL

At minimum define:

```text
User
Companion
Relationship
Conversation
Message
Memory
MemorySource
EmotionState
PhysicalState
Outfit
Scene
WorldState
Experience
FutureEvent
NotificationPreference
AIConfiguration
Asset
Entitlement
Device
Session
SafetyEvent
AuditEvent
```

Every persistent entity requires stable ID, timestamps, versioning, ownership/tenant relationship, and deletion/retention semantics as applicable.

---

# G. SECURITY / PRIVACY / SAFETY BASELINE

Threat model:
- account takeover;
- broken authorization;
- cross-user memory leakage;
- prompt injection;
- malicious tool input;
- webhook replay/spoofing;
- insecure local storage;
- secret leakage;
- supply-chain compromise;
- media access abuse;
- entitlement abuse;
- denial of service.

Data classification:
`PUBLIC / OPERATIONAL / PERSONAL / SENSITIVE / SECRET`

Safety must include:
- age gating;
- no minors or minor-like sexualization;
- consent boundaries;
- reporting/blocking;
- privacy controls;
- real-person voice/face authorization;
- licensed/provenance-controlled assets.

---

# H. AI EVALUATION BASELINE

Every major AI configuration change must be evaluated for:
- memory accuracy/relevance;
- contradiction handling;
- personality consistency/drift;
- relationship progression;
- emotion consistency;
- safety;
- prompt-injection resistance;
- tool authorization;
- latency/cost.

---

# I. GLOBAL COST / PERFORMANCE BASELINE

Measure:
- model calls/tokens where available;
- STT/TTS usage;
- vision;
- storage;
- bandwidth;
- GPU/CPU;
- rendering FPS/frame time;
- latency.

Use budgets, caching where safe, model routing, fallbacks, rate limits, and entitlements.

---

# J. ASSET GOVERNANCE

Every production asset must record:

```text
asset_id
version
type
creator/vendor
license
source
usage_rights
commercial_rights
platform_restrictions
approval_status
```

---



---

# POINT 00 — REGLAS ABSOLUTAS DEL PROYECTO

## 1. Original scope

# 0. REGLAS ABSOLUTAS DEL PROYECTO

Antes de escribir una sola línea de código, el constructor debe aceptar estas reglas.

### 0.1 Construcción secuencial

Los módulos se ejecutarán estrictamente en orden:

**Punto 1 → prueba → aprobación → Punto 2 → prueba → aprobación...**

No se permite saltar módulos porque "se pueden hacer después".

### 0.2 Definition of Done

Cada punto debe entregar:

1.  código; 
2.  configuración; 
3.  documentación; 
4.  pruebas automatizadas cuando sea posible; 
5.  pruebas manuales; 
6.  evidencia del resultado; 
7.  lista de problemas encontrados; 
8.  solución de los problemas; 
9.  criterio de aceptación cumplido. 

### 0.3 Si una prueba falla

No se continúa.

El estado será:

**FAILED → FIX → RETEST → PASS**

Nunca:

**FAILED → CONTINUE**

### 0.4 No construir un clon literal

El producto se inspirará en **capacidades observables** de productos existentes, pero:

-  no copiar código; 
-  no copiar personajes; 
-  no copiar assets; 
-  no copiar branding; 
-  no copiar prompts privados; 
-  no copiar modelos propietarios; 
-  no copiar diseños protegidos; 
-  no extraer recursos de aplicaciones de terceros. 

Todos los personajes, modelos, voces, escenarios, ropa y sistemas propietarios deberán ser nuestros o contar con las licencias correspondientes.

---

# FASE I — FUNDACIÓN DEL SISTEMA

---

## 2. Engineering expansion

Implement the original scope as a versioned, modular, testable capability.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-00/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 01 — DEFINIR EL PRODUCTO Y LA ARQUITECTURA MAESTRA

## 1. Original scope

# 1. DEFINIR EL PRODUCTO Y LA ARQUITECTURA MAESTRA

El constructor debe comenzar creando el documento técnico principal.

El sistema se denominará conceptualmente:

# COMPANION CORE

El Companion Core será la identidad central de cada personaje.

Debe existir independientemente del dispositivo.

La arquitectura conceptual será:

```
```

```
                         COMPANION CORE
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
      MIND                    BODY                   LIFE
        │                      │                      │
        ▼                      ▼                      ▼
 Personality              Avatar 3D               Events
 Memory                   Animation               Journal
 Reasoning                Voice                   Activities
 User Model               Emotion                 Relationship
 Vision                   Wardrobe                Notifications
```

Y después:

```
```

```
                         COMPANION CORE
                               │
                 ┌─────────────┼─────────────┐
                 │             │             │
                iOS         Android          PC
                                             │
                                      ┌──────┴──────┐
                                      │             │
                                   Windows        macOS
```

Más:

```
```

```
Web
Telegram
future platforms
```

### Prueba

Crear un personaje ficticio de prueba.

Comprobar que:

-  tiene un ID único; 
-  puede existir sin estar ligado a un teléfono; 
-  puede ser consultado desde distintos clientes; 
-  conserva su identidad. 

### No avanzar hasta demostrar:

Que la identidad del personaje vive en el backend y no dentro de una sola aplicación.

---

## 2. Engineering expansion

Define repository structure, bounded contexts, service boundaries, versioned API/event contracts, environment strategy, ADR process, dependency policy, and canonical-state ownership. No client owns canonical Companion identity or memory.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-01/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 02 — ARQUITECTURA MULTIPLATAFORMA

## 1. Original scope

# 2. ARQUITECTURA MULTIPLATAFORMA

Desde este punto el constructor debe diseñar el sistema para:

-  iPhone; 
-  Android; 
-  Windows; 
-  macOS; 
-  Web; 
-  Telegram. 

No se permitirá desarrollar primero móvil y "hacer PC después".

### Requisito

Todos los clientes deben conectarse al mismo:

**Companion Core.**

### Prueba

Crear un personaje de prueba.

Conversar:

1.  desde Android/iOS; 
2.  desde PC; 
3.  desde Web; 
4.  desde Telegram. 

Debe ser reconocida como **la misma persona virtual**.

### Prueba de continuidad

Decir en PC:

> "Mañana tengo una entrevista."

Cerrar.

Entrar desde teléfono.

Preguntar:

> "¿Qué recuerdas que te dije?"

Debe recuperar la información.

---

## 2. Engineering expansion

Create a platform-neutral contract layer, capability negotiation, client adapters, cache/offline rules, compatibility policy, and a rule that new clients do not require rewriting the Companion Core.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-02/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 03 — IDENTIDAD PERSISTENTE DEL PERSONAJE

## 1. Original scope

# 3. IDENTIDAD PERSISTENTE DEL PERSONAJE

Cada Companion tendrá una identidad estructurada.

Ejemplo:

```
```

```
COMPANION_ID
NAME
AGE_PRESENTATION
GENDER
PERSONALITY
VOICE
APPEARANCE
VALUES
INTERESTS
SPEECH_STYLE
HUMOR
BOUNDARIES
MEMORY
RELATIONSHIP
CURRENT_STATE
```

### Prueba

Cambiar:

-  dispositivo; 
-  ropa; 
-  escenario; 
-  cámara; 
-  idioma. 

La identidad debe permanecer intacta.

---

## 2. Engineering expansion

Use a canonical Companion schema with immutable identity fields and versioned mutable configuration. Separate identity, presentation, current state, and relationship.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-03/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 04 — SISTEMA DE PERSONALIDAD

## 1. Original scope

# 4. SISTEMA DE PERSONALIDAD

No crear personajes que sean solamente prompts gigantes.

Crear un:

# Personality Engine

Cada personalidad tendrá parámetros.

Ejemplo:

```
```

```
humor: 0.72
empathy: 0.88
curiosity: 0.91
assertiveness: 0.63
playfulness: 0.77
formality: 0.21
```

Además:

-  valores; 
-  intereses; 
-  preferencias; 
-  estilo lingüístico; 
-  límites; 
-  humor; 
-  temperamento; 
-  comportamiento. 

### Prueba

Dos usuarios interactúan con el mismo arquetipo.

Debe responder de manera consistente con su personalidad, pero adaptarse al usuario.

---

## 2. Engineering expansion

Implement structured personality traits, values, behavior rules, speech style, boundaries, and versioning. Do not rely on one giant prompt.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-04/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 05 — USER MODEL

## 1. Original scope

# 5. USER MODEL

El sistema debe crear un modelo individual del usuario.

Debe poder almacenar, según permisos y políticas de privacidad:

```
```

```
communication style
favorite topics
interests
preferences
humor style
preferred response length
known facts
important dates/events
conversation patterns
relationship preferences
```

### Prueba

Usuario A habla de deportes.

Usuario B habla de arte.

El personaje debe adaptar las conversaciones sin mezclar datos entre usuarios.

### Prueba crítica de privacidad

Los recuerdos del Usuario A jamás pueden aparecer en la conversación del Usuario B.

---

## 2. Engineering expansion

Create a tenant-isolated User Model. Distinguish explicit facts, inferred preferences, temporary context, sensitive/permissioned data, provenance, confidence, timestamp, and retention.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-05/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 06 — MOTOR DE MEMORIA

## 1. Original scope

# 6. MOTOR DE MEMORIA

Este será uno de los sistemas más importantes.

No utilizar únicamente:

> "últimos 20 mensajes".

Crear:

### Memoria episódica

Eventos concretos.

### Memoria semántica

Información estable.

### Memoria relacional

Información sobre la relación.

### Memoria de preferencias

Gustos y disgustos.

### Memoria temporal

Eventos futuros y fechas.

Arquitectura:

```
```

```
CONVERSATION
      ↓
MEMORY EXTRACTION
      ↓
CLASSIFICATION
      ↓
IMPORTANCE
      ↓
STORAGE
      ↓
RETRIEVAL
      ↓
LLM CONTEXT
```

### Prueba

Día 1:

> "Mi restaurante favorito es X."

Día 3:

Hablar de otro tema.

Preguntar:

> "¿Cuál es mi restaurante favorito?"

Debe responder correctamente.

### Prueba de asociación

Recordar información sin utilizar exactamente las mismas palabras.

---

## 2. Engineering expansion

Implement memory extraction, classification, salience, confidence, deduplication, contradiction handling, retrieval ranking, provenance, privacy filters, deletion, and user controls. Never inject the entire memory database into context.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-06/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 07 — MEMORIA DE LARGO PLAZO

## 1. Original scope

# 7. MEMORIA DE LARGO PLAZO

El constructor debe implementar memoria de:

-  días; 
-  semanas; 
-  meses; 
-  potencialmente años. 

Pero con:

```
```

```
importance
confidence
timestamp
source
privacy
```

### Prueba

Crear 100 conversaciones de prueba.

Introducir cinco hechos importantes.

Después realizar una conversación larga con múltiples temas.

Comprobar que recupera los cinco hechos relevantes sin contaminar la conversación con información irrelevante.

---

## 2. Engineering expansion

Add durable storage, backup/restore, schema migrations, retention, stale-memory handling, contradiction resolution, and retrieval evaluation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-07/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 08 — RAZONAMIENTO Y CONTEXTO

## 1. Original scope

# 8. RAZONAMIENTO Y CONTEXTO

Crear el:

# Reasoning / Agent Engine

Debe interpretar:

```
```

```
CURRENT MESSAGE
+
CONVERSATION
+
MEMORY
+
USER MODEL
+
RELATIONSHIP
+
EMOTIONAL STATE
+
ENVIRONMENT
```

y producir:

```
```

```
RESPONSE
+
EMOTION
+
INTENT
+
ANIMATION
+
VOICE STYLE
+
MEMORY ACTION
```

### Prueba

Cambiar de tema bruscamente.

Después regresar a un tema anterior.

El personaje debe mantener coherencia.

---

## 2. Engineering expansion

Build context assembly with explicit budgets and priorities. Put LLM/provider calls behind an AI gateway. Validate all structured model outputs before execution.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-08/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 09 — RELATIONSHIP ENGINE

## 1. Original scope

# 9. RELATIONSHIP ENGINE

Este módulo hará que la relación evolucione.

Debe manejar conceptualmente:

```
```

```
relationship_stage
familiarity
trust
shared_history
interaction_frequency
important_events
preferences
```

No debe ser simplemente un contador.

Debe influir en:

-  tono; 
-  referencias; 
-  familiaridad; 
-  humor; 
-  comportamiento. 

### Prueba

Crear una relación desde cero.

Después de múltiples conversaciones comprobar que el comportamiento cambia gradualmente.

No debe convertirse inmediatamente en una relación avanzada.

---

## 2. Engineering expansion

Represent relationship as a state machine plus continuous dimensions. Changes must be explainable and gradual, not arbitrary model improvisation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-09/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 10 — ESTADO EMOCIONAL

## 1. Original scope

# 10. ESTADO EMOCIONAL

Crear:

# Emotional State Engine

Variables:

```
```

```
happiness
sadness
anger
excitement
calm
surprise
affection
stress
confidence
energy
```

Con intensidad:

```
```

```
0.0 → 1.0
```

### Prueba

Una conversación alegre debe producir una respuesta emocional diferente de una conversación conflictiva.

### Prueba adicional

La emoción debe afectar:

-  texto; 
-  voz; 
-  rostro; 
-  postura; 
-  gestos. 

---

## 2. Engineering expansion

Implement emotional state with bounded transitions, decay, triggers, persistence rules, and context sensitivity. Treat it as an internal simulation, not a claim of sentience.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-10/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 11 — EMOCIONES NO DEBEN SER SIMPLES INTERRUPTORES

## 1. Original scope

# 11. EMOCIONES NO DEBEN SER SIMPLES INTERRUPTORES

No hacer:

```
```

```
happy = animation_01
sad = animation_02
angry = animation_03
```

Crear estados combinables.

Ejemplo:

```
```

```
emotion:
happy = 0.61
excited = 0.78
nervous = 0.20
```

### Prueba

Generar emociones mixtas.

Verificar que el comportamiento resultante sea coherente.

---

## 2. Engineering expansion

Support blended affect and competing signals. Coordinate text, voice, gaze, face, posture, and gestures through a mapping layer.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-11/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 12 — SPEECH-TO-TEXT

## 1. Original scope

# 12. SPEECH-TO-TEXT

Implementar conversación por voz.

Arquitectura:

```
```

```
MICROPHONE
    ↓
AUDIO PROCESSING
    ↓
SPEECH TO TEXT
    ↓
CONVERSATION ENGINE
```

Debe soportar múltiples idiomas.

### Pruebas

Probar:

-  inglés; 
-  español; 
-  conversación rápida; 
-  pausas; 
-  ruido; 
-  diferentes acentos; 
-  frases largas; 
-  interrupciones. 

---

## 2. Engineering expansion

Abstract STT providers. Support streaming, partial/final transcripts, endpointing, language detection, permissions, fallback, and configurable audio retention.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-12/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 13 — TEXT-TO-SPEECH

## 1. Original scope

# 13. TEXT-TO-SPEECH

Crear sistema de voz propio/licenciado para cada personaje.

La voz debe conservar identidad.

Debe permitir variables como:

```
```

```
pitch
speed
energy
emotion
volume
pause
```

### Prueba

La misma frase con:

-  felicidad; 
-  tristeza; 
-  enojo; 
-  sorpresa. 

Debe sonar diferente sin perder la identidad vocal.

---

## 2. Engineering expansion

Abstract TTS providers. Define stable licensed voice identities, prosody controls, streaming, interruption, and fallback.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-13/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 14 — CONVERSACIÓN EN TIEMPO REAL

## 1. Original scope

# 14. CONVERSACIÓN EN TIEMPO REAL

La conversación no debe sentirse como:

> usuario habla → espera 10 segundos → personaje responde.

Implementar:

-  streaming; 
-  detección de silencio; 
-  interrupciones; 
-  respuestas parciales cuando corresponda; 
-  latencia reducida. 

### Prueba de aceptación

La experiencia debe sentirse suficientemente inmediata para una conversación natural.

Registrar:

-  STT latency; 
-  LLM latency; 
-  TTS latency; 
-  rendering latency; 
-  total response latency. 

---

# FASE II — EL CUERPO

## 2. Engineering expansion

Build a cancellable streaming conversation state machine: listening, processing, speaking, interrupted, resumed, ended. Measure end-to-end latency.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-14/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 15 — CREAR EL SISTEMA DE PERSONAJE 3D

## 1. Original scope

# 15. CREAR EL SISTEMA DE PERSONAJE 3D

Construir un sistema de personajes 3D hiperrealistas.

No generar una imagen nueva en cada conversación.

Cada personaje debe ser un modelo persistente.

Debe contener:

```
```

```
BODY
FACE
HAIR
EYES
SKIN
TEETH
CLOTHING
ACCESSORIES
RIG
FACIAL RIG
```

### Prueba

El personaje debe conservar identidad después de:

-  100 cargas; 
-  distintos escenarios; 
-  distintos outfits; 
-  distintas expresiones. 

---

## 2. Engineering expansion

Choose and benchmark a real-time 3D runtime. Define canonical skeleton, facial rig, LODs, texture budgets, animation compression, platform budgets, and licensing.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-15/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 16 — IDENTIDAD VISUAL PERSISTENTE

## 1. Original scope

# 16. IDENTIDAD VISUAL PERSISTENTE

Crear un sistema para garantizar que:

**Yuki siempre sea Yuki.**

No debe cambiar:

-  estructura facial; 
-  proporciones; 
-  ojos; 
-  color de piel; 
-  cabello base; 
-  características fundamentales. 

### Prueba

Generar 50 combinaciones de:

-  ropa; 
-  iluminación; 
-  escenarios; 
-  poses. 

Comprobar consistencia visual.

---

## 2. Engineering expansion

Create immutable visual identity anchors and automated visual regression. Outfits, lighting, camera, and scenes may vary without changing the canonical identity.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-16/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 17 — SISTEMA FACIAL

## 1. Original scope

# 17. SISTEMA FACIAL

Crear facial rig.

Debe controlar:

-  ojos; 
-  párpados; 
-  cejas; 
-  boca; 
-  mandíbula; 
-  mejillas; 
-  nariz; 
-  sonrisa; 
-  tensión facial; 
-  rubor; 
-  microexpresiones. 

### Prueba

Generar:

-  sonrisa; 
-  tristeza; 
-  enojo; 
-  sorpresa; 
-  vergüenza; 
-  confusión; 
-  sarcasmo. 

Cada estado debe resultar visualmente distinguible.

---

## 2. Engineering expansion

Implement a facial control layer independent of individual clips, with constraints, smoothing, priorities, and procedural variation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-17/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 18 — LIP SYNC

## 1. Original scope

# 18. LIP SYNC

La boca debe sincronizarse con la voz.

No depender solamente de animaciones pregrabadas.

Utilizar:

```
```

```
AUDIO
 ↓
PHONEMES / VISEMES
 ↓
MOUTH SHAPES
 ↓
FACIAL RIG
```

### Prueba

Probar frases rápidas, lentas y diferentes idiomas.

La boca no debe quedar adelantada o atrasada perceptiblemente.

---

## 2. Engineering expansion

Implement phoneme/viseme timing with coarticulation, silence handling, latency compensation, and language-specific mappings.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-18/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 19 — EYES / GAZE

## 1. Original scope

# 19. EYES / GAZE

Crear sistema de mirada.

El personaje debe poder:

-  mirar al usuario; 
-  apartar la mirada; 
-  mirar hacia un objeto; 
-  parpadear; 
-  cambiar atención; 
-  hacer eye contact. 

### Prueba

Durante conversación normal no debe parecer que está mirando fijamente como una estatua.

---

## 2. Engineering expansion

Implement gaze targets, saccades, blink timing, attention priorities, camera/user targeting, and natural gaze breaks.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-19/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 20 — BODY LANGUAGE

## 1. Original scope

# 20. BODY LANGUAGE

Crear sistema de:

-  cabeza; 
-  cuello; 
-  hombros; 
-  brazos; 
-  manos; 
-  torso; 
-  postura. 

### Prueba

El personaje debe poder:

-  señalar; 
-  cruzar brazos; 
-  saludar; 
-  reír; 
-  encogerse de hombros; 
-  asentir; 
-  negar; 
-  cambiar postura. 

---

## 2. Engineering expansion

Build layered body-language control with priority arbitration so idle, conversational, scene, and navigation behaviors do not conflict.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-20/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 21 — MICROEXPRESIONES

## 1. Original scope

# 21. MICROEXPRESIONES

Implementar expresiones de baja intensidad.

Ejemplo:

```
```

```
smile = 0.17
eyebrow = 0.11
eye_contact = 0.87
head_tilt = 0.08
```

### Prueba

Conversación de 5 minutos sin repetir exactamente la misma animación facial.

---

## 2. Engineering expansion

Generate bounded micro-variation with anti-repetition and deterministic seeds for regression testing.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-21/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 22 — SEMANTIC ANIMATION ENGINE

## 1. Original scope

# 22. SEMANTIC ANIMATION ENGINE

Este es un punto crítico.

El LLM no debe ordenar:

> "play animation 14".

Debe producir información semántica:

```
```

```
emotion = amused
intensity = 0.65
intent = tease
gesture = subtle
gaze = direct
energy = medium
```

El Animation Engine decide cómo representarlo.

### Prueba

Decir la misma frase en cinco contextos.

El personaje debe reaccionar de manera diferente según el contexto.

---

## 2. Engineering expansion

Define a versioned semantic-animation schema. Models emit intent-level parameters only; the runtime resolves them into approved behaviors.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-22/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 23 — ANIMACIÓN GENERATIVA / PROCEDURAL

## 1. Original scope

# 23. ANIMACIÓN GENERATIVA / PROCEDURAL

Combinar:

-  animaciones base; 
-  procedural animation; 
-  blending; 
-  IK; 
-  facial animation; 
-  gestures; 
-  physics cuando corresponda. 

### Objetivo

Evitar que el personaje parezca un muñeco que ejecuta clips.

### Prueba

Conversación de 15 minutos.

Registrar repetición de movimientos.

---

## 2. Engineering expansion

Combine animation graphs, procedural overlays, blending, IK, constraints, and selective physics with platform performance budgets.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-23/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 24 — SISTEMA DE ESTADO FÍSICO DEL PERSONAJE

## 1. Original scope

# 24. SISTEMA DE ESTADO FÍSICO DEL PERSONAJE

Crear:

```
```

```
posture
energy
position
orientation
activity
attention
```

Ejemplo:

```
```

```
activity = sitting
energy = 0.32
attention = user
mood = calm
```

Esto permitirá continuidad física.

---

# FASE III — APARIENCIA Y MUNDO

## 2. Engineering expansion

Persist physical state separately from conversation state. Define authoritative ownership, serialization, update frequency, and reconnect reconciliation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-24/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 25 — CLOSET / WARDROBE ENGINE

## 1. Original scope

# 25. CLOSET / WARDROBE ENGINE

Aquí entra una de nuestras mayores diferencias.

Cada personaje tendrá un closet.

```
```

```
CASUAL
FORMAL
SPORT
SUMMER
WINTER
EVENING
SLEEPWEAR
WORK
VACATION
DATE
```

Cada outfit será un asset independiente.

### Prueba

Cambiar ropa sin cambiar:

-  personalidad; 
-  memoria; 
-  voz; 
-  identidad; 
-  relación. 

---

## 2. Engineering expansion

Create an outfit catalog with fit, layering, compatibility, licensing, version, thumbnail, and platform metadata. Outfit changes must be transactional.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-25/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 26 — CAMBIO DE ROPA INTELIGENTE

## 1. Original scope

# 26. CAMBIO DE ROPA INTELIGENTE

El sistema podrá responder a:

```
```

```
USER REQUEST
TIME
WEATHER
EVENT
LOCATION
PERSONALITY
CONTEXT
```

### Prueba

Decir:

> "Vamos a la playa."

El sistema debe poder sugerir o seleccionar ropa apropiada si el usuario lo permite.

---

## 2. Engineering expansion

Build context-aware clothing recommendations with explicit user controls. Weather/location access must be permissioned and privacy-preserving.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-26/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 27 — PREFERENCIAS DE ROPA

## 1. Original scope

# 27. PREFERENCIAS DE ROPA

Si el usuario dice:

> "Me gusta mucho ese vestido."

Debe poder guardarse como preferencia.

### Prueba

Semanas después:

El sistema puede recordar:

> "Sé que te gustó este estilo."

No debe inventar que al usuario le gustó algo que nunca expresó.

---

## 2. Engineering expansion

Store clothing preferences with provenance and confidence. Users can correct/delete them; inferred preferences must not be presented as explicit facts.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-27/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 28 — SCENE ENGINE

## 1. Original scope

# 28. SCENE ENGINE

Crear entornos 3D.

Primera versión:

-  dormitorio; 
-  sala; 
-  cocina; 
-  oficina; 
-  cafetería; 
-  restaurante; 
-  parque; 
-  playa; 
-  ciudad; 
-  balcón. 

### Prueba

Cambiar escena sin reiniciar el Companion Core.

---

## 2. Engineering expansion

Build modular, versioned scene packages with interaction points, lighting, audio zones, navigation, and performance budgets.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-28/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 29 — WORLD STATE

## 1. Original scope

# 29. WORLD STATE

Cada escena debe poder manejar:

```
```

```
time
lighting
weather
ambient_audio
props
camera
character_position
```

### Prueba

Comparar:

**día / noche**

**sol / lluvia**

**interior / exterior**

Debe existir diferencia visual y ambiental real.

---

## 2. Engineering expansion

Model time, lighting, weather, audio, props, camera, and character position as reproducible world-state snapshots.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-29/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 30 — DATE / EXPERIENCE MODE

## 1. Original scope

# 30. DATE / EXPERIENCE MODE

Crear experiencias preconfiguradas.

Ejemplo:

```
```

```
Date
Movie
Coffee
Beach
Walk
Dinner
Vacation
Relax
```

El sistema debe cambiar:

-  escena; 
-  outfit; 
-  comportamiento; 
-  cámara; 
-  ambiente; 
-  conversación. 

### Prueba

Ejecutar una experiencia completa sin que el personaje pierda identidad.

---

# FASE IV — VIDA Y AUTONOMÍA

## 2. Engineering expansion

Implement experiences as declarative scenarios with transitions, outfit/scene suggestions, camera behavior, conversation context, exit, and recovery.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-30/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 31 — AUTONOMOUS EVENT ENGINE

## 1. Original scope

# 31. AUTONOMOUS EVENT ENGINE

El personaje puede recordar eventos futuros.

Ejemplo:

> "Mañana tengo una entrevista."

Crear:

```
```

```
future_event
date
importance
context
```

Después:

> "¿Cómo te fue?"

### Prueba

Crear 20 eventos.

Verificar:

-  fecha correcta; 
-  recuperación correcta; 
-  no duplicación; 
-  no preguntas equivocadas. 

---

## 2. Engineering expansion

Use a durable, idempotent event scheduler with time-zone correctness, permissions, retries, cancellation, and duplicate prevention.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-31/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 32 — JOURNAL / INNER LIFE

## 1. Original scope

# 32. JOURNAL / INNER LIFE

Crear diario del personaje.

Pero debe quedar claramente separado entre:

**memoria real del usuario**

y

**contenido generado del personaje**.

El personaje puede tener:

-  reflexiones; 
-  actividades; 
-  pensamientos ficticios; 
-  experiencias internas diseñadas. 

### Prueba

Verificar que nunca se presente una ficción como un hecho real del usuario.

---

## 2. Engineering expansion

Separate simulated Companion inner-life data from user facts in storage, APIs, UI, and model context. Mark fictional/internal content explicitly.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-32/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 33 — PROACTIVE MEMORY

## 1. Original scope

# 33. PROACTIVE MEMORY

Permitir que el Companion recuerde acontecimientos importantes y los utilice posteriormente.

Ejemplo:

> "El viernes tengo una cita médica."

Posteriormente:

> "¿Cómo te fue?"

Esto debe ser configurable.

### Prueba

Usuario puede desactivar recuerdos proactivos.

---

# FASE V — MULTIPLATAFORMA

## 2. Engineering expansion

Implement proactive-memory policies, quiet hours, relevance thresholds, anti-spam limits, auditability, and user disable controls.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-33/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 34 — MOBILE

## 1. Original scope

# 34. MOBILE

Crear clientes:

### iOS

### Android

Funciones:

-  chat; 
-  voz; 
-  personaje 3D; 
-  animación; 
-  outfits; 
-  escenas; 
-  memoria; 
-  configuración; 
-  suscripción. 

### Pruebas

Múltiples dispositivos reales.

No aceptar únicamente emuladores.

---

## 2. Engineering expansion

Treat iOS/Android as production clients with secure storage, lifecycle handling, permissions, push, audio, rendering budgets, crash reporting, and real-device tests.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-34/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 35 — DESKTOP — WINDOWS Y macOS

## 1. Original scope

# 35. DESKTOP — WINDOWS Y macOS

Aquí incorporamos específicamente tu nueva idea.

Crear aplicación de escritorio real.

Debe soportar:

### Full Screen

Experiencia inmersiva.

### Windowed

Ventana normal.

### Floating Companion

Personaje flotante.

### Overlay

Personaje encima de otras ventanas cuando el usuario lo habilite.

### Minimal Mode

Personaje pequeño + voz.

### Pruebas

Cambiar entre todos los modos sin pérdida de sesión.

---

## 2. Engineering expansion

Build Windows/macOS through shared Core contracts plus platform adapters. Define windowing, tray/menu-bar, permissions, GPU handling, updates, and uninstall behavior.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-35/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 36 — DESKTOP IMMERSIVE MODE

## 1. Original scope

# 36. DESKTOP IMMERSIVE MODE

La PC debe aprovechar la pantalla grande.

El personaje puede ocupar gran parte del monitor.

Debe existir:

-  cámara configurable; 
-  cuerpo completo; 
-  iluminación avanzada; 
-  escenarios; 
-  outfits; 
-  audio espacial cuando corresponda; 
-  conversación de voz; 
-  interacción. 

### Prueba

Conversación de 30 minutos en PC.

Evaluar:

-  FPS; 
-  temperatura; 
-  memoria; 
-  GPU; 
-  latencia; 
-  estabilidad. 

---

## 2. Engineering expansion

Create immersive desktop rendering with quality tiers, frame-time budgets, dynamic LOD/resolution, audio routing, and resource safeguards.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-36/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 37 — DESKTOP COMPANION MODE

## 1. Original scope

# 37. DESKTOP COMPANION MODE

El usuario puede trabajar mientras el Companion permanece presente.

Debe poder:

-  hablar; 
-  escuchar; 
-  aparecer/desaparecer; 
-  minimizar; 
-  reposicionarse; 
-  mostrar notificaciones; 
-  responder por voz. 

### Prueba

Abrir otra aplicación.

Mantener Companion activo.

Verificar que no bloquee el trabajo del usuario ni cause comportamiento inesperado.

---

## 2. Engineering expansion

Create non-invasive floating mode with explicit always-on-top permission, repositioning, hide/mute, privacy indicators, and suspend behavior.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-37/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 38 — WEB + TELEGRAM + ECOSISTEMA COMPLETO

## 1. Original scope

# 38. WEB + TELEGRAM + ECOSISTEMA COMPLETO

Este último punto engloba la conectividad externa y completa el sistema.

## Web

El usuario puede iniciar sesión y continuar la relación.

## Telegram

Debe existir integración mediante API oficial.

Arquitectura:

```
```

```
TELEGRAM
   ↓
WEBHOOK
   ↓
COMPANION BACKEND
   ↓
MEMORY
   ↓
REASONING
   ↓
RESPONSE
   ↓
TELEGRAM
```

El Telegram del usuario y la aplicación deben compartir:

-  identidad; 
-  memoria; 
-  relación; 
-  historial permitido; 
-  preferencias. 

### Prueba final

1.  Hablar en PC. 
2.  Continuar en iPhone. 
3.  Continuar en Android. 
4.  Continuar en Web. 
5.  Continuar en Telegram. 
6.  Volver a PC. 

El personaje debe saber que **es la misma relación**.

---

# PERO AQUÍ NO TERMINA EL PROYECTO

Los 38 puntos son el núcleo funcional.

Ahora vienen los sistemas que el constructor debe implementar alrededor de esos 38 puntos para que realmente tengamos un producto comercial serio.

---

## 2. Engineering expansion

Build Web and Telegram as independent adapters over the same backend contracts. Use official APIs, webhook verification/deduplication, and explicit account linking.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-38/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 39 — SISTEMA DE CUENTAS

## 1. Original scope

# 39. SISTEMA DE CUENTAS

Crear:

-  registro; 
-  login; 
-  recuperación; 
-  sesiones; 
-  dispositivos; 
-  seguridad; 
-  cierre de sesión. 

### Prueba

Iniciar sesión en varios dispositivos.

Cerrar sesión en uno.

Los demás deben permanecer correctamente controlados.

---

## 2. Engineering expansion

Use standards-based authentication with MFA-ready architecture, session/device management, revocation, recovery, deletion, and audit events.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-39/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 40 — SINCRONIZACIÓN

## 1. Original scope

# 40. SINCRONIZACIÓN

Todo debe sincronizarse:

```
```

```
Memory
Personality
Outfit
Scene
Preferences
Relationship
Conversation
Settings
```

### Prueba

Cambiar outfit en PC.

Abrir teléfono.

Debe aparecer correctamente.

---

## 2. Engineering expansion

Use versioned event/state synchronization with idempotency and conflict resolution. Define server authority and client reconciliation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-40/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 41 — SISTEMA DE IDIOMAS

## 1. Original scope

# 41. SISTEMA DE IDIOMAS

Debe soportar inicialmente:

-  inglés; 
-  español. 

Arquitectura preparada para más.

El personaje debe poder cambiar de idioma sin perder personalidad.

### Prueba

Conversación bilingüe.

Debe mantener contexto.

---

## 2. Engineering expansion

Use locale-aware UI, date/time/number formatting, language-specific voice/viseme profiles, and personality-preserving bilingual behavior.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-41/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 42 — VISIÓN

## 1. Original scope

# 42. VISIÓN

Crear Vision Engine opcional.

Puede analizar:

-  imágenes; 
-  cámara; 
-  pantalla; 
-  documentos permitidos. 

Siempre bajo permisos explícitos.

### Prueba

El usuario desactiva cámara.

El sistema debe ser incapaz de utilizarla.

---

## 2. Engineering expansion

Implement Vision as permission-gated, denial-by-default capability with capture indicators, ephemeral processing where possible, retention controls, and provider isolation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-42/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 43 — PERSONALIDAD ADAPTATIVA

## 1. Original scope

# 43. PERSONALIDAD ADAPTATIVA

El Companion adapta:

-  vocabulario; 
-  humor; 
-  profundidad; 
-  tono; 
-  velocidad; 
-  nivel de formalidad. 

Pero mantiene su identidad.

### Prueba

Tres perfiles de usuario completamente diferentes.

Verificar adaptación sin pérdida de personalidad.

---

## 2. Engineering expansion

Adapt to users through bounded measurable signals while preserving stable personality anchors. Version adaptive policies and test drift.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-43/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 44 — SISTEMA DE VOZ INTERRUPTIBLE

## 1. Original scope

# 44. SISTEMA DE VOZ INTERRUPTIBLE

El usuario debe poder:

> hablar mientras el Companion habla.

El Companion debe:

-  detectar interrupción; 
-  detener TTS; 
-  escuchar; 
-  actualizar contexto. 

### Prueba

Interrumpirlo 20 veces.

No debe quedar atrapado reproduciendo audio antiguo.

---

## 2. Engineering expansion

Make speech output cancellable and audio pipelines interruptible through barge-in detection, cancellation tokens, stream teardown, and state reconciliation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-44/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 45 — LATENCIA Y RENDIMIENTO

## 1. Original scope

# 45. LATENCIA Y RENDIMIENTO

Crear dashboard interno.

Medir:

```
```

```
STT
LLM
Memory Retrieval
TTS
Animation
Rendering
Network
Total Latency
```

### Objetivo

Optimizar continuamente.

No aceptar:

> "funciona"

sin métricas.

---

## 2. Engineering expansion

Create observability for latency, errors, model usage, costs, FPS, memory, GPU/CPU, and provider health. Define SLOs/SLIs from benchmarks.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-45/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 46 — ESCALABILIDAD

## 1. Original scope

# 46. ESCALABILIDAD

El backend debe estar preparado para:

```
```

```
100 usuarios
1,000
10,000
100,000
1,000,000+
```

El constructor debe documentar cómo escala cada componente.

### Prueba

Pruebas de carga progresivas.

---

## 2. Engineering expansion

Use stateless services where possible, queues, caching, partitioning, object storage, autoscaling, and progressive load testing. Document the cost curve.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-46/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 47 — SEGURIDAD

## 1. Original scope

# 47. SEGURIDAD

Implementar:

-  cifrado; 
-  autenticación; 
-  autorización; 
-  separación de usuarios; 
-  protección de APIs; 
-  rate limiting; 
-  logs; 
-  detección de abuso. 

### Prueba

Intentar acceder a memoria de otro usuario.

Resultado obligatorio:

**DENIED.**

---

## 2. Engineering expansion

Threat-model account takeover, broken authorization, memory leakage, prompt injection, malicious tool input, webhook abuse, insecure storage, secrets, supply chain, and DoS.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-47/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 48 — PRIVACIDAD

## 1. Original scope

# 48. PRIVACIDAD

El usuario debe poder controlar:

-  memoria; 
-  voz; 
-  cámara; 
-  pantalla; 
-  datos; 
-  historial. 

Debe poder solicitar eliminación de datos conforme a las obligaciones legales aplicables.

---

## 2. Engineering expansion

Implement data classification, minimization, retention/deletion, export where required, consent, privacy settings, vendor review, and region-aware compliance hooks.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-48/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 49 — CONTROLES DE EDAD Y SEGURIDAD

## 1. Original scope

# 49. CONTROLES DE EDAD Y SEGURIDAD

Como quieres conversaciones adultas, el producto debe tener desde arquitectura inicial:

-  age gating apropiado; 
-  políticas de contenido; 
-  protección de menores; 
-  consentimiento; 
-  controles de privacidad; 
-  mecanismos de reporte; 
-  límites para contenido ilegal o abusivo. 

Nunca diseñar el sistema para sexualizar menores ni personajes que aparenten ser menores.

Y no utilizar clonación de rostro/voz de personas reales sin autorización.

---

## 2. Engineering expansion

Make safety a shared platform service: age gating, no minors, consent boundaries, reporting/blocking, prohibited-content handling, and authorization for real-person voice/face.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-49/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 50 — CHARACTER CMS

## 1. Original scope

# 50. CHARACTER CMS

Necesitamos un panel administrativo donde podamos crear personajes sin modificar el código principal.

Ejemplo:

```
```

```
CREATE CHARACTER
│
├── Name
├── Personality
├── Voice
├── Face
├── Body
├── Hair
├── Outfits
├── Scenes
├── Interests
├── Values
├── Behavior
└── System Configuration
```

Esto será fundamental para crear nuestros:

# 10 personajes femeninos + 5 masculinos

---

## 2. Engineering expansion

Create versioned Character CMS with draft/review/publish/rollback, schema validation, permissions, previews, and audit logs.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-50/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 51 — ASSET MANAGEMENT

## 1. Original scope

# 51. ASSET MANAGEMENT

Sistema para administrar:

-  modelos 3D; 
-  ropa; 
-  cabello; 
-  texturas; 
-  animaciones; 
-  escenarios; 
-  sonidos; 
-  voces. 

Cada asset debe tener:

```
```

```
ID
VERSION
LICENSE
AUTHOR
STATUS
COMPATIBILITY
```

---

## 2. Engineering expansion

Create a license-aware asset registry. Every production asset needs provenance, owner/vendor, license, version, compatibility, and approval status.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-51/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 52 — PROMPT / AI CONFIGURATION CMS

## 1. Original scope

# 52. PROMPT / AI CONFIGURATION CMS

No poner prompts críticos directamente en código.

Crear versiones.

```
```

```
Prompt v1
Prompt v2
Prompt v3
```

Permitir rollback.

### Prueba

Cambiar configuración de personalidad sin recompilar la aplicación.

---

## 2. Engineering expansion

Create versioned AI configuration with environments, approvals, rollback, experiment flags, provider/model metadata, and reproducible snapshots. Never store secrets in prompts/source.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-52/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 53 — ANALYTICS

## 1. Original scope

# 53. ANALYTICS

Medir:

-  retención; 
-  sesiones; 
-  duración; 
-  conversaciones; 
-  uso de voz; 
-  personajes más utilizados; 
-  outfits; 
-  escenas; 
-  errores; 
-  latencia. 

Nunca utilizar datos sensibles de manera indebida.

---

## 2. Engineering expansion

Implement privacy-aware analytics with event schemas, consent gating, sampling, retention, and separation of operational telemetry from content data.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-53/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 54 — SUSCRIPCIONES

## 1. Original scope

# 54. SUSCRIPCIONES

Crear arquitectura para:

```
```

```
Free
Premium
Pro
```

Los nombres y precios pueden definirse después.

Debe controlar:

-  uso de voz; 
-  modelos; 
-  memoria; 
-  personajes; 
-  outfits; 
-  escenas; 
-  calidad; 
-  funciones premium. 

---

## 2. Engineering expansion

Build entitlement-based subscriptions with server authority, receipt validation, webhook idempotency, grace periods, refunds, revocation, and entitlement caching.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-54/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 55 — SISTEMA DE NOTIFICACIONES

## 1. Original scope

# 55. SISTEMA DE NOTIFICACIONES

Ejemplos:

> "Yuki tiene algo que decirte."

o

> "¿Quieres continuar la conversación?"

Pero deben existir controles para evitar comportamiento invasivo.

### Prueba

Usuario desactiva notificaciones.

No recibir ninguna notificación promocional/no esencial fuera de lo permitido.

---

## 2. Engineering expansion

Implement notification categories, preferences, quiet hours, deduplication, rate limits, localization, and transactional/promotional separation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-55/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 56 — SISTEMA DE RECUPERACIÓN

## 1. Original scope

# 56. SISTEMA DE RECUPERACIÓN

Si:

-  servidor cae; 
-  conexión se pierde; 
-  app se cierra; 
-  PC se reinicia; 

la conversación debe poder recuperarse.

### Prueba

Interrumpir conexión durante conversación.

Restaurarla.

Verificar continuidad.

---

## 2. Engineering expansion

Add retries, resumable sessions, idempotency keys, checkpointing, offline queues where appropriate, provider fallback, and disaster-recovery procedures.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-56/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 57 — SISTEMA DE LOGS Y DIAGNÓSTICO

## 1. Original scope

# 57. SISTEMA DE LOGS Y DIAGNÓSTICO

Cada módulo debe producir logs técnicos.

Pero jamás registrar indiscriminadamente información privada.

Crear:

```
```

```
ERROR
WARNING
INFO
PERFORMANCE
SECURITY
```

---

## 2. Engineering expansion

Centralize structured logs, traces, metrics, correlation IDs, redaction, retention, alerting, and incident context. Never log secrets or unrestricted private content.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-57/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 58 — SISTEMA DE PRUEBAS AUTOMÁTICAS

## 1. Original scope

# 58. SISTEMA DE PRUEBAS AUTOMÁTICAS

El constructor deberá crear tests para:

-  memoria; 
-  usuarios; 
-  autenticación; 
-  personalidad; 
-  relaciones; 
-  API; 
-  sincronización; 
-  voz; 
-  animación; 
-  pagos; 
-  Telegram; 
-  seguridad. 

---

## 2. Engineering expansion

Create unit, integration, contract, end-to-end, security, performance, and AI-evaluation tests. Use deterministic fixtures where possible.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-58/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 59 — PRUEBAS DE REGRESIÓN

## 1. Original scope

# 59. PRUEBAS DE REGRESIÓN

Cada vez que se cambie un sistema importante:

```
```

```
BUILD
 ↓
AUTOMATED TESTS
 ↓
REGRESSION TEST
 ↓
MANUAL TEST
 ↓
APPROVAL
```

Una nueva función no puede romper memoria, voz o animación.

---

## 2. Engineering expansion

Maintain a regression suite tied to every acceptance gate. Shared-contract changes automatically trigger affected downstream suites.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-59/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 60 — PRUEBA DE REALIDAD DEL COMPANION

## 1. Original scope

# 60. PRUEBA DE REALIDAD DEL COMPANION

Esta será una de las pruebas más importantes.

Seleccionar un personaje.

Mantener una conversación de mínimo:

**30–60 minutos.**

Probar:

-  cambios de tema; 
-  recuerdos; 
-  emociones; 
-  interrupciones; 
-  humor; 
-  voz; 
-  gestos; 
-  ropa; 
-  escenario; 
-  preguntas inesperadas. 

El equipo debe evaluar:

### ¿Parece una persona virtual coherente?

No:

> "¿El código funciona?"

Sino:

> **"¿La experiencia realmente se siente viva?"**

---

## 2. Engineering expansion

Create a repeatable human evaluation protocol for memory, personality, emotion, latency, animation repetition, naturalness, and failure classification.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-60/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 61 — PRUEBA DE CONTINUIDAD DE 7 DÍAS

## 1. Original scope

# 61. PRUEBA DE CONTINUIDAD DE 7 DÍAS

Crear un usuario de prueba.

Día 1:

Conversación.

Día 2:

Nuevo tema.

Día 3:

Recordar algo.

Día 4:

Cambiar ropa.

Día 5:

Cambiar dispositivo.

Día 6:

Telegram.

Día 7:

PC.

El personaje debe mantener:

**identidad + memoria + relación + personalidad.**

---

## 2. Engineering expansion

Run controlled seven-day continuity tests for facts, events, deletion, temporal reasoning, relationships, and cross-device reconciliation.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-61/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 62 — PRUEBA MULTIPLATAFORMA FINAL

## 1. Original scope

# 62. PRUEBA MULTIPLATAFORMA FINAL

Debe ejecutarse:

```
```

```
iPhone
↓
Android
↓
Windows
↓
macOS
↓
Web
↓
Telegram
```

El personaje debe permanecer consistente.

---

## 2. Engineering expansion

Run a complete device/platform matrix including voice, memory, sync, Telegram, failure, recovery, upgrade, and account-linking scenarios.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-62/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 63 — PRUEBA DE PERSONAJE

## 1. Original scope

# 63. PRUEBA DE PERSONAJE

Crear inicialmente:

### 1 personaje completamente terminado.

No construir 15 personajes mediocres.

El primer personaje debe demostrar:

-  cuerpo; 
-  rostro; 
-  voz; 
-  memoria; 
-  personalidad; 
-  emociones; 
-  outfits; 
-  escenas; 
-  animación; 
-  PC; 
-  móvil; 
-  Telegram. 

---

## 2. Engineering expansion

Freeze the reference Companion as the quality benchmark. Create reusable fixtures and a character template only after all gates pass.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-63/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 64 — ESCALAMIENTO A LOS 15 PERSONAJES

## 1. Original scope

# 64. ESCALAMIENTO A LOS 15 PERSONAJES

Después de aprobar el personaje piloto:

### 10 femeninos

### 5 masculinos

Cada uno deberá tener:

-  identidad; 
-  personalidad; 
-  voz; 
-  apariencia; 
-  historia; 
-  intereses; 
-  comportamiento; 
-  ropa inicial; 
-  escenas compatibles. 

### Prueba

Cambiar entre personajes.

La memoria de uno jamás puede mezclarse con otro.

---

## 2. Engineering expansion

Scale through data-driven character definitions and asset bundles, not code forks. Each character gets automated identity and memory-isolation tests.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-64/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 65 — QUALITY CONTROL

## 1. Original scope

# 65. QUALITY CONTROL

Crear una matriz:

| SistemaFuncionaProbadoRegresiónAprobado |   |   |   |   |
| --------------------------------------- | - | - | - | - |
| Memory                                  | ☐ | ☐ | ☐ | ☐ |
| Voice                                   | ☐ | ☐ | ☐ | ☐ |
| Animation                               | ☐ | ☐ | ☐ | ☐ |
| PC                                      | ☐ | ☐ | ☐ | ☐ |
| Mobile                                  | ☐ | ☐ | ☐ | ☐ |
| Telegram                                | ☐ | ☐ | ☐ | ☐ |
| Personality                             | ☐ | ☐ | ☐ | ☐ |
| Relationship                            | ☐ | ☐ | ☐ | ☐ |
| Wardrobe                                | ☐ | ☐ | ☐ | ☐ |
| Scenes                                  | ☐ | ☐ | ☐ | ☐ |

---

## 2. Engineering expansion

Create a quality matrix with severity, owner, evidence, pass/fail history, and waiver rules. No critical/high unresolved defects at release.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-65/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 66 — BETA INTERNA

## 1. Original scope

# 66. BETA INTERNA

Antes de público:

### 10–20 testers internos.

Cada tester debe utilizar:

-  móvil; 
-  PC; 
-  voz; 
-  texto; 
-  distintos personajes; 
-  distintos idiomas. 

Registrar:

-  errores; 
-  latencia; 
-  respuestas incoherentes; 
-  memoria incorrecta; 
-  movimientos repetitivos; 
-  problemas de voz; 
-  problemas de UI. 

---

## 2. Engineering expansion

Run internal beta with feedback taxonomy, crash/latency monitoring, privacy review, support process, and daily triage.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-66/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 67 — BETA EXTERNA

## 1. Original scope

# 67. BETA EXTERNA

Después de corregir:

Grupo mayor de usuarios.

Aquí se medirá:

```
```

```
Retention
Session Length
Conversation Frequency
Voice Usage
Character Preference
Memory Satisfaction
Animation Satisfaction
PC Usage
Mobile Usage
```

---

## 2. Engineering expansion

Run staged external beta with cohorts, rollback, abuse monitoring, retention analysis, and incident response.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-67/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 68 — PRUEBA FINAL DE PRODUCTO

## 1. Original scope

# 68. PRUEBA FINAL DE PRODUCTO

Antes de lanzar:

El equipo debe responder afirmativamente a:

### ¿El personaje recuerda?

### ¿Razona?

### ¿Mantiene personalidad?

### ¿Se adapta al usuario?

### ¿Tiene emociones?

### ¿Mueve labios correctamente?

### ¿Tiene gestos?

### ¿Tiene microexpresiones?

### ¿Puede cambiar de ropa?

### ¿Puede cambiar de escenario?

### ¿Puede vivir en PC?

### ¿Puede vivir en teléfono?

### ¿Puede continuar por Telegram?

### ¿Recuerda entre dispositivos?

### ¿Tiene seguridad?

### ¿Tiene privacidad?

### ¿Escala?

### ¿Tenemos pruebas?

---

## 2. Engineering expansion

Run a release audit across functionality, security, privacy, AI behavior, billing, performance, platform requirements, and operational readiness.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-68/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 69 — RELEASE CANDIDATE

## 1. Original scope

# 69. RELEASE CANDIDATE

Crear:

```
```

```
RC1
↓
Testing
↓
Fix
↓
RC2
↓
Testing
↓
Final
```

No publicar una versión simplemente porque "ya funciona".

---

## 2. Engineering expansion

Use immutable release artifacts, versioned builds, migration checks, rollback plans, release notes, and staged deployment.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-69/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# POINT 70 — DOCUMENTACIÓN FINAL

## 1. Original scope

# 70. DOCUMENTACIÓN FINAL

El constructor debe entregar:

### Código fuente

### Arquitectura

### APIs

### Base de datos

### Infraestructura

### Modelos

### Assets

### Prompts

### Configuración AI

### Sistema de memoria

### Sistema de animación

### Sistema de voz

### Aplicaciones

### Panel administrativo

### CI/CD

### Seguridad

### Manual de despliegue

### Manual de mantenimiento

### Manual para agregar personajes

### Manual para agregar outfits

### Manual para agregar escenas

### Manual para agregar nuevas plataformas

---

# ORDEN DE EJECUCIÓN OBLIGATORIO

El constructor debe trabajar así:

```
```

```
01 Arquitectura
      ↓
02 Multiplatform Core
      ↓
03 Identity
      ↓
04 Personality
      ↓
05 User Model
      ↓
06 Memory
      ↓
07 Long-Term Memory
      ↓
08 Reasoning
      ↓
09 Relationship
      ↓
10 Emotion
      ↓
11 Voice Input
      ↓
12 Voice Output
      ↓
13 Real-Time Conversation
      ↓
14 3D Character
      ↓
15 Visual Identity
      ↓
16 Facial System
      ↓
17 Lip Sync
      ↓
18 Eye System
      ↓
19 Body Language
      ↓
20 Microexpressions
      ↓
21 Semantic Animation
      ↓
22 Procedural Animation
      ↓
23 Physical State
      ↓
24 Wardrobe
      ↓
25 Smart Clothing
      ↓
26 Clothing Preferences
      ↓
27 Scenes
      ↓
28 World State
      ↓
29 Experience Mode
      ↓
30 Autonomous Events
      ↓
31 Journal
      ↓
32 Proactive Memory
      ↓
33 Mobile
      ↓
34 Windows/macOS
      ↓
35 Desktop Immersive
      ↓
36 Desktop Companion
      ↓
37 Web
      ↓
38 Telegram
      ↓
39 Accounts
      ↓
40 Sync
      ↓
41 Languages
      ↓
42 Vision
      ↓
43 Adaptive Personality
      ↓
44 Interruptible Voice
      ↓
45 Performance
      ↓
46 Scalability
      ↓
47 Security
      ↓
48 Privacy
      ↓
49 Safety/Age Controls
      ↓
50 Character CMS
      ↓
51 Asset Management
      ↓
52 AI Configuration CMS
      ↓
53 Analytics
      ↓
54 Subscriptions
      ↓
55 Notifications
      ↓
56 Recovery
      ↓
57 Diagnostics
      ↓
58 Automated Testing
      ↓
59 Regression
      ↓
60 Reality Test
      ↓
61 Seven-Day Test
      ↓
62 Cross-Platform Test
      ↓
63 First Character
      ↓
64 15 Characters
      ↓
65 Quality Control
      ↓
66 Internal Beta
      ↓
67 External Beta
      ↓
68 Final Product Test
      ↓
69 Release Candidate
      ↓
70 Production
      ↓
71 Documentation
```

---

# Y ESTA ES LA ORDEN QUE YO LE DARÍA LITERALMENTE AL CONSTRUCTOR

> **Construya el sistema como una plataforma multiplataforma de AI Companions persistentes, no como una aplicación de chat convencional.**
>
> El núcleo del sistema deberá ser un **Companion Core** independiente del cliente. Cada Companion debe existir como una entidad persistente con identidad, personalidad, memoria, relación, estado emocional, voz, apariencia, cuerpo, actividades y configuración propia.
>
> Los clientes iOS, Android, Windows, macOS, Web y Telegram serán interfaces diferentes conectadas al mismo Companion Core.
>
> **No avance al siguiente módulo hasta que el módulo actual haya pasado todas las pruebas de aceptación especificadas.**
>
> Cada módulo debe entregar código funcional, documentación, pruebas automatizadas cuando corresponda, pruebas manuales, métricas y evidencia de funcionamiento.
>
> Si alguna prueba falla, el estado será **FAILED → FIX → RETEST → PASS**. Está prohibido marcar un módulo como terminado simplemente porque compila o porque puede demostrarse parcialmente.
>
> Primero construya la infraestructura y el Companion Core. Después construya personalidad, User Model, memoria, razonamiento y relación. Posteriormente implemente voz y conversación en tiempo real. Después construya el avatar 3D persistente, facial rig, lip sync, ojos, lenguaje corporal, microexpresiones y Semantic Animation Engine.
>
> Posteriormente implemente Wardrobe Engine, escenarios 3D, World State y Experience Mode.
>
> Después implemente autonomía, eventos futuros, diario y memoria proactiva.
>
> Posteriormente implemente los clientes móviles y de escritorio, asegurando que Windows y macOS no sean adaptaciones posteriores sino clientes contemplados desde la arquitectura inicial.
>
> En PC debe existir Full Screen Mode, Windowed Mode, Floating Companion, Overlay y Minimal Mode. El PC debe aprovechar GPU, pantalla grande, cámara, micrófono, audio y capacidades superiores de hardware cuando estén disponibles.
>
> Después implemente Web y Telegram, garantizando que la identidad, memoria y relación sean exactamente las mismas entre plataformas.
>
> Posteriormente implemente cuentas, sincronización, idiomas, visión, personalidad adaptativa, conversación interrumpible, rendimiento, escalabilidad, seguridad, privacidad, controles de edad, Character CMS, Asset Management, AI Configuration CMS, Analytics, Subscription System, Notifications y Recovery.
>
> Después construya el sistema completo de testing, regression testing, quality control, beta y producción.
>
> **No construya los 15 personajes inicialmente. Construya primero un único Companion de referencia completamente terminado.**
>
> Ese Companion deberá demostrar toda la arquitectura: conversación de texto y voz, memoria de largo plazo, razonamiento, personalidad, User Model, relación, emociones, expresiones faciales, lip sync, ojos, brazos, gestos, microexpresiones, cambio de ropa, escenarios, experiencias, PC, móvil, Web y Telegram.
>
> Cuando el Companion de referencia supere todas las pruebas, convierta su arquitectura en una plantilla y cree los otros personajes.
>
> El objetivo final no es producir un chatbot con un avatar.
>
> **El objetivo es crear una persona virtual persistente con cuerpo, voz, personalidad, memoria, relación, apariencia variable y capacidad de existir de manera coherente a través de múltiples dispositivos y plataformas.**
>
> La experiencia final debe producir la sensación de que el usuario está interactuando con un Companion digital consistente, no con una sucesión de respuestas generadas por un chatbot.

---

## Y hay una última condición que yo pondría en el contrato del proyecto

**NO QUIERO QUE EL CONSTRUCTOR ME ENTREGUE "UNA DEMO BONITA".**

Quiero:

> **un sistema modular, probado, documentado, escalable y mantenible.**

La diferencia es enorme.

Una demo puede hacer que una mujer 3D diga:

> "Hola ❤️"

y mover la boca.

Nuestro sistema debe poder hacer esto:

```
```

```
Usuario
   ↓
habla
   ↓
STT
   ↓
User Model
   ↓
Memory Retrieval
   ↓
Relationship State
   ↓
Current Emotion
   ↓
Reasoning Engine
   ↓
Response
   ↓
TTS
   ↓
Emotion
   ↓
Semantic Animation
   ↓
Facial Animation
   ↓
Lip Sync
   ↓
Body Language
   ↓
3D Character
   ↓
Conversation Memory
   ↓
Future Relationship
```

Y **esa misma persona** debe poder continuar la conversación:

**en el iPhone → Android → PC → Mac → Web → Telegram**, sin convertirse en otra persona.

Ese es el corazón de lo que estamos construyendo.

## 2. Engineering expansion

Publish architecture, APIs, data models, infrastructure, AI/model configuration, asset provenance, CI/CD, runbooks, deployment, maintenance, and expansion manuals.

## 3. Dependencies

All explicitly required upstream points must be PASS. Do not create hidden dependencies outside `BUILD_PLAN.md`.

## 4. Required implementation artifacts

- production code/modules;
- configuration;
- versioned contracts/schemas;
- documentation;
- automated tests where applicable;
- manual acceptance procedure;
- telemetry/metrics where applicable;
- rollback/recovery behavior;
- security/privacy checks where applicable.

## 5. Required test gate

- happy-path test;
- negative-path test;
- timeout/failure/retry test;
- integration/contract test;
- regression suite;
- manual acceptance scenario from the original specification;
- real-device test where the point affects a client;
- evidence saved under `docs/evidence/point-70/`.

## 6. PASS criteria

The point passes only when:
1. the original requirements are satisfied;
2. the engineering expansion is implemented;
3. automated tests pass;
4. manual acceptance passes;
5. no critical/high unresolved defect exists;
6. failure/recovery behavior is verified;
7. documentation is updated;
8. `BUILD_PLAN.md` records PASS and commit SHA;
9. evidence is reproducible.

## 7. Failure criteria

FAIL if the feature only works in a demo, only works on one platform when shared Core behavior is required, loses state on restart/reconnect, leaks data, bypasses authorization, relies on undocumented manual steps, lacks required evidence, or violates a declared performance/security/privacy/license constraint.

## 8. Status

`NOT_STARTED`


---

# K. CROSS-SYSTEM RELEASE TESTS

Before production, run all of these in addition to the 70 point gates:

## Tenant isolation
Multiple users and Companions must never share memory, relationship, preferences, media, entitlements, or sessions.

## Memory
Test exact recall, semantic recall, temporal recall, contradiction, deletion, stale facts, irrelevant-memory suppression, and cross-user leakage.

## Recovery
Force network loss, app termination, PC restart, provider timeout, TTS failure, STT failure, duplicate message, and reconnect.

## Model failure
Force malformed structured output, provider timeout, rate limit, unavailable provider, moderation failure, and context overflow.

## Animation failure
Force missing assets, invalid semantic intent, asset-load failure, low GPU, and low memory.

## Billing
Test expired subscription, refund, revocation, duplicate webhook, delayed webhook, and offline client.

## Reality test
Run a 30–60 minute natural conversation and score:
- coherence;
- memory;
- personality;
- emotion;
- interruption;
- voice;
- gestures;
- microexpressions;
- repetition;
- responsiveness.

## Seven-day test
Test identity + memory + relationship + personality across seven days and multiple platforms.

## Cross-platform test
`iPhone → Android → Windows → macOS → Web → Telegram → PC`

---

# L. RELEASE CHECKPOINTS

Recommended tags:

```text
v0.1-foundation
v0.2-core
v0.3-memory
v0.4-voice
v0.5-avatar
v0.6-world
v0.7-platforms
v0.8-production-systems
v0.9-beta
v1.0-release
```

Only tag after the corresponding gates and regression suite pass.

---

# M. PRODUCTION-READY DEFINITION

The system is not production-ready until:
- all required points PASS;
- critical/high defects are resolved or formally waived;
- security review passes;
- privacy review passes;
- asset/license audit passes;
- AI evaluation passes;
- regression passes;
- real-device platform tests pass;
- backup/restore is tested;
- deployment is reproducible;
- rollback is documented;
- runbooks exist;
- reference Companion passes reality test;
- seven-day continuity passes;
- cross-platform continuity passes.

---

# N. LITERAL BUILDER ORDER

> Build this as a production platform for persistent AI Companions, not as a chatbot demo.
>
> Execute the numbered points sequentially. Do not ask the human to paste the next point.
>
> After PASS, update `BUILD_PLAN.md`, commit, store evidence, run required regression tests, and automatically begin the next point.
>
> If a point fails, fix and retest. Never continue through a failed gate.
>
> Stop only for an unresolvable failure or a major human decision.
>
> Never claim success from compilation alone.
>
> Never allow model output to execute arbitrary code or privileged actions.
>
> Never mix data between users or Companions.
>
> Never copy proprietary code, assets, characters, branding, prompts, models, voices, or protected designs.
>
> First complete one reference Companion. Only after it passes the full matrix should the architecture scale to 10 female and 5 male Companions.
>
> The final product must preserve identity, personality, memory, relationship, emotion, appearance, and continuity across iOS, Android, Windows, macOS, Web, and Telegram.
>
> The objective is not a beautiful demo. The objective is a modular, tested, documented, scalable, maintainable Companion ecosystem.

---

# O. FIRST COMMAND FOR THE BUILDER

Before application implementation:

1. initialize Git repository;
2. create repository structure;
3. create `AGENTS.md`;
4. create `BUILD_PLAN.md`;
5. create `ARCHITECTURE.md`;
6. create `DECISIONS.md`;
7. create `ACCEPTANCE_TESTS.md`;
8. establish CI baseline;
9. establish dev/staging/prod environment strategy;
10. create initial architecture ADR;
11. identify unresolved human decisions;
12. begin Point 01 only after governance baseline exists.

**STATUS: READY FOR CURSOR**


# V3 CONSOLIDATED PRODUCT DIRECTIVE — LIVING COMPANION

> This section supersedes any earlier sequencing or interpretation where it conflicts with the Reference Companion, Reference World, Reference Wardrobe, World & Life Engine, Action Engine, and Living Companion requirements below.

## A. CATEGORY DEFINITION

The product is not a chatbot with an avatar. It is a persistent embodied AI companion platform.

Reference products such as Replika and Animates are functional benchmarks only. Replika publicly demonstrates memory, personality adaptation, avatar customization, clothing/accessories, rooms, activities, calls and long-term personalization; Animates publicly emphasizes real-time voice, emotional presence, persistent memory and continuity across app and messaging. These observations are benchmarks, not implementation specifications. Replika's current public materials explicitly describe layered memory and personalization, while its store includes clothing, accessories, appearance and room items. Animates' current App Store description emphasizes real-time voice, emotional range, memory and continuity across app and messenger. 

Our category is:

# LIVING COMPANION PLATFORM

A Companion that can converse, remember, speak, look, move, dress, inhabit spaces, interact with objects, perform activities, maintain routines, make bounded contextual decisions and continue the same relationship across devices and channels.

## B. NON-NEGOTIABLE SCALING RULE

Do NOT build 15 mediocre characters first.

Build one Reference Companion to exceptional quality.

The same rule applies to content:

- one Reference Wardrobe;
- one Reference Accessory System;
- one Reference Bedroom;
- one Reference Bathroom;
- one Reference Kitchen;
- one Reference Living Room;
- one Reference Office;
- one Reference Outdoor Space;
- one Reference Home;
- one Reference Object Interaction System;
- one Reference Action Library;
- one Reference Activity System;
- one Reference Daily Routine;
- one Reference Autonomous Life cycle.

Only after the complete reference stack passes its quality gate may the system become a reusable template.

The correct progression is:

```text
REFERENCE
  ↓
VALIDATE
  ↓
ABSTRACT
  ↓
TEMPLATE
  ↓
VARIATIONS
  ↓
SCALE
```

## C. NEW MASTER SYSTEM: WORLD & LIFE ENGINE

Add a first-class World & Life Engine to the architecture.

It owns or coordinates:

- current location;
- current activity;
- world time;
- date;
- lighting;
- weather when relevant;
- ambient audio;
- available objects;
- interaction points;
- character physical state;
- current outfit;
- routine state;
- autonomous goals;
- scheduled events;
- scene state;
- activity state;
- user presence;
- context for decisions.

The Companion must not merely appear inside a scene. It must understand the scene as a stateful environment.

## D. WORLD MODEL

Every room is a functional system, not a background.

A room definition must support, where applicable:

```text
room_id
room_type
navigation_mesh
interaction_points
objects
lighting_profiles
ambient_audio
available_activities
supported_actions
camera_points
entry_points
exit_points
privacy_rules
state_variables
asset_versions
```

## E. REFERENCE HOME

Build one complete home before multiplying environments.

Minimum reference home:

- entrance;
- living room;
- kitchen;
- dining area;
- bathroom;
- bedroom;
- closet/walk-in closet;
- office;
- outdoor area.

Each space must contain meaningful interaction opportunities.

The first goal is not asset quantity. The goal is believable continuity between spaces.

## F. REFERENCE BEDROOM

The bedroom must support contextual actions including, where appropriate:

```text
enter
walk
look
sit_floor
sit_bed
sit_edge_of_bed
read
use_phone
relax
conversation
lie_down
adjust_blanket
turn_light_on
turn_light_off
wake_up
sleep
```

The bed is not merely geometry. It is an interaction surface with multiple supported states.

The closet must support:

```text
open
browse
select_outfit
close
```

The mirror must support:

```text
look
inspect_appearance
adjust_clothing
```

## G. REFERENCE KITCHEN

The kitchen should support a meaningful subset of:

- enter;
- open refrigerator;
- retrieve item;
- prepare drink;
- prepare food;
- cook;
- eat;
- drink;
- clean;
- sit;
- converse.

Do not make every object interactive merely to inflate feature count. Prioritize objects that create believable routines.

## H. REFERENCE BATHROOM

The bathroom should support personal-preparation context and appropriate interactions while respecting privacy and safety requirements.

The environment must demonstrate:

- entering;
- mirror interaction;
- sink/personal preparation;
- clothing change context;
- exit;
- lighting/state changes.

## I. REFERENCE LIVING ROOM

The living room should support:

- sit on sofa;
- stand;
- relax;
- watch media;
- read;
- listen to music;
- talk;
- receive the user;
- change lighting;
- interact with selected objects.

## J. ACTION ENGINE

Add a dedicated Action Engine.

An action is not a clip. It is a structured operation:

```text
Action
├── intent
├── preconditions
├── target
├── navigation
├── object_interaction
├── animation_plan
├── emotion_overlay
├── duration
├── priority
├── interruptibility
├── cancellation
├── completion_condition
└── follow_up
```

Example:

```text
GO_TO_BED
→ decide_bedtime_context
→ navigate_to_bedroom
→ enter_room
→ approach_bed
→ sit
→ change posture
→ lie_down
→ adjust_blanket
→ lights_off
→ sleep
```

## K. INTERRUPTIBLE ACTIONS

Any multi-step action must be interruptible unless explicitly marked non-interruptible for technical reasons.

If the user says something while the Companion is walking:

```text
walking
→ detect user input
→ interrupt movement
→ orient toward user
→ listen
→ update context
→ resume / replace action
```

This is a core requirement, not polish.

## L. NAVIGATION ENGINE

Characters must navigate real spaces rather than teleport between predefined poses.

The system should support:

- navmesh/pathfinding;
- obstacle avoidance;
- doors and thresholds;
- interaction points;
- furniture-aware positioning;
- alternative paths;
- animation-aware movement.

## M. OBJECT INTERACTION FRAMEWORK

Every interactive object has:

```text
object_id
state
interaction_points
supported_actions
required_animation_mappings
availability_rules
ownership
visibility
```

The framework must allow adding a new object without rewriting the Companion Core.

## N. WORLD-AWARE COMPANION

The Companion must receive world context before making contextual decisions.

Minimum decision context:

```text
current_time
current_date
current_location
current_activity
current_outfit
energy
emotion
recent_conversation
relationship_state
routine_state
user_presence
available_actions
available_objects
```

## O. TIME-AWARE BEHAVIOR

The Companion should be able to recognize context such as:

```text
late night
morning
meal time
work hours
weekend
special event
```

Time must influence behavior but must not dictate it deterministically.

Personality, relationship and recent events can alter the choice.

## P. AUTONOMOUS LIFE ENGINE

The Companion can perform bounded autonomous activities without a direct command.

Example:

```text
wake
→ bathroom
→ wardrobe
→ dress
→ kitchen
→ coffee
→ work
→ lunch
→ relax
→ evening activity
→ bedroom
→ sleep
```

This is a probabilistic/contextual policy, not a fixed daily script.

## Q. AGENCY

Create a bounded Agency layer that chooses among permitted actions.

Inputs:

```text
current_goal
energy
time
location
emotion
personality
relationship
routine
recent_activity
user_presence
available_actions
world_state
```

Outputs must be structured and validated.

Agency must never bypass safety or authorization.

## R. REFERENCE SLEEP SCENARIO — REQUIRED END-TO-END TEST

At late night, a user says:

> "I think we should go to sleep."

The Companion may respond naturally and choose a sequence such as:

```text
understand intent
→ decide bedtime context
→ go to bedroom
→ choose sleepwear
→ change outfit
→ enter bedroom
→ choose posture
→ sit on bed
→ continue conversation
→ lie down
→ dim/turn off lights
→ sleep
```

The user can interrupt at any point.

The test must validate:

- reasoning;
- time awareness;
- agency;
- navigation;
- wardrobe selection;
- outfit persistence;
- animation;
- object interaction;
- voice;
- emotional state;
- world state;
- interruption;
- memory;
- cross-platform persistence.

## S. REFERENCE WARDROBE

Do not create a large mediocre catalog.

First create one fully finished reference wardrobe.

It must prove:

- garment compatibility;
- layering;
- outfit composition;
- shoes;
- accessories;
- persistent identity;
- physical fit;
- animation compatibility;
- contextual selection;
- change-of-clothes workflow.

Then generalize it into a wardrobe template.

## T. GARMENT INTELLIGENCE

Each garment must have structured metadata such as:

```text
garment_id
category
fit
material
color
style
season
weather
formality
occasion
layer
body_compatibility
rig_compatibility
physics_profile
animation_constraints
personality_affinity
license
version
```

## U. CONTEXTUAL CLOTHING ENGINE

Outfit selection should consider:

- time;
- weather;
- season;
- activity;
- location;
- occasion;
- personality;
- comfort;
- preferences;
- recent outfits;
- available clean garments.

Example:

```text
23:30
+ bedroom
+ sleep intent
→ sleepwear
```

## V. OUTFIT MEMORY

Store explicit and inferred clothing preferences separately.

```text
explicit_preference
inferred_preference
liked
 disliked
frequent_selection
recently_used
```

Inferred preferences must have lower confidence than explicit statements.

## W. CHARACTER AGENCY MUST ALSO BE EXPRESSED PHYSICALLY

Personality is not only dialogue.

Examples:

- a calm Companion may move slowly and use relaxed postures;
- an energetic Companion may choose more active activities;
- a social Companion may seek interaction;
- a private Companion may spend more time independently;
- a playful Companion may select playful objects/activities.

These are configurable tendencies, not stereotypes.

## X. REFERENCE COMPANION GATE

The first Companion cannot pass until all of these are demonstrated together:

### Mind

- identity;
- personality;
- user model;
- memory;
- relationship;
- emotion;
- reasoning;
- safety.

### Body

- hyperrealistic/persistent 3D identity;
- face;
- eyes;
- hair;
- skin;
- voice;
- lip sync;
- gaze;
- body language;
- microexpressions;
- procedural idle.

### World

- navigation;
- bedroom;
- bathroom;
- kitchen;
- living room;
- office;
- outdoor space;
- objects;
- interactions.

### Life

- routine;
- activities;
- autonomous events;
- proactive memory;
- sleep/wake;
- bounded agency.

### Ecosystem

- iOS;
- Android;
- Windows;
- macOS;
- Web;
- Telegram.

## Y. REFERENCE-TO-TEMPLATE CONVERSION

Only after the Reference Gate passes:

```text
Reference Companion
↓
identify reusable systems
↓
separate configuration from code
↓
create templates
↓
create CMS workflows
↓
create asset compatibility rules
↓
create second Companion
```

The second Companion should be substantially faster to produce because the platform already exists.

## Z. 15-COMPANION SCALE

Only after the reference stack passes:

- 10 female Companions;
- 5 male Companions.

Each must differ in:

- identity;
- personality;
- voice;
- appearance;
- history;
- interests;
- behavior;
- clothing preferences;
- environmental preferences;
- routines;
- relationship style.

Never fork the core engine per character.

## AA. REFERENCE HOME → WORLD TEMPLATES

After the Reference Home passes:

```text
Reference Home
↓
Room Templates
↓
World Templates
↓
Variants
```

Future variants may include apartments, luxury homes, beach houses, city homes, studios and other original environments.

## AB. QUALITY PRINCIPLE

The first objective is not maximum content quantity.

It is maximum interaction quality per asset.

Prefer:

```text
1 excellent interactive bed
```

over:

```text
100 decorative beds
```

Prefer:

```text
1 excellent outfit-selection system
```

over:

```text
500 clothing thumbnails with no intelligence
```

## AC. CROSS-SYSTEM INTEGRATION TESTS

Required combined tests include:

### Test 1 — Bedtime

Conversation → time awareness → bedroom → wardrobe → action → sleep.

### Test 2 — Morning

Wake → bathroom → mirror → wardrobe → kitchen → coffee.

### Test 3 — Movie

User asks to watch a movie → living room → sofa → TV → lighting → activity → conversation.

### Test 4 — Cooking

User asks to cook → kitchen → outfit suitability → objects → activity → interruption.

### Test 5 — Cross-device

PC → phone → Telegram → PC while preserving world and relationship state.

### Test 6 — Seven-day continuity

Memories, preferences, events and routines remain coherent.

## AD. LIVING COMPANION REALITY REVIEW

A human evaluator must answer:

1. Does the Companion appear to wait for commands constantly?
2. Do movements feel repetitive?
3. Does gaze feel natural?
4. Does clothing feel contextual?
5. Do rooms have functional purpose?
6. Are actions continuous?
7. Does the Companion know where it is?
8. Does it remember accurately?
9. Does it preserve identity?
10. Does autonomy feel plausible rather than random?
11. Does the voice feel like the same person?
12. Does the relationship feel continuous?
13. Does the environment react to time and context?
14. Can the user interrupt naturally?
15. Does the experience feel fundamentally different from a chatbot with an avatar?

A substantial cluster of negative answers is a FAIL.

## AE. UPDATED BUILD ORDER

The earlier 70-point functional core remains the foundation, but the production sequence is expanded to explicitly build and validate the embodied reference stack before character/content scaling.

```text
FOUNDATION
→ Companion Core
→ Identity
→ Personality
→ User Model
→ Memory
→ Reasoning
→ Relationship
→ Emotion

REAL-TIME
→ STT
→ TTS
→ Streaming
→ Interruptible Voice

REFERENCE BODY
→ 3D Character
→ Visual Identity
→ Facial System
→ Lip Sync
→ Gaze
→ Body Language
→ Microexpressions
→ Semantic Animation
→ Procedural Animation
→ Physical State

REFERENCE INTERACTION
→ Action Engine
→ Navigation
→ Object Interaction

REFERENCE CONTENT
→ Reference Wardrobe
→ Smart Clothing
→ Bedroom
→ Bathroom
→ Kitchen
→ Living Room
→ Office
→ Outdoor
→ Reference Home

WORLD & LIFE
→ World State
→ Time Awareness
→ Activities
→ Experiences
→ Routine Engine
→ Autonomous Events
→ Agency
→ Autonomous Life
→ Journal
→ Proactive Memory

PLATFORMS
→ iOS
→ Android
→ Windows
→ macOS
→ Desktop Immersive
→ Desktop Companion
→ Web
→ Telegram

PRODUCTION SYSTEMS
→ Accounts
→ Sync
→ Languages
→ Vision
→ Security
→ Privacy
→ Safety
→ CMS
→ Assets
→ AI Configuration
→ Analytics
→ Notifications
→ Recovery
→ Diagnostics

VALIDATION
→ Automated Tests
→ Regression
→ Reality Test
→ Seven-Day Test
→ Cross-Platform Test
→ Reference Companion Gate

SCALE
→ Reference-to-Template
→ 10 Female
→ 5 Male
→ More Worlds
→ More Wardrobes
→ More Activities

RELEASE
→ Internal Beta
→ External Beta
→ Final Product Test
→ Release Candidate
→ Production
→ Documentation
```

## AF. FINAL BUILDER COMMAND

> Construya una plataforma de Living AI Companions persistentes, encarnados y multiplataforma. No construya una aplicación de chat convencional y no construya 15 personajes mediocres.
>
> Primero construya un Reference Companion extraordinariamente completo. Construya alrededor de él un Reference Wardrobe, una Reference Home, una biblioteca de acciones, interacciones con objetos, actividades y un ciclo de vida autónomo. Valide todo como un sistema integrado.
>
> El Companion debe conocer su identidad, personalidad, memoria, relación, emoción, ubicación, hora, actividad, ropa y contexto del mundo. Debe poder conversar, escuchar, mirar, moverse, cambiarse de ropa, navegar entre habitaciones, sentarse, acostarse, interactuar con objetos, realizar actividades y tomar decisiones acotadas y seguras.
>
> Cuando sea tarde y el contexto indique descanso, debe poder decidir prepararse para dormir, escoger ropa de dormir, ir al dormitorio, cambiarse, elegir una postura, continuar conversando y finalmente dormir. Si el usuario interviene, la acción debe interrumpirse y adaptarse.
>
> No implementar cada comportamiento como una animación rígida. El LLM debe producir intención semántica y el runtime debe convertirla en acciones físicas coherentes.
>
> No escalar contenido hasta que el sistema de referencia pase todos los gates. Después convertirlo en una plantilla y utilizar esa plantilla para crear los demás Companions, mundos, closets y experiencias.
>
> Replika y Animates son referencias funcionales. No son el límite del producto ni el blueprint de implementación. El objetivo es crear una categoría propia: Living Companion Platform.
>
> Cada módulo debe tener pruebas, métricas y evidencia. Si falla: FAILED → FIX → RETEST → PASS. Nunca continuar por encima de un fallo.

## AG. DEFINICIÓN FINAL DE ÉXITO

El producto alcanza su objetivo cuando un usuario puede conocer a un Companion y, con el tiempo, sentir continuidad porque:

- recuerda correctamente;
- conserva su personalidad;
- reconoce la relación;
- habla con voz consistente;
- reacciona emocionalmente de forma coherente;
- se mueve naturalmente;
- sabe dónde está;
- puede cambiar de ropa de manera contextual;
- utiliza espacios funcionales;
- interactúa con objetos;
- realiza actividades;
- mantiene rutinas flexibles;
- toma decisiones acotadas;
- puede iniciar o continuar comportamientos apropiados;
- puede ser interrumpido naturalmente;
- mantiene continuidad entre PC, móvil, Web y Telegram;
- y puede convertirse en una plantilla escalable sin duplicar la arquitectura.

# FIN DE LA DIRECTIVA V3
