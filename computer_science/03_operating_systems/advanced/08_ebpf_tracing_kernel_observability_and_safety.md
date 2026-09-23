# eBPF, tracing, kernel observability và safety boundary

Khi application chậm, evidence ở user space thường chỉ cho thấy symptom: request latency tăng, thread bị block, syscall lâu hoặc packet biến mất. Muốn biết kernel thực sự làm gì, ta cần quan sát scheduler, syscall, network path, page fault, block I/O và nhiều state transition khác. Vấn đề là instrumentation trong kernel có thể làm crash máy hoặc thay đổi timing đủ lớn để phá chính hiện tượng đang đo.

**eBPF (extended Berkeley Packet Filter)** là một cơ chế cho phép chạy chương trình nhỏ trong các hook được kiểm soát, với verification và runtime constraints để biến kernel observability từ “patch kernel rồi reboot” thành một cơ chế động hơn.

Mental model:

```text
kernel event / hook
→ verified BPF program
→ bounded state access
→ map / ring buffer / counter
→ user-space collector
→ correlation với application evidence
```

Điểm cốt lõi không phải học tool command. Cần hiểu vì sao kernel cho phép code động chạy mà vẫn cố giữ safety invariant.

## 1. Vì sao tracing kernel khó

Kernel sở hữu address space đặc quyền, scheduler, memory manager, device và network stack. Một null pointer, unbounded loop hoặc race trong instrumentation có thể ảnh hưởng toàn máy.

Traditional logging cũng có vấn đề. Nếu thêm log vào hot path, formatting, allocation, lock và I/O có thể tạo overhead lớn. Khi event rate cao, log pipeline có thể trở thành bottleneck mới.

Observability vì vậy phải giữ hai invariant:

```text
instrumentation không được phá safety của kernel
instrumentation overhead phải đủ nhỏ để evidence còn đại diện workload thật
```

## 2. Hook là nơi semantics được neo

Một BPF program không chạy tùy ý mọi lúc. Nó được attach vào một hook: tracepoint, kprobe/kretprobe, perf event, socket/network hook hoặc các attachment point khác tùy subsystem.

Hook quyết định context nào đang chạy, dữ liệu nào hợp lệ, helper nào được phép và latency budget nào có thể chấp nhận. Instrumentation ở syscall entry trả lời câu hỏi khác instrumentation ở scheduler switch hoặc packet receive path.

Vì vậy “có trace” chưa đủ. Phải hỏi trace được lấy ở **state transition nào**.

## 3. Verifier là safety gate

Trước khi chương trình được load, verifier phân tích control flow và state để từ chối những chương trình không chứng minh được safety theo rule của runtime. Ý tưởng quan trọng là kernel không tin code chỉ vì người dùng có quyền load nó.

Verifier reasoning thường quan tâm tới pointer provenance, bounds, initialized state, helper contract và khả năng termination. Với loop, hệ thống cần một bound mà verifier có thể reasoning được; một vòng lặp không kiểm soát trong kernel hook có thể treo CPU.

Đây là một dạng **proof before execution**: không chứng minh mọi tính chất của chương trình, nhưng chứng minh đủ một tập invariant để giảm class failure nguy hiểm.

## 4. JIT và execution cost

Sau verification, implementation có thể interpret hoặc JIT compile BPF bytecode xuống native instruction. JIT giảm overhead trên hot path nhưng không làm instrumentation miễn phí.

Mỗi event vẫn có cost: execute instructions, access map, copy/aggregate data, có thể wake consumer. Nếu attach vào event xảy ra hàng triệu lần mỗi giây, một program nhỏ vẫn tạo overhead đáng kể.

Do đó sampling và in-kernel aggregation thường tốt hơn emit mọi event. Nếu câu hỏi chỉ cần histogram latency, việc cộng bucket tại kernel rồi đọc định kỳ thường rẻ hơn stream từng event ra user space.

