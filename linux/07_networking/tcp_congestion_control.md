# TCP congestion control, flow control và hành vi mạng dưới tải

TCP không chỉ thiết lập kết nối rồi chuyển byte. Nó còn phải trả lời hai câu hỏi khác nhau: **người nhận có đủ buffer để nhận thêm dữ liệu không?** và **mạng ở giữa có đủ khả năng vận chuyển thêm dữ liệu không?** Hai câu hỏi này tương ứng với **điều khiển luồng (flow control)** và **điều khiển tắc nghẽn (congestion control)**.

Nếu không hiểu hai cơ chế này, rất dễ nhìn một kết nối “không mất” nhưng throughput thấp rồi đổ lỗi sai cho ứng dụng hoặc server.

## Flow control và congestion control khác nhau

Flow control bảo vệ **receiver**. Receiver quảng bá cửa sổ nhận (receive window) để sender biết lượng dữ liệu có thể gửi thêm mà chưa cần acknowledgment.

Congestion control bảo vệ **network path**. Sender cố ước lượng bao nhiêu dữ liệu có thể tồn tại trên đường mà không gây tắc nghẽn nghiêm trọng.

Có thể hình dung lượng dữ liệu sender được phép giữ “đang bay” là giới hạn bởi cả hai:

```text
send window ≈ min(receiver window, congestion window)
```

Receiver khỏe không có nghĩa network path khỏe, và ngược lại.

## Congestion window

**Cửa sổ tắc nghẽn (congestion window - cwnd)** là trạng thái ở sender. TCP tăng hoặc giảm `cwnd` dựa trên tín hiệu từ mạng như acknowledgment, packet loss hoặc ECN tùy thuật toán.

Nếu `cwnd` nhỏ, sender không thể giữ nhiều byte in-flight dù link có bandwidth cao.

## Bandwidth-delay product

Một khái niệm quan trọng là **tích băng thông–độ trễ (bandwidth-delay product - BDP)**:

```text
BDP = bandwidth × round-trip time
```

Ví dụ đường truyền 1 Gbit/s với RTT 100 ms:

```text
1,000,000,000 bit/s × 0.1 s
= 100,000,000 bit
≈ 12.5 MB
```

Muốn dùng gần hết bandwidth, kết nối cần có khả năng giữ khoảng 12.5 MB dữ liệu đang bay trên đường.

Đây là lý do cùng một server nhưng truyền file tới máy cùng datacenter và tới lục địa khác có throughput khác rất lớn.

## RTT là gì?

**Round-trip time (RTT)** là thời gian một tín hiệu đi tới peer và phản hồi quay lại.

Có thể quan sát sơ bộ:

```bash
ping <host>
```

Nhưng ICMP RTT không luôn bằng TCP application RTT. Route, firewall, queuing và ưu tiên traffic có thể khác.

Trong TCP socket, `ss` có thể cung cấp thông tin sâu hơn:

```bash
ss -ti dst <IP>
```

Tùy kernel, output có thể cho thấy `rtt`, `cwnd`, retransmission và thuật toán congestion control.

## Slow start

Khi kết nối mới bắt đầu, sender chưa biết capacity của path. **Khởi động chậm (slow start)** tăng lượng dữ liệu in-flight theo tốc độ nhanh từ một cửa sổ ban đầu thay vì lập tức gửi hết bandwidth.

Ý tưởng:

```text
cwnd nhỏ
  ↓
ACK thành công
  ↓
cwnd tăng nhanh
  ↓
tiếp tục cho tới ngưỡng hoặc tín hiệu congestion
```

Tên “slow start” hơi gây hiểu lầm vì tốc độ tăng ban đầu thực ra khá nhanh theo cấp số nhân qua các vòng RTT.

## Vì sao request ngắn chịu ảnh hưởng lớn?

Nếu response chỉ vài KB, slow start không đáng kể. Nhưng response vừa đủ lớn và kết nối tồn tại ngắn, connection có thể kết thúc trước khi TCP đạt throughput tối đa.

Điều này là một lý do HTTP keep-alive và connection pooling có giá trị: tái sử dụng connection không chỉ tránh handshake mà còn giữ lại một phần trạng thái transport đã “học” path.

## Congestion avoidance

Sau giai đoạn đầu, TCP chuyển sang tăng thận trọng hơn. Khi phát hiện congestion, thuật toán giảm tốc độ gửi.

Cơ chế cụ thể phụ thuộc congestion control algorithm.

## Packet loss là một tín hiệu congestion truyền thống

Nhiều thuật toán TCP cổ điển coi packet loss là tín hiệu mạng đã quá tải. Khi mất packet, sender retransmit và giảm congestion window.

Nhưng packet loss cũng có thể do:

- link lỗi;
- Wi-Fi nhiễu;
- firewall/policer;
- buffer overflow;
- route thay đổi;
- NIC/kernel drop.

