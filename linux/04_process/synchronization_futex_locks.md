# Đồng bộ hóa tiến trình/luồng, mutex, condition variable và `futex`

Đa luồng cho phép nhiều luồng thực thi cùng chia sẻ dữ liệu, nhưng chính khả năng chia sẻ này tạo ra race condition. Linux không giải quyết mọi vấn đề đồng bộ thay ứng dụng; phần lớn logic lock nằm trong thư viện user space, còn kernel cung cấp primitive cần thiết khi thread phải ngủ hoặc được đánh thức. Một primitive đặc biệt quan trọng là **futex (fast userspace mutex)**.

## Race condition xuất hiện như thế nào?

Giả sử hai thread cùng tăng biến `counter`:

```text
read counter
add 1
write counter
```

Nếu hai thread xen kẽ các bước, một lần tăng có thể bị mất.

Vấn đề không nằm ở “CPU chạy sai” mà ở việc operation logic không atomic đối với execution xen kẽ.

## Atomic operation

CPU cung cấp instruction atomic cho một số thao tác như compare-and-swap. Runtime và thư viện dùng chúng để xây lock hoặc cấu trúc lock-free.

Atomicity chỉ đảm bảo operation cụ thể không bị xen kẽ theo cách phá vỡ semantics. Nó không tự động giải quyết mọi invariant phức tạp giữa nhiều biến.

## Mutex

Mutex bảo đảm chỉ một thread giữ lock tại một thời điểm.

```text
lock
→ critical section
→ unlock
```

Nếu lock đang rảnh, thao tác có thể hoàn tất hoàn toàn trong user space bằng atomic instruction mà không cần system call.

Đây là điểm quan trọng: **lock không đồng nghĩa luôn vào kernel**.

## Khi contention xảy ra

Nếu thread B cố lấy mutex mà thread A đang giữ, B có hai lựa chọn tổng quát:

- quay vòng chờ (spin);
- ngủ và chờ được đánh thức.

Spin phù hợp nếu chờ cực ngắn vì tránh scheduling overhead, nhưng lãng phí CPU nếu lock giữ lâu.

Sleeping tiết kiệm CPU nhưng cần kernel hỗ trợ block/wakeup.

## Futex là gì?

Futex cho phép trạng thái lock thông thường nằm trong memory user space, chỉ gọi kernel khi cần phối hợp chờ/đánh thức.

Mô hình đơn giản:

```text
uncontended lock
→ atomic operation trong user space
→ không syscall

contended lock
→ futex(FUTEX_WAIT, ...)
→ thread sleep

unlock
→ futex(FUTEX_WAKE, ...)
→ đánh thức waiter nếu cần
```

Đây là lý do gọi là **fast userspace mutex**: fast path ở user space, kernel chủ yếu xử lý slow path.

## `strace` và futex

Ứng dụng Java hoặc native nhiều thread thường xuất hiện:

```text
futex(..., FUTEX_WAIT_PRIVATE, ...)
```

Điều đó không tự động nghĩa lỗi. Thread có thể đang chờ monitor, condition variable, thread pool queue hoặc runtime synchronization bình thường.

Nếu CPU thấp và nhiều thread ngủ trong futex, hệ thống có thể đơn giản đang chờ công việc.

Nếu latency cao và request threads đều chờ cùng lock, đó lại có thể là contention bottleneck.

## Condition variable

Condition variable cho phép thread ngủ cho tới khi một điều kiện logic có thể đã thay đổi.

Pattern:

```text
lock mutex
while condition false:
    wait(condition, mutex)
process state
unlock
```

Tại sao phải dùng `while` thay vì `if`? Vì wakeup không đảm bảo điều kiện vẫn đúng khi thread thực sự giành lại mutex; có thể có spurious wakeup hoặc thread khác đã thay đổi state.

## Semaphore

Semaphore quản lý một bộ đếm permit thay vì ownership một-một như mutex.

Ví dụ giới hạn tối đa 20 tác vụ cùng dùng resource.

Semaphore phù hợp với capacity control; mutex phù hợp với mutual exclusion. Dùng chúng như cùng một khái niệm sẽ làm reasoning sai.

## Read-write lock

Read-write lock cho phép nhiều reader cùng vào nhưng writer cần độc quyền.

Nó có thể hữu ích khi read nhiều và write ít, nhưng overhead và starvation/fairness có thể làm nó tệ hơn mutex trong workload thực tế.

Không chọn lock chỉ vì tên nghe “tối ưu hơn”.

## Spinlock

Spinlock làm thread quay vòng kiểm tra lock thay vì ngủ.

Trong kernel, spinlock cần thiết ở context không thể sleep hoặc critical section rất ngắn. Trong user space, spin có thể hữu ích trong workload đặc biệt nhưng dễ đốt CPU.

Nếu lock holder bị scheduler deschedule trong khi waiter spin, hiệu quả có thể rất tệ.

## Priority inversion

Thread ưu tiên cao chờ lock do thread ưu tiên thấp giữ, trong khi thread ưu tiên trung bình liên tục chiếm CPU. Đây là **priority inversion**.

Một số mutex/protocol hỗ trợ priority inheritance để giảm vấn đề này.

Chủ đề đặc biệt quan trọng với real-time systems.

## Deadlock

Deadlock kinh điển:

```text
Thread A giữ lock 1, chờ lock 2
Thread B giữ lock 2, chờ lock 1
```

Bốn điều kiện Coffman thường được dùng để reasoning: mutual exclusion, hold-and-wait, no preemption và circular wait.

Cách phòng tránh phổ biến là định nghĩa lock ordering nhất quán.

## Livelock và starvation

Deadlock nghĩa không ai tiến triển vì chờ nhau.

