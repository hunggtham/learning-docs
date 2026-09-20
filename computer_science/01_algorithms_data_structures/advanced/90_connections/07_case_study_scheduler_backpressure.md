# Case Study: Scheduler, Queue và Backpressure
**Scheduling & Backpressure Case Study / 스케줄링과 백프레셔 사례**

Scheduler xuất hiện ở CPU, job queue, thread pool, message processing, network packet scheduling và background worker. Bài toán tưởng như chỉ là “chọn công việc tiếp theo”, nhưng thực tế phải cân bằng nhiều mục tiêu: độ trễ, throughput, fairness, deadline, priority, memory và khả năng hấp thụ burst.

Case study này nối Queue, Deque, Priority Queue, Heap, Hash Table, Fair Scheduling và Backpressure thành một mô hình hệ thống thống nhất.

## 1. FIFO là baseline

Queue FIFO xử lý theo thứ tự đến:

```text
job1 -> job2 -> job3 -> ...
```

Ưu điểm:

```text
đơn giản
fair theo thời gian đến
chi phí thấp
```

Nhưng FIFO không biết job nào quan trọng hơn hoặc job nào có deadline gần hơn.

## 2. Priority Queue

Nếu mỗi job có priority, min/max heap là lựa chọn tự nhiên:

```text
(priority, arrivalOrder, jobId)
```

Tie-break bằng `arrivalOrder` giúp giữ fairness giữa các job cùng priority.

Nếu không có tie-break ổn định, scheduler có thể cho hành vi khó dự đoán dù priority chính vẫn đúng.

## 3. Mutable Priority

Priority có thể thay đổi theo thời gian: job chờ lâu được tăng độ ưu tiên để tránh starvation.

Heap chuẩn không tự sắp xếp lại khi field của object thay đổi. Có ba hướng:

```text
indexed heap + decrease/increase-key
chèn entry mới và bỏ entry cũ khi pop
rebuild heap theo chu kỳ
```

Lazy stale-entry thường đơn giản và robust nếu memory overhead chấp nhận được.

## 4. Starvation và Aging

Nếu luôn chọn priority cao nhất, job priority thấp có thể chờ vô hạn.

**Aging** tăng effective priority theo thời gian:

\[
effectivePriority = basePriority + f(waitTime)
\]

Scheduler không còn tối ưu một scalar cố định; priority trở thành hàm của state động.

## 5. Deadline Scheduling

Nếu job có deadline, một strategy cổ điển là **Earliest Deadline First (EDF)**: luôn chọn job có deadline sớm nhất.

Priority Queue có key là deadline.

Nhưng EDF chỉ có guarantee mạnh dưới những giả định cụ thể về mô hình task và utilization. Không nên áp dụng theorem real-time vào workload tùy ý mà không kiểm tra giả định.

## 6. Shortest Job First

Nếu biết service time, xử lý job ngắn trước có thể giảm average waiting time trong một số mô hình.

Nhưng long job có thể starvation nếu short job đến liên tục.

Một mục tiêu tối ưu average latency có thể xung đột fairness.

Đây là bài học quan trọng: scheduler cần **objective rõ ràng**, không chỉ data structure nhanh.

## 7. Multi-Level Queue

Có thể chia job thành nhiều queue:

```text
critical
interactive
batch
background
```

Scheduler chọn giữa các queue theo policy rồi FIFO/priority bên trong mỗi queue.

Composition này thường dễ kiểm soát hơn một global priority formula cực phức tạp.

## 8. Weighted Fairness

Giả sử ba tenant có trọng số:

```text
A: 5
B: 3
C: 2
```

Ta muốn chia capacity tương đối 50% / 30% / 20% trong dài hạn.

Weighted Round Robin là một cách đơn giản. Các thuật toán công bằng hơn có thể mô hình hóa **virtual finish time** và dùng priority queue.

Một scheduler tốt phải phân biệt:

```text
priority -> ai nên đi trước
fairness -> ai nhận bao nhiêu tài nguyên theo thời gian
```

Hai khái niệm không giống nhau.

## 9. Queue có giới hạn

Queue vô hạn về logic là nguy hiểm trong hệ thống thật.

Nếu producer tạo 100k job/s nhưng consumer chỉ xử lý 80k/s, queue tăng 20k/s. Sau đủ lâu, memory hoặc disk sẽ cạn.

