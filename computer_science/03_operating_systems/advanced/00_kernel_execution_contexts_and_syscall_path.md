# Kernel execution contexts, synchronization và syscall path

Một system call nhìn từ application như function call đặc biệt, nhưng phía dưới nó là boundary giữa user privilege và kernel privilege. Khi đi sâu hơn, cần hiểu thêm một constraint quan trọng: kernel không chỉ phục vụ một thread tại một thời điểm. Process context, interrupt, deferred work và nhiều CPU cores có thể cùng truy cập kernel state. Vì vậy kernel correctness phụ thuộc vào **execution context + synchronization discipline + object lifetime** chứ không chỉ syscall logic.

Mental model của chapter này là:

```text
user request / hardware event
→ privilege hoặc execution-context transition
→ kernel shared state
→ synchronization / lifetime protocol
→ possible sleep/preemption/deferred work
→ completion/wakeup
→ observable application behavior
```

## 1. User mode và kernel mode không phải hai process khác nhau

Khi thread gọi syscall, cùng logical thread chuyển privilege và stack/context theo cơ chế architecture/OS. Kernel xử lý request thay mặt thread đó. Nếu operation hoàn tất ngay, execution quay lại user mode; nếu phải chờ I/O hoặc lock, thread có thể sleep và scheduler chạy thread khác.

Vì vậy “kernel đang chạy” không có nghĩa luôn tồn tại một kernel thread riêng cho mỗi syscall.

Invariant quan trọng là privilege transition không được làm mất architectural state cần để trở lại userspace, và kernel không được tin dữ liệu userspace chỉ vì syscall entry đã hợp lệ.

## 2. Syscall entry là trust boundary

Userspace wrapper chuẩn bị syscall number và arguments theo ABI rồi dùng instruction như `syscall` hoặc `svc` tùy architecture. CPU chuyển privilege, save state cần thiết và nhảy vào entry point do kernel cấu hình.

Arguments như pointer, length, file descriptor và flags là untrusted input. Kernel phải kiểm tra permission, overflow, lifetime và copy semantics. Một pointer hợp lệ tại lúc check có thể trở nên không còn hợp lệ hoặc data có thể thay đổi nếu protocol cho phép concurrent mutation.

Đây là nguồn của các lỗi kiểu TOCTOU: **check một assumption rồi sử dụng resource sau khi assumption không còn chắc đúng**.

## 3. Một syscall thường đi qua nhiều subsystem

Ví dụ `read(fd, buf, n)` có thể đi qua:

```text
userspace wrapper
→ syscall entry
→ file-descriptor lookup
→ VFS / file operation
→ page cache hoặc socket/pipe subsystem
→ filesystem / network stack / block layer
→ driver / device nếu cần
→ completion
→ wakeup
→ copy/return to userspace
```

Cùng surface API `read` nhưng lower layer khác nhau hoàn toàn theo loại file descriptor. Vì vậy production latency không thể suy ra chỉ từ tên syscall.

## 4. Execution context quyết định operation nào được phép

Kernel code có thể chạy trong nhiều context. **Process context** gắn với current task và ở nhiều điểm có thể sleep. **Hard interrupt context** cần phản ứng nhanh và không được tùy tiện block. Deferred mechanisms như softirq, workqueue hoặc threaded interrupt chuyển work sang context phù hợp hơn.

Invariant là code chỉ được dùng operation tương thích với context hiện tại. Một path giữ spinlock hoặc chạy interrupt context mà gọi primitive có thể sleep có thể tạo deadlock hoặc kernel failure.

Do đó khi đọc kernel path, câu hỏi đầu tiên không chỉ là “function này làm gì?” mà là **“nó đang chạy trong context nào và có thể bị preempt/sleep ở đâu?”**

## 5. Blocking syscall nối trực tiếp với scheduler

Nếu resource chưa sẵn sàng, kernel đặt task vào wait structure, đổi task state và gọi scheduler. Event như I/O completion hoặc futex wake làm task trở lại runnable.

“Blocking” không có nghĩa CPU đứng chờ. Logical thread dừng progress, còn core có thể chạy task khác.

End-to-end latency vì vậy có thể chứa:

```text
syscall execution
+ wait trong kernel object
+ device/network latency
+ wakeup delay
+ run-queue delay
```

Application trace chỉ đo thời gian giữa call/return có thể không biết phần nào chiếm latency nếu thiếu kernel evidence.

## 6. Mutex và spinlock giải hai loại waiting khác nhau

Kernel mutex cho phép waiter sleep khi resource bận, phù hợp khi critical section có thể kéo dài và context cho phép schedule. **Spinlock** giữ CPU active trong vòng chờ ngắn, hữu ích khi sleep không được phép hoặc lock hold time cực ngắn.

Trade-off:

