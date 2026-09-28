# Coroutine, continuation, async thời gian chạy (runtime / 런타임) và structured tính đồng thời (concurrency / 동시성)

> **Mạch đọc:** Đặt **Coroutine, continuation, async thời gian chạy (runtime / 런타임) và structured tính đồng thời (concurrency / 동시성)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. luồng thực thi (thread / 스레드) và coroutine khác nhau ở tầng nào?** sang **2. Continuation là gì?**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một chương trình đồng thời (concurrent program) có thể phải xử lý hàng nghìn công việc chờ mạng (network / 네트워크) hoặc lưu trữ (storage / 저장소) nhưng chỉ có vài CPU cốt lõi (core / 핵심). Nếu ánh xạ mỗi công việc thành một OS luồng thực thi (thread / 스레드), chi phí ngăn xếp (stack / 스택), scheduling và ngữ cảnh (context / 맥락) switch có thể tăng nhanh. Coroutine và async thời gian chạy (runtime / 런타임) tồn tại để tách **đơn vị công việc lô-gic (logic / 논리)** khỏi **đơn vị thực thi của hệ điều hành**.

## 1. luồng thực thi (thread / 스레드) và coroutine khác nhau ở tầng nào?

**Luồng (thread / 스레드)** là đơn vị mà OS scheduler có thể lập lịch trực tiếp. Một luồng thực thi (thread / 스레드) có ngăn xếp (stack / 스택) riêng, register trạng thái (state / 상태) và kernel/thời gian chạy (runtime / 런타임) siêu dữ liệu (metadata / 메타데이터).

**Coroutine** là một đơn vị thực thi có thể tạm dừng rồi tiếp tục sau. Nó thường được thời gian chạy (runtime / 런타임) hoặc thư viện quản lý phía trên OS luồng thực thi (thread / 스레드).

```text
nhiều coroutine
      ↓
runtime scheduler
      ↓
một số OS thread
      ↓
CPU cores
```

Điểm cốt lõi là coroutine không tự chạy song song. Nó cần một scheduler và cuối cùng vẫn chạy trên luồng thực thi (thread / 스레드) thật.

## 2. Continuation là gì?

**Continuation** là thông tin mô tả “sau điểm hiện tại phải tiếp tục tính toán thế nào”. Khi một coroutine tạm dừng ở `await`, thời gian chạy (runtime / 런타임) phải lưu đủ trạng thái để sau này tiếp tục đúng chỗ.

Về mặt khái niệm, một ngăn xếp lời gọi (call stack / 호출 스택) đang hoạt động cũng là một dạng continuation được biểu diễn bằng ngăn xếp (stack / 스택) frame. Coroutine có thể biến trạng thái này thành đối tượng (object / 객체)/máy trạng thái (state machine / 상태 머신) nằm trên vùng nhớ động (heap / 힙) thay vì giữ toàn bộ bản địa (native / 네이티브) ngăn xếp (stack / 스택) đang chiếm luồng thực thi (thread / 스레드).

## 3. Async/await thường được hạ thành máy trạng thái (state machine / 상태 머신)

Mã (code / 코드):

```text
A
await B
C
```

có thể được trình biên dịch (compiler / 컴파일러) biến thành lô-gic (logic / 논리) gần giống:

```text
state 0: chạy A, bắt đầu B, lưu continuation
state 1: khi B hoàn thành, khôi phục state và chạy C
```

`await` vì vậy không phải “dừng luồng thực thi (thread / 스레드)”. Nếu thao tác (operation / 연산) hỗ trợ non-blocking I/O, coroutine nhường quyền thực thi để luồng thực thi (thread / 스레드) chạy công việc khác.

## 4. Blocking và suspension không giống nhau

Nếu coroutine gọi một API blocking truyền thống, OS luồng thực thi (thread / 스레드) vẫn bị chặn. Đặt mã (code / 코드) blocking bên trong `async` không tự biến nó thành non-blocking.

Đây là lỗi mô hình tư duy (mental model / 사고 모델) phổ biến:

```text
coroutine suspended -> thread có thể chạy việc khác
thread blocked      -> thread không làm việc khác được
```

Thời gian chạy (runtime / 런타임) thường cần luồng thực thi (thread / 스레드) pool riêng cho blocking I/O hoặc API legacy.

## 5. vòng lặp sự kiện (event loop / 이벤트 루프)

