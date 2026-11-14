---
name: Recommendations
description: After a build, analyze the project and propose what it still needs — missing features, improvements, and ideas prioritized by value and effort — without building anything until approved. Load after build stages complete (or at any checkpoint) when the user asks "what should we add?" or before readiness review. Output feeds PLAN.md / STATUS.md.
---

# Recommendations

The build does what `IDEA.md` asked. This skill answers the next question: **"What should this project have that it doesn't yet?"** — as a prioritized, evidence-based proposal, never as unrequested code.

## When to run

- After the main build stages complete (pipeline position: after `build-anything`, before `readiness-judge`).
- At any checkpoint the user asks "what's next / what should we add?"
- Findings from here do **not** get built until the user approves them into `PLAN.md` as new stages (via `micro-planner`'s format).

## Sources — look in this order

1. **The project itself**: run it, click through it, read `PLAN.md`/`STATUS.md`/code. What's missing, slow, rough, or unhandled? Dead ends in the UX? Error paths that dump raw failures? Any TODO you wrote?
2. **`IDEA.md`'s quality bar & dream-version answers** — the user already told you what "better" looks like; gap against it.
3. **The category checklist** — what users of this kind of product always expect (e.g. for a booking app: confirmation/cancel, reminders, timezone handling, search/filter, roles; for a landing page: analytics, testimonials, favicon, meta images). List only what fits *this* product.
4. **The evidence**: analytics gaps, error logs, performance numbers if available — real signals beat guesses.

## Output format

Present in chat first (table), then write approved items into `STATUS.md` → Next actions (and `PLAN.md` if scheduled):

| # | Recommendation | Why it matters (evidence) | Effort | Impact |
|---|---|---|---|---|
| 1 | … | … | S/M/L | High/Med/Low |

Rules for the list:
- **Max ~10 items**, ranked — quick wins (S+High) first. A list of 40 ideas is noise; curate.
- Every item ties to evidence: a user need from `IDEA.md`, something observed in the running app, or a stated category norm — not "it would be cool".
- Split **bug/gap** (definitely should fix — goes before readiness) from **feature idea** (optional — goes to a "v2 ideas" section).
- Include at least one **"do nothing" option** when the project already meets its bar — recommending restraint is a senior move.
- Effort must be honest: an S estimate that becomes M when started is worse than a correct M.

## Handoff

- Gaps/bugs → propose as immediate extra stages (micro-planner format) before `readiness-judge`.
- Approved features → `PLAN.md` §6 as new stages, then `build-anything` gates them.
- Rejected/v2 ideas → `STATUS.md` → Next actions (or a `ROADMAP.md` for larger projects), so nothing the user liked is forgotten.
- Then run **`readiness-judge`** for the verdict.

## Rules

- Propose, don't build: zero code changes in this skill.
- No filler items to look thorough — if the honest answer is "it's feature-complete", say exactly that.
- Every recommendation must be understandable by a non-developer in one sentence (they're often the decision-maker — see `idea-to-product`).
