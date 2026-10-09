# Editorial update handoff: HCI/Graphics foundation batch 03–04

## Scope

- `task_id`: `editorial-update-cs-hci-graphics-foundation-03-04`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/finish-editorial`
- `branch`: `codex/finish-editorial`
- `base_sha`: `cc6218bd`
- `canonical_owner`: `computer_science/11_hci_graphics/README.md`
- `allowed_paths`: the two lessons below and this handoff
- `non_goals`: Planner/archive, provenance ledgers, publication files, generated site,
  and other domains

## Batch completed

- `computer_science/11_hci_graphics/03_images_color_rasterization_and_rendering.md`
- `computer_science/11_hci_graphics/04_multimedia_animation_and_interactive_systems.md`

The legacy `Chuyển mạch` blocks were replaced manually with topic-specific
handoffs. The prose now connects sampling to color encoding and compositing,
texture to lighting and rendering strategy, and frame deadlines to buffering,
input latency, A/V synchronization, compression dependencies and real-time
semantics. No quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-cs-hci-foundation-03-04.md --strict-links`
  - pass: 2 Markdown files, 11 links, 0 errors, 0 warnings
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: 6/6
- `git diff --check -- $(cat /tmp/batch-editorial-cs-hci-foundation-03-04.md)`
  - pass
- marker/quiz scan over the two lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, old transition boilerplate,
    quiz, mock-exam, active-recall, or self-check marker

## Status and limits

- `content_status`: `QA_PASS` for connector prose; learner review and
  source-freshness review remain open.
- `git_status`: `COMMITTED` after the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. Existing mixed-language sentences remain outside
  the connector edits; this does not certify corpus-wide prose quality.
- Live scope after this batch: all 8 HCI/Graphics foundation and advanced
  lessons in this owner are free of `Chuyển mạch`.

## Next action

Continue with the next explicitly owned computer-science scope. The remaining
legacy marker burden is outside HCI/Graphics and must be handled in bounded
owner-specific batches.
