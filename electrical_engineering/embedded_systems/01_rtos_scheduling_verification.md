# RTOS Scheduling and xác minh (verification / 확인) — Scheduling, RTOS và xác minh (verification / 확인)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **RTOS Scheduling and xác minh (verification / 확인) — Scheduling, RTOS và xác minh (verification / 확인)**. Route đi từ priority/blocking → WCET/deadlines → scheduling policies, interrupts và bus contention → isolation/recovery → verification evidence, để realtime claims được chứng minh thay vì giả định.

MCU chapter mô tả thời gian chạy (runtime / 런타임). Chapter này đi vào câu hỏi nhiều tác vụ (task / 작업) cùng tranh CPU, bus và bộ nhớ (memory / 메모리) thì làm sao chứng minh deadline, isolation và khôi phục (recovery / 복구).

## 1. Priority và blocking

Priority-based scheduler cần phân tích preemption, trọng yếu (critical / 중요) section, interrupt interference và priority inversion. Priority inheritance có thể giảm inversion nhưng không thay thế việc giới hạn khóa (lock / 잠금) hold thời gian (time / 시간).

Sau khi xác định quan hệ chờ và nguy cơ priority inversion, ta cần định lượng thời gian đáp ứng ở tình huống xấu nhất. Vì vậy phần tiếp theo chuyển sang WCET và deadline; sau đó các giới hạn bộ nhớ và fault containment sẽ cho biết một task lỗi có thể lan tới đâu.

## 2. WCET và deadline

Worst-case thực thi (execution / 실행) thời gian (time / 시간) phải đo ở bộ nhớ đệm (cache / 캐시), branch, bus và trình biên dịch (compiler / 컴파일러) cấu hình (configuration / 구성) phù hợp. dấu vết (trace / 추적) average độ trễ (latency / 지연 시간) chỉ cho biết typical đường dẫn (path / 경로). Deadline miss cần chính sách (policy / 정책): skip mẫu (sample / 표본), degrade đầu ra (output / 출력), reset subsystem hay chuyển safe trạng thái (state / 상태).

Deadline chỉ có ý nghĩa khi đi kèm bằng chứng. Từ các giới hạn thời gian và khả năng cô lập ở trên, phần **4. Verification ladder** sắp xếp kiểm thử từ unit đến timing để mỗi claim an toàn có mức kiểm chứng tương ứng.

## 3. bộ nhớ (memory / 메모리) và fault containment

MPU/MMU, ngăn xếp (stack / 스택) watermark, vùng nhớ động (heap / 힙) chính sách (policy / 정책) và quyền sở hữu (ownership / 소유권) giúp một tác vụ (task / 작업) lỗi không phá toàn bộ hệ. động (dynamic / 동적) allocation trong real-time không sai tuyệt đối, nhưng fragmentation và unbounded độ trễ (latency / 지연 시간) phải được kiểm soát.

Verification ladder kết nối các lớp thời gian, bộ nhớ và recovery thành một chuỗi bằng chứng. Phần **Cầu nối** tiếp theo sẽ ghi rõ điều kiện bàn giao sang firmware hoặc system audit, nơi các quyền sở hữu và giới hạn runtime được theo dõi tiếp.

## 4. xác minh (verification / 확인) ladder

    Đơn vị (unit / 단위) → tích hợp (integration / 통합) → timing dấu vết (trace / 추적) → HIL → fault injection → trường dữ liệu (field / 필드) telemetry

Kiểm thử (test / 테스트) phải bao gồm clock drift, hàng đợi (queue / 큐) full, DMA lỗi (error / 오류), watchdog, brownout và firmware quay lui (rollback / 롤백). Pass functional kiểm thử (test / 테스트) không chứng minh pass temporal/an toàn (safety / 안전) đặc tả hợp đồng (contract / 계약).

Như vậy, priority, deadline, containment và test evidence đã được đặt trong cùng một chu trình kiểm chứng. Có thể dùng **Cầu nối** như checklist RTOS lặp lại khi chuyển sang bus, firmware hoặc vòng điều khiển.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) để kiểm tra quyền sở hữu (ownership / 소유권) ở bus ranh giới (boundary / 경계) và [control systems](../control_systems/01_state_space_discrete_control.md) cho deadline của vòng điều khiển (control loop / 제어 루프).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
