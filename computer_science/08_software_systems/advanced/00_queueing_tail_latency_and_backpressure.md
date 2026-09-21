# Queueing, tail latency và backpressure

Một system có thể đủ CPU trung bình nhưng vẫn timeout vì requests đến bursty, service time biến động và queues tích tụ. Advanced performance reasoning vì vậy không dừng ở average latency hay CPU utilization; nó nhìn **arrival rate, service rate, queue length, percentile latency và feedback loops**.

## Queue xuất hiện khi demand tạm thời vượt service capacity

Nếu requests đến với rate `λ` và server xử lý trung bình rate `μ`, khi `λ` tiến gần `μ`, queue có xu hướng nhạy mạnh với variability. Utilization 90% không đơn giản có nghĩa “còn 10% headroom”; tail latency có thể tăng rất nhanh trước khi đạt 100%.

Đây là lý do production systems thường cần capacity headroom, đặc biệt khi service time distribution heavy-tailed hoặc traffic bursty.

## Little's Law là cầu nối giữa concurrency và latency

Trong stable system:

\[
L = \lambda W
\]

`L` là average number of items trong system, `λ` throughput/arrival rate, `W` average time trong system.

Nếu throughput 1000 req/s và average end-to-end time 0.2 s, trung bình khoảng 200 requests đang in-flight. Công thức không nói distribution hay tail, nhưng là sanity check mạnh cho concurrency sizing.

## Tail latency lan qua fan-out

Service A gọi song song 20 downstream shards và chỉ hoàn tất khi đủ responses. Dù mỗi shard p99 “khá tốt”, xác suất ít nhất một call chậm tăng theo fan-out. End-to-end percentile vì vậy không thể suy ra đơn giản từ average downstream.

Hedged requests có thể giảm tail bằng cách gửi duplicate sau threshold, nhưng tăng load; nếu system đang overload, hedging thiếu kiểm soát có thể làm tình hình tệ hơn.

## Backpressure khác retry

Backpressure truyền tín hiệu rằng downstream không tiếp nhận thêm work với tốc độ hiện tại. Bounded queue, semaphore, demand-based streaming hoặc credit/token mechanisms đều là cách biểu diễn capacity.

Retry làm ngược lại: nó tạo thêm attempts. Nếu dependency đang chậm, retry không jitter/budget có thể tạo **retry storm**, tăng queue và đẩy dependency vào overload collapse.

## Bounded queue là correctness/performance tool

Unbounded queue tránh reject ngay nhưng đổi failure thành memory growth và latency vô hạn. Khi work cũ đã quá deadline nhưng vẫn nằm queue, system tiêu resource xử lý request mà client không còn cần.

Bounded queue + deadline + admission control giúp system fail sớm và giữ phần traffic còn lại khỏe hơn.

## Load shedding bảo vệ core function

Khi overload, system có thể reject low-priority work, skip optional enrichment, serve stale cache hoặc degrade response. Mục tiêu không phải giữ success rate 100% bằng mọi giá; mục tiêu là tránh toàn hệ thống collapse.

Priority phải gắn với resource reservation hoặc fair scheduling. Nếu high-priority và low-priority cùng tranh một exhausted pool, label priority không tạo isolation thật.

## Connection pool cũng là queue

DB pool 50 connections nghĩa tối đa 50 queries active qua pool; requests còn lại chờ acquire. Tăng pool vô hạn có thể chỉ chuyển queue từ application sang database và làm DB thrash.

Sizing cần dựa bottleneck thật: DB CPU/I/O/concurrency, query service time và acceptable queue delay. Queue nên nằm ở layer có visibility/admission policy tốt nhất, không phải cứ “nhiều connection hơn là nhanh hơn”.

## Deadline propagation

Nếu upstream request còn 100 ms deadline nhưng downstream call timeout 2 s, downstream có thể tiếp tục work vô ích sau khi upstream đã bỏ cuộc. Propagate deadline/budget giúp từng hop biết thời gian còn lại và tránh zombie work.

Timeout mỗi hop cần gồm queue wait + service time + network uncertainty; nếu chỉ đặt timeout tùy ý, system dễ tạo synchronized retry waves.

## Mental Model

> Khi latency tăng, hỏi **work đang xếp hàng ở đâu**. Queue là nơi demand gặp capacity. Tail latency là hậu quả của variability + fan-out + saturation. Backpressure/admission control giới hạn lượng work đi vào trước khi retry và queue biến slowdown thành collapse.

## Kết nối

Ôn [performance/capacity](../../basic/08_software_systems/02_performance_capacity_and_scalability.md), [state/queues/backpressure](../../basic/08_software_systems/03_state_queues_backpressure_and_boundaries.md) và [reliability](../../basic/07_security_reliability/05_fault_tolerance_observability_and_reliability.md).