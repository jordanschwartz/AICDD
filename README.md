# Capability-Driven Delivery (CDD)

> **Traditional software delivery manages work and reconstructs knowledge. Capability-Driven Delivery manages knowledge and derives work.**

---

## Overview

CDD is an AI-native delivery methodology that treats **system understanding as a first-class, versioned artifact**.

Most delivery processes rebuild understanding at the start of every initiative — reading source, hunting tickets, asking whoever was here last time. That rebuild is expensive, it produces a slightly different answer each time, and none of it survives the initiative.

CDD replaces the rebuild with a **capability graph**: a persistent, committed model of what the system does and why. Every initiative begins by reading it and ends by improving it.

The graph is not documentation about the system. It is the artifact the work is planned from.

---

## Where CDD sits

There is a growing category of tools that give coding agents a map of a codebase — repo maps, code graphs, semantic indexes. They read the source, produce a description an agent can consume faster than the raw files, and regenerate that description when the code changes. Most treat the result as a local cache: regenerable, disposable, correctly kept out of version control.

That design solves a real problem, and it solves it well. It also has a defining property: **a map derived from code can only contain what the code already contains.** It cannot be wrong about the system, because it is a projection of the system. It can only be out of date.

CDD's capability graph is authored rather than derived, and it holds three things a projection cannot:

- **Intent.** `if (balance < 0) reject()` is in the source. *Why* that rule exists, what outcome it protects, and what it would cost to relax it are not.
- **Rejected alternatives.** The design space that was considered and closed. Removed from the code by definition.
- **A behavioral contract stated independently of the implementation.** What the system promises, expressed so that a refactor does not change it and a regression shows up as a divergence.

That third one is load-bearing. Because the capability graph makes an independent claim, it *can* disagree with the code — and that disagreement is the signal. "Is this a bug or an undocumented change?" is answerable only against a stated contract. A derived map has nothing to diverge from.

|                        | Derived code map                      | CDD capability graph                          |
| ---------------------- | ------------------------------------- | --------------------------------------------- |
| Source of truth        | The code                              | Authored intent, verified against code        |
| Lifecycle              | Regenerated, typically gitignored     | Authored, committed, reviewed, versioned      |
| Can be wrong           | No — only stale                       | Yes, deliberately                             |
| Organizing unit        | Subsystem, module, symbol             | Business capability                           |
| Primary consumer       | The coding agent                      | Product and engineering, then agents          |
| Standing cost          | Rebuild time                          | Ongoing stewardship                           |

**These layers compose.** CDD does not replace a code map and does not care which one you use. A good structural map is a useful input to the Bootstrapper and to the Planner's repository-impact analysis. CDD's claim is about the layer above: that delivery itself should start and end at a persistent model of what the system promises.

### The cost this design incurs

