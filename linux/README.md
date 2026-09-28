# Thư viện kiến thức Linux

> **Mạch đọc:** Đọc **Thư viện kiến thức Linux** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Bản đồ đọc và quan hệ phụ thuộc** sang **Cấu trúc thư viện**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Linux không chỉ là một tập hợp câu lệnh (command) để điều khiển máy chủ (server / 서버). Muốn sử dụng Linux vững trong phát triển phần mềm và môi trường vận hành thực tế (production), cần hiểu mô hình mà các câu lệnh đang tác động lên: hạt nhân (kernel) quản lý tài nguyên; tiến trình (process / 프로세스) làm việc với hệ thống thông qua bộ mô tả tệp (file descriptor); hệ thống tệp (filesystem) ánh xạ tên đường dẫn tới `inode`; bộ nhớ ảo (virtual memory) tách không gian địa chỉ của tiến trình khỏi RAM vật lý; ổ cắm mạng (socket) cung cấp giao diện vào/ra cho truyền thông mạng; còn trình vỏ lệnh (shell) ghép các chương trình nhỏ thành chuỗi xử lý (pipeline / 파이프라인).

Thư viện này được tổ chức theo **khái niệm (concept), quan hệ phụ thuộc (dependency / 의존성) và cấu trúc của hệ thống**, không theo mức Beginner → Advanced. Các chương chính được viết như tài liệu học lâu dài: giải thích vì sao cơ chế tồn tại, nó hoạt động ở lớp nào, có thể quan sát bằng công cụ nào và liên hệ tới backend/môi trường vận hành (production / 운영 환경) ra sao. Tài liệu tham chiếu câu lệnh chỉ dùng để tra cứu sau khi đã hiểu cơ chế bên dưới.

Một số miền có hai lớp tài liệu: **chapter nền tảng** cung cấp mô hình tư duy (mental model / 사고 모델) và thuật ngữ trước, sau đó **deep dive** đi vào cơ chế triển khai, accounting, dạng thất bại (failure mode / 실패 모드) và công cụ quan sát. Cách tách này giúp nội dung đủ sâu mà không biến một tệp (file / 파일) thành cuốn sách khổng lồ.

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


> **Chuyển mạch:** Từ **Bản đồ đọc và quan hệ phụ thuộc**, ta sang **Cấu trúc thư viện** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cấu trúc thư viện

### Nền tảng hệ điều hành

- [`00_foundations/linux_and_unix_model.md`](./00_foundations/linux_and_unix_model.md) — Linux là gì, triết lý Unix (Unix philosophy) và các lớp trừu tượng (abstraction / 추상화) nền tảng.
- [`00_foundations/kernel_userspace_syscalls.md`](./00_foundations/kernel_userspace_syscalls.md) — không gian hạt nhân (kernel space), không gian người dùng (user space), lời gọi hệ thống (system call / 시스템 호출) và ranh giới đặc quyền (privilege boundary).
- [`00_foundations/proc_sysfs_kernel_interfaces.md`](./00_foundations/proc_sysfs_kernel_interfaces.md) — `/proc`, `/sys`, `/dev`, `sysctl`, trạng thái tiến trình, kernel đối tượng (object / 객체) và cách các công cụ user-space quan sát hệ thống.
- [`00_foundations/interrupts_softirq_device_model.md`](./00_foundations/interrupts_softirq_device_model.md) — interrupt, softirq, `ksoftirqd`, NAPI, IRQ affinity, RSS/RPS, DMA, driver, `/sys`, `/dev`, udev và cách kernel nhận/xử lý sự kiện phần cứng.

### Hệ thống tệp và I/O

