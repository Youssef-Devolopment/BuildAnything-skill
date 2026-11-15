---
name: Backend
description: Use when building server-side code — APIs, data models, business logic, auth, validation, security, and integration tests.
---

# Backend

Load `build-anything` first (discovery, plan, stage gates). This skill covers implementing the server side.

## API design

- Resource-oriented, consistent naming; version from day one (`/v1/...`).
- Request validation at the boundary — every input (body, query, params, headers) validated and typed; reject with specific, actionable messages.
- Consistent error shape: `{ code, message, details? }` with correct HTTP status codes; never leak stack traces or internals to clients.
- Pagination, filtering, and sorting conventions defined once and applied everywhere.
- Idempotency for retries on mutating endpoints where it matters; safe methods are safe.

## Data

- Schema first: tables/collections, keys, indexes, constraints — model the real invariants, don't "figure it out while coding".
- Migrations are versioned files; never mutate production data by hand.
- Transactional consistency for multi-step writes; no N+1 queries — verify with logs/query counts.
- Soft-delete only when required; define cascades explicitly.

## Security (default posture)

- AuthN/AuthZ on every endpoint by default (deny-by-default), with roles/permissions checked server-side — never trust the client.
- Secrets via environment/secret manager only; `.env.example` committed, `.env` ignored.
- Rate limiting on sensitive endpoints; strict CORS; input size limits.
- Parameterized queries always; output encoding for the consumer; no eval/dynamic-code paths.
- Dependency versions pinned; audit new dependencies.

## Reliability & observability

- Structured logs with request/trace IDs; never log secrets or PII.
- Timeouts and explicit error handling on every external call (DB, third-party APIs); graceful degradation documented.
- Health check endpoint; readiness reflects dependencies.
- Background jobs (if any) are retried with backoff and are idempotent.

## Testing

- Unit tests for business logic; integration tests against a real (or containerized) database — not mocks — for queries and migrations.
- Contract tests for API request/response shapes; auth tests for every permission boundary (401/403 paths included).
- Run the suite in the stage gate; coverage of new code is a floor, not the goal.

## Rules

- No silent `catch {}` — log with context or propagate with a typed error.
- No endpoint that "works" only in the happy path.
- If a business rule is unclear, ask during discovery — never encode a guess as logic.
