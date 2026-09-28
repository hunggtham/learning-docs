# End-to-end yêu cầu (request / 요청): DNS → TCP/TLS → proxy/bộ cân bằng tải (load balancer / 로드 밸런서) → thời gian chạy (runtime / 런타임) → cơ sở dữ liệu (database / 데이터베이스), và vòng thử lại (retry / 재시도) → overload

> **Mạch đọc:** Đặt **End-to-end yêu cầu (request / 요청): DNS → TCP/TLS → proxy/bộ cân bằng tải (load balancer / 로드 밸런서) → thời gian chạy (runtime / 런타임) → cơ sở dữ liệu (database / 데이터베이스), và vòng thử lại (retry / 재시도) → overload** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. đường đi của yêu cầu (request path / 요청 경로) thật sự bắt đầu trước HTTP handler** sang **2. bất biến (invariant / 불변식) end-to-end: deadline và nhân quả (causal / 인과적) ngữ cảnh (context / 맥락) phải sống qua mọi hop**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một yêu cầu (request / 요청) “mất 800 ms” không có một nguyên nhân duy nhất. Nó đi qua một chuỗi resolution, liên kết (connection / 연결), hàng đợi (queue / 큐), scheduler và lưu trữ (storage / 저장소) boundaries. Advanced lập luận (reasoning / 추론) không bắt đầu bằng câu “mạng (network / 네트워크) chậm” hay “cơ sở dữ liệu (database / 데이터베이스) chậm”; nó dựng **đường găng (critical path / 임계 경로)**, xác định bất biến (invariant / 불변식) ở từng ranh giới (boundary / 경계) và tìm nơi demand bắt đầu vượt sức chứa (capacity / 용량).

## 1. đường đi của yêu cầu (request path / 요청 경로) thật sự bắt đầu trước HTTP handler

Một cold yêu cầu (request / 요청) có thể đi qua:

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

Steady-state yêu cầu (request / 요청) có thể reuse DNS kết quả (result / 결과), liên kết (connection / 연결) và TLS session nên bỏ qua nhiều bước. Vì vậy benchmark warm liên kết (connection / 연결) và sự cố (incident / 인시던트) cold-start có thể là hai tải công việc (workload / 워크로드) khác nhau.

## 2. bất biến (invariant / 불변식) end-to-end: deadline và nhân quả (causal / 인과적) ngữ cảnh (context / 맥락) phải sống qua mọi hop

Một yêu cầu (request / 요청) có độ trễ (latency / 지연 시간) ngân sách (budget / 예산) hữu hạn. Nếu upstream chỉ còn 80 ms nhưng downstream được gọi với hết thời gian chờ (timeout / 타임아웃) 2 s, hệ thống (system / 시스템) đã mất bất biến (invariant / 불변식) về deadline: downstream có thể tiếp tục công việc (work / 작업) sau khi kết quả không còn giá trị.

Tương tự, dấu vết (trace / 추적)/yêu cầu (request / 요청) định danh (identity / 식별자) cần truyền qua proxy, thời gian chạy (runtime / 런타임) và downstream để bằng chứng (evidence / 증거) vẫn nối được cùng chuỗi nhân quả (causal chain / 인과 사슬).

Một môi trường vận hành (production / 운영 환경) đường dẫn (path / 경로) tốt cố giữ:

```text
remaining deadline
request/trace identity
attempt number
security principal cần thiết
idempotency context khi có side effect
```

qua mỗi ranh giới (boundary / 경계) phù hợp.

## 3. DNS: cùng một hostname không bảo đảm cùng một endpoint

DNS là phân tán (distributed / 분산) caching hệ thống (system / 시스템). Resolver bộ nhớ đệm (cache / 캐시), TTL, negative caching, split-horizon DNS và traffic steering có thể làm hai clients nhận kết quả khác nhau hợp lệ.

Dạng thất bại (failure mode / 실패 모드) không chỉ là “DNS down”. trượt bộ nhớ đệm (cache miss / 캐시 미스) có thể tăng độ trễ (latency / 지연 시간), stale bản ghi (record / 레코드) có thể đưa traffic tới endpoint đã rút, TTL quá ngắn có thể tạo truy vấn (query / 쿼리) pressure, và failover bằng DNS bị giới hạn bởi bộ nhớ đệm (cache / 캐시) thời gian tồn tại (lifetime / 수명).

