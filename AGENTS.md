# Repository agent rules

## Content authoring boundary

- Read `prompt/COMMON_PROMPT.md` before creating, reviewing, or regenerating learning docs.
- Do not use Python, JavaScript, regex, templates, workers, or any other automation to invent, inject, duplicate, or rewrite learner-facing prose, section introductions, transitions, summaries, explanations, examples, or conclusions.
- Generators may perform structural work only: read an authoritative source, preserve source text, normalize markup, split or order files, create navigation links, and write machine metadata or audit reports.
- Any new learner-facing prose must be written and reviewed manually for the specific topic. If an existing generator would add prose, remove that logic before running it.
- AI may propose a draft, but the draft is not accepted content until a human has reviewed the changed file, its source boundary, evidence, examples and learner flow.
- Do not invent facts, current claims, citations, URLs, quotations, page numbers, formulas, code/SQL outputs, translations, or examples. Mark unresolved claims `UNVERIFIED` or `NEEDS_SOURCE` instead of guessing.
- Do not use generated/public output, catalogs, manifests or a previous AI draft as the authoritative source for new prose. Preserve the canonical source and provenance boundary.
- Do not upload private notes, copyrighted books, exports, secrets, API keys or credentials to an external AI/API service.
- Do not delete, overwrite, rename, reorder or regenerate outside an explicit allowed-path manifest. Inspect status before the batch and the scoped diff after it.
- Do not expand from one requested file/batch into another topic, subject or corpus-wide goal without explicit authorization.
- Do not modify a checker, count, metadata or state file merely to make a batch pass. Do not claim `accepted`, `validated`, `published` or `synced` without the corresponding evidence.
- Examples containing invented people, organizations, events, numbers or claims must be labeled hypothetical; do not present them as real evidence.
- Do not copy or lightly paraphrase proprietary/reference definitions, translations, examples or explanations. Use references to verify usage, then write original teaching prose.
- Never regenerate over manually authored content without inspecting the diff and preserving unrelated or manually reviewed text.
- A structural or link audit cannot be used as evidence that prose is natural or semantically correct.

## Source and output boundary

- Treat `raw/`, `raw_md/`, and imported material as sources, not as permission to mass-rewrite text.
- For source-generated outputs, change the source or a structural-only generator, then inspect the scoped diff. Do not use a generator to restore boilerplate.
- Keep content, evidence, Git, and publication status separate in any handoff.
