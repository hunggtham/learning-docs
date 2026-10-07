# Workflow: Daintree fleet run

Use when Daintree launches several agent CLIs or worktrees for one repository.

## Before dispatch

1. Create one task manifest per worktree.
2. Record base SHA, allowed/forbidden paths, conflict class, dependencies and expected artifacts.
3. Route each task with agent-surface-dispatch.
4. Do not give two agents a shared-policy or integration-sensitive scope.

## During dispatch

- Daintree manages worktree creation, terminal state, monitoring and review queue.
- The worker follows the task manifest and writes artifacts in the claimed scope.
- A broadcast prompt is allowed for read-only research or truly disjoint tasks only.
- Waiting, blocked and finished are operational states, not acceptance states.

## Review and integration

1. Collect revision-anchored handoffs from every worktree.
2. Check base drift, path overlap, generated-output consistency and validation evidence.
3. Use one integration owner for shared indexes, manifests, generators and final merge.
4. Run acceptance-gate after integration, not before.

## Recovery

If a run stops, inspect the worktree, task manifest, diff and latest handoff. Resume from the last validated checkpoint; never recreate a task with a broader scope just because the dashboard lost context.
