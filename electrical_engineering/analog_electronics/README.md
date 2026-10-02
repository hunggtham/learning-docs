# Analog Electronics — Điện tử tương tự

> **Mạch đọc:** README này là owner của **Analog Electronics — Điện tử tương tự**. Route đi từ bias và small-signal model → gain, feedback và frequency response → noise, stability và non-idealities → data converters, sensing và actuation → đo kiểm, để tín hiệu liên tục được nối với thiết kế thực.

Analog electronics biến tín hiệu (signal / 신호) liên tục thành gain, filtering, sensing và actuation có thể thiết kế. Trọng tâm là độ lệch (bias / 편향) điểm (point / 지점), small-signal mô hình (model / 모델), phản hồi (feedback / 피드백), noise và stability dưới non-idealities.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
diode → BJT/MOSFET stages → biasing → op-amp/feedback → filters → ADC/DAC front-end
```

> **Chuyển mạch:** Trong **Analog Electronics — Điện tử tương tự**, **Cốt lõi (core / 핵심) chapter** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) tuyến (route / 경로)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cần nắm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cốt lõi (core / 핵심) chapter

- [Device biasing and feedback](00_device_biasing_feedback.md) — operating điểm (point / 지점), small-signal gain, phản hồi (feedback / 피드백), stability, noise và sensor front-end.
- [Data converters and noise budget](01_data_converters_noise_budget.md) — ADC/DAC, ENOB, tham chiếu (reference / 참조), settling và lỗi (error / 오류) allocation.

> **Chuyển mạch:** Ở chặng này của **Analog Electronics — Điện tử tương tự**, **Cần nắm** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) chapter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cần nắm

- operating region và tải (load / 로드) line;
- gain, đầu vào (input / 입력)/đầu ra (output / 출력) impedance, bandwidth và slew tỷ lệ (rate / 비율);
- negative phản hồi (feedback / 피드백), vòng lặp (loop / 루프) gain, phase margin và oscillation;
- thermal noise, shot noise, offset, drift và động (dynamic / 동적) phạm vi (range / 범위);
- anti-alias filter, sample-and-hold, tham chiếu (reference / 참조) và converter errors.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Analog Electronics — Điện tử tương tự**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Cần nắm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

MOSFET/semiconductor physics thuộc [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md); cách chọn topology, độ lệch (bias / 편향), compensation và verify thuộc nhánh này. Đi tiếp sang [digital electronics](../digital_electronics/README.md) ở converter ranh giới (boundary / 경계).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
