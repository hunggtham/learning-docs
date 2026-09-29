# Hardware–Software Interfaces — Giao diện phần cứng–phần mềm

> **Mạch đọc:** Đọc **Hardware–Software Interfaces — Giao diện phần cứng–phần mềm** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **cốt lõi (core / 핵심) tuyến (route / 경로)** sang **cốt lõi (core / 핵심) chapter**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

Nhánh này mô tả đặc tả hợp đồng (contract / 계약) nơi register, bus giao dịch (transaction / 트랜잭션), interrupt, DMA, boot và driver biến hành vi phần cứng thành API mà software có thể tin cậy. Đây là điểm nối trực tiếp nhất từ Electrical kỹ thuật (engineering / 엔지니어링) sang Computer kiến trúc (architecture / 아키텍처) và Software.

## Cốt lõi (core / 핵심) tuyến (route / 경로)
Phần “Cốt lõi (core / 핵심) tuyến (route / 경로)” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


```text
register map → bus protocol → driver contract → interrupt/DMA → boot/update → observability/fault recovery
```


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) tuyến (route / 경로)**, ta sang **cốt lõi (core / 핵심) chapter** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cốt lõi (core / 핵심) chapter
Phần “Cốt lõi (core / 핵심) chapter” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- [Register, bus and driver contracts](00_register_bus_driver_contracts.md) — register ngữ nghĩa (semantics / 의미론), thứ tự (ordering / 순서), DMA quyền sở hữu (ownership / 소유권), errors, boot/cập nhật (update / 업데이트) và tính tương thích (compatibility / 호환성).
- [Protocols and driver lifecycle](01_protocols_driver_lifecycle.md) — bus thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론), máy trạng thái (state machine / 상태 머신), tính tương thích (compatibility / 호환성), khôi phục (recovery / 복구) và khả năng quan sát (observability / 관측 가능성).


> **Chuyển mạch:** Từ **cốt lõi (core / 핵심) chapter**, ta sang **Cần nắm** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cần nắm
Phần “Cần nắm” nối kiến thức trước với nội dung sắp đọc, giúp người mới hiểu mục đích, tiêu chí theo dõi và kết luận cần rút ra trước khi xem danh sách, bảng hoặc ví dụ.


- memory-mapped I/O, volatile/thứ tự (ordering / 순서), atomicity và side effects;
- SPI/I²C/UART/CAN/USB/Ethernet ở ranh giới (boundary / 경계) giao dịch (transaction / 트랜잭션) và thất bại (failure / 실패) ngữ nghĩa (semantics / 의미론);
- interrupt acknowledgement, hàng đợi (queue / 큐) quyền sở hữu (ownership / 소유권), DMA buffer thời gian tồn tại (lifetime / 수명) và bộ nhớ đệm (cache / 캐시);
- reset/power sequencing, bootloader, firmware versioning và quay lui (rollback / 롤백);
- hết thời gian chờ (timeout / 타임아웃), thử lại (retry / 재시도), idempotency, degraded chế độ (mode / 모드) và diagnostic bằng chứng (evidence / 증거).


> **Chuyển mạch:** Từ **Cần nắm**, ta sang **cầu nối (bridge / 브리지)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cầu nối (bridge / 브리지)

Đọc cùng [embedded systems](../embedded_systems/README.md), [digital electronics](../digital_electronics/README.md) và [Computer Science](../../computer_science/README.md). giao thức (protocol / 프로토콜) ngữ nghĩa (semantics / 의미론) không thay thế electrical timing, và driver API không được che giấu safety-critical thất bại (failure / 실패).

> **Bàn giao:** Sau **cầu nối (bridge / 브리지)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 register bus driver contracts](./00_register_bus_driver_contracts.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
