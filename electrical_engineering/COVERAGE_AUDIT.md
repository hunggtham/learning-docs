# Coverage Audit — Electrical Engineering Knowledge Library

## Phạm vi P3

Electrical Engineering được thêm như một domain bridge giữa Physics và Computing. Mục tiêu của P3 không phải biến repository thành handbook cho mọi specialization, mà xây một core đủ để suy luận từ:

```text
định luật vật lý → topology → signal/power/control → device → firmware/software contract
```

## Trạng thái hiện tại

| Nhánh | Trạng thái | Mục tiêu tiếp theo |
|---|---|---|
| Circuits | Core + depth 1 | KCL/KVL, loading, transients, network theorems, Bode, tolerance |
| Analog electronics | Core + depth 1 | biasing, feedback, noise, ADC/DAC, ENOB, error budget |
| Digital electronics | Core + depth 1 | timing, metastability, memory, buses, FIFO, HDL verification |
| Signals and systems | Core + depth 1 | LTI, sampling, filters, Laplace/Z, matched filter, estimation |
| Communication systems | Core + depth 1 | modulation, link budget, capacity, EVM, synchronization, goodput |
| Control systems | Core + depth 1 | stability, PID, state-space, discretization, deadlines, HIL |
| Embedded systems | Core + depth 1 | boot, ISR/DMA, WCET, RTOS, isolation, fault injection |
| Power electronics | Core + depth 1 | converters, inverter, battery, thermal, protection, EMI |
| Hardware–software interfaces | Core + depth 1 | registers, protocols, lifecycle, recovery, compatibility |

“Core + depth 1” nghĩa là mỗi nhánh đã có một chapter nền tảng và một chapter design/verification mở rộng; các bài lab, case study và specialization vẫn còn mở rộng.

## Đánh giá vòng này

### Điểm đã đạt

- Dependency graph đã nối được từ Physics tới hardware/software boundary.
- Mỗi nhánh có ít nhất một worked reasoning hoặc design budget.
- Non-idealities không còn bị giới hạn ở component physics: đã thêm timing, tolerance, latency, ownership, thermal và recovery.
- Verification được đưa vào digital, control, embedded, power và driver lifecycle thay vì để ở phần cuối.

### Điểm chưa đạt

- Chưa có schematic/waveform thực thi hoặc lab reproducibility; các worked reasoning hiện vẫn là paper design.
- RF/microwave, FPGA implementation, EMC compliance, battery management chi tiết và functional safety vẫn ở mức boundary.
- Glossary Việt–Anh–Hàn mới ở mức initial và chưa bao phủ mọi specialization.

Các khoảng trống còn lại được phân biệt rõ trong [case study end-to-end](90_connections/00_end_to_end_temperature_control_case.md), [glossary](90_connections/01_glossary_vi_en_ko.md) và [lab checklist](90_connections/02_lab_and_measurement_checklist.md). Chúng vẫn chưa thay thế lab thực thi hoặc chứng nhận an toàn.

### Ưu tiên update tiếp theo

1. Bổ sung test artifacts hoặc waveform reproducibility cho case study.
2. Mở rộng glossary và cross-domain navigation tự động.
3. Thêm RF, FPGA hoặc safety certification chỉ khi có nguồn và use case đủ rõ.
4. Giữ depth/verification ưu tiên trước breadth để tránh shallow coverage.

## Chuẩn hoàn thiện

Một nhánh chỉ được đánh dấu strong khi có:

- dependency và prerequisite rõ;
- model lý tưởng cùng các non-idealities quan trọng;
- equations với đơn vị, limiting cases và điều kiện áp dụng;
- schematic/waveform hoặc worked reasoning có thể kiểm tra;
- measurement, calibration, tolerance và test strategy;
- failure modes, protection và safety boundary;
- bridge tới Physics, Computer Architecture, Embedded hoặc Software;
- glossary và links không trỏ tới file tạm.

## Khoảng trống có chủ đích

- Không duplicate Maxwell, semiconductor physics, transmission line hoặc MOSFET derivation đã có trong `physics/`.
- Không duplicate CPU/ISA/OS theory đã có trong `computer_science/`.
- RF/microwave, ASIC physical design, semiconductor fabrication, power grid và safety certification chỉ mở rộng khi có nhu cầu và nguồn học đủ sâu.

## Audit checklist trước khi mở rộng

```text
[ ] chapter giải thích design problem, không chỉ liệt kê component
[ ] mô hình lý tưởng được nối với parasitic/tolerance/temperature
[ ] signal, power, timing và control loop được xem như các budget riêng
[ ] mọi boundary hardware/software có ownership và failure semantics
[ ] link Physics/CS dùng đúng canonical path
[ ] README, CATALOG và library config đồng bộ
```
