# MCU Runtime and Real-Time Reasoning — MCU, runtime và real-time

Embedded system là một closed-loop giữa code và physical world. Correctness có hai chiều: giá trị phải đúng (functional correctness) và phải đến đúng deadline (temporal correctness).

## 1. Boot và ownership

Một MCU thường đi qua:

    reset/vector → clock/power init → memory init
    → peripheral init → scheduler/main loop → application

Mỗi peripheral cần owner rõ: ai cấu hình, ai đọc/ghi, ai xử lý error, và trạng thái khi reset/power transition là gì. Global register access không phải architecture.

## 2. Interrupt, DMA và concurrency

Interrupt handler nên ngắn: acknowledge source, capture minimal state, enqueue work. Logic dài trong ISR làm tăng latency của interrupt khác và gây jitter.

DMA giảm CPU copy nhưng tạo ownership problem:

    producer writes buffer → memory visibility/cache sync
    → consumer reads → producer reclaims

Buffer descriptor cần trạng thái rõ ràng; không dùng một flag thiếu memory ordering để đồng bộ giữa CPU/DMA.

## 3. Real-time budget

Với task periodic, utilization đơn giản là:

    U = tổng Ci / Ti

Ci là worst-case execution time, Ti là period. Average execution time không đủ cho deadline analysis. Cần cộng interrupt interference, blocking, cache miss, bus contention và safety margin.

Jitter có thể làm control loop kém ổn định dù average frequency đúng.

## 4. Timer và timestamp

Hardware timer overflow là bình thường. Timestamp nên so sánh theo modulo arithmetic:

    elapsed = now - then

với điều kiện interval nhỏ hơn nửa chu kỳ counter. Không đổi timer ticks sang milliseconds bằng integer division sớm nếu cần precision.

## 5. Safety và degraded mode

Watchdog không sửa được mọi lỗi; nó chỉ reset khi software không kick đúng contract. Thiết kế cần xác định reset có làm actuator về state an toàn không, brownout có thể ghi dở persistent state không, sensor invalid có được phát hiện bằng range/rate/plausibility checks không, firmware update fail giữa chừng có rollback không.

## 6. Worked reasoning: sampling sensor 1 kHz

Nếu sensor cần sample mỗi 1 ms, task period là 1 ms. Nhưng deadline thực tế bao gồm ADC acquisition, DMA completion, filter, control calculation và output update. Nếu worst-case là 0.7 ms, utilization riêng task là 70%; thêm ISR và communication có thể vượt budget. Tăng average CPU speed không chứng minh worst-case pass nếu bus contention chưa đo.

## 7. Bring-up và evidence

Trình tự bring-up nên cô lập failure domain:

    power rails → clock/reset → debug link → GPIO heartbeat
    → one peripheral → sensor path → actuator guarded → full application

Mỗi bước cần waveform/register/log evidence. Nếu chỉ “board chạy”, ta không biết timing margin hoặc recovery behavior.

## Failure modes

- priority inversion làm task quan trọng miss deadline;
- ISR và main loop cùng sửa buffer không có ownership;
- compiler optimization làm register access sai vì thiếu volatile/barrier;
- watchdog reset nhưng không lưu fault cause;
- firmware update đổi register contract mà driver cũ vẫn chạy.

## Bridge

Đi tiếp sang [hardware–software interfaces](../hardware_software_interfaces/00_register_bus_driver_contracts.md), [digital electronics](../digital_electronics/00_logic_timing_state.md) và Computer Science về concurrency/architecture.
