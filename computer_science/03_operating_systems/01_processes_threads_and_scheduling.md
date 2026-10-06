# Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling**. Route đi từ address space/process → thread/context switch → scheduling/queues → latency, fairness và throughput, để hành vi ứng dụng được nối với cách CPU phân phối thời gian.

Một máy có thể chạy trình duyệt (browser / 브라우저), cơ sở dữ liệu (database / 데이터베이스), IDE và hàng trăm services dù số CPU cores hữu hạn. OS tạo illusion bằng cách multiplex thực thi (execution / 실행). Để lập luận (reasoning / 추론) đúng, cần tách tiến trình (process / 프로세스) — isolation/tài nguyên (resource / 자원) bộ chứa (container / 컨테이너) — khỏi luồng thực thi (thread / 스레드) — thực thi (execution / 실행) stream có thể được scheduled.

## Tiến trình (process / 프로세스)

Tiến trình (process / 프로세스) thường có virtual address không gian (space / 공간), open handles/tệp (file / 파일) descriptors, bảo mật (security / 보안) định danh (identity / 식별자) và một hoặc nhiều threads. Hai processes mặc định không đọc bộ nhớ (memory / 메모리) của nhau vì page mappings/protection khác.

Tiến trình (process / 프로세스) creation ngữ nghĩa (semantics / 의미론) khác OS. Unix `fork()` conceptually tạo child từ parent, thường dùng sao chép khi ghi (copy-on-write / 쓰기 시 복사) pages; `exec()` thay tiến trình (process / 프로세스) ảnh (image / 이미지) bằng program mới. Windows tạo tiến trình (process / 프로세스) qua APIs khác. High-level runtimes có thể hide details.

> **Nối mạch:** **Tiến trình (process / 프로세스)** đặt đầu vào cho **Luồng thực thi (thread / 스레드)**, rồi **Ngữ cảnh (context / 맥락) switch** mở rộng hệ quả.

## Luồng thực thi (thread / 스레드)

Luồng thực thi (thread / 스레드) là thực thi (execution / 실행) ngữ cảnh (context / 맥락): program counter, registers, ngăn xếp (stack / 스택), scheduling trạng thái (state / 상태). Threads cùng tiến trình (process / 프로세스) share vùng nhớ động (heap / 힙)/address không gian (space / 공간) và resources.

Sharing làm communication rẻ nhưng tạo dữ liệu (data / 데이터) races. Processes cách ly tốt hơn nhưng IPC thường có overhead/serialization. Đây là isolation-vs-sharing sự đánh đổi (trade-off / 트레이드오프).

> **Nối mạch:** Thread chia sẻ process address space; context switch đổi execution state, còn scheduler tiếp theo tối ưu fairness, latency hoặc throughput theo policy.

## Ngữ cảnh (context / 맥락) switch

Scheduler chuyển CPU từ tác vụ (task / 작업) A sang B bằng cách lưu/restoring thực thi (execution / 실행) ngữ cảnh (context / 맥락) và cập nhật address-space trạng thái (state / 상태) nếu cần. chi phí (cost / 비용) không chỉ vài register stores; bộ nhớ đệm (cache / 캐시)/TLB locality có thể bị ảnh hưởng.

Do đó “thêm luồng thực thi (thread / 스레드) để nhanh” có điểm giới hạn. Quá nhiều runnable threads tăng switching, bộ nhớ đệm (cache / 캐시) contention và scheduling overhead.

> **Nối mạch:** **Scheduler đang tối ưu gì?** nối từ **Ngữ cảnh (context / 맥락) switch** sang **CPU-bound và I/O-bound**, vì cơ chế trước tạo đầu vào cho bước sau.

## Scheduler đang tối ưu gì?

Scheduling (스케줄링) phải cân bằng thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간), responsiveness, fairness và priorities. Batch tải công việc (workload / 워크로드) muốn thông lượng (throughput / 처리량); interactive UI muốn low phản hồi (response / 응답) độ trễ (latency / 지연 시간); real-time hệ thống (system / 시스템) cần deadline guarantees.

Textbook algorithms như FCFS, SJF, Round Robin, Priority Scheduling giúp hiểu dimensions, nhưng môi trường vận hành (production / 운영 환경) schedulers như Linux CFS/EEVDF-family lô-gic (logic / 논리) phức tạp hơn và thay đổi theo kernel versions.

> **Nối mạch:** **CPU-bound và I/O-bound** nối từ **Scheduler đang tối ưu gì?** sang **Người dùng (user / 사용자) threads, kernel threads và runtimes**, vì cơ chế trước tạo đầu vào cho bước sau.

## CPU-bound và I/O-bound

CPU-bound tác vụ (task / 작업) dùng nhiều compute và luôn runnable. I/O-bound tác vụ (task / 작업) chạy ngắn rồi sleep chờ disk/mạng (network / 네트워크). Scheduler có thể tận dụng khi một tác vụ (task / 작업) blocked để chạy tác vụ (task / 작업) khác.

