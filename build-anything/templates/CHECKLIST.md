# Pre-Flight Checklist

> Mandatory verification before **any code is output for a stage** and again before **deploy/release**.
> Answer every line explicitly (`yes` + evidence, or `fix first`). One `no` = the code doesn't ship.

## Before writing a stage's code

1. **Env vars** — every variable the code reads already exists in `.env.example` (with description + safe placeholder)? New ones added in this change?
2. **Dependencies** — every import/library used is declared in the project's package file (`package.json`, `requirements.txt`, `pyproject.toml`, `go.mod`, …) with a pinned/lockfile-consistent version? Nothing assumed-installed?
3. **No secrets or placeholders** — zero hardcoded keys/tokens/passwords/URLs-with-credentials; no `TODO`, lorem ipsum, fake data, or stubbed returns that pretend to work?

## Before the gate closes (deploy/release only)

4. **Tests** — the full suite runs green from the exact command in README?
5. **Fresh-clone path** — install → run → test works with no private context and no machine-specific paths?
6. **Docs touched** — `STATUS.md` ledger updated, `CHANGELOG.md` entry appended, any behavior change reflected in the docs that describe it?
7. **Secrets scan** — `.env` ignored, `.env.example` current, no personal data/internal URLs in code or history?

## How to answer

- Copy this file's relevant section into the stage review if the stage touches env/deps/secrets.
- Evidence required: the command you ran or the file:line you checked — not "should be fine".
- A `no` on 1–3 → fix before writing more code (cheap now, expensive later).
- A `no` on 4–7 → the gate does not pass; back to the stage.

Template rule: keep this file in the repo root of BuildAnything projects (copy from `templates/CHECKLIST.md`); `readiness-judge` treats an unchecked pre-flight as a blocker.
