# Hardware–Software Interfaces — Giao diện phần cứng–phần mềm

> **Mạch đọc:** README này là owner của **Hardware–Software Interfaces — Giao diện phần cứng–phần mềm**. Route đi từ register/bus contracts → interrupt/DMA/boot → driver lifecycle và protocol semantics → testing/tooling → hardware failures, để phần cứng được đọc như API có timing và failure semantics.

Nhánh này mô tả đặc tả hợp đồng (contract / 계약) nơi register, bus giao dịch (transaction / 트랜잭션), interrupt, DMA, boot và driver biến hành vi phần cứng thành API mà software có thể tin cậy. Đây là điểm nối trực tiếp nhất từ Electrical kỹ thuật (engineering / 엔지니어링) sang Computer kiến trúc (architecture / 아키텍처) và Software.

## Cốt lõi (core / 핵심) tuyến (route / 경로)

```text
register map → bus protocol → driver contract → interrupt/DMA → boot/update → observability/fault recovery
```

> **Chuyển mạch:** **Cốt lõi tuyến** đi từ register, bus và protocol đến driver lifecycle; **Cốt lõi chapter** giải thích hợp đồng, còn **Cần nắm** ghi điều kiện đồng bộ và lỗi.

## Cốt lõi (core / 핵심) chapter

- [Register, bus and driver contracts](00_register_bus_driver_contracts.md) — register ngữ nghĩa (semantics / 의미론), thứ tự (ordering / 순서), DMA quyền sở hữu (ownership / 소유권), errors, boot/cập nhật (update / 업데이트) và tính tương thích (compatibility / 호환성).
- [Protocols and driver lifecycle](01_protocols_driver_lifecycle.md) — bus thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), máy trạng thái (state machine / 상태 머신), tính tương thích (compatibility / 호환성), khôi phục (recovery / 복구) và khả năng quan sát (observability / 관측 가능성).

> **Chuyển mạch:** Sau khi hiểu hợp đồng register/bus và driver, **Cầu nối** đưa chúng vào protocol, timeout, recovery và kiểm thử tích hợp.

## Cần nắm

- memory-mapped I/O, volatile/thứ tự (ordering / 순서), atomicity và side effects;
- SPI/I²C/UART/CAN/USB/Ethernet ở ranh giới (boundary / 경계) giao dịch (transaction / 트랜잭션) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론);
- interrupt acknowledgement, hàng đợi (queue / 큐) quyền sở hữu (ownership / 소유권), DMA buffer thời gian tồn tại (lifetime / 수명) và bộ nhớ đệm (cache / 캐시);
- reset/power sequencing, bootloader, firmware versioning và quay lui (rollback / 롤백);
- hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), idempotency, degraded chế độ (mode / 모드) và diagnostic bằng chứng (evidence / 증거).

> **Chuyển mạch:** **Cầu nối** khép README bằng tiêu chí bàn giao giữa phần cứng và phần mềm: trạng thái, lỗi, thời hạn và owner phải truy được.

## Cầu nối (bridge / 브리지)

Đọc cùng [embedded systems](../embedded_systems/README.md), [digital electronics](../digital_electronics/README.md) và [Computer Science](../../computer_science/README.md). giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론) không thay thế electrical timing, và driver API không được che giấu safety-critical thất bại (failure / 실패).

> **Bàn giao:** Sau **Cầu nối (bridge / 브리지)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
