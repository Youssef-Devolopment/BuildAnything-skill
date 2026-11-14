---
name: BuildAnything
description: The universal build skill — works with any AI, any model, any project. Before any code, interview the user with many detailed questions until the project is fully understood, then write a PLAN.md with the full plan; then think step by step and research instead of guessing (works on any model, small or large), write the least code that truly solves the problem, choose the best technology, produce real quality (not AI slop), keep a clean organized folder structure and .md documentation GitHub-native from day one, recommend MCPs/plugins/skills that make the work easier, and at the ~50% mark capture everything about the project in its own project skill. Use when starting or continuing any project, deciding architecture, writing significant code, or when asked to "do your best work".
---

# BuildAnything

The universal build skill: **any AI, any model, any project.** Load it to turn a vague idea into a shipped, quality product — no matter which model is running this session, this process is what produces the result, not the parameter count. If this skill is present, work follows it; specialized sub-skills (`design-ui`, `frontend`, `backend`, `website`, `mobile-app`, `project-skill-creator`) extend it for specific layers.

## Core principles

1. **Never guess.** Before writing code, read the existing code, configs, docs, and tests. Verify assumptions with actual evidence (run the command, read the source, check the version). If something is unknown and matters, ask the user or investigate — do not invent APIs, paths, or behavior.
2. **Least code, best result.** Prefer the smallest change that fully solves the problem. No speculative abstractions, no premature frameworks, no boilerplate "just in case". Delete code when you can. But never sacrifice correctness or readability for brevity — "least" means least *unnecessary*, not least readable.
3. **Real work, not AI slop.** AI slop looks like: generic variable names, dead code, copy-pasted blocks, TODO walls, half-finished features, "placeholder" UI, over-engineered layers, and docs that describe what the code *might* do. Real work means: every line earns its place, the feature actually works end to end, edge cases are handled, and you verified it.
4. **Templates are a starting point, not the answer.** Strip out anything the project doesn't need. Shape the architecture around this specific project's requirements, not around what a boilerplate gives you.
5. **Think first, search before you answer — on any model.** The quality of the work must not depend on how big the model is. Smaller models compensate with discipline: slow down, reason step by step, and research instead of recalling from memory. Frontier-level output comes from the process, not the parameter count.
6. **Two paths to the same result: pick the one that leaves the least code behind.** If one route is longer to do but clean, and another is quicker but leaves unnecessary code, wrappers, or duplication in the repo — the quick one is **no**. Speed never justifies code the project must maintain forever. (This is not an excuse to gold-plate: the "long" path must still be the *least* code that solves the problem, just built in the right shape.)
7. **Deliver better than what was asked.** The user describes what they *can* articulate; your job is the product they *would have asked for* if they knew what was possible. So: (a) understand the intent behind the request, not just its literal words; (b) anticipate the next need — the empty state, the error path, the mobile view, the thing they'll ask for next week — and build it in; (c) raise the quality bar above the request (faster, clearer UI, fewer clicks, better defaults); (d) when you improve on their idea, say so — one line: what you added and why it's better. Never silently *shrink* the idea to the literal ask, and never silently *change* what they asked for — improving quality, scope coverage, and UX is welcome; changing the goal is not.

## Reasoning and research discipline (for any model size)

Treat these as mandatory steps, not optional extras — they are how a smaller model produces work on par with the largest ones:

