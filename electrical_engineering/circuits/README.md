# Circuits — Mạch điện

> **Mạch đọc:** Đọc **Circuits — Mạch điện** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Nhánh này xây ngôn ngữ nền của kỹ thuật điện: nút (node / 노드), branch, vòng lặp (loop / 루프), charge, voltage, hiện tại (current / 현재), power, impedance và năng lượng (energy / 에너지). Mạch được học như một mô hình có ranh giới (boundary / 경계), nguồn (source / 소스), tải (load / 로드), trạng thái (state / 상태) và đo lường (measurement / 측정) điểm (point / 지점).

## Cốt lõi (core / 핵심) tuyến (route / 경로)
Phần “Cốt lõi (core / 핵심) tuyến (route / 경로)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
KCL/KVL → Thévenin/Norton → RC/RL/RLC → phasor/impedance → frequency response → measurement
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter
Phần “Cốt lõi (core / 핵심) chapter” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- [Circuit analysis and measurement](00_circuit_analysis_and_measurement.md) — KCL/KVL, loading, transient, AC impedance, ADC divider và đo kiểm.
- [Network theorems and frequency response](01_network_theorems_frequency_response.md) — nodal/mesh, Thevenin/Norton, Bode, sensitivity và tolerance.


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm
Phần “Cần nắm” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- sign convention, tham chiếu (reference / 참조) nút (node / 노드), floating ground và common-mode;
- DC operating điểm (point / 지점), transient phản hồi (response / 응답), thời gian (time / 시간) constant và initial điều kiện (condition / 조건);
- AC steady trạng thái (state / 상태), complex impedance, resonance, power factor và three-phase intuition;
- loading, nguồn (source / 소스) impedance, tolerance, parasitic và lỗi (error / 오류) ngân sách (budget / 예산);
- multimeter, oscilloscope, probe loading, grounding và safe đo lường (measurement / 측정).


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Prerequisite chính là [Physics — mạch DC](../../physics/05_electromagnetism/01_dc_circuits.md) và [mạch AC/RLC](../../physics/05_electromagnetism/02_ac_rlc_circuits.md); chapter này tập trung vào phân tích (analysis / 분석)/thiết kế (design / 설계)/đo lường (measurement / 측정). Đi tiếp sang [analog electronics](../analog_electronics/README.md) hoặc [signals and systems](../signals_and_systems/README.md).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 circuit analysis and measurement](./00_circuit_analysis_and_measurement.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
