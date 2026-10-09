# Editorial update handoff: computer science architecture batch 00–02

## Scope

- `task_id`: `editorial-update-cs-architecture-00-02`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/README.md`
- `allowed paths`: three canonical lessons listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and the
  rest of the corpus

## Batch completed

1. `computer_science/02_computer_architecture/00_digital_logic_and_circuits.md`
2. `computer_science/02_computer_architecture/01_cpu_isa_and_instruction_cycle.md`
3. `computer_science/02_computer_architecture/02_memory_hierarchy_and_cache.md`

The legacy `Chuyển mạch` blocks were replaced manually with short,
topic-specific Vietnamese transitions. Each transition now names the mechanism
that connects adjacent sections: state and timing, datapath and memory, ISA and
microarchitecture, cache mapping and miss cost, coherence and false sharing,
and locality and prefetching. No quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-00-02.md --strict-links`
  - pass: `markdown=3`, `links=18`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- computer_science/02_computer_architecture/00_digital_logic_and_circuits.md computer_science/02_computer_architecture/01_cpu_isa_and_instruction_cycle.md computer_science/02_computer_architecture/02_memory_hierarchy_and_cache.md`
  - pass
- Marker and quiz scan over the three changed lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, legacy boilerplate, quiz,
    mock-exam, active-recall, or self-check marker

## Live remaining work

The live checkout scan after this batch still reports:

- `1024` Markdown files containing `Chuyển mạch`;
- `815` files containing the old transition phrases;
- `393` `computer_science` Markdown files containing `Chuyển mạch`;
- `271` `정보처리기사` Markdown files containing `Chuyển mạch`.

These are scan counts, not acceptance claims. They require manual, small-batch
review against each domain README and adjacent sections.

## Status and limits

- `content_status`: `QA_PASS` for this three-file batch; learner review has not
  been run.
- `git_status`: `COMMITTED` after the checkpoint commit below.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. The surrounding corpus still contains legacy
  connectors and mixed-language prose. This batch intentionally did not rewrite
  unrelated sentences or normalize terminology across the chapter.
- `safe_to_merge`: yes for the three listed lessons and this handoff after
  parent-agent review; do not infer corpus-wide completion.

## Next action

Continue with the next small `computer_science` batch, beginning with the next
architecture lessons, and rerun the same scoped audit before each checkpoint.
