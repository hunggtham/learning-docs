# RTOS Scheduling and Verification — Scheduling, RTOS và verification

MCU chapter mô tả runtime. Chapter này đi vào câu hỏi nhiều task cùng tranh CPU, bus và memory thì làm sao chứng minh deadline, isolation và recovery.

## 1. Priority và blocking

Priority-based scheduler cần phân tích preemption, critical section, interrupt interference và priority inversion. Priority inheritance có thể giảm inversion nhưng không thay thế việc giới hạn lock hold time.

## 2. WCET và deadline

Worst-case execution time phải đo ở cache, branch, bus và compiler configuration phù hợp. Trace average latency chỉ cho biết typical path. Deadline miss cần policy: skip sample, degrade output, reset subsystem hay chuyển safe state.

## 3. Memory và fault containment

MPU/MMU, stack watermark, heap policy và ownership giúp một task lỗi không phá toàn bộ hệ. Dynamic allocation trong real-time không sai tuyệt đối, nhưng fragmentation và unbounded latency phải được kiểm soát.

## 4. Verification ladder

    unit → integration → timing trace → HIL → fault injection → field telemetry

Test phải bao gồm clock drift, queue full, DMA error, watchdog, brownout và firmware rollback. Pass functional test không chứng minh pass temporal/safety contract.

## Bridge

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md) để kiểm tra ownership ở bus boundary và [control systems](../control_systems/01_state_space_discrete_control.md) cho deadline của control loop.
