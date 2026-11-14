# Scaffold Templates

Copy-from templates for day-one project scaffolding. Use these instead of inventing file structures — they eliminate hallucinated boilerplate and make setup consistent and zero-config across every project.

## How to use

1. Copy the needed template from this directory into the project root (or `.github/workflows/` for the CI file).
2. **Rename** `gitignore` → `.gitignore` and `env.example` → `.env.example` (dots omitted here so template tooling never confuses them with real config).
3. Replace every `<!-- … -->` placeholder and `{{…}}` token with project-specific content. Delete any section that doesn't apply — an empty section is worse than a missing one.
4. Never copy a template and ship it unfilled: `readiness-judge` treats placeholder text in these files as a blocker.

## Which template, when

| Template | Create when | Target path |
|---|---|---|
| `PLAN.md` | After discovery (Phase B), **before any code** — always | `/PLAN.md` |
| `TODO.md` | After plan approval (Phase D), **before any application code** — always | `/TODO.md` |
| `STATUS.md` | Day one; update at every stage gate — always | `/STATUS.md` |
| `README.md` | Day one (skeleton), completed before first release — always | `/README.md` |
| `ARCHITECTURE.md` | Day one if the stack/architecture is decided; filled as components appear | `/ARCHITECTURE.md` |
| `STRUCTURE.md` | Day one (tree with placeholders), real content by first review | `/STRUCTURE.md` |
| `CHANGELOG.md` | Day one; appended at every stage gate | `/CHANGELOG.md` |
| `CHECKLIST.md` | Day one; run before every stage's code output and every deploy | `/CHECKLIST.md` |
| `env.example` | Whenever the project reads environment variables | `/.env.example` |
| `gitignore` | Day one — pick the closest profile and trim it | `/.gitignore` |
| `ci.yml` | Day one, GitHub-native rule: lint + tests on every push | `/.github/workflows/ci.yml` |

## Gitignore profiles

`gitignore` ships as one file with **three clearly-marked profiles** — `# ── node ──`, `# ── python ──`, `# ── general ──` (always keep). Delete the blocks for languages the project doesn't use; keep `general` intact (it covers `.env`, OS junk, editor files, build artifacts).

## CI file notes

`ci.yml` assumes Node — for other stacks, swap the run steps for the equivalent (`ruff check && pytest`, `go test ./...`, …) but keep the structure: trigger on push/PR, checkout, setup, install from lockfile, lint, test. The badge goes in README when the workflow is green.
