# Capacity planning, utilization knee và admission control

Capacity planning không phải lấy peak traffic rồi cộng 20%. Một service có thể vẫn còn throughput capacity nhưng tail latency đã tăng mạnh vì queueing và contention. Ở mức advanced, cần giữ một invariant vận hành: **accepted work phải nằm trong vùng mà system còn đủ resource để hoàn thành trước deadline với xác suất/SLO đã công bố.**

Khi system tiếp tục accept work sau vùng đó, queue debt, timeout và retry có thể biến slowdown thành overload collapse.

## 1. Capacity là một safe operating envelope

Một service có nhiều bottleneck resources: CPU, memory/GC, thread hoặc event-loop concurrency, DB connections, sockets/file descriptors, I/O bandwidth, network bandwidth, downstream quota và locks/shared state.

Throughput tối đa bị giới hạn bởi resource đầu tiên saturate hoặc bởi interaction giữa nhiều resources. CPU 40% không chứng minh service còn nhiều capacity nếu DB pool đã 100% busy.

Capacity vì vậy là một **vùng đa chiều**, không phải một số RPS duy nhất.

## 2. Utilization knee quan trọng hơn maximum throughput

Khi arrival rate tiến gần service capacity, variance nhỏ cũng tạo queue. Latency thường cong mạnh trước khi resource đạt 100%.

Điểm chuyển từ “service time chi phối” sang “queue wait chi phối” thường được gọi không chính thức là **utilization knee**.

Latency-sensitive system nên operate trước vùng này và giữ headroom cho burst, deploy, instance failure hoặc downstream degradation.

## 3. Little's Law nối throughput, concurrency và latency

Trong stable system:

```text
L = λW
```

`L` là số request trung bình trong system, `λ` throughput/arrival rate, `W` average time trong system.

Nếu throughput 1,000 req/s và average end-to-end time 0.2 s, trung bình khoảng 200 requests đang in-flight.

Little's Law không mô tả tail distribution, nhưng là sanity check mạnh để phát hiện pool/concurrency assumptions phi thực tế.

## 4. Service-time distribution quan trọng hơn average

Nếu 99% requests mất 5 ms nhưng 1% mất 1 s, slow requests giữ worker/connection lâu và có thể gây head-of-line blocking.

Capacity model cần workload mix, percentile service time và dependency behavior. Average service time có thể che đúng class request đang giữ resource lâu nhất.

## 5. Concurrency limit là một control boundary

Tăng threads/connections vô hạn không tăng throughput vô hạn. Sau một mức, context switch, cache miss, GC, lock contention và downstream saturation làm **service time tự tăng**.

Concurrency limiting đặt upper bound active work. Excess work có thể queue có giới hạn hoặc bị reject sớm.

Mục tiêu không phải giữ mọi request “đã được nhận”, mà giữ active set trong vùng mà resource còn làm useful progress.

## 6. Admission control quyết định work có được vào expensive path hay không

Admission control có thể dựa trên semaphore, queue length, token/rate budget, tenant quota hoặc estimated request cost.

Một `429/503` nhanh đôi khi đúng hơn accept rồi timeout 30 giây. Reject sớm bảo vệ resource cho work đã nhận và cho caller signal rõ để backoff hoặc degrade.

Invariant là rejection phải xảy ra **trước** khi request tiêu quá nhiều resource khan hiếm.

## 7. Bounded queue biến overload thành failure hữu hạn

Unbounded queue không loại failure; nó đổi failure thành latency và memory debt.

Nếu worker service time là 100 ms nhưng queue cho phép hàng chục nghìn requests, nhiều request đã chắc chắn vượt deadline ngay lúc enqueue.

Queue capacity cần liên hệ với latency budget và cancellation semantics. Work đã hết deadline không nên tiếp tục giữ slot nếu có thể hủy an toàn.

## 8. Retry amplification tạo positive feedback loop

Client timeout nhưng server vẫn xử lý. Client retry tạo thêm attempt. Load tăng làm queue dài, service time xấu, thêm timeout và thêm retry.

```text
slowdown
→ timeout
→ retry
→ arrival rate tăng
→ queue + contention tăng
→ service time tăng
→ nhiều timeout hơn
```

