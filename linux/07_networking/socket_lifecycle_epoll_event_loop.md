# Vòng đời socket, blocking/non-blocking I/O, `epoll` và vòng lặp sự kiện (event loop / 이벤트 루프)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Socket là gì ở góc nhìn Linux?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **socket() chưa tạo kết nối** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối socket lifecycle với epoll và event loop, để hiểu readiness, close và backpressure trong một tiến trình network.

Socket là một trong những lớp trừu tượng (abstraction / 추상화) quan trọng nhất của Linux networking. Ứng dụng không làm việc trực tiếp với packet ở hầu hết trường hợp; nó thao tác với socket qua tệp (file / 파일) descriptor. Để hiểu máy chủ (server / 서버) hiệu năng cao, reverse proxy, Java NIO/Netty hay event-driven kiến trúc (architecture / 아키텍처), cần hiểu **vòng đời của socket** và cách kernel thông báo rằng một tệp (file / 파일) descriptor đã sẵn sàng cho I/O.

## Socket là gì ở góc nhìn Linux?

Socket là kernel đối tượng (object / 객체) đại diện cho một endpoint giao tiếp. người dùng (user / 사용자) không gian (space / 공간) truy cập nó thông qua tệp (file / 파일) descriptor.

Một TCP máy chủ (server / 서버) điển hình:

```text
socket()
→ bind()
→ listen()
→ accept()
→ read()/write()
→ close()
```

Máy khách (client / 클라이언트):

```text
socket()
→ connect()
→ read()/write()
→ close()
```

Đây không chỉ là chuỗi API; mỗi bước thay đổi trạng thái (state / 상태) của socket trong kernel.

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **socket() chưa tạo kết nối** tiếp nhận điểm tựa từ **Socket là gì ở góc nhìn Linux?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **bind() thực sự làm gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `socket()` chưa tạo kết nối

`socket()` tạo endpoint và tệp (file / 파일) descriptor, nhưng TCP liên kết (connection / 연결) chưa tồn tại.

```c
int fd = socket(AF_INET, SOCK_STREAM, 0);
```

Kernel khởi tạo đối tượng (object / 객체) với giao thức (protocol / 프로토콜) trạng thái (state / 상태) tương ứng. Chỉ khi `connect()` hoặc `listen()/accept()` diễn ra mới có liên kết (connection / 연결) ngữ nghĩa (semantics / 의미론) cụ thể.

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **bind() thực sự làm gì?** tiếp nhận điểm tựa từ **socket() chưa tạo kết nối** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **listen() và backlog** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `bind()` thực sự làm gì?

`bind()` gắn socket với cục bộ (local / 로컬) address/cổng (port / 포트).

```c
bind(fd, ... 0.0.0.0:8080 ...);
```

`0.0.0.0` nghĩa là lắng nghe trên mọi địa chỉ IPv4 phù hợp của host, không phải “địa chỉ mà máy khách (client / 클라이언트) kết nối tới”.

Nếu bind `127.0.0.1:8080`, remote host không thể kết nối trực tiếp dù dịch vụ (service / 서비스) đang chạy bình thường.

Kiểm tra:

```bash
ss -lntp
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **listen() và backlog** tiếp nhận điểm tựa từ **bind() thực sự làm gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **accept() tạo socket mới** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `listen()` và backlog

`listen()` chuyển socket thành listening socket.

Kernel duy trì hàng đợi cho liên kết (connection / 연결) đang hoàn tất handshake và liên kết (connection / 연결) đã hoàn tất chờ ứng dụng (application / 애플리케이션) `accept()`.

Backlog nhỏ hoặc ứng dụng (application / 애플리케이션) accept chậm có thể tạo liên kết (connection / 연결) drop/hết thời gian chờ (timeout / 타임아웃) khi tải tăng.

Giới hạn thực tế còn chịu ảnh hưởng bởi kernel tunables, không chỉ tham số truyền vào `listen()`.

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **accept() tạo socket mới** tiếp nhận điểm tựa từ **listen() và backlog** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Blocking I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `accept()` tạo socket mới

Listening socket tiếp tục lắng nghe. Mỗi liên kết (connection / 연결) được chấp nhận tạo tệp (file / 파일) descriptor mới đại diện cho kết nối cụ thể.

```text
listen fd 3
  ├─ accepted fd 7 → client A
  ├─ accepted fd 8 → client B
  └─ accepted fd 9 → client C
