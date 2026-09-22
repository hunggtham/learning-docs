# Độ trễ, thông lượng, năng lực xử lý và khả năng mở rộng

Kỹ thuật hiệu năng (performance engineering) không đơn giản là “làm mã chạy nhanh”. Một hệ thống là dòng công việc đi qua CPU, cache, memory, scheduler, runtime, network, database và storage; mỗi tầng có service time, queue và giới hạn riêng. Tối ưu đúng bắt đầu bằng một câu hỏi có thể kiểm chứng: **work đang chờ ở đâu, resource nào đang giới hạn progress, và invariant nào về latency/throughput phải được giữ khi load tăng?**

Performance tốt không phải maximum benchmark number. Với production system, mục tiêu thường là giữ latency distribution, throughput, cost và reliability trong một **safe operating envelope** dưới workload thực tế.

## 1. Latency và throughput là hai trục khác nhau

**Độ trễ (latency / 지연 시간)** là thời gian một operation hoàn thành. **Thông lượng (throughput / 처리량)** là số operation hoàn thành trên một đơn vị thời gian.

Hai metric liên quan nhưng không đồng nhất. Batching có thể tăng throughput vì amortize fixed cost nhưng làm request đầu batch phải chờ. Tăng concurrency có thể tăng throughput đến một điểm, rồi contention và queueing làm latency tăng mạnh mà throughput hầu như không tăng nữa.

Một design cần nói rõ objective nào quan trọng hơn theo workload: interactive API ưu tiên tail latency; offline batch có thể chấp nhận latency lớn để đổi lấy throughput/cost tốt hơn.

## 2. Service time và waiting time phải được tách ra

End-to-end latency có thể được xem gần đúng như:

```text
latency = useful/service time + waiting/queueing time + coordination overhead
```

Nếu database query execute 20 ms nhưng request chờ connection pool 300 ms, tối ưu query chỉ chạm một phần nhỏ latency. Nếu CPU handler chỉ dùng 5 ms nhưng thread chờ run queue 100 ms, application profiler chỉ đo on-CPU code sẽ bỏ mất bottleneck.

Advanced diagnosis luôn hỏi: **thời gian được dùng để làm việc hay để chờ quyền dùng resource?**

## 3. Utilization gần capacity làm queue nhạy với variance

Khi arrival rate `λ` tiến gần service rate `μ`, một burst nhỏ hoặc vài request chậm có thể tạo queue. Mô hình M/M/1 đơn giản với `ρ = λ/μ` chỉ là approximation, nhưng intuition quan trọng vẫn đúng: khi `ρ` tiến gần 1, waiting time tăng rất nhanh.

Production workload thường tệ hơn model lý tưởng vì service time không exponential đẹp, arrivals bursty, dependencies correlated và resource có nhiều classes. Vì vậy target 100% utilization cho user-facing workload thường đồng nghĩa không còn headroom hấp thụ variance.

## 4. Little's Law nối concurrency, latency và throughput

Trong stable system:

\[
L = \lambda W
\]

`L` là average work in-flight, `λ` là throughput/arrival rate ổn định, `W` là average time trong system.

Nếu service hoàn thành 1.000 req/s và average latency 0,2 s, khoảng 200 requests tồn tại trong system trung bình.

Little's Law không dự đoán p99, nhưng rất mạnh để sanity-check. Nếu team nói service cần 10.000 req/s, mỗi request giữ DB connection trung bình 100 ms, thì workload đó đã hàm ý khoảng 1.000 concurrent connection-hold time nếu không thay architecture/parallelism. Một pool 50 connections không thể giữ cùng contract chỉ bằng “tuning”.

## 5. Bottleneck là resource làm giới hạn throughput hoặc latency hiện tại

Một system có nhiều resources, nhưng tại một operating point thường có một hoặc vài resources đang giới hạn progress: CPU execution, memory bandwidth, run queue, GC, lock, connection pool, DB I/O, WAL flush, network bandwidth hoặc downstream quota.

Tăng tốc phần không phải bottleneck chỉ cải thiện tổng thể rất ít. Đây là intuition của Amdahl: speedup toàn hệ thống bị giới hạn bởi phần thời gian không được cải thiện.

Quan trọng hơn, bottleneck **di chuyển**. Sau khi giảm CPU cost, database có thể trở thành giới hạn mới; sau khi thêm replica, network hoặc storage trở thành giới hạn tiếp theo. Performance engineering là vòng lặp đo → giả thuyết → thay đổi → đo lại, không phải một lần tối ưu.

## 6. CPU utilization không nói CPU đang làm gì

CPU 100% có thể là useful compute, spin lock, GC, scheduler overhead hoặc retry loop. CPU 40% cũng không chứng minh service có headroom nếu bottleneck là single-thread event loop, DB pool, lock hay storage.

