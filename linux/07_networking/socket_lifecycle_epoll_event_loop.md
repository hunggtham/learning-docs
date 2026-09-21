# Vòng đời socket, blocking/non-blocking I/O, `epoll` và event loop

Socket là một trong những abstraction quan trọng nhất của Linux networking. Ứng dụng không làm việc trực tiếp với packet ở hầu hết trường hợp; nó thao tác với socket qua file descriptor. Để hiểu server hiệu năng cao, reverse proxy, Java NIO/Netty hay event-driven architecture, cần hiểu **vòng đời của socket** và cách kernel thông báo rằng một file descriptor đã sẵn sàng cho I/O.

## Socket là gì ở góc nhìn Linux?

Socket là kernel object đại diện cho một endpoint giao tiếp. User space truy cập nó thông qua file descriptor.

Một TCP server điển hình:

```text
socket()
→ bind()
→ listen()
→ accept()
→ read()/write()
→ close()
```

Client:

```text
socket()
→ connect()
→ read()/write()
→ close()
```

Đây không chỉ là chuỗi API; mỗi bước thay đổi state của socket trong kernel.

## `socket()` chưa tạo kết nối

`socket()` tạo endpoint và file descriptor, nhưng TCP connection chưa tồn tại.

```c
int fd = socket(AF_INET, SOCK_STREAM, 0);
```

Kernel khởi tạo object với protocol state tương ứng. Chỉ khi `connect()` hoặc `listen()/accept()` diễn ra mới có connection semantics cụ thể.

## `bind()` thực sự làm gì?

`bind()` gắn socket với local address/port.

```c
bind(fd, ... 0.0.0.0:8080 ...);
```

`0.0.0.0` nghĩa là lắng nghe trên mọi địa chỉ IPv4 phù hợp của host, không phải “địa chỉ mà client kết nối tới”.

Nếu bind `127.0.0.1:8080`, remote host không thể kết nối trực tiếp dù service đang chạy bình thường.

Kiểm tra:

```bash
ss -lntp
```

## `listen()` và backlog

`listen()` chuyển socket thành listening socket.

Kernel duy trì hàng đợi cho connection đang hoàn tất handshake và connection đã hoàn tất chờ application `accept()`.

Backlog nhỏ hoặc application accept chậm có thể tạo connection drop/timeout khi tải tăng.

Giới hạn thực tế còn chịu ảnh hưởng bởi kernel tunables, không chỉ tham số truyền vào `listen()`.

## `accept()` tạo socket mới

Listening socket tiếp tục lắng nghe. Mỗi connection được chấp nhận tạo file descriptor mới đại diện cho kết nối cụ thể.

```text
listen fd 3
  ├─ accepted fd 7 → client A
  ├─ accepted fd 8 → client B
  └─ accepted fd 9 → client C
```

Một lỗi FD leak có thể khiến server cuối cùng không accept thêm connection dù CPU/memory còn khỏe.

## Blocking I/O

Mặc định nhiều socket chạy blocking mode.

```text
read(socket)
→ nếu có data: trả data
→ nếu chưa có data: thread ngủ chờ
```

Blocking không có nghĩa CPU bận. Thread có thể rời run queue và ngủ trong kernel.

Mô hình “mỗi connection một thread” dễ hiểu nhưng có chi phí stack, scheduling và synchronization khi connection count lớn.

## Non-blocking I/O

Với non-blocking mode, nếu operation chưa thể hoàn tất ngay, kernel có thể trả `EAGAIN`/`EWOULDBLOCK`.

```bash
fcntl(fd, F_SETFL, O_NONBLOCK)
```

Application không nên vòng lặp busy-spin liên tục gọi `read()`; nó cần cơ chế chờ readiness như `poll()` hoặc `epoll()`.

## Readiness khác completion

`epoll` chủ yếu báo rằng file descriptor **có khả năng thực hiện I/O mà không block theo điều kiện hiện tại**. Nó không có nghĩa toàn bộ business operation đã hoàn tất.

Ví dụ socket readable có thể vì:

- có data;
- peer đã đóng;
- có error condition.

Application vẫn phải gọi `read()` và xử lý kết quả.

## `select()` và `poll()`

`select()` và `poll()` cho phép một thread chờ nhiều file descriptor.

Nhưng khi số FD lớn, application có thể phải truyền/quét tập descriptor nhiều lần.

`epoll` được thiết kế tốt hơn cho workload có rất nhiều FD nhưng mỗi thời điểm chỉ một phần nhỏ active.

## `epoll` mental model

Application tạo epoll instance:

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

Kernel trả danh sách FD có event sẵn sàng.

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

## Level-triggered và edge-triggered

**Level-triggered** tiếp tục báo readiness miễn điều kiện còn đúng.

**Edge-triggered** chủ yếu báo khi state chuyển từ không-ready sang ready. Application phải drain dữ liệu cho tới `EAGAIN`, nếu không có thể bỏ lỡ event tiếp theo.

Edge-triggered không tự động “nhanh hơn”. Nó làm state machine phức tạp hơn và chỉ đáng dùng khi design phù hợp.

## Event loop

Event loop thường lặp:

```text
wait events
→ dispatch handler
→ read/write non-blocking
→ update interest
→ repeat
```

Một thread có thể quản lý hàng nghìn connection nếu mỗi handler không block lâu.

Đây là mô hình của nhiều web server, proxy và framework event-driven.

## Vì sao event loop sợ blocking operation?

Nếu event-loop thread gọi database query đồng bộ mất 2 giây, nó không xử lý các socket khác trong 2 giây đó.

Vì vậy event-driven design thường cần:

- async downstream I/O;
- worker pool cho blocking task;
- timeout;
- backpressure.

Một event loop không biến code blocking thành non-blocking một cách kỳ diệu.

