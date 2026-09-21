# Thư viện kiến thức Linux

Linux không chỉ là một tập hợp câu lệnh (command) để điều khiển máy chủ (server). Muốn sử dụng Linux vững trong phát triển phần mềm và môi trường vận hành thực tế (production), cần hiểu mô hình mà các câu lệnh đang tác động lên: hạt nhân (kernel) quản lý tài nguyên; tiến trình (process) làm việc với hệ thống thông qua bộ mô tả tệp (file descriptor); hệ thống tệp (filesystem) ánh xạ tên đường dẫn tới `inode`; bộ nhớ ảo (virtual memory) tách không gian địa chỉ của tiến trình khỏi RAM vật lý; ổ cắm mạng (socket) cung cấp giao diện vào/ra cho truyền thông mạng; còn trình vỏ lệnh (shell) ghép các chương trình nhỏ thành chuỗi xử lý (pipeline).

Thư viện này được tổ chức theo **khái niệm (concept), quan hệ phụ thuộc (dependency) và cấu trúc của hệ thống**, không theo mức Beginner → Advanced. Các chương chính được viết như tài liệu học lâu dài: giải thích vì sao cơ chế tồn tại, nó hoạt động ở lớp nào, có thể quan sát bằng công cụ nào và liên hệ tới backend/production ra sao. Tài liệu tham chiếu câu lệnh chỉ dùng để tra cứu sau khi đã hiểu cơ chế bên dưới.

Một số miền có hai lớp tài liệu: **chapter nền tảng** cung cấp mô hình tư duy (mental model) và thuật ngữ trước, sau đó **deep dive** đi vào cơ chế triển khai, accounting, failure mode và công cụ quan sát. Cách tách này giúp nội dung đủ sâu mà không biến một file thành cuốn sách khổng lồ.

## Bản đồ đọc và quan hệ phụ thuộc

```mermaid
graph TD
    A[Linux và mô hình Unix] --> B[Kernel, user space và system calls]
    B --> PK[/proc, /sys và kernel interfaces]
    B --> INT[Interrupt, softirq và device model]
    A --> C[Mô hình filesystem]
    C --> VF[VFS, page cache và writeback]
    C --> CJ[Journaling và consistency]
    B --> D[Process, thread và signal]
    D --> IPC[IPC: pipe, socket, shared memory]
    C --> E[File, stream và file descriptor]
    E --> F[Shell, Bash, pipe và redirection]
    F --> G[Xử lý văn bản]
    F --> GS[Bash scripting đáng tin cậy]
    C --> H[User, group và permission]
    H --> HC[Credentials, capabilities, ACL và MAC]
    B --> BOOT[Boot, kernel và initramfs]
    BOOT --> I[systemd và service]
    I --> SD[systemd dependency, cgroup và sandboxing]
    I --> J[Logging và observability]
    J --> JL[journald, rsyslog và log pipeline]
    I --> T[Time, clock và NTP]
    C --> K[Storage và filesystem]
    CJ --> K
    VF --> K
    K --> BL[Block layer và I/O scheduler]
    INT --> BL
    B --> L[Memory và virtual memory]
    L --> VM[Page fault, allocator, reclaim và PSI]
    B --> M[CPU, scheduling và performance]
    M --> MS[Kernel scheduler deep dive]
    BL --> IO[I/O performance]
    VF --> IO
    VM --> IO
    M --> IO
    E --> N[Networking, DNS, socket và port]
    IPC --> N
    INT --> N
    N --> NR[IP routing, NAT và conntrack]
    N --> DNS[DNS resolution internals]
    N --> NT[TCP, HTTP và TLS]
    NT --> CC[TCP congestion control]
    NT --> TLS[TLS, PKI và certificate lifecycle]
    DNS --> RP[Reverse proxy và load balancing]
    NR --> RP
    CC --> RP
    TLS --> RP
    N --> O[SSH và thao tác từ xa]
    F --> P[Automation và scheduling]
    GS --> P
    H --> Q[Security và hardening]
    HC --> Q
    HC --> CG
    P --> DEP[Deployment và rollback]
    K --> BK[Backup, restore và DR]
    Q --> BK
    P --> ELF[ELF và dynamic linking]
    B --> ELF
    ELF --> PKG[Package lifecycle và supply chain]
    PKG --> DEP
    DEP --> R[Xử lý sự cố production]
    BK --> R
    J --> R
    JL --> R
    T --> R
    IO --> R
    RP --> R
    MS --> CAP[Capacity planning và sizing]
    VM --> CAP
    IO --> CAP
    RP --> CAP
    CAP --> R
    R --> SRE[SLO, error budget và incident engineering]
    CAP --> SRE
    DEP --> SRE
    BK --> SRE
    D --> JR[Java backend incident playbook]
    L --> JR
    VM --> JR
    M --> JR
    IO --> JR
    NT --> JR
    RP --> JR
    PK --> TR[Tracing: strace, perf, eBPF]
    D --> TR
    IO --> TR
    TR --> R
    D --> CG[Namespace, cgroup, capability, seccomp]
    H --> CG
    N --> CG
    CG --> CON[Linux containers]
    CON --> R
    JR --> R
```

