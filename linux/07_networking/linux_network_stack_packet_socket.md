# Linux mạng (network / 네트워크) ngăn xếp (stack / 스택): từ packet tới socket

> **Mạch đọc:** Đọc **Linux mạng (network / 네트워크) ngăn xếp (stack / 스택): từ packet tới socket** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **mạng (network / 네트워크) ngăn xếp (stack / 스택) là một chuỗi xử lý (pipeline / 파이프라인) nhiều lớp** sang **NIC nhận packet thế nào?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Các chapter networking trước đã giải thích DNS, routing, TCP, TLS và tải (load / 로드) balancing. Chương này đi sâu vào nền tảng bên trong host Linux: **một packet đi qua NIC, driver, softirq, mạng (network / 네트워크) ngăn xếp (stack / 스택), routing, firewall và cuối cùng tới socket của tiến trình (process / 프로세스) như thế nào; chiều gửi đi diễn ra theo hướng ngược ra sao; và vì sao ứng dụng (application / 애플리케이션) có thể chậm dù CPU user-space không cao**.

Mục tiêu là nối các lớp thường bị học rời rạc thành một packet đường dẫn (path / 경로) thống nhất.

## Mạng (network / 네트워크) ngăn xếp (stack / 스택) là một chuỗi xử lý (pipeline / 파이프라인) nhiều lớp

Một yêu cầu (request / 요청) HTTP đến máy chủ (server / 서버) không nhảy trực tiếp từ dây mạng vào Java phương thức (method / 메서드).

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

Mỗi lớp có hàng đợi (queue / 큐), trạng thái (state / 상태) và dạng thất bại (failure mode / 실패 모드) riêng.

## NIC nhận packet thế nào?

Mạng (network / 네트워크) giao diện (interface / 인터페이스) Card (NIC) nhận frame từ mạng (network / 네트워크) medium rồi đưa dữ liệu vào bộ nhớ (memory / 메모리) thông qua DMA theo cơ chế driver/hardware tương ứng.

CPU không bản sao (copy / 복사) từng byte trực tiếp từ dây mạng bằng một vòng lặp user-space.

Driver quản lý descriptor ring giữa NIC và kernel bộ nhớ (memory / 메모리). NIC có thể ghi packet vào buffer rồi báo cho CPU rằng có công việc mới.

Xem nền tảng interrupt/DMA tại [Interrupt, softirq và device model](../00_foundations/interrupts_softirq_device_model.md).

## Receive ring

NIC thường có **receive descriptor ring**. Driver cung cấp buffer cho NIC, NIC điền packet vào rồi cập nhật trạng thái descriptor.

Nếu kernel không xử lý kịp và ring đầy, packet có thể bị drop ngay ở lớp rất thấp.

Điều này giải thích một dạng thất bại (failure mode / 실패 모드) quan trọng:

> ứng dụng (application / 애플리케이션) chưa hề thấy yêu cầu (request / 요청) nhưng host vẫn có thể drop traffic vì receive đường dẫn (path / 경로) bị quá tải.

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

Vì vậy tuning mạng (network / 네트워크) luôn có sự đánh đổi (trade-off / 트레이드오프) độ trễ (latency / 지연 시간)/thông lượng (throughput / 처리량).

## NAPI

Linux dùng **NAPI** cho nhiều mạng (network / 네트워크) driver để tránh interrupt storm.

Ý tưởng khái niệm:

1. NIC báo có packet;
2. driver tạm giảm phụ thuộc interrupt liên tục;
3. kernel poll một batch packet;
4. khi hàng đợi (queue / 큐) đã xử lý ổn, quay lại chế độ interrupt bình thường.

NAPI giúp hệ thống xử lý burst traffic hiệu quả hơn.

## Softirq và `NET_RX`

Phần lớn packet processing không nên thực hiện toàn bộ trong hard interrupt handler vì hard IRQ cần ngắn.

Linux đẩy nhiều công việc mạng (network / 네트워크) xuống **softirq**, đặc biệt `NET_RX` cho receive đường dẫn (path / 경로) và `NET_TX` cho transmit-related công việc (work / 작업).

Quan sát:

```bash
cat /proc/softirqs
```

Nếu `NET_RX` tăng mạnh và CPU `si` cao, host có thể đang dành đáng kể CPU cho mạng (network / 네트워크) packet processing.

## `ksoftirqd`

