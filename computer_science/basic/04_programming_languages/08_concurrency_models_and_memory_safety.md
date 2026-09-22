# Concurrency models và memory safety

Concurrency không chỉ là “dùng nhiều threads”. Một concurrency model trả lời bốn câu hỏi nền tảng: **execution units nào tồn tại, state thuộc về ai, communication diễn ra qua shared memory hay messages, và ordering/lifetime nào được guarantee**. Threads + locks, actors, CSP/channels, async tasks, immutable data và ownership chỉ là những cách khác nhau để đặt boundary cho cùng bài toán: nhiều hoạt động tiến triển cùng lúc nhưng vẫn phải giữ invariant.

Advanced reasoning không bắt đầu bằng API như `Thread`, `async`, `Mutex` hay `Channel`. Nó bắt đầu bằng state machine và invariant cần được giữ khi operations có thể interleave.

## 1. Concurrency và parallelism không giống nhau

**Concurrency** nghĩa nhiều tasks có lifetime chồng lấp và tiến triển xen kẽ. **Parallelism** nghĩa nhiều operations thật sự chạy đồng thời trên nhiều execution resources.

Một event loop single-thread vẫn concurrent nếu nó multiplex nhiều I/O tasks. Một CPU 8 cores có thể chạy 8 threads song song, nhưng nếu tất cả chờ cùng lock thì parallelism hữu ích gần bằng zero.

Phân biệt này quan trọng vì async có thể tăng utilization mà không tạo thêm CPU compute capacity.

## 2. Invariant phải được viết trước synchronization primitive

Giả sử hai threads cùng cập nhật account balance. Câu hỏi đầu tiên không phải “dùng mutex hay atomic?”, mà là invariant:

```text
balance mới phải được tính từ một state hợp lệ duy nhất
không được mất update
không được quan sát transaction ở trạng thái nửa hoàn thành nếu contract cấm
```

Sau khi biết invariant, mới chọn primitive đủ mạnh. Một atomic integer có thể đủ cho counter; một multi-field invariant có thể cần lock hoặc protocol khác.

Dùng primitive mạnh mà không hiểu invariant dễ tạo over-synchronization; dùng primitive yếu dễ tạo race tinh vi.

## 3. Shared-memory threading: flexibility đổi lấy proof burden

OS/runtime threads thường chia sẻ heap và có stack riêng. Shared mutable state tạo giao tiếp rất rẻ nhưng correctness khó vì mọi interleaving hợp lệ phải được xét.

Mutex tạo **mutual exclusion** cho critical section. Condition variable cho thread chờ predicate thay vì busy-spin. Atomics cung cấp read-modify-write và memory-order semantics.

Lock không “bảo vệ variable” theo phép màu. Nó bảo vệ invariant nếu mọi access liên quan đều tuân cùng lock discipline.

## 4. Race condition và data race khác nhau

**Data race** thường có nghĩa hai execution contexts truy cập cùng memory location, ít nhất một bên write và không có synchronization hợp lệ theo language memory model.

**Race condition** rộng hơn: kết quả phụ thuộc timing/order theo cách làm vi phạm logic dù không có data race ở memory-level.

Ví dụ hai requests đều làm:

```text
if stock > 0:
    reserve()
```

Mỗi access có thể thread-safe riêng, nhưng check-then-act vẫn có logical race nếu invariant “không bán vượt stock” không được giữ atomically.

Vì vậy “race detector không báo” không chứng minh concurrent protocol đúng.

## 5. Happens-before là nền tảng reasoning cho shared memory

Compiler và CPU được phép reorder nhiều operations miễn không phá observable semantics theo contract. Vì vậy source order một mình không đủ.

Language memory model định nghĩa synchronization actions và relation như **happens-before**. Nếu writer publish state qua release/unlock/volatile action và reader acquire/read tương ứng, software có ordering/visibility guarantee để reasoning.

Không có synchronization edge, việc “test nhiều lần đều thấy đúng” không phải proof.