Đây là lý do tính đồng thời (concurrency / 동시성) tăng thông lượng (throughput / 처리량) ngay cả trên ít cores cho I/O-heavy workloads: lúc tác vụ (task / 작업) A chờ mạng (network / 네트워크), tác vụ (task / 작업) B dùng CPU.

> **Nối mạch:** **Người dùng (user / 사용자) threads, kernel threads và runtimes** nối từ **CPU-bound và I/O-bound** sang **Luồng thực thi (thread / 스레드) pools**, vì cơ chế trước tạo đầu vào cho bước sau.

## Người dùng (user / 사용자) threads, kernel threads và runtimes

Có các mô hình (models / 모델들) 1:1, many-to-one, many-to-many giữa ngôn ngữ (language / 언어) tasks và OS threads. Java traditional threads thường map 1:1; Java virtual threads multiplex nhiều lightweight continuations trên carrier threads. Go goroutines có thời gian chạy (runtime / 런타임) scheduler M:N. Async JavaScript thường event-loop + tasks.

Do đó từ “luồng thực thi (thread / 스레드)” trong conversation phải xác định tầng: OS luồng thực thi (thread / 스레드), ngôn ngữ (language / 언어) luồng thực thi (thread / 스레드), virtual luồng thực thi (thread / 스레드) hay tác vụ (task / 작업)/coroutine.

> **Nối mạch:** **Luồng thực thi (thread / 스레드) pools** nối từ **Người dùng (user / 사용자) threads, kernel threads và runtimes** sang **Priority inversion**, vì cơ chế trước tạo đầu vào cho bước sau.

## Luồng thực thi (thread / 스레드) pools

Creating unbounded threads dễ exhaust bộ nhớ (memory / 메모리)/scheduler. luồng thực thi (thread / 스레드) pool giới hạn workers và hàng đợi (queue / 큐) tasks. Nhưng fixed pool có thể deadlock/starve nếu tasks blocking và chờ tasks khác cùng pool. Pool kích thước (size / 크기) phải match tải công việc (workload / 워크로드): CPU-bound gần cốt lõi (core / 핵심) count; I/O-bound có thể cần tính đồng thời (concurrency / 동시성) cao hơn, nhưng bên ngoài (external / 외부) tài nguyên (resource / 자원) limits vẫn chi phối.

> **Nối mạch:** **Priority inversion** nối từ **Luồng thực thi (thread / 스레드) pools** sang **Little's Law intuition**, vì cơ chế trước tạo đầu vào cho bước sau.

## Priority inversion

High-priority luồng thực thi (thread / 스레드) có thể chờ khóa (lock / 잠금) do low-priority luồng thực thi (thread / 스레드) giữ, trong khi medium-priority tasks preempt low-priority holder. Priority inheritance là một mitigation. Điều này cho thấy scheduling và synchronization không độc lập.

> **Nối mạch:** **Little's Law intuition** nối từ **Priority inversion** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Little's Law intuition

Trong stable hệ thống (system / 시스템):

\[
L = \lambda W
\]

với L average items in hệ thống (system / 시스템), λ arrival tỷ lệ (rate / 비율), W average thời gian (time / 시간). Nếu yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng trong khi arrival tỷ lệ (rate / 비율) giữ, tính đồng thời (concurrency / 동시성)/in-flight count tăng. Scheduling/queues vì vậy nối trực tiếp hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링).

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Little's Law intuition**; **Dùng chung (common / 공통) Misconceptions** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> **tiến trình (process / 프로세스) bảo vệ ranh giới (boundary / 경계); luồng thực thi (thread / 스레드) mang dòng thực thi (execution / 실행); scheduler phân CPU thời gian (time / 시간).** tính đồng thời (concurrency / 동시성) cho phép overlap; parallelism cần nhiều thực thi (execution / 실행) resources thật.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

**“Một tiến trình (process / 프로세스) = một luồng thực thi (thread / 스레드).”** tiến trình (process / 프로세스) có thể có nhiều threads.

**“Nhiều threads luôn tăng speed.”** CPU saturation, locks, bộ nhớ đệm (cache / 캐시) và ngữ cảnh (context / 맥락) switches có thể làm chậm.

**“Blocked luồng thực thi (thread / 스레드) vẫn ăn CPU như busy vòng lặp (loop / 루프).”** Blocked tác vụ (task / 작업) thường không runnable; scheduler cho CPU cho tác vụ (task / 작업) khác.

> **Nối mạch:** **Kết nối** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Hardware multicore ở [parallel architecture](../02_computer_architecture/05_parallel_computer_architecture.md). Sharing trạng thái (state / 상태) dẫn tới [concurrency/synchronization](./02_concurrency_synchronization_and_deadlock.md). thời gian chạy (runtime / 런타임) các mô hình (models / 모델들) được nối ở [execution models](../04_programming_languages/00_language_semantics_and_execution_models.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
