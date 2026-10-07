# Workflow: acceptance and integration

Use after authoring, self-review, learner review and any external runtime verification.

## Evidence collection

Collect:

- source ledger and semantic map;
- self-review and learner-feedback reports;
- test/build/link results;
- screenshots or recordings when UI/runtime evidence is required;
- current diff, base/current SHA and generated-output report.

## Gate order

1. Content acceptance.
2. Evidence completeness.
3. Scope and conflict check.
4. Source/generated parity.
5. Integration review.
6. User approval.
7. Publication verification.

Record each gate as PASS, FAIL or BLOCKED. A failure at one gate must not be hidden by a pass at another.
