# Discovery: detect, interview, plan, ledger (read before a new project or feature)

## Dynamic Initialization Protocol (run this first, always)

Before anything else — before questions, before templates, before assuming an empty folder — **inspect the workspace and adapt to it.** This skill must fit any folder, any stack, any project state (empty directory, half-built React app, Python script, Godot repo, legacy codebase) with zero manual reconfiguration.

### Phase 0 — Project auto-detection

Run this the moment the skill is invoked in a project context:

1. **Survey the workspace** — list the root, read existing manifests and configs (`package.json`, `pyproject.toml`, `go.mod`, `project.godot`, `pubspec.yaml`, `Cargo.toml`, lockfiles), git status/history, CI configs, and any existing `PLAN.md` / `TODO.md` / `STATUS.md` / `README` / docs.
2. **Classify the state:**
   - **Empty/new** → full pipeline: `idea-refiner` → `micro-planner` → build (discovery below runs in full).
   - **Existing project, no docs** → detection-first: derive the stack and architecture from code, run discovery *against reality* (ask only what the code can't answer), backfill the doc set, then continue.
   - **Existing project with docs** → read `PLAN.md`/`TODO.md`/`STATUS.md` first: **resume, don't restart.** Update stale docs, pick up the next unchecked task.
   - **Not a project at all** (single script, scratch folder) → shrink the process to match: still plan before code, still gate — but one stage, minimal docs.
3. **State what you detected** in one short block before proceeding: detected stack, project state, what you'll do differently because of it. Wrong detection = ask, don't assume.

### Dynamic context injection

Everything the workflow decides is fed from three pillars gathered by detection + discovery, and injected into `PLAN.md` / `TODO.md` when they're written:

1. **The Stack** — the *active* technologies detected in the workspace (Next.js, Godot, Python, Expo, …), not a default. Templates, CI, and sub-skill choice adapt to it (`templates/TEMPLATE.md` says how; unknown stacks → follow the repo's existing conventions).
2. **The Objective** — what this session must build, refactor, or fix. For a resumed project this comes from `TODO.md`'s next unchecked task; for a new one from `idea-refiner`.
3. **Constraints & preferences** — required libraries, architectural rules, forbidden patterns: explicit user wishes *plus* whatever the existing codebase already implies (its conventions are constraints until the user says otherwise).

### Universal stage gates (same pipeline, any scale)

The execution pipeline is invariant — only its size adapts to the project:

1. **Inception & Discovery** — auto-detect (Phase 0), interview what's unknown, generate the tailored `PLAN.md` + granular `TODO.md` for *this* stack and state.
2. **Execution & task breakdown** — implement tasks atomically, `- [x]` each in `TODO.md` upon verification (tests/lint), before the next.
3. **Self-correction loop** — any build/test/runtime error in *that specific codebase* triggers `recovery-loop.md` immediately — same protocol, whatever the stack.

A 20-stage product and a one-file script share this pipeline; only the number of stages and docs differ. Never scale the *rigor* down (plan → gate → verify → document), only the ceremony.

## Discovery: ask until you fully understand, then plan

**Before writing a single line of code, run this phase. Do not skip it, even for "small" tasks.** (Phase 0 auto-detection above runs first — for resumed projects, much of this phase is answered by the docs already on disk.)

### Phase A — Interview the user
Ask questions in batches until you have complete understanding. A good default is 5–15 questions (more for a new/complex project), grouped by topic, offered together with a `question` tool or as one numbered list so the user can answer in one pass. Keep asking follow-ups while anything important is still unclear. Cover:

**Adapt to who the user is.** This skill is for anyone with an idea — developer or not. Detect their level and match it: if they're a non-developer, ask about the *product* (who uses it, what it does, what it looks like) in plain language — no jargon, no stack questions — and own the technical decisions yourself, stating them in one plain sentence each ("I'll use X so it's free to host and fast"). If they're a developer, they can be part of the technical choices. Either way the outcome is the same: a complete `PLAN.md` the user can actually read.

1. **Goal & users** — What is this project? Who uses it? What does success look like? What problem does it actually solve?
2. **Scope** — What is in v1, and explicitly what is out of scope? Any deadline or must-have feature?
3. **Functional detail** — Walk through the main flows end to end. What happens on the happy path and the failure paths? What data is created, read, updated, deleted?
4. **Non-functional** — Expected scale (users, data volume), performance needs, offline/mobile, security/compliance requirements.
5. **Tech & constraints** — Preferred stack or hard constraints (hosting, budget, language, existing services)? Must integrate with anything? Existing code/docs to read? *(Skip or simplify for non-developers — decide for them and explain.)*
6. **Quality bar** — What does "done and good" mean here? Tests required? Deployment target? Who reviews?
7. **Style & taste** — For UI: reference designs, brands, colors, tone. For API/CLI: conventions to follow.
8. **The bar to beat** — "What would make this *better* than you're imagining?" Ask what they've seen that annoyed them, what their dream version does, what a competitor lacks. That answer is the standard you exceed.

Rules for questioning:
- Base each question on what you already know or found in the codebase — never ask about things you could have read yourself.
- Ask about decisions, not trivia: every question should change what you build.
- If the user doesn't know or says "you decide", record the decision (and the alternative rejected) as an assumption in the plan — don't re-ask, don't silently guess.

### Phase B — Write the plan file
When understanding is complete, **write `PLAN.md` at the project root before any code**. It is the single source of truth for what will be built:

```markdown
# PLAN.md
## 1. Overview          — one-paragraph restatement of the goal and users
## 2. Requirements      — numbered functional requirements (from the interview)
## 3. Out of scope      — explicitly excluded, so nobody builds it later by accident
## 4. Tech stack        — chosen technologies + why (and rejected alternatives + why not)
## 5. Architecture      — components, data model, key flows, integrations
## 6. Implementation    — ordered steps, each with files to create/change and acceptance criteria
## 7. UI/UX             — screens/views, states (loading/empty/error), design references
## 8. Testing & QA      — what must be tested and how it will be verified
## 9. Assumptions & decisions — every "you decide" item, decisions, and open questions
## 10. Definition of done — the checklist this project is judged against
```

### Phase C — Get approval, then build
- Present the plan summary to the user and get explicit approval (or their corrections) before implementing. If the user is hands-off ("just build it"), proceed — but the plan file still must exist first.
- Treat `PLAN.md` as a living contract: when requirements change, update it in the same change that implements them.
- Build exactly the plan. If you discover the plan is wrong, revise `PLAN.md` first, then the code.

### Phase D — Generate the task ledger (`TODO.md` Protocol)

**Before writing a single line of application code**, generate a granular `TODO.md` at the project root (template: `templates/TODO.md`) mapping every step of execution:

1. **Pre-code breakdown** — split the approved `PLAN.md` §6 into **atomic, verifiable tasks grouped by stage gate**. Every task = a single file, module, or feature:
   ```markdown
   # Project TODO Ledger

   ## Stage 1: Foundation & Setup
   - [ ] Initialize project structure and configuration files
   - [ ] Set up database schema and environment variables (`.env.example`)

   ## Stage 2: Core Features
   - [ ] Build authentication middleware and routes
   - [ ] Create main dashboard UI components
   ```
   Atomicity rules: one verb per task (two verbs = split it), you can name the test/demo that proves it done, edge cases and multi-file dependencies are **their own tasks** — never hidden inside a vague one. Stage titles must match `PLAN.md` §6 exactly.

2. **Real-time tracking** — after completing each task **and verifying it passes tests/linting**, immediately check it off (`- [x]`) *before* moving on to the next item. A checked box without a green test is a lie the judge will catch.

3. **Scope discipline** — building features **not listed in `TODO.md` is forbidden**. New requirements discovered mid-build are added as tasks (or routed through `PLAN.md` if they change scope) *first*, so the roadmap remains the single source of truth. No side quests, no "while I'm here" additions.

`TODO.md` is the *granular* twin of `PLAN.md` (plan = what/why per stage; TODO = every atomic step), and `STATUS.md` is the *summary* (ledger of stages for handoff). All three update at their respective gates.
