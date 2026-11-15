---
name: Project Skill Creator
description: Use when creating or updating the project's own SKILL.md — day-one skeleton, ~50% full capture, kept current at every stage gate so any AI can rebuild context from one file.
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

**Copy [`templates/PROJECT-SKILL.md`](templates/PROJECT-SKILL.md) from this skill's folder** to `.opencode/skills/<project-id>/SKILL.md`, then fill every `<angle-bracket placeholder>`. The template is fill-in-the-blank:

- The file ships with all nine sections and the fill-in rules in an HTML comment at the top — a finished file has **zero `<...>` placeholders left**.
- **Never delete a section you don't understand** — write `TBD — <when it will be known>` instead (day-one skeleton: most sections get a one-line TBD or "just started" note).
- Only verified facts go in: commands you actually ran, features that actually work.

Sections: *What this project is* · *Stack & versions* · *Repo map* · *Commands* · *Conventions* · *Key decisions & rejected alternatives* · *Gotchas & hard-won knowledge* · *Current state & next actions*.

## Rules

1. **Index, not encyclopedia.** Keep it tight (target ≤150 lines). Deep detail lives in `ARCHITECTURE.md`, `DECISIONS.md`, `STATUS.md` — link to them instead of duplicating (duplicated docs go stale twice as fast).
2. **Written for a zero-context reader.** A brand-new AI (or human) must be able to work productively after reading only this file.
3. **Only verified facts.** Never describe an unimplemented feature as done — this file is the project's memory, and false memory is worse than none.
4. **Commands must be tested.** Paste-and-run works from a fresh clone.
5. **Gotchas are the crown jewels.** Actively append every surprising thing discovered while building — that's the highest-value section for the next agent.
6. Update it at every stage gate alongside the other `.md` files.
