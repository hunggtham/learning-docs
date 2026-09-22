# Hệ điều hành nâng cao

Bắt đầu từ [nền tảng hệ điều hành](../../basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md).

## Canonical chapters

1. [Ngữ cảnh thực thi kernel và đường đi system call](./00_kernel_execution_contexts_and_syscall_path.md)
2. [Scheduler internals, run queue và đánh đổi công bằng/độ trễ](./01_scheduler_run_queues_fairness_and_latency.md)
3. [Page fault, reclaim, dirty page và áp lực bộ nhớ](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md)
4. [Bộ nhớ ảo: page table, TLB shootdown và huge page](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md)
5. [Tính nhất quán sau crash của filesystem, journaling và copy-on-write](./04_filesystem_crash_consistency_journaling_and_cow.md)
6. [I/O nâng cao: epoll, io_uring, zero-copy và DMA](./05_epoll_io_uring_zero_copy_and_dma.md)
7. [Cơ chế container: namespace, cgroup, capability và seccomp](./06_containers_namespaces_cgroups_capabilities_and_seccomp.md)

Track này nối system call/scheduling với memory pressure, address translation, durability, async I/O và isolation. Mỗi phần phải chỉ ra resource/kernel invariant, failure under pressure, queue/wait nào hình thành và production evidence nào quan sát được.

## Depth priorities

Kernel synchronization, RCU, real-time scheduling, tracing/eBPF không mặc định trở thành chapter mới. Nếu chúng phục vụ reasoning về scheduler, concurrency, syscall/I/O hoặc observability thì đào sâu ngay tại canonical chapter liên quan và cross-link sang Architecture/Runtime/Software Systems.

Hai tuyến xuyên tầng bắt buộc: [correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).