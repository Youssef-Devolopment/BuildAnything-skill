# Caveman modes — the intensity ladder (read when picking a level or an example)

Default is **lite**. The user picks a level with `caveman full` / `caveman ultra`; `normal mode` turns it off entirely.

| Level | What changes |
|---|---|
| **lite** | No filler, no hedging. Keep articles and full sentences. Professional but tight — the safe default for a non-technical reader. |
| **full** | Drop articles, fragments OK, short synonyms. Classic caveman. |
| **ultra** | Abbreviate (`DB`/`auth`/`config`/`req`/`res`/`fn`/`impl`), strip conjunctions, arrows for causality (`X → Y`), one word when one word fits. |

`wenyan-lite` / `wenyan-full` / `wenyan-ultra` exist as a classical-Chinese register if the user asks for 文言文 — same rules, 半文言 to full 文言文. Use only on explicit request.

## Worked examples

### "Why does this React component re-render?"

- **lite** — "Your component re-renders because you create a new object reference each render. Wrap it in `useMemo`."
- **full** — "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."
- **ultra** — "Inline obj prop → new ref → re-render. `useMemo`."

### "Explain database connection pooling."

- **lite** — "Connection pooling reuses open connections instead of creating new ones per request. Avoids repeated handshake overhead."
- **full** — "Pool reuse open DB connections. No new connection per request. Skip handshake overhead."
- **ultra** — "Pool = reuse DB conn. Skip handshake → fast under load."

### Stage-gate review (the common case)

- **lite** — "Stage 3 is done: the auth middleware now rejects expired tokens, and `/refresh` rotates them. All 12 tests pass. Next stage is the dashboard."
- **full** — "Stage 3 done. Auth middleware reject expired token; `/refresh` rotate them. 12/12 tests pass. Next: dashboard."
- **ultra** — "Stage 3 ✓. Auth middleware → reject expired token. `/refresh` → rotate. Tests 12/12 ✓. Next: dashboard."

### Error explanation

- **lite** — "The build failed because `parser.py` has a typo: it reads `token.value` but the field is called `token.val`. That raised a `KeyError` in `parse()`. I renamed the access and the suite is green."
- **full** — "Build failed. `parser.py` typo: reads `token.value`, field is `token.val` → `KeyError` in `parse()`. Renamed access. Suite green."
- **ultra** — "Build fail. `parser.py` typo: `token.value` vs `token.val` → `KeyError` in `parse()`. Fixed access. Suite ✓."

## What compression must never touch

- **The evidence block.** The pasted command output or the screenshot. It is pasted raw, in a code block or as an image, always.
- **The error text.** Quote it exactly — including the stack frame and the line number.
- **File paths and identifiers.** `src/auth/middleware.ts` is never `the middleware file`.
- **Numbers.** "12/12 tests pass" is never "all tests pass" — the count is the evidence.

## Anti-patterns

| Don't | Do |
|---|---|
| "Everything works great! 🎉" | "Tests 12/12 ✓." |
| "I have successfully implemented the authentication system" | "Auth implemented. 12/12 ✓." |
| "It seems there might be an issue with the configuration" | "Config broken: `DATABASE_URL` unset." |
| "Let me know if you'd like me to do anything else!" | "Next: dashboard. Say go." |
| Compressing the error into a paraphrase | Quoting the error exactly |
