# Multimedia, animation và interactive các hệ thống (systems / 시스템들)

> **Mạch đọc:** Đọc **Multimedia, animation và interactive các hệ thống (systems / 시스템들)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Frame tỷ lệ (rate / 비율) và frame thời gian (time / 시간)** sang **Game/kết xuất (render / 렌더링) vòng lặp (loop / 루프)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Interactive media kết hợp rendering, audio/video, đầu vào (input / 입력), timing và tính đồng thời (concurrency / 동시성). Khác batch computation, một frame đúng nhưng đến muộn vẫn tạo trải nghiệm sai. Vì vậy real-time các hệ thống (systems / 시스템들) cần lập luận (reasoning / 추론) về deadlines, buffering và synchronization.

## Frame tỷ lệ (rate / 비율) và frame thời gian (time / 시간)

60 frames/second cho ngân sách (budget / 예산) khoảng:

\[
1000/60 \approx 16.67\ ms/frame
\]

120 FPS chỉ còn khoảng 8.33 ms. Nếu CPU simulation + GPU kết xuất (render / 렌더링) vượt ngân sách (budget / 예산), frame miss và stutter xảy ra.

Average FPS có thể cao nhưng frame-time spikes vẫn khó chịu; phân phối (distribution / 분포)/pacing quan trọng.


> **Chuyển mạch:** Từ **Frame tỷ lệ (rate / 비율) và frame thời gian (time / 시간)**, ta sang **Game/kết xuất (render / 렌더링) vòng lặp (loop / 루프)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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


> **Chuyển mạch:** Từ **Game/kết xuất (render / 렌더링) vòng lặp (loop / 루프)**, ta sang **Double buffering** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Double buffering

Nếu display đọc framebuffer trong khi GPU đang viết, tearing/inconsistent frame có thể xảy ra. Double buffering dùng front buffer để display và back buffer để kết xuất (render / 렌더링) rồi swap.

VSync đồng bộ present với display refresh để giảm tearing nhưng có độ trễ (latency / 지연 시간) trade-offs.


> **Chuyển mạch:** Từ **Double buffering**, ta sang **đầu vào (input / 입력) độ trễ (latency / 지연 시간)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Đầu vào (input / 입력) độ trễ (latency / 지연 시간)

Độ trễ (latency / 지연 시간) đường dẫn (path / 경로) từ vật lý (physical / 물리적) đầu vào (input / 입력) → OS sự kiện (event / 이벤트) → game lô-gic (logic / 논리) → kết xuất (render / 렌더링) → display scanout. tối ưu hóa (optimization / 최적화) chỉ rendering không đủ nếu sự kiện (event / 이벤트) hàng đợi (queue / 큐) hoặc buffering thêm delay.

Competitive/VR các hệ thống (systems / 시스템들) nhạy với end-to-end motion-to-photon/input-to-photon độ trễ (latency / 지연 시간).


> **Chuyển mạch:** Từ **đầu vào (input / 입력) độ trễ (latency / 지연 시간)**, ta sang **Animation** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Animation

Keyframe animation định nghĩa states tại times rồi interpolate. Skeletal animation dùng bones + skinning weights để deform mesh.

Interpolation tuyến tính (linear / 선형) dễ tính nhưng orientation thường dùng quaternions/slerp để tránh artifacts của Euler angle interpolation.


> **Chuyển mạch:** Từ **Animation**, ta sang **Audio sampling** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Audio sampling

Digital audio mẫu (sample / 표본) amplitude theo thời gian. mẫu (sample / 표본) tỷ lệ (rate / 비율) cần đủ cho frequency band; 44.1/48 kHz phổ biến cho human-audible phạm vi (range / 범위) với filter các giả định (assumptions / 가정들).

Bit độ sâu (depth / 깊이) ảnh hưởng quantization động (dynamic / 동적) phạm vi (range / 범위)/noise. Compression codecs exploit psychoacoustic redundancy.


> **Chuyển mạch:** Từ **Audio sampling**, ta sang **Audio/video synchronization** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Audio/video synchronization

Audio clock và video/kết xuất (render / 렌더링) clock có thể drift. Playback các hệ thống (systems / 시스템들) buffer và resample/drop/repeat frames để giữ A/V sync.

Mạng (network / 네트워크) streaming thêm jitter; jitter buffer đổi độ trễ (latency / 지연 시간) lấy smooth playback.


> **Chuyển mạch:** Từ **Audio/video synchronization**, ta sang **Video compression intuition** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Video compression intuition

Video codec không encode mỗi frame độc lập hoàn toàn. Intra frames encode spatial cấu trúc (structure / 구조); inter frames exploit temporal similarity bằng motion prediction/residual.

Mất mát (loss / 손실) hoặc seek hành vi (behavior / 동작) phụ thuộc phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조) giữa frames, giải thích keyframes/GOP.


> **Chuyển mạch:** Từ **Video compression intuition**, ta sang **Real-time vs fast** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Real-time vs fast

Real-time không nhất thiết nghĩa cực nhanh; nó nghĩa đáp ứng deadline các ràng buộc (constraints / 제약조건들). Hard real-time miss deadline có thể catastrophic; soft real-time miss làm chất lượng (quality / 품질) degrade.

Games/video lời gọi (call / 호출) thường soft real-time; industrial điều khiển (control / 제어) có thể hard/firm các ràng buộc (constraints / 제약조건들).


> **Chuyển mạch:** Từ **Real-time vs fast**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“FPS cao là độ trễ (latency / 지연 시간) thấp.”** Buffering/đầu vào (input / 입력) chuỗi xử lý (pipeline / 파이프라인) có thể giữ độ trễ (latency / 지연 시간) cao dù FPS cao.

**“Real-time nghĩa chạy nhanh nhất có thể.”** Predictable deadline hành vi (behavior / 동작) quan trọng hơn peak thông lượng (throughput / 처리량).

**“Video là chuỗi JPEG.”** hiện đại (modern / 현대적) codecs exploit temporal prediction mạnh.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> Interactive media là chuỗi xử lý (pipeline / 파이프라인) có deadline. tính đúng đắn (correctness / 정확성) gồm cả nội dung và thời điểm dữ liệu xuất hiện.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc [performance measurement](../02_computer_architecture/07_performance_power_and_hardware_measurement.md), [OS scheduling/I/O](../03_operating_systems/01_processes_threads_and_scheduling.md), [graphics](./02_computer_graphics_pipeline_and_geometry.md) và [network congestion](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 hci human factors and interaction models](./00_hci_human_factors_and_interaction_models.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
