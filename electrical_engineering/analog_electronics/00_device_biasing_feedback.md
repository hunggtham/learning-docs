# Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**. Route đi từ DC bias và operating region → small-signal gain → feedback, bandwidth và noise → power, load và stability → đo/thiết kế dưới non-idealities, để transistor được đọc như một hệ có giới hạn.

Một transistor không “khuếch đại” chỉ vì nó là transistor. Nó cần độ lệch (bias / 편향) điểm (point / 지점) đúng operating region, một small-signal đường dẫn (path / 경로) để tín hiệu (signal / 신호) đi qua và một tải (load / 로드) phù hợp. Analog thiết kế (design / 설계) là bài toán đồng thời của DC operating điểm (point / 지점), AC gain, bandwidth, noise, power và stability.

## 1. độ lệch (bias / 편향) trước, gain sau

Với MOSFET, operating region phụ thuộc VGS, VDS và threshold VTH. Một điểm độ lệch (bias / 편향) Q đặt transistor ở vùng hoạt động mong muốn. Small-signal mô hình (model / 모델) tuyến tính hóa quanh điểm đó:

    id ≈ gm vgs + go vds

Trong đó gm = ∂ID/∂VGS là transconductance và go biểu diễn đầu ra (output / 출력) conductance. Cùng một transistor có thể có gain và linearity rất khác khi độ lệch (bias / 편향) hiện tại (current / 현재) thay đổi.

Độ lệch (bias / 편향) mạng (network / 네트워크) phải chịu được tiến trình (process / 프로세스) variation, temperature drift, supply variation, thiết bị (device / 장치) mismatch và tải (load / 로드)/phản hồi (feedback / 피드백) làm dịch operating điểm (point / 지점).

