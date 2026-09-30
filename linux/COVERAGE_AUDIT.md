# Linux — kiểm toán phạm vi và độ sâu

> **Mạch đọc:** Đọc tệp này sau [`README.md`](./README.md). README giải thích Linux như một hệ thống cơ chế; audit này trả lời: **những lớp nào đã đủ mạnh, ranh giới nào cần giữ với Computer Science/Backend/DevOps, và các deep dive hiện có nên được nối lại thành reasoning production như thế nào?**

**Ngày rà soát:** 2026-09-29.

## 1. Phạm vi sở hữu

`linux/` sở hữu lớp hệ điều hành/thời gian chạy của máy chủ: ranh giới hạt nhân–không gian người dùng (kernel/userspace boundary / 커널·사용자 공간 경계), hệ thống tệp (filesystem / 파일시스템), tiến trình và luồng (process/thread / 프로세스·스레드), identity/permission, shell, `systemd`, logging, thời gian, CPU/bộ nhớ/lưu trữ, mạng, package/runtime provenance, tracing, container primitives và xử lý sự cố production.

Mục tiêu của domain không phải học thuộc lệnh. Một command chỉ là **công cụ quan sát hoặc tác động lên trạng thái**. Khái niệm thật nằm ở object/resource nào đang tồn tại, kernel đang giữ trạng thái gì, accounting/limit nào đang áp dụng, failure xuất hiện ra sao và bằng chứng nào xác nhận giả thuyết.

Lý thuyết hệ điều hành và distributed systems sâu hơn thuộc [Computer Science](../computer_science/README.md); contract của ứng dụng thuộc [Backend](../10_backend/README.md); Kubernetes, delivery, SRE và platform operations thuộc [DevOps / Platform Engineering](../devops_platform_engineering/README.md).

## 2. Coverage hiện đã mạnh

README hiện có dependency graph rộng và hợp lý: kernel/userspace, `/proc`/`/sys`, filesystem–VFS–page cache–writeback, process/thread/signal/IPC, Bash đáng tin cậy, credential/capability/ACL/MAC, boot/initramfs/systemd, journald/rsyslog, clock/NTP, storage/memory/reclaim/OOM, scheduler/I/O, routing/NAT/conntrack/DNS/TCP/TLS, `strace`/`perf`/eBPF, namespace/cgroup/seccomp/container, deployment/backup/restore và incident/SRE.

Điểm mạnh của thư viện là nhiều chapter đã đi tới cơ chế chứ không dừng ở syntax. Vì vậy vòng nâng cấp tiếp theo nên **nối các deep dive thành đường suy luận xuyên tài nguyên**, thay vì tiếp tục thêm chapter lệnh rời rạc.

## 3. Bất biến khi viết Linux

Một topic Linux nên tạo được chuỗi:

```text
resource/object
→ kernel state
→ user-space interface
→ accounting/limit
→ observable evidence
→ failure mode
→ recovery/change action
```

Ví dụ, “memory pressure” không đồng nghĩa với một con số `free`. Cần nối working set, page cache, reclaim, cgroup limit và PSI tới latency/OOM. Khi người học hiểu chuỗi đó, `free`, `/proc`, `vmstat`, PSI hay cgroup counters mới có nghĩa; nếu học command trước, rất dễ diễn giải sai bằng chứng.

## 4. Ranh giới dễ nhầm

### Linux networking và network theory

Linux sở hữu socket, routing table, namespace, conntrack, host-level TCP state và packet-path evidence. Thiết kế protocol và distributed-system theory vẫn thuộc Computer Science.

### Container primitives và orchestration

Linux sở hữu namespace, cgroup, capability và seccomp. Scheduler, controller, GitOps và cluster operations thuộc DevOps/Platform Engineering.

### Host troubleshooting và application debugging

Linux xác định trạng thái host/process/resource. Backend xác định transaction, business invariant và application semantics. Một CPU spike có thể là bằng chứng, nhưng không tự cho biết request nào vi phạm business invariant.

### Security enforcement và security architecture

