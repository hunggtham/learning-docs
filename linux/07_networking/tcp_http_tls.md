# TCP, HTTP và TLS dưới góc nhìn Linux

> **Mạch đọc:** Đọc **TCP, HTTP và TLS dưới góc nhìn Linux** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Từ hostname tới HTTP yêu cầu (request / 요청)** sang **TCP là connection-oriented vận chuyển (transport / 전송)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một backend nhà phát triển (developer / 개발자) thường nhìn yêu cầu (request / 요청) ở tầng khung phần mềm (framework / 프레임워크): controller nhận HTTP yêu cầu (request / 요청), dịch vụ (service / 서비스) gọi cơ sở dữ liệu (database / 데이터베이스), rồi phản hồi (response / 응답) được trả về. Nhưng trước khi yêu cầu (request / 요청) tới Spring Boot, nhiều lớp đã phải hoạt động đúng: DNS, tuyến (route / 경로), TCP handshake, socket, TLS handshake và HTTP giao thức (protocol / 프로토콜). Khi môi trường vận hành (production / 운영 환경) gặp hết thời gian chờ (timeout / 타임아웃) hoặc `connection reset`, việc hiểu các lớp này giúp phân biệt lỗi ở đâu thay vì gộp tất cả thành “mạng (network / 네트워크) issue”.

## Từ hostname tới HTTP yêu cầu (request / 요청)

Giả sử máy khách (client / 클라이언트) gọi:

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

Mỗi bước có dạng thất bại (failure mode / 실패 모드) riêng. DNS lỗi khác TCP hết thời gian chờ (timeout / 타임아웃); TCP thành công nhưng TLS thất bại (fail / 실패) khác HTTP 500.

## TCP là connection-oriented vận chuyển (transport / 전송)

TCP cung cấp một byte stream có thứ tự giữa hai endpoint. Endpoint thường được mô tả bằng IP + cổng (port / 포트).

Trước khi truyền ứng dụng (application / 애플리케이션) dữ liệu (data / 데이터), TCP thiết lập liên kết (connection / 연결) bằng three-way handshake:

```text
Client                      Server
  | ------- SYN ----------> |
  | <---- SYN, ACK -------- |
  | ------- ACK ----------> |
```

Nếu máy khách (client / 클라이언트) ở `SYN-SENT` lâu, nó đã gửi yêu cầu kết nối nhưng chưa hoàn tất handshake.

```bash
ss -antp
```

có thể quan sát TCP states.

## TCP không biết HTTP

TCP chỉ cung cấp ordered byte stream. Nó không biết đường đi của yêu cầu (request path / 요청 경로) `/orders`, status mã (code / 코드) `500` hay JSON.

HTTP nằm phía trên TCP. Vì vậy:

```bash
nc -vz api.example.com 443
```

thành công chỉ chứng minh TCP liên kết (connection / 연결) có thể thiết lập tới endpoint đó. Nó chưa chứng minh TLS hoặc HTTP hoạt động.

## Liên kết (connection / 연결) refused

Nếu máy khách (client / 클라이언트) nhận `Connection refused`, thường có phản hồi từ mạng (network / 네트워크) ngăn xếp (stack / 스택) cho biết endpoint không chấp nhận liên kết (connection / 연결). Trường hợp phổ biến là không có listener trên IP/cổng (port / 포트) đó hoặc firewall chủ động reject.

Máy chủ (server / 서버) side kiểm tra:

```bash
sudo ss -lntp | grep ':8080'
```

Nếu Java tiến trình (process / 프로세스) tồn tại nhưng không có `LISTEN`, cần điều tra startup/bind/ứng dụng (application / 애플리케이션) tầng (layer / 계층) trước.

## Hết thời gian chờ (timeout / 타임아웃)

Hết thời gian chờ (timeout / 타임아웃) có thể xuất hiện ở nhiều tầng.

TCP connect hết thời gian chờ (timeout / 타임아웃) có thể do packet bị drop, tuyến (route / 경로) sai, firewall hoặc host không phản hồi. HTTP read hết thời gian chờ (timeout / 타임아웃) xảy ra sau khi liên kết (connection / 연결) đã được thiết lập nhưng ứng dụng (application / 애플리케이션)/upstream không trả dữ liệu đúng hạn.

Vì vậy câu “yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃)” chưa đủ. Cần biết hết thời gian chờ (timeout / 타임아웃) ở giai đoạn nào.

`curl -v` giúp nhìn progression:

```bash
curl -v https://api.example.com/health
```

Nếu đầu ra (output / 출력) dừng trước `Connected to`, lỗi khác với trường hợp TLS hoàn tất rồi chờ HTTP phản hồi (response / 응답).

## TCP reset

`Connection reset by peer` thường nghĩa liên kết (connection / 연결) đã tồn tại nhưng phía bên kia hoặc thiết bị trung gian gửi RST để đóng đột ngột.

Nguyên nhân có thể là ứng dụng (application / 애플리케이션) crash, proxy hết thời gian chờ (timeout / 타임아웃), firewall hành vi (behavior / 동작) hoặc tiến trình (process / 프로세스) đóng socket theo trạng thái bất thường.

Packet capture có thể chứng minh ai gửi RST:

```bash
sudo tcpdump -ni any host 10.0.0.20 and port 8080
```

Không nên kết luận “máy chủ (server / 서버) reset” chỉ từ thông báo ở máy khách (client / 클라이언트) khi chưa xem đường dẫn (path / 경로).

## TIME-WAIT

Sau khi liên kết (connection / 연결) đóng, một endpoint có thể giữ `TIME-WAIT` để xử lý segment cũ và tránh nhầm liên kết (connection / 연결) mới.

Nhiều `TIME-WAIT` không tự động là bộ nhớ (memory / 메모리) leak.

```bash
ss -ant state time-wait | wc -l
```

Nếu số lượng rất lớn và gây cổng (port / 포트) pressure, cần xem liên kết (connection / 연결) reuse, máy khách (client / 클라이언트) hành vi (behavior / 동작), tải (load / 로드) mẫu (pattern / 패턴) và ephemeral cổng (port / 포트) phạm vi (range / 범위) trước khi chỉnh kernel parameter.

## CLOSE-WAIT

`CLOSE-WAIT` nghĩa peer đã gửi FIN nhưng cục bộ (local / 로컬) tiến trình (process / 프로세스) chưa đóng socket của mình.

Nhiều `CLOSE-WAIT` tồn tại lâu có thể gợi ý ứng dụng (application / 애플리케이션) không bản phát hành (release / 릴리스) liên kết (connection / 연결) đúng cách.

```bash
ss -antp state close-wait
```

Trong Java, cần liên hệ tới vòng đời (lifecycle / 생명주기) của HTTP máy khách (client / 클라이언트), JDBC/socket hoặc stream tài nguyên (resource / 자원).

## Ephemeral ports

Máy khách (client / 클라이언트) khi mở outbound liên kết (connection / 연결) thường dùng một cục bộ (local / 로컬) ephemeral cổng (port / 포트).

Ví dụ:

```text
10.0.0.5:49152 → 10.0.0.20:443
```

Nếu ứng dụng (application / 애플리케이션) tạo lượng liên kết (connection / 연결) rất lớn mà không reuse, ephemeral ports có thể trở thành tài nguyên giới hạn.

Kiểm tra phạm vi (range / 범위):

```bash
cat /proc/sys/net/ipv4/ip_local_port_range
```

Không chỉnh phạm vi (range / 범위) như giải pháp đầu tiên; liên kết (connection / 연결) pooling/keep-alive thường là câu hỏi kiến trúc quan trọng hơn.

## Listen backlog

Máy chủ (server / 서버) socket có hàng đợi (queue / 큐) liên quan liên kết (connection / 연결) đang chờ được accept. Nếu ứng dụng (application / 애플리케이션) không accept đủ nhanh, backlog pressure có thể xuất hiện.

Điều này liên hệ trực tiếp tới luồng thực thi (thread / 스레드) pool/vòng lặp sự kiện (event loop / 이벤트 루프) và CPU saturation. mạng (network / 네트워크) symptom có thể bắt nguồn từ ứng dụng (application / 애플리케이션) sức chứa (capacity / 용량).

## HTTP yêu cầu (request / 요청)/phản hồi (response / 응답)

HTTP/1.1 yêu cầu (request / 요청) đơn giản:

```http
GET /health HTTP/1.1
Host: api.example.com
Connection: keep-alive
```

Phản hồi (response / 응답):

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 15

