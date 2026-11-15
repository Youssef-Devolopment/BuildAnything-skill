---
name: Open Source Showcase
description: Use when an open-source project needs to attract stars — SVG logo, a 30-second README (badges, screenshot, quickstart), and a one-page GitHub Pages website.
---

# Open Source Showcase

People decide in ~30 seconds whether a repo is worth their time. This skill makes those 30 seconds count: **README + logo + project website**, all generated as files in the repo, all deployable with zero extra infrastructure.

Load after `open-or-private` has confirmed **open source** (license + hygiene done first — a beautiful README on a leaked-secret repo is a disaster).

## 1. Logo (`assets/logo.svg`)

Simple, scalable, and free — **SVG only** (text in the repo, renders on GitHub, works at any size):

- **One mark**: a shape or letterform that says what the project *is* (a booking app → calendar/check; a CLI → terminal prompt; else an abstract mark from the project's initial).
- **One color** (the project's primary, or a single confident hue) + transparent background; optional dark/light variants if it sits on both.
- **Wordmark**: project name in a clean sans (system font stack or the typeface already chosen in `design-ui`), letter-spaced, legible at 32px.
- Write it by hand as compact SVG — no raster images, no AI-generated PNG blobs, no clip-art. If unsure, a bold monogram in a rounded square is a solid default.
- Also produce `assets/logo-mark.svg` (icon only) for the favicon/social card.

## 2. README.md — the 30-second pitch

Structure (top to bottom, cut ruthlessly — aim ≤1 screen before the fold):

```markdown
<p align="center"><img src="assets/logo.svg" width="360" alt="Project"></p>
<p align="center">One-line tagline — what it does, for whom, in ≤12 words.</p>
<p align="center">
  <img src="https://img.shields.io/..."> (CI, license, version, downloads/stars if real)
</p>

<!-- If it's a UI project: one hero screenshot/GIF, center, bordered, real data. -->

## Why            # the problem in 2–3 lines; what makes this different (honest, no hype)
## Quick start    # copy-paste: install → run → first result, ≤3 commands, tested
## Features       # bullet list tied to real, shipped behavior only
## How it works   # 1 diagram or short paragraph; link to docs/ARCHITECTURE
## Documentation  # links: full docs, examples, API
## Contributing   # one paragraph + link to CONTRIBUTING.md
## License        # badge + one line + link to LICENSE
```

Rules:
- **Every command tested** from a fresh clone before it's written down.
- No lorem ipsum, no planned features, no badges for things that don't exist (red CI badge is worse than none).
- Screenshots/GIF: real content, real UI, current state of the app.
- Badges only from services actually used (CI, license, release) — max ~4.
- Plain language in the tagline and Why — a non-developer should get it (see `idea-to-product`).

## 3. Project website (`docs/` → GitHub Pages)

One static page that presents the repo — no backend, no build step required (plain HTML + CSS, or the project's own stack if it already exists):

- **Sections**: hero (logo + tagline + Install/View-on-GitHub buttons), why/features, a screenshot or live demo link, quick start, docs links, license/contributing footer.
- Load the `website` skill for the quality bar: mobile-first, WCAG AA contrast, fast (single page, self-hosted font or system stack), real content, OG meta tags + `og:image` (compose logo + name).
- **Deploy**: GitHub Pages from `/docs` (or the platform the project already uses) — record the URL in README badge + `STATUS.md`.
- The site must not drift from the repo: its content comes from README sections, and the stage-gate doc rule applies — update both in the same change.

## Handoff

- Files added: `assets/logo.svg`, `assets/logo-mark.svg`, rewritten `README.md`, `docs/index.html` (+ assets).
- Record the Pages URL in README and `STATUS.md`; mention the site in the project skill (`project-skill-creator`).
- Final check: fresh-clone → README quickstart works; logo renders on GitHub; Pages URL loads on mobile.

## Rules

- Showcase the truth: if the project is small, a clean small README beats inflated marketing copy.
- Never block shipping on design bikeshedding — logo has a 30-minute budget, then ship.
- The README is the product's front door and the AI's context source: it must stay accurate as the project evolves (same-change doc rule).