Queue có giới hạn biến tài nguyên hữu hạn thành một invariant:

```text
0 <= size <= capacity
```

Khi đầy, hệ thống buộc phải có policy.

## 10. Backpressure

Backpressure là cơ chế truyền tín hiệu “downstream đang quá tải” ngược lên upstream.

Các lựa chọn:

```text
block producer
reject request
return 429 / busy
slow down producer
drop low-priority work
spill to disk
scale consumer
```

Không có policy chung đúng cho mọi hệ thống. Log telemetry có thể drop một phần; payment request thường không thể âm thầm drop.

## 11. Little’s Law

Trong trạng thái ổn định:

\[
L = \lambda W
\]

với:

```text
L      = số item trung bình trong hệ thống
lambda = throughput trung bình
W      = thời gian trung bình một item ở trong hệ thống
```

Nếu arrival rate tiến sát service capacity, queueing latency có thể tăng mạnh.

Little’s Law không thiết kế scheduler thay ta, nhưng giúp liên hệ queue length, throughput và latency.

## 12. Batching

Thay vì xử lý từng item:

```text
pop 1 -> xử lý -> pop 1
```

có thể lấy một batch:

```text
pop 100 -> xử lý chung
```

Batching giảm overhead khóa, syscall, network round-trip hoặc vectorization cost trên mỗi item.

Nhưng batch quá lớn làm tăng waiting latency cho item đầu tiên.

Đây là trade-off throughput–latency.

## 13. Work Stealing

Trong thread pool, mỗi worker có deque riêng.

Worker thường:

```text
push/pop task của mình ở một đầu
```

Worker rảnh có thể **steal** từ đầu còn lại của worker khác.

Deque giúp giảm contention vì owner và thief thường thao tác ở hai đầu khác nhau.

Work stealing đặc biệt phù hợp task recursive/fork-join vì các task mới sinh thường có locality với worker hiện tại.

## 14. Global Queue vs Local Queues

Global queue đơn giản nhưng nhiều worker cùng tranh chấp một lock/cache line.

Per-worker queue giảm contention nhưng tạo imbalance.

Work stealing là một cách kết hợp:

```text
local fast path
+
steal khi thiếu việc
```

Đây là ví dụ system design sinh ra từ việc ghép nhiều queue thay vì chỉ tối ưu một queue duy nhất.

## 15. SPSC, MPSC, MPMC

Queue đồng thời cần xác định mô hình producer/consumer:

```text
SPSC -> single producer, single consumer
MPSC -> multiple producer, single consumer
MPMC -> multiple producer, multiple consumer
```

SPSC có thể đơn giản hơn rất nhiều vì ownership của head/tail rõ ràng. MPMC cần protocol atomic/memory-order phức tạp hơn.

Không nên dùng cấu trúc concurrent tổng quát nếu mô hình thực tế đơn giản hơn.

## 16. Ring Buffer

Bounded queue thường dùng ring buffer:

```text
buffer[capacity]
head
tail
```

Nếu capacity là lũy thừa hai, modulo có thể thay bằng bitmask trong một số implementation:

```text
index & (capacity - 1)
```

Nhưng optimization này chỉ đúng nếu invariant capacity được giữ.

## 17. Queue Depth không chỉ là metric vận hành

Queue depth phản ánh chênh lệch giữa arrival và service rate.

Một spike ngắn có thể được queue hấp thụ. Queue tăng liên tục cho thấy hệ thống không đạt trạng thái ổn định.

Các alert nên nhìn:

```text
queue length
age của item cũ nhất
arrival rate
service rate
rejection/drop rate
processing latency
```

Chỉ nhìn CPU usage có thể bỏ sót backlog.

## 18. Retry Storm

Khi downstream lỗi, upstream có thể retry. Nếu mọi client retry ngay, arrival rate tăng đúng lúc capacity giảm.

Queue/backpressure cần phối hợp với:

```text
exponential backoff
jitter
retry budget
circuit breaker
```

DSA queue đúng nhưng policy retry sai vẫn làm hệ thống sụp.

## 19. Delay Queue và Timer Heap

Nếu job chỉ được chạy sau `readyAt`, scheduler cần cấu trúc theo thời gian.

Min-heap theo timestamp:

```text
peek -> job sớm nhất
```

phù hợp khi số timer vừa phải.

