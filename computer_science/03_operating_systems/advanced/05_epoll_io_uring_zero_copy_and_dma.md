# Advanced I/O: epoll, io_uring, zero-copy và DMA

I/O performance không chỉ phụ thuộc device nhanh hay chậm. Nó phụ thuộc cách application biểu diễn concurrency, số lần chuyển user/kernel, số copies, queue depth, ownership của buffers và việc application biết một operation **sẵn sàng** hay **đã hoàn tất** bằng cách nào.

Mental model trung tâm là: **async I/O đổi cách chờ và cách giữ operations in-flight; nó không tạo thêm bandwidth vật lý.** Khi concurrency tăng, correctness phải giữ lifetime/ownership của fd và buffers, còn performance phải giữ queue debt trong giới hạn downstream xử lý được.

## 1. Bài toán ban đầu: nhiều logical operations hơn số execution threads

Một blocking `read()` đơn giản và dễ reasoning: thread ngủ tới khi có data. Với số connection nhỏ, model này có thể hoàn toàn tốt. Khi có hàng chục nghìn sockets hoặc nhiều storage operations chờ đồng thời, one-thread-per-operation tạo stack memory, scheduler overhead và context switches không cần thiết.

Non-blocking/async I/O tách:

```text
logical operation đang tồn tại
≠
OS thread phải đứng yên chờ operation đó
```

Đây là invariant tài nguyên, không phải lời hứa rằng mỗi operation sẽ nhanh hơn.

## 2. Readiness và completion là hai contract khác nhau

**Readiness model** báo rằng một fd *có khả năng* thực hiện operation mà không block theo điều kiện hiện tại. `epoll`/`kqueue` thuộc family này.

**Completion model** báo rằng operation đã được submit và kernel/runtime trả completion khi nó kết thúc. `io_uring`, IOCP và nhiều async storage APIs thuộc family này ở mức abstraction khác nhau.

```text
readiness:
ready event → application gọi read/write → operation có thể partial

completion:
submit operation → kernel/device xử lý → completion event/result
```

Nhầm hai model tạo bug: “socket writable” không nghĩa toàn buffer đã gửi; “completion nhận được” mới là boundary cho operation cụ thể đã submit.

## 3. `select`/`poll` tới `epoll`/`kqueue`: giữ interest state ở đâu?

`select`/`poll` thường yêu cầu application đưa tập descriptors vào kernel và scan kết quả lặp lại. `epoll`/`kqueue` giữ registration/interest state phía kernel và trả các events liên quan, giảm overhead khi tập fd rất lớn nhưng chỉ ít fd active.

Invariant không phải “epoll luôn O(1) và nhanh”. Cost vẫn phụ thuộc event rate, wakeups, lock contention, cache locality và application xử lý event thế nào.

Một event loop vẫn phải xử lý partial read/write, `EAGAIN`-like conditions, closed peer và fd lifecycle chính xác.

## 4. Level-triggered và edge-triggered thay đổi protocol đọc event

Với level-triggered semantics, event có thể tiếp tục được báo khi condition còn đúng. Với edge-triggered semantics, application thường phải **drain** resource tới trạng thái “không còn làm tiếp được” trước khi chờ edge mới.

Failure điển hình:

```text
edge arrives
→ application đọc chỉ một phần
→ data vẫn còn nhưng app không drain
→ không có state transition mới để tạo edge tiếp
→ connection trông như “treo”
```

Đây là protocol bug ở application, không phải kernel đánh mất packet.

## 5. Partial I/O là normal behavior, không phải rare error

`read` có thể trả ít bytes hơn message logic; `write` có thể chỉ accept một phần buffer. TCP là byte stream nên application phải giữ framing/state riêng.

Một robust event loop cần state machine:

```text
bytes expected
bytes received/sent
buffer ownership
current protocol state
deadline/cancellation
```

Nếu code giả định “một write gửi cả response”, bug sẽ chỉ xuất hiện dưới pressure khi socket buffer đầy hơn—đúng lúc production khác local test.

## 6. FD lifecycle và stale event race

File descriptor là một integer handle có thể được kernel tái sử dụng sau close. Nếu application giữ event cũ rồi descriptor number được cấp lại cho connection khác, xử lý event stale theo chỉ số fd đơn thuần có thể tác động nhầm object.

