# PLAN.md

> The contract for what is being built and why. Written after discovery, **before any code**.
> Updated in the same change as any requirement change. Status: `draft` → `approved`.

## 1. Overview

<!-- One paragraph: the goal, the users, what success looks like. -->

## 2. Requirements

<!-- Numbered, testable, one per line. Source: the discovery interview / IDEA.md. -->
1. <!-- R1: … -->

## 3. Out of scope

<!-- Explicitly excluded so nobody builds it later by accident. -->
- <!-- …

## 4. Tech stack

<!-- Chosen technologies + why. One line each. Then rejected alternatives + why not. -->
- **{{choice}}** — {{why}}

**Rejected:**
- {{alternative}} — {{why not}}

## 5. Architecture

<!-- Components, data model, key flows, integrations. The folder layout goes here too. -->
- **Layout:** see `STRUCTURE.md` (decided day one).

## 6. Implementation

<!-- Ordered micro-stages (from micro-planner). One outcome each, small enough to demo in a minute. -->

### Stage 1: <one-sentence outcome>
- **Files:** …
- **Steps:** …
- **Acceptance criteria:** …
- **Test:** …
- **Demo:** …
- **Docs:** STATUS.md (usually)

## 7. UI/UX

<!-- Screens/views, states (loading/empty/error), design references. -->

## 8. Testing & QA

<!-- Test pyramid per layer, key flows to cover, how verification happens. -->

## 9. Assumptions & decisions

<!-- Every "you decide" item, decisions with rationale, open questions. -->
- **A1:** {{assumption}} — confirm at review

## 10. Definition of done

<!-- The checklist this project is judged against (readiness-judge uses this). -->
- [ ] All stages pass their gates
- [ ] Tests green; main flows verified by running them
- [ ] Docs current; fresh clone installs/runs with no private context