## Socket receive/send buffer

Kernel có buffer nhận và gửi cho socket.

Application `write()` thành công có thể chỉ nghĩa data đã vào send buffer, không phải peer đã đọc.

Tương tự data từ network có thể đã ở receive buffer dù application chưa gọi `read()`.

Quan sát:

```bash
ss -tinp
```

Các trường send/receive queue giúp thấy backlog ở socket layer.

## Partial read và partial write

TCP là byte stream, không bảo toàn message boundary.

```text
write 1000 bytes
```

không đảm bảo peer nhận đúng một `read()` 1000 bytes.

Application protocol phải tự framing, ví dụ length-prefix, delimiter hoặc HTTP parser.

Non-blocking `write()` có thể chỉ ghi một phần buffer. Code phải giữ phần chưa gửi và tiếp tục khi socket writable.

## Half-close

TCP cho phép đóng một chiều bằng `shutdown()`.

```text
client không gửi thêm data
nhưng vẫn có thể nhận response
```

Điều này khác đóng hoàn toàn file descriptor.

Protocol và proxy đôi khi dựa vào semantics half-close.

## EOF trên socket

`read()` trả `0` trên TCP thường nghĩa peer đã đóng hướng gửi một cách có trật tự.

Đây không phải “không có data lúc này”. Non-blocking khi chưa có data thường là `EAGAIN`, còn `0` là EOF/connection closure semantics.

## Connection reset

Nếu peer reset connection, application có thể nhận `ECONNRESET` hoặc `EPIPE` khi đọc/ghi.

`SIGPIPE` có thể xuất hiện khi ghi vào connection đã đóng nếu không suppress/handle đúng.

Nhiều runtime che giấu chi tiết này thành exception.

## `TIME_WAIT`

Endpoint chủ động đóng TCP connection thường đi vào `TIME_WAIT` để xử lý delayed segments và sequence-number safety.

Nhiều `TIME_WAIT` không tự động là lỗi.

Vấn đề thật có thể là connection churn cao, thiếu pooling hoặc cạn ephemeral port.

## Connection pooling

Tạo TCP/TLS connection mới cho mọi request có chi phí handshake và port/state.

Pool giúp reuse connection, giảm latency và kernel overhead.

Nhưng pool quá lớn lại giữ nhiều socket idle và có thể dồn tải vào downstream.

Capacity phải dựa trên concurrency thực tế, không phải “càng nhiều connection càng tốt”.

## Accept thundering herd

Nhiều worker cùng chờ một listening socket có thể bị đánh thức cùng lúc cho một số event pattern, gây contention.

Kernel và server architecture hiện đại có nhiều cơ chế giảm thundering herd, nhưng đây vẫn là mental model quan trọng khi hiểu multi-worker server.

## `SO_REUSEADDR` và `SO_REUSEPORT`

`SO_REUSEADDR` hỗ trợ một số trường hợp bind lại address/port theo semantics hệ điều hành.

`SO_REUSEPORT` cho phép nhiều socket bind cùng address/port trong điều kiện phù hợp, hữu ích cho multi-worker load distribution.

Không nên bật option chỉ vì thấy trong sample code; semantics khác nhau và ảnh hưởng routing connection tới worker.

## Java NIO và Netty

Java NIO `Selector` thường ánh xạ xuống cơ chế readiness của hệ điều hành như epoll trên Linux.

Netty event loop cũng xây dựng trên non-blocking channels và event dispatch.

Do đó khi Java thread dump cho thấy vài event-loop thread xử lý hàng nghìn connection, đó là design bình thường.

Nhưng nếu handler block, toàn event loop có thể tăng latency.

## Backpressure

Nếu application đọc request nhanh hơn downstream xử lý, queue sẽ tăng.

Event-driven system cần biết khi nào tạm ngừng đọc thêm hoặc giới hạn outstanding work.

```text
network input
→ event loop
→ work queue
→ downstream
```

Nếu work queue không bound, memory có thể tăng tới OOM dù socket layer hoạt động đúng.

## Debug socket stall

Một quy trình hữu ích:

```bash
ss -lntp
ss -antp
ss -tinp
lsof -p <PID> -a -i
strace -tt -T -p <PID> -e epoll_wait,accept4,read,write,recvfrom,sendto
```

Nếu process ngủ nhiều trong `epoll_wait`, có thể nó đơn giản đang chờ event. Nếu event loop CPU cao nhưng ít throughput, cần xem busy loop, error retry hoặc handler behavior.

## Mô hình tư duy

Server event-driven có thể hình dung:

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

Mỗi tầng có queue và backpressure riêng. Latency tăng khi bất kỳ queue nào bắt đầu tích tụ.

## Những hiểu lầm phổ biến

**“Non-blocking nghĩa là operation luôn thành công ngay.”** Không; nó có thể trả `EAGAIN`.

**“epoll hoàn tất I/O thay application.”** Không; epoll chủ yếu báo readiness.

**“Một connection tương ứng một thread.”** Chỉ đúng với một kiến trúc; event loop có thể quản lý rất nhiều connection trên ít thread.

**“`write()` thành công nghĩa client đã nhận data.”** Data có thể mới chỉ vào kernel send buffer.

**“Nhiều `TIME_WAIT` chắc chắn là bug kernel.”** Thường cần kiểm tra connection churn và pooling trước.

## Kết nối kiến thức

Chương này nối [system call lifecycle](../00_foundations/system_call_lifecycle.md), [IPC](../04_process/interprocess_communication.md), [TCP/HTTP/TLS](./tcp_http_tls.md), [congestion control](./tcp_congestion_control.md), [reverse proxy](./reverse_proxy_load_balancing.md) và [Java backend incident playbook](../09_production/java_backend_incident_playbook.md).