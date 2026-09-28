# Tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling

> **Mạch đọc:** Đặt **tiến trình (process / 프로세스), luồng thực thi (thread / 스레드) và scheduling** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **tiến trình (process / 프로세스)** sang **luồng thực thi (thread / 스레드)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một máy có thể chạy trình duyệt (browser / 브라우저), cơ sở dữ liệu (database / 데이터베이스), IDE và hàng trăm services dù số CPU cores hữu hạn. OS tạo illusion bằng cách multiplex thực thi (execution / 실행). Để lập luận (reasoning / 추론) đúng, cần tách tiến trình (process / 프로세스) — isolation/tài nguyên (resource / 자원) bộ chứa (container / 컨테이너) — khỏi luồng thực thi (thread / 스레드) — thực thi (execution / 실행) stream có thể được scheduled.

## Tiến trình (process / 프로세스)

Tiến trình (process / 프로세스) thường có virtual address không gian (space / 공간), open handles/tệp (file / 파일) descriptors, bảo mật (security / 보안) định danh (identity / 식별자) và một hoặc nhiều threads. Hai processes mặc định không đọc bộ nhớ (memory / 메모리) của nhau vì page mappings/protection khác.

Tiến trình (process / 프로세스) creation ngữ nghĩa (semantics / 의미론) khác OS. Unix `fork()` conceptually tạo child từ parent, thường dùng sao chép khi ghi (copy-on-write / 쓰기 시 복사) pages; `exec()` thay tiến trình (process / 프로세스) ảnh (image / 이미지) bằng program mới. Windows tạo tiến trình (process / 프로세스) qua APIs khác. High-level runtimes có thể hide details.


> **Chuyển mạch:** Từ **tiến trình (process / 프로세스)**, ta sang **luồng thực thi (thread / 스레드)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Luồng thực thi (thread / 스레드)

Luồng thực thi (thread / 스레드) là thực thi (execution / 실행) ngữ cảnh (context / 맥락): program counter, registers, ngăn xếp (stack / 스택), scheduling trạng thái (state / 상태). Threads cùng tiến trình (process / 프로세스) share vùng nhớ động (heap / 힙)/address không gian (space / 공간) và resources.

Sharing làm communication rẻ nhưng tạo dữ liệu (data / 데이터) races. Processes cách ly tốt hơn nhưng IPC thường có overhead/serialization. Đây là isolation-vs-sharing sự đánh đổi (trade-off / 트레이드오프).


> **Chuyển mạch:** Từ **luồng thực thi (thread / 스레드)**, ta sang **ngữ cảnh (context / 맥락) switch** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Ngữ cảnh (context / 맥락) switch

Scheduler chuyển CPU từ tác vụ (task / 작업) A sang B bằng cách lưu/restoring thực thi (execution / 실행) ngữ cảnh (context / 맥락) và cập nhật address-space trạng thái (state / 상태) nếu cần. chi phí (cost / 비용) không chỉ vài register stores; bộ nhớ đệm (cache / 캐시)/TLB locality có thể bị ảnh hưởng.

Do đó “thêm luồng thực thi (thread / 스레드) để nhanh” có điểm giới hạn. Quá nhiều runnable threads tăng switching, bộ nhớ đệm (cache / 캐시) contention và scheduling overhead.


> **Chuyển mạch:** Từ **ngữ cảnh (context / 맥락) switch**, ta sang **Scheduler đang tối ưu gì?** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Scheduler đang tối ưu gì?

Scheduling (스케줄링) phải cân bằng thông lượng (throughput / 처리량), độ trễ (latency / 지연 시간), responsiveness, fairness và priorities. Batch tải công việc (workload / 워크로드) muốn thông lượng (throughput / 처리량); interactive UI muốn low phản hồi (response / 응답) độ trễ (latency / 지연 시간); real-time hệ thống (system / 시스템) cần deadline guarantees.

Textbook algorithms như FCFS, SJF, Round Robin, Priority Scheduling giúp hiểu dimensions, nhưng môi trường vận hành (production / 운영 환경) schedulers như Linux CFS/EEVDF-family lô-gic (logic / 논리) phức tạp hơn và thay đổi theo kernel versions.


> **Chuyển mạch:** Từ **Scheduler đang tối ưu gì?**, ta sang **CPU-bound và I/O-bound** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## CPU-bound và I/O-bound

CPU-bound tác vụ (task / 작업) dùng nhiều compute và luôn runnable. I/O-bound tác vụ (task / 작업) chạy ngắn rồi sleep chờ disk/mạng (network / 네트워크). Scheduler có thể tận dụng khi một tác vụ (task / 작업) blocked để chạy tác vụ (task / 작업) khác.

