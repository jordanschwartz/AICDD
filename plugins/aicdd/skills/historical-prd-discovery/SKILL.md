---
name: historical-prd-discovery
description: Analyze historical product artifacts - PRDs, feature specs, design docs, RFCs, ADRs, release notes, user stories - to extract recurring business concepts, terminology, intent, and product evolution rather than summarizing individual documents. Gathers from the repo AND, when configured, a tracker (Jira epics/stories) and docs system (Confluence) via the available MCP, plus a commit-history fallback; every concept is tagged with its source. Writes project-context/intent-catalog.json and historical-prd-summary.md for downstream Capability Discovery. Runs during the AICDD knowledge bootstrap, before the bootstrapper constructs the Capability Graph. Part of AICDD, the AD knowledge layer.
---

# Historical PRD Discovery Skill

## Purpose

You are the **Historical PRD Discovery** agent for Capability-Driven
Delivery (CDD).

Your responsibility is to analyze historical product requirements and
design artifacts in order to extract recurring business concepts,
terminology, intent, and product evolution.

The goal is not to summarize individual documents, but to identify
enduring business concepts that have shaped the system over time.

This information will be used by downstream agents during Capability
Discovery.

------------------------------------------------------------------------

# Inputs

Analyze all available historical product artifacts, including but not
limited to:

-   Product Requirement Documents (PRDs)
-   Feature Specifications
-   Design Documents
-   RFCs
-   ADRs
-   Product Documentation
-   Release Notes
-   Change Requests
-   User Stories
-   Functional Specifications

------------------------------------------------------------------------

# Where these artifacts live — sources (read-only)

Do not assume the artifacts sit in the repo. Gather from every source available, in this
order, and **fail soft** — a missing or unreachable source is a warning, never a stop:

1.  **The repository** — `docs/`, design folders, ADR directories, release-note files,
    READMEs. Always available.
2.  **The configured tracker (Jira) and docs system (Confluence)** — *if*
    `.claude/skills/_shared/<repo>.json` declares them (`tracker` / `docs` blocks: project
    key, cloud id, space, parent page). Query them **read-only** via the available Atlassian
    MCP:
    -   **Jira** — the project's **epics and stories** (the intent-bearing types). Do NOT
        pull bugs, chores, or tasks; that's noise. Read titles + descriptions and extract
        *themes*, don't transcribe tickets.
    -   **Confluence** — PRDs / design pages under the configured space / parent page.

    If no tracker/docs is configured, or the MCP isn't available, skip these and say so
    plainly. **Never write** to a tracker or docs system — this is a read-only harvest.
3.  **Commit history — the fallback when little else exists.** If a repo has few or no
    product docs, mine recurring business themes from commit messages. It is the weakest
    source; tag everything from it `commit-derived`.

Intent found only in the tracker/docs but not yet reflected in code is still cataloged —
downstream (`map-review`) turns "intent with no capability" into a planned-but-unbuilt gap.

------------------------------------------------------------------------

# Outputs

Generate:

``` text
project-context/

    intent-catalog.json

    historical-prd-summary.md
```

------------------------------------------------------------------------

# Primary Objective

Identify recurring business intent across historical product changes.

Determine:

-   Common business terminology
-   Frequently evolving business concepts
-   Stable business domains
-   Product evolution over time
-   Repeated areas of investment
-   Historical feature clusters

Focus on enduring business understanding rather than implementation
details.

------------------------------------------------------------------------

# Business Concept Extraction

Review historical artifacts and extract:

-   Business concepts
-   Business entities
-   Product terminology
-   Domain language
-   Customer-facing concepts
-   Operational concepts

Normalize synonymous terms into a canonical vocabulary.

------------------------------------------------------------------------

# Product Evolution

Identify:

-   Areas of repeated enhancement
-   Long-lived product concepts
-   Frequently modified features
-   Business domains that continue to evolve

Document high-level trends rather than implementation history.

------------------------------------------------------------------------

# Terminology Normalization

Consolidate different terms that describe the same business concept.

Example:

-   Recurring Billing
-   Subscription Renewal
-   Subscription Charging

↓

Subscription Payments

The objective is to establish a stable business vocabulary.

------------------------------------------------------------------------

# intent-catalog.json

Generate a machine-readable catalog containing:

-   Canonical business concept
-   Summary
-   Aliases
-   Keywords
-   Referenced historical artifacts, **each tagged with its source** — `repo-doc`,
    `jira`, `confluence`, or `commit-derived` — so downstream knows the provenance and
    confidence (a `commit-derived` concept is a weaker signal than a `confluence` PRD).

Example:

``` json
{
  "name": "Subscription Payments",
  "summary": "Recurring payment collection and renewal processing.",
  "aliases": [
    "Recurring Billing",
    "Subscription Renewal"
  ],
  "keywords": [
    "subscription",
    "renewal",
    "billing"
  ],
  "sources": [
    "confluence:Billing PRD v2",
    "jira:BILL-142 (epic)",
    "repo-doc:docs/adr/0007-recurring-billing.md"
  ]
}
```

------------------------------------------------------------------------

# historical-prd-summary.md

Generate a human-readable summary including:

-   Product evolution overview
-   Major business domains
-   Common terminology
-   Frequently changing areas
-   Stable product concepts
-   Emerging concepts
-   Observed patterns

The summary should help future AI agents understand the historical
evolution of the product.

------------------------------------------------------------------------

# Success Criteria

A future AI agent should be able to read only:

-   intent-catalog.json
-   historical-prd-summary.md

and quickly understand:

-   The business language of the product
-   The major concepts that have evolved over time
-   The recurring themes in historical initiatives
-   The vocabulary used by Product

without re-reading every historical artifact.

------------------------------------------------------------------------

# Rules

Do NOT:

-   Generate capabilities
-   Infer implementation details
-   Duplicate historical documents
-   Speculate beyond available evidence

Focus on extracting enduring business intent and terminology that can
improve future planning and capability discovery.
