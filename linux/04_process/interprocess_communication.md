# Giao tiếp giữa các tiến trình (IPC)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Giao tiếp giữa các tiến trình (IPC)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao không cho mọi tiến trình (process / 프로세스) đọc bộ nhớ (memory / 메모리) của nhau?** cho thấy đối tượng vận hành qua những bước nào và tạo ra hệ quả gì; sau đó sang **Pipe: dòng byte một chiều** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối nhu cầu trao đổi dữ liệu với pipe và các cơ chế IPC khác, để chọn đúng kênh theo hướng truyền, bộ đệm và mô hình đồng bộ.

Một tiến trình (process / 프로세스) bị cô lập về không gian địa chỉ (address space), nhưng hệ thống thực tế cần nhiều tiến trình trao đổi dữ liệu và phối hợp trạng thái. Web máy chủ (server / 서버) nói chuyện với cơ sở dữ liệu (database / 데이터베이스), shell nối đầu ra (output / 출력) của chương trình này vào đầu vào (input / 입력) của chương trình khác, worker nhận job từ hàng đợi (queue / 큐), ứng dụng (application / 애플리케이션) gửi tín hiệu cho daemon.

Các cơ chế **giao tiếp giữa các tiến trình (Inter-Process Communication / IPC)** tồn tại để giải quyết nhu cầu này.

## Vì sao không cho mọi tiến trình (process / 프로세스) đọc bộ nhớ (memory / 메모리) của nhau?

Nếu tiến trình (process / 프로세스) A có thể đọc/ghi trực tiếp bộ nhớ (memory / 메모리) của tiến trình (process / 프로세스) B mà không kiểm soát, một bug nhỏ có thể phá toàn bộ hệ thống.

Virtual bộ nhớ (memory / 메모리) tạo isolation. IPC cung cấp các **kênh có kiểm soát** để chia sẻ dữ liệu hoặc sự kiện.

Do đó IPC là điểm cân bằng giữa isolation và cooperation.

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **Vì sao không cho mọi tiến trình (process / 프로세스) đọc bộ nhớ (memory / 메모리) của nhau?** xác định đầu vào; **Pipe: dòng byte một chiều** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Named pipe (FIFO)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pipe: dòng byte một chiều

Anonymous pipe thường xuất hiện trong shell:

```bash
ps -ef | grep java
```

Shell tạo pipe, nối stdout của `ps` vào đầu ghi và stdin của `grep` vào đầu đọc.

Pipe thường phù hợp khi:

- quan hệ producer/bên tiêu thụ (consumer / 소비자) đơn giản;
- dữ liệu dạng stream;
- tiến trình có quan hệ cha–con hoặc shell đang orchestration.

Pipe không có pathname trong filesystem theo cách regular tệp (file / 파일) có.

> **Chuyển mạch:** Ở chặng này của **Giao tiếp giữa các tiến trình (IPC)**, **Named pipe (FIFO)** tiếp nhận điểm tựa từ **Pipe: dòng byte một chiều** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Unix lĩnh vực (domain / 도메인) socket** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

FIFO hữu ích để hiểu rằng pathname có thể trỏ tới đối tượng (object / 객체) IPC chứ không chỉ tệp (file / 파일) lưu trữ.

Không nên dùng `/tmp` FIFO môi trường vận hành (production / 운영 환경) mà không nghĩ tới permission, thời gian tồn tại (lifetime / 수명) và cleanup.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao tiếp giữa các tiến trình (IPC)**, **Unix lĩnh vực (domain / 도메인) socket** tiếp nhận điểm tựa từ **Named pipe (FIFO)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **TCP socket cũng là IPC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Unix lĩnh vực (domain / 도메인) socket

Unix lĩnh vực (domain / 도메인) socket cho phép IPC qua socket API nhưng không cần đi qua IP networking.

Ví dụ pathname:

```text
/run/docker.sock
/run/postgresql/.s.PGSQL.5432
```

Một ứng dụng (application / 애플리케이션) cục bộ (local / 로컬) có thể dùng Unix socket thay TCP loopback.

Ưu điểm có thể gồm:

- không cần IP/cổng (port / 포트);
- permission có thể quản lý qua filesystem đường dẫn (path / 경로);
- overhead thấp hơn trong một số tải công việc (workload / 워크로드);
- rõ ràng rằng communication chỉ cục bộ (local / 로컬) host.

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **TCP socket cũng là IPC** tiếp nhận điểm tựa từ **Unix lĩnh vực (domain / 도메인) socket** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tín hiệu (signal / 신호): gửi sự kiện, không phải payload lớn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## TCP socket cũng là IPC

IPC không nhất thiết chỉ cục bộ (local / 로컬) machine.

TCP socket là cơ chế communication giữa processes qua mạng (network / 네트워크) ngăn xếp (stack / 스택), có thể cùng host hoặc khác host.

```text
process A -> socket -> TCP/IP -> socket -> process B
```

Khi hai services cùng host dùng `127.0.0.1`, vẫn là mạng (network / 네트워크) IPC.

> **Chuyển mạch:** Ở chặng này của **Giao tiếp giữa các tiến trình (IPC)**, **Tín hiệu (signal / 신호): gửi sự kiện, không phải payload lớn** tiếp nhận điểm tựa từ **TCP socket cũng là IPC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tín hiệu (signal / 신호): gửi sự kiện, không phải payload lớn

Tín hiệu (signal / 신호) phù hợp với notification/điều khiển (control / 제어) hơn là truyền dữ liệu lớn.

Ví dụ:

```bash
kill -TERM 1234
```

hoặc daemon reload bằng `SIGHUP` nếu software hỗ trợ.

Tín hiệu (signal / 신호) có thể mang rất ít thông tin so với socket/pipe. Nó nói kiểu “một sự kiện xảy ra”, không phải stream dữ liệu (data / 데이터) phức tạp.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao tiếp giữa các tiến trình (IPC)**, **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Tín hiệu (signal / 신호): gửi sự kiện, không phải payload lớn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **POSIX dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) cho phép nhiều processes map cùng vùng bộ nhớ (memory / 메모리) vật lý/logical để trao đổi dữ liệu tốc độ cao.

Ưu điểm là không cần bản sao (copy / 복사) payload qua pipe/socket cho mỗi exchange.

Nhưng vấn đề khó hơn xuất hiện: **đồng bộ hóa (synchronization)**.

Nếu hai processes cùng ghi một cấu trúc mà không coordination, dữ liệu có thể race/corrupt.

Do đó dùng chung (shared / 공유) bộ nhớ (memory / 메모리) thường đi cùng:

- mutex;
- semaphore;
- futex;
- lock-free thuật toán (algorithm / 알고리즘);
- bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) rules.

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **POSIX dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Semaphore** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## POSIX dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

Một số hệ thống dùng objects dưới `/dev/shm`:

```bash
ls -lah /dev/shm
```

`/dev/shm` thường là tmpfs dùng cho POSIX dùng chung (shared / 공유) bộ nhớ (memory / 메모리) và application-specific files.

Nếu `/dev/shm` quá nhỏ trong bộ chứa (container / 컨테이너), một số cơ sở dữ liệu (database / 데이터베이스)/trình duyệt (browser / 브라우저)/thời gian chạy (runtime / 런타임) có thể gặp lỗi.

> **Chuyển mạch:** Ở chặng này của **Giao tiếp giữa các tiến trình (IPC)**, **Semaphore** tiếp nhận điểm tựa từ **POSIX dùng chung (shared / 공유) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Message hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Semaphore