Đây là lý do tính đồng thời (concurrency / 동시성) tăng thông lượng (throughput / 처리량) ngay cả trên ít cores cho I/O-heavy workloads: lúc tác vụ (task / 작업) A chờ mạng (network / 네트워크), tác vụ (task / 작업) B dùng CPU.


> **Chuyển mạch:** Từ **CPU-bound và I/O-bound**, ta sang **người dùng (user / 사용자) threads, kernel threads và runtimes** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Người dùng (user / 사용자) threads, kernel threads và runtimes

Có các mô hình (models / 모델들) 1:1, many-to-one, many-to-many giữa ngôn ngữ (language / 언어) tasks và OS threads. Java traditional threads thường map 1:1; Java virtual threads multiplex nhiều lightweight continuations trên carrier threads. Go goroutines có thời gian chạy (runtime / 런타임) scheduler M:N. Async JavaScript thường event-loop + tasks.

Do đó từ “luồng thực thi (thread / 스레드)” trong conversation phải xác định tầng: OS luồng thực thi (thread / 스레드), ngôn ngữ (language / 언어) luồng thực thi (thread / 스레드), virtual luồng thực thi (thread / 스레드) hay tác vụ (task / 작업)/coroutine.


> **Chuyển mạch:** Từ **người dùng (user / 사용자) threads, kernel threads và runtimes**, ta sang **luồng thực thi (thread / 스레드) pools** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Luồng thực thi (thread / 스레드) pools

Creating unbounded threads dễ exhaust bộ nhớ (memory / 메모리)/scheduler. luồng thực thi (thread / 스레드) pool giới hạn workers và hàng đợi (queue / 큐) tasks. Nhưng fixed pool có thể deadlock/starve nếu tasks blocking và chờ tasks khác cùng pool. Pool kích thước (size / 크기) phải match tải công việc (workload / 워크로드): CPU-bound gần cốt lõi (core / 핵심) count; I/O-bound có thể cần tính đồng thời (concurrency / 동시성) cao hơn, nhưng bên ngoài (external / 외부) tài nguyên (resource / 자원) limits vẫn chi phối.


> **Chuyển mạch:** Từ **luồng thực thi (thread / 스레드) pools**, ta sang **Priority inversion** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Priority inversion

High-priority luồng thực thi (thread / 스레드) có thể chờ khóa (lock / 잠금) do low-priority luồng thực thi (thread / 스레드) giữ, trong khi medium-priority tasks preempt low-priority holder. Priority inheritance là một mitigation. Điều này cho thấy scheduling và synchronization không độc lập.


> **Chuyển mạch:** Từ **Priority inversion**, ta sang **Little's Law intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Little's Law intuition

Trong stable hệ thống (system / 시스템):

\[
L = \lambda W
\]

với L average items in hệ thống (system / 시스템), λ arrival tỷ lệ (rate / 비율), W average thời gian (time / 시간). Nếu yêu cầu (request / 요청) độ trễ (latency / 지연 시간) tăng trong khi arrival tỷ lệ (rate / 비율) giữ, tính đồng thời (concurrency / 동시성)/in-flight count tăng. Scheduling/queues vì vậy nối trực tiếp hiệu năng (performance / 성능) kỹ thuật (engineering / 엔지니어링).


> **Chuyển mạch:** Từ **Little's Law intuition**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> **tiến trình (process / 프로세스) bảo vệ ranh giới (boundary / 경계); luồng thực thi (thread / 스레드) mang dòng thực thi (execution / 실행); scheduler phân CPU thời gian (time / 시간).** tính đồng thời (concurrency / 동시성) cho phép overlap; parallelism cần nhiều thực thi (execution / 실행) resources thật.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Một tiến trình (process / 프로세스) = một luồng thực thi (thread / 스레드).”** tiến trình (process / 프로세스) có thể có nhiều threads.

**“Nhiều threads luôn tăng speed.”** CPU saturation, locks, bộ nhớ đệm (cache / 캐시) và ngữ cảnh (context / 맥락) switches có thể làm chậm.

**“Blocked luồng thực thi (thread / 스레드) vẫn ăn CPU như busy vòng lặp (loop / 루프).”** Blocked tác vụ (task / 작업) thường không runnable; scheduler cho CPU cho tác vụ (task / 작업) khác.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Hardware multicore ở [parallel architecture](../02_computer_architecture/05_parallel_computer_architecture.md). Sharing trạng thái (state / 상태) dẫn tới [concurrency/synchronization](./02_concurrency_synchronization_and_deadlock.md). thời gian chạy (runtime / 런타임) các mô hình (models / 모델들) được nối ở [execution models](../04_programming_languages/00_language_semantics_and_execution_models.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 kernel syscalls and os abstractions](./00_kernel_syscalls_and_os_abstractions.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
