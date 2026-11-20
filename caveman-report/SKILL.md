---
name: Caveman Report
description: Use when reporting to the user what was just built, fixed, or broken — stage-gate reviews, delivery summaries, error explanations, progress updates — to cut filler and tokens while keeping every fact, caveat, and piece of evidence intact.
---

# Caveman Report

The evidence rule says a "done" needs pasted output. This skill applies the opposite pressure to **words**: same facts, fewer words. It removes padding, never substance.

## When it applies

- Stage-gate review — "what stage N delivered"
- Delivery summary — "what did you make"
- Error explanation — why it broke, what the fix was
- Progress update mid-build
- Whenever the user says "be brief", "less tokens", "caveman mode", "stop padding"

**Never** applies to: source code, commit messages, PR bodies, or any file in the repo (`PLAN.md`, `TODO.md`, `STATUS.md`, `CHANGELOG.md`, `README.md`). Those stay normal prose — they are read by other agents and by humans who did not ask for caveman.

## The rules

**Drop:** articles (`a`/`an`/`the`), filler (`just`/`really`/`basically`/`actually`/`simply`), pleasantries (`sure`/`certainly`/`happy to`), hedges (`maybe`, `probably`, `I think`, `it seems`).

**Keep:** exact technical terms, file paths, identifiers, numbers, and quoted error text. Technical terms are never translated into shorter words — `middleware` is not `middle bit`.

**Fragments are fine.** Short synonyms win (`fix` not `implement a solution for`, `big` not `extensive`, `broken` not `non-functional`).

**Code blocks, diffs, and command output are never compressed.** Paste them raw and unchanged.

Pattern: `[thing] [action] [reason]. [next step].`

Not: "Sure! I'd be happy to help with that. The issue you're experiencing is likely caused by a misconfigured environment variable."

Yes: "Env var `DATABASE_URL` unset. App cannot connect at boot. Fix: add it to `.env`."

## What never shrinks

These stay in normal prose, whatever the mode:

1. **Evidence** — the pasted command output or screenshot the gate requires. A compressed report with no evidence is a false claim.
2. **Security warnings and destructive-action confirmations.**
3. **Multi-step sequences** where fragment order could be misread (setup steps, migrations, multi-file edits).
4. **Anything the user asked to clarify, repeated, or showed signs of not understanding.**

Resume caveman once the clear part is done.

## Report skeleton

```text
<what shipped, one line>
<evidence — raw output or screenshot>
<what's left / next step>
```

Three parts. Never four. Never a preamble. If a stage has more to say, it needs more stages, not a longer message.

## Modes

| Mode | Use |
|---|---|
| **lite** (default) | Filler and hedges gone, sentences intact. Best for non-technical users and for anything a human must act on. |
| **full** | Articles dropped, fragments fine, short synonyms. |
| **ultra** | Abbreviated (`DB`/`auth`/`config`/`req`/`res`/`fn`/`impl`), causality as arrows (`X → Y`), one word where one word fits. |

Switch on request: `caveman full`, `caveman ultra`, `normal mode` (off). The mode persists until changed or the session ends. Full ladder with worked examples: `references/modes.md`.

## Rules

- Compression never deletes a fact, a caveat, a blocker, or a warning.
- Never compress the evidence block, a file path, or the error text.
- If a compressed line needs the reader to open a file to understand it, it is not safe — write the missing fact in.
- Do not use caveman to look clever. The reader is checking what you built, not your vocabulary.
- One sentence per claim. If a claim needs two, split it.
- Do not end a report with "does this look good?" — state what is done and what is next.

## Handoff

- Loaded by `build-anything` at every stage-gate review and at the final delivery summary.
- If the user asks for "normal mode" mid-build, drop it for the rest of the session — do not silently re-apply it at the next gate.
