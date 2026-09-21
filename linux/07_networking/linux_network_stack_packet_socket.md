# Linux network stack: từ packet tới socket

Các chapter networking trước đã giải thích DNS, routing, TCP, TLS và load balancing. Chương này đi sâu vào nền tảng bên trong host Linux: **một packet đi qua NIC, driver, softirq, network stack, routing, firewall và cuối cùng tới socket của process như thế nào; chiều gửi đi diễn ra theo hướng ngược ra sao; và vì sao application có thể chậm dù CPU user-space không cao**.

Mục tiêu là nối các lớp thường bị học rời rạc thành một packet path thống nhất.

## Network stack là một pipeline nhiều lớp

Một request HTTP đến server không nhảy trực tiếp từ dây mạng vào Java method.

Một đường đi khái niệm:

```text
NIC
 ↓
DMA / driver receive queue
 ↓
interrupt / NAPI / softirq
 ↓
Linux network stack
 ↓
Ethernet / IP processing
 ↓
netfilter / routing
 ↓
TCP
 ↓
socket receive queue
 ↓
process read()/recv()
 ↓
application protocol
```

Mỗi lớp có queue, state và failure mode riêng.

## NIC nhận packet thế nào?

Network Interface Card (NIC) nhận frame từ network medium rồi đưa dữ liệu vào memory thông qua DMA theo cơ chế driver/hardware tương ứng.

CPU không copy từng byte trực tiếp từ dây mạng bằng một vòng lặp user-space.

Driver quản lý descriptor ring giữa NIC và kernel memory. NIC có thể ghi packet vào buffer rồi báo cho CPU rằng có công việc mới.

Xem nền tảng interrupt/DMA tại [Interrupt, softirq và device model](../00_foundations/interrupts_softirq_device_model.md).

## Receive ring

NIC thường có **receive descriptor ring**. Driver cung cấp buffer cho NIC, NIC điền packet vào rồi cập nhật trạng thái descriptor.

Nếu kernel không xử lý kịp và ring đầy, packet có thể bị drop ngay ở lớp rất thấp.

Điều này giải thích một failure mode quan trọng:

> Application chưa hề thấy request nhưng host vẫn có thể drop traffic vì receive path bị quá tải.

## Interrupt moderation

Nếu NIC tạo interrupt cho từng packet ở tốc độ hàng triệu packet/s, CPU có thể tốn quá nhiều thời gian chỉ xử lý interrupt.

Hardware/driver có thể dùng **interrupt coalescing/moderation**: gom nhiều packet rồi báo CPU ít lần hơn.

Đánh đổi:

```text
interrupt ít hơn
→ overhead thấp hơn
→ throughput tốt hơn
→ nhưng có thể thêm một ít latency
```

Vì vậy tuning network luôn có trade-off latency/throughput.

## NAPI

Linux dùng **NAPI** cho nhiều network driver để tránh interrupt storm.

Ý tưởng khái niệm:

1. NIC báo có packet;
2. driver tạm giảm phụ thuộc interrupt liên tục;
3. kernel poll một batch packet;
4. khi queue đã xử lý ổn, quay lại chế độ interrupt bình thường.

NAPI giúp hệ thống xử lý burst traffic hiệu quả hơn.

## Softirq và `NET_RX`

Phần lớn packet processing không nên thực hiện toàn bộ trong hard interrupt handler vì hard IRQ cần ngắn.

Linux đẩy nhiều công việc network xuống **softirq**, đặc biệt `NET_RX` cho receive path và `NET_TX` cho transmit-related work.

Quan sát:

```bash
cat /proc/softirqs
```

Nếu `NET_RX` tăng mạnh và CPU `si` cao, host có thể đang dành đáng kể CPU cho network packet processing.

## `ksoftirqd`

Nếu softirq work quá nhiều để xử lý inline, kernel thread như `ksoftirqd/<cpu>` có thể tiếp nhận công việc.

Nếu `ksoftirqd` dùng CPU cao, không nên kết luận đây là process “gây lỗi”. Nó thường là triệu chứng host đang có lượng softirq work lớn.

Cần kiểm tra packet rate, drop, NIC queue và application traffic.

## RSS: phân phối packet qua nhiều CPU

