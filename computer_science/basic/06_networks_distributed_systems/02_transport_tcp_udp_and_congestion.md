# TCP, UDP, flow control, congestion control và packet-level diagnosis

IP best-effort chuyển datagrams nhưng không guarantee delivery, order hay duplicate-free. Transport layer thêm abstraction giữa application endpoints qua ports và state machines. Ở mức foundation, cần hiểu TCP/UDP semantics; ở mức systems reasoning, cần theo được đường **packet → ACK/loss signal → congestion/window state → retransmission/queue → application latency**.

Điểm quan trọng là phân biệt ba pressure sources:

```text
receiver pressure
network-path pressure
application/runtime pressure
```

TCP có mechanism cho hai loại đầu, nhưng application vẫn có thể tạo queue/backlog ở tầng trên.

## 1. UDP: ít contract hơn, không phải “TCP nhưng nhanh”

UDP (User Datagram Protocol) giữ datagram boundaries và thêm ports + checksum semantics, nhưng không connection handshake, retransmission, ordering hay congestion control ở protocol itself.

Application có thể tự xây reliability, sequencing, pacing và congestion behavior. QUIC chạy trên UDP nhưng tự triển khai transport semantics phong phú hơn ở userspace, cho thấy UDP có thể là substrate chứ không phải lời giải hoàn chỉnh.

Invariant của UDP layer đơn giản hơn; burden được chuyển lên application/protocol phía trên.

## 2. TCP cung cấp reliable ordered byte stream

TCP là byte stream, không giữ application message boundaries. Sender có thể `write()` 100 bytes rồi 200 bytes nhưng receiver có thể `read()` theo chunks khác tùy buffering.

Application protocol cần framing riêng: length prefix, delimiter hoặc higher-level format.

TCP invariant chính là dữ liệu được trình bày cho application theo byte order hợp lệ, duplicate bytes được loại và missing data được phục hồi hoặc connection thất bại thay vì âm thầm tạo byte stream sai.

## 3. Sequence number và ACK tạo knowledge về progress

TCP gắn sequence number cho bytes và receiver ACK progress. Sender dùng ACK, duplicate/selective acknowledgement và timers để suy ra dữ liệu đã tới hay có khả năng mất.

ACK không nhất thiết nghĩa application bên nhận đã xử lý bytes; nó chủ yếu phản ánh transport receive progress theo implementation/protocol semantics.

Đây là abstraction boundary quan trọng: transport delivery không phải business acknowledgement.

## 4. Retransmission là recovery, nhưng làm latency tăng

Khi packet bị mất, sender gửi lại data cần thiết. Reliability được mua bằng waiting + extra traffic.

Loss recovery có thể được kích hoạt bởi timeout hoặc ACK-pattern-based detection tùy implementation. Nếu recovery phải đợi timeout, latency spike có thể lớn hơn nhiều so với một RTT bình thường.

Do đó application p99 có thể tăng mạnh dù average packet loss rất nhỏ.

## 5. Packet loss không nói nguyên nhân

Một packet có thể mất vì:

```text
congested queue drop
device/NIC/kernel drop
wireless corruption/interference
routing/path change
MTU/fragmentation issue
firewall/policy drop
receiver/application không đọc kịp gây secondary pressure
```

“Có retransmission” là evidence của delivery problem, không tự chứng minh ISP/network congestion.

Diagnosis cần correlate path, interface, queue và endpoint evidence.

## 6. Flow control bảo vệ receiver

Receiver có finite buffer. Advertised receive window nói sender biết bao nhiêu bytes có thể outstanding mà receiver còn khả năng nhận.

Nếu application bên nhận đọc socket chậm, receive buffer đầy và advertised window có thể co lại. Sender bị giới hạn dù network path còn bandwidth.

Causal chain có thể là:

```text
receiver application chậm
→ socket buffer đầy
→ receive window giảm
→ sender throughput giảm
```

Đây là receiver backpressure, khác congestion control.

## 7. Congestion control bảo vệ network path

Congestion control giới hạn amount in flight theo signal như ACK timing, loss và ECN tùy algorithm. Congestion window phản ánh estimate về safe path capacity.

Nếu sender bơm quá nhanh, router/switch queues tăng, delay tăng rồi packet bị drop/mark. Congestion control cố giữ throughput tốt mà tránh congestion collapse.

Flow-control window và congestion window cùng có thể giới hạn sender:

```text
usable in-flight data
≈ min(receiver window, congestion window, protocol/implementation limits)
```

## 8. Bandwidth-delay product giải thích vì sao RTT quan trọng

Để fill một path bandwidth cao nhưng RTT lớn, cần đủ data in flight:

\[
BDP = bandwidth \times RTT
\]

Ví dụ 1 Gbit/s × 0,1 s ≈ 12,5 MB. Nếu effective window thấp hơn nhiều BDP, sender không thể tận dụng link dù không có loss.

Đây là lý do “bandwidth 1 Gbps” không đồng nghĩa một TCP flow đạt 1 Gbps trên high-RTT path.

## 9. Queueing delay có thể tăng trước packet loss

