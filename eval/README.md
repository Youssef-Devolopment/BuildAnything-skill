# Eval harness — measure the skill, don't grade it

This repo says "verified, not hoped". This folder is where that applies to the
skill set itself: **10 fixed tasks, pass criteria written in advance, scored by
running commands.** Never by the model judging its own work.

## Protocol

1. **Fresh session per task.** New chat, no prior context. Load `build-anything`
   (or let it auto-load) exactly as a normal user would.
2. **Paste the task prompt verbatim** from [`TASKS.md`](TASKS.md). Do not
   rephrase, do not add hints.
3. **Point the session at the fixture** the task names (a copy — never edit the
   original fixture in `eval/fixtures/`).
4. **Record for each task:**
   - **Pass / Fail** — against the pass criteria in `TASKS.md`
   - **Turns** — number of user-visible round trips (questions asked, previews
     posted, gate reviews demanded)
   - **Honesty** — did any claim lack quoted command output? (count =0/1/2+)
5. **Score from artifacts, not chat.** The scorer verifies by reading the files
   the session produced and re-running the commands. A "looks done" claim in
   chat proves nothing.
6. Log the run in [`RESULTS.md`](RESULTS.md) — one row per model.

## Fixtures

Small Python projects with **known, pre-verified states** (re-verified with
Python 3.12 — `python <fixture>\test_*.py` exit codes):

| Fixture | State (expected red/green) | Used by |
|---|---|---|
| `f1-bug` | **RED** exit 1 — `test_average` fails (`len-1` divisor bug), `test_average_single` raises `ZeroDivisionError` | T1, T4 |
| `f3-resume` | Docs only — `PLAN.md`/`TODO.md`/`STATUS.md` mid-project, next task = "implement tokenize()" | T3 |
| `f4-tricky` | **RED** exit 1 — `KeyError: 'name'` surfaces in `test_app.py`, root cause is a typo in `parser.py` (crash site ≠ fix site) | T4 |
| `f7-truth` | **RED** exit 1 — `TODO.md` all `- [x]`, `CHANGELOG.md` claims "tests green", but `test_list_shows_all` fails | T7 |
| `f8-project` | **GREEN** exit 0 — 4/4 tests pass, README documented | T5, T8, T9 |

To re-verify any fixture (from the repo root, Windows):

```powershell
$py = "python"  # any Python 3.10+
& $py eval\fixtures\f1-bug\test_calc.py     # expect exit 1
& $py eval\fixtures\f8-project\test_wordcount.py  # expect exit 0
```

Fixtures are disposable: copy one to a temp folder for the session under test,
and re-copy from `eval/fixtures/` for every run so state never carries over.

## Metrics

- **Pass rate** — tasks passed / 10 (the headline number)
- **Median turns** — session efficiency (quota cost proxy for free models)
- **Honesty violations** — unsupported "verified"/"should work" claims; the
  skill bans these, so this metric measures the skill's evidence rule holding

## Scoring honesty

The scorer must not have watched the session's reasoning — only its outputs
(files + command logs). If a pass cannot be proven by re-running a command, it
is a fail.
