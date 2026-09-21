# Reverse Proxy, Load Balancing và đường đi của HTTP Request

Một backend production hiếm khi để client kết nối trực tiếp tới Java process. Request thường đi qua nhiều lớp:

```text
client
  ↓
DNS
  ↓
CDN / WAF
  ↓
load balancer
  ↓
reverse proxy
  ↓
application server
  ↓
database / downstream service
```

Mỗi lớp thêm khả năng kiểm soát, nhưng cũng thêm state, timeout và failure mode. Khi user nhận `502`, `504` hoặc request timeout, muốn chẩn đoán đúng cần hiểu từng lớp đang làm gì.

## Proxy là gì?

**Proxy** là thành phần đứng giữa hai phía và chuyển tiếp traffic.

Có hai khái niệm thường gặp:

- **forward proxy** đại diện cho client khi đi ra ngoài;
- **reverse proxy** đại diện cho server/application khi nhận traffic từ client.

Reverse proxy như Nginx, HAProxy, Envoy hoặc cloud load balancer thường nhận request trước backend.

Client nhìn thấy proxy như endpoint chính, còn proxy biết backend thật.

## Vì sao cần reverse proxy?

Một Java application có thể tự terminate TLS và serve HTTP trực tiếp. Nhưng reverse proxy cho phép tách nhiều trách nhiệm:

- TLS termination;
- routing theo hostname/path;
- load balancing;
- connection management;
- compression;
- rate limiting;
- access logging;
- health checks;
- static file serving;
- request/response header normalization.

Việc tách này giúp application tập trung business logic, nhưng architecture trở thành multi-hop.

## Reverse proxy không phải “chỉ forward packet”

Ở layer 7, proxy có thể terminate TCP/TLS, parse HTTP rồi tạo một connection khác tới backend.

Ví dụ:

```text
client TCP connection
    ↓
Nginx
    ↓
backend TCP connection
```

Hai connection này độc lập về timeout, keep-alive và socket state.

Do đó client timeout 30 giây không nhất thiết bằng backend timeout 30 giây.

## Layer 4 và Layer 7 load balancing

**Layer 4 load balancer** thường cân bằng theo TCP/UDP connection mà không cần hiểu HTTP semantics sâu.

**Layer 7 load balancer** hiểu HTTP hostname, path, headers và có thể route:

```text
/api/users  → user-service
/api/orders → order-service
```

Layer 7 cho flexibility cao hơn nhưng cần nhiều processing và protocol awareness hơn.

## Load balancing giải quyết vấn đề gì?

Một backend instance có capacity hữu hạn. Nếu toàn bộ traffic vào một process, nó có thể trở thành single point of failure và bottleneck.

Load balancer phân phối request/connections tới nhiều upstreams:

```text
             ┌─ app-1
client → LB ─┼─ app-2
             └─ app-3
```

Nhưng “chia đều” không phải lúc nào cũng tối ưu. Request cost có thể khác nhau, connection có thể sống lâu và instance capacity có thể không đồng nhất.

## Round robin

Thuật toán đơn giản là lần lượt chọn backend:

```text
request 1 → A
request 2 → B
request 3 → C
request 4 → A
```

Round robin hoạt động tốt khi request cost tương đối tương đồng và backend có capacity gần nhau.

Nhưng nếu một request chạy 30 giây còn request khác 10 ms, số request không phản ánh current load.

## Least connections

**Least connections** chọn backend đang có ít active connections hơn.

Cách này có thể phù hợp với long-lived connections hơn round robin, nhưng connection count vẫn không nói đầy đủ CPU/memory/business cost.

## Weighted balancing

Nếu server A mạnh gấp đôi server B, có thể dùng weight:

```text
A weight 2
B weight 1
```

A nhận tỷ lệ traffic cao hơn.

Weight là model capacity gần đúng, không phải guarantee performance.

## Consistent hashing

Một số hệ thống muốn cùng key/client thường đi tới cùng backend để tăng cache locality hoặc session affinity.

