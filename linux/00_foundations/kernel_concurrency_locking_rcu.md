# Đồng thời, khóa và RCU trong Linux kernel

Khi một máy chỉ có một CPU và kernel chỉ xử lý từng việc nối tiếp, bảo vệ trạng thái chung tương đối đơn giản. Nhưng Linux hiện đại chạy trên nhiều core, xử lý nhiều process, interrupt, softirq và kernel worker đồng thời. Cùng một cấu trúc dữ liệu có thể bị nhiều execution context truy cập gần như cùng lúc.

Vì vậy một trong những nền tảng quan trọng nhất của kernel là **đồng thời (concurrency)**: làm sao cho nhiều luồng thực thi cùng tiến triển mà không làm hỏng trạng thái chung, không deadlock và không tạo latency không cần thiết.

Chương này không nhằm dạy viết kernel module. Mục tiêu là hiểu vì sao Linux có spinlock, mutex, atomic operation, wait queue, seqlock và RCU; khi nào code được phép ngủ; và những primitive này liên hệ thế nào tới hiện tượng production như lock contention, softirq backlog hoặc thread chờ `futex()`.

## Concurrency khác parallelism

**Đồng thời (concurrency)** nghĩa nhiều công việc có vòng đời chồng lấn và hệ thống phải quản lý tương tác giữa chúng. **Song song (parallelism)** nghĩa nhiều công việc thực sự chạy cùng lúc trên nhiều CPU/core.

Một máy một core vẫn có concurrency do scheduler xen kẽ process và do interrupt có thể xảy ra. Máy nhiều core thêm parallelism, khiến race condition có thể xuất hiện thực sự cùng thời điểm.

## Race condition hình thành như thế nào?

Giả sử hai CPU cùng tăng một biến đếm:

```text
counter = counter + 1
```

Ở source code đây trông như một thao tác. Ở machine level nó có thể gồm:

```text
load counter
add 1
store counter
```

Nếu hai CPU đọc cùng giá trị trước khi một CPU ghi lại, một lần tăng có thể bị mất.

Đây là **race condition**: kết quả phụ thuộc thứ tự xen kẽ của các operation mà chương trình không kiểm soát đúng.

## “Chạy trong kernel” không có nghĩa là không bị tranh chấp

Một hiểu lầm phổ biến là kernel là một khối code duy nhất nên tự nhiên tuần tự. Thực tế kernel có thể xử lý đồng thời:

- system call từ nhiều process trên nhiều CPU;
- interrupt trên nhiều CPU;
- softirq;
- kernel thread;
- workqueue;
- timer callback;
- scheduler activity.

Một data structure toàn cục phải được thiết kế cho mô hình này.

## Critical section

**Vùng tới hạn (critical section)** là đoạn code thao tác trạng thái cần được bảo vệ khỏi truy cập đồng thời không an toàn.

Mục tiêu của synchronization không phải “khóa càng nhiều càng tốt”. Khóa quá rộng làm giảm parallelism và tăng contention.

Thiết kế tốt cố giảm phạm vi shared mutable state và giữ critical section đủ ngắn.

## Atomic operation

Một số thao tác nhỏ có thể dùng **atomic operation**, tức operation mà các CPU khác không quan sát thấy trạng thái trung gian theo guarantee tương ứng.

Ví dụ kernel có các primitive atomic counter thay vì bảo vệ mọi increment bằng mutex.

Atomic operation hữu ích cho thao tác nhỏ, nhưng không giải quyết transaction gồm nhiều bước logic.

Nếu cần bảo đảm quan hệ:

```text
kiểm tra trạng thái A
rồi cập nhật B
rồi cập nhật C
```

một atomic increment riêng lẻ thường không đủ.

## Spinlock: chờ bằng cách quay

**Spinlock** phù hợp khi critical section rất ngắn và context không thể ngủ.

Khi lock đang bị giữ, CPU chờ có thể “spin”, tức lặp kiểm tra cho tới khi lock được giải phóng.

Mental model:

```text
CPU 0: acquire -> critical section -> release
CPU 1:          spin spin spin -> acquire
```

Nếu giữ spinlock quá lâu, CPU khác đốt CPU time chỉ để chờ. Vì vậy spinlock phải đi kèm discipline rất chặt.

## Vì sao interrupt context cần primitive khác process context?

Code trong interrupt context không thể hành xử giống một process bình thường. Nó không có quyền ngủ tùy ý chờ một mutex rồi để scheduler xử lý như thread thông thường.

Vì vậy kernel phải phân biệt context:

- process context;
- interrupt context;
- softirq context;
- preemption state.

Một primitive hợp lệ ở process context có thể không hợp lệ trong interrupt context.

