# IPC: signals, pipes, sockets và dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **IPC: signals, pipes, sockets và dùng chung (shared / 공유) bộ nhớ (memory / 메모리)**. Route đi từ process isolation → signal/pipe/socket semantics → shared memory/synchronization → backpressure, failure và observability, để kênh IPC được chọn theo payload, ordering và lifetime.

Processes được isolation để một tiến trình (process / 프로세스) không tùy tiện đọc/ghi bộ nhớ (memory / 메모리) của tiến trình (process / 프로세스) khác. Nhưng software hữu ích lại cần cooperation. Inter-process communication (IPC / 프로세스 간 통신) là tập mechanisms cho phép isolated processes trao đổi dữ liệu (data / 데이터) hoặc synchronization signals mà vẫn giữ điều khiển (control / 제어) ranh giới (boundary / 경계) của OS.

## Isolation tạo ra nhu cầu IPC

Nếu mọi tiến trình (process / 프로세스) dùng chung một address không gian (space / 공간), communication rất dễ nhưng một pointer bug có thể phá toàn hệ thống. OS chọn isolation làm default rồi cung cấp tường minh (explicit / 명시적) channels cho communication.

Đây là một recurring principle trong CS: **ranh giới (boundary / 경계) tăng an toàn (safety / 안전) nhưng tạo communication chi phí (cost / 비용)**.

> **Nối mạch:** **Signals: notification với payload nhỏ** nối từ **Isolation tạo ra nhu cầu IPC** sang **Pipes: byte stream qua kernel**, vì cơ chế trước tạo đầu vào cho bước sau.

## Signals: notification với payload nhỏ

Unix tín hiệu (signal / 신호) là asynchronous notification gửi tới tiến trình (process / 프로세스)/luồng thực thi (thread / 스레드). `SIGTERM` yêu cầu termination có thể handle; `SIGKILL` không thể catch/ignore; `SIGCHLD` báo child trạng thái (state / 상태) thay đổi (change / 변경).

Tín hiệu (signal / 신호) handler chạy trong ngữ cảnh (context / 맥락) đặc biệt nên chỉ một subset operations là async-signal-safe. Gọi arbitrary thư viện (library / 라이브러리) mã (code / 코드) trong handler có thể deadlock hoặc corrupt trạng thái (state / 상태).

Tín hiệu (signal / 신호) phù hợp sự kiện (event / 이벤트) notification, không phải bulk dữ liệu (data / 데이터) transfer.

> **Nối mạch:** **Pipes: byte stream qua kernel** nối từ **Signals: notification với payload nhỏ** sang **Unix lĩnh vực (domain / 도메인) sockets**, vì cơ chế trước tạo đầu vào cho bước sau.

## Pipes: byte stream qua kernel

Anonymous pipe cung cấp unidirectional byte stream, thường giữa parent-child processes. Shell chuỗi xử lý (pipeline / 파이프라인):

```bash
producer | consumer
```

kết nối stdout của tiến trình (process / 프로세스) trước với stdin tiến trình (process / 프로세스) sau qua pipe.

Pipe có kernel buffer hữu hạn. Nếu writer nhanh hơn reader và buffer đầy, writer khối (block / 블록) hoặc nhận backpressure hành vi (behavior / 동작) tùy chế độ (mode / 모드). Đây là một ví dụ rất rõ về queueing và luồng (flow / 흐름) điều khiển (control / 제어) trong cùng máy.

Named pipe/FIFO cho unrelated processes giao tiếp qua filesystem không gian tên (namespace / 네임스페이스).

> **Nối mạch:** **Unix lĩnh vực (domain / 도메인) sockets** nối từ **Pipes: byte stream qua kernel** sang **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리): bản sao (copy / 복사) ít hơn, synchronization khó hơn**, vì cơ chế trước tạo đầu vào cho bước sau.

## Unix lĩnh vực (domain / 도메인) sockets

Unix lĩnh vực (domain / 도메인) socket có API gần mạng (network / 네트워크) socket nhưng communication cục bộ (local / 로컬) host. Nó hỗ trợ bidirectional streams/datagrams và có thể truyền credentials hoặc tệp (file / 파일) descriptors trên Unix-like các hệ thống (systems / 시스템들).

So với TCP loopback, Unix socket bỏ bớt networking overhead và có ngữ nghĩa (semantics / 의미론) local-specific hữu ích.

