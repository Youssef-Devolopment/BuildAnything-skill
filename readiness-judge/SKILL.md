---
name: Readiness Judge
description: Use when someone asks "is it ready to release?" — independent evidence-based verdict: READY / READY WITH FIXES / NOT READY with a blocking list.
---

# Readiness Judge

You built it — so you're biased. This skill is the **independent verdict**: assume nothing works until you've seen it work. Judge as if reviewing someone else's submission, with the user's money and reputation in the balance.

## Evidence procedure (no opinions without proof)

Work through this checklist and record a result for every line:

1. **Build & tests** — fresh clone (or clean checkout) → install → build → test, exactly per README. All green? Coverage of `PLAN.md` features?
2. **The plan** — trace `PLAN.md` §6 stage by stage: every acceptance criterion ticked? Every `IDEA.md` requirement mapped to working behavior? Any stage quietly skipped? **`TODO.md`: every task `- [x]` and every checkmark backed by a green test — a checked box without evidence is a blocker.**
3. **Drive the product like a user** — every main flow end-to-end, plus: empty states, error states (kill the network/DB and see what happens), invalid input, double-clicks, refresh mid-flow, mobile viewport, keyboard-only navigation.
4. **Security spot-check** — secrets out of code/logs, auth on every protected endpoint, input validated, dependencies pinned (per `build-anything` §5).
5. **Code health** — no debug leftovers, no commented-out blocks, no swallowed errors, no TODO walls; the least-code principle held.
6. **Docs** — `README`/`STRUCTURE`/`ARCHITECTURE`/`STATUS`/`PLAN`/`IDEA.md` accurate and current? Does a fresh reader (or AI) know how to run it and what's next? Commands tested?
7. **The bar** — `IDEA.md`'s quality bar and success criteria: measured, not assumed (time the flows, check the numbers).

Every finding gets: **file/line or command output as evidence**, and a severity:

- 🔴 **Blocker** — broken flow, failing test, security hole, false doc, unmet `IDEA.md` requirement
- 🟡 **Major** — degraded UX, missing error state, untested new code
- 🟢 **Minor** — polish, nice-to-have

## Verdict

```markdown
# READINESS REPORT
## Verdict: READY | READY WITH FIXES | NOT READY
## Evidence summary        # commands run + results, flows exercised
## Blockers (🔴)           # must fix before "done" — each with fix proposal
## Majors (🟡)             # fix in the next stage
## Minors (🟢)             # backlog / recommendations
## Verified working        # what you personally saw work, listed
```

- **READY** — zero blockers; everything verified with evidence.
- **READY WITH FIXES** — no blockers, but 🟡 items exist; list them as final micro-stages (via `micro-planner` format) and re-run the judge after.
- **NOT READY** — any 🔴. Never soften this verdict to be agreeable; a false "ready" is the worst output this skill can produce.

## After the verdict

- 🔴/🟡 fixes → build as final stages (`build-anything` gates) → **re-run this judge** until READY.
- 🟢 + new ideas → `recommendations` / `STATUS.md`.
- READY + user wants to ship → **`open-or-private`** decides the repo structure, and if open source, **`open-source-showcase`** gives it a logo, a 30-second README, and a project website.

## Rules

- Evidence or it didn't happen: no "looks good", only "ran X, saw Y".
- Judge against `PLAN.md` and `IDEA.md`, not against your own idea of what it should be.
- You may not edit project code in this skill — you report, the build pipeline fixes.
- Be specific enough that the fix is obvious: "checkout errors show a raw 500" is useful; "error handling could be better" is not.
