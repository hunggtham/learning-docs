# End-to-end request: DNS → TCP/TLS → proxy/load balancer → runtime → database, và vòng retry → overload

Một request “mất 800 ms” không có một nguyên nhân duy nhất. Nó đi qua một chuỗi resolution, connection, queue, scheduler và storage boundaries. Advanced reasoning không bắt đầu bằng câu “network chậm” hay “database chậm”; nó dựng **critical path**, xác định invariant ở từng boundary và tìm nơi demand bắt đầu vượt capacity.

## 1. Request path thật sự bắt đầu trước HTTP handler

Một cold request có thể đi qua:

```text
URL/hostname
→ DNS cache/resolver/authoritative lookup
→ route/NAT
→ TCP handshake hoặc QUIC setup
→ TLS handshake + certificate validation
→ CDN / reverse proxy / WAF
→ load balancer
→ application connection accept
→ runtime/event loop/thread pool
→ application queue/pool
→ database/cache/downstream service
→ response serialization
→ transport back to client
```

Steady-state request có thể reuse DNS result, connection và TLS session nên bỏ qua nhiều bước. Vì vậy benchmark warm connection và incident cold-start có thể là hai workload khác nhau.

## 2. Invariant end-to-end: deadline và causal context phải sống qua mọi hop

Một request có latency budget hữu hạn. Nếu upstream chỉ còn 80 ms nhưng downstream được gọi với timeout 2 s, system đã mất invariant về deadline: downstream có thể tiếp tục work sau khi kết quả không còn giá trị.

Tương tự, trace/request identity cần truyền qua proxy, runtime và downstream để evidence vẫn nối được cùng causal chain.

Một production path tốt cố giữ:

```text
remaining deadline
request/trace identity
attempt number
security principal cần thiết
idempotency context khi có side effect
```

qua mỗi boundary phù hợp.

## 3. DNS: cùng một hostname không bảo đảm cùng một endpoint

DNS là distributed caching system. Resolver cache, TTL, negative caching, split-horizon DNS và traffic steering có thể làm hai clients nhận kết quả khác nhau hợp lệ.

Failure mode không chỉ là “DNS down”. Cache miss có thể tăng latency, stale record có thể đưa traffic tới endpoint đã rút, TTL quá ngắn có thể tạo query pressure, và failover bằng DNS bị giới hạn bởi cache lifetime.

Evidence cần phân biệt DNS resolution time với connection time thay vì gộp cả hai thành “network”.

## 4. TCP: connection establishment, flow control và congestion đều có queue

Với TCP, handshake thêm RTT trước khi application data chảy trên cold connection. Sau đó throughput/latency chịu ảnh hưởng của congestion control, receive/send windows, packet loss và retransmission.

Một application timeout không chứng minh remote service chậm. Có thể request đang chờ retransmission, socket send buffer, SYN backlog hoặc connection establishment.

Persistent connection giảm setup cost nhưng tạo state: pool sizing, stale connection, connection lifetime và head-of-line behavior cần được quản lý.

## 5. TLS thêm identity vào transport path

TLS không chỉ mã hóa bytes; client còn xác minh peer identity qua certificate chain/hostname rules. Handshake cần cryptographic work và có thể cần thêm network round trips tùy protocol/version/resumption state.

Một certificate/PKI incident có thể xuất hiện dưới symptom “network connect fail”. Vì vậy lower layer thực sự quyết định behavior có thể là trust store, clock, certificate lifetime hoặc service identity chứ không phải HTTP code.

Đọc thêm [PKI, mTLS và service identity](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).

## 6. Proxy, WAF và load balancer là execution layers, không phải dây dẫn trong suốt

Edge/proxy có thể terminate TLS, authenticate, rate-limit, decompress/compress, cache, rewrite header, retry upstream và chọn backend. Mỗi operation có queue và policy riêng.

Nếu proxy tự retry một failed upstream call trong khi application/client cũng retry, amplification có thể xảy ra ở nhiều tầng mà team application không nhìn thấy.