> **Nối mạch:** **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리): bản sao (copy / 복사) ít hơn, synchronization khó hơn** nối từ **Unix lĩnh vực (domain / 도메인) sockets** sang **Message queues và mailbox mô hình (model / 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (shared / 공유) bộ nhớ (memory / 메모리): bản sao (copy / 복사) ít hơn, synchronization khó hơn

Dùng chung (shared / 공유) bộ nhớ (memory / 메모리) map cùng vật lý (physical / 물리적) pages vào address spaces của nhiều processes. dữ liệu (data / 데이터) transfer không cần bản sao (copy / 복사) qua kernel mỗi message sau khi ánh xạ (mapping / 매핑) thiết lập.

Nhưng dùng chung (shared / 공유) bytes không tự tạo giao thức (protocol / 프로토콜). Processes phải thống nhất bố cục (layout / 레이아웃), quyền sở hữu (ownership / 소유권), synchronization và thời gian tồn tại (lifetime / 수명). Mutex/semaphore/atomics hoặc lock-free structures có thể cần thiết.

Vì vậy dùng chung (shared / 공유) bộ nhớ (memory / 메모리) đổi **bản sao (copy / 복사)/serialization chi phí (cost / 비용)** lấy **coordination độ phức tạp (complexity / 복잡도)**.

> **Nối mạch:** **Message queues và mailbox mô hình (model / 모델)** nối từ **Dùng chung (shared / 공유) bộ nhớ (memory / 메모리): bản sao (copy / 복사) ít hơn, synchronization khó hơn** sang **Memory-mapped files như cầu nối (bridge / 브리지) giữa IPC và lưu trữ (storage / 저장소)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Message queues và mailbox mô hình (model / 모델)

OS hoặc thời gian chạy (runtime / 런타임) có thể cung cấp message queues. Sender gửi discrete messages; receiver đọc theo boundaries rõ hơn byte stream.

Message passing giảm dùng chung (shared / 공유) mutable trạng thái (state / 상태) và có thể mở đường chuyển từ cục bộ (local / 로컬) tiến trình (process / 프로세스) communication sang phân tán (distributed / 분산) communication. Nhưng hàng đợi (queue / 큐) ngữ nghĩa (semantics / 의미론)—thứ tự (ordering / 순서), sức chứa (capacity / 용량), delivery—phải được xác định rõ.

> **Nối mạch:** **Memory-mapped files như cầu nối (bridge / 브리지) giữa IPC và lưu trữ (storage / 저장소)** nối từ **Message queues và mailbox mô hình (model / 모델)** sang **Bản sao (copy / 복사) chi phí (cost / 비용), ngữ cảnh (context / 맥락) switch và zero-copy**, vì cơ chế trước tạo đầu vào cho bước sau.

## Memory-mapped files như cầu nối (bridge / 브리지) giữa IPC và lưu trữ (storage / 저장소)

Nhiều processes có thể `mmap` cùng tệp (file / 파일) và chia sẻ pages backed bởi filesystem. Điều này hữu ích cho databases, dùng chung (shared / 공유) indexes hoặc large datasets.

Tuy nhiên persistence ngữ nghĩa (semantics / 의미론), bộ nhớ đệm (cache / 캐시) coherence và synchronization vẫn cần lập luận (reasoning / 추론) riêng. “Cùng nhìn thấy bytes” không tự động nghĩa ứng dụng (application / 애플리케이션) trạng thái (state / 상태) transactionally consistent.

> **Nối mạch:** **Bản sao (copy / 복사) chi phí (cost / 비용), ngữ cảnh (context / 맥락) switch và zero-copy** nối từ **Memory-mapped files như cầu nối (bridge / 브리지) giữa IPC và lưu trữ (storage / 저장소)** sang **Dùng chung (common / 공통) Misconceptions**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bản sao (copy / 복사) chi phí (cost / 비용), ngữ cảnh (context / 맥락) switch và zero-copy

Traditional I/O đường dẫn (path / 경로) có thể bản sao (copy / 복사) dữ liệu (data / 데이터) nhiều lần giữa người dùng (user / 사용자)/kernel buffers. Mechanisms như `sendfile`, `splice`, dùng chung (shared / 공유) buffers hoặc DMA giảm copies/ngữ cảnh (context / 맥락) transitions trong một số đường dẫn (path / 경로).

Zero-copy thường nghĩa “giảm một hoặc nhiều CPU copies”, không phải dữ liệu (data / 데이터) không bao giờ di chuyển trong hardware.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Bản sao (copy / 복사) chi phí (cost / 비용), ngữ cảnh (context / 맥락) switch và zero-copy** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“dùng chung (shared / 공유) bộ nhớ (memory / 메모리) luôn nhanh nhất nên luôn tốt nhất.”** Raw transfer có thể nhanh, nhưng synchronization bugs và bộ nhớ đệm (cache / 캐시) contention có thể làm hệ thống (system / 시스템) khó đúng và khó maintain.

**“Pipe là message hàng đợi (queue / 큐).”** Pipe là byte stream; ứng dụng (application / 애플리케이션) phải tự framing nếu cần message boundaries.

**“tín hiệu (signal / 신호) giống exception.”** tín hiệu (signal / 신호) là asynchronous process-level sự kiện (event / 이벤트) với restrictions rất khác synchronous ngôn ngữ (language / 언어) exception.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> IPC là thiết kế một tường minh (explicit / 명시적) channel xuyên isolation ranh giới (boundary / 경계). Mỗi cơ chế (mechanism / 메커니즘) chọn khác nhau giữa bản sao (copy / 복사) chi phí (cost / 비용), framing, synchronization, an toàn (safety / 안전) và portability.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc cùng [process/thread](./01_processes_threads_and_scheduling.md), [concurrency](./02_concurrency_synchronization_and_deadlock.md), [socket/networking](../06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) và [state/queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
