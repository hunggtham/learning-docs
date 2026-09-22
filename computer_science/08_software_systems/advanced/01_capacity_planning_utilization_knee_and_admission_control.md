# Capacity planning, utilization knee và admission control

Capacity planning không phải lấy peak traffic rồi cộng 20%. Một service có thể vẫn còn throughput capacity nhưng tail latency đã tăng mạnh vì queueing và contention. Ở mức advanced, cần giữ một invariant vận hành: **accepted work phải nằm trong vùng mà system còn đủ resource để hoàn thành trước deadline với xác suất/SLO đã công bố.**

Khi system tiếp tục accept work sau vùng đó, queue debt, timeout và retry có thể biến slowdown thành overload collapse.

## 1. Capacity là một safe operating envelope

Một service có nhiều bottleneck resources:

```text
CPU
memory / GC
thread or event-loop concurrency
DB connections
sockets/file descriptors
I/O bandwidth
network bandwidth
downstream quota
locks/shared state
```

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

Vì vậy adaptive limit phải reasoning như feedback controller, không phải magic autoscaling switch.

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

Capacity diagnosis cần kết hợp:

```text
arrival rate và completion rate
active concurrency
queue depth + queue wait
service-time distribution
retry/attempt rate
resource saturation tại bottleneck
rejection/load-shed count
remaining deadline/cancellation rate
```

Nếu throughput đứng yên nhưng concurrency/queue tăng, system đang tích debt. Nếu CPU thấp mà pool wait cao, bottleneck nằm downstream/resource khác.

Load test cần workload mix và failure mode gần production; benchmark single endpoint happy path không đủ để tìm safe envelope.

## 16. Lower abstraction nào quyết định behavior?

Nếu application queue tăng vì CPU run queue dài, scheduler là lower layer. Nếu DB pool full vì lock waits, database concurrency control quyết định capacity. Nếu write latency tăng vì storage flush, durability path quyết định service time. Nếu TLS/KMS dependency chậm, security control plane cũng có thể trở thành capacity bottleneck.

Capacity model chỉ đúng khi biết resource thật sự đang giới hạn progress.

## 17. Mô hình tư duy

> Capacity engineering là giữ system **bên trái điểm overload**. Utilization cao làm queue nhạy với variance; concurrency limit giữ active work hữu hạn; bounded queue giới hạn debt; admission control/load shedding từ chối work trước khi bottleneck collapse; retry budget ngăn caller biến slowdown thành load amplifier. Capacity là safe operating envelope, không phải maximum RPS đẹp nhất.

## Kết nối

Đọc cùng [Queueing, tail latency và backpressure](./00_queueing_tail_latency_and_backpressure.md), [Load balancing và connection pools](./03_load_balancing_connection_pools_and_locality.md), [End-to-end request và retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) và [OS scheduler internals](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md).