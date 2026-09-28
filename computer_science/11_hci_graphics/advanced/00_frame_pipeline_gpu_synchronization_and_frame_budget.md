# Frame chuỗi xử lý (pipeline / 파이프라인), GPU synchronization và frame ngân sách (budget / 예산)

> **Mạch đọc:** Đặt **Frame chuỗi xử lý (pipeline / 파이프라인), GPU synchronization và frame ngân sách (budget / 예산)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **CPU và GPU chạy chuỗi xử lý (pipeline / 파이프라인) song song** sang **Frame thời gian (time / 시간) khác FPS average**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Real-time graphics không chỉ hỏi “kết xuất (render / 렌더링) đúng hình không?” mà hỏi “có tạo frame đúng deadline và đều không?”. 60 FPS cho khoảng 16.67 ms mỗi frame; 120 FPS khoảng 8.33 ms. Average nhanh nhưng occasional 40 ms stall vẫn tạo judder/stutter thấy rõ.

## CPU và GPU chạy chuỗi xử lý (pipeline / 파이프라인) song song

Ứng dụng (application / 애플리케이션) CPU cập nhật (update / 업데이트) đầu vào (input / 입력), simulation, scene và bản dựng (build / 빌드) rendering commands. GPU consume command stream để chạy vertex/compute/raster/fragment công việc (work / 작업). Hai bên có thể overlap qua multiple frames in flight.

Nếu CPU chờ GPU mỗi frame không cần thiết, thông lượng (throughput / 처리량) giảm. Nếu CPU submit quá xa, độ trễ (latency / 지연 시간) input-to-display tăng và tài nguyên (resource / 자원) thời gian tồn tại (lifetime / 수명) phức tạp.


> **Chuyển mạch:** Từ **CPU và GPU chạy chuỗi xử lý (pipeline / 파이프라인) song song**, ta sang **Frame thời gian (time / 시간) khác FPS average** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Frame thời gian (time / 시간) khác FPS average

FPS là reciprocal của frame thời gian (time / 시간) nhưng average FPS che spikes. 100 frames 8 ms và một frame 100 ms có average nhìn “cao”, nhưng người dùng (user / 사용자) cảm nhận hitch.

Hiệu năng (performance / 성능) phân tích (analysis / 분석) nên dùng frame-time phân phối (distribution / 분포)/percentiles và timeline traces, không chỉ counter FPS.


> **Chuyển mạch:** Từ **Frame thời gian (time / 시간) khác FPS average**, ta sang **GPU synchronization giải phụ thuộc (dependency / 의존성) thật** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## GPU synchronization giải phụ thuộc (dependency / 의존성) thật

Rendering công việc (work / 작업) có dependencies: compute shader viết buffer rồi draw đọc buffer; kết xuất (render / 렌더링) pass ghi texture rồi post-process mẫu (sample / 표본) texture. tài nguyên (resource / 자원) barrier/synchronization làm visibility/thứ tự (order / 순서) tường minh (explicit / 명시적) theo API/hardware mô hình (model / 모델).

Barrier quá yếu tạo race/sản phẩm tạo ra (artifact / 산출물); barrier quá mạnh serialize chuỗi xử lý (pipeline / 파이프라인) và mất parallelism. Advanced graphics giống tính đồng thời (concurrency / 동시성) programming: tính đúng đắn (correctness / 정확성) và hiệu năng (performance / 성능) cùng phụ thuộc phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프).


> **Chuyển mạch:** Từ **GPU synchronization giải phụ thuộc (dependency / 의존성) thật**, ta sang **Double/triple buffering và presentation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Double/triple buffering và presentation

Back buffer cho phép kết xuất (render / 렌더링) frame mới trong khi display đang scan frame trước. VSync đồng bộ presentation với refresh để tránh tearing nhưng có thể thêm waiting/độ trễ (latency / 지연 시간) nếu miss refresh ranh giới (boundary / 경계).

Triple buffering có thể cải thiện thông lượng (throughput / 처리량)/smoothness trong một số pipelines nhưng cũng có thể tăng queued frames. Low-latency modes cố giới hạn kết xuất (render / 렌더링) hàng đợi (queue / 큐).


> **Chuyển mạch:** Từ **Double/triple buffering và presentation**, ta sang **CPU-bound và GPU-bound** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## CPU-bound và GPU-bound

