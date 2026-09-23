# Digital Electronics — Điện tử số

Nhánh này giải thích cách transistor và logic gate trở thành state machine, memory, clocked system và programmable hardware. “0/1” là abstraction có voltage, noise margin, delay và energy ở bên dưới.

## Core route

```text
Boolean logic → combinational circuits → flip-flop/register → FSM → memory/bus → HDL/FPGA
```

## Core chapter

- [Logic, timing and state](00_logic_timing_state.md) — voltage margin, setup/hold, metastability, FSM, reset và verification.
- [Memory, buses and HDL verification](01_memory_buses_hdl_verification.md) — SRAM/DRAM/Flash, ready/valid, FIFO, assertions và synthesis boundary.

## Cần nắm

- voltage thresholds, noise margin, propagation delay và fan-out;
- setup/hold, clock skew, metastability và synchronizer;
- latches/flip-flops, counters, FIFOs, arbiters và reset semantics;
- SRAM/DRAM/Flash ở mức interface và trade-off latency/energy/density;
- synchronous design, timing closure và simulation-vs-hardware mismatch.

## Bridge

Đi tiếp sang [embedded systems](../embedded_systems/README.md), còn CPU/ISA và memory hierarchy sâu hơn thuộc [Computer Science](../../computer_science/02_computer_architecture/README.md).