**Receive Side Scaling (RSS)** cho phép NIC hash flow và phân phối packet vào nhiều receive queue/CPU.

Nếu mọi packet dồn vào một CPU, một core có thể thành bottleneck dù tổng CPU toàn máy chỉ 25%.

Quan sát per-CPU interrupt:

```bash
cat /proc/interrupts
```

Nếu một NIC queue chỉ tăng trên một CPU, cần hiểu RSS/IRQ affinity trước khi kết luận “máy còn nhiều CPU nên network không thể nghẽn”.

## RPS và RFS

Linux có software mechanism như **Receive Packet Steering (RPS)** và **Receive Flow Steering (RFS)** để phân phối receive processing khi hardware RSS không đủ hoặc để cải thiện locality.

Tuning các cơ chế này cần benchmark thực tế vì phân phối rộng hơn cũng tăng cross-CPU cache traffic.

## Packet trở thành `skb`

Trong Linux networking, một abstraction quan trọng là `sk_buff` hay thường gọi **skb**.

Không cần học toàn bộ field, nhưng nên hiểu skb là object kernel mang packet data và metadata qua nhiều lớp network stack.

Metadata có thể gồm:

- protocol;
- interface;
- headers;
- checksum state;
- routing state;
- references tới socket hoặc device tùy giai đoạn.

Một packet không chỉ là mảng byte; kernel phải giữ ngữ cảnh xử lý xung quanh nó.

## Ethernet layer

Nếu interface là Ethernet-like, kernel xử lý frame header và xác định protocol tầng trên như IPv4/IPv6.

MAC address có ý nghĩa trong local link. Khi packet phải đi qua router, MAC header thay đổi theo từng hop trong khi IP destination có thể giữ nguyên trừ NAT.

Đây là lý do không nên dùng MAC address để suy luận end-to-end Internet path.

## Neighbor table / ARP / NDP

Để gửi packet tới next hop trên local link, host cần ánh xạ IP next-hop sang link-layer address.

IPv4 thường dùng ARP; IPv6 dùng Neighbor Discovery.

Quan sát:

```bash
ip neigh
```

Nếu neighbor entry thất bại, routing table có thể đúng nhưng packet vẫn không rời host thành công.

## IP receive path

Sau khi xác định packet IPv4/IPv6, kernel kiểm tra header, destination và policy cần thiết.

Nếu packet dành cho local host, nó đi tới **local input**.

Nếu host đóng vai router và forwarding được bật, packet có thể đi qua **forwarding path**.

Nếu packet do local process tạo, nó đi theo **local output path**.

Đây là ba đường logic khác nhau và firewall rule có thể áp dụng khác nhau.

## Routing không chỉ dành cho packet gửi ra ngoài

Kernel phải quyết định packet nhận vào có destination local hay cần forward. Routing data structure tham gia nhiều hơn người mới thường nghĩ.

Kiểm tra đường gửi:

```bash
ip route get <DESTINATION_IP>
```

Nhưng packet thực tế còn chịu policy routing, namespace và netfilter rules.

## Netfilter hooks

Linux có framework **netfilter** cho packet filtering/NAT.

Mental model đơn giản thường dùng các điểm:

```text
PREROUTING
INPUT
FORWARD
OUTPUT
POSTROUTING
```

Tên hook thể hiện vị trí tương đối trong packet path.

Packet tới local service thường liên quan PREROUTING → routing decision → INPUT.

Packet do local process gửi thường liên quan OUTPUT → POSTROUTING.

Packet được host forward đi qua FORWARD.

Không nên coi đây là thứ tự tuyệt đối cho mọi subsystem/detail, nhưng mental model này rất hữu ích khi đọc nftables/iptables.

## nftables và iptables

`iptables` là giao diện lịch sử phổ biến. Hệ thống hiện đại thường dùng nftables hoặc iptables frontend trên nft backend tùy distribution.

Quan sát:

```bash
sudo nft list ruleset
```

Khi troubleshooting, điều quan trọng là biết **policy thật đang được quản lý ở đâu**. Không nên thêm rule tạm một cách ngẫu nhiên rồi để configuration drift.

## Conntrack

**Connection tracking (conntrack)** giữ state flow để firewall/NAT hiểu packet thuộc connection nào.

Ví dụ trạng thái logic:

```text
NEW
ESTABLISHED
RELATED
```

Conntrack không phải TCP state machine đầy đủ, nhưng có liên hệ với flow state.

Nếu conntrack table đầy, connection mới có thể thất bại dù application và listener hoàn toàn khỏe.

Xem [IP routing, NAT và conntrack](./ip_routing_nat_conntrack.md).

## TCP demultiplexing tới socket

Khi IP layer xác định packet TCP dành cho local host, TCP stack phải tìm socket phù hợp dựa trên tuple như:

```text
source IP
source port
destination IP
destination port
protocol
```

Một listening socket trên `0.0.0.0:8080` có semantics khác socket bind một IP cụ thể.

Kernel dùng các table/hash structure để tìm đúng socket hiệu quả.

## SYN tới listening socket

Khi client gửi SYN:

```text
client SYN
   ↓
server TCP stack
   ↓
listening socket
   ↓
SYN queue / handshake state
   ↓
connection established
   ↓
accept queue
   ↓
application accept()
```

Có hai khái niệm queue dễ bị gộp:

- trạng thái connection đang handshake;
- connection đã established chờ application `accept()`.

Nếu application accept quá chậm hoặc backlog quá nhỏ, connection có thể gặp failure dù process vẫn LISTEN.

## `listen(backlog)`

Application gọi `listen()` với backlog. Kernel còn có các limit hệ thống.

Quan sát một số setting:

```bash
sysctl net.core.somaxconn
sysctl net.ipv4.tcp_max_syn_backlog
```

Không nên tăng các giá trị theo công thức internet mà không xác định queue nào đang bão hòa.

## SYN flood và SYN cookies

Kẻ tấn công hoặc traffic bất thường có thể gửi nhiều SYN làm state handshake tăng mạnh.

Linux có cơ chế như SYN cookies trong tình huống phù hợp để giảm resource cần giữ cho half-open connection.

```bash
sysctl net.ipv4.tcp_syncookies
```

Đây là protection mechanism, không phải cách giải quyết mọi connection overload.

## Established socket và receive queue

Sau handshake, TCP nhận data, sắp xếp sequence, xử lý retransmission/ACK rồi đưa payload vào receive buffer của socket.

Application gọi:

```text
read()
recv()
```

để lấy dữ liệu.

Nếu application xử lý chậm, receive queue có thể tăng. TCP flow control sẽ phản ánh khả năng nhận của receiver thông qua receive window.

## Socket buffer

Mỗi socket có send/receive buffering theo policy autotuning và giới hạn hệ thống.

Quan sát:

```bash
ss -tin
```

`ss` có thể cho nhiều thông tin TCP như queue, RTT, congestion control tùy option/kernel.

Không nên tăng socket buffer chỉ vì “network nhanh”. Buffer quá lớn có thể làm latency tăng do queueing.

## Backpressure bắt đầu từ kernel nhưng lan lên application

Nếu application không đọc socket đủ nhanh:

```text
application chậm
→ receive buffer đầy dần
→ advertised window giảm
→ sender chậm lại
```

Đây là backpressure tự nhiên của TCP.

Nếu application/framework thêm queue lớn phía trên, data có thể tiếp tục tích tụ ở user-space và tăng latency/memory thay vì tạo backpressure sớm.

## `CLOSE_WAIT`

Khi peer đã đóng connection và kernel báo EOF cho application, local application phải đóng socket của mình.

Nếu application quên close, socket có thể nằm `CLOSE-WAIT` lâu.

Nhiều `CLOSE-WAIT` thường là dấu hiệu lifecycle ở application, không phải TCP kernel tự quên đóng.

## `TIME_WAIT`

`TIME-WAIT` thường xuất hiện ở phía chủ động đóng connection để bảo vệ TCP semantics với segment cũ.

Nhiều `TIME-WAIT` không tự động là leak.

Cần xem connection churn, ephemeral port range, reuse pattern và connection pooling.

Xem [TCP congestion control](./tcp_congestion_control.md).

## Send path từ application xuống NIC

Chiều gửi khái niệm:

```text
application send()/write()
 ↓
socket send buffer
 ↓
TCP segmentation/state
 ↓
IP routing
 ↓
netfilter
 ↓
qdisc
 ↓
driver transmit queue
 ↓
NIC
```

