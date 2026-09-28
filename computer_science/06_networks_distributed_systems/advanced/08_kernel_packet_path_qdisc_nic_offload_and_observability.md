# Kernel packet path, qdisc, NIC offload và observability

Một request HTTP có thể chậm dù application không dùng nhiều CPU, database ổn và network interface vẫn báo băng thông còn dư. Lý do là “network” không phải một hop duy nhất. Packet đi qua nhiều queue và abstraction: socket buffer, transport state, IP routing, firewall/policy, traffic control, driver ring, NIC queue, physical link; chiều nhận đi theo chuỗi ngược lại với interrupt/NAPI, receive queue và socket wakeup.

Chapter này đặt kernel packet path trong boundary Networks & Distributed Systems nhưng cross-link chặt với Operating Systems. Mục tiêu không phải học tên từng Linux function. Mục tiêu là biết **packet đang chờ ở đâu, queue nào sở hữu nó, backpressure được truyền hay bị che ở đâu và offload nào làm evidence nhìn khác với wire reality**.

Mental model:

```text
application write
→ socket send buffer
→ TCP/UDP/IP state
→ routing / policy
→ qdisc / traffic control
→ driver TX ring
→ NIC hardware queue
→ wire

wire
→ NIC RX ring
→ interrupt / polling
→ kernel network stack
→ socket receive buffer
→ application read
```

Invariant cơ bản là bytes/packets phải được xử lý theo semantics của protocol và policy, trong khi mỗi tầng giữ queue hữu hạn và có thể drop, delay, coalesce hoặc batch work.

## 1. Socket API che rất nhiều queue

Khi application gọi `send` hoặc `write`, việc call trả về không đồng nghĩa peer đã nhận bytes. Thông thường dữ liệu mới được copy hoặc reference vào kernel-owned buffer và được transport/network stack xử lý tiếp.

Vì vậy cần phân biệt:

```text
application accepted bytes
≠ kernel transmitted packet
≠ NIC put frame on wire
≠ peer received bytes
≠ peer application consumed bytes
```

Một syscall nhanh chỉ chứng minh enqueue ở boundary gần application diễn ra nhanh. Nó không chứng minh downstream không đang backlog.

## 2. Send buffer và receive buffer là flow-control boundary

Socket send buffer hấp thụ burst giữa tốc độ producer của application và tốc độ network/peer có thể nhận. Nếu downstream chậm, buffer đầy và application cuối cùng phải block, nhận `EAGAIN` trong non-blocking mode hoặc thấy async write không progress.

Receive buffer làm điều tương tự ở chiều vào. Nếu application đọc chậm, buffer tăng. Với TCP, advertised receive window có thể giảm để truyền backpressure tới sender. Với UDP, không có reliable stream flow control; receive queue đầy có thể dẫn tới drop.

Điểm quan trọng là buffer không tạo capacity mới. Nó chỉ đổi **khi nào** pressure lộ ra.

## 3. TCP state quyết định packet nào được phép gửi

TCP sender không chỉ nhìn socket buffer. Nó còn bị giới hạn bởi congestion window, receive window, pacing, retransmission state và bytes đang in flight.

Có thể hình dung send permission gần đúng như:

```text
sendable ≈ min(congestion window, receive window) - in-flight data
```

Nếu congestion control giảm window sau loss/ECN signal, application có thể vẫn tiếp tục enqueue cho tới khi send buffer đầy. Đây tạo delay giữa network congestion và application-visible backpressure.

Do đó throughput thấp với send buffer lớn chưa chắc là NIC bottleneck; có thể transport cố ý giới hạn flight size.

## 4. Routing decision và policy không dừng ở bảng route

Sau khi packet có network-layer destination, kernel phải chọn route, output interface và next hop theo routing/policy state. Namespace, VRF, policy routing, firewall/NAT hoặc tunnel có thể làm path khác trực giác “destination IP → interface”.

BGP ở control plane có thể quyết định route được học như thế nào, nhưng local kernel forwarding dùng state đã được cài xuống routing/FIB. Vì vậy BGP session healthy không chứng minh host forwarding đúng; ngược lại packet path local có thể hỏng dù control plane vẫn ổn.

Xem [BGP, routing policy và convergence](./07_bgp_routing_policy_convergence_and_route_security.md) để phân biệt advertisement/RIB/FIB với observed packet path.

## 5. qdisc là queueing policy trước device

**Queueing discipline (qdisc)** quyết định cách packet được xếp hàng, phân loại, pacing hoặc drop trước khi đi xuống device. Nó có thể rất đơn giản hoặc thực hiện scheduling/fairness/shaping phức tạp.

