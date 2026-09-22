# Scheduler internals, run queue và fairness/latency trade-offs

Operating-system scheduler quyết định task nào được chạy trên CPU nào, trong bao lâu và khi nào bị preempt. Ở mức advanced, bài toán không phải nhớ tên scheduling algorithm mà là hiểu invariant của một resource allocator: **CPU time hữu hạn phải được phân phối theo policy trong khi scheduler cố giữ fairness/deadline, hạn chế starvation và không phá locality nhiều hơn mức cần thiết.**

Performance pressure làm bài toán khó vì cùng một quyết định có thể tốt cho fairness nhưng xấu cho cache locality, tốt cho throughput nhưng xấu cho wake-up latency.

## 1. Runnable không có nghĩa đang chạy

Một task có thể đang running, runnable nhưng chờ CPU, sleeping/blocked vì I/O hoặc synchronization, hoặc stopped. Scheduler chủ yếu lựa chọn trong tập **runnable tasks**.

Nếu một service có 64 runnable threads trên 8 cores, phần lớn threads đang chờ CPU dù process không “blocked” theo nghĩa I/O. Đây là queueing ở tầng OS:

```text
arrival of runnable work
→ per-CPU run queue
→ CPU service time
→ completion/block/preemption
```

Khi arrival pressure gần CPU service capacity, scheduler delay trở thành thành phần của tail latency.

## 2. Per-CPU run queue: giảm contention nhưng tạo bài toán cân bằng

Một global queue duy nhất trên multicore vừa tạo lock/contention vừa làm task dễ nhảy core và mất cache warmth. Kernel hiện đại thường giữ scheduling state theo CPU hoặc theo cấu trúc có tính cục bộ cao.

Điều này tạo trade-off nền tảng:

```text
keep task local  <------>  migrate task
cache/NUMA warmth          load balance/fairness
```

Nếu CPU A có queue dài còn CPU B rảnh, migration có thể giảm wait. Nhưng migrate task có working set lớn sang core/socket khác có thể tăng cache miss và remote NUMA access.

Invariant không phải “queue mọi CPU luôn bằng nhau”. Mục tiêu là policy-level fairness/capacity mà vẫn giữ locality hợp lý.

## 3. Fairness là policy theo thời gian

Round-robin là mental model dễ hiểu nhưng production scheduler thường cần weighted fairness. Linux CFS lịch sử dùng **virtual runtime** để biểu diễn lượng CPU service đã nhận tương đối theo weight; implementation scheduler có thể thay đổi qua kernel versions, nhưng mental model bền hơn tên cấu trúc dữ liệu cụ thể.

Fairness cần trả lời câu hỏi: trong một window đủ dài, task runnable liên tục nhận bao nhiêu CPU so với weight/policy của nó?

Fairness không đồng nghĩa latency tối thiểu. Một task có thể nhận “phần CPU công bằng” nhưng wake-up phải chờ quá lâu đối với request latency-sensitive.

## 4. Wake-up path và latency

Một server thread thường:

```text
sleep/block chờ socket/futex/timer
→ event/interrupt xảy ra
→ kernel đánh thức task
→ chọn target CPU
→ enqueue runnable
→ có thể preempt task hiện tại
→ thread thật sự chạy application code
```

Thời gian từ wake-up tới execution là **scheduler latency**. Khi run queue dài hoặc CPU bị throttled, request có thể mất phần lớn latency budget trước khi handler thực thi instruction hữu ích nào.

Đây là lower layer thường bị che bởi application tracing nếu span chỉ bắt đầu sau khi worker được schedule.

## 5. Context switch cost không chỉ là save/restore register

Direct context-switch work gồm lưu/khôi phục architectural state, scheduler accounting và có thể address-space-related state. Nhưng indirect cost thường lớn hơn:

```text
cache working set bị thay
TLB locality thay đổi
branch predictor/pipeline phải warm lại
NUMA locality có thể xấu đi
```

Quantum quá nhỏ tăng responsiveness nhưng tăng switching/locality cost. Quantum quá lớn amortize overhead tốt nhưng làm interactive/wakeup latency xấu.

Vì vậy “nhiều threads để tận dụng CPU” chỉ đúng tới điểm concurrency còn tạo useful parallelism. Sau đó scheduler và cache interference có thể làm service time tăng.

## 6. CPU affinity và pinning là constraint, không phải default optimization

**CPU affinity (CPU 친화성)** giới hạn task chạy trên tập CPU nhất định. Pinning có thể hữu ích cho benchmark ổn định, latency-sensitive workload, cache locality hoặc NUMA placement.

