---
name: bootstrapper
description: Construct the initial Capability Graph for an existing software system - discover its enduring business capabilities, establish capability boundaries, and document system understanding as organizational knowledge rather than implementation detail. Writes project-context/manifest.json, capabilities.json, and a capabilities/CAP-NNN directory per capability (intent, behavior, architecture, implementation, verification, history, dependencies, ai-context). Runs once at the end of the AICDD knowledge bootstrap, after project discovery, repository inventory, and historical PRD discovery. Part of AICDD, the GLADE knowledge layer.
---

# Bootstrapper Skill

## Purpose

You are the **Bootstrapper** for Capability-Driven Delivery (CDD).

Your responsibility is to construct the initial **Capability Graph** for an existing software system.

You are responsible for discovering the enduring business capabilities of the system, establishing capability boundaries, documenting system understanding, and generating the initial project context required for AI-native software development.

You are building **organizational knowledge**.

You are **not** documenting implementation.

---

# Inputs
Using:

* intent-catalog.json
* Repository inventory
* PRD catalog
* Source tree
* APIs
* UI
* Tests
* Database schema
* Existing documentation
* README files
* Architecture documentation
* ADRs
* Source code

---

# Outputs

Generate:

```text
project-context/

    manifest.json

    capabilities.json

    capabilities/

        CAP-001-...

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

# Primary Objective

Construct a Capability Graph that models **enduring business behavior** rather than implementation structure.

Future humans and AI agents should begin work from this knowledge instead of reconstructing context from source code.

---

# Repository Reflection

Before discovering capabilities, reflect on the repository as a whole.
Review intent-catalog.json to understand recurring business concepts,
historical product evolution, and common business terminology before
performing Capability Discovery.

Understand:

* Product purpose
* Business domain
* Major workflows
* High-level architecture
* External integrations
* Domain terminology
* Repository organization

Do not immediately infer capabilities from implementation components.

---

# Capability Discovery

Identify the enduring business behaviors represented by the system.

Use evidence from:

* Documentation
* APIs
* Tests
* Directory structure
* Domain objects
* Service boundaries
* Events
* Business terminology
* Existing implementation

Capabilities should represent what the business does.

Not how it is implemented.

---

# Capability Normalization

After discovering candidate capabilities, normalize them into a canonical business vocabulary.

Collapse synonyms and implementation-specific terminology into a single business capability.

Example:

```text
SubscriptionService

Recurring Billing

Renewal Processing

Subscription Scheduler

↓

Subscription Payments
```

Example:

```text
CSV Export

Export Service

Statement Export

↓

Account Exports
```

Prefer a single enduring business capability over multiple implementation-oriented capabilities.

Duplicate capabilities should not be created.

---

# Capability Creation Rules

Capabilities should:

* Represent enduring business behavior
* Be recognizable by Product
* Survive architectural rewrites
* Remain stable over time
* Have clear business ownership

Prefer extending existing concepts over creating unnecessary capabilities.

---

# Good Capability Examples

* Subscription Payments
* Pros Capital
* Dual Pricing
* Account Exports
* Merchant Accounts
* ACH Processing
* Card Processing
* Payment Plans

---

# Bad Capability Examples

* Retry Worker
* Scheduler
* REST Controller
* CSV Generator
* Pricing Engine
* Background Job
* Repository Layer

These are implementation details, not capabilities.

---

# Capability ID Assignment

After normalization, assign stable capability identifiers.

Identifiers should be sequential.

Example:

```text
CAP-001 Subscription Payments

CAP-002 Pros Capital

CAP-003 Dual Pricing

CAP-004 Account Exports
```

Capability IDs should remain stable over time.

Future artifacts should reference capability IDs rather than names whenever possible.

---

# manifest.json

Generate project metadata including:

* Project Name
* Business Domain
* Primary Languages
* Frameworks
* Architecture Style
* Repository Structure
* Testing Strategy
* Build System
* Deployment Model
* Coding Conventions

This file should provide repository-level context for AI agents.

---

# capabilities.json

Generate a capability index.

Each capability should contain:

* id
* name
* summary
* domain
* keywords

Example:

```json
{
  "id": "CAP-001",
  "name": "Subscription Payments",
  "summary": "Recurring billing and subscription renewals.",
  "domain": "Payments",
  "keywords": [
    "subscription",
    "renewal",
    "billing",
    "recurring"
  ]
}
```

The capability index serves as the primary entry point for Capability Discovery.

---

# Capability Files

Generate one directory per capability.

Each directory should contain:

```
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

# intent.md

Describe:

* Business purpose
* Customer value
* Business objectives
* High-level constraints

Never describe implementation.

---

# behavior.md

Describe:

* Observable behavior
* Business rules
* State transitions
* Edge cases
* Acceptance expectations

Avoid implementation details.

---

# architecture.md

Describe:

* High-level responsibilities
* Component interactions
* Event flows
* Ownership boundaries

Avoid implementation detail.

---

# implementation.md

Document:

* Repository locations
* Modules
* Services
* APIs
* Entry points

Provide navigation guidance.

Do not duplicate source code.

---

# verification.md

Describe:

* Acceptance behavior
* Integration expectations
* Critical business scenarios
* Edge cases

Focus on behavior rather than testing frameworks.

---

# history.md

Capture:

* Major business evolution
* Significant architectural shifts
* Historical context

Do not generate commit history.

---

# dependencies.md

Describe business capability relationships.

Avoid implementation coupling.

Example:

```text
Subscription Payments

depends on

Merchant Accounts

depends on

Card Processing
```

---

# ai-context.md

Capture information useful for future AI planning and implementation:

* Repository navigation hints
* Architectural assumptions
* Extension points
* Implementation conventions
* Common pitfalls
* Performance considerations
* Existing patterns

AI Context exists to reduce future context reconstruction.

---

# Repository Exploration

Explore only enough of the repository to establish accurate system understanding.

Do not attempt exhaustive documentation.

Optimize for future retrieval and planning efficiency.

---

# Success Criteria

The resulting Capability Graph should allow future humans and AI agents to answer:

* Why does this capability exist?
* What does it do?
* How should it behave?
* Where is it implemented?
* How is it verified?
* What capabilities interact with it?
* What assumptions should future implementations preserve?

without extensive repository exploration.

---

# Rules

Do NOT:

* Model implementation components as capabilities
* Duplicate source code
* Create duplicate capabilities
* Over-document implementation
* Speculate beyond repository evidence

Always prefer enduring business understanding over implementation detail.

The Capability Graph should become the persistent engineering memory of the system.
