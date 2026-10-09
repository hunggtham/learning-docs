# Editorial update handoff: 정보처리기사 Môn 1 lesson batch 12/13/16

## Scope

- `task_id`: `editorial-update-information-processing-subject01-lessons-12-13-16`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/finish-editorial`
- `branch`: `codex/finish-editorial`
- `base_sha`: `92fcb49e`
- `canonical_owner`: `정보처리기사/output/01-software-design/README.md`
- `allowed_paths`: the three lessons below and this handoff
- `non_goals`: Planner/archive, raw/raw_md, provenance registers, publication files,
  generated site, README owner files, and other subjects

## Batch completed

- `정보처리기사/output/01-software-design/lessons/12-bai-hoc.md`
- `정보처리기사/output/01-software-design/lessons/13-bai-hoc.md`
- `정보처리기사/output/01-software-design/lessons/16-bai-hoc.md`

The legacy transition blocks were replaced manually with lesson-specific prose
for current-system analysis, current-system understanding and UML. Each handoff
now names the dependency or evidence relationship relevant to the next topic.
No quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-kiip-subject01-lessons-12-13-16.md --strict-links`
  - pass: 3 Markdown files, 6 links, 0 errors, 0 warnings
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: 6/6
- `git diff --check -- $(cat /tmp/batch-editorial-kiip-subject01-lessons-12-13-16.md)`
  - pass
- marker/quiz scan over the three lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, quiz, mock-exam,
    active-recall, or self-check marker

## Status and limits

- `content_status`: `QA_PASS` for connector prose; learner review and
  source-freshness review remain open.
- `git_status`: `COMMITTED` after the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. Môn 1 still has 20 lesson files with transition
  blocks; this checkpoint does not certify subject completion.

## Next action

Continue Môn 1 in another 3-file lesson batch, preserving owner and adjacent
lesson boundaries.