Sơ đồ giữ một số từ khóa tiếng Anh vì đây là những thuật ngữ người đọc sẽ thường xuyên gặp trong tài liệu Linux. Phần giải thích trong từng chương ưu tiên tiếng Việt và chỉ giữ thuật ngữ gốc trong ngoặc khi nó giúp nhận diện khái niệm.

## Cấu trúc thư viện

### Nền tảng hệ điều hành

- [`00_foundations/linux_and_unix_model.md`](./00_foundations/linux_and_unix_model.md) — Linux là gì, triết lý Unix (Unix philosophy) và các lớp trừu tượng (abstraction) nền tảng.
- [`00_foundations/kernel_userspace_syscalls.md`](./00_foundations/kernel_userspace_syscalls.md) — không gian hạt nhân (kernel space), không gian người dùng (user space), lời gọi hệ thống (system call) và ranh giới đặc quyền (privilege boundary).
- [`00_foundations/proc_sysfs_kernel_interfaces.md`](./00_foundations/proc_sysfs_kernel_interfaces.md) — `/proc`, `/sys`, `/dev`, `sysctl`, trạng thái tiến trình, kernel object và cách các công cụ user-space quan sát hệ thống.
- [`00_foundations/interrupts_softirq_device_model.md`](./00_foundations/interrupts_softirq_device_model.md) — interrupt, softirq, `ksoftirqd`, NAPI, IRQ affinity, RSS/RPS, DMA, driver, `/sys`, `/dev`, udev và cách kernel nhận/xử lý sự kiện phần cứng.

### Hệ thống tệp và I/O

- [`01_filesystem/filesystem_paths_inodes_links.md`](./01_filesystem/filesystem_paths_inodes_links.md) — đường dẫn, thư mục, `inode`, liên kết cứng (hard link), liên kết tượng trưng (symbolic link) và cấu trúc phân cấp của hệ thống tệp.
- [`01_filesystem/files_streams_descriptors.md`](./01_filesystem/files_streams_descriptors.md) — bộ mô tả tệp (file descriptor), `stdin`/`stdout`/`stderr` và mô hình vào/ra (I/O).
- [`01_filesystem/journaling_consistency_mounts.md`](./01_filesystem/journaling_consistency_mounts.md) — journaling, crash consistency, `fsync`, atomic rename, mount namespace, bind mount, read-only/noexec và mối liên hệ với database durability.
- [`01_filesystem/vfs_page_cache_writeback.md`](./01_filesystem/vfs_page_cache_writeback.md) — VFS, dentry/inode/file object, page cache, buffered/direct I/O, dirty page, writeback, read-ahead, `fsync` và mối liên hệ giữa filesystem với memory pressure.

### Shell và tự động hóa cấp lệnh

- [`02_shell/shell_bash_pipes_redirection.md`](./02_shell/shell_bash_pipes_redirection.md) — cách shell phân tích lệnh, mở rộng biểu thức (expansion), pipe, chuyển hướng (redirection), mã thoát (exit status) và cách ghép câu lệnh.
- [`02_shell/text_processing.md`](./02_shell/text_processing.md) — `grep`, `find`, `sed`, `awk` và tư duy xử lý luồng văn bản.
- [`02_shell/bash_scripting_reliability.md`](./02_shell/bash_scripting_reliability.md) — viết Bash script đáng tin cậy với validation, quoting, exit status, `trap`, temporary file, idempotency, locking và atomic update.