> **Chuyển mạch:** Trong **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **2. Gain không miễn phí** tiếp nhận điểm tựa từ **1. độ lệch (bias / 편향) trước, gain sau** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. Negative phản hồi (feedback / 피드백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Gain không miễn phí

Một common-source stage lý tưởng có gain gần:

    Av ≈ -gm (RD || RL)

Tăng RD hoặc gm làm gain lớn hơn, nhưng đầu ra (output / 출력) swing giảm, bandwidth giảm do parasitic capacitance và sensitivity tăng. Tăng độ lệch (bias / 편향) hiện tại (current / 현재) có thể tăng gm, đồng thời tăng power và self-heating.

Đây là sự đánh đổi (trade-off / 트레이드오프) cốt lõi: voltage gain, bandwidth, noise, linearity và power không thể đồng thời cực đại.

> **Chuyển mạch:** Ở chặng này của **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **3. Negative phản hồi (feedback / 피드백)** tiếp nhận điểm tựa từ **2. Gain không miễn phí** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Stability và phase margin** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Negative phản hồi (feedback / 피드백)

Một vòng lặp (loop / 루프) có forward gain A và phản hồi (feedback / 피드백) factor β có closed-loop gain:

    T = A / (1 + Aβ)

Khi |Aβ| lớn, gain gần 1/β và ít nhạy với thiết bị (device / 장치) variation. Nhưng phản hồi (feedback / 피드백) chỉ tốt nếu vòng lặp (loop / 루프) ổn định. Denominator bằng zero khi phase/gain phù hợp có thể tạo oscillation.

Phản hồi (feedback / 피드백) thường cải thiện distortion, đầu ra (output / 출력) resistance hoặc bandwidth trong một vùng, nhưng đổi lại cần headroom, vòng lặp (loop / 루프) bandwidth và phase margin.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **4. Stability và phase margin** tiếp nhận điểm tựa từ **3. Negative phản hồi (feedback / 피드백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Noise và động (dynamic / 동적) phạm vi (range / 범위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Stability và phase margin

Tại tần số vòng lặp (loop / 루프) gain có magnitude bằng 1, nếu phase lag gần -180°, hệ có thể oscillate. Parasitic pole từ transistor, op-amp, tải (load / 로드) capacitor và PCB dấu vết (trace / 추적) đều thêm phase lag.

Không được kết luận “op-amp ổn định” chỉ từ datasheet ở một gain. Cần kiểm tra vòng lặp (loop / 루프) gain, crossover frequency, phase margin, tải (load / 로드) variation và temperature/tiến trình (process / 프로세스) corners.

> **Chuyển mạch:** Trong **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **5. Noise và động (dynamic / 동적) phạm vi (range / 범위)** tiếp nhận điểm tựa từ **4. Stability và phase margin** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Worked lập luận (reasoning / 추론): sensor cầu nối (bridge / 브리지) vào ADC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Noise và động (dynamic / 동적) phạm vi (range / 범위)

Tổng noise không cộng trực tiếp theo biên độ nếu các nguồn độc lập; power spectral densities cộng:

    Stotal(f) = tổng Sk(f)

RMS noise lấy căn tích phân trên bandwidth. 1/f noise chi phối ở tần số thấp; thermal noise tăng với bandwidth. tín hiệu (signal / 신호) chuỗi (chain / 사슬) cần đủ gain trước ADC nhưng không được để offset/noise đẩy amplifier vào saturation.

Động (dynamic / 동적) phạm vi (range / 범위) là khoảng giữa tín hiệu nhỏ nhất còn phân biệt được và tín hiệu lớn nhất chưa méo/saturate. Một chuỗi (chain / 사슬) có gain cao nhưng ADC clipping vẫn là thiết kế kém.

> **Chuyển mạch:** Ở chặng này của **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **5. Noise và động (dynamic / 동적) phạm vi (range / 범위)** cho ta quy tắc; **6. Worked lập luận (reasoning / 추론): sensor cầu nối (bridge / 브리지) vào ADC** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. Đo kiểm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Worked lập luận (reasoning / 추론): sensor cầu nối (bridge / 브리지) vào ADC

Giả sử sensor tạo 10 mV full-scale, ADC 3.3 V, cần gain khoảng 330. Một op-amp stage đơn có thể đạt gain này trên giấy, nhưng offset 100 µV đã tạo 33 mV ở đầu ra (output / 출력); bandwidth closed-loop giảm theo gain-bandwidth sản phẩm (product / 제품); đầu vào (input / 입력) noise tích phân qua bandwidth có thể lớn hơn tín hiệu (signal / 신호); nguồn (source / 소스) impedance và đầu vào (input / 입력) độ lệch (bias / 편향) hiện tại (current / 현재) tạo thêm offset; đầu ra (output / 출력) swing không chạm rail nếu op-amp không rail-to-rail.

Giải pháp thường là instrumentation amplifier hoặc hai tầng gain, lọc trước gain lớn, rồi kiểm tra offset/noise ngân sách (budget / 예산) theo từng stage.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **6. Worked lập luận (reasoning / 추론): sensor cầu nối (bridge / 브리지) vào ADC** cho ta quy tắc; **7. Đo kiểm** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Đo kiểm

- Đo DC độ lệch (bias / 편향) trước khi đưa tín hiệu (signal / 신호).
- Dùng tín hiệu (signal / 신호) nhỏ để kiểm tra gain tuyến tính.
- Quét frequency và đo magnitude/phase thay vì chỉ đo một điểm.
- Thay đổi tải (load / 로드) capacitor và dây nối để tìm stability margin thật.
- Tách noise của nguồn, sensor và amplifier bằng short-input/known-source kiểm thử (test / 테스트).

> **Chuyển mạch:** Trong **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **Thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **7. Đo kiểm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes

- độ lệch (bias / 편향) sai làm transistor saturation/cutoff, khiến small-signal equation vô hiệu.
- phản hồi (feedback / 피드백) polarity nhầm biến negative phản hồi (feedback / 피드백) thành positive phản hồi (feedback / 피드백).
- Op-amp đầu vào (input / 입력) common-mode hoặc đầu ra (output / 출력) swing vượt rail.
- Compensation đẹp trên simulation nhưng thất bại (fail / 실패) với parasitic PCB.
- Gain đúng ở room temperature nhưng drift vượt sensor tolerance.

> **Chuyển mạch:** Ở chặng này của **Thiết bị (device / 장치) Biasing and phản hồi (feedback / 피드백) — độ lệch (bias / 편향), gain và ổn định**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [digital electronics](../digital_electronics/00_logic_timing_state.md) tại comparator/ADC ranh giới (boundary / 경계), hoặc [signals and systems](../signals_and_systems/00_lti_sampling_filtering.md) để định lượng bandwidth và filtering. Semiconductor thiết bị (device / 장치) physics nằm ở [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