Router queue có thể dài lên khi arrival rate gần/exceeds output capacity. Packet vẫn chưa drop nhưng RTT tăng vì phải chờ queue.

Đây là **bufferbloat-style reasoning**: large buffers có thể giữ throughput nhưng làm latency lớn. Nếu application timeout dựa baseline RTT thấp, queueing spike có thể tạo retry trước cả khi packet loss nghiêm trọng.

Network pressure vì vậy nên đo cả latency/RTT distribution chứ không chỉ loss percentage.

## 10. Congestion window thay đổi theo feedback loop

Sender tăng sending rate dựa observed delivery, rồi giảm/điều chỉnh khi thấy congestion signal. Algorithm khác nhau chọn cách probe bandwidth và respond loss/ECN khác nhau.

Tên algorithm như CUBIC/BBR là implementation family; mental model bền hơn là:

```text
estimate path state
→ choose in-flight/pacing rate
→ observe ACK/loss/RTT
→ update estimate
```

Control loop quá aggressive có thể tạo queue/loss; quá conservative làm underutilization.

## 11. RTT measurement và retransmission timeout cần variance

Một fixed timeout không phù hợp mọi path. TCP ước lượng RTT và variance để chọn recovery timer theo state hiện tại.

Timeout quá ngắn tạo spurious retransmission; quá dài làm recovery chậm. Path có jitter cao khiến timer design khó hơn.

Production symptom “request thỉnh thoảng chậm đúng vài trăm ms/giây” có thể liên quan loss recovery/retransmission timer chứ không phải handler compute.

## 12. Reordering khác loss

Packets có thể tới khác thứ tự vì parallel paths, NIC/offload behavior hoặc network conditions. Sender/receiver không nên kết luận mọi out-of-order arrival là loss ngay lập tức.

Modern mechanisms như selective acknowledgement giúp mô tả holes trong received sequence space tốt hơn cumulative ACK đơn giản.

Diagnosis packet trace cần phân biệt:

```text
actual loss
reordering
duplicate packet
retransmission
spurious retransmission
```

Nếu không, ta dễ đổ lỗi congestion sai.

## 13. Head-of-line blocking là consequence của ordered byte-stream contract

Nếu byte range trước bị mất, TCP không thể deliver later bytes tới application như thể gap không tồn tại. Với HTTP/2 nhiều logical streams trên một TCP connection, packet loss ở transport có thể trì hoãn data của nhiều streams cùng connection.

HTTP/3/QUIC dùng independent streams nên loss trên một stream không phải block application delivery của stream khác theo cùng cách, dù chúng vẫn chia sẻ congestion/path capacity.

Đây là ví dụ design trade-off: giữ ordering ở granularity nào quyết định blast radius của một lost packet.

## 14. Connection setup tạo cold-path latency

TCP handshake thêm RTT trước khi application data theo classic flow. TLS thêm identity/cryptographic handshake, dù resumption và modern protocol giảm round trips.

Connection reuse amortize setup cost nhưng tạo state: pool size, idle timeout, stale connections và load-balancing locality.

Cold vs warm request phải được tách trong latency analysis.

## 15. SYN backlog và accept queue là server-side network queues

Trước application handler, connection có thể phải đi qua handshake state và accept queue. Under burst/attack/saturation, backlog limits có thể tạo drops/timeouts trước khi application framework thấy request.

Một service dashboard có “0 request errors” trong lúc clients connect timeout có thể là observability blind spot: failure đang xảy ra trước HTTP/application layer.

Evidence cần nối kernel socket/listen state với edge/client metrics.

## 16. Socket buffers có thể che pressure tạm thời

`send()` return nhanh có thể chỉ nghĩa bytes đã vào local socket buffer. Nếu network/downstream chậm, buffer dần đầy; sau đó sender block hoặc nhận backpressure/error tùy mode.

Unbounded application buffering phía trên socket không giải pressure; nó chỉ chuyển queue vào heap và làm latency/memory debt lớn hơn.

Giống các layer khác, buffer hấp thụ burst ngắn chứ không tạo sustainable capacity.

## 17. MTU và fragmentation: packet size là path property

Mỗi link có Maximum Transmission Unit (MTU). IP packet lớn hơn path hỗ trợ cần fragmentation ở một số scenarios/protocol versions hoặc sender phải dùng packet size nhỏ hơn qua Path MTU Discovery.

Nếu required ICMP/control signals bị filter hoặc PMTU knowledge sai, connection có thể exhibit “small request works, large transfer stalls” kiểu black-hole behavior.

Diagnosis cần hỏi:

```text
problem phụ thuộc payload size không?
path MTU có thay đổi qua tunnel/VPN không?
ICMP/PMTU discovery có hoạt động không?
MSS negotiated là bao nhiêu?
```

Không phải mọi timeout đều là packet loss ngẫu nhiên.

## 18. Tunneling/VPN làm effective MTU thấp hơn

Encapsulation thêm headers nên payload packet phải nhỏ hơn để fit outer path MTU. Nếu network design thêm VPN/overlay/service mesh tunnel mà không quản MTU/MSS đúng, fragmentation/drop có thể xuất hiện chỉ ở một path/environment.

