# DNS Resolution Internals trên Linux

Khi application gọi một hostname như:

```text
api.example.com
```

nó không thể tự gửi packet tới “tên miền”. Network stack cần địa chỉ IP. Quá trình chuyển hostname thành address gọi là **phân giải tên (name resolution)**.

DNS thường được mô tả đơn giản là “đổi domain thành IP”, nhưng trong Linux thực tế còn có `/etc/hosts`, NSS, stub resolver, local cache, DNS server, search domain, TTL, nhiều record types và IPv4/IPv6 preference.

Hiểu các lớp này rất quan trọng khi gặp lỗi kiểu:

```text
Could not resolve host
Temporary failure in name resolution
UnknownHostException
SERVFAIL
NXDOMAIN
```

## Application không nhất thiết gọi DNS trực tiếp

Một chương trình C thường gọi hàm như:

```c
getaddrinfo()
```

Java có API tương ứng như:

```java
InetAddress.getByName("api.example.com")
```

Application yêu cầu hệ thống phân giải tên. Resolver library sau đó mới quyết định nguồn dữ liệu nào được dùng.

Do đó câu “DNS lỗi” đôi khi chưa chính xác: lỗi có thể nằm ở `/etc/hosts`, NSS policy, local resolver hoặc upstream DNS.

## `/etc/nsswitch.conf` và thứ tự lookup

Linux dùng **Name Service Switch (NSS)** để xác định nguồn dữ liệu cho nhiều loại lookup.

Kiểm tra:

```bash
grep '^hosts:' /etc/nsswitch.conf
```

Ví dụ:

```text
hosts: files dns
```

nghĩa là resolver có thể kiểm tra `/etc/hosts` trước rồi mới DNS.

Một hệ thống dùng systemd-resolved có thể có dòng khác như:

```text
hosts: files myhostname resolve [!UNAVAIL=return] dns
```

Chi tiết phụ thuộc distribution.

Điểm quan trọng là hostname resolution không nhất thiết đi thẳng ra DNS server.

## `/etc/hosts`

File `/etc/hosts` cung cấp ánh xạ tĩnh:

```text
127.0.0.1 localhost
10.0.0.20 internal-api
```

Nếu application resolve `internal-api`, entry local có thể override DNS tùy NSS order.

Debug:

```bash
getent hosts internal-api
```

`getent` rất hữu ích vì nó đi qua NSS và gần với cách nhiều application resolve hơn `dig`.

Đây là khác biệt quan trọng:

```bash
dig internal-api
```

hỏi DNS trực tiếp, còn:

```bash
getent hosts internal-api
```

phản ánh system resolver/NSS.

Nếu hai command trả kết quả khác nhau, vấn đề có thể nằm trước DNS query.

## `/etc/resolv.conf`

File này truyền thống chứa resolver configuration:

```bash
cat /etc/resolv.conf
```

Có thể thấy:

```text
nameserver 10.0.0.2
search corp.example.com
options timeout:2 attempts:2
```

Nhưng trên nhiều distro hiện đại, `/etc/resolv.conf` có thể là symlink tới file được quản lý bởi systemd-resolved, NetworkManager hoặc tool khác.

Kiểm tra:

```bash
ls -l /etc/resolv.conf
```

Không nên edit trực tiếp file generated nếu network manager sẽ ghi đè lại.

## Search domain

Nếu config có:

```text
search corp.example.com
```

và application resolve:

```text
db01
```

resolver có thể thử:

```text
db01.corp.example.com
```

Điều này tiện trong mạng nội bộ nhưng cũng tạo ambiguity. Một hostname ngắn có thể resolve khác nhau giữa servers tùy search domain.

Trong production config, FQDN rõ ràng thường giảm surprise.

## Recursive resolver và authoritative server

DNS hierarchy có nhiều vai trò.

Application thường gửi query tới **recursive resolver**. Resolver này có thể hỏi các DNS servers khác và cache kết quả.

Authoritative DNS server chịu trách nhiệm trả lời records cho zone mà nó quản lý.

Mental model:

```text
application
    ↓
stub resolver
    ↓
recursive DNS resolver
    ↓
root / TLD / authoritative chain nếu cache miss
```

Trong doanh nghiệp, recursive resolver có thể là corporate DNS, cloud resolver hoặc local service.

## TTL và cache

DNS record có **TTL — Time To Live**, chỉ thời gian cache có thể giữ answer.

```bash
dig api.example.com
```

Output hiển thị TTL.

Nếu DNS record đổi từ IP A sang IP B, client không nhất thiết thấy B ngay. Resolver cache vẫn có thể trả A cho tới khi TTL hết.

Nhưng actual caching còn có thể tồn tại ở nhiều layer:

- recursive resolver;
- OS/local resolver;
- JVM;
- application cache;
- browser;
- proxy.

Do đó “DNS TTL là 60 giây” không đảm bảo mọi application refresh sau đúng 60 giây nếu runtime có cache riêng.

## Java DNS caching

JVM có cơ chế cache DNS result. Behavior phụ thuộc JVM/security properties/version.

Điều này có impact khi backend dependency thay IP nhưng application giữ connection hoặc DNS result quá lâu.

Không nên tùy tiện đặt DNS TTL JVM cực thấp hoặc bằng 0; DNS query volume và dependency behavior cũng cần cân nhắc.

Khi điều tra Java `UnknownHostException`, cần phân biệt:

- resolver thực sự không trả IP;
- JVM cache negative result;
- network tới DNS server lỗi;
- hostname config sai.

## Record A và AAAA

`A` record chứa IPv4 address.

`AAAA` record chứa IPv6 address.

```bash
dig A example.com
dig AAAA example.com
```

Một hostname có thể có cả hai. Application/runtime có thể thử IPv6 trước hoặc dùng Happy Eyeballs behavior.

Nếu IPv6 address resolve được nhưng IPv6 routing không hoạt động, connection có thể delay/fail theo cách khó hiểu.

Vì vậy DNS success không đồng nghĩa network reachability success.

## CNAME

**CNAME** tạo alias tới canonical name.

Ví dụ:

```text
api.example.com CNAME lb.example.net
```

Resolver tiếp tục resolve canonical target.

CNAME thường dùng cho CDN/load balancer service, nhưng chain dài có thể tăng resolution work và tạo dependency vào nhiều zones.

## MX, TXT, SRV và các record khác

DNS không chỉ lưu IP.

- `MX`: mail exchange;
- `TXT`: arbitrary text, thường dùng SPF/domain verification;
- `SRV`: service location với port/priority;
- `NS`: authoritative name servers;
- `PTR`: reverse DNS.

Service discovery systems có thể dùng SRV hoặc custom DNS schemes.

## NXDOMAIN và SERVFAIL khác nhau

`NXDOMAIN` nghĩa tên được hỏi không tồn tại theo DNS response.

`SERVFAIL` nghĩa resolver/server không thể hoàn thành query, ví dụ upstream/DNSSEC/delegation issue.

Hai lỗi này cần reasoning khác nhau.

```bash
dig nonexistent.example.com
```

Xem status trong header:

```text
status: NXDOMAIN
```

## Negative caching

Không chỉ successful answers được cache. Kết quả “không tồn tại” cũng có thể được cache theo DNS rules.

Do đó nếu record vừa được tạo sau khi client đã nhận NXDOMAIN, client/resolver có thể tiếp tục thấy failure một thời gian.

Đây là lý do “tôi vừa thêm DNS record rồi nhưng app vẫn không resolve” không nhất thiết do update thất bại.

## systemd-resolved

Một số Linux distributions dùng `systemd-resolved`.

Kiểm tra:

```bash
systemctl status systemd-resolved
resolvectl status
```

`resolvectl` có thể cho biết DNS server theo interface, search domains và current resolver state.

Query:

```bash
resolvectl query api.example.com
```

Điều này đặc biệt hữu ích khi VPN/interface khác nhau có DNS server riêng.

## Split DNS

Doanh nghiệp/VPN thường dùng **split DNS**: một số domains được resolve qua DNS nội bộ, các domains khác qua public resolver.

Ví dụ:

```text
*.corp.example.com → VPN DNS
other domains      → normal DNS
```

Nếu VPN route hoạt động nhưng DNS routing/config không đúng, user có thể ping internal IP nhưng không resolve internal hostname.

Đây là một ví dụ network routing và name resolution là hai control planes khác nhau.

## `dig`, `host`, `nslookup`, `getent`

Các tools trả lời câu hỏi khác nhau.

`dig` cho DNS protocol details:

```bash
dig api.example.com
```

`dig @server` hỏi resolver cụ thể:

```bash
dig @8.8.8.8 example.com
```

`getent hosts` đi qua NSS:

```bash
getent hosts api.example.com
```

`host` và `nslookup` tiện cho lookup nhanh nhưng `dig` thường chi tiết hơn.

Khi application fail nhưng `dig` success, hãy thử `getent` trước khi kết luận application bug.

## Tracing DNS bằng packet capture

DNS truyền thống thường dùng UDP 53, và TCP trong một số trường hợp. DNS over TLS/HTTPS thay đổi transport.

Với local resolver thông thường:

```bash
sudo tcpdump -ni any port 53
```

Sau đó chạy:

```bash
getent hosts api.example.com
```

