# 12 — Cost, performance và capacity

Data platform phải tối ưu total cost of ownership và data-product SLO, không chỉ một query benchmark. Cost đến từ bytes scanned, shuffle, storage, network, file operations, idle capacity, retries, compaction và thời gian kỹ sư.

## 1. Capacity model

Bắt đầu từ volume và concurrency:

```text
daily input × retention × replication
daily compute × peak concurrency × SLA window
shuffle bytes + spill bytes + network egress
```

Peak thường quan trọng hơn average: backfill, month-end close hoặc incident replay có thể cạnh tranh với freshness workload.

## 2. Scan và layout

Partition pruning, column pruning, predicate pushdown, clustering và file size giảm bytes đọc. Nhưng partition quá mịn, compaction quá thường xuyên hoặc sort order đắt có thể chuyển cost sang ingestion/maintenance.

Đo end-to-end: files opened, bytes scanned, CPU decode, network, queue wait, task count và output freshness.

## 3. Shuffle, skew và spill

Shuffle bytes thường là predictor tốt hơn row count. Skew tạo long-tail task; spill tăng disk I/O và merge. Tối ưu có thể là pre-aggregation, salting, broadcast nhỏ, projection sớm hoặc tách heavy hitter—không mặc định là thêm worker.

## 4. Small files và compaction budget

Small-file problem tăng metadata/listing/task overhead. Compaction tạo write amplification và có thể tranh resource với query. Cần budget compaction theo file count, query latency và recovery policy, không chạy cron mù quáng.

## 5. Concurrency và isolation

Một query nhanh khi chạy một mình có thể làm freshness job trễ khi chạy cùng nhiều dashboard. Capacity plan cần workload class, queue, priority, admission control và isolation. SLO nên nêu cả latency và freshness impact.

## 6. Unit economics

Theo dõi cost per TB processed, cost per successful pipeline run, cost per published dataset hoặc cost per active consumer. Unit economics bắt regression sớm hơn tổng invoice, vì tổng invoice có thể tăng đơn giản do volume tăng.

## 7. Experiment loop

1. Chọn workload và correctness baseline.
2. Đo bytes/CPU/network/queue/spill trước thay đổi.
3. Thay một layout/partition/join strategy.
4. Chạy cùng input và code version.
5. So sánh cost, latency, freshness và data reconciliation.

Không chấp nhận performance gain nếu làm mất late event, duplicate, history hoặc audit evidence.

Đọc tiếp: [06 — Distributed processing](../06_distributed_processing/README.md), [09 — Warehouse/lakehouse](../09_warehouse_lake_lakehouse/README.md), [04 — Reliability](../04_reliability_and_production.md).
