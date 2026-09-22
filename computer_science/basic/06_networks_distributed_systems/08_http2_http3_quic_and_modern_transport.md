# HTTP/2, HTTP/3, QUIC và modern transport

HTTP/1.1 over TCP/TLS vẫn là nền lịch sử quan trọng, nhưng web hiện đại phát triển để giảm connection overhead, multiplex requests tốt hơn và cải thiện behavior khi packet loss xảy ra. Muốn hiểu HTTP/2 và HTTP/3, cần tách ba lớp thường bị trộn lẫn: **HTTP semantics**, **stream multiplexing**, và **transport delivery/congestion behavior**.

Một request `GET /api/users` vẫn mang HTTP semantics dù chạy qua HTTP/1.1, HTTP/2 hay HTTP/3. Điều thay đổi mạnh là cách nhiều requests chia sẻ connection, cách bytes được đánh số/giao lại sau loss và cách handshake/security state được thiết lập.

## 1. HTTP/1.1 và giới hạn của connection-level parallelism

HTTP/1.1 hỗ trợ persistent connection, nhưng một connection vẫn là một TCP byte stream có thứ tự. Pipelining từng tồn tại trong specification nhưng khó triển khai rộng vì response ordering và head-of-line behavior. Browsers vì thế thường mở nhiều TCP connections tới cùng origin để tăng parallelism.

Nhiều connections giúp tránh một số blocking giữa requests nhưng phải trả thêm handshake, congestion state, socket memory và server resource. Đây là ví dụ điển hình: khi một abstraction không multiplex tốt, system thường tạo parallelism bằng cách nhân số resource bên dưới.

## 2. HTTP/2: binary framing và nhiều stream trên một TCP connection

HTTP/2 giữ HTTP methods/status/caching semantics nhưng đổi wire representation thành binary frames. Mỗi request/response thuộc một **luồng (stream / 스트림)** có stream ID riêng; frames của nhiều streams có thể interleave trên cùng connection.

Headers được compress bằng HPACK để giảm repeated metadata. Application không còn phải chờ response của request A hoàn tất mới gửi/nhận frames của request B theo kiểu tuần tự đơn giản.

Điều này giảm **application-level head-of-line blocking**, nhưng tất cả frames cuối cùng vẫn được đặt vào một TCP byte stream duy nhất.

## 3. Vì sao HTTP/2 vẫn có transport head-of-line blocking?

TCP hứa giao một byte stream **reliable và in-order**. Nếu segment chứa bytes ở giữa stream bị mất, TCP có thể đã nhận bytes nằm sau gap nhưng chưa được phép giao chúng lên application trước khi phần thiếu được retransmit.

Giả sử HTTP/2 stream A và B có frames interleave:

```text
TCP bytes:
A1 | B1 | A2 | B2
```

Nếu segment chứa `A2` bị mất nhưng segment chứa `B2` tới nơi, TCP vẫn phải lấp gap byte-stream trước khi giao phần sau. Từ góc nhìn HTTP/2, stream B không liên quan logic tới A nhưng vẫn bị transport ordering chặn.

Điểm cần giữ:

```text
HTTP/2 multiplexing
≠
independent transport delivery
```

## 4. QUIC dùng UDP làm substrate nhưng tự cung cấp transport semantics

**QUIC** chạy trên UDP datagrams để có không gian triển khai transport logic ở user space, nhưng QUIC không phải “UDP gửi gì mất nấy”. Nó tự cung cấp reliable streams, loss detection/recovery, flow control, congestion control, cryptographic handshake và connection management.

HTTP/3 ánh xạ HTTP semantics lên QUIC. Mỗi QUIC stream có không gian byte/offset riêng nên loss của dữ liệu stream A không buộc transport giữ lại dữ liệu đã hoàn chỉnh của stream B chỉ để bảo toàn một global byte stream như TCP.

Điều này giảm connection-wide head-of-line blocking do transport ordering, nhưng packet loss không miễn phí: lost bytes vẫn phải retransmit, congestion controller vẫn có thể giảm sending rate và nhiều streams vẫn chia sẻ cùng network path/capacity.

## 5. Packet number và stream offset là hai loại ordering khác nhau

Một mental model hữu ích là tách **packet number** khỏi **stream offset**.

