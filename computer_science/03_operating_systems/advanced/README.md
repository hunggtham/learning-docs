# Hệ điều hành nâng cao

Bắt đầu từ [nền tảng hệ điều hành](../../basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md).

## Canonical chapters

1. [Ngữ cảnh thực thi kernel, synchronization/RCU và đường đi system call](./00_kernel_execution_contexts_and_syscall_path.md)
2. [Scheduler internals, run queue và đánh đổi công bằng/độ trễ](./01_scheduler_run_queues_fairness_and_latency.md)
3. [Page fault, reclaim, dirty page và áp lực bộ nhớ](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md)
4. [Bộ nhớ ảo: page table, TLB shootdown và huge page](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md)
5. [Tính nhất quán sau crash của filesystem, journaling và copy-on-write](./04_filesystem_crash_consistency_journaling_and_cow.md)
6. [I/O nâng cao: epoll, io_uring, zero-copy và DMA](./05_epoll_io_uring_zero_copy_and_dma.md)
7. [Cơ chế container: namespace, cgroup, capability và seccomp](./06_containers_namespaces_cgroups_capabilities_and_seccomp.md)
8. [RCU, seqlock và safe memory reclamation](./07_rcu_seqlock_and_safe_memory_reclamation.md)
9. [eBPF, tracing kernel, observability và safety](./08_ebpf_tracing_kernel_observability_and_safety.md)

Track này nối system call/scheduling với kernel synchronization, object lifetime, memory pressure, address translation, durability, async I/O và isolation. Mỗi phần phải chỉ ra resource/kernel invariant, context nào được phép sleep/preempt, failure under pressure, queue/wait nào hình thành và production evidence nào quan sát được.

Chapter syscall/context vẫn giữ overview về synchronization và RCU vì đây là prerequisite để đọc kernel path. Chapter RCU/seqlock mới là canonical depth cho publication, grace period, quiescent state, deferred reclamation, ABA, epoch/hazard-pointer comparison, retry starvation và production evidence của reclamation debt. Chapter eBPF/tracing sở hữu reasoning path từ probe attachment → verifier/JIT → helper/map/ring-buffer → event loss/overhead → packet lifecycle/queue boundary → production evidence và safety boundary. Nội dung mới không biến synchronization hoặc observability thành danh sách primitive/tool; trọng tâm vẫn là state/lifetime proof và evidence quality.

Kernel networking path đã được deepen trong chapter eBPF qua ingress/egress lifecycle, NAPI/softirq, socket/qdisc boundaries, GRO/GSO, drop-vs-delay-vs-retransmission và flow-correlated evidence. Bước tiếp theo là validate trên workload/driver cụ thể nếu có incident thực tế; không mở chapter riêng chỉ để lặp lại packet-path overview.

Production evidence cần nối application symptom với syscall latency, blocked/off-CPU stack, wakeup/run-queue delay, interrupt/softirq CPU, lock/spin contention, page fault/reclaim, block I/O, network drop/retransmission, cgroup throttling và khi phù hợp grace-period/reclamation backlog. Tool name có thể thay đổi; evidence model không đổi.

Hai tuyến xuyên tầng bắt buộc: [correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).