Do đó retransmission cho biết có vấn đề truyền tải, không tự chứng minh nguyên nhân cuối cùng.

## Retransmission

Quan sát tổng quan:

```bash
nstat -az | grep -E 'TcpRetransSegs|TcpTimeouts'
```

Hoặc:

```bash
ss -ti
```

Packet capture:

```bash
sudo tcpdump -ni any host <IP>
```

Wireshark thường đánh dấu retransmission, duplicate ACK và out-of-order packet, nhưng phải cẩn thận với capture point và offloading.

## Fast retransmit

Sender không nhất thiết chờ timeout mới retransmit. Duplicate ACK có thể cho sender biết một segment bị mất trong khi segment sau vẫn tới nơi, giúp retransmit nhanh hơn.

Đây là ví dụ TCP dùng pattern acknowledgment để suy luận trạng thái mạng.

## RTO và timeout

**Retransmission timeout (RTO)** được ước lượng từ RTT và độ biến thiên RTT. Nếu acknowledgment không tới trước timeout, sender retransmit.

Tail latency mạng cao hoặc jitter mạnh có thể làm timeout tăng và throughput giảm ngay cả khi bandwidth danh nghĩa lớn.

## CUBIC

Nhiều Linux distribution sử dụng hoặc từng sử dụng **CUBIC** làm congestion control mặc định. CUBIC tăng cửa sổ dựa trên một hàm bậc ba theo thời gian sau congestion event, nhằm hoạt động tốt hơn trên mạng bandwidth-delay product lớn so với Reno truyền thống.

Kiểm tra thuật toán hiện tại:

```bash
sysctl net.ipv4.tcp_congestion_control
```

Danh sách thuật toán khả dụng:

```bash
sysctl net.ipv4.tcp_available_congestion_control
```

Không nên đổi thuật toán trên production chỉ để “tăng tốc” nếu chưa benchmark workload/path thực tế.

## BBR

**BBR (Bottleneck Bandwidth and Round-trip propagation time)** dùng mô hình ước lượng bandwidth bottleneck và RTT tối thiểu thay vì chủ yếu đợi packet loss mới giảm tốc.

Ý tưởng lớn:

```text
ước lượng bandwidth có thể phục vụ
+
ước lượng RTT nền
        ↓
điều khiển pacing và lượng data in-flight
```

BBR có thể cải thiện một số workload/path, nhưng hành vi fairness và tương tác với queue/network khác cần được đánh giá thực tế.

## Pacing

Thay vì gửi một burst lớn rồi im lặng, sender có thể **điều tiết nhịp gửi (pacing)** để phân bố packet đều hơn theo thời gian.

Burst lớn dễ làm queue tăng đột ngột và gây drop. Pacing giúp giảm burstiness.

## Bufferbloat

Queue mạng quá lớn có thể tránh packet loss nhưng giữ packet quá lâu, tạo **bufferbloat**.

Kết quả nghịch lý:

```text
không mất packet nhiều
nhưng RTT tăng mạnh dưới tải
```

Ví dụ đường truyền bình thường ping 20 ms nhưng khi upload lớn ping tăng 300–1000 ms. Đây là queueing latency.

## Queue management

Các cơ chế **Active Queue Management (AQM)** như fq_codel cố kiểm soát queue latency thay vì chỉ để buffer đầy rồi drop.

Trên Linux có thể kiểm tra qdisc:

```bash
tc qdisc show
```

Việc cấu hình qdisc cần hiểu topology và workload; đây không phải setting nên đổi mù quáng.

## Receive window và window scaling

TCP header truyền thống có giới hạn kích thước field window. **Window scaling** cho phép cửa sổ lớn hơn, cần cho high-BDP network.

Nếu receive/send buffer quá nhỏ, throughput có thể bị giới hạn dù congestion window cho phép nhiều hơn.

Kernel Linux thường auto-tune TCP buffers trong giới hạn cấu hình.

Kiểm tra:

```bash
sysctl net.ipv4.tcp_rmem
sysctl net.ipv4.tcp_wmem
sysctl net.core.rmem_max
sysctl net.core.wmem_max
```

Không nên tăng tất cả buffer lên cực lớn. Buffer lớn tiêu RAM và có thể góp phần vào queueing/bufferbloat.

## Zero window

Nếu receiver không đọc socket đủ nhanh, receive buffer có thể đầy và quảng bá **zero window**. Sender phải tạm dừng.

Đây là flow-control bottleneck, không phải congestion network.

Trong backend, nguyên nhân có thể là:

- application thread bị block;
- GC pause dài;
- downstream processing chậm;
- event loop không đọc socket kịp.

## TCP backlog và handshake dưới tải

Server còn có queue cho kết nối đang handshake và kết nối đã hoàn thành handshake chờ application `accept()`.

Nếu application accept quá chậm hoặc server bị overload, connection mới có thể timeout/drop dù process vẫn sống.

Quan sát:

```bash
ss -s
nstat -az | grep -i listen
```

