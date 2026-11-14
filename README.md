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

This repo lives at **`C:\Buildanything skill`** and is registered as a skills source in `~/.config/opencode/opencode.json` (`"skills": ["C:\\Buildanything skill"]`), so OpenCode loads it from there.

**Windows (PowerShell):**

```powershell
.\install.ps1
```

**Manual / any OS:**

```bash
git clone <this-repo-url> "C:\Buildanything skill"   # or any folder
# then add that folder path to the "skills" array in opencode.json
```

OpenCode discovers these automatically; load one with `@<skill-id>` or let the model load it via the `skill` tool. Compatible with Claude Code (`.claude/skills`) and other agents (`.agents/skills`) — `install.ps1` can target those too.

## Layout

```
C:\Buildanything skill\
├── build-anything/
│   ├── SKILL.md
│   ├── references/stacks.md
│   └── templates/          # TEMPLATE.md + PLAN/STATUS/README/ARCHITECTURE/STRUCTURE/CHANGELOG skeletons, .env.example, .gitignore, CI workflow
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