Đây là leaky abstraction: application thấy TCP timeout nhưng lower layer quyết định behavior là encapsulation overhead.

## 19. ECN tách congestion signal khỏi drop trong một số path

Explicit Congestion Notification cho phép network mark congestion thay vì phải drop packet nếu endpoints/path hỗ trợ. Mental model quan trọng là congestion signal không bắt buộc đồng nghĩa packet loss.

Điều này củng cố distinction:

```text
congestion = resource pressure trên path
loss       = một possible observable consequence
```

Production tooling phải đọc đúng signal của stack hiện tại.

## 20. NIC offload làm packet capture khó diễn giải hơn

TSO/GSO/GRO/LRO-family optimizations cho phép kernel/NIC xử lý packets theo batches/segments lớn để giảm per-packet CPU cost. Vì vậy packet capture tại host có thể hiển thị segment size/checksum behavior khác wire-level packets.

Một capture “checksum bad” trên outbound packet có thể là artifact trước NIC hoàn tất checksum offload, không nhất thiết packet thật trên wire bị hỏng.

Evidence cần biết capture point và offload state trước khi kết luận.

## 21. Distributed timeout nằm trên transport reliability

TCP reliable byte stream không làm RPC reliable theo business semantics. Process có thể crash sau khi nhận request, response có thể mất, connection có thể reset, caller có thể timeout sau khi remote side effect đã commit.

Transport trả lời “bytes có đi theo stream không”; distributed application vẫn phải giải ambiguity:

```text
request chưa tới?
đã tới nhưng chưa xử lý?
đã xử lý nhưng response mất?
```

Do đó idempotency/retry semantics nằm trên TCP.

## 22. Packet-level diagnosis bắt đầu từ symptom và direction

Khi thấy network latency/error, trước tiên xác định:

```text
connect path hay established connection?
upload hay download?
một endpoint hay nhiều endpoints?
payload-size dependent?
regional/path dependent?
loss/retransmission hay pure queueing delay?
receiver window hay congestion window limiting?
```

Sau đó mới chọn packet capture/counters.

Không bắt đầu bằng “TCP tuning” trước khi biết pressure nằm sender, receiver hay path.

## 23. Evidence ở client/server/path

Một diagnosis mạnh kết hợp nhiều viewpoints:

```text
Application:
- connect/TLS/request timing
- timeout/retry rate
- bytes transferred

Host transport:
- RTT estimate
- retransmissions
- send/receive queue
- window state
- connection resets

Kernel/NIC:
- drops/errors
- listen/accept backlog
- interface queue
- offload context

Packet trace:
- sequence/ACK progression
- retransmission/reordering
- RTT samples
- handshake/FIN/RST
- MSS/MTU clues

Network path:
- route/path change
- loss/latency by hop only when measurement semantics justify it
- ECN/queue telemetry where available
```

Một traceroute đơn lẻ không chứng minh hop hiển thị cao là bottleneck; control-plane response behavior có thể khác forwarded traffic.

## 24. Failure matrix cho transport path

Hãy thử phân biệt:

```text
DNS resolves wrong/stale endpoint
SYN timeout
TCP established nhưng TLS fail
small packets work, large payload stalls
retransmission burst khi load tăng
receive window collapses
server accept queue saturation
RST sau idle reuse
path migration/routing change
```

Mỗi symptom chỉ tới abstraction khác nhau. “Network issue” quá rộng để là root cause.

## 25. Mô hình tư duy

> TCP là state machine biến unreliable packet delivery thành ordered byte stream bằng sequence, ACK, retransmission, flow control và congestion control. Receiver window bảo vệ endpoint; congestion window/pacing phản ứng path capacity; socket/backlog queues nối transport với OS/application. **Packet loss, reordering, MTU, queueing và receiver pressure có thể tạo symptom giống nhau ở application, nên production diagnosis phải theo sequence/ACK/window/queue evidence thay vì chỉ nhìn timeout.**

## Những hiểu nhầm thường gặp

**“TCP preserve message boundaries.”** Không; application cần framing.

**“UDP nhanh hơn TCP.”** UDP có ít transport semantics hơn; application có thể phải tự trả complexity/cost.

**“Retransmission nghĩa network congestion.”** Không; congestion chỉ là một possible cause.

**“0% packet loss nghĩa network healthy.”** Queueing delay/bufferbloat có thể làm latency xấu trước drop.

**“Ping/traceroute đủ để chứng minh application path tốt.”** Không; protocol/path/policy có thể khác và chúng không đo server/runtime queues.

**“TCP reliable nghĩa retry request luôn an toàn.”** Transport reliability không tạo business idempotency.

## Kết nối

[Queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md) giải buffering; [Web request](./03_dns_http_tls_and_web_request.md) xây HTTP/TLS trên transport; [Distributed systems](./04_distributed_systems_time_failure_and_consistency.md) giải timeout ambiguity; [Advanced end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md) nối DNS/TCP/TLS với proxy/runtime/DB; [OS I/O](../../03_operating_systems/advanced/05_epoll_io_uring_zero_copy_and_dma.md) giải socket readiness/completion phía host.