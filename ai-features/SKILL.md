---
name: AI Features
description: Build AI-powered features properly — LLM integration, prompts, structured output, RAG/search, agents, evals, cost/latency, and guardrails. Load when the project or stage involves calling an LLM, chat interfaces, embeddings, semantic search, or AI automation. Works with build-anything, backend, and frontend.
---

# AI Features

Load `build-anything` first (an AI feature is a stage like any other — planned, gated, reviewed). This skill covers the AI-specific layer: it is **software engineering around a probabilistic component**, not magic.

## Decide AI is actually right

- Rule out the boring version first: a form + validation + a database query often beats an LLM (cheaper, deterministic, testable). If the task is classification/extraction with clear examples, consider a small fine-tuned model or simple heuristics.
- Use AI for: language understanding/generation, fuzzy matching, summarization, copilots, semantic search.
- Record the decision + rejected alternative in `PLAN.md` §4.

## Architecture (keep it boring)

- **One model layer**: a single module wraps the provider (OpenAI/Anthropic/local) — model name, retries, timeouts, token accounting live there. Never call a provider from UI components.
- **Provider-agnostic interface** so models can be swapped; pin the model *version* (e.g. dated model IDs), never "latest".
- **Every LLM call is I/O**: timeout (10–30s), retry with backoff on transient errors, and a **graceful fallback** (cached answer, degraded feature, or clear error UI) — the UI must handle failure like any async flow.
- **Stream responses** for anything user-facing (perceived latency).

## Prompts & structured output

- Prompts are **versioned code**: stored in files/constants, not inline strings; changing one is a reviewed change.
- Enforce structure: JSON schema / tool-calling / provider structured outputs → validate with Zod/Pydantic → **retry once with the validation error fed back** → fail typed, never `JSON.parse` on faith.
- Give context explicitly (system prompt = role + rules + format); few-shot examples for tricky formats; instruct "say you don't know" over hallucination.
- Treat prompt + model + settings as one versioned unit; log which was used per request.

## RAG / semantic search

- Pipeline: chunk (with overlap, by document structure) → embed → store (**pgvector** default — one DB until scale says otherwise) → retrieve (top-k + optional rerank) → stuff into prompt with citations.
- Hybrid search (keyword + vector) beats pure vector for most corpora; evaluate before adding complexity.
- Always show sources; if retrieval finds nothing relevant, say so instead of generating.

## Guardrails, cost, latency

- **Never trust model output**: validate everything; sanitize before it hits HTML/SQL/shell; the model is untrusted input like any user input.
- **AuthZ stays server-side**: the model never decides permissions; tool calls run under the user's actual rights.
- **PII**: redact before sending to providers; document what leaves your system (and where) in `ARCHITECTURE.md`.
- **Cost**: log tokens + cost per request/feature; set per-user/per-key budgets and rate limits; cache identical calls; cheaper model for simple subtasks, big model only where it earns it.
- **Latency**: parallelize independent calls; keep the first token fast; measure p95 at the stage gate.

## Evals — the tests of AI

- Build a **golden set**: 20–50 real input/expected-output pairs, versioned in the repo, run on every prompt/model change (CI or manual gate).
- Track: task success rate, format-validity rate, hallucination spot-checks, cost & latency per case.
- Never ship a prompt change on vibes — run the eval, compare, record the result.
- For user-facing chat: log conversations (with consent/retention policy) as eval material.

## UX (with `design-ui` + `frontend`)

- Show thinking/loading states; make regeneration/edit easy; never block the user on a slow call without feedback.
- Be honest it's AI: label generated content, allow correction, show confidence/sources where meaningful.
- The user should be able to *fix* wrong answers (edit, retry, provide context) — designs where AI is uncorrectable are not done.

## Rules

- Model output is never written to the DB or rendered without validation.
- Every AI feature ships with: fallback on failure, cost logging, and at least a small golden-set eval.
- If the feature can't meet its quality bar on the golden set, report the numbers to the user before the stage gate — don't pass with 40% accuracy.