```text
sleeping lock
→ scheduler/context-switch cost
→ không đốt CPU khi wait dài

spinlock
→ tránh sleep/wakeup cho wait rất ngắn
→ đốt CPU và cache-coherence traffic nếu contention kéo dài
```

Spinlock không “nhanh hơn mutex” universal. Khi hold time hoặc contention tăng, spinning trở thành wasted CPU và có thể làm owner chạy chậm hơn vì coherence pressure.

## 7. Preemption và interrupt state là một phần của synchronization protocol

Một kernel critical section đôi khi cần ngăn local CPU bị preempt hoặc ngăn một loại interrupt tái-enter cùng state. Nhưng disable preemption/interrupt không bảo vệ khỏi core khác trên SMP machine.

Mental model:

```text
local execution control
≠
global mutual exclusion
```

Nếu shared state có thể được core khác truy cập, cần synchronization cross-CPU phù hợp. Đây là lỗi reasoning phổ biến khi chuyển intuition single-core sang multicore.

## 8. Atomic operation không thay object-lifetime protocol

Atomic increment/CAS có thể giữ một field transition indivisible, nhưng kernel objects thường có lifetime phức tạp: pointer có thể vẫn được reader giữ trong lúc writer muốn remove/free object.

Nếu writer chỉ atomically xóa pointer rồi free memory ngay, reader đã lấy pointer trước đó vẫn có thể use-after-free.

Vì vậy kernel synchronization phải giải cả:

```text
state mutation
+
object publication
+
reader lifetime
+
reclamation
```

RCU là một cơ chế tiêu biểu cho bài toán này.

## 9. RCU giải bài toán read-mostly như thế nào?

**Read-Copy-Update (RCU)** là family technique tối ưu cho structures có rất nhiều readers và ít writers. Mục tiêu là cho read-side critical section rất nhẹ trong khi writer vẫn có thể thay thế version của structure an toàn.

Mental model đơn giản:

```text
reader lấy reference tới version hiện tại

writer:
1. tạo/chuẩn bị version mới
2. publish pointer mới atomically theo ordering contract
3. version cũ chưa được free ngay
4. đợi grace period: mọi reader có thể còn dùng version cũ đã đi qua quiescent state
5. reclaim version cũ
```

Điểm cốt lõi không phải “RCU không dùng lock”. Invariant là:

> **Không reclaim object cũ cho tới khi chắc chắn không reader hợp lệ nào còn có thể dereference nó.**

## 10. Grace period là lifetime barrier, không phải wall-clock delay

Grace period không có nghĩa sleep một số milliseconds. Nó biểu diễn một điều kiện logical: các read-side critical sections có thể giữ reference cũ đã kết thúc theo RCU model.

Nếu CPU/task bị stall lâu trong read-side section, reclamation có thể bị trì hoãn. Điều này chuyển pressure từ reader latency sang memory/reclamation backlog.

Đây là trade-off quan trọng: reader path cực rẻ có thể đổi lấy writer/reclaimer complexity và deferred memory cost.

## 11. RCU không thay mọi lock

RCU phù hợp read-mostly access và lifetime/reclamation patterns. Nếu nhiều writers cần giữ invariant multi-field hoặc cập nhật structure theo sequence phức tạp, writer side vẫn có thể cần mutex/spinlock/other coordination.

RCU cũng không tự giải atomicity của business/kernel state. Nó chủ yếu cho phép readers truy cập version cũ an toàn trong lúc version mới được publish.

Mental model đúng là **versioned publication + delayed reclamation**, không phải “magic lock-free kernel”.

## 12. Memory ordering vẫn nằm bên dưới publication

Writer phải publish fully initialized object theo ordering semantics để reader không thấy pointer mới nhưng fields chưa hợp lệ. Reader-side access cũng phải tuân primitive/API của RCU implementation để compiler/CPU không phá protocol.

Đây là connection trực tiếp:

```text
RCU publication
→ language/compiler primitives của kernel code
→ ISA memory ordering
→ cache coherence
```

RCU correctness vì thế dựa trên memory model, không đứng ngoài nó.

## 13. Seqlock và optimistic read là một mental model khác

Một số read-mostly state nhỏ dùng **sequence lock (seqlock)**: writer tăng sequence counter quanh update; reader đọc version, copy state rồi kiểm tra counter có đổi/odd hay không. Nếu conflict, reader retry.

Invariant là reader chỉ chấp nhận snapshot nếu không có writer overlap.

Trade-off khác RCU: readers có thể retry/starve khi writer liên tục; nhưng không cần giữ old version object theo cùng cách. Đây là ví dụ quan trọng rằng “read-mostly” có nhiều protocol tùy invariant và update shape.

## 14. Lock contention có thể trở thành cache-coherence bottleneck

Một hot spinlock hoặc atomic field là một cache line phải đổi ownership giữa cores. Khi CPU count tăng, bottleneck có thể chuyển từ critical-section compute sang cache-line transfer.

