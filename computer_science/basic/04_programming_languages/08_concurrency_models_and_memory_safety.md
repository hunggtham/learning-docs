# Concurrency models và memory safety

Concurrency không chỉ là “dùng nhiều threads”. Programming languages/runtimes cung cấp những models khác nhau để biểu diễn work xảy ra đồng thời và để kiểm soát shared state: threads + locks, actors, CSP/channels, async tasks, immutable data, ownership hoặc transactional memory.

## Shared-memory threading

Nhiều languages map threads gần với OS threads. Threads chia sẻ heap và có private stacks. Model này linh hoạt nhưng race conditions xuất hiện khi nhiều threads access mutable state mà synchronization không đúng.

Mutex bảo vệ critical section; condition variable chờ predicate; atomics cung cấp operations với memory-order semantics.

Điểm khó là correctness phụ thuộc **happens-before relation**, không chỉ source-code order.

## Memory model

Compiler và CPU có thể reorder operations nếu single-thread semantics không đổi. Trong concurrent program, language memory model xác định observations nào hợp lệ và synchronization nào tạo ordering guarantees.

`volatile` có nghĩa khác nhau theo language. Trong Java, volatile read/write có visibility/order semantics; trong C/C++, `volatile` chủ yếu liên quan observable accesses và không thay thế atomics cho data races.

Đây là lý do keyword giống nhau không nên được suy luận qua languages.

## Actors: isolate mutable state

Actor model (액터 모델) tổ chức system thành actors có private state và giao tiếp bằng messages. Mỗi actor xử lý messages tuần tự theo mailbox model, giảm shared-memory races.

Nhưng distributed actors vẫn có message ordering, failure, duplication và mailbox overload. Actor model di chuyển complexity, không xóa complexity.

## CSP và channels

Communicating Sequential Processes (CSP) nhấn mạnh processes giao tiếp qua channels. Go goroutines/channels lấy cảm hứng từ family ideas này.

Unbuffered channel có thể đồng bộ sender/receiver; buffered channel thêm queue. Channel capacity vì vậy trở thành backpressure control chứ không chỉ syntax communication.

## Async/await và structured concurrency

Async task thường phù hợp I/O concurrency. `await` biểu diễn suspension point thay vì block OS thread, tùy runtime.

Structured concurrency cố gắn lifetime child tasks vào lexical/task scope: parent không silently kết thúc trong khi children bị bỏ quên. Điều này làm cancellation, error propagation và resource lifetime dễ reasoning hơn.

## Ownership và borrowing

Ownership model như Rust giới hạn aliasing/mutation bằng compile-time rules. Một value có owner; borrowing tạo references với constraints. Mục tiêu là ngăn use-after-free, double free và nhiều data races trước runtime mà không cần garbage collector cho mọi allocation.

Điều quan trọng không phải học syntax Rust ở đây mà thấy ownership là một **static protocol cho resource lifetime và aliasing**.

## Memory safety và type safety

Memory safety nghĩa program không access memory ngoài valid lifetime/bounds theo model. Type safety là concept rộng hơn về invalid operations theo type system. Một language có thể type-safe ở mức high-level nhưng FFI/native extension mở unsafe boundary.

Bounds checks, GC, ownership, safe references và sandboxing là các mechanisms khác nhau hướng tới memory safety.

## Cancellation là control-flow cross-cutting

Concurrent task có thể bị cancel trong khi giữ lock, transaction hoặc file. Cancellation-safe code phải định nghĩa cleanup và state consistency.

Async cancellation vì vậy liên quan exception safety và resource management. RAII, `finally`, defer-style constructs và structured concurrency đều cố làm lifetime explicit.

## Common Misconceptions

**“Không dùng threads thì không có race.”** Actor/message systems vẫn có logical races do message ordering; distributed systems còn có stale state.

**“Async nhanh hơn sync.”** Async cải thiện utilization dưới waiting workloads; CPU-bound work vẫn cần compute resources.

**“GC làm program memory-safe hoàn toàn.”** GC ngăn nhiều lifetime errors nhưng không ngăn out-of-bounds trong unsafe/native code hoặc logical resource leaks.

## Mental Model

> Concurrency model là bộ quy tắc trả lời ba câu: ai sở hữu state, những execution units giao tiếp thế nào, và ordering/lifetime nào được guarantee.

## Kết nối

Đọc cùng [OS concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [IPC](../03_operating_systems/06_ipc_signals_pipes_and_shared_memory.md), [type systems](./06_type_systems_generics_and_polymorphism.md) và [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).