Một **vòng lặp sự kiện (event loop / 이벤트 루프)** lấy các tác vụ (task / 작업) sẵn sàng rồi chạy từng đoạn ngắn. Khi tác vụ (task / 작업) gặp I/O chưa hoàn tất, nó đăng ký interest và nhường điều khiển (control / 제어).

```text
ready queue
   ↓
run task
   ↓
await I/O -> register -> yield
   ↓
run next task
```

Khi kernel báo I/O sẵn sàng qua epoll/kqueue/IOCP/io_uring, thời gian chạy (runtime / 런타임) đưa continuation tương ứng về ready hàng đợi (queue / 큐).

Đây là liên kết (connection / 연결) trực tiếp giữa async thời gian chạy (runtime / 런타임) và OS I/O subsystem.

## 6. Cooperative scheduling

Nhiều coroutine thời gian chạy (runtime / 런타임) dùng **lập lịch hợp tác (cooperative scheduling)**: tác vụ (task / 작업) chỉ nhường tại điểm xác định như `await` hoặc yield. Nếu một coroutine chạy CPU vòng lặp (loop / 루프) dài mà không yield, nó có thể giữ luồng thực thi (thread / 스레드) và làm các coroutine khác đói tài nguyên.

Do đó async thời gian chạy (runtime / 런타임) phù hợp nhất với tải công việc (workload / 워크로드) có nhiều chờ I/O; CPU-heavy công việc (work / 작업) cần executor/luồng thực thi (thread / 스레드) pool phù hợp hoặc chia nhỏ.

## 7. Structured tính đồng thời (concurrency / 동시성)

**Đồng thời có cấu trúc (structured concurrency)** yêu cầu thời gian tồn tại (lifetime / 수명) của tác vụ (task / 작업) con nằm trong phạm vi (scope / 범위) rõ ràng của tác vụ (task / 작업) cha.

```text
parent scope
  ├── child A
  └── child B
```

Phạm vi (scope / 범위) chỉ hoàn tất khi children hoàn tất hoặc được cancel theo chính sách (policy / 정책). Điều này làm quyền sở hữu (ownership / 소유권) của tác vụ (task / 작업) rõ ràng hơn so với việc fire-and-forget tác vụ (task / 작업) tùy ý.

Mô hình tư duy (mental model / 사고 모델) giống structured programming: thay vì `goto` làm điều khiển (control / 제어) luồng (flow / 흐름) khó theo dõi, structured tính đồng thời (concurrency / 동시성) tránh tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명) trôi tự do khỏi nơi tạo nó.

## 8. Cancellation là một giao thức (protocol / 프로토콜)

Cancel không phải lúc nào cũng “giết tác vụ (task / 작업) ngay”. Nhiều thời gian chạy (runtime / 런타임) dùng cooperative cancellation: đặt cờ hoặc đơn vị từ (token / 토큰), rồi tác vụ (task / 작업) kiểm tra tại suspension điểm (point / 지점).

Mã (code / 코드) cần xác định:

```text
resource nào phải đóng?
transaction nào phải rollback?
finally/defer có chạy không?
child task có bị cancel theo không?
```

Cancellation an toàn (safety / 안전) là một phần tính đúng đắn (correctness / 정확성), không chỉ UX.

## 9. hết thời gian chờ (timeout / 타임아웃) là cancellation có deadline

Hết thời gian chờ (timeout / 타임아웃) thường được xây bằng cancellation sau một deadline. Nhưng hết thời gian chờ (timeout / 타임아웃) ở máy khách (client / 클라이언트) không chứng minh remote thao tác (operation / 연산) chưa xảy ra. Nếu HTTP yêu cầu (request / 요청) gửi payment rồi hết thời gian chờ (timeout / 타임아웃), máy chủ (server / 서버) có thể đã lần ghi nhận (commit / 커밋).

Async điều khiển (control / 제어) luồng (flow / 흐름) vì vậy phải kết nối với idempotency và distributed-system ngữ nghĩa (semantics / 의미론), không chỉ thời gian chạy (runtime / 런타임) scheduling.

## 10. Backpressure trong async chuỗi xử lý (pipeline / 파이프라인)

Nếu producer tạo tác vụ (task / 작업) nhanh hơn bên tiêu thụ (consumer / 소비자) xử lý, hàng đợi (queue / 큐) tăng vô hạn dù mỗi tác vụ (task / 작업) riêng lẻ non-blocking. Async không xóa sức chứa (capacity / 용량) limit.