Symptoms:

```text
CPU cao nhưng useful throughput không tăng
spin time tăng
cache-to-cache/coherence traffic tăng
owner bị preempt làm waiters spin lâu
```

Per-CPU data, sharding hoặc RCU thường nhằm giảm shared mutable hotspot, không chỉ giảm instruction count.

## 15. Interrupt/deferred-work batching thay đổi latency-throughput trade-off

Network stack thường không xử lý vô hạn work ngay trong interrupt. Cơ chế polling/batching như NAPI-style design giúp giảm interrupt storm và amortize per-packet overhead.

Nhưng batching lớn có thể tăng latency của individual packet/task hoặc làm một subsystem giữ CPU lâu hơn. Performance pressure vì thế thay đổi scheduling giữa interrupt, deferred work và process context.

Không có invariant “interrupt xử lý càng sớm càng tốt”; cần cân throughput, fairness và latency.

## 16. eBPF/tracing là evidence mechanism, không phải fix

Production kernel debugging thường cần quan sát boundaries mà application profiler không thấy: syscall duration, scheduling delay, block I/O, network retransmission, lock contention hoặc page fault.

Kernel tracepoints, sampling profiler, kprobe/fentry-style instrumentation và eBPF-based tooling có thể thu event theo PID/TID/CPU/cgroup/stack/context. Công cụ cụ thể thay đổi theo OS/kernel version; mental model bền hơn là:

```text
chọn hypothesis
→ chọn kernel event/state gần mechanism
→ giữ timestamp/context/identity
→ correlate với request/runtime evidence
```

Không nên trace mọi thứ production vô hạn; instrumentation có overhead và cardinality/storage cost.

## 17. Off-CPU analysis thường quan trọng hơn on-CPU profile

On-CPU profiler trả lời “CPU đang chạy code nào?”. Nhưng request chậm có thể dành phần lớn thời gian sleeping trên futex, I/O, timer hoặc run queue.

Off-CPU timeline cần biết:

```text
thread block lúc nào?
wait channel/resource nào?
ai hoặc event nào wake nó?
wake rồi chờ run queue bao lâu?
```

Đây là evidence mạnh để phân biệt lock wait, device wait, network wait và scheduler saturation.

## 18. Tracing cần monotonic time và causal correlation

Wall-clock có thể jump do synchronization/adjustment; latency measurement trong kernel/process nên dựa monotonic clock phù hợp. Khi correlate với distributed trace, cần hiểu clock uncertainty giữa machines.

Trace ID ở application không tự xuất hiện trong kernel. Correlation thường dựa PID/TID, socket tuple, cgroup, timestamps hoặc explicit context propagation tùy tooling.

Evidence pipeline phải biết uncertainty của chính nó.

## 19. Failure modes cần phân loại theo context

Một symptom “kernel CPU tăng” có thể là:

```text
spinlock contention
interrupt/softirq storm
packet processing burst
reclaim/writeback
syscall-heavy workload
scheduler/context-switch overhead
bug/livelock
```

Một symptom “syscall chậm” có thể do:

```text
wait lock
page fault
storage/network completion
run-queue delay sau wakeup
cgroup/IO throttling
```

Tên syscall không đủ để chọn fix.

## 20. Production evidence checklist

Khi cần đi xuống kernel layer, ưu tiên evidence theo hypothesis:

```text
syscall latency + stack
on-CPU flame/profile
blocked/off-CPU stacks
scheduler wakeup/run-queue latency
context switches / migrations
interrupt/softirq CPU time
lock/spin contention evidence
page faults / reclaim / writeback
block-I/O latency/queue
network retransmission/drop
cgroup throttling
```

Sau đó quay lại application invariant. Kernel evidence giải thích mechanism; fix có thể vẫn là giảm application concurrency, đổi data ownership, tune queue hoặc sửa I/O pattern.

## 21. Mô hình tư duy

> Kernel là một concurrent state machine chạy trong nhiều execution contexts. Syscall là privilege transition vào state machine đó; synchronization phải phù hợp khả năng sleep/preempt của context; RCU giữ read-mostly object lifetime bằng version publication + grace period + delayed reclamation; tracing cung cấp evidence về thời gian chạy và chờ. **Đừng hỏi chỉ “kernel function nào chậm?”—hãy hỏi context nào đang giữ resource, invariant nào đang được bảo vệ và wait/reclamation cost đang xuất hiện ở đâu.**

## Kết nối

Ôn [kernel/syscall foundation](../../basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md), [OS concurrency foundation](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [Scheduler internals](./01_scheduler_run_queues_fairness_and_latency.md), [Memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [I/O advanced](./05_epoll_io_uring_zero_copy_and_dma.md), [Architecture memory ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).