Nhưng pinning sai tạo hotspot và ngăn scheduler dùng idle capacity. Nếu memory của task nằm chủ yếu ở node khác, pinning còn có thể cố định remote-memory penalty.

Trước khi pin, cần có hypothesis và evidence: migration có thật sự là bottleneck hay không?

## 7. NUMA nối scheduler với memory subsystem

Trên NUMA machine, “CPU balance” và “memory locality” có thể xung đột. Task chạy trên node 0 nhưng working pages ở node 1 tạo remote accesses; migrate task hoặc migrate pages đều có cost.

Vì vậy performance anomaly có thể xuất hiện như scheduler/load issue nhưng tầng dưới quyết định cost là interconnect + memory placement. Đọc cùng [NUMA và scalable coherence](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md).

## 8. Priority inversion: scheduling và synchronization giao nhau

High-priority task có thể chờ lock do low-priority task giữ. Nếu medium-priority tasks liên tục preempt low-priority holder, high-priority task bị trì hoãn gián tiếp. Đây là **đảo ngược ưu tiên (priority inversion / 우선순위 역전)**.

Priority inheritance tạm nâng priority của lock holder để nó hoàn tất critical section. Bài học rộng hơn: scheduler policy không thể reasoning tách khỏi lock ownership và blocking graph.

Invariant real-time không phải “task priority cao luôn chạy”. Nó là deadline/blocking bound có thể chứng minh dưới assumptions của scheduler + synchronization protocol.

## 9. Real-time khác với “nhanh”

Real-time quan tâm bounded worst-case/known latency hơn average speed. Task trung bình 1 ms nhưng đôi lúc 100 ms có thể không phù hợp deadline 10 ms, trong khi task ổn định 5 ms lại phù hợp hơn.

Hard real-time đòi hỏi control chặt scheduling, interrupt, memory allocation, locks và I/O. Soft real-time chấp nhận một số misses nhưng vẫn cần tail-bound reasoning.

## 10. cgroup, VM và scheduler tạo thêm resource boundaries

Trong container, CPU quota/weight có thể throttle workload dù host còn idle CPU theo cách nhìn tổng quát. Trong VM, **steal time** cho thấy vCPU runnable nhưng hypervisor chưa cấp physical CPU.

Do đó invariant “service có 4 vCPU” không đồng nghĩa bốn cores luôn available. Capacity thực tế phụ thuộc scheduler ở nhiều tầng:

```text
application workers
→ guest/container scheduler boundary
→ host scheduler
→ physical CPU
```

## 11. Failure modes dưới performance pressure

Scheduler hiếm khi “crash” application theo nghĩa logic, nhưng pressure có thể tạo failure behavior cấp hệ thống:

```text
run queue dài → wake-up latency tăng → timeout
threads quá nhiều → context-switch/cache interference → service time tăng
CPU throttle → queue tăng dù host utilization nhìn chưa đầy
priority inversion → deadline miss
bad affinity → hotspot + remote NUMA access
```

Các failure này thường feedback sang retry/overload ở tầng application.

## 12. Production evidence

CPU utilization một mình không đủ. Khi điều tra scheduler pressure, cần kết hợp:

```text
per-CPU utilization và runnable queue
voluntary/involuntary context switches
scheduler/run-queue latency
CPU migrations và affinity
cgroup throttled time/quota pressure
VM steal time nếu có
NUMA local/remote memory evidence
on-CPU vs off-CPU profile
```

Linux có nhiều facility như scheduler tracepoints, `perf`, pressure metrics và eBPF-based tooling; tên tool có thể thay nhưng evidence model không đổi: **task runnable từ lúc nào, thật sự chạy lúc nào, bị preempt/block bởi gì, trên CPU/node nào**.

## 13. Connection với queueing/backpressure

Run queue là một queue giống nhiều queue khác trong system. Nếu application tiếp tục accept work trong khi CPU already saturated, queue debt tăng rồi deadline hết hạn. Admission control ở tầng application có thể bảo vệ scheduler khỏi phải giữ quá nhiều runnable work.

Đây là lý do concurrency limit thường tốt hơn “spawn thêm threads khi chậm”. Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 14. Mô hình tư duy

> Scheduler là resource allocator theo thời gian trên topology CPU/NUMA. **Run queue biểu diễn demand chưa được CPU phục vụ; policy quyết định fairness/priority; preemption/migration đổi latency và locality; production evidence phải tách useful CPU work khỏi queueing, throttling và interference.** Khi pressure tăng, scheduler behavior trở thành một phần của end-to-end latency chứ không còn là chi tiết “bên dưới OS”.

## Kết nối

Đọc tiếp [Page faults, reclaim và memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [NUMA architecture](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md), [End-to-end request latency](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).