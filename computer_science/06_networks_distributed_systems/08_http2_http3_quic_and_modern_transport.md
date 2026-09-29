# HTTP/2, HTTP/3, QUIC và hiện đại (modern / 현대적) vận chuyển (transport / 전송)

> **Mạch đọc:** Đặt **HTTP/2, HTTP/3, QUIC và hiện đại (modern / 현대적) vận chuyển (transport / 전송)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **HTTP/1.1 và giới hạn connection-level** sang **HTTP/2: nhị phân (binary / 이진) framing và streams**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


HTTP/1.1 over TCP/TLS vẫn là nền lịch sử quan trọng, nhưng web hiện đại phát triển để giảm liên kết (connection / 연결) overhead, multiplex requests tốt hơn và cải thiện hành vi (behavior / 동작) khi packet mất mát (loss / 손실) xảy ra. Muốn hiểu HTTP/2/3 cần tách ứng dụng (application / 애플리케이션) multiplexing khỏi vận chuyển (transport / 전송) thứ tự (ordering / 순서).

## HTTP/1.1 và giới hạn connection-level

HTTP/1.1 hỗ trợ persistent connections, nhưng phản hồi (response / 응답) thứ tự (ordering / 순서)/pipelining historically khó dùng rộng do head-of-line concerns và ecosystem hành vi (behavior / 동작). Browsers thường mở nhiều TCP connections để tăng parallelism.

Nhiều connections tăng handshake, congestion trạng thái (state / 상태) và máy chủ (server / 서버) tài nguyên (resource / 자원) overhead.


> **Chuyển mạch:** Từ **HTTP/1.1 và giới hạn connection-level**, ta sang **HTTP/2: nhị phân (binary / 이진) framing và streams** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## HTTP/2: nhị phân (binary / 이진) framing và streams

HTTP/2 giữ HTTP ngữ nghĩa (semantics / 의미론) nhưng đổi wire framing thành nhị phân (binary / 이진) và multiplex nhiều streams trên một TCP liên kết (connection / 연결).

Headers được compress bằng HPACK; requests/responses chia frames và interleave theo stream IDs.

Application-level head-of-line giữa requests được giảm, nhưng tất cả streams vẫn chia sẻ một TCP byte stream.


> **Chuyển mạch:** Từ **HTTP/2: nhị phân (binary / 이진) framing và streams**, ta sang **TCP head-of-line vẫn tồn tại** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## TCP head-of-line vẫn tồn tại

Nếu một TCP segment mất, TCP phải deliver byte stream in-order. Bytes của các HTTP/2 streams khác nằm sau gap cũng không được giao lên ứng dụng (application / 애플리케이션) dù packets của chúng đã tới.

Đây là transport-level head-of-line blocking.


> **Chuyển mạch:** Từ **TCP head-of-line vẫn tồn tại**, ta sang **QUIC: vận chuyển (transport / 전송) trên UDP với streams riêng** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## QUIC: vận chuyển (transport / 전송) trên UDP với streams riêng

QUIC chạy trên UDP nhưng tự triển khai reliable vận chuyển (transport / 전송), congestion điều khiển (control / 제어), stream multiplexing và cryptographic handshake. HTTP/3 chạy trên QUIC.

Một packet mất mát (loss / 손실) ảnh hưởng bytes của stream liên quan thay vì chặn delivery mọi streams như single ordered TCP stream.

QUIC liên kết (connection / 연결) IDs giúp liên kết (connection / 연결) survive một số mạng (network / 네트워크) đường dẫn (path / 경로)/address changes tốt hơn 4-tuple-only định danh (identity / 식별자).


> **Chuyển mạch:** Từ **QUIC: vận chuyển (transport / 전송) trên UDP với streams riêng**, ta sang **TLS tích hợp (integration / 통합) và handshake độ trễ (latency / 지연 시간)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## TLS tích hợp (integration / 통합) và handshake độ trễ (latency / 지연 시간)

QUIC tích hợp TLS 1.3 handshake chặt với vận chuyển (transport / 전송) setup, giảm round trips trong dùng chung (common / 공통) cases. 0-RTT dữ liệu (data / 데이터) có thể giảm độ trễ (latency / 지연 시간) cho repeat connections nhưng có replay rủi ro (risk / 위험), nên chỉ safe cho operations có ngữ nghĩa (semantics / 의미론) phù hợp.

Đây là ví dụ bảo mật (security / 보안)/hiệu năng (performance / 성능) sự đánh đổi (trade-off / 트레이드오프) phải được thiết kế xuyên giao thức (protocol / 프로토콜) layers.