- [`01_filesystem/filesystem_paths_inodes_links.md`](./01_filesystem/filesystem_paths_inodes_links.md) — đường dẫn, thư mục, `inode`, liên kết cứng (hard link), liên kết tượng trưng (symbolic link) và cấu trúc phân cấp của hệ thống tệp.
- [`01_filesystem/files_streams_descriptors.md`](./01_filesystem/files_streams_descriptors.md) — bộ mô tả tệp (file descriptor), `stdin`/`stdout`/`stderr` và mô hình vào/ra (I/O).
- [`01_filesystem/journaling_consistency_mounts.md`](./01_filesystem/journaling_consistency_mounts.md) — journaling, crash consistency, `fsync`, atomic rename, mount không gian tên (namespace / 네임스페이스), bind mount, read-only/noexec và mối liên hệ với cơ sở dữ liệu (database / 데이터베이스) durability.
- [`01_filesystem/vfs_page_cache_writeback.md`](./01_filesystem/vfs_page_cache_writeback.md) — VFS, dentry/inode/tệp (file / 파일) đối tượng (object / 객체), page bộ nhớ đệm (cache / 캐시), buffered/direct I/O, dirty page, writeback, read-ahead, `fsync` và mối liên hệ giữa filesystem với bộ nhớ (memory / 메모리) pressure.

### Shell và tự động hóa cấp lệnh

- [`02_shell/shell_bash_pipes_redirection.md`](./02_shell/shell_bash_pipes_redirection.md) — cách shell phân tích lệnh, mở rộng biểu thức (expansion), pipe, chuyển hướng (redirection), mã thoát (exit status) và cách ghép câu lệnh.
- [`02_shell/text_processing.md`](./02_shell/text_processing.md) — `grep`, `find`, `sed`, `awk` và tư duy xử lý luồng văn bản.
- [`02_shell/bash_scripting_reliability.md`](./02_shell/bash_scripting_reliability.md) — viết Bash script đáng tin cậy với kiểm tra hợp lệ (validation / 검증), quoting, exit status, `trap`, temporary tệp (file / 파일), idempotency, locking và atomic cập nhật (update / 업데이트).

### Danh tính, quyền, tiến trình và IPC

- [`03_identity/users_groups_permissions.md`](./03_identity/users_groups_permissions.md) — `UID`/`GID`, quyền truy cập (permission), `sudo`, ACL và đặc quyền.
- [`03_identity/credentials_capabilities_acl_mac.md`](./03_identity/credentials_capabilities_acl_mac.md) — real/effective UID, supplementary groups, ACL mask/default ACL, setuid/setgid, Linux capabilities, người dùng (user / 사용자) không gian tên (namespace / 네임스페이스), SELinux/AppArmor, seccomp và cách kernel đưa ra quyết định allow/deny.
- [`04_process/processes_threads_signals_jobs.md`](./04_process/processes_threads_signals_jobs.md) — vòng đời tiến trình (process lifecycle), `PID`, luồng (thread), tín hiệu (signal / 신호) và điều khiển tác vụ (job control).
- [`04_process/interprocess_communication.md`](./04_process/interprocess_communication.md) — pipe, FIFO, Unix socket, TCP socket, tín hiệu (signal / 신호), dùng chung (shared / 공유) bộ nhớ (memory / 메모리), semaphore, `mmap`, `epoll`, non-blocking I/O và backpressure.

### Khởi động, dịch vụ, log và thời gian

- [`05_system/boot_kernel_initramfs.md`](./05_system/boot_kernel_initramfs.md) — firmware → bootloader → kernel → initramfs → gốc (root / 루트) filesystem → PID 1, kernel command line, khôi phục (recovery / 복구) và boot thất bại (failure / 실패) lập luận (reasoning / 추론).
- [`05_system/systemd_boot_services.md`](./05_system/systemd_boot_services.md) — `PID 1`, đơn vị systemd (unit), quan hệ phụ thuộc và vòng đời dịch vụ.
- [`05_system/systemd_units_dependencies_resources.md`](./05_system/systemd_units_dependencies_resources.md) — phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프), `Requires/Wants/After`, dịch vụ (service / 서비스) `Type`, socket/timer activation, cgroup tài nguyên (resource / 자원) controls, restart/hết thời gian chờ (timeout / 타임아웃) ngữ nghĩa (semantics / 의미론), drop-in override và systemd sandboxing.
- [`05_system/logging_journal_observability.md`](./05_system/logging_journal_observability.md) — nhật ký (log), `journald`, xoay vòng nhật ký (log rotation) và gỡ lỗi dựa trên bằng chứng.
- [`05_system/journald_rsyslog_log_pipeline.md`](./05_system/journald_rsyslog_log_pipeline.md) — stdout/stderr → journald → rsyslog/collector, journal siêu dữ liệu (metadata / 메타데이터), persistent/volatile lưu trữ (storage / 저장소), retention/tỷ lệ (rate / 비율) limit, rotation, deleted-open log, centralized shipping, buffering và backpressure.
- [`05_system/time_clock_ntp.md`](./05_system/time_clock_ntp.md) — UTC, timezone, wall clock, monotonic clock, NTP/Chrony, clock drift và tác động tới TLS, đơn vị từ (token / 토큰), cron và log correlation.

