---
name: Database
description: Design and evolve data layers — schema modeling, migrations, indexes, query performance, and backup/retention. Load when choosing a database, designing tables/collections, writing or reviewing migrations, or debugging slow queries. Works with build-anything and backend.
---

# Database

Load `build-anything` (plan first) and `backend` (it owns API-level rules). This skill owns the data layer itself — the part that's expensive to change later.

## Design first, code second

1. **Model the real invariants** — entities, relationships, cardinality, and what must never be false (unique emails, valid states). Sketch tables + keys before writing a migration; put the diagram/notes in `ARCHITECTURE.md`.
2. **Choose deliberately** (record in `PLAN.md` §4): **PostgreSQL is the default** — relational data, constraints, JSONB for flexibility. SQLite for single-node/local tools. DocumentDB/graph only with a stated reason. "We might need flexibility later" is not a reason to skip modeling.
3. **3NF by default, denormalize with a reason** — duplicates (e.g. counters) only where measured read cost justifies the write complexity, with the sync strategy written down.

## Schema rules

- **Primary keys**: UUID/ULID for anything distributed or exposed; serial/bigserial fine for internal high-write tables. Never use a mutable business field as a key.
- **Foreign keys with explicit `ON DELETE`** — `RESTRICT`, `CASCADE`, or `SET NULL` chosen per relationship, never left to default.
- **Timestamps on every table**: `created_at`, `updated_at` (`updated_at` via trigger or ORM convention).
- **Constraints over trust**: `NOT NULL`, `CHECK`, `UNIQUE` at the DB level — the app is not the only writer.
- **Money**: integer minor units (cents), never floats; currency as a column if multi-currency is possible.
- **Soft delete** only when required — and if used, it's a column + partial unique indexes, applied consistently.
- **Enums**: Postgres `ENUM` only for values that never change; otherwise lookup table or `CHECK` so values can grow.

## Migrations

- Every schema change is a **versioned migration file**, forward + (if the platform supports) reversible; run automatically as a deploy step.
- **Expand → migrate → contract**: add nullable/new structures first, backfill, switch reads, then drop old ones — so the previous app version survives a rollback.
- Never edit an applied migration; write a new one. Never touch production data by hand — a migration or a reviewed script.

## Performance

- **Indexes follow queries**: every `WHERE`/`JOIN`/`ORDER BY` on non-trivial data gets an index — but measure: each index costs writes. Document the query each index serves.
- **No N+1**: verify with query logging at the stage gate; batch/`JOIN`/eager-load instead.
- **Paginate always** — keyset (`WHERE id > cursor`) for large/infinite lists, offset only for small tables.
- **Explain before optimizing**: `EXPLAIN ANALYZE` on slow queries; fix seq-scans on big tables with the right index, not with caching layers.
- **Limits**: connection pooling sized for the host; statement timeouts; input size limits at the API boundary.

## Safety & lifecycle

- Backups **on before first real data**; restore tested once (an untested backup isn't a backup).
- Retention/deletion policy (GDPR-style "delete user" = a documented, cascading or anonymizing script).
- Seed data for dev: realistic, small, versioned — fake data never in production.
- Schema changes and app changes that depend on each other ship in the same release (expand-contract keeps them independent).

## Rules

- If a business rule is unclear, ask during discovery — never encode a guess as a constraint.
- Every migration runs green in CI against a real database before it merges.
- Report table/index changes in `ARCHITECTURE.md` in the same change.
