# Best Tech Stacks (opinionated defaults)

These are the defaults to propose in discovery unless the user has a preference or the project already uses something else. "Best" here means: proven at scale, easy to hire for, great DX, strong ecosystem, low maintenance. Always confirm with the user and record the choice + rejected alternatives in `PLAN.md`.

## Web app (most projects)

| Layer | Choice | Why |
|---|---|---|
| Framework | **Next.js (React) or SvelteKit** | Full-stack, SEO-capable, huge ecosystem. SvelteKit if you want less boilerplate. |
| Language | **TypeScript (strict)** | Catches real bugs; non-negotiable for anything non-trivial. |
| Styling | **Tailwind CSS + headless UI (Radix/shadcn)** | Fast, consistent tokens, accessible primitives. |
| Data fetching | Framework's built-in (server components / load functions) | Avoid extra state libraries for server data. |
| ORM | **Drizzle** or **Prisma** | Typed queries, migrations. |
| Database | **PostgreSQL** (Supabase/Neon/RDS) | The default relational DB; JSON when you need flexibility. |
| Auth | **Better Auth** or platform auth (Supabase/Clerk) | Don't hand-roll auth. |
| Validation | **Zod** | One schema, shared types client+server. |
| Testing | **Vitest + Playwright** | Fast unit tests + real E2E. |
| Hosting | **Vercel** (app) + managed Postgres | Zero-ops start; portable via Docker later. |

## API / backend service

- **Node**: Fastify or Hono + TypeScript + Zod + Drizzle/Prisma + PostgreSQL + Vitest. (Express only if maintaining legacy.)
- **Python**: FastAPI + Pydantic + SQLAlchemy + PostgreSQL + pytest. (Django if you need the admin/batteries.)
- **Go**: stdlib `net/http` or chi + sqlc + PostgreSQL + `go test`. Best for high-throughput/simple deploys.
- **Default pick: Fastify/Hono + TypeScript** when the team is JS; **FastAPI** when data/ML-heavy.

## CLI / developer tool

- **Node**: TypeScript + Commander/clack + Vitest — publishable to npm instantly.
- **Go**: single static binary, trivial distribution — pick when the tool must run anywhere with no runtime.

## Mobile

- **React Native (Expo)** — one codebase with the web team; EAS for builds.
- **Flutter** — best when UI fidelity/perf matters and there's no web overlap.
- Backend: reuse the API stack above.

## Data / ML / AI features

- Python: FastAPI service + **uv** for deps + ruff/mypy + pytest.
- Vector store: **pgvector** (keep it in Postgres until scale forces otherwise).
- Queue: **Redis (BullMQ/ARQ)** or managed (SQS) — don't run Kafka for one worker.

## Realtime

- WebSockets via the app framework (Socket.IO if JS) or **Phoenix/LiveView** for Elixir fans.
- Default: start with polling/SSR if realtime isn't a stated requirement — add it when the plan says so.

## DevOps (day one, GitHub-native)

- **GitHub Actions**: lint + typecheck + tests on every PR.
- **Docker** for anything with stateful deps; docker-compose for local.
- **Fly.io / Railway / Render** for small services; **AWS/GCP** only when requirements demand it.
- **Sentry** (errors) + structured logs; **OpenTelemetry** when you need tracing.

## Deliberately NOT chosen (defaults rejected)

- MongoDB for relational data → Postgres (JSONB when needed)
- Redux/Zustand for server data → framework data layer
- Microservices for a new product → modular monolith until scale proves otherwise
- GraphQL by default → REST until a client actually needs it
- CSS-in-JS new projects → Tailwind
- Rolling your own auth, date, or validation libs → proven libraries

## How to use this file

1. In discovery, ask the user if they have stack preferences/constraints.
2. Propose the matching row above (or justify a deviation with evidence).
3. Record final choices + rejected alternatives in `PLAN.md` §4.
4. Once chosen, the whole project follows it — no per-file stack drift.
