---
name: Micro Planner
description: Turn a refined idea brief into a PLAN.md with many small, individually verifiable stages — never big batch plans. Each stage: one outcome, files, steps, acceptance criteria, test, demo. Load after idea-refiner when the brief is confirmed, before any code. Output is executed by build-anything's stage gates.
---

# Micro Planner

Big batch plans ("build the backend", "make the UI") fail: they can't be tested mid-way, reviewed late, or recovered when wrong. This skill cuts the work into stages so small that **each one is finished, tested, demoed, and reviewed before the next begins.**

## Input → Output

- **Input:** a confirmed `IDEA.md` (from `idea-refiner`). If it doesn't exist or isn't confirmed, stop — send it back to `idea-refiner`.
- **Output:** `PLAN.md` at the project root, in the standard 10-section format from `build-anything`, with §6 (Implementation) written as **micro-stages**.

## How to cut stages

**Size rule:** a stage is one sitting of work — roughly 30–90 minutes for a human reviewer, a handful of files, one clear demoable outcome. If you can't explain it in one sentence and demo it in under a minute, it's too big — split it.

Splitting heuristics:
- **By layer** first: schema → API → UI → wiring, never two layers in one stage.
- **By screen/endpoint**: one endpoint, one screen, one flow per stage.
- **By state**: "screen renders" and "screen loads real data with loading/empty/error" are two stages.
- **By risk**: anything uncertain (new integration, unfamiliar API) gets its own tiny spike stage *first*, so a wrong assumption costs one stage, not five.
- Ban these whole-stage names: "set up the project", "implement features", "finish the app", "polish". A stage named "wire checkout button to POST /orders and show success/error states" is the right size.

**Order:** dependency-driven and demoable early — skeleton + a thin end-to-end slice (one thing working start to finish) before breadth. The user sees something real by stage 3–4, not at the end.

**Budget check:** count stages × estimate vs. the user's timeline from `IDEA.md`; if over, cut scope (§3) with the user — never inflate stage size to hide the overrun.

## Stage format (every stage in §6)

```markdown
### Stage N: <one-sentence outcome>
- **Files:** src/orders/routes.ts, src/orders/routes.test.ts, …
- **Steps:** exact build order (small enough that nothing is left vague)
- **Acceptance criteria:** verifiable checkboxes a reviewer can tick
- **Test:** the specific test(s) that must pass (name/type)
- **Demo:** the exact action that proves it works ("POST /orders with cart → 201 + order in DB")
- **Docs:** which .md files this stage updates (usually STATUS.md)
```

Each stage must independently satisfy `build-anything`'s stage gate: clean least code → tests pass → errors fixed or reported → user review. Also write §8 (Testing & QA) per layer and §10 (Definition of done) from `build-anything`.

## Sanity pass before presenting

- [ ] Every requirement in `IDEA.md` maps to ≥1 stage (trace them; show the mapping if unsure)
- [ ] Every stage has test + demo + acceptance criteria
- [ ] No stage mixes layers; no stage is a batch
- [ ] Thin end-to-end slice appears in the first third
- [ ] Risky items are isolated early spike stages
- [ ] §3 out-of-scope matches `IDEA.md`

Present the stage list (titles + demos only, one screen) for approval — the user approves *order and outcomes*, not code details. Then hand execution to **`build-anything`** (stage gates), which runs tests at every gate; after completion the pipeline continues with `recommendations` → `readiness-judge` → `open-or-private`.

## Rules

- Never merge stages "because they're related" — related stages are the easiest ones to split further.
- A stage that can't be demoed is a documentation task, not a build stage — put it in another stage's "Docs" line.
- If discovery during a stage reveals the plan is wrong: stop, revise `PLAN.md`, get approval, then continue (never improvise around a bad plan).