Đường xuyên tầng đầy đủ nằm ở [CPU cache → memory ordering → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

## 6. Atomicity, visibility và ordering phải tách riêng

Ba property hay bị trộn:

```text
Atomicity  -> operation có thể bị interleave thành state trung gian/lost update không?
Visibility -> write có được reader hợp lệ quan sát không?
Ordering   -> các operations liên quan được phép xuất hiện theo thứ tự nào?
```

Một `volatile` field trong Java có visibility/order semantics nhưng `count++` vẫn không phải atomic read-modify-write. Một CAS atomic có thể bảo vệ một transition nhưng protocol nhiều fields vẫn cần ordering đúng.

Review concurrent code nên kiểm tra cả ba, không chỉ “có dùng atomic không?”.

## 7. Lock correctness có nhiều failure mode hơn deadlock

Mutex giải mutual exclusion nhưng tạo thêm risks:

```text
contention -> throughput/tail latency xấu
lock convoy -> nhiều threads nối đuôi một slow holder
priority inversion -> task quan trọng chờ holder ít priority
starvation -> một participant hiếm khi lấy được lock
deadlock -> wait-for cycle không thể tiến triển
```

Lock scope quá lớn giữ correctness dễ hơn nhưng giảm parallelism. Lock scope quá nhỏ tăng interleavings cần chứng minh.

Performance pressure không cho phép bỏ invariant; nó buộc protocol tốt hơn hoặc partition state hợp lý hơn.

## 8. Lock-free không có nghĩa không chờ

Lock-free algorithms thường dùng compare-and-swap và đảm bảo system-wide progress theo định nghĩa. Một thread cụ thể vẫn có thể retry/starve. Wait-free guarantee mạnh hơn vì mỗi operation có bounded progress theo model.

Correctness còn cần linearization point, memory ordering, ABA handling và memory reclamation. CAS thành công không tự chứng minh object lifetime hoặc toàn protocol đúng.

Lock-free đổi blocking risk lấy proof complexity; nó không phải optimization mặc định.

## 9. Actor model: isolate mutable state, nhưng mailbox là queue

**Actor model (액터 모델)** gắn private mutable state với actor và communication bằng message. Nếu actor xử lý một message tại một thời điểm, nhiều shared-memory race biến mất structurally.

Nhưng complexity chuyển sang message semantics:

```text
message có thể reorder không?
mailbox có bounded không?
actor crash khi đang xử lý thì message được retry không?
duplicate có thể xuất hiện không?
state transition có idempotent không?
```

Mailbox unbounded có thể biến burst thành memory growth và latency vô hạn. Actor isolation không thay backpressure.

## 10. CSP/channels: communication primitive đồng thời là flow-control primitive

Communicating Sequential Processes nhấn mạnh các processes giao tiếp qua channels. Unbuffered channel thường tạo rendezvous: sender và receiver đồng bộ tại communication point. Buffered channel tạo queue.

Channel capacity vì vậy là architecture decision:

```text
capacity = 0/small -> backpressure mạnh, producer dễ bị chặn
capacity lớn       -> hấp thụ burst, nhưng tăng queued state và latency debt
```

“Không share memory; communicate” không loại bỏ overload. Queue chỉ chuyển vào channel/mailbox.

## 11. Async/await thay execution representation, không xóa resource constraint

Async task cho phép suspension khi chờ I/O thay vì giữ OS thread blocked, tùy runtime. Điều này rất hữu ích khi có nhiều I/O waits.

Nhưng async CPU-bound work vẫn cần CPU. Nếu callback/continuation block event loop bằng compute dài, hàng nghìn sockets có thể bị stall cùng lúc.

Runtime có worker pool, timer queue, I/O completion mechanism và task scheduler; tất cả đều có capacity. “Async” là programming model, không phải infinite concurrency.

## 12. Structured concurrency giữ lifetime invariant của tasks

Fire-and-forget task dễ leak lifetime: parent request đã kết thúc nhưng child vẫn giữ connection, lock hoặc continue side effect.

**Structured concurrency** cố giữ invariant:

> Child tasks thuộc một scope; scope không hoàn tất cho tới khi children hoàn tất/cancel theo policy; errors và cancellation được propagate có cấu trúc.

Điều này làm task lifetime giống resource lifetime hơn, giảm orphan work và giúp deadline/cancellation đi xuyên call tree.

Đọc [coroutines, async runtime và structured concurrency](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md).

## 13. Cancellation là một failure injection vào control flow

Task có thể bị cancel tại suspension point trong lúc đã acquire một resource hoặc thực hiện nửa side effect.

Cancellation-safe code cần biết:

```text
state nào đã được mutate?
cleanup có chạy chắc không?
operation có idempotent/restartable không?
transaction có rollback không?
lock/resource có release không?
```

RAII, `finally`, defer-style cleanup và structured lifetime giúp giữ invariant. Cancellation không nên được coi như `return` bình thường.

## 14. Ownership đưa một phần concurrency proof vào type system

Ownership/borrowing giới hạn aliasing và mutable access. Nếu mutable state không thể được unrestricted-share giữa threads, một class data race bị loại trước runtime.

Nhưng ownership không loại deadlock, logical race hoặc distributed inconsistency. Static proof chỉ mạnh trong boundary mà type system kiểm soát; FFI/unsafe code mở lại assumptions.

Đọc [Ownership, borrowing và memory safety](../../04_programming_languages/advanced/02_ownership_borrowing_linear_types_and_memory_safety.md).

## 15. Immutability giảm state-space cần reasoning

Immutable data có thể share an toàn hơn vì readers không tranh mutation. Functional-style updates tạo value mới thay vì modify shared object.

Trade-off có thể là allocation/copying, GC pressure hoặc need persistent data structures. Nhưng lợi ích lớn nhất không phải “functional code đẹp”; đó là giảm số interleavings có thể thay đổi invariant.

Concurrency design tốt thường **partition mutable state** trước khi cố synchronize mọi thứ.

## 16. Memory safety và concurrency safety giao nhau nhưng không đồng nhất

Memory safety ngăn use-after-free, invalid pointer/bounds access theo model. Concurrency safety quan tâm race/order/progress. Một GC language có thể memory-safe ở heap lifetime nhưng vẫn có data race/logical race. Một ownership language có thể ngăn nhiều alias/lifetime bugs nhưng vẫn deadlock.

FFI/native extension, unsafe block và shared-memory boundary là nơi guarantee có thể suy yếu.

Security cũng liên quan: memory-unsafe race/use-after-free có thể trở thành vulnerability, nhưng logical authorization race có thể xảy ra trong memory-safe language.

## 17. Performance pressure thay đổi model nào phù hợp

Threads có context-switch/stack cost nhưng rất tự nhiên cho blocking code. Async tasks scale số I/O waits tốt hơn nhưng runtime scheduling/debugging phức tạp. Actors isolate state nhưng mailbox/message serialization tạo overhead. Atomics tránh kernel blocking trong một số paths nhưng cache-line contention có thể giới hạn scalability.

Không có model nhanh nhất universal. Chọn theo workload và invariant:

```text
CPU-bound independent work -> parallel workers/data parallelism
I/O-heavy high concurrency -> async/evented model có thể hợp lý
state ownership rõ          -> actor/partitioning có thể giảm sharing
low-level shared counters   -> atomics nếu invariant thật sự local
complex multi-field state   -> lock/transaction thường dễ proof hơn
```

## 18. Production evidence cho concurrency bug và contention

Correctness evidence gồm race detector/sanitizer khi ecosystem hỗ trợ, stress testing, invariant assertion và minimal reproducer. Performance evidence gồm thread dump, lock/park wait, on/off-CPU profiler, scheduler delay, run queue, context switches, cache-line/coherence counters và NUMA placement khi cần.

Một deadlock cần wait-for graph/stack evidence. Một false-sharing issue cần cache/coherence evidence. Một event-loop stall cần long-task/on-CPU evidence. Cùng symptom “request treo” có thể có mechanism hoàn toàn khác.

## 19. Failure ở tầng thấp hơn có thể quyết định behavior

Concurrency abstraction leak khi lower layer trở thành decisive:

```text
language lock contention -> OS futex/scheduler behavior
atomic hot spot           -> cache-coherence ownership transfer
async latency             -> event loop + OS I/O completion + CPU scheduling
shared object performance -> NUMA/cache-line placement
safe publication          -> language memory model mapped xuống ISA ordering
```

Ta không cần debug mọi bug bằng assembly, nhưng phải biết khi nào abstraction hiện tại không giải thích được evidence.

## 20. Mô hình tư duy

> Concurrency model là protocol về **ownership, communication, ordering, lifetime và progress**. Threads/locks dùng shared state trực tiếp; actors/channels di chuyển communication sang message/queue; async tách logical tasks khỏi blocking OS threads; ownership đưa một phần proof vào type system. Không model nào xóa concurrency complexity—mỗi model chuyển invariant và failure mode sang boundary khác.

## Những hiểu nhầm thường gặp

**“Không dùng threads thì không có race.”** Actors/messages vẫn có logical race, duplicate, reorder và stale state.

**“Async nhanh hơn sync.”** Async chủ yếu cải thiện utilization khi có waits; CPU-bound work vẫn bị CPU capacity giới hạn.

**“Atomic nghĩa toàn operation business đã atomic.”** Atomic primitive chỉ bảo vệ transition mà primitive đó định nghĩa.

**“Lock-free luôn nhanh hơn lock.”** Contention, retries, coherence và reclamation có thể làm lock-free tệ hơn.

## Kết nối

Đọc cùng [OS concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [Advanced memory ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md), [Ownership](../../04_programming_languages/advanced/02_ownership_borrowing_linear_types_and_memory_safety.md), [Structured concurrency](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md), [Queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [Correctness path xuyên tầng](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).