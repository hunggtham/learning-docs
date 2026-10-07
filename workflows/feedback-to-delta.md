# Workflow: learner feedback to bounded delta

Use after the user or learner reports that a document is wrong, unclear, incomplete or unusable.

## 1. Capture

Preserve the exact feedback, revision, learner action and affected path. If the report is vague, mark NEEDS_CLARIFICATION instead of inventing a defect.

## 2. Triage

Run learner-feedback-triage. Classify the root cause and identify the smallest section that can repair it.

## 3. Verify

Reproduce the issue or use an evidence-equivalent test. Recheck source, semantic map, owner and current-state boundary.

## 4. Repair

Edit only the claimed paths. If the correction changes a prerequisite or handoff, inspect the adjacent sections and record them as regression scope.

## 5. Regression

Run the original learner/test scenario, scoped structural checks and any generator audit. Record pass, fail or blocked with exact evidence.

## 6. Handoff

Return feedback triage, changed paths, revision, evidence, unresolved issues and next status. Do not call the task complete merely because wording changed.