### CPU, bộ nhớ (memory / 메모리), lưu trữ (storage / 저장소) và hiệu năng

- [`06_resources/storage_filesystems.md`](./06_resources/storage_filesystems.md) — thiết bị khối (block device), phân vùng, hệ thống tệp, điểm gắn kết (mount), `inode` và dung lượng.
- [`06_resources/memory_virtual_memory.md`](./06_resources/memory_virtual_memory.md) — bộ nhớ ảo, trang nhớ (page), bộ nhớ đệm (cache / 캐시), swap và OOM.
- [`06_resources/virtual_memory_page_fault_reclaim_allocator.md`](./06_resources/virtual_memory_page_fault_reclaim_allocator.md) — VMA/bảng trang (page table / 페이지 테이블)/TLB, minor/major page fault, COW, anonymous/file-backed bộ nhớ (memory / 메모리), buddy/SLUB allocator, reclaim, PSI, swap/thrashing, toàn cục (global / 전역)/cgroup OOM, NUMA và JVM bản địa (native / 네이티브) bộ nhớ (memory / 메모리).
- [`06_resources/cpu_scheduling_performance.md`](./06_resources/cpu_scheduling_performance.md) — lập lịch CPU (CPU scheduling), tải trung bình (load average), mức sử dụng (utilization) và tư duy phân tích hiệu năng.
- [`06_resources/kernel_scheduler_deep_dive.md`](./06_resources/kernel_scheduler_deep_dive.md) — run hàng đợi (queue / 큐), scheduling lớp (class / 클래스), nice/priority, ngữ cảnh (context / 맥락) switch, CPU affinity, SMT, NUMA, steal thời gian (time / 시간), cgroup throttling và mối liên hệ với Java luồng thực thi (thread / 스레드) pool.
- [`06_resources/io_performance.md`](./06_resources/io_performance.md) — độ trễ (latency / 지연 시간), thông lượng (throughput / 처리량), IOPS, queueing, page bộ nhớ đệm (cache / 캐시), `iostat`, `pidstat`, `vmstat`, durability và cách suy luận khi lưu trữ (storage / 저장소) chậm.
- [`06_resources/block_layer_io_scheduler.md`](./06_resources/block_layer_io_scheduler.md) — khối (block / 블록) tầng (layer / 계층), blk-mq, hàng đợi (queue / 큐) độ sâu (depth / 깊이), I/O scheduler, `iostat`, dirty throttling, direct/async I/O, `io_uring`, NVMe và cgroup I/O.

### Networking và truy cập từ xa