Nếu softirq công việc (work / 작업) quá nhiều để xử lý inline, kernel luồng thực thi (thread / 스레드) như `ksoftirqd/<cpu>` có thể tiếp nhận công việc.

Nếu `ksoftirqd` dùng CPU cao, không nên kết luận đây là tiến trình (process / 프로세스) “gây lỗi”. Nó thường là triệu chứng host đang có lượng softirq công việc (work / 작업) lớn.

Cần kiểm tra packet tỷ lệ (rate / 비율), drop, NIC hàng đợi (queue / 큐) và ứng dụng (application / 애플리케이션) traffic.

## RSS: phân phối packet qua nhiều CPU

**Receive Side Scaling (RSS)** cho phép NIC băm (hash / 해시) luồng (flow / 흐름) và phân phối packet vào nhiều receive hàng đợi (queue / 큐)/CPU.

Nếu mọi packet dồn vào một CPU, một cốt lõi (core / 핵심) có thể thành bottleneck dù tổng CPU toàn máy chỉ 25%.

Quan sát per-CPU interrupt:

```bash
cat /proc/interrupts
```

Nếu một NIC hàng đợi (queue / 큐) chỉ tăng trên một CPU, cần hiểu RSS/IRQ affinity trước khi kết luận “máy còn nhiều CPU nên mạng (network / 네트워크) không thể nghẽn”.

## RPS và RFS

Linux có software cơ chế (mechanism / 메커니즘) như **Receive Packet Steering (RPS)** và **Receive luồng (flow / 흐름) Steering (RFS)** để phân phối receive processing khi hardware RSS không đủ hoặc để cải thiện locality.

Tuning các cơ chế này cần benchmark thực tế vì phân phối rộng hơn cũng tăng cross-CPU bộ nhớ đệm (cache / 캐시) traffic.

## Packet trở thành `skb`

Trong Linux networking, một lớp trừu tượng (abstraction / 추상화) quan trọng là `sk_buff` hay thường gọi **skb**.

Không cần học toàn bộ trường dữ liệu (field / 필드), nhưng nên hiểu skb là đối tượng (object / 객체) kernel mang packet dữ liệu (data / 데이터) và siêu dữ liệu (metadata / 메타데이터) qua nhiều lớp mạng (network / 네트워크) ngăn xếp (stack / 스택).

Siêu dữ liệu (metadata / 메타데이터) có thể gồm:

- giao thức (protocol / 프로토콜);
- giao diện (interface / 인터페이스);
- headers;
- checksum trạng thái (state / 상태);
- routing trạng thái (state / 상태);
- references tới socket hoặc thiết bị (device / 장치) tùy giai đoạn.

Một packet không chỉ là mảng byte; kernel phải giữ ngữ cảnh xử lý xung quanh nó.

## Ethernet tầng (layer / 계층)

Nếu giao diện (interface / 인터페이스) là Ethernet-like, kernel xử lý frame header và xác định giao thức (protocol / 프로토콜) tầng trên như IPv4/IPv6.

MAC address có ý nghĩa trong cục bộ (local / 로컬) link. Khi packet phải đi qua router, MAC header thay đổi theo từng hop trong khi IP destination có thể giữ nguyên trừ NAT.

Đây là lý do không nên dùng MAC address để suy luận end-to-end Internet đường dẫn (path / 경로).

## Neighbor bảng (table / 테이블) / ARP / NDP

Để gửi packet tới next hop trên cục bộ (local / 로컬) link, host cần ánh xạ IP next-hop sang link-layer address.

IPv4 thường dùng ARP; IPv6 dùng Neighbor Discovery.

Quan sát:

```bash
ip neigh
```

Nếu neighbor entry thất bại, routing bảng (table / 테이블) có thể đúng nhưng packet vẫn không rời host thành công.

## IP receive đường dẫn (path / 경로)

Sau khi xác định packet IPv4/IPv6, kernel kiểm tra header, destination và chính sách (policy / 정책) cần thiết.

Nếu packet dành cho cục bộ (local / 로컬) host, nó đi tới **cục bộ (local / 로컬) đầu vào (input / 입력)**.

Nếu host đóng vai router và forwarding được bật, packet có thể đi qua **forwarding đường dẫn (path / 경로)**.

Nếu packet do cục bộ (local / 로컬) tiến trình (process / 프로세스) tạo, nó đi theo **cục bộ (local / 로컬) đầu ra (output / 출력) đường dẫn (path / 경로)**.

Đây là ba đường lô-gic (logic / 논리) khác nhau và firewall quy tắc (rule / 규칙) có thể áp dụng khác nhau.

