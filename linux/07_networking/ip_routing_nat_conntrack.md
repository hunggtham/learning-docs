# IP Routing, NAT, Conntrack và đường đi của packet

Khi một request mạng thất bại, việc chỉ kiểm tra `ping` hoặc `curl` thường chưa đủ. Linux kernel phải quyết định packet đi qua interface nào, dùng source address nào, có bị firewall/NAT thay đổi hay không, connection có state gì và response sẽ quay về theo route nào.

Hiểu **định tuyến IP (IP routing)**, **NAT**, **conntrack** và network namespace giúp biến câu “network lỗi” thành các câu hỏi cụ thể hơn.

## Một packet rời host như thế nào?

Giả sử process cần gửi TCP packet tới:

```text
10.20.30.40:443
```

Application tạo socket và gọi `connect()`. Kernel phải:

1. xác định destination IP;
2. tra bảng định tuyến (routing table);
3. chọn output interface;
4. chọn source IP phù hợp;
5. tạo transport state TCP;
6. áp dụng firewall/NAT rules nếu có;
7. truyền frame ra interface.

Application không tự chọn Ethernet frame hoặc ARP packet trong trường hợp thông thường. Network stack của kernel làm phần việc đó.

## Routing table là gì?

Routing table là tập các rule cho biết destination prefix nào nên đi qua interface/gateway nào.

Xem routing table:

```bash
ip route
```

Ví dụ:

```text
10.0.0.0/24 dev eth0 proto kernel src 10.0.0.10
default via 10.0.0.1 dev eth0
```

Rule đầu nói traffic tới `10.0.0.0/24` đi trực tiếp qua `eth0`. Rule `default` dùng khi không có route cụ thể hơn.

## Longest prefix match

Kernel ưu tiên route có prefix cụ thể nhất.

Giả sử có:

```text
10.0.0.0/8 via A
10.20.0.0/16 via B
10.20.30.0/24 via C
```

Destination `10.20.30.40` sẽ chọn `/24`, vì route đó cụ thể nhất.

Đây gọi là **longest prefix match**.

Không phải route xuất hiện trước trong output sẽ luôn thắng.

## `ip route get` có giá trị gì?

Thay vì tự đọc toàn bộ bảng:

```bash
ip route get 10.20.30.40
```

Kernel trả route thực tế mà nó sẽ chọn, thường gồm:

- output interface;
- gateway;
- source IP;
- table/rule liên quan.

Đây là một trong những command có giá trị nhất khi máy có nhiều NIC, VPN hoặc container networks.

## Default gateway không phải “internet”

Default gateway chỉ là next hop dùng khi không có route cụ thể hơn. Gateway đó có thể dẫn tới router nội bộ, VPN gateway hoặc thiết bị khác.

Nếu default route sai, DNS vẫn có thể resolve bình thường nhưng TCP connection ra ngoài fail.

## ARP và neighbor table

Trong IPv4 Ethernet network, kernel cần biết MAC address của next hop. ARP giúp ánh xạ IP local-neighbor thành MAC.

Xem neighbor table:

```bash
ip neigh
```

Nếu gateway xuất hiện ở trạng thái bất thường như `FAILED`, vấn đề có thể nằm ở layer 2/local network chứ chưa tới remote service.

IPv6 dùng Neighbor Discovery thay vì ARP theo cách tương ứng.

## Multiple routing tables và policy routing

Linux không chỉ có một routing table. `ip rule` cho phép **policy routing** dựa trên source address, fwmark và các điều kiện khác.

```bash
ip rule
ip route show table all
```

Điều này thường xuất hiện trong:

- VPN;
- multi-homed host;
- Kubernetes/CNI;
- advanced routing;
- traffic policy.

Khi `ip route` nhìn bình thường nhưng traffic vẫn đi sai path, cần nhớ rằng policy rules có thể chọn table khác.

## NAT là gì?

**Network Address Translation (NAT)** thay đổi source hoặc destination address/port của packet.

Hai dạng thường gặp:

- **SNAT**: đổi source address;
- **DNAT**: đổi destination address.

