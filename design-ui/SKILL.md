---
name: Design UI
description: Use when designing any UI or choosing a visual direction — design system, every-state screens, accessibility, motion tiers; records decisions for frontend to implement.
---

# Design UI

Design is decisions, not decoration. Follow the `build-anything` skill's discovery phase first: ask the user about brand, references, audience, and taste **before** designing.

## Process

1. **Gather inputs** — brand colors/fonts, reference products the user likes, audience, platform (web/mobile/desktop), density preference. If the user has no reference, propose 2–3 concrete directions (not vague adjectives) and let them pick.
2. **Define the system first** — before individual screens: color scales, type scale, spacing scale (4/8px grid), radius, elevation/shadow, motion. Write it down (a short `DESIGN.md` or a section in `PLAN.md`).
3. **Design every state per view** — default, hover, focus, active, disabled, loading, empty, error, success. A screen designed only in its happy path is not designed.
4. **Layout** — one primary action per view; clear visual hierarchy (3 levels max per screen); consistent alignment; generous whitespace over borders/dividers.
5. **Accessibility (non-negotiable)** — WCAG AA contrast (4.5:1 body text), visible focus states, keyboard operability, semantic landmarks/labels, `prefers-reduced-motion` respected, alt text.
6. **Responsive** — mobile-first breakpoints; no horizontal scroll at 320px; touch targets ≥44px.
7. **Handoff** — frontend gets: component inventory, states, spacing/type tokens, and asset requirements.

## Quality bar (what "not AI slop" looks like)

- Real content in designs — actual words, real-looking data, no lorem ipsum, no "Title Here".
- Consistent tokens everywhere — no one-off hex colors, no random pixel values.
- Deliberate typography: 1 typeface (or a justified pairing), a real type scale, sensible line-height (1.5 body) and measure (45–75 chars).
- Color used with intent: 1 primary brand color + neutrals + semantic (success/warning/danger); never rainbow.
- Density fits the product: dashboards dense, marketing pages airy.
- Micro-details: skeleton loaders (not spinners for lists), optimistic where sensible, toasts for confirmations, empty states that teach the user what to do next.
- Motion: 150–250ms, ease-out, only where it aids comprehension.

## Motion & polish discretion (decide yourself, don't wait to be asked)

Judge whether animation/3D would make *this* work better and act on it — then state it in one line at review ("added X because Y" / "skipped X because Y"). Pick the highest tier the work genuinely benefits from:

| Tier | What | When it fits |
|---|---|---|
| **1 — Micro** | hover/focus/press transitions, 150–250ms ease-out, skeleton loaders, animated state changes | almost always — this is the baseline |
| **2 — Choreographed** | scroll-reveal, entrance animations, animated empty states, subtle page transitions | marketing, portfolio, landing, product pages — anywhere motion guides attention |
| **3 — Showpiece** | hero 3D (Three.js/Spline), canvas/WebGL scenes, interactive object viewers | only when it shows the real product/subject and the budget allows |

**Skip (or drop a tier) when:** the work is a doc site, dashboard, or data-dense tool (clarity beats spectacle); the user asked for plain/functional/minimal; motion would delay content; or the stack has no budget for it.

Hard guardrails (they beat any tier choice):
- `prefers-reduced-motion` respected at every tier — tier 2/3 must degrade to tier 1 behavior.
- Least code first: CSS transitions before JS animation libraries; never add a 3D framework for a hover state. Tier 3 requires a one-line justification (what it shows, why it beats a static hero).
- Content must be readable and usable before effects load; effects never block input or hide information.
- Performance budget wins over decoration — `website` keeps Lighthouse ≥95; if an effect breaks it, shrink or cut the effect.
- Record the tier choice and any rejected effect in the design notes so the next AI doesn't redesign from scratch.

## Stack

Prefer the project's existing design stack. If none: Tailwind CSS + a headless component library (Radix/shadcn-style) + Lucide icons; fonts from a stable source (system font stack or Google Fonts self-hosted). For mockups before code, ASCII/wireframe or HTML prototypes are fine — record the choice in `PLAN.md`.

## Rules

- Never invent a new visual language when the project already has one — extend it.
- Record every design decision and rejected direction so the next AI doesn't redesign from scratch.
- Test at real viewport sizes and real content lengths, not just the ideal case.
