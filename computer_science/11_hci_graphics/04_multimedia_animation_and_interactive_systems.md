# Multimedia, animation và interactive các hệ thống (systems / 시스템들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Multimedia, animation và interactive systems**. Route đi từ frame rate/timing → render loop/double buffering → input latency/animation → audio sampling/sync → video compression và real-time constraints, để cảm nhận tương tác gắn với deadline.

Interactive media kết hợp rendering, audio/video, đầu vào (input / 입력), timing và tính đồng thời (concurrency / 동시성). Khác batch computation, một frame đúng nhưng đến muộn vẫn tạo trải nghiệm sai. Vì vậy real-time các hệ thống (systems / 시스템들) cần lập luận (reasoning / 추론) về deadlines, buffering và synchronization.

## Frame tỷ lệ (rate / 비율) và frame thời gian (time / 시간)

60 frames/second cho ngân sách (budget / 예산) khoảng:

\[
1000/60 \approx 16.67\ ms/frame
\]

120 FPS chỉ còn khoảng 8.33 ms. Nếu CPU simulation + GPU kết xuất (render / 렌더링) vượt ngân sách (budget / 예산), frame miss và stutter xảy ra.

Average FPS có thể cao nhưng frame-time spikes vẫn khó chịu; phân phối (distribution / 분포)/pacing quan trọng.

Frame budget chỉ trở nên có thể thực thi khi được đặt vào game/render loop. Loop đó cũng xác định thời điểm buffer được tạo và trình bày.

## Game/kết xuất (render / 렌더링) vòng lặp (loop / 루프)

Vòng lặp (loop / 루프) đơn giản:

```text
process input
update simulation
render
present
repeat
```

Simulation timestep có thể variable theo frame delta hoặc fixed timestep. Fixed timestep ổn định physics/determinism hơn; rendering có thể interpolate giữa simulation states.

Double buffering ngăn display đọc dữ liệu đang bị ghi, nhưng thêm buffer và chờ refresh cũng có thể tăng độ trễ. Vì vậy cần theo dõi input-to-display path.

## Double buffering

Nếu display đọc framebuffer trong khi GPU đang viết, tearing/inconsistent frame có thể xảy ra. Double buffering dùng front buffer để display và back buffer để kết xuất (render / 렌더링) rồi swap.

VSync đồng bộ present với display refresh để giảm tearing nhưng có độ trễ (latency / 지연 시간) trade-offs.

Độ trễ là đường đi từ input đến photon, không chỉ là thời gian render. Animation phải cập nhật theo đường đi đó mà vẫn giữ chuyển động ổn định.

## Đầu vào (input / 입력) độ trễ (latency / 지연 시간)

Độ trễ (latency / 지연 시간) đường dẫn (path / 경로) từ vật lý (physical / 물리적) đầu vào (input / 입력) → OS sự kiện (event / 이벤트) → game lô-gic (logic / 논리) → kết xuất (render / 렌더링) → display scanout. tối ưu hóa (optimization / 최적화) chỉ rendering không đủ nếu sự kiện (event / 이벤트) hàng đợi (queue / 큐) hoặc buffering thêm delay.

Competitive/VR các hệ thống (systems / 시스템들) nhạy với end-to-end motion-to-photon/input-to-photon độ trễ (latency / 지연 시간).

Animation nội suy trạng thái theo thời gian; audio cũng là dữ liệu lấy mẫu theo thời gian. Hai đường thời gian này phải được đồng bộ khi media có cả hình và tiếng.

## Animation

Keyframe animation định nghĩa states tại times rồi interpolate. Skeletal animation dùng bones + skinning weights để deform mesh.

Interpolation tuyến tính (linear / 선형) dễ tính nhưng orientation thường dùng quaternions/slerp để tránh artifacts của Euler angle interpolation.

Sampling rate và bit depth quyết định audio được biểu diễn ra sao; playback còn phải ghép clock audio với clock video để tránh drift.

## Audio sampling

Digital audio mẫu (sample / 표본) amplitude theo thời gian. mẫu (sample / 표본) tỷ lệ (rate / 비율) cần đủ cho frequency band; 44.1/48 kHz phổ biến cho human-audible phạm vi (range / 범위) với filter các giả định (assumptions / 가정들).

Bit độ sâu (depth / 깊이) ảnh hưởng quantization động (dynamic / 동적) phạm vi (range / 범위)/noise. Compression codecs exploit psychoacoustic redundancy.

Đồng bộ A/V xử lý sai khác clock và jitter bằng buffering, resampling hoặc điều chỉnh frame. Video compression lại tạo dependency giữa các frame, ảnh hưởng seek và khả năng khôi phục khi mất dữ liệu.

## Audio/video synchronization

Audio clock và video/kết xuất (render / 렌더링) clock có thể drift. Playback các hệ thống (systems / 시스템들) buffer và resample/drop/repeat frames để giữ A/V sync.

Mạng (network / 네트워크) streaming thêm jitter; jitter buffer đổi độ trễ (latency / 지연 시간) lấy smooth playback.

GOP và motion prediction đổi băng thông lấy dependency và độ trễ giải mã. Đánh đổi đó phải được đánh giá trong deadline của ứng dụng, không chỉ bằng tốc độ giải mã trung bình.

## Video compression intuition

Video codec không encode mỗi frame độc lập hoàn toàn. Intra frames encode spatial cấu trúc (structure / 구조); inter frames exploit temporal similarity bằng motion prediction/residual.

Mất mát (loss / 손실) hoặc seek hành vi (behavior / 동작) phụ thuộc phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조) giữa frames, giải thích keyframes/GOP.

Real-time nghĩa là đáp ứng deadline đã cam kết, không phải luôn chạy nhanh nhất. Những ngộ nhận sau đây thường nhầm throughput với tính đúng đắn theo thời gian.

## Real-time vs fast

Real-time không nhất thiết nghĩa cực nhanh; nó nghĩa đáp ứng deadline các ràng buộc (constraints / 제약조건들). Hard real-time miss deadline có thể catastrophic; soft real-time miss làm chất lượng (quality / 품질) degrade.

Games/video lời gọi (call / 호출) thường soft real-time; industrial điều khiển (control / 제어) có thể hard/firm các ràng buộc (constraints / 제약조건들).

Các ví dụ trên cùng chỉ về một nguyên tắc: media pipeline phải giữ cả nội dung lẫn thời điểm xuất hiện trong giới hạn deadline.

## Dùng chung (common / 공통) Misconceptions

**“FPS cao là độ trễ (latency / 지연 시간) thấp.”** Buffering/đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) có thể giữ độ trễ (latency / 지연 시간) cao dù FPS cao.

**“Real-time nghĩa chạy nhanh nhất có thể.”** Predictable deadline hành vi (behavior / 동작) quan trọng hơn peak thông lượng (throughput / 처리량).

**“Video là chuỗi JPEG.”** hiện đại (modern / 현대적) codecs exploit temporal prediction mạnh.

## Mô hình tư duy (mental model / 사고 모델)

> Interactive media là chuỗi xử lý (pipeline / 파이프라인) có deadline. tính đúng đắn (correctness / 정확성) gồm cả nội dung và thời điểm dữ liệu xuất hiện.

## Kết nối

Đọc [performance measurement](../02_computer_architecture/07_performance_power_and_hardware_measurement.md), [OS scheduling/I/O](../03_operating_systems/01_processes_threads_and_scheduling.md), [graphics](./02_computer_graphics_pipeline_and_geometry.md) và [network congestion](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
