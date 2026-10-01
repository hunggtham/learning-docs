# Mạng (network / 네트워크) layers, packets và encapsulation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Mạng (network / 네트워크) layers, packets và encapsulation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Giao thức (protocol / 프로토콜) là đặc tả hợp đồng (contract / 계약) giữa peers** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Layering** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Mạng (network / 네트워크) cho phép computers trao đổi dữ liệu qua links không hoàn hảo, heterogeneous hardware và nhiều administrative domains. Để hệ thống không phải giải mọi vấn đề cùng lúc, networking chia responsibilities thành layers và protocols.

## Giao thức (protocol / 프로토콜) là đặc tả hợp đồng (contract / 계약) giữa peers

Giao thức (protocol / 프로토콜) định nghĩa message format, trạng thái (state / 상태) transitions, timing/lỗi (error / 오류) rules và meaning. Hai endpoints có thể hiện thực (implementation / 구현) khác nhau nhưng interoperable nếu cùng đặc tả hợp đồng (contract / 계약).

Giao thức (protocol / 프로토콜) không nhất thiết “reliable”. Ethernet frame có CRC detection; IP best-effort; UDP không retransmit; TCP thêm reliable ordered byte stream. Mỗi tầng (layer / 계층) cung cấp thuộc tính (property / 속성) phù hợp phạm vi (scope / 범위).

> **Chuyển mạch:** Protocol là contract giữa peers; layering tách trách nhiệm và failure domain, rồi encapsulation đóng gói header/payload qua từng layer.

## Layering

OSI 7-layer mô hình (model / 모델) hữu ích về vocabulary nhưng Internet ngăn xếp (stack / 스택) thực tế thường được lập luận (reasoning / 추론) như link → internet/mạng (network / 네트워크) → vận chuyển (transport / 전송) → ứng dụng (application / 애플리케이션). tầng (layer / 계층) boundaries không hoàn toàn sạch; firewalls, NAT, TLS termination và proxies tạo cross-layer realities.

Một ứng dụng (application / 애플리케이션) HTTP không cần biết Wi-Fi modulation. IP không cần biết HTTP ngữ nghĩa (semantics / 의미론). Đây là lớp trừu tượng (abstraction / 추상화).

> **Chuyển mạch:** Ở chặng này của **Mạng (network / 네트워크) layers, packets và encapsulation**, **Encapsulation** tiếp nhận điểm tựa từ **Layering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Packet switching** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Encapsulation

Ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터) được wrapped bởi headers theo layers:

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

Receiver unwrap theo chiều ngược. Header chứa siêu dữ liệu (metadata / 메타데이터) tầng (layer / 계층) cần: ports, addresses, chuỗi (sequence / 시퀀스) numbers, checksums, giao thức (protocol / 프로토콜) identifiers...