Semaphore là synchronization thành phần nguyên thủy (primitive / 기본 요소) dùng để kiểm soát quyền truy cập hoặc biểu diễn số tài nguyên (resource / 자원) available.

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
counter > 0 -> một worker được phép đi tiếp
counter = 0 -> worker phải chờ
```

Hệ thống (system / 시스템) V/POSIX semaphores tồn tại ở OS mức (level / 수준), nhưng ứng dụng (application / 애플리케이션) hiện đại thường sử dụng lớp trừu tượng (abstraction / 추상화) từ thời gian chạy (runtime / 런타임)/thư viện (library / 라이브러리).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao tiếp giữa các tiến trình (IPC)**, **Message hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **Semaphore** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Memory-mapped tệp (file / 파일) (mmap)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Message hàng đợi (queue / 큐)

POSIX/hệ thống (system / 시스템) V message hàng đợi (queue / 큐) cho phép gửi discrete messages thay vì byte stream.

Ngày nay nhiều ứng dụng (application / 애플리케이션) dùng Redis, Kafka, RabbitMQ hoặc bên ngoài (external / 외부) broker cho phân tán (distributed / 분산) messaging, nhưng OS-level queues vẫn là nền tảng quan trọng trong một số software.

Điểm khác biệt:

- OS IPC hàng đợi (queue / 큐) thường cục bộ (local / 로컬) host;
- phân tán (distributed / 분산) broker thêm persistence, replication, routing và mạng (network / 네트워크) giao thức (protocol / 프로토콜).

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **Memory-mapped tệp (file / 파일) (mmap)** tiếp nhận điểm tựa từ **Message hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bản sao (copy / 복사) và zero-copy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Memory-mapped tệp (file / 파일) (`mmap`)

`mmap()` ánh xạ tệp (file / 파일) hoặc anonymous bộ nhớ (memory / 메모리) vào address không gian (space / 공간) của tiến trình (process / 프로세스).

Điều này có thể dùng cho:

- tệp (file / 파일) I/O;
- dùng chung (shared / 공유) libraries;
- dùng chung (shared / 공유) bộ nhớ (memory / 메모리);
- cơ sở dữ liệu (database / 데이터베이스) lưu trữ (storage / 저장소) engines.

Một tệp (file / 파일) ánh xạ (mapping / 매핑) không có nghĩa toàn bộ tệp (file / 파일) được tải (load / 로드) vào RAM ngay. Kernel demand-pages các vùng khi cần.

Xem ánh xạ (mapping / 매핑):

```bash
cat /proc/<PID>/maps
```

> **Chuyển mạch:** Ở chặng này của **Giao tiếp giữa các tiến trình (IPC)**, **Bản sao (copy / 복사) và zero-copy** tiếp nhận điểm tựa từ **Memory-mapped tệp (file / 파일) (mmap)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **sendfile() và Nginx** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bản sao (copy / 복사) và zero-copy

Một dữ liệu (data / 데이터) đường dẫn (path / 경로) thông thường có thể bản sao (copy / 복사) bytes nhiều lần giữa kernel/người dùng (user / 사용자) buffers.

Linux có các cơ chế giảm bản sao (copy / 복사) trong một số trường hợp như:

- `sendfile()`;
- `splice()`;
- bộ nhớ (memory / 메모리) ánh xạ (mapping / 매핑);
- io_uring-related paths;
- DMA ở hardware tầng (layer / 계층).

Web máy chủ (server / 서버) gửi static tệp (file / 파일) có thể dùng `sendfile()` để giảm bản sao (copy / 복사) qua user-space buffer.

Đây là ví dụ hiệu năng (performance / 성능) tối ưu hóa (optimization / 최적화) xuất phát từ hiểu dữ liệu (data / 데이터) movement.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao tiếp giữa các tiến trình (IPC)**, **sendfile() và Nginx** tiếp nhận điểm tựa từ **Bản sao (copy / 복사) và zero-copy** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IPC và tệp (file / 파일) descriptor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## `sendfile()` và Nginx

Nginx có directive `sendfile on;` để tận dụng kernel cơ chế (mechanism / 메커니즘) cho static tệp (file / 파일) trong môi trường phù hợp.

Nhưng mạng (network / 네트워크) filesystem/virtualized filesystem có thể có ngữ nghĩa (semantics / 의미론) khác. Không nên bật/tắt chỉ theo “best practice” mà không benchmark tải công việc (workload / 워크로드) thực.

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **IPC và tệp (file / 파일) descriptor** tiếp nhận điểm tựa từ **sendfile() và Nginx** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Eventfd và epoll** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IPC và tệp (file / 파일) descriptor

Pipe, socket, eventfd và nhiều IPC objects đều được tiến trình (process / 프로세스) giữ qua tệp (file / 파일) descriptor.

Đây là lý do `lsof` và `/proc/<PID>/fd` có thể cho insight về nhiều tài nguyên (resource / 자원) types khác nhau.

```bash
ls -l /proc/<PID>/fd
```

> **Chuyển mạch:** Ở chặng này của **Giao tiếp giữa các tiến trình (IPC)**, **Eventfd và epoll** tiếp nhận điểm tựa từ **IPC và tệp (file / 파일) descriptor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Blocking I/O và non-blocking I/O** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Eventfd và epoll

Linux máy chủ (server / 서버) hiệu năng cao thường cần chờ nhiều tệp (file / 파일) descriptors mà không tạo một luồng thực thi (thread / 스레드) blocking cho từng liên kết (connection / 연결).

`epoll` cho phép một tiến trình (process / 프로세스) đăng ký nhiều descriptors và được thông báo khi descriptor sẵn sàng.

Mô hình tư duy (mental model / 사고 모델):

```text
10,000 sockets
     ↓
