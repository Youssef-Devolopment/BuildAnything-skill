---
name: BuildAnything
description: Use when starting or continuing any project build, deciding architecture, or writing significant code — picks the process tier, plans in PLAN.md, executes under stage gates with evidence, documents for handoff. Orchestrator for all other BuildAnything skills.
---

# BuildAnything — working card

The universal build skill: **any AI, any model, any project.** First time in this project? Read `references/first-time-guide.md` once, then work from this card.

## If you need it, go here (load on demand)

| Situation | Read |
|---|---|
| First-time read / new project onboarding | `references/first-time-guide.md` |
| Weak/free model, quota limits, minimum ceremony | `references/core-protocol.md` (includes the capability contract) |
| A command, build, or test failed | `references/recovery-loop.md` — run the 5-step loop immediately |
| Before shipping a stage / closing a gate | `references/pre-flight.md` |
| New project: interview, `PLAN.md`, `TODO.md`, Phase 0 | `references/discovery.md` |
| Interviewing the user | `references/question-bank.md` — copy-paste, max 5 |
| Docs, structure, CHANGELOG, cold-start handoff prompt | `references/repo-and-docs.md` |
| Execution steps, definition of done | `references/workflow.md` |
| Choosing a tech stack | `references/stacks.md` |

## First: survey, then state your tier

Survey the workspace (root, manifests/configs, git state, existing `PLAN.md`/`TODO.md`/`STATUS.md`), then state one short block: what you detected and which tier you're in. Wrong detection or tier = ask, don't assume.

| Trigger | Tier | Run |
|---|---|---|
| `STATUS.md` exists and is fresh | **Resume** | `STATUS.md` → next unchecked `TODO.md` task → continue. One status line; no re-interview. |
| Bug fix / small change (≤3 sentences) | **Fix** | Task sketch → code → test → done. No interview, no `PLAN.md`. |
| Single feature in an existing repo | **Feature** | 5-line mini-plan (or `PLAN.md` §6 addition) → build → verify → gate. |
| New project, or "build/create an app/site/thing" | **Full** | `references/first-time-guide.md` → `references/discovery.md` → `PLAN.md` → `TODO.md` → stage gates. |

The pipeline is invariant — only its size adapts. **Never scale the rigor down, only the ceremony.**

## Core principles

1. **Never guess** — verify by reading and running; never invent APIs, paths, or behavior.
2. **Least code, best result** — least *unnecessary* code, never least readable; no speculative abstractions; delete what you can.
3. **Real work, not AI slop** — features work end to end, edge cases handled, verified; no placeholders shipped as "done".
4. **Templates are a starting point** — strip what this project doesn't need.
5. **Think first, search before you answer** — decompose, read the actual source/docs, plan before code. Process beats parameter count.
6. **The path that leaves the least code behind wins** — no wrappers or duplication (still not an excuse to gold-plate).
7. **Deliver better than asked** — anticipate the next need, say one line what you added and why; additions beyond `PLAN.md` go in a "proposed additions" list, confirmed by the user in one message.
8. **Judge visual polish yourself** — `prefers-reduced-motion`, content readable before effects, budget green; state the call in one line.

## Stage gates (every stage, in order)

> clean least code → tests pass → *any command failed?* → **`references/recovery-loop.md`, immediately** → **`references/pre-flight.md`** → `- [x]` this stage's `TODO.md` tasks + append `CHANGELOG.md` + flip `STATUS.md` → **user review with a demo**: run it and show it (screenshot for UI, raw command output otherwise — "tests green" alone is not a demo).

**Evidence rule:** every "done" carries pasted raw output (or the screenshot). Never write "should work", "looks correct", or "verified" without it; a `- [x]` without green output is a lie the judge will catch.

**Gate clears = four updates in the same change:** `TODO.md` (each `- [x]` backed by green test) · `CHANGELOG.md` (stage entry) · `STATUS.md` (stage flip) · any doc the stage changed. Done = clean, tested, error-free (or errors reported first), reviewed — not "code written".

Errors you can't fix: quote the exact error, say what it means, propose the fix — **before** moving on. Never swallow an error.

## Dry-run preview (major changes)

```text
Dry run: I'll change <file(s)> by <what — one sentence> — because <why/risk>.
Approve? (y, or tell me to change it)
```

**Major (preview required):** wholesale rewrite, 3+ files in one move, new dependency, schema/migration, auth/payments/deletion, anything destructive. **Not major:** next unchecked `TODO.md` task, test fixes, formatting, docs. No code before approval; read-only investigation is free. Hands-off mode ("just build it") makes it a statement — destructive still blocks. Approval covers only what was described.

## Delegate to sub-skills

| Task | Load |
|---|---|
| Raw idea → AI-proof `IDEA.md` | `idea-refiner` |
| Brief → `PLAN.md` of small stages | `micro-planner` |
| User has only an idea / is non-technical | `idea-to-product` |
| What to add next | `recommendations` |
| Is it actually ready to release? | `readiness-judge` |
| Open-source or private? | `open-or-private` |
| Open source: logo, README, site | `open-source-showcase` |
| Rebuild an existing product ("clone X") | `clone-anything` (websites/apps → its `references/`) |
| UI/UX and design systems | `design-ui` |
| Client-side / server-side code | `frontend` / `backend` |
| Websites / mobile apps | `website` / `mobile-app` |
| Data layer, testing, shipping | `database` / `testing` / `deployment` |
| AI/LLM features | `ai-features` |
| The project's own knowledge skill | `project-skill-creator` |
| Choosing a stack | `references/stacks.md` |

Not listed (CLI tools, payments, pipelines)? Follow this card's process and quality bar — the pattern is the same.

**Handoff** (switching models/tools/sessions): the cold-start prompt lives in `references/repo-and-docs.md`.