Consistent hashing giảm số keys bị remap khi backend thay đổi so với modulo hashing đơn giản.

Nhưng sticky routing tạo trade-off: distribution có thể kém đều và failure recovery phức tạp hơn.

## Session affinity và vấn đề stateful application

Nếu user session chỉ tồn tại trong memory của một application instance:

```text
request 1 → app-A → session exists
request 2 → app-B → session missing
```

Load balancer có thể dùng sticky session, nhưng solution tốt hơn trong nhiều hệ thống là đưa session/state ra shared store hoặc dùng stateless token khi phù hợp.

Load balancing hoạt động tốt nhất khi application instance có thể thay thế lẫn nhau.

## Health check

Load balancer không nên gửi traffic tới instance chết.

Health check có thể kiểm tra:

```http
GET /health
```

Nhưng thiết kế health endpoint cần cẩn thận.

Nếu health check phụ thuộc database/downstream và dependency tạm chậm, mọi app instances có thể đồng loạt bị đánh dấu unhealthy, làm outage nặng hơn.

Cần phân biệt:

- **liveness**: process còn sống hay không;
- **readiness**: instance có sẵn sàng nhận traffic hay không;
- **dependency health**: downstream có khỏe không.

Không nên gộp tất cả vào một boolean đơn giản.

## Passive health và active health

**Active health check** gửi request định kỳ tới backend.

**Passive health check** quan sát failure từ traffic thật, ví dụ consecutive connection errors.

Kết hợp hai cách có thể phản ánh state tốt hơn, nhưng cần tránh flap khi backend chỉ có transient latency.

## 502 Bad Gateway

HTTP `502 Bad Gateway` thường nghĩa proxy nhận response không hợp lệ hoặc không thể thiết lập/duy trì communication đúng với upstream.

Các nguyên nhân có thể gồm:

- backend process không listen;
- connection refused;
- backend reset connection;
- TLS upstream mismatch;
- protocol mismatch;
- malformed response.

`502` chỉ là symptom ở proxy layer. Cần xem proxy log và backend state.

## 504 Gateway Timeout

`504 Gateway Timeout` thường nghĩa proxy đã chờ upstream vượt timeout.

Backend có thể:

- xử lý quá lâu;
- chờ database lock;
- chờ downstream API;
- thread pool exhausted;
- network packet loss;
- timeout chain cấu hình không hợp lý.

Không nên chỉ tăng proxy timeout. Nếu root cause là dependency latency, tăng timeout có thể làm connections tích tụ lâu hơn và tạo resource exhaustion.

## Timeout phải được thiết kế theo chuỗi

Giả sử:

```text
client timeout     = 30s
load balancer      = 60s
Nginx proxy timeout= 90s
Java DB timeout    = 120s
```

Client đã bỏ cuộc ở giây 30 nhưng backend có thể tiếp tục giữ thread/DB connection thêm nhiều chục giây.

Một design thường hợp lý hơn là timeout phía trong nhỏ hơn hoặc aligned với request budget tổng, tùy architecture.

Mental model:

```text
request deadline
   ↓
proxy budget
   ↓
application budget
   ↓
dependency budget
```

Timeout nên phản ánh end-to-end latency objective, không phải các con số độc lập.

## Retry có thể khuếch đại sự cố

Nếu proxy retry request fail sang backend khác, reliability có thể tăng với transient failure.

Nhưng khi upstream chậm, retry tạo thêm traffic:

```text
100 requests
× 3 retries
= tối đa 300 attempts
```

Đây là **retry amplification**.

Nếu nhiều layers đều retry, amplification có thể nhân lên mạnh.

Retry cần:

- giới hạn attempts;
- timeout nhỏ;
- exponential backoff khi phù hợp;
- jitter;
- chỉ retry idempotent operations nếu không có deduplication semantics.

## Idempotency và retry POST

Retry `GET` thường ít nguy hiểm hơn retry một operation tạo payment/order.

Nếu client gửi:

```http
POST /payments
```

rồi timeout nhưng server đã xử lý thành công, retry có thể tạo duplicate payment.

