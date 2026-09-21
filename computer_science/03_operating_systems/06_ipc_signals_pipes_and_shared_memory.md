# IPC: signals, pipes, sockets và shared memory

Processes được isolation để một process không tùy tiện đọc/ghi memory của process khác. Nhưng software hữu ích lại cần cooperation. Inter-process communication (IPC / 프로세스 간 통신) là tập mechanisms cho phép isolated processes trao đổi data hoặc synchronization signals mà vẫn giữ control boundary của OS.

## Isolation tạo ra nhu cầu IPC

Nếu mọi process dùng chung một address space, communication rất dễ nhưng một pointer bug có thể phá toàn hệ thống. OS chọn isolation làm default rồi cung cấp explicit channels cho communication.

Đây là một recurring principle trong CS: **boundary tăng safety nhưng tạo communication cost**.

## Signals: notification với payload nhỏ

Unix signal là asynchronous notification gửi tới process/thread. `SIGTERM` yêu cầu termination có thể handle; `SIGKILL` không thể catch/ignore; `SIGCHLD` báo child state change.

Signal handler chạy trong context đặc biệt nên chỉ một subset operations là async-signal-safe. Gọi arbitrary library code trong handler có thể deadlock hoặc corrupt state.

Signal phù hợp event notification, không phải bulk data transfer.

## Pipes: byte stream qua kernel

Anonymous pipe cung cấp unidirectional byte stream, thường giữa parent-child processes. Shell pipeline:

```bash
producer | consumer
```

kết nối stdout của process trước với stdin process sau qua pipe.

Pipe có kernel buffer hữu hạn. Nếu writer nhanh hơn reader và buffer đầy, writer block hoặc nhận backpressure behavior tùy mode. Đây là một ví dụ rất rõ về queueing và flow control trong cùng máy.

Named pipe/FIFO cho unrelated processes giao tiếp qua filesystem namespace.

## Unix domain sockets

Unix domain socket có API gần network socket nhưng communication local host. Nó hỗ trợ bidirectional streams/datagrams và có thể truyền credentials hoặc file descriptors trên Unix-like systems.

So với TCP loopback, Unix socket bỏ bớt networking overhead và có semantics local-specific hữu ích.

## Shared memory: copy ít hơn, synchronization khó hơn

Shared memory map cùng physical pages vào address spaces của nhiều processes. Data transfer không cần copy qua kernel mỗi message sau khi mapping thiết lập.

Nhưng shared bytes không tự tạo protocol. Processes phải thống nhất layout, ownership, synchronization và lifetime. Mutex/semaphore/atomics hoặc lock-free structures có thể cần thiết.

Vì vậy shared memory đổi **copy/serialization cost** lấy **coordination complexity**.

## Message queues và mailbox model

OS hoặc runtime có thể cung cấp message queues. Sender gửi discrete messages; receiver đọc theo boundaries rõ hơn byte stream.

Message passing giảm shared mutable state và có thể mở đường chuyển từ local process communication sang distributed communication. Nhưng queue semantics—ordering, capacity, delivery—phải được xác định rõ.

## Memory-mapped files như bridge giữa IPC và storage

Nhiều processes có thể `mmap` cùng file và chia sẻ pages backed bởi filesystem. Điều này hữu ích cho databases, shared indexes hoặc large datasets.

Tuy nhiên persistence semantics, cache coherence và synchronization vẫn cần reasoning riêng. “Cùng nhìn thấy bytes” không tự động nghĩa application state transactionally consistent.

## Copy cost, context switch và zero-copy

Traditional I/O path có thể copy data nhiều lần giữa user/kernel buffers. Mechanisms như `sendfile`, `splice`, shared buffers hoặc DMA giảm copies/context transitions trong một số path.

Zero-copy thường nghĩa “giảm một hoặc nhiều CPU copies”, không phải data không bao giờ di chuyển trong hardware.

## Common Misconceptions

**“Shared memory luôn nhanh nhất nên luôn tốt nhất.”** Raw transfer có thể nhanh, nhưng synchronization bugs và cache contention có thể làm system khó đúng và khó maintain.

**“Pipe là message queue.”** Pipe là byte stream; application phải tự framing nếu cần message boundaries.

**“Signal giống exception.”** Signal là asynchronous process-level event với restrictions rất khác synchronous language exception.

## Mental Model

> IPC là thiết kế một explicit channel xuyên isolation boundary. Mỗi mechanism chọn khác nhau giữa copy cost, framing, synchronization, safety và portability.

## Kết nối

Đọc cùng [process/thread](./01_processes_threads_and_scheduling.md), [concurrency](./02_concurrency_synchronization_and_deadlock.md), [socket/networking](../06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md) và [state/queues/backpressure](../08_software_systems/03_state_queues_backpressure_and_boundaries.md).
