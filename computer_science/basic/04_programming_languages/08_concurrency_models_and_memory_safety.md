# Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)

> **Mạch đọc:** Đọc **tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. tính đồng thời (concurrency / 동시성) và parallelism không giống nhau** sang **2. bất biến (invariant / 불변식) phải được viết trước synchronization thành phần nguyên thủy (primitive / 기본 요소)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tính đồng thời (concurrency / 동시성) không chỉ là “dùng nhiều threads”. Một tính đồng thời (concurrency / 동시성) mô hình (model / 모델) trả lời bốn câu hỏi nền tảng: **thực thi (execution / 실행) units nào tồn tại, trạng thái (state / 상태) thuộc về ai, communication diễn ra qua dùng chung (shared / 공유) bộ nhớ (memory / 메모리) hay messages, và thứ tự (ordering / 순서)/thời gian tồn tại (lifetime / 수명) nào được guarantee**. Threads + locks, actors, CSP/channels, async tasks, immutable dữ liệu (data / 데이터) và quyền sở hữu (ownership / 소유권) chỉ là những cách khác nhau để đặt ranh giới (boundary / 경계) cho cùng bài toán: nhiều hoạt động tiến triển cùng lúc nhưng vẫn phải giữ bất biến (invariant / 불변식).

Advanced lập luận (reasoning / 추론) không bắt đầu bằng API như `Thread`, `async`, `Mutex` hay `Channel`. Nó bắt đầu bằng máy trạng thái (state machine / 상태 머신) và bất biến (invariant / 불변식) cần được giữ khi operations có thể interleave.

## 1. tính đồng thời (concurrency / 동시성) và parallelism không giống nhau

**tính đồng thời (concurrency / 동시성)** nghĩa nhiều tasks có thời gian tồn tại (lifetime / 수명) chồng lấp và tiến triển xen kẽ. **Parallelism** nghĩa nhiều operations thật sự chạy đồng thời trên nhiều thực thi (execution / 실행) resources.

Một vòng lặp sự kiện (event loop / 이벤트 루프) single-thread vẫn concurrent nếu nó multiplex nhiều I/O tasks. Một CPU 8 cores có thể chạy 8 threads song song, nhưng nếu tất cả chờ cùng khóa (lock / 잠금) thì parallelism hữu ích gần bằng zero.

Phân biệt này quan trọng vì async có thể tăng utilization mà không tạo thêm CPU compute sức chứa (capacity / 용량).

## 2. bất biến (invariant / 불변식) phải được viết trước synchronization thành phần nguyên thủy (primitive / 기본 요소)

Giả sử hai threads cùng cập nhật account balance. Câu hỏi đầu tiên không phải “dùng mutex hay atomic?”, mà là bất biến (invariant / 불변식):

```text
balance mới phải được tính từ một state hợp lệ duy nhất
không được mất update
không được quan sát transaction ở trạng thái nửa hoàn thành nếu contract cấm
```

Sau khi biết bất biến (invariant / 불변식), mới chọn thành phần nguyên thủy (primitive / 기본 요소) đủ mạnh. Một atomic integer có thể đủ cho counter; một multi-field bất biến (invariant / 불변식) có thể cần khóa (lock / 잠금) hoặc giao thức (protocol / 프로토콜) khác.

Dùng thành phần nguyên thủy (primitive / 기본 요소) mạnh mà không hiểu bất biến (invariant / 불변식) dễ tạo over-synchronization; dùng thành phần nguyên thủy (primitive / 기본 요소) yếu dễ tạo race tinh vi.

## 3. Shared-memory threading: flexibility đổi lấy proof burden

OS/thời gian chạy (runtime / 런타임) threads thường chia sẻ vùng nhớ động (heap / 힙) và có ngăn xếp (stack / 스택) riêng. dùng chung (shared / 공유) mutable trạng thái (state / 상태) tạo giao tiếp rất rẻ nhưng tính đúng đắn (correctness / 정확성) khó vì mọi interleaving hợp lệ phải được xét.