## Routing không chỉ dành cho packet gửi ra ngoài

Kernel phải quyết định packet nhận vào có destination cục bộ (local / 로컬) hay cần forward. Routing cấu trúc dữ liệu (data structure / 자료구조) tham gia nhiều hơn người mới thường nghĩ.

Kiểm tra đường gửi:

```bash
ip route get <DESTINATION_IP>
```

Nhưng packet thực tế còn chịu chính sách (policy / 정책) routing, không gian tên (namespace / 네임스페이스) và netfilter rules.

## Netfilter hooks

Linux có khung phần mềm (framework / 프레임워크) **netfilter** cho packet filtering/NAT.

Mô hình tư duy (mental model / 사고 모델) đơn giản thường dùng các điểm:

```text
PREROUTING
INPUT
FORWARD
OUTPUT
POSTROUTING
```

Tên hook thể hiện vị trí tương đối trong packet đường dẫn (path / 경로).

Packet tới cục bộ (local / 로컬) dịch vụ (service / 서비스) thường liên quan PREROUTING → routing quyết định (decision / 결정) → đầu vào (input / 입력).

Packet do cục bộ (local / 로컬) tiến trình (process / 프로세스) gửi thường liên quan đầu ra (output / 출력) → POSTROUTING.

Packet được host forward đi qua FORWARD.

Không nên coi đây là thứ tự tuyệt đối cho mọi subsystem/detail, nhưng mô hình tư duy (mental model / 사고 모델) này rất hữu ích khi đọc nftables/iptables.

## nftables và iptables

`iptables` là giao diện lịch sử phổ biến. Hệ thống hiện đại thường dùng nftables hoặc iptables frontend trên nft backend tùy phân phối (distribution / 분포).

Quan sát:

```bash
sudo nft list ruleset
```

Khi troubleshooting, điều quan trọng là biết **chính sách (policy / 정책) thật đang được quản lý ở đâu**. Không nên thêm quy tắc (rule / 규칙) tạm một cách ngẫu nhiên rồi để cấu hình (configuration / 구성) drift.

## Conntrack

**liên kết (connection / 연결) tracking (conntrack)** giữ trạng thái (state / 상태) luồng (flow / 흐름) để firewall/NAT hiểu packet thuộc liên kết (connection / 연결) nào.

Ví dụ trạng thái lô-gic (logic / 논리):

```text
NEW
ESTABLISHED
RELATED
```

Conntrack không phải TCP máy trạng thái (state machine / 상태 머신) đầy đủ, nhưng có liên hệ với luồng (flow / 흐름) trạng thái (state / 상태).

Nếu conntrack bảng (table / 테이블) đầy, liên kết (connection / 연결) mới có thể thất bại dù ứng dụng (application / 애플리케이션) và listener hoàn toàn khỏe.

Xem [IP routing, NAT và conntrack](./ip_routing_nat_conntrack.md).

## TCP demultiplexing tới socket

Khi IP tầng (layer / 계층) xác định packet TCP dành cho cục bộ (local / 로컬) host, TCP ngăn xếp (stack / 스택) phải tìm socket phù hợp dựa trên tuple như:

```text
source IP
source port
destination IP
destination port
protocol
```

Một listening socket trên `0.0.0.0:8080` có ngữ nghĩa (semantics / 의미론) khác socket bind một IP cụ thể.

Kernel dùng các bảng (table / 테이블)/băm (hash / 해시) cấu trúc (structure / 구조) để tìm đúng socket hiệu quả.

## SYN tới listening socket

Khi máy khách (client / 클라이언트) gửi SYN:

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

Có hai khái niệm hàng đợi (queue / 큐) dễ bị gộp:

- trạng thái liên kết (connection / 연결) đang handshake;
- liên kết (connection / 연결) đã established chờ ứng dụng (application / 애플리케이션) `accept()`.

Nếu ứng dụng (application / 애플리케이션) accept quá chậm hoặc backlog quá nhỏ, liên kết (connection / 연결) có thể gặp thất bại (failure / 실패) dù tiến trình (process / 프로세스) vẫn LISTEN.

## `listen(backlog)`

Ứng dụng (application / 애플리케이션) gọi `listen()` với backlog. Kernel còn có các limit hệ thống.

Quan sát một số setting:

```bash
sysctl net.core.somaxconn
sysctl net.ipv4.tcp_max_syn_backlog
```

