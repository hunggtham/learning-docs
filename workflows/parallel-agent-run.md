# Workflow: parallel agent run

Use when several chats, worktrees or external agent surfaces work on one repository.

## 1. Decompose

Split by semantic or operational boundary, not by arbitrary file count. Classify each task as DISJOINT, SHARED_POLICY, GENERATED_DEPENDENCY or INTEGRATION_SENSITIVE.

## 2. Claim

Create one task manifest per worktree with base_sha, allowed_paths, forbidden_paths, dependencies, expected artifacts and stop condition. Only disjoint tasks run concurrently.

## 3. Dispatch

Daintree may create worktrees and launch Codex/Antigravity/other CLIs. ChatGPT Web may produce research artifacts. Do not let two supervisors mutate the same worktree.

## 4. Observe

Track PLANNED → CLAIMED → IN_PROGRESS → WAITING_DEPENDENCY → READY_FOR_REVIEW → MERGE_READY → INTEGRATED. A finished agent is not an integrated change.

## 5. Review

Use the diff and handoff, not the agent's completion message. Check base drift, scope overlap, source/output consistency, generated changes and validation evidence.

## 6. Integrate

One integration owner updates shared indexes, regenerates dependent output and records the resulting revision. Preserve unrelated dirty changes and stage only claimed paths.

## 7. Recover

If a chat stops, inspect its worktree, manifest, diff and last handoff. Resume from the last validated checkpoint; do not restart or silently broaden scope.