## 5. Maps: state có kiểm soát giữa kernel và user space

BPF map là cơ chế lưu state có cấu trúc. Nó có thể dùng cho counter, histogram, lookup table, per-CPU state hoặc correlation giữa entry/exit event.

Per-CPU map giảm contention vì mỗi CPU cập nhật state riêng rồi aggregate sau. Đây là trade-off quen thuộc:

```text
ít synchronization ở write path
↔ cần merge state khi đọc
```

Map cũng tạo lifetime và memory-pressure concern. Cardinality không giới hạn theo PID, connection hoặc key tùy ý có thể biến observability thành memory leak logic. Instrumentation phải có eviction/bound hoặc aggregation phù hợp.

## 6. Ring buffer và event transport

Khi cần event chi tiết, kernel phải chuyển data sang user space. Ring-buffer-like mechanism tránh allocation cho từng event và cho phép producer/consumer giao tiếp hiệu quả hơn.

Nhưng buffer hữu hạn. Nếu producer nhanh hơn consumer:

```text
arrival rate > drain rate
→ backlog
→ buffer full
→ event drop hoặc backpressure tùy mechanism
```

Dropped telemetry là một phần của semantics. Nếu không đo drop count, ta có thể nhìn trace “sạch” chỉ vì hệ thống mất evidence đúng lúc overload.

## 7. kprobe, tracepoint và stability contract

Dynamic probe vào function nội bộ linh hoạt nhưng phụ thuộc implementation detail. Kernel version đổi symbol, signature hoặc inlining có thể làm probe không còn mang semantics cũ.

Stable tracepoint thường có contract rõ hơn nhưng ít vị trí hơn. Đây là trade-off giữa coverage và compatibility.

Khi xây production observability lâu dài, nên ưu tiên semantic attachment point ổn định nếu có; probe implementation detail phù hợp hơn cho investigation có kiểm soát.

## 8. CO-RE và type metadata

Một challenge thực tế là kernel data structure thay đổi theo version/configuration. Cơ chế kiểu BTF/CO-RE cho phép program dựa vào type metadata và relocation thay vì hard-code offset của field.

Mental model không phải “portable binary tuyệt đối”, mà là:

```text
program expresses field/type intent
→ target kernel exposes type metadata
→ loader relocates access
→ verifier kiểm tra target-specific result
```

Compatibility vẫn phải được test; metadata không xóa mọi semantic change.

## 9. Scheduler tracing

Một request “đang chạy chậm” có thể thực ra không chạy. Scheduler evidence giúp phân biệt:

```text
on-CPU execution time
run-queue waiting time
sleep/block time
preemption/migration
```

Nếu wall-clock latency cao nhưng on-CPU thấp và run-queue delay cao, bottleneck nằm ở scheduling/capacity hơn là code path. Nếu thread ngủ trên futex, cần quay lên synchronization owner. Nếu blocked ở I/O, cần nối tới device/filesystem evidence.

## 10. Network tracing

Packet path đi qua NIC, driver/NAPI-like receive processing, kernel networking, firewall/routing, socket queue rồi mới tới application. Một timeout ở application không nói packet mất ở đâu.

Kernel observability có thể kiểm tra drop reason, queue occupancy, retransmission-related state, socket backlog hoặc latency giữa network hook. Nhưng cần tránh biến mỗi packet thành một event user-space ở traffic cao.

Đây là nơi eBPF kết nối trực tiếp với [BGP/routing policy](../../06_networks_distributed_systems/advanced/07_bgp_routing_policy_convergence_and_route_security.md) và transport evidence: BGP giải thích route control plane; kernel tracing giải thích packet thực tế đi qua host như thế nào.

### Packet lifecycle và các queue boundary

Một mô hình host-level đơn giản cho chiều vào là:

