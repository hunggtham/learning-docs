# Kernel thực thi (execution / 실행) contexts, synchronization và syscall đường dẫn (path / 경로)

> **Mạch đọc:** Đặt **Kernel thực thi (execution / 실행) contexts, synchronization và syscall đường dẫn (path / 경로)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. chế độ người dùng (user mode / 사용자 모드) và kernel chế độ (mode / 모드) không phải hai tiến trình (process / 프로세스) khác nhau** sang **2. Syscall entry là trust ranh giới (boundary / 경계)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một lời gọi hệ thống (system call / 시스템 호출) nhìn từ ứng dụng (application / 애플리케이션) như hàm (function / 함수) lời gọi (call / 호출) đặc biệt, nhưng phía dưới nó là ranh giới (boundary / 경계) giữa người dùng (user / 사용자) privilege và kernel privilege. Khi đi sâu hơn, cần hiểu thêm một ràng buộc (constraint / 제약조건) quan trọng: kernel không chỉ phục vụ một luồng thực thi (thread / 스레드) tại một thời điểm. tiến trình (process / 프로세스) ngữ cảnh (context / 맥락), interrupt, deferred công việc (work / 작업) và nhiều CPU cores có thể cùng truy cập kernel trạng thái (state / 상태). Vì vậy kernel tính đúng đắn (correctness / 정확성) phụ thuộc vào **thực thi (execution / 실행) ngữ cảnh (context / 맥락) + synchronization discipline + đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명)** chứ không chỉ syscall lô-gic (logic / 논리).

Mô hình tư duy (mental model / 사고 모델) của chapter này là:

```text
user request / hardware event
→ privilege hoặc execution-context transition
→ kernel shared state
→ synchronization / lifetime protocol
→ possible sleep/preemption/deferred work
→ completion/wakeup
→ observable application behavior
```

## 1. chế độ người dùng (user mode / 사용자 모드) và kernel chế độ (mode / 모드) không phải hai tiến trình (process / 프로세스) khác nhau

Khi luồng thực thi (thread / 스레드) gọi syscall, cùng logical luồng thực thi (thread / 스레드) chuyển privilege và ngăn xếp (stack / 스택)/ngữ cảnh (context / 맥락) theo cơ chế kiến trúc (architecture / 아키텍처)/OS. Kernel xử lý yêu cầu (request / 요청) thay mặt luồng thực thi (thread / 스레드) đó. Nếu thao tác (operation / 연산) hoàn tất ngay, thực thi (execution / 실행) quay lại chế độ người dùng (user mode / 사용자 모드); nếu phải chờ I/O hoặc khóa (lock / 잠금), luồng thực thi (thread / 스레드) có thể sleep và scheduler chạy luồng thực thi (thread / 스레드) khác.

Vì vậy “kernel đang chạy” không có nghĩa luôn tồn tại một kernel luồng thực thi (thread / 스레드) riêng cho mỗi syscall.

Bất biến (invariant / 불변식) quan trọng là privilege chuyển tiếp (transition / 전이) không được làm mất architectural trạng thái (state / 상태) cần để trở lại userspace, và kernel không được tin dữ liệu userspace chỉ vì syscall entry đã hợp lệ.

## 2. Syscall entry là trust ranh giới (boundary / 경계)

Userspace wrapper chuẩn bị syscall number và arguments theo ABI rồi dùng instruction như `syscall` hoặc `svc` tùy kiến trúc (architecture / 아키텍처). CPU chuyển privilege, save trạng thái (state / 상태) cần thiết và nhảy vào entry điểm (point / 지점) do kernel cấu hình.

Arguments như pointer, length, tệp (file / 파일) descriptor và flags là untrusted đầu vào (input / 입력). Kernel phải kiểm tra permission, overflow, thời gian tồn tại (lifetime / 수명) và bản sao (copy / 복사) ngữ nghĩa (semantics / 의미론). Một pointer hợp lệ tại lúc check có thể trở nên không còn hợp lệ hoặc dữ liệu (data / 데이터) có thể thay đổi nếu giao thức (protocol / 프로토콜) cho phép concurrent mutation.

Đây là nguồn của các lỗi kiểu TOCTOU: **check một giả định (assumption / 가정) rồi sử dụng tài nguyên (resource / 자원) sau khi giả định (assumption / 가정) không còn chắc đúng**.

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

