---
name: Design UI
description: Design and build real, polished user interfaces — layout, typography, color, spacing, states, accessibility, and design systems. Load when designing any UI, choosing a visual direction, building screens or components, or reviewing UI quality. Works alongside build-anything; produces decisions recorded for frontend to implement.
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

## Stack

Prefer the project's existing design stack. If none: Tailwind CSS + a headless component library (Radix/shadcn-style) + Lucide icons; fonts from a stable source (system font stack or Google Fonts self-hosted). For mockups before code, ASCII/wireframe or HTML prototypes are fine — record the choice in `PLAN.md`.

## Rules

- Never invent a new visual language when the project already has one — extend it.
- Record every design decision and rejected direction so the next AI doesn't redesign from scratch.
- Test at real viewport sizes and real content lengths, not just the ideal case.
