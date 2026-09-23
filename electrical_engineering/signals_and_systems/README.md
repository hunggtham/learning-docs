# Signals and Systems — Tín hiệu và hệ thống

Nhánh này cung cấp ngôn ngữ chung cho sensor, audio, control và communication: signal là gì, system biến đổi signal ra sao, information nào bị mất và sampling/filtering tạo artefact nào.

## Core route

```text
LTI systems → convolution → Fourier/Laplace/Z → sampling → filters → estimation
```

## Core chapter

- [LTI, sampling and filtering](00_lti_sampling_filtering.md) — poles/zeros, aliasing, ADC quantization, FIR/IIR và đo PSD.
- [Transforms and estimation](01_transforms_and_estimation.md) — Laplace/Z, matched filter, state estimation, covariance và sensor fusion.

## Cần nắm

- continuous/discrete time, energy/power signal và state-space intuition;
- impulse response, convolution, poles/zeros và stability;
- spectrum, bandwidth, phase/group delay và aliasing;
- FIR/IIR, quantization, ADC/DAC và noise shaping;
- SNR, PSD, correlation, detection và uncertainty.

## Bridge

Nền wave/Fourier có ở [Physics — waves, Fourier và âm thanh](../../physics/02_oscillations_waves/01_waves_fourier_sound.md); nhánh này hướng vào system design và measurement. Đi tiếp sang [communication systems](../communication_systems/README.md) hoặc [control systems](../control_systems/README.md).