Cùng surface API `read` nhưng lower tầng (layer / 계층) khác nhau hoàn toàn theo loại tệp (file / 파일) descriptor. Vì vậy môi trường vận hành (production / 운영 환경) độ trễ (latency / 지연 시간) không thể suy ra chỉ từ tên syscall.

## 4. thực thi (execution / 실행) ngữ cảnh (context / 맥락) quyết định thao tác (operation / 연산) nào được phép

Kernel mã (code / 코드) có thể chạy trong nhiều ngữ cảnh (context / 맥락). **tiến trình (process / 프로세스) ngữ cảnh (context / 맥락)** gắn với hiện tại (current / 현재) tác vụ (task / 작업) và ở nhiều điểm có thể sleep. **Hard interrupt ngữ cảnh (context / 맥락)** cần phản ứng nhanh và không được tùy tiện khối (block / 블록). Deferred mechanisms như softirq, workqueue hoặc threaded interrupt chuyển công việc (work / 작업) sang ngữ cảnh (context / 맥락) phù hợp hơn.

Bất biến (invariant / 불변식) là mã (code / 코드) chỉ được dùng thao tác (operation / 연산) tương thích với ngữ cảnh (context / 맥락) hiện tại. Một đường dẫn (path / 경로) giữ spinlock hoặc chạy interrupt ngữ cảnh (context / 맥락) mà gọi thành phần nguyên thủy (primitive / 기본 요소) có thể sleep có thể tạo deadlock hoặc kernel thất bại (failure / 실패).

Do đó khi đọc kernel đường dẫn (path / 경로), câu hỏi đầu tiên không chỉ là “hàm (function / 함수) này làm gì?” mà là **“nó đang chạy trong ngữ cảnh (context / 맥락) nào và có thể bị preempt/sleep ở đâu?”**

## 5. Blocking syscall nối trực tiếp với scheduler

Nếu tài nguyên (resource / 자원) chưa sẵn sàng, kernel đặt tác vụ (task / 작업) vào wait cấu trúc (structure / 구조), đổi tác vụ (task / 작업) trạng thái (state / 상태) và gọi scheduler. sự kiện (event / 이벤트) như I/O completion hoặc futex wake làm tác vụ (task / 작업) trở lại runnable.

“Blocking” không có nghĩa CPU đứng chờ. Logical luồng thực thi (thread / 스레드) dừng progress, còn cốt lõi (core / 핵심) có thể chạy tác vụ (task / 작업) khác.

End-to-end độ trễ (latency / 지연 시간) vì vậy có thể chứa:

```text
syscall execution
+ wait trong kernel object
+ device/network latency
+ wakeup delay
+ run-queue delay
```

Ứng dụng (application / 애플리케이션) dấu vết (trace / 추적) chỉ đo thời gian giữa lời gọi (call / 호출)/return có thể không biết phần nào chiếm độ trễ (latency / 지연 시간) nếu thiếu kernel bằng chứng (evidence / 증거).

## 6. Mutex và spinlock giải hai loại waiting khác nhau

Kernel mutex cho phép waiter sleep khi tài nguyên (resource / 자원) bận, phù hợp khi trọng yếu (critical / 중요) section có thể kéo dài và ngữ cảnh (context / 맥락) cho phép schedule. **Spinlock** giữ CPU active trong vòng chờ ngắn, hữu ích khi sleep không được phép hoặc khóa (lock / 잠금) hold thời gian (time / 시간) cực ngắn.

Sự đánh đổi (trade-off / 트레이드오프):

```text
sleeping lock
→ scheduler/context-switch cost
→ không đốt CPU khi wait dài

spinlock
→ tránh sleep/wakeup cho wait rất ngắn
→ đốt CPU và cache-coherence traffic nếu contention kéo dài
```

Spinlock không “nhanh hơn mutex” universal. Khi hold thời gian (time / 시간) hoặc contention tăng, spinning trở thành wasted CPU và có thể làm đơn vị sở hữu (owner / 오너) chạy chậm hơn vì coherence pressure.

## 7. Preemption và interrupt trạng thái (state / 상태) là một phần của synchronization giao thức (protocol / 프로토콜)

Một kernel trọng yếu (critical / 중요) section đôi khi cần ngăn cục bộ (local / 로컬) CPU bị preempt hoặc ngăn một loại interrupt tái-enter cùng trạng thái (state / 상태). Nhưng disable preemption/interrupt không bảo vệ khỏi cốt lõi (core / 핵심) khác trên SMP machine.

