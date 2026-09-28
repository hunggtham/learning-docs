# Hệ điều hành nâng cao

> **Mạch đọc:** Đọc **Hệ điều hành nâng cao** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Hãy xác định đối tượng và câu hỏi trung tâm trước, rồi dùng phần này để đối chiếu với mục liên quan sau khi đã nắm mô hình tư duy (mental model / 사고 모델) chính.


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
9. [eBPF, tracing kernel, observability và safety](./08_ebpf_tracing_kernel_observability_and_safety.md)

Nhánh học (track / 트랙) này nối lời gọi hệ thống (system call / 시스템 호출)/scheduling với kernel synchronization, đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명), bộ nhớ (memory / 메모리) pressure, address translation, durability, async I/O và isolation. Mỗi phần phải chỉ ra tài nguyên (resource / 자원)/kernel bất biến (invariant / 불변식), ngữ cảnh (context / 맥락) nào được phép sleep/preempt, thất bại (failure / 실패) under pressure, hàng đợi (queue / 큐)/wait nào hình thành và bằng chứng vận hành (production evidence / 운영 증거) nào quan sát được.

Chapter syscall/ngữ cảnh (context / 맥락) vẫn giữ overview về synchronization và RCU vì đây là prerequisite để đọc kernel đường dẫn (path / 경로). Chapter RCU/seqlock mới là chuẩn gốc (canonical / 정본) độ sâu (depth / 깊이) cho publication, grace period, quiescent trạng thái (state / 상태), deferred reclamation, ABA, epoch/hazard-pointer comparison, thử lại (retry / 재시도) starvation và bằng chứng vận hành (production evidence / 운영 증거) của reclamation debt. Chapter eBPF/tracing sở hữu lập luận (reasoning / 추론) đường dẫn (path / 경로) từ probe attachment → verifier/JIT → helper/map/ring-buffer → sự kiện (event / 이벤트) mất mát (loss / 손실)/overhead → packet vòng đời (lifecycle / 생명주기)/hàng đợi (queue / 큐) ranh giới (boundary / 경계) → bằng chứng vận hành (production evidence / 운영 증거) và an toàn (safety / 안전) ranh giới (boundary / 경계). Nội dung mới không biến synchronization hoặc khả năng quan sát (observability / 관측 가능성) thành danh sách thành phần nguyên thủy (primitive / 기본 요소)/công cụ (tool / 도구); trọng tâm vẫn là trạng thái (state / 상태)/thời gian tồn tại (lifetime / 수명) proof và bằng chứng (evidence / 증거) chất lượng (quality / 품질).

Kernel networking đường dẫn (path / 경로) đã được deepen trong chapter eBPF qua ingress/egress vòng đời (lifecycle / 생명주기), NAPI/softirq, socket/qdisc boundaries, GRO/GSO, drop-vs-delay-vs-retransmission và flow-correlated bằng chứng (evidence / 증거). Bước tiếp theo là validate trên tải công việc (workload / 워크로드)/driver cụ thể nếu có sự cố (incident / 인시던트) thực tế; không mở chapter riêng chỉ để lặp lại packet-path overview.

Bằng chứng vận hành (production evidence / 운영 증거) cần nối ứng dụng (application / 애플리케이션) symptom với syscall độ trễ (latency / 지연 시간), blocked/off-CPU ngăn xếp (stack / 스택), wakeup/run-queue delay, interrupt/softirq CPU, khóa (lock / 잠금)/spin contention, page fault/reclaim, khối (block / 블록) I/O, mạng (network / 네트워크) drop/retransmission, cgroup throttling và khi phù hợp grace-period/reclamation backlog. công cụ (tool / 도구) name có thể thay đổi; bằng chứng (evidence / 증거) mô hình (model / 모델) không đổi.

Hai tuyến xuyên tầng bắt buộc: [correctness path](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md) và [durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **chuẩn gốc (canonical / 정본) chapters**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kernel execution contexts and syscall path](./00_kernel_execution_contexts_and_syscall_path.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