Linux giải thích cơ chế enforcement cục bộ. Threat model, identity architecture và control/evidence chain xuyên hệ thống thuộc Computer Science Security.

## 5. Khoảng trống ưu tiên

### P1 — Tuyến overload xuyên nhiều tài nguyên

Cần một case nối:

```text
traffic tăng
→ socket/backlog
→ process/thread/event-loop pressure
→ CPU scheduling
→ memory/page cache/reclaim
→ storage/network I/O
→ cgroup limit
→ latency/error
→ evidence
→ recovery
```

Giá trị của case này là dạy **quan hệ nhân quả giữa các counter**. Nếu từng chapter CPU/memory/network được đọc tách rời, người học dễ tối ưu sai bottleneck.

### P1 — Ranh giới durability giữa filesystem và database

Cần làm rõ đường:

```text
application write
→ userspace buffer
→ page cache
→ filesystem journal
→ block/device cache
→ fsync/barrier
→ database durability assumption
```

Linux chỉ sở hữu phần OS/storage; WAL/transaction semantics thuộc database owner. Mục tiêu là giải thích vì sao “đã write()” hoặc “process đã trả success” chưa chắc tương đương với durability sau mất điện.

### P1 — cgroup v2 như mô hình accounting thống nhất

CPU, memory, I/O và PID limits nên được nối quanh cgroup v2 để người học hiểu host view và container view có thể khác nhau. Đây là nền cho capacity reasoning trong production containerized systems.

### P2 — Packet-path troubleshooting

Cần một mô hình bằng chứng dùng lại được:

```text
process/socket
→ namespace/interface
→ route
→ firewall/NAT/conntrack
→ physical/virtual interface
→ remote path
```

Mục tiêu là khoanh vùng failure, không phải nhớ chuỗi command cố định.

### P2 — eBPF: khi nào dùng và giới hạn diễn giải

Cần giải thích khi eBPF tạo thêm evidence, khi `strace`/`perf`/counters đã đủ, và overhead/sampling/aggregation có thể làm chẩn đoán sai ra sao. Công cụ quan sát cũng có failure mode của chính nó.

### P2 — Package/runtime provenance

Nên nối repository/signature → installed files → shared libraries → executable → running process. Điều này biến “package nào đã cài?” thành câu hỏi có thể truy ngược tới binary thật đang chạy.

### P2 — Xác minh sau recovery

Restart/rollback/restore/failover không kết thúc ở việc process “running”. Cần xác minh mount, time sync, network binding/route, resource limits, log continuity và application-facing health. Recovery chỉ hoàn tất khi trạng thái phục vụ đúng invariant, không chỉ khi daemon sống lại.

## 6. Thông tin nhạy theo phiên bản

Cơ chế Linux tương đối bền, nhưng kernel feature, `systemd`, distro defaults, packaging và tool behavior thay đổi theo phiên bản. Khi một chapter dựa vào hành vi cụ thể, phải phân biệt đó là kernel invariant, `systemd` behavior, distro default, container-runtime behavior hay tool-version behavior.

Không lấy mặc định của một distro làm chân lý chung cho Linux.

## 7. Quy trình review

Khi thêm nội dung lớn, kiểm theo chuỗi:

```text
owner
→ kernel/userspace boundary
→ resource/accounting model
→ evidence
→ failure mode
→ recovery/change semantics
→ version/distro sensitivity
→ handoff sang Backend/DevOps/Computer Science
```

Một danh sách command chỉ nên tồn tại khi từng command được gắn với trạng thái cần quan sát hoặc thao tác cần thực hiện.

## 8. Kết luận và bàn giao

Độ rộng khái niệm, kernel/resource depth và production troubleshooting hiện **mạnh**. Gap có giá trị nhất là reasoning xuyên tài nguyên, cgroup v2 như accounting model, durability boundary với database và recovery verification.

Từ đây, nên đọc tiếp [production request → storage → queue → failure → recovery](../devops_platform_engineering/10_production_practice/01_request_storage_queue_failure_and_recovery_case.md) để thấy Linux evidence tham gia vào một failure xuyên nhiều lớp như thế nào.