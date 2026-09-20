# Multimedia, animation và interactive systems

Interactive media kết hợp rendering, audio/video, input, timing và concurrency. Khác batch computation, một frame đúng nhưng đến muộn vẫn tạo trải nghiệm sai. Vì vậy real-time systems cần reasoning về deadlines, buffering và synchronization.

## Frame rate và frame time

60 frames/second cho budget khoảng:

\[
1000/60 \approx 16.67\ ms/frame
\]

120 FPS chỉ còn khoảng 8.33 ms. Nếu CPU simulation + GPU render vượt budget, frame miss và stutter xảy ra.

Average FPS có thể cao nhưng frame-time spikes vẫn khó chịu; distribution/pacing quan trọng.

## Game/render loop

Loop đơn giản:

```text
process input
update simulation
render
present
repeat
```

Simulation timestep có thể variable theo frame delta hoặc fixed timestep. Fixed timestep ổn định physics/determinism hơn; rendering có thể interpolate giữa simulation states.

## Double buffering

Nếu display đọc framebuffer trong khi GPU đang viết, tearing/inconsistent frame có thể xảy ra. Double buffering dùng front buffer để display và back buffer để render rồi swap.

VSync đồng bộ present với display refresh để giảm tearing nhưng có latency trade-offs.

## Input latency

Latency path từ physical input → OS event → game logic → render → display scanout. Optimization chỉ rendering không đủ nếu event queue hoặc buffering thêm delay.

Competitive/VR systems nhạy với end-to-end motion-to-photon/input-to-photon latency.

## Animation

Keyframe animation định nghĩa states tại times rồi interpolate. Skeletal animation dùng bones + skinning weights để deform mesh.

Interpolation linear dễ tính nhưng orientation thường dùng quaternions/slerp để tránh artifacts của Euler angle interpolation.

## Audio sampling

Digital audio sample amplitude theo thời gian. Sample rate cần đủ cho frequency band; 44.1/48 kHz phổ biến cho human-audible range với filter assumptions.

Bit depth ảnh hưởng quantization dynamic range/noise. Compression codecs exploit psychoacoustic redundancy.

## Audio/video synchronization

Audio clock và video/render clock có thể drift. Playback systems buffer và resample/drop/repeat frames để giữ A/V sync.

Network streaming thêm jitter; jitter buffer đổi latency lấy smooth playback.

## Video compression intuition

Video codec không encode mỗi frame độc lập hoàn toàn. Intra frames encode spatial structure; inter frames exploit temporal similarity bằng motion prediction/residual.

Loss hoặc seek behavior phụ thuộc dependency structure giữa frames, giải thích keyframes/GOP.

## Real-time vs fast

Real-time không nhất thiết nghĩa cực nhanh; nó nghĩa đáp ứng deadline constraints. Hard real-time miss deadline có thể catastrophic; soft real-time miss làm quality degrade.

Games/video call thường soft real-time; industrial control có thể hard/firm constraints.

## Common Misconceptions

**“FPS cao là latency thấp.”** Buffering/input pipeline có thể giữ latency cao dù FPS cao.

**“Real-time nghĩa chạy nhanh nhất có thể.”** Predictable deadline behavior quan trọng hơn peak throughput.

**“Video là chuỗi JPEG.”** Modern codecs exploit temporal prediction mạnh.

## Mental Model

> Interactive media là pipeline có deadline. Correctness gồm cả nội dung và thời điểm dữ liệu xuất hiện.

## Kết nối

Đọc [performance measurement](../02_computer_architecture/07_performance_power_and_hardware_measurement.md), [OS scheduling/I/O](../03_operating_systems/01_processes_threads_and_scheduling.md), [graphics](./02_computer_graphics_pipeline_and_geometry.md) và [network congestion](../06_networks_distributed_systems/02_transport_tcp_udp_and_congestion.md).