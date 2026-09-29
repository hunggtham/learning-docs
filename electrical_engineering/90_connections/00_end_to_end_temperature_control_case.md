# End-to-End trường hợp (case / 사례) — Temperature Instrumentation and điều khiển (control / 제어)

> **Mạch đọc:** Đọc **End-to-End trường hợp (case / 사례) — Temperature Instrumentation and điều khiển (control / 제어)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. yêu cầu (requirement / 요구사항) và ranh giới (boundary / 경계)** sang **2. Sensor và analog front-end**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Trường hợp (case / 사례) này nối cả chín nhánh trong một hệ nhỏ: đo nhiệt độ, biến đổi analog, sampling, điều khiển, power stage, firmware timing và hardware/software khôi phục (recovery / 복구). Số liệu là giả định để luyện lập luận (reasoning / 추론); không dùng thay cho thiết kế safety-certified.

## 1. yêu cầu (requirement / 요구사항) và ranh giới (boundary / 경계)

Mục tiêu:

- giữ nhiệt độ chamber ở tham chiếu (reference / 참조) 60 °C;
- dải vận hành 0–100 °C;
- steady-state lỗi (error / 오류) dưới 1 °C trong điều kiện nominal;
- không overshoot quá 5 °C;
- mẫu (sample / 표본) sensor 100 Hz, cập nhật (update / 업데이트) heater 10 Hz;
- khi sensor invalid, over-temperature hoặc watchdog fault, heater phải về OFF.

Ranh giới (boundary / 경계) gồm sensor, analog front-end, ADC, MCU, PWM/MOSFET, heater, chamber và telemetry. Không đưa laptop/UI vào an toàn (safety / 안전) ranh giới (boundary / 경계); UI chỉ là observer.


> **Chuyển mạch:** Từ **1. yêu cầu (requirement / 요구사항) và ranh giới (boundary / 경계)**, ta sang **2. Sensor và analog front-end** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Sensor và analog front-end

Giả sử sensor có đầu ra (output / 출력) 0–1.0 V cho 0–100 °C. Chọn non-inverting amplifier gain 2.8 để đầu ra (output / 출력) 0–2.8 V, chừa headroom dưới ADC 3.3 V.

ADC 12-bit có LSB lý tưởng:

    LSB = 3.3 V / 4096 ≈ 0.806 mV

Sau gain, 1 °C tương ứng 28 mV; lượng tử hóa lý tưởng tương đương khoảng 0.029 °C ở sensor đầu ra (output / 출력). Nhưng accuracy thật còn phụ thuộc sensor calibration, op-amp offset/drift, resistor ratio, tham chiếu (reference / 참조) và noise.

Nếu sensor nguồn (source / 소스) impedance và ADC acquisition capacitor tạo settling lỗi (error / 오류), cần buffer hoặc tăng acquisition thời gian (time / 시간). Đây là lý do không thể chọn ADC chỉ bằng số bit.


> **Chuyển mạch:** Từ **2. Sensor và analog front-end**, ta sang **3. Sampling và filtering** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Sampling và filtering

Thermal plant chậm nên tín hiệu (signal / 신호) hữu ích dưới 1 Hz, nhưng chọn mẫu (sample / 표본) 100 Hz để có margin và phát hiện fault. Analog low-pass đặt corner khoảng 5 Hz; digital filter có thể giảm noise thêm nhưng phải tính độ trễ (latency / 지연 시간).

Một moving average 10 mẫu ở 100 Hz thêm delay trung tâm khoảng 45 ms. Delay này nhỏ so với plant thời gian (time / 시간) constant 20 s nhưng phải ghi vào điều khiển (control / 제어) mô hình (model / 모델).


> **Chuyển mạch:** Từ **3. Sampling và filtering**, ta sang **4. Plant và controller** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Plant và controller

Mô hình bậc nhất quanh operating điểm (point / 지점):

    G(s) = K / (τs + 1)

Giả sử `τ = 20 s` và `K = 0.8 °C/% duty`. Controller chạy mỗi 100 ms, dùng PI với đầu ra (output / 출력) giới hạn 0–100% duty. Integral anti-windup bắt buộc vì warm-up thường chạm saturation.

Khi tham chiếu (reference / 참조) đổi từ 25 lên 60 °C, heater saturate lúc đầu. kiểm thử (test / 테스트) phải đo rise thời gian (time / 시간), overshoot, settling và integral trạng thái (state / 상태) sau khi rời saturation; chỉ nhìn temperature cuối cùng là không đủ.


> **Chuyển mạch:** Từ **4. Plant và controller**, ta sang **5. Power stage** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Power stage

Heater là tải điện trở 12 V, 2 A. Low-side N-MOSFET được điều khiển bằng PWM; vì tải không cảm, flyback diode không phải phần tử chính như với motor/relay, nhưng gate resistor, pull-down, hiện tại (current / 현재) limit và thermal derating vẫn cần.

Power đường dẫn (path / 경로) phải có:

```text
12 V input → fuse/current limit → heater → MOSFET → return
```

Independent thermal cutoff đặt ngoài MCU để xử lý MOSFET stuck-on hoặc firmware runaway. MOSFET temperature phải được tính từ conduction mất mát (loss / 손실), switching mất mát (loss / 손실) và thermal resistance.


> **Chuyển mạch:** Từ **5. Power stage**, ta sang **6. Firmware máy trạng thái (state machine / 상태 머신)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 6. Firmware máy trạng thái (state machine / 상태 머신)
Phần “6. Firmware máy trạng thái (state machine / 상태 머신)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
BOOT → SELF_TEST → IDLE → HEATING → HOLD
                  ↘ FAULT ← sensor/power/watchdog fault
