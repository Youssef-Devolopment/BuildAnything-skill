---
name: BuildAnything
description: Use when starting or continuing any project build, deciding architecture, or writing significant code — picks the process tier, plans in PLAN.md, executes under stage gates with evidence, documents for handoff. Orchestrator for all other BuildAnything skills.
---

# BuildAnything

The universal build skill: **any AI, any model, any project.** The process produces the result, not the parameter count. This file is the entry point — tier decision, principles, gates, routing. Deep protocols live in `references/`; **open one only when its situation calls for it, never preload them.**

## If you need it, go here (load on demand)

| Situation | Read |
|---|---|
| A command, build, or test failed | `references/recovery-loop.md` — run the 5-step loop immediately |
| Before shipping a stage's code / closing a gate | `references/pre-flight.md` — evidence checklist |
| New project: interview, `PLAN.md`, `TODO.md` protocol, Phase 0 detection | `references/discovery.md` |
| Docs, folder structure, templates, versioning/CHANGELOG, tooling tips | `references/repo-and-docs.md` |
| Reasoning discipline, day-to-day execution steps, definition of done | `references/workflow.md` |
| Choosing a tech stack | `references/stacks.md` |
| Brand-new session with no context | Cold-start prompt at the bottom of this file |

## First: survey, then state your tier

Survey the workspace first (root, manifests/configs, git state, existing `PLAN.md`/`TODO.md`/`STATUS.md`), then state one short block: what you detected and which tier you're in. Wrong detection or tier = ask, don't assume.

| Trigger | Tier | Run |
|---|---|---|
| `STATUS.md` exists and is fresh | **Resume** | `STATUS.md` → next unchecked `TODO.md` task → continue. One status line; no re-interview, no new plan. |
| Bug fix / small change (described in ≤3 sentences, no new feature) | **Fix** | Task sketch → code → test → done. No interview, no `PLAN.md`. |
| Single feature in an existing repo | **Feature** | 5-line mini-plan (or a `PLAN.md` §6 addition) → build → verify → gate. |
| New project, or "build/create an app/site/thing" | **Full** | `references/discovery.md` → `PLAN.md` → `TODO.md` → stage gates. |

The pipeline is invariant — only its size adapts: a one-file script and a 20-stage product share plan → gate → verify → document. **Never scale the rigor down, only the ceremony.**

## Core principles

1. **Never guess** — verify by reading and running; when something unknown matters, ask or investigate. Never invent APIs, paths, or behavior.
2. **Least code, best result** — least *unnecessary* code, never least readable; no speculative abstractions or "just in case" boilerplate; delete what you can.
3. **Real work, not AI slop** — every line earns its place, features work end to end, edge cases handled, and you verified it. No placeholders shipped as "done".
4. **Templates are a starting point** — strip what this project doesn't need; shape the architecture around the project, not the boilerplate.
5. **Think first, search before you answer** — decompose, grep/read the actual source and docs, show the plan before the code. Frontier-level output comes from the process, not the parameter count.
6. **Pick the path that leaves the least code behind** — the quicker route that leaves wrappers or duplication is **no** (still not an excuse to gold-plate).
7. **Deliver better than asked** — anticipate the next need (empty state, error path, mobile view), raise the quality bar, and say one line what you added and why. Never silently shrink or change the goal; additions beyond `PLAN.md` go in a "proposed additions" list, confirmed by the user in one message.
8. **Judge visual polish yourself** — decide alone whether animation/3D genuinely helps; guardrails: `prefers-reduced-motion`, content readable before effects, budget stays green (tiers in `design-ui`, budget in `website`); state the call in one line at review.

## Stage gates (every stage, in order)

> clean least code → tests pass → *any command failed?* → **`references/recovery-loop.md`, immediately** → **`references/pre-flight.md`** → check off this stage's `TODO.md` tasks + append `CHANGELOG.md` + flip `STATUS.md` → **user review with a demo**: run it and show it (screenshot for UI, raw command output otherwise — "tests green" alone is not a demo).

**Evidence rule:** every "done" carries pasted raw output (or the screenshot). Never write "should work", "looks correct", or "verified" without it; a `- [x]` without green output is a lie the judge will catch.