Một lần `write()` lớn không nhất thiết tạo một Ethernet frame duy nhất. TCP/IP stack và offload có thể chia/gộp công việc.

## qdisc

**Queueing discipline (qdisc)** quản lý queue packet ở tầng transmit trong Linux.

Quan sát:

```bash
tc qdisc show
```

Qdisc ảnh hưởng queueing, shaping và latency.

Các thuật toán như fq, fq_codel có thể giúp kiểm soát queue/bufferbloat trong một số môi trường.

## TSO, GSO, GRO

Để giảm CPU overhead, Linux/NIC có các offload:

- **TSO (TCP Segmentation Offload)**;
- **GSO (Generic Segmentation Offload)**;
- **GRO (Generic Receive Offload)**.

Ý tưởng là xử lý logical packet lớn hơn ở một số layer rồi để hardware/kernel chia/gộp tối ưu.

Vì vậy packet capture trên host có thể nhìn packet size khác với packet thực đi trên wire ở từng thời điểm.

Đây là điều cần nhớ khi đọc tcpdump/Wireshark.

## Checksum offload

NIC có thể tính checksum. Packet capture trước khi NIC hoàn tất offload có thể hiển thị checksum “incorrect” dù packet trên wire hoàn toàn đúng.

Đây là một trap phổ biến khi phân tích pcap trên sending host.

## MTU

**Maximum Transmission Unit (MTU)** giới hạn kích thước packet layer 3 trên link.

```bash
ip link show
```

Nếu path có MTU nhỏ hơn nhưng discovery bị chặn, connection có thể handshake được nhưng payload lớn bị treo — một failure mode khó chịu gọi gần với PMTU black hole.

## MSS

TCP **Maximum Segment Size (MSS)** thường được đàm phán dựa trên MTU để tránh tạo IP packet quá lớn.

MTU và MSS liên quan nhưng không giống nhau.

## Fragmentation

IPv4 có cơ chế fragmentation trong điều kiện nhất định. IPv6 thay đổi semantics so với IPv4.

Trong production hiện đại thường muốn tránh fragmentation không cần thiết vì tăng complexity và failure surface.

Tunnels/VPN/container overlay làm effective MTU càng quan trọng vì encapsulation thêm header.

## Network namespace

Mỗi network namespace có thể có:

- interfaces;
- routing table;
- firewall state;
- sockets;
- sysctl network-related nhất định.

Container network vì vậy không phải chỉ là “port mapping”. Container nhìn một network stack namespace riêng nhưng dùng cùng kernel.

Quan sát:

```bash
ip netns list
```

Container runtime có thể quản lý namespace theo cách không hiện trực tiếp dưới `ip netns`, nhưng khái niệm vẫn tương tự.

## veth pair

**veth** giống một cặp virtual Ethernet cable:

```text
vethA <======> vethB
```

Packet đi vào một đầu xuất hiện ở đầu kia.

Container thường có một đầu veth trong container namespace, đầu kia nối bridge hoặc host networking.

Điều này giúp giải thích packet path Docker/Kubernetes cơ bản.

## Linux bridge

Bridge chuyển frame giữa interface ở layer 2 tương tự switch phần mềm.

```bash
bridge link
bridge fdb show
```

Docker bridge networking dùng khái niệm này cùng veth, routing/NAT tùy mode.

## Loopback đặc biệt thế nào?

Traffic tới `127.0.0.1` không đi qua physical NIC. Nó vẫn sử dụng network stack nhưng loopback device xử lý cục bộ.

Do đó:

```bash
curl localhost
```

thành công chỉ chứng minh application + local stack path, không chứng minh NIC, external routing hay firewall ngoài host.

## Packet drop có thể xảy ra ở nhiều lớp

Một packet có thể bị drop vì:

- NIC ring full;
- driver issue;
- softirq backlog;
- firewall;
- routing policy;
- conntrack full;
- TCP state invalid;
- socket queue pressure;
- application không accept đủ nhanh.

Vì vậy metric “packet loss” cần xác định loss ở đâu.

## Quan sát interface counters

```bash
ip -s link
```

Xem RX/TX packets, errors, dropped.

Chi tiết driver:

```bash
ethtool -S <interface>
```

