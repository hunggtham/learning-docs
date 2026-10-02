# TCP, HTTP và TLS dưới góc nhìn Linux

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **TCP, HTTP và TLS dưới góc nhìn Linux**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Từ hostname tới HTTP yêu cầu (request / 요청)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **TCP là connection-oriented vận chuyển (transport / 전송)** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối TCP, HTTP và TLS thành một request path, để phân biệt lỗi transport, handshake và giao thức ứng dụng.

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

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **TCP là connection-oriented vận chuyển (transport / 전송)** tiếp nhận điểm tựa từ **Từ hostname tới HTTP yêu cầu (request / 요청)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TCP không biết HTTP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, **TCP không biết HTTP** tiếp nhận điểm tựa từ **TCP là connection-oriented vận chuyển (transport / 전송)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) refused** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TCP không biết HTTP

TCP chỉ cung cấp ordered byte stream. Nó không biết đường đi của yêu cầu (request path / 요청 경로) `/orders`, status mã (code / 코드) `500` hay JSON.

HTTP nằm phía trên TCP. Vì vậy:

```bash
nc -vz api.example.com 443
```

thành công chỉ chứng minh TCP liên kết (connection / 연결) có thể thiết lập tới endpoint đó. Nó chưa chứng minh TLS hoặc HTTP hoạt động.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, sau nội dung của **TCP không biết HTTP**, **Liên kết (connection / 연결) refused** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Hết thời gian chờ (timeout / 타임아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) refused

Nếu máy khách (client / 클라이언트) nhận `Connection refused`, thường có phản hồi từ mạng (network / 네트워크) ngăn xếp (stack / 스택) cho biết endpoint không chấp nhận liên kết (connection / 연결). Trường hợp phổ biến là không có listener trên IP/cổng (port / 포트) đó hoặc firewall chủ động reject.

Máy chủ (server / 서버) side kiểm tra:

```bash
sudo ss -lntp | grep ':8080'
```

Nếu Java tiến trình (process / 프로세스) tồn tại nhưng không có `LISTEN`, cần điều tra startup/bind/ứng dụng (application / 애플리케이션) tầng (layer / 계층) trước.

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **Hết thời gian chờ (timeout / 타임아웃)** tiếp nhận điểm tựa từ **Liên kết (connection / 연결) refused** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TCP reset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hết thời gian chờ (timeout / 타임아웃)

Hết thời gian chờ (timeout / 타임아웃) có thể xuất hiện ở nhiều tầng.

TCP connect hết thời gian chờ (timeout / 타임아웃) có thể do packet bị drop, tuyến (route / 경로) sai, firewall hoặc host không phản hồi. HTTP read hết thời gian chờ (timeout / 타임아웃) xảy ra sau khi liên kết (connection / 연결) đã được thiết lập nhưng ứng dụng (application / 애플리케이션)/upstream không trả dữ liệu đúng hạn.

Vì vậy câu “yêu cầu (request / 요청) hết thời gian chờ (timeout / 타임아웃)” chưa đủ. Cần biết hết thời gian chờ (timeout / 타임아웃) ở giai đoạn nào.

`curl -v` giúp nhìn progression:

```bash
curl -v https://api.example.com/health
```

