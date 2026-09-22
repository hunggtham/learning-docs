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

## 11. Connection cũng là tài nguyên hữu hạn ở phía client

Mỗi TCP connection dùng socket/file descriptor và thường chiếm một source port tạm thời (ephemeral port). Khi application mở rất nhiều outbound connection ngắn sống, không reuse connection hoặc retry storm, client/NAT có thể hết port khả dụng trước khi server CPU cao.

Triệu chứng có thể là connect timeout hoặc lỗi mở connection trong khi DNS, server listener và server CPU đều bình thường. Vì vậy outbound failure cần nhìn cả client-side socket state, connection pool và NAT boundary, không chỉ server.

`TIME_WAIT` không tự động là bug; nó là phần của TCP lifecycle giúp tránh packet cũ bị nhầm với connection mới. Nhưng connection churn cực lớn làm port/socket state tăng và trở thành capacity concern. Reuse/pooling/keep-alive đúng cách thường tốt hơn chỉ tăng port range.

## 12. NAT/conntrack có state và có thể là bottleneck ẩn

Firewall/NAT/load balancer thường giữ connection-tracking state. Một node hoặc gateway có thể hết conntrack table/translation capacity dù application metric bình thường. Khi đó packet mới bị drop hoặc connection setup thất bại không đồng đều.

Pattern hay gặp là nhiều Pod cùng node gọi một external endpoint qua cùng NAT, hoặc retry storm làm số connection mới tăng đột biến. Evidence cần đi xuống node/gateway metric: active connection, conntrack usage, SNAT port allocation, packet drop.

Đây là ví dụ network abstraction “rò”: service chỉ thấy `connect timeout`, nhưng bottleneck nằm ở shared network state bên dưới.

## 13. Long-lived connection làm DNS change không có hiệu lực ngay

DNS TTL chỉ ảnh hưởng lần resolve. Nếu client đã giữ HTTP keep-alive, HTTP/2 hoặc database connection lâu dài, nó có thể tiếp tục nói chuyện với endpoint cũ ngay cả khi DNS cache đã hết hạn cho lookup mới.

Vì vậy migration bằng DNS cần xét connection lifetime và draining. “TTL đã xuống 30 giây nên sau 30 giây mọi traffic sang IP mới” là giả định sai nếu connection hiện tại sống hàng phút hoặc hàng giờ.

Khi thay load balancer/database endpoint, cần plan cho cả resolver cache **và** connection pool lifecycle.

## 14. Timeout budget phải tính cả retry và queue

Giả sử user deadline là 2 giây. Service A gọi B timeout 1,5 giây và retry một lần. Nếu attempt đầu dùng hết 1,5 giây, attempt hai gần như không còn thời gian để hoàn thành trước user deadline. Nếu B còn queue nội bộ, timeout ở A không biết work đã bắt đầu hay chưa.

Thiết kế tốt truyền deadline hoặc tính remaining budget. Downstream timeout phải ngắn hơn remaining upstream deadline đủ để trả failure có kiểm soát. Retry chỉ được thực hiện nếu còn budget và operation an toàn.

Timeout không nên được chọn độc lập từng team. Nó là một contract xuyên call graph.

## 15. Retry multiplication giữa nhiều layer

Nếu client retry 3 lần, proxy retry 2 lần và application SDK retry 3 lần, một user request có thể tạo số attempt downstream lớn hơn rất nhiều so với ý định của từng layer. Không phải lúc nào cũng đạt tích số tối đa vì timeout/deadline, nhưng risk amplification là thật.

Vì vậy platform cần convention “layer nào sở hữu retry”. Proxy có thể retry connect failure cho idempotent request; application có domain context để biết operation nào safe. Không nên bật retry mặc định ở mọi layer mà không nhìn toàn path.

## 16. 502, 503 và 504 chỉ là clue theo vị trí phát sinh

Mã lỗi từ proxy thường gợi layer nhưng không phải universal truth. `502` thường nghĩa proxy không nhận response hợp lệ từ upstream; `503` có thể không có backend ready/overload; `504` thường là upstream timeout. Implementation cụ thể có thể khác.

Do đó luôn xác định **ai phát status** bằng response header/access log rồi mới suy luận. Một application cũng có thể tự trả 503; nhìn status code mà không biết emitter dễ đi sai layer.

## 17. Senior walkthrough: chỉ một số Pod không gọi được external API

Giả sử 30% Pod timeout khi gọi external payment API, server payment không thấy request tương ứng. DNS giống nhau, Pod CPU/memory bình thường. Nếu các Pod lỗi tập trung trên vài node, hypothesis chuyển sang node/network boundary.

Kiểm tra node NAT/conntrack/SNAT port, CNI/network policy và outbound route. Nếu conntrack gần đầy hoặc SNAT allocation cạn đúng trên node lỗi, scale thêm Pod vào cùng node có thể làm tệ hơn. Mitigation có thể phân tán workload/node, giảm connection churn/retry hoặc tăng gateway capacity tùy architecture.

Causal chain quan trọng: partial failure theo node là dimension giúp giảm search space từ “external API không ổn” xuống “shared egress state trên subset node”.

## 18. Negative DNS cache có thể kéo dài failure sau khi record đã được sửa