epoll interest set
     ↓
threads chỉ xử lý sockets ready
```

Đây là nền tảng của nhiều event-driven servers.

Java NIO `Selector`, Netty vòng lặp sự kiện (event loop / 이벤트 루프) và nút (node / 노드).js/libuv đều có liên kết (connection / 연결) tới readiness-based I/O mechanisms như epoll trên Linux.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao tiếp giữa các tiến trình (IPC)**, **Blocking I/O và non-blocking I/O** tiếp nhận điểm tựa từ **Eventfd và epoll** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Blocking I/O và non-blocking I/O

Với blocking I/O, `read()` có thể làm luồng thực thi (thread / 스레드) ngủ cho tới khi dữ liệu (data / 데이터) sẵn sàng.

Với non-blocking descriptor, lời gọi (call / 호출) có thể trả ngay với trạng thái chưa có dữ liệu (data / 데이터), và ứng dụng (application / 애플리케이션) dùng polling/sự kiện (event / 이벤트) cơ chế (mechanism / 메커니즘) như epoll.

Không có mô hình nào “luôn tốt hơn”. Blocking mã (code / 코드) đơn giản; event-driven mô hình (model / 모델) quy mô (scale / 규모) tốt với nhiều mostly-idle connections nhưng tăng độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **Backpressure** tiếp nhận điểm tựa từ **Blocking I/O và non-blocking I/O** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thundering herd** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backpressure

Nếu producer tạo dữ liệu nhanh hơn bên tiêu thụ (consumer / 소비자) xử lý, buffer cuối cùng đầy.

Pipe/socket có sức chứa (capacity / 용량) hữu hạn. Khi buffer đầy:

- ghi (write / 쓰기) có thể khối (block / 블록);
- non-blocking ghi (write / 쓰기) trả lỗi/trạng thái chưa thể ghi;
- ứng dụng (application / 애플리케이션) phải hàng đợi (queue / 큐)/drop/throttle.

Backpressure không phải khái niệm riêng của Kafka hay reactive programming; nó xuất hiện ngay trong IPC primitives của OS.

> **Chuyển mạch:** Ở chặng này của **Giao tiếp giữa các tiến trình (IPC)**, **Thundering herd** tiếp nhận điểm tựa từ **Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **IPC và bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thundering herd

Nếu nhiều workers cùng chờ một sự kiện (event / 이벤트) và tất cả được đánh thức dù chỉ một worker cần xử lý, scheduler overhead có thể tăng.

Linux và máy chủ (server / 서버) frameworks có nhiều kỹ thuật để giảm thundering herd.

Đây là ví dụ cho việc synchronization thiết kế (design / 설계) ảnh hưởng scalability.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao tiếp giữa các tiến trình (IPC)**, **IPC và bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스)** tiếp nhận điểm tựa từ **Thundering herd** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Gỡ lỗi (debug / 디버그) IPC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## IPC và bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스)

IPC không gian tên (namespace / 네임스페이스) tách một số hệ thống (system / 시스템) V/POSIX IPC resources giữa containers.

Unix socket bind-mounted giữa host/bộ chứa (container / 컨테이너) lại có thể cố ý tạo communication channel xuyên isolation ranh giới (boundary / 경계).

Ví dụ nổi tiếng:

```text
/var/run/docker.sock
```

Mount Docker socket vào bộ chứa (container / 컨테이너) trao quyền điều khiển Docker daemon rất lớn. Đây là ranh giới bảo mật (security boundary / 보안 경계) quan trọng, không chỉ “một tệp (file / 파일) socket”.

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **Gỡ lỗi (debug / 디버그) IPC** tiếp nhận điểm tựa từ **IPC và bộ chứa (container / 컨테이너) không gian tên (namespace / 네임스페이스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Java liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gỡ lỗi (debug / 디버그) IPC

### Pipe/socket descriptors

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
sudo lsof -p <PID>
```