Encapsulation không “mã hóa bảo mật”; nó chỉ đóng gói cấu trúc (structure / 구조). Encryption như TLS là separate thuộc tính (property / 속성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mạng (network / 네트워크) layers, packets và encapsulation**, **Packet switching** tiếp nhận điểm tựa từ **Encapsulation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MTU và fragmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Packet switching

Internet chia dữ liệu (data / 데이터) thành packets thay vì reserve dedicated circuit cho mỗi conversation. Links multiplex packets từ nhiều flows. Routers forward mỗi packet theo routing trạng thái (state / 상태).

Packet switching sử dụng bandwidth linh hoạt nhưng tạo queueing, mất mát (loss / 손실) và variable delay khi demand vượt sức chứa (capacity / 용량). vận chuyển (transport / 전송)/ứng dụng (application / 애플리케이션) phải sống với những effects này.

> **Chuyển mạch:** Trong **Mạng (network / 네트워크) layers, packets và encapsulation**, **MTU và fragmentation** tiếp nhận điểm tựa từ **Packet switching** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Addressing ở nhiều layers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MTU và fragmentation

Link có Maximum Transmission đơn vị (unit / 단위) — MTU. IP packet quá lớn có thể cần fragmentation tùy IPv4/đường dẫn (path / 경로) hành vi (behavior / 동작); IPv6 routers không fragment in-path theo same way. hiện đại (modern / 현대적) transports thường use đường dẫn (path / 경로) MTU Discovery/kích thước (size / 크기) choices để tránh fragmentation.

TCP MSS liên quan maximum TCP payload based on đường dẫn (path / 경로)/giao diện (interface / 인터페이스) các giả định (assumptions / 가정들). “Packet kích thước (size / 크기)” vì vậy không một con số universal.

> **Chuyển mạch:** Ở chặng này của **Mạng (network / 네트워크) layers, packets và encapsulation**, **Addressing ở nhiều layers** tiếp nhận điểm tựa từ **MTU và fragmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lỗi (error / 오류) detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Addressing ở nhiều layers

MAC address phục vụ local-link delivery lĩnh vực (domain / 도메인); IP address cho network-layer routing; cổng (port / 포트) number identify vận chuyển (transport / 전송) endpoint/ứng dụng (application / 애플리케이션) socket; DNS name là human/ứng dụng (application / 애플리케이션) naming ánh xạ (mapping / 매핑) tới records/addresses.

Một yêu cầu (request / 요청) `example.com:443` trải qua nhiều naming/address layers. Không nên gọi tất cả là “địa chỉ mạng” như một khái niệm duy nhất.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mạng (network / 네트워크) layers, packets và encapsulation**, **Lỗi (error / 오류) detection** tiếp nhận điểm tựa từ **Addressing ở nhiều layers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Queues và độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lỗi (error / 오류) detection

Frame CRC detect corruption ở link; TCP/UDP checksum cover vận chuyển (transport / 전송) pseudo-header/dữ liệu (data / 데이터) với strength limitations; higher layers may use cryptographic integrity. Detection không đồng nghĩa correction/retransmission; tầng (layer / 계층) chính sách (policy / 정책) quyết định reaction.

> **Chuyển mạch:** Trong **Mạng (network / 네트워크) layers, packets và encapsulation**, **Queues và độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Lỗi (error / 오류) detection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Queues và độ trễ (latency / 지연 시간)

Router/NIC/socket buffers absorb bursts. Khi buffer full, packet drop; khi buffer quá lớn, queueing độ trễ (latency / 지연 시간) tăng (bufferbloat). More buffering không luôn better.

Độ trễ (latency / 지연 시간) có propagation + transmission + processing + queueing. Bandwidth cao giảm transmission thời gian (time / 시간) nhưng không làm speed of light nhanh hơn.

> **Chuyển mạch:** Ở chặng này của **Mạng (network / 네트워크) layers, packets và encapsulation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Queues và độ trễ (latency / 지연 시간)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> mạng (network / 네트워크) ngăn xếp (stack / 스택) là **nhiều contracts lồng nhau**. Mỗi tầng (layer / 계층) chỉ thấy payload + siêu dữ liệu (metadata / 메타데이터) cần thiết; độ tin cậy (reliability / 신뢰성)/bảo mật (security / 보안)/naming/routing được thêm ở những tầng khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Mạng (network / 네트워크) layers, packets và encapsulation**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“TCP packet” là cách gọi chính xác cho mọi thứ.”** TCP segment được carried trong IP packet, rồi link frame; colloquial dùng packet rộng nhưng layer-aware lập luận (reasoning / 추론) nên phân biệt.

**“Nhiều bandwidth nghĩa ping thấp.”** RTT có propagation/queueing/processing; bandwidth và độ trễ (latency / 지연 시간) là dimensions khác.

**“Encapsulation = encryption.”** Encapsulation là framing/siêu dữ liệu (metadata / 메타데이터); encryption bảo confidentiality.

> **Chuyển mạch:** Trong **Mạng (network / 네트워크) layers, packets và encapsulation**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[I/O/DMA](../02_computer_architecture/03_io_interrupts_dma_and_devices.md) giải NIC ↔ bộ nhớ (memory / 메모리); [queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) xuất hiện trong buffers; tiếp theo [Ethernet/IP/routing](./01_ethernet_ip_subnetting_and_routing.md) giải forwarding, rồi [TCP/UDP](./02_transport_tcp_udp_and_congestion.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
