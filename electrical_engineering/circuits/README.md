# Circuits — Mạch điện

> **Mạch đọc:** README này là owner của **Circuits — Mạch điện**. Giữ tuyến **KCL/KVL → Thévenin/Norton → RC/RL/RLC → phasor/impedance → frequency response → measurement**, rồi quay lại từng chapter khi cần kiểm tra node, source, load, state và phép đo; tuyến này không thay thế nội dung kỹ thuật của mỗi file.

Nhánh này xây ngôn ngữ nền của kỹ thuật điện: nút (node / 노드), branch, vòng lặp (loop / 루프), charge, voltage, hiện tại (current / 현재), power, impedance và năng lượng (energy / 에너지). Mạch được học như một mô hình có ranh giới (boundary / 경계), nguồn (source / 소스), tải (load / 로드), trạng thái (state / 상태) và đo lường (measurement / 측정) điểm (point / 지점).

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
KCL/KVL → Thévenin/Norton → RC/RL/RLC → phasor/impedance → frequency response → measurement
```

> **Chuyển mạch:** **Cốt lõi route** sắp xếp charge, voltage, current và energy; **Cốt lõi chapter** biến route thành mô hình mạch cụ thể, rồi **Cần nắm** nêu prerequisite phải giữ.

## Cốt lõi (core / 핵심) chapter

- [Circuit analysis and measurement](00_circuit_analysis_and_measurement.md) — KCL/KVL, loading, transient, AC impedance, ADC divider và đo kiểm.
- [Network theorems and frequency response](01_network_theorems_frequency_response.md) — nodal/mesh, Thevenin/Norton, Bode, sensitivity và tolerance.

> **Chuyển mạch:** **Cần nắm** chốt định luật và phép đo tối thiểu; **Cầu nối** dùng chúng để chuyển từ circuit model sang electronics, signals hoặc power owner.

## Cần nắm

- sign convention, tham chiếu (reference / 참조) nút (node / 노드), floating ground và common-mode;
- DC operating điểm (point / 지점), transient phản hồi (response / 응답), thời gian (time / 시간) constant và initial điều kiện (condition / 조건);
- AC steady trạng thái (state / 상태), complex impedance, resonance, power factor và three-phase intuition;
- loading, nguồn (source / 소스) impedance, tolerance, parasitic và lỗi (error / 오류) ngân sách (budget / 예산);
- multimeter, oscilloscope, probe loading, grounding và safe đo lường (measurement / 측정).

> **Chuyển mạch:** **Cầu nối** khép README bằng cách chỉ rõ circuit concept nào được tái sử dụng ở domain kế tiếp và link về canonical owner tương ứng.

## Cầu nối (bridge / 브리지)

Prerequisite chính là [Physics — mạch DC](../../physics/05_electromagnetism/01_dc_circuits.md) và [mạch AC/RLC](../../physics/05_electromagnetism/02_ac_rlc_circuits.md); chapter này tập trung vào phân tích (analysis / 분석)/thiết kế (design / 설계)/đo lường (measurement / 측정). Đi tiếp sang [analog electronics](../analog_electronics/README.md) hoặc [signals and systems](../signals_and_systems/README.md).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