Nếu CPU mất 20 ms bản dựng (build / 빌드) frame còn GPU 8 ms, tối ưu shader không giải bottleneck. Nếu GPU 20 ms còn CPU 5 ms, giảm draw-call overhead CPU có thể không đổi frame tỷ lệ (rate / 비율) nhiều.

GPU-bound lại chia thành vertex/hình học (geometry / 기하학), fragment/fill, bandwidth, compute, synchronization hoặc bộ nhớ (memory / 메모리) pressure. Profiling cần timestamp queries/counters/công cụ (tool / 도구) timeline thay vì suy đoán từ “GPU 100%”.


> **Chuyển mạch:** Từ **CPU-bound và GPU-bound**, ta sang **Batching và draw-call sự đánh đổi (trade-off / 트레이드오프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Batching và draw-call sự đánh đổi (trade-off / 트레이드오프)

Batching giảm CPU submission overhead nhưng có thể tăng overdraw, giảm culling granularity hoặc làm material/trạng thái (state / 상태) management khó. hiện đại (modern / 현대적) APIs giảm per-draw overhead nhưng không xóa chi phí (cost / 비용) trạng thái (state / 상태) changes/tài nguyên (resource / 자원) binding.

Instancing phù hợp nhiều objects cùng mesh/material với per-instance dữ liệu (data / 데이터). Indirect draws/GPU-driven rendering chuyển culling/command generation sang GPU cho scene lớn.


> **Chuyển mạch:** Từ **Batching và draw-call sự đánh đổi (trade-off / 트레이드오프)**, ta sang **Frame ngân sách (budget / 예산) là phân bổ ràng buộc (constraint / 제약조건)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Frame ngân sách (budget / 예산) là phân bổ ràng buộc (constraint / 제약조건)

Với ngân sách (budget / 예산) 16.67 ms, graphics không sở hữu toàn bộ. Game/app còn simulation, animation, scripting, UI, networking và asset streaming. Một tính năng (feature / 기능) “chỉ thêm 2 ms” có thể là lớn nếu headroom chỉ 1 ms.

Ngân sách (budget / 예산) nên phân theo đường găng (critical path / 임계 경로) và worst realistic scene, không chỉ empty scene benchmark.


> **Chuyển mạch:** Từ **Frame ngân sách (budget / 예산) là phân bổ ràng buộc (constraint / 제약조건)**, ta sang **độ trễ (latency / 지연 시간) là chuỗi xử lý (pipeline / 파이프라인) end-to-end** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Độ trễ (latency / 지연 시간) là chuỗi xử lý (pipeline / 파이프라인) end-to-end

Đầu vào (input / 입력) mẫu (sample / 표본) → ứng dụng (application / 애플리케이션) processing → CPU frame bản dựng (build / 빌드) → GPU thực thi (execution / 실행) → compositor → display scanout. Tối ưu một stage không đảm bảo đầu vào (input / 입력) độ trễ (latency / 지연 시간) giảm nếu hàng đợi (queue / 큐) phía sau vẫn dài.

Đây là cùng mô hình tư duy (mental model / 사고 모델) với phân tán (distributed / 분산) các hệ thống (systems / 시스템들): end-to-end độ trễ (latency / 지연 시간) là tổng/tương tác (interaction / 상호작용) của nhiều queues, không chỉ dịch vụ (service / 서비스) thời gian (time / 시간) một thành phần (component / 컴포넌트).


> **Chuyển mạch:** Từ **độ trễ (latency / 지연 시간) là chuỗi xử lý (pipeline / 파이프라인) end-to-end**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Real-time rendering là **deadline-driven producer/bên tiêu thụ (consumer / 소비자) chuỗi xử lý (pipeline / 파이프라인)**. Hãy đo frame-time timeline, tìm stage trên đường găng (critical path / 임계 경로), hiểu tài nguyên (resource / 자원) dependencies và giữ hàng đợi (queue / 큐) vừa đủ để thông lượng (throughput / 처리량) tốt mà độ trễ (latency / 지연 시간) không phình.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Ôn [graphics pipeline](../../basic/11_hci_graphics/02_computer_graphics_pipeline_and_geometry.md), [GPU architecture](../../basic/02_computer_architecture/05_parallel_computer_architecture.md) và [queueing/backpressure](../../08_software_systems/advanced/00_queueing_tail_latency_and_backpressure.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 gpu pipeline command buffers and resource barriers](./01_gpu_pipeline_command_buffers_and_resource_barriers.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
