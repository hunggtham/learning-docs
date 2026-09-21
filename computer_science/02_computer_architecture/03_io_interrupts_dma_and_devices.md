# I/O, interrupt, DMA và devices

CPU không hữu ích nếu không giao tiếp storage, keyboard, display, NIC, sensors hay accelerators. Input/Output — I/O (입출력) là boundary giữa computation core và external devices, nơi speed mismatch rất lớn và asynchronous behavior xuất hiện.

## Device registers và controllers

Hardware device thường được điều khiển qua controller expose registers/queues. CPU/driver ghi commands, đọc status và map buffers. Memory-mapped I/O làm device registers xuất hiện trong address space; special instructions là một model khác.

Driver (장치 드라이버 / trình điều khiển) trong OS biến device-specific protocol thành generic abstractions như block device, network interface hoặc character device.

## Polling vs interrupt

Polling: CPU liên tục hỏi “xong chưa?”. Nếu event rất nhanh/dày, polling có thể hiệu quả vì tránh interrupt overhead; nếu event hiếm, nó lãng phí CPU.

Interrupt: device báo CPU khi cần attention. CPU tạm chuyển tới handler, sau đó scheduler/driver tiếp tục processing. Interrupt giảm busy waiting nhưng có context/coordination overhead; high-rate devices thường batch/interrupt-coalesce.

Trade-off không phải polling xấu, interrupt tốt; nó phụ thuộc event rate và latency target.

## DMA

Nếu CPU phải copy từng byte từ NIC/storage controller vào RAM, throughput bị giới hạn và CPU bận việc đơn giản. Direct Memory Access — DMA cho phép device/controller transfer data trực tiếp tới/from memory sau khi CPU setup descriptor/buffer.

CPU vẫn orchestration, nhưng bulk transfer không cần instruction cho từng word. NIC rings, NVMe queues và GPU transfers đều dùng DMA concepts.

## Memory-mapped I/O và ordering

Access device registers không giống normal cached RAM. Reads/writes có side effects và ordering requirements. Compiler/CPU reordering phải được kiểm soát bằng volatile semantics, memory barriers hoặc architecture-specific rules trong kernel/driver code.

Đây cho thấy “load/store” ở source/assembly có semantics phụ thuộc address region và memory model.

## Blocking, non-blocking và asynchronous I/O

Blocking I/O cho caller ngủ/chờ đến khi operation progress đủ. Non-blocking trả ngay nếu chưa ready. Async I/O submit request rồi completion đến qua callback/event/completion queue.

Tầng API khác hardware interrupt nhưng mental model tương tự: đừng giữ CPU busy khi latency nằm ngoài CPU.

High-concurrency servers dùng event loop, async runtimes hoặc many lightweight threads để quản lý hàng nghìn I/O waits mà không cần one OS thread per idle connection.

## Buffering

Buffers hấp thụ speed mismatch và batch operations. User buffer, kernel page cache, device cache và controller queue có thể cùng tồn tại. `write()` thành công không nhất thiết data đã tới stable medium; durability cần flush/fsync semantics và storage guarantees.

Điều này quan trọng cho database WAL và filesystem correctness.

## Device latency và queue depth

Modern SSD/NVMe có thể xử lý nhiều requests concurrent. Queue depth đủ giúp khai thác parallelism; quá nhiều requests tăng queueing latency. Throughput và latency vì vậy trade-off theo load.

## Mental Model

> I/O là **asynchronous conversation với thiết bị chậm/khác tốc độ**. CPU setup work, buffers giữ data, interrupt/completion báo tiến độ, DMA chuyển bulk bytes, OS driver cung cấp abstraction.

## Common Misconceptions

**“Interrupt luôn nhanh hơn polling.”** High-rate workloads có thể polling/batching tốt hơn.

**“write() trả về nghĩa dữ liệu đã bền trên disk.”** Thường chỉ nghĩa kernel accepted bytes; durability phụ thuộc buffering/filesystem/device flush.

**“DMA không dùng CPU.”** CPU vẫn setup queues/descriptors và xử lý completion; DMA giảm per-byte copy work.

## Kết nối

I/O là nền của [kernel/syscalls](../03_operating_systems/00_kernel_syscalls_and_os_abstractions.md), [filesystem](../03_operating_systems/04_filesystems_storage_and_io.md), [database durability](../05_data_databases/04_storage_logs_recovery_and_durability.md) và [network packets](../06_networks_distributed_systems/00_network_layers_packets_and_encapsulation.md).
