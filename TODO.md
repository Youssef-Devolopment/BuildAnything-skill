# Project TODO Ledger

## Stage 1: Protocol compliance (dogfood run)

- [x] Audit repo against skill's own definition of done (doc set, tests, doctor) — evidence: `python scripts\verify.py` → ALL CHECKS PASSED; `install.ps1 -Doctor` → exit 0
- [x] Write PLAN.md (retrospective contract, §9 assumptions) — evidence: file exists at repo root
- [x] Write TODO.md (this ledger) — evidence: file exists at repo root
- [x] Write STATUS.md (stage ledger for handoff) — evidence: file exists at repo root
- [x] Append CHANGELOG stage entry — evidence: CHANGELOG.md entry "Dogfood run"

## Stage 2: Eval first run (not started — needs live model sessions)

- [ ] Run T1–T10 from `eval/TASKS.md` in fresh sessions against one model
- [ ] Score from artifacts (re-run commands; no self-grading) and fill `eval/RESULTS.md`
- [ ] Record median turns + honesty violations per `eval/README.md`

Rules: `- [x]` only with quoted green output or file evidence. New work discovered
mid-build becomes a task here first — no side quests.
