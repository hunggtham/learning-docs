# Sockets, IPv6, NAT, firewalls và VPN

IP/TCP mô tả network protocols, nhưng applications cần một programming abstraction để dùng chúng. Socket (소켓) là endpoint abstraction nối process với transport/network stack. Từ đó, các mechanisms như NAT, firewall và VPN thay đổi đường đi hoặc trust boundary của packets.

## Socket là interface giữa application và network stack

Một TCP server thường tạo socket, `bind` local address/port, `listen`, rồi `accept` connections. Client tạo socket và `connect` remote endpoint.

Sau connection, application nhìn thấy byte stream; TCP segmentation/retransmission nằm bên dưới. `send()` một lần không tương ứng một network packet và receiver `recv()` không giữ message boundaries.

Vì vậy application protocol phải tự framing: length-prefix, delimiter hoặc structured protocol.

## Port không phải process ID

Port number thuộc transport endpoint namespace trên host/address. Một process có thể mở nhiều ports; nhiều processes có thể phối hợp reuse port tùy OS; một service có thể có nhiều connections cùng local port nhưng khác remote tuple.

TCP connection thường được định danh bởi 4-tuple source IP/port + destination IP/port.

## IPv6 không chỉ là “nhiều địa chỉ hơn”

IPv6 dùng 128-bit addresses, đơn giản hóa một số header fields, tích hợp Neighbor Discovery thay ARP-style IPv4 behavior và loại broadcast theo kiểu IPv4.

Address types gồm global unicast, link-local, multicast; notation dùng hex và `::` compression.

IPv6 adoption không tự loại NAT ngay trong mọi deployment, nhưng thiết kế end-to-end addressing ít phụ thuộc address scarcity hơn IPv4.

## NAT: rewrite addressing state

Network Address Translation sửa source/destination addresses/ports tại boundary. Home router thường dùng source NAT/PAT để nhiều private hosts chia sẻ một public IPv4 address.

NAT tạo state mapping outbound tuple → public tuple. Inbound unsolicited traffic khó hơn vì không có mapping, nên cần port forwarding hoặc traversal techniques.

NAT không phải firewall về bản chất, dù consumer routers thường kết hợp hai chức năng.

## Firewall: policy enforcement trên traffic

Firewall quyết định allow/drop/reject theo rules. Stateless firewall xét từng packet; stateful firewall theo dõi connection state để cho response traffic tương ứng.

Layer-7 firewall/WAF có thể parse application protocol, nhưng deeper inspection tăng cost và parser complexity.

Security không nên dựa riêng “nằm sau NAT”; explicit policy và authentication vẫn cần thiết.

## VPN: tạo secure overlay

Virtual Private Network tạo tunnel logic qua network khác. Packets được encapsulate, thường encrypted/authenticated, giữa endpoints hoặc gateways.

VPN có thể là remote-access hoặc site-to-site. Split tunneling gửi chỉ một số routes qua VPN; full tunnel gửi default traffic qua tunnel.

VPN bảo vệ traffic trên segment/tunnel path nhưng không biến endpoint compromised thành trustworthy.

## MTU và fragmentation

Link có Maximum Transmission Unit (MTU). Packet lớn hơn path support có thể cần fragmentation hoặc Path MTU Discovery.

Tunnel thêm headers làm effective payload MTU nhỏ hơn. Misconfigured MTU có thể gây symptom “một số site/request treo” rất khó debug.

## Socket buffers và backpressure

Kernel có send/receive buffers. `send()` thành công có thể chỉ nghĩa bytes được copy vào send buffer, chưa tới peer.

Nếu peer/network chậm, buffer đầy rồi writer block/return backpressure. Application-level queue không được grow vô hạn chỉ vì socket API tạm nhận được data.

## Common Misconceptions

**“Một send = một recv.”** Sai với TCP byte stream.

**“NAT là security mechanism.”** Nó có side effect chặn unsolicited inbound mappings nhưng không thay thế firewall/authentication.

**“VPN bảo mật mọi thứ.”** Nó bảo vệ tunnel traffic; endpoint malware, weak credentials và application vulnerabilities vẫn tồn tại.

## Mental Model

> Socket là local handle tới protocol state; NAT/firewall/VPN là transformations/policies ở network boundaries. Debug network cần biết bytes đang ở process buffer, kernel socket, packet path hay tunnel layer nào.

## Kết nối

Đọc [TCP/UDP](./02_transport_tcp_udp_and_congestion.md), [routing](./07_routing_protocols_and_the_internet.md), [OS async I/O](../03_operating_systems/07_boot_device_drivers_and_async_io.md) và [web security](../07_security_reliability/06_web_application_security.md).