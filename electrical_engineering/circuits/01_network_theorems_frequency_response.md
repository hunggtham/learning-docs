# Network Theorems and Frequency Response — Định lý mạng và đáp ứng tần số

Chapter đầu xây phương trình cho một mạch cụ thể. Chapter này nâng abstraction: thay một phần mạch bằng equivalent, đo sensitivity theo frequency và nhận ra khi lumped model không còn đủ.

## 1. Nodal và mesh analysis

Nodal analysis chọn voltage node làm unknown. Với linear resistive network, hệ phương trình có dạng Gv = i. Ma trận conductance có cấu trúc từ topology; đó là lý do circuit simulator có thể giải hàng nghìn node thay vì viết từng KVL thủ công.

Mesh analysis chọn loop current và hữu ích khi mạch planar có ít loop. Khi có current source giữa mesh hoặc dependent source, cần supermesh và constraint bổ sung. Không chọn phương pháp theo thói quen; chọn unknowns ít và boundary rõ.

## 2. Thevenin/Norton như phép nén interface

Một linear two-terminal network tương đương với Vth nối tiếp Rth hoặc In song song Rn. Vth là open-circuit voltage; Rth có thể tìm bằng test source khi dependent source còn hoạt động. Tắt independent source chỉ có nghĩa voltage source thành short và current source thành open, không được tắt dependent source.

Equivalent chỉ đúng nhìn từ cặp terminal trong miền operating assumptions. Nó không giữ được internal power, noise correlation hoặc behavior khi load đi vào nonlinear region.

## 3. Transfer function và Bode

Với zero/pole, magnitude dB là 20 log10 |H(jω)| và phase là arg H(jω). Mỗi pole bậc nhất đóng góp gần -20 dB/decade sau corner; mỗi zero đóng góp ngược lại. Corner frequency là nơi xấp xỉ asymptote bắt đầu đổi, không phải boundary cứng.

RLC bậc hai có thể tạo resonance. Q cao cho peak lớn và ringing dài; damping tăng làm response phẳng hơn nhưng mất selectivity.

## 4. Sensitivity và tolerance

Nếu output y phụ thuộc component x, sensitivity chuẩn hóa gần:

    Sx = (x/y) · (∂y/∂x)

Tolerance stack không nên chỉ cộng phần trăm khi biến độc lập và nonlinear. Worst-case, RSS và Monte Carlo trả lời các risk question khác nhau.

## 5. Worked reasoning: load thay đổi bandwidth

Một op-amp output driving capacitor có thể biến load thành pole mới. Nếu pole hạ dưới loop crossover, phase margin giảm. Vì vậy đo frequency response phải lặp với minimum/maximum load, cable length và supply corner; response của board không phải response của schematic lý tưởng.

## Bridge

Đi tiếp sang [analog electronics](../analog_electronics/00_device_biasing_feedback.md) để xem active device và [control systems](../control_systems/00_feedback_stability_pid.md) để dùng poles/zeros trong closed loop.