Nếu không thấy packet DNS, answer có thể đến từ `/etc/hosts`, local cache hoặc resolver path khác.

Nếu query đi ra nhưng không có response, scope chuyển sang route/firewall/DNS server.

## DNS và container

Container runtime thường inject `/etc/resolv.conf` riêng vào container.

```bash
cat /etc/resolv.conf
```

bên host và container có thể khác.

Docker có embedded DNS ở một số network modes; Kubernetes thường dùng CoreDNS và service names.

Do đó “host resolve được nhưng container không resolve” không mâu thuẫn. Chúng đang dùng resolver context khác.

## Kubernetes connection

Trong Kubernetes, hostname như:

```text
service.namespace.svc.cluster.local
```

được cluster DNS resolve tới Service virtual IP hoặc records thích hợp.

Nếu CoreDNS unhealthy hoặc pod DNS config sai, application có thể báo dependency failure dù network route tới raw IP vẫn hoạt động.

Linux DNS fundamentals vẫn áp dụng; Kubernetes chỉ thêm service-discovery layer.

## DNS và load balancing

Một DNS name có thể trả nhiều A/AAAA records:

```text
api.example.com → 10.0.0.10
                  10.0.0.11
                  10.0.0.12
```

Client behavior quyết định nó dùng address nào và failover ra sao.

DNS round-robin không có health-awareness đầy đủ như application load balancer. Client có thể cache một IP đã unhealthy.

## Case: `curl` resolve được nhưng Java không

Kiểm tra Java process có đang dùng hostname giống hệt không, runtime cache thế nào, container namespace nào và resolver config nào.

Có thể kiểm tra OS:

```bash
getent ahosts api.example.com
```

rồi JVM/log application.

Không nên restart JVM chỉ để flush DNS mà chưa hiểu TTL/cache policy; restart có thể che architecture issue.

## Case: resolve chậm 5 giây

Potential causes:

- DNS server đầu tiên timeout rồi resolver thử server thứ hai;
- IPv6/AAAA behavior;
- search domain tạo nhiều queries;
- unreachable resolver qua VPN;
- packet drop/firewall;
- DNS server overloaded.

Quan sát:

```bash
time getent hosts api.example.com
resolvectl status
sudo tcpdump -ni any port 53
```

Timeline packet thường cho thấy query nào chờ timeout.

## DNSSEC

DNSSEC thêm cryptographic validation để chống giả mạo dữ liệu DNS trong trust chain. Nếu validation fail, resolver có thể trả `SERVFAIL` dù authoritative data tồn tại.

DNSSEC không mã hóa query; nó bảo vệ tính xác thực/toàn vẹn của DNS data.

Không nên nhầm DNSSEC với DNS over HTTPS (DoH) hoặc DNS over TLS (DoT), vốn tập trung vào transport confidentiality/integrity giữa client và resolver.

## Mô hình tư duy (Mental Model)

Khi resolve hostname, hãy nghĩ theo chuỗi:

```text
application
   ↓
NSS / resolver library
   ↓
/etc/hosts hoặc local resolver/cache
   ↓
configured recursive DNS
   ↓
DNS hierarchy / authoritative server
   ↓
A/AAAA/CNAME/... answer
   ↓
application cache
```

Sau khi có IP, networking mới tiếp tục với route/TCP/TLS.

DNS success chỉ giải quyết câu hỏi “địa chỉ nào?”, không giải quyết câu hỏi “có kết nối được không?”.

## Những hiểu lầm phổ biến

**“`dig` success nghĩa application chắc chắn resolve được.”** Application có thể đi qua NSS/cache/runtime khác.

**“DNS record đổi là mọi client thấy ngay.”** TTL và nhiều lớp cache làm propagation có độ trễ.

**“NXDOMAIN và timeout là cùng lỗi DNS.”** Một bên là negative answer; bên kia có thể là transport/resolver failure.

**“Host resolve được thì container cũng resolve được.”** Resolver configuration có thể khác theo namespace/runtime.

**“DNS chỉ có A record.”** DNS là hệ thống dữ liệu phân tán với nhiều record types.

**“DNSSEC mã hóa DNS.”** DNSSEC xác thực dữ liệu, không cung cấp transport encryption theo nghĩa DoH/DoT.

## Xem thêm

- [Networking, DNS, sockets và ports](./networking_dns_sockets_ports.md)
- [IP routing, NAT và conntrack](./ip_routing_nat_conntrack.md)
- [TCP, HTTP và TLS](./tcp_http_tls.md)
- [Reverse proxy và load balancing](./reverse_proxy_load_balancing.md)
- [Java backend incident playbook](../09_production/java_backend_incident_playbook.md)