Không nên tăng các giá trị theo công thức internet mà không xác định hàng đợi (queue / 큐) nào đang bão hòa.

## SYN flood và SYN cookies

Kẻ tấn công hoặc traffic bất thường có thể gửi nhiều SYN làm trạng thái (state / 상태) handshake tăng mạnh.

Linux có cơ chế như SYN cookies trong tình huống phù hợp để giảm tài nguyên (resource / 자원) cần giữ cho half-open liên kết (connection / 연결).

```bash
sysctl net.ipv4.tcp_syncookies
```

Đây là protection cơ chế (mechanism / 메커니즘), không phải cách giải quyết mọi liên kết (connection / 연결) overload.

## Established socket và receive hàng đợi (queue / 큐)

Sau handshake, TCP nhận dữ liệu (data / 데이터), sắp xếp chuỗi (sequence / 시퀀스), xử lý retransmission/ACK rồi đưa payload vào receive buffer của socket.

Ứng dụng (application / 애플리케이션) gọi:

```text
read()
recv()
```

để lấy dữ liệu.

Nếu ứng dụng (application / 애플리케이션) xử lý chậm, receive hàng đợi (queue / 큐) có thể tăng. TCP luồng (flow / 흐름) điều khiển (control / 제어) sẽ phản ánh khả năng nhận của receiver thông qua receive cửa sổ (window / 윈도우).

## Socket buffer

Mỗi socket có send/receive buffering theo chính sách (policy / 정책) autotuning và giới hạn hệ thống.

Quan sát:

```bash
ss -tin
```

`ss` có thể cho nhiều thông tin TCP như hàng đợi (queue / 큐), RTT, congestion điều khiển (control / 제어) tùy option/kernel.

Không nên tăng socket buffer chỉ vì “mạng (network / 네트워크) nhanh”. Buffer quá lớn có thể làm độ trễ (latency / 지연 시간) tăng do queueing.

## Backpressure bắt đầu từ kernel nhưng lan lên ứng dụng (application / 애플리케이션)

Nếu ứng dụng (application / 애플리케이션) không đọc socket đủ nhanh:

```text
application chậm
→ receive buffer đầy dần
→ advertised window giảm
→ sender chậm lại
```

Đây là backpressure tự nhiên của TCP.

Nếu ứng dụng (application / 애플리케이션)/khung phần mềm (framework / 프레임워크) thêm hàng đợi (queue / 큐) lớn phía trên, dữ liệu (data / 데이터) có thể tiếp tục tích tụ ở user-space và tăng độ trễ (latency / 지연 시간)/bộ nhớ (memory / 메모리) thay vì tạo backpressure sớm.

## `CLOSE_WAIT`

Khi peer đã đóng liên kết (connection / 연결) và kernel báo EOF cho ứng dụng (application / 애플리케이션), cục bộ (local / 로컬) ứng dụng (application / 애플리케이션) phải đóng socket của mình.

Nếu ứng dụng (application / 애플리케이션) quên close, socket có thể nằm `CLOSE-WAIT` lâu.

Nhiều `CLOSE-WAIT` thường là dấu hiệu vòng đời (lifecycle / 생명주기) ở ứng dụng (application / 애플리케이션), không phải TCP kernel tự quên đóng.

## `TIME_WAIT`

`TIME-WAIT` thường xuất hiện ở phía chủ động đóng liên kết (connection / 연결) để bảo vệ TCP ngữ nghĩa (semantics / 의미론) với segment cũ.

Nhiều `TIME-WAIT` không tự động là leak.

Cần xem liên kết (connection / 연결) churn, ephemeral cổng (port / 포트) phạm vi (range / 범위), reuse mẫu (pattern / 패턴) và liên kết (connection / 연결) pooling.

Xem [TCP congestion control](./tcp_congestion_control.md).

## Send đường dẫn (path / 경로) từ ứng dụng (application / 애플리케이션) xuống NIC

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

Một lần `write()` lớn không nhất thiết tạo một Ethernet frame duy nhất. TCP/IP ngăn xếp (stack / 스택) và offload có thể chia/gộp công việc.

## qdisc

**Queueing discipline (qdisc)** quản lý hàng đợi (queue / 큐) packet ở tầng transmit trong Linux.

Quan sát:

```bash
tc qdisc show
```

Qdisc ảnh hưởng queueing, shaping và độ trễ (latency / 지연 시간).

Các thuật toán như fq, fq_codel có thể giúp kiểm soát hàng đợi (queue / 큐)/bufferbloat trong một số môi trường.

