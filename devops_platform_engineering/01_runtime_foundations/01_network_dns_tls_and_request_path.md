# Từ URL đến process: DNS, TCP, TLS, proxy và request path

## 1. Network troubleshooting cần một đường đi cụ thể

Khi user nói “API không vào được”, câu đó chưa phải failure model. Request đi qua nhiều state: tên miền phải resolve, route phải tồn tại, TCP connection phải mở, TLS handshake phải thành công, proxy/load balancer phải chọn backend, backend phải listen, application phải xử lý dependency rồi response mới quay về.

Mental model hiệu quả là vẽ request path thay vì đoán:

```text
client
  ↓ DNS
IP / load balancer
  ↓ TCP + TLS
edge / ingress / reverse proxy
  ↓ service routing
backend endpoint
  ↓ socket
application process
  ↓
database / cache / external service
```

Mỗi mũi tên có failure mode và evidence riêng.

## 2. DNS là mapping có cache và thời gian sống

DNS không phải một “danh bạ tức thời”. Resolver có thể cache record theo TTL, nhiều tầng cache tồn tại ở OS, runtime, local DNS, cluster DNS và upstream resolver. Vì vậy vừa đổi record nhưng một số client vẫn đi IP cũ không nhất thiết là DNS “sai”; có thể là expected cache behavior.

Khi debug, cần phân biệt name resolution thất bại với connection thất bại. `dig` hoặc `nslookup` cho thấy resolver trả gì; nhưng application runtime có thể có cache policy khác. Trong Kubernetes còn có service discovery và cluster DNS, nên cùng một hostname có thể resolve khác tùy namespace/search domain.

## 3. TCP kiểm tra reachability ở mức connection

Nếu DNS đã trả đúng IP, bước sau là có mở TCP connection được không. `curl` tiện nhưng gộp DNS, TCP, TLS và HTTP thành một thao tác. Khi cần cô lập layer, có thể dùng `nc -vz host port`, `ss`, hoặc `curl -v` để xem sequence.

`connection refused` thường hàm ý route tới host tồn tại nhưng tại endpoint đó không có listener hoặc firewall chủ động reject. `timeout` có thể là packet bị drop, route sai, security policy hoặc server không phản hồi. Hai error này không nên được giải thích giống nhau.

## 4. TLS không chỉ là encryption

TLS vừa bảo vệ kênh vừa xác thực danh tính endpoint thông qua certificate chain và hostname validation. Một service có thể reachable ở TCP nhưng TLS fail vì certificate hết hạn, SAN không khớp hostname, trust chain thiếu intermediate hoặc client/server không có cipher/protocol chung.

Trong service-to-service, mutual TLS còn xác thực cả client. Cơ chế PKI, certificate validation và service identity đã có canonical chapter tại [PKI, mTLS và service identity](../../computer_science/07_security_reliability/advanced/02_pki_certificate_validation_mtls_and_service_identity.md). DevOps cần tập trung vào lifecycle: ai issue cert, ai rotate, trust bundle phân phối thế nào, expiry được alert trước bao lâu và rollout có backward compatibility không.

## 5. Load balancer và reverse proxy tạo thêm state

Load balancer không đơn giản “chia đều request”. Nó có health state, connection pool, timeout, retry, algorithm và có thể terminate TLS. Nếu health check path khác behavior thật, backend có thể được coi healthy nhưng user request vẫn fail. Nếu proxy timeout 30 giây nhưng application timeout 60 giây, request có thể bị client-facing failure trong khi backend vẫn tiếp tục xử lý.

Timeout nên được thiết kế như budget giảm dần dọc request path. Upstream timeout phải dài hơn downstream operation đủ để application có thời gian xử lý failure và trả response, nhưng không dài đến mức giữ resource vô hạn.

## 6. Retry có thể cứu transient failure hoặc khuếch đại outage

Retry hữu ích khi failure tạm thời và operation an toàn để lặp. Nhưng khi downstream đã quá tải, mỗi request retry thêm làm traffic tăng, tạo feedback dương và có thể biến latency spike thành outage. Retry cần deadline, backoff, jitter và giới hạn attempt; write operation còn cần idempotency semantics.

Distributed failure semantics được đào sâu ở [distributed transactions, exactly-once và failure semantics](../../computer_science/06_networks_distributed_systems/advanced/00_distributed_transactions_exactly_once_and_failure_semantics.md). Ở tầng platform, invariant là retry policy phải nhìn thấy được và không được mặc định vô hạn trong nhiều proxy layer cùng lúc.

## 7. Kubernetes thêm virtual network abstraction

Trong Kubernetes, `Service` thường cung cấp virtual endpoint ổn định trong khi `Pod` endpoint thay đổi. Ingress/Gateway nhận traffic từ ngoài và route vào service. Network policy có thể giới hạn flow. CNI implementation quyết định packet đi như thế nào nhưng mental model trước tiên vẫn là: name → virtual service → endpoint → pod socket.

Khi một `Service` không trả traffic, kiểm tra selector/endpoints trước khi đổ lỗi cho DNS. Nếu endpoint list rỗng, name resolution có thể hoàn toàn đúng nhưng không có backend. Nếu endpoint có và pod listen, tiếp tục kiểm tra port mapping, readiness, network policy và proxy/data-plane state.

## 8. NAT và địa chỉ quan sát được

NAT thay đổi source/destination address ở một số boundary. Điều này quan trọng với allowlist, logging và rate limit. Application có thể thấy IP của proxy thay vì client thật; proxy có thể đưa original client IP qua header nhưng chỉ nên trust header từ proxy boundary đã biết.

Khi debug “IP nào đang gọi”, phải hỏi ở layer nào. Packet capture trên node, load balancer access log và application access log có thể hiển thị ba địa chỉ khác nhau mà đều đúng theo perspective của chúng.

## 9. Một bài toán debug từng bước

Giả sử `https://api.example.com/orders` trả `502`.

Đầu tiên xác nhận DNS trả endpoint mong muốn. Sau đó `curl -v` để biết TLS có hoàn thành không. Nếu TLS thành công và response là HTTP 502 từ ingress, client-to-ingress path về cơ bản đã hoạt động. Tập trung sang ingress-to-backend.

Kiểm tra route/service mapping. Nếu Kubernetes service không có endpoint, xem label selector và readiness. Nếu endpoint có, kiểm tra pod có listen đúng port bằng `ss -lntp` hoặc probe phù hợp. Nếu pod nhận request nhưng trả chậm, xem application trace/log và downstream dependency. Đây là cách giảm search space theo evidence.

## 10. Senior note: request path là dependency graph có deadline

Một request synchronous là một chuỗi dependency về thời gian. Nếu request đi qua năm hop và mỗi hop dùng timeout 30 giây độc lập, worst-case behavior có thể vượt xa user deadline. Platform nên cung cấp convention về connection timeout, request deadline, retry và propagation của correlation/trace context.

Khi topology thay đổi, mental model vẫn giữ nguyên: xác định name resolution, connection, identity, routing, endpoint health, application behavior và downstream dependency. Tool chỉ giúp lấy evidence ở từng điểm.