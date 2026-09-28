# Sockets, IPv6, NAT, firewalls và VPN

> **Mạch đọc:** Đọc **Sockets, IPv6, NAT, firewalls và VPN** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Socket là giao diện (interface / 인터페이스) giữa ứng dụng (application / 애플리케이션) và mạng (network / 네트워크) ngăn xếp (stack / 스택)** sang **cổng (port / 포트) không phải tiến trình (process / 프로세스) ID**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


IP/TCP mô tả mạng (network / 네트워크) protocols, nhưng applications cần một programming lớp trừu tượng (abstraction / 추상화) để dùng chúng. Socket (소켓) là endpoint lớp trừu tượng (abstraction / 추상화) nối tiến trình (process / 프로세스) với vận chuyển (transport / 전송)/mạng (network / 네트워크) ngăn xếp (stack / 스택). Từ đó, các mechanisms như NAT, firewall và VPN thay đổi đường đi hoặc trust ranh giới (boundary / 경계) của packets.

## Socket là giao diện (interface / 인터페이스) giữa ứng dụng (application / 애플리케이션) và mạng (network / 네트워크) ngăn xếp (stack / 스택)

Một TCP máy chủ (server / 서버) thường tạo socket, `bind` cục bộ (local / 로컬) address/cổng (port / 포트), `listen`, rồi `accept` connections. máy khách (client / 클라이언트) tạo socket và `connect` remote endpoint.

Sau liên kết (connection / 연결), ứng dụng (application / 애플리케이션) nhìn thấy byte stream; TCP segmentation/retransmission nằm bên dưới. `send()` một lần không tương ứng một mạng (network / 네트워크) packet và receiver `recv()` không giữ message boundaries.

Vì vậy ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜) phải tự framing: length-prefix, delimiter hoặc structured giao thức (protocol / 프로토콜).


> **Chuyển mạch:** Từ **Socket là giao diện (interface / 인터페이스) giữa ứng dụng (application / 애플리케이션) và mạng (network / 네트워크) ngăn xếp (stack / 스택)**, ta sang **cổng (port / 포트) không phải tiến trình (process / 프로세스) ID** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cổng (port / 포트) không phải tiến trình (process / 프로세스) ID

Cổng (port / 포트) number thuộc vận chuyển (transport / 전송) endpoint không gian tên (namespace / 네임스페이스) trên host/address. Một tiến trình (process / 프로세스) có thể mở nhiều ports; nhiều processes có thể phối hợp reuse cổng (port / 포트) tùy OS; một dịch vụ (service / 서비스) có thể có nhiều connections cùng cục bộ (local / 로컬) cổng (port / 포트) nhưng khác remote tuple.

TCP liên kết (connection / 연결) thường được định danh bởi 4-tuple nguồn (source / 소스) IP/cổng (port / 포트) + destination IP/cổng (port / 포트).


> **Chuyển mạch:** Từ **cổng (port / 포트) không phải tiến trình (process / 프로세스) ID**, ta sang **IPv6 không chỉ là “nhiều địa chỉ hơn”** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## IPv6 không chỉ là “nhiều địa chỉ hơn”

IPv6 dùng 128-bit addresses, đơn giản hóa một số header fields, tích hợp Neighbor Discovery thay ARP-style IPv4 hành vi (behavior / 동작) và loại broadcast theo kiểu IPv4.

Address types gồm toàn cục (global / 전역) unicast, link-local, multicast; notation dùng hex và `::` compression.

IPv6 adoption không tự loại NAT ngay trong mọi triển khai (deployment / 배포), nhưng thiết kế end-to-end addressing ít phụ thuộc address scarcity hơn IPv4.


> **Chuyển mạch:** Từ **IPv6 không chỉ là “nhiều địa chỉ hơn”**, ta sang **NAT: rewrite addressing trạng thái (state / 상태)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## NAT: rewrite addressing trạng thái (state / 상태)

Mạng (network / 네트워크) Address Translation sửa nguồn (source / 소스)/destination addresses/ports tại ranh giới (boundary / 경계). Home router thường dùng nguồn (source / 소스) NAT/PAT để nhiều private hosts chia sẻ một công khai (public / 공개) IPv4 address.

NAT tạo trạng thái (state / 상태) ánh xạ (mapping / 매핑) outbound tuple → công khai (public / 공개) tuple. Inbound unsolicited traffic khó hơn vì không có ánh xạ (mapping / 매핑), nên cần cổng (port / 포트) forwarding hoặc traversal techniques.

