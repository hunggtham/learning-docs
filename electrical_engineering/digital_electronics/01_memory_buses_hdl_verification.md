# Bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL

> **Mạch đọc:** Đặt **bộ nhớ (memory / 메모리), Buses and HDL xác minh (verification / 확인) — bộ nhớ (memory / 메모리), bus và HDL** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)** sang **2. Ready/valid và backpressure**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Lô-gic (logic / 논리) gate chỉ là phần đầu. Hệ thống số có giá trị khi trạng thái (state / 상태) được lưu, giao dịch (transaction / 트랜잭션) có giao thức (protocol / 프로토콜) và hiện thực (implementation / 구현) được chứng minh trước khi synthesis hoặc tape-out.

## 1. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)

SRAM nhanh và tốn diện tích; DRAM dense nhưng cần refresh; Flash non-volatile nhưng có erase/program granularity và wear. Chọn bộ nhớ (memory / 메모리) theo độ trễ (latency / 지연 시간), bandwidth, endurance, retention, power và fault mô hình (model / 모델).


> **Chuyển mạch:** Từ **1. bộ nhớ (memory / 메모리) sự đánh đổi (trade-off / 트레이드오프)**, ta sang **2. Ready/valid và backpressure** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. Ready/valid và backpressure

Một streaming giao diện (interface / 인터페이스) có thể dùng ready/valid: transfer xảy ra khi cả hai cùng high trong clock edge. Producer không được đổi payload khi valid high nhưng ready low; bên tiêu thụ (consumer / 소비자) không được nhận khi valid low. Backpressure là một phần tính đúng đắn (correctness / 정확성), không chỉ tối ưu thông lượng (throughput / 처리량).


> **Chuyển mạch:** Từ **2. Ready/valid và backpressure**, ta sang **3. HDL là mô tả hardware** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. HDL là mô tả hardware

Một đoạn HDL có thể suy ra combinational lô-gic (logic / 논리), latch hoặc flip-flop tùy sensitivity/assignment. Simulation ngữ nghĩa (semantics / 의미론) và synthesis ngữ nghĩa (semantics / 의미론) phải được kiểm tra cùng nhau. Nonblocking assignment thường diễn tả sequential cập nhật (update / 업데이트); blocking assignment phù hợp hơn trong combinational procedural lô-gic (logic / 논리) khi dùng đúng discipline.


> **Chuyển mạch:** Từ **3. HDL là mô tả hardware**, ta sang **4. xác minh (verification / 확인) chiến lược (strategy / 전략)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. xác minh (verification / 확인) chiến lược (strategy / 전략)
Phần “4. xác minh (verification / 확인) chiến lược (strategy / 전략)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- đơn vị (unit / 단위) kiểm thử (test / 테스트) cho mô-đun (module / 모듈);
- assertion cho giao thức (protocol / 프로토콜)/timing bất biến (invariant / 불변식);
- constrained-random cho trạng thái (state / 상태) combination;
- functional coverage để biết scenario nào đã chạy;
- formal proof cho thuộc tính (property / 속성) có thể biểu diễn;
- gate-level/timing simulation chỉ cho lớp vấn đề tương ứng.


> **Chuyển mạch:** Từ **4. xác minh (verification / 확인) chiến lược (strategy / 전략)**, ta sang **5. Worked lập luận (reasoning / 추론): FIFO** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 5. Worked lập luận (reasoning / 추론): FIFO

FIFO cần định nghĩa empty/full, simultaneous read/ghi (write / 쓰기), pointer wrap, reset và overflow/underflow. FIFO crossing clock lĩnh vực (domain / 도메인) cần Gray-coded pointer hoặc asynchronous FIFO thành phần nguyên thủy (primitive / 기본 요소); chỉ đồng bộ từng bit của nhị phân (binary / 이진) counter có thể tạo trạng thái giả.


> **Chuyển mạch:** Từ **5. Worked lập luận (reasoning / 추론): FIFO**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md) cho memory-mapped peripheral và [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) cho bus giao dịch (transaction / 트랜잭션).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 logic timing state](./00_logic_timing_state.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
