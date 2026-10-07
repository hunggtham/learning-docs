---
name: agent-surface-dispatch
description: Select Codex, Daintree, Antigravity or ChatGPT Web for a bounded task based on side effects and required evidence.
metadata:
  short-description: Route work to the right agent surface
---

# Agent surface dispatch

Use when a task may run across multiple AI tools.

## Routing

- Use ChatGPT Web for source research, comparison, decision memo and prose/learner review when no local mutation is needed.
- Use Daintree for worktree creation, parallel CLI runs, monitoring and review orchestration.
- Use Antigravity for browser/UI/runtime tasks that need screenshots, recordings or interactive verification.
- Use Codex for canonical repository edits, source/generator changes, audits and integration.

## Required dispatch record

Write the task id, selected surface, allowed side effects, worktree/revision, expected artifacts, validation and handoff target before dispatch.

Do not dispatch a write-capable surface when the task is still a research question. Do not use two supervisors on one worktree. If a surface cannot provide revision-anchored evidence, keep its result advisory rather than integrated.
