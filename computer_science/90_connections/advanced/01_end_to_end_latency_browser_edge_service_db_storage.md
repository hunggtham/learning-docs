# End-to-end latency: browser → edge → service → DB → storage

Một request “mất 800 ms” không có một nguyên nhân duy nhất. Latency là tổng và interaction của nhiều queues qua browser, DNS/network, edge/proxy, application, database và storage. Debugging senior-level bắt đầu bằng việc phân rã critical path thay vì tối ưu component có metric dễ nhìn nhất.

## Latency budget

Nếu product SLO yêu cầu p95 dưới 500 ms, có thể phân budget cho network, edge, service compute, dependencies và database. Budget không cần cố định tuyệt đối; nó tạo framework để biết 300 ms ở DB là bất thường hay expected.

## Browser/client

Client có DNS lookup, connection establishment, TLS handshake, request queueing, upload/download và rendering. Connection reuse, HTTP multiplexing và cache có thể loại bỏ nhiều setup cost ở steady state nhưng cold request vẫn khác.

Mobile network có RTT và packet-loss distribution khác office LAN; backend benchmark local không đại diện user latency.

## Edge và gateway

CDN/reverse proxy có thể terminate TLS, authenticate, rate-limit, route và cache. Queue hoặc connection pool ở gateway có thể tạo latency trước khi request chạm application.

Trace nên bắt đầu đủ sớm để không biến edge time thành “network mystery”.

## Application service

Service latency gồm queueing chờ worker/event loop, CPU execution, GC/scheduler pause và downstream waits. “Handler mất 300 ms” cần tách on-CPU và off-CPU.

Nếu thread chủ yếu chờ DB, tăng CPU instance có thể không giúp. Nếu event loop blocked bởi CPU work, async I/O cũng không cứu latency.

## Database

DB time gồm connection-pool wait, parse/plan, lock wait, execution, buffer-cache miss và storage I/O. Query 20 ms trên server nhưng request chờ pool 200 ms vẫn là database-path bottleneck từ góc nhìn application.

Do đó instrumentation cần đo **acquire connection** riêng với **execute query**.

## Storage

Storage latency có queue depth, cache, device writeback và durability flush. Database `COMMIT` có thể phải chờ WAL durability; average device latency không phản ánh fsync tail under contention.

## Parallel calls

Nếu service gọi ba dependencies song song, end-to-end wait gần max latency của critical dependencies, không phải tổng. Nhưng probability ít nhất một call chậm tăng khi fan-out lớn. Tail latency vì thế bị khuếch đại bởi fan-out.

## Retry

Retry có thể biến một transient 200 ms thành 200 + timeout + retry latency, đồng thời tăng load lên dependency đang yếu. Trace phải giữ attempt information để không nhìn retry như một call bí ẩn kéo dài.

## Clock và tracing

Distributed trace dùng spans để reconstruct causal path, nhưng timestamp giữa hosts có uncertainty. Duration đo bằng monotonic clock trong process thường đáng tin hơn so sánh raw wall-clock giữa machines.

Trace sampling cũng có thể bỏ mất rare tail events; metrics và logs vẫn cần bổ sung.

## Debugging workflow

Bắt đầu từ user-visible percentile → chọn slow trace → xác định span/queue chiếm critical path → phân biệt on-CPU/off-CPU → correlate saturation metrics của resource tương ứng → tạo hypothesis → thay đổi một yếu tố và đo lại.

Không bắt đầu bằng “database chắc chậm” hoặc “network chắc lag”.

## Mental model

> End-to-end latency là critical path qua nhiều queues. Mỗi boundary có service time và waiting time. Observability tốt phải giữ causal context xuyên các boundary để ta biết thời gian được tiêu ở đâu, chờ cái gì và saturation nào làm tail tăng.