Cần bounded hàng đợi (queue / 큐), semaphore, luồng (flow / 흐름) điều khiển (control / 제어) hoặc demand giao thức (protocol / 프로토콜) để tạo **áp lực ngược (backpressure)**.

```text
arrival rate > service rate
→ queue tăng
→ memory tăng
→ latency tăng
→ timeout/retry
→ tải tăng thêm
```

Đây là liên kết (connection / 연결) giữa thời gian chạy (runtime / 런타임) tính đồng thời (concurrency / 동시성) và queueing lý thuyết (theory / 이론).

## 11. Thread-local trở nên khó với coroutine

Coroutine có thể suspend trên luồng thực thi (thread / 스레드) A rồi resume trên luồng thực thi (thread / 스레드) B. Vì vậy trạng thái (state / 상태) gắn với OS luồng thực thi (thread / 스레드) không nhất thiết gắn với logical yêu cầu (request / 요청).

Thời gian chạy (runtime / 런타임) thường cung cấp ngữ cảnh (context / 맥락) propagation riêng như coroutine ngữ cảnh (context / 맥락), task-local hoặc async-local. Logging dấu vết (trace / 추적) ID, bảo mật (security / 보안) ngữ cảnh (context / 맥락) và giao dịch (transaction / 트랜잭션) ngữ cảnh (context / 맥락) cần hiểu ranh giới (boundary / 경계) này.

## 12. Synchronization vẫn tồn tại

Coroutine không loại race điều kiện (condition / 조건). Nếu nhiều coroutine chạy trên nhiều worker luồng thực thi (thread / 스레드) và cùng truy cập mutable trạng thái (state / 상태), vẫn cần mutex, actor, channel hoặc bất biến (invariant / 불변식) khác.

Ngay cả single-threaded vòng lặp sự kiện (event loop / 이벤트 루프) cũng có logical race giữa hai async thao tác (operation / 연산) nếu trạng thái (state / 상태) thay đổi qua các `await` điểm (point / 지점).

```text
read balance
await network
write balance
```

Trong lúc await, tác vụ (task / 작업) khác có thể thay đổi balance. Suspension điểm (point / 지점) là nơi bất biến (invariant / 불변식) có thể bị phá nếu mã (code / 코드) giả định trạng thái (state / 상태) đứng yên.

## 13. Actor và channel

**Actor mô hình (model / 모델)** đặt trạng thái (state / 상태) bên trong actor và xử lý message tuần tự theo mailbox. **Channel** cho phép tác vụ (task / 작업) giao tiếp qua hàng đợi (queue / 큐) có ngữ nghĩa (semantics / 의미론) rõ.

Hai mô hình này giảm dùng chung (shared / 공유) mutable trạng thái (state / 상태) nhưng không loại thất bại (failure / 실패): mailbox có thể đầy, actor có thể crash, message có thể bị duplicate ở ranh giới (boundary / 경계) phân tán (distributed / 분산).

## 14. công việc (work / 작업) stealing

Một thời gian chạy (runtime / 런타임) nhiều worker có thể dùng **công việc (work / 작업) stealing**: mỗi worker giữ deque tác vụ (task / 작업) riêng; worker rảnh lấy tác vụ (task / 작업) từ worker khác.

Điều này giảm contention trên một toàn cục (global / 전역) hàng đợi (queue / 큐) và cân bằng tải tương đối tốt. Nhưng tác vụ (task / 작업) affinity, bộ nhớ đệm (cache / 캐시) locality và blocking tác vụ (task / 작업) vẫn ảnh hưởng hiệu năng.

## 15. Scheduler fairness và starvation

Async scheduler phải quyết định tác vụ (task / 작업) nào chạy tiếp. Nếu một tác vụ (task / 작업) liên tục enqueue công việc mới hoặc không yield, tác vụ (task / 작업) khác có thể bị starvation.

Fairness tuyệt đối có thể giảm thông lượng (throughput / 처리량) do tăng scheduling overhead. Đây là sự đánh đổi (trade-off / 트레이드오프) giống OS scheduler nhưng ở tầng thời gian chạy (runtime / 런타임).

## 16. Async dấu vết ngăn xếp (stack trace / 스택 트레이스)

Vì continuation có thể bị tách qua nhiều callback/máy trạng thái (state machine / 상태 머신), bản địa (native / 네이티브) ngăn xếp lời gọi (call stack / 호출 스택) không còn biểu diễn toàn bộ logical chuỗi (chain / 사슬). thời gian chạy (runtime / 런타임) hiện đại thường dựng **logical/async dấu vết ngăn xếp (stack trace / 스택 트레이스)** bằng siêu dữ liệu (metadata / 메타데이터) bổ sung.

