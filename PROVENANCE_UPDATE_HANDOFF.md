# Provenance/currentness update handoff

## Status

`MERGE_READY` for the scoped provenance update. Branch: `codex/finish-provenance`.

- Base: `68c6ee09d9327a82f7eba29fa0d6d51c75698b88`
- Commits: `b71533de`, `9b528464`, `da478237`, `45c980af`
- HEAD: `45c980af`
- Worktree: clean
- Scope: canonical domain `SOURCES.md` ledgers and README/index discoverability links only
- Explicitly not changed: Planner, connector prose, publication workflow, generated site and unrelated dirty paths

## Coverage

All 29 canonical catalog domains now have a `SOURCES.md` ledger. The ledgers define:

- owner and allowed claim type;
- authority/source URL and version/date boundary;
- currentness boundary;
- explicit `NEEDS_SOURCE` and `REVIEW_REQUIRED` gaps;
- refresh procedure and evidence limits.

The remaining catalog paths without a ledger are supporting/non-canonical (`planner/`, `learning-library/`, `dev_everyday/`, `99.template_folder/`) and were intentionally left unchanged.

## Validation

- Each batch: `python3 automation/repo_audit.py --files-from ... --strict-links` — pass, `errors=0`, `warnings=0`.
- Each batch: `git diff --check` — pass.
- Repository unit audit: `python3 -m unittest automation/test_repo_audit.py` — `6/6` pass.
- Whole-repository strict audit: 123 pre-existing errors, concentrated in raw `정보처리기사/raw_md/merged_subjects/` links; these are outside this scoped provenance change.

## Review boundary

This handoff establishes source routing and currentness policy. It does not prove that every chapter claim is correctly cited, prose is publication-ready, data is live, or a provider/runtime behaves as documented. Domain owners must resolve the ledger gaps before treating affected claims as accepted.
