# Modern GPU pipeline, command buffers và resource barriers

GPU đạt throughput cao bằng cách chạy lượng lớn work song song, nhưng CPU không điều khiển từng shader invocation trực tiếp. Modern graphics API dùng **command buffers/queues** để CPU mô tả work rồi GPU consume bất đồng bộ. Performance và correctness phụ thuộc việc resource chuyển qua các stages theo đúng dependency.

## CPU submission và GPU execution là hai timeline

CPU có thể record commands cho frame tiếp theo trong khi GPU vẫn render frame hiện tại. Điều này tăng overlap nhưng tạo resources “in flight”. Nếu CPU ghi đè buffer mà GPU chưa đọc xong, corruption/race có thể xảy ra.

Frames-in-flight vì thế cần synchronization và resource lifetime rõ.

## Command buffer

Command buffer chứa operations như bind pipeline/resource, draw, dispatch compute, copy. Recording tách preparation khỏi execution và cho driver/runtime có representation hiệu quả hơn nhiều API calls immediate-mode nhỏ.

Explicit APIs như Vulkan/Direct3D 12 chuyển nhiều responsibility synchronization/resource state từ driver sang application để giảm hidden overhead và tăng predictability.

## Pipeline stages

Graphics pipeline đi qua vertex processing, rasterization, fragment/pixel processing và output operations; compute pipeline có dispatch riêng. Resource có thể được đọc/ghi ở nhiều stages khác nhau.

Dependency cần nói không chỉ “operation A trước B” mà còn **stage nào** và **access nào** phải visible.

## Resource barrier

Barrier đảm bảo ordering/visibility cần thiết giữa accesses. Ví dụ compute shader ghi texture rồi fragment shader đọc texture đó; application phải đảm bảo write hoàn tất và visible trước read.

Barrier quá yếu gây race/corruption; barrier quá rộng serialize GPU và làm mất parallelism. Advanced graphics performance thường là bài toán đặt synchronization chính xác thay vì “thêm barrier cho chắc”.

## Layout/state transition

Một số APIs yêu cầu resource ở state/layout phù hợp cho render target, shader read, transfer source... Transition cho driver/hardware biết intended usage và có thể kích hoạt cache/layout operation cần thiết.

State tracking vì thế là một phần correctness model.

## Queue và semaphore/fence

GPU có thể có graphics, compute, transfer queues. Work giữa queues cần synchronization khi share resource. Semaphore thường phối hợp GPU work; fence thường giúp CPU biết GPU đã hoàn thành một submission.

Tên primitive khác nhau theo API nhưng câu hỏi chung là: ai chờ ai, dependency nằm trên timeline nào và wait có block CPU hay chỉ order GPU work.

## Async compute không tự động nhanh

Chạy compute song song graphics chỉ có lợi nếu hardware resources còn headroom và workloads overlap được. Nếu cả hai cùng saturate execution units/memory bandwidth, concurrency có thể không tăng throughput.

Profile phải xác định bottleneck thay vì bật async feature theo checklist.

## Frame pacing

Average 60 FPS tương đương ~16.7 ms/frame nhưng nếu frame times xen kẽ 8 ms và 25 ms, motion vẫn giật. Pipeline buffering quá sâu còn tăng input latency dù throughput cao.

Graphics system vì thế tối ưu cả throughput, frame-time variance và input-to-display latency.

## Mental model

> GPU là asynchronous throughput machine. Command buffers mô tả work; queues tạo timelines; barriers encode dependency/visibility; fences/semaphores phối hợp producers-consumers. Correct synchronization cho phép parallelism, còn over-synchronization biến GPU song song thành pipeline tuần tự.