Khả năng quan sát (observability / 관측 가능성) công cụ (tool / 도구) cần hiểu async ngữ cảnh (context / 맥락); nếu không, dấu vết (trace / 추적) sẽ mất parent-child quan hệ (relation / 관계) ở điểm suspension.

## 17. thất bại (failure / 실패) propagation

Structured tính đồng thời (concurrency / 동시성) thường định nghĩa rõ lỗi child ảnh hưởng parent thế nào. Một chính sách (policy / 정책) có thể cancel siblings khi một child thất bại (fail / 실패); chính sách (policy / 정책) khác gom nhiều lỗi.

Không có ngữ nghĩa (semantics / 의미론) duy nhất. Điều quan trọng là tác vụ (task / 작업) cây (tree / 트리) phải có quy tắc (rule / 규칙) xác định thay vì exception bị mất trong background tác vụ (task / 작업).

## 18. Java, Kotlin, JavaScript và Go

JavaScript thường dùng vòng lặp sự kiện (event loop / 이벤트 루프) + Promise/async-await. Kotlin coroutine dùng suspension và dispatcher, có structured tính đồng thời (concurrency / 동시성) mạnh. Java hiện đại có virtual luồng thực thi (thread / 스레드) giúp viết blocking style nhưng thời gian chạy (runtime / 런타임) ánh xạ nhiều virtual luồng thực thi (thread / 스레드) lên carrier luồng thực thi (thread / 스레드). Go dùng goroutine và scheduler M:N.

Các API khác nhau nhưng câu hỏi nền tảng giống nhau:

```text
logical task được lưu state ở đâu?
OS thread bị block hay được giải phóng?
scheduler chọn task nào?
cancellation truyền như thế nào?
context truyền như thế nào?
backpressure nằm ở đâu?
```

## Dùng chung (common / 공통) Misconceptions

**“Async nghĩa là chạy song song.”** Không. Async chủ yếu cho phép không giữ luồng thực thi (thread / 스레드) trong lúc chờ; parallelism cần nhiều thực thi (execution / 실행) tài nguyên (resource / 자원).

**“Coroutine nhẹ nên tạo vô hạn được.”** Mỗi coroutine vẫn có trạng thái (state / 상태), hàng đợi (queue / 큐) entry, future/promise và downstream tài nguyên (resource / 자원).

**“Single-thread vòng lặp sự kiện (event loop / 이벤트 루프) không có race.”** Không có dữ liệu (data / 데이터) race kiểu nhiều CPU luồng thực thi (thread / 스레드) trong một thời điểm, nhưng logical interleaving qua `await` vẫn có thể phá bất biến (invariant / 불변식).

**“Cancellation dừng thao tác (operation / 연산) remote.”** Cancel cục bộ (local / 로컬) wait không đảm bảo remote máy chủ (server / 서버) chưa thực hiện side tác động (effect / 효과).

## Mô hình tư duy

> Async thời gian chạy (runtime / 런타임) là một scheduler ở tầng ngôn ngữ: nó lưu continuation của hàng nghìn công việc lô-gic (logic / 논리) và ánh xạ chúng lên ít thực thi (execution / 실행) tài nguyên (resource / 자원) hơn, nhưng vẫn phải tôn trọng các giới hạn của OS, CPU, I/O và downstream hệ thống (system / 시스템).

Muốn lập luận (reasoning / 추론) ở mức cấp cao (senior / 시니어)/Master, hãy theo đường: coroutine trạng thái (state / 상태) → thời gian chạy (runtime / 런타임) scheduler → OS luồng thực thi (thread / 스레드) → syscall/I/O readiness → mạng (network / 네트워크)/lưu trữ (storage / 저장소) → completion → continuation resume, đồng thời theo dõi cancellation, ngữ cảnh (context / 맥락) propagation và backpressure.

Xem thêm: [OS async I/O](../../03_operating_systems/advanced/05_epoll_io_uring_zero_copy_and_dma.md), [Software Systems queues](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [Distributed transactions](../../05_data_databases/advanced/07_distributed_transactions_2pc_consensus_sagas_and_outbox.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 type systems effects and runtime contracts](./00_type_systems_effects_and_runtime_contracts.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
