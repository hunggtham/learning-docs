# Data Engineering Knowledge Library

Data Engineering là lĩnh vực xây dựng các hệ thống biến dữ liệu thô, phân tán và thường không đáng tin cậy thành dữ liệu có cấu trúc, có ngữ nghĩa, có thể kiểm chứng và đủ ổn định để phục vụ phân tích, sản phẩm dữ liệu, machine learning và vận hành doanh nghiệp.

Library này không được tổ chức như danh sách công cụ. Kafka, Spark, Airflow, dbt, một data warehouse hay một cloud service chỉ là các hiện thực cụ thể của những vấn đề sâu hơn: dữ liệu đến từ đâu, trạng thái nào là đúng, dữ liệu được lưu theo hình dạng nào, khi chạy lại pipeline có phá kết quả không, schema thay đổi thì điều gì xảy ra, một record đến muộn được xử lý thế nào, và khi dashboard sai thì làm sao lần ngược về nguyên nhân.

Mục tiêu học tập vì vậy đi theo chuỗi reasoning:

`nguồn dữ liệu → ingestion → storage → modeling → transformation → serving → observation/governance`

Mỗi bước đều phải trả lời ba câu hỏi: invariant nào cần được giữ, failure nào có thể phá invariant đó, và evidence nào cho phép chứng minh hệ thống đang hoạt động đúng.

## Lộ trình canonical

Bắt đầu với [01 — Data Engineering từ first principles](01_foundations.md). Chapter này thiết lập mental model về data lifecycle, batch/streaming, OLTP/OLAP, correctness và vì sao pipeline không đơn giản là "copy dữ liệu từ A sang B".

Tiếp theo đọc [02 — Kiến trúc pipeline và semantics](02_pipeline_architecture.md) để hiểu ingestion, ETL/ELT, CDC, idempotency, replay, delivery semantics, event time và backfill. Đây là lớp kiến thức cần có trước khi học một orchestration framework hoặc streaming engine cụ thể.

Sau đó đọc [03 — Storage, file format và analytical layout](03_storage_and_formats.md). Phần này giải thích row/column layout, Parquet, compression, partitioning, small-file problem và tại sao cách đặt dữ liệu vật lý ảnh hưởng trực tiếp đến query cost.

Cuối cùng đọc [04 — Reliability, quality và production reasoning](04_reliability_and_production.md), nơi pipeline được nhìn như một production system: data quality, contracts, lineage, observability, retry, recovery, security và cost.

Các chapter sau sẽ tiếp tục đào sâu distributed processing, streaming internals, orchestration, warehouse/lake/lakehouse, governance và production architecture nhưng chỉ được tách thành file riêng khi conceptual boundary đủ rõ.

## Boundary với SQL và Database

Repository hiện có `sql/` chứa tài liệu SQL và mô hình dữ liệu. Không di chuyển thư mục đó một cách cơ học. SQL sau này sẽ được consolidate vào Data Engineering theo boundary sau.

Kiến thức về relational model, query semantics, joins, aggregation, window functions, analytical SQL và cách SQL tham gia transformation thuộc learning path Data Engineering. Kiến thức về transaction engine, MVCC, WAL, B-tree, buffer pool, optimizer internals và concurrency control là nền tảng database systems; Data Engineering sẽ cross-link thay vì copy lại toàn bộ.

Trong giai đoạn migration, `sql/` vẫn là nguồn canonical cho nội dung SQL hiện có. Khi migration diễn ra, link cũ phải được kiểm tra trước khi đổi path và raw/source material không được xóa chỉ vì canonical reading material đã chuyển nơi.

## Mental model xuyên suốt

Một pipeline tốt không được định nghĩa bởi việc job "chạy xanh". Một job có thể thành công về mặt process nhưng tạo dữ liệu sai. Correctness phải được nhìn ở nhiều lớp: record có bị mất hoặc duplicate không, schema có đúng không, business invariant có còn đúng không, dữ liệu có đủ fresh không, và downstream consumer có đang đọc đúng version hay không.

Vì vậy library này ưu tiên reasoning về correctness, replayability, observability và ownership trước syntax của công cụ. Khi hiểu các invariant đó, việc học Spark, Kafka, Airflow, dbt hoặc một cloud data platform trở thành việc ánh xạ một công cụ vào mental model đã có thay vì ghi nhớ hàng loạt API.