- [`07_networking/networking_dns_sockets_ports.md`](./07_networking/networking_dns_sockets_ports.md) — giao diện mạng, định tuyến (routing), DNS, socket, cổng (port / 포트) và xử lý sự cố mạng.
- [`07_networking/ip_routing_nat_conntrack.md`](./07_networking/ip_routing_nat_conntrack.md) — routing bảng (table / 테이블), chính sách (policy / 정책) routing, ARP/neighbor, NAT, conntrack, ephemeral cổng (port / 포트), mạng (network / 네트워크) không gian tên (namespace / 네임스페이스), veth, MTU và packet đường dẫn (path / 경로).
- [`07_networking/dns_resolution_internals.md`](./07_networking/dns_resolution_internals.md) — NSS, `/etc/hosts`, `/etc/resolv.conf`, recursive/authoritative DNS, TTL/bộ nhớ đệm (cache / 캐시), A/AAAA/CNAME, Java DNS bộ nhớ đệm (cache / 캐시), split DNS và bộ chứa (container / 컨테이너)/Kubernetes DNS.
- [`07_networking/tcp_http_tls.md`](./07_networking/tcp_http_tls.md) — TCP handshake/trạng thái (state / 상태), hết thời gian chờ (timeout / 타임아웃)/reset, ephemeral cổng (port / 포트), HTTP keep-alive, TLS certificate/SNI và cách khoanh vùng yêu cầu (request / 요청) thất bại (failure / 실패) theo từng lớp.
- [`07_networking/tcp_congestion_control.md`](./07_networking/tcp_congestion_control.md) — luồng (flow / 흐름)/congestion điều khiển (control / 제어), `cwnd`, BDP, RTT, slow start, retransmission, CUBIC/BBR, pacing, bufferbloat, receive cửa sổ (window / 윈도우), socket buffers và TCP hành vi (behavior / 동작) dưới tải.
- [`07_networking/tls_pki_certificates.md`](./07_networking/tls_pki_certificates.md) — PKI, certificate chuỗi (chain / 사슬), SAN/hostname xác minh (verification / 확인), SNI, TLS handshake, Java trust/key store, mTLS, certificate rotation, OCSP, ALPN và TLS troubleshooting.
- [`07_networking/reverse_proxy_load_balancing.md`](./07_networking/reverse_proxy_load_balancing.md) — reverse proxy, tầng (layer / 계층) 4/tầng (layer / 계층) 7 tải (load / 로드) balancing, health check, 502/504, ngân sách thời gian chờ (timeout budget / 타임아웃 예산), thử lại (retry / 재시도) amplification, keep-alive, tỷ lệ (rate / 비율) limiting, forwarded headers và yêu cầu (request / 요청) correlation.
- [`07_networking/ssh_remote_operations.md`](./07_networking/ssh_remote_operations.md) — khóa SSH, mô hình tin cậy (trust), đường hầm (tunnel), SCP/SFTP và `rsync`.

### Vận hành, phần mềm và khả năng phục hồi

- [`08_operations/packages_software_libraries.md`](./08_operations/packages_software_libraries.md) — trình quản lý gói (package manager / 패키지 관리자), phụ thuộc phần mềm và thư viện dùng chung (shared library).
- [`08_operations/package_repositories_updates_supply_chain.md`](./08_operations/package_repositories_updates_supply_chain.md) — gói (package / 패키지) cơ sở dữ liệu (database / 데이터베이스), repository siêu dữ liệu (metadata / 메타데이터)/signing, candidate phiên bản (version / 버전), pin/hold, gói (package / 패키지) scripts/cấu hình (config / 설정), patch vòng đời (lifecycle / 생명주기), thời gian chạy (runtime / 런타임) restart/reboot, snapshot repository, SBOM và software supply chuỗi (chain / 사슬).
- [`08_operations/elf_dynamic_linking.md`](./08_operations/elf_dynamic_linking.md) — ELF, `execve`, shebang, động (dynamic / 동적) linker, dùng chung (shared / 공유) thư viện (library / 라이브러리) resolution, symbol/ABI, PIE/ASLR và cách chẩn đoán nhị phân (binary / 이진) tồn tại nhưng không chạy.
- [`08_operations/scheduling_automation.md`](./08_operations/scheduling_automation.md) — `cron`, bộ hẹn giờ systemd (systemd timer) và độ tin cậy của tự động hóa.
- [`08_operations/security_hardening.md`](./08_operations/security_hardening.md) — đặc quyền tối thiểu (least privilege), bề mặt tấn công (attack surface), cập nhật bản vá và gia cố máy chủ (host hardening).
- [`08_operations/deployment_release_rollback.md`](./08_operations/deployment_release_rollback.md) — desired trạng thái (state / 상태)/thời gian chạy (runtime / 런타임) trạng thái (state / 상태), bản phát hành (release / 릴리스) directory, atomic symlink switch, health/smoke kiểm thử (test / 테스트), cơ sở dữ liệu (database / 데이터베이스) di chuyển (migration / 마이그레이션) tính tương thích (compatibility / 호환성), canary, blue–green và quay lui (rollback / 롤백).
- [`08_operations/backup_restore_disaster_recovery.md`](./08_operations/backup_restore_disaster_recovery.md) — RPO/RTO, tệp (file / 파일)/cơ sở dữ liệu (database / 데이터베이스) backup, snapshot, PITR, integrity, retention, restore kiểm thử (test / 테스트) và disaster khôi phục (recovery / 복구) runbook.

