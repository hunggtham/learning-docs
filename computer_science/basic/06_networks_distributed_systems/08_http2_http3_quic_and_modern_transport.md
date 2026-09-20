# HTTP/2, HTTP/3, QUIC và modern transport

HTTP/1.1 over TCP/TLS vẫn là nền lịch sử quan trọng, nhưng web hiện đại phát triển để giảm connection overhead, multiplex requests tốt hơn và cải thiện behavior khi packet loss xảy ra. Muốn hiểu HTTP/2/3 cần tách application multiplexing khỏi transport ordering.

## HTTP/1.1 và giới hạn connection-level

HTTP/1.1 hỗ trợ persistent connections, nhưng response ordering/pipelining historically khó dùng rộng do head-of-line concerns và ecosystem behavior. Browsers thường mở nhiều TCP connections để tăng parallelism.

Nhiều connections tăng handshake, congestion state và server resource overhead.

## HTTP/2: binary framing và streams

HTTP/2 giữ HTTP semantics nhưng đổi wire framing thành binary và multiplex nhiều streams trên một TCP connection.

Headers được compress bằng HPACK; requests/responses chia frames và interleave theo stream IDs.

Application-level head-of-line giữa requests được giảm, nhưng tất cả streams vẫn chia sẻ một TCP byte stream.

## TCP head-of-line vẫn tồn tại

Nếu một TCP segment mất, TCP phải deliver byte stream in-order. Bytes của các HTTP/2 streams khác nằm sau gap cũng không được giao lên application dù packets của chúng đã tới.

Đây là transport-level head-of-line blocking.

## QUIC: transport trên UDP với streams riêng

QUIC chạy trên UDP nhưng tự triển khai reliable transport, congestion control, stream multiplexing và cryptographic handshake. HTTP/3 chạy trên QUIC.

Một packet loss ảnh hưởng bytes của stream liên quan thay vì chặn delivery mọi streams như single ordered TCP stream.

QUIC connection IDs giúp connection survive một số network path/address changes tốt hơn 4-tuple-only identity.

## TLS integration và handshake latency

QUIC tích hợp TLS 1.3 handshake chặt với transport setup, giảm round trips trong common cases. 0-RTT data có thể giảm latency cho repeat connections nhưng có replay risk, nên chỉ safe cho operations có semantics phù hợp.

Đây là ví dụ security/performance trade-off phải được thiết kế xuyên protocol layers.

## HTTP semantics không đổi hoàn toàn theo version

Methods, status codes, caching concepts và headers semantics vẫn thuộc HTTP family. HTTP/2/3 chủ yếu thay framing/transport behavior.

Application không nên infer business idempotency chỉ từ transport retry. `GET` thường safe/idempotent theo HTTP semantics; `POST` không mặc định như vậy.

## Congestion control và pacing

QUIC có thể triển khai congestion algorithms trong user space nhanh hơn kernel TCP upgrade cycles. Nhưng fairness và network stability vẫn là shared-resource problem.

Pacing phân bố packets theo thời gian thay vì burst, giúp queue behavior tốt hơn.

## Connection coalescing và origin boundaries

HTTP/2/3 có thể reuse connection cho multiple origins trong conditions về DNS/certificate/address, nhưng browser security rules vẫn phải giữ origin isolation semantics.

Transport reuse không đồng nghĩa authorization giữa applications.

## Observability khó hơn khi encryption sâu hơn

QUIC encrypts nhiều transport metadata hơn TCP, cải thiện privacy và ossification resistance nhưng làm middlebox diagnostics truyền thống khó hơn.

Protocol design trade-off giữa evolvability/privacy và network operator visibility.

## Common Misconceptions

**“HTTP/2 bỏ TCP.”** Không; HTTP/2 thường chạy trên TCP + TLS.

**“QUIC là UDP không reliable.”** QUIC dùng UDP datagrams làm substrate nhưng tự cung cấp reliable streams và congestion control.

**“HTTP/3 luôn nhanh hơn.”** Lợi ích phụ thuộc RTT, loss, connection reuse, server/client implementation và network policy.

## Mental Model

> HTTP evolution tách application semantics khỏi wire/transport improvements. Hãy hỏi head-of-line nằm ở layer nào, connection state nằm ở đâu và handshake cần bao nhiêu round trips.

## Kết nối

Đọc [TCP/UDP](./02_transport_tcp_udp_and_congestion.md), [DNS/HTTP/TLS](./03_dns_http_tls_and_web_request.md), [socket/NAT/VPN](./06_sockets_ipv6_nat_firewalls_and_vpn.md) và [web request end-to-end](../90_connections/01_browser_to_database_request.md).