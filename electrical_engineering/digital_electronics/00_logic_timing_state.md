# Logic, Timing and State — Logic, timing và trạng thái

Digital electronics dùng các vùng điện áp để biểu diễn logic, nhưng hệ thống số thật vẫn chịu delay, noise, loading, clock skew, metastability và power. Thiết kế số là thiết kế state transitions có timing contract.

## 1. Từ voltage đến Boolean

Một cổng logic không nhận “0/1” trừu tượng; nó nhận khoảng điện áp. VIL, VIH, VOL, VOH tạo noise margin:

    NMH = VOH(min) - VIH(min)
    NML = VIL(max) - VOL(max)

Nếu output của driver không đủ margin cho input kế tiếp, Boolean simulation vẫn đúng nhưng hardware có thể fail theo nhiệt độ hoặc nhiễu.

## 2. Combinational và sequential

Combinational circuit có output là hàm của input hiện tại. Sequential circuit có state q:

    q_next = F(q, x)
    y = G(q, x)

Flip-flop chụp input quanh clock edge. Timing contract cơ bản:

    t_clk_period ≥ t_clk_to_q + t_comb + t_setup + skew + margin

Hold constraint kiểm tra dữ liệu mới không đến quá sớm sau clock edge.

## 3. Metastability

Nếu input đổi gần sampling edge, flip-flop có thể tạm thời không settle về 0 hoặc 1. Đây là giới hạn analog của bistable circuit. Với tín hiệu asynchronous, dùng synchronizer nhiều tầng và chấp nhận xác suất lỗi giảm theo thời gian settle.

Không dùng một synchronizer cho bus nhiều bit rồi giả định cả bus nhất quán. Dùng handshake, Gray code hoặc asynchronous FIFO tùy semantics.

## 4. FSM và invariant

Một finite-state machine nên xác định rõ:

    state set → input event → next-state → output → illegal-state recovery

Ví dụ protocol receiver không chỉ có IDLE → DATA → DONE; cần xử lý timeout, framing error, reset giữa packet và input đến khi buffer đầy. Invariant như “không phát DONE trước khi checksum pass” nên xuất hiện trong simulation/assertion.

## 5. Clock, reset và power

Clock domain crossing cần protocol; không giải quyết bằng cách “đọc hai lần” một cách mơ hồ. Reset cũng có semantics: synchronous hay asynchronous, reset release có đồng bộ không, trạng thái sau brownout có an toàn không, memory/peripheral reset có cùng thời điểm không.

Clock gating giảm dynamic power nhưng tạo clock-domain và wake-up complexity. Power intent phải được xem cùng logic correctness.

## 6. Worked reasoning: counter 100 MHz

Một counter 32-bit chạy ở 100 MHz overflow sau khoảng 42.95 s. Nếu firmware dùng counter để timeout 60 s mà không xử lý wrap-around, so sánh tuyệt đối sẽ fail. Cách đúng là dùng unsigned elapsed-time arithmetic modulo 2^32, miễn timeout nhỏ hơn nửa chu kỳ wrap.

Đây là ví dụ hardware state nối trực tiếp với software time semantics.

## 7. Verification

- truth table và Boolean simplification cho combinational logic;
- waveform với clock/reset/error cases;
- assertion cho safety invariant và protocol ordering;
- static timing analysis cho setup/hold;
- CDC analysis và metastability assumptions;
- FPGA/board test với clock, voltage và temperature corners.

## Failure modes

- glitch combinational đi vào clock/reset;
- inferred latch do thiếu assignment;
- simulation dùng ideal zero-delay nhưng silicon có race;
- reset release khác domain tạo state không xác định;
- bus width/endianness mismatch ở hardware–software boundary.

## Bridge

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) để chạy state machine trong MCU/SoC, hoặc [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) để định nghĩa register/bus contract. Computer Architecture mở rộng phần này sang CPU, ISA và memory hierarchy.
