# Advanced I/O: epoll, io_uring, zero-copy và DMA

I/O performance không chỉ phụ thuộc device nhanh hay chậm. Nó còn phụ thuộc số lần chuyển user/kernel, số copies, cách application chờ readiness/completion và khả năng giữ nhiều operations in-flight.

## Blocking I/O và concurrency cost

Một blocking `read()` đơn giản và dễ reasoning: thread ngủ tới khi có data. Với hàng chục connections, model này ổn. Với hàng chục nghìn sockets, một thread per connection tạo stack memory, scheduling và context-switch overhead.

Non-blocking I/O tách “connection tồn tại” khỏi “thread đang bị block”. Nhưng application cần mechanism biết fd nào đã sẵn sàng.

## select/poll tới epoll/kqueue

`select`/`poll` thường phải truyền và scan tập descriptors lặp lại. **epoll** trên Linux và **kqueue** trên BSD/macOS giữ interest state trong kernel và trả events thay đổi/sẵn sàng, phù hợp số lượng fd lớn hơn.

Readiness notification không có nghĩa operation đã hoàn thành. Event loop vẫn gọi read/write và phải xử lý partial I/O, edge-triggered semantics, backpressure và lifecycle races.

## Completion model và io_uring

**io_uring** dùng shared ring buffers giữa user space và kernel để submit operations và nhận completion với ít syscall hơn. Nó hướng tới asynchronous completion thay vì chỉ readiness.

Batching nhiều submissions/completions giúp amortize transition cost. Tuy nhiên queue depth quá lớn có thể tăng tail latency và memory pressure. Async không xóa capacity limit; nó chỉ cho phép giữ pipeline đầy hiệu quả hơn.

## DMA

**Direct Memory Access (DMA)** cho device truyền data tới/from RAM mà CPU không phải copy từng byte. CPU vẫn thiết lập descriptors, mapping và xử lý completion/interrupts.

IOMMU có thể kiểm soát DMA address space để device không truy cập tùy ý memory. Đây là connection giữa performance và isolation.

## Zero-copy

“Zero-copy” thường nghĩa giảm copies giữa buffers/layers, không nhất thiết literal zero data movement. `sendfile`, splice-like mechanisms hoặc NIC offload có thể tránh copy user buffer → kernel buffer → socket buffer.

Giảm copy tiết kiệm memory bandwidth và CPU cache pollution, đặc biệt với file serving lớn. Nhưng API phức tạp hơn và không phải workload nhỏ nào cũng hưởng lợi.

## Interrupt, polling và busy-poll

Interrupt tiết kiệm CPU khi event thưa nhưng mỗi interrupt có overhead. High-throughput network có thể dùng interrupt moderation hoặc polling để xử lý batch packets. Busy-poll giảm latency nhưng tiêu CPU ngay cả khi ít work.

Đây là trade-off latency–throughput–energy, không có lựa chọn tuyệt đối tốt.

## Event loop và backpressure

Event-driven server có thể accept work nhanh hơn downstream xử lý. Nếu mọi socket luôn được đọc vào memory queue, process vẫn OOM. Event loop phải phối hợp flow control, bounded queues và admission control.

Xem thêm: [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## Mental Model

> Advanced I/O là bài toán giữ đủ operations in-flight trong khi giảm transitions, copies và idle waits. Nhưng concurrency càng lớn càng cần backpressure; async I/O không tạo thêm bandwidth vật lý.