# Data Engineering Knowledge Library

Data Engineering là lĩnh vực xây dựng các hệ thống biến dữ liệu thô, phân tán và thường không đáng tin cậy thành dữ liệu có cấu trúc, có ngữ nghĩa, có thể kiểm chứng và đủ ổn định để phục vụ phân tích, sản phẩm dữ liệu, machine learning và vận hành doanh nghiệp.

Đọc [COVERAGE_AUDIT.md](COVERAGE_AUDIT.md) để xem quality gate, invariant checklist và các gap còn lại của toàn bộ library.

Library này không được tổ chức như danh sách công cụ. Kafka, Spark, Airflow, dbt, một data warehouse hay một cloud service chỉ là các hiện thực cụ thể của những vấn đề sâu hơn: dữ liệu đến từ đâu, trạng thái nào là đúng, dữ liệu được lưu theo hình dạng nào, khi chạy lại pipeline có phá kết quả không, schema thay đổi thì điều gì xảy ra, một record đến muộn được xử lý thế nào, và khi dashboard sai thì làm sao lần ngược về nguyên nhân.

Mục tiêu học tập vì vậy đi theo chuỗi reasoning:

`nguồn dữ liệu → ingestion → storage → modeling → transformation → serving → observation/governance`

Mỗi bước đều phải trả lời ba câu hỏi: invariant nào cần được giữ, failure nào có thể phá invariant đó, và evidence nào cho phép chứng minh hệ thống đang hoạt động đúng.

## Chuẩn độ sâu của chapter

Mỗi chapter canonical phải đi qua chuỗi:

```text
problem → mental model → mechanism → invariant
       → failure/edge case → evidence → trade-off → lower-layer connection
```

Nếu một phần chỉ mô tả API hoặc tên sản phẩm mà không nói guarantee và failure behavior, nó là implementation note chứ chưa phải Data Engineering reasoning.

## Lộ trình canonical

Bắt đầu với [01 — Data Engineering từ first principles](01_foundations.md). Chapter này thiết lập mental model về data lifecycle, batch/streaming, OLTP/OLAP, correctness và vì sao pipeline không đơn giản là "copy dữ liệu từ A sang B".

Tiếp theo đọc [02 — Kiến trúc pipeline và semantics](02_pipeline_architecture.md) để hiểu ingestion, ETL/ELT, CDC, idempotency, replay, delivery semantics, event time và backfill. Đây là lớp kiến thức cần có trước khi học một orchestration framework hoặc streaming engine cụ thể.

Sau đó đọc [03 — Storage, file format và analytical layout](03_storage_and_formats.md). Phần này giải thích row/column layout, Parquet, compression, partitioning, small-file problem và tại sao cách đặt dữ liệu vật lý ảnh hưởng trực tiếp đến query cost.

Cuối cùng đọc [04 — Reliability, quality và production reasoning](04_reliability_and_production.md), nơi pipeline được nhìn như một production system: data quality, contracts, lineage, observability, retry, recovery, security và cost.

## Lộ trình mở rộng theo conceptual boundary

Sau bốn foundation chapters, đi theo các boundary sau. Mỗi phần bắt đầu từ invariant và failure mode rồi mới ánh xạ sang tool:

1. [05 — Data modeling và transformation](05_data_modeling_and_transformation/README.md): grain, identity, event/state/snapshot, history và deterministic transformation.
2. [06 — Distributed processing](06_distributed_processing/README.md): partition → shuffle → skew → spill, join semantics và fault recovery.
3. [07 — Streaming systems](07_streaming_systems/README.md): event time → watermark → state → late event, CDC, schema evolution và replay.
4. [08 — Orchestration và backfill](08_orchestration_and_backfill/README.md): dependency, partition completeness, retry, catchup và backfill correctness.
5. [09 — Warehouse, lake và lakehouse](09_warehouse_lake_lakehouse/README.md): snapshot, commit protocol, compaction, schema evolution và object-storage boundaries.
6. [10 — Serving và semantic layer](10_serving_semantic_layer/README.md): metric contract, point-in-time correctness, materialization và consumer shape.
7. [11 — Governance, lineage và security](11_governance_lineage_security/README.md): ownership, data contract, lineage, access, retention và deletion.
8. [12 — Cost, performance và capacity](12_cost_performance_capacity/README.md): scan, shuffle, spill, small files, concurrency và unit economics.
9. [90 — Case studies](90_case_studies/README.md): CDC duplicate, late event, backfill race, compaction race và semantic fan-out.

### Dependency map

```text
01 foundations
  ├── 02 pipeline semantics ──┬── 07 streaming ────────┐
  ├── 03 storage/layout ──────┴── 09 warehouse/lakehouse ┤
  └── 04 reliability ───────────────┬── 08 orchestration ─┤
                                    ├── 11 governance ────┤
05 modeling/transformation ─────────┴── 10 serving ───────┤
06 distributed processing ───────────── 12 cost/capacity ─┤
                                                         90 case studies
```

### Tool boundary

Kafka, Spark, Flink, Airflow, dbt, warehouse và cloud services chỉ nên xuất hiện như implementation mapping sau khi các chapter tương ứng đã giải thích mental model. Một tool mới phải trả lời được: nó duy trì invariant nào, failure boundary ở đâu, và evidence nào chứng minh guarantee đó trong production.

## Boundary với SQL và Database

Repository hiện có `sql/` chứa tài liệu SQL và mô hình dữ liệu. Không di chuyển thư mục đó một cách cơ học. SQL sau này sẽ được consolidate vào Data Engineering theo boundary sau.

Kiến thức về relational model, query semantics, joins, aggregation, window functions, analytical SQL và cách SQL tham gia transformation thuộc learning path Data Engineering. Kiến thức về transaction engine, MVCC, WAL, B-tree, buffer pool, optimizer internals và concurrency control là nền tảng database systems; Data Engineering sẽ cross-link thay vì copy lại toàn bộ.

Trong giai đoạn migration, `sql/` vẫn là nguồn canonical cho nội dung SQL hiện có. Khi migration diễn ra, link cũ phải được kiểm tra trước khi đổi path và raw/source material không được xóa chỉ vì canonical reading material đã chuyển nơi.

## Mental model xuyên suốt

Một pipeline tốt không được định nghĩa bởi việc job "chạy xanh". Một job có thể thành công về mặt process nhưng tạo dữ liệu sai. Correctness phải được nhìn ở nhiều lớp: record có bị mất hoặc duplicate không, schema có đúng không, business invariant có còn đúng không, dữ liệu có đủ fresh không, và downstream consumer có đang đọc đúng version hay không.

Vì vậy library này ưu tiên reasoning về correctness, replayability, observability và ownership trước syntax của công cụ. Khi hiểu các invariant đó, việc học Spark, Kafka, Airflow, dbt hoặc một cloud data platform trở thành việc ánh xạ một công cụ vào mental model đã có thay vì ghi nhớ hàng loạt API.