## TSO, GSO, GRO

Để giảm CPU overhead, Linux/NIC có các offload:

- **TSO (TCP Segmentation Offload)**;
- **GSO (Generic Segmentation Offload)**;
- **GRO (Generic Receive Offload)**.

Ý tưởng là xử lý logical packet lớn hơn ở một số tầng (layer / 계층) rồi để hardware/kernel chia/gộp tối ưu.

Vì vậy packet capture trên host có thể nhìn packet kích thước (size / 크기) khác với packet thực đi trên wire ở từng thời điểm.

Đây là điều cần nhớ khi đọc tcpdump/Wireshark.

## Checksum offload

NIC có thể tính checksum. Packet capture trước khi NIC hoàn tất offload có thể hiển thị checksum “incorrect” dù packet trên wire hoàn toàn đúng.

Đây là một trap phổ biến khi phân tích pcap trên sending host.

## MTU

**Maximum Transmission đơn vị (unit / 단위) (MTU)** giới hạn kích thước packet tầng (layer / 계층) 3 trên link.

```bash
ip link show
```

Nếu đường dẫn (path / 경로) có MTU nhỏ hơn nhưng discovery bị chặn, liên kết (connection / 연결) có thể handshake được nhưng payload lớn bị treo — một dạng thất bại (failure mode / 실패 모드) khó chịu gọi gần với PMTU black hole.

## MSS

TCP **Maximum Segment kích thước (size / 크기) (MSS)** thường được đàm phán dựa trên MTU để tránh tạo IP packet quá lớn.

MTU và MSS liên quan nhưng không giống nhau.

## Fragmentation

IPv4 có cơ chế fragmentation trong điều kiện nhất định. IPv6 thay đổi ngữ nghĩa (semantics / 의미론) so với IPv4.

Trong môi trường vận hành (production / 운영 환경) hiện đại thường muốn tránh fragmentation không cần thiết vì tăng độ phức tạp (complexity / 복잡도) và thất bại (failure / 실패) surface.

Tunnels/VPN/bộ chứa (container / 컨테이너) overlay làm effective MTU càng quan trọng vì encapsulation thêm header.

## Mạng (network / 네트워크) không gian tên (namespace / 네임스페이스)

Mỗi mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) có thể có:

- interfaces;
- routing bảng (table / 테이블);
- firewall trạng thái (state / 상태);
- sockets;
- sysctl network-related nhất định.

Bộ chứa (container / 컨테이너) mạng (network / 네트워크) vì vậy không phải chỉ là “ánh xạ cổng (port mapping / 포트 매핑)”. bộ chứa (container / 컨테이너) nhìn một mạng (network / 네트워크) ngăn xếp (stack / 스택) không gian tên (namespace / 네임스페이스) riêng nhưng dùng cùng kernel.

Quan sát:

```bash
ip netns list
```

Bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) có thể quản lý không gian tên (namespace / 네임스페이스) theo cách không hiện trực tiếp dưới `ip netns`, nhưng khái niệm vẫn tương tự.

## veth pair

**veth** giống một cặp virtual Ethernet cable:

```text
vethA <======> vethB
```

Packet đi vào một đầu xuất hiện ở đầu kia.

Bộ chứa (container / 컨테이너) thường có một đầu veth trong bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스), đầu kia nối cầu nối (bridge / 브리지) hoặc host networking.

Điều này giúp giải thích packet đường dẫn (path / 경로) Docker/Kubernetes cơ bản.

## Linux cầu nối (bridge / 브리지)

Cầu nối (bridge / 브리지) chuyển frame giữa giao diện (interface / 인터페이스) ở tầng (layer / 계층) 2 tương tự switch phần mềm.

```bash
bridge link
bridge fdb show
```

Docker cầu nối (bridge / 브리지) networking dùng khái niệm này cùng veth, routing/NAT tùy chế độ (mode / 모드).

## Loopback đặc biệt thế nào?

Traffic tới `127.0.0.1` không đi qua vật lý (physical / 물리적) NIC. Nó vẫn sử dụng mạng (network / 네트워크) ngăn xếp (stack / 스택) nhưng loopback thiết bị (device / 장치) xử lý cục bộ.

Do đó:

```bash
curl localhost
```

thành công chỉ chứng minh ứng dụng (application / 애플리케이션) + cục bộ (local / 로컬) ngăn xếp (stack / 스택) đường dẫn (path / 경로), không chứng minh NIC, bên ngoài (external / 외부) routing hay firewall ngoài host.

