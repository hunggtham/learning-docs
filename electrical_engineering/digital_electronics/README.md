# Digital Electronics — Điện tử số

> **Mạch đọc:** Đọc **Digital Electronics — Điện tử số** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Nhánh này giải thích cách transistor và lô-gic (logic / 논리) gate trở thành máy trạng thái (state machine / 상태 머신), bộ nhớ (memory / 메모리), clocked hệ thống (system / 시스템) và programmable hardware. “0/1” là lớp trừu tượng (abstraction / 추상화) có voltage, noise margin, delay và năng lượng (energy / 에너지) ở bên dưới.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
Boolean logic → combinational circuits → flip-flop/register → FSM → memory/bus → HDL/FPGA
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter

- [Logic, timing and state](00_logic_timing_state.md) — voltage margin, setup/hold, metastability, FSM, reset và xác minh (verification / 확인).
- [Memory, buses and HDL verification](01_memory_buses_hdl_verification.md) — SRAM/DRAM/Flash, ready/valid, FIFO, assertions và synthesis ranh giới (boundary / 경계).


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm

- voltage thresholds, noise margin, propagation delay và fan-out;
- setup/hold, clock skew, metastability và synchronizer;
- latches/flip-flops, counters, FIFOs, arbiters và reset ngữ nghĩa (semantics / 의미론);
- SRAM/DRAM/Flash ở mức giao diện (interface / 인터페이스) và sự đánh đổi (trade-off / 트레이드오프) độ trễ (latency / 지연 시간)/năng lượng (energy / 에너지)/density;
- synchronous thiết kế (design / 설계), timing closure và simulation-vs-hardware mismatch.


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đi tiếp sang [embedded systems](../embedded_systems/README.md), còn CPU/ISA và bộ nhớ (memory / 메모리) hierarchy sâu hơn thuộc [Computer Science](../../computer_science/02_computer_architecture/README.md).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 logic timing state](./00_logic_timing_state.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