Mental model không nên là “qdisc = một queue”. Qdisc là **policy trên backlog**. Nó trả lời packet nào được gửi tiếp, packet nào chờ, khi nào drop và flow nào được ưu tiên.

Nếu offered load vượt service rate, backlog phải tăng hoặc packet phải bị drop. Không có queueing algorithm nào xóa định luật đó. Algorithm chỉ thay phân phối delay/drop giữa flows.

## 6. Bufferbloat là latency ẩn trong queue

Một buffer quá lớn có thể làm throughput trông tốt nhưng latency tăng mạnh. Khi bottleneck link phục vụ chậm hơn arrival rate, queue dài giữ packet thay vì drop sớm. Interactive traffic phải chờ sau bulk traffic.

Đây là **bufferbloat**: hệ thống dùng buffering để che overload, đổi packet loss thành queueing delay.

Evidence quan trọng không chỉ là interface utilization mà là queue depth/sojourn time, RTT inflation và drop/mark behavior. Nếu RTT tăng cùng backlog trong khi link gần saturation, bottleneck có thể nằm ở queue trước link chứ không ở application.

## 7. Driver ring và NIC hardware queue

Sau qdisc, driver thường đưa descriptors vào transmit ring. NIC đọc descriptors, DMA data và gửi frame. Ở chiều nhận, NIC DMA packet vào receive buffers rồi kernel xử lý descriptors.

Ring là một queue khác. Nếu software producer nhanh hơn NIC, TX ring có thể đầy. Nếu NIC nhận nhanh hơn kernel drain, RX ring có thể overflow và packet bị drop trước khi protocol stack thấy nó.

Multi-queue NIC phân traffic qua nhiều hardware queues để scale trên nhiều CPU. RSS/hash policy và CPU affinity ảnh hưởng locality. Một queue có thể nóng trong khi aggregate interface utilization chưa cao nếu flow distribution skew.

## 8. Interrupt, NAPI và polling trade-off

Nếu mỗi packet tạo một interrupt riêng ở packet rate cao, CPU có thể bị interrupt storm. Kernel network stack thường dùng cơ chế kết hợp interrupt với polling/budget để xử lý batch packet.

Batching tăng throughput vì amortize overhead nhưng có thể tăng latency cho packet chờ trong batch. Budget quá nhỏ làm backlog không drain kịp; budget quá lớn có thể để network processing chiếm CPU lâu và làm application thread chậm được schedule.

Đây là cross-layer feedback:

```text
packet rate tăng
→ softirq/poll work tăng
→ CPU time cho application giảm
→ application drain socket chậm
→ receive backlog tăng
→ latency/drop tăng
```

Network bottleneck vì vậy có thể biểu hiện như CPU scheduling problem.

## 9. Offload làm packet capture dễ bị hiểu sai

NIC/kernel có nhiều optimization gom hoặc tách packet để giảm per-packet overhead. Ví dụ, transmit side có thể để kernel xử lý một buffer lớn rồi NIC chia thành nhiều frames; receive side có thể coalesce nhiều segments trước khi đưa lên stack.

Do đó packet capture ở host có thể thấy “packet” lớn hơn MTU hoặc segmentation khác wire. Đây không nhất thiết là lỗi protocol; có thể là vị trí capture nằm trước/after offload boundary.

Mental model quan trọng:

```text
logical transport data
→ software segmentation/coalescing view
→ NIC offload transformation
→ wire frames
```

Khi debug MTU, retransmission hoặc packet count, phải biết evidence được quan sát ở layer nào.

## 10. Checksum offload và false alarm

Tương tự, packet capture trên sender có thể thấy checksum chưa hoàn chỉnh vì NIC sẽ tính checksum sau khi capture point đã ghi packet. Nếu không hiểu offload boundary, engineer có thể kết luận sai rằng host đang phát packet corrupt.

Rule chung: **evidence trước hardware transformation không thể được diễn giải như wire evidence nếu transformation chưa xảy ra**.

## 11. GRO/GSO và throughput–latency trade-off

Generic segmentation/coalescing giúp giảm số lần stack xử lý packet. Khi packet rate cao, giảm per-packet overhead có thể tiết kiệm CPU đáng kể.

Nhưng batching/coalescing thay timing. Work được gom lại rồi xử lý theo cụm. Với workload cực nhạy latency, throughput optimization có thể làm tail behavior khác. Không nên tắt offload theo thói quen; cần hypothesis và measurement theo workload.

## 12. Drops có nhiều owner khác nhau

