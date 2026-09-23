# 15 — ML feature platform và point-in-time correctness

Feature platform nối Data Engineering với training và serving. Rủi ro lớn nhất không phải feature thiếu đẹp, mà là **training/serving skew** và data leakage do dùng thông tin của tương lai.

## 1. Feature time semantics

Mỗi feature cần event time, availability time và entity key. Training row tại prediction time T chỉ được dùng feature có `available_at <= T`, không chỉ `event_time <= T`.

```text
entity + prediction_time
→ latest feature version available before T
```

Dùng current dimension cho historical training có thể đưa outcome tương lai vào input mà không tạo exception.

## 2. Offline/online parity

Offline store tối ưu scan lịch sử; online store tối ưu point lookup latency. Cùng feature definition phải tạo giá trị tương đương, timezone/encoding/null policy giống nhau và version được trace.

Dual-write có thể lệch khi một sink thành công còn sink kia fail. Event log + deterministic projection thường dễ replay hơn hai writer độc lập.

## 3. Freshness và missing feature

Feature SLO cần freshness, completeness, availability và acceptable staleness. Missing value phải phân biệt “chưa đến”, “không áp dụng”, “bị xóa” và “pipeline lỗi”. Default value có thể che incident và làm model drift.

## 4. Backfill và leakage test

Backfill feature cần giữ snapshot/code/schema version, không rewrite training set mà không có provenance. Test leakage bằng cách dịch prediction cutoff, kiểm tra feature availability và chạy negative control với field chỉ xuất hiện sau outcome.

## 5. Deletion và lineage

Xóa một subject phải lan qua raw event, offline feature, online key, training artifact, cache và exported model nếu policy yêu cầu. Feature catalog cần owner, source columns, transformation, TTL, sensitivity và downstream model.

## 6. Evidence

Theo dõi offline-online diff, feature freshness distribution, missingness by entity, point-in-time join violations, training data hash, feature version và model input schema. Chỉ model accuracy không chứng minh pipeline feature đúng.

Đọc tiếp: [05 — Modeling](../05_data_modeling_and_transformation/README.md), [10 — Serving](../10_serving_semantic_layer/README.md), [11 — Governance](../11_governance_lineage_security/README.md).