Masquerade là một dạng SNAT thường dùng khi source IP của outgoing interface có thể thay đổi.

Container bridge networking thường dùng NAT để container private IP truy cập network ngoài.

## NAT không phải routing

Routing quyết định packet đi đâu. NAT thay đổi address/port của packet.

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

Nếu route không tồn tại, NAT không tự tạo đường đi.

## nftables và iptables

Linux hiện đại thường dùng nftables ở kernel/userspace stack mới hơn, trong khi nhiều hệ thống vẫn expose iptables compatibility.

Xem ruleset nftables:

```bash
sudo nft list ruleset
```

Legacy/compatibility:

```bash
sudo iptables -S
sudo iptables -t nat -S
```

Không nên thay firewall/NAT rule trên production chỉ để “test nhanh” nếu chưa biết rule được quản lý bởi firewalld, Docker, Kubernetes hay automation nào khác.

## Conntrack là gì?

Linux **connection tracking (conntrack)** theo dõi state của network flows để firewall/NAT có thể áp dụng policy theo connection.

Ví dụ TCP flow có thể được xem là `NEW`, `ESTABLISHED`, `RELATED`.

NAT cần conntrack để response packet được dịch ngược đúng mapping.

Xem conntrack table nếu tool có sẵn:

```bash
sudo conntrack -L
```

hoặc xem counters trong `/proc`/`sysctl` tùy kernel:

```bash
sysctl net.netfilter.nf_conntrack_count
sysctl net.netfilter.nf_conntrack_max
```

Nếu conntrack table đầy, connection mới có thể bị drop dù application vẫn healthy.

## Connection tracking và high traffic

Một server proxy/NAT có rất nhiều connections có thể tạo pressure lên conntrack state.

Điều quan trọng là không chỉ tăng `nf_conntrack_max` ngay. Cần hỏi:

- connection rate có tăng bất thường không?
- timeout state có phù hợp không?
- retry storm có đang tạo hàng triệu connections không?
- server có đủ memory cho table lớn hơn không?

Tăng limit chỉ kéo dài thời gian trước failure nếu nguyên nhân là traffic amplification.

## Ephemeral port

Client TCP connection cần source port tạm thời, gọi là **ephemeral port**.

Xem range:

```bash
sysctl net.ipv4.ip_local_port_range
```

Nếu một host tạo số lượng rất lớn outbound connections tới cùng destination tuple và không reuse connection, có thể gặp pressure ephemeral-port space.

HTTP keep-alive và connection pooling giảm connection churn.

Đây là connection trực tiếp giữa Linux networking và backend HTTP client configuration.

## TIME_WAIT và port reuse

Sau khi TCP connection close, một endpoint có thể ở `TIME_WAIT` để đảm bảo delayed packets từ connection cũ không gây nhầm cho connection mới.

Xem:

```bash
ss -ant state time-wait
```

Nhiều `TIME_WAIT` không tự động là lỗi. Cần đặt trong context connection rate và port availability.

Nếu service mở hàng nghìn short-lived outbound requests mỗi giây, root cause có thể là không dùng connection pool chứ không phải kernel “giữ TIME_WAIT quá lâu”.

## Reverse path và asymmetric routing

Packet đi từ A tới B qua path X nhưng response từ B quay qua path Y gọi là **asymmetric routing**.

Asymmetry không luôn sai, nhưng stateful firewall/NAT có thể yêu cầu cả hai chiều đi qua cùng stateful device.

Linux còn có reverse path filtering (`rp_filter`) có thể drop traffic khi source route không phù hợp policy.

Kiểm tra:

```bash
sysctl net.ipv4.conf.all.rp_filter
```

Không tắt `rp_filter` chỉ vì một packet fail. Cần hiểu topology trước.

## Network namespace thay đổi routing context

Container có thể có network namespace riêng:

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

ở host và bên trong container có thể cho kết quả hoàn toàn khác.

`localhost` cũng thuộc namespace hiện tại.

Xem namespace:

```bash
ip netns list
```

Tùy runtime, namespace container có thể không xuất hiện trực tiếp theo tên trong `ip netns`.

