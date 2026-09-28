# Analog Electronics — Điện tử tương tự

> **Mạch đọc:** Đọc **Analog Electronics — Điện tử tương tự** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Analog electronics biến tín hiệu (signal / 신호) liên tục thành gain, filtering, sensing và actuation có thể thiết kế. Trọng tâm là độ lệch (bias / 편향) điểm (point / 지점), small-signal mô hình (model / 모델), phản hồi (feedback / 피드백), noise và stability dưới non-idealities.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
diode → BJT/MOSFET stages → biasing → op-amp/feedback → filters → ADC/DAC front-end
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter

- [Device biasing and feedback](00_device_biasing_feedback.md) — operating điểm (point / 지점), small-signal gain, phản hồi (feedback / 피드백), stability, noise và sensor front-end.
- [Data converters and noise budget](01_data_converters_noise_budget.md) — ADC/DAC, ENOB, tham chiếu (reference / 참조), settling và lỗi (error / 오류) allocation.


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm

- operating region và tải (load / 로드) line;
- gain, đầu vào (input / 입력)/đầu ra (output / 출력) impedance, bandwidth và slew tỷ lệ (rate / 비율);
- negative phản hồi (feedback / 피드백), vòng lặp (loop / 루프) gain, phase margin và oscillation;
- thermal noise, shot noise, offset, drift và động (dynamic / 동적) phạm vi (range / 범위);
- anti-alias filter, sample-and-hold, tham chiếu (reference / 참조) và converter errors.


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

MOSFET/semiconductor physics thuộc [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md); cách chọn topology, độ lệch (bias / 편향), compensation và verify thuộc nhánh này. Đi tiếp sang [digital electronics](../digital_electronics/README.md) ở converter ranh giới (boundary / 경계).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 device biasing feedback](./00_device_biasing_feedback.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