Đây là lý do câu hỏi “lock nào nhanh hơn?” quá đơn giản. Câu hỏi đúng trước tiên là **context này có được phép sleep không?**

## Mutex: chờ bằng cách ngủ

**Mutex** thường dùng khi holder có thể giữ lock lâu hơn và waiter được phép sleep.

Thay vì quay CPU vô ích, task không lấy được mutex có thể bị block, scheduler chạy task khác, rồi task được wake khi lock sẵn sàng.

Điều này giảm lãng phí CPU nhưng có chi phí scheduling/wakeup.

Spinlock và mutex vì vậy không chỉ khác implementation; chúng phù hợp với hai mô hình chờ khác nhau.

## Semaphore

Semaphore biểu diễn một số lượng permit thay vì chỉ trạng thái locked/unlocked. Nó có thể phù hợp khi có N resource tương đương.

Trong user-space, connection pool có mental model gần giống semaphore: chỉ một số lượng giới hạn request được giữ connection cùng lúc.

Kernel có nhiều primitive hiện đại chuyên biệt hơn cho từng use case; không nên coi semaphore là primitive mặc định cho mọi synchronization.

## Read-write lock

Nếu workload có nhiều reader và ít writer, reader-writer lock cho phép nhiều reader cùng truy cập khi không có writer.

Tuy nhiên loại lock này không tự động nhanh hơn mutex. Overhead, starvation và cache-line contention có thể khiến lợi ích phụ thuộc workload.

Một thiết kế read-heavy cực lớn có thể phù hợp hơn với RCU.

## Seqlock

**Sequence lock (seqlock)** tối ưu cho trường hợp reader rất nhanh và có thể retry.

Writer cập nhật sequence counter quanh quá trình ghi. Reader:

1. đọc sequence;
2. đọc dữ liệu;
3. kiểm tra sequence có thay đổi không;
4. nếu thay đổi thì đọc lại.

Reader có thể không cần block writer, nhưng phải chấp nhận retry và không phù hợp với mọi loại dữ liệu.

## RCU là gì?

**Read-Copy-Update (RCU)** là kỹ thuật synchronization quan trọng trong Linux cho workload đọc cực nhiều, ghi ít.

Ý tưởng khái niệm:

```text
reader đọc phiên bản hiện tại gần như không khóa
writer tạo/cập nhật phiên bản mới
writer publish pointer mới
phiên bản cũ chỉ được giải phóng sau khi chắc chắn reader cũ đã rời critical section
```

Thay vì bắt mọi reader tranh một lock, RCU tối ưu read path.

## Grace period trong RCU

Sau khi writer thay pointer, vẫn có thể có reader đang giữ reference tới object cũ.

Writer không thể `free()` object cũ ngay.

RCU chờ một **grace period**: khoảng thời gian đủ để các reader trước đó hoàn tất critical section liên quan. Sau đó object cũ mới được reclaim an toàn.

Điểm sâu ở đây là synchronization không chỉ là “ai được vào critical section”. Nó còn là **quản lý lifetime của object khi reader lockless vẫn có thể giữ reference**.

## Reference counting

Một kỹ thuật khác để quản lý lifetime là **đếm tham chiếu (reference counting)**.

Khi có thêm reference, count tăng; khi release reference, count giảm. Object chỉ được free khi count về 0.

Linux dùng nhiều dạng reference counting cho kernel object.

Nhưng reference counting không giải quyết mọi race. Nếu thread cố tăng count sau khi object đã về 0 và đang được free, vẫn cần quy tắc publication/lifetime đúng.

Do đó reference counting và locking thường phối hợp thay vì thay thế hoàn toàn nhau.

## Memory ordering: atomic chưa chắc đủ

CPU và compiler có thể sắp xếp lại operation trong giới hạn memory model để tối ưu hiệu năng.

Vì vậy concurrent code cần quan tâm không chỉ “operation có atomic không” mà còn “các CPU khác được phép quan sát thứ tự memory operation ra sao”.

Kernel sử dụng **memory barrier** và semantics acquire/release trong nhiều primitive.

Ví dụ writer muốn publish object:

```text
ghi toàn bộ fields của object
        ↓
publish pointer
```

Nếu CPU khác nhìn pointer trước khi nhìn đầy đủ field update, reader có thể thấy object chưa hoàn chỉnh. Primitive synchronization phải thiết lập ordering cần thiết.

Đây là lý do viết lock-free code chính xác khó hơn rất nhiều so với chỉ dùng atomic integer.

## Cache coherence và false sharing

Nhiều CPU core có cache riêng nhưng phải duy trì coherence cho memory chia sẻ.

Nếu nhiều core liên tục ghi vào cùng cache line, cache line có thể “ping-pong” giữa core và làm performance giảm mạnh.