### Danh tính, quyền, tiến trình và IPC

- [`03_identity/users_groups_permissions.md`](./03_identity/users_groups_permissions.md) — `UID`/`GID`, quyền truy cập (permission), `sudo`, ACL và đặc quyền.
- [`03_identity/credentials_capabilities_acl_mac.md`](./03_identity/credentials_capabilities_acl_mac.md) — real/effective UID, supplementary groups, ACL mask/default ACL, setuid/setgid, Linux capabilities, user namespace, SELinux/AppArmor, seccomp và cách kernel đưa ra quyết định allow/deny.
- [`04_process/processes_threads_signals_jobs.md`](./04_process/processes_threads_signals_jobs.md) — vòng đời tiến trình (process lifecycle), `PID`, luồng (thread), tín hiệu (signal) và điều khiển tác vụ (job control).
- [`04_process/interprocess_communication.md`](./04_process/interprocess_communication.md) — pipe, FIFO, Unix socket, TCP socket, signal, shared memory, semaphore, `mmap`, `epoll`, non-blocking I/O và backpressure.

### Khởi động, dịch vụ, log và thời gian

- [`05_system/boot_kernel_initramfs.md`](./05_system/boot_kernel_initramfs.md) — firmware → bootloader → kernel → initramfs → root filesystem → PID 1, kernel command line, recovery và boot failure reasoning.
- [`05_system/systemd_boot_services.md`](./05_system/systemd_boot_services.md) — `PID 1`, đơn vị systemd (unit), quan hệ phụ thuộc và vòng đời dịch vụ.
- [`05_system/systemd_units_dependencies_resources.md`](./05_system/systemd_units_dependencies_resources.md) — dependency graph, `Requires/Wants/After`, service `Type`, socket/timer activation, cgroup resource controls, restart/timeout semantics, drop-in override và systemd sandboxing.
- [`05_system/logging_journal_observability.md`](./05_system/logging_journal_observability.md) — nhật ký (log), `journald`, xoay vòng nhật ký (log rotation) và gỡ lỗi dựa trên bằng chứng.
- [`05_system/journald_rsyslog_log_pipeline.md`](./05_system/journald_rsyslog_log_pipeline.md) — stdout/stderr → journald → rsyslog/collector, journal metadata, persistent/volatile storage, retention/rate limit, rotation, deleted-open log, centralized shipping, buffering và backpressure.
- [`05_system/time_clock_ntp.md`](./05_system/time_clock_ntp.md) — UTC, timezone, wall clock, monotonic clock, NTP/Chrony, clock drift và tác động tới TLS, token, cron và log correlation.

### CPU, memory, storage và hiệu năng

- [`06_resources/storage_filesystems.md`](./06_resources/storage_filesystems.md) — thiết bị khối (block device), phân vùng, hệ thống tệp, điểm gắn kết (mount), `inode` và dung lượng.
- [`06_resources/memory_virtual_memory.md`](./06_resources/memory_virtual_memory.md) — bộ nhớ ảo, trang nhớ (page), bộ nhớ đệm (cache), swap và OOM.
- [`06_resources/virtual_memory_page_fault_reclaim_allocator.md`](./06_resources/virtual_memory_page_fault_reclaim_allocator.md) — VMA/page table/TLB, minor/major page fault, COW, anonymous/file-backed memory, buddy/SLUB allocator, reclaim, PSI, swap/thrashing, global/cgroup OOM, NUMA và JVM native memory.
- [`06_resources/cpu_scheduling_performance.md`](./06_resources/cpu_scheduling_performance.md) — lập lịch CPU (CPU scheduling), tải trung bình (load average), mức sử dụng (utilization) và tư duy phân tích hiệu năng.
- [`06_resources/kernel_scheduler_deep_dive.md`](./06_resources/kernel_scheduler_deep_dive.md) — run queue, scheduling class, nice/priority, context switch, CPU affinity, SMT, NUMA, steal time, cgroup throttling và mối liên hệ với Java thread pool.
- [`06_resources/io_performance.md`](./06_resources/io_performance.md) — latency, throughput, IOPS, queueing, page cache, `iostat`, `pidstat`, `vmstat`, durability và cách suy luận khi storage chậm.
- [`06_resources/block_layer_io_scheduler.md`](./06_resources/block_layer_io_scheduler.md) — block layer, blk-mq, queue depth, I/O scheduler, `iostat`, dirty throttling, direct/async I/O, `io_uring`, NVMe và cgroup I/O.

