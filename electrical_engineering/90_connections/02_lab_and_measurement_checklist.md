# Lab and đo lường (measurement / 측정) Checklist — Đo kiểm có thể lặp lại

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Lab and đo lường (measurement / 측정) Checklist — Đo kiểm có thể lặp lại**. Route đi từ oscilloscope và logic analyzer → probe, bandwidth, sampling và trigger → calibration, reference và tải → ghi nhận waveform, uncertainty và tái lập → kết luận đo, để checklist biến phép đo thành bằng chứng có thể lặp lại.

Một waveform đẹp không phải bằng chứng (evidence / 증거) đủ. đo lường (measurement / 측정) phải ghi rõ setup, probe, bandwidth, tham chiếu (reference / 참조), calibration, mẫu (sample / 표본) tỷ lệ (rate / 비율) và điều kiện tải để người khác tái hiện được.

## 1. Oscilloscope

- Ghi probe ratio, bandwidth limit, mẫu (sample / 표본) tỷ lệ (rate / 비율), bản ghi (record / 레코드) length và trigger.
- Dùng short ground spring ở switch nút (node / 노드); ground lead dài có thể tạo ringing giả.
- Chụp cả startup, steady trạng thái (state / 상태), shutdown và fault chuyển tiếp (transition / 전이).
- Đo peak, RMS, frequency, overshoot và settling bằng cùng thời gian (time / 시간)/voltage quy mô (scale / 규모).
- Không nối earth-referenced ground clip vào nút (node / 노드) floating hoặc high-side nếu chưa phân tích an toàn (safety / 안전).

> **Chuyển mạch:** **1. Oscilloscope** cho dạng sóng và thời gian; **2. Logic analyzer** đọc trạng thái số, rồi **3. Power measurement** kiểm tra nguồn và nhiễu gây sai cả hai phép đo.

## 2. lô-gic (logic / 논리) analyzer

- Chọn mẫu (sample / 표본) tỷ lệ (rate / 비율) đủ lớn so với fastest edge cần kiểm tra, không chỉ so với bit tỷ lệ (rate / 비율).
- Ghi giao thức (protocol / 프로토콜) decoder phiên bản (version / 버전) và threshold voltage.
- Kiểm tra framing, ACK/NACK, hết thời gian chờ (timeout / 타임아웃), repeated start, reset giữa giao dịch (transaction / 트랜잭션) và bus contention.
- Correlate timestamp với oscilloscope hoặc firmware dấu vết (trace / 추적); hai thiết bị có thể có clock khác nhau.

> **Chuyển mạch:** Ở chặng này của **Lab and đo lường (measurement / 측정) Checklist — Đo kiểm có thể lặp lại**, **2. lô-gic (logic / 논리) analyzer** nêu điều cần giải thích; **3. Power đo lường (measurement / 측정)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **4. HIL và fault injection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Power đo lường (measurement / 측정)

- Đo đầu vào (input / 입력) voltage ngay tại DUT, không chỉ ở bench supply.
- Tách average, peak, inrush, sleep và transient tải (load / 로드).
- Dùng shunt/hiện tại (current / 현재) probe có bandwidth và burden phù hợp.
- Tính cả conversion mất mát (loss / 손실), thermal rise và derating ở ambient khác nhau.
- Kiểm tra current-limit hành vi (behavior / 동작) và năng lượng (energy / 에너지) còn lại sau fault.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Lab and đo lường (measurement / 측정) Checklist — Đo kiểm có thể lặp lại**, **3. Power đo lường (measurement / 측정)** nêu điều cần giải thích; **4. HIL và fault injection** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **5. đo lường (measurement / 측정) bản ghi (record / 레코드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

Mỗi kiểm thử (test / 테스트) cần expected safe trạng thái (state / 상태), deadline, fault mã (code / 코드), khôi phục (recovery / 복구) chính sách (policy / 정책) và bằng chứng (evidence / 증거) sản phẩm tạo ra (artifact / 산출물).

> **Chuyển mạch:** Trong **Lab and đo lường (measurement / 측정) Checklist — Đo kiểm có thể lặp lại**, **4. HIL và fault injection** nêu điều cần giải thích; **5. đo lường (measurement / 측정) bản ghi (record / 레코드)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. đo lường (measurement / 측정) bản ghi (record / 레코드)

Một bản ghi (record / 레코드) tối thiểu có:

| Trường | Ví dụ |
|---|---|
| DUT revision | board-A rev2 |
| firmware/cấu hình (config / 설정) | fw 1.4, điều khiển (control / 제어) Kp/Ki |
| supply/tải (load / 로드) | 12.0 V, 1.8 A, 25 °C |
| instrument | phạm vi (scope / 범위) mô hình (model / 모델), probe, calibration date |
| setup | ground điểm (point / 지점), cable, termination |
| kết quả (result / 결과) | pass/thất bại (fail / 실패), raw tệp (file / 파일), interpretation |

Không sửa waveform bằng smoothing rồi coi đó là raw bằng chứng (evidence / 증거). Nếu có post-processing, giữ raw capture và ghi rõ transform.

> **Chuyển mạch:** **5. Measurement record** biến phép đo thành bằng chứng có thể lặp; **Cầu nối** chỉ cách bàn giao record, điều kiện và sai số sang lần debug sau.

## Cầu nối (bridge / 브리지)

Dùng checklist này cho [end-to-end temperature control case](00_end_to_end_temperature_control_case.md), rồi quay lại từng nhánh để map đo lường (measurement / 측정) tới circuit, điều khiển (control / 제어), power và firmware đặc tả hợp đồng (contract / 계약).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