Runtime thường cần generation/token hoặc object identity/lifecycle rule rõ. Invariant là:

> Một completion/readiness event chỉ được áp dụng cho logical resource đã tạo registration/operation đó, không phải bất kỳ resource mới nào tình cờ có cùng integer handle.

Đây là cùng family với ABA: identity và lifetime không thể suy ra chỉ từ bit pattern của handle.

## 7. `io_uring`: submission/completion rings đổi syscall path, không đổi capacity

`io_uring` dùng shared ring structures để user space submit operations và kernel trả completion. Batching submission/completion có thể amortize syscall/transition cost và giữ nhiều operations in-flight.

Simplified:

```text
prepare SQ entries
→ publish to submission ring
→ kernel consumes
→ operation waits/runs through subsystem/device
→ CQ entry appears
→ application reaps completion
```

Correctness cần ownership rõ: entry nào thuộc operation nào, buffer còn sống tới khi nào, cancellation/timeout race với completion ra sao.

## 8. Queue depth: quá ít thì device idle, quá nhiều thì tail latency phình

Storage/NIC thường cần nhiều requests in-flight để đạt throughput. Nhưng queue sâu tạo waiting time và giữ nhiều memory/state hơn.

```text
queue depth thấp quá
→ pipeline/device không đủ work
→ utilization thấp

queue depth cao quá
→ waiting time + memory + tail latency tăng
→ cancellation làm nhiều zombie work
```

Điểm tối ưu phụ thuộc device, workload, request size và SLO. Async API không thay định luật queueing.

## 9. Cancellation là một state transition, không phải xóa lịch sử operation

Khi cancel một async operation, có race:

```text
operation chưa bắt đầu
operation đang chạy
operation vừa complete nhưng completion chưa được reap
cancel request đang đến
```

Application phải chấp nhận semantics mà API cung cấp: cancellation có thể thành công, fail vì operation đã hoàn thành, hoặc completion vẫn phải được consume để giải phóng resource.

Invariant quan trọng là buffer/resource chỉ được free/reuse sau boundary mà API bảo đảm kernel/device không còn truy cập nó.

## 10. Registered/pinned buffers đổi syscall/copy cost thành lifetime cost

Một số async mechanisms cho phép register hoặc pin buffers để giảm repeated mapping/setup. Performance tốt hơn nhưng memory đó ít linh hoạt hơn với allocator/reclaim và ownership protocol phức tạp hơn.

Nếu buffer được tái sử dụng trước completion, DMA/kernel có thể ghi vào memory hiện đã thuộc logical request khác. Đây là correctness bug do lifetime, không phải “data corruption ngẫu nhiên”.

## 11. DMA: CPU không copy từng byte nhưng vẫn quản lý protocol

**Direct Memory Access (DMA)** cho device truyền data tới/from RAM mà CPU không phải thực hiện từng load/store. CPU vẫn thiết lập descriptors, mappings, queues và xử lý completion.

IOMMU tạo address-translation/isolation boundary cho DMA để device không có quyền truy cập arbitrary physical memory. Vì vậy performance path đi cùng security/isolation path:

```text
user buffer
→ kernel mapping/pinning
→ DMA descriptor
→ IOMMU translation
→ device transfer
→ completion
```

Lower abstraction quyết định latency có thể là IOMMU/TLB, PCIe/interconnect hoặc device queue, không phải user-space function.

## 12. Zero-copy là giảm copies, không phải “data không di chuyển”

“Zero-copy” thường nghĩa loại bỏ một hoặc nhiều copies giữa layers. `sendfile`, splice-like paths, memory mapping hoặc NIC offloads có thể tránh user-buffer → kernel-buffer copy trong một số workloads.

Nhưng data vẫn di chuyển qua memory/interconnect/NIC. Invariant mới xuất hiện: buffer/page phải sống đủ lâu và không bị mutate sai lúc device/kernel còn reference.

Zero-copy có lợi khi copy + memory bandwidth là bottleneck; với payload nhỏ, setup/lifetime complexity có thể lớn hơn lợi ích.

## 13. Interrupt, interrupt moderation và polling là trade-off latency–throughput–CPU

