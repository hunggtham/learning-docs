# Đồng bộ hóa tiến trình/luồng, mutex, điều kiện (condition / 조건) variable và `futex`

> **Mạch đọc:** Đọc **Đồng bộ hóa tiến trình/luồng, mutex, điều kiện (condition / 조건) variable và futex** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Race điều kiện (condition / 조건) xuất hiện như thế nào?** sang **Atomic thao tác (operation / 연산)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Đa luồng cho phép nhiều luồng thực thi cùng chia sẻ dữ liệu, nhưng chính khả năng chia sẻ này tạo ra race điều kiện (condition / 조건). Linux không giải quyết mọi vấn đề đồng bộ thay ứng dụng; phần lớn lô-gic (logic / 논리) khóa (lock / 잠금) nằm trong thư viện người dùng (user / 사용자) không gian (space / 공간), còn kernel cung cấp thành phần nguyên thủy (primitive / 기본 요소) cần thiết khi luồng thực thi (thread / 스레드) phải ngủ hoặc được đánh thức. Một thành phần nguyên thủy (primitive / 기본 요소) đặc biệt quan trọng là **futex (fast userspace mutex)**.

## Race điều kiện (condition / 조건) xuất hiện như thế nào?

Giả sử hai luồng thực thi (thread / 스레드) cùng tăng biến `counter`:

```text
read counter
add 1
write counter
```

Nếu hai luồng thực thi (thread / 스레드) xen kẽ các bước, một lần tăng có thể bị mất.

Vấn đề không nằm ở “CPU chạy sai” mà ở việc thao tác (operation / 연산) lô-gic (logic / 논리) không atomic đối với thực thi (execution / 실행) xen kẽ.

## Atomic thao tác (operation / 연산)

CPU cung cấp instruction atomic cho một số thao tác như compare-and-swap. thời gian chạy (runtime / 런타임) và thư viện dùng chúng để xây khóa (lock / 잠금) hoặc cấu trúc lock-free.

Atomicity chỉ đảm bảo thao tác (operation / 연산) cụ thể không bị xen kẽ theo cách phá vỡ ngữ nghĩa (semantics / 의미론). Nó không tự động giải quyết mọi bất biến (invariant / 불변식) phức tạp giữa nhiều biến.

## Mutex

Mutex bảo đảm chỉ một luồng thực thi (thread / 스레드) giữ khóa (lock / 잠금) tại một thời điểm.

```text
lock
→ critical section
→ unlock
```

Nếu khóa (lock / 잠금) đang rảnh, thao tác có thể hoàn tất hoàn toàn trong người dùng (user / 사용자) không gian (space / 공간) bằng atomic instruction mà không cần lời gọi hệ thống (system call / 시스템 호출).

Đây là điểm quan trọng: **khóa (lock / 잠금) không đồng nghĩa luôn vào kernel**.

## Khi contention xảy ra

Nếu luồng thực thi (thread / 스레드) B cố lấy mutex mà luồng thực thi (thread / 스레드) A đang giữ, B có hai lựa chọn tổng quát:

- quay vòng chờ (spin);
- ngủ và chờ được đánh thức.

Spin phù hợp nếu chờ cực ngắn vì tránh scheduling overhead, nhưng lãng phí CPU nếu khóa (lock / 잠금) giữ lâu.

Sleeping tiết kiệm CPU nhưng cần kernel hỗ trợ khối (block / 블록)/wakeup.

## Futex là gì?

Futex cho phép trạng thái khóa (lock / 잠금) thông thường nằm trong bộ nhớ (memory / 메모리) người dùng (user / 사용자) không gian (space / 공간), chỉ gọi kernel khi cần phối hợp chờ/đánh thức.

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

Đây là lý do gọi là **fast userspace mutex**: fast đường dẫn (path / 경로) ở người dùng (user / 사용자) không gian (space / 공간), kernel chủ yếu xử lý slow đường dẫn (path / 경로).

## `strace` và futex

Ứng dụng Java hoặc bản địa (native / 네이티브) nhiều luồng thực thi (thread / 스레드) thường xuất hiện:

```text
futex(..., FUTEX_WAIT_PRIVATE, ...)
```

