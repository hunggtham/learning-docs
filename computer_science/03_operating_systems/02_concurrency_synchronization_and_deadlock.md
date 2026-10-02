# Tính đồng thời (concurrency / 동시성), synchronization và deadlock

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**. Route đi từ interleaving/race → atomicity và mutual exclusion → ordering/condition variables → deadlock/livelock/starvation, để correctness và progress được kiểm tra cùng nhau.

Tính đồng thời (concurrency / 동시성) bugs khó vì hành vi (behavior / 동작) phụ thuộc timing/interleaving mà mã nguồn (source code / 소스 코드) tuyến tính không thể hiện rõ. Hai threads cùng đúng khi chạy riêng có thể sai khi share mutable trạng thái (state / 상태).

## Race điều kiện (condition / 조건) và dữ liệu (data / 데이터) race

Race điều kiện (condition / 조건) là tính đúng đắn (correctness / 정확성) phụ thuộc relative timing. dữ liệu (data / 데이터) race theo nhiều ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) các mô hình (models / 모델들) là concurrent conflicting accesses tới cùng location, ít nhất một ghi (write / 쓰기), không có synchronization phù hợp.

Ví dụ `counter++` không nhất thiết atomic. Nó có thể là tải (load / 로드) → add → store. Hai threads cùng tải (load / 로드) 10, cùng compute 11, cùng store 11; một increment bị mất.

> **Chuyển mạch:** Trong **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Race điều kiện (condition / 조건) và dữ liệu (data / 데이터) race** nêu điều cần giải thích; **Trọng yếu (critical / 중요) section và mutual exclusion** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Atomic operations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Trọng yếu (critical / 중요) section và mutual exclusion

Trọng yếu (critical / 중요) section truy cập dùng chung (shared / 공유) bất biến (invariant / 불변식) cần serialize. Mutex/khóa (lock / 잠금) bảo đảm một holder tại một thời điểm. khóa (lock / 잠금) không “bảo vệ variable” tự động; tính đúng đắn (correctness / 정확성) đến từ discipline rằng mọi accesses liên quan bất biến (invariant / 불변식) dùng cùng synchronization giao thức (protocol / 프로토콜).

Coarse-grained khóa (lock / 잠금) đơn giản nhưng contention cao. Fine-grained locks tăng parallelism nhưng phức tạp và tăng deadlock rủi ro (risk / 위험).

> **Chuyển mạch:** Critical section/mutual exclusion bảo vệ invariant; atomic operations rút ngắn boundary, còn memory ordering/happens-before xác định visibility giữa threads.

## Atomic operations

CPU cung cấp atomic read-modify-write như compare-and-swap (CAS). Atomicity bảo đảm thao tác (operation / 연산) không quan sát intermediate trạng thái (state / 상태). Lock-free algorithms dùng atomics để coordinate mà không mutex blocking, nhưng lập luận (reasoning / 추론) bộ nhớ (memory / 메모리) thứ tự (ordering / 순서), ABA bài toán (problem / 문제) và reclamation rất khó.

Atomic không đồng nghĩa toàn giao dịch (transaction / 트랜잭션) lô-gic (logic / 논리) atomic. Hai atomic variables riêng không tự bảo đảm bất biến (invariant / 불변식) liên-variable.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và happens-before** tiếp nhận điểm tựa từ **Atomic operations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Điều kiện (condition / 조건) variables, semaphores và monitors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và happens-before

Trình biên dịch (compiler / 컴파일러) và CPU được phép reorder operations trong giới hạn observable single-thread ngữ nghĩa (semantics / 의미론). Multithread tính đúng đắn (correctness / 정확성) không thể giả định nguồn (source / 소스) thứ tự (order / 순서) luôn visible cùng thứ tự ở cốt lõi (core / 핵심) khác.

Ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) định nghĩa happens-before relationships qua locks, volatile/atomic operations, luồng thực thi (thread / 스레드) start/phép nối (join / 조인)... Nếu ghi (write / 쓰기) happens-before read, read được guarantee visibility theo mô hình (model / 모델).

Đây là tầng trên bộ nhớ đệm (cache / 캐시) coherence: coherence không tự tạo program thứ tự (ordering / 순서) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Điều kiện (condition / 조건) variables, semaphores và monitors** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) thứ tự (ordering / 순서) và happens-before** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Deadlock** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Điều kiện (condition / 조건) variables, semaphores và monitors

Điều kiện (condition / 조건) variable cho luồng thực thi (thread / 스레드) ngủ tới khi predicate trên trạng thái dùng chung (shared state / 공유 상태) có thể thay đổi; luôn re-check predicate trong vòng lặp (loop / 루프) vì wakeup/spurious wakeup/interleavings.