Bằng chứng (evidence / 증거) cần phân biệt DNS resolution thời gian (time / 시간) với liên kết (connection / 연결) thời gian (time / 시간) thay vì gộp cả hai thành “mạng (network / 네트워크)”.

## 4. TCP: liên kết (connection / 연결) establishment, luồng (flow / 흐름) điều khiển (control / 제어) và congestion đều có hàng đợi (queue / 큐)

Với TCP, handshake thêm RTT trước khi ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터) chảy trên cold liên kết (connection / 연결). Sau đó thông lượng (throughput / 처리량)/độ trễ (latency / 지연 시간) chịu ảnh hưởng của congestion điều khiển (control / 제어), receive/send windows, packet mất mát (loss / 손실) và retransmission.

Một ứng dụng (application / 애플리케이션) hết thời gian chờ (timeout / 타임아웃) không chứng minh remote dịch vụ (service / 서비스) chậm. Có thể yêu cầu (request / 요청) đang chờ retransmission, socket send buffer, SYN backlog hoặc liên kết (connection / 연결) establishment.

Persistent liên kết (connection / 연결) giảm setup chi phí (cost / 비용) nhưng tạo trạng thái (state / 상태): pool sizing, stale liên kết (connection / 연결), liên kết (connection / 연결) thời gian tồn tại (lifetime / 수명) và head-of-line hành vi (behavior / 동작) cần được quản lý.

## 5. TLS thêm định danh (identity / 식별자) vào vận chuyển (transport / 전송) đường dẫn (path / 경로)

TLS không chỉ mã hóa bytes; máy khách (client / 클라이언트) còn xác minh peer định danh (identity / 식별자) qua certificate chuỗi (chain / 사슬)/hostname rules. Handshake cần cryptographic công việc (work / 작업) và có thể cần thêm mạng (network / 네트워크) round trips tùy giao thức (protocol / 프로토콜)/phiên bản (version / 버전)/resumption trạng thái (state / 상태).

Một certificate/PKI sự cố (incident / 인시던트) có thể xuất hiện dưới symptom “mạng (network / 네트워크) connect thất bại (fail / 실패)”. Vì vậy lower tầng (layer / 계층) thực sự quyết định hành vi (behavior / 동작) có thể là trust store, clock, certificate thời gian tồn tại (lifetime / 수명) hoặc dịch vụ (service / 서비스) định danh (identity / 식별자) chứ không phải HTTP mã (code / 코드).

Đọc thêm [PKI, mTLS và service identity](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md).

## 6. Proxy, WAF và bộ cân bằng tải (load balancer / 로드 밸런서) là thực thi (execution / 실행) layers, không phải dây dẫn trong suốt

Edge/proxy có thể terminate TLS, authenticate, rate-limit, decompress/compress, bộ nhớ đệm (cache / 캐시), rewrite header, thử lại (retry / 재시도) upstream và chọn backend. Mỗi thao tác (operation / 연산) có hàng đợi (queue / 큐) và chính sách (policy / 정책) riêng.

Nếu proxy tự thử lại (retry / 재시도) một failed upstream lời gọi (call / 호출) trong khi ứng dụng (application / 애플리케이션)/máy khách (client / 클라이언트) cũng thử lại (retry / 재시도), amplification có thể xảy ra ở nhiều tầng mà nhóm (team / 팀) ứng dụng (application / 애플리케이션) không nhìn thấy.

Bộ cân bằng tải (load balancer / 로드 밸런서) cũng quyết định locality và hot-spot hành vi (behavior / 동작). “Các backend đều healthy” không có nghĩa chúng còn sức chứa (capacity / 용량) an toàn; health check có thể xanh trong khi hàng đợi (queue / 큐) độ trễ (latency / 지연 시간) đã tăng mạnh.

## 7. thời gian chạy (runtime / 런타임): yêu cầu (request / 요청) đã tới tiến trình (process / 프로세스) nhưng chưa chắc đã chạy handler

Trong ứng dụng (application / 애플리케이션) thời gian chạy (runtime / 런타임), yêu cầu (request / 요청) có thể chờ vòng lặp sự kiện (event loop / 이벤트 루프), worker/luồng thực thi (thread / 스레드) pool, coroutine scheduler, GC pause hoặc khóa (lock / 잠금). Cần tách:

