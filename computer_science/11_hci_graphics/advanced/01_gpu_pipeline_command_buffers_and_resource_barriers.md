# Hiện đại (modern / 현대적) GPU chuỗi xử lý (pipeline / 파이프라인), command buffers và tài nguyên (resource / 자원) barriers

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Modern GPU pipeline, command buffers và resource barriers**. Route đi từ CPU submission/GPU execution timelines → command recording → resource states/barriers → synchronization hazards → queue overlap, để correctness và throughput được đọc cùng nhau.

GPU đạt thông lượng (throughput / 처리량) cao bằng cách chạy lượng lớn công việc (work / 작업) song song, nhưng CPU không điều khiển từng shader invocation trực tiếp. hiện đại (modern / 현대적) graphics API dùng **command buffers/queues** để CPU mô tả công việc (work / 작업) rồi GPU consume bất đồng bộ. hiệu năng (performance / 성능) và tính đúng đắn (correctness / 정확성) phụ thuộc việc tài nguyên (resource / 자원) chuyển qua các stages theo đúng phụ thuộc (dependency / 의존성).

## CPU submission và GPU thực thi (execution / 실행) là hai timeline

CPU có thể bản ghi (record / 레코드) commands cho frame tiếp theo trong khi GPU vẫn kết xuất (render / 렌더링) frame hiện tại. Điều này tăng overlap nhưng tạo resources “in flight”. Nếu CPU ghi đè buffer mà GPU chưa đọc xong, corruption/race có thể xảy ra.

Frames-in-flight vì thế cần synchronization và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) rõ.

Hai timeline chỉ hữu ích khi CPU mô tả công việc bằng một biểu diễn GPU có thể thực thi. Vì vậy phần tiếp theo xem command buffer chứa gì và nó tách ghi lệnh khỏi thực thi ra sao.

## Command buffer

Command buffer chứa operations như bind chuỗi xử lý (pipeline / 파이프라인)/tài nguyên (resource / 자원), draw, dispatch compute, bản sao (copy / 복사). Recording tách preparation khỏi thực thi (execution / 실행) và cho driver/thời gian chạy (runtime / 런타임) có biểu diễn (representation / 표현) hiệu quả hơn nhiều API calls immediate-mode nhỏ.

Tường minh (explicit / 명시적) APIs như Vulkan/Direct3D 12 chuyển nhiều responsibility synchronization/tài nguyên (resource / 자원) trạng thái (state / 상태) từ driver sang ứng dụng (application / 애플리케이션) để giảm hidden overhead và tăng predictability.

Command buffer mô tả thao tác, còn pipeline stage xác định nơi thao tác đó đọc hoặc ghi tài nguyên. Muốn tránh race, ta phải nối hai lớp này bằng barrier có phạm vi rõ.

## Chuỗi xử lý (pipeline / 파이프라인) stages

Graphics chuỗi xử lý (pipeline / 파이프라인) đi qua vertex processing, rasterization, fragment/điểm ảnh (pixel / 픽셀) processing và đầu ra (output / 출력) operations; compute chuỗi xử lý (pipeline / 파이프라인) có dispatch riêng. tài nguyên (resource / 자원) có thể được đọc/ghi ở nhiều stages khác nhau.

Phụ thuộc (dependency / 의존성) cần nói không chỉ “thao tác (operation / 연산) A trước B” mà còn **stage nào** và **truy cập (access / 접근) nào** phải visible.

Barrier cần nói rõ access nào phải visible giữa những stage nào. Trên các API explicit, visibility này còn gắn với layout hoặc state transition của chính resource.

## Tài nguyên (resource / 자원) barrier

Barrier đảm bảo thứ tự (ordering / 순서)/visibility cần thiết giữa accesses. Ví dụ compute shader ghi texture rồi fragment shader đọc texture đó; ứng dụng (application / 애플리케이션) phải đảm bảo ghi (write / 쓰기) hoàn tất và visible trước read.

