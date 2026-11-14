# TODO.md — Project Task Ledger

> **The single source of truth for granular execution.** Generated from `PLAN.md` *before any application code*.
> Rules: check off `- [x]` immediately after a task passes tests/lint; **never build anything not listed here** — new requirements get added as tasks *first*; one task = one file/module/feature.
> Keep the stage titles identical to `PLAN.md` §6 so the two files always map 1:1.

## Stage 1: {{Foundation & setup}}

- [ ] Initialize project structure and configuration files (from `templates/`)
- [ ] Set up database schema and environment variables (`.env.example`)
- [ ] Create `README.md` / `STATUS.md` skeletons and first CI run

## Stage 2: {{Core features}}

- [ ] {{Build authentication middleware}} — `src/auth/middleware.ts`
- [ ] {{Auth routes (register/login/logout)}} — `src/auth/routes.ts` + tests
- [ ] {{Main dashboard UI components}} — `src/dashboard/`

## Stage 3: {{…}}

- [ ] …

<!-- Task-writing rules:
     - Atomic: a single file, module, or feature — if it needs two verbs ("set up X and Y"), split it.
     - Verifiable: you can point at the test or demo that proves it done.
     - Named by outcome, not activity: "Auth routes return 401 on bad password" > "work on auth".
     - Include the test task explicitly when it isn't obvious from the task itself.
     - Edge cases and multi-file dependencies become their own tasks, never "part of" a vague one. -->
