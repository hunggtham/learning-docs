# 07 — Streaming systems: event time, watermark, state và replay

Streaming là bài toán duy trì computation trên input chưa bao giờ thực sự “đóng”. Vì vậy trọng tâm là thời gian, state, late event và cách kết quả được sửa khi assumption ban đầu thay đổi.

## 1. Ba loại thời gian

- event time: thời điểm sự kiện xảy ra theo domain;
- ingestion time: lúc platform nhận event;
- processing time: lúc worker xử lý event.

Dashboard vận hành thường cần processing/ingestion time; business window thường cần event time. Trộn chúng làm số liệu lệch mà không nhất thiết tạo lỗi.

## 2. Window và watermark

Window biến stream vô hạn thành nhóm hữu hạn để aggregate. Với event-time window, hệ thống phải chờ event đến muộn. Watermark là một frontier tiến dần, thể hiện mức event-time mà engine tin rằng phần lớn dữ liệu đã đến.

Watermark không phải sự thật tuyệt đối. Nó là policy đánh đổi latency, completeness và state size. Late event sau watermark cần rule rõ: update kết quả, ghi correction, đưa vào quarantine, hay bỏ qua có audit.

## 3. State lifecycle

State có thể là count theo key, session, deduplication set, join buffer hoặc current projection. Mỗi state cần:

```text
key → value/schema → update rule → retention → checkpoint → recovery behavior
```

State vô hạn là memory leak ở cấp data product. TTL phải dựa trên business late-arrival bound và replay requirement, không chỉ default của engine.

## 4. Late data và corrections

Một event đến muộn có thể thay đổi aggregate đã publish. Nếu consumer chỉ đọc append-only output, correction cần một record điều chỉnh hoặc version mới. Nếu consumer đọc snapshot, cần publish atomic snapshot pointer.

Không nên giả vờ stream là immutable khi domain cho phép correction. Hãy mô tả rõ metric là provisional hay final và khi nào finalization xảy ra.

## 5. CDC, ordering và schema evolution

CDC stream thường có transaction/order metadata. Consumer cần biết ordering guarantee là per-key, per-partition hay global; delete có payload hay tombstone; snapshot nối vào log position nào; schema version đi cùng record hay được tra ngoài.

Schema evolution an toàn thường theo trình tự: add optional field → nâng consumer → producer bắt đầu ghi field → deprecate field cũ sau compatibility window. Rename trực tiếp có thể làm reader cũ hiểu sai hoặc tạo drop+add.

## 6. Delivery và sink

At-least-once là lựa chọn phổ biến vì replay an toàn hơn loss, nhưng sink phải idempotent theo `event_id`/version. “Exactly-once” của processor không tự mở rộng qua external API, email, payment hoặc database không tham gia transaction.

Tách pure projection khỏi side effect:

```text
stream → deterministic projection → durable output
                         └──────→ side-effect dispatcher với idempotency key
```

## 7. Replay

Replay cần xác định offset/time range, schema version, code version, state reset strategy và output write mode. Replay vào cùng sink có thể duplicate hoặc ghi đè kết quả mới nếu không có namespace/version.

Một hệ thống trưởng thành có thể chạy replay nhỏ trên sample, đối chiếu aggregate với snapshot/reference và chỉ promote output sau reconciliation.

## 8. Streaming checklist

1. Metric dùng event time hay processing time?
2. Watermark dựa trên bound nào và late event sau đó đi đâu?
3. State key, retention và checkpoint có invariant gì?
4. Duplicate, delete, correction và schema version biểu diễn thế nào?
5. Replay có tái tạo đúng kết quả và không lặp side effect không?

Đọc tiếp: [02 — Pipeline semantics](../02_pipeline_architecture.md), [06 — Distributed processing](../06_distributed_processing/README.md), [08 — Orchestration và backfill](../08_orchestration_and_backfill/README.md).

## 9. Window result là state machine

Một window không chỉ có giá trị số; nó có lifecycle:

```text
open → updating → provisional → finalized → corrected/expired
```

Watermark chuyển window từ open sang provisional/finalized theo policy. Late event sau finalized không được âm thầm mutate kết quả mà không phát version/correction evidence.

## 10. State store và checkpoint

Checkpoint phải bao phủ cả input position và state snapshot. Chỉ lưu offset mà không lưu state tương ứng có thể làm restart tính lại với state cũ hoặc bỏ mất event. State schema evolution cần migration/version, đặc biệt khi operator đổi key hoặc window definition.

Checkpoint interval là trade-off: interval ngắn giảm replay work nhưng tăng I/O; interval dài giảm overhead nhưng recovery lâu hơn. Đo recovery point, checkpoint size, restore time và duplicate/correction behavior.

## 11. CDC snapshot handoff

Snapshot + log CDC cần một cutover point atomic. Nếu snapshot đọc lúc T1 nhưng log bắt đầu từ T2, mutation giữa T1 và T2 bị mất; nếu log bắt đầu trước T1, event có thể bị duplicate và phải dedup theo transaction position.

Consumer nên lưu `snapshot_id`, `log_position`, schema version và source transaction metadata. Đây là evidence để chứng minh không có gap trong handoff.

## 12. Backpressure

Khi sink chậm hơn source, lag tăng. Backpressure có thể làm giảm ingest rate, tăng state/retention pressure hoặc đẩy dữ liệu sang durable buffer. Không nên chỉ tăng consumer count nếu bottleneck là sink partition, network hoặc skew key.

Theo dõi lag theo partition, arrival rate, processing rate, watermark delay, state size và sink latency. Một average lag thấp có thể che một partition bị kẹt.