### Môi trường vận hành (production / 운영 환경), bộ chứa (container / 컨테이너) và xử lý sự cố

- [`09_production/production_troubleshooting.md`](./09_production/production_troubleshooting.md) — phương pháp khoanh vùng sự cố (incident / 인시던트) từ triệu chứng tới nguyên nhân gốc (root cause / 근본 원인).
- [`09_production/java_backend_incident_playbook.md`](./09_production/java_backend_incident_playbook.md) — playbook thực tế cho Java/Spring backend: systemd → JVM → luồng thực thi (thread / 스레드)/vùng nhớ động (heap / 힙)/FD → CPU/bộ nhớ (memory / 메모리)/I/O/mạng (network / 네트워크) → phụ thuộc (dependency / 의존성) → khôi phục (recovery / 복구) và RCA.
- [`09_production/observability_tracing_strace_perf.md`](./09_production/observability_tracing_strace_perf.md) — quan sát sâu bằng `/proc`, `pidstat`, `lsof`, `strace`, `perf`, flame đồ thị (graph / 그래프) và eBPF; phân biệt CPU thời gian (time / 시간) với off-CPU waiting.
- [`09_production/namespaces_cgroups_seccomp.md`](./09_production/namespaces_cgroups_seccomp.md) — PID/mount/mạng (network / 네트워크)/người dùng (user / 사용자) không gian tên (namespace / 네임스페이스), cgroup v2, CPU/giới hạn bộ nhớ (memory limit / 메모리 제한), Linux capabilities, seccomp và cách gỡ lỗi (debug / 디버그) isolation/tài nguyên (resource / 자원) chính sách (policy / 정책).
- [`09_production/linux_containers.md`](./09_production/linux_containers.md) — cách bộ chứa (container / 컨테이너) ghép không gian tên (namespace / 네임스페이스), cgroup, filesystem tầng (layer / 계층) và host kernel thành môi trường thời gian chạy (runtime / 런타임) cô lập tương đối.
- [`09_production/capacity_planning_server_sizing.md`](./09_production/capacity_planning_server_sizing.md) — CPU/bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소)/mạng (network / 네트워크) sizing, Little's Law, headroom, autoscaling, N+1 sức chứa (capacity / 용량), tải (load / 로드) testing, SLO và cách nối RED/USE metrics với bottleneck Linux.
- [`09_production/sre_slo_error_budget_incident_engineering.md`](./09_production/sre_slo_error_budget_incident_engineering.md) — SLI/SLO/SLA, lỗi (error / 오류) ngân sách (budget / 예산), burn tỷ lệ (rate / 비율), alert chiến lược (strategy / 전략), sự cố (incident / 인시던트) roles/timeline, tải (load / 로드) shedding, thử lại (retry / 재시도)/circuit breaker, postmortem, toil, runbook và cách nối người dùng (user / 사용자) impact với Linux bằng chứng (evidence / 증거).

### Kết nối kiến thức và tra cứu

- [`90_connections/linux_system_mental_models.md`](./90_connections/linux_system_mental_models.md) — kết nối các lớp trừu tượng thành mô hình tư duy (mental model / 사고 모델) thống nhất về Linux.
- [`reference/putty_ssh_linux_server_commands.md`](./reference/putty_ssh_linux_server_commands.md) — bảng câu lệnh, tùy chọn, ví dụ và ghi chú thực tế để tra cứu nhanh.


