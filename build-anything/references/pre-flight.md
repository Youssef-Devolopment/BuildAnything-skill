# Pre-flight sanity check (mandatory)

Before outputting a stage's code — and again before any deploy/release — run `templates/CHECKLIST.md` and answer every line with evidence:

1. **Env vars** — everything the code reads exists in `.env.example`?
2. **Dependencies** — everything imported is declared in the package file, lockfile-consistent?
3. **No secrets or placeholders** — zero hardcoded keys, no TODO/lorem/fake data pretending to work?
4. **Security floor** — no secrets/keys committed (history included), `.env*` gitignored, dependency audit clean (`npm audit` / `pip-audit` / equivalent where the stack has one), no dangerously permissive defaults (open CORS, debug mode in prod)?

Before the *gate* closes additionally: tests green from the README command, fresh-clone path works, docs touched, secrets scan clean, dependency audit clean. One explicit `no` = don't ship; fix first (cheap now, expensive later). Never answer "should be fine" — the answer needs the command run or the file:line checked.