Mô hình tư duy (mental model / 사고 모델):

```text
local execution control
≠
global mutual exclusion
```

Nếu trạng thái dùng chung (shared state / 공유 상태) có thể được cốt lõi (core / 핵심) khác truy cập, cần synchronization cross-CPU phù hợp. Đây là lỗi lập luận (reasoning / 추론) phổ biến khi chuyển intuition single-core sang multicore.

## 8. Atomic thao tác (operation / 연산) không thay object-lifetime giao thức (protocol / 프로토콜)

Atomic increment/CAS có thể giữ một trường dữ liệu (field / 필드) chuyển tiếp (transition / 전이) indivisible, nhưng kernel objects thường có thời gian tồn tại (lifetime / 수명) phức tạp: pointer có thể vẫn được reader giữ trong lúc writer muốn remove/free đối tượng (object / 객체).

Nếu writer chỉ atomically xóa pointer rồi free bộ nhớ (memory / 메모리) ngay, reader đã lấy pointer trước đó vẫn có thể use-after-free.

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

**Read-Copy-Update (RCU)** là family technique tối ưu cho structures có rất nhiều readers và ít writers. Mục tiêu là cho read-side trọng yếu (critical / 중요) section rất nhẹ trong khi writer vẫn có thể thay thế phiên bản (version / 버전) của cấu trúc (structure / 구조) an toàn.

Mô hình tư duy (mental model / 사고 모델) đơn giản:

```text
reader lấy reference tới version hiện tại

writer:
1. tạo/chuẩn bị version mới
2. publish pointer mới atomically theo ordering contract
3. version cũ chưa được free ngay
4. đợi grace period: mọi reader có thể còn dùng version cũ đã đi qua quiescent state
5. reclaim version cũ
```

Điểm cốt lõi không phải “RCU không dùng khóa (lock / 잠금)”. bất biến (invariant / 불변식) là:

> **Không reclaim đối tượng (object / 객체) cũ cho tới khi chắc chắn không reader hợp lệ nào còn có thể dereference nó.**

## 10. Grace period là thời gian tồn tại (lifetime / 수명) barrier, không phải wall-clock delay

Grace period không có nghĩa sleep một số milliseconds. Nó biểu diễn một điều kiện logical: các read-side trọng yếu (critical / 중요) sections có thể giữ tham chiếu (reference / 참조) cũ đã kết thúc theo RCU mô hình (model / 모델).

Nếu CPU/tác vụ (task / 작업) bị stall lâu trong read-side section, reclamation có thể bị trì hoãn. Điều này chuyển pressure từ reader độ trễ (latency / 지연 시간) sang bộ nhớ (memory / 메모리)/reclamation backlog.

Đây là sự đánh đổi (trade-off / 트레이드오프) quan trọng: reader đường dẫn (path / 경로) cực rẻ có thể đổi lấy writer/reclaimer độ phức tạp (complexity / 복잡도) và deferred bộ nhớ (memory / 메모리) chi phí (cost / 비용).

## 11. RCU không thay mọi khóa (lock / 잠금)

RCU phù hợp read-mostly truy cập (access / 접근) và thời gian tồn tại (lifetime / 수명)/reclamation patterns. Nếu nhiều writers cần giữ bất biến (invariant / 불변식) multi-field hoặc cập nhật cấu trúc (structure / 구조) theo chuỗi (sequence / 시퀀스) phức tạp, writer side vẫn có thể cần mutex/spinlock/other coordination.

RCU cũng không tự giải atomicity của nghiệp vụ (business / 비즈니스)/kernel trạng thái (state / 상태). Nó chủ yếu cho phép readers truy cập phiên bản (version / 버전) cũ an toàn trong lúc phiên bản (version / 버전) mới được publish.

Mô hình tư duy (mental model / 사고 모델) đúng là **versioned publication + delayed reclamation**, không phải “magic lock-free kernel”.

## 12. bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) vẫn nằm bên dưới publication

Writer phải publish fully initialized đối tượng (object / 객체) theo thứ tự (ordering / 순서) ngữ nghĩa (semantics / 의미론) để reader không thấy pointer mới nhưng fields chưa hợp lệ. Reader-side truy cập (access / 접근) cũng phải tuân thành phần nguyên thủy (primitive / 기본 요소)/API của RCU hiện thực (implementation / 구현) để trình biên dịch (compiler / 컴파일러)/CPU không phá giao thức (protocol / 프로토콜).

