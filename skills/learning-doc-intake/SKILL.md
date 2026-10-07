---
name: learning-doc-intake
description: Create a bounded task manifest and source boundary before writing or converting learning documents.
metadata:
  short-description: Scope a learning-doc task safely
---

# Learning document intake

Use this skill before authoring, converting, auditing, or repairing a learning-document corpus.

## Outcome

Produce a task manifest that makes ownership, scope, source state, allowed paths, dependencies, acceptance evidence and stop conditions explicit. Do not write canonical learning prose in this mode.

## Procedure

1. Inspect the current branch/worktree, status, README/canonical map and existing prompt contract.
2. Resolve the corpus root and identify raw/, research/, planning/, output/ and audit/ paths. Do not assume a directory exists from its name alone.
3. Register every source in SOURCE_MANIFEST.yaml; preserve original files and record extraction/OCR provenance.
4. Create or update a task manifest using templates/TASK_MANIFEST.yaml.
5. Set allowed_paths narrowly. Mark shared prompts, indexes, generators and generated outputs as conflict-sensitive.
6. State the next mode (INGEST, PLAN, PILOT, or REVIEW) and the exact evidence required to leave intake.

## Stop conditions

Stop with INTAKE_REQUIRED if owner, audience, source boundary, base revision or acceptance test is missing. Do not invent a scope or remove unrelated dirty changes.

## Handoff

Return the task id, resolved corpus root, source count, allowed paths, dependencies, current Git status and next action. Separate content status from Git and publication status.
