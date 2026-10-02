# Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**. Route đi từ address space/process → thread/context switch → scheduling/queues → latency, fairness và throughput, để hành vi ứng dụng được nối với cách CPU phân phối thời gian.

Một máy có thể chạy trình duyệt (browser / 브라우저), cơ sở dữ liệu (database / 데이터베이스), IDE và hàng trăm services dù số CPU cores hữu hạn. OS tạo illusion bằng cách multiplex thực thi (execution / 실행). Để lập luận (reasoning / 추론) đúng, cần tách tiến trình (process / 프로세스) — isolation/tài nguyên (resource / 자원) bộ chứa (container / 컨테이너) — khỏi luồng thực thi (thread / 스레드) — thực thi (execution / 실행) stream có thể được scheduled.

## Tiến trình (process / 프로세스)

Tiến trình (process / 프로세스) thường có virtual address không gian (space / 공간), open handles/tệp (file / 파일) descriptors, bảo mật (security / 보안) định danh (identity / 식별자) và một hoặc nhiều threads. Hai processes mặc định không đọc bộ nhớ (memory / 메모리) của nhau vì page mappings/protection khác.

Tiến trình (process / 프로세스) creation ngữ nghĩa (semantics / 의미론) khác OS. Unix `fork()` conceptually tạo child từ parent, thường dùng sao chép khi ghi (copy-on-write / 쓰기 시 복사) pages; `exec()` thay tiến trình (process / 프로세스) ảnh (image / 이미지) bằng program mới. Windows tạo tiến trình (process / 프로세스) qua APIs khác. High-level runtimes có thể hide details.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Tiến trình (process / 프로세스)** xác định đầu vào; **Luồng thực thi (thread / 스레드)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Ngữ cảnh (context / 맥락) switch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng thực thi (thread / 스레드)

Luồng thực thi (thread / 스레드) là thực thi (execution / 실행) ngữ cảnh (context / 맥락): program counter, registers, ngăn xếp (stack / 스택), scheduling trạng thái (state / 상태). Threads cùng tiến trình (process / 프로세스) share vùng nhớ động (heap / 힙)/address không gian (space / 공간) và resources.

Sharing làm communication rẻ nhưng tạo dữ liệu (data / 데이터) races. Processes cách ly tốt hơn nhưng IPC thường có overhead/serialization. Đây là isolation-vs-sharing sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Thread chia sẻ process address space; context switch đổi execution state, còn scheduler tiếp theo tối ưu fairness, latency hoặc throughput theo policy.

## Ngữ cảnh (context / 맥락) switch

Scheduler chuyển CPU từ tác vụ (task / 작업) A sang B bằng cách lưu/restoring thực thi (execution / 실행) ngữ cảnh (context / 맥락) và cập nhật address-space trạng thái (state / 상태) nếu cần. chi phí (cost / 비용) không chỉ vài register stores; bộ nhớ đệm (cache / 캐시)/TLB locality có thể bị ảnh hưởng.

Do đó “thêm luồng thực thi (thread / 스레드) để nhanh” có điểm giới hạn. Quá nhiều runnable threads tăng switching, bộ nhớ đệm (cache / 캐시) contention và scheduling overhead.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Scheduler đang tối ưu gì?** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) switch** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CPU-bound và I/O-bound** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scheduler đang tối ưu gì?

Scheduling (스케줄링) phải cân bằng thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간), responsiveness, fairness và priorities. Batch tải công việc (workload / 워크로드) muốn thông lượng (throughput / 처리량); interactive UI muốn low phản hồi (response / 응답) độ trễ (latency / 지연 시간); real-time hệ thống (system / 시스템) cần deadline guarantees.

Textbook algorithms như FCFS, SJF, Round Robin, Priority Scheduling giúp hiểu dimensions, nhưng môi trường vận hành (production / 운영 환경) schedulers như Linux CFS/EEVDF-family lô-gic (logic / 논리) phức tạp hơn và thay đổi theo kernel versions.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **CPU-bound và I/O-bound** tiếp nhận điểm tựa từ **Scheduler đang tối ưu gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Người dùng (user / 사용자) threads, kernel threads và runtimes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CPU-bound và I/O-bound

CPU-bound tác vụ (task / 작업) dùng nhiều compute và luôn runnable. I/O-bound tác vụ (task / 작업) chạy ngắn rồi sleep chờ disk/mạng (network / 네트워크). Scheduler có thể tận dụng khi một tác vụ (task / 작업) blocked để chạy tác vụ (task / 작업) khác.