## Packet drop có thể xảy ra ở nhiều lớp

Một packet có thể bị drop vì:

- NIC ring full;
- driver issue;
- softirq backlog;
- firewall;
- routing chính sách (policy / 정책);
- conntrack full;
- TCP trạng thái (state / 상태) invalid;
- socket hàng đợi (queue / 큐) pressure;
- ứng dụng (application / 애플리케이션) không accept đủ nhanh.

Vì vậy chỉ số (metric / 지표) “packet mất mát (loss / 손실)” cần xác định mất mát (loss / 손실) ở đâu.

## Quan sát giao diện (interface / 인터페이스) counters

```bash
ip -s link
```

Xem RX/TX packets, errors, dropped.

Chi tiết driver:

```bash
ethtool -S <interface>
```

Tên counter phụ thuộc driver/NIC.

Nếu `ip -s link` drop tăng, đó là bằng chứng gần host hơn ứng dụng (application / 애플리케이션) log.

## `netstat -s` / `ss -s`

Thống kê giao thức (protocol / 프로토콜):

```bash
ss -s
netstat -s 2>/dev/null
```

Có thể cung cấp retransmission, failed liên kết (connection / 연결), reset và nhiều counter TCP/IP tùy hệ thống (system / 시스템).

Không đọc một counter tuyệt đối đơn lẻ. Hãy lấy tỷ lệ (rate / 비율) theo thời gian và so với traffic volume.

## `/proc/net`

Kernel expose nhiều networking trạng thái (state / 상태) qua `/proc/net` hoặc netlink interfaces.

Các công cụ hiện đại như `ss`, `ip` dùng netlink thay vì yêu cầu người dùng parse tệp (file / 파일) proc trực tiếp.

Mô hình tư duy (mental model / 사고 모델) quan trọng: command là máy khách (client / 클라이언트) của kernel trạng thái (state / 상태), không phải nguồn chân lý độc lập.

## Netlink

**Netlink** là cơ chế IPC giữa người dùng (user / 사용자) không gian (space / 공간) và kernel rất quan trọng cho networking.

`ip`, `ss`, routing daemon, bộ chứa (container / 컨테이너) thời gian chạy (runtime / 런타임) dùng netlink để truy vấn (query / 쿼리)/thay đổi (change / 변경) mạng (network / 네트워크) trạng thái (state / 상태).

Đây là lý do bộ công cụ `iproute2` có thể thao tác giao diện (interface / 인터페이스), tuyến (route / 경로), neighbor và không gian tên (namespace / 네임스페이스) theo cách nhất quán.

## `tcpdump` bắt packet ở đâu?

`tcpdump` dùng packet socket/capture cơ chế (mechanism / 메커니즘) để quan sát packet qua giao diện (interface / 인터페이스).

Ví dụ:

```bash
sudo tcpdump -ni any host 10.0.0.20 and port 443
```

Nếu máy khách (client / 클라이언트) gửi SYN nhưng máy chủ (server / 서버) host không thấy, lỗi nằm trước capture điểm (point / 지점) đó.

Nếu host thấy SYN và SYN-ACK nhưng máy khách (client / 클라이언트) không nhận, cần nhìn return đường dẫn (path / 경로)/firewall/mạng (network / 네트워크).

Nếu handshake hoàn tất nhưng ứng dụng (application / 애플리케이션) hết thời gian chờ (timeout / 타임아웃), đi lên socket/ứng dụng (application / 애플리케이션) tầng (layer / 계층).

## Packet capture không chứng minh ứng dụng (application / 애플리케이션) đã đọc dữ liệu

Thấy packet tới giao diện (interface / 인터페이스) chỉ chứng minh traffic đã tới capture điểm (point / 지점).

Packet vẫn có thể bị firewall drop hoặc TCP ngăn xếp (stack / 스택) reject trước khi socket nhận.

Tương tự, packet tới socket buffer chưa có nghĩa ứng dụng (application / 애플리케이션) luồng thực thi (thread / 스레드) đã `read()`.

Cần phân biệt các tầng (layer / 계층) bằng chứng (evidence / 증거).

## CPU softirq saturation

Một host có thể có:

```text
tổng CPU 40%
nhưng CPU 3 = 100% softirq
```

Nếu luồng (flow / 흐름)/RSS tập trung vào CPU 3, mạng (network / 네트워크) thông lượng (throughput / 처리량)/độ trễ (latency / 지연 시간) có thể bottleneck dù average CPU thấp.

