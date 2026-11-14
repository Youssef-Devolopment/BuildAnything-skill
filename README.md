# BuildAnything

The universal build skill set — one system that makes **any AI, with any model, build anything** the right way: interviewed first, planned in `PLAN.md`, built stage by stage with clean least-code, tested, reviewed, and documented so the next agent (human or AI) picks it up cold.

## Skills

| Skill | ID | What it does |
|---|---|---|
| **BuildAnything** | `build-anything` | The orchestrator + full pipeline: idea-refiner → micro-planner → stage-gated build (clean least-code, test, fix/report errors, user review) → recommendations → readiness-judge → open-or-private. GitHub-native docs, reasoning discipline for any model size, "least code wins", "deliver better than asked". |
| **Idea Refiner** | `idea-refiner` | Raw prompt/vague idea → polished, AI-understandable `IDEA.md` in 1–3 passes. |
| **Micro Planner** | `micro-planner` | `IDEA.md` → `PLAN.md` of many small, individually verifiable stages — never batch plans. |
| **Idea To Product** | `idea-to-product` | For the user who has *only an idea* — developer or not. Plain-language interview, tech decisions made for them, a readable plan, and a build that beats what they imagined. |
| **Design UI** | `design-ui` | Design systems, layout, typography, color, every-state design, WCAG AA accessibility. |
| **Frontend** | `frontend` | Components, state hierarchy, data fetching, performance, a11y, testing. |
| **Backend** | `backend` | API design, schema-first data, deny-by-default security, observability, integration tests. |
| **Database** | `database` | Schema modeling, migrations, indexes, query performance, backups. |
| **Website** | `website` | Landing/marketing/static sites: content first, SEO, Core Web Vitals, Lighthouse ≥95. |
| **Mobile App** | `mobile-app` | Expo/React Native: safe areas, permissions, offline states, store submission. |
| **Testing** | `testing` | Test strategy per layer, test quality bar, killing flaky tests. |
| **Deployment** | `deployment` | CI/CD, environments, hosting choices, releases, rollback, go-live checklist. |
| **AI Features** | `ai-features` | LLM integration, prompts as code, RAG, evals, cost/latency, guardrails. |
| **Project Skill Creator** | `project-skill-creator` | Builds the project's own in-repo SKILL.md (day one skeleton + ~50% full capture). |
| **Recommendations** | `recommendations` | After the build: prioritized list of missing features/ideas with evidence — nothing built until approved. |
| **Readiness Judge** | `readiness-judge` | Independent evidence-based verdict: READY / READY WITH FIXES / NOT READY. |
| **Open Or Private** | `open-or-private` | Asks open-source vs. private, then structures the repo for that choice (license+community files vs. owner-runnable structure). |
| **Open Source Showcase** | `open-source-showcase` | For open-source projects: SVG logo, a 30-second README (badges, screenshot, tested quickstart), and a one-page GitHub Pages website. |

Reference: [`build-anything/references/stacks.md`](build-anything/references/stacks.md) — opinionated best-stack defaults for web, API, CLI, mobile, ML, and DevOps. Scaffolding templates (`.gitignore`, CI workflow, doc skeletons, `.env.example`) live in [`build-anything/templates/`](build-anything/templates/TEMPLATE.md) — copy, fill, done.

## Install

Repo: **https://github.com/Youssef-Devolopment/BuildAnything-skill** (public — clone, download, or copy freely)

Pick one method. All of them give you the same 18 skills.

### Option 1 — OpenCode, one-liner (auto-discovery, recommended)

Clone straight into OpenCode's global skills folder — it discovers nested `SKILL.md` files automatically, no config changes:

```powershell
git clone https://github.com/Youssef-Devolopment/BuildAnything-skill.git "$env:USERPROFILE\.config\opencode\skills\buildanything"
```

macOS/Linux: `git clone https://github.com/Youssef-Devolopment/BuildAnything-skill.git ~/.config/opencode/skills/buildanything`

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
| Clone (Option 1/2) | `git pull` in the clone folder |
| Copy (Option 3/4) | Re-run `install.ps1 -Target … -Force` |

### Using the skills

OpenCode discovers them automatically — load one with `@<skill-id>` (e.g. `@build-anything`) or let the model load it via the `skill` tool. Claude Code picks up `-Target claude` installs the same way.

## Layout

```
C:\Buildanything skill\
├── build-anything/
│   ├── SKILL.md
│   ├── references/stacks.md
│   └── templates/          # TEMPLATE.md + PLAN/TODO/STATUS/README/ARCHITECTURE/STRUCTURE/CHANGELOG/CHECKLIST skeletons, .env.example, .gitignore, CI workflow
├── idea-refiner/SKILL.md
├── micro-planner/SKILL.md
├── idea-to-product/SKILL.md
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
├── project-skill-creator/SKILL.md
├── install.ps1
└── README.md
```

## Versioning

Releases are tagged (`v1.0`, `v1.1`, …). The commit history is the changelog.
