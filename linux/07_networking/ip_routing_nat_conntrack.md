# IP Routing, NAT, Conntrack và đường đi của packet

> **Mạch đọc:** Đọc **IP Routing, NAT, Conntrack và đường đi của packet** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Một packet rời host như thế nào?** sang **Routing bảng (table / 테이블) là gì?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Khi một yêu cầu (request / 요청) mạng thất bại, việc chỉ kiểm tra `ping` hoặc `curl` thường chưa đủ. Linux kernel phải quyết định packet đi qua giao diện (interface / 인터페이스) nào, dùng nguồn (source / 소스) address nào, có bị firewall/NAT thay đổi hay không, liên kết (connection / 연결) có trạng thái (state / 상태) gì và phản hồi (response / 응답) sẽ quay về theo tuyến (route / 경로) nào.

Hiểu **định tuyến IP (IP routing)**, **NAT**, **conntrack** và mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) giúp biến câu “mạng (network / 네트워크) lỗi” thành các câu hỏi cụ thể hơn.

## Một packet rời host như thế nào?

Giả sử tiến trình (process / 프로세스) cần gửi TCP packet tới:

```text
10.20.30.40:443
```

Ứng dụng (application / 애플리케이션) tạo socket và gọi `connect()`. Kernel phải:

1. xác định destination IP;
2. tra bảng định tuyến (routing table);
3. chọn đầu ra (output / 출력) giao diện (interface / 인터페이스);
4. chọn nguồn (source / 소스) IP phù hợp;
5. tạo vận chuyển (transport / 전송) trạng thái (state / 상태) TCP;
6. áp dụng firewall/NAT rules nếu có;
7. truyền frame ra giao diện (interface / 인터페이스).

Ứng dụng (application / 애플리케이션) không tự chọn Ethernet frame hoặc ARP packet trong trường hợp thông thường. mạng (network / 네트워크) ngăn xếp (stack / 스택) của kernel làm phần việc đó.

## Routing bảng (table / 테이블) là gì?

Routing bảng (table / 테이블) là tập các quy tắc (rule / 규칙) cho biết destination prefix nào nên đi qua giao diện (interface / 인터페이스)/gateway nào.

Xem routing bảng (table / 테이블):

```bash
ip route
```

Ví dụ:

```text
10.0.0.0/24 dev eth0 proto kernel src 10.0.0.10
default via 10.0.0.1 dev eth0
```

Quy tắc (rule / 규칙) đầu nói traffic tới `10.0.0.0/24` đi trực tiếp qua `eth0`. quy tắc (rule / 규칙) `default` dùng khi không có tuyến (route / 경로) cụ thể hơn.

## Longest prefix match

Kernel ưu tiên tuyến (route / 경로) có prefix cụ thể nhất.

Giả sử có:

```text
10.0.0.0/8 via A
10.20.0.0/16 via B
10.20.30.0/24 via C
```

Destination `10.20.30.40` sẽ chọn `/24`, vì tuyến (route / 경로) đó cụ thể nhất.

Đây gọi là **longest prefix match**.

Không phải tuyến (route / 경로) xuất hiện trước trong đầu ra (output / 출력) sẽ luôn thắng.

## `ip route get` có giá trị gì?

Thay vì tự đọc toàn bộ bảng:

```bash
ip route get 10.20.30.40
```

Kernel trả tuyến (route / 경로) thực tế mà nó sẽ chọn, thường gồm:

- đầu ra (output / 출력) giao diện (interface / 인터페이스);
- gateway;
- nguồn (source / 소스) IP;
- bảng (table / 테이블)/quy tắc (rule / 규칙) liên quan.

Đây là một trong những command có giá trị nhất khi máy có nhiều NIC, VPN hoặc bộ chứa (container / 컨테이너) networks.

## Default gateway không phải “internet”

Default gateway chỉ là next hop dùng khi không có tuyến (route / 경로) cụ thể hơn. Gateway đó có thể dẫn tới router nội bộ, VPN gateway hoặc thiết bị khác.

