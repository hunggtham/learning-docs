# Signals and các hệ thống (systems / 시스템들) — Tín hiệu và hệ thống

> **Mạch đọc:** README này là owner của **Signals and các hệ thống (systems / 시스템들) — Tín hiệu và hệ thống**. Route đi từ signal/system abstraction → LTI, sampling và filtering → transforms, estimation và control → sensor/audio/communication applications → noise, bandwidth và measurement, để các chapter dùng chung một ngôn ngữ toán–kỹ thuật.

Nhánh này cung cấp ngôn ngữ chung cho sensor, audio, điều khiển (control / 제어) và communication: tín hiệu (signal / 신호) là gì, hệ thống (system / 시스템) biến đổi tín hiệu (signal / 신호) ra sao, thông tin (information / 정보) nào bị mất và sampling/filtering tạo artefact nào.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
LTI systems → convolution → Fourier/Laplace/Z → sampling → filters → estimation
```

> **Chuyển mạch:** Trong **Signals and các hệ thống (systems / 시스템들) — Tín hiệu và hệ thống**, **Cốt lõi (core / 핵심) chapter** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) tuyến (route / 경로)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cần nắm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cốt lõi (core / 핵심) chapter

- [LTI, sampling and filtering](00_lti_sampling_filtering.md) — poles/zeros, aliasing, ADC quantization, FIR/IIR và đo PSD.
- [Transforms and estimation](01_transforms_and_estimation.md) — Laplace/Z, matched filter, trạng thái (state / 상태) estimation, covariance và sensor fusion.

> **Chuyển mạch:** Ở chặng này của **Signals and các hệ thống (systems / 시스템들) — Tín hiệu và hệ thống**, **Cần nắm** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) chapter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cần nắm

- continuous/discrete thời gian (time / 시간), năng lượng (energy / 에너지)/power tín hiệu (signal / 신호) và state-space intuition;
- impulse phản hồi (response / 응답), convolution, poles/zeros và stability;
- spectrum, bandwidth, phase/group delay và aliasing;
- FIR/IIR, quantization, ADC/DAC và noise shaping;
- SNR, PSD, correlation, detection và bất định (uncertainty / 불확실성).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Signals and các hệ thống (systems / 시스템들) — Tín hiệu và hệ thống**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Cần nắm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Nền wave/Fourier có ở [Physics — waves, Fourier và âm thanh](../../physics/02_oscillations_waves/01_waves_fourier_sound.md); nhánh này hướng vào hệ thống (system / 시스템) thiết kế (design / 설계) và đo lường (measurement / 측정). Đi tiếp sang [communication systems](../communication_systems/README.md) hoặc [control systems](../control_systems/README.md).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
