# Linux — source ledger và distro/version boundary

> **Owner:** `linux/` (canonical Linux learning content). Ledger này phân biệt kernel ABI/behavior, POSIX/Unix contract, user-space tool và distro configuration.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| LNX-KERNEL-01 | Linux kernel documentation | kernel interfaces, scheduler, memory, networking, tracing và subsystem behavior | https://docs.kernel.org/ | docs live; kernel release/config phải ghi khi claim versioned | Không suy behavior của một kernel/config sang mọi distro; ghi release, architecture và config khi cần | foundations/process/memory/network |
| LNX-POSIX-01 | The Open Group — POSIX Base Specifications | portable shell, filesystem, process và API contract | https://pubs.opengroup.org/onlinepubs/9699919799/ | POSIX.1-2017; kiểm tra 2026-10-09 | POSIX không bao phủ Linux-specific behavior; tách standard contract khỏi extension | shell/filesystem/portable tooling |
| LNX-GNU-01 | GNU Project manuals | Bash, coreutils và GNU user-space semantics | https://www.gnu.org/manual/manual.html | manual/version riêng | Ghi command/package version; flags/defaults có thể đổi và distro patch có thể khác | shell/CLI |
| LNX-SYSTEMD-01 | systemd project documentation | systemd units, boot, service manager, logging và resource controls | https://systemd.io/ | docs live; systemd release phải ghi cho behavior | Không coi systemd là Linux kernel hoặc universal init; distro preset/config có thể override | identity/process/operations |
| LNX-DEBIAN-01 | Debian documentation | distro packaging, release policy và administrator behavior của Debian | https://www.debian.org/doc/ | release-specific docs; kiểm tra 2026-10-09 | Chỉ dùng cho Debian release đã ghi; không suy ra RHEL/Arch defaults | production/distro examples |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| LNX-VERSION-01 | `NEEDS_SOURCE` | Claim về default, path, unit, package hoặc syscall phải ghi kernel/distro/user-space version; “Linux” không đủ specificity. | Owner chapter tương ứng |
| LNX-PERF-01 | `NEEDS_SOURCE` | Throughput, latency, memory và scheduler result cần hardware, kernel config, workload và measurement window. | Owner production/performance |
| LNX-SECURITY-01 | `REVIEW_REQUIRED` | Security posture phụ thuộc threat model, distro patch, config và update state; không gọi một setting là hardening phổ quát. | Owner security chapter |
| LNX-COMMAND-01 | `REVIEW_REQUIRED` | Command example phải nêu side effect, privilege, destructive risk và portability; không dùng output một máy làm invariant. | Owner shell/operations |

## Quy trình refresh

1. Ghi release, architecture, distro và config trong lesson/lab khi behavior không phải invariant.
2. Tách POSIX contract, kernel implementation và user-space/distro policy; link owner tương ứng.
3. Re-run command/lab sau kernel, systemd, Bash hoặc distro release thay đổi; ghi expected-vs-observed output.
4. Giữ `NEEDS_SOURCE` nếu claim performance/security/current default chưa có điều kiện và evidence.
