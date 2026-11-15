---
name: Clone Website
description: Use when cloning a specific website from a URL — 4-breakpoint capture, section/copy/asset inventory, rebuild top-to-bottom with original content, side-by-side verify, Lighthouse >=95 intact.
---

# Clone Website

Rebuilding a specific site with a URL in hand. Load `clone-anything` for the contract (legal line, v1 cut, beat-the-original bar) and `build-anything` for the pipeline — this skill is the website-specific method.

## Capture (before any plan)

1. **Open the real page in a browser** — never clone from memory. Screenshot every section top to bottom at 320 / 768 / 1024 / 1440px, including: nav (closed *and* open/mobile states), hero, each content section, forms (default + validation states), footer.
2. **Inventory what you saw** — goes into `PLAN.md`:
   - **Sections** in order, with each one's job (hero → proof → features → pricing → CTA → footer).
   - **Copy** — headline/subhead/CTA text: capture the *intent*, then write original words (or flag placeholders for the user's real copy). Never paste the original's text wholesale.
   - **Assets** — logos / photos / illustrations / icons / fonts: classify each as **replace** (find or make an original), **redraw** (SVG you author), or **drop**.
   - **Interactive bits** — menu behavior, carousels, forms, animations: record each animation as a `design-ui` tier choice.
3. **Note the reference's behavior** — is it an SPA, static, server-rendered? Learn from how it *behaves*, but choose the stack from `website`'s defaults (Astro or Next.js + Tailwind) and justify it in `PLAN.md`.

## Build order (one stage per section, top to bottom)

1. **Skeleton stage** — layout, design tokens (colors/type/spacing *sampled* from the reference — patterns are fine, exact brand assets are not), responsive shell.
2. **Section stages** — one section per stage: real content, all states, mobile-first.
3. **Interactive stages** — nav/mobile menu → forms → effects/animation (tier per `design-ui`, budget per `website`'s effects budget).
4. **SEO & performance pass** — meta, sitemap, robots, images: the `website` quality bar applies unchanged, including Lighthouse ≥95 with your effects in place.

## Verify at every gate (side by side)

- Reference and clone open next to each other in a real browser at all four breakpoints — same sections in the same order, comparable hierarchy and density.
- Walk every link and flow in the clone: no dead ends, no broken anchors, forms validate and show success *and* error states.
- Run the Lighthouse/performance check — if an effect pushed it below the bar, shrink or cut the effect (`website`).

## Rules

- Original branding, copy, and assets only — `clone-anything`'s contract; list anything still placeholder for the user.
- If the reference shows facts you can't know (real prices, testimonials, team names), use clearly-marked placeholders and list them — never invent "real-looking" facts.
- The original's clutter is not sacred: cut what's redundant, keep what converts, and note the change in one line at review.
