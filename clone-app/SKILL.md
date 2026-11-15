---
name: Clone App
description: Use when cloning an existing app (mobile, desktop, or web) — record flows, map screens and navigation, reverse-engineer the data model, core loop first, same-flow side-by-side walks.
---

# Clone App

Rebuilding an app the user points at. Load `clone-anything` for the contract (legal line, v1 core-loop cut, beat-the-original bar) and `build-anything` for the pipeline — this skill is the app-specific method.

## Capture (before any plan)

1. **Get the original running in front of you** — install it, or take screen recordings/screenshots from the user. Never clone from a vague memory of the app.
2. **Walk and record the core loop** — do the one thing the app exists for, start to finish, noting every screen, tap, and state transition (a recording beats prose for the handoff).
3. **Inventory** — goes into `PLAN.md`:
   - **Flow map** — screens + navigation edges: which screen leads where, back behavior, modals vs pushes, tab structure.
   - **Feature inventory** — every observed feature tagged `v1` / `later` / `skip`.
   - **States per screen** — default, loading, empty, error, success: the original's states are requirements (missing ones are improvements to add — say so).
   - **Platform conventions** — iOS/Android/web patterns in play (tab bar? FAB? swipe actions? keyboard shortcuts?): clone the *conventions*, not the skin.
4. **Reverse-engineer the data model** — list the entities the app implies (users, items, lists, settings…) and their relationships; hand this to the `database` skill. Choose storage honestly: local-first (localStorage/SQLite/Expo SQLite) for v1 unless the core loop *requires* multi-user or sync — say why in `PLAN.md`.

## Build order (one stage per flow slice)

1. **Skeleton stage** — project + navigation shell per `mobile-app` (Expo/React Native) or `frontend` (web/desktop): the flow map as real routes/screens, even with placeholder content.
2. **Data layer stage** — schema + storage (`database` skill), read/write of the core entity, with tests.
3. **Core loop stages** — one flow per stage: the screen, its five states, and the data behind it.
4. **Polish stages** — settings/account, then `design-ui` motion tiers, then platform niceties the original has (haptics, shortcuts, swipe gestures).

## Verify at every gate (side by side)

- Run your clone next to the original (or its recording) and walk the **same flow in both**: same steps reachable? same feedback at each step? same error/empty states shown?
- Record mismatches as `TODO.md` fixes *before* the gate closes.
- Test on a real device/emulator at real viewport sizes — not just the ideal simulator case.

## Rules

- Original branding, copy, and assets only — `clone-anything`'s contract.
- Don't stub what v1 can't support honestly (multiplayer, payments, push): tag it `later` and say so — a stub that pretends to work is AI slop.
- Permissions, offline behavior, and destructive actions (delete, logout) get real confirmation states — the original's sloppiness is not an excuse.
- Same bars as any project: least code, tests for the core loop, stage gates, errors fixed or reported first.