```

Một lỗi FD leak có thể khiến máy chủ (server / 서버) cuối cùng không accept thêm liên kết (connection / 연결) dù CPU/bộ nhớ (memory / 메모리) còn khỏe.

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Blocking I/O** tiếp nhận điểm tựa từ **accept() tạo socket mới** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Non-blocking I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Blocking I/O

Mặc định nhiều socket chạy blocking chế độ (mode / 모드).

```text
read(socket)
→ nếu có data: trả data
→ nếu chưa có data: thread ngủ chờ
```

Blocking không có nghĩa CPU bận. luồng thực thi (thread / 스레드) có thể rời run hàng đợi (queue / 큐) và ngủ trong kernel.

Mô hình “mỗi liên kết (connection / 연결) một luồng thực thi (thread / 스레드)” dễ hiểu nhưng có chi phí ngăn xếp (stack / 스택), scheduling và synchronization khi liên kết (connection / 연결) count lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Non-blocking I/O** tiếp nhận điểm tựa từ **Blocking I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Readiness khác completion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Non-blocking I/O

Với non-blocking chế độ (mode / 모드), nếu thao tác (operation / 연산) chưa thể hoàn tất ngay, kernel có thể trả `EAGAIN`/`EWOULDBLOCK`.

```bash
fcntl(fd, F_SETFL, O_NONBLOCK)
```

Ứng dụng (application / 애플리케이션) không nên vòng lặp busy-spin liên tục gọi `read()`; nó cần cơ chế chờ readiness như `poll()` hoặc `epoll()`.

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Readiness khác completion** tiếp nhận điểm tựa từ **Non-blocking I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **select() và poll()** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Readiness khác completion

`epoll` chủ yếu báo rằng tệp (file / 파일) descriptor **có khả năng thực hiện I/O mà không khối (block / 블록) theo điều kiện hiện tại**. Nó không có nghĩa toàn bộ nghiệp vụ (business / 비즈니스) thao tác (operation / 연산) đã hoàn tất.

Ví dụ socket readable có thể vì:

- có dữ liệu (data / 데이터);
- peer đã đóng;
- có lỗi (error / 오류) điều kiện (condition / 조건).

Ứng dụng (application / 애플리케이션) vẫn phải gọi `read()` và xử lý kết quả.

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **select() và poll()** tiếp nhận điểm tựa từ **Readiness khác completion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **epoll mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `select()` và `poll()`

`select()` và `poll()` cho phép một luồng thực thi (thread / 스레드) chờ nhiều tệp (file / 파일) descriptor.

Nhưng khi số FD lớn, ứng dụng (application / 애플리케이션) có thể phải truyền/quét tập descriptor nhiều lần.

`epoll` được thiết kế tốt hơn cho tải công việc (workload / 워크로드) có rất nhiều FD nhưng mỗi thời điểm chỉ một phần nhỏ active.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **epoll mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **select() và poll()** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Level-triggered và edge-triggered** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `epoll` mô hình tư duy (mental model / 사고 모델)

Ứng dụng (application / 애플리케이션) tạo epoll instance:

```text
epoll_create1()
```

đăng ký interest:

```text
epoll_ctl(ADD fd, events)
```

rồi chờ:

```text
epoll_wait()
```

Kernel trả danh sách FD có sự kiện (event / 이벤트) sẵn sàng.

Mô hình:

```text
many sockets
   ↓ registered
kernel readiness tracking
   ↓
epoll_wait
   ↓
small active set
   ↓