QUIC packets có packet numbers phục vụ acknowledgement/loss recovery. Dữ liệu application bên trong lại thuộc các streams với offsets riêng. Một stream cần reconstruct bytes theo thứ tự của chính stream đó, nhưng stream khác không cần chờ một gap không liên quan.

Đây là cơ chế bên trong giải thích tại sao HTTP/3 cải thiện behavior dưới loss so với HTTP/2/TCP mà không từ bỏ reliability.

Câu hỏi đúng là: **ordering invariant nằm ở connection-wide byte stream hay từng logical stream?**

## 6. ACK và loss recovery không đồng nghĩa retransmit packet y hệt

Transport reliable cần biết dữ liệu nào peer đã nhận và dữ liệu nào cần gửi lại. QUIC có acknowledgements cho packet ranges và loss-detection logic dựa trên packet ordering/timing. Khi loss được suy ra, implementation có thể retransmit **information/frames cần thiết** trong packet mới thay vì tái phát nguyên datagram cũ với cùng packet identity.

Điều này quan trọng cho debugging: packet numbers phản ánh transmission attempts, còn stream offsets phản ánh logical data. Một request chậm có thể do cùng stream data phải được gửi lại dù packet identity đã thay đổi.

## 7. Congestion control vẫn là shared-resource invariant

QUIC tránh một loại head-of-line blocking nhưng không thể bỏ **điều khiển tắc nghẽn (congestion control / 혼잡 제어)**. Nhiều connections cùng chia sẻ bottleneck link; sender phải điều chỉnh amount of in-flight data theo evidence từ ACK/loss/ECN và algorithm đang dùng.

Các streams trên một connection thường vẫn chịu chung path congestion state. Nếu packet loss làm congestion window giảm, throughput của nhiều streams có thể cùng giảm dù delivery ordering độc lập hơn.

Vì vậy câu “HTTP/3 packet loss chỉ ảnh hưởng một stream” là quá mạnh. Chính xác hơn: loss không bắt transport block delivery của stream khác chỉ vì một global byte gap, nhưng **capacity reaction ở connection/path level vẫn có thể ảnh hưởng tất cả**.

## 8. Flow control khác congestion control

**Điều khiển luồng (flow control / 흐름 제어)** bảo vệ receiver khỏi sender gửi nhanh hơn khả năng nhận/buffer. **Congestion control** bảo vệ network path khỏi lượng in-flight traffic quá lớn.

QUIC có thể có connection-level và stream-level flow-control limits. Một stream hết receive credit có thể dừng dù network không congested. Ngược lại, receive buffers còn nhiều nhưng congestion window nhỏ vẫn giới hạn transmission.

Khi debug throughput thấp, cần phân biệt receiver flow-control limited, congestion-window/path limited, application không tạo dữ liệu đủ nhanh, packet loss/retransmission hay CPU/crypto/runtime bottleneck.

## 9. TLS integration làm security trở thành một phần của transport state machine

QUIC tích hợp TLS 1.3 chặt với connection establishment. Transport parameters và cryptographic state tiến triển cùng handshake, giúp common path giảm round trips so với việc dựng TCP rồi mới dựng TLS như hai state machine nối tiếp.

Tuy nhiên “ít round trip hơn” không đồng nghĩa zero cost. Certificate validation, key derivation, server processing, packet loss và path RTT vẫn tồn tại.

Handshake failure cũng không nhất thiết là “QUIC bug”. Nguyên nhân có thể nằm ở certificate, clock, trust store, network policy, UDP filtering hoặc version negotiation.

## 10. 0-RTT đổi latency lấy replay assumption

Repeat client có thể gửi **0-RTT early data** khi có session state phù hợp. Lợi ích là application data có thể đi trước khi full handshake mới hoàn tất.

Đổi lại, early data có replay risk theo threat model của protocol. Application chỉ nên cho 0-RTT thực hiện operation có semantics chịu được replay hoặc có idempotency/deduplication bảo vệ phù hợp.

Một payment `POST` không tự trở nên an toàn chỉ vì transport cho phép gửi sớm. Security/performance optimization không được làm yếu business invariant.

## 11. Connection ID tách logical connection khỏi 4-tuple