Điều đó không tự động nghĩa lỗi. luồng thực thi (thread / 스레드) có thể đang chờ monitor, điều kiện (condition / 조건) variable, luồng thực thi (thread / 스레드) pool hàng đợi (queue / 큐) hoặc thời gian chạy (runtime / 런타임) synchronization bình thường.

Nếu CPU thấp và nhiều luồng thực thi (thread / 스레드) ngủ trong futex, hệ thống có thể đơn giản đang chờ công việc.

Nếu độ trễ (latency / 지연 시간) cao và yêu cầu (request / 요청) threads đều chờ cùng khóa (lock / 잠금), đó lại có thể là contention bottleneck.

## Điều kiện (condition / 조건) variable

Điều kiện (condition / 조건) variable cho phép luồng thực thi (thread / 스레드) ngủ cho tới khi một điều kiện lô-gic (logic / 논리) có thể đã thay đổi.

Mẫu (pattern / 패턴):

```text
lock mutex
while condition false:
    wait(condition, mutex)
process state
unlock
```

Tại sao phải dùng `while` thay vì `if`? Vì wakeup không đảm bảo điều kiện vẫn đúng khi luồng thực thi (thread / 스레드) thực sự giành lại mutex; có thể có spurious wakeup hoặc luồng thực thi (thread / 스레드) khác đã thay đổi trạng thái (state / 상태).

## Semaphore

Semaphore quản lý một bộ đếm permit thay vì quyền sở hữu (ownership / 소유권) một-một như mutex.

Ví dụ giới hạn tối đa 20 tác vụ cùng dùng tài nguyên (resource / 자원).

Semaphore phù hợp với sức chứa (capacity / 용량) điều khiển (control / 제어); mutex phù hợp với mutual exclusion. Dùng chúng như cùng một khái niệm sẽ làm lập luận (reasoning / 추론) sai.

## Read-write khóa (lock / 잠금)

Read-write khóa (lock / 잠금) cho phép nhiều reader cùng vào nhưng writer cần độc quyền.

Nó có thể hữu ích khi read nhiều và ghi (write / 쓰기) ít, nhưng overhead và starvation/fairness có thể làm nó tệ hơn mutex trong tải công việc (workload / 워크로드) thực tế.

Không chọn khóa (lock / 잠금) chỉ vì tên nghe “tối ưu hơn”.

## Spinlock

Spinlock làm luồng thực thi (thread / 스레드) quay vòng kiểm tra khóa (lock / 잠금) thay vì ngủ.

Trong kernel, spinlock cần thiết ở ngữ cảnh (context / 맥락) không thể sleep hoặc trọng yếu (critical / 중요) section rất ngắn. Trong người dùng (user / 사용자) không gian (space / 공간), spin có thể hữu ích trong tải công việc (workload / 워크로드) đặc biệt nhưng dễ đốt CPU.

Nếu khóa (lock / 잠금) holder bị scheduler deschedule trong khi waiter spin, hiệu quả có thể rất tệ.

## Priority inversion

Luồng thực thi (thread / 스레드) ưu tiên cao chờ khóa (lock / 잠금) do luồng thực thi (thread / 스레드) ưu tiên thấp giữ, trong khi luồng thực thi (thread / 스레드) ưu tiên trung bình liên tục chiếm CPU. Đây là **priority inversion**.

Một số mutex/giao thức (protocol / 프로토콜) hỗ trợ priority inheritance để giảm vấn đề này.

Chủ đề đặc biệt quan trọng với real-time các hệ thống (systems / 시스템들).

## Deadlock

Deadlock kinh điển:

```text
Thread A giữ lock 1, chờ lock 2
Thread B giữ lock 2, chờ lock 1
```

Bốn điều kiện Coffman thường được dùng để lập luận (reasoning / 추론): mutual exclusion, hold-and-wait, no preemption và circular wait.

Cách phòng tránh phổ biến là định nghĩa khóa (lock / 잠금) thứ tự (ordering / 순서) nhất quán.

## Livelock và starvation

Deadlock nghĩa không ai tiến triển vì chờ nhau.

Livelock nghĩa các luồng thực thi (thread / 스레드) vẫn hoạt động nhưng liên tục nhường/thử lại (retry / 재시도) nên không hoàn thành công việc.