> **Chuyển mạch:** Từ **Cấu trúc thư viện**, ta sang **Gợi ý đường đọc theo nhu cầu** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Gợi ý đường đọc theo nhu cầu

Nếu mục tiêu là **dùng PuTTY/SSH để vận hành máy chủ (server / 서버)**, hãy đọc theo thứ tự: Linux/Unix mô hình (model / 모델) → filesystem → tệp (file / 파일) descriptor → shell → permissions → credentials/capabilities → tiến trình (process / 프로세스) → systemd → journal/log chuỗi xử lý (pipeline / 파이프라인) → networking → routing/DNS → SSH → môi trường vận hành (production / 운영 환경) troubleshooting → command tham chiếu (reference / 참조).

Nếu mục tiêu là **backend Java/Spring**, hãy đọc tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) → IPC → bộ nhớ (memory / 메모리) overview → page fault/reclaim → CPU → kernel scheduler → tệp (file / 파일) descriptor → VFS/page bộ nhớ đệm (cache / 캐시) → khối (block / 블록) I/O → networking → routing/DNS → TCP/HTTP/TLS → TCP congestion → TLS/PKI → reverse proxy/tải (load / 로드) balancing → systemd/logging → tracing → Java backend sự cố (incident / 인시던트) playbook → sức chứa (capacity / 용량) planning → SLO/sự cố (incident / 인시던트) kỹ thuật (engineering / 엔지니어링). Đường đọc này giúp nối trực tiếp JVM với Linux thay vì xem JVM như một hộp đen.

Nếu mục tiêu là **DevOps/môi trường vận hành (production / 운영 환경) operations**, hãy bổ sung boot/initramfs → `/proc`/`/sys` → interrupt/thiết bị (device / 장치) mô hình (model / 모델) → ELF/động (dynamic / 동적) linking → gói (package / 패키지) vòng đời (lifecycle / 생명주기)/supply chuỗi (chain / 사슬) → Bash scripting → scheduling → triển khai (deployment / 배포)/quay lui (rollback / 롤백) → backup/restore → bảo mật (security / 보안)/credentials → routing/NAT → TCP/TLS → reverse proxy → không gian tên (namespace / 네임스페이스)/cgroup → bộ chứa (container / 컨테이너) → log chuỗi xử lý (pipeline / 파이프라인)/tracing → sức chứa (capacity / 용량) planning → SLO/lỗi (error / 오류) ngân sách (budget / 예산) → môi trường vận hành (production / 운영 환경) troubleshooting. Đây là nhóm kiến thức giúp chuyển từ “biết câu lệnh” sang quản lý vòng đời (lifecycle / 생명주기), isolation, traffic đường dẫn (path / 경로), sức chứa (capacity / 용량) và độ tin cậy (reliability / 신뢰성) mục tiêu (objective / 목표) của hệ thống.

Nếu mục tiêu là **hiểu Linux từ bản chất hệ điều hành**, hãy đi theo: Unix mô hình (model / 모델) → kernel/người dùng (user / 사용자) không gian (space / 공간)/lời gọi hệ thống (system call / 시스템 호출) → `/proc`/`/sys` → interrupt/softirq/thiết bị (device / 장치) mô hình (model / 모델) → tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드)/IPC → virtual bộ nhớ (memory / 메모리) → page fault/reclaim → filesystem/inode/VFS/page bộ nhớ đệm (cache / 캐시)/journaling → khối (block / 블록) tầng (layer / 계층) → scheduler/CPU → ELF/thời gian chạy (runtime / 런타임) → mạng (network / 네트워크)/socket → routing/NAT → TCP congestion → credentials/capabilities → không gian tên (namespace / 네임스페이스)/cgroup. Đây là đường đọc gần với cách một hệ điều hành thực sự được cấu tạo hơn là cách một khóa học command-line thường trình bày.