Nếu default tuyến (route / 경로) sai, DNS vẫn có thể resolve bình thường nhưng TCP liên kết (connection / 연결) ra ngoài thất bại (fail / 실패).

## ARP và neighbor bảng (table / 테이블)

Trong IPv4 Ethernet mạng (network / 네트워크), kernel cần biết MAC address của next hop. ARP giúp ánh xạ IP local-neighbor thành MAC.

Xem neighbor bảng (table / 테이블):

```bash
ip neigh
```

Nếu gateway xuất hiện ở trạng thái bất thường như `FAILED`, vấn đề có thể nằm ở tầng (layer / 계층) 2/cục bộ (local / 로컬) mạng (network / 네트워크) chứ chưa tới remote dịch vụ (service / 서비스).

IPv6 dùng Neighbor Discovery thay vì ARP theo cách tương ứng.

## Multiple routing tables và chính sách (policy / 정책) routing

Linux không chỉ có một routing bảng (table / 테이블). `ip rule` cho phép **chính sách (policy / 정책) routing** dựa trên nguồn (source / 소스) address, fwmark và các điều kiện khác.

```bash
ip rule
ip route show table all
```

Điều này thường xuất hiện trong:

- VPN;
- multi-homed host;
- Kubernetes/CNI;
- advanced routing;
- traffic chính sách (policy / 정책).

Khi `ip route` nhìn bình thường nhưng traffic vẫn đi sai đường dẫn (path / 경로), cần nhớ rằng chính sách (policy / 정책) rules có thể chọn bảng (table / 테이블) khác.

## NAT là gì?

**mạng (network / 네트워크) Address Translation (NAT)** thay đổi nguồn (source / 소스) hoặc destination address/cổng (port / 포트) của packet.

Hai dạng thường gặp:

- **SNAT**: đổi nguồn (source / 소스) address;
- **DNAT**: đổi destination address.

Masquerade là một dạng SNAT thường dùng khi nguồn (source / 소스) IP của outgoing giao diện (interface / 인터페이스) có thể thay đổi.

Bộ chứa (container / 컨테이너) cầu nối (bridge / 브리지) networking thường dùng NAT để bộ chứa (container / 컨테이너) private IP truy cập mạng (network / 네트워크) ngoài.

## NAT không phải routing

Routing quyết định packet đi đâu. NAT thay đổi address/cổng (port / 포트) của packet.

Hai cơ chế thường hoạt động cùng nhau nhưng giải quyết hai vấn đề khác nhau.

Ví dụ:

```text
container 172.17.0.2
    ↓
SNAT/MASQUERADE
    ↓
host 10.0.0.10
    ↓
route tới internet
```

Nếu tuyến (route / 경로) không tồn tại, NAT không tự tạo đường đi.

## nftables và iptables

Linux hiện đại thường dùng nftables ở kernel/userspace ngăn xếp (stack / 스택) mới hơn, trong khi nhiều hệ thống vẫn expose iptables tính tương thích (compatibility / 호환성).

Xem ruleset nftables:

```bash
sudo nft list ruleset
```

Legacy/tính tương thích (compatibility / 호환성):

```bash
sudo iptables -S
sudo iptables -t nat -S
```

Không nên thay firewall/NAT quy tắc (rule / 규칙) trên môi trường vận hành (production / 운영 환경) chỉ để “kiểm thử (test / 테스트) nhanh” nếu chưa biết quy tắc (rule / 규칙) được quản lý bởi firewalld, Docker, Kubernetes hay automation nào khác.

## Conntrack là gì?

Linux **liên kết (connection / 연결) tracking (conntrack)** theo dõi trạng thái (state / 상태) của mạng (network / 네트워크) flows để firewall/NAT có thể áp dụng chính sách (policy / 정책) theo liên kết (connection / 연결).

Ví dụ TCP luồng (flow / 흐름) có thể được xem là `NEW`, `ESTABLISHED`, `RELATED`.

