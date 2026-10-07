---
name: scope-claim
description: Claim a narrow file and artifact scope for concurrent chats, worktrees and external agent runs.
metadata:
  short-description: Prevent parallel task overlap
---

# Scope claim

Use before a task starts writing in a shared repository.

## Conflict classes

- DISJOINT: independent files and artifacts; safe to run in parallel.
- SHARED_POLICY: common prompts, schemas, README/index or registry; one owner at a time.
- GENERATED_DEPENDENCY: source, generator and output; serialize source-to-output work.
- INTEGRATION_SENSITIVE: migrations, deploy config, catalogs and global indexes; integration owner only.

## Procedure

1. Record task id, worktree, base SHA, allowed paths and forbidden paths.
2. Compare the claim with active claims and canonical owners.
3. Record dependencies and the next handoff target.
4. Release or update the claim only in the handoff; do not silently reuse another task's scope.

If an overlap is found, choose disjoint paths, wait for the dependency, or escalate to an integration owner. Never resolve overlap by deleting another task's changes.
