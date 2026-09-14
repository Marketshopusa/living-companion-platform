# Product specification pointer

This file does **not** replace, summarize-away, or fork product requirements.

## Source of truth

All product requirements live in [MASTER_BUILD_SPECIFICATION.md](MASTER_BUILD_SPECIFICATION.md).

That document contains:

- Absolute project rules (sequential gates, canonical state, untrusted LLM, licensing).
- Points 00–70 (original scope plus engineering expansions). Every point is `NOT_STARTED` until a gate records otherwise in [BUILD_PLAN.md](BUILD_PLAN.md).
- The **V3 Consolidated Product Directive**, which is authoritative on:
  - Living Companion Platform category
  - Reference-first development (`REFERENCE → VALIDATE → ABSTRACT → TEMPLATE → VARIATIONS → SCALE`)
  - World & Life Engine, Action Engine, Navigation, Object Interaction
  - Reference Companion, Wardrobe, Home, and rooms
  - Interruptible embodied actions
  - Updated production sequence (section AE)

## Category

A Companion that can converse, remember, speak, look, move, dress, inhabit spaces, interact with objects, perform activities, maintain routines, make bounded contextual decisions, and continue the same relationship across iOS, Android, Windows, macOS, Web, and Telegram.

## What this repo must not become

- A chatbot
- A chatbot with an avatar
- A mobile-only application
- A static 3D character
- A collection of scripted animations
- Fifteen mediocre companions before one complete reference stack

## Conflicts

If this file, [ARCHITECTURE.md](ARCHITECTURE.md), or chat history disagrees with the master specification, the master specification wins. If earlier numbered points disagree with V3 on sequencing or embodiment, **V3 wins**.
