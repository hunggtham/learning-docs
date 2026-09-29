# Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)

> **Mạch đọc:** Đặt **tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Shared-memory threading** sang **bộ nhớ (memory / 메모리) mô hình (model / 모델)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Tính đồng thời (concurrency / 동시성) không chỉ là “dùng nhiều threads”. Programming languages/runtimes cung cấp những các mô hình (models / 모델들) khác nhau để biểu diễn công việc (work / 작업) xảy ra đồng thời và để kiểm soát trạng thái dùng chung (shared state / 공유 상태): threads + locks, actors, CSP/channels, async tasks, immutable dữ liệu (data / 데이터), quyền sở hữu (ownership / 소유권) hoặc transactional bộ nhớ (memory / 메모리).

## Shared-memory threading

Nhiều languages map threads gần với OS threads. Threads chia sẻ vùng nhớ động (heap / 힙) và có private stacks. mô hình (model / 모델) này linh hoạt nhưng race conditions xuất hiện khi nhiều threads truy cập (access / 접근) mutable trạng thái (state / 상태) mà synchronization không đúng.

Mutex bảo vệ trọng yếu (critical / 중요) section; điều kiện (condition / 조건) variable chờ predicate; atomics cung cấp operations với memory-order ngữ nghĩa (semantics / 의미론).

Điểm khó là tính đúng đắn (correctness / 정확성) phụ thuộc **happens-before quan hệ (relation / 관계)**, không chỉ source-code thứ tự (order / 순서).


> **Chuyển mạch:** Từ **Shared-memory threading**, ta sang **bộ nhớ (memory / 메모리) mô hình (model / 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bộ nhớ (memory / 메모리) mô hình (model / 모델)

Trình biên dịch (compiler / 컴파일러) và CPU có thể reorder operations nếu single-thread ngữ nghĩa (semantics / 의미론) không đổi. Trong concurrent program, ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) xác định observations nào hợp lệ và synchronization nào tạo thứ tự (ordering / 순서) guarantees.

`volatile` có nghĩa khác nhau theo ngôn ngữ (language / 언어). Trong Java, volatile read/ghi (write / 쓰기) có visibility/thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론); trong C/C++, `volatile` chủ yếu liên quan observable accesses và không thay thế atomics cho dữ liệu (data / 데이터) races.

Đây là lý do từ khóa (keyword / 키워드) giống nhau không nên được suy luận qua languages.


> **Chuyển mạch:** Từ **bộ nhớ (memory / 메모리) mô hình (model / 모델)**, ta sang **Actors: isolate mutable trạng thái (state / 상태)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Actors: isolate mutable trạng thái (state / 상태)

Actor mô hình (model / 모델) tổ chức hệ thống (system / 시스템) thành actors có private trạng thái (state / 상태) và giao tiếp bằng messages. Mỗi actor xử lý messages tuần tự theo mailbox mô hình (model / 모델), giảm shared-memory races.

Nhưng phân tán (distributed / 분산) actors vẫn có message thứ tự (ordering / 순서), thất bại (failure / 실패), duplication và mailbox overload. Actor mô hình (model / 모델) di chuyển độ phức tạp (complexity / 복잡도), không xóa độ phức tạp (complexity / 복잡도).


> **Chuyển mạch:** Từ **Actors: isolate mutable trạng thái (state / 상태)**, ta sang **CSP và channels** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## CSP và channels

Communicating Sequential Processes (CSP) nhấn mạnh processes giao tiếp qua channels. Go goroutines/channels lấy cảm hứng từ family ideas này.

Unbuffered channel có thể đồng bộ sender/receiver; buffered channel thêm hàng đợi (queue / 큐). Channel sức chứa (capacity / 용량) vì vậy trở thành backpressure điều khiển (control / 제어) chứ không chỉ cú pháp (syntax / 문법) communication.


> **Chuyển mạch:** Từ **CSP và channels**, ta sang **Async/await và structured tính đồng thời (concurrency / 동시성)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Async/await và structured tính đồng thời (concurrency / 동시성)

Async tác vụ (task / 작업) thường phù hợp I/O tính đồng thời (concurrency / 동시성). `await` biểu diễn suspension điểm (point / 지점) thay vì khối (block / 블록) OS luồng thực thi (thread / 스레드), tùy thời gian chạy (runtime / 런타임).

Structured tính đồng thời (concurrency / 동시성) cố gắn thời gian tồn tại (lifetime / 수명) child tasks vào lexical/tác vụ (task / 작업) phạm vi (scope / 범위): parent không silently kết thúc trong khi children bị bỏ quên. Điều này làm cancellation, lan truyền lỗi (error propagation / 오류 전파) và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) dễ lập luận (reasoning / 추론) hơn.


