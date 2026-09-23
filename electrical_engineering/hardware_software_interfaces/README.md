# Hardware–Software Interfaces — Giao diện phần cứng–phần mềm

Nhánh này mô tả contract nơi register, bus transaction, interrupt, DMA, boot và driver biến hành vi phần cứng thành API mà software có thể tin cậy. Đây là điểm nối trực tiếp nhất từ Electrical Engineering sang Computer Architecture và Software.

## Core route

```text
register map → bus protocol → driver contract → interrupt/DMA → boot/update → observability/fault recovery
```

## Core chapter

- [Register, bus and driver contracts](00_register_bus_driver_contracts.md) — register semantics, ordering, DMA ownership, errors, boot/update và compatibility.
- [Protocols and driver lifecycle](01_protocols_driver_lifecycle.md) — bus failure semantics, state machine, compatibility, recovery và observability.

## Cần nắm

- memory-mapped I/O, volatile/ordering, atomicity và side effects;
- SPI/I²C/UART/CAN/USB/Ethernet ở boundary transaction và failure semantics;
- interrupt acknowledgement, queue ownership, DMA buffer lifetime và cache;
- reset/power sequencing, bootloader, firmware versioning và rollback;
- timeout, retry, idempotency, degraded mode và diagnostic evidence.

## Bridge

Đọc cùng [embedded systems](../embedded_systems/README.md), [digital electronics](../digital_electronics/README.md) và [Computer Science](../../computer_science/README.md). Protocol semantics không thay thế electrical timing, và driver API không được che giấu safety-critical failure.
