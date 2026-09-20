# Multi-region replication và geo-distributed trade-offs

Khi replicas nằm ở nhiều regions, speed of light và network geography trở thành part of consistency model. Không có protocol nào làm Seoul–Virginia round trip biến thành local memory access. Architecture phải quyết định operation nào chờ cross-region coordination và operation nào được xử lý local rồi reconcile.

## Latency floor

Cross-region RTT tạo lower bound cho synchronous protocol. Nếu write cần quorum trải nhiều continents, user latency phải trả ít nhất một phần network round trips đó.

Optimization có thể giảm software overhead nhưng không loại physical distance. Vì vậy placement là architecture decision, không chỉ deployment detail.

## Synchronous và asynchronous replication

Synchronous replication giảm RPO vì write chỉ ack sau replicas cần thiết đã durable, nhưng tăng latency và giảm availability khi remote region unreachable.

Asynchronous replication cho local ack nhanh hơn nhưng failover có thể mất recent writes hoặc cần conflict handling.

RPO/RTO phải gắn với replication semantics thực tế, không chỉ SLA marketing.

## Single-leader geo replication

Một global leader đơn giản hóa write order nhưng clients xa leader chịu latency. Read replicas local giảm read latency nhưng có thể stale.

Read-your-writes có thể yêu cầu session stickiness, version token hoặc route read về replica đã catch up.

## Multi-leader

Mỗi region nhận local writes cải thiện availability/latency nhưng concurrent updates tạo conflicts. Unique constraints, counters và inventory trở nên khó vì invariant có thể bị vi phạm trước khi regions trao đổi.

Conflict resolution cần domain semantics, không chỉ “latest timestamp wins”.

## Data sovereignty và placement

Geo architecture còn bị ràng buộc bởi residency/compliance: dữ liệu nào được rời jurisdiction, backup nằm đâu, logs có chứa personal data không. Placement policy vì vậy vừa là performance vừa governance.

## Failover

Failover không chỉ promote replica. DNS/cache TTL, connection pools, stale clients, replication lag và split-brain đều ảnh hưởng. Fencing old primary là bước critical để tránh hai writers cùng authority.

Xem thêm: [Leases, fencing tokens và split-brain](./02_leases_fencing_tokens_and_split_brain_prevention.md).

## Active-active không đồng nghĩa zero downtime

Hai regions active vẫn có shared dependencies, global control plane hoặc replicated data paths. Correlated software bug có thể hạ cả hai. Availability cần failure-domain analysis thay vì đếm regions.

## Geo partitioning

Nếu user/data có locality tự nhiên, partition theo home region có thể giữ phần lớn transactions local và chỉ cross-region cho operations thật sự cần. Đây thường hiệu quả hơn replicate mọi write everywhere.

## Mental Model

> Geo-distributed design là phân bổ coordination theo khoảng cách. Stronger global agreement trả bằng latency/availability; local autonomy trả bằng staleness/conflict. Kiến trúc tốt đặt invariant ở nơi thật sự cần coordination và giữ phần còn lại gần user/data.