TCP connection thường gắn chặt với source/destination IP+port pair. QUIC dùng **Connection ID** để peer có thể nhận diện logical connection ngay cả khi network address thay đổi trong một số tình huống như NAT rebinding hoặc client chuyển Wi-Fi sang cellular.

Migration không có nghĩa “chấp nhận packet từ bất kỳ địa chỉ nào”. Path mới cần được validation để tránh spoofing/amplification và implementation vẫn phải quản lý congestion/path state đúng.

Transport connection continuity cũng không thay application authorization/session semantics. Một valid connection không tự chứng minh request được phép truy cập resource.

## 12. Address validation và amplification protection

UDP cho phép sender giả mạo source address dễ hơn connection-oriented handshake intuition. Server không nên gửi lượng dữ liệu lớn tới địa chỉ chưa được chứng minh reachable, nếu không attacker có thể biến server thành reflection/amplification source.

QUIC vì vậy có cơ chế address validation và giới hạn amount of data server được gửi trước khi client address được validate.

Đây là ví dụ security invariant ảnh hưởng trực tiếp performance path: trước khi trust reachability, server phải hạn chế amplification dù nó có response lớn sẵn sàng.

## 13. Path MTU: transport không thể gửi datagram lớn tùy ý

Mỗi network path có giới hạn kích thước packet có thể đi qua mà không cần fragmentation, thường được reasoning bằng **Path MTU (Maximum Transmission Unit / 경로 MTU)**.

QUIC chạy trên UDP nên implementation phải chọn datagram size phù hợp và thích nghi với path. Datagram quá lớn có thể bị drop trên một hop. Nếu ICMP/PTB signaling bị firewall chặn hoặc path behavior bất thường, system có thể gặp **PMTU black hole**: small packets/handshake có vẻ hoạt động nhưng large datagrams liên tục biến mất.

Symptom thường khó chịu: connection thiết lập được, request nhỏ chạy, nhưng transfer lớn stall hoặc retransmit nhiều.

Đây là lý do packet-level diagnosis phải nhìn size distribution, ICMP/network policy và loss pattern thay vì chỉ “ping được nên network ổn”.

## 14. UDP blocking và fallback là production reality

Một số enterprise network, firewall hoặc middlebox vẫn chặn/giới hạn UDP. Browser/client có thể thử HTTP/3 rồi fallback sang HTTP/2/TCP.

Nếu chỉ nhìn server-side HTTP/3 metrics, ta có thể bỏ qua population đang fallback. Production evidence nên phân biệt attempted HTTP/3, successful HTTP/3, fallback HTTP/2, handshake/version error và UDP path failure.

Protocol mới phải coexist với deployment reality; compatibility path là một phần của system design.

## 15. Connection coalescing và origin boundary

HTTP/2/3 có thể reuse connection cho nhiều origins trong điều kiện certificate/DNS/address và client policy cho phép. Điều này tiết kiệm handshake/socket state, nhưng **transport reuse không hợp nhất security origins**.

Browser vẫn phải duy trì origin isolation, credential/cookie rules và certificate identity. “Cùng connection” không có nghĩa hai applications được phép đọc state của nhau.

## 16. Header compression có state và failure boundary riêng

HTTP/2 dùng HPACK; HTTP/3 dùng QPACK để thích nghi với transport có streams độc lập. Header compression giảm repeated bytes nhưng tạo dynamic-table state giữa peers.

Stateful compression phải tránh biến packet/stream reordering thành global blocking quá mức. Đây là lý do HTTP/3 không chỉ “đổi TCP thành QUIC”; một số mechanism phía HTTP cũng phải thiết kế lại để phù hợp delivery model mới.

## 17. Worked example: packet loss trên một page nhiều requests

Giả sử browser tải HTML, CSS, JavaScript và nhiều API calls qua một connection. Với HTTP/2/TCP, một lost TCP segment có thể tạo byte gap; frames của streams khác đã tới sau gap vẫn chưa được TCP giao lên HTTP/2.

Với HTTP/3/QUIC, lost data của stream JavaScript vẫn phải recover, nhưng completed data của API stream khác có thể được deliver nếu stream của nó không thiếu bytes. Tuy nhiên loss evidence có thể khiến congestion controller giảm sending rate cho connection, nên mọi stream vẫn có thể chậm hơn một phần.