Do đó khi phân tích network-intensive tải công việc (workload / 워크로드) nên nhìn per-CPU utilization.

```bash
mpstat -P ALL 1
```

## NUMA và NIC locality

Trên máy chủ (server / 서버) nhiều NUMA nút (node / 노드), NIC nằm gần một CPU/socket nhất định. Nếu interrupt xử lý ở NUMA nút (node / 노드) khác và ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리) ở nơi xa, cross-NUMA traffic có thể tăng độ trễ (latency / 지연 시간).

Đây là tối ưu hóa (optimization / 최적화) sâu chỉ cần khi có bằng chứng (evidence / 증거). Không nên pin IRQ/ứng dụng (application / 애플리케이션) theo cảm tính.

## XDP và eBPF ở receive đường dẫn (path / 경로)

**XDP (eXpress data Path)** cho phép eBPF program xử lý packet rất sớm trong receive đường dẫn (path / 경로) ở nhiều driver.

Use trường hợp (case / 사례):

- packet filtering;
- DDoS mitigation;
- tải (load / 로드) balancing;
- khả năng quan sát (observability / 관측 가능성).

Ưu điểm là tránh đưa packet không cần thiết qua toàn bộ mạng (network / 네트워크) ngăn xếp (stack / 스택).

Nhưng XDP/eBPF tăng độ phức tạp (complexity / 복잡도) và yêu cầu hiểu an toàn (safety / 안전)/verifier/tooling.

## Socket API là lớp trừu tượng (abstraction / 추상화) cuối cùng cho ứng dụng (application / 애플리케이션)

Ứng dụng (application / 애플리케이션) không cần biết skb, qdisc hay NIC ring trong mã (code / 코드) thông thường. Nó thấy:

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

Socket là ranh giới API cho phép mạng (network / 네트워크) ngăn xếp (stack / 스택) phức tạp phía dưới được ẩn đi.

Đây là Unix lớp trừu tượng (abstraction / 추상화) rất mạnh: mạng (network / 네트워크) communication cuối cùng được tiến trình (process / 프로세스) thao tác thông qua tệp (file / 파일) descriptor-like handle.

## Blocking socket

Với blocking I/O, nếu `read()` chưa có dữ liệu, luồng thực thi (thread / 스레드) có thể sleep trên wait hàng đợi (queue / 큐).

Khi packet tới và socket trở nên readable, kernel wake tác vụ (task / 작업).

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

Toàn bộ chuỗi giải thích độ trễ (latency / 지연 시간) từ packet đến ứng dụng (application / 애플리케이션).

## Non-blocking socket và `epoll`

Với non-blocking chế độ (mode / 모드), `read()` có thể trả `EAGAIN` nếu chưa có dữ liệu.

Ứng dụng (application / 애플리케이션) dùng `epoll` để chờ nhiều tệp (file / 파일) descriptor có sự kiện (event / 이벤트) mà không cần một luồng thực thi (thread / 스레드) khối (block / 블록) riêng trên mỗi socket.

```text
many sockets
    ↓
epoll interest set
    ↓
kernel báo ready fd
    ↓
application xử lý batch event
```

Đây là nền tảng của event-driven máy chủ (server / 서버) như Nginx/Netty.

## Edge-triggered và level-triggered

`epoll` có các chế độ (mode / 모드) khác nhau. Với edge-triggered, ứng dụng (application / 애플리케이션) thường phải drain socket tới `EAGAIN`, nếu không có thể bỏ lỡ cơ hội xử lý tiếp theo theo lô-gic (logic / 논리) sự kiện (event / 이벤트).

Không cần dùng edge-triggered để có hiệu năng tốt trong mọi trường hợp. tính đúng đắn (correctness / 정확성) quan trọng hơn micro-optimization.

## Java NIO và Linux epoll

Trên Linux, Java NIO selector hiện thực (implementation / 구현) có thể sử dụng epoll tùy JDK/thời gian chạy (runtime / 런타임).

Netty cũng khai thác epoll/bản địa (native / 네이티브) vận chuyển (transport / 전송) trong môi trường phù hợp.

Vì vậy khái niệm Selector ở Java không phải lớp trừu tượng (abstraction / 추상화) tách rời OS; bên dưới nó có thể nối trực tiếp với Linux sự kiện (event / 이벤트) notification.

## `SO_REUSEADDR` và `SO_REUSEPORT`