Mitigation gồm bounded retries, exponential backoff, jitter, retry budget, deadline propagation và idempotency. Nhưng nếu dependency hết capacity kéo dài, retry policy không tạo capacity; admission/backpressure vẫn cần.

## 9. Concurrency limit khác rate limit

Rate limit kiểm soát arrivals per time. Concurrency limit kiểm soát active work.

Operation 5 ms và 5 s có thể cùng QPS nhưng resource footprint khác rất nhiều. Với service time biến động, concurrency thường phản ánh pressure trực tiếp hơn rate.

Nhiều system cần cả hai: rate để bảo vệ abuse/burst, concurrency để bảo vệ finite downstream capacity.

## 10. Adaptive concurrency là control theory problem

Static limit có thể sai khi downstream capacity thay đổi. Adaptive controller quan sát latency/error/queue rồi điều chỉnh concurrency.

Phản ứng quá nhanh gây oscillation; quá chậm cho overload lan rộng. Measurement delay và noisy tail metrics có thể làm controller chase noise.

Adaptive limit phải reasoning như feedback controller, không phải magic autoscaling switch.

## 11. Bulkhead tạo failure-domain boundary

Chia resource pools theo workload/tenant có thể ngăn một class ăn hết capacity.

Ví dụ background export và user-facing request dùng pools riêng. Điều này có thể làm tổng utilization kém tối ưu ở một số thời điểm, nhưng tăng fault isolation.

Isolation chỉ thật khi resource được reserve/partition ở layer bottleneck. Hai logical priority classes cùng dùng một exhausted DB pool không phải bulkhead thực sự.

## 12. Headroom cho failure và deploy

Cluster 10 nodes muốn chịu mất 2 nodes thì 8 nodes còn lại phải tiếp tục nằm trước utilization knee. Rolling deployment, autoscaling warm-up, zone failure và cache cold-start đều tiêu headroom.

Capacity planning vì thế là reliability requirement, không chỉ cost optimization.

## 13. Autoscaling không thay admission control

Autoscaler phản ứng sau metric change và instance cần startup/warmup. Burst có thể phá system trước khi scale-out hoàn tất.

Admission control/load shedding bảo vệ trong transient window đó. Scale-out cũng không giúp nếu bottleneck là DB, shared lock hoặc downstream quota.

## 14. Graceful degradation phải giữ correctness-critical invariant

Khi overload, system có thể bỏ optional enrichment, phục vụ stale cache, giảm chất lượng recommendation hoặc reject low-priority work.

Nhưng không được “degrade” bằng cách bỏ authorization, durability hoặc business validation chỉ để giữ success rate. Degradation policy cần phân biệt optional quality với correctness/security invariant.

## 15. Production evidence

Capacity diagnosis cần kết hợp arrival rate và completion rate, active concurrency, queue depth + queue wait, service-time distribution, retry/attempt rate, resource saturation tại bottleneck, rejection/load-shed count và remaining deadline/cancellation rate.

Nếu throughput đứng yên nhưng concurrency/queue tăng, system đang tích debt. Nếu CPU thấp mà pool wait cao, bottleneck nằm downstream/resource khác.

Load test cần workload mix và failure mode gần production; benchmark single endpoint happy path không đủ để tìm safe envelope.

## 16. Lower abstraction nào quyết định behavior?

Nếu application queue tăng vì CPU run queue dài, scheduler là lower layer. Nếu DB pool full vì lock waits, database concurrency control quyết định capacity. Nếu write latency tăng vì storage flush, durability path quyết định service time. Nếu TLS/KMS dependency chậm, security control plane cũng có thể trở thành capacity bottleneck.

Capacity model chỉ đúng khi biết resource thật sự đang giới hạn progress.

## 17. Whole-system profiling bắt đầu từ time decomposition

Một request mất 500 ms không đồng nghĩa CPU đã dùng 500 ms. Wall-clock time có thể gồm queue wait, scheduler delay, lock wait, page fault, network wait, DB pool wait, storage flush và chỉ một phần nhỏ on-CPU execution.

**Lập hồ sơ toàn hệ thống (whole-system profiling / 전체 시스템 프로파일링)** cần tách ít nhất:

```text
queueing time
on-CPU time
off-CPU blocked/waiting time
runtime pause/GC
network/downstream wait
storage I/O wait
```

