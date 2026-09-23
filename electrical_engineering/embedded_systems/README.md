# Embedded Systems — Hệ thống nhúng

Embedded systems là nơi điện tử, timing, firmware và physical environment gặp nhau. Một system đúng không chỉ trả về giá trị đúng; nó phải đúng thời hạn, trong power/thermal/memory budget và có hành vi an toàn khi peripheral hoặc sensor hỏng.

## Core route

```text
MCU/SoC → clock/reset/power → GPIO/timer/ADC → interrupt/DMA → RTOS/real-time → bring-up → verification
```

## Core chapter

- [MCU runtime and real-time reasoning](00_mcu_runtime_real_time.md) — boot ownership, ISR/DMA, WCET, timer wrap, watchdog và bring-up evidence.
- [RTOS scheduling and verification](01_rtos_scheduling_verification.md) — priority inversion, WCET, isolation, HIL và fault injection.

## Cần nắm

- boot chain, memory map, register access và peripheral state machine;
- interrupt latency, priority inversion, DMA ownership và cache coherency;
- deterministic scheduling, deadline, jitter, watchdog và brownout;
- board bring-up, signal integrity, logging/trace và hardware-in-the-loop test;
- update/rollback, secure boot và field failure recovery.

## Bridge

Digital logic là prerequisite; [hardware–software interfaces](../hardware_software_interfaces/README.md) giữ contract chi tiết. OS, concurrency và architecture semantics sâu hơn thuộc [Computer Science](../../computer_science/README.md).
