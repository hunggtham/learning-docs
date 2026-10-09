# Editorial update handoff: computer science architecture batch 03–04

## Scope

- `task_id`: `editorial-update-cs-architecture-03-04`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/README.md`
- `allowed paths`: the two canonical lessons listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and the
  rest of the corpus

## Batch completed

1. `computer_science/02_computer_architecture/03_io_interrupts_dma_and_devices.md`
2. `computer_science/02_computer_architecture/04_machine_code_assembly_and_abi.md`

The legacy `Chuyển mạch` blocks were replaced manually with transitions tied to
the actual mechanism chain. The I/O lesson now connects controller state to
polling/interrupt, DMA, memory ordering, buffering and queue depth. The ABI
lesson now connects instruction representation to calling convention, stack
layout, linking, binary contracts, syscalls and debug symbols. No quiz or
answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-03-04.md --strict-links`
  - pass: `markdown=2`, `links=12`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- $(cat /tmp/batch-editorial-architecture-03-04.md)`
  - pass
- Marker and quiz scan over the two changed lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, legacy boilerplate, quiz,
    mock-exam, active-recall, or self-check marker

## Live remaining work

The live checkout scan after this batch reports:

- `1023` Markdown files containing `Chuyển mạch`;
- `813` files containing the old transition phrases;
- `391` `computer_science` Markdown files containing `Chuyển mạch`.

These are scan counts, not acceptance claims. The remaining files require the
same manual review against their domain README and adjacent sections.

## Status and limits

- `content_status`: `QA_PASS` for this two-file batch; learner review has not
  been run.
- `git_status`: `UNCOMMITTED` while this handoff is written; becomes
  `COMMITTED` in the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. This batch only repairs transitions and does not
  normalize the mixed-language prose elsewhere in either lesson.
- `safe_to_merge`: yes for the two listed lessons and this handoff after
  parent-agent review; do not infer corpus-wide completion.

## Next action

Continue with the next small architecture batch, then begin the
`정보처리기사` output lessons only after confirming their canonical owner and
source boundary.
