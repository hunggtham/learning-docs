# Device Biasing and Feedback — Bias, gain và ổn định

Một transistor không “khuếch đại” chỉ vì nó là transistor. Nó cần bias point đúng operating region, một small-signal path để signal đi qua và một load phù hợp. Analog design là bài toán đồng thời của DC operating point, AC gain, bandwidth, noise, power và stability.

## 1. Bias trước, gain sau

Với MOSFET, operating region phụ thuộc VGS, VDS và threshold VTH. Một điểm bias Q đặt transistor ở vùng hoạt động mong muốn. Small-signal model tuyến tính hóa quanh điểm đó:

    id ≈ gm vgs + go vds

Trong đó gm = ∂ID/∂VGS là transconductance và go biểu diễn output conductance. Cùng một transistor có thể có gain và linearity rất khác khi bias current thay đổi.

Bias network phải chịu được process variation, temperature drift, supply variation, device mismatch và load/feedback làm dịch operating point.

## 2. Gain không miễn phí

Một common-source stage lý tưởng có gain gần:

    Av ≈ -gm (RD || RL)

Tăng RD hoặc gm làm gain lớn hơn, nhưng output swing giảm, bandwidth giảm do parasitic capacitance và sensitivity tăng. Tăng bias current có thể tăng gm, đồng thời tăng power và self-heating.

Đây là trade-off cốt lõi: voltage gain, bandwidth, noise, linearity và power không thể đồng thời cực đại.

## 3. Negative feedback

Một loop có forward gain A và feedback factor β có closed-loop gain:

    T = A / (1 + Aβ)

Khi |Aβ| lớn, gain gần 1/β và ít nhạy với device variation. Nhưng feedback chỉ tốt nếu loop ổn định. Denominator bằng zero khi phase/gain phù hợp có thể tạo oscillation.

Feedback thường cải thiện distortion, output resistance hoặc bandwidth trong một vùng, nhưng đổi lại cần headroom, loop bandwidth và phase margin.

## 4. Stability và phase margin

Tại tần số loop gain có magnitude bằng 1, nếu phase lag gần -180°, hệ có thể oscillate. Parasitic pole từ transistor, op-amp, load capacitor và PCB trace đều thêm phase lag.

Không được kết luận “op-amp ổn định” chỉ từ datasheet ở một gain. Cần kiểm tra loop gain, crossover frequency, phase margin, load variation và temperature/process corners.

## 5. Noise và dynamic range

Tổng noise không cộng trực tiếp theo biên độ nếu các nguồn độc lập; power spectral densities cộng:

    Stotal(f) = tổng Sk(f)

RMS noise lấy căn tích phân trên bandwidth. 1/f noise chi phối ở tần số thấp; thermal noise tăng với bandwidth. Signal chain cần đủ gain trước ADC nhưng không được để offset/noise đẩy amplifier vào saturation.

Dynamic range là khoảng giữa tín hiệu nhỏ nhất còn phân biệt được và tín hiệu lớn nhất chưa méo/saturate. Một chain có gain cao nhưng ADC clipping vẫn là thiết kế kém.

## 6. Worked reasoning: sensor bridge vào ADC

Giả sử sensor tạo 10 mV full-scale, ADC 3.3 V, cần gain khoảng 330. Một op-amp stage đơn có thể đạt gain này trên giấy, nhưng offset 100 µV đã tạo 33 mV ở output; bandwidth closed-loop giảm theo gain-bandwidth product; input noise tích phân qua bandwidth có thể lớn hơn signal; source impedance và input bias current tạo thêm offset; output swing không chạm rail nếu op-amp không rail-to-rail.

Giải pháp thường là instrumentation amplifier hoặc hai tầng gain, lọc trước gain lớn, rồi kiểm tra offset/noise budget theo từng stage.

## 7. Đo kiểm

- Đo DC bias trước khi đưa signal.
- Dùng signal nhỏ để kiểm tra gain tuyến tính.
- Quét frequency và đo magnitude/phase thay vì chỉ đo một điểm.
- Thay đổi load capacitor và dây nối để tìm stability margin thật.
- Tách noise của nguồn, sensor và amplifier bằng short-input/known-source test.

## Failure modes

- Bias sai làm transistor saturation/cutoff, khiến small-signal equation vô hiệu.
- Feedback polarity nhầm biến negative feedback thành positive feedback.
- Op-amp input common-mode hoặc output swing vượt rail.
- Compensation đẹp trên simulation nhưng fail với parasitic PCB.
- Gain đúng ở room temperature nhưng drift vượt sensor tolerance.

## Bridge

Đi tiếp sang [digital electronics](../digital_electronics/00_logic_timing_state.md) tại comparator/ADC boundary, hoặc [signals and systems](../signals_and_systems/00_lti_sampling_filtering.md) để định lượng bandwidth và filtering. Semiconductor device physics nằm ở [Physics](../../physics/10_condensed_matter_devices/01_semiconductors_devices.md).
