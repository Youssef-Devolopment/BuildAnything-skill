# OpenCode Skills

My global OpenCode skill set — a senior-engineer workflow plus specialized sub-skills, so any AI (any model, small or large) produces real, well-planned, well-tested projects.

## Skills

| Skill | ID | What it does |
|---|---|---|
| **Senior Engineering** | `senior-engineering` | The orchestrator: discovery interview → `PLAN.md` → stage gates (clean least-code, test, fix/report errors, user review) → GitHub-native docs. Includes reasoning discipline for any model size and the "least code wins" rule. |
| **Design UI** | `design-ui` | Design systems, layout, typography, color, every-state design, WCAG AA accessibility. |
| **Frontend** | `frontend` | Components, state hierarchy, data fetching, performance, a11y, testing. |
| **Backend** | `backend` | API design, schema-first data, deny-by-default security, observability, integration tests. |
| **Website** | `website` | Landing/marketing/static sites: content first, SEO, Core Web Vitals, Lighthouse ≥95. |
| **Mobile App** | `mobile-app` | Expo/React Native: safe areas, permissions, offline states, store submission. |
| **Project Skill Creator** | `project-skill-creator` | Builds the project's own in-repo SKILL.md (day one skeleton + ~50% full capture). |

Reference: [`senior-engineering/references/stacks.md`](senior-engineering/references/stacks.md) — opinionated best-stack defaults for web, API, CLI, mobile, ML, and DevOps.

## Install

```bash
# Clone into the OpenCode global config
git clone <this-repo-url> ~/.config/opencode/skills
```

Or copy the folders into `~/.config/opencode/skills/` (Windows: `C:\Users\<you>\.config\opencode\skills\`).

OpenCode discovers these automatically; load one with `@<skill-id>` or let the model load it via the `skill` tool.

## Layout

```
skills/
├── senior-engineering/
│   ├── SKILL.md
│   └── references/stacks.md
├── design-ui/SKILL.md
├── frontend/SKILL.md
├── backend/SKILL.md
├── website/SKILL.md
├── mobile-app/SKILL.md
└── project-skill-creator/SKILL.md
```
