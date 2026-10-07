---
name: acceptance-gate
description: Decide whether a learning-document task is ready for learner approval, merge or publication using explicit evidence.
metadata:
  short-description: Apply the final evidence gate
---

# Acceptance gate

Use after self-review, learner review and scoped validation.

## Check

1. Read the task manifest and handoff.
2. Verify source, semantic, prose, owner/link and learner criteria separately.
3. Verify diff scope, revision, generated-output parity and validation artifacts.
4. Separate content status from Git and publication status.
5. Return PASS or FAIL with remaining issues, not a generic completion claim.

repo_audit.py, link checks, build success or an agent's finished state prove only their own scope. They do not prove learner usability or integration.
