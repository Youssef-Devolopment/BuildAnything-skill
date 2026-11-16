# PLAN.md — BuildAnything (this repo)

> Retrospective contract: written during the v1.13 dogfood run, from the shipped
> README + CHANGELOG evidence. Before this file existed the repo was built from
> chat intent alone — exactly what this skill forbids.

## 1. Overview

BuildAnything is a public skill set (19 skills) that makes any AI, with any
model, build anything the right way — interviewed, planned, stage-gated,
tested, documented. Primary users: OpenCode users (Windows-first), free/small
models, non-developers.

## 2. Requirements

1. Any AI/model can load and follow the process (progressive disclosure, tier table).
2. Install is foolproof: one method chosen, duplicate detection (`install.ps1 -Doctor`).
3. Self-verified: CI runs `scripts/verify.py` on every push (frontmatter, core files, fixture states).
4. Handoff-complete: README, CHANGELOG, eval harness all in-repo.
5. Releases are tagged and changelogged (append-only).

## 3. Out of scope

- macOS/Linux installers (owner decision: Windows/PowerShell only).
- Further skill merges beyond the clone merge (owner decision).
- Running the eval harness against live models (needs model sessions; harness ready).

## 4. Tech stack

Pure Markdown + PowerShell 5.1 (ASCII-safe) + Python 3.10+ for verification.
No package managers, no runtime dependencies — install takes seconds.

## 5. Architecture

Per skill: `build-anything/` (working card + `references/` + `templates/`) then
18 layer/phase skills. Support files: `scripts/verify.py` (CI gate),
`eval/` (10 tasks + 5 fixtures), `install.ps1`/`update.ps1`, `.github/workflows/verify.yml`.
Layout tree lives in README.

## 6. Implementation — stages

1. **Protocol compliance (this stage)** — backfill PLAN/TODO/STATUS, gate evidence = verify.py + doctor.
2. **Eval first run** — execute T1–T10 in fresh sessions against one model, fill `eval/RESULTS.md`.
3. **Ongoing maintenance** — every feature/fix follows the same gates from here.

## 7. UI/UX

None — no user interface. README is the storefront; install paths documented for OpenCode, Claude, agents, Bionic (drag-and-drop folder/file).

## 8. Testing & QA

`python scripts\verify.py` = the suite (9 core files, 19 frontmatters, 4 fixture
red/green exit codes). Must pass locally and in CI before every release tag.

## 9. Assumptions & decisions

- Windows-only install was an explicit owner decision (session evidence).
- Clone skills merged; all other 18 skills stay separate (owner decision).
- Single-file `BuildAnything` edition in Downloads was a one-off deliverable, not repo content.
- Future roadmap beyond §6 Stage 2: **not assumed** — TBD via `recommendations` when the owner asks.
- Rejected: force-pushing releases (history is append-only; we revert instead).

## 10. Definition of done

- [x] Repo docs complete: PLAN.md, TODO.md, STATUS.md, README, CHANGELOG
- [x] `verify.py` green locally and in CI on latest commit
- [x] `install.ps1 -Doctor` exit 0 (one install, no conflict)
- [x] All releases tagged; CHANGELOG append-only
- [ ] Eval harness run once with results in `eval/RESULTS.md` (Stage 2)
