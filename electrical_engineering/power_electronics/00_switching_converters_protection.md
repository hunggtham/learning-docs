# Switching Converters and Protection — Converter, switching và bảo vệ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Switching Converters and Protection — Converter, switching và bảo vệ**. Route đi từ ideal buck → energy/ripple and losses → control/feedback → protection, short-circuit/thermal limits → measurement and design margin.

Power electronics điều khiển năng lượng lớn bằng các phần tử đóng/ngắt nhanh. Khác với tín hiệu (signal / 신호) chuỗi (chain / 사슬), một lỗi ngắn mạch có thể phá hỏng silicon, dấu vết (trace / 추적) hoặc gây hazard trước khi software kịp phản ứng.

## 1. Buck converter lý tưởng

Ở continuous conduction chế độ (mode / 모드), buck converter lý tưởng có:

    Vout ≈ D · Vin

D là duty cycle. Inductor làm dòng liên tục; capacitor giảm ripple voltage. Trong thực tế phải xét switch Ron, diode/MOSFET drop, ESR, dead thời gian (time / 시간) và switching mất mát (loss / 손실).

> **Chuyển mạch:** Trong **Switching Converters and Protection — Converter, switching và bảo vệ**, **2. năng lượng (energy / 에너지) và ripple** tiếp nhận điểm tựa từ **1. Buck converter lý tưởng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. mất mát (loss / 손실) và thermal đường dẫn (path / 경로)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. năng lượng (energy / 에너지) và ripple

Inductor không cho dòng đổi tức thời:

    ΔIL = VL · Δt / L

Capacitor không cho voltage đổi tức thời:

    ΔVC ≈ IC · Δt / C

Ripple quá lớn gây đầu ra (output / 출력) noise, điều khiển (control / 제어) instability, magnetic saturation hoặc violation của tải (load / 로드).

> **Chuyển mạch:** Ở chặng này của **Switching Converters and Protection — Converter, switching và bảo vệ**, **2. năng lượng (energy / 에너지) và ripple** xác định đầu vào; **3. mất mát (loss / 손실) và thermal đường dẫn (path / 경로)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **4. vòng điều khiển (control loop / 제어 루프) và compensation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. mất mát (loss / 손실) và thermal đường dẫn (path / 경로)

Conduction mất mát (loss / 손실) gần Pcond ≈ Irms² Ron. Switching mất mát (loss / 손실) phụ thuộc voltage, hiện tại (current / 현재), chuyển tiếp (transition / 전이) thời gian (time / 시간) và frequency. Tổng mất mát (loss / 손실) đi qua junction → gói (package / 패키지) → PCB/heatsink → ambient. Nhiệt độ junction gần:

    Tj ≈ Ta + Ploss · θJA

Chọn thành phần (component / 컴포넌트) theo average hiện tại (current / 현재) là chưa đủ; phải xét peak hiện tại (current / 현재), SOA, transient và derating.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Switching Converters and Protection — Converter, switching và bảo vệ**, **3. mất mát (loss / 손실) và thermal đường dẫn (path / 경로)** xác định đầu vào; **4. vòng điều khiển (control loop / 제어 루프) và compensation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **5. Protection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. vòng điều khiển (control loop / 제어 루프) và compensation

Converter là plant có poles từ LC filter và zero từ ESR. phản hồi (feedback / 피드백) controller phải đạt transient phản hồi (response / 응답) nhưng giữ phase margin qua đầu vào (input / 입력) voltage, tải (load / 로드) và thành phần (component / 컴포넌트) tolerance. Current-mode điều khiển (control / 제어) thêm inner vòng lặp (loop / 루프) nhưng cần slope compensation ở một số duty cycle.

> **Chuyển mạch:** Trong **Switching Converters and Protection — Converter, switching và bảo vệ**, **5. Protection** tiếp nhận điểm tựa từ **4. vòng điều khiển (control loop / 제어 루프) và compensation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Worked lập luận (reasoning / 추론): chọn inductor** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Protection

Các lớp thường cần cycle-by-cycle over-current, short-circuit phản hồi (response / 응답), over-voltage/under-voltage lockout, over-temperature, reverse polarity, inrush limiting, shoot-through prevention/dead thời gian (time / 시간) và isolation khi fault lĩnh vực (domain / 도메인) khác nhau.

Protection không chỉ là “ngắt khi quá dòng”; phải xem năng lượng còn lại trong inductor/capacitor và đường discharge.

> **Chuyển mạch:** Ở chặng này của **Switching Converters and Protection — Converter, switching và bảo vệ**, **5. Protection** cho ta quy tắc; **6. Worked lập luận (reasoning / 추론): chọn inductor** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **7. EMI/EMC và bố cục (layout / 레이아웃)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Worked lập luận (reasoning / 추론): chọn inductor

Nếu buck 12 V → 5 V, fs = 500 kHz, Iout = 2 A, chọn ripple mục tiêu (target / 대상) 30% tức ΔIL = 0.6 A. Duty lý tưởng D ≈ 5/12. Trong on-time, VL ≈ 7 V, nên:

    L ≈ VL · D / (fs · ΔIL)

Sau khi tính, phải kiểm tra saturation hiện tại (current / 현재), copper mất mát (loss / 손실), cốt lõi (core / 핵심) mất mát (loss / 손실), DCR và transient tải (load / 로드). Một giá trị L đúng trên công thức nhưng saturate ở startup là thiết kế sai.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Switching Converters and Protection — Converter, switching và bảo vệ**, **6. Worked lập luận (reasoning / 추론): chọn inductor** cho ta quy tắc; **7. EMI/EMC và bố cục (layout / 레이아웃)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Thất bại (failure / 실패) modes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. EMI/EMC và bố cục (layout / 레이아웃)

Vòng dòng switching càng lớn thì di/dt và nhiễu bức xạ/conduction càng khó kiểm soát. bố cục (layout / 레이아웃) cần high di/dt vòng lặp (loop / 루프) nhỏ, gate vòng lặp (loop / 루프) ngắn, power/analog ground có chủ đích và sense Kelvin.

EMI filter thêm poles/impedance và có thể làm vòng điều khiển (control loop / 제어 루프) thay đổi; không thêm filter sau cùng mà không re-verify stability.

> **Chuyển mạch:** Trong **Switching Converters and Protection — Converter, switching và bảo vệ**, **Thất bại (failure / 실패) modes** tiếp nhận điểm tựa từ **7. EMI/EMC và bố cục (layout / 레이아웃)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thất bại (failure / 실패) modes

- switch nút (node / 노드) ringing vượt VDS rating;
- diode reverse khôi phục (recovery / 복구) tạo shoot-through;
- inductor saturation làm hiện tại (current / 현재) spike;
- thermal runaway do Ron tăng theo nhiệt;
- protection chậm hơn fault năng lượng (energy / 에너지);
- probe ground lead tạo ringing giả.

> **Chuyển mạch:** Ở chặng này của **Switching Converters and Protection — Converter, switching và bảo vệ**, **Cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Thất bại (failure / 실패) modes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [control systems](../control_systems/00_feedback_stability_pid.md) để phân tích vòng lặp (loop / 루프), [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho digital power điều khiển (control / 제어), và Physics về semiconductor/thiết bị (device / 장치) hành vi (behavior / 동작).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
