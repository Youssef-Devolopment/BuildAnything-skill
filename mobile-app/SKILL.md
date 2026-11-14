---
name: Mobile App
description: Build production mobile apps with React Native/Expo — navigation, platform conventions, offline/error states, permissions, testing, and store submission. Load when the project is a mobile app or work involves native device features, app stores, or mobile-specific UX. Follows build-anything's stage gates and design-ui's visual decisions.
---

# Mobile App

Load `build-anything` first (discovery, plan, stage gates) and `design-ui` for visuals. This skill covers the mobile-specific layer.

## Stack (defaults — record in `PLAN.md`)

- **Expo (React Native) + TypeScript (strict)** — EAS builds, over-the-air updates, one codebase for iOS/Android.
- **expo-router** for file-based navigation.
- State: local → URL/route params → server data (React Query/TanStack) → global store last. Same hierarchy as frontend.
- Forms: react-hook-form + Zod (shared validation with the API).
- Testing: Jest + Testing Library; **Maestro** for E2E flows.

## Process

1. **Platform conventions in discovery** — target iOS/Android/both; minimum OS versions; whether it needs native features (camera, push, maps, biometrics) — these drive scope.
2. **Navigation skeleton first** — the screen/route tree wired up and clickable before filling in screens (matches `PLAN.md` §7).
3. **Screen by screen behind stage gates** — each screen ships with its loading, empty, and error states.
4. **Device testing before each gate** — simulator alone is not verification.

## Quality bar

- **Layout**: safe-area insets respected (notch/home-indicator), keyboard never covers inputs (`KeyboardAvoidingView`), scroll-to-dismiss on long forms, dark mode handled if claimed.
- **Lists**: `FlatList` with keys, pagination, pull-to-refresh; no 60-frame jank on long lists.
- **States**: every async screen has loading (skeleton where sensible), empty (with next action), and error (with retry) states; app works offline for cached data or explains why it can't.
- **Permissions**: ask in context with a rationale *before* the system prompt; handle denial gracefully (feature degrades, no crash loop).
- **Feedback**: toasts/snackbars for success, inline errors for failures, optimistic updates only where rollback is safe.
- **Performance**: startup <2s to interactive, no unnecessary re-renders, images cached and sized, bundle split by route if large.

## Testing & release

- Unit tests for logic/hooks; one test per screen state; Maestro E2E for the core flows in `PLAN.md`.
- Test on a real device (or device cloud) at least once per stage — simulators hide permission, keyboard, and safe-area bugs.
- **Store checklist**: app icon + adaptive icon, all required screenshot sizes, accurate privacy policy URL, permission usage descriptions, category, version/build numbers in `app.json`/`app.config.ts`.
- EAS: preview builds for the user's review before any store submission.

## Rules

- Never hand-roll native modules for what Expo config/plugins already cover.
- No `console.log` shipping; route logs through a logger with levels.
- If a native feature's cost is high (custom module, review risk), surface it to the user in discovery — don't bury it mid-build.
