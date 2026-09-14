# Build plan

The repository is the project-management system. Update this file at every gate.

**Governing spec:** [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md). **V3 is authoritative** on Reference-first development, World & Life Engine, Action Engine, and embodied sequencing. Points 00â€“70 remain the functional checklist.

**Status model:** `NOT_STARTED â†’ IN_PROGRESS â†’ TESTING â†’ PASS`. Failure: `FAIL â†’ FIX â†’ RETEST â†’ PASS`.

**Agents must not edit the same files concurrently.**

## Sequence (V3 AE)

`Gate 0 governance â†’ Gate 1 / Companion Core identity â†’ Foundation mind â†’ Real-time (STT/TTS/stream/interrupt) â†’ Reference body â†’ Action/Nav/Objects â†’ Reference wardrobe & home â†’ World & Life â†’ Platforms â†’ Production systems â†’ Validation â†’ Scale â†’ Release`

Do not build 15 companions first.

## Engineering gates

| Gate | Description | Status | Owner | Branch | Commit SHA | Tests | Evidence | Blocker | Timestamp (UTC) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Repository governance baseline | PASS | Primary Engineering Agent | main | pending commit | scripts/check-baseline.ps1 | docs/evidence/gate-0/README.md | none | 2026-09-14 |
| 1 | Companion Core identity contracts (Point 01 intent) | NOT_STARTED | â€” | â€” | â€” | â€” | docs/evidence/point-01/ | Gate 0 must PASS; human approval | â€” |

## Spec points 00â€“70

All points below inherit the spec Definition of Done. None are started in Gate 0.