Cache không chỉ lưu câu trả lời thành công. Resolver/runtime cũng có thể cache kết quả âm như `NXDOMAIN` hoặc lookup failure trong một khoảng thời gian. Vì vậy một hostname vừa được tạo hoặc vừa sửa có thể vẫn fail trên một số client dù authoritative DNS hiện đã đúng.

Trong incident migration, cần hỏi client nào đã lookup vào thời điểm record chưa tồn tại và runtime đó giữ negative result bao lâu. Restart process đôi khi “sửa” vì xóa cache cục bộ, nhưng đó chỉ là observation. Long-term fix là hiểu resolver/cache contract, chuẩn bị record trước cutover và tránh giả định mọi client re-query ngay.

DNS debugging trưởng thành luôn xác định **resolver path + cache lifetime + connection lifetime**, không chỉ chạy một `dig` từ laptop operator.

## 19. Connection pool có queue riêng và có thể che network khỏe

Application thường không mở socket mới cho mỗi request mà mượn connection từ pool. Khi pool đã dùng hết, request có thể chờ trong pool queue trước khi bất kỳ packet nào được gửi đi. Từ góc nhìn server downstream, không có traffic; từ góc nhìn user, request vẫn timeout.

Do đó cần tách `pool wait time`, `connect time`, TLS time và request/service time. Nếu pool wait tăng nhưng connect/request latency của connection đã mượn vẫn bình thường, bottleneck nằm ở client-side concurrency/pool sizing hoặc connection leak, không nằm ở network path.

Tăng pool size không luôn là fix. Pool lớn hơn làm tăng concurrency downstream và có thể đẩy database/API vào saturation. Connection pool là một admission-control boundary nhỏ; sizing phải gắn với downstream budget.

## 20. MTU mismatch có thể tạo “kết nối được nhưng request lớn bị treo”

Đường mạng có giới hạn kích thước packet tối đa theo từng hop. Nếu Path MTU Discovery hoạt động không đúng hoặc ICMP cần thiết bị chặn, packet lớn có thể bị drop trong khi packet nhỏ vẫn đi được. Triệu chứng điển hình là TCP connect/TLS ban đầu có vẻ ổn nhưng upload, response lớn hoặc một số protocol message lại timeout.

Failure này dễ bị hiểu nhầm thành application bug vì health check nhỏ vẫn xanh. Evidence cần so request nhỏ/lớn, packet retransmission và MTU trên overlay/VPN/tunnel path. Trong môi trường container/VXLAN/WireGuard, encapsulation làm effective MTU nhỏ hơn physical network.

Không nên “fix” bằng hạ MTU ngẫu nhiên toàn hệ thống. Mục tiêu là tìm boundary nào làm packet vượt effective path MTU và cấu hình endpoint/tunnel nhất quán.

## 21. HTTP/2 multiplexing giảm connection count nhưng tạo failure scope khác

Với HTTP/1.1, nhiều client thường dùng pool nhiều connection để song song request. HTTP/2 cho phép nhiều stream multiplex trên một connection. Điều này giảm connection churn nhưng làm một connection trở thành shared transport cho nhiều request.

Nếu connection HTTP/2 gặp packet loss, GOAWAY, flow-control hoặc proxy reset, nhiều stream có thể bị ảnh hưởng cùng lúc. Vì vậy metric “chỉ có vài connection” không có nghĩa blast radius nhỏ. Cần quan sát stream/request error cùng connection lifecycle.

Platform không cần buộc mọi team hiểu frame protocol chi tiết, nhưng phải tránh assumption `1 connection = 1 request`. Capacity và failure reasoning phải theo protocol semantics thực tế.

## 22. Load balancer health là một observation có độ trễ

Backend có thể vừa fail nhưng load balancer chưa mark unhealthy cho tới vài lần probe; hoặc backend vừa hồi nhưng chưa được đưa lại vào pool. Trong cửa sổ đó, một phần traffic có thể vẫn đi sai nơi hoặc capacity thực thấp hơn dashboard application nghĩ.

Health-check interval, unhealthy/healthy threshold, connection draining và endpoint propagation tạo một control loop riêng. Nếu rollout đổi hàng loạt backend nhanh hơn health system hội tụ, transient 5xx có thể xuất hiện dù từng process shutdown “đúng”.

Khi điều tra, overlay backend lifecycle với health-state transition và routing evidence. “Pod Ready” và “load balancer đã route ổn định” là hai state khác nhau.

## 23. Senior walkthrough: health check xanh nhưng upload file lớn timeout

Giả sử GET `/health` và request JSON nhỏ đều thành công, nhưng upload trên 2 MiB treo qua VPN/overlay path. Server application không thấy request hoàn chỉnh, CPU và pool bình thường. Đây là clue rằng failure phụ thuộc packet size/path chứ không phụ thuộc business logic.

So sánh direct path với tunneled path, kiểm tra retransmission và effective MTU. Nếu tunnel thêm encapsulation làm packet lớn bị black-hole trong khi ICMP feedback bị chặn, health check nhỏ sẽ không phát hiện.

Bài học là synthetic check chỉ chứng minh đúng workload mà nó thực sự phát. Production verification phải đại diện đủ các property quan trọng của request path: size, protocol, identity, route và deadline.