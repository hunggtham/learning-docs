# Coverage kiểm tra (audit / 감사) — Electrical kỹ thuật (engineering / 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)

> **Mạch đọc:** [README](./README.md) là owner của **Coverage kiểm tra (audit / 감사) — Electrical kỹ thuật (engineering / 엔지니어링) thư viện kiến thức (knowledge library / 지식 라이브러리)**; dùng audit này để kiểm tra coverage chứ không thay thế các chapter kỹ thuật. Từ **Phạm vi P3** nối qua trạng thái hiện tại, đánh giá vòng này và các domain circuits/digital/power, rồi quay lại README để xác định owner và khoảng trống cần bổ sung.

## Phạm vi P3

Electrical kỹ thuật (engineering / 엔지니어링) được thêm như một lĩnh vực (domain / 도메인) cầu nối (bridge / 브리지) giữa Physics và Computing. Mục tiêu của P3 không phải biến repository thành handbook cho mọi specialization, mà xây một cốt lõi (core / 핵심) đủ để suy luận từ:

```text
định luật vật lý → topology → signal/power/control → device → firmware/software contract
```

> **Chuyển mạch:** **Phạm vi P3** xác định phần cần bao phủ; **Trạng thái hiện tại** ghi bằng chứng đang có, rồi **Đánh giá vòng này** chọn issue có tác động lớn nhất.

## Trạng thái hiện tại

| Nhánh | Trạng thái | Mục tiêu tiếp theo |
|---|---|---|
| Circuits | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | KCL/KVL, loading, transients, mạng (network / 네트워크) theorems, Bode, tolerance |
| Analog electronics | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | biasing, phản hồi (feedback / 피드백), noise, ADC/DAC, ENOB, lỗi (error / 오류) ngân sách (budget / 예산) |
| Digital electronics | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | timing, metastability, bộ nhớ (memory / 메모리), buses, FIFO, HDL xác minh (verification / 확인) |
| Signals and các hệ thống (systems / 시스템들) | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | LTI, sampling, filters, Laplace/Z, matched filter, estimation |
| Communication các hệ thống (systems / 시스템들) | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | modulation, link ngân sách (budget / 예산), sức chứa (capacity / 용량), EVM, synchronization, goodput |
| điều khiển (control / 제어) các hệ thống (systems / 시스템들) | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | stability, PID, state-space, discretization, deadlines, HIL |
| Embedded các hệ thống (systems / 시스템들) | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | boot, ISR/DMA, WCET, RTOS, isolation, fault injection |
| Power electronics | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | converters, inverter, battery, thermal, protection, EMI |
| Hardware–software interfaces | cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1 | registers, protocols, vòng đời (lifecycle / 생명주기), khôi phục (recovery / 복구), tính tương thích (compatibility / 호환성) |

“cốt lõi (core / 핵심) + độ sâu (depth / 깊이) 1” nghĩa là mỗi nhánh đã có một chapter nền tảng và một chapter thiết kế (design / 설계)/xác minh (verification / 확인) mở rộng; các bài lab, trường hợp (case / 사례) study và specialization vẫn còn mở rộng.

> **Chuyển mạch:** **Đánh giá vòng này** biến trạng thái thành hành động; **Chuẩn hoàn thiện** nêu claim, link, ví dụ và test cần có để đóng issue.

## Đánh giá vòng này

### Điểm đã đạt

- phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) đã nối được từ Physics tới hardware/software ranh giới (boundary / 경계).
- Mỗi nhánh có ít nhất một worked lập luận (reasoning / 추론) hoặc thiết kế (design / 설계) ngân sách (budget / 예산).
- Non-idealities không còn bị giới hạn ở thành phần (component / 컴포넌트) physics: đã thêm timing, tolerance, độ trễ (latency / 지연 시간), quyền sở hữu (ownership / 소유권), thermal và khôi phục (recovery / 복구).
- xác minh (verification / 확인) được đưa vào digital, điều khiển (control / 제어), embedded, power và driver vòng đời (lifecycle / 생명주기) thay vì để ở phần cuối.

### Điểm chưa đạt