> **Chuyển mạch:** Từ **TLS tích hợp (integration / 통합) và handshake độ trễ (latency / 지연 시간)**, ta sang **HTTP ngữ nghĩa (semantics / 의미론) không đổi hoàn toàn theo phiên bản (version / 버전)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## HTTP ngữ nghĩa (semantics / 의미론) không đổi hoàn toàn theo phiên bản (version / 버전)

Methods, status codes, caching concepts và headers ngữ nghĩa (semantics / 의미론) vẫn thuộc HTTP family. HTTP/2/3 chủ yếu thay framing/vận chuyển (transport / 전송) hành vi (behavior / 동작).

Ứng dụng (application / 애플리케이션) không nên infer nghiệp vụ (business / 비즈니스) idempotency chỉ từ vận chuyển (transport / 전송) thử lại (retry / 재시도). `GET` thường safe/idempotent theo HTTP ngữ nghĩa (semantics / 의미론); `POST` không mặc định như vậy.


> **Chuyển mạch:** Từ **HTTP ngữ nghĩa (semantics / 의미론) không đổi hoàn toàn theo phiên bản (version / 버전)**, ta sang **Congestion điều khiển (control / 제어) và pacing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Congestion điều khiển (control / 제어) và pacing

QUIC có thể triển khai congestion algorithms trong người dùng (user / 사용자) không gian (space / 공간) nhanh hơn kernel TCP upgrade cycles. Nhưng fairness và mạng (network / 네트워크) stability vẫn là shared-resource bài toán (problem / 문제).

Pacing phân bố packets theo thời gian thay vì burst, giúp hàng đợi (queue / 큐) hành vi (behavior / 동작) tốt hơn.


> **Chuyển mạch:** Từ **Congestion điều khiển (control / 제어) và pacing**, ta sang **liên kết (connection / 연결) coalescing và origin boundaries** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết (connection / 연결) coalescing và origin boundaries

HTTP/2/3 có thể reuse liên kết (connection / 연결) cho multiple origins trong conditions về DNS/certificate/address, nhưng trình duyệt (browser / 브라우저) bảo mật (security / 보안) rules vẫn phải giữ origin isolation ngữ nghĩa (semantics / 의미론).

Vận chuyển (transport / 전송) reuse không đồng nghĩa authorization giữa applications.


> **Chuyển mạch:** Từ **liên kết (connection / 연결) coalescing và origin boundaries**, ta sang **khả năng quan sát (observability / 관측 가능성) khó hơn khi encryption sâu hơn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Khả năng quan sát (observability / 관측 가능성) khó hơn khi encryption sâu hơn

QUIC encrypts nhiều vận chuyển (transport / 전송) siêu dữ liệu (metadata / 메타데이터) hơn TCP, cải thiện privacy và ossification resistance nhưng làm middlebox diagnostics truyền thống khó hơn.

Giao thức (protocol / 프로토콜) thiết kế (design / 설계) sự đánh đổi (trade-off / 트레이드오프) giữa evolvability/privacy và mạng (network / 네트워크) operator visibility.


> **Chuyển mạch:** Từ **khả năng quan sát (observability / 관측 가능성) khó hơn khi encryption sâu hơn**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“HTTP/2 bỏ TCP.”** Không; HTTP/2 thường chạy trên TCP + TLS.

**“QUIC là UDP không reliable.”** QUIC dùng UDP datagrams làm substrate nhưng tự cung cấp reliable streams và congestion điều khiển (control / 제어).

**“HTTP/3 luôn nhanh hơn.”** Lợi ích phụ thuộc RTT, mất mát (loss / 손실), liên kết (connection / 연결) reuse, máy chủ (server / 서버)/máy khách (client / 클라이언트) hiện thực (implementation / 구현) và chính sách mạng (network policy / 네트워크 정책).


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> HTTP evolution tách ứng dụng (application / 애플리케이션) ngữ nghĩa (semantics / 의미론) khỏi wire/vận chuyển (transport / 전송) improvements. Hãy hỏi head-of-line nằm ở tầng (layer / 계층) nào, liên kết (connection / 연결) trạng thái (state / 상태) nằm ở đâu và handshake cần bao nhiêu round trips.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [TCP/UDP](./02_transport_tcp_udp_and_congestion.md), [DNS/HTTP/TLS](./03_dns_http_tls_and_web_request.md), [socket/NAT/VPN](./06_sockets_ipv6_nat_firewalls_and_vpn.md) và [web request end-to-end](../90_connections/01_browser_to_database_request.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 network layers packets and encapsulation](./00_network_layers_packets_and_encapsulation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