CPU flame graph rất hữu ích khi work thật sự on-CPU. Nhưng nếu thread ngủ chờ mutex hoặc socket, flame graph on-CPU có thể nhìn “khỏe” trong khi user latency rất xấu.

## 18. On-CPU và off-CPU trả lời hai câu hỏi khác nhau

**On-CPU profiling** hỏi CPU cycles đang được tiêu ở code path nào. Nó giúp tìm serialization, hashing, regex, GC work, lock spinning, compression hoặc algorithm hot path.

**Off-CPU profiling** hỏi execution context đang bị block ở đâu: futex/mutex, condition variable, socket, disk I/O, page fault hoặc scheduler wait.

Một lock contention incident có thể có CPU tổng thể thấp vì đa số threads ngủ; tăng CPU cores không giải quyết. Ngược lại spin lock có thể làm CPU 100% nhưng useful throughput không tăng.

Evidence phải khớp failure mechanism, không phải tool quen tay nhất.

## 19. Scheduler evidence nối application concurrency với CPU reality

Application có thể báo 200 runnable workers, nhưng máy chỉ có 8 cores. Khi runnable set lớn hơn execution capacity, run queue và context switching tăng. Thread migration còn làm cache locality xấu hơn.

Useful evidence gồm run-queue length, runnable-vs-blocked threads, scheduler delay, context switches và CPU migrations. Nếu p99 request tăng đúng lúc run queue tăng dù handler compute không đổi, capacity boundary nằm ở scheduling contention chứ không phải network.

Logical concurrency, OS runnable concurrency và physical cores là ba tầng khác nhau.

## 20. PMU counters cho biết CPU chờ cái gì, nhưng cần hypothesis trước

**Bộ đếm hiệu năng phần cứng (Performance Monitoring Unit counters, PMU / 성능 모니터링 카운터)** có thể cung cấp evidence về cycles, instructions, cache misses, branch misses, stalled cycles, memory bandwidth hoặc cache-to-cache traffic tùy CPU/model/tool.

Counter không tự giải thích root cause. LLC miss cao có thể hợp lý với streaming workload; branch miss thấp không chứng minh code tối ưu; event names khác giữa architectures.

Cách dùng đúng là bắt đầu bằng hypothesis, ví dụ “throughput dừng tăng vì memory bandwidth”, rồi tìm evidence tương ứng.

## 21. Roofline reasoning phân biệt compute-bound và bandwidth-bound

Một workload thực hiện nhiều phép tính trên mỗi byte dữ liệu có **cường độ tính toán (operational intensity / 연산 집약도)** cao và có thể tiến gần compute limit. Workload đọc lượng lớn memory để làm ít arithmetic thường bị memory-bandwidth limit trước.

Mental model roofline đơn giản:

```text
performance thực tế
≤ min(compute ceiling,
      memory bandwidth × operational intensity)
```

Nếu workload bandwidth-bound, tăng core count có thể làm các cores tranh cùng memory channels và không tăng throughput. Tối ưu data layout/cache reuse có thể giá trị hơn vectorizing thêm arithmetic.

## 22. I/O queue depth cũng có utilization knee

Storage throughput có thể tăng khi nhiều operations in-flight vì device có parallelism. Nhưng queue depth quá cao làm requests chờ lâu trước device và tail latency tăng.

Network NIC, NVMe, remote storage và database connection pool đều có biến thể của cùng pattern: cần đủ concurrency để giữ pipeline bận, nhưng không để queue debt vượt latency budget.

Với latency-sensitive foreground work, background compaction/checkpoint có thể cần throttle dù bandwidth chưa đạt peak benchmark đẹp nhất.

## 23. Cost/performance phải tính theo bottleneck unit

Hai instance cùng giá không có nghĩa cùng economics. Workload có thể bị giới hạn bởi CPU, memory capacity, memory bandwidth, network egress, local NVMe, accelerator memory hoặc managed-service quota.

Một useful cost model có dạng:

```text
cost per completed useful request
cost per durable transaction
cost per GB processed
cost per model token under SLO
```

thay vì chỉ `$/instance-hour`.

Nếu instance đắt hơn 30% nhưng hoàn thành gấp đôi useful work trước utilization knee, nó có thể rẻ hơn trên một đơn vị outcome. Ngược lại scale-up CPU không giúp nếu bottleneck là shared database.

