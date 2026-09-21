# TCP, HTTP và TLS dưới góc nhìn Linux

Một backend developer thường nhìn request ở tầng framework: controller nhận HTTP request, service gọi database, rồi response được trả về. Nhưng trước khi request tới Spring Boot, nhiều lớp đã phải hoạt động đúng: DNS, route, TCP handshake, socket, TLS handshake và HTTP protocol. Khi production gặp timeout hoặc `connection reset`, việc hiểu các lớp này giúp phân biệt lỗi ở đâu thay vì gộp tất cả thành “network issue”.

## Từ hostname tới HTTP request

Giả sử client gọi:

```text
https://api.example.com/orders
```

Đường đi đơn giản hóa:

```text
hostname
→ DNS lookup
→ IP address
→ route selection
→ TCP connection
→ TLS handshake
→ HTTP request
→ application handler
```

Mỗi bước có failure mode riêng. DNS lỗi khác TCP timeout; TCP thành công nhưng TLS fail khác HTTP 500.

## TCP là connection-oriented transport

TCP cung cấp một byte stream có thứ tự giữa hai endpoint. Endpoint thường được mô tả bằng IP + port.

Trước khi truyền application data, TCP thiết lập connection bằng three-way handshake:

```text
Client                      Server
  | ------- SYN ----------> |
  | <---- SYN, ACK -------- |
  | ------- ACK ----------> |
```

Nếu client ở `SYN-SENT` lâu, nó đã gửi yêu cầu kết nối nhưng chưa hoàn tất handshake.

```bash
ss -antp
```

có thể quan sát TCP states.

## TCP không biết HTTP

TCP chỉ cung cấp ordered byte stream. Nó không biết request path `/orders`, status code `500` hay JSON.

HTTP nằm phía trên TCP. Vì vậy:

```bash
nc -vz api.example.com 443
```

thành công chỉ chứng minh TCP connection có thể thiết lập tới endpoint đó. Nó chưa chứng minh TLS hoặc HTTP hoạt động.

## Connection refused

Nếu client nhận `Connection refused`, thường có phản hồi từ network stack cho biết endpoint không chấp nhận connection. Trường hợp phổ biến là không có listener trên IP/port đó hoặc firewall chủ động reject.

Server side kiểm tra:

```bash
sudo ss -lntp | grep ':8080'
```

Nếu Java process tồn tại nhưng không có `LISTEN`, cần điều tra startup/bind/application layer trước.

## Timeout

Timeout có thể xuất hiện ở nhiều tầng.

TCP connect timeout có thể do packet bị drop, route sai, firewall hoặc host không phản hồi. HTTP read timeout xảy ra sau khi connection đã được thiết lập nhưng application/upstream không trả dữ liệu đúng hạn.

Vì vậy câu “request timeout” chưa đủ. Cần biết timeout ở giai đoạn nào.

`curl -v` giúp nhìn progression:

```bash
curl -v https://api.example.com/health
```

Nếu output dừng trước `Connected to`, lỗi khác với trường hợp TLS hoàn tất rồi chờ HTTP response.

## TCP reset

`Connection reset by peer` thường nghĩa connection đã tồn tại nhưng phía bên kia hoặc thiết bị trung gian gửi RST để đóng đột ngột.

Nguyên nhân có thể là application crash, proxy timeout, firewall behavior hoặc process đóng socket theo trạng thái bất thường.

Packet capture có thể chứng minh ai gửi RST:

```bash
sudo tcpdump -ni any host 10.0.0.20 and port 8080
```

Không nên kết luận “server reset” chỉ từ thông báo ở client khi chưa xem path.

## TIME-WAIT

Sau khi connection đóng, một endpoint có thể giữ `TIME-WAIT` để xử lý segment cũ và tránh nhầm connection mới.

Nhiều `TIME-WAIT` không tự động là memory leak.

```bash
ss -ant state time-wait | wc -l
```

Nếu số lượng rất lớn và gây port pressure, cần xem connection reuse, client behavior, load pattern và ephemeral port range trước khi chỉnh kernel parameter.

