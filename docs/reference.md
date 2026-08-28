# CDD Reference

Full walkthrough and glossary. For the thesis and positioning, see the [README](../README.md).

---

## Part 1 — Building the capability graph

Run once per repository. Each step feeds the next.

### Step 1 — Create the project context

```
mkdir project-context
```

This folder holds the persistent knowledge model. It is committed.

### Step 2 — Project discovery

```
/project-discovery
```

Produces `project-context/project.md` — high-level understanding of what the repository is and what it does.

### Step 3 — Repository inventory

```
/repository-inventory
```

Produces `project-context/repository-inventory.md` — a structural inventory. API endpoints are inventoried at the controller (or router/module) level, not per route; per-route inventories balloon on large services and duplicate what the source expresses better.

### Step 4 — Historical PRD discovery

```
/historical-prd-discovery
```

Produces `project-context/intent-catalog.json` and `historical-prd-summary.md` — historical business intent and the terminology the organization actually uses.

**When a repository has no PRDs or ADRs**, this step falls back to mining recurring business terms from commit history and labels the resulting catalog *commit-derived* rather than *PRD-derived*, so downstream agents can weight it accordingly.

### Step 5 — Bootstrapper

```
/bootstrapper
```

Synthesizes project discovery, repository inventory, historical intent, source, and documentation into an initial capability graph:

```
project-context/
    capabilities.json
    capabilities/
        CAP-001-payment-processing/
        CAP-002-reporting-exports/
        …
```

Capability directories follow `CAP-NNN-lowercase-hyphen-slug` — zero-padded three-digit number, then a lowercase hyphenated slug — so independently bootstrapped repositories produce consistent names.

The bootstrapper owns `manifest.json`.

### Step 6 — Enricher

```
/enricher CAP-001
/enricher CAP-001 CAP-002 CAP-003
```

Deepens existing capabilities. It never creates, removes, or renames one.

On large repositories, run enrichers in parallel background agents:

```
Agent 1 → CAP-001 … CAP-005
Agent 2 → CAP-006 … CAP-010
Agent 3 → CAP-011 … CAP-015
```

The orchestrator owns scope checking per batch; parallel enrichers sharing a worktree cannot self-verify scope via `git status`.

Enrichment is expected to find and correct wrong bootstrap claims. Corrections carry a note recording what was changed and on what evidence.

---

## Part 2 — Delivering a change

### Step 1 — Create an initiative

```
project-context/initiatives/001-add-reporting-exports/
```

Every artifact for the initiative lives here. The PRD is not written by hand; it is produced after inquiry.

### Step 2 — Inquiry — *what is true today?*

```
/inquiry How do reporting exports work today?
```

Inquiry reads the capability graph and verifies against the repository only when necessary. Ask for a current-state brief when you are ready to move to a PRD:

```
current-state brief
```

Produces `current-state-brief.md` — the shared understanding of existing behavior the PRD will be written against.

### Step 3 — PRD Writer — *what should become true?*

```
/prd-writer project-context/initiatives/001-add-reporting-exports/
```

Reads the current-state brief, clarifies product intent, optionally performs industry and incumbent research, and produces `prd.md`.

The PRD is implementation-agnostic: desired behavior, business rules, scope boundaries, success criteria.

### Step 4 — Capability Author — *what must each capability become?*

```
/capability-author project-context/initiatives/001-add-reporting-exports/
```

Performs capability discovery against the PRD — deciding which capabilities change — and authors one CCR per impacted capability into `CCR/`.

This step exists separately from planning on purpose. It isolates the design decision behind its own review gate, before any work is decomposed.

### Step 5 — Planner

```
/planner project-context/initiatives/001-add-reporting-exports/
```

Consumes the CCRs, analyzes repository impact, and decomposes the work into atomic, parallelizable tasks in `execution-plan.md`. It does not author capabilities.

### Step 6 — Review gate

Engineering and Product review two things:

- **CCRs** — are these the right capability changes?
- **execution-plan.md** — is this the right work plan?

The CCR describes how behavior evolves. The execution plan describes how implementation happens. They are approved separately.

### Step 7 — Assignments

```
/techlead project-context/initiatives/001-add-reporting-exports/
```

Produces `assignments.md`, mapping execution tasks to implementation agents while maximizing parallel execution.

### Step 8 — Implement

```
/implementer project-context/initiatives/001-add-reporting-exports/
```

Executes the assignment plan using the generated agent team.

### Step 9 — Review

```
/reviewer project-context/initiatives/001-add-reporting-exports/
```

Validates CCR compliance, execution plan compliance, architecture, behavior, test coverage, and regression risk.

### Step 10 — Steward

```
/steward project-context/initiatives/001-add-reporting-exports/
```

Synchronizes the capability graph with the newly implemented behavior. **The initiative is not complete until this runs.**

---

## Capability artifacts

### intent.md
Business purpose, customer value, goals, constraints. Avoids implementation detail.

### behavior.md
Observable behavior, business rules, state transitions, edge cases. Avoids implementation detail.

### architecture.md
Responsibilities, high-level interactions, ownership boundaries, system organization.

### implementation.md
Repository locations, modules, services, entry points. Navigation guidance — a pointer, not a description.

### verification.md
Acceptance expectations, integration expectations, critical scenarios, edge cases.

### history.md
Business evolution, major architectural changes, historical context. Mining evolution with read-only `git log` is permitted here.

### dependencies.md
Relationships between capabilities. Also the standard home for code that straddles a capability boundary: document the seam here.

### ai-context.md
Repository navigation hints, architectural assumptions, extension points, existing patterns, common pitfalls. Exists exclusively to reduce future context reconstruction.

---

## Glossary

**Capability** — An enduring business behavior implemented by the system, named from the outside. Capabilities evolve and outlive individual initiatives.

**Capability Graph** — The complete collection of capability knowledge representing system understanding. The primary artifact of CDD.

**Current-State Brief** — A synthesized description of what the system does today in the area under consideration. Produced by Inquiry. The baseline the PRD is written against.

**PRD** — Describes the business problem and desired outcome. Produced by the PRD Writer with Product. Does not reference implementation.

**CCR (Capability Change Request)** — Describes how one capability must evolve to satisfy a PRD. One per impacted capability, authored by the Capability Author. Bridges product intent and engineering implementation.

**Execution Plan** — A temporary implementation plan derived from the CCRs. Exists only for the duration of the initiative.

**Assignment Plan** — Maps execution tasks to implementation agents, maximizing parallel execution.

**Bootstrapper** — Constructs the initial capability graph from the repository and historical artifacts.

**Enricher** — Improves the quality of existing capabilities. Does not create new ones.

**Inquiry** — Answers "what is true today?". Reads the graph, verifies against the repository only when necessary. Does not define desired future state.

**PRD Writer** — Answers "what should become true?". Does not plan the change.

**Capability Author** — Performs capability discovery and authors one CCR per impacted capability. Runs after the PRD and before the Planner. Does not decompose work or write code.

**Planner** — Consumes CCRs and decomposes them into an execution plan. Does not author capabilities.

**Implementer** — Executes assigned implementation tasks.

**Reviewer** — Validates implementation against the approved CCR and execution plan.

**Steward** — Synchronizes the capability graph after implementation is complete.

**map-refresh / map-review** — Freshness tools. `map-refresh` re-verifies and writes; `map-review` audits adversarially and only reports.
