# Workflow: source to learning docs

This workflow turns a source corpus into traceable learning Markdown without mixing raw material and canonical prose.

## Gates

### Gate 1 — intake

Run learning-doc-intake.

Required: task manifest, source manifest, owner, audience, allowed paths, acceptance test and current Git status.

### Gate 2 — source quality

Preserve raw/original/. Record extraction/OCR method, representative quality checks, hash and unresolved source ambiguity. A failed OCR export is not a usable source.

### Gate 3 — semantic plan

Run semantic-source-map. Produce source-unit coverage, conceptual dependencies, canonical owners and one pilot section.

### Gate 4 — pilot

Write one representative section and self-review it. If tone, depth, source separation or learner replacement is wrong, repair the pilot before fan-out.

### Gate 5 — batch authoring

Generate output in dependency order. Each batch owns disjoint output paths and records its source units. Shared index/manifest files have one owner.

### Gate 6 — self-review

Run docs-self-review on the draft and affected handoffs. Structural scripts complement manual prose/source review.

### Gate 7 — learner review

Give the user a reader packet and pilot/full output. Normalize feedback with cross-tool-handoff; repair the smallest affected section and rerun regression checks.

### Gate 8 — acceptance and integration

Record content, Git and publication statuses separately. Integrate only a revision-anchored, scoped, validated handoff.

## Parallel surfaces

- ChatGPT Web: source-ledger and decision memo;
- Daintree: task/worktree dispatch and monitoring;
- Codex: canonical authoring, audit and integration;
- Antigravity: browser/UI/runtime verification.

All surfaces return artifacts and revision information; none replaces the repository as the durable source of truth.