Giải pháp có thể dùng **idempotency key**:

```http
Idempotency-Key: abc123
```

Backend lưu kết quả và nhận diện retry cùng operation.

Đây là connection giữa networking reliability và business correctness.

## Keep-alive và connection pooling

Proxy thường giữ persistent connection tới backend để giảm TCP/TLS handshake overhead.

Nếu keep-alive pool quá nhỏ, connection churn tăng. Nếu quá lớn, backend có thể bị giữ quá nhiều sockets.

Các metrics cần nhìn:

- active connections;
- idle keep-alive connections;
- connection creation rate;
- TIME_WAIT;
- upstream latency.

## Queue tại proxy

Khi upstream capacity đầy, proxy có thể có pending requests/connections.

Queue không tự động xấu. Một queue nhỏ hấp thụ burst. Nhưng khi arrival rate > service rate kéo dài, queue tăng liên tục và latency tăng.

Đây là application của queueing theory.

Xem thêm: [Capacity planning](../09_production/capacity_planning_server_sizing.md).

## Backpressure

**Backpressure** là cơ chế để hệ thống phía sau báo rằng nó không thể nhận work vô hạn.

Nếu load balancer/proxy cứ tiếp tục nhận mọi request và xếp queue vô hạn, memory/latency cuối cùng collapse.

Better behavior có thể là reject sớm bằng `429`/`503` khi capacity đã đạt threshold phù hợp.

Fail fast đôi khi bảo vệ system tốt hơn “cố xử lý tất cả”.

## Rate limiting

Proxy có thể giới hạn request rate theo IP, user/token hoặc endpoint.

Rate limiting giúp chống abuse và bảo vệ backend, nhưng threshold phải dựa traffic model.

Một endpoint login và một endpoint file download có cost khác nhau; chỉ dùng requests/second không phản ánh mọi resource cost.

## TLS termination

Reverse proxy thường terminate TLS:

```text
client HTTPS
   ↓
proxy terminates TLS
   ↓
HTTP hoặc HTTPS tới backend
```

Nếu proxy→backend dùng HTTP, traffic nội bộ không được TLS bảo vệ. Có phù hợp hay không phụ thuộc trust boundary.

Một số environment dùng TLS ở cả hai đoạn hoặc mTLS.

## X-Forwarded-* headers

Khi proxy tạo connection mới tới backend, backend nhìn source IP của proxy thay vì client thật.

Proxy có thể thêm:

```text
X-Forwarded-For
X-Forwarded-Proto
X-Forwarded-Host
```

hoặc standard `Forwarded` header.

Application chỉ nên tin các headers này từ proxy đáng tin cậy. Nếu client internet có thể tự set header và app tin vô điều kiện, audit/security logic có thể bị giả mạo.

## Client IP và nhiều proxy hops

`X-Forwarded-For` có thể là list:

```text
client, proxy1, proxy2
```

Muốn lấy client IP đúng cần biết số trusted proxy hops và framework configuration.

Không nên đơn giản chọn giá trị đầu/cuối mà không hiểu topology.

## Reverse proxy và WebSocket

WebSocket bắt đầu bằng HTTP upgrade rồi chuyển sang long-lived bidirectional connection.

Proxy phải hỗ trợ upgrade headers và timeout phù hợp.

Long-lived connections cũng làm load balancing theo request count kém meaningful hơn.

## HTTP/2 multiplexing

Một HTTP/2 connection có thể mang nhiều concurrent streams.

Do đó connection count client→proxy không trực tiếp tương đương request concurrency.

Nếu proxy dùng HTTP/1.1 tới backend, một HTTP/2 client connection có thể fan out thành nhiều upstream connections/requests.

## Nginx upstream example

Ví dụ đơn giản:

```nginx
upstream app_backend {
    server 10.0.0.11:8080;
    server 10.0.0.12:8080;
}

server {
    listen 443 ssl;

    location / {
        proxy_pass http://app_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Đây chỉ là skeleton. Production cần timeout, TLS, health behavior, logging, buffering và security settings phù hợp.

## Proxy buffering

Một reverse proxy có thể buffer request/response thay vì stream ngay.

Buffering có lợi vì backend có thể trả nhanh rồi proxy gửi chậm cho client. Nhưng với streaming/SSE/large upload, buffering có thể gây latency hoặc memory/disk use không mong muốn.

Behavior cần align workload.

## Load balancer ở cloud

AWS ALB/NLB, GCP Load Balancer, Azure Load Balancer hay Kubernetes Ingress đều cung cấp abstraction khác nhau nhưng các nguyên lý vẫn giống:

- listener;
- target/backend pool;
- health check;
- routing;
- connection timeout;
- TLS;
- observability.

Không nên học từng vendor như hệ thống hoàn toàn riêng. Hãy map chúng về network/proxy mental model.

## Kubernetes Service và Ingress

Kubernetes `Service` cung cấp stable virtual endpoint cho pods. Ingress/Gateway xử lý layer 7 routing tùy implementation.

Request path có thể là:

```text
external LB
 → ingress controller
 → Kubernetes Service
 → Pod
```

Mỗi layer có logs/metrics/state riêng. `curl podIP` thành công không chứng minh external ingress path đúng.

## Debug 502/504 theo layer

Bắt đầu từ proxy host:

```bash
curl -v http://backend-ip:8080/health
```

Nếu fail, vấn đề nằm backend/network giữa proxy và backend.

Kiểm tra listener backend:

```bash
ss -lntp | grep ':8080'
```

Xem proxy log:

```bash
journalctl -u nginx
```

hoặc access/error logs.

Sau đó correlate timestamp với backend logs.

## Access log như structured evidence

Một proxy access log tốt nên có:

- request timestamp;
- method/path;
- status;
- total request time;
- upstream address;
- upstream connect time;
- upstream response time;
- request ID.

Ví dụ nếu total time 10s nhưng upstream time 9.9s, proxy overhead ít khả năng là bottleneck chính.

Nếu connect time cao, connection establishment/network/upstream accept path đáng điều tra.

## Request ID propagation

Proxy có thể tạo hoặc forward request ID:

```text
X-Request-ID: 7f8a...
```

Backend log cùng ID giúp nối:

```text
proxy access log
 ↔ application log
 ↔ downstream log
```

Đây là nền tảng distributed tracing đơn giản.

## Mô hình tư duy (Mental Model)

Reverse proxy/load balancer là **một application mạng có state và resource riêng**, không phải “đường ống trong suốt”.

Khi request đi qua proxy, hãy theo dõi:

```text
DNS
 ↓
client→proxy connection
 ↓
TLS / HTTP parsing
 ↓
routing / load-balancing decision
 ↓
proxy→backend connection
 ↓
backend processing
 ↓
response path
```

Mỗi mũi tên có timeout, queue và failure mode riêng.

## Những hiểu lầm phổ biến

**“502 nghĩa backend code trả 502.”** Thường 502 được proxy tạo vì upstream communication failure.

**“504 chỉ cần tăng timeout.”** Nếu backend thực sự saturated, tăng timeout có thể làm tình hình tệ hơn.

**“Round robin luôn chia tải đều.”** Request cost và connection lifetime khác nhau.

**“Health endpoint càng kiểm tra nhiều dependency càng tốt.”** Health check quá coupled có thể tạo cascading failure.

**“Retry luôn tăng reliability.”** Retry không kiểm soát có thể tạo amplification và duplicate side effects.

**“Proxy không ảnh hưởng performance.”** Proxy có connection pools, buffers, TLS cost, queues và resource limits riêng.

## Xem thêm

- [DNS resolution internals](./dns_resolution_internals.md)
- [IP routing, NAT và conntrack](./ip_routing_nat_conntrack.md)
- [TCP, HTTP và TLS](./tcp_http_tls.md)
- [Java backend incident playbook](../09_production/java_backend_incident_playbook.md)
- [Capacity planning và server sizing](../09_production/capacity_planning_server_sizing.md)
