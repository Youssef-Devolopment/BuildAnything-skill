# Architecture

> The system's shape and the *why* behind it. Complements README (user-facing) and PLAN.md (the contract).
> Update in the same change that alters the structure it describes.

## Context

<!-- One paragraph: what this system is, what it talks to (users, external services, other systems). -->

## Components

<!-- Major parts, one block each: responsibility, key files, what it depends on. -->
### {{Component}}
- **Does:** …
- **Key files:** `{{path}}`
- **Depends on:** {{…}}

## Data model

<!-- Entities, relationships, keys. Link to migrations/ if they exist. -->
### {{Entity}}
| Field | Type | Notes |
|---|---|---|
| id | uuid | PK |
| created_at | timestamptz | |

## Key flows

<!-- The 2–4 most important flows, step by step (request → validation → logic → storage → response). -->
1. **{{Flow}}** — {{steps}}

## Key decisions

<!-- Decision → why. Full log lives in DECISIONS.md if the project is large. -->
- **{{choice}}** because {{reason}} (rejected: {{alternative}}).

## Integrations

<!-- External services, APIs, queues: what, auth how, failure behavior. -->

## Cross-cutting concerns

<!-- Auth model, error strategy, logging/observability, config/secrets — where each lives and how it works. -->