Ngay cả khi hai biến logic khác nhau nhưng nằm cùng cache line, chúng vẫn có thể gây **false sharing**.

Vì vậy scalability của kernel không chỉ phụ thuộc số lock; layout dữ liệu và locality cũng quan trọng.

## Per-CPU data

Một chiến lược giảm contention là giữ dữ liệu **per-CPU** thay vì dùng một biến global.

Ví dụ mỗi CPU có counter riêng rồi tổng hợp khi cần. Update fast path không phải tranh cùng một cache line.

Đánh đổi là việc đọc tổng giá trị phức tạp hơn và có thể chỉ nhất quán tương đối tùy semantics.

Đây là pattern rất quan trọng trong kernel performance.

## Wait queue

Khi task phải chờ một condition, kernel không nên busy-spin vô hạn trong process context. Task có thể ngủ trên **wait queue**.

Mental model:

```text
condition chưa đúng
→ task đăng ký chờ
→ task sleep
→ producer/event thay đổi state
→ wake_up
→ task runnable
→ scheduler cho chạy lại
```

Socket read, pipe, device I/O và nhiều subsystem sử dụng những ý tưởng tương tự.

Wait queue nối synchronization với scheduler.

## Futex: phần lớn lock ở user-space, kernel chỉ can thiệp khi tranh chấp

Trong user-space, pthread mutex và nhiều runtime lock có thể dựa trên **futex (fast userspace mutex)**.

Fast path khi lock không bị tranh có thể hoàn tất bằng atomic operation trong user space mà không gọi kernel.

Khi có contention, thread dùng `futex()` system call để ngủ/wake thông qua kernel.

Mental model:

```text
uncontended lock
→ user-space atomic only

contended lock
→ futex syscall
→ waiter sleep
→ wake later
```

Đây là một ví dụ đẹp về thiết kế tránh privilege transition khi chưa cần.

Nếu `strace` cho thấy nhiều `futex()` chờ lâu, đó có thể là dấu hiệu contention ở runtime/application, không phải kernel “bị chậm”.

## Deadlock

Deadlock có thể xảy ra khi nhiều execution context giữ tài nguyên rồi chờ lẫn nhau.

Ví dụ:

```text
Task A giữ lock X, chờ lock Y
Task B giữ lock Y, chờ lock X
```

Không task nào tiến triển được.

Kernel code phải dùng quy tắc lock ordering rất chặt.

Ở tầng application, cùng nguyên lý xuất hiện với Java monitor, database row lock hoặc distributed lock.

## Lock ordering

Một cách tránh deadlock là định nghĩa thứ tự lấy lock cố định:

```text
luôn acquire A trước B
```

Nếu mọi đường code tuân thủ cùng thứ tự, vòng chờ A↔B bị loại bỏ.

Đây là ví dụ cho thấy correctness của synchronization là thuộc tính của **toàn bộ protocol**, không phải của từng lock riêng lẻ.

## Priority inversion

Task ưu tiên cao có thể bị block bởi task ưu tiên thấp đang giữ lock. Nếu task ưu tiên trung bình liên tục chiếm CPU, task thấp khó chạy để release lock, khiến task cao bị trì hoãn gián tiếp.

Đây là **priority inversion**.

Một số hệ thống dùng priority inheritance trong primitive phù hợp để giảm vấn đề này.

Khái niệm quan trọng với real-time workload và latency-sensitive system.

## Preemption và critical section

Nếu kernel task đang sửa cấu trúc per-CPU rồi bị migrate giữa CPU ở thời điểm không phù hợp, invariants có thể bị phá.

Vì vậy một số critical section cần kiểm soát preemption hoặc migration.

Nhưng disable preemption quá lâu làm tăng scheduling latency.

Tương tự với interrupt disable: nó là công cụ mạnh nhưng kéo dài thời gian interrupt bị chặn có thể gây latency toàn hệ thống.

## Interrupt disabling không phải lock tổng quát

Trên máy nhiều CPU, disable interrupt trên CPU hiện tại không ngăn CPU khác truy cập shared data.

Do đó code SMP vẫn cần synchronization phù hợp.

Điều này cho thấy nhiều kỹ thuật từng đủ trên uniprocessor không đủ trên hệ thống đa core.

## RCU, lock và scalability

Có thể hình dung một phổ thiết kế:

```text
coarse global lock
    ↓ dễ đúng, nhưng contention cao
fine-grained locks
    ↓ parallel hơn, protocol phức tạp hơn
per-CPU / lockless / RCU
    ↓ scalability cao trong workload phù hợp
    ↓ reasoning khó hơn nhiều
```

Không có primitive “tốt nhất”. Lựa chọn phụ thuộc read/write ratio, sleepability, latency, lifetime và correctness requirements.