Barrier quá yếu gây race/corruption; barrier quá rộng serialize GPU và làm mất parallelism. Advanced graphics hiệu năng (performance / 성능) thường là bài toán đặt synchronization chính xác thay vì “thêm barrier cho chắc”.

State transition làm rõ resource đang được dùng cho mục đích nào; khi công việc đi qua nhiều queue, ta cần thêm cơ chế báo hiệu để phối hợp các timeline đó.

## Bố cục (layout / 레이아웃)/chuyển tiếp trạng thái (state transition / 상태 전이)

Một số APIs yêu cầu tài nguyên (resource / 자원) ở trạng thái (state / 상태)/bố cục (layout / 레이아웃) phù hợp cho kết xuất (render / 렌더링) mục tiêu (target / 대상), shader read, transfer nguồn (source / 소스)... chuyển tiếp (transition / 전이) cho driver/hardware biết intended usage và có thể kích hoạt bộ nhớ đệm (cache / 캐시)/bố cục (layout / 레이아웃) thao tác (operation / 연산) cần thiết.

Trạng thái (state / 상태) tracking vì thế là một phần tính đúng đắn (correctness / 정확성) mô hình (model / 모델).

Semaphore và fence xác định ai chờ ai, nhưng phối hợp được không có nghĩa là chạy nhanh hơn. Async compute chỉ đáng dùng khi profile cho thấy hai workload còn tài nguyên để chồng lấp.

## Hàng đợi (queue / 큐) và semaphore/fence

GPU có thể có graphics, compute, transfer queues. công việc (work / 작업) giữa queues cần synchronization khi share tài nguyên (resource / 자원). Semaphore thường phối hợp GPU công việc (work / 작업); fence thường giúp CPU biết GPU đã hoàn thành một submission.

Tên thành phần nguyên thủy (primitive / 기본 요소) khác nhau theo API nhưng câu hỏi chung là: ai chờ ai, phụ thuộc (dependency / 의존성) nằm trên timeline nào và wait có khối (block / 블록) CPU hay chỉ thứ tự (order / 순서) GPU công việc (work / 작업).

Nếu overlap tạo thêm contention hoặc wait, frame-time có thể xấu đi dù throughput lý thuyết tăng. Vì vậy cần đọc kết quả async ở mức frame pacing và input-to-display latency.

## Async compute không tự động nhanh

Chạy compute song song graphics chỉ có lợi nếu hardware resources còn headroom và workloads overlap được. Nếu cả hai cùng saturate thực thi (execution / 실행) units/bộ nhớ (memory / 메모리) bandwidth, tính đồng thời (concurrency / 동시성) có thể không tăng thông lượng (throughput / 처리량).

Profile phải xác định bottleneck thay vì bật async tính năng (feature / 기능) theo checklist.

Frame pacing là nơi các quyết định về queue, barrier và overlap lộ ra dưới dạng jitter hoặc latency. Nó cung cấp tiêu chí cuối để cân bằng throughput với trải nghiệm hiển thị.

## Frame pacing

Average 60 FPS tương đương ~16.7 ms/frame nhưng nếu frame times xen kẽ 8 ms và 25 ms, motion vẫn giật. chuỗi xử lý (pipeline / 파이프라인) buffering quá sâu còn tăng đầu vào (input / 입력) độ trễ (latency / 지연 시간) dù thông lượng (throughput / 처리량) cao.

Graphics hệ thống (system / 시스템) vì thế tối ưu cả thông lượng (throughput / 처리량), frame-time variance và input-to-display độ trễ (latency / 지연 시간).

## Mô hình tư duy (mental model / 사고 모델)

> GPU là asynchronous thông lượng (throughput / 처리량) machine. Command buffers mô tả công việc (work / 작업); queues tạo timelines; barriers encode phụ thuộc (dependency / 의존성)/visibility; fences/semaphores phối hợp producers-consumers. Correct synchronization cho phép parallelism, còn over-synchronization biến GPU song song thành chuỗi xử lý (pipeline / 파이프라인) tuần tự.

> **Bàn giao:** Sau **Mô hình tư duy (mental model / 사고 모델)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
