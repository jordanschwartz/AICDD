# Capability-Driven Delivery (CDD)

> **Traditional software development manages work and reconstructs knowledge. Capability-Driven Delivery manages knowledge and derives work.**

---

# Overview

Capability-Driven Delivery (CDD) is an AI-native software delivery methodology that treats **system understanding as a first-class artifact**.

Rather than repeatedly reconstructing context from source code, tickets, and documentation for every initiative, CDD builds and maintains a **persistent knowledge model** of the system that continuously evolves alongside the implementation.

Every initiative begins from that knowledge model and ends by improving it.

---

# Core Philosophy

Traditional software delivery revolves around **work artifacts**:

* Epics
* User Stories
* Tasks
* Bugs

These artifacts are valuable during execution but become historical records once work is complete.

CDD shifts the focus toward **Capabilities**.

Capabilities represent enduring business behavior that evolves over the lifetime of the system.

Execution plans are temporary.

Knowledge is permanent.

---

# Getting Started

## Step 1 - Create the Project Context

Create a folder in the root of your repository:

```text
project-context/
```

This folder will contain the persistent knowledge model.

---

## Step 2 - Run Project Discovery

Execute:

```
/project-discovery
```

This generates:

```
project-context/

    project.md

    manifest.json
```

These files establish high-level understanding of the repository.

---

## Step 3 - Run Repository Inventory

Execute:

```
/repository-inventory
```

This generates:

```
project-context/

    repository-inventory.md
```

This provides a structural inventory of the repository.

---

## Step 4 - Run Historical PRD Discovery

Execute:

```
/historical-prd-discovery
```

This generates:

```
project-context/

    intent-catalog.json

    historical-prd-summary.md
```

These artifacts establish historical business intent and terminology.

---

## Step 5 - Run the Bootstrapper

Execute:

```
/bootstrapper
```

The Bootstrapper synthesizes:

* Project Discovery
* Repository Inventory
* Historical Product Intent
* Source Code
* Documentation

into an initial Capability Graph.

It generates:

```text
project-context/

    capabilities.json

    capabilities/

        CAP-001/

        CAP-002/

        ...
```

---

## Step 6 - Run the Enricher

Execute:

```
/enricher
```

Pass the capability(s) you wish to enrich.

Example:

```
/enricher CAP-001
```

or

```
/enricher CAP-001 CAP-002 CAP-003
```

For large repositories, launch multiple background agents simultaneously.

Example:

```
Agent 1 → CAP-001 ... CAP-005

Agent 2 → CAP-006 ... CAP-010

Agent 3 → CAP-011 ... CAP-015
```

This significantly accelerates enrichment.

---

# The Knowledge Model is Now Ready

At this point the repository contains a persistent Capability Graph that becomes the foundation for all future initiatives.

---

# Delivering a Change

## Step 1 - Create an Initiative

Create:

```text
project-context/initiatives/

    001-add-reporting-exports/
```

This folder will hold every artifact produced for the initiative.

The PRD is not written by hand.

It is produced by the PRD Writer after Capability Inquiry.

---

## Step 2 - Run Inquiry

Execute:

```
/inquiry
```

Ask about the area of the system you are considering changing.

Example:

```
/inquiry How do reporting exports work today?
```

Inquiry answers:

> What is true today?

It reads the Capability Graph and, only when necessary, verifies against the repository.

When ready to prepare for a PRD, ask for a Current-State Brief:

```
current-state brief
```

Inquiry generates:

```
project-context/initiatives/001-add-reporting-exports/

    current-state-brief.md
```

This brief establishes the shared understanding of existing behavior that the PRD will build against.

---

## Step 3 - Run PRD Writer

Execute:

```
/prd-writer
```

Pass the initiative directory and describe the desired change.

Example:

```
/prd-writer project-context/initiatives/001-add-reporting-exports/
```

The PRD Writer answers:

> What should become true?

It reads the Current-State Brief, clarifies product intent, optionally performs industry and incumbent research, and produces:

```
project-context/initiatives/001-add-reporting-exports/

    prd.md
```