Đây là liên kết (connection / 연결) trực tiếp:

```text
RCU publication
→ language/compiler primitives của kernel code
→ ISA memory ordering
→ cache coherence
```

RCU tính đúng đắn (correctness / 정확성) vì thế dựa trên bộ nhớ (memory / 메모리) mô hình (model / 모델), không đứng ngoài nó.

## 13. Seqlock và optimistic read là một mô hình tư duy (mental model / 사고 모델) khác

Một số read-mostly trạng thái (state / 상태) nhỏ dùng **chuỗi (sequence / 시퀀스) khóa (lock / 잠금) (seqlock)**: writer tăng chuỗi (sequence / 시퀀스) counter quanh cập nhật (update / 업데이트); reader đọc phiên bản (version / 버전), bản sao (copy / 복사) trạng thái (state / 상태) rồi kiểm tra counter có đổi/odd hay không. Nếu xung đột (conflict / 충돌), reader thử lại (retry / 재시도).

Bất biến (invariant / 불변식) là reader chỉ chấp nhận snapshot nếu không có writer overlap.

Sự đánh đổi (trade-off / 트레이드오프) khác RCU: readers có thể thử lại (retry / 재시도)/starve khi writer liên tục; nhưng không cần giữ old phiên bản (version / 버전) đối tượng (object / 객체) theo cùng cách. Đây là ví dụ quan trọng rằng “read-mostly” có nhiều giao thức (protocol / 프로토콜) tùy bất biến (invariant / 불변식) và cập nhật (update / 업데이트) shape.

## 14. tranh chấp khóa (lock contention / 잠금 경합) có thể trở thành cache-coherence bottleneck

Một hot spinlock hoặc atomic trường dữ liệu (field / 필드) là một bộ nhớ đệm (cache / 캐시) line phải đổi quyền sở hữu (ownership / 소유권) giữa cores. Khi CPU count tăng, bottleneck có thể chuyển từ critical-section compute sang cache-line transfer.

Symptoms:

```text
CPU cao nhưng useful throughput không tăng
spin time tăng
cache-to-cache/coherence traffic tăng
owner bị preempt làm waiters spin lâu
```

Per-CPU dữ liệu (data / 데이터), sharding hoặc RCU thường nhằm giảm dùng chung (shared / 공유) mutable hotspot, không chỉ giảm instruction count.

## 15. Interrupt/deferred-work batching thay đổi latency-throughput sự đánh đổi (trade-off / 트레이드오프)

Mạng (network / 네트워크) ngăn xếp (stack / 스택) thường không xử lý vô hạn công việc (work / 작업) ngay trong interrupt. Cơ chế polling/batching như NAPI-style thiết kế (design / 설계) giúp giảm interrupt storm và amortize per-packet overhead.

Nhưng batching lớn có thể tăng độ trễ (latency / 지연 시간) của individual packet/tác vụ (task / 작업) hoặc làm một subsystem giữ CPU lâu hơn. hiệu năng (performance / 성능) pressure vì thế thay đổi scheduling giữa interrupt, deferred công việc (work / 작업) và tiến trình (process / 프로세스) ngữ cảnh (context / 맥락).

Không có bất biến (invariant / 불변식) “interrupt xử lý càng sớm càng tốt”; cần cân thông lượng (throughput / 처리량), fairness và độ trễ (latency / 지연 시간).

## 16. eBPF/tracing là bằng chứng (evidence / 증거) cơ chế (mechanism / 메커니즘), không phải fix

Môi trường vận hành (production / 운영 환경) kernel debugging thường cần quan sát boundaries mà ứng dụng (application / 애플리케이션) profiler không thấy: syscall duration, scheduling delay, khối (block / 블록) I/O, mạng (network / 네트워크) retransmission, tranh chấp khóa (lock contention / 잠금 경합) hoặc page fault.

Kernel tracepoints, sampling profiler, kprobe/fentry-style instrumentation và eBPF-based tooling có thể thu sự kiện (event / 이벤트) theo PID/TID/CPU/cgroup/ngăn xếp (stack / 스택)/ngữ cảnh (context / 맥락). Công cụ cụ thể thay đổi theo OS/kernel phiên bản (version / 버전); mô hình tư duy (mental model / 사고 모델) bền hơn là:

```text
chọn hypothesis
→ chọn kernel event/state gần mechanism
→ giữ timestamp/context/identity
→ correlate với request/runtime evidence
```

