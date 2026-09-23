# 10 — Serving layer và semantic layer

Serving biến modeled data thành interface mà người khác dùng: dashboard, metric API, feature pipeline, reverse ETL hoặc operational read model. Semantic layer bảo đảm hai consumer không tự định nghĩa “revenue”, “active user” và “order” theo ba cách khác nhau.

## 1. Các serving shape

- analytical table: scan và aggregate lớn;
- dimensional model: join theo dimension/fact với grain rõ;
- materialized aggregate: latency thấp cho metric ổn định;
- semantic metric: định nghĩa measure, dimension, filter và time grain;
- API/read model: shape theo access pattern của ứng dụng;
- feature view: point-in-time correct cho machine learning.

Không có serving shape tốt cho mọi consumer. Dùng cùng một bảng cho BI ad-hoc và online API thường tạo conflict về latency, update và schema.

## 2. Metric contract

Một metric cần nêu:

```text
name + grain + numerator/denominator + time semantics
→ filters + null policy + late-data policy
→ owner + freshness SLO + version/deprecation
```

“Revenue” có tính refund không? Dùng event time hay paid_at? Currency conversion ở đâu? Câu hỏi này là contract, không phải chi tiết dashboard.

## 3. Point-in-time correctness

Feature hoặc report lịch sử không được dùng dimension của tương lai. Khi join fact event với customer state, phải chọn version có `effective_time <= event_time` và xử lý tie-breaker. Join theo trạng thái hiện tại có thể tạo data leakage trong ML và lịch sử sai trong analytics.

## 4. Materialization và freshness

Materialized result giảm latency nhưng cần refresh policy, invalidation, backfill và dependency graph. Freshness timestamp chỉ cho biết lúc job chạy; cần thêm completeness và source watermark để biết data có đủ hay chưa.

Serving nên public một version/snapshot atomically. Consumer không nên thấy nửa output cũ/nửa output mới.

## 5. Semantic consistency

Metric logic nên được định nghĩa một lần và reuse, nhưng semantic layer không nên che giấu grain hoặc query cost. Nếu metric join nhiều fact khác grain, contract phải nêu pre-aggregation hoặc allowed dimensions.

Versioning metric là cần thiết khi business meaning thay đổi. Đổi logic âm thầm làm time series discontinuity mà không có schema error.

## 6. Failure modes

- dashboard fresh nhưng thiếu partition;
- API trả số liệu stale vì cache không invalidate;
- aggregate double-count do fan-out;
- ML feature dùng future state;
- metric đổi filter nhưng giữ cùng tên;
- consumer đọc output khi materialization chưa atomic.

## 7. Serving review

1. Consumer cần latency, freshness và consistency nào?
2. Grain và point-in-time rule có explicit không?
3. Metric version, owner và deprecation có tồn tại không?
4. Output publish, cache invalidation và rollback ra sao?
5. Có reconcile serving result với modeled/source layer không?

Đọc tiếp: [05 — Modeling](../05_data_modeling_and_transformation/README.md), [04 — Reliability](../04_reliability_and_production.md), [11 — Governance](../11_governance_lineage_security/README.md).
