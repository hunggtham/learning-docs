# Memory, Buses and HDL Verification — Memory, bus và HDL

Logic gate chỉ là phần đầu. Hệ thống số có giá trị khi state được lưu, transaction có protocol và implementation được chứng minh trước khi synthesis hoặc tape-out.

## 1. Memory trade-off

SRAM nhanh và tốn diện tích; DRAM dense nhưng cần refresh; Flash non-volatile nhưng có erase/program granularity và wear. Chọn memory theo latency, bandwidth, endurance, retention, power và fault model.

## 2. Ready/valid và backpressure

Một streaming interface có thể dùng ready/valid: transfer xảy ra khi cả hai cùng high trong clock edge. Producer không được đổi payload khi valid high nhưng ready low; consumer không được nhận khi valid low. Backpressure là một phần correctness, không chỉ tối ưu throughput.

## 3. HDL là mô tả hardware

Một đoạn HDL có thể suy ra combinational logic, latch hoặc flip-flop tùy sensitivity/assignment. Simulation semantics và synthesis semantics phải được kiểm tra cùng nhau. Nonblocking assignment thường diễn tả sequential update; blocking assignment phù hợp hơn trong combinational procedural logic khi dùng đúng discipline.

## 4. Verification strategy

- unit test cho module;
- assertion cho protocol/timing invariant;
- constrained-random cho state combination;
- functional coverage để biết scenario nào đã chạy;
- formal proof cho property có thể biểu diễn;
- gate-level/timing simulation chỉ cho lớp vấn đề tương ứng.

## 5. Worked reasoning: FIFO

FIFO cần định nghĩa empty/full, simultaneous read/write, pointer wrap, reset và overflow/underflow. FIFO crossing clock domain cần Gray-coded pointer hoặc asynchronous FIFO primitive; chỉ đồng bộ từng bit của binary counter có thể tạo trạng thái giả.

## Bridge

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho memory-mapped peripheral và [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) cho bus transaction.