Mental model đúng là:

```text
independent stream ordering
+
shared path capacity
```

chứ không phải “loss chỉ ảnh hưởng đúng một request”.

## 18. Observability khó hơn vì transport metadata được mã hóa nhiều hơn

QUIC mã hóa nhiều transport metadata hơn TCP, giúp privacy và giảm protocol ossification do middlebox phụ thuộc vào fields nội bộ. Đổi lại packet capture ngoài endpoint không còn nhìn được mọi state như TCP truyền thống.

Diagnosis cần tăng endpoint telemetry: handshake phase, negotiated version, RTT estimate, loss/recovery counters, congestion state, flow-control blocked time, stream latency và fallback reason.

Privacy/evolvability và operator visibility là trade-off thật, không phải implementation accident.

## 19. Packet-level diagnosis: đọc symptom theo mechanism

Nếu time-to-first-byte tăng, trước tiên tách DNS, connection setup, TLS/QUIC handshake, server processing và first response bytes. Nếu throughput transfer lớn thấp, kiểm tra RTT, loss, congestion window/pacing, flow-control blocked state và path MTU. Nếu chỉ một subset network fail, so sánh UDP reachability/fallback, NAT/firewall behavior và MTU.

Evidence hữu ích gồm:

```text
protocol/version negotiated
connection reuse vs cold setup
handshake duration/failure reason
smoothed RTT và RTT variance
loss/retransmitted data
congestion-limited time
flow-control-limited time
stream-level latency
UDP/HTTP3 fallback rate
packet/datagram sizes và PMTU symptoms
```

Packet capture chỉ là một evidence source. Application trace giải thích request semantics; endpoint transport metrics giải thích state mà encrypted wire capture có thể không thấy.

## 20. Version evolution và deployment

HTTP/2 và HTTP/3 là protocol standards, nhưng production behavior phụ thuộc client/server implementation, congestion algorithm, TLS library, kernel/network path và intermediaries. Không nên gắn một optimization với một browser/server version rồi coi nó là universal law.

Khi rollout HTTP/3, nên so theo cohorts và network conditions: RTT thấp/cao, loss thấp/cao, mobile/Wi-Fi, geographic region, cold/reused connections. Average toàn fleet có thể che nhóm thật sự được lợi hoặc bị regression.

## Common Misconceptions

**“HTTP/2 bỏ TCP.”** Không; HTTP/2 thường chạy trên TCP + TLS.

**“QUIC là UDP nên không reliable.”** QUIC dùng UDP datagrams làm substrate nhưng tự cung cấp reliable streams, loss recovery, flow control và congestion control.

**“HTTP/3 loại bỏ mọi head-of-line blocking.”** Nó giảm connection-wide HOL do TCP byte-stream ordering; một stream vẫn cần thứ tự bytes của chính nó và path congestion vẫn là shared constraint.

**“QUIC migration nghĩa session/auth tự survive mọi network change.”** Transport có thể survive path change; business/session authorization là contract ở tầng khác.

**“Ping được nghĩa MTU/path ổn.”** Small packets có thể đi trong khi larger UDP datagrams bị black-hole.

**“HTTP/3 luôn nhanh hơn.”** Lợi ích phụ thuộc RTT, loss, connection reuse, workload, implementation và network policy.

## Mental Model

> HTTP evolution giữ application semantics nhưng thay cách **nhiều streams chia sẻ một transport connection**. HTTP/2 multiplex ở application layer nhưng vẫn chịu một TCP byte stream; HTTP/3 dùng QUIC để cho từng stream có ordering riêng, trong khi congestion/path capacity vẫn được chia sẻ. Khi debug, hãy tách handshake, stream ordering, flow control, congestion control và path MTU thay vì gọi chung là “network chậm”.

## Kết nối

Đọc [TCP/UDP và congestion](./02_transport_tcp_udp_and_congestion.md), [DNS/HTTP/TLS](./03_dns_http_tls_and_web_request.md), [socket/NAT/firewall/VPN](./06_sockets_ipv6_nat_firewalls_and_vpn.md), [web request end-to-end](../90_connections/01_browser_to_database_request.md) và [request path advanced](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).