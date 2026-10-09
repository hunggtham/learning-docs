# Editorial update handoff: computer science architecture batch 05–07

## Scope

- `task_id`: `editorial-update-cs-architecture-05-07`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/README.md`
- `allowed paths`: the three canonical lessons listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and the
  rest of the corpus

## Batch completed

1. `computer_science/02_computer_architecture/05_parallel_computer_architecture.md`
2. `computer_science/02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md`
3. `computer_science/02_computer_architecture/07_performance_power_and_hardware_measurement.md`

The legacy `Chuyển mạch` blocks were replaced manually with transitions that
follow the mechanisms in each lesson. The batch now connects pipelining,
multicore, SIMD, GPU, bandwidth and NUMA; storage media, translation, queueing,
alignment, durability and backup; and performance metrics, Amdahl, power,
benchmark conditions and roofline analysis. No quiz or answer-bank content was
added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-05-07.md --strict-links`
  - pass: `markdown=3`, `links=17`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- $(cat /tmp/batch-editorial-architecture-05-07.md)`
  - pass
- Marker and quiz scan over the three changed lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, legacy boilerplate, quiz,
    mock-exam, active-recall, or self-check marker

## Live remaining work

The live checkout scan after this batch reports:

- `1021` Markdown files containing `Chuyển mạch`;
- `810` files containing the old transition phrases;
- `388` `computer_science` Markdown files containing `Chuyển mạch`.

The architecture root lessons 00–07 are now covered by three validated
checkpoints. Advanced architecture lessons and the `computer_science` AI/HCI/
other domain groups still require separate manifests and manual review.

## Status and limits

- `content_status`: `QA_PASS` for this three-file batch; learner review has not
  been run.
- `git_status`: `UNCOMMITTED` while this handoff is written; becomes
  `COMMITTED` in the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. This batch repairs connector prose only; mixed-language
  sentences and domain-wide currentness remain outside this checkpoint.
- `safe_to_merge`: yes for the three listed lessons and this handoff after
  parent-agent review; do not infer corpus-wide completion.

## Next action

Parent agent may integrate the three editorial commits. A future batch can move
to `computer_science/02_computer_architecture/advanced/` or begin
`정보처리기사/output/` after reading its owner README and creating a new
manifest.
