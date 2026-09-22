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
9. [eBPF, tracing, kernel observability và safety boundary](./08_ebpf_tracing_kernel_observability_and_safety.md)

Track này nối system call/scheduling với kernel synchronization, object lifetime, memory pressure, address translation, durability, async I/O, isolation và cuối cùng là cách thu production evidence mà không phá safety/timing của kernel. Mỗi phần phải chỉ ra resource/kernel invariant, context nào được phép sleep/preempt, failure under pressure, queue/wait nào hình thành và evidence nào quan sát được.

Chapter syscall/context giữ overview về synchronization và RCU vì đây là prerequisite để đọc kernel path. Chapter RCU/seqlock là canonical depth cho publication, grace period, quiescent state, deferred reclamation, ABA, epoch/hazard-pointer comparison, retry starvation và reclamation debt.

Chapter eBPF/tracing không phải catalog tool. Nó giải thích hook semantics, verifier safety proof, helper/map boundary, per-CPU aggregation, ring-buffer pressure, sampling bias, JIT overhead và cách instrumentation có thể làm thay đổi hiện tượng đang đo. Evidence chỉ có nghĩa khi biết nó được thu tại state transition nào.

Production evidence cần nối application symptom với syscall latency, blocked/off-CPU stack, wakeup/run-queue delay, interrupt/softirq CPU, lock/spin contention, page fault/reclaim, block I/O, network drop/retransmission, cgroup throttling, grace-period/reclamation backlog và tracing loss/overhead khi phù hợp.

Hai tuyến xuyên tầng bắt buộc: [correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md). Kernel networking chi tiết được đặt tại [Networks & Distributed Systems](../../06_networks_distributed_systems/advanced/08_kernel_packet_path_qdisc_nic_offload_and_observability.md) để tránh duplicate packet semantics.