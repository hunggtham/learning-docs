# Editorial update handoff: advanced architecture batch 03–04

## Scope

- `task_id`: `editorial-update-cs-architecture-advanced-03-04`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/advanced/README.md`
- `allowed paths`: the two canonical lessons listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and
  other advanced chapters

## Batch completed

1. `computer_science/02_computer_architecture/advanced/03_advanced_cache_hierarchy_prefetching_and_replacement.md`
2. `computer_science/02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md`

The legacy transition blocks were replaced manually. The cache lesson now
connects associativity, hierarchy policy, replacement uncertainty, prefetch
pollution, software layout, coherence/consistency and evidence. The NUMA
lesson now connects topology, first-touch placement, affinity, interconnect,
directory coherence, false sharing, DB/JVM behavior and scale-out. No quiz or
answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-advanced-03-04.md --strict-links`
  - pass: `markdown=2`, `links=5`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- $(cat /tmp/batch-editorial-architecture-advanced-03-04.md)`
  - pass
- Marker and quiz scan over both changed lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, old transition boilerplate,
    quiz, mock-exam, active-recall, or self-check marker

## Live remaining work

The live checkout scan after this batch reports:

- `1020` Markdown files containing `Chuyển mạch`;
- `805` files containing the old transition phrases;
- `3` remaining advanced architecture Markdown files containing `Chuyển mạch`.

Only advanced chapters 05–07 remain in `computer_science/02_computer_architecture`.
The wider `computer_science` and `정보처리기사` corpus remains incomplete.

## Status and limits

- `content_status`: `QA_PASS` for this two-file batch; learner review has not
  been run.
- `git_status`: `UNCOMMITTED` while this handoff is written; becomes
  `COMMITTED` in the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. This checkpoint repairs connector prose only; mixed
  language, source freshness and wider corpus quality remain open.
- `safe_to_merge`: yes for the two listed lessons and this handoff after
  parent-agent review; do not infer corpus-wide completion.

## Next action

Continue advanced chapters 05–07 in the final architecture batch, validate the
whole advanced directory after that batch, and report architecture status before
opening another domain.
