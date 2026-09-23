# Lab and Measurement Checklist — Đo kiểm có thể lặp lại

Một waveform đẹp không phải evidence đủ. Measurement phải ghi rõ setup, probe, bandwidth, reference, calibration, sample rate và điều kiện tải để người khác tái hiện được.

## 1. Oscilloscope

- Ghi probe ratio, bandwidth limit, sample rate, record length và trigger.
- Dùng short ground spring ở switch node; ground lead dài có thể tạo ringing giả.
- Chụp cả startup, steady state, shutdown và fault transition.
- Đo peak, RMS, frequency, overshoot và settling bằng cùng time/voltage scale.
- Không nối earth-referenced ground clip vào node floating hoặc high-side nếu chưa phân tích safety.

## 2. Logic analyzer

- Chọn sample rate đủ lớn so với fastest edge cần kiểm tra, không chỉ so với bit rate.
- Ghi protocol decoder version và threshold voltage.
- Kiểm tra framing, ACK/NACK, timeout, repeated start, reset giữa transaction và bus contention.
- Correlate timestamp với oscilloscope hoặc firmware trace; hai thiết bị có thể có clock khác nhau.

## 3. Power measurement

- Đo input voltage ngay tại DUT, không chỉ ở bench supply.
- Tách average, peak, inrush, sleep và transient load.
- Dùng shunt/current probe có bandwidth và burden phù hợp.
- Tính cả conversion loss, thermal rise và derating ở ambient khác nhau.
- Kiểm tra current-limit behavior và energy còn lại sau fault.

## 4. HIL và fault injection

HIL không chỉ replay happy-path sensor. Tối thiểu cần inject:

```text
sensor open/short/out-of-range
ADC stuck/noisy
clock drift/jitter
DMA/queue full
bus timeout/NACK
brownout/reset giữa transaction
actuator stuck-on/stuck-off
```

Mỗi test cần expected safe state, deadline, fault code, recovery policy và evidence artifact.

## 5. Measurement record

Một record tối thiểu có:

| Trường | Ví dụ |
|---|---|
| DUT revision | board-A rev2 |
| firmware/config | fw 1.4, control Kp/Ki |
| supply/load | 12.0 V, 1.8 A, 25 °C |
| instrument | scope model, probe, calibration date |
| setup | ground point, cable, termination |
| result | pass/fail, raw file, interpretation |

Không sửa waveform bằng smoothing rồi coi đó là raw evidence. Nếu có post-processing, giữ raw capture và ghi rõ transform.

## Bridge

Dùng checklist này cho [end-to-end temperature control case](00_end_to_end_temperature_control_case.md), rồi quay lại từng nhánh để map measurement tới circuit, control, power và firmware contract.
