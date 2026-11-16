# Interview question bank (copy-paste, max 5 per project)

Rules: **one batch, ≤5 questions, every question with your best-guess answer.** Unanswered → `PLAN.md` §9 Assumptions. Pick the group matching the project type, then stop. Question order: goal → scope → the one flow that matters → quality bar → taste.

## Universal 5 (any project, fill guesses from what the user already said)

1. Who uses this and what's the one thing it must do for them? *My guess: <from their message>.*
2. What's in v1 — and what's explicitly NOT? *My guess: <smallest useful version>.*
3. What does "done and good" look like — how will you check it works? *My guess: you click/see it working.*
4. Any hard constraints (free hosting, a deadline, must-use tool, must-avoid tech)? *My guess: free + simple.*
5. What would make this **better** than what you're imagining? *My guess: <their earlier frustration>.*

## SaaS / web app

1. What does a user do first after signing up? *My guess: <core action>.*
2. What data does the app own (accounts, posts, orders…)? *My guess: <entity list>.*
3. Who logs in — one admin, members, the public? *My guess: <auth shape>.*
4. Payments in v1 or later? *My guess: later.*
5. Roughly how many users at launch? *My guess: <tens — sets the simple stack>.*

## Landing page / marketing site

1. Who is the visitor and what should they do in 10 seconds? *My guess: <action>.*
2. Sections: hero, proof, features, pricing, FAQ, CTA — which are real? *My guess: <list>.*
3. Real copy/photos available, or placeholders until you provide them? *My guess: placeholders, flagged.*
4. Where does it live (domain, GitHub Pages, free host)? *My guess: free host.*
5. A reference site you like? *My guess: <none — your call>.*

## CLI / developer tool

1. What's the exact command and its input → output? *My guess: `tool <file>` → report.*
2. Where does it run — Windows/Linux/both, no-install Python OK? *My guess: Windows first.*
3. What error should a user see when it fails? *My guess: one clear line, exit code.*
4. Config: flags, config file, or hardcoded? *My guess: flags.*
5. Who else uses it — just you or public release? *My guess: just you for now.*

## Mobile app

1. Which platform first — iOS, Android, both? *My guess: both via Expo if you have a phone of each.*
2. The core loop: open app → do what → feel what? *My guess: <action> → <result>.*
3. Offline needed? What happens with no connection? *My guess: cached view, clear message.*
4. Real device features used (camera, GPS, notifications)? *My guess: <none/list>.*
5. Store release in scope, or personal install? *My guess: personal install first.*

## Non-developer add-ons (append instead of tech questions)

- "I'll decide the tech — one question instead: should it work on phone, desktop, or both?" *My guess: both.*
- "Free hosting is fine unless you need a custom domain — correct?" *My guess: free is fine.*
