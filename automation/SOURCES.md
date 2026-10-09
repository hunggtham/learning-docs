# Automation — source ledger và tool/version boundary

> **Owner:** `automation/` (repository automation and operational tooling). Ledger này phân biệt workflow contract, tool behavior, generated artifact và local environment.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| AUTO-GH-01 | GitHub Actions documentation | workflow syntax, permissions, runners, artifacts và expressions | https://docs.github.com/en/actions | docs live; action/runner version phải ghi | Marketplace action, runner image và permission defaults có thể đổi; pin/version và log run cụ thể | `.github/workflows/`, automation scripts |
| AUTO-GIT-01 | Git project documentation | Git object, worktree, diff, hooks và transport semantics | https://git-scm.com/docs | Git version phải ghi khi behavior versioned | Local config, filesystem, hooks và remote policy ảnh hưởng result; command success không chứng minh publication | Git workflows |
| AUTO-PY-01 | Python documentation | language/stdlib behavior của supported Python version | https://docs.python.org/3/ | Python minor version phải ghi | Package/dependency behavior không nằm hết trong stdlib docs; lock environment và test output | Python scripts |
| AUTO-NODE-01 | Node.js documentation | Node runtime/API behavior | https://nodejs.org/docs/latest/api/ | Node major/minor phải ghi | Runtime flags, package manager và OS environment ảnh hưởng behavior; ghi lockfile/engine | JS scripts/build |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| AUTO-ENV-01 | `NEEDS_SOURCE` | “Script chạy được” cần OS, runtime, dependency lock, cwd, env và exit/log evidence; không suy từ source code. | Owner script + CI |
| AUTO-CI-01 | `REVIEW_REQUIRED` | Green CI chỉ chứng minh job/path/test đã chạy trong context đó; không chứng minh live provider, browser hoặc external service. | Owner workflow |
| AUTO-GENERATED-01 | `REVIEW_REQUIRED` | Generated artifact phải truy ngược generator/input/version; copied output không phải source of truth. | Owner generator + publication |
| AUTO-DESTRUCTIVE-01 | `NEEDS_SOURCE` | Command thay đổi Git/filesystem/external state cần scope, dry-run, backup/rollback và authorization evidence. | Owner operational runbook |

## Quy trình refresh

1. Ghi runtime/tool/action version, lockfile, OS, working directory và relevant environment.
2. Lưu log/exit status và phân biệt code validation với external/publication acceptance.
3. Khi action/runner/runtime/dependency đổi, chạy lại scoped tests và inspect diff/artifact.
4. Không dùng CI green hoặc copied/generated file làm bằng chứng cho live state nếu chưa kiểm tra boundary tương ứng.