Load balancer cũng quyết định locality và hot-spot behavior. “Các backend đều healthy” không có nghĩa chúng còn capacity an toàn; health check có thể xanh trong khi queue latency đã tăng mạnh.

## 7. Runtime: request đã tới process nhưng chưa chắc đã chạy handler

Trong application runtime, request có thể chờ event loop, worker/thread pool, coroutine scheduler, GC pause hoặc lock. Cần tách:

```text
queue wait
on-CPU execution
runtime pause
blocked/off-CPU wait
downstream wait
```

Async I/O giúp không giữ OS thread khi chờ I/O, nhưng không loại bỏ queue. Nếu event loop bị CPU-bound callback block, toàn bộ connections có thể tăng tail latency dù CPU tổng thể chưa đạt 100% trên máy nhiều core.

## 8. Connection pool là một admission-control boundary

Database/client pool giới hạn số operations active xuống downstream. Request có thể mất 300 ms để acquire connection rồi query chỉ chạy 20 ms.

Do đó metric `query duration = 20 ms` không phủ `database path = 320 ms` từ góc nhìn request. Evidence cần đo riêng pool wait, execute time và transaction lifetime.

Tăng pool size không miễn phí: nó có thể chỉ chuyển queue từ application sang database, nơi contention/lock/I/O làm service time tăng thêm.

## 9. Database và storage có nhiều loại waiting time

DB latency có thể gồm parse/plan, lock wait, buffer miss, CPU execution, WAL flush và replication wait. Hai query cùng SQL text có thể khác latency vì snapshot/lock/cache/storage state khác nhau.

Commit path đặc biệt có thể phụ thuộc filesystem/device/replication, nên tail latency ở request layer có thể bắt nguồn từ SSD garbage collection hoặc replica lag.

Xem [đường durability xuyên tầng](./03_durability_path_application_commit_wal_filesystem_device.md).

## 10. Fan-out khuếch đại tail latency

Nếu một request gọi 20 shards song song và cần đủ kết quả, critical path gần với slowest required branch. Khi fan-out tăng, xác suất gặp ít nhất một tail event cũng tăng.

Do đó p99 của service tổng không thể suy ra bằng cách nhìn average của từng dependency. Timeout budget và fallback phải reasoning trên call graph, không trên component đơn lẻ.

## 11. Retry bắt đầu như reliability mechanism nhưng có thể biến thành load generator

Retry hữu ích khi failure thật sự transient và operation an toàn để thử lại. Nhưng khi nguyên nhân là saturation, retry tăng arrival rate đúng lúc service rate đang giảm.

Causal loop điển hình:

```text
service time tăng
→ queue dài
→ latency vượt timeout
→ client/proxy retry
→ arrival rate thực tế tăng
→ queue dài hơn
→ context switch/GC/lock/DB pressure tăng
→ service time tiếp tục tăng
→ nhiều timeout hơn
→ cascading failure
```

Đây là **positive feedback loop**. Root condition có thể chỉ là một slowdown nhỏ, nhưng retry policy biến nó thành outage.

## 12. Timeout không phải safety valve nếu work không bị cancel

Client timeout chỉ có nghĩa client ngừng chờ. Server có thể vẫn xử lý request cũ. Nếu client retry, cùng business operation có hai attempts đồng thời.

Với read-heavy work, hậu quả chủ yếu là wasted capacity. Với side effect, hậu quả có thể là duplicate charge/order/message nếu thiếu idempotency.

Timeout design cần đi cùng cancellation/deadline propagation và idempotency policy.

## 13. Backoff + jitter giải đồng bộ retry, nhưng không tạo capacity

Exponential backoff giảm frequency attempt; jitter tránh hàng nghìn clients thức dậy cùng một thời điểm. Retry budget giới hạn tổng extra load mà retry được phép tạo.

Nhưng nếu dependency hết capacity kéo dài, backoff không làm service rate tăng. System vẫn cần **backpressure, bounded queue, admission control hoặc load shedding** ở boundary phù hợp.

Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 14. Queue nên nằm ở nơi có policy và evidence tốt nhất

