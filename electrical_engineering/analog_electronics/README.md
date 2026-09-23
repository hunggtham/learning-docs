# Analog Electronics — Điện tử tương tự

Analog electronics biến signal liên tục thành gain, filtering, sensing và actuation có thể thiết kế. Trọng tâm là bias point, small-signal model, feedback, noise và stability dưới non-idealities.

## Core route

```text
diode → BJT/MOSFET stages → biasing → op-amp/feedback → filters → ADC/DAC front-end
```

## Core chapter

- [Device biasing and feedback](00_device_biasing_feedback.md) — operating point, small-signal gain, feedback, stability, noise và sensor front-end.
- [Data converters and noise budget](01_data_converters_noise_budget.md) — ADC/DAC, ENOB, reference, settling và error allocation.

## Cần nắm

- operating region và load line;
- gain, input/output impedance, bandwidth và slew rate;
- negative feedback, loop gain, phase margin và oscillation;
- thermal noise, shot noise, offset, drift và dynamic range;
- anti-alias filter, sample-and-hold, reference và converter errors.

## Bridge

MOSFET/semiconductor physics thuộc [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md); cách chọn topology, bias, compensation và verify thuộc nhánh này. Đi tiếp sang [digital electronics](../digital_electronics/README.md) ở converter boundary.
