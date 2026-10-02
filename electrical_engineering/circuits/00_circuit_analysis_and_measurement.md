# Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch

> **Mạch đọc:** [README](./README.md) là owner của **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**; dùng nó để định vị chapter nền tảng trước network theorems. Từ **1. ranh giới (boundary / 경계), tham chiếu (reference / 참조) và sign convention** chuyển sang KCL/KVL, equivalent circuits, transient response và measurement uncertainty; mỗi phương trình phải gắn với boundary và cách kiểm chứng bằng dụng cụ.

Mạch điện (circuit) là một mô hình thu gọn của hệ điện thật. Ta thay dây dẫn, nguồn, linh kiện và tải bằng các phần tử có terminal, rồi hỏi: với topology và excitation này, voltage/hiện tại (current / 현재)/power thay đổi thế nào? Mục tiêu kỹ thuật (engineering / 엔지니어링) không chỉ là giải ra một con số, mà còn phải biết con số đó nhạy với giả định nào và đo nó ra sao.

## 1. ranh giới (boundary / 경계), tham chiếu (reference / 참조) và sign convention

Chọn hệ thống (system / 시스템) ranh giới (boundary / 경계) trước khi viết phương trình. Một nút (node / 노드) được chọn làm tham chiếu (reference / 참조) 0 V; mọi điện áp còn lại là chênh lệch so với nút (node / 노드) đó. Dòng điện là đại lượng có hướng quy ước, không phải mũi tên chứng minh electron thực sự chạy theo hướng đó.

Với passive sign convention, dòng đi vào cực dương của phần tử thì công suất hấp thụ là:

    p(t) = v(t)i(t)

Nếu p < 0, phần tử đang cung cấp năng lượng cho phần còn lại. Quy ước nhất quán quan trọng hơn việc chọn hướng nào.

> **Chuyển mạch:** Trong **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, **1. ranh giới (boundary / 경계), tham chiếu (reference / 참조) và sign convention** đã nêu tiêu chí phân biệt, còn **2. KCL và KVL** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **3. Voltage divider và loading** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. KCL và KVL

Kirchhoff hiện tại (current / 현재) Law (KCL) là bảo toàn điện tích tại nút (node / 노드):

    tổng i vào = tổng i ra

Kirchhoff Voltage Law (KVL) là tổng biến thiên thế năng quanh một vòng lặp (loop / 루프) kín bằng không trong mô hình lumped:

    tổng v quanh vòng lặp (loop / 루프) = 0

KCL/KVL không phải hai công thức độc lập với Physics. KCL dựa trên continuity của charge; KVL là xấp xỉ phù hợp khi kích thước mạch nhỏ so với bước sóng và hiệu ứng phân tán (distributed / 분산)/transmission-line chưa chi phối.

> **Chuyển mạch:** Ở chặng này của **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, **3. Voltage divider và loading** tiếp nhận điểm tựa từ **2. KCL và KVL** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Linearization và transient** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Voltage divider và loading

Với R1 nối tiếp R2 qua nguồn Vs, điện áp lý tưởng trên R2 là:

    Vout = Vs · R2 / (R1 + R2)

Nếu tải RL nối vào đầu ra (output / 출력), điện trở dưới trở thành Rdown = R2 || RL. Divider có Thevenin equivalent:

    Vth = Vs · R2 / (R1 + R2)
    Rth = R1 || R2

Một divider không phải nguồn áp lý tưởng; đầu ra (output / 출력) sẽ sụt khi RL không lớn hơn đáng kể Rth. Vì vậy “đúng điện áp khi không tải” chưa chứng minh mạch hoạt động đúng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, **4. Linearization và transient** tiếp nhận điểm tựa từ **3. Voltage divider và loading** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. AC, impedance và power factor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Linearization và transient

Với tụ điện và cuộn cảm:

    iC = C · dvC/dt
    vL = L · diL/dt

Năng lượng lưu trữ là EC = 1/2 C V² và EL = 1/2 L I². Mạch RC có thời gian (time / 시간) constant τ = RC. Khi nạp từ 0 tới Vs:

    vC(t) = Vs(1 - exp(-t/RC))

Sau khoảng 5τ, sai số còn xấp xỉ dưới 1%. Kết luận này giả định linh kiện tuyến tính, nguồn lý tưởng và không có loading/parasitic đáng kể.

