# Control Systems — Hệ thống điều khiển

Control systems biến measurement thành action để giữ plant trong vùng mong muốn dưới disturbance, uncertainty và delay. Feedback không tự động làm hệ tốt hơn: gain, phase, saturation và sensor failure có thể tạo instability.

## Core route

```text
plant/sensor/actuator → transfer function → stability → PID → state-space → observer → digital/safety control
```

## Core chapter

- [Feedback, stability and PID](00_feedback_stability_pid.md) — closed-loop sensitivity, poles, phase margin, saturation, anti-windup và digital control.
- [State-space and discrete control](01_state_space_discrete_control.md) — controllability, observability, discretization, deadline và HIL verification.

## Cần nắm

- open-loop vs closed-loop, reference, error và disturbance;
- poles/zeros, Bode/Nyquist/root locus và stability margin;
- PID tuning, anti-windup, saturation, rate limit và feedforward;
- controllability/observability, state estimator và sensor fusion;
- sampling, discretization, latency, fail-safe state và verification.

## Bridge

Nền toán học nối với [mathematics](../../mathematics/README.md), còn controller chạy trên [embedded systems](../embedded_systems/README.md). Với hệ safety-critical, thêm requirements/test evidence thay vì chỉ tune waveform đẹp.