application event loop
```

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Level-triggered và edge-triggered** gom các mảnh từ **epoll mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Vòng lặp sự kiện (event loop / 이벤트 루프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Level-triggered và edge-triggered

**Level-triggered** tiếp tục báo readiness miễn điều kiện còn đúng.

**Edge-triggered** chủ yếu báo khi trạng thái (state / 상태) chuyển từ không-ready sang ready. ứng dụng (application / 애플리케이션) phải drain dữ liệu cho tới `EAGAIN`, nếu không có thể bỏ lỡ sự kiện (event / 이벤트) tiếp theo.

Edge-triggered không tự động “nhanh hơn”. Nó làm máy trạng thái (state machine / 상태 머신) phức tạp hơn và chỉ đáng dùng khi thiết kế (design / 설계) phù hợp.

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Vòng lặp sự kiện (event loop / 이벤트 루프)** tiếp nhận điểm tựa từ **Level-triggered và edge-triggered** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vì sao vòng lặp sự kiện (event loop / 이벤트 루프) sợ blocking thao tác (operation / 연산)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vòng lặp sự kiện (event loop / 이벤트 루프)

Vòng lặp sự kiện (event loop / 이벤트 루프) thường lặp:

```text
wait events
→ dispatch handler
→ read/write non-blocking
→ update interest
→ repeat
```

Một luồng thực thi (thread / 스레드) có thể quản lý hàng nghìn liên kết (connection / 연결) nếu mỗi handler không khối (block / 블록) lâu.

Đây là mô hình của nhiều web máy chủ (server / 서버), proxy và khung phần mềm (framework / 프레임워크) event-driven.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Vì sao vòng lặp sự kiện (event loop / 이벤트 루프) sợ blocking thao tác (operation / 연산)?** tiếp nhận điểm tựa từ **Vòng lặp sự kiện (event loop / 이벤트 루프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Socket receive/send buffer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao vòng lặp sự kiện (event loop / 이벤트 루프) sợ blocking thao tác (operation / 연산)?

Nếu event-loop luồng thực thi (thread / 스레드) gọi truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리) đồng bộ mất 2 giây, nó không xử lý các socket khác trong 2 giây đó.

Vì vậy event-driven thiết kế (design / 설계) thường cần:

- async downstream I/O;
- worker pool cho blocking tác vụ (task / 작업);
- hết thời gian chờ (timeout / 타임아웃);
- backpressure.

Một vòng lặp sự kiện (event loop / 이벤트 루프) không biến mã (code / 코드) blocking thành non-blocking một cách kỳ diệu.

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Socket receive/send buffer** tiếp nhận điểm tựa từ **Vì sao vòng lặp sự kiện (event loop / 이벤트 루프) sợ blocking thao tác (operation / 연산)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Partial read và partial ghi (write / 쓰기)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Socket receive/send buffer

Kernel có buffer nhận và gửi cho socket.

Ứng dụng (application / 애플리케이션) `write()` thành công có thể chỉ nghĩa dữ liệu (data / 데이터) đã vào send buffer, không phải peer đã đọc.

Tương tự dữ liệu (data / 데이터) từ mạng (network / 네트워크) có thể đã ở receive buffer dù ứng dụng (application / 애플리케이션) chưa gọi `read()`.

Quan sát:

```bash
ss -tinp
```

Các trường send/receive hàng đợi (queue / 큐) giúp thấy backlog ở socket tầng (layer / 계층).

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Partial read và partial ghi (write / 쓰기)** tiếp nhận điểm tựa từ **Socket receive/send buffer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Half-close** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Partial read và partial ghi (write / 쓰기)

TCP là byte stream, không bảo toàn message ranh giới (boundary / 경계).

```text
write 1000 bytes
```

không đảm bảo peer nhận đúng một `read()` 1000 bytes.

Ứng dụng (application / 애플리케이션) giao thức (protocol / 프로토콜) phải tự framing, ví dụ length-prefix, delimiter hoặc HTTP parser.

Non-blocking `write()` có thể chỉ ghi một phần buffer. mã (code / 코드) phải giữ phần chưa gửi và tiếp tục khi socket writable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Half-close** tiếp nhận điểm tựa từ **Partial read và partial ghi (write / 쓰기)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **EOF trên socket** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Half-close

TCP cho phép đóng một chiều bằng `shutdown()`.

```text
client không gửi thêm data
nhưng vẫn có thể nhận response
```

Điều này khác đóng hoàn toàn tệp (file / 파일) descriptor.

Giao thức (protocol / 프로토콜) và proxy đôi khi dựa vào ngữ nghĩa (semantics / 의미론) half-close.

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **EOF trên socket** tiếp nhận điểm tựa từ **Half-close** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) reset** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## EOF trên socket

`read()` trả `0` trên TCP thường nghĩa peer đã đóng hướng gửi một cách có trật tự.

Đây không phải “không có dữ liệu (data / 데이터) lúc này”. Non-blocking khi chưa có dữ liệu (data / 데이터) thường là `EAGAIN`, còn `0` là EOF/liên kết (connection / 연결) closure ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, sau nội dung của **EOF trên socket**, **Liên kết (connection / 연결) reset** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **TIMEWAIT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) reset

Nếu peer reset liên kết (connection / 연결), ứng dụng (application / 애플리케이션) có thể nhận `ECONNRESET` hoặc `EPIPE` khi đọc/ghi.

`SIGPIPE` có thể xuất hiện khi ghi vào liên kết (connection / 연결) đã đóng nếu không suppress/handle đúng.

Nhiều thời gian chạy (runtime / 런타임) che giấu chi tiết này thành exception.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **TIMEWAIT** tiếp nhận điểm tựa từ **Liên kết (connection / 연결) reset** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Liên kết (connection / 연결) pooling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `TIME_WAIT`

Endpoint chủ động đóng TCP liên kết (connection / 연결) thường đi vào `TIME_WAIT` để xử lý delayed segments và sequence-number an toàn (safety / 안전).

Nhiều `TIME_WAIT` không tự động là lỗi.

Vấn đề thật có thể là liên kết (connection / 연결) churn cao, thiếu pooling hoặc cạn ephemeral cổng (port / 포트).

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, sau nội dung của **TIMEWAIT**, **Liên kết (connection / 연결) pooling** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Accept thundering herd** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Liên kết (connection / 연결) pooling

Tạo TCP/TLS liên kết (connection / 연결) mới cho mọi yêu cầu (request / 요청) có chi phí handshake và cổng (port / 포트)/trạng thái (state / 상태).

Pool giúp reuse liên kết (connection / 연결), giảm độ trễ (latency / 지연 시간) và kernel overhead.

Nhưng pool quá lớn lại giữ nhiều socket idle và có thể dồn tải vào downstream.

Sức chứa (capacity / 용량) phải dựa trên tính đồng thời (concurrency / 동시성) thực tế, không phải “càng nhiều liên kết (connection / 연결) càng tốt”.

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Accept thundering herd** tiếp nhận điểm tựa từ **Liên kết (connection / 연결) pooling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **SOREUSEADDR và SOREUSEPORT** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Accept thundering herd

Nhiều worker cùng chờ một listening socket có thể bị đánh thức cùng lúc cho một số sự kiện (event / 이벤트) mẫu (pattern / 패턴), gây contention.

Kernel và máy chủ (server / 서버) kiến trúc (architecture / 아키텍처) hiện đại có nhiều cơ chế giảm thundering herd, nhưng đây vẫn là mô hình tư duy (mental model / 사고 모델) quan trọng khi hiểu multi-worker máy chủ (server / 서버).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **SOREUSEADDR và SOREUSEPORT** tiếp nhận điểm tựa từ **Accept thundering herd** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java NIO và Netty** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `SO_REUSEADDR` và `SO_REUSEPORT`

`SO_REUSEADDR` hỗ trợ một số trường hợp bind lại address/cổng (port / 포트) theo ngữ nghĩa (semantics / 의미론) hệ điều hành.

`SO_REUSEPORT` cho phép nhiều socket bind cùng address/cổng (port / 포트) trong điều kiện phù hợp, hữu ích cho multi-worker tải (load / 로드) phân phối (distribution / 분포).

Không nên bật option chỉ vì thấy trong mẫu (sample / 표본) mã (code / 코드); ngữ nghĩa (semantics / 의미론) khác nhau và ảnh hưởng routing liên kết (connection / 연결) tới worker.

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Java NIO và Netty** tiếp nhận điểm tựa từ **SOREUSEADDR và SOREUSEPORT** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java NIO và Netty

Java NIO `Selector` thường ánh xạ xuống cơ chế readiness của hệ điều hành như epoll trên Linux.

Netty vòng lặp sự kiện (event loop / 이벤트 루프) cũng xây dựng trên non-blocking channels và sự kiện (event / 이벤트) dispatch.

Do đó khi Java luồng thực thi (thread / 스레드) dump cho thấy vài event-loop luồng thực thi (thread / 스레드) xử lý hàng nghìn liên kết (connection / 연결), đó là thiết kế (design / 설계) bình thường.

Nhưng nếu handler khối (block / 블록), toàn vòng lặp sự kiện (event loop / 이벤트 루프) có thể tăng độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Backpressure** tiếp nhận điểm tựa từ **Java NIO và Netty** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gỡ lỗi (debug / 디버그) socket stall** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backpressure

Nếu ứng dụng (application / 애플리케이션) đọc yêu cầu (request / 요청) nhanh hơn downstream xử lý, hàng đợi (queue / 큐) sẽ tăng.

Event-driven hệ thống (system / 시스템) cần biết khi nào tạm ngừng đọc thêm hoặc giới hạn outstanding công việc (work / 작업).

```text
network input
→ event loop
→ work queue
→ downstream
```

Nếu công việc (work / 작업) hàng đợi (queue / 큐) không bound, bộ nhớ (memory / 메모리) có thể tăng tới OOM dù socket tầng (layer / 계층) hoạt động đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Gỡ lỗi (debug / 디버그) socket stall** tiếp nhận điểm tựa từ **Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gỡ lỗi (debug / 디버그) socket stall

Một quy trình hữu ích:

```bash
ss -lntp
ss -antp
ss -tinp
lsof -p <PID> -a -i
strace -tt -T -p <PID> -e epoll_wait,accept4,read,write,recvfrom,sendto
```

Nếu tiến trình (process / 프로세스) ngủ nhiều trong `epoll_wait`, có thể nó đơn giản đang chờ sự kiện (event / 이벤트). Nếu vòng lặp sự kiện (event loop / 이벤트 루프) CPU cao nhưng ít thông lượng (throughput / 처리량), cần xem busy vòng lặp (loop / 루프), lỗi (error / 오류) thử lại (retry / 재시도) hoặc handler hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Mô hình tư duy** gom các mảnh từ **Gỡ lỗi (debug / 디버그) socket stall** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy

Máy chủ (server / 서버) event-driven có thể hình dung:

```text
NIC / TCP stack
   ↓