{"status":"UP"}
```

Khung phần mềm (framework / 프레임워크) che phần lớn chi tiết này, nhưng khi gỡ lỗi (debug / 디버그) proxy/header/body length/liên kết (connection / 연결) reuse, hiểu wire-level ngữ nghĩa (semantics / 의미론) rất hữu ích.

## Status mã (code / 코드) không giống vận chuyển (transport / 전송) thất bại (failure / 실패)

HTTP `500` nghĩa TCP/TLS/HTTP đã đi đủ xa để máy chủ (server / 서버) gửi HTTP phản hồi (response / 응답) có status 500.

Ngược lại `Connection refused` xảy ra trước khi HTTP yêu cầu (request / 요청) được trao đổi.

Điều này giúp xác định tầng (layer / 계층):

```text
HTTP 500 → application/proxy xử lý request rồi trả error
TCP refused → chưa có HTTP response
DNS error → còn chưa có IP endpoint
```

## HTTP keep-alive

Tạo TCP/TLS liên kết (connection / 연결) có chi phí. HTTP keep-alive cho phép reuse liên kết (connection / 연결) cho nhiều requests.

Liên kết (connection / 연결) pool trong Java HTTP máy khách (client / 클라이언트) hoặc cơ sở dữ liệu (database / 데이터베이스) driver tồn tại vì cùng nguyên lý: reuse expensive connections và giới hạn tính đồng thời (concurrency / 동시성).

Nhưng pool quá nhỏ tạo hàng đợi (queue / 큐); pool quá lớn có thể overload downstream. Linux socket trạng thái (state / 상태) là một nguồn bằng chứng để quan sát pool hành vi (behavior / 동작).

## HTTP/2

HTTP/2 có thể multiplex nhiều streams trên một TCP liên kết (connection / 연결), giảm nhu cầu nhiều parallel TCP connections so với HTTP/1.1.

Tuy nhiên vì nhiều streams chia một TCP liên kết (connection / 연결), packet mất mát (loss / 손실) và connection-level issue có thể ảnh hưởng nhiều requests cùng lúc.

`curl` có thể hiển thị giao thức (protocol / 프로토콜) negotiated trong verbose đầu ra (output / 출력) tùy bản dựng (build / 빌드):

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

TLS cung cấp encryption, integrity và máy chủ (server / 서버) authentication thông qua certificate kiểm tra hợp lệ (validation / 검증).

Nếu TCP 443 connect được nhưng TLS handshake thất bại (fail / 실패), firewall TCP cơ bản ít khả năng là nguyên nhân chính.

## Certificate chuỗi (chain / 사슬)

Máy chủ (server / 서버) certificate thường được ký bởi intermediate CA, sau đó chuỗi (chain / 사슬) tới trusted gốc (root / 루트) CA.

Máy khách (client / 클라이언트) cần xây dựng trust chuỗi (chain / 사슬) hợp lệ và kiểm tra hostname, thời gian hiệu lực và các chính sách (policy / 정책) khác.

Kiểm tra bằng OpenSSL:

```bash
openssl s_client -connect api.example.com:443 -servername api.example.com
```

`-servername` gửi SNI, rất quan trọng khi nhiều HTTPS virtual hosts chia cùng IP.

## SNI

Máy chủ (server / 서버) Name Indication (SNI) cho phép máy khách (client / 클라이언트) gửi hostname trong TLS handshake để máy chủ (server / 서버) chọn certificate phù hợp.

Nếu kiểm thử (test / 테스트) chỉ bằng IP mà không gửi SNI, có thể nhận certificate mặc định khác với certificate môi trường vận hành (production / 운영 환경) yêu cầu (request / 요청) nhận được.

Vì vậy khi gỡ lỗi (debug / 디버그) HTTPS virtual host, hostname rất quan trọng.

## ALPN

Application-Layer giao thức (protocol / 프로토콜) Negotiation cho phép TLS handshake thống nhất giao thức (protocol / 프로토콜) phía trên như HTTP/2 hoặc HTTP/1.1.

Đây là ví dụ networking ngăn xếp (stack / 스택) không chỉ là các tầng (layer / 계층) độc lập hoàn toàn; tầng (layer / 계층) trên có thể được negotiated trong handshake tầng (layer / 계층) dưới.

## TLS lỗi do clock

Certificate có `Not Before` và `Not After`. Nếu hệ thống (system / 시스템) clock sai, certificate hợp lệ có thể bị báo expired hoặc not yet valid.

```bash
date -u
timedatectl
```

Do đó TLS troubleshooting phải liên kết với [Time, Clock, Timezone và NTP](../05_system/time_clock_ntp.md).

## Proxy và reverse proxy

Môi trường vận hành (production / 운영 환경) thường có:

```text
Client → Load Balancer / Nginx → Java application
```

Có thể có hai TCP connections riêng: máy khách (client / 클라이언트) tới proxy và proxy tới backend.

Máy khách (client / 클라이언트) nhận 502/504 không tự động nghĩa Java trả status đó. Proxy có thể tự tạo phản hồi (response / 응답) vì upstream connect/read hết thời gian chờ (timeout / 타임아웃).

Cần xem proxy log và backend log cùng timeline.

## 502 và 504

Ý nghĩa cụ thể phụ thuộc proxy, nhưng thường:

**502 Bad Gateway** gợi ý proxy không nhận được upstream phản hồi (response / 응답) hợp lệ.

**504 Gateway hết thời gian chờ (timeout / 타임아웃)** gợi ý proxy chờ upstream quá thời gian cấu hình.

Đây là tín hiệu (signal / 신호) để kiểm tra liên kết (connection / 연결) từ proxy tới backend, không chỉ từ laptop tới công khai (public / 공개) endpoint.

## Local-first rồi đi ra ngoài

Nếu app listen 8080:

```bash
curl -v http://127.0.0.1:8080/health
```

Nếu cục bộ (local / 로컬) thất bại (fail / 실패), lỗi nằm trước bên ngoài (external / 외부) bộ cân bằng tải (load balancer / 로드 밸런서) trong phụ thuộc (dependency / 의존성) chuỗi (chain / 사슬).

Nếu cục bộ (local / 로컬) success nhưng yêu cầu (request / 요청) qua lĩnh vực (domain / 도메인) thất bại (fail / 실패):

```bash
dig +short api.example.com
curl -v https://api.example.com/health
```

thì phạm vi (scope / 범위) chuyển sang DNS, TLS, proxy, firewall hoặc tuyến (route / 경로).

## Packet capture như bằng chứng cuối cùng

```bash
sudo tcpdump -ni any port 8080
```

Cho phép thấy SYN, ACK, FIN, RST và traffic tới host.

Nếu cần phân tích sâu:

```bash
sudo tcpdump -ni any port 8080 -w /tmp/app.pcap
```

Sau đó mở bằng Wireshark ở môi trường phù hợp. Capture có thể chứa dữ liệu nhạy cảm; phải xử lý như sự cố (incident / 인시던트) sản phẩm tạo ra (artifact / 산출물).

## Mô hình tư duy (mental model / 사고 모델)

Khi yêu cầu (request / 요청) lỗi, hãy đặt nó vào chuỗi:

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

Không cần kiểm tra từng bước nếu đã có bằng chứng (evidence / 증거) mạnh, nhưng phải biết bước nào đã được chứng minh và bước nào chỉ đang giả định.

## Những hiểu lầm phổ biến

**“cổng (port / 포트) 443 mở nghĩa HTTPS khỏe.”** TCP listener không chứng minh TLS/certificate/HTTP đúng.

**“HTTP 500 là mạng (network / 네트워크) lỗi (error / 오류).”** HTTP phản hồi (response / 응답) đã được tạo, nghĩa yêu cầu (request / 요청) đã đi qua nhiều tầng (layer / 계층) mạng (network / 네트워크) thành công.

**“TIME-WAIT nhiều chắc chắn là bug.”** Đây là TCP trạng thái (state / 상태) bình thường; cần ngữ cảnh (context / 맥락) về tỷ lệ (rate / 비율) và tài nguyên (resource / 자원) pressure.

**“curl localhost thành công nghĩa người dùng (user / 사용자) bên ngoài phải truy cập được.”** bên ngoài (external / 외부) đường dẫn (path / 경로) còn DNS, bind address, firewall, proxy và bộ cân bằng tải (load balancer / 로드 밸런서).

**“Certificate đúng trên trình duyệt (browser / 브라우저) nghĩa mọi máy khách (client / 클라이언트) đều đúng.”** Trust store, SNI, giao thức (protocol / 프로토콜) phiên bản (version / 버전) và clock có thể khác giữa máy khách (client / 클라이언트).

## Kết nối kiến thức

Chương này mở rộng [Networking, DNS, Sockets và Ports](./networking_dns_sockets_ports.md), liên hệ [File Descriptors](../01_filesystem/files_streams_descriptors.md), [Time/NTP](../05_system/time_clock_ntp.md), [Java Backend Incident Playbook](../09_production/java_backend_incident_playbook.md) và [Production Troubleshooting](../09_production/production_troubleshooting.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [dns resolution internals](./dns_resolution_internals.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
