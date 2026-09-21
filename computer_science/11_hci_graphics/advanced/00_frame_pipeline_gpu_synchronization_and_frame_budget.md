# Frame pipeline, GPU synchronization và frame budget

Real-time graphics không chỉ hỏi “render đúng hình không?” mà hỏi “có tạo frame đúng deadline và đều không?”. 60 FPS cho khoảng 16.67 ms mỗi frame; 120 FPS khoảng 8.33 ms. Average nhanh nhưng occasional 40 ms stall vẫn tạo judder/stutter thấy rõ.

## CPU và GPU chạy pipeline song song

Application CPU update input, simulation, scene và build rendering commands. GPU consume command stream để chạy vertex/compute/raster/fragment work. Hai bên có thể overlap qua multiple frames in flight.

Nếu CPU chờ GPU mỗi frame không cần thiết, throughput giảm. Nếu CPU submit quá xa, latency input-to-display tăng và resource lifetime phức tạp.

## Frame time khác FPS average

FPS là reciprocal của frame time nhưng average FPS che spikes. 100 frames 8 ms và một frame 100 ms có average nhìn “cao”, nhưng user cảm nhận hitch.

Performance analysis nên dùng frame-time distribution/percentiles và timeline traces, không chỉ counter FPS.

## GPU synchronization giải dependency thật

Rendering work có dependencies: compute shader viết buffer rồi draw đọc buffer; render pass ghi texture rồi post-process sample texture. Resource barrier/synchronization làm visibility/order explicit theo API/hardware model.

Barrier quá yếu tạo race/artifact; barrier quá mạnh serialize pipeline và mất parallelism. Advanced graphics giống concurrency programming: correctness và performance cùng phụ thuộc dependency graph.

## Double/triple buffering và presentation

Back buffer cho phép render frame mới trong khi display đang scan frame trước. VSync đồng bộ presentation với refresh để tránh tearing nhưng có thể thêm waiting/latency nếu miss refresh boundary.

Triple buffering có thể cải thiện throughput/smoothness trong một số pipelines nhưng cũng có thể tăng queued frames. Low-latency modes cố giới hạn render queue.

## CPU-bound và GPU-bound

Nếu CPU mất 20 ms build frame còn GPU 8 ms, tối ưu shader không giải bottleneck. Nếu GPU 20 ms còn CPU 5 ms, giảm draw-call overhead CPU có thể không đổi frame rate nhiều.

GPU-bound lại chia thành vertex/geometry, fragment/fill, bandwidth, compute, synchronization hoặc memory pressure. Profiling cần timestamp queries/counters/tool timeline thay vì suy đoán từ “GPU 100%”.

## Batching và draw-call trade-off

Batching giảm CPU submission overhead nhưng có thể tăng overdraw, giảm culling granularity hoặc làm material/state management khó. Modern APIs giảm per-draw overhead nhưng không xóa cost state changes/resource binding.

Instancing phù hợp nhiều objects cùng mesh/material với per-instance data. Indirect draws/GPU-driven rendering chuyển culling/command generation sang GPU cho scene lớn.

## Frame budget là phân bổ constraint

Với budget 16.67 ms, graphics không sở hữu toàn bộ. Game/app còn simulation, animation, scripting, UI, networking và asset streaming. Một feature “chỉ thêm 2 ms” có thể là lớn nếu headroom chỉ 1 ms.

Budget nên phân theo critical path và worst realistic scene, không chỉ empty scene benchmark.

## Latency là pipeline end-to-end

Input sample → application processing → CPU frame build → GPU execution → compositor → display scanout. Tối ưu một stage không đảm bảo input latency giảm nếu queue phía sau vẫn dài.

Đây là cùng mental model với distributed systems: end-to-end latency là tổng/interaction của nhiều queues, không chỉ service time một component.

## Mental Model

> Real-time rendering là **deadline-driven producer/consumer pipeline**. Hãy đo frame-time timeline, tìm stage trên critical path, hiểu resource dependencies và giữ queue vừa đủ để throughput tốt mà latency không phình.

## Kết nối

Ôn [graphics pipeline](../../basic/11_hci_graphics/02_computer_graphics_pipeline_and_geometry.md), [GPU architecture](../../basic/02_computer_architecture/05_parallel_computer_architecture.md) và [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).