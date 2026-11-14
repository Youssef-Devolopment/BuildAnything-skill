# STATUS.md

> The handoff document. The next AI (or human) reads this first and knows exactly what to make next.
> **Update at every stage gate** — same change as the code it describes.

**Last updated:** {{date}} · **Current stage:** {{N — name}} · **Build:** {{green ✅ / failing ❌}}

## What's done

<!-- Only verified, working behavior. Never list unimplemented features. -->
- ✅ Stage {{N}}: {{outcome}} — {{date}}

## In progress

<!-- The stage currently being built, or "—". -->
- 🔄 Stage {{N}}: {{outcome}}

## Next up

<!-- The next stage(s), in order. This is the "tell me what to build" list. -->
1. Stage {{N+1}}: {{outcome}}
2. Stage {{N+2}}: {{outcome}}

## Known issues

<!-- Real, confirmed problems with severity. Empty = none. -->
- 🔴 {{blocker}} — {{where / how to reproduce}}
- 🟡 {{major}} — …

## Decisions needed from the user

<!-- Open questions blocking progress. Empty = none. -->
- —

## Environment & commands

<!-- The copy-pasteable facts. Keep exact; test them. -->
- Install: `{{cmd}}` · Run: `{{cmd}}` · Test: `{{cmd}}`
- URL: {{local/prod URL}} · CI: {{badge/link}}
