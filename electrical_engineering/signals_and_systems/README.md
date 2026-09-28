# Signals and các hệ thống (systems / 시스템들) — Tín hiệu và hệ thống

> **Mạch đọc:** Đọc **Signals and các hệ thống (systems / 시스템들) — Tín hiệu và hệ thống** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Nhánh này cung cấp ngôn ngữ chung cho sensor, audio, điều khiển (control / 제어) và communication: tín hiệu (signal / 신호) là gì, hệ thống (system / 시스템) biến đổi tín hiệu (signal / 신호) ra sao, thông tin (information / 정보) nào bị mất và sampling/filtering tạo artefact nào.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
LTI systems → convolution → Fourier/Laplace/Z → sampling → filters → estimation
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter

- [LTI, sampling and filtering](00_lti_sampling_filtering.md) — poles/zeros, aliasing, ADC quantization, FIR/IIR và đo PSD.
- [Transforms and estimation](01_transforms_and_estimation.md) — Laplace/Z, matched filter, trạng thái (state / 상태) estimation, covariance và sensor fusion.


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm

- continuous/discrete thời gian (time / 시간), năng lượng (energy / 에너지)/power tín hiệu (signal / 신호) và state-space intuition;
- impulse phản hồi (response / 응답), convolution, poles/zeros và stability;
- spectrum, bandwidth, phase/group delay và aliasing;
- FIR/IIR, quantization, ADC/DAC và noise shaping;
- SNR, PSD, correlation, detection và bất định (uncertainty / 불확실성).


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Nền wave/Fourier có ở [Physics — waves, Fourier và âm thanh](../../physics/02_oscillations_waves/01_waves_fourier_sound.md); nhánh này hướng vào hệ thống (system / 시스템) thiết kế (design / 설계) và đo lường (measurement / 측정). Đi tiếp sang [communication systems](../communication_systems/README.md) hoặc [control systems](../control_systems/README.md).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 lti sampling filtering](./00_lti_sampling_filtering.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