**When a gate clears — four updates in the same change:** `TODO.md` (all this stage's tasks `- [x]`, each backed by its green test) · `CHANGELOG.md` (stage entry) · `STATUS.md` (flip the stage ledger — the anti-context-drift tracker) · any doc the stage changed. A stage is done when it is clean, tested, error-free (or errors reported to the user first), and reviewed — not when the code was written.

Errors you can't fix: quote the exact error, say what it means, propose the fix — **before** moving on. Never swallow an error, never carry a known failure into the next stage.

## Dry-run preview: say it before you do it (major changes)

Before executing any **major** modification, post a two-line preview and get a yes — the user has 100% control over their code:

```text
Dry run: I'll change <file(s)> by <what — one sentence> — because <why/risk>.
Approve? (y, or tell me to change it)
```

**What counts as major (preview required):** rewriting a file wholesale, touching 3+ files in one move, adding a dependency, any schema/migration change, anything touching auth, payments, or data deletion, and anything destructive or hard to reverse (overwrites, deletes, force operations).

**What doesn't (don't nag):** the next unchecked `TODO.md` task already in the approved plan, test fixes, formatting, docs edits — the stage gates already cover those.

Rules:
- The preview states files + approach + risk, not an essay; name one alternative in a line if a real choice exists.
- No code for that change is written before the approval. Read-only investigation is always allowed without asking.
- If the user already granted hands-off mode ("just build it"), the preview becomes a statement before execution instead of a blocking question — but destructive or irreversible changes still block.
- An approval covers exactly what was described; a different change needs a new preview. "Go on for the rest of the stage" grants blanket approval until the next gate.

## The pipeline (new project, in order)

1. **`idea-refiner`** — raw idea → AI-proof `IDEA.md`
2. **`micro-planner`** — → `PLAN.md` of small, verifiable stages
3. **`build-anything`** (this skill) — stage-gated execution
4. **`recommendations`** — what to add next (built only if approved)
5. **`readiness-judge`** — evidence-based READY / READY WITH FIXES / NOT READY
6. **`open-or-private`** — structure for the choice; if open source, `open-source-showcase` adds logo, README, site

Skip nothing without saying why. Non-developers: `idea-to-product` wraps all six. "Clone X": `clone-anything` (websites → `clone-website`, apps → `clone-app`).

## Delegate to sub-skills

For specialized work, load the matching sub-skill instead of improvising:

| Task | Load |
|---|---|
| Raw idea/prompt → detailed, AI-understandable `IDEA.md` | `idea-refiner` |
| Brief → `PLAN.md` with small, verifiable stages | `micro-planner` |
| The user has only an idea (developer or not) — translate it into a product | `idea-to-product` |
| What should we add next? — prioritized features/ideas | `recommendations` |
| Is the project actually ready? — independent evidence-based verdict | `readiness-judge` |
| Open-source or private? — ask, then structure the repo for that choice | `open-or-private` |
| Open source: logo, 30-second README, project website (GitHub Pages) | `open-source-showcase` |
| Rebuild an existing product ("clone X") — any kind | `clone-anything` (websites → `clone-website`, apps → `clone-app`) |
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
| Choosing the tech stack for a project type | `references/stacks.md` |

Not listed but needed (e.g. CLI tools, data pipelines, payments)? Follow this skill's process and the quality bar — the pattern is the same.

## Cold-start prompt (model/session handoff)

Switching models, tools, or chat windows mid-project must be frictionless. Use this exact 3-line prompt to resume any BuildAnything project from zero context — give it to the user (or paste it into the new session yourself):

```text
Read PLAN.md, TODO.md, STRUCTURE.md, and .opencode/skills/<project-id>/SKILL.md.
State our current status from STATUS.md and CHANGELOG.md.
Tell me the next unchecked task from TODO.md and what you need from me to start it.
```

The prompt is only as good as the docs — if STATUS/CHANGELOG are stale, fixing them is part of handoff, not optional. For a *brand-new* project (no docs yet), the cold-start prompt is instead `idea-refiner`'s input: paste your raw idea.