socket buffers
   ↓
readiness state
   ↓
epoll
   ↓
event loop
   ↓
protocol parser
   ↓
business work / downstream
```

Mỗi tầng có hàng đợi (queue / 큐) và backpressure riêng. độ trễ (latency / 지연 시간) tăng khi bất kỳ hàng đợi (queue / 큐) nào bắt đầu tích tụ.

> **Chuyển mạch:** Ở chặng này của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Những hiểu lầm phổ biến** gom các mảnh từ **Mô hình tư duy** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“Non-blocking nghĩa là thao tác (operation / 연산) luôn thành công ngay.”** Không; nó có thể trả `EAGAIN`.

**“epoll hoàn tất I/O thay ứng dụng (application / 애플리케이션).”** Không; epoll chủ yếu báo readiness.

**“Một liên kết (connection / 연결) tương ứng một luồng thực thi (thread / 스레드).”** Chỉ đúng với một kiến trúc; vòng lặp sự kiện (event loop / 이벤트 루프) có thể quản lý rất nhiều liên kết (connection / 연결) trên ít luồng thực thi (thread / 스레드).

**“`write()` thành công nghĩa máy khách (client / 클라이언트) đã nhận dữ liệu (data / 데이터).”** dữ liệu (data / 데이터) có thể mới chỉ vào kernel send buffer.

**“Nhiều `TIME_WAIT` chắc chắn là bug kernel.”** Thường cần kiểm tra liên kết (connection / 연결) churn và pooling trước.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vòng đời socket, blocking/non-blocking I/O, epoll và vòng lặp sự kiện (event loop / 이벤트 루프)**, **Kết nối kiến thức** tiếp nhận điểm tựa từ **Những hiểu lầm phổ biến** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối kiến thức

Chương này nối [system call lifecycle](../00_foundations/system_call_lifecycle.md), [IPC](../04_process/interprocess_communication.md), [TCP/HTTP/TLS](./tcp_http_tls.md), [congestion control](./tcp_congestion_control.md), [reverse proxy](./reverse_proxy_load_balancing.md) và [Java backend incident playbook](../09_production/java_backend_incident_playbook.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