Nếu đầu ra (output / 출력) dừng trước `Connected to`, lỗi khác với trường hợp TLS hoàn tất rồi chờ HTTP phản hồi (response / 응답).

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, **TCP reset** tiếp nhận điểm tựa từ **Hết thời gian chờ (timeout / 타임아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TIME-WAIT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TCP reset

`Connection reset by peer` thường nghĩa liên kết (connection / 연결) đã tồn tại nhưng phía bên kia hoặc thiết bị trung gian gửi RST để đóng đột ngột.

Nguyên nhân có thể là ứng dụng (application / 애플리케이션) crash, proxy hết thời gian chờ (timeout / 타임아웃), firewall hành vi (behavior / 동작) hoặc tiến trình (process / 프로세스) đóng socket theo trạng thái bất thường.

Packet capture có thể chứng minh ai gửi RST:

```bash
sudo tcpdump -ni any host 10.0.0.20 and port 8080
```

Không nên kết luận “máy chủ (server / 서버) reset” chỉ từ thông báo ở máy khách (client / 클라이언트) khi chưa xem đường dẫn (path / 경로).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, **TIME-WAIT** tiếp nhận điểm tựa từ **TCP reset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CLOSE-WAIT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TIME-WAIT

Sau khi liên kết (connection / 연결) đóng, một endpoint có thể giữ `TIME-WAIT` để xử lý segment cũ và tránh nhầm liên kết (connection / 연결) mới.

Nhiều `TIME-WAIT` không tự động là bộ nhớ (memory / 메모리) leak.

```bash
ss -ant state time-wait | wc -l
```

Nếu số lượng rất lớn và gây cổng (port / 포트) pressure, cần xem liên kết (connection / 연결) reuse, máy khách (client / 클라이언트) hành vi (behavior / 동작), tải (load / 로드) mẫu (pattern / 패턴) và ephemeral cổng (port / 포트) phạm vi (range / 범위) trước khi chỉnh kernel parameter.

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **CLOSE-WAIT** tiếp nhận điểm tựa từ **TIME-WAIT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ephemeral ports** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CLOSE-WAIT

`CLOSE-WAIT` nghĩa peer đã gửi FIN nhưng cục bộ (local / 로컬) tiến trình (process / 프로세스) chưa đóng socket của mình.

Nhiều `CLOSE-WAIT` tồn tại lâu có thể gợi ý ứng dụng (application / 애플리케이션) không bản phát hành (release / 릴리스) liên kết (connection / 연결) đúng cách.

```bash
ss -antp state close-wait
```

Trong Java, cần liên hệ tới vòng đời (lifecycle / 생명주기) của HTTP máy khách (client / 클라이언트), JDBC/socket hoặc stream tài nguyên (resource / 자원).

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, **Ephemeral ports** tiếp nhận điểm tựa từ **CLOSE-WAIT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Listen backlog** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, **Listen backlog** tiếp nhận điểm tựa từ **Ephemeral ports** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HTTP yêu cầu (request / 요청)/phản hồi (response / 응답)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Listen backlog

Máy chủ (server / 서버) socket có hàng đợi (queue / 큐) liên quan liên kết (connection / 연결) đang chờ được accept. Nếu ứng dụng (application / 애플리케이션) không accept đủ nhanh, backlog pressure có thể xuất hiện.

Điều này liên hệ trực tiếp tới luồng thực thi (thread / 스레드) pool/vòng lặp sự kiện (event loop / 이벤트 루프) và CPU saturation. mạng (network / 네트워크) symptom có thể bắt nguồn từ ứng dụng (application / 애플리케이션) sức chứa (capacity / 용량).

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **HTTP yêu cầu (request / 요청)/phản hồi (response / 응답)** tiếp nhận điểm tựa từ **Listen backlog** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Status mã (code / 코드) không giống vận chuyển (transport / 전송) thất bại (failure / 실패)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, **Status mã (code / 코드) không giống vận chuyển (transport / 전송) thất bại (failure / 실패)** tiếp nhận điểm tựa từ **HTTP yêu cầu (request / 요청)/phản hồi (response / 응답)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HTTP keep-alive** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Status mã (code / 코드) không giống vận chuyển (transport / 전송) thất bại (failure / 실패)

HTTP `500` nghĩa TCP/TLS/HTTP đã đi đủ xa để máy chủ (server / 서버) gửi HTTP phản hồi (response / 응답) có status 500.

Ngược lại `Connection refused` xảy ra trước khi HTTP yêu cầu (request / 요청) được trao đổi.

Điều này giúp xác định tầng (layer / 계층):

```text
HTTP 500 → application/proxy xử lý request rồi trả error
TCP refused → chưa có HTTP response
DNS error → còn chưa có IP endpoint
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, **HTTP keep-alive** tiếp nhận điểm tựa từ **Status mã (code / 코드) không giống vận chuyển (transport / 전송) thất bại (failure / 실패)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HTTP/2** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HTTP keep-alive

Tạo TCP/TLS liên kết (connection / 연결) có chi phí. HTTP keep-alive cho phép reuse liên kết (connection / 연결) cho nhiều requests.

Liên kết (connection / 연결) pool trong Java HTTP máy khách (client / 클라이언트) hoặc cơ sở dữ liệu (database / 데이터베이스) driver tồn tại vì cùng nguyên lý: reuse expensive connections và giới hạn tính đồng thời (concurrency / 동시성).

Nhưng pool quá nhỏ tạo hàng đợi (queue / 큐); pool quá lớn có thể overload downstream. Linux socket trạng thái (state / 상태) là một nguồn bằng chứng để quan sát pool hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **HTTP/2** tiếp nhận điểm tựa từ **HTTP keep-alive** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TLS nằm giữa TCP và HTTP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HTTP/2

HTTP/2 có thể multiplex nhiều streams trên một TCP liên kết (connection / 연결), giảm nhu cầu nhiều parallel TCP connections so với HTTP/1.1.

Tuy nhiên vì nhiều streams chia một TCP liên kết (connection / 연결), packet mất mát (loss / 손실) và connection-level issue có thể ảnh hưởng nhiều requests cùng lúc.

`curl` có thể hiển thị giao thức (protocol / 프로토콜) negotiated trong verbose đầu ra (output / 출력) tùy bản dựng (build / 빌드):

```bash
curl -v --http2 https://api.example.com/
```

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, **TLS nằm giữa TCP và HTTP** tiếp nhận điểm tựa từ **HTTP/2** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Certificate chuỗi (chain / 사슬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLS nằm giữa TCP và HTTP

Với HTTPS:

```text
TCP connection
→ TLS handshake
→ encrypted HTTP
```

TLS cung cấp encryption, integrity và máy chủ (server / 서버) authentication thông qua certificate kiểm tra hợp lệ (validation / 검증).

Nếu TCP 443 connect được nhưng TLS handshake thất bại (fail / 실패), firewall TCP cơ bản ít khả năng là nguyên nhân chính.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, **TLS nằm giữa TCP và HTTP** xác định đầu vào; **Certificate chuỗi (chain / 사슬)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **SNI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Certificate chuỗi (chain / 사슬)

Máy chủ (server / 서버) certificate thường được ký bởi intermediate CA, sau đó chuỗi (chain / 사슬) tới trusted gốc (root / 루트) CA.

Máy khách (client / 클라이언트) cần xây dựng trust chuỗi (chain / 사슬) hợp lệ và kiểm tra hostname, thời gian hiệu lực và các chính sách (policy / 정책) khác.

Kiểm tra bằng OpenSSL:

```bash
openssl s_client -connect api.example.com:443 -servername api.example.com
```

`-servername` gửi SNI, rất quan trọng khi nhiều HTTPS virtual hosts chia cùng IP.

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **Certificate chuỗi (chain / 사슬)** xác định đầu vào; **SNI** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **ALPN** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SNI

Máy chủ (server / 서버) Name Indication (SNI) cho phép máy khách (client / 클라이언트) gửi hostname trong TLS handshake để máy chủ (server / 서버) chọn certificate phù hợp.

Nếu kiểm thử (test / 테스트) chỉ bằng IP mà không gửi SNI, có thể nhận certificate mặc định khác với certificate môi trường vận hành (production / 운영 환경) yêu cầu (request / 요청) nhận được.

Vì vậy khi gỡ lỗi (debug / 디버그) HTTPS virtual host, hostname rất quan trọng.

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, **ALPN** tiếp nhận điểm tựa từ **SNI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TLS lỗi do clock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ALPN

Application-Layer giao thức (protocol / 프로토콜) Negotiation cho phép TLS handshake thống nhất giao thức (protocol / 프로토콜) phía trên như HTTP/2 hoặc HTTP/1.1.

Đây là ví dụ networking ngăn xếp (stack / 스택) không chỉ là các tầng (layer / 계층) độc lập hoàn toàn; tầng (layer / 계층) trên có thể được negotiated trong handshake tầng (layer / 계층) dưới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, **TLS lỗi do clock** tiếp nhận điểm tựa từ **ALPN** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Proxy và reverse proxy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TLS lỗi do clock

Certificate có `Not Before` và `Not After`. Nếu hệ thống (system / 시스템) clock sai, certificate hợp lệ có thể bị báo expired hoặc not yet valid.

```bash
date -u
timedatectl
```

Do đó TLS troubleshooting phải liên kết với [Time, Clock, Timezone và NTP](../05_system/time_clock_ntp.md).

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **Proxy và reverse proxy** tiếp nhận điểm tựa từ **TLS lỗi do clock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **502 và 504** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Proxy và reverse proxy

Môi trường vận hành (production / 운영 환경) thường có:

```text
Client → Load Balancer / Nginx → Java application
```

Có thể có hai TCP connections riêng: máy khách (client / 클라이언트) tới proxy và proxy tới backend.

Máy khách (client / 클라이언트) nhận 502/504 không tự động nghĩa Java trả status đó. Proxy có thể tự tạo phản hồi (response / 응답) vì upstream connect/read hết thời gian chờ (timeout / 타임아웃).

Cần xem proxy log và backend log cùng timeline.

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, **502 và 504** tiếp nhận điểm tựa từ **Proxy và reverse proxy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Local-first rồi đi ra ngoài** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 502 và 504

Ý nghĩa cụ thể phụ thuộc proxy, nhưng thường:

**502 Bad Gateway** gợi ý proxy không nhận được upstream phản hồi (response / 응답) hợp lệ.

**504 Gateway hết thời gian chờ (timeout / 타임아웃)** gợi ý proxy chờ upstream quá thời gian cấu hình.

Đây là tín hiệu (signal / 신호) để kiểm tra liên kết (connection / 연결) từ proxy tới backend, không chỉ từ laptop tới công khai (public / 공개) endpoint.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, **Local-first rồi đi ra ngoài** tiếp nhận điểm tựa từ **502 và 504** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Packet capture như bằng chứng cuối cùng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **Local-first rồi đi ra ngoài** nêu điều cần giải thích; **Packet capture như bằng chứng cuối cùng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Packet capture như bằng chứng cuối cùng

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
sudo tcpdump -ni any port 8080
```

Cho phép thấy SYN, ACK, FIN, RST và traffic tới host.

Nếu cần phân tích sâu:

```bash
sudo tcpdump -ni any port 8080 -w /tmp/app.pcap
```

Sau đó mở bằng Wireshark ở môi trường phù hợp. Capture có thể chứa dữ liệu nhạy cảm; phải xử lý như sự cố (incident / 인시던트) sản phẩm tạo ra (artifact / 산출물).

> **Chuyển mạch:** Ở chặng này của **TCP, HTTP và TLS dưới góc nhìn Linux**, các dấu vết trong **Packet capture như bằng chứng cuối cùng** được đọc cùng nhau ở **Mô hình tư duy (mental model / 사고 모델)** để rút ra mô hình, thay vì giữ chúng như những quan sát rời. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **TCP, HTTP và TLS dưới góc nhìn Linux**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“cổng (port / 포트) 443 mở nghĩa HTTPS khỏe.”** TCP listener không chứng minh TLS/certificate/HTTP đúng.

**“HTTP 500 là mạng (network / 네트워크) lỗi (error / 오류).”** HTTP phản hồi (response / 응답) đã được tạo, nghĩa yêu cầu (request / 요청) đã đi qua nhiều tầng (layer / 계층) mạng (network / 네트워크) thành công.

**“TIME-WAIT nhiều chắc chắn là bug.”** Đây là TCP trạng thái (state / 상태) bình thường; cần ngữ cảnh (context / 맥락) về tỷ lệ (rate / 비율) và tài nguyên (resource / 자원) pressure.

**“curl localhost thành công nghĩa người dùng (user / 사용자) bên ngoài phải truy cập được.”** bên ngoài (external / 외부) đường dẫn (path / 경로) còn DNS, bind address, firewall, proxy và bộ cân bằng tải (load balancer / 로드 밸런서).

**“Certificate đúng trên trình duyệt (browser / 브라우저) nghĩa mọi máy khách (client / 클라이언트) đều đúng.”** Trust store, SNI, giao thức (protocol / 프로토콜) phiên bản (version / 버전) và clock có thể khác giữa máy khách (client / 클라이언트).

> **Chuyển mạch:** Trong **TCP, HTTP và TLS dưới góc nhìn Linux**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Chương này mở rộng [Networking, DNS, Sockets và Ports](./networking_dns_sockets_ports.md), liên hệ [File Descriptors](../01_filesystem/files_streams_descriptors.md), [Time/NTP](../05_system/time_clock_ntp.md), [Java Backend Incident Playbook](../09_production/java_backend_incident_playbook.md) và [Production Troubleshooting](../09_production/production_troubleshooting.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