```text
NIC DMA / RX ring
→ driver + NAPI poll / softirq
→ packet representation (thường là skb, tùy hook)
→ XDP/tc/ingress processing
→ routing + firewall/netfilter
→ transport state (TCP/UDP)
→ socket receive queue
→ task wakeup
→ application read()
```

Chiều ra có các boundary tương ứng:

```text
application write()
→ socket send buffer
→ TCP segmentation / UDP packetization
→ qdisc / egress policy
→ driver TX ring
→ NIC DMA / wire
```

Mỗi mũi tên có thể tạo queue, drop hoặc delay. `read()` thành công chỉ chứng minh application đã lấy bytes khỏi socket queue; nó không chứng minh packet vừa đến, cũng không cho biết bytes đã đi qua wire ở chiều ra. Tương tự, packet rời một hook ingress không chứng minh nó sẽ được deliver tới process.

Thứ tự chi tiết phụ thuộc driver, offload, namespace, kernel configuration và hook type. Vì vậy phải ghi rõ semantics của attachment point thay vì vẽ một pipeline duy nhất rồi coi đó là mọi máy.

### GRO, GSO và offload làm thay đổi đơn vị quan sát

NIC và kernel có thể gộp nhiều packet thành một representation lớn ở receive path (GRO), hoặc trì hoãn segmentation tới driver/NIC ở transmit path (GSO/TSO). Firewall, qdisc, TCP counters và user-space capture vì vậy có thể đếm các đơn vị khác nhau.

Một event “packet” trong trace không nhất thiết tương ứng một Ethernet frame trên wire. Nếu không biết layer đang đếm gì, ta dễ kết luận sai về packet rate, MTU, retransmission hoặc cost per packet. Khi cần đối chiếu, ghi rõ:

```text
wire frame count
→ kernel aggregate/segment count
→ transport segment/byte count
→ socket read/write bytes
→ application message count
```

Offload cũng có thể làm stack trace hoặc timestamp nằm ở điểm khác với intuition. Đây là lý do packet capture, NIC counters, kernel hook và application trace nên được dùng như các evidence source độc lập, không trộn chúng thành một metric “packets” duy nhất.

### Drop, delay và retransmission là ba hypothesis khác nhau

Khi request timeout, tối thiểu phải tách:

```text
drop: packet bị loại ở một boundary
delay: packet còn sống nhưng chờ queue/processing
retransmission: transport không nhận ACK/response đúng hạn và gửi lại
```

Một retransmission counter tăng không tự chứng minh host đã drop packet; loss có thể xảy ra trên link, remote host, middlebox hoặc do ACK bị mất. Ngược lại, socket backlog đầy có thể tạo local drop trước khi TCP có cơ hội phản ứng như operator mong đợi.

Evidence hữu ích nên ghép theo cùng flow/connection và time window:

```text
RX/TX ring và softirq work
→ ingress/egress drop reason
→ qdisc/socket backlog và queue age
→ TCP state, retransmission, RTT/RTO
→ wakeup/read/write delay
→ application span/message deadline
```

Nếu queue age tăng trước khi drop, capacity/servicing là hypothesis mạnh. Nếu kernel path pass nhưng retransmission chỉ xuất hiện ở một link/vantage point, cần quay lên network path/control plane. Nếu socket có bytes nhưng task không wake/read kịp, bottleneck có thể nằm ở scheduler hoặc application backpressure thay vì packet forwarding.

### Tracing packet path mà không biến tracing thành bottleneck

Packet-level tracing toàn bộ traffic thường không bền vững. Một workflow an toàn hơn là:

```text
flow/CPU/drop counters
→ sample connection hoặc namespace/CPU bị nghi
→ correlate queue boundary bằng flow identity
→ chỉ emit stack/event chi tiết cho một fraction nhỏ
→ kiểm tra event loss và instrumentation overhead
```

