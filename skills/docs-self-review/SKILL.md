---
name: docs-self-review
description: Review a learning-document draft before learner reading across source, coverage, prose and ownership evidence.
metadata:
  short-description: Preflight a learning-doc draft
---

# Learning document self-review

Use after a draft or pilot exists and before sending it to the user for reading.

## Review layers

Review separately:

1. **Source/fact** — important claims have an appropriate source, version/date and currentness boundary.
2. **Semantic coverage** — source units are FULL/PARTIAL/MISSING for defensible reasons.
3. **Mental model** — each teaching block connects object/goal → mechanism/constraint → consequence or decision.
4. **Learner prose** — Vietnamese explains the idea naturally; terms in English/Korean remain only when useful for lookup.
5. **Ownership/navigation** — owner, links, prerequisites and handoffs match the canonical map.

## Severity

- high: wrong fact, missing core unit, misleading boundary, broken ownership, source-wrapper prose, quiz content or unusable example;
- medium: reasoning is correct but abrupt, under-explained or hard to navigate;
- low: wording that does not alter the mental model.

## Output

Return a report with PASS or FAIL, evidence for each issue, affected paths, smallest safe repair and remaining limits. repo_audit.py, link checks and whitespace checks are structural evidence only; they do not prove prose quality.

Do not perform a broad rewrite to make the report look clean. Re-read the affected section and adjacent handoffs after any repair.
