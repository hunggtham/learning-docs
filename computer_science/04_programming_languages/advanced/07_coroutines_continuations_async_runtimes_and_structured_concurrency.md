# Coroutine, continuation, async runtime và structured concurrency

Một chương trình đồng thời (concurrent program) có thể phải xử lý hàng nghìn công việc chờ network hoặc storage nhưng chỉ có vài CPU core. Nếu ánh xạ mỗi công việc thành một OS thread, chi phí stack, scheduling và context switch có thể tăng nhanh. Coroutine và async runtime tồn tại để tách **đơn vị công việc logic** khỏi **đơn vị thực thi của hệ điều hành**.

## 1. Thread và coroutine khác nhau ở tầng nào?

**Luồng (thread / 스레드)** là đơn vị mà OS scheduler có thể lập lịch trực tiếp. Một thread có stack riêng, register state và kernel/runtime metadata.

**Coroutine** là một đơn vị thực thi có thể tạm dừng rồi tiếp tục sau. Nó thường được runtime hoặc thư viện quản lý phía trên OS thread.

```text
nhiều coroutine
      ↓
runtime scheduler
      ↓
một số OS thread
      ↓
CPU cores
```

Điểm cốt lõi là coroutine không tự chạy song song. Nó cần một scheduler và cuối cùng vẫn chạy trên thread thật.

## 2. Continuation là gì?

**Continuation** là thông tin mô tả “sau điểm hiện tại phải tiếp tục tính toán thế nào”. Khi một coroutine tạm dừng ở `await`, runtime phải lưu đủ trạng thái để sau này tiếp tục đúng chỗ.

Về mặt khái niệm, một call stack đang hoạt động cũng là một dạng continuation được biểu diễn bằng stack frame. Coroutine có thể biến trạng thái này thành object/state machine nằm trên heap thay vì giữ toàn bộ native stack đang chiếm thread.

## 3. Async/await thường được hạ thành state machine

Code:

```text
A
await B
C
```

có thể được compiler biến thành logic gần giống:

```text
state 0: chạy A, bắt đầu B, lưu continuation
state 1: khi B hoàn thành, khôi phục state và chạy C
```

`await` vì vậy không phải “dừng thread”. Nếu operation hỗ trợ non-blocking I/O, coroutine nhường quyền thực thi để thread chạy công việc khác.

## 4. Blocking và suspension không giống nhau

Nếu coroutine gọi một API blocking truyền thống, OS thread vẫn bị chặn. Đặt code blocking bên trong `async` không tự biến nó thành non-blocking.

Đây là lỗi mental model phổ biến:

```text
coroutine suspended -> thread có thể chạy việc khác
thread blocked      -> thread không làm việc khác được
```

Runtime thường cần thread pool riêng cho blocking I/O hoặc API legacy.

## 5. Event loop

Một **vòng lặp sự kiện (event loop)** lấy các task sẵn sàng rồi chạy từng đoạn ngắn. Khi task gặp I/O chưa hoàn tất, nó đăng ký interest và nhường control.

```text
ready queue
   ↓
run task
   ↓
await I/O -> register -> yield
   ↓
run next task
```

Khi kernel báo I/O sẵn sàng qua epoll/kqueue/IOCP/io_uring, runtime đưa continuation tương ứng về ready queue.

Đây là connection trực tiếp giữa async runtime và OS I/O subsystem.

## 6. Cooperative scheduling

Nhiều coroutine runtime dùng **lập lịch hợp tác (cooperative scheduling)**: task chỉ nhường tại điểm xác định như `await` hoặc yield. Nếu một coroutine chạy CPU loop dài mà không yield, nó có thể giữ thread và làm các coroutine khác đói tài nguyên.

Do đó async runtime phù hợp nhất với workload có nhiều chờ I/O; CPU-heavy work cần executor/thread pool phù hợp hoặc chia nhỏ.

## 7. Structured concurrency

**Đồng thời có cấu trúc (structured concurrency)** yêu cầu lifetime của task con nằm trong scope rõ ràng của task cha.

```text
parent scope
  ├── child A
  └── child B
```

Scope chỉ hoàn tất khi children hoàn tất hoặc được cancel theo policy. Điều này làm ownership của task rõ ràng hơn so với việc fire-and-forget task tùy ý.

Mental model giống structured programming: thay vì `goto` làm control flow khó theo dõi, structured concurrency tránh task lifetime trôi tự do khỏi nơi tạo nó.

## 8. Cancellation là một protocol

Cancel không phải lúc nào cũng “giết task ngay”. Nhiều runtime dùng cooperative cancellation: đặt cờ hoặc token, rồi task kiểm tra tại suspension point.

Code cần xác định:

```text
resource nào phải đóng?
transaction nào phải rollback?
finally/defer có chạy không?
child task có bị cancel theo không?
```

Cancellation safety là một phần correctness, không chỉ UX.

## 9. Timeout là cancellation có deadline

Timeout thường được xây bằng cancellation sau một deadline. Nhưng timeout ở client không chứng minh remote operation chưa xảy ra. Nếu HTTP request gửi payment rồi timeout, server có thể đã commit.

Async control flow vì vậy phải kết nối với idempotency và distributed-system semantics, không chỉ runtime scheduling.

