---
name: source-generated-integrity
description: Keep canonical sources, generators, derived Markdown and audits consistent during regeneration.
metadata:
  short-description: Regenerate from the real owner safely
---

# Source-generated integrity

Use when a corpus has raw/source files, a generator or build script, and generated learning output.

## Rules

1. Identify the canonical source and generator before editing output.
2. Inspect current source, generator, generated output and README/index references.
3. Make the smallest change to source or generator that expresses the intended correction.
4. Regenerate deterministically and inspect the scoped diff.
5. Run the generator audit, link/format checks and any domain test.
6. Record source revision, generated paths, stable rerun result and remaining ambiguity.

Do not hand-edit generated output as the primary fix. Do not claim source/output parity from a successful command if the output diff was not inspected.

## Stop conditions

Stop if the canonical owner is unclear, generated output is unstable between identical runs, or regeneration touches paths outside the task claim.