Tên counter phụ thuộc driver/NIC.

Nếu `ip -s link` drop tăng, đó là bằng chứng gần host hơn application log.

## `netstat -s` / `ss -s`

Thống kê protocol:

```bash
ss -s
netstat -s 2>/dev/null
```

Có thể cung cấp retransmission, failed connection, reset và nhiều counter TCP/IP tùy system.

Không đọc một counter tuyệt đối đơn lẻ. Hãy lấy rate theo thời gian và so với traffic volume.

## `/proc/net`

Kernel expose nhiều networking state qua `/proc/net` hoặc netlink interfaces.

Các công cụ hiện đại như `ss`, `ip` dùng netlink thay vì yêu cầu người dùng parse file proc trực tiếp.

Mental model quan trọng: command là client của kernel state, không phải nguồn chân lý độc lập.

## Netlink

**Netlink** là cơ chế IPC giữa user space và kernel rất quan trọng cho networking.

`ip`, `ss`, routing daemon, container runtime dùng netlink để query/change network state.

Đây là lý do bộ công cụ `iproute2` có thể thao tác interface, route, neighbor và namespace theo cách nhất quán.

## `tcpdump` bắt packet ở đâu?

`tcpdump` dùng packet socket/capture mechanism để quan sát packet qua interface.

Ví dụ:

```bash
sudo tcpdump -ni any host 10.0.0.20 and port 443
```

Nếu client gửi SYN nhưng server host không thấy, lỗi nằm trước capture point đó.

Nếu host thấy SYN và SYN-ACK nhưng client không nhận, cần nhìn return path/firewall/network.

Nếu handshake hoàn tất nhưng application timeout, đi lên socket/application layer.

## Packet capture không chứng minh application đã đọc dữ liệu

Thấy packet tới interface chỉ chứng minh traffic đã tới capture point.

Packet vẫn có thể bị firewall drop hoặc TCP stack reject trước khi socket nhận.

Tương tự, packet tới socket buffer chưa có nghĩa application thread đã `read()`.

Cần phân biệt các layer evidence.

## CPU softirq saturation

Một host có thể có:

```text
tổng CPU 40%
nhưng CPU 3 = 100% softirq
```

Nếu flow/RSS tập trung vào CPU 3, network throughput/latency có thể bottleneck dù average CPU thấp.

Do đó khi phân tích network-intensive workload nên nhìn per-CPU utilization.

```bash
mpstat -P ALL 1
```

## NUMA và NIC locality

Trên server nhiều NUMA node, NIC nằm gần một CPU/socket nhất định. Nếu interrupt xử lý ở NUMA node khác và application memory ở nơi xa, cross-NUMA traffic có thể tăng latency.

Đây là optimization sâu chỉ cần khi có evidence. Không nên pin IRQ/application theo cảm tính.

## XDP và eBPF ở receive path

**XDP (eXpress Data Path)** cho phép eBPF program xử lý packet rất sớm trong receive path ở nhiều driver.

Use case:

- packet filtering;
- DDoS mitigation;
- load balancing;
- observability.

Ưu điểm là tránh đưa packet không cần thiết qua toàn bộ network stack.

Nhưng XDP/eBPF tăng complexity và yêu cầu hiểu safety/verifier/tooling.

## Socket API là abstraction cuối cùng cho application

Application không cần biết skb, qdisc hay NIC ring trong code thông thường. Nó thấy:

```text
socket()
bind()
listen()
accept()
connect()
read()/recv()
write()/send()
close()
```

Socket là ranh giới API cho phép network stack phức tạp phía dưới được ẩn đi.

Đây là Unix abstraction rất mạnh: network communication cuối cùng được process thao tác thông qua file descriptor-like handle.

## Blocking socket

Với blocking I/O, nếu `read()` chưa có dữ liệu, thread có thể sleep trên wait queue.

Khi packet tới và socket trở nên readable, kernel wake task.

Đây là nối trực tiếp:

```text
NIC interrupt
→ softirq
→ TCP receive
→ socket readable
→ wake task
→ scheduler
→ thread chạy
```

Toàn bộ chuỗi giải thích latency từ packet đến application.

## Non-blocking socket và `epoll`

Với non-blocking mode, `read()` có thể trả `EAGAIN` nếu chưa có dữ liệu.

