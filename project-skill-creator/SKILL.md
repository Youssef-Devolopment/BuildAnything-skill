---
name: Project Skill Creator
description: Create the project-specific knowledge skill — a SKILL.md inside the repo that captures everything about this project (stack, structure, conventions, commands, gotchas, state) so any AI can rebuild full context instantly. Load at project day one (skeleton) and at the ~50% mark (full capture), then keep it updated. Used with build-anything.
---

# Project Skill Creator

The general skills (`build-anything`, `frontend`, …) teach *how* to work. This skill creates the file that teaches *what this specific project is*. It lives **in the repository**, so it travels with GitHub and is available to every future session and every collaborator's AI.

## When

- **Day one** — create the folder skeleton immediately, with the real identity/stack filled in and a "Current state: just started" note. The skill exists from commit #1.
- **~50% / first major milestone** — fill in the full capture: architecture, conventions, decisions, and everything hard-won so far.
- **Ongoing** — update it in the same change that invalidates any of it (same rule as all docs).

## Where

```
.opencode/skills/<project-id>/SKILL.md    ← committed to the repo (GitHub-native)
```

`<project-id>` is lowercase kebab-case matching the project name (e.g. `acme-store`). This overrides any global skill of the same ID for this project — which is exactly what a project-specific skill should do.

## What it must contain

```markdown
---
name: <project-id>
description: Everything about <project> — <one-line what it is>. Load when working on this repo.
---

# <project> — project skill

## What this project is
One paragraph: the goal, the users, what "done" means. Pointer to PLAN.md.

## Stack & versions
Languages, framework, DB, key libs — with versions and *why each was chosen*.

## Repo map
The folder tree annotated in one line per folder. Pointer to STRUCTURE.md for the full tour.

## Commands
install / run dev / test / lint / build / migrate / deploy — exact commands, copy-pasteable.

## Conventions
Naming, file layout, error style, logging style, commit style, branch flow — whatever this
repo actually does, stated as rules.

## Key decisions & rejected alternatives
Short list: decision → why. Pointer to DECISIONS.md for the full log.

## Gotchas & hard-won knowledge
The non-obvious stuff: flaky test and its workaround, the API quirk that cost a day,
the env var nobody remembers, "never do X here because Y".

## Current state & next actions
What's built, what's in progress, what's next. Pointer to STATUS.md for detail.
```

## Rules

1. **Index, not encyclopedia.** Keep it tight (target ≤150 lines). Deep detail lives in `ARCHITECTURE.md`, `DECISIONS.md`, `STATUS.md` — link to them instead of duplicating (duplicated docs go stale twice as fast).
2. **Written for a zero-context reader.** A brand-new AI (or human) must be able to work productively after reading only this file.
3. **Only verified facts.** Never describe an unimplemented feature as done — this file is the project's memory, and false memory is worse than none.
4. **Commands must be tested.** Paste-and-run works from a fresh clone.
5. **Gotchas are the crown jewels.** Actively append every surprising thing discovered while building — that's the highest-value section for the next agent.
6. Update it at every stage gate alongside the other `.md` files.
