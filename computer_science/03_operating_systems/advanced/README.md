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

Track này nối system call/scheduling với kernel synchronization, RCU object lifetime, memory pressure, address translation, durability, async I/O và isolation. Mỗi phần phải chỉ ra resource/kernel invariant, context nào được phép sleep/preempt, failure under pressure, queue/wait nào hình thành và production evidence nào quan sát được.

Kernel synchronization và tracing không bị tách thành chapter mới chỉ để tăng roadmap. Canonical syscall/context chapter đã chứa spinlock vs sleeping lock, preemption/interrupt constraints, RCU grace-period/reclamation model, optimistic read intuition và tracing/off-CPU evidence. Nếu tiếp tục đào sâu, ưu tiên mở rộng các mechanism này tại nơi state/lifetime/wait thực sự được quản lý.

Production evidence cần nối application symptom với syscall latency, blocked/off-CPU stack, wakeup/run-queue delay, interrupt/softirq CPU, lock/spin contention, page fault/reclaim, block I/O, network drop/retransmission và cgroup throttling. Tool name có thể thay đổi; evidence model không đổi.

Hai tuyến xuyên tầng bắt buộc: [correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).