NAT cần conntrack để phản hồi (response / 응답) packet được dịch ngược đúng ánh xạ (mapping / 매핑).

Xem conntrack bảng (table / 테이블) nếu công cụ (tool / 도구) có sẵn:

```bash
sudo conntrack -L
```

hoặc xem counters trong `/proc`/`sysctl` tùy kernel:

```bash
sysctl net.netfilter.nf_conntrack_count
sysctl net.netfilter.nf_conntrack_max
```

Nếu conntrack bảng (table / 테이블) đầy, liên kết (connection / 연결) mới có thể bị drop dù ứng dụng (application / 애플리케이션) vẫn healthy.

## Liên kết (connection / 연결) tracking và high traffic

Một máy chủ (server / 서버) proxy/NAT có rất nhiều connections có thể tạo pressure lên conntrack trạng thái (state / 상태).

Điều quan trọng là không chỉ tăng `nf_conntrack_max` ngay. Cần hỏi:

- liên kết (connection / 연결) tỷ lệ (rate / 비율) có tăng bất thường không?
- hết thời gian chờ (timeout / 타임아웃) trạng thái (state / 상태) có phù hợp không?
- thử lại (retry / 재시도) storm có đang tạo hàng triệu connections không?
- máy chủ (server / 서버) có đủ bộ nhớ (memory / 메모리) cho bảng (table / 테이블) lớn hơn không?

Tăng limit chỉ kéo dài thời gian trước thất bại (failure / 실패) nếu nguyên nhân là traffic amplification.

## Ephemeral cổng (port / 포트)

Máy khách (client / 클라이언트) TCP liên kết (connection / 연결) cần nguồn (source / 소스) cổng (port / 포트) tạm thời, gọi là **ephemeral cổng (port / 포트)**.

Xem phạm vi (range / 범위):

```bash
sysctl net.ipv4.ip_local_port_range
```

Nếu một host tạo số lượng rất lớn outbound connections tới cùng destination tuple và không reuse liên kết (connection / 연결), có thể gặp pressure ephemeral-port không gian (space / 공간).

HTTP keep-alive và liên kết (connection / 연결) pooling giảm liên kết (connection / 연결) churn.

Đây là liên kết (connection / 연결) trực tiếp giữa Linux networking và backend HTTP máy khách (client / 클라이언트) cấu hình (configuration / 구성).

## TIME_WAIT và cổng (port / 포트) reuse

Sau khi TCP liên kết (connection / 연결) close, một endpoint có thể ở `TIME_WAIT` để đảm bảo delayed packets từ liên kết (connection / 연결) cũ không gây nhầm cho liên kết (connection / 연결) mới.

Xem:

```bash
ss -ant state time-wait
```

Nhiều `TIME_WAIT` không tự động là lỗi. Cần đặt trong ngữ cảnh (context / 맥락) liên kết (connection / 연결) tỷ lệ (rate / 비율) và cổng (port / 포트) availability.

Nếu dịch vụ (service / 서비스) mở hàng nghìn short-lived outbound requests mỗi giây, nguyên nhân gốc (root cause / 근본 원인) có thể là không dùng liên kết (connection / 연결) pool chứ không phải kernel “giữ TIME_WAIT quá lâu”.

## Reverse đường dẫn (path / 경로) và asymmetric routing

Packet đi từ A tới B qua đường dẫn (path / 경로) X nhưng phản hồi (response / 응답) từ B quay qua đường dẫn (path / 경로) Y gọi là **asymmetric routing**.

Asymmetry không luôn sai, nhưng stateful firewall/NAT có thể yêu cầu cả hai chiều đi qua cùng stateful thiết bị (device / 장치).

Linux còn có reverse đường dẫn (path / 경로) filtering (`rp_filter`) có thể drop traffic khi nguồn (source / 소스) tuyến (route / 경로) không phù hợp chính sách (policy / 정책).

Kiểm tra:

