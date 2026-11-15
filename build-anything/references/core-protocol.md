# Core protocol (one file — weak/free models, quota limits, or minimum ceremony)

The whole BuildAnything loop without chaining skills. Follow this file directly when you are a small model, low on quota, or the user wants minimum ceremony. **Rigor stays (plan → gate → verify → document); only ceremony shrinks.**

## 1. Detect & choose the tier

Survey the workspace (root, manifests/configs, git state, existing `PLAN.md`/`TODO.md`/`STATUS.md`). State one short block: detected state + tier (**Resume / Fix / Feature / Full** — definitions in `SKILL.md`).

## 2. Plan (Full and Feature tiers only)

- **Full:** one batch of **max 5 questions**, each with a best-guess answer → copy `templates/PLAN.md`, fill all sections (unanswered → §9 Assumptions) → get approval (proceed if hands-off, file must exist) → copy `templates/TODO.md`, atomic tasks grouped by stage.
- **Feature:** 5-line mini-plan (or a `PLAN.md` §6 addition) → tasks.
- **Resume:** read `STATUS.md` → next unchecked `TODO.md` task → go. No interview, no new plan.
- **Fix:** no plan files. Sketch the tasks in chat/`TODO.md`, then code.

## 3. Per stage, repeat

1. Pick the next unchecked task.
2. **Dry-run preview first** if the change is major (wholesale rewrite, 3+ files at once, new dependency, schema/migration, auth/payments/deletion, anything destructive) — two lines, wait for yes. Otherwise just do the task.
3. Write the **least code** that works; run the tests.
4. Command failed → `recovery-loop.md`: capture → read → one hypothesis → minimal fix → re-run. **Max 3 iterations**, then report with the captured evidence.
5. Run `pre-flight.md` before shipping the stage.
6. **Evidence:** paste the raw command output (screenshot for UI). Banned: "should work", "looks correct", "verified" without quoted output.
7. Check off the `TODO.md` tasks, append `CHANGELOG.md`, flip `STATUS.md`.
8. Review checkpoint: show it running. *Quota mode:* batch reviews into one at stage end — say explicitly that you're batching and that the user can demand per-stage reviews.

## 4. Finish

Run the definition of done (`references/workflow.md`) → optionally `recommendations` → `readiness-judge`: **run the commands, paste the output; the user makes the READY call from that evidence** — never a self-graded verdict.

## 5. Handoff

Docs current (`STATUS.md` accurate, `CHANGELOG.md` appended). For the next session, give the cold-start prompt from `SKILL.md`.

## Banned in this protocol

- Thrashing: more than 3 fix iterations without progress.
- Scope additions not in the "proposed additions" list (principle 7).
- `- [x]` without green output quoted.
- Swallowed or deferred-silently errors.
- A second round of interview questions when §9 Assumptions would do.