## Quan sát contention từ user space

Không cần viết kernel code vẫn có thể quan sát triệu chứng synchronization.

```bash
pidstat -w -p <PID> 1
perf sched timehist
perf lock record -- <command>
```

Khả năng công cụ phụ thuộc kernel/config/permission.

Với Java:

```bash
jcmd <PID> Thread.print
```

Thread dump có thể cho thấy nhiều thread BLOCKED trên cùng monitor. Đây là tầng application, nhưng mental model contention giống kernel: nhiều execution context cạnh tranh shared state.

## Context switch tự nguyện và không tự nguyện

Một task có thể tự nguyện nhường CPU vì chờ lock/I/O hoặc bị scheduler preempt.

`pidstat -w` có thể cung cấp số context switch tự nguyện và không tự nguyện.

Con số cao không tự động xấu. Cần đặt cạnh workload, latency và blocking model.

Một server xử lý nhiều blocking I/O tự nhiên có nhiều context switch hơn một vòng tính CPU đơn luồng.

## Lock convoy

Nếu nhiều task cùng chờ một lock và sau mỗi lần release chỉ một task tiến lên rất ngắn rồi lại tranh lock, hệ thống có thể tạo **lock convoy**.

Throughput giảm dù CPU vẫn hoạt động mạnh.

Mẫu này cũng xuất hiện ở database connection pool, synchronized section hoặc global queue trong application.

## Thundering herd

Nếu một event đánh thức quá nhiều waiter nhưng chỉ một hoặc vài waiter có thể thực sự làm việc, các task còn lại tốn CPU để wake rồi ngủ lại.

Đây là **thundering herd**.

Các API như `epoll` và cơ chế wakeup hiện đại cố giảm vấn đề này trong những use case nhất định.

## Kernel lockup và watchdog

Nếu CPU mắc quá lâu trong kernel mà không schedule hoặc interrupt đúng cách, hệ thống có thể báo soft lockup/hard lockup tùy tình huống.

Kiểm tra kernel log:

```bash
journalctl -k | grep -Ei 'lockup|stall|hung task|rcu'
```

Các cảnh báo này không giống application deadlock thông thường. Chúng cho thấy kernel execution hoặc CPU progress đang có vấn đề nghiêm trọng hơn.

## RCU stall

Kernel có thể báo RCU stall nếu grace period không thể tiến triển như dự kiến, ví dụ CPU giữ trạng thái khiến RCU không nhận được quiescent state trong thời gian dài.

Đây là dấu hiệu cần xem CPU lockup, interrupt/preemption hoặc kernel/module behavior, không nên xử lý bằng cách tăng timeout một cách mù quáng.

## Mental Model

Hãy xem kernel như một hệ thống nhiều execution context cùng thao tác một đồ thị object sống động.

Synchronization phải giải quyết ba câu hỏi:

```text
1. Ai được truy cập cùng lúc?
2. Những operation phải được quan sát theo thứ tự nào?
3. Object được phép tồn tại đến khi nào?
```

Lock giải quyết phần mutual exclusion. Memory ordering giải quyết visibility/order. Reference counting và RCU giải quyết lifetime trong nhiều thiết kế.

## Những hiểu lầm phổ biến

**“Atomic nghĩa là thread-safe cho toàn bộ thuật toán.”** Atomic chỉ bảo vệ semantics của operation tương ứng; invariant nhiều bước có thể vẫn race.

**“Spinlock nhanh hơn mutex nên nên dùng spinlock.”** Nếu waiter có thể sleep hoặc critical section dài, spin có thể lãng phí CPU nghiêm trọng.

**“RCU là một mutex nhanh.”** RCU là một mô hình synchronization/lifetime khác, đặc biệt tối ưu read-heavy workload.

**“Disable interrupt là đủ để bảo vệ shared data.”** Không trên SMP; CPU khác vẫn có thể truy cập.

**“Nhiều context switch chắc chắn là lỗi.”** Phải hiểu blocking model và workload trước.

## Knowledge Connection

Chương này nên được đọc cùng:

- [CPU privilege và syscall path](./cpu_privilege_exceptions_syscall_path.md) để biết các execution context đi vào kernel thế nào;
- [Interrupt và softirq](./interrupts_softirq_device_model.md) để hiểu context không được sleep;
- [Process, thread và scheduler](../04_process/processes_threads_signals_jobs.md);
- [Kernel scheduler deep dive](../06_resources/kernel_scheduler_deep_dive.md);
- [IPC](../04_process/interprocess_communication.md) để nối wait queue, futex, socket và event-driven I/O;
- [Tracing](../09_production/observability_tracing_strace_perf.md) để quan sát contention và off-CPU time.
