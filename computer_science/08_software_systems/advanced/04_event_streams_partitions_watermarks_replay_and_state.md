# Event streams: partitions, watermarks, replay và stateful processing

Event stream không chỉ là queue dài. Nó là ordered history được chia partition, có retention và có thể replay. Điều này cho phép nhiều consumers xây state riêng từ cùng event log, nhưng cũng đưa ordering, time và recovery thành vấn đề kiến trúc.

## Partition là đơn vị ordering

Broker thường chỉ đảm bảo total order trong một partition, không phải toàn topic. Partition key quyết định events nào phải cùng order.

Nếu mọi event dùng cùng key để có global order, throughput bị giới hạn bởi một partition. Nếu partition quá rộng, business operation cần order có thể bị tách.

## Consumer group

Trong consumer group, partitions được phân cho consumers để parallel processing. Số consumers vượt số partitions không tăng parallelism hữu ích cho group đó.

Rebalance khi consumer join/leave có thể tạm dừng work hoặc chuyển ownership state, nên frequent churn ảnh hưởng latency.

## Offset

Offset là vị trí trong log, không phải business transaction ID. Commit offset trước side effect có thể mất processing khi crash; commit sau side effect có thể duplicate side effect.

Vì vậy at-least-once processing thường kết hợp idempotency/deduplication.

## Event time và processing time

Event có thể xảy ra lúc 10:00 nhưng tới processor lúc 10:05 vì mobile offline/network delay. **Event time** phản ánh thời điểm business event; **processing time** phản ánh lúc system xử lý.

Window analytics cần chọn semantics đúng, nếu không late events làm số liệu sai.

## Watermark

Watermark là estimate rằng phần lớn events trước một event-time threshold đã tới. Nó cho phép engine đóng window mà không chờ vô hạn.

Watermark luôn là trade-off completeness và latency. Chờ lâu bắt được late data nhưng output trễ; đóng sớm cần correction/retraction khi event muộn tới.

## Stateful processing

Join streams, aggregate window và detect patterns cần state. State phải checkpoint cùng progress/offset để recovery không tạo mismatch.

Exactly-once trong stream processor thường là coordination giữa state snapshot và source/sink positions, không phải magical network guarantee.

## Replay

Retention cho phép consumer mới hoặc bug-fixed job replay history. Nhưng replay có thể gọi lại external side effects nếu architecture không phân biệt rebuilding state với live action.

Event sourcing đặc biệt cần versioning: code mới phải hiểu old event schemas hoặc có migration/upcasting strategy.

## Hot partition

Key distribution skew làm một partition overload dù cluster tổng thể còn capacity. Celebrity user, tenant lớn hoặc timestamp-based key có thể tạo hotspot.

Partition design vì vậy là data-model decision, không chỉ broker config.

## Mental Model

> Stream là history được partition. Partition xác định ordering và parallelism; offset xác định progress; watermark quản lý uncertainty về time; checkpoint gắn state với progress. Replay mạnh vì history còn đó, nhưng side effects phải được thiết kế để chịu replay.