### Networking và truy cập từ xa

- [`07_networking/networking_dns_sockets_ports.md`](./07_networking/networking_dns_sockets_ports.md) — giao diện mạng, định tuyến (routing), DNS, socket, cổng (port) và xử lý sự cố mạng.
- [`07_networking/ip_routing_nat_conntrack.md`](./07_networking/ip_routing_nat_conntrack.md) — routing table, policy routing, ARP/neighbor, NAT, conntrack, ephemeral port, network namespace, veth, MTU và packet path.
- [`07_networking/dns_resolution_internals.md`](./07_networking/dns_resolution_internals.md) — NSS, `/etc/hosts`, `/etc/resolv.conf`, recursive/authoritative DNS, TTL/cache, A/AAAA/CNAME, Java DNS cache, split DNS và container/Kubernetes DNS.
- [`07_networking/tcp_http_tls.md`](./07_networking/tcp_http_tls.md) — TCP handshake/state, timeout/reset, ephemeral port, HTTP keep-alive, TLS certificate/SNI và cách khoanh vùng request failure theo từng lớp.
- [`07_networking/tcp_congestion_control.md`](./07_networking/tcp_congestion_control.md) — flow/congestion control, `cwnd`, BDP, RTT, slow start, retransmission, CUBIC/BBR, pacing, bufferbloat, receive window, socket buffers và TCP behavior dưới tải.
- [`07_networking/tls_pki_certificates.md`](./07_networking/tls_pki_certificates.md) — PKI, certificate chain, SAN/hostname verification, SNI, TLS handshake, Java trust/key store, mTLS, certificate rotation, OCSP, ALPN và TLS troubleshooting.
- [`07_networking/reverse_proxy_load_balancing.md`](./07_networking/reverse_proxy_load_balancing.md) — reverse proxy, layer 4/layer 7 load balancing, health check, 502/504, timeout budget, retry amplification, keep-alive, rate limiting, forwarded headers và request correlation.
- [`07_networking/ssh_remote_operations.md`](./07_networking/ssh_remote_operations.md) — khóa SSH, mô hình tin cậy (trust), đường hầm (tunnel), SCP/SFTP và `rsync`.

### Vận hành, phần mềm và khả năng phục hồi

- [`08_operations/packages_software_libraries.md`](./08_operations/packages_software_libraries.md) — trình quản lý gói (package manager), phụ thuộc phần mềm và thư viện dùng chung (shared library).
- [`08_operations/package_repositories_updates_supply_chain.md`](./08_operations/package_repositories_updates_supply_chain.md) — package database, repository metadata/signing, candidate version, pin/hold, package scripts/config, patch lifecycle, runtime restart/reboot, snapshot repository, SBOM và software supply chain.
- [`08_operations/elf_dynamic_linking.md`](./08_operations/elf_dynamic_linking.md) — ELF, `execve`, shebang, dynamic linker, shared library resolution, symbol/ABI, PIE/ASLR và cách chẩn đoán binary tồn tại nhưng không chạy.
- [`08_operations/scheduling_automation.md`](./08_operations/scheduling_automation.md) — `cron`, bộ hẹn giờ systemd (systemd timer) và độ tin cậy của tự động hóa.
- [`08_operations/security_hardening.md`](./08_operations/security_hardening.md) — đặc quyền tối thiểu (least privilege), bề mặt tấn công (attack surface), cập nhật bản vá và gia cố máy chủ (host hardening).
- [`08_operations/deployment_release_rollback.md`](./08_operations/deployment_release_rollback.md) — desired state/runtime state, release directory, atomic symlink switch, health/smoke test, database migration compatibility, canary, blue–green và rollback.
- [`08_operations/backup_restore_disaster_recovery.md`](./08_operations/backup_restore_disaster_recovery.md) — RPO/RTO, file/database backup, snapshot, PITR, integrity, retention, restore test và disaster recovery runbook.

