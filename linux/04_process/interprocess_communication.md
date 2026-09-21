# Giao tiếp giữa các tiến trình (IPC)

Một tiến trình (process) bị cô lập về không gian địa chỉ (address space), nhưng hệ thống thực tế cần nhiều tiến trình trao đổi dữ liệu và phối hợp trạng thái. Web server nói chuyện với database, shell nối output của chương trình này vào input của chương trình khác, worker nhận job từ queue, application gửi tín hiệu cho daemon.

Các cơ chế **giao tiếp giữa các tiến trình (Inter-Process Communication / IPC)** tồn tại để giải quyết nhu cầu này.

## Vì sao không cho mọi process đọc memory của nhau?

Nếu process A có thể đọc/ghi trực tiếp memory của process B mà không kiểm soát, một bug nhỏ có thể phá toàn bộ hệ thống.

Virtual memory tạo isolation. IPC cung cấp các **kênh có kiểm soát** để chia sẻ dữ liệu hoặc sự kiện.

Do đó IPC là điểm cân bằng giữa isolation và cooperation.

## Pipe: dòng byte một chiều

Anonymous pipe thường xuất hiện trong shell:

```bash
ps -ef | grep java
```

Shell tạo pipe, nối stdout của `ps` vào đầu ghi và stdin của `grep` vào đầu đọc.

Pipe thường phù hợp khi:

- quan hệ producer/consumer đơn giản;
- dữ liệu dạng stream;
- tiến trình có quan hệ cha–con hoặc shell đang orchestration.

Pipe không có pathname trong filesystem theo cách regular file có.

## Named pipe (FIFO)

FIFO có tên trong filesystem:

```bash
mkfifo /tmp/myfifo
```

Terminal 1:

```bash
cat /tmp/myfifo
```

Terminal 2:

```bash
echo hello > /tmp/myfifo
```

FIFO hữu ích để hiểu rằng pathname có thể trỏ tới object IPC chứ không chỉ file lưu trữ.

Không nên dùng `/tmp` FIFO production mà không nghĩ tới permission, lifetime và cleanup.

## Unix domain socket

Unix domain socket cho phép IPC qua socket API nhưng không cần đi qua IP networking.

Ví dụ pathname:

```text
/run/docker.sock
/run/postgresql/.s.PGSQL.5432
```

Một application local có thể dùng Unix socket thay TCP loopback.

Ưu điểm có thể gồm:

- không cần IP/port;
- permission có thể quản lý qua filesystem path;
- overhead thấp hơn trong một số workload;
- rõ ràng rằng communication chỉ local host.

## TCP socket cũng là IPC

IPC không nhất thiết chỉ local machine.

TCP socket là cơ chế communication giữa processes qua network stack, có thể cùng host hoặc khác host.

```text
process A -> socket -> TCP/IP -> socket -> process B
```

Khi hai services cùng host dùng `127.0.0.1`, vẫn là network IPC.

## Signal: gửi sự kiện, không phải payload lớn

Signal phù hợp với notification/control hơn là truyền dữ liệu lớn.

Ví dụ:

```bash
kill -TERM 1234
```

hoặc daemon reload bằng `SIGHUP` nếu software hỗ trợ.

Signal có thể mang rất ít thông tin so với socket/pipe. Nó nói kiểu “một sự kiện xảy ra”, không phải stream data phức tạp.

## Shared memory

Shared memory cho phép nhiều processes map cùng vùng memory vật lý/logical để trao đổi dữ liệu tốc độ cao.

Ưu điểm là không cần copy payload qua pipe/socket cho mỗi exchange.

Nhưng vấn đề khó hơn xuất hiện: **đồng bộ hóa (synchronization)**.

Nếu hai processes cùng ghi một cấu trúc mà không coordination, dữ liệu có thể race/corrupt.

Do đó shared memory thường đi cùng:

- mutex;
- semaphore;
- futex;
- lock-free algorithm;
- memory ordering rules.

## POSIX shared memory

Một số hệ thống dùng objects dưới `/dev/shm`:

```bash
ls -lah /dev/shm
```

`/dev/shm` thường là tmpfs dùng cho POSIX shared memory và application-specific files.

Nếu `/dev/shm` quá nhỏ trong container, một số database/browser/runtime có thể gặp lỗi.

## Semaphore

Semaphore là synchronization primitive dùng để kiểm soát quyền truy cập hoặc biểu diễn số resource available.

Mental model đơn giản:

```text
counter > 0 -> một worker được phép đi tiếp
counter = 0 -> worker phải chờ
```

System V/POSIX semaphores tồn tại ở OS level, nhưng application hiện đại thường sử dụng abstraction từ runtime/library.

## Message queue

POSIX/System V message queue cho phép gửi discrete messages thay vì byte stream.

Ngày nay nhiều application dùng Redis, Kafka, RabbitMQ hoặc external broker cho distributed messaging, nhưng OS-level queues vẫn là nền tảng quan trọng trong một số software.

Điểm khác biệt:

- OS IPC queue thường local host;
- distributed broker thêm persistence, replication, routing và network protocol.

## Memory-mapped file (`mmap`)

`mmap()` ánh xạ file hoặc anonymous memory vào address space của process.

Điều này có thể dùng cho:

- file I/O;
- shared libraries;
- shared memory;
- database storage engines.

Một file mapping không có nghĩa toàn bộ file được load vào RAM ngay. Kernel demand-pages các vùng khi cần.

Xem mapping:

```bash
cat /proc/<PID>/maps
```

## Copy và zero-copy

Một data path thông thường có thể copy bytes nhiều lần giữa kernel/user buffers.

Linux có các cơ chế giảm copy trong một số trường hợp như:

- `sendfile()`;
- `splice()`;
- memory mapping;
- io_uring-related paths;
- DMA ở hardware layer.

Web server gửi static file có thể dùng `sendfile()` để giảm copy qua user-space buffer.

Đây là ví dụ performance optimization xuất phát từ hiểu data movement.

## `sendfile()` và Nginx

Nginx có directive `sendfile on;` để tận dụng kernel mechanism cho static file trong môi trường phù hợp.

Nhưng network filesystem/virtualized filesystem có thể có semantics khác. Không nên bật/tắt chỉ theo “best practice” mà không benchmark workload thực.

## IPC và file descriptor

Pipe, socket, eventfd và nhiều IPC objects đều được process giữ qua file descriptor.

Đây là lý do `lsof` và `/proc/<PID>/fd` có thể cho insight về nhiều resource types khác nhau.

```bash
ls -l /proc/<PID>/fd
```

## Eventfd và epoll

Linux server hiệu năng cao thường cần chờ nhiều file descriptors mà không tạo một thread blocking cho từng connection.

`epoll` cho phép một process đăng ký nhiều descriptors và được thông báo khi descriptor sẵn sàng.

Mental model:

```text
10,000 sockets
     ↓
epoll interest set
     ↓
threads chỉ xử lý sockets ready
```

Đây là nền tảng của nhiều event-driven servers.

Java NIO `Selector`, Netty event loop và Node.js/libuv đều có connection tới readiness-based I/O mechanisms như epoll trên Linux.

## Blocking I/O và non-blocking I/O

Với blocking I/O, `read()` có thể làm thread ngủ cho tới khi data sẵn sàng.

Với non-blocking descriptor, call có thể trả ngay với trạng thái chưa có data, và application dùng polling/event mechanism như epoll.

Không có mô hình nào “luôn tốt hơn”. Blocking code đơn giản; event-driven model scale tốt với nhiều mostly-idle connections nhưng tăng complexity.

## Backpressure

Nếu producer tạo dữ liệu nhanh hơn consumer xử lý, buffer cuối cùng đầy.

Pipe/socket có capacity hữu hạn. Khi buffer đầy:

- write có thể block;
- non-blocking write trả lỗi/trạng thái chưa thể ghi;
- application phải queue/drop/throttle.

Backpressure không phải khái niệm riêng của Kafka hay reactive programming; nó xuất hiện ngay trong IPC primitives của OS.

## Thundering herd

Nếu nhiều workers cùng chờ một event và tất cả được đánh thức dù chỉ một worker cần xử lý, scheduler overhead có thể tăng.

Linux và server frameworks có nhiều kỹ thuật để giảm thundering herd.

Đây là ví dụ cho việc synchronization design ảnh hưởng scalability.

## IPC và container namespace

IPC namespace tách một số System V/POSIX IPC resources giữa containers.

Unix socket bind-mounted giữa host/container lại có thể cố ý tạo communication channel xuyên isolation boundary.

Ví dụ nổi tiếng:

```text
/var/run/docker.sock
```

Mount Docker socket vào container trao quyền điều khiển Docker daemon rất lớn. Đây là security boundary quan trọng, không chỉ “một file socket”.

## Debug IPC

### Pipe/socket descriptors

```bash
sudo lsof -p <PID>
```

### Unix sockets

```bash
ss -xl
```

### TCP sockets

```bash
ss -antp
```

### Shared memory

```bash
ls -lah /dev/shm
ipcs
```

`ipcs` hiển thị System V IPC objects nếu hệ thống sử dụng.

### Syscalls

```bash
strace -e trace=network,ipc -p <PID>
```

support của trace categories phụ thuộc strace version.

## Java connection

Trong Java backend:

- `Socket` / Netty channel → socket IPC;
- `FileChannel.map()` → mmap;
- `Selector` → readiness multiplexing, thường epoll trên Linux;
- thread coordination → futex ở tầng runtime/kernel;
- database connection pool → tập hợp TCP sockets;
- UNIX domain socket support → local IPC trong các library/runtime hiện đại.

Khi JVM thread dump cho thấy nhiều threads `WAITING` hoặc `RUNNABLE` trong network/native calls, hiểu IPC giúp giải thích chúng đang chờ cái gì.

## Những hiểu lầm phổ biến

**“IPC chỉ là pipe.”** Linux có pipe, socket, shared memory, semaphore, signals, queues và nhiều cơ chế khác.

**“Shared memory luôn nhanh nhất nên nên dùng.”** Nó giảm copy nhưng synchronization và correctness phức tạp hơn nhiều.

**“Unix socket và TCP socket giống hệt nhau.”** API có điểm chung nhưng address domain, routing và security semantics khác.

**“Non-blocking I/O luôn nhanh hơn blocking I/O.”** Hiệu quả phụ thuộc concurrency model và workload.

**“Socket file permission nhỏ nên không nguy hiểm.”** Một socket như Docker daemon socket có thể trao quyền cực lớn.

## Mô hình tư duy

Chọn IPC theo câu hỏi:

```text
Cần stream bytes đơn giản?        → pipe/socket
Cần local request/response?       → Unix socket
Cần network communication?        → TCP/UDP socket
Cần event/control đơn giản?       → signal/eventfd
Cần chia sẻ data rất nhanh?       → shared memory + synchronization
Cần chờ rất nhiều descriptors?    → epoll/event loop
```

Không chọn primitive chỉ vì “nhanh”; chọn theo semantics, failure model và maintainability.

Xem thêm: [Files, streams và file descriptors](../01_filesystem/files_streams_descriptors.md), [Networking](../07_networking/networking_dns_sockets_ports.md), [Process và threads](./processes_threads_signals_jobs.md).