Không nên dấu vết (trace / 추적) mọi thứ môi trường vận hành (production / 운영 환경) vô hạn; instrumentation có overhead và cardinality/lưu trữ (storage / 저장소) chi phí (cost / 비용).

## 17. Off-CPU phân tích (analysis / 분석) thường quan trọng hơn on-CPU profile

On-CPU profiler trả lời “CPU đang chạy mã (code / 코드) nào?”. Nhưng yêu cầu (request / 요청) chậm có thể dành phần lớn thời gian sleeping trên futex, I/O, timer hoặc run hàng đợi (queue / 큐).

Off-CPU timeline cần biết:

```text
thread block lúc nào?
wait channel/resource nào?
ai hoặc event nào wake nó?
wake rồi chờ run queue bao lâu?
```

Đây là bằng chứng (evidence / 증거) mạnh để phân biệt khóa (lock / 잠금) wait, thiết bị (device / 장치) wait, mạng (network / 네트워크) wait và scheduler saturation.

## 18. Tracing cần monotonic thời gian (time / 시간) và nhân quả (causal / 인과적) correlation

Wall-clock có thể jump do synchronization/adjustment; độ trễ (latency / 지연 시간) đo lường (measurement / 측정) trong kernel/tiến trình (process / 프로세스) nên dựa monotonic clock phù hợp. Khi correlate với phân tán (distributed / 분산) dấu vết (trace / 추적), cần hiểu clock bất định (uncertainty / 불확실성) giữa machines.

Dấu vết (trace / 추적) ID ở ứng dụng (application / 애플리케이션) không tự xuất hiện trong kernel. Correlation thường dựa PID/TID, socket tuple, cgroup, timestamps hoặc tường minh (explicit / 명시적) ngữ cảnh (context / 맥락) propagation tùy tooling.

Bằng chứng (evidence / 증거) chuỗi xử lý (pipeline / 파이프라인) phải biết bất định (uncertainty / 불확실성) của chính nó.

## 19. thất bại (failure / 실패) modes cần phân loại theo ngữ cảnh (context / 맥락)

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

## 20. bằng chứng vận hành (production evidence / 운영 증거) checklist

Khi cần đi xuống kernel tầng (layer / 계층), ưu tiên bằng chứng (evidence / 증거) theo hypothesis:

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

Sau đó quay lại ứng dụng (application / 애플리케이션) bất biến (invariant / 불변식). Kernel bằng chứng (evidence / 증거) giải thích cơ chế (mechanism / 메커니즘); fix có thể vẫn là giảm ứng dụng (application / 애플리케이션) tính đồng thời (concurrency / 동시성), đổi dữ liệu (data / 데이터) quyền sở hữu (ownership / 소유권), tune hàng đợi (queue / 큐) hoặc sửa I/O mẫu (pattern / 패턴).

## 21. Mô hình tư duy

> Kernel là một concurrent máy trạng thái (state machine / 상태 머신) chạy trong nhiều thực thi (execution / 실행) contexts. Syscall là privilege chuyển tiếp (transition / 전이) vào máy trạng thái (state machine / 상태 머신) đó; synchronization phải phù hợp khả năng sleep/preempt của ngữ cảnh (context / 맥락); RCU giữ read-mostly đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) bằng phiên bản (version / 버전) publication + grace period + delayed reclamation; tracing cung cấp bằng chứng (evidence / 증거) về thời gian chạy và chờ. **Đừng hỏi chỉ “kernel hàm (function / 함수) nào chậm?”—hãy hỏi ngữ cảnh (context / 맥락) nào đang giữ tài nguyên (resource / 자원), bất biến (invariant / 불변식) nào đang được bảo vệ và wait/reclamation chi phí (cost / 비용) đang xuất hiện ở đâu.**

## Kết nối

Ôn [kernel/syscall foundation](../../basic/03_operating_systems/00_kernel_syscalls_and_os_abstractions.md), [OS concurrency foundation](../../basic/03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [Scheduler internals](./01_scheduler_run_queues_fairness_and_latency.md), [Memory pressure](./02_page_faults_reclaim_dirty_pages_and_memory_pressure.md), [I/O advanced](./05_epoll_io_uring_zero_copy_and_dma.md), [Architecture memory ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md) và [Debugging xuyên abstraction layers](../../90_connections/advanced/00_debugging_across_abstraction_layers.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 scheduler run queues fairness and latency](./01_scheduler_run_queues_fairness_and_latency.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
