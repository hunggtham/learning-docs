# Điều khiển (control / 제어) các hệ thống (systems / 시스템들) — Hệ thống điều khiển

> **Mạch đọc:** Đọc **điều khiển (control / 제어) các hệ thống (systems / 시스템들) — Hệ thống điều khiển** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Điều khiển (control / 제어) các hệ thống (systems / 시스템들) biến đo lường (measurement / 측정) thành hành động (action / 동작) để giữ plant trong vùng mong muốn dưới disturbance, bất định (uncertainty / 불확실성) và delay. phản hồi (feedback / 피드백) không tự động làm hệ tốt hơn: gain, phase, saturation và sensor thất bại (failure / 실패) có thể tạo instability.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
plant/sensor/actuator → transfer function → stability → PID → state-space → observer → digital/safety control
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter

- [Feedback, stability and PID](00_feedback_stability_pid.md) — closed-loop sensitivity, poles, phase margin, saturation, anti-windup và digital điều khiển (control / 제어).
- [State-space and discrete control](01_state_space_discrete_control.md) — controllability, khả năng quan sát (observability / 관측 가능성), discretization, deadline và HIL xác minh (verification / 확인).


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm

- open-loop vs closed-loop, tham chiếu (reference / 참조), lỗi (error / 오류) và disturbance;
- poles/zeros, Bode/Nyquist/gốc (root / 루트) locus và stability margin;
- PID tuning, anti-windup, saturation, tỷ lệ (rate / 비율) limit và feedforward;
- controllability/khả năng quan sát (observability / 관측 가능성), trạng thái (state / 상태) estimator và sensor fusion;
- sampling, discretization, độ trễ (latency / 지연 시간), fail-safe trạng thái (state / 상태) và xác minh (verification / 확인).


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Nền toán học nối với [mathematics](../../mathematics/README.md), còn controller chạy trên [embedded systems](../embedded_systems/README.md). Với hệ safety-critical, thêm requirements/kiểm thử (test / 테스트) bằng chứng (evidence / 증거) thay vì chỉ tune waveform đẹp.

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 feedback stability pid](./00_feedback_stability_pid.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
