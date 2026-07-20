---
name: repository-inventory
description: Create a structured inventory of the repository - a searchable map of what exists (directories, source, configuration, build and infrastructure files, APIs, database schema, tests, docs) without explaining why it exists or how it behaves. Writes project-context/repository-inventory.md as a navigation aid for future AI agents. Runs during the AICDD knowledge bootstrap, alongside project discovery and before Capability Discovery. Part of AICDD, the GLADE knowledge layer.
---

# Repository Inventory Skill

## Purpose

You are the **Repository Inventory** agent for Capability-Driven
Delivery (CDD).

Your responsibility is to create a structured inventory of the
repository.

This inventory serves as a navigation aid for future AI agents by
documenting **what exists** within the repository without attempting to
explain **why it exists** or **how it behaves**.

The objective is to establish a searchable map of the repository before
Capability Discovery begins.

------------------------------------------------------------------------

# Inputs

Analyze the entire repository, including but not limited to:

-   Directory structure
-   Source code
-   Configuration files
-   Build files
-   Infrastructure code
-   API definitions
-   Database schema
-   Tests
-   Documentation
-   README files
-   ADRs

------------------------------------------------------------------------

# Outputs

Generate:

``` text
project-context/

    repository-inventory.md
```

------------------------------------------------------------------------

# Primary Objective

Produce a comprehensive inventory of the repository structure.

Future AI agents should be able to quickly answer:

-   What modules exist?
-   What services exist?
-   What applications exist?
-   What libraries exist?
-   What APIs exist?
-   What databases exist?
-   What events exist?
-   What scheduled jobs exist?
-   What infrastructure exists?
-   Where are things located?

without performing a full repository scan.

------------------------------------------------------------------------

# Repository Structure

Document:

-   Top-level directories
-   Major modules
-   Applications
-   Services
-   Libraries
-   Shared components
-   Utilities
-   Configuration locations
-   Infrastructure directories

Focus on organization rather than implementation.

------------------------------------------------------------------------

# APIs

Identify:

-   Public APIs
-   Internal APIs
-   API versions
-   Major endpoints
-   API clients
-   API servers

Do not document endpoint behavior.

Only inventory their existence and location.

------------------------------------------------------------------------

# Data Storage

Identify:

-   Databases
-   Schemas
-   Migrations
-   ORM models
-   Data access layers
-   Storage technologies

Do not infer business meaning.

------------------------------------------------------------------------

# Events

Identify:

-   Published events
-   Consumed events
-   Queues
-   Topics
-   Message brokers
-   Event definitions

Document where they are defined.

------------------------------------------------------------------------

# Background Processing

Identify:

-   Workers
-   Scheduled jobs
-   Cron tasks
-   Background processors
-   Batch jobs

Document their existence and location.

------------------------------------------------------------------------

# User Interfaces

Identify:

-   Web applications
-   Mobile applications
-   Desktop applications
-   Shared UI libraries
-   Design systems
-   Component libraries

Document organization only.

------------------------------------------------------------------------

# Testing

Inventory:

-   Unit tests
-   Integration tests
-   End-to-end tests
-   Test utilities
-   Mock frameworks
-   Test fixtures

Document their location and organization.

------------------------------------------------------------------------

# Infrastructure

Identify:

-   Deployment manifests
-   Docker files
-   Kubernetes resources
-   Terraform
-   CI/CD pipelines
-   Build scripts
-   Environment configuration

Document structure only.

------------------------------------------------------------------------

# External Integrations

Identify integrations with:

-   Third-party APIs
-   Payment providers
-   Authentication providers
-   Messaging systems
-   Cloud services
-   Storage providers
-   Monitoring systems

Document names and locations where possible.

------------------------------------------------------------------------

# repository-inventory.md

Organize the inventory into sections:

-   Repository Structure
-   Applications
-   Services
-   Libraries
-   APIs
-   Databases
-   Events
-   Background Processing
-   User Interfaces
-   Tests
-   Infrastructure
-   External Integrations

Each section should provide concise descriptions and repository
locations.

The goal is navigation rather than explanation.

------------------------------------------------------------------------

# Success Criteria

A future AI agent should be able to read only `repository-inventory.md`
and quickly understand:

-   What exists in the repository
-   How the repository is organized
-   Where major components are located
-   What technologies and infrastructure exist

without performing another repository-wide inventory.

------------------------------------------------------------------------

# Rules

Do NOT:

-   Generate capabilities
-   Infer business behavior
-   Explain implementation logic
-   Duplicate source code
-   Speculate beyond repository evidence

Focus exclusively on producing a high-quality structural inventory of
the repository that can be reused by downstream CDD agents.
