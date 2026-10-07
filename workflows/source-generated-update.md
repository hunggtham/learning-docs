# Workflow: source-generated update

Use for corpora whose output Markdown, catalog or index is produced from a source or generator.

1. Claim the source, generator and generated output as one GENERATED_DEPENDENCY scope.
2. Inspect current source, generator, output and README/index ownership.
3. Change the canonical source or generator only.
4. Regenerate in a clean, repeatable run.
5. Compare the scoped output diff and detect unrelated changes.
6. Run generator, link, format and domain audits.
7. Re-run generation without edits and confirm a stable result.
8. Write a handoff with source revision, generated paths, commands/results and remaining currentness limits.

Do not hand-edit generated output as the primary change and do not stage unrelated generated files.
