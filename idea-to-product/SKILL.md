---
name: Idea To Product
description: Turn a bare idea into a finished product for a user who may not be a developer — plain-language interview, technical decisions made and explained simply, then a readable PLAN.md and a build that beats what they imagined. Load when the user has "just an idea", asks to build something from a description, or is non-technical. Entry point that delegates to build-anything and the layer skills.
---

# Idea To Product

For the user who has **an idea and nothing else** — no code, no stack preference, maybe no technical vocabulary. They describe it in their own words; you deliver the product they meant, or better. Everything else in this skill set is loaded *for* them, not *by* them.

## Process

### 1. Listen in their language
- Take the idea as given, however vague: "a thing where customers book appointments" is enough to start.
- Ask **product questions only**: Who uses it? What should they see first? What does success look like? What have they seen that they liked/disliked? What's the dream version?
- No jargon. Never ask a non-developer about stacks, frameworks, databases, or hosting. If they *are* a developer, adapt and include them in technical choices.
- Reflect back a one-paragraph "here's what I understand you want" and get a yes before anything else.

### 2. Make the technical decisions yourself
You own everything technical. For each decision: choose the best fit (see `build-anything`'s `references/stacks.md`), then explain it in one plain sentence a normal person can read ("Free to start, easy to change later"). Record choices + rejections in `PLAN.md` §4.

### 3. Plan for a non-technical reader
- `PLAN.md` must be readable by the user: plain words first, technical detail in the sections that need it.
- Show the **scope comparison**: "What you asked for" vs "What I'm building (includes X, Y you didn't know to ask for)" — this is where "better than they imagined" becomes visible and approved up front.
- Get approval in plain language: "This is what I'll build — OK?"

### 4. Build, gate, review — as usual
Delegate to `build-anything`: stage gates, least code, tests, errors fixed or reported, user review each stage. For each layer, load the matching skill (`design-ui`, `frontend`, `backend`, `website`, `mobile-app`).
- **Demo in the user's language**: at each review, describe what changed as a user would experience it ("You can now tap Book and pick a time — try it"), not as a developer would ("added POST /appointments").
- Non-developers review *by using it*, not by reading diffs — make it runnable for them with one command (or a deployed preview URL) from the first stage.

### 5. Hand off a project anyone can continue
By the ~50% mark, `project-skill-creator` produces the in-repo skill; `STRUCTURE.md`/`README.md` explain the project in plain words. The user — or any future developer or AI — can pick it up cold.

## The bar: better than they imagined

Actively look for the upgrades the user didn't know to ask for, propose them, and build the ones they approve (fold into `PLAN.md` before coding):

- **They didn't say "mobile"** → it's responsive from the start anyway.
- **They didn't say "what happens when it fails"** → loading, empty, and error states exist.
- **They didn't ask for polish** → real content, consistent design, fast pages.
- **They'll need the next thing** → the obvious v2 hooks exist (export, invite, notification) without building v2.
- **Their dream-version answer from the interview** → treat it as the actual target.

Say what you added and why, in one line, at every review. Never silently *change the goal*; always exceed the *quality and completeness* of the ask.

## Rules

- If you catch yourself writing a sentence the user can't understand, rewrite it.
- Never make the user feel behind: their job is the idea, yours is everything else.
- One idea, one product — resist scope creep from *your* side; extra ideas go to `PLAN.md` §3 (out of scope) or §6 as approved stages.