Starvation nghĩa một luồng thực thi (thread / 스레드) hiếm khi hoặc không bao giờ nhận được tài nguyên (resource / 자원) do scheduling/fairness.

Ba dạng thất bại (failure mode / 실패 모드) này khác nhau và cần quan sát khác nhau.

## Bộ nhớ (memory / 메모리) thứ tự (ordering / 순서)

Ngay cả khi không có khóa (lock / 잠금) truyền thống, CPU/trình biên dịch (compiler / 컴파일러) có thể reorder bộ nhớ (memory / 메모리) thao tác (operation / 연산) theo quy tắc bộ nhớ (memory / 메모리) mô hình (model / 모델). Atomic thao tác (operation / 연산) và bộ nhớ (memory / 메모리) barrier đảm bảo thứ tự (ordering / 순서) cần thiết.

Đây là lý do concurrent programming không thể chỉ lập luận (reasoning / 추론) theo thứ tự mã nguồn (source code / 소스 코드) đơn giản.

Java bộ nhớ (memory / 메모리) mô hình (model / 모델) che giấu nhiều chi tiết phần cứng nhưng vẫn yêu cầu `volatile`, synchronization hoặc concurrent primitives để thiết lập happens-before quan hệ (relation / 관계).

## Tranh chấp khóa (lock contention / 잠금 경합) và scheduler

Contention không chỉ là “nhiều luồng thực thi (thread / 스레드) muốn khóa (lock / 잠금)”. Nó tác động tới scheduler:

```text
thread chạy
→ cố lấy lock
→ sleep
→ context switch
→ holder chạy
→ wake waiter
→ waiter trở lại run queue
```

Nếu khóa (lock / 잠금) rất nóng, hệ thống có thể tốn thời gian vào wakeup/ngữ cảnh (context / 맥락) switch hơn nghiệp vụ (business / 비즈니스) công việc (work / 작업).

## Thundering herd

Nếu một sự kiện (event / 이벤트) đánh thức rất nhiều waiter nhưng chỉ một hoặc ít luồng thực thi (thread / 스레드) có thể tiến triển, các luồng thực thi (thread / 스레드) còn lại thức dậy rồi lại ngủ, gây overhead.

Kernel và thời gian chạy (runtime / 런타임) có kỹ thuật giảm herd, nhưng mẫu (pattern / 패턴) này vẫn xuất hiện trong máy chủ (server / 서버) thiết kế (design / 설계) và queueing.

## Java monitor và Linux

Java `synchronized`, `ReentrantLock`, `LockSupport.park()` và nhiều concurrent utilities cuối cùng dựa vào thời gian chạy (runtime / 런타임) + OS primitives khi luồng thực thi (thread / 스레드) cần khối (block / 블록).

Không nên giả định một Java monitor tương ứng trực tiếp một futex đơn giản, vì JVM có nhiều tối ưu hóa (optimization / 최적화) như biased/thin/heavyweight locking tùy phiên bản/thời gian chạy (runtime / 런타임).

Nhưng ở tầng Linux, contention cuối cùng thường dẫn tới luồng thực thi (thread / 스레드) sleep/wakeup primitives.

## Luồng thực thi (thread / 스레드) dump và futex bằng chứng (evidence / 증거)

Luồng thực thi (thread / 스레드) dump Java cho ngữ nghĩa (semantic / 의미적) application-level tốt hơn `strace`:

```bash
jcmd <PID> Thread.print
```

Linux tools bổ sung tầng scheduling:

```bash
pidstat -t -p <PID> 1
ps -L -p <PID> -o pid,tid,stat,pcpu,wchan:30,comm
```

`wchan` có thể cho biết kernel wait channel, nhưng không thay thế thời gian chạy (runtime / 런타임) dấu vết ngăn xếp (stack trace / 스택 트레이스).

Kết hợp hai tầng:

```text
Java stack: đang chờ lock nào?
Linux: thread đang runnable hay sleeping?
perf: CPU nóng ở đâu?
strace: có futex wait/wake pattern gì?
```

## Khóa (lock / 잠금) convoy