### Production, container và xử lý sự cố

- [`09_production/production_troubleshooting.md`](./09_production/production_troubleshooting.md) — phương pháp khoanh vùng sự cố (incident) từ triệu chứng tới nguyên nhân gốc (root cause).
- [`09_production/java_backend_incident_playbook.md`](./09_production/java_backend_incident_playbook.md) — playbook thực tế cho Java/Spring backend: systemd → JVM → thread/heap/FD → CPU/memory/I/O/network → dependency → recovery và RCA.
- [`09_production/observability_tracing_strace_perf.md`](./09_production/observability_tracing_strace_perf.md) — quan sát sâu bằng `/proc`, `pidstat`, `lsof`, `strace`, `perf`, flame graph và eBPF; phân biệt CPU time với off-CPU waiting.
- [`09_production/namespaces_cgroups_seccomp.md`](./09_production/namespaces_cgroups_seccomp.md) — PID/mount/network/user namespace, cgroup v2, CPU/memory limit, Linux capabilities, seccomp và cách debug isolation/resource policy.
- [`09_production/linux_containers.md`](./09_production/linux_containers.md) — cách container ghép namespace, cgroup, filesystem layer và host kernel thành môi trường runtime cô lập tương đối.
- [`09_production/capacity_planning_server_sizing.md`](./09_production/capacity_planning_server_sizing.md) — CPU/memory/storage/network sizing, Little's Law, headroom, autoscaling, N+1 capacity, load testing, SLO và cách nối RED/USE metrics với bottleneck Linux.
- [`09_production/sre_slo_error_budget_incident_engineering.md`](./09_production/sre_slo_error_budget_incident_engineering.md) — SLI/SLO/SLA, error budget, burn rate, alert strategy, incident roles/timeline, load shedding, retry/circuit breaker, postmortem, toil, runbook và cách nối user impact với Linux evidence.

### Kết nối kiến thức và tra cứu

- [`90_connections/linux_system_mental_models.md`](./90_connections/linux_system_mental_models.md) — kết nối các lớp trừu tượng thành mô hình tư duy (mental model) thống nhất về Linux.
- [`reference/putty_ssh_linux_server_commands.md`](./reference/putty_ssh_linux_server_commands.md) — bảng câu lệnh, tùy chọn, ví dụ và ghi chú thực tế để tra cứu nhanh.

## Gợi ý đường đọc theo nhu cầu

Nếu mục tiêu là **dùng PuTTY/SSH để vận hành server**, hãy đọc theo thứ tự: Linux/Unix model → filesystem → file descriptor → shell → permissions → credentials/capabilities → process → systemd → journal/log pipeline → networking → routing/DNS → SSH → production troubleshooting → command reference.

Nếu mục tiêu là **backend Java/Spring**, hãy đọc process/thread → IPC → memory overview → page fault/reclaim → CPU → kernel scheduler → file descriptor → VFS/page cache → block I/O → networking → routing/DNS → TCP/HTTP/TLS → TCP congestion → TLS/PKI → reverse proxy/load balancing → systemd/logging → tracing → Java backend incident playbook → capacity planning → SLO/incident engineering. Đường đọc này giúp nối trực tiếp JVM với Linux thay vì xem JVM như một hộp đen.

Nếu mục tiêu là **DevOps/production operations**, hãy bổ sung boot/initramfs → `/proc`/`/sys` → interrupt/device model → ELF/dynamic linking → package lifecycle/supply chain → Bash scripting → scheduling → deployment/rollback → backup/restore → security/credentials → routing/NAT → TCP/TLS → reverse proxy → namespace/cgroup → container → log pipeline/tracing → capacity planning → SLO/error budget → production troubleshooting. Đây là nhóm kiến thức giúp chuyển từ “biết câu lệnh” sang quản lý lifecycle, isolation, traffic path, capacity và reliability objective của hệ thống.