> **Chuyển mạch:** Trong **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, **5. AC, impedance và power factor** tiếp nhận điểm tựa từ **4. Linearization và transient** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Đo đúng một mạch** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. AC, impedance và power factor

Trong steady trạng thái (state / 상태) hình sin, trở kháng biểu diễn quan hệ phasor:

    ZR = R
    ZL = jωL
    ZC = 1/(jωC)

RMS voltage/hiện tại (current / 현재) cho công suất thực P = Vrms Irms cos φ. Với tải switching, còn distortion power factor; chỉ nhìn phase shift là chưa đủ.

> **Chuyển mạch:** Ở chặng này của **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, **6. Đo đúng một mạch** tiếp nhận điểm tựa từ **5. AC, impedance và power factor** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Worked lập luận (reasoning / 추론): divider cho ADC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Đo đúng một mạch

Đo là một phần của circuit mô hình (model / 모델) vì instrument cũng trở thành phần tử trong mạch:

- voltmeter có đầu vào (input / 입력) resistance hữu hạn và tạo loading;
- ammeter có burden voltage và phải mắc nối tiếp;
- oscilloscope probe có capacitance, ground lead inductance và bandwidth;
- ground clip nối các điểm với nhau và có thể tạo short hoặc ground vòng lặp (loop / 루프);
- bandwidth limit, mẫu (sample / 표본) tỷ lệ (rate / 비율) và probe compensation thay đổi waveform quan sát.

Quy trình an toàn:

    power off → inspect polarity/short → current-limited supply
    → đo resistance trước → power on ở giới hạn thấp
    → kiểm tra DC operating điểm (point / 지점) → mới xem transient/AC

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, **6. Đo đúng một mạch** cho ta quy tắc; **7. Worked lập luận (reasoning / 추론): divider cho ADC** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **8. thất bại (failure / 실패) modes và giới hạn** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Worked lập luận (reasoning / 추론): divider cho ADC

Giả sử cần đưa 0–12 V về ADC 0–3.3 V. Tỉ lệ lý tưởng là 3.3/12 = 0.275. Chọn R1 = 27 kΩ, R2 = 10 kΩ cho tỉ lệ 0.270, đầu ra (output / 출력) cực đại khoảng 3.24 V.

Nhưng ADC có sampling capacitor. Nếu Rth = R1 || R2 ≈ 7.3 kΩ quá lớn so với acquisition thời gian (time / 시간), capacitor chưa kịp settle và mã (code / 코드) ADC thấp. Có thể giảm cả hai điện trở, thêm buffer op-amp, hoặc tăng acquisition thời gian (time / 시간). Đây là điểm circuit phân tích (analysis / 분석) nối trực tiếp sang analog front-end và embedded ADC.

> **Chuyển mạch:** Trong **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, trường hợp ở **7. Worked lập luận (reasoning / 추론): divider cho ADC** cho thấy quy tắc hoạt động; **8. thất bại (failure / 실패) modes và giới hạn** kiểm tra nơi quy tắc ấy không còn áp dụng hoặc dễ bị hiểu nhầm. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. thất bại (failure / 실패) modes và giới hạn

- Ground tham chiếu (reference / 참조) sai làm mọi điện áp “đúng tương đối” nhưng sai so với hệ thống (system / 시스템).
- Tụ phân cực ngược có thể hỏng trước khi waveform nhìn thấy bất thường.
- R = 0 và C = 0 là ideal limits, không phải thành phần (component / 컴포넌트) thật.
- Khi kích thước dây đủ lớn hoặc tần số đủ cao, lumped KVL thất bại (fail / 실패); cần transmission-line mô hình (model / 모델).
- Khi mạch có semiconductor, topology có thể đổi theo operating region; giải tuyến tính một lần là chưa đủ.

> **Chuyển mạch:** Ở chặng này của **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch**, **8. thất bại (failure / 실패) modes và giới hạn** đã nêu tiêu chí phân biệt, còn **Cầu nối (bridge / 브리지)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Tiếp theo: [Analog electronics — device biasing và feedback](../analog_electronics/00_device_biasing_feedback.md), hoặc [Signals and systems — LTI, sampling và filtering](../signals_and_systems/00_lti_sampling_filtering.md). Nền Physics tương ứng: [mạch DC](../../physics/05_electromagnetism/01_dc_circuits.md), [mạch AC/RLC](../../physics/05_electromagnetism/02_ac_rlc_circuits.md) và [transmission lines](../../physics/05_electromagnetism/05_transmission_lines_waveguides.md).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