Các counter cụ thể phụ thuộc kernel.

## SYN flood và SYN cookies

SYN flood cố làm cạn tài nguyên theo dõi kết nối chưa hoàn tất. Linux có cơ chế SYN cookies để giảm một số ảnh hưởng khi queue bị áp lực.

Kiểm tra:

```bash
sysctl net.ipv4.tcp_syncookies
```

SYN cookies là cơ chế phòng vệ, không thay thế capacity planning hoặc network protection upstream.

## TIME_WAIT và congestion control

`TIME_WAIT` thường xuất hiện ở endpoint chủ động đóng connection. Nhiều `TIME_WAIT` không trực tiếp nghĩa congestion control lỗi, nhưng connection churn cao làm mất lợi ích từ connection reuse và tăng chi phí handshake/slow start.

Vì vậy connection pool có tác động cả application resource lẫn transport efficiency.

## Keepalive transport và keep-alive HTTP khác nhau

TCP keepalive là probe để phát hiện peer đã chết sau một khoảng thời gian. HTTP keep-alive là tái sử dụng connection cho nhiều request.

Hai khái niệm cùng tên gần giống nhưng mục tiêu khác nhau.

## MTU, MSS và fragmentation

TCP thường chọn **Maximum Segment Size (MSS)** dựa trên MTU. Nếu path MTU nhỏ hơn dự đoán và ICMP cần thiết bị chặn, connection có thể gặp hiện tượng “handshake được nhưng truyền payload lớn bị treo”.

Đây là **PMTU black hole**.

Điều tra:

```bash
tracepath <host>
ip link show
```

## TSO/GSO/GRO và quan sát packet

Linux/NIC có offloading để gom hoặc tách packet nhằm giảm CPU overhead. Vì vậy packet capture trên host đôi khi hiển thị segment lớn hoặc pattern khác wire thực tế.

Các khái niệm:

- TSO: TCP Segmentation Offload;
- GSO: Generic Segmentation Offload;
- GRO: Generic Receive Offload.

Kiểm tra:

```bash
ethtool -k eth0
```

Khi phân tích packet capture, cần biết offloading có thể làm cách nhìn trên host khác packet vật lý.

## Throughput của một TCP connection

Throughput đơn connection phụ thuộc nhiều yếu tố:

```text
RTT
loss rate
congestion algorithm
receiver window
socket buffers
application read/write rate
path bandwidth
queueing
CPU/kernel processing
```

Vì vậy “link 10 Gbps” không có nghĩa một connection luôn đạt 10 Gbps.

## Nhiều connection có thể che giới hạn một connection

Nếu một connection bị giới hạn bởi window/RTT, chạy nhiều connection song song có thể tăng aggregate throughput. Đây là lý do một số transfer tool dùng parallel streams.

Nhưng nhiều connection cũng có thể cạnh tranh unfair với traffic khác và tăng load server.

## Cách đo thực tế

`iperf3` thường được dùng để tách network throughput khỏi HTTP/application logic:

```bash
iperf3 -s
iperf3 -c <server>
```

Nếu `iperf3` đạt throughput tốt nhưng API vẫn chậm, bottleneck có khả năng ở application/proxy/dependency thay vì raw network capacity.

Nếu `iperf3` cũng kém, cần tiếp tục kiểm tra path, loss, RTT, queue và host networking.

## Mô hình tư duy

TCP là một vòng điều khiển phản hồi (feedback control loop):

```text
sender gửi
   ↓
network phản hồi bằng ACK/loss/delay/ECN
   ↓
sender cập nhật mô hình/cửa sổ
   ↓
điều chỉnh tốc độ gửi
```

Không nên coi TCP chỉ là “socket đáng tin cậy”. Nó là hệ thống thích nghi liên tục với trạng thái path.

## Những hiểu lầm phổ biến

**“Bandwidth cao thì TCP phải nhanh.”** RTT, loss và cửa sổ quyết định lượng data in-flight.

**“Không packet loss nghĩa mạng tốt.”** Bufferbloat có thể tạo latency rất cao mà gần như không drop.

**“Tăng socket buffer luôn cải thiện throughput.”** Buffer quá lớn có thể tốn RAM và tăng queue latency.

**“Nhiều `TIME_WAIT` nghĩa TCP bị lỗi.”** Thường đó là hệ quả bình thường của connection lifecycle; cần nhìn rate và architecture connection reuse.

**“BBR luôn tốt hơn CUBIC.”** Hiệu quả phụ thuộc workload, kernel và network path.

## Kết nối kiến thức

Đọc cùng [TCP, HTTP và TLS](./tcp_http_tls.md), [IP routing/NAT/conntrack](./ip_routing_nat_conntrack.md) và [reverse proxy/load balancing](./reverse_proxy_load_balancing.md). Với backend Java, connection pool, retry, timeout và request latency đều chịu ảnh hưởng từ transport behavior bên dưới.