Semaphore giữ count permits, dùng giới hạn tính đồng thời (concurrency / 동시성) hoặc signaling. nhị phân (binary / 이진) semaphore giống mutex ở surface nhưng quyền sở hữu (ownership / 소유권) ngữ nghĩa (semantics / 의미론) có thể khác.

Monitor kết hợp mutual exclusion với điều kiện (condition / 조건) synchronization trong một lớp trừu tượng (abstraction / 추상화); Java `synchronized`/wait-notify là family idea.

> **Chuyển mạch:** Ở chặng này của **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Deadlock** tiếp nhận điểm tựa từ **Điều kiện (condition / 조건) variables, semaphores và monitors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Livelock và starvation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Deadlock

Deadlock (교착 상태) xảy ra khi tasks chờ nhau theo cycle và không tác vụ (task / 작업) nào tiến được. Coffman conditions kinh điển: mutual exclusion, hold-and-wait, no preemption, circular wait. Phá ít nhất một điều kiện có thể ngăn lớp (class / 클래스) deadlock.

Ví dụ luồng thực thi (thread / 스레드) A giữ khóa (lock / 잠금) X chờ Y; B giữ Y chờ X. toàn cục (global / 전역) khóa (lock / 잠금) thứ tự (ordering / 순서) — luôn lấy X trước Y — phá circular wait.

Deadlock không chỉ locks. phân tán (distributed / 분산) services có thể chờ RPC cycles; luồng thực thi (thread / 스레드) pools có tác vụ (task / 작업) chờ future queued vào chính saturated pool.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Livelock và starvation** tiếp nhận điểm tựa từ **Deadlock** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Immutability và message passing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Livelock và starvation

Livelock: tasks vẫn hoạt động/thay trạng thái (state / 상태) nhưng liên tục nhường/thử lại (retry / 재시도) khiến không progress. Starvation: một tác vụ (task / 작업) không được tài nguyên (resource / 자원) đủ lâu vì scheduling/khóa (lock / 잠금) unfairness.

Correct concurrent hệ thống (system / 시스템) cần an toàn (safety / 안전) (“không xảy ra điều xấu”) và liveness (“điều tốt cuối cùng xảy ra”).

> **Chuyển mạch:** Trong **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Immutability và message passing** tiếp nhận điểm tựa từ **Livelock và starvation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Immutability và message passing

Cách tốt để giảm shared-state synchronization là giảm mutable sharing. Immutable values có thể share an toàn hơn. Actor/message-passing mô hình (model / 모델) isolate trạng thái (state / 상태) và communicate bằng messages, chuyển độ phức tạp (complexity / 복잡도) từ dùng chung (shared / 공유) bộ nhớ (memory / 메모리) sang thứ tự (ordering / 순서), mailbox và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론).

Không có free lunch: phân tán (distributed / 분산)/message các hệ thống (systems / 시스템들) cần xử lý duplicate, thử lại (retry / 재시도) và partial thất bại (failure / 실패).

> **Chuyển mạch:** Ở chặng này của **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Immutability và message passing** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Concurrent tính đúng đắn (correctness / 정확성) là lập luận (reasoning / 추론) về **trạng thái dùng chung (shared state / 공유 상태) + atomic boundaries + thứ tự (ordering / 순서) + progress**. Hỏi ai có thể truy cập (access / 접근) trạng thái (state / 상태) này, thao tác (operation / 연산) nào phải indivisible, visibility được bảo đảm bằng gì, và có cycle chờ nào không.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“volatile làm mọi thao tác (operation / 연산) thread-safe.”** Volatile/atomic visibility/thứ tự (order / 순서) guarantee không biến multi-step bất biến (invariant / 불변식) thành giao dịch (transaction / 트랜잭션).

**“Không dùng khóa (lock / 잠금) thì không deadlock.”** tài nguyên (resource / 자원) waits, futures, channels và phân tán (distributed / 분산) calls vẫn có wait cycles.

**“Thread-safe collection làm toàn workflow thread-safe.”** chuỗi (sequence / 시퀀스) check-then-act trên nhiều calls vẫn có race nếu không có higher-level atomicity.

> **Chuyển mạch:** Trong **Tính đồng thời (concurrency / 동시성), synchronization và deadlock**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

[Transactions](../05_data_databases/02_transactions_acid_and_concurrency_control.md) giải cùng bài toán atomicity/isolation ở cơ sở dữ liệu (database / 데이터베이스). [Distributed systems](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) làm thứ tự (ordering / 순서) khó hơn vì không có dùng chung (shared / 공유) clock/bộ nhớ (memory / 메모리). Hardware side nằm ở [cache coherence](../02_computer_architecture/02_memory_hierarchy_and_cache.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
