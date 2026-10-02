# Event-driven các hệ thống (systems / 시스템들) và stream processing

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Event-driven systems và stream processing**. Route đi từ event/command/message → queue/log → delivery semantics → ordering/time windows → backpressure/dead-letter → event sourcing, để processing guarantee gắn với replay và failure.

Yêu cầu (request / 요청)/phản hồi (response / 응답) phù hợp khi caller cần kết quả ngay. Nhưng nhiều workflows cần decouple producers và consumers, xử lý dữ liệu liên tục, fan-out hoặc chịu spikes. Event-driven kiến trúc (architecture / 아키텍처) dùng events/messages làm ranh giới (boundary / 경계), nhưng đổi call-stack trực tiếp lấy delivery/thứ tự (order / 순서)/trạng thái (state / 상태) độ phức tạp (complexity / 복잡도).

## Sự kiện (event / 이벤트), command và message

Message là envelope vận chuyển (transport / 전송). Command thường biểu đạt yêu cầu “hãy làm X” với intended handler. sự kiện (event / 이벤트) biểu đạt “X đã xảy ra” và có thể có nhiều subscribers.

Terminology không tuyệt đối giữa frameworks, nhưng distinction intent vs fact hữu ích cho coupling.

> **Chuyển mạch:** Trong **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Hàng đợi (queue / 큐) và log** tiếp nhận điểm tựa từ **Sự kiện (event / 이벤트), command và message** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **At-most-once, at-least-once, effectively-once** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hàng đợi (queue / 큐) và log

Traditional công việc (work / 작업) hàng đợi (queue / 큐) phân phối messages để worker xử lý, thường mỗi message bởi một bên tiêu thụ (consumer / 소비자) trong group.

Append-only phân tán (distributed / 분산) log như Kafka giữ ordered records theo partition và consumers nhánh học (track / 트랙) offsets. Multiple bên tiêu thụ (consumer / 소비자) groups có thể replay cùng lịch sử (history / 이력) độc lập.

Hàng đợi (queue / 큐) nhấn mạnh công việc (work / 작업) phân phối (distribution / 분포); log nhấn mạnh durable ordered lịch sử (history / 이력)/replay.

> **Chuyển mạch:** Ở chặng này của **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **At-most-once, at-least-once, effectively-once** tiếp nhận điểm tựa từ **Hàng đợi (queue / 큐) và log** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thứ tự (ordering / 순서) chỉ có phạm vi (scope / 범위)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## At-most-once, at-least-once, effectively-once

At-most-once có thể mất message nhưng không redeliver. At-least-once thử lại (retry / 재시도) nên có duplicates. Exactly-once end-to-end rất khó vì broker acknowledgment và bên ngoài (external / 외부) side tác động (effect / 효과) không atomic mặc định.

Thực tế thường dùng idempotent consumers, deduplication keys hoặc transactional tích hợp (integration / 통합) để đạt effectively-once nghiệp vụ (business / 비즈니스) kết quả (outcome / 결과).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Thứ tự (ordering / 순서) chỉ có phạm vi (scope / 범위)** tiếp nhận điểm tựa từ **At-most-once, at-least-once, effectively-once** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thứ tự (ordering / 순서) chỉ có phạm vi (scope / 범위)

Toàn cục (global / 전역) total thứ tự (ordering / 순서) đắt và hiếm cần. các hệ thống (systems / 시스템들) thường guarantee thứ tự (order / 순서) per partition/key.

Nếu account updates phải ordered, partition theo account ID giúp cùng account vào một ordered stream, trong khi accounts khác xử lý parallel.

Thứ tự (ordering / 순서) yêu cầu (requirement / 요구사항) vì vậy ảnh hưởng partitioning và thông lượng (throughput / 처리량).

> **Chuyển mạch:** Trong **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Thứ tự (ordering / 순서) chỉ có phạm vi (scope / 범위)** xác định đầu vào; **Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)

Processing thời gian (time / 시간) là lúc hệ thống (system / 시스템) xử lý bản ghi (record / 레코드). sự kiện (event / 이벤트) thời gian (time / 시간) là lúc sự kiện (event / 이벤트) thực sự xảy ra theo nguồn (source / 소스) timestamp.

