# Digital Electronics — Điện tử số

> **Mạch đọc:** README này là owner của **Digital Electronics — Điện tử số**. Route đi từ transistor/gates và voltage/noise margins → sequential logic/state machines → memory, timing và buses → programmable hardware → verification, power và failure, để 0/1 luôn được nối với vật lý thực.

Nhánh này giải thích cách transistor và lô-gic (logic / 논리) gate trở thành máy trạng thái (state machine / 상태 머신), bộ nhớ (memory / 메모리), clocked hệ thống (system / 시스템) và programmable hardware. “0/1” là lớp trừu tượng (abstraction / 추상화) có voltage, noise margin, delay và năng lượng (energy / 에너지) ở bên dưới.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
Boolean logic → combinational circuits → flip-flop/register → FSM → memory/bus → HDL/FPGA
```

> **Chuyển mạch:** **Cốt lõi tuyến** đi từ logic và timing đến memory, bus và HDL; **Cốt lõi chapter** giải thích từng cơ chế, còn **Cần nắm** chốt điều kiện cần đo.

## Cốt lõi (core / 핵심) chapter

- [Logic, timing and state](00_logic_timing_state.md) — voltage margin, setup/hold, metastability, FSM, reset và xác minh (verification / 확인).
- [Memory, buses and HDL verification](01_memory_buses_hdl_verification.md) — SRAM/DRAM/Flash, ready/valid, FIFO, assertions và synthesis ranh giới (boundary / 경계).

> **Chuyển mạch:** Sau khi nắm logic, timing và bus, **Cầu nối** đưa chúng vào thiết kế, verification và giới hạn phần cứng thực.

## Cần nắm

- voltage thresholds, noise margin, propagation delay và fan-out;
- setup/hold, clock skew, metastability và synchronizer;
- latches/flip-flops, counters, FIFOs, arbiters và reset ngữ nghĩa (semantics / 의미론);
- SRAM/DRAM/Flash ở mức giao diện (interface / 인터페이스) và sự đánh đổi (trade-off / 트레이드오프) độ trễ (latency / 지연 시간)/năng lượng (energy / 에너지)/density;
- synchronous thiết kế (design / 설계), timing closure và simulation-vs-hardware mismatch.

> **Chuyển mạch:** **Cầu nối** khép README bằng tiêu chí nối biểu diễn logic với tín hiệu, kiểm thử và owner chapter kế tiếp.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/README.md), còn CPU/ISA và bộ nhớ (memory / 메모리) hierarchy sâu hơn thuộc [Computer Science](../../computer_science/02_computer_architecture/README.md).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