The PRD is implementation-agnostic.

It describes desired product behavior, business rules, scope boundaries, and success criteria.

---

## Step 4 - Run Planner

Execute:

```
/planner
```

Pass the initiative directory.

Example:

```
/planner project-context/initiatives/001-add-reporting-exports/
```

Planner generates:

```
CCR/

execution-plan.md
```

---

## Step 5 - Review

Engineering and Product review:

* CCR(s)
* execution-plan.md

The CCR describes how existing capabilities evolve.

The execution plan describes how implementation will occur.

---

## Step 6 - Generate Assignments

Execute:

```
/techlead
```

Pass the initiative directory.

Example:

```
/techlead project-context/initiatives/001-add-reporting-exports/
```

This produces:

```
assignments.md
```

which assigns execution tasks to implementation agents while maximizing parallel execution.

---

## Step 7 - Implement

Execute:

```
/implementer
```

Pass the initiative directory.

The Implementer executes the assignment plan using the generated agent team.

---

## Step 8 - Review

Execute:

```
/reviewer
```

Pass the initiative directory.

The Reviewer validates:

* CCR compliance
* Execution Plan compliance
* Architecture
* Behavior
* Test coverage
* Regression risk

---

## Step 9 - Update Knowledge

After implementation has been approved:

Execute:

```
/steward
```

Pass the initiative directory.

The Steward synchronizes the Capability Graph with the newly implemented behavior.

The initiative is complete.

---

# Repository Layout

```text
repository/

├── project-context/
│
│   ├── project.md
│   ├── manifest.json
│   ├── repository-inventory.md
│   ├── intent-catalog.json
│   ├── historical-prd-summary.md
│   ├── capabilities.json
│   │
│   ├── capabilities/
│   │
│   │   ├── CAP-001/
│   │   ├── CAP-002/
│   │   └── ...
│   │
│   └── initiatives/
│
│       └── 001-add-reporting-exports/
│
│           ├── current-state-brief.md
│           ├── prd.md
│           ├── CCR/
│           ├── execution-plan.md
│           ├── assignments.md
│           └── review-report.md
│
└── skills/
```

---

# Capability Structure

Each capability contains:

```text
CAP-001/

    intent.md

    behavior.md

    architecture.md

    implementation.md

    verification.md

    history.md

    dependencies.md

    ai-context.md
```

---

# Capability Artifact Descriptions

## intent.md

Describes:

* Business purpose
* Customer value
* Goals
* Constraints

---

## behavior.md

Describes:

* Observable behavior
* Business rules
* State transitions
* Edge cases

---

## architecture.md

Describes:

* Responsibilities
* High-level interactions
* Ownership boundaries
* System organization

---

## implementation.md

Documents:

* Repository locations
* Modules
* Services
* Entry points

Provides navigation guidance.

---

## verification.md

Documents:

* Acceptance expectations
* Integration expectations
* Critical scenarios
* Edge cases

---

## history.md

Captures:

* Business evolution
* Major architectural changes
* Historical context

---

## dependencies.md

Documents relationships between capabilities.

---

## ai-context.md

Provides:

* Repository navigation hints
* Architectural assumptions
* Extension points
* Existing patterns
* Common pitfalls

This file exists exclusively to reduce future context reconstruction.

---

# Glossary

## Capability

An enduring business behavior implemented by the system.

Capabilities evolve over time and outlive individual initiatives.

---

## Capability Graph

The complete collection of capability knowledge representing system understanding.

It is the primary artifact of CDD.

---

## Current-State Brief

A synthesized description of what the system does today for the area under consideration.

Produced by Inquiry.

Provides the baseline that the PRD is written against.

---

## PRD (Product Requirements Document)

Describes the business problem and desired outcome.

Produced by the PRD Writer in collaboration with Product.

Does not reference implementation.

---

## CCR (Capability Change Request)

Describes how one or more capabilities must evolve to satisfy a PRD.

Generated by the Planner.

Bridges Product intent and Engineering implementation.

---

## Execution Plan

A temporary implementation plan generated from the Capability Graph.

