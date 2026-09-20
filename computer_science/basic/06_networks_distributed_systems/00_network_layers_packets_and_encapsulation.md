# Network layers, packets và encapsulation

Network (네트워크 / mạng máy tính) cho phép computers trao đổi dữ liệu qua links không hoàn hảo, heterogeneous hardware và nhiều administrative domains. Để hệ thống không phải giải mọi vấn đề cùng lúc, networking chia responsibilities thành layers và protocols.

## Protocol là contract giữa peers

Protocol (프로토콜 / giao thức) định nghĩa message format, state transitions, timing/error rules và meaning. Hai endpoints có thể implementation khác nhau nhưng interoperable nếu cùng contract.

Protocol không nhất thiết “reliable”. Ethernet frame có CRC detection; IP best-effort; UDP không retransmit; TCP thêm reliable ordered byte stream. Mỗi layer cung cấp property phù hợp scope.

## Layering

OSI 7-layer model hữu ích về vocabulary nhưng Internet stack thực tế thường được reasoning như link → internet/network → transport → application. Layer boundaries không hoàn toàn sạch; firewalls, NAT, TLS termination và proxies tạo cross-layer realities.

Một application HTTP không cần biết Wi-Fi modulation. IP không cần biết HTTP semantics. Đây là abstraction.

## Encapsulation

Application data được wrapped bởi headers theo layers:

```text
HTTP message
  ↓ TCP header
TCP segment
  ↓ IP header
IP packet/datagram
  ↓ Ethernet/Wi‑Fi header+trailer
frame
  ↓ physical signals
```

Receiver unwrap theo chiều ngược. Header chứa metadata layer cần: ports, addresses, sequence numbers, checksums, protocol identifiers...

Encapsulation không “mã hóa bảo mật”; nó chỉ đóng gói structure. Encryption như TLS là separate property.

## Packet switching

Internet chia data thành packets thay vì reserve dedicated circuit cho mỗi conversation. Links multiplex packets từ nhiều flows. Routers forward mỗi packet theo routing state.

Packet switching sử dụng bandwidth linh hoạt nhưng tạo queueing, loss và variable delay khi demand vượt capacity. Transport/application phải sống với những effects này.

## MTU và fragmentation

Link có Maximum Transmission Unit — MTU. IP packet quá lớn có thể cần fragmentation tùy IPv4/path behavior; IPv6 routers không fragment in-path theo same way. Modern transports thường use Path MTU Discovery/size choices để tránh fragmentation.

TCP MSS liên quan maximum TCP payload based on path/interface assumptions. “Packet size” vì vậy không một con số universal.

## Addressing ở nhiều layers

MAC address phục vụ local-link delivery domain; IP address cho network-layer routing; port number identify transport endpoint/application socket; DNS name là human/application naming mapping tới records/addresses.

Một request `example.com:443` trải qua nhiều naming/address layers. Không nên gọi tất cả là “địa chỉ mạng” như một khái niệm duy nhất.

## Error detection

Frame CRC detect corruption ở link; TCP/UDP checksum cover transport pseudo-header/data với strength limitations; higher layers may use cryptographic integrity. Detection không đồng nghĩa correction/retransmission; layer policy quyết định reaction.

## Queues và latency

Router/NIC/socket buffers absorb bursts. Khi buffer full, packet drop; khi buffer quá lớn, queueing latency tăng (bufferbloat). More buffering không luôn better.

Latency có propagation + transmission + processing + queueing. Bandwidth cao giảm transmission time nhưng không làm speed of light nhanh hơn.

## Mental Model

> Network stack là **nhiều contracts lồng nhau**. Mỗi layer chỉ thấy payload + metadata cần thiết; reliability/security/naming/routing được thêm ở những tầng khác nhau.

## Common Misconceptions

**“TCP packet” là cách gọi chính xác cho mọi thứ.”** TCP segment được carried trong IP packet, rồi link frame; colloquial dùng packet rộng nhưng layer-aware reasoning nên phân biệt.

**“Nhiều bandwidth nghĩa ping thấp.”** RTT có propagation/queueing/processing; bandwidth và latency là dimensions khác.

**“Encapsulation = encryption.”** Encapsulation là framing/metadata; encryption bảo confidentiality.

## Kết nối

[I/O/DMA](../02_computer_architecture/03_io_interrupts_dma_and_devices.md) giải NIC ↔ memory; [queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) xuất hiện trong buffers; tiếp theo [Ethernet/IP/routing](./01_ethernet_ip_subnetting_and_routing.md) giải forwarding, rồi [TCP/UDP](./02_transport_tcp_udp_and_congestion.md).