Đây là lý do tính đồng thời (concurrency / 동시성) tăng thông lượng (throughput / 처리량) ngay cả trên ít cores cho I/O-heavy workloads: lúc tác vụ (task / 작업) A chờ mạng (network / 네트워크), tác vụ (task / 작업) B dùng CPU.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Người dùng (user / 사용자) threads, kernel threads và runtimes** tiếp nhận điểm tựa từ **CPU-bound và I/O-bound** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Luồng thực thi (thread / 스레드) pools** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Người dùng (user / 사용자) threads, kernel threads và runtimes

Có các mô hình (models / 모델들) 1:1, many-to-one, many-to-many giữa ngôn ngữ (language / 언어) tasks và OS threads. Java traditional threads thường map 1:1; Java virtual threads multiplex nhiều lightweight continuations trên carrier threads. Go goroutines có thời gian chạy (runtime / 런타임) scheduler M:N. Async JavaScript thường event-loop + tasks.

Do đó từ “luồng thực thi (thread / 스레드)” trong conversation phải xác định tầng: OS luồng thực thi (thread / 스레드), ngôn ngữ (language / 언어) luồng thực thi (thread / 스레드), virtual luồng thực thi (thread / 스레드) hay tác vụ (task / 작업)/coroutine.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Luồng thực thi (thread / 스레드) pools** tiếp nhận điểm tựa từ **Người dùng (user / 사용자) threads, kernel threads và runtimes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Priority inversion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Luồng thực thi (thread / 스레드) pools

Creating unbounded threads dễ exhaust bộ nhớ (memory / 메모리)/scheduler. luồng thực thi (thread / 스레드) pool giới hạn workers và hàng đợi (queue / 큐) tasks. Nhưng fixed pool có thể deadlock/starve nếu tasks blocking và chờ tasks khác cùng pool. Pool kích thước (size / 크기) phải match tải công việc (workload / 워크로드): CPU-bound gần cốt lõi (core / 핵심) count; I/O-bound có thể cần tính đồng thời (concurrency / 동시성) cao hơn, nhưng bên ngoài (external / 외부) tài nguyên (resource / 자원) limits vẫn chi phối.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Priority inversion** tiếp nhận điểm tựa từ **Luồng thực thi (thread / 스레드) pools** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Little's Law intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Priority inversion

High-priority luồng thực thi (thread / 스레드) có thể chờ khóa (lock / 잠금) do low-priority luồng thực thi (thread / 스레드) giữ, trong khi medium-priority tasks preempt low-priority holder. Priority inheritance là một mitigation. Điều này cho thấy scheduling và synchronization không độc lập.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Little's Law intuition** tiếp nhận điểm tựa từ **Priority inversion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Little's Law intuition

Trong stable hệ thống (system / 시스템):

\[
L = \lambda W
\]

với L average items in hệ thống (system / 시스템), λ arrival tỷ lệ (rate / 비율), W average thời gian (time / 시간). Nếu yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng trong khi arrival tỷ lệ (rate / 비율) giữ, tính đồng thời (concurrency / 동시성)/in-flight count tăng. Scheduling/queues vì vậy nối trực tiếp hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Little's Law intuition** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **tiến trình (process / 프로세스) bảo vệ ranh giới (boundary / 경계); luồng thực thi (thread / 스레드) mang dòng thực thi (execution / 실행); scheduler phân CPU thời gian (time / 시간).** tính đồng thời (concurrency / 동시성) cho phép overlap; parallelism cần nhiều thực thi (execution / 실행) resources thật.

> **Chuyển mạch:** Trong **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Một tiến trình (process / 프로세스) = một luồng thực thi (thread / 스레드).”** tiến trình (process / 프로세스) có thể có nhiều threads.

**“Nhiều threads luôn tăng speed.”** CPU saturation, locks, bộ nhớ đệm (cache / 캐시) và ngữ cảnh (context / 맥락) switches có thể làm chậm.

**“Blocked luồng thực thi (thread / 스레드) vẫn ăn CPU như busy vòng lặp (loop / 루프).”** Blocked tác vụ (task / 작업) thường không runnable; scheduler cho CPU cho tác vụ (task / 작업) khác.

> **Chuyển mạch:** Ở chặng này của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Hardware multicore ở [parallel architecture](../02_computer_architecture/05_parallel_computer_architecture.md). Sharing trạng thái (state / 상태) dẫn tới [concurrency/synchronization](./02_concurrency_synchronization_and_deadlock.md). thời gian chạy (runtime / 런타임) các mô hình (models / 모델들) được nối ở [execution models](../04_programming_languages/00_language_semantics_and_execution_models.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