| Point | Name | Status | Dependencies | Evidence |
| --- | --- | --- | --- | --- |
| 00 | Absolute project rules | NOT_STARTED | â€” | docs/evidence/point-00/ |
| 01 | Product and master architecture / Companion Core | NOT_STARTED | Gate 0, 00 | docs/evidence/point-01/ |
| 02 | Multiplatform architecture | NOT_STARTED | 01 | docs/evidence/point-02/ |
| 03 | Persistent character identity | NOT_STARTED | 01 | docs/evidence/point-03/ |
| 04 | Personality engine | NOT_STARTED | 03 | docs/evidence/point-04/ |
| 05 | User model | NOT_STARTED | 03 | docs/evidence/point-05/ |
| 06 | Memory engine | NOT_STARTED | 05 | docs/evidence/point-06/ |
| 07 | Long-term memory | NOT_STARTED | 06 | docs/evidence/point-07/ |
| 08 | Reasoning and context | NOT_STARTED | 06, 04, 05 | docs/evidence/point-08/ |
| 09 | Relationship engine | NOT_STARTED | 08 | docs/evidence/point-09/ |
| 10 | Emotional state | NOT_STARTED | 08 | docs/evidence/point-10/ |
| 11 | Blended emotions | NOT_STARTED | 10 | docs/evidence/point-11/ |
| 12 | Speech-to-text | NOT_STARTED | 08 | docs/evidence/point-12/ |
| 13 | Text-to-speech | NOT_STARTED | 12 | docs/evidence/point-13/ |
| 14 | Real-time conversation | NOT_STARTED | 12, 13 | docs/evidence/point-14/ |
| 15 | Persistent 3D character | NOT_STARTED | ADR 3D engine | docs/evidence/point-15/ |
| 16 | Persistent visual identity | NOT_STARTED | 15 | docs/evidence/point-16/ |
| 17 | Facial system | NOT_STARTED | 15 | docs/evidence/point-17/ |
| 18 | Lip sync | NOT_STARTED | 13, 17 | docs/evidence/point-18/ |
| 19 | Eyes / gaze | NOT_STARTED | 17 | docs/evidence/point-19/ |
| 20 | Body language | NOT_STARTED | 15 | docs/evidence/point-20/ |
| 21 | Microexpressions | NOT_STARTED | 17 | docs/evidence/point-21/ |
| 22 | Semantic animation engine | NOT_STARTED | 11, 20 | docs/evidence/point-22/ |
| 23 | Procedural animation | NOT_STARTED | 22 | docs/evidence/point-23/ |
| 24 | Physical state | NOT_STARTED | 15 | docs/evidence/point-24/ |
| 25 | Wardrobe engine | NOT_STARTED | 15, 24 | docs/evidence/point-25/ |
| 26 | Contextual clothing | NOT_STARTED | 25 | docs/evidence/point-26/ |
| 27 | Clothing preferences | NOT_STARTED | 25, 06 | docs/evidence/point-27/ |
| 28 | Scene engine | NOT_STARTED | V3: Reference Home first | docs/evidence/point-28/ |
| 29 | World state | NOT_STARTED | 28 | docs/evidence/point-29/ |
| 30 | Experience mode | NOT_STARTED | 29, 25 | docs/evidence/point-30/ |
| 31 | Autonomous event engine | NOT_STARTED | 06, 29 | docs/evidence/point-31/ |
| 32 | Journal / inner life | NOT_STARTED | 06 | docs/evidence/point-32/ |
| 33 | Proactive memory | NOT_STARTED | 31 | docs/evidence/point-33/ |
| 34 | Mobile iOS / Android | NOT_STARTED | Core contracts | docs/evidence/point-34/ |
| 35 | Desktop Windows / macOS | NOT_STARTED | Core contracts | docs/evidence/point-35/ |
| 36 | Desktop immersive | NOT_STARTED | 35 | docs/evidence/point-36/ |
| 37 | Desktop companion mode | NOT_STARTED | 35 | docs/evidence/point-37/ |
| 38 | Web + Telegram | NOT_STARTED | Core contracts | docs/evidence/point-38/ |
| 39 | Accounts | NOT_STARTED | Open: pull earlier? DECISIONS | docs/evidence/point-39/ |
| 40 | Synchronization | NOT_STARTED | 39 | docs/evidence/point-40/ |
| 41 | Languages | NOT_STARTED | 08 | docs/evidence/point-41/ |
| 42 | Vision | NOT_STARTED | Privacy deny-by-default | docs/evidence/point-42/ |
| 43 | Adaptive personality | NOT_STARTED | 04, 05 | docs/evidence/point-43/ |
| 44 | Interruptible voice | NOT_STARTED | 14 | docs/evidence/point-44/ |
| 45 | Latency and performance | NOT_STARTED | 14 | docs/evidence/point-45/ |
| 46 | Scalability | NOT_STARTED | backend | docs/evidence/point-46/ |
| 47 | Security | NOT_STARTED | from architecture start | docs/evidence/point-47/ |
| 48 | Privacy | NOT_STARTED | from architecture start | docs/evidence/point-48/ |
| 49 | Age and safety controls | NOT_STARTED | legal ADR | docs/evidence/point-49/ |
| 50 | Character CMS | NOT_STARTED | Reference gate | docs/evidence/point-50/ |
| 51 | Asset management | NOT_STARTED | 15 | docs/evidence/point-51/ |
| 52 | AI configuration CMS | NOT_STARTED | 08 | docs/evidence/point-52/ |
| 53 | Analytics | NOT_STARTED | 48 | docs/evidence/point-53/ |
| 54 | Subscriptions / entitlements | NOT_STARTED | 39 | docs/evidence/point-54/ |
| 55 | Notifications | NOT_STARTED | 31, 33 | docs/evidence/point-55/ |
| 56 | Recovery | NOT_STARTED | 40 | docs/evidence/point-56/ |
| 57 | Logs and diagnostics | NOT_STARTED | 47, 48 | docs/evidence/point-57/ |
| 58 | Automated tests | NOT_STARTED | ongoing | docs/evidence/point-58/ |
| 59 | Regression | NOT_STARTED | 58 | docs/evidence/point-59/ |
| 60 | Reality test 30â€“60 min | NOT_STARTED | Reference stack | docs/evidence/point-60/ |
| 61 | Seven-day continuity | NOT_STARTED | 60 | docs/evidence/point-61/ |
| 62 | Cross-platform final | NOT_STARTED | 34â€“38 | docs/evidence/point-62/ |
| 63 | Reference character complete | NOT_STARTED | V3 X | docs/evidence/point-63/ |
| 64 | Scale to 15 companions | NOT_STARTED | 63 + templates | docs/evidence/point-64/ |
| 65 | Quality control matrix | NOT_STARTED | 63 | docs/evidence/point-65/ |
| 66 | Internal beta | NOT_STARTED | 65 | docs/evidence/point-66/ |
| 67 | External beta | NOT_STARTED | 66 | docs/evidence/point-67/ |
| 68 | Final product test | NOT_STARTED | 67 | docs/evidence/point-68/ |
| 69 | Release candidate | NOT_STARTED | 68 | docs/evidence/point-69/ |
| 70 | Final documentation | NOT_STARTED | 69 | docs/evidence/point-70/ |

## V3 systems not numbered in 00â€“70 (track here)

| Item | Status | Notes |
| --- | --- | --- |
| Action Engine | NOT_STARTED | After reference body; before Reference Home |
| Navigation Engine | NOT_STARTED | |
| Object Interaction Framework | NOT_STARTED | |
| Reference Home / rooms | NOT_STARTED | Before extra scenes (cafe/beach/city) |
| Agency / Autonomous Life | NOT_STARTED | Bounded, interruptible, policy-controlled |

## Next allowed work after Gate 0 PASS

Stop. Wait for human review. Then Gate 1 only (identity contracts, no UI/3D/paid providers).