Interrupt phù hợp event thưa: CPU làm việc khác rồi được đánh thức. Ở packet rate cao, một interrupt mỗi event có overhead lớn; hệ thống có thể coalesce/moderate interrupts hoặc chuyển sang polling/batched processing.

Busy-poll có thể giảm wakeup latency nhưng dùng CPU ngay cả khi ít work. Không có mode “luôn nhanh nhất”; workload thay đổi thì operating point tối ưu cũng thay đổi.

## 14. Event loop vẫn có thể bị starvation

Non-blocking socket không giúp nếu callback chạy CPU-heavy 100 ms trên single event-loop thread. Trong lúc đó hàng nghìn connections ready nhưng không được service.

Evidence phải tách:

```text
kernel/device wait
runtime ready-queue wait
on-CPU callback time
GC/runtime pause
network/storage service time
```

CPU toàn máy có thể chỉ 20% trên máy nhiều core nhưng một event-loop core đã saturated.

## 15. Backpressure phải bắt đầu trước khi buffers đầy

Event-driven server có thể accept/read work nhanh hơn downstream xử lý. Nếu mọi socket được drain vào unbounded user-space queue, process chỉ chuyển queue từ kernel sang heap.

Causal loop:

```text
arrival > service capacity
→ user queue grows
→ memory + latency grow
→ deadlines expire
→ clients retry
→ arrival grows further
→ OOM/cascading failure
```

Bounded queues, per-connection/per-tenant limits, flow control, semaphore/admission control và stop-reading strategy là các cách biểu diễn capacity. Đọc [Queueing, tail latency và backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

## 16. Performance pressure làm behavior đổi phase

Ở low concurrency, syscall/copy overhead có thể negligible. Khi QPS tăng, transition/copy/cache pollution trở nên đáng kể; batching và async giúp throughput. Khi concurrency tiếp tục tăng, queue wait và memory pressure lại dominate.

Vì vậy “io_uring nhanh hơn epoll” không phải universal conclusion. Hai models phù hợp operation mix khác nhau; benchmark phải giữ request size, concurrency, queue depth, CPU pinning, device/network conditions và SLO tương đồng.

## 17. Production evidence

Evidence hữu ích theo tầng:

```text
Application/runtime:
- event-loop lag / ready-queue wait
- active operations, queue depth, cancellation/timeout
- buffer pool / allocator pressure
- syscall rate và batch size

OS:
- runnable vs blocked/off-CPU time
- context switch / wakeup rate
- fd/socket state, send/receive queue
- I/O scheduler/block queue latency

Hardware/device:
- NIC/storage queue depth
- interrupt/poll rate
- throughput, packet/drop/retransmission hoặc device errors
- memory bandwidth / NUMA locality khi copy path nghi ngờ
```

Một flame graph on-CPU không giải thích thời gian đang nằm trong device queue; một storage latency graph không giải thích event-loop starvation. Cần causal timeline xuyên layers.

## 18. Failure reasoning theo abstraction layer

Nếu fd “ready nhưng không chạy tiếp”, kiểm tra edge-triggered drain/lifecycle trước khi nghi kernel. Nếu data bị ghi vào request sai, kiểm tra buffer/fd identity và late completion. Nếu throughput thấp nhưng device idle, xem queue depth/submission batching. Nếu p99 tăng khi QPS cao, xem queue/backpressure trước khi chỉ tối ưu syscall.

## 19. Mô hình tư duy

> Advanced I/O là bài toán **ownership + queues + completion semantics**. Readiness cho biết lúc nào nên thử; completion cho biết operation nào đã kết thúc; DMA/zero-copy giảm CPU/copy cost nhưng làm buffer lifetime quan trọng hơn; async giữ pipeline đầy nhưng không tạo capacity. **Khi concurrency tăng, backpressure quyết định hệ thống còn ổn định hay chỉ tích lũy work nhanh hơn.**

## Kết nối

Ôn [OS async I/O foundation](../../basic/03_operating_systems/07_boot_device_drivers_and_async_io.md), [runtime coroutine/event loop](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md), [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [end-to-end request path](../../90_connections/advanced/01_end_to_end_latency_browser_edge_service_db_storage.md).