Queue không tự xấu. Nó hấp thụ burst ngắn khi system có headroom để trả debt. Vấn đề là queue vô hạn hoặc queue nằm ở layer không có deadline/priority/visibility.

Một design tốt muốn biết:

```text
queue đang bảo vệ resource nào?
capacity của resource là gì?
request tối đa được chờ bao lâu?
khi đầy thì reject/degrade thế nào?
metric nào cho biết queue debt đang tăng?
```

Nếu có ba queues nối tiếp—proxy, thread pool, DB pool—mỗi queue có thể nhìn “không quá lớn” nhưng tổng waiting time đã phá SLO.

## 15. Load shedding bảo vệ invariant quan trọng hơn success rate tức thời

Khi overload, cố accept 100% request có thể làm 100% timeout. Reject sớm một phần traffic giúp giữ system trong safe operating region để phần còn lại hoàn thành.

Load shedding có thể theo priority/tenant/cost, nhưng isolation phải gắn với resource thật. Gắn nhãn “high priority” không giúp nếu mọi class cùng tranh một exhausted connection pool.

## 16. Performance pressure làm behavior thay đổi theo phase

Cùng một system có thể có ba phase khác nhau:

```text
low load: service time chiếm phần lớn latency
near knee: queue wait bắt đầu tăng mạnh
overload: retries + queue + contention làm service time cũng xấu đi
```

Đây là lý do benchmark ở 30% utilization không dự đoán được behavior tại 95%. Production capacity engineering cần tìm **utilization knee**, không chỉ maximum throughput.

## 17. Evidence: dựng waterfall và causal timeline

Một slow trace hữu ích cần spans bắt đầu đủ sớm: DNS/connection nếu client instrumentation có thể đo, edge/proxy, queue wait, runtime handler, pool acquire, DB execution, WAL/replication và response.

Kết hợp trace với metrics:

```text
arrival rate / retry rate
queue depth / wait time
active workers/connections
CPU run queue / GC pause
DB locks / pool utilization
network retransmission / connection errors
storage/replica latency
```

Một percentile aggregate không chỉ ra mechanism. Một trace đơn lẻ cũng không chứng minh capacity condition toàn hệ thống. Cần cả hai.

## 18. Clock và tracing có giới hạn

Duration trong cùng process nên dựa monotonic clock. Wall-clock giữa hosts có skew; distributed trace backend thường reconstruct đủ causal path nhưng không nên coi timestamp từ hai host như measurement vật lý tuyệt đối ở microsecond precision.

Sampling có thể bỏ rare tail incidents. Error-biased/tail sampling hữu ích nhưng metrics/logs vẫn cần làm independent evidence.

## 19. System Design reasoning từ request path

Khi thiết kế, đừng bắt đầu bằng “dùng Nginx/Kafka/Redis gì?”. Hãy bắt đầu bằng invariant và pressure:

```text
latency SLO là gì?
side effect có cần idempotent không?
capacity bottleneck nào hữu hạn?
queue nằm đâu?
retry budget ở tầng nào?
deadline được propagate không?
security principal đổi ở boundary nào?
failover có thay endpoint/connection state ra sao?
```

Technology chỉ là implementation của các contract này.

## 20. Mô hình tư duy

> HTTP request là một causal path qua DNS, transport, TLS identity, proxy/load balancer, runtime scheduler, pools, database và storage. Mỗi boundary có queue và contract riêng. **Retry có thể chuyển slowdown thành overload; backpressure và admission control giới hạn feedback loop; production evidence phải chỉ ra request đã chờ ở đâu và resource nào thật sự saturated.**

## Kết nối

Đọc cùng [DNS/HTTP/TLS foundation](../../basic/06_networks_distributed_systems/03_dns_http_tls_and_web_request.md), [Load balancing và connection pools](../../08_software_systems/advanced/03_load_balancing_connection_pools_and_locality.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [PKI/mTLS](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md), [Durability path](./03_durability_path_application_commit_wal_filesystem_device.md) và [Debugging xuyên abstraction layers](./00_debugging_across_abstraction_layers.md).