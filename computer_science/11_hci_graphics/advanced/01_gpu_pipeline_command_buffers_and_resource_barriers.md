# Hiện đại (modern / 현대적) GPU chuỗi xử lý (pipeline / 파이프라인), command buffers và tài nguyên (resource / 자원) barriers

> **Mạch đọc:** Đặt **hiện đại (modern / 현대적) GPU chuỗi xử lý (pipeline / 파이프라인), command buffers và tài nguyên (resource / 자원) barriers** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **CPU submission và GPU thực thi (execution / 실행) là hai timeline** sang **Command buffer**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


GPU đạt thông lượng (throughput / 처리량) cao bằng cách chạy lượng lớn công việc (work / 작업) song song, nhưng CPU không điều khiển từng shader invocation trực tiếp. hiện đại (modern / 현대적) graphics API dùng **command buffers/queues** để CPU mô tả công việc (work / 작업) rồi GPU consume bất đồng bộ. hiệu năng (performance / 성능) và tính đúng đắn (correctness / 정확성) phụ thuộc việc tài nguyên (resource / 자원) chuyển qua các stages theo đúng phụ thuộc (dependency / 의존성).

## CPU submission và GPU thực thi (execution / 실행) là hai timeline

CPU có thể bản ghi (record / 레코드) commands cho frame tiếp theo trong khi GPU vẫn kết xuất (render / 렌더링) frame hiện tại. Điều này tăng overlap nhưng tạo resources “in flight”. Nếu CPU ghi đè buffer mà GPU chưa đọc xong, corruption/race có thể xảy ra.

Frames-in-flight vì thế cần synchronization và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) rõ.


> **Chuyển mạch:** Từ **CPU submission và GPU thực thi (execution / 실행) là hai timeline**, ta sang **Command buffer** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Command buffer

Command buffer chứa operations như bind chuỗi xử lý (pipeline / 파이프라인)/tài nguyên (resource / 자원), draw, dispatch compute, bản sao (copy / 복사). Recording tách preparation khỏi thực thi (execution / 실행) và cho driver/thời gian chạy (runtime / 런타임) có biểu diễn (representation / 표현) hiệu quả hơn nhiều API calls immediate-mode nhỏ.

Tường minh (explicit / 명시적) APIs như Vulkan/Direct3D 12 chuyển nhiều responsibility synchronization/tài nguyên (resource / 자원) trạng thái (state / 상태) từ driver sang ứng dụng (application / 애플리케이션) để giảm hidden overhead và tăng predictability.


> **Chuyển mạch:** Từ **Command buffer**, ta sang **chuỗi xử lý (pipeline / 파이프라인) stages** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Chuỗi xử lý (pipeline / 파이프라인) stages

Graphics chuỗi xử lý (pipeline / 파이프라인) đi qua vertex processing, rasterization, fragment/điểm ảnh (pixel / 픽셀) processing và đầu ra (output / 출력) operations; compute chuỗi xử lý (pipeline / 파이프라인) có dispatch riêng. tài nguyên (resource / 자원) có thể được đọc/ghi ở nhiều stages khác nhau.

Phụ thuộc (dependency / 의존성) cần nói không chỉ “thao tác (operation / 연산) A trước B” mà còn **stage nào** và **truy cập (access / 접근) nào** phải visible.


> **Chuyển mạch:** Từ **chuỗi xử lý (pipeline / 파이프라인) stages**, ta sang **tài nguyên (resource / 자원) barrier** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Tài nguyên (resource / 자원) barrier

Barrier đảm bảo thứ tự (ordering / 순서)/visibility cần thiết giữa accesses. Ví dụ compute shader ghi texture rồi fragment shader đọc texture đó; ứng dụng (application / 애플리케이션) phải đảm bảo ghi (write / 쓰기) hoàn tất và visible trước read.

Barrier quá yếu gây race/corruption; barrier quá rộng serialize GPU và làm mất parallelism. Advanced graphics hiệu năng (performance / 성능) thường là bài toán đặt synchronization chính xác thay vì “thêm barrier cho chắc”.


