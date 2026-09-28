# Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch

> **Mạch đọc:** Đặt **Circuit phân tích (analysis / 분석) and đo lường (measurement / 측정) — Phân tích và đo mạch** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. ranh giới (boundary / 경계), tham chiếu (reference / 참조) và sign convention** sang **2. KCL và KVL**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Mạch điện (circuit) là một mô hình thu gọn của hệ điện thật. Ta thay dây dẫn, nguồn, linh kiện và tải bằng các phần tử có terminal, rồi hỏi: với topology và excitation này, voltage/hiện tại (current / 현재)/power thay đổi thế nào? Mục tiêu kỹ thuật (engineering / 엔지니어링) không chỉ là giải ra một con số, mà còn phải biết con số đó nhạy với giả định nào và đo nó ra sao.

## 1. ranh giới (boundary / 경계), tham chiếu (reference / 참조) và sign convention

Chọn hệ thống (system / 시스템) ranh giới (boundary / 경계) trước khi viết phương trình. Một nút (node / 노드) được chọn làm tham chiếu (reference / 참조) 0 V; mọi điện áp còn lại là chênh lệch so với nút (node / 노드) đó. Dòng điện là đại lượng có hướng quy ước, không phải mũi tên chứng minh electron thực sự chạy theo hướng đó.

Với passive sign convention, dòng đi vào cực dương của phần tử thì công suất hấp thụ là:

    p(t) = v(t)i(t)

Nếu p < 0, phần tử đang cung cấp năng lượng cho phần còn lại. Quy ước nhất quán quan trọng hơn việc chọn hướng nào.


> **Chuyển mạch:** Từ **1. ranh giới (boundary / 경계), tham chiếu (reference / 참조) và sign convention**, ta sang **2. KCL và KVL** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. KCL và KVL

Kirchhoff hiện tại (current / 현재) Law (KCL) là bảo toàn điện tích tại nút (node / 노드):

    tổng i vào = tổng i ra

Kirchhoff Voltage Law (KVL) là tổng biến thiên thế năng quanh một vòng lặp (loop / 루프) kín bằng không trong mô hình lumped:

    tổng v quanh vòng lặp (loop / 루프) = 0

KCL/KVL không phải hai công thức độc lập với Physics. KCL dựa trên continuity của charge; KVL là xấp xỉ phù hợp khi kích thước mạch nhỏ so với bước sóng và hiệu ứng phân tán (distributed / 분산)/transmission-line chưa chi phối.


> **Chuyển mạch:** Từ **2. KCL và KVL**, ta sang **3. Voltage divider và loading** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. Voltage divider và loading

Với R1 nối tiếp R2 qua nguồn Vs, điện áp lý tưởng trên R2 là:

    Vout = Vs · R2 / (R1 + R2)

Nếu tải RL nối vào đầu ra (output / 출력), điện trở dưới trở thành Rdown = R2 || RL. Divider có Thevenin equivalent:

    Vth = Vs · R2 / (R1 + R2)
    Rth = R1 || R2

Một divider không phải nguồn áp lý tưởng; đầu ra (output / 출력) sẽ sụt khi RL không lớn hơn đáng kể Rth. Vì vậy “đúng điện áp khi không tải” chưa chứng minh mạch hoạt động đúng.


> **Chuyển mạch:** Từ **3. Voltage divider và loading**, ta sang **4. Linearization và transient** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. Linearization và transient

Với tụ điện và cuộn cảm:

    iC = C · dvC/dt
    vL = L · diL/dt

Năng lượng lưu trữ là EC = 1/2 C V² và EL = 1/2 L I². Mạch RC có thời gian (time / 시간) constant τ = RC. Khi nạp từ 0 tới Vs:

    vC(t) = Vs(1 - exp(-t/RC))

Sau khoảng 5τ, sai số còn xấp xỉ dưới 1%. Kết luận này giả định linh kiện tuyến tính, nguồn lý tưởng và không có loading/parasitic đáng kể.


> **Chuyển mạch:** Từ **4. Linearization và transient**, ta sang **5. AC, impedance và power factor** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. AC, impedance và power factor

Trong steady trạng thái (state / 상태) hình sin, trở kháng biểu diễn quan hệ phasor:

    ZR = R
    ZL = jωL
    ZC = 1/(jωC)

RMS voltage/hiện tại (current / 현재) cho công suất thực P = Vrms Irms cos φ. Với tải switching, còn distortion power factor; chỉ nhìn phase shift là chưa đủ.


> **Chuyển mạch:** Từ **5. AC, impedance và power factor**, ta sang **6. Đo đúng một mạch** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

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


> **Chuyển mạch:** Từ **6. Đo đúng một mạch**, ta sang **7. Worked lập luận (reasoning / 추론): divider cho ADC** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 7. Worked lập luận (reasoning / 추론): divider cho ADC

Giả sử cần đưa 0–12 V về ADC 0–3.3 V. Tỉ lệ lý tưởng là 3.3/12 = 0.275. Chọn R1 = 27 kΩ, R2 = 10 kΩ cho tỉ lệ 0.270, đầu ra (output / 출력) cực đại khoảng 3.24 V.

Nhưng ADC có sampling capacitor. Nếu Rth = R1 || R2 ≈ 7.3 kΩ quá lớn so với acquisition thời gian (time / 시간), capacitor chưa kịp settle và mã (code / 코드) ADC thấp. Có thể giảm cả hai điện trở, thêm buffer op-amp, hoặc tăng acquisition thời gian (time / 시간). Đây là điểm circuit phân tích (analysis / 분석) nối trực tiếp sang analog front-end và embedded ADC.


> **Chuyển mạch:** Từ **7. Worked lập luận (reasoning / 추론): divider cho ADC**, ta sang **8. thất bại (failure / 실패) modes và giới hạn** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 8. thất bại (failure / 실패) modes và giới hạn

- Ground tham chiếu (reference / 참조) sai làm mọi điện áp “đúng tương đối” nhưng sai so với hệ thống (system / 시스템).
- Tụ phân cực ngược có thể hỏng trước khi waveform nhìn thấy bất thường.
- R = 0 và C = 0 là ideal limits, không phải thành phần (component / 컴포넌트) thật.
- Khi kích thước dây đủ lớn hoặc tần số đủ cao, lumped KVL thất bại (fail / 실패); cần transmission-line mô hình (model / 모델).
- Khi mạch có semiconductor, topology có thể đổi theo operating region; giải tuyến tính một lần là chưa đủ.


> **Chuyển mạch:** Từ **8. thất bại (failure / 실패) modes và giới hạn**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Tiếp theo: [Analog electronics — device biasing và feedback](../analog_electronics/00_device_biasing_feedback.md), hoặc [Signals and systems — LTI, sampling và filtering](../signals_and_systems/00_lti_sampling_filtering.md). Nền Physics tương ứng: [mạch DC](../../physics/05_electromagnetism/01_dc_circuits.md), [mạch AC/RLC](../../physics/05_electromagnetism/02_ac_rlc_circuits.md) và [transmission lines](../../physics/05_electromagnetism/05_transmission_lines_waveguides.md).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 network theorems frequency response](./01_network_theorems_frequency_response.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
