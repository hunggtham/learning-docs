# Embedded các hệ thống (systems / 시스템들) — Hệ thống nhúng

> **Mạch đọc:** Đọc **Embedded các hệ thống (systems / 시스템들) — Hệ thống nhúng** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Embedded các hệ thống (systems / 시스템들) là nơi điện tử, timing, firmware và vật lý (physical / 물리적) môi trường (environment / 환경) gặp nhau. Một hệ thống (system / 시스템) đúng không chỉ trả về giá trị đúng; nó phải đúng thời hạn, trong power/thermal/bộ nhớ (memory / 메모리) ngân sách (budget / 예산) và có hành vi an toàn khi peripheral hoặc sensor hỏng.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
MCU/SoC → clock/reset/power → GPIO/timer/ADC → interrupt/DMA → RTOS/real-time → bring-up → verification
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter

- [MCU runtime and real-time reasoning](00_mcu_runtime_real_time.md) — boot quyền sở hữu (ownership / 소유권), ISR/DMA, WCET, timer wrap, watchdog và bring-up bằng chứng (evidence / 증거).
- [RTOS scheduling and verification](01_rtos_scheduling_verification.md) — priority inversion, WCET, isolation, HIL và fault injection.


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm

- boot chuỗi (chain / 사슬), bộ nhớ (memory / 메모리) map, register truy cập (access / 접근) và peripheral máy trạng thái (state machine / 상태 머신);
- interrupt độ trễ (latency / 지연 시간), priority inversion, DMA quyền sở hữu (ownership / 소유권) và bộ nhớ đệm (cache / 캐시) coherency;
- deterministic scheduling, deadline, jitter, watchdog và brownout;
- board bring-up, tín hiệu (signal / 신호) integrity, logging/dấu vết (trace / 추적) và hardware-in-the-loop kiểm thử (test / 테스트);
- cập nhật (update / 업데이트)/quay lui (rollback / 롤백), secure boot và trường dữ liệu (field / 필드) thất bại (failure / 실패) khôi phục (recovery / 복구).


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Digital lô-gic (logic / 논리) là prerequisite; [hardware–software interfaces](../hardware_software_interfaces/README.md) giữ đặc tả hợp đồng (contract / 계약) chi tiết. OS, tính đồng thời (concurrency / 동시성) và kiến trúc (architecture / 아키텍처) ngữ nghĩa (semantics / 의미론) sâu hơn thuộc [Computer Science](../../computer_science/README.md).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mcu runtime real time](./00_mcu_runtime_real_time.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
