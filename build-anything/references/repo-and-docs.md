# Repo, docs, versioning, tooling (read when writing docs or structuring the repo)

## Keep the repo GitHub-native from day one

Everything needed to understand, run, and continue the project lives **as files in the repository**, committed from the first day — no knowledge that exists only in chat history:

- All docs (`PLAN.md`, `TODO.md`, `README.md`, `STRUCTURE.md`, `ARCHITECTURE.md`, `STATUS.md`, `CHANGELOG.md`, `DECISIONS.md`) are committed files.
- Setup, scripts, and decisions are reproducible from a fresh `git clone`: install → run → test works with no private context.
- `.gitignore` excludes secrets and build artifacts; `.env.example` documents required variables.
- CI (if the platform supports it) runs lint + tests on push from day one.
- Commit early and often; the commit history tells the story of each stage.

**Organized folder structure from day one** — decide the layout in `PLAN.md` §5 and create it before the first feature, not after files pile up at the root. Typical shape:

```text
project/
├── PLAN.md  README.md  STRUCTURE.md  ARCHITECTURE.md  STATUS.md  DECISIONS.md
├── src/            # application code, grouped by feature or layer (pick one, stay consistent)
├── tests/          # test files mirroring src/ (or colocated — pick one, stay consistent)
├── scripts/        # dev/build/deploy helpers
├── docs/           # anything beyond the root .md set
├── public/ or app/ # static assets / platform entry (as the stack dictates)
└── .github/        # workflows
```

One place for each kind of file; no loose files at the root beyond the documented set; naming consistent within every folder.

**Scaffold from templates, don't invent structure.** This skill ships copy-from templates in `templates/` (next to this SKILL.md): skeletons for `PLAN.md`, `README.md`, `STATUS.md`, `ARCHITECTURE.md`, `STRUCTURE.md`, `CHANGELOG.md`, plus `.env.example`, a profiled `.gitignore`, and a GitHub Actions CI workflow. Read `templates/TEMPLATE.md` first — it says which template to copy when and where. Copy → fill every placeholder → delete sections that don't apply; shipping a template with placeholder text is a readiness blocker.

## Versioning & CHANGELOG protocol

`CHANGELOG.md` is the project's chronological memory (template in `templates/CHANGELOG.md`), newest first, append-only:

- **Every stage-gate review**: append a versioned entry `## [0.N — stage name] — YYYY-MM-DD` with `Added` (the outcome + its one-line demo) and `Fixed` (error text → cause → fix, from `recovery-loop.md`). Same change as the code.
- **Release**: bump to `vX.Y.Z`, move `Unreleased` items under the version heading, tag the commit to match. SemVer: fix → patch, feature → minor, breaking → major.
- **Never rewrite entries.** The history is evidence; `readiness-judge` cross-checks stage completion against it.
- `STATUS.md` answers "what's true *now*"; `CHANGELOG.md` answers "how did we get here". Keep both current at every gate.

## Project-specific skill (capture at ~50%)

At day one create the folder skeleton, and **when the project reaches ~50% (or its first major milestone), load the `project-skill-creator` skill** and produce `.opencode/skills/<project-id>/SKILL.md` inside the repo — a complete, self-contained description of *this* project (stack, commands, conventions, decisions, gotchas, current state) so any AI in any future session rebuilds full context from one file. Keep it updated at every stage gate from then on.

## Recommend tooling that makes the work easier

During the work, watch for friction a tool would remove. When one would materially help — an **MCP server** (browser automation, database introspection, Figma design import, API docs lookup), a **plugin**, or another **skill** — recommend it to the user with a one-line benefit and how to enable it (e.g. `opencode.json` `mcp` entry). Examples worth suggesting:

- Browser/Playwright MCP → verifying UI in a real browser during stage gates
- Database MCP → inspecting real schema/data instead of guessing
- Context7 or docs MCP → current library docs instead of stale memory
- Figma MCP → building exactly what the designer drew

Never silently depend on a tool that isn't installed: check availability, and if absent either work without it or ask the user to install it first.
