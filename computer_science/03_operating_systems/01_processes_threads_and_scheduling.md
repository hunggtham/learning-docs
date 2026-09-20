# Process, thread và scheduling

Một máy có thể chạy browser, database, IDE và hàng trăm services dù số CPU cores hữu hạn. OS tạo illusion bằng cách multiplex execution. Để reasoning đúng, cần tách process — isolation/resource container — khỏi thread — execution stream có thể được scheduled.

## Process

Process (프로세스 / tiến trình) thường có virtual address space, open handles/file descriptors, security identity và một hoặc nhiều threads. Hai processes mặc định không đọc memory của nhau vì page mappings/protection khác.

Process creation semantics khác OS. Unix `fork()` conceptually tạo child từ parent, thường dùng copy-on-write pages; `exec()` thay process image bằng program mới. Windows tạo process qua APIs khác. High-level runtimes có thể hide details.

## Thread

Thread (스레드 / luồng) là execution context: program counter, registers, stack, scheduling state. Threads cùng process share heap/address space và resources.

Sharing làm communication rẻ nhưng tạo data races. Processes cách ly tốt hơn nhưng IPC thường có overhead/serialization. Đây là isolation-vs-sharing trade-off.

## Context switch

Scheduler chuyển CPU từ task A sang B bằng cách lưu/restoring execution context và cập nhật address-space state nếu cần. Cost không chỉ vài register stores; cache/TLB locality có thể bị ảnh hưởng.

Do đó “thêm thread để nhanh” có điểm giới hạn. Quá nhiều runnable threads tăng switching, cache contention và scheduling overhead.

## Scheduler đang tối ưu gì?

Scheduling (스케줄링) phải cân bằng throughput, latency, responsiveness, fairness và priorities. Batch workload muốn throughput; interactive UI muốn low response latency; real-time system cần deadline guarantees.

Textbook algorithms như FCFS, SJF, Round Robin, Priority Scheduling giúp hiểu dimensions, nhưng production schedulers như Linux CFS/EEVDF-family logic phức tạp hơn và thay đổi theo kernel versions.

## CPU-bound và I/O-bound

CPU-bound task dùng nhiều compute và luôn runnable. I/O-bound task chạy ngắn rồi sleep chờ disk/network. Scheduler có thể tận dụng khi một task blocked để chạy task khác.

Đây là lý do concurrency tăng throughput ngay cả trên ít cores cho I/O-heavy workloads: lúc task A chờ network, task B dùng CPU.

## User threads, kernel threads và runtimes

Có models 1:1, many-to-one, many-to-many giữa language tasks và OS threads. Java traditional threads thường map 1:1; Java virtual threads multiplex nhiều lightweight continuations trên carrier threads. Go goroutines có runtime scheduler M:N. Async JavaScript thường event-loop + tasks.

Do đó từ “thread” trong conversation phải xác định tầng: OS thread, language thread, virtual thread hay task/coroutine.

## Thread pools

Creating unbounded threads dễ exhaust memory/scheduler. Thread pool giới hạn workers và queue tasks. Nhưng fixed pool có thể deadlock/starve nếu tasks blocking và chờ tasks khác cùng pool. Pool size phải match workload: CPU-bound gần core count; I/O-bound có thể cần concurrency cao hơn, nhưng external resource limits vẫn chi phối.

## Priority inversion

High-priority thread có thể chờ lock do low-priority thread giữ, trong khi medium-priority tasks preempt low-priority holder. Priority inheritance là một mitigation. Điều này cho thấy scheduling và synchronization không độc lập.

## Little's Law intuition

Trong stable system:

\[
L = \lambda W
\]

với L average items in system, λ arrival rate, W average time. Nếu request latency tăng trong khi arrival rate giữ, concurrency/in-flight count tăng. Scheduling/queues vì vậy nối trực tiếp performance engineering.

## Mental Model

> **Process bảo vệ boundary; thread mang dòng execution; scheduler phân CPU time.** Concurrency cho phép overlap; parallelism cần nhiều execution resources thật.

## Common Misconceptions

**“Một process = một thread.”** Process có thể có nhiều threads.

**“Nhiều threads luôn tăng speed.”** CPU saturation, locks, cache và context switches có thể làm chậm.

**“Blocked thread vẫn ăn CPU như busy loop.”** Blocked task thường không runnable; scheduler cho CPU cho task khác.

## Kết nối

Hardware multicore ở [parallel architecture](../02_computer_architecture/05_parallel_computer_architecture.md). Sharing state dẫn tới [concurrency/synchronization](./02_concurrency_synchronization_and_deadlock.md). Runtime models được nối ở [execution models](../04_programming_languages/00_language_semantics_and_execution_models.md).
