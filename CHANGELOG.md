# Changelog

All notable changes to the **BuildAnything skill set** — newest first, append-only. This file is the human-readable summary; the commit history is the full record. Releases are tagged (`v1.0`, `v1.1`, …) to match the entries below.

## [v1.11] — 2026-11-15

### Added
- **`project-skill-creator/templates/PROJECT-SKILL.md`** — a copy-fill skeleton for the project's own in-repo skill: all nine sections pre-built with `<placeholders>`, fill-in rules in a header comment (replace every placeholder, keep every section and write `TBD — <when>` instead of deleting, only verified facts). The AI copies the file and fills it instead of writing the project skill from scratch.
- **`clone-anything/references/clone-website.md` and `clone-app.md`** — the website and app cloning methods moved as load-on-demand references inside `clone-anything`.

### Changed
- **Merged the three clone skills into one** (`clone-anything` with `references/clone-website.md` and `references/clone-app.md`) — deleted the separate `clone-website/` and `clone-app/` directories. Total skills: **21 → 19**. Cross-references in `build-anything/SKILL.md`, README skills table, layout tree, and trigger examples updated.
- **`project-skill-creator/SKILL.md`** — inline template block replaced by a pointer to `templates/PROJECT-SKILL.md` (68 → 41 lines): copy → fill → never delete a section you don't understand.

### Not done (deliberate)
- **Other proposed skill merges** (`readiness-judge` + `recommendations`, demoting `open-source-showcase` into `open-or-private`) remain **not done** — only the clone skills were merged; all other 18 skills stay separate.

## [v1.10] — 2026-11-15

