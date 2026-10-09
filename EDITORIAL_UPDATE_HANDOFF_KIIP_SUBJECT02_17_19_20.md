# Editorial update handoff: 정보처리기사 Môn 2 lesson batch 17/19/20

## Scope

- `task_id`: `editorial-update-information-processing-subject02-lessons-17-19-20`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/finish-editorial`
- `branch`: `codex/finish-editorial`
- `base_sha`: `4ff927f6`
- `canonical_owner`: `정보처리기사/output/02-software-development/README.md`
- `allowed_paths`: the three lessons below and this handoff
- `non_goals`: Planner/archive, raw/raw_md, provenance registers, publication files,
  generated site, README owner files, and other subjects

## Batch completed

- `정보처리기사/output/02-software-development/lessons/17-bai-hoc.md`
- `정보처리기사/output/02-software-development/lessons/19-bai-hoc.md`
- `정보처리기사/output/02-software-development/lessons/20-bai-hoc.md`

The legacy transition blocks were replaced manually with lesson-specific prose
for insertion, selection, and bubble sort. The prose keeps each algorithm's
invariant, operation, and cost visible, then hands off to the next sorting
comparison. No quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-kiip-subject02-lessons-17-19-20.md --strict-links`
  - pass: 3 Markdown files, 6 links, 0 errors, 0 warnings
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: 6/6
- `git diff --check -- $(cat /tmp/batch-editorial-kiip-subject02-lessons-17-19-20.md)`
  - pass
- marker/quiz scan over the three lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, quiz, mock-exam,
    active-recall, or self-check marker

## Status and limits

- `content_status`: `QA_PASS` for connector prose; learner review and
  source-freshness review remain open.
- `git_status`: `COMMITTED` after the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. Subject 2 still has 74 files and 394 transition
  blocks; the remaining exact legacy scope includes lessons 18, 21 onward.

## Next action

Continue subject 2 in another 3-file batch, preserving owner and lesson order.
