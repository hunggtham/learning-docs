# Editorial update handoff: advanced architecture batch 02

## Scope

- `task_id`: `editorial-update-cs-architecture-advanced-02`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/advanced/README.md`
- `allowed paths`: the canonical lesson listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and
  other advanced chapters

## Batch completed

- `computer_science/02_computer_architecture/advanced/02_branch_prediction_speculation_and_pipeline_recovery.md`

All legacy transition blocks in this chapter were replaced manually. The new
prose follows control dependency, predictor state and aliasing, speculation,
misprediction recovery, branchless trade-offs, cache/TLB side effects, indirect
targets, front-end bandwidth and the Spectre security boundary. No quiz or
answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-advanced-02.md --strict-links`
  - pass: `markdown=1`, `links=3`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- $(cat /tmp/batch-editorial-architecture-advanced-02.md)`
  - pass
- Marker and quiz scan over the changed lesson
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, old transition boilerplate,
    quiz, mock-exam, active-recall, or self-check marker

## Live remaining work

The live checkout scan after this batch reports:

- `1021` Markdown files containing `Chuyển mạch`;
- `807` files containing the old transition phrases;
- `5` remaining advanced architecture Markdown files containing `Chuyển mạch`.

Advanced chapters 03–07 and the wider `computer_science`/`정보처리기사` corpus
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

Continue advanced chapters 03–04 in a new manifest, then 05–07 if validation
remains clean.