```text
queue wait
on-CPU execution
runtime pause
blocked/off-CPU wait
downstream wait
```

Async I/O giúp không giữ OS luồng thực thi (thread / 스레드) khi chờ I/O, nhưng không loại bỏ hàng đợi (queue / 큐). Nếu vòng lặp sự kiện (event loop / 이벤트 루프) bị CPU-bound callback khối (block / 블록), toàn bộ connections có thể tăng tail độ trễ (latency / 지연 시간) dù CPU tổng thể chưa đạt 100% trên máy nhiều cốt lõi (core / 핵심).

## 8. liên kết (connection / 연결) pool là một admission-control ranh giới (boundary / 경계)

Cơ sở dữ liệu (database / 데이터베이스)/máy khách (client / 클라이언트) pool giới hạn số operations active xuống downstream. yêu cầu (request / 요청) có thể mất 300 ms để acquire liên kết (connection / 연결) rồi truy vấn (query / 쿼리) chỉ chạy 20 ms.

Do đó chỉ số (metric / 지표) `query duration = 20 ms` không phủ `database path = 320 ms` từ góc nhìn yêu cầu (request / 요청). bằng chứng (evidence / 증거) cần đo riêng pool wait, execute thời gian (time / 시간) và giao dịch (transaction / 트랜잭션) thời gian tồn tại (lifetime / 수명).

Tăng pool kích thước (size / 크기) không miễn phí: nó có thể chỉ chuyển hàng đợi (queue / 큐) từ ứng dụng (application / 애플리케이션) sang cơ sở dữ liệu (database / 데이터베이스), nơi contention/khóa (lock / 잠금)/I/O làm dịch vụ (service / 서비스) thời gian (time / 시간) tăng thêm.

## 9. cơ sở dữ liệu (database / 데이터베이스) và lưu trữ (storage / 저장소) có nhiều loại waiting thời gian (time / 시간)

DB độ trễ (latency / 지연 시간) có thể gồm parse/plan, khóa (lock / 잠금) wait, buffer miss, CPU thực thi (execution / 실행), WAL flush và replication wait. Hai truy vấn (query / 쿼리) cùng SQL văn bản (text / 텍스트) có thể khác độ trễ (latency / 지연 시간) vì snapshot/khóa (lock / 잠금)/bộ nhớ đệm (cache / 캐시)/lưu trữ (storage / 저장소) trạng thái (state / 상태) khác nhau.

Lần ghi nhận (commit / 커밋) đường dẫn (path / 경로) đặc biệt có thể phụ thuộc filesystem/thiết bị (device / 장치)/replication, nên tail độ trễ (latency / 지연 시간) ở yêu cầu (request / 요청) tầng (layer / 계층) có thể bắt nguồn từ SSD garbage collection hoặc replica lag.

Xem [đường durability xuyên tầng](./03_durability_path_application_commit_wal_filesystem_device.md).

## 10. Fan-out khuếch đại tail độ trễ (latency / 지연 시간)

Nếu một yêu cầu (request / 요청) gọi 20 shards song song và cần đủ kết quả, đường găng (critical path / 임계 경로) gần với slowest required branch. Khi fan-out tăng, xác suất gặp ít nhất một tail sự kiện (event / 이벤트) cũng tăng.

Do đó p99 của dịch vụ (service / 서비스) tổng không thể suy ra bằng cách nhìn average của từng phụ thuộc (dependency / 의존성). ngân sách thời gian chờ (timeout budget / 타임아웃 예산) và fallback phải lập luận (reasoning / 추론) trên lời gọi (call / 호출) đồ thị (graph / 그래프), không trên thành phần (component / 컴포넌트) đơn lẻ.

## 11. thử lại (retry / 재시도) bắt đầu như độ tin cậy (reliability / 신뢰성) cơ chế (mechanism / 메커니즘) nhưng có thể biến thành tải (load / 로드) generator

Thử lại (retry / 재시도) hữu ích khi thất bại (failure / 실패) thật sự transient và thao tác (operation / 연산) an toàn để thử lại. Nhưng khi nguyên nhân là saturation, thử lại (retry / 재시도) tăng arrival tỷ lệ (rate / 비율) đúng lúc dịch vụ (service / 서비스) tỷ lệ (rate / 비율) đang giảm.