## 24. Heterogeneous hardware làm capacity thành placement problem

Modern fleet có thể có cores khác tốc độ, NUMA topology khác, local vs remote memory, GPU/accelerator khác generation hoặc storage class khác nhau. Một request “giống nhau” có service time khác tùy placement.

Scheduler/load balancer cần hiểu resource shape khi workload nhạy topology. Memory-heavy worker chạy trên NUMA placement xấu có thể tăng latency; AI model không fit accelerator memory có thể spill/offload và đổi bottleneck từ compute sang PCIe/network transfer.

Capacity model vì vậy phải ghi rõ **hardware class**, không gộp mọi replica thành một số instance count.

## 25. Worked example: CPU thấp nhưng p99 tăng mạnh

Giả sử service có 100 request/s, CPU chỉ 35%, query database mất 20 ms nhưng end-to-end p99 là 900 ms. DB connection pool có 20 slots và pool-acquire p99 là 700 ms.

```text
request concurrency tăng
→ 20 DB slots giữ lâu
→ queue trước pool tăng
→ handler phần lớn off-CPU chờ connection
→ process CPU vẫn thấp
→ p99 tăng
```

Tăng application threads từ 100 lên 500 làm queue lớn hơn nhưng không tạo DB capacity. Tăng pool lên 100 có thể chuyển queue vào DB và làm lock/I/O contention xấu hơn.

Evidence cần đo transaction lifetime, pool hold time, acquire wait, DB active sessions và DB saturation.

## 26. Worked example: thêm cores nhưng throughput không tăng

Một analytics workload scan vùng memory lớn, arithmetic ít và LLC miss cao. Từ 8 lên 16 cores, CPU utilization vẫn cao nhưng throughput gần như đứng yên, memory bandwidth đã gần ceiling.

Ở đây core count không còn là capacity dimension hữu ích. Lower abstraction quyết định behavior là memory subsystem. Tối ưu representation, batching/cache locality hoặc giảm bytes touched có thể tốt hơn mua thêm CPU.

## 27. Benchmark phải tìm phase transition, không chỉ một điểm đẹp

Capacity test tốt tăng load theo các bậc và quan sát khi system đổi phase:

```text
service-time dominated
→ queue begins growing
→ tail increases sharply
→ retries/errors appear
→ useful throughput plateaus
→ collapse/recovery behavior
```

Cần giữ workload mix, payload size, cache state và dependency condition đủ gần production. Nếu benchmark chỉ chạy ngắn, autoscaling/warm-up/GC/compaction/checkpoint có thể chưa lộ.

Sau khi giảm load, còn phải quan sát **recovery**. System có queue/retry debt lớn có thể tiếp tục xấu sau khi traffic trở lại bình thường.

## 28. Evidence chain cho performance incident

Whole-system diagnosis có thể đi theo thứ tự:

```text
SLO symptom
→ trace critical path
→ queue/service-time split
→ on-CPU vs off-CPU
→ subsystem saturation
→ OS scheduler/I/O evidence
→ PMU/device evidence nếu cần
```

Không phải incident nào cũng cần xuống PMU. Mục tiêu là xuống đủ thấp để mechanism rõ rồi sửa ở layer sở hữu invariant/capacity boundary.

## 29. Mô hình tư duy

> Capacity engineering là giữ system **bên trái điểm overload** và biết resource nào thật sự giới hạn progress. Utilization cao làm queue nhạy với variance; concurrency limit giữ active work hữu hạn; admission control giới hạn debt. Whole-system profiling nối request time với on-CPU, off-CPU, scheduler, memory và I/O evidence. Cost/performance chỉ có ý nghĩa khi tính trên useful outcome dưới SLO, không phải peak benchmark hay giá instance riêng lẻ.

## Kết nối

Đọc cùng [Queueing, tail latency và backpressure](./00_queueing_tail_latency_and_backpressure.md), [Load balancing và connection pools](./03_load_balancing_connection_pools_and_locality.md), [End-to-end request và retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md), [Debugging xuyên layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md), [OS scheduler internals](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [Memory hierarchy/cache](../../basic/02_computer_architecture/02_memory_hierarchy_and_cache.md) và [NUMA/interconnect](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md).