## 10. Backpressure trong async pipeline

Nếu producer tạo task nhanh hơn consumer xử lý, queue tăng vô hạn dù mỗi task riêng lẻ non-blocking. Async không xóa capacity limit.

Cần bounded queue, semaphore, flow control hoặc demand protocol để tạo **áp lực ngược (backpressure)**.

```text
arrival rate > service rate
→ queue tăng
→ memory tăng
→ latency tăng
→ timeout/retry
→ tải tăng thêm
```

Đây là connection giữa runtime concurrency và queueing theory.

## 11. Thread-local trở nên khó với coroutine

Coroutine có thể suspend trên thread A rồi resume trên thread B. Vì vậy state gắn với OS thread không nhất thiết gắn với logical request.

Runtime thường cung cấp context propagation riêng như coroutine context, task-local hoặc async-local. Logging trace ID, security context và transaction context cần hiểu boundary này.

## 12. Synchronization vẫn tồn tại

Coroutine không loại race condition. Nếu nhiều coroutine chạy trên nhiều worker thread và cùng truy cập mutable state, vẫn cần mutex, actor, channel hoặc invariant khác.

Ngay cả single-threaded event loop cũng có logical race giữa hai async operation nếu state thay đổi qua các `await` point.

```text
read balance
await network
write balance
```

Trong lúc await, task khác có thể thay đổi balance. Suspension point là nơi invariant có thể bị phá nếu code giả định state đứng yên.

## 13. Actor và channel

**Actor model** đặt state bên trong actor và xử lý message tuần tự theo mailbox. **Channel** cho phép task giao tiếp qua queue có semantics rõ.

Hai mô hình này giảm shared mutable state nhưng không loại failure: mailbox có thể đầy, actor có thể crash, message có thể bị duplicate ở boundary distributed.

## 14. Work stealing

Một runtime nhiều worker có thể dùng **work stealing**: mỗi worker giữ deque task riêng; worker rảnh lấy task từ worker khác.

Điều này giảm contention trên một global queue và cân bằng tải tương đối tốt. Nhưng task affinity, cache locality và blocking task vẫn ảnh hưởng hiệu năng.

## 15. Scheduler fairness và starvation

Async scheduler phải quyết định task nào chạy tiếp. Nếu một task liên tục enqueue công việc mới hoặc không yield, task khác có thể bị starvation.

Fairness tuyệt đối có thể giảm throughput do tăng scheduling overhead. Đây là trade-off giống OS scheduler nhưng ở tầng runtime.

## 16. Async stack trace

Vì continuation có thể bị tách qua nhiều callback/state machine, native call stack không còn biểu diễn toàn bộ logical chain. Runtime hiện đại thường dựng **logical/async stack trace** bằng metadata bổ sung.

Observability tool cần hiểu async context; nếu không, trace sẽ mất parent-child relation ở điểm suspension.

## 17. Failure propagation

Structured concurrency thường định nghĩa rõ lỗi child ảnh hưởng parent thế nào. Một policy có thể cancel siblings khi một child fail; policy khác gom nhiều lỗi.

Không có semantics duy nhất. Điều quan trọng là task tree phải có rule xác định thay vì exception bị mất trong background task.

## 18. Java, Kotlin, JavaScript và Go

JavaScript thường dùng event loop + Promise/async-await. Kotlin coroutine dùng suspension và dispatcher, có structured concurrency mạnh. Java hiện đại có virtual thread giúp viết blocking style nhưng runtime ánh xạ nhiều virtual thread lên carrier thread. Go dùng goroutine và scheduler M:N.

Các API khác nhau nhưng câu hỏi nền tảng giống nhau:

```text
logical task được lưu state ở đâu?
OS thread bị block hay được giải phóng?
scheduler chọn task nào?
cancellation truyền như thế nào?
context truyền như thế nào?
backpressure nằm ở đâu?
```

## Common Misconceptions

**“Async nghĩa là chạy song song.”** Không. Async chủ yếu cho phép không giữ thread trong lúc chờ; parallelism cần nhiều execution resource.

**“Coroutine nhẹ nên tạo vô hạn được.”** Mỗi coroutine vẫn có state, queue entry, future/promise và downstream resource.

**“Single-thread event loop không có race.”** Không có data race kiểu nhiều CPU thread trong một thời điểm, nhưng logical interleaving qua `await` vẫn có thể phá invariant.

**“Cancellation dừng operation remote.”** Cancel local wait không đảm bảo remote server chưa thực hiện side effect.

## Mô hình tư duy

> Async runtime là một scheduler ở tầng ngôn ngữ: nó lưu continuation của hàng nghìn công việc logic và ánh xạ chúng lên ít execution resource hơn, nhưng vẫn phải tôn trọng các giới hạn của OS, CPU, I/O và downstream system.

Muốn reasoning ở mức Senior/Master, hãy theo đường: coroutine state → runtime scheduler → OS thread → syscall/I/O readiness → network/storage → completion → continuation resume, đồng thời theo dõi cancellation, context propagation và backpressure.

Xem thêm: [OS async I/O](../../03_operating_systems/advanced/05_epoll_io_uring_zero_copy_and_dma.md), [Software Systems queues](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [Distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md).
