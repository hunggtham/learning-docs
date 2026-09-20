# Advanced Operating Systems

Roadmap sau [OS foundation](../../basic/03_operating_systems/README.md):

1. [Kernel execution contexts và syscall path](./00_kernel_execution_contexts_and_syscall_path.md)
2. [Scheduler internals, run queue và fairness/latency trade-offs](./01_scheduler_run_queues_fairness_and_latency.md)
3. [Page faults, reclaim, dirty pages và memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md)
4. Virtual memory internals: page tables, TLB shootdown, huge pages
5. Filesystem crash consistency, journaling và copy-on-write
6. Advanced I/O: epoll/kqueue/io_uring, zero-copy và DMA
7. Containers internals: namespaces, cgroups, capabilities, seccomp
8. Kernel synchronization, RCU và lockless read paths
9. eBPF, tracing và production observability
10. Real-time scheduling và priority inversion

Phần đã triển khai hiện nối execution path với scheduler và memory pressure để người đọc có thể reasoning latency từ syscall tới CPU scheduling và reclaim.