## Veth và bridge

Container networking thường dùng cặp **veth (virtual Ethernet)**. Một đầu nằm trong container namespace, đầu kia nối bridge hoặc host networking.

Mental model:

```text
container eth0
   ↕ veth pair
host vethX
   ↓
linux bridge
   ↓
host routing/NAT
```

Hiểu mô hình này giúp đọc `ip link`, `bridge link`, `ip addr` khi Docker/Kubernetes network có vấn đề.

## MTU và fragmentation

**MTU — Maximum Transmission Unit** là kích thước packet/frame payload tối đa theo link.

Tunnel/VPN/VXLAN thêm headers, làm effective MTU nhỏ hơn.

Một lỗi khó chịu là small request hoạt động nhưng large request timeout vì Path MTU Discovery/firewall ICMP issue.

Kiểm tra interface MTU:

```bash
ip link
```

Ping với kích thước/DF flag có thể giúp test trên Linux:

```bash
ping -M do -s 1400 <host>
```

Giá trị phù hợp phụ thuộc IPv4/headers/path; không dùng một threshold cố định cho mọi mạng.

## Packet forwarding

Linux host có thể hoạt động như router nếu IP forwarding được bật:

```bash
sysctl net.ipv4.ip_forward
```

Container hosts, VPN gateways và Kubernetes nodes thường cần forwarding.

Nếu `ip_forward=0`, host có thể giao tiếp cho chính nó nhưng không forward traffic giữa interfaces như router.

## `tcpdump` đặt ở đâu?

Khi có nhiều network layers, vị trí capture rất quan trọng.

Có thể capture:

```bash
sudo tcpdump -ni any host 10.20.30.40
```

hoặc cụ thể interface:

```bash
sudo tcpdump -ni eth0 tcp port 443
```

Nếu packet xuất hiện ở container veth nhưng không xuất hiện ở external NIC, vấn đề nằm trong host forwarding/firewall/NAT path.

Nếu external NIC có outgoing SYN nhưng không có response, scope chuyển ra ngoài host.

## Troubleshooting theo packet path

Một flow outbound có thể kiểm tra:

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

Không cần chạy tất cả nếu symptom đã khoanh được layer.

## Case: container truy cập internet không được

Kiểm tra bên trong container:

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

Nếu container có default route tới bridge nhưng host không forward/NAT đúng, DNS hay application config không phải nguyên nhân đầu tiên.

## Case: local service hoạt động nhưng remote không vào được

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

remote traffic không thể tới application qua external IP.

Nếu bind `0.0.0.0` nhưng remote vẫn fail, chuyển sang host firewall, cloud security policy và upstream routing.

## Mô hình tư duy (Mental Model)

Network không phải một “đường dây” duy nhất. Mỗi packet đi qua chuỗi quyết định:

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

Khi debug, hãy hỏi packet đang biến mất hoặc bị thay đổi ở bước nào.

## Những hiểu lầm phổ biến

**“Có default gateway thì mọi destination đều đi được.”** Gateway cũng cần route/network phía sau hoạt động.

**“NAT và routing là một.”** Routing chọn path, NAT thay đổi address/port.

**“TIME_WAIT nhiều nghĩa kernel lỗi.”** Nó có thể là hệ quả tự nhiên của connection churn.

**“Container dùng network của host.”** Tùy network mode; thường container có namespace/routing riêng.

**“Ping được nghĩa TCP chắc chắn được.”** ICMP và TCP đi qua policy/state khác nhau.

**“Firewall rule nhìn đúng nghĩa packet chắc chắn qua.”** Conntrack, policy routing, namespace và upstream firewall vẫn có thể tác động.

## Xem thêm

- [Networking, DNS, socket và port](./networking_dns_sockets_ports.md)
- [TCP, HTTP và TLS](./tcp_http_tls.md)
- [Namespace, cgroup và seccomp](../09_production/namespaces_cgroups_seccomp.md)
- [Linux container](../09_production/linux_containers.md)
- [Tracing và observability](../09_production/observability_tracing_strace_perf.md)