Mutex tạo **mutual exclusion** cho trọng yếu (critical / 중요) section. điều kiện (condition / 조건) variable cho luồng thực thi (thread / 스레드) chờ predicate thay vì busy-spin. Atomics cung cấp read-modify-write và memory-order ngữ nghĩa (semantics / 의미론).

Khóa (lock / 잠금) không “bảo vệ variable” theo phép màu. Nó bảo vệ bất biến (invariant / 불변식) nếu mọi truy cập (access / 접근) liên quan đều tuân cùng khóa (lock / 잠금) discipline.

## 4. Race điều kiện (condition / 조건) và dữ liệu (data / 데이터) race khác nhau

**dữ liệu (data / 데이터) race** thường có nghĩa hai thực thi (execution / 실행) contexts truy cập cùng bộ nhớ (memory / 메모리) location, ít nhất một bên ghi (write / 쓰기) và không có synchronization hợp lệ theo ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델).

**Race điều kiện (condition / 조건)** rộng hơn: kết quả phụ thuộc timing/thứ tự (order / 순서) theo cách làm vi phạm lô-gic (logic / 논리) dù không có dữ liệu (data / 데이터) race ở memory-level.

Ví dụ hai requests đều làm:

```text
if stock > 0:
    reserve()
```

Mỗi truy cập (access / 접근) có thể thread-safe riêng, nhưng check-then-act vẫn có logical race nếu bất biến (invariant / 불변식) “không bán vượt stock” không được giữ atomically.

Vì vậy “race detector không báo” không chứng minh concurrent giao thức (protocol / 프로토콜) đúng.

## 5. Happens-before là nền tảng lập luận (reasoning / 추론) cho dùng chung (shared / 공유) bộ nhớ (memory / 메모리)

Trình biên dịch (compiler / 컴파일러) và CPU được phép reorder nhiều operations miễn không phá observable ngữ nghĩa (semantics / 의미론) theo đặc tả hợp đồng (contract / 계약). Vì vậy nguồn (source / 소스) thứ tự (order / 순서) một mình không đủ.

Ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) định nghĩa synchronization actions và quan hệ (relation / 관계) như **happens-before**. Nếu writer publish trạng thái (state / 상태) qua bản phát hành (release / 릴리스)/unlock/volatile hành động (action / 동작) và reader acquire/read tương ứng, software có thứ tự (ordering / 순서)/visibility guarantee để lập luận (reasoning / 추론).

Không có synchronization edge, việc “kiểm thử (test / 테스트) nhiều lần đều thấy đúng” không phải proof.

Đường xuyên tầng đầy đủ nằm ở [CPU cache → memory ordering → language memory model → concurrency bug](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

## 6. Atomicity, visibility và thứ tự (ordering / 순서) phải tách riêng

Ba thuộc tính (property / 속성) hay bị trộn:

```text
Atomicity  -> operation có thể bị interleave thành state trung gian/lost update không?
Visibility -> write có được reader hợp lệ quan sát không?
Ordering   -> các operations liên quan được phép xuất hiện theo thứ tự nào?
```

Một `volatile` trường dữ liệu (field / 필드) trong Java có visibility/thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론) nhưng `count++` vẫn không phải atomic read-modify-write. Một CAS atomic có thể bảo vệ một chuyển tiếp (transition / 전이) nhưng giao thức (protocol / 프로토콜) nhiều fields vẫn cần thứ tự (ordering / 순서) đúng.

Rà soát (review / 검토) concurrent mã (code / 코드) nên kiểm tra cả ba, không chỉ “có dùng atomic không?”.

## 7. khóa (lock / 잠금) tính đúng đắn (correctness / 정확성) có nhiều dạng thất bại (failure mode / 실패 모드) hơn deadlock