> **Chuyển mạch:** Từ **Async/await và structured tính đồng thời (concurrency / 동시성)**, ta sang **quyền sở hữu (ownership / 소유권) và borrowing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Quyền sở hữu (ownership / 소유권) và borrowing

Quyền sở hữu (ownership / 소유권) mô hình (model / 모델) như Rust giới hạn aliasing/mutation bằng compile-time rules. Một giá trị (value / 값) có đơn vị sở hữu (owner / 오너); borrowing tạo references với các ràng buộc (constraints / 제약조건들). Mục tiêu là ngăn use-after-free, double free và nhiều dữ liệu (data / 데이터) races trước thời gian chạy (runtime / 런타임) mà không cần garbage collector cho mọi allocation.

Điều quan trọng không phải học cú pháp (syntax / 문법) Rust ở đây mà thấy quyền sở hữu (ownership / 소유권) là một **static giao thức (protocol / 프로토콜) cho tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) và aliasing**.


> **Chuyển mạch:** Từ **quyền sở hữu (ownership / 소유권) và borrowing**, ta sang **bộ nhớ (memory / 메모리) an toàn (safety / 안전) và kiểu (type / 타입) an toàn (safety / 안전)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bộ nhớ (memory / 메모리) an toàn (safety / 안전) và kiểu (type / 타입) an toàn (safety / 안전)

Bộ nhớ (memory / 메모리) an toàn (safety / 안전) nghĩa program không truy cập (access / 접근) bộ nhớ (memory / 메모리) ngoài valid thời gian tồn tại (lifetime / 수명)/bounds theo mô hình (model / 모델). kiểu (type / 타입) an toàn (safety / 안전) là concept rộng hơn về invalid operations theo hệ kiểu (type system / 타입 시스템). Một ngôn ngữ (language / 언어) có thể type-safe ở mức high-level nhưng FFI/bản địa (native / 네이티브) extension mở unsafe ranh giới (boundary / 경계).

Bounds checks, GC, quyền sở hữu (ownership / 소유권), safe references và sandboxing là các mechanisms khác nhau hướng tới bộ nhớ (memory / 메모리) an toàn (safety / 안전).


> **Chuyển mạch:** Từ **bộ nhớ (memory / 메모리) an toàn (safety / 안전) và kiểu (type / 타입) an toàn (safety / 안전)**, ta sang **Cancellation là control-flow cross-cutting** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cancellation là control-flow cross-cutting

Concurrent tác vụ (task / 작업) có thể bị cancel trong khi giữ khóa (lock / 잠금), giao dịch (transaction / 트랜잭션) hoặc tệp (file / 파일). Cancellation-safe mã (code / 코드) phải định nghĩa cleanup và trạng thái (state / 상태) consistency.

Async cancellation vì vậy liên quan exception an toàn (safety / 안전) và tài nguyên (resource / 자원) management. RAII, `finally`, defer-style constructs và structured tính đồng thời (concurrency / 동시성) đều cố làm thời gian tồn tại (lifetime / 수명) tường minh (explicit / 명시적).


> **Chuyển mạch:** Từ **Cancellation là control-flow cross-cutting**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Không dùng threads thì không có race.”** Actor/message các hệ thống (systems / 시스템들) vẫn có logical races do message thứ tự (ordering / 순서); phân tán (distributed / 분산) các hệ thống (systems / 시스템들) còn có stale trạng thái (state / 상태).

**“Async nhanh hơn sync.”** Async cải thiện utilization dưới waiting workloads; CPU-bound công việc (work / 작업) vẫn cần compute resources.

**“GC làm program memory-safe hoàn toàn.”** GC ngăn nhiều thời gian tồn tại (lifetime / 수명) errors nhưng không ngăn out-of-bounds trong unsafe/bản địa (native / 네이티브) mã (code / 코드) hoặc logical tài nguyên (resource / 자원) leaks.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> tính đồng thời (concurrency / 동시성) mô hình (model / 모델) là bộ quy tắc trả lời ba câu: ai sở hữu trạng thái (state / 상태), những thực thi (execution / 실행) units giao tiếp thế nào, và thứ tự (ordering / 순서)/thời gian tồn tại (lifetime / 수명) nào được guarantee.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc cùng [OS concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [IPC](../03_operating_systems/06_ipc_signals_pipes_and_shared_memory.md), [type systems](./06_type_systems_generics_and_polymorphism.md) và [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 language semantics and execution models](./00_language_semantics_and_execution_models.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
