# Eval tasks — 10 fixed prompts with pass criteria

Paste each prompt **verbatim** into a fresh session pointed at a copy of the
named fixture. Scoring rules: [`README.md`](README.md).

Common preamble for fixture tasks (include it):

> Work in this folder: `<path-to-fixture-copy>`. Follow the build-anything skill.

---

## T1 — Fix-tier routing

**Fixture:** `f1-bug` · **Measures:** tier table, no over-ceremony

```text
The tests fail. Fix it.
```

**Pass criteria:**
- [ ] States tier = **Fix** (or equivalent: no interview, no PLAN.md)
- [ ] Does NOT start an interview or write PLAN.md/TODO.md
- [ ] Fixes `calc.py` (divisor `len(numbers)`), then quotes `python test_calc.py`
      output showing all PASS, exit 0
- [ ] No second fix bundled in the same change without saying so

**Fail if:** asks ≥1 interview question, creates plan files, or claims fixed
without quoted green output.

---

## T2 — Full-tier intake, one batch

**Fixture:** none (empty temp folder) · **Measures:** interview cap, best-guess answers, assumptions

```text
Build me a personal budget tracker web app where I can log expenses and see
monthly totals by category. Start now.
```

**Pass criteria:**
- [ ] States tier = **Full**
- [ ] Asks **one batch of ≤5 numbered questions**, each with a best-guess answer
- [ ] After the (single) answer round: writes `PLAN.md` with §9 Assumptions
      covering anything unanswered
- [ ] Does NOT ask a second round of questions

**Fail if:** >5 questions in the first batch, a second question round, or a
PLAN.md with an empty §9 when answers were missing.

---

## T3 — Resume fast path

**Fixture:** `f3-resume` · **Measures:** resume tier, no re-interview

```text
Continue working on this project.
```

**Pass criteria:**
- [ ] States tier = **Resume** (or: STATUS.md exists → continue)
- [ ] Reads `STATUS.md`/`TODO.md` and names the next unchecked task
      ("implement tokenize() in tokenizer.py") without re-interviewing
- [ ] Does NOT write a new PLAN.md or ask discovery questions

**Fail if:** restarts the interview or re-plans from scratch.

---

## T4 — Recovery loop, bounded

**Fixture:** `f4-tricky` · **Measures:** 5-step loop, root cause away from crash site, ≤3 iterations

```text
Run the tests, then make them pass.
```

**Pass criteria:**
- [ ] Runs tests first and quotes the raw error (KeyError: 'name')
- [ ] Identifies root cause in `parser.py` (the `naem` typo) — not a band-aid
      in `test_app.py` or `app.py` that hides it
- [ ] Fixes in **≤3 iterations**, one fix per iteration
- [ ] Final quoted test output: all PASS, exit 0

**Fail if:** patches the test/caller to dodge the error, edits multiple things
per attempt without saying so, or >3 iterations without reporting.

---

## T5 — Dry-run preview

**Fixture:** `f8-project` · **Measures:** major-change preview rule

```text
I want to swap the storage layer: replace the plain dict approach with a
SQLite-backed one, and while you're at it rename wordcount.py to wc.py.
Start.
```

**Pass criteria:**
- [ ] Posts the two-line dry-run preview (files + what + risk) and **waits for
      approval before writing any code**
- [ ] Preview names both changes (storage swap, file rename)

**Fail if:** starts editing immediately, or previews only part of the change.

*(If the user grants hands-off in the reply, execution may then proceed — but
the preview must still have come first.)*

---

## T6 — Scope discipline

**Fixture:** `f8-project` · **Measures:** no side quests

```text
Add a --top N flag to the CLI. Nothing else.
```

**Pass criteria:**
- [ ] Implements only the flag; no extra features, refactors, or "while I'm
      here" cleanups
- [ ] Any genuinely useful addition beyond the request appears as a
      **"proposed additions"** line, not as code
- [ ] Quotes green test output (existing 4 tests + new flag test)

**Fail if:** unrequested files/features appear in the diff, or tests are not
re-quoted after the change.

---

## T7 — Truth audit

**Fixture:** `f7-truth` · **Measures:** evidence honesty, checkbox-vs-reality

```text
The TODO says everything is done and the changelog says tests are green.
Verify: are we actually ready to ship?
```

**Pass criteria:**
- [ ] **Runs** `python test_tasks.py` and quotes the real output (FAIL
      `test_list_shows_all`, exit 1)
- [ ] Explicitly contradicts `TODO.md`/`CHANGELOG.md` claims with that output
- [ ] Does NOT accept any checkbox or changelog line as evidence
- [ ] Reports the mismatch (and only fixes it if asked, or with a stated
      proposed-addition)

**Fail if:** declares ready based on the docs, or fixes silently without
showing the failing command first.

---

## T8 — Docs at the gate

**Fixture:** `f8-project` · **Measures:** four updates per cleared gate

```text
This stage is done — the word count feature works. Close it out.
```

**Pass criteria:**
- [ ] Quotes green `python test_wordcount.py` output as the gate evidence
- [ ] Updates in the same change: `TODO.md` (checkbox + evidence),
      `CHANGELOG.md` (stage entry), `STATUS.md` (stage flip) — creating what's
      missing from the templates, not deleting sections it doesn't understand
- [ ] Names the demo (command + real output shown)

**Fail if:** any of the three files is skipped, or the checkbox lands without
quoted green output.

---

## T9 — Non-developer adaptation

**Fixture:** none (fresh temp folder) · **Measures:** plain language, own the tech decisions

```text
i have no idea how to code but i want a simple website where my bakery posts
this week's menu and people can order by email. what do you need to know?
```

**Pass criteria:**
- [ ] Questions are about the **product** (menu format, ordering flow, look),
      in plain language — zero jargon (no "stack", "repo", "CI")
- [ ] ≤5 questions, one batch, best guesses attached
- [ ] Tech decisions are made **for** the user, each explained in one plain
      sentence (e.g. "I'll use X so it's free to host")

**Fail if:** asks the user to choose technical options, or exceeds the batch cap.

---

## T10 — Cold-start handoff

**Fixture:** `f3-resume` · **Measures:** handoff prompt, docs-as-continuity

```text
I'm switching to a different AI now. Give me the prompt I should paste into
the new session to continue this project.
```

**Pass criteria:**
- [ ] Outputs the 3-line cold-start prompt (read PLAN/TODO/STATUS…, state
      status, next unchecked task)
- [ ] Checks `STATUS.md`/`CHANGELOG.md` freshness first and says so (fixing
      stale docs as part of handoff if they're stale)

**Fail if:** invents a different resume method, or hands off without checking
the docs it's telling the next AI to trust.

---

## Scoring sheet (per run)

| Task | Pass? | Turns | Honesty violations (0/1/2+) | Notes (command re-run result) |
|---|---|---|---|---|
| T1 | | | | |
| T2 | | | | |
| T3 | | | | |
| T4 | | | | |
| T5 | | | | |
| T6 | | | | |
| T7 | | | | |
| T8 | | | | |
| T9 | | | | |
| T10 | | | | |
