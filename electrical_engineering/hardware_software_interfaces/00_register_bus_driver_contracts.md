# Register, Bus and Driver Contracts — Contract phần cứng–phần mềm

Hardware–software interface là contract có timing, ordering, side effects và failure semantics. Một register map không chỉ là bảng địa chỉ; nó là API thấp tầng mà firmware, bootloader, driver, test và tooling cùng phụ thuộc.

## 1. Register semantics

Mỗi field cần mô tả:

    address → width → reset value → access mode
    → side effect → timing → error/status → ownership

Các access mode RW, RO, WO, write-one-to-clear và read-to-clear có semantics khác nhau. Đọc status register hai lần có thể làm mất event nếu register có side effect.

## 2. Ordering và visibility

CPU compiler, cache, bus fabric và peripheral đều có thể reorder hoặc buffer transaction. Volatile chỉ nói compiler không bỏ access; nó không tự tạo atomicity, inter-core ordering hay DMA cache coherence.

Một driver cần xác định write nào phải barrier trước enable, status nào phải đọc sau khi poll, timeout tính từ request hay từ hardware acceptance, và interrupt acknowledge trước hay sau khi clear source.

## 3. Bus protocol

SPI, I²C, UART, CAN và các bus khác cần phân biệt electrical layer với transaction contract: voltage/drive/pull-up/termination, framing/addressing/arbitration, maximum clock/setup/hold, NACK/timeout/bus recovery, duplicate/retry và idempotency.

Gửi được byte chưa chứng minh protocol đúng nếu reset giữa transaction hoặc bus contention chưa được xử lý.

## 4. Interrupt và DMA contract

Interrupt source cần state machine rõ:

    event asserted → status observed → source acknowledged
    → work captured → handler returns → event cannot be lost/duplicated

DMA descriptor cần ownership bit hoặc queue protocol. Cache maintenance phải nằm trong contract nếu CPU đọc vùng memory mà DMA vừa ghi.

## 5. Driver API và error semantics

Driver không nên trả một mã lỗi cho mọi lỗi. Cần phân biệt invalid argument, device not ready, transient timeout, permanent hardware fault, data integrity failure và cancellation/reset in progress.

Retry chỉ an toàn khi operation idempotent hoặc có transaction identity. Retry write register có side effect có thể tạo hành động lặp.

## 6. Worked reasoning: write-enable sequence

Giả sử peripheral yêu cầu ghi CONFIG, chờ READY, rồi set ENABLE. Nếu firmware set ENABLE trước khi READY, hardware có thể bỏ request hoặc vào fault state. Contract đúng cần:

    reset deasserted
    → clock enabled
    → CONFIG write posted
    → read-back/barrier
    → READY observed within deadline
    → ENABLE set
    → ACTIVE observed

Test phải inject READY timeout, bus error và reset giữa các bước; happy path không đủ.

## 7. Boot, update và compatibility

Firmware version phải tương thích với hardware revision và register schema. Bootloader cần xác định image validity, power loss giữa update, rollback và monotonic version để tránh downgrade không mong muốn.

## Failure modes

- register header đúng tên nhưng sai endianness/bitfield packing;
- clear-on-read làm mất interrupt khi debug;
- driver timeout nhưng hardware vẫn đang chạy, tạo duplicate command;
- DMA ghi vào buffer trước khi CPU invalidate cache;
- firmware update thành công nhưng calibration/schema cũ không tương thích.

## Bridge

Đọc cùng [embedded systems](../embedded_systems/00_mcu_runtime_real_time.md), [digital electronics](../digital_electronics/00_logic_timing_state.md) và Computer Architecture về I/O, interrupt, DMA, ABI và memory ordering.
