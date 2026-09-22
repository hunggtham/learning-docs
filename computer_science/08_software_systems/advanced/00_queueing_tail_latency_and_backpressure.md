# Queueing, tail latency và backpressure

Một system có thể còn CPU trung bình nhưng vẫn timeout vì requests đến bursty, service time biến động và queues tích tụ. Advanced performance reasoning vì vậy không dừng ở average latency hay utilization; nó theo dõi **arrival rate, service capacity, concurrency, queue debt, percentile latency và feedback loops**.

Mental model cốt lõi là: **queue là nơi demand gặp một resource hữu hạn**. Khi demand vượt capacity đủ lâu, hệ thống phải backpressure, reject, degrade hoặc tích debt. Nếu nó chỉ tiếp tục accept rồi retry khi timeout, slowdown có thể tự khuếch đại thành cascading failure.

## 1. Bài toán ban đầu: throughput ổn định không có nghĩa latency ổn định

Giả sử arrival rate là `λ` và service capacity trung bình là `μ`. Nếu `λ < μ`, queue có thể drain về lâu dài. Nhưng khi `λ` tiến gần `μ`, một burst hoặc vài slow requests dễ làm queue tăng mạnh vì system không còn headroom để trả debt.

Utilization 90% không đơn giản nghĩa “còn 10%”. Variability làm tail latency tăng trước khi đạt 100%.

Vì vậy capacity engineering cần tìm **utilization knee**: vùng mà tăng load nhỏ bắt đầu làm waiting time tăng phi tuyến.

## 2. Queueing delay và service time phải đo riêng

End-to-end latency có thể tách mental model:

```text
W = W_queue + W_service + W_downstream/network
```

Một DB query chạy 20 ms không chứng minh request chỉ tốn 20 ms ở DB path nếu trước đó chờ 300 ms để acquire connection.

Khi incident, câu hỏi đầu tiên nên là:

> Work đang chờ **trước resource nào**?

Nếu không tách queue wait, team thường tối ưu code đang chạy thay vì resource đang saturated.

## 3. Little's Law nối concurrency với latency

Trong stable system:

\[
L = \lambda W
\]

`L` là average number of items trong system, `λ` throughput và `W` average time.

Nếu throughput 1000 req/s và average end-to-end time 0.2 s, trung bình có khoảng 200 requests in-flight.

Little's Law không mô tả tail distribution và không cứu system unstable, nhưng là sanity check mạnh: nếu concurrency observed lệch rất xa estimate, có thể có hidden queue, retry, zombie work hoặc measurement boundary khác nhau.

## 4. Variability tạo queue ngay cả khi average capacity đủ

Hai systems cùng average service time có tail khác nếu variance khác. Một vài slow operations giữ workers/connections lâu hơn, làm requests phía sau chờ.

Sources của variability có thể là:

```text
cache hit vs miss
GC/runtime pause
lock contention
storage GC/checkpoint
network retransmission
replica lag
query plan/data skew
cold start/JIT warm-up
```

Tail latency là property của whole pipeline, không chỉ slowest code path.

## 5. Fan-out khuếch đại tail

Nếu một request gọi 20 shards song song và cần đủ tất cả, critical path gần với slowest required branch. Xác suất gặp ít nhất một tail event tăng khi fan-out tăng.

Hedged request có thể giảm tail bằng duplicate attempt sau threshold, nhưng tạo load. Nếu system gần saturation, hedging thiếu budget có thể làm tail xấu hơn.

Optimization tail phải tính **extra work generated per user request**, không chỉ latency của winner.

## 6. Retry không phải backpressure

**Backpressure** nói với producer: downstream không thể nhận work với tốc độ hiện tại.

**Retry** nói: thử lại một attempt đã fail/không chắc outcome.

Nếu dependency slow vì overload, retry thường tạo demand mới đúng lúc `μ` đang giảm.

```text
slowdown
→ timeout
→ retry
→ arrival rate thực tế tăng
→ queue sâu hơn
→ contention/GC/storage pressure tăng
→ service time tăng
→ nhiều timeout hơn
```

Đây là positive feedback loop của **retry storm**.

## 7. Timeout là deadline decision, không phải cancellation proof

Client timeout chỉ nghĩa client ngừng chờ sau boundary nào đó. Server/downstream có thể vẫn xử lý work cũ.

Nếu retry ngay:

```text
attempt 1 vẫn chạy
+
attempt 2 mới bắt đầu
```

Concurrency thật tăng dù user chỉ có một logical request. Với side effect, còn có duplicate-effect risk nếu operation thiếu idempotency.

Timeout design phải đi cùng deadline propagation, cancellation semantics và idempotency contract.

## 8. Deadline cần giảm dần qua call graph

