# RTOS Scheduling and xác minh (verification / 확인) — Scheduling, RTOS và xác minh (verification / 확인)

> **Mạch đọc:** Đặt **RTOS Scheduling and xác minh (verification / 확인) — Scheduling, RTOS và xác minh (verification / 확인)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **1. Priority và blocking** sang **2. WCET và deadline**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

MCU chapter mô tả thời gian chạy (runtime / 런타임). Chapter này đi vào câu hỏi nhiều tác vụ (task / 작업) cùng tranh CPU, bus và bộ nhớ (memory / 메모리) thì làm sao chứng minh deadline, isolation và khôi phục (recovery / 복구).

## 1. Priority và blocking

Priority-based scheduler cần phân tích preemption, trọng yếu (critical / 중요) section, interrupt interference và priority inversion. Priority inheritance có thể giảm inversion nhưng không thay thế việc giới hạn khóa (lock / 잠금) hold thời gian (time / 시간).


> **Chuyển mạch:** Từ **1. Priority và blocking**, ta sang **2. WCET và deadline** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 2. WCET và deadline

Worst-case thực thi (execution / 실행) thời gian (time / 시간) phải đo ở bộ nhớ đệm (cache / 캐시), branch, bus và trình biên dịch (compiler / 컴파일러) cấu hình (configuration / 구성) phù hợp. dấu vết (trace / 추적) average độ trễ (latency / 지연 시간) chỉ cho biết typical đường dẫn (path / 경로). Deadline miss cần chính sách (policy / 정책): skip mẫu (sample / 표본), degrade đầu ra (output / 출력), reset subsystem hay chuyển safe trạng thái (state / 상태).


> **Chuyển mạch:** Từ **2. WCET và deadline**, ta sang **3. bộ nhớ (memory / 메모리) và fault containment** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 3. bộ nhớ (memory / 메모리) và fault containment

MPU/MMU, ngăn xếp (stack / 스택) watermark, vùng nhớ động (heap / 힙) chính sách (policy / 정책) và quyền sở hữu (ownership / 소유권) giúp một tác vụ (task / 작업) lỗi không phá toàn bộ hệ. động (dynamic / 동적) allocation trong real-time không sai tuyệt đối, nhưng fragmentation và unbounded độ trễ (latency / 지연 시간) phải được kiểm soát.


> **Chuyển mạch:** Từ **3. bộ nhớ (memory / 메모리) và fault containment**, ta sang **4. xác minh (verification / 확인) ladder** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## 4. xác minh (verification / 확인) ladder

    Đơn vị (unit / 단위) → tích hợp (integration / 통합) → timing dấu vết (trace / 추적) → HIL → fault injection → trường dữ liệu (field / 필드) telemetry

Kiểm thử (test / 테스트) phải bao gồm clock drift, hàng đợi (queue / 큐) full, DMA lỗi (error / 오류), watchdog, brownout và firmware quay lui (rollback / 롤백). Pass functional kiểm thử (test / 테스트) không chứng minh pass temporal/an toàn (safety / 안전) đặc tả hợp đồng (contract / 계약).


> **Chuyển mạch:** Từ **4. xác minh (verification / 확인) ladder**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) để kiểm tra quyền sở hữu (ownership / 소유권) ở bus ranh giới (boundary / 경계) và [control systems](../control_systems/01_state_space_discrete_control.md) cho deadline của vòng điều khiển (control loop / 제어 루프).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mcu runtime real time](./00_mcu_runtime_real_time.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