Socket option này giải quyết các vấn đề khác nhau về bind/reuse tùy giao thức (protocol / 프로토콜)/nền tảng (platform / 플랫폼).

`SO_REUSEPORT` có thể cho nhiều listening socket bind cùng endpoint với tải (load / 로드) phân phối (distribution / 분포) của kernel trong use trường hợp (case / 사례) phù hợp.

Không nên bản sao (copy / 복사) option mà không hiểu ngữ nghĩa (semantics / 의미론) vì khác biệt nền tảng (platform / 플랫폼) có thể quan trọng.

## Liên kết (connection / 연결) refused ở ngăn xếp (stack / 스택) nào?

Nếu SYN tới host nhưng không có listener, kernel có thể trả RST. máy khách (client / 클라이언트) thấy `ECONNREFUSED`.

Điều này nghĩa thất bại (failure / 실패) có thể xảy ra hoàn toàn trong kernel trước khi ứng dụng (application / 애플리케이션) mã (code / 코드) đích được chạy.

## Hết thời gian chờ (timeout / 타임아웃) có thể do drop im lặng

Nếu firewall DROP packet thay vì REJECT, máy khách (client / 클라이언트) có thể retransmit cho tới hết thời gian chờ (timeout / 타임아웃).

Cùng một “không kết nối được” nhưng symptom khác:

```text
RST/REJECT → lỗi nhanh
DROP       → timeout lâu hơn
```

Đây là lý do độ trễ (latency / 지연 시간) của thất bại (failure / 실패) chứa thông tin chẩn đoán.

## Mô hình tư duy (mental model / 사고 모델)

Một yêu cầu (request / 요청) mạng (network / 네트워크) đi qua một chuỗi hàng đợi (queue / 큐) và máy trạng thái (state machine / 상태 머신):

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

Khi độ trễ (latency / 지연 시간) hoặc drop xảy ra, hãy hỏi **hàng đợi (queue / 큐) nào đang đầy, máy trạng thái (state machine / 상태 머신) nào chưa tiến triển, và bằng chứng (evidence / 증거) ở lớp nào chứng minh packet đã đi tới đó**.

## Những hiểu lầm phổ biến

**“Packet tới NIC nghĩa là ứng dụng (application / 애플리케이션) đã nhận.”** Còn nhiều lớp kernel ở giữa.

**“CPU tổng chưa cao nên mạng (network / 네트워크) không thể nghẽn.”** Một softirq CPU hoặc NIC hàng đợi (queue / 큐) có thể bão hòa cục bộ.

**“Listener tồn tại nghĩa là accept không thể nghẽn.”** Accept hàng đợi (queue / 큐)/backlog và ứng dụng (application / 애플리케이션) scheduling vẫn có thể bottleneck.

**“tcpdump thấy checksum bad nghĩa packet thật bị lỗi.”** Offload có thể làm capture trước bước checksum hardware.

**“Loopback kiểm thử (test / 테스트) thành công chứng minh đường mạng ngoài host khỏe.”** Loopback bỏ qua NIC và nhiều lớp bên ngoài.

**“TIME_WAIT là liên kết (connection / 연결) leak.”** Nó thường là trạng thái (state / 상태) TCP bình thường sau active close.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Đọc tiếp theo hướng:

- [Interrupt/softirq/device model](../00_foundations/interrupts_softirq_device_model.md) — packet vào CPU thế nào;
- [IP routing/NAT/conntrack](./ip_routing_nat_conntrack.md) — packet chọn đường và chính sách (policy / 정책);
- [TCP/HTTP/TLS](./tcp_http_tls.md) — vận chuyển (transport / 전송)/ứng dụng (application / 애플리케이션) trạng thái (state / 상태);
- [TCP congestion control](./tcp_congestion_control.md) — hành vi (behavior / 동작) khi mạng (network / 네트워크) có sức chứa (capacity / 용량)/hàng đợi (queue / 큐)/mất mát (loss / 손실);
- [IPC và epoll](../04_process/interprocess_communication.md) — socket readiness và event-driven I/O;
- [Scheduler](../06_resources/kernel_scheduler_deep_dive.md) — tác vụ (task / 작업) được wake rồi khi nào thực sự chạy;
- [Tracing](../09_production/observability_tracing_strace_perf.md) — đo packet/socket/off-CPU đường dẫn (path / 경로) trong môi trường vận hành (production / 운영 환경).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [dns resolution internals](./dns_resolution_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
