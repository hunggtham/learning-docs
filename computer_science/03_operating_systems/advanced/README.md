# Advanced Operating Systems

Roadmap sau [OS foundation](../../basic/03_operating_systems/README.md):

1. [Kernel execution contexts và syscall path](./00_kernel_execution_contexts_and_syscall_path.md)
2. [Scheduler internals, run queue và fairness/latency trade-offs](./01_scheduler_run_queues_fairness_and_latency.md)
3. [Page faults, reclaim, dirty pages và memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md)
4. [Virtual memory internals: page tables, TLB shootdown và huge pages](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md)
5. [Filesystem crash consistency, journaling và copy-on-write](./04_filesystem_crash_consistency_journaling_and_cow.md)
6. [Advanced I/O: epoll, io_uring, zero-copy và DMA](./05_epoll_io_uring_zero_copy_and_dma.md)
7. Containers internals: namespaces, cgroups, capabilities, seccomp
8. Kernel synchronization, RCU và lockless read paths
9. eBPF, tracing và production observability
10. Real-time scheduling và priority inversion

Phần hiện có đã nối syscall/scheduling với memory pressure, virtual-memory translation, durability và asynchronous I/O. Đây là nền để đi tiếp vào containers, kernel synchronization và production tracing.