Late/out-of-order events làm cửa sổ (window / 윈도우) aggregation khó. Watermark là estimate rằng hệ thống (system / 시스템) đã thấy phần lớn events trước một event-time frontier.

Streaming tính đúng đắn (correctness / 정확성) phải nói rõ lateness chính sách (policy / 정책), cửa sổ (window / 윈도우) kiểu (type / 타입) và cập nhật (update / 업데이트)/retraction ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Ở chặng này của **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Sự kiện (event / 이벤트) thời gian (time / 시간) và processing thời gian (time / 시간)** xác định đầu vào; **Backpressure** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Dead-letter hàng đợi (queue / 큐)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backpressure

Producer nhanh hơn bên tiêu thụ (consumer / 소비자) vô hạn thời gian thì hàng đợi (queue / 큐) grow vô hạn. Backpressure cần giới hạn/buffering/tỷ lệ (rate / 비율) điều khiển (control / 제어) hoặc drop/degrade chính sách (policy / 정책).

Hàng đợi (queue / 큐) chỉ hấp thụ burst tạm thời; nó không tạo processing sức chứa (capacity / 용량).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Dead-letter hàng đợi (queue / 큐)** tiếp nhận điểm tựa từ **Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sự kiện (event / 이벤트) sourcing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dead-letter hàng đợi (queue / 큐)

Messages thử lại (retry / 재시도) mãi do malformed dữ liệu (data / 데이터) có thể khối (block / 블록) thông lượng (throughput / 처리량) hoặc waste resources. DLQ tách poison messages để investigate.

Nhưng DLQ không nên là nơi dữ liệu (data / 데이터) biến mất vô thời hạn; cần quyền sở hữu (ownership / 소유권), alerting và replay tiến trình (process / 프로세스).

> **Chuyển mạch:** Trong **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Sự kiện (event / 이벤트) sourcing** tiếp nhận điểm tựa từ **Dead-letter hàng đợi (queue / 큐)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sự kiện (event / 이벤트) sourcing

Sự kiện (event / 이벤트) sourcing lưu trạng thái (state / 상태) changes như chuỗi (sequence / 시퀀스) events và derive trạng thái hiện tại (current state / 현재 상태) bằng replay/projection. Nó tạo kiểm tra (audit / 감사)/lịch sử (history / 이력) mạnh nhưng lược đồ (schema / 스키마) evolution, sự kiện (event / 이벤트) immutability và replay chi phí (cost / 비용) phức tạp.

Không phải mọi event-driven hệ thống (system / 시스템) đều event-sourced.

> **Chuyển mạch:** Ở chặng này của **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Sự kiện (event / 이벤트) sourcing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“Message broker làm hệ thống (system / 시스템) reliable tự động.”** độ tin cậy (reliability / 신뢰성) phụ thuộc producer ack, retention, bên tiêu thụ (consumer / 소비자) idempotency, thử lại (retry / 재시도) và downstream side effects.

**“Exactly-once là checkbox của broker.”** End-to-end tác động (effect / 효과) vượt broker ranh giới (boundary / 경계) cần additional giao thức (protocol / 프로토콜)/trạng thái (state / 상태).

**“hàng đợi (queue / 큐) giải overload.”** Nó trì hoãn overload; sustained arrival tỷ lệ (rate / 비율) > dịch vụ (service / 서비스) tỷ lệ (rate / 비율) vẫn không ổn định.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Event-driven thiết kế (design / 설계) biến temporal coupling thành trạng thái (state / 상태) in queues/logs. Đổi lại bạn phải tường minh (explicit / 명시적) delivery, thứ tự (ordering / 순서), replay, idempotency và backpressure.

> **Chuyển mạch:** Trong **Event-driven các hệ thống (systems / 시스템들) và stream processing**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc [queues/backpressure](./03_state_queues_backpressure_and_boundaries.md), [time/idempotency](./04_time_serialization_and_idempotency.md), [distributed failure](../06_networks_distributed_systems/04_distributed_systems_time_failure_and_consistency.md) và [reliability](../07_security_reliability/05_fault_tolerance_observability_and_reliability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
