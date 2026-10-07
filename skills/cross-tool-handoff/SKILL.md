---
name: cross-tool-handoff
description: Normalize work and evidence when a task moves between Codex, Daintree, Antigravity, ChatGPT Web or another agent surface.
metadata:
  short-description: Create revision-anchored agent handoffs
---

# Cross-tool handoff

Use whenever a task leaves one chat, worktree, agent surface or orchestration app.

## Required handoff fields

~~~yaml
task_id:
agent_surface:
worktree:
branch:
base_sha:
current_revision:
changed_paths: []
unchanged_paths: []
artifacts: []
validation:
  commands: []
  results: []
content_status:
git_status:
publication_status:
known_issues: []
next_action:
safe_to_merge: false
~~~

## Rules

- Anchor claims to a revision, not to a chat message or dashboard state.
- Attach screenshots, recordings, source ledgers and reports as artifacts with paths.
- State whether evidence is source-backed, test-backed, user-verified or integrated.
- Never imply that an uncommitted worktree is merged or published.
- If the next agent lacks a required source or permission, mark BLOCKED instead of guessing.