Livelock nghĩa các thread vẫn hoạt động nhưng liên tục nhường/retry nên không hoàn thành công việc.

Starvation nghĩa một thread hiếm khi hoặc không bao giờ nhận được resource do scheduling/fairness.

Ba failure mode này khác nhau và cần quan sát khác nhau.

## Memory ordering

Ngay cả khi không có lock truyền thống, CPU/compiler có thể reorder memory operation theo quy tắc memory model. Atomic operation và memory barrier đảm bảo ordering cần thiết.

Đây là lý do concurrent programming không thể chỉ reasoning theo thứ tự source code đơn giản.

Java Memory Model che giấu nhiều chi tiết phần cứng nhưng vẫn yêu cầu `volatile`, synchronization hoặc concurrent primitives để thiết lập happens-before relation.

## Lock contention và scheduler

Contention không chỉ là “nhiều thread muốn lock”. Nó tác động tới scheduler:

```text
thread chạy
→ cố lấy lock
→ sleep
→ context switch
→ holder chạy
→ wake waiter
→ waiter trở lại run queue
```

Nếu lock rất nóng, hệ thống có thể tốn thời gian vào wakeup/context switch hơn business work.

## Thundering herd

Nếu một event đánh thức rất nhiều waiter nhưng chỉ một hoặc ít thread có thể tiến triển, các thread còn lại thức dậy rồi lại ngủ, gây overhead.

Kernel và runtime có kỹ thuật giảm herd, nhưng pattern này vẫn xuất hiện trong server design và queueing.

## Java monitor và Linux

Java `synchronized`, `ReentrantLock`, `LockSupport.park()` và nhiều concurrent utilities cuối cùng dựa vào runtime + OS primitives khi thread cần block.

Không nên giả định một Java monitor tương ứng trực tiếp một futex đơn giản, vì JVM có nhiều optimization như biased/thin/heavyweight locking tùy phiên bản/runtime.

Nhưng ở tầng Linux, contention cuối cùng thường dẫn tới thread sleep/wakeup primitives.

## Thread dump và futex evidence

Thread dump Java cho semantic application-level tốt hơn `strace`:

```bash
jcmd <PID> Thread.print
```

Linux tools bổ sung tầng scheduling:

```bash
pidstat -t -p <PID> 1
ps -L -p <PID> -o pid,tid,stat,pcpu,wchan:30,comm
```

`wchan` có thể cho biết kernel wait channel, nhưng không thay thế runtime stack trace.

Kết hợp hai tầng:

```text
Java stack: đang chờ lock nào?
Linux: thread đang runnable hay sleeping?
perf: CPU nóng ở đâu?
strace: có futex wait/wake pattern gì?
```

## Lock convoy

Nếu nhiều thread xếp hàng sau một lock và mỗi lần chỉ một thread tiến triển, hệ thống có thể hình thành lock convoy. Khi lock holder bị chậm bởi I/O hoặc preemption, hàng đợi phía sau tăng mạnh.

Đây là ví dụ tail latency có thể tăng dù CPU trung bình chưa 100%.

## Blocking queue và thread pool

Thread pool thường dùng queue + condition/futex để worker ngủ khi không có việc.

Đây là trạng thái bình thường:

```text
queue empty
→ workers sleep
→ producer enqueue
→ wake worker
```

Nhưng nếu queue tăng liên tục, vấn đề nằm ở service rate/capacity chứ không phải futex bản thân.

## Lock-free không đồng nghĩa wait-free

Lock-free algorithm bảo đảm hệ thống tổng thể có tiến triển theo định nghĩa nhất định, nhưng một thread cụ thể vẫn có thể starvation.

Wait-free mạnh hơn: mỗi operation hoàn thành trong số bước hữu hạn theo mô hình.

Đây là thuật ngữ concurrency chính xác, không nên dùng “lock-free = không bao giờ chờ”.

## False sharing

Hai thread sửa hai biến logic khác nhau nhưng nằm trên cùng CPU cache line có thể gây cache coherence traffic lớn.

Đây không phải lock contention truyền thống nhưng có triệu chứng CPU/performance tương tự.

`perf` và hardware counters có thể hỗ trợ điều tra workload nâng cao.

## Mô hình tư duy

Một synchronization primitive có hai tầng:

```text
fast path:
atomic state trong user space

slow path khi contention:
wait queue / futex / scheduler
→ sleep
→ wakeup
→ runnable
→ scheduled again
```

Vì vậy muốn hiểu lock contention phải nhìn cả **logic đồng bộ của ứng dụng** và **trạng thái scheduling của Linux**.

## Những hiểu lầm phổ biến

**“Mutex luôn là syscall.”** Fast path thường có thể xử lý hoàn toàn trong user space.

**“Thấy futex trong strace nghĩa app deadlock.”** Futex wait là hoạt động bình thường của nhiều runtime.

**“CPU thấp nghĩa app không bị contention.”** Nhiều thread có thể đang ngủ chờ cùng lock.

**“Nhiều thread hơn luôn tăng throughput.”** Nếu shared lock hoặc downstream là bottleneck, thread thêm chỉ tăng queue/context switch.

**“Lock-free nghĩa mọi thread luôn tiến triển ngay.”** Lock-free và wait-free có định nghĩa chặt chẽ khác nhau.

## Kết nối kiến thức

Chương này nối [process/thread](./processes_threads_signals_jobs.md), [scheduler sâu](../06_resources/kernel_scheduler_deep_dive.md), [system call lifecycle](../00_foundations/system_call_lifecycle.md), [IPC](./interprocess_communication.md) và [Java incident playbook](../09_production/java_backend_incident_playbook.md).