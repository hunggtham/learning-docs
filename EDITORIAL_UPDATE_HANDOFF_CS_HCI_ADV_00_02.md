# Editorial update handoff: HCI/Graphics advanced batch 00–02

## Scope

- `task_id`: `editorial-update-cs-hci-graphics-advanced-00-02`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/finish-editorial`
- `branch`: `codex/finish-editorial`
- `base_sha`: `68c6ee09d9327a82f7eba29fa0d6d51c75698b88`
- `canonical_owner`: `computer_science/11_hci_graphics/README.md`
- `allowed_paths`: the three lessons below and this handoff
- `non_goals`: Planner/archive, provenance ledgers, publication files, generated site,
  and other HCI/Graphics chapters

## Batch completed

- `computer_science/11_hci_graphics/advanced/00_frame_pipeline_gpu_synchronization_and_frame_budget.md`
- `computer_science/11_hci_graphics/advanced/01_gpu_pipeline_command_buffers_and_resource_barriers.md`
- `computer_science/11_hci_graphics/advanced/02_pbr_brdf_lighting_and_material_models.md`

The legacy `Chuyển mạch` blocks were replaced manually with topic-specific prose.
The new handoffs connect CPU/GPU timelines to dependency visibility, barriers to
resource state and queue coordination, and rendering equation to BRDF/material
parameters and display color. No quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-cs-hci-adv-00-02.md --strict-links`
  - pass: 3 Markdown files, 9 links, 0 errors, 0 warnings
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: 6/6
- `git diff --check -- $(cat /tmp/batch-editorial-cs-hci-adv-00-02.md)`
  - pass
- marker/quiz scan over the three lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, old transition boilerplate,
    quiz, mock-exam, active-recall, or self-check marker

## Status and limits

- `content_status`: `QA_PASS` for connector prose in these three lessons;
  learner review and source-freshness review remain open.
- `git_status`: `COMMITTED` after the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. Mixed Vietnamese/English prose and broader corpus
  legacy markers remain; this is not corpus-wide completion.
- Live scope after this batch: HCI/Graphics advanced still has 0 legacy
  `Chuyển mạch` markers in the three changed files, but 5 foundation and 3
  other advanced files remain in this owner with legacy markers.

## Next action

Review the remaining HCI/Graphics foundation chapters in a separate 3–5-file
batch, then continue to the next explicitly owned computer-science scope.