Ở tầng CPU, IPC, cache/TLB miss, branch miss, stalled cycles và memory bandwidth có thể giải thích vì sao cùng 100% CPU nhưng throughput khác nhau. Ở tầng OS, run queue/context switch/throttling cho biết runnable work có đang phải chờ hay không.

Do đó utilization chỉ là symptom-level signal. Cần attribution xuống mechanism.

## 7. Memory hierarchy làm Big-O chưa đủ để dự đoán performance

Hai thuật toán cùng `O(n)` có thể khác rất xa nếu một bên sequentially scan contiguous array còn bên kia pointer-chase qua random heap nodes.

Cache line, TLB, prefetcher, NUMA và memory bandwidth quyết định cost của data movement. Khi working set không fit cache, arithmetic có thể rẻ hơn rất nhiều so với chờ memory.

Đây là lý do data layout, locality và allocation strategy là performance concepts ngang hàng với algorithmic complexity trong systems code.

Đọc [memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md) và advanced Architecture để nối tới hardware evidence.

## 8. Concurrency tạo parallelism nhưng cũng tạo contention

Tăng workers/threads chỉ giúp khi workload có independent work và resource phía dưới còn capacity. Khi nhiều workers cùng tranh lock, cache line, DB row, connection pool hoặc memory bandwidth, concurrency tăng có thể làm **service time tự xấu đi**.

Một đường cong phổ biến:

```text
concurrency thấp  → resource chưa dùng hết → throughput tăng
concurrency vừa   → gần điểm hiệu quả nhất
concurrency cao   → queue + contention + cache/scheduler overhead tăng
                   → latency tăng mạnh, throughput phẳng hoặc giảm
```

Vì vậy concurrency limit là một performance control, không chỉ reliability control.

## 9. Tail latency quan trọng vì fan-out khuếch đại phần đuôi

Average che slow outliers. Nếu một request cần kết quả từ nhiều dependencies/shards, end-to-end latency bị chi phối bởi slow branch cần thiết nhất.

Fan-out càng lớn, xác suất gặp ít nhất một tail event càng cao. Vì vậy p95/p99 của downstream không thể cộng/trừ đơn giản để suy ra p99 của system.

Performance test cần đo distribution, không chỉ mean. Với SLO, cần biết p50 cho normal path nhưng cũng phải quan sát p95/p99 và timeout rate dưới load.

## 10. Batching amortize fixed cost nhưng đổi queueing behavior

Batching chia sẻ cost như syscall, network round-trip, disk flush, transaction commit hoặc GPU kernel launch.

Nhưng batch phải chờ hình thành; batch lớn giữ memory nhiều hơn, tăng head-of-line delay và tăng blast radius nếu failure xảy ra.

Group commit trong database là ví dụ rõ: nhiều transaction dùng chung một WAL flush để tăng throughput, nhưng batching policy vẫn phải giữ durability invariant trước khi acknowledgement.

Optimization tốt đổi timing/cost, không âm thầm đổi correctness contract.

## 11. Cache là trade-off giữa reuse và consistency

Cache có lợi khi reuse probability cao và cache hit rẻ hơn source lookup đủ nhiều. Nhưng cache tạo thêm state cần eviction, invalidation và capacity management.

Metrics cần tách hit ratio với **miss cost**. Hit ratio 99% vẫn có thể tệ nếu 1% miss cực đắt và nằm trong tail-critical path.

Cache stampede, hot key và stale data là failure modes xuất hiện khi load tăng. Advanced cache reasoning nằm ở [caching consistency, invalidation, stampede và hot keys](../../08_software_systems/advanced/02_caching_consistency_invalidation_stampede_and_hot_keys.md).

## 12. Connection pool là queue + admission-control boundary

Connection pool tái sử dụng setup cost và giới hạn concurrency xuống downstream.

Pool quá nhỏ làm request chờ; pool quá lớn có thể làm database nhận quá nhiều simultaneous work, tăng lock/I/O/cache pressure. Tăng pool size thường chỉ **di chuyển queue** từ application sang database chứ không xóa queue.

Khi debug, đo riêng:

```text
acquire wait
active connections
query service time
transaction lifetime
DB saturation/wait class
```

Đừng chỉ nhìn query execution duration.

## 13. Vertical scaling và horizontal scaling giải các constraint khác nhau

Vertical scaling tăng resource của một node và thường giữ architecture đơn giản hơn. Horizontal scaling thêm nodes nhưng chỉ giúp nếu work có thể partition và shared bottleneck không trở thành giới hạn.

Thêm application replicas không tăng DB write capacity nếu mọi replicas cùng tranh một database. Sharding có thể tăng capacity nhưng thêm routing, rebalancing, cross-shard transaction và hotspot risk.

