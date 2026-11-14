# BuildAnything

The universal build skill set — one system that makes **any AI, with any model, build anything** the right way: interviewed first, planned in `PLAN.md`, built stage by stage with clean least-code, tested, reviewed, and documented so the next agent (human or AI) picks it up cold.

## Skills

| Skill | ID | What it does |
|---|---|---|
| **BuildAnything** | `build-anything` | The orchestrator: discovery interview → `PLAN.md` → stage gates (clean least-code, test, fix/report errors, user review) → GitHub-native docs. Includes reasoning discipline for any model size and the "least code wins" rule. |
| **Design UI** | `design-ui` | Design systems, layout, typography, color, every-state design, WCAG AA accessibility. |
| **Frontend** | `frontend` | Components, state hierarchy, data fetching, performance, a11y, testing. |
| **Backend** | `backend` | API design, schema-first data, deny-by-default security, observability, integration tests. |
| **Website** | `website` | Landing/marketing/static sites: content first, SEO, Core Web Vitals, Lighthouse ≥95. |
| **Mobile App** | `mobile-app` | Expo/React Native: safe areas, permissions, offline states, store submission. |
| **Project Skill Creator** | `project-skill-creator` | Builds the project's own in-repo SKILL.md (day one skeleton + ~50% full capture). |

Reference: [`build-anything/references/stacks.md`](build-anything/references/stacks.md) — opinionated best-stack defaults for web, API, CLI, mobile, ML, and DevOps.

## Install

**Windows (PowerShell):**

```powershell
.\install.ps1
```

**Manual / any OS:**

```bash
git clone <this-repo-url> ~/.config/opencode/skills
# Windows: copy the folders into C:\Users\<you>\.config\opencode\skills\
```

OpenCode discovers these automatically; load one with `@<skill-id>` or let the model load it via the `skill` tool. Compatible with Claude Code (`.claude/skills`) and other agents (`.agents/skills`) — `install.ps1` can target those too.

## Layout

```
skills/
├── build-anything/
│   ├── SKILL.md
│   └── references/stacks.md
├── design-ui/SKILL.md
├── frontend/SKILL.md
├── backend/SKILL.md
├── website/SKILL.md
├── mobile-app/SKILL.md
├── project-skill-creator/SKILL.md
├── install.ps1
└── README.md
```

## Versioning

Releases are tagged (`v1.0`, `v1.1`, …). The commit history is the changelog.
