# Hệ điều hành nâng cao

Lộ trình sau [nền tảng hệ điều hành](../../basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md):

1. [Ngữ cảnh thực thi kernel và đường đi system call](./00_kernel_execution_contexts_and_syscall_path.md)
2. [Scheduler internals, run queue và đánh đổi công bằng/độ trễ](./01_scheduler_run_queues_fairness_and_latency.md)
3. [Page fault, reclaim, dirty page và áp lực bộ nhớ](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md)
4. [Bộ nhớ ảo: page table, TLB shootdown và huge page](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md)
5. [Tính nhất quán sau crash của filesystem, journaling và copy-on-write](./04_filesystem_crash_consistency_journaling_and_cow.md)
6. [I/O nâng cao: epoll, io_uring, zero-copy và DMA](./05_epoll_io_uring_zero_copy_and_dma.md)
7. [Cơ chế container: namespace, cgroup, capability và seccomp](./06_containers_namespaces_cgroups_capabilities_and_seccomp.md)
8. Đồng bộ kernel, RCU và đường đọc không khóa
9. eBPF, tracing và khả năng quan sát production
10. Lập lịch thời gian thực và đảo ngược ưu tiên (priority inversion)

Bảy chapter hiện có nối system call và scheduling với memory pressure, virtual-memory translation, durability, asynchronous I/O và container isolation. Phần tiếp theo sẽ đi sâu vào kernel synchronization, RCU, eBPF/tracing và real-time behavior.