- Chưa có schematic/waveform thực thi hoặc lab reproducibility; các worked lập luận (reasoning / 추론) hiện vẫn là paper thiết kế (design / 설계).
- RF/microwave, FPGA hiện thực (implementation / 구현), EMC compliance, battery management chi tiết và functional an toàn (safety / 안전) vẫn ở mức ranh giới (boundary / 경계).
- Glossary Việt–Anh–Hàn mới ở mức initial và chưa bao phủ mọi specialization.

Các khoảng trống còn lại được phân biệt rõ trong [case study end-to-end](90_connections/00_end_to_end_temperature_control_case.md), [glossary](90_connections/01_glossary_vi_en_ko.md) và [lab checklist](90_connections/02_lab_and_measurement_checklist.md). Chúng vẫn chưa thay thế lab thực thi hoặc chứng nhận an toàn.

### Ưu tiên cập nhật (update / 업데이트) tiếp theo

1. Bổ sung kiểm thử (test / 테스트) artifacts hoặc waveform reproducibility cho trường hợp (case / 사례) study.
2. Mở rộng glossary và cross-domain điều hướng (navigation / 내비게이션) tự động.
3. Thêm RF, FPGA hoặc an toàn (safety / 안전) certification chỉ khi có nguồn và use trường hợp (case / 사례) đủ rõ.
4. Giữ độ sâu (depth / 깊이)/xác minh (verification / 확인) ưu tiên trước breadth để tránh shallow coverage.

> **Chuyển mạch:** Khi chuẩn hoàn thiện rõ, **Khoảng trống có chủ đích** phân biệt thiếu thật với phần được giữ ngoài phạm vi để không ép mọi topic vào một checklist.

## Chuẩn hoàn thiện

Một nhánh chỉ được đánh dấu strong khi có:

- phụ thuộc (dependency / 의존성) và prerequisite rõ;
- mô hình (model / 모델) lý tưởng cùng các non-idealities quan trọng;
- equations với đơn vị, limiting cases và điều kiện áp dụng;
- schematic/waveform hoặc worked lập luận (reasoning / 추론) có thể kiểm tra;
- đo lường (measurement / 측정), calibration, tolerance và kiểm thử (test / 테스트) chiến lược (strategy / 전략);
- thất bại (failure / 실패) modes, protection và an toàn (safety / 안전) ranh giới (boundary / 경계);
- cầu nối (bridge / 브리지) tới Physics, Computer kiến trúc (architecture / 아키텍처), Embedded hoặc Software;
- glossary và links không trỏ tới tệp (file / 파일) tạm.

> **Chuyển mạch:** **Khoảng trống có chủ đích** ghi rõ lý do và owner; **audit checklist trước khi mở rộng** xác nhận gap không phải link hỏng hay claim thiếu nguồn.

## Khoảng trống có chủ đích

- Không duplicate Maxwell, semiconductor physics, transmission line hoặc MOSFET derivation đã có trong `physics/`.
- Không duplicate CPU/ISA/OS lý thuyết (theory / 이론) đã có trong `computer_science/`.
- RF/microwave, ASIC vật lý (physical / 물리적) thiết kế (design / 설계), semiconductor fabrication, power grid và an toàn (safety / 안전) certification chỉ mở rộng khi có nhu cầu và nguồn học đủ sâu.

> **Chuyển mạch:** Checklist cuối khép vòng coverage bằng việc kiểm tra owner, link, claim, ví dụ và boundary trước khi mở thêm chapter.

## Kiểm tra (audit / 감사) checklist trước khi mở rộng

```text
[ ] chapter giải thích design problem, không chỉ liệt kê component
[ ] mô hình lý tưởng được nối với parasitic/tolerance/temperature
[ ] signal, power, timing và control loop được xem như các budget riêng
[ ] mọi boundary hardware/software có ownership và failure semantics
[ ] link Physics/CS dùng đúng canonical path
[ ] README, CATALOG và library config đồng bộ
```

> **Bàn giao:** Sau **Kiểm tra (audit / 감사) checklist trước khi mở rộng**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