Khi dùng per-CPU maps, phải merge theo flow/CPU mà không tạo cardinality vô hạn. Khi dùng ring buffer, ghi drop counter và consumer lag cạnh event count. Khi trace container, cần giữ network namespace, cgroup, pod/task identity và interface index; thiếu một chiều identity có thể ghép nhầm hai flow giống tuple ở các namespace khác nhau.

## 11. Off-CPU profiling

CPU profiler truyền thống tập trung nơi chương trình đang execute. Nhiều production latency lại đến từ thời gian **không chạy**: lock wait, scheduler wait, I/O sleep, page fault hoặc throttling.

Off-CPU profiling ghi lại stack/context khi task bị deschedule và khi nó trở lại, từ đó gán waiting time về call path gây block. Nó giúp biến “service chậm nhưng CPU thấp” thành hypothesis cụ thể.

## 12. Observer effect

Instrumentation có thể thay đổi hệ thống đang đo. Event emission dày làm cache pressure tăng; stack walking tốn CPU; map contention tạo lock/cache-line bouncing; user-space consumer cạnh tranh CPU với workload.

Do đó evidence phải kèm overhead budget. Một trace chỉ xuất hiện khi bật tracing nặng có thể là artifact.

Một workflow tốt là:

```text
cheap always-on counters
→ detect anomaly
→ targeted sampling
→ narrow high-detail tracing
→ disable/reduce sau khi có evidence
```

## 13. Security boundary

BPF program có visibility rất mạnh vào kernel/application behavior. Quyền load/attach vì thế là security capability, không chỉ observability permission. Một deployment sai quyền có thể tạo data exposure hoặc mở attack surface.

Verifier giảm memory-safety risk nhưng không thay authorization. Program hợp lệ về memory vẫn có thể thu thập dữ liệu nhạy cảm nếu principal được cấp capability quá rộng.

## 14. Failure modes

**Telemetry loss:** ring buffer đầy hoặc collector chậm làm mất event đúng lúc overload.

**Cardinality explosion:** map key theo request/connection không bounded làm memory tăng.

**Version drift:** probe dựa implementation detail không còn đúng sau kernel update.

**Instrumentation-induced latency:** tracing quá dày làm workload chậm rồi kết luận sai nguyên nhân.

**Semantic misattachment:** hook nằm trước/ sau state transition khác với giả định, khiến timestamp/counter bị diễn giải sai.

**Privilege overreach:** observability agent có capability kernel lớn hơn nhu cầu thực.

## 15. Production evidence và workflow

Khi điều tra incident, bắt đầu từ invariant và câu hỏi cụ thể. Ví dụ:

```text
request latency tăng
→ CPU hay waiting?
→ nếu waiting: scheduler, lock hay I/O?
→ nếu I/O: filesystem/device hay network?
→ chọn hook gần state transition cần chứng minh
→ thu evidence tối thiểu
→ correlate bằng timestamp/identity
```

Không attach hàng chục probe chỉ vì có thể. Evidence càng nhiều càng tăng overhead và ambiguity.

Các signal quan trọng gồm event/drop count, map occupancy, per-CPU skew, run-queue delay, off-CPU duration, syscall latency, page-fault latency, network/socket queue và correlation với application trace.

## 16. Kết nối các layer

Chapter này nối [kernel execution context](./00_kernel_execution_contexts_and_syscall_path.md), [scheduler](./01_scheduler_run_queues_fairness_and_latency.md), [memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [async I/O/DMA](./05_epoll_io_uring_zero_copy_and_dma.md) và [debugging across abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

Reasoning path cuối cùng là:

```text
symptom ở application
→ hypothesis về kernel state transition
→ attachment point đúng semantics
→ verified low-overhead instrumentation
→ bounded evidence transport
→ correlation
→ lower-layer cause hoặc hypothesis bị bác bỏ
```

Giá trị của eBPF không nằm ở việc có thêm một tool, mà ở khả năng đưa **state-transition evidence** từ kernel vào cùng reasoning chain với runtime, database, network và service.
