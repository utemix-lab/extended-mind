# System Overview

This repository describes a graph-first system for composing, executing, and experiencing thinking processes.

The system is built around a simple but strict separation of concerns:

- **Composition** — how meaning, knowledge, and intent are structured.
- **Execution** — how this structure is transformed into concrete output.
- **Experience** — how a human encounters and navigates the system.

Architecture, content, and interface are treated not as separate layers, but as different projections of the same underlying structure.

---

## Core Abstractions

### Graph as the Primary Form

All knowledge, projects, and processes are represented as graphs:

- **Universe Graph** — the global semantic space.
- **Subgraphs** — bounded projections of the universe (projects, domains).
- **Route Graphs** — finite, intentional paths through a subgraph.

Graphs are not encyclopedic. They are designed to be *traversable*.

---

### Route over Totality

The system does not aim to represent “everything”.

Instead, it emphasizes:
- finite routes,
- bounded sessions,
- intentional traversal.

A user never sees “the whole graph” — only a meaningful slice.

---

### Three Projections (3S)

Every route and session can be viewed through three complementary projections:

- **Story** — what this is, what happens, who is involved.
- **System** — how this is implemented and structured.
- **Service** — what actions can be performed.

These are not modes, but simultaneous perspectives on the same structure.

---

## Editor vs Runtime

The system distinguishes between:

- **Editor / Compiler**
  - where graphs and routes are designed,
  - where meaning is composed,
  - where sessions are assembled.

- **Runtime**
  - where sessions are executed,
  - where external engines (LLMs) operate,
  - where results are produced.

This separation is fundamental and intentional.

---

## Role of LLMs

Language models are treated as **external execution engines**.

They do not own knowledge, truth, or structure.
They execute compiled sessions under explicit constraints.

---

## Purpose

This system is a universal scaffold from which multiple products, formats, and practices can emerge:
- authorial performances,
- personal thinking environments,
- research tools,
- educational experiences.

The core remains the same.
Only the projection changes.