Mutex giải mutual exclusion nhưng tạo thêm risks:

```text
contention -> throughput/tail latency xấu
lock convoy -> nhiều threads nối đuôi một slow holder
priority inversion -> task quan trọng chờ holder ít priority
starvation -> một participant hiếm khi lấy được lock
deadlock -> wait-for cycle không thể tiến triển
```

Khóa (lock / 잠금) phạm vi (scope / 범위) quá lớn giữ tính đúng đắn (correctness / 정확성) dễ hơn nhưng giảm parallelism. khóa (lock / 잠금) phạm vi (scope / 범위) quá nhỏ tăng interleavings cần chứng minh.

Hiệu năng (performance / 성능) pressure không cho phép bỏ bất biến (invariant / 불변식); nó buộc giao thức (protocol / 프로토콜) tốt hơn hoặc partition trạng thái (state / 상태) hợp lý hơn.

## 8. Lock-free không có nghĩa không chờ

Lock-free algorithms thường dùng compare-and-swap và đảm bảo system-wide progress theo định nghĩa. Một luồng thực thi (thread / 스레드) cụ thể vẫn có thể thử lại (retry / 재시도)/starve. Wait-free guarantee mạnh hơn vì mỗi thao tác (operation / 연산) có bounded progress theo mô hình (model / 모델).

Tính đúng đắn (correctness / 정확성) còn cần linearization điểm (point / 지점), bộ nhớ (memory / 메모리) thứ tự (ordering / 순서), ABA handling và bộ nhớ (memory / 메모리) reclamation. CAS thành công không tự chứng minh đối tượng (object / 객체) thời gian tồn tại (lifetime / 수명) hoặc toàn giao thức (protocol / 프로토콜) đúng.

Lock-free đổi blocking rủi ro (risk / 위험) lấy proof độ phức tạp (complexity / 복잡도); nó không phải tối ưu hóa (optimization / 최적화) mặc định.

## 9. Actor mô hình (model / 모델): isolate mutable trạng thái (state / 상태), nhưng mailbox là hàng đợi (queue / 큐)

**Actor mô hình (model / 모델)** gắn private mutable trạng thái (state / 상태) với actor và communication bằng message. Nếu actor xử lý một message tại một thời điểm, nhiều shared-memory race biến mất structurally.

Nhưng độ phức tạp (complexity / 복잡도) chuyển sang message ngữ nghĩa (semantics / 의미론):

```text
message có thể reorder không?
mailbox có bounded không?
actor crash khi đang xử lý thì message được retry không?
duplicate có thể xuất hiện không?
state transition có idempotent không?
```

Mailbox unbounded có thể biến burst thành bộ nhớ (memory / 메모리) growth và độ trễ (latency / 지연 시간) vô hạn. Actor isolation không thay backpressure.

## 10. CSP/channels: communication thành phần nguyên thủy (primitive / 기본 요소) đồng thời là flow-control thành phần nguyên thủy (primitive / 기본 요소)

Communicating Sequential Processes nhấn mạnh các processes giao tiếp qua channels. Unbuffered channel thường tạo rendezvous: sender và receiver đồng bộ tại communication điểm (point / 지점). Buffered channel tạo hàng đợi (queue / 큐).

Channel sức chứa (capacity / 용량) vì vậy là kiến trúc (architecture / 아키텍처) quyết định (decision / 결정):

```text
capacity = 0/small -> backpressure mạnh, producer dễ bị chặn
capacity lớn       -> hấp thụ burst, nhưng tăng queued state và latency debt
```

“Không share bộ nhớ (memory / 메모리); communicate” không loại bỏ overload. hàng đợi (queue / 큐) chỉ chuyển vào channel/mailbox.

## 11. Async/await thay thực thi (execution / 실행) biểu diễn (representation / 표현), không xóa tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건)