Exists only for the duration of the initiative.

---

## Assignment Plan

Maps execution tasks to implementation agents while maximizing parallel execution.

---

## Bootstrapper

Constructs the initial Capability Graph from the repository and historical artifacts.

---

## Enricher

Improves the quality of existing capabilities.

Does not create new capabilities.

---

## Inquiry

Answers the question "What is true today?".

Reads the Capability Graph and, only when necessary, verifies against the repository.

Produces conversational answers or a Current-State Brief.

Does not define desired future state.

---

## PRD Writer

Answers the question "What should become true?".

Takes the Current-State Brief plus human intent and, optionally, industry and incumbent research to produce a precise, implementation-agnostic PRD.

Does not plan the change.

---

## Planner

Transforms a PRD into CCR(s) and an execution plan.

---

## Implementer

Executes assigned implementation tasks.

---

## Reviewer

Validates implementation against the approved CCR and execution plan.

---

## Steward

Synchronizes the Capability Graph after implementation is complete.

---

# Lifecycle

```text
Knowledge Bootstrap

Project Discovery
        │
Repository Inventory
        │
Historical PRD Discovery
        │
Bootstrapper
        │
Enricher
        ▼
Capability Graph


Delivery

Inquiry
 │
 ▼
Current-State Brief
 │
 ▼
PRD Writer
 │
 ▼
PRD
 │
 ▼
Planner
 │
 ▼
CCR(s)
 │
 ▼
Execution Plan
 │
 ▼
Assignments
 │
 ▼
Implementer
 │
 ▼
Reviewer
 │
 ▼
Steward
 │
 ▼
Updated Capability Graph
```

---

# Guiding Principle

> **Every initiative should leave the system easier to understand than it was before the initiative began.**

The objective of CDD is not simply to automate software development.

The objective is to build a persistent understanding of the system that compounds over time, allowing both humans and AI agents to spend less time reconstructing context and more time delivering value.

---

## GLADE packaging notes

Instruction fixes found in the first real use of these skills (packaging them for Claude Code under GLADE). Each one is a gap or conflict in the skill instructions themselves, recorded here until the skill bodies are revised:

1. **manifest.json belongs to the bootstrapper alone.** Both project-discovery and bootstrapper currently claim `project-context/manifest.json` as an output. Two writers for one file means the second run silently overwrites the first. The bootstrapper should own it; project-discovery should write only `project.md`.

2. **historical-prd-discovery needs a documented fallback for repos with zero PRDs/ADRs.** Many real repos have no historical product artifacts at all. When none exist, the skill should fall back to mining commit-message themes (frequency of recurring business terms across commit history) and clearly label the resulting intent catalog as commit-derived, not PRD-derived, so downstream agents know the confidence level.

3. **repository-inventory endpoint granularity is controller-level.** The skill should state explicitly that API endpoints are inventoried at the controller (or router/module) level, not per-route. Per-route inventories balloon on large services and duplicate what the source itself expresses better.

4. **Capability directory slug rule should be explicit.** Capability directories follow `CAP-NNN-lowercase-hyphen` (zero-padded three-digit number, then a lowercase hyphenated slug, e.g. `CAP-007-payment-processing`). The bootstrapper body shows `CAP-001-...` by example only; the rule should be stated so independently bootstrapped repos produce consistent names.

### Enricher notes from first full run (servicing, 15 capabilities, 2026-07-13)
1. Permit read-only `git log` explicitly — history.md guidance implies mining evolution, but "do not run git commands" forbids it.
2. Say where evidence citations belong per file type (intent/behavior avoid implementation detail, yet evidence-only demands citable paths).
3. Parallel enrichers in one worktree can't self-verify scope via git status — the orchestrator should own scope checks per batch.
4. Bless evidence-based correction of wrong bootstrap claims (14+ found in one run) and require a correction note.
5. Standard resolution for boundary-straddling code: document the seam in dependencies.md — agents converged on this independently.
6. Add a channel for source-doc defects found during enrichment (stale diagrams/docs) — currently parked in ai-context pitfall notes.
