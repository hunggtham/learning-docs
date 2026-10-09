# Editorial update handoff: 정보처리기사 Môn 2 lesson batch 93/95/96

## Scope

- `task_id`: `editorial-update-information-processing-subject02-lessons-93-95-96`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/resume-editorial`
- `branch`: `codex/resume-editorial`
- `base_sha`: `bd680e98`
- `canonical_owner`: `정보처리기사/output/02-software-development/README.md`
- `allowed_paths`: the three lessons below and this handoff
- `non_goals`: Planner/archive, raw/raw_md, provenance registers, publication files,
  generated site, README owner files, and other subjects

## Batch completed

- `정보처리기사/output/02-software-development/lessons/93-bai-hoc.md`
- `정보처리기사/output/02-software-development/lessons/95-bai-hoc.md`
- `정보처리기사/output/02-software-development/lessons/96-bai-hoc.md`

The legacy transition blocks were replaced manually with lesson-specific prose
for database/DBMS, schema layers, and procedural SQL. The edits keep the
learner-facing sequence tied to data versus management responsibilities,
schema boundaries, control flow, events, and controlled testing. Existing
technical notes were preserved; no quiz or answer-bank content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-kiip-subject02-lessons-93-95-96.md --strict-links`
  - pass: 3 Markdown files, 6 links, 0 errors, 0 warnings
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: 6/6
- `git diff --check -- $(cat /tmp/batch-editorial-kiip-subject02-lessons-93-95-96.md)`
  - pass
- marker/quiz scan over the three lessons
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, quiz, mock-exam,
    active-recall, or self-check marker

## Status and limits

- `content_status`: `QA_PASS` for connector prose; learner review and
  source-freshness review remain open.
- `git_status`: `COMMITTED` after the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: yes. Subject 2 now has 4 files and 16 exact legacy
  transition blocks; remaining files are lessons 13, 97, 98, and 101.

## Next action

Continue subject 2 in another 3-file batch, then close the final remaining
lesson and run a subject-wide marker/link audit before considering subject 2
complete.
