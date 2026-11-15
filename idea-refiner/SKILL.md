---
name: Idea Refiner
description: Use when a raw prompt or vague idea needs to become a precise, AI-understandable IDEA.md — one batch of smart questions with best-guess answers, 1–3 passes until a fresh model could build from it alone.
---

# Idea Refiner

Raw ideas are underspecified — an AI fills the gaps with guesses. This skill removes the guessing: it takes whatever the user wrote (one sentence, a paragraph, a rambling voice note) and refines it into a **brief so complete that a fresh AI with no chat history could build the right thing from it alone.**

## Process — up to 3 passes, then hand off

Each pass improves the brief, shows the user the result, and asks only about what genuinely can't be inferred. Stop early if the brief already passes the checklist; never exceed 3 passes — after 3, hand the best version to `micro-planner` and note remaining unknowns as assumptions.

### Pass 1 — Interpret and expose gaps
- Restate the idea in one precise paragraph (the user confirms or corrects this first).
- List every ambiguity: undefined terms, missing users, unstated platforms, vague verbs ("manage", "handle", "fast"), missing failure paths.
- Answer what you can from context; turn the rest into **3–7 targeted questions max**, grouped in one batch.

### Pass 2 — Add the missing dimensions
Fill in, explicitly and in writing:
- **Who** uses it, and their journey (happy path + what happens when it fails).
- **What** exists in v1 vs. out of scope; the data involved (what's created/read/changed/deleted).
- **How it looks/feels**: platform(s), tone, reference products, quality bar ("better than X").
- **Constraints**: budget/free-tier, timeline, must-integrate-with, compliance.
- **Success criteria**: how anyone knows it works ("a customer can book in <30 seconds").
- Quantify every fuzzy word: "fast" → loads in under 2s; "lots of users" → hundreds/day; "simple" → ≤3 clicks to the core action.

### Pass 3 — Harden for AI consumption
- Rewrite as unambiguous, testable requirements — numbered, one requirement each, no "should/maybe/somehow".
- Resolve contradictions; make every requirement verifiable by a test or a demo.
- Add the implied-but-unstated things (empty states, mobile, errors, permissions) as explicit requirements.
- **The hand-off test:** could a brand-new model build exactly this from this document, with zero chat history? If it needs a sentence of oral tradition to be correct, that sentence belongs in the brief.

## Output

Write the refined brief to **`IDEA.md`** at the project root (create the repo folder first if none exists — see `build-anything`'s GitHub-native rules). Structure:

```markdown
# IDEA.md — the brief
## One-paragraph summary          # the user's "yes, that's it" statement
## Users & journeys               # who, happy path, failure paths
## Requirements                   # numbered, testable, v1
## Out of scope                   # explicit non-goals
## Quality bar                    # what "better than expected" means here
## Constraints & integrations     # budget, time, external services
## Success criteria               # measurable
## Assumptions                    # everything inferred, flagged for user confirmation
```

Then hand off to **`micro-planner`** (brief → staged `PLAN.md`). If the user only has an idea and is non-technical, this runs inside `idea-to-product`, which translates their language and owns the technical parts of the brief.

## Rules

- The user's intent is sacred: refining means *clarifying and completing*, never changing what they asked for. Improvements go in as proposals they approve.
- Show, don't ask: every question is preceded by your best-guess answer ("I'm assuming X — correct me if wrong").
- Keep `IDEA.md` plain-language — a non-developer must read it and say "yes, that's my idea, only clearer."
- Never start `micro-planner` on an unconfirmed Pass-1 restatement.