Nếu nhiều luồng thực thi (thread / 스레드) xếp hàng sau một khóa (lock / 잠금) và mỗi lần chỉ một luồng thực thi (thread / 스레드) tiến triển, hệ thống có thể hình thành khóa (lock / 잠금) convoy. Khi khóa (lock / 잠금) holder bị chậm bởi I/O hoặc preemption, hàng đợi phía sau tăng mạnh.

Đây là ví dụ tail độ trễ (latency / 지연 시간) có thể tăng dù CPU trung bình chưa 100%.

## Blocking hàng đợi (queue / 큐) và luồng thực thi (thread / 스레드) pool

Luồng thực thi (thread / 스레드) pool thường dùng hàng đợi (queue / 큐) + điều kiện (condition / 조건)/futex để worker ngủ khi không có việc.

Đây là trạng thái bình thường:

```text
queue empty
→ workers sleep
→ producer enqueue
→ wake worker
```

Nhưng nếu hàng đợi (queue / 큐) tăng liên tục, vấn đề nằm ở dịch vụ (service / 서비스) tỷ lệ (rate / 비율)/sức chứa (capacity / 용량) chứ không phải futex bản thân.

## Lock-free không đồng nghĩa wait-free

Lock-free thuật toán (algorithm / 알고리즘) bảo đảm hệ thống tổng thể có tiến triển theo định nghĩa nhất định, nhưng một luồng thực thi (thread / 스레드) cụ thể vẫn có thể starvation.

Wait-free mạnh hơn: mỗi thao tác (operation / 연산) hoàn thành trong số bước hữu hạn theo mô hình.

Đây là thuật ngữ tính đồng thời (concurrency / 동시성) chính xác, không nên dùng “lock-free = không bao giờ chờ”.

## False sharing

Hai luồng thực thi (thread / 스레드) sửa hai biến lô-gic (logic / 논리) khác nhau nhưng nằm trên cùng CPU bộ nhớ đệm (cache / 캐시) line có thể gây bộ nhớ đệm (cache / 캐시) coherence traffic lớn.

Đây không phải tranh chấp khóa (lock contention / 잠금 경합) truyền thống nhưng có triệu chứng CPU/hiệu năng (performance / 성능) tương tự.

`perf` và hardware counters có thể hỗ trợ điều tra tải công việc (workload / 워크로드) nâng cao.

## Mô hình tư duy

Một synchronization thành phần nguyên thủy (primitive / 기본 요소) có hai tầng:

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

Vì vậy muốn hiểu tranh chấp khóa (lock contention / 잠금 경합) phải nhìn cả **lô-gic (logic / 논리) đồng bộ của ứng dụng** và **trạng thái scheduling của Linux**.

## Những hiểu lầm phổ biến

**“Mutex luôn là syscall.”** Fast đường dẫn (path / 경로) thường có thể xử lý hoàn toàn trong người dùng (user / 사용자) không gian (space / 공간).

**“Thấy futex trong strace nghĩa app deadlock.”** Futex wait là hoạt động bình thường của nhiều thời gian chạy (runtime / 런타임).

**“CPU thấp nghĩa app không bị contention.”** Nhiều luồng thực thi (thread / 스레드) có thể đang ngủ chờ cùng khóa (lock / 잠금).

**“Nhiều luồng thực thi (thread / 스레드) hơn luôn tăng thông lượng (throughput / 처리량).”** Nếu dùng chung (shared / 공유) khóa (lock / 잠금) hoặc downstream là bottleneck, luồng thực thi (thread / 스레드) thêm chỉ tăng hàng đợi (queue / 큐)/ngữ cảnh (context / 맥락) switch.

**“Lock-free nghĩa mọi luồng thực thi (thread / 스레드) luôn tiến triển ngay.”** Lock-free và wait-free có định nghĩa chặt chẽ khác nhau.

## Kết nối kiến thức

Chương này nối [process/thread](./processes_threads_signals_jobs.md), [scheduler sâu](../06_resources/kernel_scheduler_deep_dive.md), [system call lifecycle](../00_foundations/system_call_lifecycle.md), [IPC](./interprocess_communication.md) và [Java incident playbook](../09_production/java_backend_incident_playbook.md).

> **Bàn giao:** Sau **Kết nối kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [interprocess communication](./interprocess_communication.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