## CLOSE-WAIT

`CLOSE-WAIT` nghĩa peer đã gửi FIN nhưng local process chưa đóng socket của mình.

Nhiều `CLOSE-WAIT` tồn tại lâu có thể gợi ý application không release connection đúng cách.

```bash
ss -antp state close-wait
```

Trong Java, cần liên hệ tới lifecycle của HTTP client, JDBC/socket hoặc stream resource.

## Ephemeral ports

Client khi mở outbound connection thường dùng một local ephemeral port.

Ví dụ:

```text
10.0.0.5:49152 → 10.0.0.20:443
```

Nếu application tạo lượng connection rất lớn mà không reuse, ephemeral ports có thể trở thành tài nguyên giới hạn.

Kiểm tra range:

```bash
cat /proc/sys/net/ipv4/ip_local_port_range
```

Không chỉnh range như giải pháp đầu tiên; connection pooling/keep-alive thường là câu hỏi kiến trúc quan trọng hơn.

## Listen backlog

Server socket có queue liên quan connection đang chờ được accept. Nếu application không accept đủ nhanh, backlog pressure có thể xuất hiện.

Điều này liên hệ trực tiếp tới thread pool/event loop và CPU saturation. Network symptom có thể bắt nguồn từ application capacity.

## HTTP request/response

HTTP/1.1 request đơn giản:

```http
GET /health HTTP/1.1
Host: api.example.com
Connection: keep-alive
```

Response:

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 15

