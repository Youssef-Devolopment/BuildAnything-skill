---
name: Frontend
description: Build production-quality frontend code — components, state, routing, data fetching, performance, accessibility, and testing. Load when implementing any client-side code in a web/app project. Follows senior-engineering's stage gates and the design-ui skill's decisions.
---

# Frontend

Load `senior-engineering` first (discovery, plan, stage gates). Load `design-ui` when there are design decisions to make. This skill covers implementing them.

## Principles

- **Least code**: no state libraries for state the DOM already holds; no abstraction until the third duplication; no "configurable" props nobody configures.
- **Follow the design system**: consume tokens/components — don't hand-roll styles that drift from `design-ui` decisions.
- **Real data shapes**: components receive typed/validated props; render loading, empty, and error states for every data view.

## Architecture

- **Component structure** — colocate component + styles + tests; one concern per component; props over context; composition over prop-drilling and over god-components.
- **State** — local state first → URL state (shareable/filterable) → server state (via the framework's data layer, with cache/invalidations) → global client state last. Never duplicate server state in client stores.
- **Data fetching** — single layer for API calls (typed client), handle loading/error/retry, cancel stale requests, no fetch calls buried in components when a data layer exists.
- **Routing** — URL is the source of truth for navigation/filters; deep links work; 404 handled.

## Quality bar

- **Accessibility**: semantic HTML first, ARIA only when needed, keyboard paths for every interaction, focus management on route change/modals, tested with keyboard-only navigation.
- **Performance**: no unnecessary re-renders; memoize only with evidence; images sized/lazy/`srcset`; code-split routes; no bundle additions without justification; measure before optimizing.
- **Robustness**: every async flow handles failure (retry, message, recovery); forms validate inline with server errors surfaced; no unhandled promise rejections.
- **DX consistency**: ESLint + Prettier configured day one; TypeScript strict if the stack has TS.

## Testing

- Component tests for behavior (what the user does), not implementation details.
- One test per state: loading, empty, error, success.
- E2E (Playwright/Cypress) for the main flows defined in `PLAN.md` — run before every stage gate.
- Avoid snapshot tests as a substitute for assertions.

## Rules

- Never ship: console noise, commented-out code, `TODO` walls, disabled-but-visible features, placeholder screens.
- Verify in the browser at multiple viewports before calling a stage done.
- If a design decision is missing, load `design-ui` or ask — don't improvise UI in code.
