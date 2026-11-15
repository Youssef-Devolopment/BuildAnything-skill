---
name: Clone Anything
description: Use when the user says clone, rebuild, or copy an existing product (site, app, game, tool) — reference capture, feature inventory, v1 core loop only, original branding and assets, side-by-side verification.
---

# Clone Anything

The user points at an existing product ("clone Netflix", "make a copy of Notion", "rebuild this URL") and you build a working equivalent. Load `build-anything` first — the pipeline (discovery → `PLAN.md` → `TODO.md` → stage gates) is unchanged; this skill defines *what a clone is* and how one enters that pipeline.

## Specialized methods (load on demand)

| Product type | Read |
|---|---|
| Websites, landing pages, URLs | `references/clone-website.md` (4-breakpoint capture, section-by-section build, Lighthouse ≥95) |
| Mobile, desktop, or web apps | `references/clone-app.md` (flow recording, data model reverse-engineering, same-flow walks) |
| Games, CLI tools, other | Follow this skill's contract, load matching layer skill (`frontend`, `backend`, `mobile-app`) |

## The clone contract

- **Clone behavior and structure, never identity.** Functionality, flows, layout patterns, and interaction ideas are fair game. Logos, trademarks, brand names, copyrighted assets, and copied text are not: use original branding and write your own copy (flag placeholders until the user supplies real content). State this constraint in `PLAN.md` — one line.
- **v1 = the core loop only.** A clone that attempts every feature of the original dies mid-build. Inventory everything first, then cut to the one flow that makes the product make sense (e.g. video site: watch + upload — not live, podcasts, and subscriptions).
- **The bar to beat is the original.** The clone must feel as finished as the reference within its v1 scope — and where the original is objectively worse (slow, cluttered, inaccessible, hidden features), improve it and say so in one line (principle #7 of `build-anything`).

## Process

1. **Capture the reference** — get from the user: URL(s), screenshots, screen recordings, or a written walkthrough. If a URL exists, open it in a browser and capture the *real* thing (breakpoints, flows, states). Never clone from a vague memory of the product, and never guess at screens you haven't seen.
2. **Inventory** — produce two lists, which go into `PLAN.md`:
   - **Feature inventory**: every feature/flow observed, each tagged `v1` / `later` / `skip`.
   - **Screen/flow map**: every screen/section and how navigation moves between them.
3. **Dispatch** — read the matching method:
   - Websites / marketing pages → `references/clone-website.md`
   - Mobile / desktop / web apps → `references/clone-app.md`
   - Games, CLI tools, and everything else → keep this contract and load the matching layer skill (`frontend`, `backend`, `mobile-app`).
4. **Plan against the inventory** — `PLAN.md` §6 stages each own one screen/flow (or one layer of it). The inventory *is* the requirements section; the `later`/`skip` tags *are* §3 out-of-scope.
5. **Build under stage gates** — one flow per stage: tested, demoed, reviewed — unchanged `build-anything` gates.
6. **Verify side-by-side at every gate** — run your clone next to the reference and walk the same flow in both: same steps reachable? same information visible? same states (loading/empty/error/success) present? Record differences as fixes, not surprises.
7. **Beat it where you can** — one line per improvement at review ("the original hides X behind two menus; mine surfaces it").

## Quality bar

- The core loop works end to end with no dead ends — and without the reference visible, a first-time user still understands what to do.
- Every `v1` item in the inventory exists; nothing outside it was built (scope discipline).
- Original branding, original copy, original assets — zero trademark/copyright landmines (check: logo, brand name, shipped screenshots, text).
- States match or beat the reference: loading, empty, error, success all designed (`design-ui`).
- Stack chosen from `references/stacks.md` / the relevant layer skill, justified in `PLAN.md`.

## Rules

- Never scrape or hotlink the reference's assets; never paste its text into the build.
- If the user asks to clone something whose primary value *is* copyrighted content (a movie site, a book text), clone the shell and say plainly what needs their own content or license.
- A clone is not an excuse for lower quality — same least code, same tests, same gates, same docs as any `build-anything` project.
