---
name: learner-feedback-triage
description: Classify learner or user feedback and repair the smallest affected learning-document scope with regression evidence.
metadata:
  short-description: Turn feedback into a bounded delta
---

# Learner feedback triage

Use after a user or learner reports that a document is wrong, unclear, incomplete or unusable.

## Procedure

1. Preserve the exact feedback and identify the affected file, section, claim or learner action.
2. Classify the root cause: fact, stale source, missing prerequisite, distinction failure, example/test failure, broken reasoning, wording, ownership/link, scope or insufficient feedback evidence.
3. Reproduce the issue or state the closest evidence-equivalent test.
4. Choose the smallest edit that repairs the mental model. Do not rewrite unrelated sections.
5. Re-read the affected section and adjacent handoffs; check source, semantic map and owner consistency.
6. Run the relevant learner/test scenario and record pass, fail or blocked.

## Output

Create a feedback triage report with original feedback, root cause, evidence, changed paths, regression checks, unresolved questions and next status. A vague report must remain NEEDS_CLARIFICATION; do not invent an issue.