Application dùng `epoll` để chờ nhiều file descriptor có event mà không cần một thread block riêng trên mỗi socket.

```text
many sockets
    ↓
epoll interest set
    ↓
kernel báo ready fd
    ↓
application xử lý batch event
```

Đây là nền tảng của event-driven server như Nginx/Netty.

## Edge-triggered và level-triggered

`epoll` có các mode khác nhau. Với edge-triggered, application thường phải drain socket tới `EAGAIN`, nếu không có thể bỏ lỡ cơ hội xử lý tiếp theo theo logic event.

Không cần dùng edge-triggered để có hiệu năng tốt trong mọi trường hợp. Correctness quan trọng hơn micro-optimization.

## Java NIO và Linux epoll

Trên Linux, Java NIO selector implementation có thể sử dụng epoll tùy JDK/runtime.

Netty cũng khai thác epoll/native transport trong môi trường phù hợp.

Vì vậy khái niệm Selector ở Java không phải abstraction tách rời OS; bên dưới nó có thể nối trực tiếp với Linux event notification.

## `SO_REUSEADDR` và `SO_REUSEPORT`

Socket option này giải quyết các vấn đề khác nhau về bind/reuse tùy protocol/platform.

`SO_REUSEPORT` có thể cho nhiều listening socket bind cùng endpoint với load distribution của kernel trong use case phù hợp.

Không nên copy option mà không hiểu semantics vì khác biệt platform có thể quan trọng.

## Connection refused ở stack nào?

Nếu SYN tới host nhưng không có listener, kernel có thể trả RST. Client thấy `ECONNREFUSED`.

Điều này nghĩa failure có thể xảy ra hoàn toàn trong kernel trước khi application code đích được chạy.

## Timeout có thể do drop im lặng

Nếu firewall DROP packet thay vì REJECT, client có thể retransmit cho tới timeout.

Cùng một “không kết nối được” nhưng symptom khác:

```text
RST/REJECT → lỗi nhanh
DROP       → timeout lâu hơn
```

Đây là lý do latency của failure chứa thông tin chẩn đoán.

## Mental Model

Một request network đi qua một chuỗi queue và state machine:

```text
wire
→ NIC ring
→ CPU/softirq
→ packet object
→ IP/routing/firewall
→ TCP state
→ socket buffer
→ wait queue/epoll
→ thread/event loop
→ application
```

Khi latency hoặc drop xảy ra, hãy hỏi **queue nào đang đầy, state machine nào chưa tiến triển, và evidence ở lớp nào chứng minh packet đã đi tới đó**.

## Những hiểu lầm phổ biến

**“Packet tới NIC nghĩa là application đã nhận.”** Còn nhiều lớp kernel ở giữa.

**“CPU tổng chưa cao nên network không thể nghẽn.”** Một softirq CPU hoặc NIC queue có thể bão hòa cục bộ.

**“Listener tồn tại nghĩa là accept không thể nghẽn.”** Accept queue/backlog và application scheduling vẫn có thể bottleneck.

**“tcpdump thấy checksum bad nghĩa packet thật bị lỗi.”** Offload có thể làm capture trước bước checksum hardware.

**“Loopback test thành công chứng minh đường mạng ngoài host khỏe.”** Loopback bỏ qua NIC và nhiều lớp bên ngoài.

**“TIME_WAIT là connection leak.”** Nó thường là state TCP bình thường sau active close.

## Knowledge Connection

Đọc tiếp theo hướng:

- [Interrupt/softirq/device model](../00_foundations/interrupts_softirq_device_model.md) — packet vào CPU thế nào;
- [IP routing/NAT/conntrack](./ip_routing_nat_conntrack.md) — packet chọn đường và policy;
- [TCP/HTTP/TLS](./tcp_http_tls.md) — transport/application state;
- [TCP congestion control](./tcp_congestion_control.md) — behavior khi network có capacity/queue/loss;
- [IPC và epoll](../04_process/interprocess_communication.md) — socket readiness và event-driven I/O;
- [Scheduler](../06_resources/kernel_scheduler_deep_dive.md) — task được wake rồi khi nào thực sự chạy;
- [Tracing](../09_production/observability_tracing_strace_perf.md) — đo packet/socket/off-CPU path trong production.