Nhân quả (causal / 인과적) vòng lặp (loop / 루프) điển hình:

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

Đây là **positive vòng phản hồi (feedback loop / 피드백 루프)**. gốc (root / 루트) điều kiện (condition / 조건) có thể chỉ là một slowdown nhỏ, nhưng thử lại (retry / 재시도) chính sách (policy / 정책) biến nó thành outage.

## 12. hết thời gian chờ (timeout / 타임아웃) không phải an toàn (safety / 안전) valve nếu công việc (work / 작업) không bị cancel

Máy khách (client / 클라이언트) hết thời gian chờ (timeout / 타임아웃) chỉ có nghĩa máy khách (client / 클라이언트) ngừng chờ. máy chủ (server / 서버) có thể vẫn xử lý yêu cầu (request / 요청) cũ. Nếu máy khách (client / 클라이언트) thử lại (retry / 재시도), cùng nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) có hai attempts đồng thời.

Với read-heavy công việc (work / 작업), hậu quả chủ yếu là wasted sức chứa (capacity / 용량). Với side tác động (effect / 효과), hậu quả có thể là duplicate charge/thứ tự (order / 순서)/message nếu thiếu idempotency.

Hết thời gian chờ (timeout / 타임아웃) thiết kế (design / 설계) cần đi cùng cancellation/deadline propagation và idempotency chính sách (policy / 정책).

## 13. Backoff + jitter giải đồng bộ thử lại (retry / 재시도), nhưng không tạo sức chứa (capacity / 용량)

Exponential backoff giảm frequency attempt; jitter tránh hàng nghìn clients thức dậy cùng một thời điểm. thử lại (retry / 재시도) ngân sách (budget / 예산) giới hạn tổng extra tải (load / 로드) mà thử lại (retry / 재시도) được phép tạo.

Nhưng nếu phụ thuộc (dependency / 의존성) hết sức chứa (capacity / 용량) kéo dài, backoff không làm dịch vụ (service / 서비스) tỷ lệ (rate / 비율) tăng. hệ thống (system / 시스템) vẫn cần **backpressure, bounded hàng đợi (queue / 큐), admission điều khiển (control / 제어) hoặc tải (load / 로드) shedding** ở ranh giới (boundary / 경계) phù hợp.

Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 14. hàng đợi (queue / 큐) nên nằm ở nơi có chính sách (policy / 정책) và bằng chứng (evidence / 증거) tốt nhất

Hàng đợi (queue / 큐) không tự xấu. Nó hấp thụ burst ngắn khi hệ thống (system / 시스템) có headroom để trả debt. Vấn đề là hàng đợi (queue / 큐) vô hạn hoặc hàng đợi (queue / 큐) nằm ở tầng (layer / 계층) không có deadline/priority/visibility.

Một thiết kế (design / 설계) tốt muốn biết:

```text
queue đang bảo vệ resource nào?
capacity của resource là gì?
request tối đa được chờ bao lâu?
khi đầy thì reject/degrade thế nào?
metric nào cho biết queue debt đang tăng?
```

Nếu có ba queues nối tiếp—proxy, luồng thực thi (thread / 스레드) pool, DB pool—mỗi hàng đợi (queue / 큐) có thể nhìn “không quá lớn” nhưng tổng waiting thời gian (time / 시간) đã phá SLO.

## 15. tải (load / 로드) shedding bảo vệ bất biến (invariant / 불변식) quan trọng hơn success tỷ lệ (rate / 비율) tức thời

Khi overload, cố accept 100% yêu cầu (request / 요청) có thể làm 100% hết thời gian chờ (timeout / 타임아웃). Reject sớm một phần traffic giúp giữ hệ thống (system / 시스템) trong safe operating region để phần còn lại hoàn thành.

Tải (load / 로드) shedding có thể theo priority/tenant/chi phí (cost / 비용), nhưng isolation phải gắn với tài nguyên (resource / 자원) thật. Gắn nhãn “high priority” không giúp nếu mọi lớp (class / 클래스) cùng tranh một exhausted liên kết (connection / 연결) pool.

## 16. hiệu năng (performance / 성능) pressure làm hành vi (behavior / 동작) thay đổi theo phase

Cùng một hệ thống (system / 시스템) có thể có ba phase khác nhau:

```text
low load: service time chiếm phần lớn latency
near knee: queue wait bắt đầu tăng mạnh
overload: retries + queue + contention làm service time cũng xấu đi
```

Đây là lý do benchmark ở 30% utilization không dự đoán được hành vi (behavior / 동작) tại 95%. môi trường vận hành (production / 운영 환경) sức chứa (capacity / 용량) kỹ thuật (engineering / 엔지니어링) cần tìm **utilization knee**, không chỉ maximum thông lượng (throughput / 처리량).

## 17. bằng chứng (evidence / 증거): dựng waterfall và nhân quả (causal / 인과적) timeline

Một slow dấu vết (trace / 추적) hữu ích cần spans bắt đầu đủ sớm: DNS/liên kết (connection / 연결) nếu máy khách (client / 클라이언트) instrumentation có thể đo, edge/proxy, hàng đợi (queue / 큐) wait, thời gian chạy (runtime / 런타임) handler, pool acquire, DB thực thi (execution / 실행), WAL/replication và phản hồi (response / 응답).

Kết hợp dấu vết (trace / 추적) với metrics:

```text
arrival rate / retry rate
queue depth / wait time
active workers/connections
CPU run queue / GC pause
DB locks / pool utilization
network retransmission / connection errors
storage/replica latency
```

Một percentile aggregate không chỉ ra cơ chế (mechanism / 메커니즘). Một dấu vết (trace / 추적) đơn lẻ cũng không chứng minh sức chứa (capacity / 용량) điều kiện (condition / 조건) toàn hệ thống. Cần cả hai.

## 18. Clock và tracing có giới hạn

Duration trong cùng tiến trình (process / 프로세스) nên dựa monotonic clock. Wall-clock giữa hosts có skew; phân tán (distributed / 분산) dấu vết (trace / 추적) backend thường reconstruct đủ nhân quả (causal / 인과적) đường dẫn (path / 경로) nhưng không nên coi timestamp từ hai host như đo lường (measurement / 측정) vật lý tuyệt đối ở microsecond precision.

Sampling có thể bỏ rare tail incidents. Error-biased/tail sampling hữu ích nhưng metrics/logs vẫn cần làm independent bằng chứng (evidence / 증거).

## 19. hệ thống (system / 시스템) thiết kế (design / 설계) lập luận (reasoning / 추론) từ đường đi của yêu cầu (request path / 요청 경로)

Khi thiết kế, đừng bắt đầu bằng “dùng Nginx/Kafka/Redis gì?”. Hãy bắt đầu bằng bất biến (invariant / 불변식) và pressure:

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

Technology chỉ là hiện thực (implementation / 구현) của các đặc tả hợp đồng (contract / 계약) này.

## 20. Mô hình tư duy

> HTTP yêu cầu (request / 요청) là một nhân quả (causal / 인과적) đường dẫn (path / 경로) qua DNS, vận chuyển (transport / 전송), TLS định danh (identity / 식별자), proxy/bộ cân bằng tải (load balancer / 로드 밸런서), thời gian chạy (runtime / 런타임) scheduler, pools, cơ sở dữ liệu (database / 데이터베이스) và lưu trữ (storage / 저장소). Mỗi ranh giới (boundary / 경계) có hàng đợi (queue / 큐) và đặc tả hợp đồng (contract / 계약) riêng. **thử lại (retry / 재시도) có thể chuyển slowdown thành overload; backpressure và admission điều khiển (control / 제어) giới hạn vòng phản hồi (feedback loop / 피드백 루프); bằng chứng vận hành (production evidence / 운영 증거) phải chỉ ra yêu cầu (request / 요청) đã chờ ở đâu và tài nguyên (resource / 자원) nào thật sự saturated.**

## Kết nối

Đọc cùng [DNS/HTTP/TLS foundation](../../basic/06_networks_distributed_systems/03_dns_http_tls_and_web_request.md), [Load balancing và connection pools](../../08_software_systems/advanced/03_load_balancing_connection_pools_and_locality.md), [Capacity/admission control](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md), [PKI/mTLS](../../07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md), [Durability path](./03_durability_path_application_commit_wal_filesystem_device.md) và [Debugging xuyên abstraction layers](./00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 debugging across abstraction layers](./00_debugging_across_abstraction_layers.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