{"status":"UP"}
```

Framework che phần lớn chi tiết này, nhưng khi debug proxy/header/body length/connection reuse, hiểu wire-level semantics rất hữu ích.

## Status code không giống transport failure

HTTP `500` nghĩa TCP/TLS/HTTP đã đi đủ xa để server gửi HTTP response có status 500.

Ngược lại `Connection refused` xảy ra trước khi HTTP request được trao đổi.

Điều này giúp xác định layer:

```text
HTTP 500 → application/proxy xử lý request rồi trả error
TCP refused → chưa có HTTP response
DNS error → còn chưa có IP endpoint
```

## HTTP keep-alive

Tạo TCP/TLS connection có chi phí. HTTP keep-alive cho phép reuse connection cho nhiều requests.

Connection pool trong Java HTTP client hoặc database driver tồn tại vì cùng nguyên lý: reuse expensive connections và giới hạn concurrency.

Nhưng pool quá nhỏ tạo queue; pool quá lớn có thể overload downstream. Linux socket state là một nguồn bằng chứng để quan sát pool behavior.

## HTTP/2

HTTP/2 có thể multiplex nhiều streams trên một TCP connection, giảm nhu cầu nhiều parallel TCP connections so với HTTP/1.1.

Tuy nhiên vì nhiều streams chia một TCP connection, packet loss và connection-level issue có thể ảnh hưởng nhiều requests cùng lúc.

`curl` có thể hiển thị protocol negotiated trong verbose output tùy build:

```bash
curl -v --http2 https://api.example.com/
```

## TLS nằm giữa TCP và HTTP

Với HTTPS:

```text
TCP connection
→ TLS handshake
→ encrypted HTTP
```

TLS cung cấp encryption, integrity và server authentication thông qua certificate validation.

Nếu TCP 443 connect được nhưng TLS handshake fail, firewall TCP cơ bản ít khả năng là nguyên nhân chính.

## Certificate chain

Server certificate thường được ký bởi intermediate CA, sau đó chain tới trusted root CA.

Client cần xây dựng trust chain hợp lệ và kiểm tra hostname, thời gian hiệu lực và các policy khác.

Kiểm tra bằng OpenSSL:

```bash
openssl s_client -connect api.example.com:443 -servername api.example.com
```

`-servername` gửi SNI, rất quan trọng khi nhiều HTTPS virtual hosts chia cùng IP.

## SNI

Server Name Indication (SNI) cho phép client gửi hostname trong TLS handshake để server chọn certificate phù hợp.

Nếu test chỉ bằng IP mà không gửi SNI, có thể nhận certificate mặc định khác với certificate production request nhận được.

Vì vậy khi debug HTTPS virtual host, hostname rất quan trọng.

## ALPN

Application-Layer Protocol Negotiation cho phép TLS handshake thống nhất protocol phía trên như HTTP/2 hoặc HTTP/1.1.

Đây là ví dụ networking stack không chỉ là các layer độc lập hoàn toàn; layer trên có thể được negotiated trong handshake layer dưới.

## TLS lỗi do clock

Certificate có `Not Before` và `Not After`. Nếu system clock sai, certificate hợp lệ có thể bị báo expired hoặc not yet valid.

```bash
date -u
timedatectl
```

Do đó TLS troubleshooting phải liên kết với [Time, Clock, Timezone và NTP](../05_system/time_clock_ntp.md).

## Proxy và reverse proxy

Production thường có:

```text
Client → Load Balancer / Nginx → Java application
```

Có thể có hai TCP connections riêng: client tới proxy và proxy tới backend.

Client nhận 502/504 không tự động nghĩa Java trả status đó. Proxy có thể tự tạo response vì upstream connect/read timeout.

Cần xem proxy log và backend log cùng timeline.

## 502 và 504

Ý nghĩa cụ thể phụ thuộc proxy, nhưng thường:

**502 Bad Gateway** gợi ý proxy không nhận được upstream response hợp lệ.

**504 Gateway Timeout** gợi ý proxy chờ upstream quá thời gian cấu hình.

Đây là signal để kiểm tra connection từ proxy tới backend, không chỉ từ laptop tới public endpoint.

## Local-first rồi đi ra ngoài

Nếu app listen 8080:

```bash
curl -v http://127.0.0.1:8080/health
```

Nếu local fail, lỗi nằm trước external load balancer trong dependency chain.

Nếu local success nhưng request qua domain fail:

```bash
dig +short api.example.com
curl -v https://api.example.com/health
```

thì scope chuyển sang DNS, TLS, proxy, firewall hoặc route.

## Packet capture như bằng chứng cuối cùng

```bash
sudo tcpdump -ni any port 8080
```

Cho phép thấy SYN, ACK, FIN, RST và traffic tới host.

Nếu cần phân tích sâu:

```bash
sudo tcpdump -ni any port 8080 -w /tmp/app.pcap
```

Sau đó mở bằng Wireshark ở môi trường phù hợp. Capture có thể chứa dữ liệu nhạy cảm; phải xử lý như incident artifact.

## Mô hình tư duy (Mental Model)

Khi request lỗi, hãy đặt nó vào chuỗi:

```text
DNS
→ route
→ TCP handshake
→ socket/listener
→ TLS handshake
→ HTTP exchange
→ proxy
→ application handler
→ downstream dependency
```

Không cần kiểm tra từng bước nếu đã có evidence mạnh, nhưng phải biết bước nào đã được chứng minh và bước nào chỉ đang giả định.

## Những hiểu lầm phổ biến

**“Port 443 mở nghĩa HTTPS khỏe.”** TCP listener không chứng minh TLS/certificate/HTTP đúng.

**“HTTP 500 là network error.”** HTTP response đã được tạo, nghĩa request đã đi qua nhiều layer network thành công.

**“TIME-WAIT nhiều chắc chắn là bug.”** Đây là TCP state bình thường; cần context về rate và resource pressure.

**“curl localhost thành công nghĩa user bên ngoài phải truy cập được.”** External path còn DNS, bind address, firewall, proxy và load balancer.

**“Certificate đúng trên browser nghĩa mọi client đều đúng.”** Trust store, SNI, protocol version và clock có thể khác giữa client.

## Kết nối kiến thức

Chương này mở rộng [Networking, DNS, Sockets và Ports](./networking_dns_sockets_ports.md), liên hệ [File Descriptors](../01_filesystem/files_streams_descriptors.md), [Time/NTP](../05_system/time_clock_ntp.md), [Java Backend Incident Playbook](../09_production/java_backend_incident_playbook.md) và [Production Troubleshooting](../09_production/production_troubleshooting.md).