# Concurrency, synchronization và deadlock

Concurrency bugs khó vì behavior phụ thuộc timing/interleaving mà source code tuyến tính không thể hiện rõ. Hai threads cùng đúng khi chạy riêng có thể sai khi share mutable state.

## Race condition và data race

Race condition là correctness phụ thuộc relative timing. Data race theo nhiều language memory models là concurrent conflicting accesses tới cùng location, ít nhất một write, không có synchronization phù hợp.

Ví dụ `counter++` không nhất thiết atomic. Nó có thể là load → add → store. Hai threads cùng load 10, cùng compute 11, cùng store 11; một increment bị mất.

## Critical section và mutual exclusion

Critical section truy cập shared invariant cần serialize. Mutex/lock (뮤텍스/락) bảo đảm một holder tại một thời điểm. Lock không “bảo vệ variable” tự động; correctness đến từ discipline rằng mọi accesses liên quan invariant dùng cùng synchronization protocol.

Coarse-grained lock đơn giản nhưng contention cao. Fine-grained locks tăng parallelism nhưng phức tạp và tăng deadlock risk.

## Atomic operations

CPU cung cấp atomic read-modify-write như compare-and-swap (CAS). Atomicity bảo đảm operation không quan sát intermediate state. Lock-free algorithms dùng atomics để coordinate mà không mutex blocking, nhưng reasoning memory ordering, ABA problem và reclamation rất khó.

Atomic không đồng nghĩa toàn transaction logic atomic. Hai atomic variables riêng không tự bảo đảm invariant liên-variable.

## Memory ordering và happens-before

Compiler và CPU được phép reorder operations trong giới hạn observable single-thread semantics. Multithread correctness không thể giả định source order luôn visible cùng thứ tự ở core khác.

Language memory model định nghĩa happens-before relationships qua locks, volatile/atomic operations, thread start/join... Nếu write happens-before read, read được guarantee visibility theo model.

Đây là tầng trên cache coherence: coherence không tự tạo program ordering semantics.

## Condition variables, semaphores và monitors

Condition variable cho thread ngủ tới khi predicate trên shared state có thể thay đổi; luôn re-check predicate trong loop vì wakeup/spurious wakeup/interleavings.

Semaphore giữ count permits, dùng giới hạn concurrency hoặc signaling. Binary semaphore giống mutex ở surface nhưng ownership semantics có thể khác.

Monitor kết hợp mutual exclusion với condition synchronization trong một abstraction; Java `synchronized`/wait-notify là family idea.

## Deadlock

Deadlock (교착 상태) xảy ra khi tasks chờ nhau theo cycle và không task nào tiến được. Coffman conditions kinh điển: mutual exclusion, hold-and-wait, no preemption, circular wait. Phá ít nhất một điều kiện có thể ngăn class deadlock.

Ví dụ thread A giữ lock X chờ Y; B giữ Y chờ X. Global lock ordering — luôn lấy X trước Y — phá circular wait.

Deadlock không chỉ locks. Distributed services có thể chờ RPC cycles; thread pools có task chờ future queued vào chính saturated pool.

## Livelock và starvation

Livelock: tasks vẫn hoạt động/thay state nhưng liên tục nhường/retry khiến không progress. Starvation: một task không được resource đủ lâu vì scheduling/lock unfairness.

Correct concurrent system cần safety (“không xảy ra điều xấu”) và liveness (“điều tốt cuối cùng xảy ra”).

## Immutability và message passing

Cách tốt để giảm shared-state synchronization là giảm mutable sharing. Immutable values có thể share an toàn hơn. Actor/message-passing model isolate state và communicate bằng messages, chuyển complexity từ shared memory sang ordering, mailbox và failure semantics.

Không có free lunch: distributed/message systems cần xử lý duplicate, retry và partial failure.

## Mental Model

> Concurrent correctness là reasoning về **shared state + atomic boundaries + ordering + progress**. Hỏi ai có thể access state này, operation nào phải indivisible, visibility được bảo đảm bằng gì, và có cycle chờ nào không.

## Common Misconceptions

**“volatile làm mọi operation thread-safe.”** Volatile/atomic visibility/order guarantee không biến multi-step invariant thành transaction.

**“Không dùng lock thì không deadlock.”** Resource waits, futures, channels và distributed calls vẫn có wait cycles.

**“Thread-safe collection làm toàn workflow thread-safe.”** Sequence check-then-act trên nhiều calls vẫn có race nếu không có higher-level atomicity.

## Kết nối

[Transactions](../05_data_databases/02_transactions_acid_and_concurrency_control.md) giải cùng bài toán atomicity/isolation ở database. [Distributed systems](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) làm ordering khó hơn vì không có shared clock/memory. Hardware side nằm ở [cache coherence](../02_computer_architecture/02_memory_hierarchy_and_cache.md).
