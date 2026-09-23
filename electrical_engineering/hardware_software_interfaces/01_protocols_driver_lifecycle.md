# Protocols and Driver Lifecycle — Protocol và vòng đời driver

Register contract cần được đặt vào lifecycle: discovery, init, active operation, error recovery, suspend/resume, update và removal.

## 1. Protocol semantics

SPI thường không có framing/error semantics built-in như CAN; I²C có arbitration và ACK nhưng cần bus recovery; UART không tự bảo đảm packet boundary; CAN có arbitration và fault confinement. Chọn bus theo failure model, không chỉ theo tốc độ danh nghĩa.

## 2. State machine của driver

Driver nên có state rõ:

    RESET → PROBING → READY → RUNNING → DEGRADED → RECOVERING → OFFLINE

Mỗi transition cần trigger, timeout, side effect và observable evidence. Một timeout không được tự động retry nếu hardware chưa xác nhận command đã dừng.

## 3. ABI, schema và compatibility

Header/ABI, register schema, firmware version và calibration data đều là compatibility surface. Thay đổi field reserved, alignment hoặc endian có thể phá consumer dù function name không đổi.

## 4. Worked reasoning: I²C stuck bus

Nếu slave giữ SDA low sau reset giữa byte, controller không thể gửi command mới. Recovery có thể toggle SCL hữu hạn lần, phát STOP, reset peripheral và re-probe. Nếu vẫn fail, driver phải chuyển OFFLINE và báo rõ nguyên nhân thay vì loop retry vô hạn.

## 5. Observability

Telemetry nên ghi transaction id, bus error, retry count, reset cause, firmware/hardware revision và timing. Log một “read failed” không đủ để tái hiện race hoặc power fault.

## Bridge

Đi tiếp sang [embedded systems](../embedded_systems/01_rtos_scheduling_verification.md) cho scheduling/ownership và Computer Science về API evolution, concurrency và fault recovery.
