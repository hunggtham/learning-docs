# 14 — Multi-region, replication và data residency

Multi-region không chỉ là copy table sang hai nơi. Nó là bài toán về latency, authority, replication lag, conflict, failover, recovery point và nơi dữ liệu được phép tồn tại.

## 1. Topology và authority

Chọn primary/replica, active-passive hay multi-writer phải bắt đầu từ write authority. Nếu hai region cùng sửa một customer, cần conflict rule; eventual convergence không tự bảo toàn business invariant.

```text
single writer → replicate → read-local
multi writer  → conflict resolution → converge/compensate
```

Conflict resolution có thể là last-write-wins, version vector, field-level merge hoặc domain command. Clock wall-time không đủ đáng tin nếu clock skew có thể đảo thứ tự event.

## 2. Replication lag

Lag có thể đo theo source position, event time hoặc commit timestamp. Read-after-write guarantee cần biết request đọc ở region nào và replica đã bắt kịp position nào. Dashboard đọc local replica có thể stale dù replication job không báo lỗi.

SLO nên tách p50/p99 lag, maximum staleness và recovery catch-up time. Average lag che giấu một partition/tenant bị kẹt.

## 3. RPO/RTO và failover

RPO trả lời mất tối đa bao nhiêu dữ liệu; RTO trả lời phục hồi trong bao lâu. Failover chỉ đúng nếu target region có schema, secrets, catalog, checkpoints, routing và access policy tương ứng—không chỉ có data files.

Runbook cần fencing primary cũ để tránh split-brain. Sau failover, ghi tiếp vào đâu, replay khoảng nào, và merge/correction output thế nào phải được định nghĩa trước.

## 4. Residency và purpose limitation

Data residency có thể yêu cầu raw PII ở một quốc gia nhưng aggregate đã anonymize được phục vụ toàn cầu. Replication policy phải gắn với field classification và purpose, không chỉ database name.

Metadata, logs, backups, caches và support exports cũng có thể chứa dữ liệu nhạy cảm. “Không replicate table” chưa đủ nếu CDC log hoặc observability payload vẫn vượt region boundary.

## 5. Evidence và test

Evidence gồm replication position, lag histogram, failover timestamp, fenced writer, output reconciliation và residency audit. Test định kỳ phải mô phỏng region mất mạng, stale replica, duplicate replay và clock skew.

## 6. Trade-off

Strong consistency across regions tăng latency và coordination cost; eventual consistency giảm latency nhưng cần correction/read-your-writes strategy. Chọn guarantee theo domain, không theo default của database hoặc cloud service.

Đọc tiếp: [07 — Streaming](../07_streaming_systems/README.md), [09 — Lakehouse](../09_warehouse_lake_lakehouse/README.md), [11 — Governance](../11_governance_lineage_security/README.md).
