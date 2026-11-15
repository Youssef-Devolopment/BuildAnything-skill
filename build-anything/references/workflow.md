# Reasoning, execution, and definition of done (read when doing the work)

## Reasoning and research discipline (for any model size)

Treat these as mandatory steps, not optional extras — they are how a smaller model produces work on par with the largest ones:

1. **Decompose before answering.** Break the task into concrete sub-questions (what exists? what's the constraint? what does the API actually do? what could break?). Answer them in order instead of jumping to a conclusion.
2. **Search, don't recall.** Memory of APIs, flags, versions, and library behavior goes stale. For anything version-specific or unfamiliar: search the codebase (`grep`, `glob`), read the actual source/docs, and use web search for current facts. Quote evidence for claims that matter.
3. **Show the reasoning before the code.** Before writing anything, state the plan: which files change, what the approach is, what you rejected and why. If the plan doesn't survive contact with the evidence, revise the plan — not the evidence.
4. **Consider the alternatives deliberately.** For any non-trivial decision, name at least one alternative and why it loses. This counters the small-model tendency to latch onto the first plausible answer.
5. **Stress-test your own answer.** Ask "what's wrong with this?" before presenting it: check edge cases, false assumptions, and whether it actually satisfies the original request. Verify by running/reading, never by hoping.
6. **Escalate instead of guessing.** If reasoning stalls — contradictory evidence, missing information, repeated failed attempts — stop and ask the user or investigate further. A confident wrong answer is the worst outcome; a slow, verified right answer is the senior-engineer answer.

## Workflow

### Step 1: Understand before building
- Run **Phase 0 auto-detection** first (survey workspace → classify state → state what you detected), then the **Discovery** phase (`discovery.md` in this folder): interview the user until fully understood, then write and get approval on `PLAN.md` (+ `TODO.md` per Phase D). For resumed projects: read existing docs and continue from the next unchecked task.
- Read the whole relevant surface: existing source, `README`/docs, package manifests, config files, tests.
- List what must be true for this to work (constraints, data shapes, integrations) and verify each one rather than assuming.

### Step 2: Choose the best technology deliberately
- Pick the technology that fits the problem and the project's existing stack — not the newest, not the most familiar.
- Justify the choice in the docs: what you chose, what you rejected, and why.
- Prefer boring, proven, well-supported tools over novel ones unless the project genuinely needs novelty.
- For UI: build a real, polished interface — proper states (loading, empty, error, success), accessible markup, consistent spacing/typography, responsive behavior. No lorem ipsum, no fake data, no unfinished screens shipped as "done".
- For backend: real validation, real error handling, sane security defaults, no endpoints that silently fail.

### Step 3: Build it right
- Write the code that solves the actual problem, following the conventions already in the repo.
- Handle errors where they can occur; don't swallow them.
- Review your own diff before presenting it as complete: search for leftovers, debug code, duplicated logic, and dead paths.

### Step 4: Test and verify
- Run existing tests before and after your change; never leave a failing suite behind.
- Add tests for the behavior you introduce — especially edge cases and error paths. Match the project's existing test style and coverage level.
- Verify the way a user would: run the app, hit the endpoint, click the flow. A green test suite is not proof the feature works.
- If verification reveals a wrong assumption, fix the assumption in the docs too — don't just patch the symptom.

### Step 5: Build secure by default
- Never hardcode secrets, tokens, or credentials — use environment variables or the project's secret mechanism, and never commit `.env` files.
- Validate all external input at the boundary (user input, API requests, files) and treat output/encoding rules as mandatory for the stack.
- Keep dependencies minimal: every dependency must earn its place, be actively maintained, and be pinned to a known-good version. Prefer the standard library over a package when they're equivalent.
- Review what you add for known trade-offs (supply chain risk, bundle size, lock-in) and note significant ones in the docs.

### Step 6: Make it observable
- Log what matters with context (event, identifiers, outcome) at sensible levels — info for flow, warn/error for problems. No stray `console.log` debug noise shipped as the only signal.
- Show users actionable error messages; put diagnostic detail in logs, never stack traces or secrets in the UI.
- Never log secrets, tokens, or personal data.

### Step 7: Ship in small, honest steps (git hygiene)
- Keep changes focused: one concern per commit/PR, and keep the test suite green at every commit.
- Write commit messages that explain *why*, not just what changed.
- Self-review the diff before committing: no debug leftovers, no commented-out code, no unrelated files.

### Step 8: Document for the next agent (human or AI)
Maintain `.md` files so someone with zero context — including another AI — can understand the project and know exactly what to build next. Keep them accurate; stale docs are worse than no docs.

Maintain at minimum (structure and versioning details: `repo-and-docs.md` in this folder):
- **`PLAN.md`** — the approved plan from the discovery phase (`discovery.md`). The contract for what is being built and why.
- **`CHANGELOG.md`** — append-only timeline: one entry per stage gate (Added/Fixed/Changed), release headings with tags.
- **`STRUCTURE.md`** — a plain-language tour of the project for a human reader: the folder/file tree annotated with what each part does, where to make which kind of change, and the main entry points. Someone who has never seen the repo should understand its shape in one read.
- **`README.md`** — what the project is, how to install, run, test, and deploy it.
- **`ARCHITECTURE.md`** — the system's shape: major components, how data flows between them, key design decisions and their rationale, technology choices and rejected alternatives.
- **`STATUS.md`** (or a section in README) — what is done, what is in progress, what is next, known issues. This is the handoff document: the next AI should be able to read it and know exactly what to make.
- **`DECISIONS.md`** (optional, for larger projects) — short entries: context → decision → consequences.

Rules for docs:
- Write for someone who knows nothing about the project.
- Update the doc in the same change that alters the behavior it describes.
- Document *why*, not just *what* — the "what" is in the code.
- Never document unimplemented features as if they exist.

## Definition of done

- Every stage in `PLAN.md` passed its gate: clean least-code, tested, all errors fixed or reported to the user first, and reviewed by the user before the next stage.
- The pre-flight sanity check passed with evidence (`pre-flight.md` in this folder: env vars, dependencies, no secrets/placeholders — plus tests/docs/secrets at gate close).
- `STATUS.md` stage ledger is current: every cleared stage is `- [x]` with a date, next stage marked in progress.
- `PLAN.md` exists, was written before any code, and matches what was actually built.
- `TODO.md` exists (generated pre-code from the plan), every completed task is `- [x]` with its test green, and nothing was built that wasn't on it.
- The feature works and you have verified it by running it.
- Tests cover the new behavior and the suite passes.
- The code is the least code that fully solves the problem, and every line is intentional.
- The UI/backend meets real-world quality bars: no placeholders, no swallowed errors, no fake data.
- No secrets in code or logs; external input is validated; dependencies are justified and pinned.
- Errors and key events are logged with enough context to debug in production.
- All affected `.md` files are updated so the next AI knows the current state and what to build next.
- The repo is GitHub-native: a fresh clone installs, runs, tests, and explains itself (`README.md`, `STRUCTURE.md`) with no private context.
- The folder structure matches the layout decided on day one — files live where they belong, consistently.
- `CHANGELOG.md` has an entry per cleared stage gate, and releases are tagged to match.
- Every error hit during the build went through the 5-step recovery loop (`recovery-loop.md` in this folder; no thrash patches; unresolved ones reported to the user).
- At ~50%: `.opencode/skills/<project-id>/SKILL.md` exists and is current — any AI can rebuild full project context from it alone.
- Any tool friction worth removing was surfaced to the user as a concrete MCP/plugin/skill recommendation (or confirmed unnecessary).
- Nothing was guessed: every assumption about the codebase or external APIs was verified.
