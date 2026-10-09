# Editorial update handoff: advanced architecture batch 07

## Scope

- `task_id`: `editorial-update-cs-architecture-advanced-07`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/update-editorial`
- `branch`: `codex/update-editorial`
- `canonical owner`: `computer_science/02_computer_architecture/advanced/README.md`
- `allowed paths`: the canonical lesson listed below and this handoff
- `non-goals`: Planner/archive, CATALOG, source ledgers, generated site, and
  other domains

## Batch completed

- `computer_science/02_computer_architecture/advanced/07_power_thermal_dvfs_and_sustained_performance.md`

The legacy transition blocks were replaced manually. The new prose connects
dynamic power, DVFS operating points, boost headroom, thermal inertia,
throttling, race-to-idle, memory-bound work, heterogeneous scheduling,
datacenter capacity, failure modes, production evidence and controlled
experiments. No quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-architecture-advanced-07.md --strict-links`
  - pass: `markdown=1`, `links=6`, `errors=0`, `warnings=0`
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: `6/6`
- `git diff --check -- $(cat /tmp/batch-editorial-architecture-advanced-07.md)`
  - pass
- Marker and quiz scan over the changed lesson
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, old transition boilerplate,
    quiz, mock-exam, active-recall, or self-check marker

## Architecture scope audit

After this batch, live scan over `computer_science/02_computer_architecture`
reports zero files containing `Chuyển mạch`. Both foundation lessons 00–07 and
advanced lessons 00–07 have been handled in separate validated checkpoints.

Repository-wide scan still reports:

- `1020` Markdown files containing `Chuyển mạch`;
- `802` files containing the old transition phrases.

Those remaining files are outside this architecture scope and require their own
owner README and batch manifests.

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

Parent agent should integrate the architecture editorial commits, then choose a
new domain owner before opening another corpus batch. Architecture itself is
clean for the `Chuyển mạch` marker, not globally learner-reviewed.