“Scale out” là thay architecture của resource graph, không phải phép nhân capacity tự động.

## 14. Backpressure và admission control giữ system trước utilization knee

Khi demand vượt capacity, system cần một nơi nói “đủ rồi”. Bounded queues, concurrency semaphore, token/rate limits và load shedding tạo explicit control.

Unbounded queue biến overload thành latency debt. Request đã quá deadline nhưng vẫn chờ/được xử lý là wasted work.

Performance và reliability gặp nhau ở đây: bảo vệ latency của accepted work đôi khi cần reject một phần arrivals sớm.

Đọc [capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

## 15. Retry có thể biến performance regression thành outage

Một dependency chậm làm timeout; caller retry; attempts tăng arrival rate; queue dài hơn; service time xấu đi; timeout tiếp tục tăng.

```text
slowdown → timeout → retry → overload → longer queue → more timeout
```

Vì vậy retry rate là performance metric, không chỉ error-handling metric. Deadline propagation, cancellation, backoff+jitter và retry budget giúp giới hạn amplification nhưng không tạo capacity nếu bottleneck vẫn saturated.

## 16. Warm state và transient state phải được tách

JIT compilation, cache warming, connection establishment, DNS/TLS setup, page faults và model/data loading làm cold behavior khác steady state.

Benchmark chỉ đo warm steady-state có thể bỏ startup/cold failover; benchmark chỉ đo cold có thể đánh giá thấp steady-state throughput.

Deployment, autoscaling và failover đều tạo transient state, nên capacity plan phải giữ headroom cho warm-up phase.

## 17. Coordinated omission và benchmark methodology

Load generator cũng có thể nói dối. Nếu generator gửi request tiếp theo chỉ sau request trước hoàn thành, khi server chậm nó vô tình giảm arrival rate và bỏ sót queueing mà real clients vẫn tạo. Đây là một dạng **coordinated omission**.

Load test cần mô hình arrivals gần workload thật, giữ request timestamps/deadlines, report latency distribution và không âm thầm hạ pressure khi server chậm nếu production behavior không như vậy.

Measurement error là một failure mode của performance engineering.

## 18. Production evidence cần đi từ SLO xuống resource

Một workflow thực tế:

```text
1. xác định user-visible SLI/SLO hoặc performance invariant
2. chọn slow percentile/failed window
3. lấy trace đại diện critical path
4. tách service time và queue wait ở từng boundary
5. correlate resource saturation đúng layer
6. profile on-CPU/off-CPU hoặc hardware/runtime mechanism khi cần
7. thay đổi một hypothesis rồi đo lại
```

Evidence có thể gồm trace, queue wait, CPU profile, run queue, GC pause/allocation, cache/TLB/PMU counters, DB waits, I/O latency, retransmission và replica lag. Không cần luôn thu mọi metric; chọn metric theo hypothesis.

## 19. Performance optimization phải giữ invariant correctness/reliability

Một optimization không hợp lệ nếu đạt benchmark bằng cách làm yếu contract không được công bố: bỏ fsync, giảm isolation không được phép, bỏ auth, drop validation, dùng stale cache vượt requirement hoặc tăng retry vô hạn để che error.

Khi đánh đổi có chủ đích, API/SLO phải nói rõ semantics mới. Performance là quality attribute nằm dưới correctness constraints, không phải lý do để phá chúng.

## 20. Mô hình tư duy

> Hiệu năng là **dòng công việc qua các service centers hữu hạn**. Data locality quyết định cost bên trong CPU/memory; scheduler/runtime quyết định khi work được chạy; pools/queues quyết định khi work được vào resource; network/database/storage quyết định downstream service time. Khi load tăng, waiting time và contention thường thay đổi behavior trước khi throughput đạt cực đại. Tối ưu đúng là tìm bottleneck bằng evidence và giữ system trong safe operating envelope.

## Những hiểu nhầm thường gặp

**“CPU 100% nghĩa là tối ưu.”** Có thể CPU đang spin, GC hoặc scheduler overhead trong khi useful throughput kém.

**“Thêm threads luôn tăng throughput.”** Chỉ tới khi independent work và downstream capacity còn đủ; sau đó contention/queueing có thể làm tệ hơn.

**“Average latency đủ để benchmark.”** Tail và workload mix mới quyết định nhiều production SLO.

**“Scale horizontal giải mọi bottleneck.”** Shared state, database, network hoặc coordination có thể trở thành bottleneck mới.

## Kết nối

Đọc cùng [Architecture memory hierarchy](../02_computer_architecture/02_memory_hierarchy_and_cache.md), [OS scheduler advanced](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [Runtime GC](../../04_programming_languages/advanced/06_garbage_collection_generational_concurrent_compacting_and_barriers.md), [Queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [End-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).