Nếu mục tiêu là **hiểu Linux từ bản chất hệ điều hành**, hãy đi theo: Unix model → kernel/user space/system call → `/proc`/`/sys` → interrupt/softirq/device model → process/thread/IPC → virtual memory → page fault/reclaim → filesystem/inode/VFS/page cache/journaling → block layer → scheduler/CPU → ELF/runtime → network/socket → routing/NAT → TCP congestion → credentials/capabilities → namespace/cgroup. Đây là đường đọc gần với cách một hệ điều hành thực sự được cấu tạo hơn là cách một khóa học command-line thường trình bày.

Nếu mục tiêu là **hiểu một HTTP request production từ đầu đến cuối**, hãy đi theo: DNS resolution → IP routing/NAT → TCP handshake → TCP congestion/flow control → TLS/PKI → HTTP → reverse proxy/load balancer → Java process/thread → memory/scheduler/I/O → database/downstream dependency → logging/tracing → SLI/SLO. Đây là đường đọc giúp biến các lỗi `UnknownHostException`, `Connection refused`, TLS handshake failure, `502`, `504`, OOM và application timeout thành những failure mode thuộc từng lớp cụ thể.

Nếu mục tiêu là **hiểu reliability từ metric Linux tới trải nghiệm người dùng**, hãy đi theo: RED/USE metrics → tracing → capacity planning → deployment/rollback → backup/DR → SLI/SLO/error budget → incident engineering. Đường đọc này giải thích tại sao một server “còn tài nguyên” vẫn có thể vi phạm SLO, và ngược lại tại sao utilization cao không tự động là incident.

## Cách dùng chapter nền tảng và deep dive

Không cần đọc mọi deep dive ngay lần đầu. Với một miền kiến thức, hãy đọc chapter nền tảng để có mô hình trước, sau đó đi sâu khi gặp nhu cầu thực tế:

```text
kernel_userspace_syscalls / proc_sysfs_kernel_interfaces
→ interrupts_softirq_device_model

memory_virtual_memory
→ virtual_memory_page_fault_reclaim_allocator

filesystem_paths / files_descriptors
→ vfs_page_cache_writeback
→ journaling_consistency_mounts
→ block_layer_io_scheduler

users_groups_permissions
→ credentials_capabilities_acl_mac

systemd_boot_services
→ systemd_units_dependencies_resources

logging_journal_observability
→ journald_rsyslog_log_pipeline

networking_dns_sockets_ports
→ ip_routing_nat_conntrack
→ dns_resolution_internals
→ tcp_http_tls
→ tcp_congestion_control
→ tls_pki_certificates
→ reverse_proxy_load_balancing

packages_software_libraries
→ package_repositories_updates_supply_chain
→ elf_dynamic_linking

production_troubleshooting / capacity_planning
→ sre_slo_error_budget_incident_engineering
```

Mục tiêu không phải học thuộc mọi chi tiết kernel ngay từ đầu. Mục tiêu là có một đường đi rõ từ **mô hình tổng quan → cơ chế bên dưới → công cụ quan sát → failure mode production → reliability objective**.

## Quy ước ngôn ngữ và liên kết

Các liên kết chéo dùng đường dẫn Markdown tương đối để hoạt động nhất quán trên GitHub, GitHub Pages và phần lớn trình đọc Markdown. Phần giải thích chính dùng tiếng Việt. Khi một thuật ngữ kỹ thuật quan trọng xuất hiện lần đầu, tài liệu có thể giữ thuật ngữ tiếng Anh trong ngoặc, ví dụ **tiến trình (process)** hoặc **bộ mô tả tệp (file descriptor)**. Thuật ngữ tiếng Hàn (한국어 용어) chỉ được thêm khi nó thực sự hữu ích trong môi trường học tập hoặc làm việc tại Hàn Quốc.

> **Mô hình tư duy trung tâm:** Linux có thể được xem như một hệ thống quản lý **tên, tiến trình, bộ nhớ, I/O, CPU time, quyền truy cập, thời gian, network path, runtime dependency, isolation và các điểm cuối giao tiếp**. Câu lệnh chỉ là giao diện để quan sát hoặc thay đổi những đối tượng đó; kỹ năng Linux thực sự nằm ở khả năng hiểu state, dependency, lifecycle, capacity, evidence và ảnh hưởng cuối cùng tới người dùng.