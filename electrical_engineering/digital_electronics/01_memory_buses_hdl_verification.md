# Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL

> **Mạch đọc:** [README](../README.md) là owner của **Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL**; đặt chapter sau logic/timing/state trong tuyến digital electronics. Từ **1. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)** nối sang ready/valid, backpressure, HDL modeling và verification, rồi dùng latency/bandwidth/fault evidence để quyết định kiến trúc bus và bộ nhớ.

Lô-gic (logic / 논리) gate chỉ là phần đầu. Hệ thống số có giá trị khi trạng thái (state / 상태) được lưu, giao dịch (transaction / 트랜잭션) có giao thức (protocol / 프로토콜) và hiện thực (implementation / 구현) được chứng minh trước khi synthesis hoặc tape-out.

## 1. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)

SRAM nhanh và tốn diện tích; DRAM dense nhưng cần refresh; Flash non-volatile nhưng có erase/program granularity và wear. Chọn bộ nhớ (memory / 메모리) theo độ trễ (latency / 지연 시간), bandwidth, endurance, retention, power và fault mô hình (model / 모델).

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL**, **2. Ready/valid và backpressure** tiếp nhận điểm tựa từ **1. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **3. HDL là mô tả hardware** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Ready/valid và backpressure

Một streaming giao diện (interface / 인터페이스) có thể dùng ready/valid: transfer xảy ra khi cả hai cùng high trong clock edge. Producer không được đổi payload khi valid high nhưng ready low; bên tiêu thụ (consumer / 소비자) không được nhận khi valid low. Backpressure là một phần tính đúng đắn (correctness / 정확성), không chỉ tối ưu thông lượng (throughput / 처리량).

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL**, **3. HDL là mô tả hardware** tiếp nhận điểm tựa từ **2. Ready/valid và backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. xác minh (verification / 확인) chiến lược (strategy / 전략)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. HDL là mô tả hardware

Một đoạn HDL có thể suy ra combinational lô-gic (logic / 논리), latch hoặc flip-flop tùy sensitivity/assignment. Simulation ngữ nghĩa (semantics / 의미론) và synthesis ngữ nghĩa (semantics / 의미론) phải được kiểm tra cùng nhau. Nonblocking assignment thường diễn tả sequential cập nhật (update / 업데이트); blocking assignment phù hợp hơn trong combinational procedural lô-gic (logic / 논리) khi dùng đúng discipline.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL**, **4. xác minh (verification / 확인) chiến lược (strategy / 전략)** tiếp nhận điểm tựa từ **3. HDL là mô tả hardware** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Worked lập luận (reasoning / 추론): FIFO** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. xác minh (verification / 확인) chiến lược (strategy / 전략)

- đơn vị (unit / 단위) kiểm thử (test / 테스트) cho mô-đun (module / 모듈);
- assertion cho giao thức (protocol / 프로토콜)/timing bất biến (invariant / 불변식);
- constrained-random cho trạng thái (state / 상태) combination;
- functional coverage để biết scenario nào đã chạy;
- formal proof cho thuộc tính (property / 속성) có thể biểu diễn;
- gate-level/timing simulation chỉ cho lớp vấn đề tương ứng.

> **Chuyển mạch:** Trong **Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL**, **4. xác minh (verification / 확인) chiến lược (strategy / 전략)** cho ta quy tắc; **5. Worked lập luận (reasoning / 추론): FIFO** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Worked lập luận (reasoning / 추론): FIFO

FIFO cần định nghĩa empty/full, simultaneous read/ghi (write / 쓰기), pointer wrap, reset và overflow/underflow. FIFO crossing clock lĩnh vực (domain / 도메인) cần Gray-coded pointer hoặc asynchronous FIFO thành phần nguyên thủy (primitive / 기본 요소); chỉ đồng bộ từng bit của nhị phân (binary / 이진) counter có thể tạo trạng thái giả.

> **Chuyển mạch:** Ở chặng này của **Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL**, **5. Worked lập luận (reasoning / 추론): FIFO** cho ta quy tắc; **Cầu nối (bridge / 브리지)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho memory-mapped peripheral và [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) cho bus giao dịch (transaction / 트랜잭션).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
