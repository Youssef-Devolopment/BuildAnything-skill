# Failure recovery: the 5-step correction loop

**Trigger: immediately**, whenever a test fails, a build errors, **or any command execution fails** — no exceptions, no "try something and see". This protocol prevents trial-and-error and random code modifications:

1. **Capture** — save the *exact* error: full message, stack/line, and the command that produced it. Copy it unmodified — no paraphrasing, no truncating the stack.
2. **Read** — open the source file(s) the error points at (and their callers). Read the actual code; don't reason from memory of what it probably says. Pinpoint the exact line of failure.
3. **Hypothesize** — state **one** root cause as a single, clear, direct, testable sentence: "X fails because Y at line Z." If you can't name one specific cause, you don't understand the error yet — go back to step 2 (read deeper: the error is often in a file away from the crash site — follow the data, not the stack trace).
4. **Fix minimally** — apply the bare minimum change that makes the hypothesis true. No rewriting entire files, no drive-by refactors, no "while I'm here" cleanup, no invalid/placeholder code (AI slop). One fix per iteration.
5. **Verify** — re-run the **exact failing command** (then the full suite/build) to confirm the error is completely eliminated and the stage transitions successfully. Green → done; red → back to step 1 with the *new* error.

Rules:
- **One fix per loop iteration.** Changing three things at once makes it impossible to know which one worked.
- **Cap at 3 iterations.** Two loops with no progress → stop, write up (captured error + what you read + your hypothesis + what you tried) and report to the user. Never thrash.
- **A fix that needs a new dependency, a schema change, or >~20 lines** is a plan change: revise `PLAN.md` first, get approval, then fix.
- Log every fixed error in `CHANGELOG.md` → Fixed (error text → cause → fix), so the next agent never re-stumbles into it.
