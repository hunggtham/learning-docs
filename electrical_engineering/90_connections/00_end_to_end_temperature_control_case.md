# End-to-End Case — Temperature Instrumentation and Control

Case này nối cả chín nhánh trong một hệ nhỏ: đo nhiệt độ, biến đổi analog, sampling, điều khiển, power stage, firmware timing và hardware/software recovery. Số liệu là giả định để luyện reasoning; không dùng thay cho thiết kế safety-certified.

## 1. Requirement và boundary

Mục tiêu:

- giữ nhiệt độ chamber ở reference 60 °C;
- dải vận hành 0–100 °C;
- steady-state error dưới 1 °C trong điều kiện nominal;
- không overshoot quá 5 °C;
- sample sensor 100 Hz, update heater 10 Hz;
- khi sensor invalid, over-temperature hoặc watchdog fault, heater phải về OFF.

Boundary gồm sensor, analog front-end, ADC, MCU, PWM/MOSFET, heater, chamber và telemetry. Không đưa laptop/UI vào safety boundary; UI chỉ là observer.

## 2. Sensor và analog front-end

Giả sử sensor có output 0–1.0 V cho 0–100 °C. Chọn non-inverting amplifier gain 2.8 để output 0–2.8 V, chừa headroom dưới ADC 3.3 V.

ADC 12-bit có LSB lý tưởng:

    LSB = 3.3 V / 4096 ≈ 0.806 mV

Sau gain, 1 °C tương ứng 28 mV; lượng tử hóa lý tưởng tương đương khoảng 0.029 °C ở sensor output. Nhưng accuracy thật còn phụ thuộc sensor calibration, op-amp offset/drift, resistor ratio, reference và noise.

Nếu sensor source impedance và ADC acquisition capacitor tạo settling error, cần buffer hoặc tăng acquisition time. Đây là lý do không thể chọn ADC chỉ bằng số bit.

## 3. Sampling và filtering

Thermal plant chậm nên signal hữu ích dưới 1 Hz, nhưng chọn sample 100 Hz để có margin và phát hiện fault. Analog low-pass đặt corner khoảng 5 Hz; digital filter có thể giảm noise thêm nhưng phải tính latency.

Một moving average 10 mẫu ở 100 Hz thêm delay trung tâm khoảng 45 ms. Delay này nhỏ so với plant time constant 20 s nhưng phải ghi vào control model.

## 4. Plant và controller

Mô hình bậc nhất quanh operating point:

    G(s) = K / (τs + 1)

Giả sử `τ = 20 s` và `K = 0.8 °C/% duty`. Controller chạy mỗi 100 ms, dùng PI với output giới hạn 0–100% duty. Integral anti-windup bắt buộc vì warm-up thường chạm saturation.

Khi reference đổi từ 25 lên 60 °C, heater saturate lúc đầu. Test phải đo rise time, overshoot, settling và integral state sau khi rời saturation; chỉ nhìn temperature cuối cùng là không đủ.

## 5. Power stage

Heater là tải điện trở 12 V, 2 A. Low-side N-MOSFET được điều khiển bằng PWM; vì tải không cảm, flyback diode không phải phần tử chính như với motor/relay, nhưng gate resistor, pull-down, current limit và thermal derating vẫn cần.

Power path phải có:

```text
12 V input → fuse/current limit → heater → MOSFET → return
```

Independent thermal cutoff đặt ngoài MCU để xử lý MOSFET stuck-on hoặc firmware runaway. MOSFET temperature phải được tính từ conduction loss, switching loss và thermal resistance.

## 6. Firmware state machine

```text
BOOT → SELF_TEST → IDLE → HEATING → HOLD
                  ↘ FAULT ← sensor/power/watchdog fault
```

Các invariant:

- heater chỉ được enable khi ADC/reference/clock self-test pass;
- duty luôn bị clamp trong 0–100%;
- sensor range/rate/plausibility check fail thì vào FAULT;
- FAULT phải tắt output trước khi ghi telemetry;
- recovery cần explicit acknowledgement, không auto-retry vô hạn.

## 7. Timing và ownership

Task 100 Hz đọc ADC và cập nhật filtered sample. Task 10 Hz chạy PI. ISR/DMA chỉ capture conversion-complete và publish buffer. Telemetry task chạy chậm hơn và không được block control task.

Timing budget mẫu:

| Work | Period | WCET budget |
|---|---:|---:|
| ADC/DMA handling | 10 ms | 0.2 ms |
| filter + plausibility | 10 ms | 0.4 ms |
| PI + PWM update | 100 ms | 0.5 ms |
| telemetry | 1 s | 2 ms |

Đây là budget, không phải average đo một lần. Cần trace ở clock, interrupt và queue saturation gần worst case.

## 8. Telemetry và diagnostics

Mỗi record nên có timestamp, raw ADC, filtered temperature, reference, duty, state, fault code, watchdog counter, firmware version và sensor quality. Khi FAULT, ghi nguyên nhân đầu tiên và các fault đồng thời để tránh mất causal order.

## 9. Verification matrix

| Scenario | Expected evidence |
|---|---|
| Reference step 25→60 °C | rise/overshoot/settling trong budget |
| Sensor open/short | FAULT, heater OFF, diagnostic code |
| ADC stuck value | rate/plausibility detector hoạt động |
| MOSFET stuck-on | independent cutoff ngắt tải |
| Watchdog timeout | reset cause lưu, output safe |
| Queue/telemetry blocked | control deadline vẫn pass |
| Brownout trong update | image cũ hoặc image mới hợp lệ, không boot dở |
| Ambient/load thay đổi | stability và thermal margin còn đủ |

## 10. Kết luận thiết kế

Case cho thấy bridge không phải chuỗi tuyến tính đơn giản. ADC accuracy ảnh hưởng control quality; filter latency ảnh hưởng phase margin; power fault cần hardware protection ngoài software; driver/telemetry phải biểu diễn uncertainty và state. Một end-to-end review phải đi qua cả signal, power, timing, control và recovery budget.

## Liên kết

- [Circuit analysis](../circuits/00_circuit_analysis_and_measurement.md)
- [Analog biasing and feedback](../analog_electronics/00_device_biasing_feedback.md)
- [Data converters](../analog_electronics/01_data_converters_noise_budget.md)
- [Sampling and filtering](../signals_and_systems/00_lti_sampling_filtering.md)
- [Feedback and PID](../control_systems/00_feedback_stability_pid.md)
- [MCU real-time](../embedded_systems/00_mcu_runtime_real_time.md)
- [Power protection](../power_electronics/00_switching_converters_protection.md)
- [Driver contracts](../hardware_software_interfaces/00_register_bus_driver_contracts.md)
