# Data engineering — source ledger và version/currentness boundary

> **Owner:** `data_engineering/`. Ledger này giữ source route cho semantics, hệ thống và tool; chapter vẫn phải chỉ rõ claim nào là invariant, claim nào là implementation.

**Lần kiểm tra cổng nguồn:** 2026-10-09 (Asia/Seoul).

## Source ledger

| Source ID | Cơ quan/chủ thể | Claim type được phép | URL | Version/date | Currentness boundary | Owner/used in |
|---|---|---|---|---|---|---|
| DE-IETF-HTTP-01 | IETF / RFC Editor | HTTP semantics khi data service/API dùng giao thức HTTP | https://www.rfc-editor.org/rfc/rfc9110.html | RFC 9110, June 2022; kiểm tra 2026-10-09 | Chỉ là protocol semantics, không phải guarantee của pipeline/tool | serving/API boundary |
| DE-POSTGRES-01 | PostgreSQL Global Development Group | SQL/transaction/storage behavior của PostgreSQL | https://www.postgresql.org/docs/current/ | current manual 18.x hiển thị 2026-10-09 | Ghi major version; không suy rộng sang mọi warehouse/database | SQL/database boundary |
| DE-KAFKA-01 | Apache Kafka | broker/client/streaming implementation semantics | https://kafka.apache.org/documentation/ | docs live; ghi release khi dùng | Defaults, guarantees và config có thể đổi theo release; phải ghi version/config | `07_streaming_systems/` |
| DE-SPARK-01 | Apache Spark | distributed processing/DataFrame/Spark SQL implementation | https://spark.apache.org/docs/latest/ | docs live; ghi release khi dùng | Không coi Spark behavior là invariant của distributed systems nói chung | `06_distributed_processing/` |
| DE-AIRFLOW-01 | Apache Airflow | orchestration, scheduling và backfill implementation | https://airflow.apache.org/docs/ | docs live; ghi release khi dùng | DAG behavior cần version/provider/config; không dùng docs mới cho runtime cũ mà không ghi boundary | `08_orchestration_and_backfill/` |

## Claim chưa đủ nguồn

| Claim ID | Trạng thái | Ranh giới an toàn | Owner/next verification |
|---|---|---|---|
| DE-TOOL-GUARANTEE-01 | `NEEDS_SOURCE` | Claim “at-least-once/exactly-once”, ordering, replay, backfill hoặc freshness phải ghi engine/version/config và test evidence; không suy ra chỉ từ tên tool. | Owner chapter tool tương ứng |
| DE-BENCHMARK-01 | `NEEDS_SOURCE` | Số throughput/cost/latency cần workload, scale, hardware/cloud, version và ngày; không dùng marketing number như benchmark. | Owner case studies |
| DE-CLOUD-01 | `NEEDS_SOURCE` | Claim về cloud service, pricing, quota, residency hoặc compliance cần docs/price page hiện hành và region; nếu thiếu chỉ mô tả concept. | Owner cloud-specific chapter |

## Quy trình refresh

1. Mỗi chapter tách protocol/invariant khỏi implementation/config.
2. Ghi release/major version và ngày truy cập với docs live.
3. Khi tool deprecate hoặc đổi default, cập nhật claim map và case study; structural audit không đủ để xác nhận semantics.
