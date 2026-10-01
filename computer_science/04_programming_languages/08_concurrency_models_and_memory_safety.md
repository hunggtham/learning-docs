# Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Shared-memory threading** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bộ nhớ (memory / 메모리) mô hình (model / 모델)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Tính đồng thời (concurrency / 동시성) không chỉ là “dùng nhiều threads”. Programming languages/runtimes cung cấp những các mô hình (models / 모델들) khác nhau để biểu diễn công việc (work / 작업) xảy ra đồng thời và để kiểm soát trạng thái dùng chung (shared state / 공유 상태): threads + locks, actors, CSP/channels, async tasks, immutable dữ liệu (data / 데이터), quyền sở hữu (ownership / 소유권) hoặc transactional bộ nhớ (memory / 메모리).

## Shared-memory threading

Nhiều languages map threads gần với OS threads. Threads chia sẻ vùng nhớ động (heap / 힙) và có private stacks. mô hình (model / 모델) này linh hoạt nhưng race conditions xuất hiện khi nhiều threads truy cập (access / 접근) mutable trạng thái (state / 상태) mà synchronization không đúng.

Mutex bảo vệ trọng yếu (critical / 중요) section; điều kiện (condition / 조건) variable chờ predicate; atomics cung cấp operations với memory-order ngữ nghĩa (semantics / 의미론).

Điểm khó là tính đúng đắn (correctness / 정확성) phụ thuộc **happens-before quan hệ (relation / 관계)**, không chỉ source-code thứ tự (order / 순서).

> **Chuyển mạch:** Shared-memory threading cần memory model và synchronization để giữ invariant; actor model cô lập mutable state và giao tiếp bằng message, đổi race risk lấy coordination semantics.

## Bộ nhớ (memory / 메모리) mô hình (model / 모델)

Trình biên dịch (compiler / 컴파일러) và CPU có thể reorder operations nếu single-thread ngữ nghĩa (semantics / 의미론) không đổi. Trong concurrent program, ngôn ngữ (language / 언어) bộ nhớ (memory / 메모리) mô hình (model / 모델) xác định observations nào hợp lệ và synchronization nào tạo thứ tự (ordering / 순서) guarantees.

`volatile` có nghĩa khác nhau theo ngôn ngữ (language / 언어). Trong Java, volatile read/ghi (write / 쓰기) có visibility/thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론); trong C/C++, `volatile` chủ yếu liên quan observable accesses và không thay thế atomics cho dữ liệu (data / 데이터) races.

Đây là lý do từ khóa (keyword / 키워드) giống nhau không nên được suy luận qua languages.

> **Chuyển mạch:** Ở chặng này của **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Actors: isolate mutable trạng thái (state / 상태)** tiếp nhận điểm tựa từ **Bộ nhớ (memory / 메모리) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CSP và channels** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Actors: isolate mutable trạng thái (state / 상태)

Actor mô hình (model / 모델) tổ chức hệ thống (system / 시스템) thành actors có private trạng thái (state / 상태) và giao tiếp bằng messages. Mỗi actor xử lý messages tuần tự theo mailbox mô hình (model / 모델), giảm shared-memory races.

Nhưng phân tán (distributed / 분산) actors vẫn có message thứ tự (ordering / 순서), thất bại (failure / 실패), duplication và mailbox overload. Actor mô hình (model / 모델) di chuyển độ phức tạp (complexity / 복잡도), không xóa độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **CSP và channels** tiếp nhận điểm tựa từ **Actors: isolate mutable trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Async/await và structured tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CSP và channels

Communicating Sequential Processes (CSP) nhấn mạnh processes giao tiếp qua channels. Go goroutines/channels lấy cảm hứng từ family ideas này.

Unbuffered channel có thể đồng bộ sender/receiver; buffered channel thêm hàng đợi (queue / 큐). Channel sức chứa (capacity / 용량) vì vậy trở thành backpressure điều khiển (control / 제어) chứ không chỉ cú pháp (syntax / 문법) communication.

> **Chuyển mạch:** Trong **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Async/await và structured tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **CSP và channels** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quyền sở hữu (ownership / 소유권) và borrowing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Async/await và structured tính đồng thời (concurrency / 동시성)

Async tác vụ (task / 작업) thường phù hợp I/O tính đồng thời (concurrency / 동시성). `await` biểu diễn suspension điểm (point / 지점) thay vì khối (block / 블록) OS luồng thực thi (thread / 스레드), tùy thời gian chạy (runtime / 런타임).

Structured tính đồng thời (concurrency / 동시성) cố gắn thời gian tồn tại (lifetime / 수명) child tasks vào lexical/tác vụ (task / 작업) phạm vi (scope / 범위): parent không silently kết thúc trong khi children bị bỏ quên. Điều này làm cancellation, lan truyền lỗi (error propagation / 오류 전파) và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) dễ lập luận (reasoning / 추론) hơn.

