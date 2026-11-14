---
name: Deployment
description: Ship and operate the project — CI/CD, environments, hosting, domains, releases, and rollback. Load when deploying, setting up pipelines, choosing hosting, going live, or after the last stage gate when the project must reach users. Works with build-anything's GitHub-native rules.
---

# Deployment

Load `build-anything` first. Deployment is planned in `PLAN.md` (stack §4, steps §6) — this skill executes it properly. A project that only runs on your machine is not done.

## Day one (not day last)

- **CI**: GitHub Actions — lint → typecheck → tests on every push/PR. Green badge before the first feature merges.
- **Environments**: `dev` (your machine/preview) and `production`. One staging/preview URL if the platform supports it — the user reviews *there*, not on your laptop.
- **Config**: all secrets via environment variables; `.env.example` committed; production values never in the repo.
- **Reproducibility**: fresh `clone → install → build → test` works (GitHub-native rule) — CI proves it every push.

## Going live checklist

1. **Build verified** — production build succeeds locally and in CI; no dev-only code paths leak.
2. **Secrets set** — every required env var exists in the platform; app starts with them (fail fast if missing).
3. **Database** — migrations run as a deploy step (never manual on prod); backups enabled *before* first real data.
4. **DNS/SSL** — domain, HTTPS, redirects (www ↔ apex decided and documented).
5. **Smoke test on prod** — the main `PLAN.md` flows actually work against the real URL.
6. **Observability** — error tracking (Sentry or platform logs) receiving events; health endpoint monitored.
7. **Rollback known** — one command or one click back to the previous version; tested once.
8. **`STATUS.md` updated** — deployed, where, how to deploy next time.

## Release discipline

- Deploy small and often — every stage gate can ship; big-bang releases hide problems.
- Trunk-based or short-lived branches; the commit history stays the story.
- Migrations: backward-compatible (expand → migrate → contract) so old code survives a rollback.
- Tag releases (`v1.0`, `v1.1`); the tag is what production runs.

## Hosting defaults (justify deviations in `PLAN.md`)

| Project | Default |
|---|---|
| Web app / site | Vercel or Cloudflare Pages (frontend) + platform-managed Postgres |
| API / service | Fly.io / Railway / Render with Docker; AWS/GCP only when requirements demand |
| Static site | Cloudflare Pages (free, fast) |
| Mobile backend | Same as API; EAS for app builds |

## Rules

- No deploy requires a person doing manual steps not written in the README — automate or document it.
- Never deploy with a red test suite.
- If the user is non-technical (see `idea-to-product`): deploy for them, give them a URL, and write the "how to update it" section in plain words.
