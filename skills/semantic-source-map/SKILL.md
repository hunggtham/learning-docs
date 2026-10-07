---
name: semantic-source-map
description: Map source knowledge units to learning sections before full Markdown generation.
metadata:
  short-description: Build source-to-lesson coverage
---

# Semantic source map

Use after intake and before full authoring, especially for books, OCR, imported Markdown and large reference sets.

## Outcome

Create a semantic-map.tsv that maps knowledge-bearing source units to planned output sections. Keyword or heading presence is not coverage evidence.

## Required unit types

Inventory relevant definitions, distinctions, classifications, mechanisms, procedures, conditions, exceptions, formulas, tables, figures, examples, rules, terminology and exercises. Exclude navigation-only material explicitly rather than silently dropping it.

## Minimum columns

~~~text
source_id	source_locator	unit_type	claim_or_question	output_path	section_owner	coverage	currentness_risk	source_confidence	notes
~~~

Coverage is one of FULL, PARTIAL, MISSING, or NOT_APPLICABLE with a reason.

## Procedure

1. Read the source around each candidate unit; do not infer meaning from headings alone.
2. Group units by conceptual dependency and canonical owner.
3. Mark historical/current separation and unresolved ambiguity.
4. Identify a representative pilot section and the handoffs required between sections.
5. Review the map for duplicate ownership, missing boundaries and source units that would force reopening raw material.

Do not write polished full lessons in this mode. A map that cannot explain why a learner can replace the source for a FULL unit is not complete.
