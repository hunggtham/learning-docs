# Capacity models, admission control và load shedding

Hệ thống thường không sập vì một request “quá khó”, mà vì arrival rate vượt service capacity đủ lâu để queue phình ra, latency tăng, timeout sinh retry và retry lại tạo thêm load. Đây là vòng feedback dẫn tới **overload collapse**. Advanced system design phải biết từ chối work đúng lúc thay vì cố phục vụ mọi thứ cho tới khi tất cả cùng thất bại.

## Capacity không chỉ là CPU percent

Một service có nhiều bottleneck resources: CPU, DB connections, thread pool, sockets, memory, I/O bandwidth, downstream quota.

Throughput tối đa bị giới hạn bởi resource bão hòa đầu tiên. Nếu CPU 40% nhưng DB pool 100% busy, tăng replicas application có thể không giúp và thậm chí tăng pressure DB.

Capacity model cần xác định **concurrency limit + service time + downstream constraints**, không chỉ utilization tổng quát.

## Little's Law

Trong steady-state phù hợp:

\[
L = \lambda W
\]

`L` là số requests trung bình trong system, `λ` arrival/completion rate và `W` thời gian trung bình ở system.

Nếu throughput 1000 req/s và average latency 0.2s, trung bình khoảng 200 requests đang in-flight.

Đây là sanity check mạnh cho pool sizing và concurrency reasoning.

## Utilization gần 100% làm queue delay bùng lên

Khi arrival rate tiến gần service capacity, một ít variance đủ tạo queue. Queueing delay tăng phi tuyến dù service time bản thân không đổi.

Vì vậy vận hành ổn định thường cần **headroom**, không target mọi resource 100%.

Batch throughput workload có thể chấp nhận utilization cao hơn latency-sensitive API.

## Bounded queue

Unbounded queue biến overload thành memory growth và latency hàng phút. Request vẫn “được accept” nhưng deadline đã vô nghĩa.

Bounded queue làm failure sớm và rõ hơn. Khi queue đầy, system phải reject, shed hoặc degrade.

Đây là backpressure boundary: producer nhận tín hiệu rằng consumer hết capacity.

## Admission control

Admission control quyết định request có được vào expensive part của system hay không.

Có thể dựa concurrency semaphore, token bucket, queue length, estimated cost hoặc tenant quota.

Mục tiêu không phải tối đa số accepted requests tức thời mà giữ system trong operating region nơi accepted requests còn có xác suất hoàn thành tốt.

## Load shedding

Khi overload, bỏ bớt work có chủ đích để bảo vệ core service.

Ví dụ ưu tiên authenticated transaction hơn analytics refresh, bỏ speculative prefetch, giảm expensive enrichment hoặc reject low-priority tenant trước.

Good load shedding cần phân loại work và trả signal rõ (`429`, `503`, retry-after, queue rejected...) để caller không retry hỗn loạn.

## Retry amplification

Client timeout sau 1s nhưng server thực tế vẫn đang xử lý. Client retry tạo request thứ hai. Load tăng làm server chậm hơn, thêm timeout, thêm retries.

Nếu nhiều clients retry đồng thời, **retry storm** có thể biến slowdown nhỏ thành outage.

Mitigation: timeout hợp lý, bounded retries, exponential backoff + jitter, retry budget và idempotency.

Retry policy là một phần capacity design, không chỉ client convenience.

## Deadline propagation

Request còn 50ms deadline nhưng service A vẫn gọi B với timeout 1s là wasted work. Deadline nên propagate để downstream biết request còn đáng xử lý bao lâu.

Nếu deadline đã hết, cancel work sớm giải phóng capacity.

Structured concurrency/cancellation ở runtime giúp hiện thực hóa system principle này.

## Concurrency limit vs rate limit

Rate limit kiểm soát arrivals per time. Concurrency limit kiểm soát số work đồng thời.

Một operation 5ms và operation 5s có thể cùng rate nhưng resource footprint rất khác. Concurrency thường phản ánh capacity trực tiếp hơn cho latency-variable downstream.

Nhiều hệ thống cần cả hai.

## Adaptive concurrency

Static limit có thể không phù hợp khi downstream capacity thay đổi. Adaptive controller quan sát latency/error/queue và điều chỉnh concurrency.

Nhưng control loop tuning khó: phản ứng quá nhanh gây oscillation; quá chậm để overload lan rộng.

Đây là connection giữa software systems và control theory.

## Bulkhead

Chia resource pools theo workload/tenant để một class không ăn hết capacity. Ví dụ background export dùng pool khác user-facing requests.

Bulkhead hy sinh utilization tối đa trong một số thời điểm để tăng fault isolation.

## Graceful degradation

Khi capacity thiếu, system có thể phục vụ response ít feature hơn thay vì fail toàn bộ: cached data, omit recommendation, lower image quality, skip optional audit enrichment nếu policy cho phép.

Degradation phải được thiết kế trước; trong incident không nên tùy tiện bỏ correctness-critical steps.

## Mental Model

> Capacity engineering là giữ system **bên trái điểm overload**. Bounded queues, admission control, deadlines, retry budgets và load shedding biến overload từ collapse ngẫu nhiên thành degradation có kiểm soát.

## Common Misconceptions

**“Queue càng lớn càng chịu spike tốt.”** Queue lớn có thể chỉ biến spike thành latency cực cao và stale work.

**“Retry làm reliability tốt hơn.”** Retry không giới hạn có thể phá reliability khi failure do overload.

**“Scale app replicas luôn tăng capacity.”** Nếu bottleneck là DB/downstream quota, replicas chỉ tăng contention.

## Kết nối

Đọc cùng starter chapter về queueing/tail latency. Ở OS, run queue saturation là cùng family; ở database, connection pool và lock wait tạo queue; ở distributed systems, load shedding cần phối hợp retry/backpressure toàn call graph.