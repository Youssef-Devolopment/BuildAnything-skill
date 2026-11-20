# BuildAnything

The universal build skill set — one system that makes **any AI, with any model, build anything** the right way: interviewed first, planned in `PLAN.md`, built stage by stage with clean least-code, tested, reviewed, and documented so the next agent (human or AI) picks it up cold.

## Skills

| Skill | ID | What it does |
|---|---|---|
| **BuildAnything** | `build-anything` | The orchestrator — a **working card** (tier table: Resume / Fix / Feature / Full, 8 principles, stage gates with evidence, dry-run rule, routing) for daily use, plus `references/first-time-guide.md` read once for onboarding. Deep protocols in `references/` load on demand. Runs the pipeline: idea-refiner → micro-planner → stage-gated build → recommendations → readiness-judge → open-or-private. |
| **Idea Refiner** | `idea-refiner` | Raw prompt/vague idea → polished, AI-understandable `IDEA.md` in 1–3 passes. |
| **Micro Planner** | `micro-planner` | `IDEA.md` → `PLAN.md` of many small, individually verifiable stages — never batch plans. |
| **Idea To Product** | `idea-to-product` | For the user who has *only an idea* — developer or not. Plain-language interview, tech decisions made for them, a readable plan, and a build that beats what they imagined. |
| **Clone Anything** | `clone-anything` | Rebuild an existing product: contract (clone behavior never identity, v1 core loop, beat-the-original bar) with specialized methods in `references/` for websites and apps. |
| **Design UI** | `design-ui` | Design systems, layout, typography, color, every-state design, WCAG AA accessibility. |
| **Frontend** | `frontend` | Components, state hierarchy, data fetching, performance, a11y, testing. |
| **Backend** | `backend` | API design, schema-first data, deny-by-default security, observability, integration tests. |
| **Database** | `database` | Schema modeling, migrations, indexes, query performance, backups. |
| **Website** | `website` | Landing/marketing/static sites: content first, SEO, Core Web Vitals, Lighthouse ≥95. |
| **Mobile App** | `mobile-app` | Expo/React Native: safe areas, permissions, offline states, store submission. |
| **Testing** | `testing` | Test strategy per layer, test quality bar, killing flaky tests. |
| **Deployment** | `deployment` | CI/CD, environments, hosting choices, releases, rollback, go-live checklist. |
| **AI Features** | `ai-features` | LLM integration, prompts as code, RAG, evals, cost/latency, guardrails. |
| **Project Skill Creator** | `project-skill-creator` | Builds the project's own in-repo SKILL.md from a fill-in template (`templates/PROJECT-SKILL.md`) — day one skeleton + ~50% full capture. |
| **Caveman Report** | `caveman-report` | Compressed reporting style for stage-gate reviews, delivery summaries, and error explanations — same facts and evidence, no filler. |
| **Recommendations** | `recommendations` | After the build: prioritized list of missing features/ideas with evidence — nothing built until approved. |
| **Readiness Judge** | `readiness-judge` | Independent evidence-based verdict: READY / READY WITH FIXES / NOT READY. |
| **Open Or Private** | `open-or-private` | Asks open-source vs. private, then structures the repo for that choice (license+community files vs. owner-runnable structure). |
| **Open Source Showcase** | `open-source-showcase` | For open-source projects: SVG logo, a 30-second README (badges, screenshot, tested quickstart), and a one-page GitHub Pages website. |

Reference: [`build-anything/references/stacks.md`](build-anything/references/stacks.md) — opinionated best-stack defaults for web, API, CLI, mobile, ML, and DevOps. Scaffolding templates (`.gitignore`, CI workflow, doc skeletons, `.env.example`) live in [`build-anything/templates/`](build-anything/templates/TEMPLATE.md) — copy, fill, done.

## Install

Repo: **https://github.com/Youssef-Devolopment/BuildAnything-skill** (public — clone, download, or copy freely)

Pick **one** method. All of them give you the same 20 skills.

> ### ⚠️ Use exactly ONE option — never two
> Options 1–4 are **alternatives**, not steps. Running two (e.g. cloning into the skills folder *and* registering a path in `opencode.json`) creates **two copies** — OpenCode loads only one of them by precedence, edits to the losing copy look ignored, and updates silently stop applying.
>
> Already ran more than one? Run **`.\install.ps1 -Doctor`** — it detects every copy, prints them, and gives the exact fix.