Nếu có hàng triệu timer với độ phân giải giới hạn, **timer wheel** có thể hiệu quả hơn heap vì bucket hóa thời gian.

Lựa chọn phụ thuộc độ phân giải và scale.

## 20. Dedup và Idempotency

Job có thể được gửi lại sau retry. Nếu side effect không idempotent, xử lý hai lần có thể gây lỗi.

Có thể dùng:

```text
job_id -> processed state
```

trong Hash Map/database với TTL.

Nhưng dedup state cũng tăng theo số job và cần cleanup.

## 21. Cancellation

Nếu job đang trong heap/queue bị cancel, xóa tùy ý có thể đắt.

Một strategy đơn giản:

```text
cancelled[jobId] = true
```

khi pop thì bỏ qua job đã cancel.

Đây là lazy deletion, tương tự stale entries trong Dijkstra/Priority Queue.

## 22. Admission Control

Tốt hơn việc nhận mọi job rồi để queue nổ là quyết định ngay từ đầu hệ thống có đủ capacity hay không.

Admission control có thể dựa trên:

```text
queue depth
concurrency limit
estimated cost
tenant quota
memory budget
```

Một request bị từ chối sớm đôi khi tốt hơn request timeout sau 30 giây.

## 23. Cost-aware Scheduling

Không phải mọi job có cost giống nhau. Nếu một job cần 10 GB RAM còn job khác cần 100 MB, chỉ priority theo thời gian có thể làm resource fragmentation.

Scheduler có thể model nhiều tài nguyên:

```text
CPU
memory
GPU
network
```

Bài toán trở thành multidimensional packing/scheduling và có thể khó về mặt tổ hợp.

Đây là ranh giới nơi heap đơn giản không còn đủ.

## 24. Priority Inversion

Một task priority cao có thể phải chờ lock đang được task priority thấp giữ, trong khi task trung bình tiếp tục chạy. Đây là **priority inversion**.

Các cơ chế như priority inheritance xử lý ở tầng synchronization, cho thấy scheduler và lock/resource graph có liên hệ với nhau.

## 25. Fairness theo tenant

Nếu một tenant gửi 90% traffic, global FIFO có thể làm tenant khác chờ lâu.

Per-tenant queue + weighted scheduler cho phép isolation tốt hơn.

Hash Map có thể ánh xạ:

```text
tenant_id -> queue state
```

và heap/round-robin chọn tenant tiếp theo.

## 26. Failure Recovery

Queue in-memory mất job khi process crash nếu không có persistence.

Persistent queue phải thêm:

```text
log
ack state
replay
visibility timeout
```

Một cấu trúc FIFO đúng trong RAM chưa đủ cho delivery semantics.

## 27. Testing

Kiểm tra không chỉ thứ tự output mà còn invariant:

```text
không vượt capacity
không mất job
không chạy job đã cancel
priority/tie-break đúng
aging không làm starvation
retry không double-apply side effect theo contract
```

Property-based test có thể sinh chuỗi enqueue/dequeue/cancel/reprioritize ngẫu nhiên và so với mô hình tham chiếu.

## 28. Benchmark

Cần đo:

```text
throughput
p50/p95/p99 latency
queue age
contention theo số worker
allocation/GC
batch size
burst traffic
hot tenant
```

Average throughput tốt nhưng p99 rất xấu có thể không đáp ứng SLA.

## 29. Pipeline khái niệm

```text
Incoming Work
   ↓
Admission Control
   ↓
Per-tenant / global queues
   ↓
Priority / fairness scheduler
   ↓
Workers
   ↓
Ack / Retry / DLQ
```

Feedback loop:

```text
queue depth + latency
   ↓
backpressure / autoscaling / rejection
```

## Mô hình tư duy

> Scheduler là bài toán **chọn item tiếp theo dưới mục tiêu và ràng buộc tài nguyên**. Queue lưu backlog, Priority Queue mã hóa thứ tự ưu tiên, Deque hỗ trợ work stealing, Hash Map giữ state theo job/tenant, còn backpressure bảo đảm backlog không biến thành sự cố tài nguyên. Data structure chỉ là một nửa; policy và objective mới quyết định hệ thống có công bằng, ổn định và chịu tải tốt hay không.

Xem thêm: [Queue, Deque & Priority Queue](../01_linear_structures/03_queues_deques_and_priority_queues.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [Problem-Solving Workflow](./02_problem_solving_workflow.md).