### Added
- **`references/core-protocol.md`** — the whole plan → gate → verify → document loop in one file for weak/free models, quota limits, or minimum ceremony (max-5-question interview, batched reviews, banned-thrash list). Linked from the entry point's load-on-demand map.
- **Interview cap** (`references/discovery.md`) — one batch of **max 5 questions** (max 7 for genuinely complex Full-tier projects), each with a best-guess answer; everything unanswered goes to `PLAN.md` §9 Assumptions by default. No second round unless the user volunteers it or the unknown is unsafe to guess (legal, money, data destruction).
- **`eval/` harness** — 10 fixed tasks (`TASKS.md`) with advance-written pass criteria, protocol (`README.md`: fresh session per task, score from artifacts by re-running commands, never self-grading), scoreboard (`RESULTS.md`), and 5 Python fixtures with pre-verified red/green states: `f1-bug` (RED, exit 1), `f3-resume` (docs-only mid-project), `f4-tricky` (RED — KeyError surfaces in the test, root cause is a typo in `parser.py`), `f7-truth` (RED — docs claim green, tests aren't), `f8-project` (GREEN, exit 0). All states verified with Python 3.12 in this release.
- **Quota-control section in README** — the two OpenCode levers verified against the live docs: `metadata: opencode/autoinvoke: false` (hide from the advertised list, still loadable by ID — already set on `open-source-showcase`, live-verified hidden) and the `permissions` rule `{ "action": "skill", "resource": "build-anything", "effect": "ask" }` for ask-before-spend on the orchestrator.

### Changed
- **`install.ps1 -Doctor` precedence honesty** — instead of "the stale one may win", it now prints **which copy OpenCode actually loads** using the verified precedence (config entries > project `.opencode/skills` > `~/.config/opencode/skills` > `.agents/skills` > `.claude/skills`), says "one of N copies at the same precedence level (search order decides)" when a tie can't be resolved, and warns that `-Target claude/agents` installs also feed OpenCode's search path. Verified: clean exit 0, planted-duplicate exit 1 with tie message, cleanup confirmed.
- **README troubleshooting** — the "stale one wins" row replaced with the real precedence wording; install warning block updated to match.

## [v1.9] — 2026-11-15

### Added
- **Progressive disclosure split** — `build-anything/SKILL.md` cut from 383 lines to a slim entry point (tier table, principles, gates, dry-run rule, routing, cold-start). Deep protocols moved to `build-anything/references/` — `recovery-loop.md`, `pre-flight.md`, `discovery.md`, `repo-and-docs.md`, `workflow.md` — opened only when their situation calls for them, via an "If you need it, go here" map at the top of the entry. All cross-pointers fixed; nothing lost except deliberately trimmed wording.
- **Hard tier table** (Resume / Fix / Feature / Full) with explicit triggers; the model must state its detected state and tier in its first message. Replaces the soft "shrink the process to match" judgment call.
- **Evidence rule** — no "should work", "looks correct", or "verified" without pasted raw command output (or the screenshot).

### Changed
- **All 21 skill descriptions rewritten to trigger form** ("Use when…", ~100–170 chars each) — the always-on catalog drops from ~2,500+ chars of manifesto prose to one tight trigger line per skill, so routing costs less context on every model step.
- **Core principles compressed** to one-line forms in the entry (operative rules kept, examples trimmed); the 8 principles remain all 8.

## [v1.8] — 2026-11-14

### Added
- **Dry-run preview protocol** in `build-anything/SKILL.md`: before any *major* modification (wholesale file rewrite, 3+ files at once, new dependency, schema change, auth/payments/deletion, anything destructive) the AI must post a two-line preview — "I'll change file X this way because Y — approve?" — and get a yes before writing code. Trivial next-task work stays covered by the existing stage gates (no nagging); hands-off mode downgrades it to a statement, but destructive changes always block.
- **`CHANGELOG.md`** (this file) at the repo root — the skill set now practices its own versioning protocol instead of pointing at raw commit history.

## [v1.7] — 2026-11-14

### Added
- **Visual-polish autonomy** — core principle #8: the AI decides on its own whether animations/3D make a result better and states it in one line at review. Backed by a 3-tier motion ladder in `design-ui` (micro → choreographed → showpiece 3D) with skip heuristics and guardrails (`prefers-reduced-motion`, CSS before JS, content before effects), plus an effects budget in `website` (Lighthouse ≥95 always wins).
- **`update.ps1` auto-updater** — `.\update.ps1` (fast-forward pull + what-changed), `-Status` (check only), `-Schedule` / `-Unschedule` (hidden daily Windows task, crontab hint for macOS/Linux). Refuses to overwrite hand edits; detects copy installs and points to `install.ps1 -Force`.
- **Three clone skills** (21 skills total): `clone-anything` (contract: clone behavior never identity, v1 core loop, side-by-side verification, beat-the-original bar), `clone-website` (4-breakpoint capture, section/copy/asset inventory, rebuild top-to-bottom), `clone-app` (flow recording, screen/navigation map, reverse-engineered data model, same-flow walks at every gate).
- **Demo evidence at every stage gate** — "tests green" alone is no longer a review: each gate shows the feature running (screenshot for UI, real command output otherwise).
- **Security floor in the pre-flight checklist** — no secrets in history, `.env*` gitignored, dependency audit clean, no permissive debug/CORS defaults.
- **Global install methods** in the README — one-liner clone into OpenCode's skills folder (auto-discovery), clone+register, copy install for Claude Code/other agents, ZIP download, update table, and a global-vs-project config placement guide.
- **`install.ps1 -Doctor`** — read-only duplicate detector (exit 0/1/2): finds every install copy (auto-discovery, copies, config entries — including nested grouping folders) and prints the exact fix.

### Fixed
- The duplicate-install trap: README now demands **exactly one** install option (warning callout + troubleshooting table funneling to `-Doctor`).
- `install.ps1` rewritten ASCII-only — Windows PowerShell 5.1 read BOM-less UTF-8 em-dashes as ANSI, producing smart-quotes that broke parsing.

## [v1.6] — 2026-11-14

### Added
- **Dynamic Initialization Protocol** — Phase 0 workspace auto-detection (empty / existing / docs / non-project), 3-pillar context injection (stack, objective, constraints) into `PLAN.md`/`TODO.md`, and universal scalable stage gates that fit any project size without scaling down rigor.

## [v1.5] — 2026-11-14

### Added
- **`TODO.md` task ledger protocol** — pre-code atomic breakdown grouped by stage, real-time `- [x]` check-off only after green tests, scope discipline (building anything not listed is forbidden). Wired into gates, templates, readiness-judge, and the cold-start prompt.

## [v1.4] — 2026-11-14

### Added
- **`STATUS.md` stage ledger** — the anti-context-drift tracker: a fresh session reads it and knows exactly where work stopped.
- **Mandatory pre-flight `CHECKLIST.md`** before any stage's code ships.
- Tightened error-loop trigger wording (any command failure, no exceptions).

## [v1.3] — 2026-11-14

### Added
- **Scaffold template system** — copy-from templates for PLAN/TODO/STATUS/README/ARCHITECTURE/STRUCTURE/CHANGELOG/CHECKLIST, `.env.example`, profiled `.gitignore`, CI workflow.
- **5-step failure-recovery loop** — capture → read → hypothesize → fix minimally → verify; one fix per iteration, cap at 3, plan-change escalation.
- **CHANGELOG versioning protocol** and the **cold-start handoff prompt** (3-line model/session handoff).
- Pipeline skills: `idea-refiner`, `micro-planner`, `recommendations`, `readiness-judge`, `open-or-private`, `open-source-showcase`.

## [v1.2] — 2026-11-14

### Added
- Sub-skills: `idea-to-product`, `testing`, `deployment`, `database`, `ai-features`.
- Core principle **"deliver better than asked"** and non-developer discovery adaptation.

## [v1.1] — 2026-11-14

### Added
- Renamed to **BuildAnything**; `install.ps1`, `.gitattributes`, universal (any-AI/any-model) framing.

## [v1.0] — 2026-11-14

### Added
- Initial skill set: `build-anything` senior-engineering orchestrator, `design-ui`, `frontend`, `backend`, `website`, `mobile-app`, `project-skill-creator`, and the stacks reference.
