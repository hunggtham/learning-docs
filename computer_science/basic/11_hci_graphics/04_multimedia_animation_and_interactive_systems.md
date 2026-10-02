# Multimedia, animation và interactive các hệ thống (systems / 시스템들)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Multimedia, animation và interactive systems**. Route đi từ frame rate/timing → render loop/double buffering → input latency/animation → audio sampling/sync → video compression và real-time constraints, để cảm nhận tương tác gắn với deadline.

Interactive media kết hợp rendering, audio/video, đầu vào (input / 입력), timing và tính đồng thời (concurrency / 동시성). Khác batch computation, một frame đúng nhưng đến muộn vẫn tạo trải nghiệm sai. Vì vậy real-time các hệ thống (systems / 시스템들) cần lập luận (reasoning / 추론) về deadlines, buffering và synchronization.

## Frame tỷ lệ (rate / 비율) và frame thời gian (time / 시간)

60 frames/second cho ngân sách (budget / 예산) khoảng:

\[
1000/60 \approx 16.67\ ms/frame
\]

120 FPS chỉ còn khoảng 8.33 ms. Nếu CPU simulation + GPU kết xuất (render / 렌더링) vượt ngân sách (budget / 예산), frame miss và stutter xảy ra.

Average FPS có thể cao nhưng frame-time spikes vẫn khó chịu; phân phối (distribution / 분포)/pacing quan trọng.

> **Chuyển mạch:** Trong **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Game/kết xuất (render / 렌더링) vòng lặp (loop / 루프)** tiếp nhận điểm tựa từ **Frame tỷ lệ (rate / 비율) và frame thời gian (time / 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Double buffering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Double buffering** tiếp nhận điểm tựa từ **Game/kết xuất (render / 렌더링) vòng lặp (loop / 루프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đầu vào (input / 입력) độ trễ (latency / 지연 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Double buffering

Nếu display đọc framebuffer trong khi GPU đang viết, tearing/inconsistent frame có thể xảy ra. Double buffering dùng front buffer để display và back buffer để kết xuất (render / 렌더링) rồi swap.

VSync đồng bộ present với display refresh để giảm tearing nhưng có độ trễ (latency / 지연 시간) trade-offs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Đầu vào (input / 입력) độ trễ (latency / 지연 시간)** tiếp nhận điểm tựa từ **Double buffering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Animation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đầu vào (input / 입력) độ trễ (latency / 지연 시간)

Độ trễ (latency / 지연 시간) đường dẫn (path / 경로) từ vật lý (physical / 물리적) đầu vào (input / 입력) → OS sự kiện (event / 이벤트) → game lô-gic (logic / 논리) → kết xuất (render / 렌더링) → display scanout. tối ưu hóa (optimization / 최적화) chỉ rendering không đủ nếu sự kiện (event / 이벤트) hàng đợi (queue / 큐) hoặc buffering thêm delay.

Competitive/VR các hệ thống (systems / 시스템들) nhạy với end-to-end motion-to-photon/input-to-photon độ trễ (latency / 지연 시간).

> **Chuyển mạch:** Trong **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Animation** tiếp nhận điểm tựa từ **Đầu vào (input / 입력) độ trễ (latency / 지연 시간)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Audio sampling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Animation

Keyframe animation định nghĩa states tại times rồi interpolate. Skeletal animation dùng bones + skinning weights để deform mesh.

Interpolation tuyến tính (linear / 선형) dễ tính nhưng orientation thường dùng quaternions/slerp để tránh artifacts của Euler angle interpolation.

> **Chuyển mạch:** Ở chặng này của **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Audio sampling** tiếp nhận điểm tựa từ **Animation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Audio/video synchronization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Audio sampling

Digital audio mẫu (sample / 표본) amplitude theo thời gian. mẫu (sample / 표본) tỷ lệ (rate / 비율) cần đủ cho frequency band; 44.1/48 kHz phổ biến cho human-audible phạm vi (range / 범위) với filter các giả định (assumptions / 가정들).

Bit độ sâu (depth / 깊이) ảnh hưởng quantization động (dynamic / 동적) phạm vi (range / 범위)/noise. Compression codecs exploit psychoacoustic redundancy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Audio/video synchronization** tiếp nhận điểm tựa từ **Audio sampling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Video compression intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Audio/video synchronization

Audio clock và video/kết xuất (render / 렌더링) clock có thể drift. Playback các hệ thống (systems / 시스템들) buffer và resample/drop/repeat frames để giữ A/V sync.

Mạng (network / 네트워크) streaming thêm jitter; jitter buffer đổi độ trễ (latency / 지연 시간) lấy smooth playback.

> **Chuyển mạch:** Trong **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Video compression intuition** tiếp nhận điểm tựa từ **Audio/video synchronization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Real-time vs fast** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Video compression intuition

Video codec không encode mỗi frame độc lập hoàn toàn. Intra frames encode spatial cấu trúc (structure / 구조); inter frames exploit temporal similarity bằng motion prediction/residual.

Mất mát (loss / 손실) hoặc seek hành vi (behavior / 동작) phụ thuộc phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조) giữa frames, giải thích keyframes/GOP.

> **Chuyển mạch:** Ở chặng này của **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Real-time vs fast** tiếp nhận điểm tựa từ **Video compression intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Real-time vs fast

Real-time không nhất thiết nghĩa cực nhanh; nó nghĩa đáp ứng deadline các ràng buộc (constraints / 제약조건들). Hard real-time miss deadline có thể catastrophic; soft real-time miss làm chất lượng (quality / 품질) degrade.

Games/video lời gọi (call / 호출) thường soft real-time; industrial điều khiển (control / 제어) có thể hard/firm các ràng buộc (constraints / 제약조건들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Real-time vs fast** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“FPS cao là độ trễ (latency / 지연 시간) thấp.”** Buffering/đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) có thể giữ độ trễ (latency / 지연 시간) cao dù FPS cao.

**“Real-time nghĩa chạy nhanh nhất có thể.”** Predictable deadline hành vi (behavior / 동작) quan trọng hơn peak thông lượng (throughput / 처리량).

**“Video là chuỗi JPEG.”** hiện đại (modern / 현대적) codecs exploit temporal prediction mạnh.

> **Chuyển mạch:** Trong **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Interactive media là chuỗi xử lý (pipeline / 파이프라인) có deadline. tính đúng đắn (correctness / 정확성) gồm cả nội dung và thời điểm dữ liệu xuất hiện.

> **Chuyển mạch:** Ở chặng này của **Multimedia, animation và interactive các hệ thống (systems / 시스템들)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [performance measurement](../02_computer_architecture/07_performance_power_and_hardware_measurement.md), [OS scheduling/I/O](../03_operating_systems/01_processes_threads_and_scheduling.md), [graphics](./02_computer_graphics_pipeline_and_geometry.md) và [network congestion](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
