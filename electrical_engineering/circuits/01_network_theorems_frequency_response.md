# Mạng (network / 네트워크) Theorems and Frequency phản hồi (response / 응답) — Định lý mạng và đáp ứng tần số

> **Mạch đọc:** [README](./README.md) là owner của **Mạng (network / 네트워크) Theorems and Frequency phản hồi (response / 응답) — Định lý mạng và đáp ứng tần số**; đặt chapter sau circuit analysis và trước các mô hình động. Từ **1. Nodal và mesh phân tích (analysis / 분석)** nối sang Thevenin/Norton, transfer function, Bode và frequency response, rồi dùng equivalent boundary để giải thích khi mô hình lumped còn hợp lệ.

Chapter đầu xây phương trình cho một mạch cụ thể. Chapter này nâng lớp trừu tượng (abstraction / 추상화): thay một phần mạch bằng equivalent, đo sensitivity theo frequency và nhận ra khi lumped mô hình (model / 모델) không còn đủ.

## 1. Nodal và mesh phân tích (analysis / 분석)

Nodal phân tích (analysis / 분석) chọn voltage nút (node / 노드) làm unknown. Với tuyến tính (linear / 선형) resistive mạng (network / 네트워크), hệ phương trình có dạng Gv = i. Ma trận conductance có cấu trúc từ topology; đó là lý do circuit simulator có thể giải hàng nghìn nút (node / 노드) thay vì viết từng KVL thủ công.

Mesh phân tích (analysis / 분석) chọn vòng lặp (loop / 루프) hiện tại (current / 현재) và hữu ích khi mạch planar có ít vòng lặp (loop / 루프). Khi có hiện tại (current / 현재) nguồn (source / 소스) giữa mesh hoặc dependent nguồn (source / 소스), cần supermesh và ràng buộc (constraint / 제약조건) bổ sung. Không chọn phương pháp theo thói quen; chọn unknowns ít và ranh giới (boundary / 경계) rõ.

> **Chuyển mạch:** **1. Nodal và mesh analysis** giải mạch đầy đủ; **2. Thevenin/Norton** nén phần còn lại thành interface, rồi **3. Transfer function và Bode** mô tả đáp ứng theo tần số.

## 2. Thevenin/Norton như phép nén giao diện (interface / 인터페이스)

Một tuyến tính (linear / 선형) two-terminal mạng (network / 네트워크) tương đương với Vth nối tiếp Rth hoặc In song song Rn. Vth là open-circuit voltage; Rth có thể tìm bằng kiểm thử (test / 테스트) nguồn (source / 소스) khi dependent nguồn (source / 소스) còn hoạt động. Tắt independent nguồn (source / 소스) chỉ có nghĩa voltage nguồn (source / 소스) thành short và hiện tại (current / 현재) nguồn (source / 소스) thành open, không được tắt dependent nguồn (source / 소스).

Equivalent chỉ đúng nhìn từ cặp terminal trong miền operating các giả định (assumptions / 가정들). Nó không giữ được nội bộ (internal / 내부) power, noise correlation hoặc hành vi (behavior / 동작) khi tải (load / 로드) đi vào nonlinear region.

> **Chuyển mạch:** Từ interface tương đương, **3. Transfer function và Bode** cho gain/phase; **4. Sensitivity và tolerance** kiểm tra các kết quả đó khi linh kiện lệch.

## 3. Transfer hàm (function / 함수) và Bode

Với zero/pole, magnitude dB là 20 log10 |H(jω)| và phase là arg H(jω). Mỗi pole bậc nhất đóng góp gần -20 dB/decade sau corner; mỗi zero đóng góp ngược lại. Corner frequency là nơi xấp xỉ asymptote bắt đầu đổi, không phải ranh giới (boundary / 경계) cứng.

RLC bậc hai có thể tạo resonance. Q cao cho peak lớn và ringing dài; damping tăng làm phản hồi (response / 응답) phẳng hơn nhưng mất selectivity.

> **Chuyển mạch:** **4. Sensitivity và tolerance** biến Bode thành biên thiết kế; **5. Worked reasoning** kiểm tra khi tải đổi thì bandwidth và ổn định thay đổi ra sao.

## 4. Sensitivity và tolerance

Nếu đầu ra (output / 출력) y phụ thuộc thành phần (component / 컴포넌트) x, sensitivity chuẩn hóa gần:

    Sx = (x/y) · (∂y/∂x)

Tolerance ngăn xếp (stack / 스택) không nên chỉ cộng phần trăm khi biến độc lập và nonlinear. Worst-case, RSS và Monte Carlo trả lời các rủi ro (risk / 위험) question khác nhau.

> **Chuyển mạch:** Trong **Mạng (network / 네트워크) Theorems and Frequency phản hồi (response / 응답) — Định lý mạng và đáp ứng tần số**, **4. Sensitivity và tolerance** cho ta quy tắc; **5. Worked lập luận (reasoning / 추론): tải (load / 로드) thay đổi bandwidth** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Worked lập luận (reasoning / 추론): tải (load / 로드) thay đổi bandwidth

Một op-amp đầu ra (output / 출력) driving capacitor có thể biến tải (load / 로드) thành pole mới. Nếu pole hạ dưới vòng lặp (loop / 루프) crossover, phase margin giảm. Vì vậy đo frequency phản hồi (response / 응답) phải lặp với minimum/maximum tải (load / 로드), cable length và supply corner; phản hồi (response / 응답) của board không phải phản hồi (response / 응답) của schematic lý tưởng.

> **Chuyển mạch:** **Worked reasoning** nối theorem, frequency response và load vào một quyết định thiết kế; **Cầu nối** ghi lại phép đo cần dùng để xác nhận quyết định đó.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [analog electronics](../analog_electronics/00_device_biasing_feedback.md) để xem active thiết bị (device / 장치) và [control systems](../control_systems/00_feedback_stability_pid.md) để dùng poles/zeros trong closed vòng lặp (loop / 루프).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