NAT không phải firewall về bản chất, dù bên tiêu thụ (consumer / 소비자) routers thường kết hợp hai chức năng.


> **Chuyển mạch:** Từ **NAT: rewrite addressing trạng thái (state / 상태)**, ta sang **Firewall: chính sách (policy / 정책) enforcement trên traffic** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Firewall: chính sách (policy / 정책) enforcement trên traffic

Firewall quyết định allow/drop/reject theo rules. Stateless firewall xét từng packet; stateful firewall theo dõi liên kết (connection / 연결) trạng thái (state / 상태) để cho phản hồi (response / 응답) traffic tương ứng.

Layer-7 firewall/WAF có thể parse ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜), nhưng deeper inspection tăng chi phí (cost / 비용) và parser độ phức tạp (complexity / 복잡도).

Bảo mật (security / 보안) không nên dựa riêng “nằm sau NAT”; tường minh (explicit / 명시적) chính sách (policy / 정책) và authentication vẫn cần thiết.


> **Chuyển mạch:** Từ **Firewall: chính sách (policy / 정책) enforcement trên traffic**, ta sang **VPN: tạo secure overlay** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## VPN: tạo secure overlay

Virtual Private mạng (network / 네트워크) tạo tunnel lô-gic (logic / 논리) qua mạng (network / 네트워크) khác. Packets được encapsulate, thường encrypted/authenticated, giữa endpoints hoặc gateways.

VPN có thể là remote-access hoặc site-to-site. Split tunneling gửi chỉ một số routes qua VPN; full tunnel gửi default traffic qua tunnel.

VPN bảo vệ traffic trên segment/tunnel đường dẫn (path / 경로) nhưng không biến endpoint compromised thành trustworthy.


> **Chuyển mạch:** Từ **VPN: tạo secure overlay**, ta sang **MTU và fragmentation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## MTU và fragmentation

Link có Maximum Transmission đơn vị (unit / 단위) (MTU). Packet lớn hơn đường dẫn (path / 경로) hỗ trợ (support / 지원) có thể cần fragmentation hoặc đường dẫn (path / 경로) MTU Discovery.

Tunnel thêm headers làm effective payload MTU nhỏ hơn. Misconfigured MTU có thể gây symptom “một số site/yêu cầu (request / 요청) treo” rất khó gỡ lỗi (debug / 디버그).


> **Chuyển mạch:** Từ **MTU và fragmentation**, ta sang **Socket buffers và backpressure** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Socket buffers và backpressure

Kernel có send/receive buffers. `send()` thành công có thể chỉ nghĩa bytes được bản sao (copy / 복사) vào send buffer, chưa tới peer.

Nếu peer/mạng (network / 네트워크) chậm, buffer đầy rồi writer khối (block / 블록)/return backpressure. Application-level hàng đợi (queue / 큐) không được grow vô hạn chỉ vì socket API tạm nhận được dữ liệu (data / 데이터).


> **Chuyển mạch:** Từ **Socket buffers và backpressure**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Một send = một recv.”** Sai với TCP byte stream.

**“NAT là bảo mật (security / 보안) cơ chế (mechanism / 메커니즘).”** Nó có side tác động (effect / 효과) chặn unsolicited inbound mappings nhưng không thay thế firewall/authentication.

**“VPN bảo mật mọi thứ.”** Nó bảo vệ tunnel traffic; endpoint malware, weak credentials và ứng dụng (application / 애플리케이션) vulnerabilities vẫn tồn tại.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Socket là cục bộ (local / 로컬) handle tới giao thức (protocol / 프로토콜) trạng thái (state / 상태); NAT/firewall/VPN là transformations/policies ở mạng (network / 네트워크) boundaries. gỡ lỗi (debug / 디버그) mạng (network / 네트워크) cần biết bytes đang ở tiến trình (process / 프로세스) buffer, kernel socket, packet đường dẫn (path / 경로) hay tunnel tầng (layer / 계층) nào.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [TCP/UDP](./02_transport_tcp_udp_and_congestion.md), [routing](./07_routing_protocols_and_the_internet.md), [OS async I/O](../03_operating_systems/07_boot_device_drivers_and_async_io.md) và [web security](../07_security_reliability/06_web_application_security.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 network layers packets and encapsulation](./00_network_layers_packets_and_encapsulation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
