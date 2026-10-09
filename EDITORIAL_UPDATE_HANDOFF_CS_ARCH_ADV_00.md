# Editorial update handoff: advanced architecture batch 00

## Scope

- `task_id`: `editorial-update-cs-architecture-advanced-00`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/advanced/README.md`
- `allowed paths`: the canonical lesson listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and
  other advanced chapters

## Batch completed

- `computer_science/02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md`

All 18 legacy `Chuyển mạch` blocks in this chapter were replaced manually.
The new prose follows the actual mechanism chain: coherence versus consistency,
store-buffer visibility, message-passing edges, invalidate queues, fences,
compiler/CPU reordering, happens-before, atomicity, false sharing, lifetime,
NUMA placement, production evidence and cross-layer ownership. No quiz or
answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-advanced-00.md --strict-links`
  - pass: `markdown=1`, `links=10`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- $(cat /tmp/batch-editorial-architecture-advanced-00.md)`
  - pass
- Marker and quiz scan over the changed lesson
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, old transition boilerplate,
    quiz, mock-exam, active-recall, or self-check marker

## Live remaining work

The live checkout scan after this batch reports:

- `1021` Markdown files containing `Chuyển mạch`;
- `809` files containing the old transition phrases;
- `7` remaining advanced architecture Markdown files containing `Chuyển mạch`.

The other advanced chapters 01–07 need separate manifests and manual review.
The `computer_science` and `정보처리기사` corpus remains incomplete.

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

Continue advanced chapters 01–02 in a new small manifest, then 03–04 and 05–07
if validation remains clean. Do not treat this checkpoint as completion of the
advanced track.