Nếu upstream còn 100 ms nhưng downstream timeout 2 s, downstream có thể tiêu resource sau khi result không còn giá trị.

Một request budget hợp lý cần account:

```text
queue wait
network uncertainty
service time
retry budget nếu có
serialization/response path
```

Deadline nên propagate để downstream biết remaining budget. Không nên reset full timeout ở mỗi hop, vì chain 5 services có thể tạo total wait lớn hơn user SLO nhiều lần.

## 9. Bounded queue biến hidden latency thành explicit policy

Unbounded queue tránh reject ngay nhưng đổi failure mode thành:

```text
memory growth
latency không giới hạn
stale work xử lý sau deadline
OOM / GC pressure
recovery chậm vì backlog
```

Bounded queue buộc system quyết định khi full: reject, block producer, shed low-priority work hoặc degrade.

Đây không chỉ là performance optimization; nó làm failure semantics explicit.

## 10. Backpressure phải reach producer có quyền giảm demand

Một internal queue báo “full” nhưng upstream tiếp tục enqueue ở queue khác thì pressure chỉ bị dời chỗ.

Backpressure effective khi signal đi tới boundary có thể:

```text
stop reading socket
reduce concurrency
pause producer
reduce fetch/poll rate
reject admission
slow tenant/client
```

Nếu mỗi layer có unbounded buffer, system trông stable tới khi toàn bộ buffers cùng đầy.

## 11. Connection pool là queue + concurrency limiter

DB pool 50 connections không chỉ reuse connections; nó cap tối đa 50 active operations qua boundary đó. Requests còn lại chờ acquire.

Tăng pool size có thể giảm application wait nhưng chuyển concurrency xuống DB. Khi DB đã saturated, pool lớn hơn làm lock/I/O/cache contention tăng và service time xấu hơn.

Pool sizing phải dựa resource bottleneck thật, không dựa “nhiều connection hơn = nhanh hơn”.

## 12. Admission control giữ system trong safe operating region

Khi overload, system cần ngăn accepted work vượt khả năng hoàn tất hữu ích trước deadline.

Admission có thể dựa:

```text
max concurrency
queue occupancy
estimated cost
tenant quota
priority class
current saturation signal
```

Reject sớm một phần requests có thể làm success count thực tế cao hơn việc accept 100% rồi để 100% timeout.

## 13. Load shedding bảo vệ invariant quan trọng hơn success-rate tức thời

System có thể skip optional enrichment, serve stale cache, reject expensive reports hoặc degrade non-critical feature để giữ core transaction path khỏe.

Nhưng degrade policy phải biết dependency/invariant. Không thể serve stale authorization decision nếu security contract yêu cầu fresh revoke state, chẳng hạn.

Reliability optimization luôn bị constraint bởi correctness/security invariant.

## 14. Priority chỉ có nghĩa khi resource được phân lập hoặc schedule công bằng

Gắn `priority=high` vào request không giúp nếu high/low cùng tranh một exhausted FIFO pool.

Priority cần enforcement tại resource:

```text
reserved concurrency
weighted fair queue
separate pool
preemption khi safe
per-class admission
```

Nếu không, low-priority burst có thể giữ toàn bộ connections trước khi high-priority traffic tới.

## 15. Multi-tenant noisy neighbor là queue ownership problem

Một tenant có thể hợp lệ nhưng tạo workload lớn. Nếu mọi tenant share queue/pool/cache mà không quota/fairness, một tenant làm p99 của tất cả tăng.

Useful invariant:

> Demand của tenant A không được tiêu toàn bộ capacity cần thiết để giữ SLO tối thiểu của tenant B, theo isolation policy đã công bố.

Mechanism có thể là weighted fair scheduling, concurrency quota, token bucket, per-tenant queues hoặc partitioned resource. Exact choice phụ thuộc workload.

## 16. Token bucket và rate limit kiểm soát rate nhưng chưa chắc kiểm soát concurrency

Một request có thể nhanh hoặc rất chậm. Cùng 100 req/s nhưng service time 10 ms tạo concurrency khác 2 s.

Rate limit bảo vệ arrival rate; concurrency limiter bảo vệ number of active costly operations. Systems thường cần cả hai nếu request cost/latency biến động.

Weighted admission hữu ích khi endpoint/model/query có cost rất khác nhau.

## 17. Backoff + jitter giảm synchronization nhưng không tạo capacity

Exponential backoff giảm retry frequency; jitter tránh clients wake cùng lúc. Retry budget giới hạn tổng extra attempts.

Nhưng nếu dependency mất capacity lâu dài, backoff chỉ giảm damage. System vẫn cần load shedding, failover capacity, repair hoặc demand reduction.