> **Chuyển mạch:** Từ **tài nguyên (resource / 자원) barrier**, ta sang **bố cục (layout / 레이아웃)/chuyển tiếp trạng thái (state transition / 상태 전이)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Bố cục (layout / 레이아웃)/chuyển tiếp trạng thái (state transition / 상태 전이)

Một số APIs yêu cầu tài nguyên (resource / 자원) ở trạng thái (state / 상태)/bố cục (layout / 레이아웃) phù hợp cho kết xuất (render / 렌더링) mục tiêu (target / 대상), shader read, transfer nguồn (source / 소스)... chuyển tiếp (transition / 전이) cho driver/hardware biết intended usage và có thể kích hoạt bộ nhớ đệm (cache / 캐시)/bố cục (layout / 레이아웃) thao tác (operation / 연산) cần thiết.

Trạng thái (state / 상태) tracking vì thế là một phần tính đúng đắn (correctness / 정확성) mô hình (model / 모델).


> **Chuyển mạch:** Từ **bố cục (layout / 레이아웃)/chuyển tiếp trạng thái (state transition / 상태 전이)**, ta sang **hàng đợi (queue / 큐) và semaphore/fence** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Hàng đợi (queue / 큐) và semaphore/fence

GPU có thể có graphics, compute, transfer queues. công việc (work / 작업) giữa queues cần synchronization khi share tài nguyên (resource / 자원). Semaphore thường phối hợp GPU công việc (work / 작업); fence thường giúp CPU biết GPU đã hoàn thành một submission.

Tên thành phần nguyên thủy (primitive / 기본 요소) khác nhau theo API nhưng câu hỏi chung là: ai chờ ai, phụ thuộc (dependency / 의존성) nằm trên timeline nào và wait có khối (block / 블록) CPU hay chỉ thứ tự (order / 순서) GPU công việc (work / 작업).


> **Chuyển mạch:** Từ **hàng đợi (queue / 큐) và semaphore/fence**, ta sang **Async compute không tự động nhanh** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Async compute không tự động nhanh

Chạy compute song song graphics chỉ có lợi nếu hardware resources còn headroom và workloads overlap được. Nếu cả hai cùng saturate thực thi (execution / 실행) units/bộ nhớ (memory / 메모리) bandwidth, tính đồng thời (concurrency / 동시성) có thể không tăng thông lượng (throughput / 처리량).

Profile phải xác định bottleneck thay vì bật async tính năng (feature / 기능) theo checklist.


> **Chuyển mạch:** Từ **Async compute không tự động nhanh**, ta sang **Frame pacing** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Frame pacing

Average 60 FPS tương đương ~16.7 ms/frame nhưng nếu frame times xen kẽ 8 ms và 25 ms, motion vẫn giật. chuỗi xử lý (pipeline / 파이프라인) buffering quá sâu còn tăng đầu vào (input / 입력) độ trễ (latency / 지연 시간) dù thông lượng (throughput / 처리량) cao.

Graphics hệ thống (system / 시스템) vì thế tối ưu cả thông lượng (throughput / 처리량), frame-time variance và input-to-display độ trễ (latency / 지연 시간).


> **Chuyển mạch:** Từ **Frame pacing**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> GPU là asynchronous thông lượng (throughput / 처리량) machine. Command buffers mô tả công việc (work / 작업); queues tạo timelines; barriers encode phụ thuộc (dependency / 의존성)/visibility; fences/semaphores phối hợp producers-consumers. Correct synchronization cho phép parallelism, còn over-synchronization biến GPU song song thành chuỗi xử lý (pipeline / 파이프라인) tuần tự.

> **Bàn giao:** Sau **mô hình tư duy (mental model / 사고 모델)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 frame pipeline gpu synchronization and frame budget](./00_frame_pipeline_gpu_synchronization_and_frame_budget.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