### Unix sockets

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
ss -xl
```

### TCP sockets

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
ss -antp
```

### Dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

Phần này chuyển khái niệm Linux thành thao tác hoặc bằng chứng có thể kiểm tra. Hãy đọc mục tiêu trước, sau đó đối chiếu output với mô hình kernel, process, filesystem hoặc network đã học.

```bash
ls -lah /dev/shm
ipcs
```

`ipcs` hiển thị hệ thống (system / 시스템) V IPC objects nếu hệ thống sử dụng.

### Syscalls

Trước khi chạy hoặc đọc ví dụ dưới đây, hãy xác định câu hỏi vận hành mà nó trả lời, dữ liệu nào sẽ quan sát được và giới hạn của kết quả. Lệnh chỉ có ý nghĩa khi gắn với một giả thuyết về state của hệ thống.

```bash
strace -e trace=network,ipc -p <PID>
```

Hỗ trợ (support / 지원) của dấu vết (trace / 추적) categories phụ thuộc strace phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **Giao tiếp giữa các tiến trình (IPC)**, **Java liên kết (connection / 연결)** tiếp nhận điểm tựa từ **Gỡ lỗi (debug / 디버그) IPC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Java liên kết (connection / 연결)

Trong Java backend:

- `Socket` / Netty channel → socket IPC;
- `FileChannel.map()` → mmap;
- `Selector` → readiness multiplexing, thường epoll trên Linux;
- luồng thực thi (thread / 스레드) coordination → futex ở tầng thời gian chạy (runtime / 런타임)/kernel;
- cơ sở dữ liệu (database / 데이터베이스) liên kết (connection / 연결) pool → tập hợp TCP sockets;
- UNIX lĩnh vực (domain / 도메인) socket hỗ trợ (support / 지원) → cục bộ (local / 로컬) IPC trong các thư viện (library / 라이브러리)/thời gian chạy (runtime / 런타임) hiện đại.

Khi JVM luồng thực thi (thread / 스레드) dump cho thấy nhiều threads `WAITING` hoặc `RUNNABLE` trong mạng (network / 네트워크)/bản địa (native / 네이티브) calls, hiểu IPC giúp giải thích chúng đang chờ cái gì.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Giao tiếp giữa các tiến trình (IPC)**, **Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **Java liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Những hiểu lầm phổ biến

**“IPC chỉ là pipe.”** Linux có pipe, socket, dùng chung (shared / 공유) bộ nhớ (memory / 메모리), semaphore, signals, queues và nhiều cơ chế khác.

**“dùng chung (shared / 공유) bộ nhớ (memory / 메모리) luôn nhanh nhất nên nên dùng.”** Nó giảm bản sao (copy / 복사) nhưng synchronization và tính đúng đắn (correctness / 정확성) phức tạp hơn nhiều.

**“Unix socket và TCP socket giống hệt nhau.”** API có điểm chung nhưng address lĩnh vực (domain / 도메인), routing và bảo mật (security / 보안) ngữ nghĩa (semantics / 의미론) khác.

**“Non-blocking I/O luôn nhanh hơn blocking I/O.”** Hiệu quả phụ thuộc tính đồng thời (concurrency / 동시성) mô hình (model / 모델) và tải công việc (workload / 워크로드).

**“Socket tệp (file / 파일) permission nhỏ nên không nguy hiểm.”** Một socket như Docker daemon socket có thể trao quyền cực lớn.

> **Chuyển mạch:** Trong **Giao tiếp giữa các tiến trình (IPC)**, **Mô hình tư duy** gom các mảnh từ **Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

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

Không chọn thành phần nguyên thủy (primitive / 기본 요소) chỉ vì “nhanh”; chọn theo ngữ nghĩa (semantics / 의미론), thất bại (failure / 실패) mô hình (model / 모델) và maintainability.

Xem thêm: [Files, streams và file descriptors](../01_filesystem/files_streams_descriptors.md), [Networking](../07_networking/networking_dns_sockets_ports.md), [Process và threads](./processes_threads_signals_jobs.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