A capability graph is organized by business behavior, so the mapping from capability to code is not derivable — it has to be maintained. It decays, and decay is invisible until someone trusts a stale claim. This is the central operational risk of the methodology, and CDD answers it with explicit freshness machinery rather than by pretending it away: watermarks per capability, a read-only adversarial audit, an incremental refresh, and a mandatory steward step at the end of every initiative. See [Keeping the map current](#keeping-the-map-current).

---

## Core idea: capabilities, not work items

Traditional delivery revolves around **work artifacts** — epics, stories, tasks, bugs. They are useful while work is in flight and become historical records the moment it ships.

CDD's unit is the **capability**: an enduring business behavior the system provides, named from the outside, in the vocabulary a user or a product manager would recognize.

Capabilities outlive the initiatives that change them. A ticket says *what someone did in March*. A capability says *what the system promises today*.

This has a practical consequence for who can participate. Because capabilities are named by observable behavior rather than by module, Product can read and approve a **Capability Change Request** — the artifact that says what each capability must become — before any work is decomposed. The review gate sits on the design decision, not just on the plan.

**Execution plans are temporary. Knowledge is permanent.**

---

## Lifecycle

```
BOOTSTRAP (once)                    DELIVERY (every initiative)

  Project Discovery                   Inquiry
         │                               │  "What is true today?"
  Repository Inventory                   ▼
         │                            Current-State Brief
  Historical PRD Discovery               │
         │                               ▼
  Bootstrapper                        PRD Writer
         │                               │  "What should become true?"
  Enricher                               ▼
         ▼                             PRD
  Capability Graph  ◄──────┐             │
                           │             ▼
                           │      Capability Author
                           │             │  "What must each capability become?"
                           │             ▼
                           │           CCR(s)  ──► review gate
                           │             │
                           │             ▼
                           │          Planner ──► Execution Plan ──► Assignments
                           │             │
                           │             ▼
                           │        Implementer ──► Reviewer
                           │             │
                           └─────────  Steward
                                         (graph updated)
```

The loop is the point. The graph is an input to the first step and an output of the last one.

---

## Quick start

CDD ships as a Claude Code plugin from this repo's own marketplace:

```
/plugin marketplace add https://github.com/jordanschwartz/AICDD
/plugin install aicdd@aicdd
```

Skills are then namespaced — `aicdd:inquiry`, `aicdd:prd-writer`, `aicdd:capability-author`, `aicdd:planner`. `CDD-setup` wires this automatically; you only add it by hand for standalone use.

Then build the graph:

```
mkdir project-context

/project-discovery          # project.md — high-level understanding
/repository-inventory       # repository-inventory.md — structural inventory
/historical-prd-discovery   # intent-catalog.json — historical business intent
/bootstrapper               # capabilities.json + capabilities/CAP-NNN-*/
/enricher CAP-001 CAP-002   # deepen each capability (parallelize on large repos)
```

Deliver a change:

```
/inquiry                    # what is true today → current-state-brief.md
/prd-writer <initiative>    # what should become true → prd.md
/capability-author <init>   # which capabilities change, and how → CCR/
/planner <initiative>       # decompose → execution-plan.md
   ── review gate: CCRs and execution plan ──
/techlead <initiative>      # → assignments.md
/implementer <initiative>
/reviewer <initiative>
/steward <initiative>       # sync the graph — the initiative is not done until this runs
```

Full walkthrough with inputs, outputs, and examples for each step: **[docs/reference.md](docs/reference.md)**.

---

## Keeping the map current

The graph is built once, then maintained. Four skills touch it; pick by intent.

| You want to…                                                  | Run                         | What it does                                                                                                                                                            |
| ------------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bring the map up to date** (code moved, or scheduled check) | `/aicdd:map-refresh`        | The default freshness tool. *Incremental* re-verifies only what moved since each capability's watermark; *full re-eval* re-discovers and red-teams the whole map. Writes. |
| **Audit without changing anything**                           | `/aicdd:map-review`         | Read-only. Adversarial "disprove it" pass, independent second read, and a completeness hunt for missing capabilities. Produces findings for a human.                     |
| **Deepen an accurate-but-thin map**                           | `/aicdd:enricher CAP-0NN …` | Improves quality and completeness of existing capabilities. Never adds, removes, or renames one.                                                                        |
| **Record a change you just shipped**                          | `/aicdd:steward`            | Syncs only the capability sections the change touched. The last step of the delivery lifecycle.                                                                          |

Rule of thumb: **refresh** to keep it true, **review** to audit without touching, **enricher** to deepen, **steward** to record. `map-refresh` writes; `map-review` only reports.

---

## What a capability holds

Each capability is a directory under `project-context/capabilities/CAP-NNN-slug/`:

| File                | Holds                                                              |
| ------------------- | ------------------------------------------------------------------ |
| `intent.md`         | Business purpose, customer value, goals, constraints                |
| `behavior.md`       | Observable behavior, business rules, state transitions, edge cases  |
| `architecture.md`   | Responsibilities, interactions, ownership boundaries                |
| `implementation.md` | Where it lives — modules, services, entry points. Navigation only.  |
| `verification.md`   | Acceptance and integration expectations, critical scenarios         |
| `history.md`        | Business evolution and major architectural changes                  |
| `dependencies.md`   | Relationships to other capabilities                                 |
| `ai-context.md`     | Navigation hints, assumptions, extension points, known pitfalls     |

The split is deliberate. `intent.md` and `behavior.md` are the parts a projection of the code could not have produced; `implementation.md` is a pointer, not a description, so that refactors do not invalidate the capability.

---

## Repository layout

```
repository/
└── project-context/
    ├── project.md
    ├── manifest.json
    ├── repository-inventory.md
    ├── intent-catalog.json
    ├── historical-prd-summary.md
    ├── capabilities.json
    ├── capabilities/
    │   ├── CAP-001-payment-processing/
    │   ├── CAP-002-reporting-exports/
    │   └── …
    └── initiatives/
        └── 001-add-reporting-exports/
            ├── current-state-brief.md
            ├── prd.md
            ├── CCR/
            ├── execution-plan.md
            ├── assignments.md
            └── review-report.md
```

Skills come from the `aicdd` plugin, not from a folder in the consuming repository.

---

## Status

This is **v0.1**. It has been run end-to-end on real repositories, including a 15-capability bootstrap and enrichment pass on a production servicing codebase.

What is not yet established:

- **The maintenance tax has not been measured against the context savings.** The methodology's central claim is that stewardship costs less than repeated reconstruction. That is a testable proposition and it has not yet been tested under controlled conditions.
- **Bootstrap quality is doing unexamined work.** The initial graph is seeded by the same inference CDD exists to replace. How much bootstrap error survives enrichment, and how it propagates, is an open question.
- **Capability decomposition has no formal story for cross-cutting concerns** or for refactoring the graph itself as a system's shape changes.

Working notes, known instruction defects, and observations from real runs are kept in [docs/notes/](docs/notes/) rather than here.

---

## Reference

- **[docs/reference.md](docs/reference.md)** — full step-by-step walkthrough and glossary
- **[docs/notes/](docs/notes/)** — working notes and known gaps

---

## Guiding principle

> **Every initiative should leave the system easier to understand than it was before the initiative began.**

The objective is not to automate software development. It is to build an understanding of the system that compounds, so that humans and agents alike spend less time reconstructing context and more time changing behavior on purpose.
