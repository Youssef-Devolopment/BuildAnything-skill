# Structure

> A plain-language tour of this repo for a human who has never seen it.
> One read = you know where things are and where to make which change.
> **Keep current** — update in the same change that moves/creates files.

## The tree

```text
{{project}}/
├── PLAN.md            # What we're building and why (the contract)
├── STATUS.md          # What's done / in progress / next — read this first
├── README.md          # How to install, run, test, deploy
├── ARCHITECTURE.md    # System shape and design decisions
├── CHANGELOG.md       # Timeline: what changed, stage by stage
├── CHECKLIST.md       # Pre-flight check: env, deps, secrets — run before each stage
├── src/               # {{one line: what lives here}}
│   ├── {{module}}/    # {{what it does, entry point file}}
│   └── …
├── tests/             # {{mirrors src / colocated — say which}}
├── scripts/           # {{dev/build/deploy helpers}}
├── public/            # {{static assets, if any}}
└── .github/workflows/ # CI: lint + tests on every push
```

## Where do I change…?

| I want to… | Go to |
|---|---|
| Change {{main behavior}} | `{{path}}` |
| Change {{the UI / endpoint}} | `{{path}}` |
| Change {{data shape}} | `{{path}}` + migration `{{path}}` |
| Add a {{new screen / route}} | `{{pattern to follow}}` |
| Ship / verify a stage | `CHECKLIST.md` (pre-flight) → gate review |
| Run it / test it | README → Quick start |

## Entry points

- **App starts:** `{{file/command}}`
- **Tests start:** `{{command}}`
- **CI:** `.github/workflows/ci.yml`
