# Circuit Analysis and Measurement — Phân tích và đo mạch

Mạch điện (circuit) là một mô hình thu gọn của hệ điện thật. Ta thay dây dẫn, nguồn, linh kiện và tải bằng các phần tử có terminal, rồi hỏi: với topology và excitation này, voltage/current/power thay đổi thế nào? Mục tiêu engineering không chỉ là giải ra một con số, mà còn phải biết con số đó nhạy với giả định nào và đo nó ra sao.

## 1. Boundary, reference và sign convention

Chọn system boundary trước khi viết phương trình. Một node được chọn làm reference 0 V; mọi điện áp còn lại là chênh lệch so với node đó. Dòng điện là đại lượng có hướng quy ước, không phải mũi tên chứng minh electron thực sự chạy theo hướng đó.

Với passive sign convention, dòng đi vào cực dương của phần tử thì công suất hấp thụ là:

    p(t) = v(t)i(t)

Nếu p < 0, phần tử đang cung cấp năng lượng cho phần còn lại. Quy ước nhất quán quan trọng hơn việc chọn hướng nào.

## 2. KCL và KVL

Kirchhoff Current Law (KCL) là bảo toàn điện tích tại node:

    tổng i vào = tổng i ra

Kirchhoff Voltage Law (KVL) là tổng biến thiên thế năng quanh một loop kín bằng không trong mô hình lumped:

    tổng v quanh loop = 0

KCL/KVL không phải hai công thức độc lập với Physics. KCL dựa trên continuity của charge; KVL là xấp xỉ phù hợp khi kích thước mạch nhỏ so với bước sóng và hiệu ứng distributed/transmission-line chưa chi phối.

## 3. Voltage divider và loading

Với R1 nối tiếp R2 qua nguồn Vs, điện áp lý tưởng trên R2 là:

    Vout = Vs · R2 / (R1 + R2)

Nếu tải RL nối vào output, điện trở dưới trở thành Rdown = R2 || RL. Divider có Thevenin equivalent:

    Vth = Vs · R2 / (R1 + R2)
    Rth = R1 || R2

Một divider không phải nguồn áp lý tưởng; output sẽ sụt khi RL không lớn hơn đáng kể Rth. Vì vậy “đúng điện áp khi không tải” chưa chứng minh mạch hoạt động đúng.

## 4. Linearization và transient

Với tụ điện và cuộn cảm:

    iC = C · dvC/dt
    vL = L · diL/dt

Năng lượng lưu trữ là EC = 1/2 C V² và EL = 1/2 L I². Mạch RC có time constant τ = RC. Khi nạp từ 0 tới Vs:

    vC(t) = Vs(1 - exp(-t/RC))

Sau khoảng 5τ, sai số còn xấp xỉ dưới 1%. Kết luận này giả định linh kiện tuyến tính, nguồn lý tưởng và không có loading/parasitic đáng kể.

## 5. AC, impedance và power factor

Trong steady state hình sin, trở kháng biểu diễn quan hệ phasor:

    ZR = R
    ZL = jωL
    ZC = 1/(jωC)

RMS voltage/current cho công suất thực P = Vrms Irms cos φ. Với tải switching, còn distortion power factor; chỉ nhìn phase shift là chưa đủ.

## 6. Đo đúng một mạch

Đo là một phần của circuit model vì instrument cũng trở thành phần tử trong mạch:

- voltmeter có input resistance hữu hạn và tạo loading;
- ammeter có burden voltage và phải mắc nối tiếp;
- oscilloscope probe có capacitance, ground lead inductance và bandwidth;
- ground clip nối các điểm với nhau và có thể tạo short hoặc ground loop;
- bandwidth limit, sample rate và probe compensation thay đổi waveform quan sát.

Quy trình an toàn:

    power off → inspect polarity/short → current-limited supply
    → đo resistance trước → power on ở giới hạn thấp
    → kiểm tra DC operating point → mới xem transient/AC

## 7. Worked reasoning: divider cho ADC

Giả sử cần đưa 0–12 V về ADC 0–3.3 V. Tỉ lệ lý tưởng là 3.3/12 = 0.275. Chọn R1 = 27 kΩ, R2 = 10 kΩ cho tỉ lệ 0.270, output cực đại khoảng 3.24 V.

Nhưng ADC có sampling capacitor. Nếu Rth = R1 || R2 ≈ 7.3 kΩ quá lớn so với acquisition time, capacitor chưa kịp settle và code ADC thấp. Có thể giảm cả hai điện trở, thêm buffer op-amp, hoặc tăng acquisition time. Đây là điểm circuit analysis nối trực tiếp sang analog front-end và embedded ADC.

## 8. Failure modes và giới hạn

- Ground reference sai làm mọi điện áp “đúng tương đối” nhưng sai so với system.
- Tụ phân cực ngược có thể hỏng trước khi waveform nhìn thấy bất thường.
- R = 0 và C = 0 là ideal limits, không phải component thật.
- Khi kích thước dây đủ lớn hoặc tần số đủ cao, lumped KVL fail; cần transmission-line model.
- Khi mạch có semiconductor, topology có thể đổi theo operating region; giải tuyến tính một lần là chưa đủ.

## Bridge

Tiếp theo: [Analog electronics — device biasing và feedback](../analog_electronics/00_device_biasing_feedback.md), hoặc [Signals and systems — LTI, sampling và filtering](../signals_and_systems/00_lti_sampling_filtering.md). Nền Physics tương ứng: [mạch DC](../../physics/05_electromagnetism/01_dc_circuits.md), [mạch AC/RLC](../../physics/05_electromagnetism/02_ac_rlc_circuits.md) và [transmission lines](../../physics/05_electromagnetism/05_transmission_lines_waveguides.md).
