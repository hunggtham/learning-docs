# SQLD / SQL — Root Entrypoint

`sql/` là canonical root cho bộ tài liệu SQLD/SQL trong repository. Nội dung học đã chuẩn hóa hiện nằm tại [output/README.md](./output/README.md); các thư mục `raw/`, `raw_md/` và `scripts/` là nguồn hoặc tooling hỗ trợ, không phải learning path chính.

## Mạch đọc

Bắt đầu tại [SQLD — Tài liệu học đã chuẩn hóa](./output/README.md). Luồng chính đi từ mô hình dữ liệu (data modeling / 데이터 모델링) → SQL semantics → join/subquery/group/window → DML/TCL/transaction → DDL/constraints/view → DCL và query nâng cao.

Bộ SQLD giúp luyện cú pháp, dạng bài và thuật ngữ kỳ thi. Khi cần hiểu cơ chế sâu hơn về relational model, transaction, isolation, index, query execution hoặc optimizer, quay về canonical owner tại [Computer Science — Data & Databases](../computer_science/05_data_databases/README.md).

Khi cần hiểu dữ liệu sau database đi qua ingestion, transformation, warehouse và semantic layer như thế nào, đọc [query → transaction → pipeline → analytical serving](../computer_science/90_connections/06_query_transaction_pipeline_and_analytical_serving.md) và [Data Engineering](../data_engineering/README.md).

## Ranh giới thư mục

```text
sql/output/   = learning output chuẩn hóa
sql/raw/      = nguồn gốc / capture
sql/raw_md/   = bản trung gian Markdown
sql/scripts/  = tooling xử lý nội dung
```

Không dùng số lượng file raw làm thước đo coverage. Learning flow và canonical explanation phải đi qua `output/` hoặc các owner liên quan trong Computer Science/Data Engineering.

> **Bàn giao:** Bắt đầu tại [output/README.md](./output/README.md). Nếu một bài SQL yêu cầu hiểu “vì sao database làm như vậy”, chuyển sang [Computer Science Databases](../computer_science/05_data_databases/README.md) thay vì chỉ học thêm syntax.