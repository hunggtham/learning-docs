# Editorial update handoff: advanced architecture batch 01

## Scope

- `task_id`: `editorial-update-cs-architecture-advanced-01`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/advanced/README.md`
- `allowed paths`: the canonical lesson listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and
  other advanced chapters

## Batch completed

- `computer_science/02_computer_architecture/advanced/01_out_of_order_execution_register_renaming_and_rob.md`

All legacy transition blocks in this chapter were replaced manually. The new
prose follows program/execution/retirement order, µops, true dependencies,
renaming, physical-register lifetime, scheduling, ROB, precise exceptions,
memory disambiguation, store buffers, branch recovery, pointer chasing,
resource pressure, production evidence and the correctness/security boundary.
No quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-advanced-01.md --strict-links`
  - pass: `markdown=1`, `links=7`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- $(cat /tmp/batch-editorial-architecture-advanced-01.md)`
  - pass
- Marker and quiz scan over the changed lesson
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, old transition boilerplate,
    quiz, mock-exam, active-recall, or self-check marker

## Live remaining work

The live checkout scan after this batch reports:

- `1021` Markdown files containing `Chuyển mạch`;
- `808` files containing the old transition phrases;
- `6` remaining advanced architecture Markdown files containing `Chuyển mạch`.

Advanced chapters 02–07 and the wider `computer_science`/`정보처리기사` corpus
remain incomplete.

## Status and limits

- `content_status`: `QA_PASS` for this one-file batch; learner review has not
  been run.
- `git_status`: `UNCOMMITTED` while this handoff is written; becomes
  `COMMITTED` in the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. This checkpoint repairs connector prose only; mixed
  language, source freshness and wider corpus quality remain open.
- `safe_to_merge`: yes for the listed lesson and this handoff after parent-agent
  review; do not infer corpus-wide completion.

## Next action

Continue advanced chapter 02 in a new manifest, then review 03–07 in additional
small batches if validation remains clean.
