# Boot, device drivers và asynchronous I/O

Một program gọi `read()` và nhận bytes, nhưng để bytes đi từ SSD/NIC/keyboard tới user space cần firmware, kernel, drivers, interrupts, DMA, queues và scheduler. Chapter này nối abstraction “device/file/socket” với cơ chế OS phía dưới.

## Từ power-on đến user space

Khi máy bật, CPU bắt đầu tại một reset vector xác định bởi architecture. Firmware như UEFI khởi tạo phần cứng cơ bản, chọn boot target và load bootloader hoặc OS image.

Kernel sau đó thiết lập memory management, interrupt tables, scheduler, device discovery/drivers, mount root filesystem và cuối cùng start init/service manager rồi user-space processes.

Boot sequence cho thấy OS không xuất hiện “từ hư không”; nó phải tự xây những abstractions mà applications sau đó coi là mặc định.

## Device driver là translator giữa OS model và hardware protocol

Driver (장치 드라이버) biết registers, command queues và interrupt behavior của device, đồng thời expose interface mà kernel subsystems hiểu.

Filesystem không nên biết chi tiết từng NVMe controller; network stack không nên biết từng NIC model. Driver là abstraction adapter ở boundary hardware-specific.

Một buggy kernel driver nguy hiểm vì chạy privileged. User-space drivers và sandboxing được dùng ở một số architectures để giảm blast radius.

## Memory-mapped I/O và port I/O

Nhiều devices expose control/status registers vào memory address space. CPU đọc/ghi addresses đặc biệt để command device. Đây là memory-mapped I/O (MMIO).

Các accesses này có ordering/volatility semantics khác normal RAM; compiler/CPU không được tự do optimize như ordinary memory. Hardware programming vì vậy gắn chặt với memory barriers và architecture rules.

## Interrupt và polling

Nếu CPU liên tục hỏi device “xong chưa?” thì đó là polling. Polling đơn giản và có latency thấp khi event rate cực cao, nhưng waste CPU nếu events thưa.

Interrupt cho device báo CPU khi cần attention. Interrupt có overhead context/handler, nên modern systems có hybrid strategies như interrupt moderation hoặc busy polling trong high-performance networking.

## DMA: device chuyển data mà CPU không copy từng byte

Direct Memory Access (DMA) cho device đọc/ghi RAM theo descriptors do driver thiết lập. CPU setup transfer, device thực hiện bulk data movement, rồi completion được báo bằng interrupt hoặc queue polling.

DMA tăng performance nhưng tạo security requirement: device không được tùy ý access toàn memory. IOMMU cung cấp address translation/isolation cho device tương tự virtual memory cho CPU.

## Blocking, non-blocking và asynchronous I/O

Blocking I/O làm thread chờ cho tới khi operation có thể hoàn thành hoặc có data. Non-blocking I/O trả ngay nếu chưa sẵn sàng, thường với status như `EAGAIN`.

Readiness APIs như `select`, `poll`, `epoll`, `kqueue` báo descriptors nào sẵn sàng. Completion-based APIs như IOCP hoặc `io_uring` có thể biểu diễn “submit operation, nhận completion sau”.

Async syntax trong language không tự quyết OS I/O model. Một `async/await` runtime có thể đứng trên readiness, completion ports, thread pool hoặc combination.

## Thundering herd và event loops

Nếu nhiều workers cùng thức dậy vì một event nhưng chỉ một worker có work, hệ thống lãng phí scheduling/context switches. Kernel/runtime designs cố tránh thundering herd bằng wakeup policies và queue ownership.

Event loop xử lý nhiều concurrent connections với ít threads bằng cách multiplex I/O readiness/completions. Nó hiệu quả khi tasks chủ yếu I/O-bound và handlers không block dài.

## Common Misconceptions

**“Async nghĩa là chạy song song.”** Async là về waiting/concurrency; parallel execution cần nhiều execution resources hoặc threads/cores.

**“Interrupt luôn tốt hơn polling.”** Workload event-rate cao có thể khiến polling hoặc hybrid efficient hơn.

**“Driver chỉ là thư viện.”** Kernel driver có privilege và hardware access đặc biệt; failure impact khác user-space library.

## Mental Model

> I/O là pipeline điều phối giữa CPU, memory và device. OS chọn khi CPU nên chạy, khi nên ngủ, ai sở hữu buffer và completion được báo bằng cơ chế nào.

## Kết nối

Đọc cùng [I/O, interrupt và DMA ở architecture](../02_computer_architecture/03_io_interrupts_dma_and_devices.md), [process scheduling](./01_processes_threads_and_scheduling.md), [IPC](./06_ipc_signals_pipes_and_shared_memory.md) và [network sockets](../06_networks_distributed_systems/06_sockets_ipv6_nat_firewalls_and_vpn.md).