```

Các bất biến (invariant / 불변식):

- heater chỉ được enable khi ADC/tham chiếu (reference / 참조)/clock self-test pass;
- duty luôn bị clamp trong 0–100%;
- sensor phạm vi (range / 범위)/tỷ lệ (rate / 비율)/plausibility check thất bại (fail / 실패) thì vào FAULT;
- FAULT phải tắt đầu ra (output / 출력) trước khi ghi telemetry;
- khôi phục (recovery / 복구) cần tường minh (explicit / 명시적) acknowledgement, không auto-retry vô hạn.


> **Chuyển mạch:** Từ **6. Firmware máy trạng thái (state machine / 상태 머신)**, ta sang **7. Timing và quyền sở hữu (ownership / 소유권)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. Timing và quyền sở hữu (ownership / 소유권)

Tác vụ (task / 작업) 100 Hz đọc ADC và cập nhật filtered mẫu (sample / 표본). tác vụ (task / 작업) 10 Hz chạy PI. ISR/DMA chỉ capture conversion-complete và publish buffer. Telemetry tác vụ (task / 작업) chạy chậm hơn và không được khối (block / 블록) điều khiển (control / 제어) tác vụ (task / 작업).

Timing ngân sách (budget / 예산) mẫu:

| công việc (work / 작업) | Period | WCET ngân sách (budget / 예산) |
|---|---:|---:|
| ADC/DMA handling | 10 ms | 0.2 ms |
| filter + plausibility | 10 ms | 0.4 ms |
| PI + PWM cập nhật (update / 업데이트) | 100 ms | 0.5 ms |
| telemetry | 1 s | 2 ms |

Đây là ngân sách (budget / 예산), không phải average đo một lần. Cần dấu vết (trace / 추적) ở clock, interrupt và hàng đợi (queue / 큐) saturation gần worst trường hợp (case / 사례).


> **Chuyển mạch:** Từ **7. Timing và quyền sở hữu (ownership / 소유권)**, ta sang **8. Telemetry và diagnostics** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. Telemetry và diagnostics

Mỗi bản ghi (record / 레코드) nên có timestamp, raw ADC, filtered temperature, tham chiếu (reference / 참조), duty, trạng thái (state / 상태), fault mã (code / 코드), watchdog counter, firmware phiên bản (version / 버전) và sensor chất lượng (quality / 품질). Khi FAULT, ghi nguyên nhân đầu tiên và các fault đồng thời để tránh mất nhân quả (causal / 인과적) thứ tự (order / 순서).


> **Chuyển mạch:** Từ **8. Telemetry và diagnostics**, ta sang **9. xác minh (verification / 확인) ma trận (matrix / 행렬)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 9. xác minh (verification / 확인) ma trận (matrix / 행렬)
Phần “9. xác minh (verification / 확인) ma trận (matrix / 행렬)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


| Scenario | Expected bằng chứng (evidence / 증거) |
|---|---|
| tham chiếu (reference / 참조) step 25→60 °C | rise/overshoot/settling trong ngân sách (budget / 예산) |
| Sensor open/short | FAULT, heater OFF, diagnostic mã (code / 코드) |
| ADC stuck giá trị (value / 값) | tỷ lệ (rate / 비율)/plausibility detector hoạt động |
| MOSFET stuck-on | independent cutoff ngắt tải |
| Watchdog hết thời gian chờ (timeout / 타임아웃) | reset cause lưu, đầu ra (output / 출력) safe |
| hàng đợi (queue / 큐)/telemetry blocked | điều khiển (control / 제어) deadline vẫn pass |
| Brownout trong cập nhật (update / 업데이트) | ảnh (image / 이미지) cũ hoặc ảnh (image / 이미지) mới hợp lệ, không boot dở |
| Ambient/tải (load / 로드) thay đổi | stability và thermal margin còn đủ |


> **Chuyển mạch:** Từ **9. xác minh (verification / 확인) ma trận (matrix / 행렬)**, ta sang **10. Kết luận thiết kế** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 10. Kết luận thiết kế

Trường hợp (case / 사례) cho thấy cầu nối (bridge / 브리지) không phải chuỗi tuyến tính đơn giản. ADC accuracy ảnh hưởng điều khiển (control / 제어) chất lượng (quality / 품질); filter độ trễ (latency / 지연 시간) ảnh hưởng phase margin; power fault cần hardware protection ngoài software; driver/telemetry phải biểu diễn bất định (uncertainty / 불확실성) và trạng thái (state / 상태). Một end-to-end rà soát (review / 검토) phải đi qua cả tín hiệu (signal / 신호), power, timing, điều khiển (control / 제어) và khôi phục (recovery / 복구) ngân sách (budget / 예산).


> **Chuyển mạch:** Từ **10. Kết luận thiết kế**, ta sang **Liên kết** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Liên kết
Phần “Liên kết” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- [Circuit analysis](../circuits/00_circuit_analysis_and_measurement.md)
- [Analog biasing and feedback](../analog_electronics/00_device_biasing_feedback.md)
- [Data converters](../analog_electronics/01_data_converters_noise_budget.md)
- [Sampling and filtering](../signals_and_systems/00_lti_sampling_filtering.md)
- [Feedback and PID](../control_systems/00_feedback_stability_pid.md)
- [MCU real-time](../embedded_systems/00_mcu_runtime_real_time.md)
- [Power protection](../power_electronics/00_switching_converters_protection.md)
- [Driver contracts](../hardware_software_interfaces/00_register_bus_driver_contracts.md)

> **Bàn giao:** Sau **Liên kết**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 glossary vi en ko](./01_glossary_vi_en_ko.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