Retry policy nên phân loại:

```text
transient/retryable
permanent/non-retryable
unknown-outcome requiring idempotency
```

Blind retry mọi 5xx/timeout là load generator.

## 18. Circuit breaker là state machine, không phải magic shield

Circuit breaker quan sát failures và tạm ngừng calls để giảm pressure. Nhưng threshold/window/half-open probes tạo own behavior.

Nếu mở quá nhạy, transient blip biến thành self-inflicted outage; nếu đóng quá lâu, dependency tiếp tục bị hammered. Half-open probes phải bounded để recovery traffic không tạo thundering herd.

Breaker chỉ hữu ích khi caller có fallback/reject behavior phù hợp; nó không chữa dependency.

## 19. Queue placement quyết định nơi policy và evidence tồn tại

Có thể có queue ở:

```text
load balancer
kernel accept/socket buffers
runtime executor/event loop
application work queue
DB connection pool
database lock manager
storage device
```

Ba queues mỗi nơi “chỉ 100 ms” đã tạo 300+ ms trước service work.

Queue nên nằm nơi system hiểu deadline, priority, ownership và capacity tốt nhất; hidden queues ở lower layer cần observability vì chúng vẫn thuộc critical path.

## 20. Overload làm service rate giảm, không chỉ queue tăng

Simple queueing model hay giả định `μ` cố định. Production overload thường làm `μ` giảm vì:

```text
context switches ↑
cache locality ↓
GC pressure ↑
lock contention ↑
storage queue/GC ↑
DB plan/cache churn ↑
retry bookkeeping ↑
```

Do đó vượt knee có thể tạo **overload collapse**: thêm demand làm throughput useful giảm.

Đây là lý do headroom quan trọng hơn chạy sát 100% utilization.

## 21. Recovery cũng cần admission control

Sau outage, backlog + retries + reconnects có thể tạo **recovery storm**. Nếu dependency vừa hồi và toàn fleet gửi traffic cùng lúc, nó lại collapse.

Recovery path nên ramp traffic, jitter reconnect, limit replay consumers và prioritize fresh/critical work khi business semantics cho phép.

“Service healthy again” không đồng nghĩa “service chịu được toàn backlog ngay lập tức”.

## 22. Production evidence phải theo flow của work

Evidence hữu ích:

```text
Demand:
- original request rate
- attempt/retry/hedge rate
- per-tenant/per-class rate

Queues:
- queue depth
- queue wait distribution
- oldest item age
- reject/shed count

Capacity:
- active workers/connections
- saturation/utilization
- service time distribution
- downstream pool/storage/runtime state

Deadlines:
- timeout rate by hop
- cancellation success/late completion
- work completed after caller deadline
```

Một CPU graph không chỉ ra hidden DB pool queue; p99 alone không chỉ ra attempt amplification.

## 23. Performance experiments phải tìm knee và feedback loop

Load test nên ramp demand và giữ đủ lâu để background debt xuất hiện. Ghi lại throughput useful, attempt rate, queue wait, saturation và p50/p95/p99.

Nếu QPS user tăng 10% nhưng attempt rate tăng 40% do retry, benchmark phải coi extra attempts là part of load. Nếu throughput useful plateau rồi giảm, đã bước vào collapse region.

## 24. Abstraction nào thực sự quyết định behavior?

Nếu request chậm nhưng CPU thấp, tìm queue trước pool/I/O/network. Nếu timeout tăng cùng retry rate, inspect amplification. Nếu one tenant làm tất cả chậm, inspect fairness/resource isolation. Nếu adding threads worsens throughput, lower bottleneck/contended resource đang quyết định service rate.

## 25. Mô hình tư duy

> Queue là **debt của demand đối với capacity**. Tail latency tăng khi variability và saturation làm debt khó trả. Timeout có thể bỏ người chờ nhưng không xóa work; retry có thể nhân demand; backpressure và admission control giữ debt bounded; fairness quyết định ai được dùng capacity; load shedding giữ system trong safe region. **Khi incident latency xảy ra, hãy tìm queue, ownership và feedback loop trước khi chỉ tối ưu code.**

## Kết nối

Ôn [performance/capacity](../../basic/08_software_systems/02_performance_capacity_and_scalability.md), [state/queues/backpressure](../../basic/08_software_systems/03_state_queues_backpressure_and_boundaries.md) và [reliability](../../basic/07_security_reliability/05_fault_tolerance_observability_and_reliability.md). Đọc tiếp [capacity/admission control](./01_capacity_planning_utilization_knee_and_admission_control.md), [load balancing/pools](./03_load_balancing_connection_pools_and_locality.md), [async runtime](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md) và [end-to-end request/retry overload](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).