1. **Decompose before answering.** Break the task into concrete sub-questions (what exists? what's the constraint? what does the API actually do? what could break?). Answer them in order instead of jumping to a conclusion.
2. **Search, don't recall.** Memory of APIs, flags, versions, and library behavior goes stale. For anything version-specific or unfamiliar: search the codebase (`grep`, `glob`), read the actual source/docs, and use web search for current facts. Quote evidence for claims that matter.
3. **Show the reasoning before the code.** Before writing anything, state the plan: which files change, what the approach is, what you rejected and why. If the plan doesn't survive contact with the evidence, revise the plan — not the evidence.
4. **Consider the alternatives deliberately.** For any non-trivial decision, name at least one alternative and why it loses. This counters the small-model tendency to latch onto the first plausible answer.
5. **Stress-test your own answer.** Ask "what's wrong with this?" before presenting it: check edge cases, false assumptions, and whether it actually satisfies the original request. Verify by running/reading, never by hoping.
6. **Escalate instead of guessing.** If reasoning stalls — contradictory evidence, missing information, repeated failed attempts — stop and ask the user or investigate further. A confident wrong answer is the worst outcome; a slow, verified right answer is the senior-engineer answer.

## Discovery: ask until you fully understand, then plan

**Before writing a single line of code, run this phase. Do not skip it, even for "small" tasks.**

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

2. **Real-time tracking** — after completing each task **and verifying it passes tests/linting**, immediately check it off (`- [x]`) *before* moving to the next item. A checked box without a green test is a lie the judge will catch.

3. **Scope discipline** — building features **not listed in `TODO.md` is forbidden**. New requirements discovered mid-build are added as tasks (or routed through `PLAN.md` if they change scope) *first*, so the roadmap remains the single source of truth. No side quests, no "while I'm here" additions.

`TODO.md` is the *granular* twin of `PLAN.md` (plan = what/why per stage; TODO = every atomic step), and `STATUS.md` is the *summary* (ledger of stages for handoff). All three update at their respective gates.

## Stage gates: finish one stage before starting the next

> **Stage-gate checklist** (every stage, in order): clean least code → tests pass → *if any command fails: run the 5-step recovery loop below* → **pre-flight sanity check** (below) → check off this stage's `TODO.md` tasks + append `CHANGELOG.md` entry + flip the `STATUS.md` stage ledger → user review.

The implementation section of `PLAN.md` is ordered stages. Each stage must be **fully closed** before the next one begins:

1. **Clean code only** — the stage's code is the least working code that satisfies its acceptance criteria. Nothing extra, nothing half-done.
2. **Test the stage** — write/run tests for exactly what the stage added; the suite passes.
3. **Fix or report every error** — fix what you can. Any error you cannot fix must be **reported to the user first** (quote the exact error and say what it means and what you propose) before moving on. Never silently swallow an error, never carry a known failure into the next stage.
4. **User review checkpoint** — summarize what the stage delivered, show it working (run it), and get the user's review/OK. Gaps and errors the user spots are fixed here, before the next stage starts.

Repeat for every stage. A stage is not "done" because the code was written — it is done when it is clean, tested, error-free (or errors reported), and reviewed.

**When a gate clears — four file updates in the same change:**
1. `TODO.md` — every task of this stage is `- [x]` (each one verified by its test/lint first).
2. `CHANGELOG.md` — append the stage entry (see the versioning protocol below).
3. `STATUS.md` — flip the stage ledger line: `- [x] Stage N: {{outcome}} (Completed on YYYY-MM-DD)` and mark the next one `- [ ] … — In Progress`. This ledger is the anti-context-drift tracker: a fresh session reads it and knows *precisely* where work stopped.
4. Any doc the stage's behavior changed (same-change doc rule).

## Pre-flight sanity check (mandatory)

Before outputting a stage's code — and again before any deploy/release — run `templates/CHECKLIST.md` and answer every line with evidence:

1. **Env vars** — everything the code reads exists in `.env.example`?
2. **Dependencies** — everything imported is declared in the package file, lockfile-consistent?
3. **No secrets or placeholders** — zero hardcoded keys, no TODO/lorem/fake data pretending to work?

Before the *gate* closes additionally: tests green from the README command, fresh-clone path works, docs touched, secrets scan clean. One explicit `no` = don't ship; fix first (cheap now, expensive later). Never answer "should be fine" — the answer needs the command run or the file:line checked.

## Failure recovery: the 5-step correction loop

**Trigger: immediately**, whenever a test fails, a build errors, **or any command execution fails** — no exceptions, no "try something and see". This protocol prevents trial-and-error and random code modifications:

1. **Capture** — save the *exact* error: full message, stack/line, and the command that produced it. Copy it unmodified — no paraphrasing, no truncating the stack.
2. **Read** — open the source file(s) the error points at (and their callers). Read the actual code; don't reason from memory of what it probably says. Pinpoint the exact line of failure.
3. **Hypothesize** — state **one** root cause as a single, clear, direct, testable sentence: "X fails because Y at line Z." If you can't name one specific cause, you don't understand the error yet — go back to step 2 (read deeper: the error is often in a file away from the crash site — follow the data, not the stack trace).
4. **Fix minimally** — apply the bare minimum change that makes the hypothesis true. No rewriting entire files, no drive-by refactors, no "while I'm here" cleanup, no invalid/placeholder code (AI slop). One fix per iteration.
5. **Verify** — re-run the **exact failing command** (then the full suite/build) to confirm the error is completely eliminated and the stage transitions successfully. Green → done; red → back to step 1 with the *new* error.

Rules:
- **One fix per loop iteration.** Changing three things at once makes it impossible to know which one worked.
- **Cap at 3 iterations.** Two loops with no progress → stop, write up (captured error + what you read + your hypothesis + what you tried) and report to the user. Never thrash.
- **A fix that needs a new dependency, a schema change, or >~20 lines** is a plan change: revise `PLAN.md` first, get approval, then fix.
- Log every fixed error in `CHANGELOG.md` → Fixed (error text → cause → fix), so the next agent never re-stumbles into it.

## Keep the repo GitHub-native from day one

Everything needed to understand, run, and continue the project lives **as files in the repository**, committed from the first day — no knowledge that exists only in chat history:

- All docs (`PLAN.md`, `TODO.md`, `README.md`, `STRUCTURE.md`, `ARCHITECTURE.md`, `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`) are committed files.
- Setup, scripts, and decisions are reproducible from a fresh `git clone`: install → run → test works with no private context.
- `.gitignore` excludes secrets and build artifacts; `.env.example` documents required variables.
- CI (if the platform supports it) runs lint + tests on push from day one.
- Commit early and often; the commit history tells the story of each stage.

**Organized folder structure from day one** — decide the layout in `PLAN.md` §5 and create it before the first feature, not after files pile up at the root. Typical shape:

```text
project/
├── PLAN.md  README.md  STRUCTURE.md  ARCHITECTURE.md  STATUS.md  DECISIONS.md
├── src/            # application code, grouped by feature or layer (pick one, stay consistent)
├── tests/          # test files mirroring src/ (or colocated — pick one, stay consistent)
├── scripts/        # dev/build/deploy helpers
├── docs/           # anything beyond the root .md set
├── public/ or app/ # static assets / platform entry (as the stack dictates)
└── .github/        # workflows
```

One place for each kind of file; no loose files at the root beyond the documented set; naming consistent within every folder.

**Scaffold from templates, don't invent structure.** This skill ships copy-from templates in `templates/` (next to this SKILL.md): skeletons for `PLAN.md`, `README.md`, `STATUS.md`, `ARCHITECTURE.md`, `STRUCTURE.md`, `CHANGELOG.md`, plus `.env.example`, a profiled `.gitignore`, and a GitHub Actions CI workflow. Read `templates/TEMPLATE.md` first — it says which template to copy when and where. Copy → fill every placeholder → delete sections that don't apply; shipping a template with placeholder text is a readiness blocker.

## Versioning & CHANGELOG protocol

`CHANGELOG.md` is the project's chronological memory (template in `templates/CHANGELOG.md`), newest first, append-only:

- **Every stage-gate review**: append a versioned entry `## [0.N — stage name] — YYYY-MM-DD` with `Added` (the outcome + its one-line demo) and `Fixed` (error text → cause → fix, from the recovery loop). Same change as the code.
- **Release**: bump to `vX.Y.Z`, move `Unreleased` items under the version heading, tag the commit to match. SemVer: fix → patch, feature → minor, breaking → major.
- **Never rewrite entries.** The history is evidence; `readiness-judge` cross-checks stage completion against it.
- `STATUS.md` answers "what's true *now*"; `CHANGELOG.md` answers "how did we get here". Keep both current at every gate.

## Cold-start prompt (model/session handoff)

Switching models, tools, or chat windows mid-project must be frictionless. Use this exact 3-line prompt to resume any BuildAnything project from zero context — give it to the user (or paste it into the new session yourself):

```text
Read PLAN.md, TODO.md, STRUCTURE.md, and .opencode/skills/<project-id>/SKILL.md.
State our current status from STATUS.md and CHANGELOG.md.
Tell me the next unchecked task from TODO.md and what you need from me to start it.
```

Rules: the prompt is only as good as the docs — if STATUS/CHANGELOG are stale, fixing them is part of handoff, not optional. For a *brand-new* project (no docs yet), the cold-start prompt is instead `idea-refiner`'s input: paste your raw idea.

## Project-specific skill (capture at ~50%)

At day one create the folder skeleton, and **when the project reaches ~50% (or its first major milestone), load the `project-skill-creator` skill** and produce `.opencode/skills/<project-id>/SKILL.md` inside the repo — a complete, self-contained description of *this* project (stack, commands, conventions, decisions, gotchas, current state) so any AI in any future session rebuilds full context from one file. Keep it updated at every stage gate from then on.

## Recommend tooling that makes the work easier

During the work, watch for friction a tool would remove. When one would materially help — an **MCP server** (browser automation, database introspection, Figma design import, API docs lookup), a **plugin**, or another **skill** — recommend it to the user with a one-line benefit and how to enable it (e.g. `opencode.json` `mcp` entry). Examples worth suggesting:

- Browser/Playwright MCP → verifying UI in a real browser during stage gates
- Database MCP → inspecting real schema/data instead of guessing
- Context7 or docs MCP → current library docs instead of stale memory
- Figma MCP → building exactly what the designer drew

Never silently depend on a tool that isn't installed: check availability, and if absent either work without it or ask the user to install it first.

## The pipeline (in order)

For a new project, run these skills as one pipeline — each hands off to the next:

1. **`idea-refiner`** — raw idea/prompt → polished, AI-proof `IDEA.md` (1–3 passes until perfect)
2. **`micro-planner`** — `IDEA.md` → `PLAN.md` with many **small** stages (never batch plans)
3. **`build-anything`** (this skill) — executes stages under stage gates; tests everything, fixes or reports every error
4. **`recommendations`** — what the project still needs: prioritized feature/idea list (built only if approved)
5. **`readiness-judge`** — independent verdict: READY / READY WITH FIXES / NOT READY, with evidence
6. **`open-or-private`** — user picks open-source vs. private; repo structured accordingly; if open source, **`open-source-showcase`** adds logo, 30-second README, and project website

Skip nothing without saying why. `idea-to-product` wraps steps 1–6 for non-developers.

## Delegate to sub-skills

This skill is the orchestrator. For specialized work, load the matching sub-skill instead of improvising:

| Task | Load |
|---|---|
| Raw idea/prompt → detailed, AI-understandable `IDEA.md` | `idea-refiner` |
| Brief → `PLAN.md` with small, verifiable stages | `micro-planner` |
| The user has only an idea (developer or not) — translate it into a product | `idea-to-product` |
| What should we add next? — prioritized features/ideas | `recommendations` |
| Is the project actually ready? — independent evidence-based verdict | `readiness-judge` |
| Open-source or private? — ask, then structure the repo for that choice | `open-or-private` |
| Open source: logo, 30-second README, project website (GitHub Pages) | `open-source-showcase` |
| UI/UX, visual design, design systems | `design-ui` |
| Frontend implementation (components, state, routing, performance) | `frontend` |
| Backend implementation (APIs, data models, auth, business logic) | `backend` |
| Websites: landing pages, marketing/static sites, SEO, performance | `website` |
| Mobile apps: Expo/React Native, native features, store release | `mobile-app` |
| Data layer: schema, migrations, indexes, query performance | `database` |
| Testing strategy: what to test, how, keeping the suite trustworthy | `testing` |
| Shipping: CI/CD, environments, hosting, releases, rollback | `deployment` |
| AI/LLM features: prompts, RAG, evals, cost, guardrails | `ai-features` |
| Creating the project's own knowledge skill (day one + ~50% capture) | `project-skill-creator` |
| Choosing the tech stack for a project type | read `references/stacks.md` in this skill's directory |

Not listed but needed (e.g. CLI tools, data pipelines, payments)? Follow this skill's process and the quality bar — the pattern is the same.

## Workflow

### Step 1: Understand before building
- Run the **Discovery** phase above first: interview the user until you fully understand, then write and get approval on `PLAN.md`.
- Read the whole relevant surface: existing source, `README`/docs, package manifests, config files, tests.
- List what must be true for this to work (constraints, data shapes, integrations) and verify each one rather than assuming.

### Step 2: Choose the best technology deliberately
- Pick the technology that fits the problem and the project's existing stack — not the newest, not the most familiar.
- Justify the choice in the docs: what you chose, what you rejected, and why.
- Prefer boring, proven, well-supported tools over novel ones unless the project genuinely needs novelty.
- For UI: build a real, polished interface — proper states (loading, empty, error, success), accessible markup, consistent spacing/typography, responsive behavior. No lorem ipsum, no fake data, no unfinished screens shipped as "done".
- For backend: real validation, real error handling, sane security defaults, no endpoints that silently fail.

### Step 3: Build it right
- Write the code that solves the actual problem, following the conventions already in the repo.
- Handle errors where they can occur; don't swallow them.
- Review your own diff before presenting it as complete: search for leftovers, debug code, duplicated logic, and dead paths.

### Step 4: Test and verify
- Run existing tests before and after your change; never leave a failing suite behind.
- Add tests for the behavior you introduce — especially edge cases and error paths. Match the project's existing test style and coverage level.
- Verify the way a user would: run the app, hit the endpoint, click the flow. A green test suite is not proof the feature works.
- If verification reveals a wrong assumption, fix the assumption in the docs too — don't just patch the symptom.

### Step 5: Build secure by default
- Never hardcode secrets, tokens, or credentials — use environment variables or the project's secret mechanism, and never commit `.env` files.
- Validate all external input at the boundary (user input, API requests, files) and treat output/encoding rules as mandatory for the stack.
- Keep dependencies minimal: every dependency must earn its place, be actively maintained, and be pinned to a known-good version. Prefer the standard library over a package when they're equivalent.
- Review what you add for known trade-offs (supply chain risk, bundle size, lock-in) and note significant ones in the docs.

### Step 6: Make it observable
- Log what matters with context (event, identifiers, outcome) at sensible levels — info for flow, warn/error for problems. No stray `console.log` debug noise shipped as the only signal.
- Show users actionable error messages; put diagnostic detail in logs, never stack traces or secrets in the UI.
- Never log secrets, tokens, or personal data.

### Step 7: Ship in small, honest steps (git hygiene)
- Keep changes focused: one concern per commit/PR, and keep the test suite green at every commit.
- Write commit messages that explain *why*, not just what changed.
- Self-review the diff before committing: no debug leftovers, no commented-out code, no unrelated files.

### Step 8: Document for the next agent (human or AI)
Maintain `.md` files so someone with zero context — including another AI — can understand the project and know exactly what to build next. Keep them accurate; stale docs are worse than no docs.

Maintain at minimum:
- **`PLAN.md`** — the approved plan from the discovery phase (see above). The contract for what is being built and why.
- **`CHANGELOG.md`** — append-only timeline: one entry per stage gate (Added/Fixed/Changed), release headings with tags. See the versioning protocol above.
- **`STRUCTURE.md`** — a plain-language tour of the project for a human reader: the folder/file tree annotated with what each part does, where to make which kind of change, and the main entry points. Someone who has never seen the repo should understand its shape in one read.
- **`README.md`** — what the project is, how to install, run, test, and deploy it.
- **`ARCHITECTURE.md`** — the system's shape: major components, how data flows between them, key design decisions and their rationale, technology choices and rejected alternatives.
- **`STATUS.md`** (or a section in README) — what is done, what is in progress, what is next, known issues. This is the handoff document: the next AI should be able to read it and know exactly what to make.
- **`DECISIONS.md`** (optional, for larger projects) — short entries: context → decision → consequences.

Rules for docs:
- Write for someone who knows nothing about the project.
- Update the doc in the same change that alters the behavior it describes.
- Document *why*, not just *what* — the "what" is in the code.
- Never document unimplemented features as if they exist.

## Definition of done

- Every stage in `PLAN.md` passed its gate: clean least-code, tested, all errors fixed or reported to the user first, and reviewed by the user before the next stage.
- The pre-flight sanity check passed with evidence (env vars, dependencies, no secrets/placeholders — plus tests/docs/secrets at gate close).
- `STATUS.md` stage ledger is current: every cleared stage is `- [x]` with a date, next stage marked in progress.
- `PLAN.md` exists, was written before any code, and matches what was actually built.
- `TODO.md` exists (generated pre-code from the plan), every completed task is `- [x]` with its test green, and nothing was built that wasn't on it.
- The feature works and you have verified it by running it.
- Tests cover the new behavior and the suite passes.
- The code is the least code that fully solves the problem, and every line is intentional.
- The UI/backend meets real-world quality bars: no placeholders, no swallowed errors, no fake data.
- No secrets in code or logs; external input is validated; dependencies are justified and pinned.
- Errors and key events are logged with enough context to debug in production.
- All affected `.md` files are updated so the next AI knows the current state and what to build next.
- The repo is GitHub-native: a fresh clone installs, runs, tests, and explains itself (`README.md`, `STRUCTURE.md`) with no private context.
- The folder structure matches the layout decided on day one — files live where they belong, consistently.
- `CHANGELOG.md` has an entry per cleared stage gate, and releases are tagged to match.
- Every error hit during the build went through the 5-step recovery loop (no thrash patches; unresolved ones reported to the user).
- At ~50%: `.opencode/skills/<project-id>/SKILL.md` exists and is current — any AI can rebuild full project context from it alone.
- Any tool friction worth removing was surfaced to the user as a concrete MCP/plugin/skill recommendation (or confirmed unnecessary).
- Nothing was guessed: every assumption about the codebase or external APIs was verified.
