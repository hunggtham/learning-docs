# Điều khiển (control / 제어) các hệ thống (systems / 시스템들) — Hệ thống điều khiển

> **Mạch đọc:** README này là owner của **Điều khiển (control / 제어) các hệ thống (systems / 시스템들) — Hệ thống điều khiển**. Route đi từ plant/sensor/actuator/controller → feedback và stability → state-space, discrete control và estimation → embedded/industrial applications → saturation, delay và failure, để mỗi chapter nối đo lường với hành động.

Điều khiển (control / 제어) các hệ thống (systems / 시스템들) biến đo lường (measurement / 측정) thành hành động (action / 동작) để giữ plant trong vùng mong muốn dưới disturbance, bất định (uncertainty / 불확실성) và delay. phản hồi (feedback / 피드백) không tự động làm hệ tốt hơn: gain, phase, saturation và sensor thất bại (failure / 실패) có thể tạo instability.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
plant/sensor/actuator → transfer function → stability → PID → state-space → observer → digital/safety control
```

> **Chuyển mạch:** **Cốt lõi tuyến** đi từ mô hình động lực đến feedback, stability và PID; **Cốt lõi chapter** giải thích cơ chế, còn **Cần nắm** ghi lại điều kiện ổn định cần kiểm tra.

## Cốt lõi (core / 핵심) chapter

- [Feedback, stability and PID](00_feedback_stability_pid.md) — closed-loop sensitivity, poles, phase margin, saturation, anti-windup và digital điều khiển (control / 제어).
- [State-space and discrete control](01_state_space_discrete_control.md) — controllability, khả năng quan sát (observability / 관측 가능성), discretization, deadline và HIL xác minh (verification / 확인).

> **Chuyển mạch:** Sau khi hiểu mô hình và stability, **Cầu nối** đưa chúng vào tuning, actuator, deadline và verification của hệ điều khiển thật.

## Cần nắm

- open-loop vs closed-loop, tham chiếu (reference / 참조), lỗi (error / 오류) và disturbance;
- poles/zeros, Bode/Nyquist/gốc (root / 루트) locus và stability margin;
- PID tuning, anti-windup, saturation, tỷ lệ (rate / 비율) limit và feedforward;
- controllability/khả năng quan sát (observability / 관측 가능성), trạng thái (state / 상태) estimator và sensor fusion;
- sampling, discretization, độ trễ (latency / 지연 시간), fail-safe trạng thái (state / 상태) và xác minh (verification / 확인).

> **Chuyển mạch:** **Cầu nối** khép README bằng trade-off giữa đáp ứng, ổn định và chi phí triển khai; đó là tiêu chí chọn chapter tiếp theo.

## Cầu nối (bridge / 브리지)

Nền toán học nối với [mathematics](../../mathematics/README.md), còn controller chạy trên [embedded systems](../embedded_systems/README.md). Với hệ safety-critical, thêm requirements/kiểm thử (test / 테스트) bằng chứng (evidence / 증거) thay vì chỉ tune waveform đẹp.

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