Async tác vụ (task / 작업) cho phép suspension khi chờ I/O thay vì giữ OS luồng thực thi (thread / 스레드) blocked, tùy thời gian chạy (runtime / 런타임). Điều này rất hữu ích khi có nhiều I/O waits.

Nhưng async CPU-bound công việc (work / 작업) vẫn cần CPU. Nếu callback/continuation khối (block / 블록) vòng lặp sự kiện (event loop / 이벤트 루프) bằng compute dài, hàng nghìn sockets có thể bị stall cùng lúc.

Thời gian chạy (runtime / 런타임) có worker pool, timer hàng đợi (queue / 큐), I/O completion cơ chế (mechanism / 메커니즘) và tác vụ (task / 작업) scheduler; tất cả đều có sức chứa (capacity / 용량). “Async” là programming mô hình (model / 모델), không phải infinite tính đồng thời (concurrency / 동시성).

## 12. Structured tính đồng thời (concurrency / 동시성) giữ thời gian tồn tại (lifetime / 수명) bất biến (invariant / 불변식) của tasks

Fire-and-forget tác vụ (task / 작업) dễ leak thời gian tồn tại (lifetime / 수명): parent yêu cầu (request / 요청) đã kết thúc nhưng child vẫn giữ liên kết (connection / 연결), khóa (lock / 잠금) hoặc continue side tác động (effect / 효과).

**Structured tính đồng thời (concurrency / 동시성)** cố giữ bất biến (invariant / 불변식):

> Child tasks thuộc một phạm vi (scope / 범위); phạm vi (scope / 범위) không hoàn tất cho tới khi children hoàn tất/cancel theo chính sách (policy / 정책); errors và cancellation được propagate có cấu trúc.

Điều này làm tác vụ (task / 작업) thời gian tồn tại (lifetime / 수명) giống tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) hơn, giảm orphan công việc (work / 작업) và giúp deadline/cancellation đi xuyên lời gọi (call / 호출) cây (tree / 트리).

Đọc [coroutines, async runtime và structured concurrency](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md).

## 13. Cancellation là một thất bại (failure / 실패) injection vào điều khiển (control / 제어) luồng (flow / 흐름)

Tác vụ (task / 작업) có thể bị cancel tại suspension điểm (point / 지점) trong lúc đã acquire một tài nguyên (resource / 자원) hoặc thực hiện nửa side tác động (effect / 효과).

Cancellation-safe mã (code / 코드) cần biết:

```text
state nào đã được mutate?
cleanup có chạy chắc không?
operation có idempotent/restartable không?
transaction có rollback không?
lock/resource có release không?
```

RAII, `finally`, defer-style cleanup và structured thời gian tồn tại (lifetime / 수명) giúp giữ bất biến (invariant / 불변식). Cancellation không nên được coi như `return` bình thường.

## 14. quyền sở hữu (ownership / 소유권) đưa một phần tính đồng thời (concurrency / 동시성) proof vào hệ kiểu (type system / 타입 시스템)

Quyền sở hữu (ownership / 소유권)/borrowing giới hạn aliasing và mutable truy cập (access / 접근). Nếu mutable trạng thái (state / 상태) không thể được unrestricted-share giữa threads, một lớp (class / 클래스) dữ liệu (data / 데이터) race bị loại trước thời gian chạy (runtime / 런타임).

Nhưng quyền sở hữu (ownership / 소유권) không loại deadlock, logical race hoặc phân tán (distributed / 분산) inconsistency. Static proof chỉ mạnh trong ranh giới (boundary / 경계) mà hệ kiểu (type system / 타입 시스템) kiểm soát; FFI/unsafe mã (code / 코드) mở lại các giả định (assumptions / 가정들).

Đọc [Ownership, borrowing và memory safety](../../04_programming_languages/advanced/02_ownership_borrowing_linear_types_and_memory_safety.md).

## 15. Immutability giảm state-space cần lập luận (reasoning / 추론)