Nếu mục tiêu là **hiểu một HTTP yêu cầu (request / 요청) môi trường vận hành (production / 운영 환경) từ đầu đến cuối**, hãy đi theo: DNS resolution → IP routing/NAT → TCP handshake → TCP congestion/luồng (flow / 흐름) điều khiển (control / 제어) → TLS/PKI → HTTP → reverse proxy/bộ cân bằng tải (load balancer / 로드 밸런서) → Java tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드) → bộ nhớ (memory / 메모리)/scheduler/I/O → cơ sở dữ liệu (database / 데이터베이스)/downstream phụ thuộc (dependency / 의존성) → logging/tracing → SLI/SLO. Đây là đường đọc giúp biến các lỗi `UnknownHostException`, `Connection refused`, TLS handshake thất bại (failure / 실패), `502`, `504`, OOM và ứng dụng (application / 애플리케이션) hết thời gian chờ (timeout / 타임아웃) thành những dạng thất bại (failure mode / 실패 모드) thuộc từng lớp cụ thể.

Nếu mục tiêu là **hiểu độ tin cậy (reliability / 신뢰성) từ chỉ số (metric / 지표) Linux tới trải nghiệm người dùng**, hãy đi theo: RED/USE metrics → tracing → sức chứa (capacity / 용량) planning → triển khai (deployment / 배포)/quay lui (rollback / 롤백) → backup/DR → SLI/SLO/lỗi (error / 오류) ngân sách (budget / 예산) → sự cố (incident / 인시던트) kỹ thuật (engineering / 엔지니어링). Đường đọc này giải thích tại sao một máy chủ (server / 서버) “còn tài nguyên” vẫn có thể vi phạm SLO, và ngược lại tại sao utilization cao không tự động là sự cố (incident / 인시던트).


> **Chuyển mạch:** Từ **Gợi ý đường đọc theo nhu cầu**, ta sang **Cách dùng chapter nền tảng và deep dive** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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

Mục tiêu không phải học thuộc mọi chi tiết kernel ngay từ đầu. Mục tiêu là có một đường đi rõ từ **mô hình tổng quan → cơ chế bên dưới → công cụ quan sát → dạng thất bại (failure mode / 실패 모드) môi trường vận hành (production / 운영 환경) → độ tin cậy (reliability / 신뢰성) mục tiêu (objective / 목표)**.


> **Chuyển mạch:** Từ **Cách dùng chapter nền tảng và deep dive**, ta sang **Quy ước ngôn ngữ và liên kết** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quy ước ngôn ngữ và liên kết

Các liên kết chéo dùng đường dẫn Markdown tương đối để hoạt động nhất quán trên GitHub, GitHub Pages và phần lớn trình đọc Markdown. Phần giải thích chính dùng tiếng Việt. Khi một thuật ngữ kỹ thuật quan trọng xuất hiện lần đầu, tài liệu có thể giữ thuật ngữ tiếng Anh trong ngoặc, ví dụ **tiến trình (process / 프로세스)** hoặc **bộ mô tả tệp (file descriptor)**. Thuật ngữ tiếng Hàn (한국어 용어) chỉ được thêm khi nó thực sự hữu ích trong môi trường học tập hoặc làm việc tại Hàn Quốc.

> **Mô hình tư duy trung tâm:** Linux có thể được xem như một hệ thống quản lý **tên, tiến trình, bộ nhớ, I/O, CPU thời gian (time / 시간), quyền truy cập, thời gian, mạng (network / 네트워크) đường dẫn (path / 경로), thời gian chạy (runtime / 런타임) phụ thuộc (dependency / 의존성), isolation và các điểm cuối giao tiếp**. Câu lệnh chỉ là giao diện để quan sát hoặc thay đổi những đối tượng đó; kỹ năng Linux thực sự nằm ở khả năng hiểu trạng thái (state / 상태), phụ thuộc (dependency / 의존성), vòng đời (lifecycle / 생명주기), sức chứa (capacity / 용량), bằng chứng (evidence / 증거) và ảnh hưởng cuối cùng tới người dùng.

> **Bàn giao:** Sau **Quy ước ngôn ngữ và liên kết**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp.