“Packet drop” không đủ để chẩn đoán. Drop có thể xảy ra vì RX ring overflow, qdisc policy, firewall, route/policy, socket receive queue, transport validation hoặc device/link.

Một counter tổng không cho biết owner. Debugging phải đi theo state transition:

```text
packet có tới NIC không?
→ có vào RX ring không?
→ kernel có poll/process không?
→ routing/policy có accept không?
→ transport có accept không?
→ socket queue có chỗ không?
→ application có drain không?
```

Mỗi câu hỏi cần evidence ở đúng boundary.

## 13. ECMP/RSS skew và hot flow

Hash-based distribution giả định nhiều flows đủ đa dạng. Nếu workload chỉ có vài elephant flows, một hardware queue hoặc một path có thể nóng. Aggregate bandwidth 40% không loại trừ queue riêng lẻ 100%.

Điều này tương tự shard skew trong database hoặc partition skew trong stream processing. Average che distribution. Cần nhìn per-queue/per-flow/per-CPU cohort.

## 14. Connection pooling thay đổi packet path pressure

Application dùng connection pool giữ TCP connections lâu hơn, giảm handshake nhưng làm traffic tập trung trên ít flow. Tùy RSS/ECMP hash, điều này có thể giảm distribution entropy và tạo hot queue/path.

Ngược lại mở quá nhiều connection tăng handshake/state, port/NAT pressure và scheduler overhead. Vì vậy pool sizing không chỉ là application concern; nó có thể đổi network queue distribution.

Cross-link với [load balancing, connection pools và locality](../../08_software_systems/advanced/03_load_balancing_connection_pools_and_locality.md).

## 15. eBPF/tracing nằm ở evidence boundary

Khi cần nối syscall, scheduler và packet state, dynamic kernel tracing có thể cung cấp evidence ở các hook cụ thể. Nhưng tracing cũng có overhead và sampling bias.

Xem [eBPF, tracing, kernel observability và safety boundary](../../03_operating_systems/advanced/08_ebpf_tracing_kernel_observability_and_safety.md). Điểm quan trọng không phải dùng tool nào mà là attach evidence vào đúng state transition: enqueue, retransmit, qdisc delay, driver completion, receive/drop hay socket wakeup.

## 16. Worked reasoning: latency tăng nhưng không có packet loss rõ ràng

Giả sử service A gọi service B, p99 tăng từ 20 ms lên 400 ms khi backup traffic chạy. CPU application chỉ 50%, retransmission không tăng đáng kể.

Ta không nên dừng ở “network congestion”. Hãy kiểm tra:

```text
RTT tăng?
qdisc backlog/sojourn tăng?
interface/link utilization tăng?
per-queue utilization có skew?
socket send wait tăng?
softirq CPU tăng?
application runnable delay tăng?
```

Nếu RTT và qdisc backlog cùng tăng, bufferbloat/shaping là hypothesis mạnh. Nếu qdisc ổn nhưng một TX queue đầy, hardware queue skew hoặc driver path đáng nghi. Nếu softirq CPU tăng mạnh và application runnable nhưng không được schedule, bottleneck đã đi từ network packet rate sang CPU scheduling.

## 17. Lower layers quyết định behavior

Packet path dựa trên DMA, cache locality, interrupt delivery, NUMA placement và device queue. Driver descriptors nằm trong memory; NIC DMA qua IOMMU/device mapping; CPU xử lý protocol state và copy/reference buffer. Vì vậy network performance không tách khỏi architecture và OS.

Cross-layer path hữu ích:

```text
flow distribution
→ NIC queue
→ CPU affinity / NUMA
→ softirq work
→ socket wakeup
→ application scheduler latency
→ request tail latency
```

Đây là lý do production diagnosis cần nối Network với [scheduler internals](../../03_operating_systems/advanced/01_scheduler_run_queues_fairness_and_latency.md), [I/O/DMA](../../03_operating_systems/advanced/05_epoll_io_uring_zero_copy_and_dma.md) và [NUMA/interconnect](../../02_computer_architecture/advanced/04_numa_interconnects_and_scalable_coherence.md).

## 18. Mental model cuối

Kernel network path là chuỗi queue + state machines. Throughput, latency và drop là hệ quả của nơi arrival rate vượt service rate, nơi policy chủ động trì hoãn/drop, và nơi backpressure được truyền về application.

Khi debug, không hỏi chung “network có chậm không?”. Hãy hỏi: **packet đã tới boundary nào, đang chờ trong queue nào, ai sở hữu queue đó, queue được drain bởi CPU/device nào, offload nào biến đổi evidence, và pressure có được phản hồi về producer hay đang bị buffer che đi?**