Immutable dữ liệu (data / 데이터) có thể share an toàn hơn vì readers không tranh mutation. Functional-style updates tạo giá trị (value / 값) mới thay vì modify dùng chung (shared / 공유) đối tượng (object / 객체).

Sự đánh đổi (trade-off / 트레이드오프) có thể là allocation/copying, GC pressure hoặc need persistent dữ liệu (data / 데이터) structures. Nhưng lợi ích lớn nhất không phải “functional mã (code / 코드) đẹp”; đó là giảm số interleavings có thể thay đổi bất biến (invariant / 불변식).

Tính đồng thời (concurrency / 동시성) thiết kế (design / 설계) tốt thường **partition mutable trạng thái (state / 상태)** trước khi cố synchronize mọi thứ.

## 16. bộ nhớ (memory / 메모리) an toàn (safety / 안전) và tính đồng thời (concurrency / 동시성) an toàn (safety / 안전) giao nhau nhưng không đồng nhất

Bộ nhớ (memory / 메모리) an toàn (safety / 안전) ngăn use-after-free, invalid pointer/bounds truy cập (access / 접근) theo mô hình (model / 모델). tính đồng thời (concurrency / 동시성) an toàn (safety / 안전) quan tâm race/thứ tự (order / 순서)/progress. Một GC ngôn ngữ (language / 언어) có thể memory-safe ở vùng nhớ động (heap / 힙) thời gian tồn tại (lifetime / 수명) nhưng vẫn có dữ liệu (data / 데이터) race/logical race. Một quyền sở hữu (ownership / 소유권) ngôn ngữ (language / 언어) có thể ngăn nhiều alias/thời gian tồn tại (lifetime / 수명) bugs nhưng vẫn deadlock.

FFI/bản địa (native / 네이티브) extension, unsafe khối (block / 블록) và shared-memory ranh giới (boundary / 경계) là nơi guarantee có thể suy yếu.

Bảo mật (security / 보안) cũng liên quan: memory-unsafe race/use-after-free có thể trở thành vulnerability, nhưng logical authorization race có thể xảy ra trong memory-safe ngôn ngữ (language / 언어).

## 17. hiệu năng (performance / 성능) pressure thay đổi mô hình (model / 모델) nào phù hợp

Threads có context-switch/ngăn xếp (stack / 스택) chi phí (cost / 비용) nhưng rất tự nhiên cho blocking mã (code / 코드). Async tasks quy mô (scale / 규모) số I/O waits tốt hơn nhưng thời gian chạy (runtime / 런타임) scheduling/debugging phức tạp. Actors isolate trạng thái (state / 상태) nhưng mailbox/message serialization tạo overhead. Atomics tránh kernel blocking trong một số paths nhưng cache-line contention có thể giới hạn scalability.

Không có mô hình (model / 모델) nhanh nhất universal. Chọn theo tải công việc (workload / 워크로드) và bất biến (invariant / 불변식):

```text
CPU-bound independent work -> parallel workers/data parallelism
I/O-heavy high concurrency -> async/evented model có thể hợp lý
state ownership rõ          -> actor/partitioning có thể giảm sharing
low-level shared counters   -> atomics nếu invariant thật sự local
complex multi-field state   -> lock/transaction thường dễ proof hơn
```

## 18. bằng chứng vận hành (production evidence / 운영 증거) cho tính đồng thời (concurrency / 동시성) bug và contention

Tính đúng đắn (correctness / 정확성) bằng chứng (evidence / 증거) gồm race detector/sanitizer khi ecosystem hỗ trợ, stress testing, bất biến (invariant / 불변식) assertion và minimal reproducer. bằng chứng hiệu năng (performance evidence / 성능 증거) gồm luồng thực thi (thread / 스레드) dump, khóa (lock / 잠금)/park wait, on/off-CPU profiler, scheduler delay, run hàng đợi (queue / 큐), ngữ cảnh (context / 맥락) switches, cache-line/coherence counters và NUMA placement khi cần.

