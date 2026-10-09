# Editorial update handoff: HCI/Graphics foundation batch 00–02

## Scope

- `task_id`: `editorial-update-cs-hci-graphics-foundation-00-02`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/finish-editorial`
- `branch`: `codex/finish-editorial`
- `base_sha`: `0b6cd163`
- `canonical_owner`: `computer_science/11_hci_graphics/README.md`
- `allowed_paths`: the three lessons below and this handoff
- `non_goals`: Planner/archive, provenance ledgers, publication files, generated site,
  advanced chapters, and other domains

## Batch completed

- `computer_science/11_hci_graphics/00_hci_human_factors_and_interaction_models.md`
- `computer_science/11_hci_graphics/01_interface_design_accessibility_and_usability.md`
- `computer_science/11_hci_graphics/02_computer_graphics_pipeline_and_geometry.md`

The legacy `Chuyển mạch` blocks were replaced manually with topic-specific
handoffs. The prose now makes explicit the relationships among mental models,
feedback, cognitive cost, usability testing, accessibility, coordinate spaces,
projection, clipping, rasterization, shading and visibility. No quiz or
answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-cs-hci-foundation-00-02.md --strict-links`
  - pass: 3 Markdown files, 11 links, 0 errors, 0 warnings
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: 6/6
- `git diff --check -- $(cat /tmp/batch-editorial-cs-hci-foundation-00-02.md)`
  - pass
- marker/quiz scan over the three lessons
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
  lessons in this owner are free of `Chuyển mạch`; 0 HCI/Graphics owner files
  remain with that marker.

## Next action

Continue with the next explicitly owned computer-science scope, beginning with
the remaining HCI/Graphics files only if a full-language cleanup is authorized;
otherwise prioritize the next domain with a clear owner and small batch boundary.