### Option 1 — OpenCode, one-liner (auto-discovery, recommended)

Clone straight into OpenCode's global skills folder — it discovers nested `SKILL.md` files automatically, no config changes:

```powershell
git clone https://github.com/Youssef-Devolopment/BuildAnything-skill.git "$env:USERPROFILE\.config\opencode\skills\buildanything"
```

macOS/Linux: `git clone https://github.com/Youssef-Devolopment/BuildAnything-skill.git ~/.config/opencode/skills/buildanything`

**If you did Option 1, stop here — do NOT also do Option 2.**

### Option 2 — OpenCode, clone anywhere + register (single copy, `git pull` updates)

Clone to any folder (this machine uses `C:\Buildanything skill`), then add it to `~/.config/opencode/opencode.json`:

```jsonc
{
  "skills": ["C:\\Buildanything skill"]
}
```

OpenCode merges `skills` arrays from all config files, so append this to your existing config — don't replace it. Restart OpenCode to pick it up.

### Option 3 — Claude Code / other agents (copy install)

From the repo folder:

```powershell
.\install.ps1 -Target claude    # -> ~/.claude/skills
.\install.ps1 -Target agents    # -> ~/.agents/skills
.\install.ps1 -Target opencode  # -> ~/.config/opencode/skills (copy method instead of clone)
.\install.ps1 -Force            # overwrite an existing older copy
```

Each run copies every skill folder (those containing `SKILL.md`) into the chosen target and prints what was installed/skipped.

### Where does everything go? (global vs project)

| Piece | Where it lives | Why |
|---|---|---|
| `install.ps1` | **In the repo** (root, next to `README.md`) — already committed | You run it from your clone; it reads the skill folders next to it. Don't copy it anywhere else. |
| The skills themselves | Your agent's skills folder (clone or copy — Options 1–3) | That's what makes them load |
| The `skills` registration (Option 2) | **Global config** — `~/.config/opencode/opencode.json` (Windows: `C:\Users\<you>\.config\opencode\opencode.json`) | Applies to **every project** on your machine — recommended, this is how this machine is set up |
| | Project config — `opencode.json` in one project's root | Only applies inside that one project — use only if you want the skill exclusively for that repo |

Both config levels work and **merge**: OpenCode combines the `skills` arrays from global + project configs, so you can register globally and never touch per-project files again. The skills themselves are identical either way.

### Option 4 — No git? Download the ZIP

1. On GitHub: **Code → Download ZIP**
2. Extract anywhere
3. Run `.\install.ps1 -Target claude|agents|opencode`, or copy the skill folders into your agent's skills directory by hand

### Updating

| Method | Update command |
|---|---|
| Clone (Option 1/2) | `.\update.ps1` (or plain `git pull`) in the clone folder |
| Copy (Option 3/4) | Re-run `install.ps1 -Target … -Force` |

### Auto-update (clones)

`update.ps1` (next to this README) manages updates for clone installs:

```powershell
.\update.ps1             # fetch + pull new commits (fast-forward only), show what changed
.\update.ps1 -Status     # just check: up to date or behind? (changes nothing)
.\update.ps1 -Schedule   # register a hidden daily Windows task that runs it for you
.\update.ps1 -Unschedule # remove that task
```

- **Never overwrites your edits** — if you modified the clone by hand it aborts and tells you to commit/stash first.
- Prints **"Restart OpenCode"** after a real update — skill files only reload on restart.
- `-Schedule` runs daily at 09:00 in a hidden window and only reports when there's something new. On macOS/Linux it prints a `crontab` line instead (Windows tasks don't exist there).
- Copy installs (Options 3/4) can't self-update — the script detects that and points you back to `install.ps1 -Force`.

### Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Skills missing / flickering / updates not applying | Two copies installed — OpenCode loads only **one**, by precedence (config entries > project `.opencode/skills` > `~/.config/opencode/skills` > `.agents/skills` > `.claude/skills`), so edits to the losing copy look ignored | Run `.\install.ps1 -Doctor` → it lists every copy, **which one loads**, and the exact cleanup → restart OpenCode |
| `.\install.ps1 -Doctor` says **NOT INSTALLED** | Skills exist only in a folder no agent scans | Run `.\install.ps1 -Target opencode` (or do Option 1) — pick ONE |
| Not sure what you did before | — | `.\install.ps1 -Doctor` is always safe to run; it changes nothing |

