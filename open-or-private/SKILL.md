---
name: Open Or Private
description: Ask the user whether the finished project will be open-sourced or kept private, then structure the repository accordingly — license, community files, and public-ready hygiene for open source; or a self-contained, easy-to-run structure with one-command setup for personal use. Load after readiness-judge says READY, before the final push.
---

# Open Or Private

The project is ready — now decide **what kind of repository it becomes**. This skill asks the user (never decides for them), then structures everything for that choice.

## Step 1 — Ask (with a real explanation)

Use the `question` tool or a short numbered list. For a non-developer (see `idea-to-product`), explain in one line each:

- **Open source (public on GitHub)** — anyone can see, use, learn from, and contribute. Great for portfolio/credibility, feedback, and community help. Code is permanently public; pick a license that controls how others may use it.
- **Private (all yours)** — only you (and who you invite) can see it. Right for business code, personal data, client work, or anything you may sell.

Present the trade-off, recommend one based on the project (a portfolio/demo/tool → often open; contains secrets, business logic, user data, paid IP → private), and **wait for the answer**. Record the choice in `STATUS.md`.

## Step 2A — Open source: make it a proper public repo

- **License** — recommend explicitly: MIT/Apache-2.0 (permissive, max adoption), GPL/AGPL (derivatives must share), or "no license = all rights reserved" if they want source-visible-but-not-reusable. The user picks; you write `LICENSE` and state the choice in README.
- **Community files**: `README.md` (what/why, screenshot/GIF if UI, install, usage, badges), `CONTRIBUTING.md` (how to propose changes, run tests), `SECURITY.md` (how to report vulnerabilities — a private contact, not a public issue), `CODE_OF_CONDUCT.md` for larger projects.
- **Public hygiene pass**: scrub *all* secrets, personal emails, tokens, internal URLs, and real user data from code, history, and docs; `.env.example` stays, `.env` stays ignored; realistic seed data only.
- **Discoverability**: repo description, topics/tags, clear LICENSE badge, version tags (`v1.0`), a `CHANGELOG.md` entry for the first release.
- **CI public**: GitHub Actions badge (lint+tests) so strangers see it's alive and green.
- **Issue/PR templates** (small ones) so early contributors don't ask chaos questions.
- Push as a **public** repo; verify the clone-from-clean-machine path in README actually works.

## Step 2B — Private: make it easy for *the user* to run and own

- **One-command start**: `install.ps1` or `setup` script (deps + env + migrate) and `run` script/`dev` command — the user never needs to know the internals to start it.
- **README for the owner**: what it is, how to run it *on their machine*, how to deploy it, where the data lives, how to back it up — plain language (they may be the non-developer from `idea-to-product`).
- **Self-contained**: no dependence on your session, your paths, or your machine; fresh clone → run works (GitHub-native rule still applies — it's in a git repo either way, just not public).
- **Structure for them, not for strangers**: `docs/` can stay internal; skip CONTRIBUTING/CoC; keep `STRUCTURE.md`/`STATUS.md` so any future developer or AI they hire can take over.
- **Safety**: `.gitignore` airtight, secrets via env only, private remote (or local-only repo if they don't want a remote at all — say how to add one later).
- Push as a **private** repo (or document `git init` + backup options if no remote wanted).

## Step 3 — Confirm

- Show the result: files added/changed, visibility choice, the exact URL or command to reach the repo.
- Update `STATUS.md` (visibility, license, repo URL) and the project skill (`project-skill-creator`).
- Final line to the user: what they now have and the one command to start using/sharing it.

## Rules

- Never make this choice for the user, and never push public before an explicit "yes, open".
- Open source without a license = pointless; private with leaked secrets = disaster — both are checked before any push.
- The readiness verdict (`readiness-judge` = READY) comes first; don't structure a broken project for release.