```bash
sysctl net.ipv4.conf.all.rp_filter
```

Không tắt `rp_filter` chỉ vì một packet thất bại (fail / 실패). Cần hiểu topology trước.

## Mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) thay đổi routing ngữ cảnh (context / 맥락)

Bộ chứa (container / 컨테이너) có thể có mạng (network / 네트워크) không gian tên (namespace / 네임스페이스) riêng:

```text
host namespace
  routing table A

container namespace
  routing table B
```

Do đó chạy:

```bash
ip route
```

ở host và bên trong bộ chứa (container / 컨테이너) có thể cho kết quả hoàn toàn khác.

`localhost` cũng thuộc không gian tên (namespace / 네임스페이스) hiện tại.

Xem không gian tên (namespace / 네임스페이스):

```bash
ip netns list
```

Tùy thời gian chạy (runtime / 런타임), không gian tên (namespace / 네임스페이스) bộ chứa (container / 컨테이너) có thể không xuất hiện trực tiếp theo tên trong `ip netns`.

## Veth và cầu nối (bridge / 브리지)

Bộ chứa (container / 컨테이너) networking thường dùng cặp **veth (virtual Ethernet)**. Một đầu nằm trong bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스), đầu kia nối cầu nối (bridge / 브리지) hoặc host networking.

Mô hình tư duy (mental model / 사고 모델):

```text
container eth0
   ↕ veth pair
host vethX
   ↓
linux bridge
   ↓
host routing/NAT
```

Hiểu mô hình này giúp đọc `ip link`, `bridge link`, `ip addr` khi Docker/Kubernetes mạng (network / 네트워크) có vấn đề.

## MTU và fragmentation

**MTU — Maximum Transmission đơn vị (unit / 단위)** là kích thước packet/frame payload tối đa theo link.

Tunnel/VPN/VXLAN thêm headers, làm effective MTU nhỏ hơn.

Một lỗi khó chịu là small yêu cầu (request / 요청) hoạt động nhưng large yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃) vì đường dẫn (path / 경로) MTU Discovery/firewall ICMP issue.

Kiểm tra giao diện (interface / 인터페이스) MTU:

```bash
ip link
```

Ping với kích thước/DF flag có thể giúp kiểm thử (test / 테스트) trên Linux:

```bash
ping -M do -s 1400 <host>
```

Giá trị phù hợp phụ thuộc IPv4/headers/đường dẫn (path / 경로); không dùng một threshold cố định cho mọi mạng.

## Packet forwarding

Linux host có thể hoạt động như router nếu IP forwarding được bật:

```bash
sysctl net.ipv4.ip_forward
```

Bộ chứa (container / 컨테이너) hosts, VPN gateways và Kubernetes nodes thường cần forwarding.

Nếu `ip_forward=0`, host có thể giao tiếp cho chính nó nhưng không forward traffic giữa interfaces như router.

## `tcpdump` đặt ở đâu?

Khi có nhiều mạng (network / 네트워크) layers, vị trí capture rất quan trọng.

Có thể capture:

```bash
sudo tcpdump -ni any host 10.20.30.40
```

hoặc cụ thể giao diện (interface / 인터페이스):

```bash
sudo tcpdump -ni eth0 tcp port 443
```

Nếu packet xuất hiện ở bộ chứa (container / 컨테이너) veth nhưng không xuất hiện ở bên ngoài (external / 외부) NIC, vấn đề nằm trong host forwarding/firewall/NAT đường dẫn (path / 경로).

Nếu bên ngoài (external / 외부) NIC có outgoing SYN nhưng không có phản hồi (response / 응답), phạm vi (scope / 범위) chuyển ra ngoài host.

## Troubleshooting theo packet đường dẫn (path / 경로)

Một luồng (flow / 흐름) outbound có thể kiểm tra:

```text
application socket
    ↓
namespace routing
    ↓
firewall / conntrack
    ↓
NAT
    ↓
output interface
    ↓
gateway / network
    ↓
remote host
```