The doctor is read-only: it only inspects and reports (exit 0 = one install ✓, 1 = duplicate ✗, 2 = not installed).

### Using the skills

OpenCode discovers them automatically — load one with `@<skill-id>` (e.g. `@build-anything`) or let the model load it via the `skill` tool. Just describing the job often loads the right one too ("clone this landing page" → `clone-anything`). Claude Code picks up `-Target claude` installs the same way.

### Quota control (free/limited models)

Two OpenCode config levers control how much context and how many requests the skills consume. Both are verified against the [skills docs](https://opencode.ai/docs/skills/) and [permissions docs](https://opencode.ai/docs/permissions/).

**1. Hide never-auto-invoked skills from the advertised list.** Descriptions are injected at every model step; hiding a skill cuts its always-on context cost while keeping it loadable by explicit ID. Already set on `open-source-showcase`:

```yaml
# in the skill's SKILL.md frontmatter
metadata:
  opencode/autoinvoke: false
```

**2. Ask before loading the heavy orchestrator** — one `permissions` rule in `~/.config/opencode/opencode.jsonc`:

```jsonc
{
  "permissions": [
    { "action": "skill", "resource": "build-anything", "effect": "ask" }
  ]
}
```

The model must get your yes before spending a session's budget on the full pipeline. (Last matching rule wins; see the permissions doc for `allow`/`deny`/`ask` and wildcards.)

### Eval

[`eval/`](eval/README.md) is this repo's own measurement harness — 10 fixed tasks with pass criteria, scored by running commands (never by self-grading). Run it against any model to compare pass rate, turn count, and honesty:

| File | What it is |
|---|---|
| [`eval/README.md`](eval/README.md) | Protocol: fresh session per task, how to score |
| [`eval/TASKS.md`](eval/TASKS.md) | The 10 task prompts + pass criteria |
| [`eval/RESULTS.md`](eval/RESULTS.md) | Scoreboard — one row per model run |
| `eval/fixtures/` | Small Python projects with known red/green states to run the tasks against |

## Layout

```
C:\Buildanything skill\
├── build-anything/
│   ├── SKILL.md            # working card: tier table, principles, gates, routing (daily use)
│   ├── references/         # first-time-guide, core-protocol, question-bank, stacks, recovery-loop, pre-flight, discovery, repo-and-docs, workflow — loaded on demand
│   └── templates/          # TEMPLATE.md + PLAN/TODO/STATUS/README/ARCHITECTURE/STRUCTURE/CHANGELOG/CHECKLIST skeletons, .env.example, .gitignore, CI workflow
├── idea-refiner/SKILL.md
├── micro-planner/SKILL.md
├── idea-to-product/SKILL.md
├── clone-anything/
│   ├── SKILL.md
│   └── references/         # clone-website, clone-app methods
├── design-ui/SKILL.md
├── frontend/SKILL.md
├── backend/SKILL.md
├── database/SKILL.md
├── website/SKILL.md
├── mobile-app/SKILL.md
├── testing/SKILL.md
├── deployment/SKILL.md
├── ai-features/SKILL.md
├── recommendations/SKILL.md
├── readiness-judge/SKILL.md
├── open-or-private/SKILL.md
├── open-source-showcase/SKILL.md
├── project-skill-creator/
│   ├── SKILL.md
│   └── templates/PROJECT-SKILL.md   # copy-fill skeleton for the project's own skill
├── caveman-report/
│   ├── SKILL.md                      # compressed reporting style for reviews + summaries
│   └── references/modes.md           # intensity ladder (lite/full/ultra) + worked examples
├── eval/                   # 10-task measurement harness (README, TASKS, RESULTS, fixtures)
├── scripts/verify.py       # self-verification: frontmatters + fixture red/green states
├── .github/workflows/verify.yml  # CI: runs scripts/verify.py on every push
├── install.ps1             # Windows installer + -Doctor
├── update.ps1              # git updater (+ daily auto-update schedule)
├── CHANGELOG.md            # release history, newest first
└── README.md
```

## Versioning

Releases are tagged (`v1.0`, `v1.1`, …) and summarized in [`CHANGELOG.md`](CHANGELOG.md) — newest first, append-only, one entry per release. The commit history is the full record behind it. This repo follows its own protocol: append a `CHANGELOG.md` entry in the same commit as the change, tag to match.
