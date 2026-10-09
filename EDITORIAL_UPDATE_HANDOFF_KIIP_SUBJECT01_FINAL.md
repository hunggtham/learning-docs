# Editorial update handoff: thông tin xử lý Môn 1 final batch

## Scope

- `task_id`: `editorial-update-information-processing-subject01-final`
- `agent_surface`: Codex
- `worktree`: `/Users/mac/00.my-learning-worktrees/finish-editorial`
- `branch`: `codex/finish-editorial`
- `base_sha`: `78c1eefb`
- `canonical_owner`: `정보처리기사/output/01-software-design/README.md`
- `allowed_paths`: the five files below and this handoff
- `non_goals`: Planner/archive, raw/raw_md, provenance registers, publication files,
  generated site, README owner files, and other subjects

## Batch completed

- `정보처리기사/output/01-software-design/01-vong-doi-va-phuong-phap-phat-trien.md`
- `정보처리기사/output/01-software-design/lessons/63-bai-hoc.md`
- `정보처리기사/output/01-software-design/lessons/64-bai-hoc.md`
- `정보처리기사/output/01-software-design/lessons/65-bai-hoc.md`
- `정보처리기사/output/01-software-design/lessons/68-bai-hoc.md`

The remaining legacy transition blocks in subject 1 were replaced manually.
The deep-dive lifecycle file now connects Waterfall → Spiral → Agile → Scrum
→ XP by mechanism and feedback; lessons 63/64/65/68 connect design principles,
coupling, cohesion and reuse to change cost and ownership. No quiz or answer-bank
content was added.

## Validation

- `python3 automation/repo_audit.py --files-from /tmp/batch-editorial-kiip-subject01-final-01-63-64-65-68.md --strict-links`
  - pass: 5 Markdown files, 10 links, 0 errors, 0 warnings
- `python3 -m unittest automation/test_repo_audit.py`
  - pass: 6/6
- `git diff --check -- $(cat /tmp/batch-editorial-kiip-subject01-final-01-63-64-65-68.md)`
  - pass
- marker/quiz scan over all five files
  - pass: no `Chuyển mạch`, malformed `Nối mạch`, quiz, mock-exam,
    active-recall, or self-check marker

## Status and limits

- `content_status`: `QA_PASS` for connector prose; learner review and
  source-freshness review remain open.
- `git_status`: `COMMITTED` after the checkpoint commit.
- `publication_status`: `NOT_PUBLISHED`.
- `REVIEW_REQUIRED`: subject-level audit follows this commit; do not infer
  whole `정보처리기사/output` completion.

## Next action

Run the exact owner scan to confirm Môn 1 has zero transition blocks, then
continue with subject 2 in new bounded batches.