> **Chuyển mạch:** Ở chặng này của **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, sau nội dung của **Async/await và structured tính đồng thời (concurrency / 동시성)**, **Quyền sở hữu (ownership / 소유권) và borrowing** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Bộ nhớ (memory / 메모리) an toàn (safety / 안전) và kiểu (type / 타입) an toàn (safety / 안전)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quyền sở hữu (ownership / 소유권) và borrowing

Quyền sở hữu (ownership / 소유권) mô hình (model / 모델) như Rust giới hạn aliasing/mutation bằng compile-time rules. Một giá trị (value / 값) có đơn vị sở hữu (owner / 오너); borrowing tạo references với các ràng buộc (constraints / 제약조건들). Mục tiêu là ngăn use-after-free, double free và nhiều dữ liệu (data / 데이터) races trước thời gian chạy (runtime / 런타임) mà không cần garbage collector cho mọi allocation.

Điều quan trọng không phải học cú pháp (syntax / 문법) Rust ở đây mà thấy quyền sở hữu (ownership / 소유권) là một **static giao thức (protocol / 프로토콜) cho tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) và aliasing**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Bộ nhớ (memory / 메모리) an toàn (safety / 안전) và kiểu (type / 타입) an toàn (safety / 안전)** tiếp nhận điểm tựa từ **Quyền sở hữu (ownership / 소유권) và borrowing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cancellation là control-flow cross-cutting** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bộ nhớ (memory / 메모리) an toàn (safety / 안전) và kiểu (type / 타입) an toàn (safety / 안전)

Bộ nhớ (memory / 메모리) an toàn (safety / 안전) nghĩa program không truy cập (access / 접근) bộ nhớ (memory / 메모리) ngoài valid thời gian tồn tại (lifetime / 수명)/bounds theo mô hình (model / 모델). kiểu (type / 타입) an toàn (safety / 안전) là concept rộng hơn về invalid operations theo hệ kiểu (type system / 타입 시스템). Một ngôn ngữ (language / 언어) có thể type-safe ở mức high-level nhưng FFI/bản địa (native / 네이티브) extension mở unsafe ranh giới (boundary / 경계).

Bounds checks, GC, quyền sở hữu (ownership / 소유권), safe references và sandboxing là các mechanisms khác nhau hướng tới bộ nhớ (memory / 메모리) an toàn (safety / 안전).

> **Chuyển mạch:** Trong **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Bộ nhớ (memory / 메모리) an toàn (safety / 안전) và kiểu (type / 타입) an toàn (safety / 안전)** xác định đầu vào; **Cancellation là control-flow cross-cutting** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cancellation là control-flow cross-cutting

Concurrent tác vụ (task / 작업) có thể bị cancel trong khi giữ khóa (lock / 잠금), giao dịch (transaction / 트랜잭션) hoặc tệp (file / 파일). Cancellation-safe mã (code / 코드) phải định nghĩa cleanup và trạng thái (state / 상태) consistency.

Async cancellation vì vậy liên quan exception an toàn (safety / 안전) và tài nguyên (resource / 자원) management. RAII, `finally`, defer-style constructs và structured tính đồng thời (concurrency / 동시성) đều cố làm thời gian tồn tại (lifetime / 수명) tường minh (explicit / 명시적).

> **Chuyển mạch:** Ở chặng này của **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Cancellation là control-flow cross-cutting** xác định đầu vào; **Dùng chung (common / 공통) Misconceptions** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Không dùng threads thì không có race.”** Actor/message các hệ thống (systems / 시스템들) vẫn có logical races do message thứ tự (ordering / 순서); phân tán (distributed / 분산) các hệ thống (systems / 시스템들) còn có stale trạng thái (state / 상태).

**“Async nhanh hơn sync.”** Async cải thiện utilization dưới waiting workloads; CPU-bound công việc (work / 작업) vẫn cần compute resources.

**“GC làm program memory-safe hoàn toàn.”** GC ngăn nhiều thời gian tồn tại (lifetime / 수명) errors nhưng không ngăn out-of-bounds trong unsafe/bản địa (native / 네이티브) mã (code / 코드) hoặc logical tài nguyên (resource / 자원) leaks.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> tính đồng thời (concurrency / 동시성) mô hình (model / 모델) là bộ quy tắc trả lời ba câu: ai sở hữu trạng thái (state / 상태), những thực thi (execution / 실행) units giao tiếp thế nào, và thứ tự (ordering / 순서)/thời gian tồn tại (lifetime / 수명) nào được guarantee.

> **Chuyển mạch:** Trong **Tính đồng thời (concurrency / 동시성) các mô hình (models / 모델들) và bộ nhớ (memory / 메모리) an toàn (safety / 안전)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [OS concurrency](../03_operating_systems/02_concurrency_synchronization_and_deadlock.md), [IPC](../03_operating_systems/06_ipc_signals_pipes_and_shared_memory.md), [type systems](./06_type_systems_generics_and_polymorphism.md) và [distributed consistency](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
