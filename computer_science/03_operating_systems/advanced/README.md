# Hệ điều hành nâng cao

Bắt đầu từ [nền tảng hệ điều hành](../../basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md).

## Chuẩn gốc (canonical / 정본) chapters

1. [Ngữ cảnh thực thi kernel, synchronization/RCU và đường đi system call](./00_kernel_execution_contexts_and_syscall_path.md)
2. [Scheduler internals, run queue và đánh đổi công bằng/độ trễ](./01_scheduler_run_queues_fairness_and_latency.md)
3. [Page fault, reclaim, dirty page và áp lực bộ nhớ](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md)
4. [Bộ nhớ ảo: page table, TLB shootdown và huge page](./03_virtual_memory_page_tables_tlb_shootdown_and_huge_pages.md)
5. [Tính nhất quán sau crash của filesystem, journaling và copy-on-write](./04_filesystem_crash_consistency_journaling_and_cow.md)
6. [I/O nâng cao: epoll, io_uring, zero-copy và DMA](./05_epoll_io_uring_zero_copy_and_dma.md)
7. [Cơ chế container: namespace, cgroup, capability và seccomp](./06_containers_namespaces_cgroups_capabilities_and_seccomp.md)
8. [RCU, seqlock và safe memory reclamation](./07_rcu_seqlock_and_safe_memory_reclamation.md)
9. [eBPF, tracing, kernel observability và safety boundary](./08_ebpf_tracing_kernel_observability_and_safety.md)

Nhánh học (track / 트랙) này nối lời gọi hệ thống (system call / 시스템 호출)/scheduling với kernel synchronization, đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명), bộ nhớ (memory / 메모리) pressure, address translation, durability, async I/O, isolation và cuối cùng là cách thu bằng chứng vận hành (production evidence / 운영 증거) mà không phá an toàn (safety / 안전)/timing của kernel. Mỗi phần phải chỉ ra tài nguyên (resource / 자원)/kernel bất biến (invariant / 불변식), ngữ cảnh (context / 맥락) nào được phép sleep/preempt, thất bại (failure / 실패) under pressure, hàng đợi (queue / 큐)/wait nào hình thành và bằng chứng (evidence / 증거) nào quan sát được.

Chapter syscall/ngữ cảnh (context / 맥락) giữ overview về synchronization và RCU vì đây là prerequisite để đọc kernel đường dẫn (path / 경로). Chapter RCU/seqlock là chuẩn gốc (canonical / 정본) độ sâu (depth / 깊이) cho publication, grace period, quiescent trạng thái (state / 상태), deferred reclamation, ABA, epoch/hazard-pointer comparison, thử lại (retry / 재시도) starvation và reclamation debt.

Chapter eBPF/tracing không phải danh mục (catalog / 카탈로그) công cụ (tool / 도구). Nó giải thích hook ngữ nghĩa (semantics / 의미론), verifier an toàn (safety / 안전) proof, helper/map ranh giới (boundary / 경계), per-CPU aggregation, ring-buffer pressure, sampling độ lệch (bias / 편향), JIT overhead và cách instrumentation có thể làm thay đổi hiện tượng đang đo. Bằng chứng (evidence / 증거) chỉ có nghĩa khi biết nó được thu tại chuyển tiếp trạng thái (state transition / 상태 전이) nào.

Bằng chứng vận hành (production evidence / 운영 증거) cần nối ứng dụng (application / 애플리케이션) symptom với syscall độ trễ (latency / 지연 시간), blocked/off-CPU ngăn xếp (stack / 스택), wakeup/run-queue delay, interrupt/softirq CPU, khóa (lock / 잠금)/spin contention, page fault/reclaim, khối (block / 블록) I/O, mạng (network / 네트워크) drop/retransmission, cgroup throttling, grace-period/reclamation backlog và tracing mất mát (loss / 손실)/overhead khi phù hợp.

Hai tuyến xuyên tầng bắt buộc: [correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md). Kernel networking chi tiết được đặt tại [Networks & Distributed Systems](../../06_networks_distributed_systems/advanced/08_kernel_packet_path_qdisc_nic_offload_and_observability.md) để tránh duplicate packet ngữ nghĩa (semantics / 의미론).