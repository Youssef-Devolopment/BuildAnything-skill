# First-time handbook (read once — new project or first-time use)

This is the onboarding guide for the `build-anything` skill. Read it **once** when you first load the skill in a project (or when introducing the system to a new human/AI user), then work from the main `SKILL.md` — the working card — from then on. Don't re-read this file on every task.

## What this system is

The universal build skill: **any AI, any model, any project.** The thesis: *the quality of the work must not depend on how big the model is* — frontier-level output comes from the process (plan → gate → verify → document), not the parameter count. Everything below exists to make that process survive contact with small models, free quotas, and session handoffs.

## The pipeline (new project, in order)

1. **`idea-refiner`** — raw idea → AI-proof `IDEA.md`
2. **`micro-planner`** — → `PLAN.md` of small, verifiable stages
3. **`build-anything`** (this skill) — stage-gated execution
4. **`recommendations`** — what to add next (built only if approved)
5. **`readiness-judge`** — evidence-based READY / READY WITH FIXES / NOT READY
6. **`open-or-private`** — structure for the choice; if open source, `open-source-showcase` adds logo, README, site

Skip nothing without saying why. Non-developers: `idea-to-product` wraps all six. "Clone X": `clone-anything` (websites and apps have methods in its `references/`).

## The five docs (the memory system)

The whole system runs on files in the repo — nothing important lives only in chat:

| Doc | Answers | Written when |
|---|---|---|
| `PLAN.md` | What are we building and why? | Before any code (interview → plan → approval) |
| `TODO.md` | What exact steps remain? | Pre-code, from PLAN §6; `- [x]` each task only with green output |
| `STATUS.md` | What's true *right now*? | Flipped at every stage gate — the anti-drift ledger |
| `CHANGELOG.md` | How did we get here? | Append-only entry at every gate; releases tagged |
| `README`/`STRUCTURE.md` | How does a stranger run this? | GitHub-native from day one |

If any of these is stale, fixing it is part of handoff, not optional.

## Who this is for

- **Developers** — you make the technical calls; the skill enforces gates, evidence, and docs.
- **Non-developers** — `idea-to-product` (or this skill with the Full tier) asks product questions in plain language, makes tech decisions for you, and explains each in one sentence. You review demos, not code.
- **Small/free models** — the load-on-demand map and `references/core-protocol.md` exist so a weak model can run the loop without reading everything; evidence rules exist because weak models self-grade badly.

## Day-one checklist (Full tier)

1. Survey the workspace (Phase 0) and state what you detected.
2. One batch of ≤5 interview questions, best guesses attached.
3. Write `PLAN.md` (unanswered → §9 Assumptions), get approval.
4. Write `TODO.md` — atomic tasks grouped by stage.
5. Create the folder layout from `PLAN.md` §5 before first code.
6. Create the doc skeleton (STATUS, CHANGELOG, README) — `references/repo-and-docs.md`.
7. Build under stage gates — the working card has the loop.

## Where the deep protocols live

Everything else is in `references/` next to the main file, opened only when its situation occurs — see the load-on-demand map in `SKILL.md`. The most important one: `references/recovery-loop.md` (the 5-step error loop), which is what keeps a weak model from thrashing.
