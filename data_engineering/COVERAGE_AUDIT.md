# Data Engineering — Coverage Audit

Cập nhật: 2026-09-23. `main` là source of truth của Data Engineering.

Audit này kiểm tra library theo chuỗi:

```text
source → capture → storage → model → distributed/stream processing
       → orchestration → serving → governance → cost/recovery
```

Mỗi boundary phải mô tả được mechanism, invariant, failure mode, evidence và trade-off. Không đánh giá độ sâu bằng số lượng keyword tool.

## Trạng thái coverage

| Chapter | Boundary chính | Trạng thái |
|---|---|---|
| 01 Foundations | lifecycle, OLTP/OLAP, correctness, invariant | Strong |
| 02 Pipeline architecture | CDC, delivery, checkpoint, replay, backfill | Strong |
| 03 Storage and formats | layout, pruning, files, snapshots, schema evolution | Strong |
| 04 Reliability and production | quality, SLO, lineage, recovery, security, cost | Strong |
| 05 Modeling and transformation | grain, identity, temporal join, event/state/snapshot | Strong |
| 06 Distributed processing | partition, shuffle, skew, spill, retry determinism | Strong |
| 07 Streaming systems | event time, watermark, state, CDC handoff, backpressure | Strong |
| 08 Orchestration and backfill | manifest, fencing, partition completeness, retry taxonomy | Strong |
| 09 Warehouse/lake/lakehouse | snapshot isolation, compaction, delete, maintenance | Strong |
| 10 Serving/semantic layer | metric algebra, versioning, point-in-time, cache | Strong |
| 11 Governance/lineage/security | contract, ownership, policy, lineage confidence, deletion | Strong |
| 12 Cost/performance/capacity | queueing, saturation, attribution, semantic guardrails | Strong |
| 13 Approximate computation | sketches, sampling, mergeability, error bounds | Strong |
| 14 Multi-region/residency | replication lag, conflict, failover, RPO/RTO, residency | Strong |
| 15 ML feature platform | point-in-time joins, offline/online parity, deletion | Strong |
| 16 Privacy-preserving analytics | threat model, differential privacy, composition, release policy | Strong |
| 17 Contract testing | compatibility matrix, consumer contracts, runtime enforcement | Strong |
| 90 Case studies | end-to-end failure and evidence reasoning | Strong |

## Invariant checklist

- **Identity:** duplicate, update, delete và correction có identity/version rõ.
- **Time:** event time, processing time, ingestion time và snapshot time không bị trộn.
- **Grain:** mỗi row/metric có grain; join cardinality được kiểm tra trước aggregate.
- **Visibility:** output chỉ public qua commit marker/snapshot hợp lệ.
- **Replay:** input, code, schema, state và side effect có version/recovery policy.
- **Evolution:** schema/metric change có compatibility matrix, owner và deprecation window.
- **Quality:** freshness, completeness, correctness và availability có SLO riêng.
- **Security:** raw/model/serving access, masking, retention và deletion có evidence.
- **Economics:** scan, shuffle, spill, storage, maintenance và concurrency có attribution.

## Gaps còn lại

Các boundary P2 phía trên đã có chapter canonical. Những gap tiếp theo nên được mở chỉ khi có conceptual boundary độc lập:

1. **Approximate query operations:** error propagation qua nhiều metric và calibration theo segment.
2. **Multi-region active-active:** causal ordering, conflict-free merge và residency-aware routing.
3. **ML feature operations:** drift, training-serving parity ở scale và model rollback với feature version.
4. **Privacy composition:** privacy accountant liên domain và utility evaluation cho query workload thật.
5. **Contract platform:** schema/semantic registry, exception expiry và automated blast-radius graph.

Không mở chapter chỉ để liệt kê Kafka/Spark/Airflow/dbt. Mỗi gap phải có invariant/failure model riêng, nhiều downstream dependency và evidence có thể kiểm chứng.

## Review protocol

Khi sửa một chapter:

1. thêm hoặc cập nhật mechanism và invariant;
2. thêm ít nhất một failure/edge case;
3. nêu evidence/metric để phân biệt success giả với success thật;
4. kiểm tra link và dependency map;
5. chạy `npm run audit:library` và `npm run build:library` nếu thay đổi ảnh hưởng publishing.