Commands tương ứng:

```bash
ss -antp
ip route get <destination>
ip rule
sudo nft list ruleset
sysctl net.netfilter.nf_conntrack_count
ip neigh
sudo tcpdump -ni any host <destination>
```

Không cần chạy tất cả nếu symptom đã khoanh được tầng (layer / 계층).

## Trường hợp (case / 사례): bộ chứa (container / 컨테이너) truy cập internet không được

Kiểm tra bên trong bộ chứa (container / 컨테이너):

```bash
ip addr
ip route
```

Sau đó host:

```bash
sysctl net.ipv4.ip_forward
sudo nft list ruleset
ip route
```

Nếu bộ chứa (container / 컨테이너) có default tuyến (route / 경로) tới cầu nối (bridge / 브리지) nhưng host không forward/NAT đúng, DNS hay ứng dụng (application / 애플리케이션) cấu hình (config / 설정) không phải nguyên nhân đầu tiên.

## Trường hợp (case / 사례): cục bộ (local / 로컬) dịch vụ (service / 서비스) hoạt động nhưng remote không vào được

Nếu:

```bash
curl http://127.0.0.1:8080
```

thành công, tiếp tục:

```bash
ss -lntp | grep ':8080'
```

Nếu listener chỉ là:

```text
127.0.0.1:8080
```

remote traffic không thể tới ứng dụng (application / 애플리케이션) qua bên ngoài (external / 외부) IP.

Nếu bind `0.0.0.0` nhưng remote vẫn thất bại (fail / 실패), chuyển sang host firewall, cloud bảo mật (security / 보안) chính sách (policy / 정책) và upstream routing.

## Mô hình tư duy (mental model / 사고 모델)

Mạng (network / 네트워크) không phải một “đường dây” duy nhất. Mỗi packet đi qua chuỗi quyết định:

```text
namespace
 → route lookup
 → source selection
 → conntrack/firewall
 → NAT
 → interface
 → next hop
 → remote path
```

Khi gỡ lỗi (debug / 디버그), hãy hỏi packet đang biến mất hoặc bị thay đổi ở bước nào.

## Những hiểu lầm phổ biến

**“Có default gateway thì mọi destination đều đi được.”** Gateway cũng cần tuyến (route / 경로)/mạng (network / 네트워크) phía sau hoạt động.

**“NAT và routing là một.”** Routing chọn đường dẫn (path / 경로), NAT thay đổi address/cổng (port / 포트).

**“TIME_WAIT nhiều nghĩa kernel lỗi.”** Nó có thể là hệ quả tự nhiên của liên kết (connection / 연결) churn.

**“bộ chứa (container / 컨테이너) dùng mạng (network / 네트워크) của host.”** Tùy mạng (network / 네트워크) chế độ (mode / 모드); thường bộ chứa (container / 컨테이너) có không gian tên (namespace / 네임스페이스)/routing riêng.

**“Ping được nghĩa TCP chắc chắn được.”** ICMP và TCP đi qua chính sách (policy / 정책)/trạng thái (state / 상태) khác nhau.

**“Firewall quy tắc (rule / 규칙) nhìn đúng nghĩa packet chắc chắn qua.”** Conntrack, chính sách (policy / 정책) routing, không gian tên (namespace / 네임스페이스) và upstream firewall vẫn có thể tác động.

## Xem thêm

Các liên kết này là bước bàn giao sang cơ chế liên quan. Hãy mở chúng theo câu hỏi còn bỏ ngỏ, không coi danh sách link là phần kết luận tự thân.

- [Networking, DNS, socket và port](./networking_dns_sockets_ports.md)
- [TCP, HTTP và TLS](./tcp_http_tls.md)
- [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md)
- [Linux container](../09_production/linux_containers.md)
- [Tracing và observability](../09_production/observability_tracing_strace_perf.md)

> **Bàn giao:** Sau **Xem thêm**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [dns resolution internals](./dns_resolution_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