Một deadlock cần wait-for đồ thị (graph / 그래프)/ngăn xếp (stack / 스택) bằng chứng (evidence / 증거). Một false-sharing issue cần bộ nhớ đệm (cache / 캐시)/coherence bằng chứng (evidence / 증거). Một event-loop stall cần long-task/on-CPU bằng chứng (evidence / 증거). Cùng symptom “yêu cầu (request / 요청) treo” có thể có cơ chế (mechanism / 메커니즘) hoàn toàn khác.

## 19. thất bại (failure / 실패) ở tầng thấp hơn có thể quyết định hành vi (behavior / 동작)

Tính đồng thời (concurrency / 동시성) lớp trừu tượng (abstraction / 추상화) leak khi lower tầng (layer / 계층) trở thành decisive:

```text
language lock contention -> OS futex/scheduler behavior
atomic hot spot           -> cache-coherence ownership transfer
async latency             -> event loop + OS I/O completion + CPU scheduling
shared object performance -> NUMA/cache-line placement
safe publication          -> language memory model mapped xuống ISA ordering
```

Ta không cần gỡ lỗi (debug / 디버그) mọi bug bằng assembly, nhưng phải biết khi nào lớp trừu tượng (abstraction / 추상화) hiện tại không giải thích được bằng chứng (evidence / 증거).

## 20. Mô hình tư duy

> tính đồng thời (concurrency / 동시성) mô hình (model / 모델) là giao thức (protocol / 프로토콜) về **quyền sở hữu (ownership / 소유권), communication, thứ tự (ordering / 순서), thời gian tồn tại (lifetime / 수명) và progress**. Threads/locks dùng trạng thái dùng chung (shared state / 공유 상태) trực tiếp; actors/channels di chuyển communication sang message/hàng đợi (queue / 큐); async tách logical tasks khỏi blocking OS threads; quyền sở hữu (ownership / 소유권) đưa một phần proof vào hệ kiểu (type system / 타입 시스템). Không mô hình (model / 모델) nào xóa tính đồng thời (concurrency / 동시성) độ phức tạp (complexity / 복잡도)—mỗi mô hình (model / 모델) chuyển bất biến (invariant / 불변식) và dạng thất bại (failure mode / 실패 모드) sang ranh giới (boundary / 경계) khác.

## Những hiểu nhầm thường gặp

**“Không dùng threads thì không có race.”** Actors/messages vẫn có logical race, duplicate, reorder và stale trạng thái (state / 상태).

**“Async nhanh hơn sync.”** Async chủ yếu cải thiện utilization khi có waits; CPU-bound công việc (work / 작업) vẫn bị CPU sức chứa (capacity / 용량) giới hạn.

**“Atomic nghĩa toàn thao tác (operation / 연산) nghiệp vụ (business / 비즈니스) đã atomic.”** Atomic thành phần nguyên thủy (primitive / 기본 요소) chỉ bảo vệ chuyển tiếp (transition / 전이) mà thành phần nguyên thủy (primitive / 기본 요소) đó định nghĩa.

**“Lock-free luôn nhanh hơn khóa (lock / 잠금).”** Contention, retries, coherence và reclamation có thể làm lock-free tệ hơn.

## Kết nối

Đọc cùng [OS concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [Advanced memory ordering](../../02_computer_architecture/advanced/00_memory_consistency_cache_coherence_and_ordering.md), [Ownership](../../04_programming_languages/advanced/02_ownership_borrowing_linear_types_and_memory_safety.md), [Structured concurrency](../../04_programming_languages/advanced/07_coroutines_continuations_async_runtimes_and_structured_concurrency.md), [Queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md) và [Correctness path xuyên tầng](../../90_connections/advanced/02_correctness_path_language_os_cpu_memory_ordering.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 language semantics and execution models](./00_language_semantics_and_execution_models.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
