---
name: Testing
description: Use when adding tests, deciding strategy, or fixing a flaky suite — what to test per layer, how much, keeping the suite fast and trustworthy.
---

# Testing

Load `build-anything` first (stage gates already require tests per stage). This skill decides *what* to test and *how*, so the suite is fast, trustworthy, and worth running.

## Strategy (decide once, in `PLAN.md` §8)

Pick the pyramid that fits the project — record it, don't re-litigate per feature:

| Layer | Tool (default) | What it covers | Speed target |
|---|---|---|---|
| Unit | Vitest / pytest / go test | Pure logic, edge cases, error paths | <10s |
| Integration | Same + real DB/container | DB queries, migrations, API contracts | <60s |
| E2E | Playwright / Maestro | The main user flows in `PLAN.md` | <3min smoke |

**Rules of thumb:** test behavior, not implementation; the more expensive the layer, fewer of them — most tests are unit/integration; every `PLAN.md` main flow has exactly one E2E.

## What earns a test

✅ Business logic with branches; validation and auth boundaries (401/403 paths); data migrations; error paths; every bug you fix (regression test **first**); anything that broke before and could break again.
❌ Getters, framework code, snapshot-tests-as-coverage, testing that a library works, one-off scripts.

## Test quality bar

- **Arrange–Act–Assert**, one behavior per test, test names that read as sentences ("rejects booking in the past").
- **Independent & deterministic**: no shared state between tests, no real clock/network/randomness (inject fakes); a rerun gives the same result.
- **One test per state**: loading, empty, error, success — for anything with a data view.
- **Real where it matters**: integration tests hit a real (containerized) DB, not mocks — mocks lie about SQL.
- **Fast feedback**: unit+integration run on every save/commit; full suite green at every stage gate.

## Flaky tests are bugs

1. Retry is not a fix — quarantine the test, find the root cause (time, order, shared state, network).
2. Can't fix immediately? Mark it visibly (`test.skip` with a linked issue/`STATUS.md` entry) so it's tracked, never silently deleted.
3. A suite with known flakes trains everyone to ignore failures — that's worse than no suite.

## Workflow

1. Read `PLAN.md` §8 + existing tests; align with the project's framework (never introduce a second test runner).
2. Write tests **with** the feature (stage gate), not after — regression test for every fixed bug first.
3. Run before each gate; report coverage of the *new* code honestly.
4. Keep the suite maintainable: shared fixtures/factories over copy-paste; delete tests for deleted behavior.

## Rules

- Never weaken or delete a test to make a build pass — fix the code or tell the user.
- Never mock the thing under test.
- CI runs the suite on every push from day one (see `build-anything`'s GitHub-native rules).
