# SQLD / SQL — Coverage Audit

> **Mạch đọc:** [README](./README.md) là entrypoint cấp domain; learning output nằm trong [`output/`](./output/README.md). Audit này phân biệt rõ phần **SQLD/certification** với database internals và data engineering để tránh duplicate.

Cập nhật: **2026-09-29**. `main` là nguồn chuẩn (source of truth / 정본) sau khi thay đổi được merge.

## Phạm vi và canonical owner

`sql/` sở hữu learning material hướng SQLD: mô hình dữ liệu, relational/database terminology cần cho kỳ thi, SQL semantics/patterns và procedural familiarity với truy vấn.

```text
SQLD
├── Môn 1 — 데이터 모델링의 이해
└── Môn 2 — SQL 기본 및 활용
```

`sql/output/` là material để học. `raw/`, `raw_md/` và `scripts/` là nguồn/chuyển đổi hỗ trợ, không phải canonical prose để đọc tuần tự.

Ranh giới owner:

- database internals như optimizer, MVCC, WAL, concurrency control và recovery sâu thuộc `computer_science/05_data_databases/`;
- pipeline, warehouse, semantic layer và analytical correctness thuộc `data_engineering/`;
- `sql/` giữ SQLD exam-oriented interpretation và SQL practice.

## Trạng thái coverage

| Vùng | Coverage hiện có | Trạng thái |
|---|---|---|
| Data modeling foundations | entity, attribute, relationship, identifier, ERD | Strong |
| Normalization / performance-oriented modeling | normalization và modeling trade-off ở mức SQLD | Strong |
| SELECT / filtering / grouping / ordering | SQL foundation | Strong |
| Join / subquery / set operators | query composition | Strong |
| Group / window / TOP-N / pagination | analytical SQL patterns | Strong |
| Hierarchical query | certification-specific SQL pattern | Covered |
| DML / TCL / transaction | manipulation và transaction semantics ở mức exam | Strong |
| DDL / constraint / view / object | schema-definition layer | Strong |
| DCL / role / privilege | access-control basics | Covered |
| PIVOT / UNPIVOT / regex | advanced SQLD patterns | Covered |

## Bất biến cần giữ

SQL query không chỉ cần chạy mà phải giữ đúng **row grain**, **join cardinality**, **NULL semantics**, **aggregation boundary**, **ordering/window semantics** và **transaction boundary**. Một lời giải SQLD nên giải thích được vì sao kết quả đúng, không chỉ ghi syntax cần nhớ.

Không dùng material chứng chỉ để thay thế database engineering. Khi câu hỏi chuyển từ “query này cho kết quả gì?” sang “engine thực thi, khóa, log hoặc recover như thế nào?”, phải handoff sang Computer Science Databases.

## Gaps còn lại

Gap lớn nhất không phải thêm nhiều syntax mà là tăng practice có reasoning:

1. query tracing với intermediate relation thay vì chỉ nhìn đáp án;
2. cardinality/NULL/window edge cases dễ tạo distractor;
3. transaction scenario nối exam semantics với canonical database model;
4. cross-link từ SQLD sang route `query → transaction → pipeline → analytical serving` để người học thấy giới hạn của SQLD sau kỳ thi.

Không mở rộng `sql/` thành database textbook thứ hai.

## Review protocol

Khi cập nhật:

1. kiểm tra phạm vi/outline chứng chỉ hiện hành trước khi thêm phần exam-specific;
2. giữ `output/README.md` là map chi tiết cho learning output;
3. source/OCR/generated material chỉ được promoted khi đã kiểm tra format và meaning;
4. ví dụ SQL phải nêu row set/grain hoặc transaction effect khi đó là điểm học chính;
5. link các cơ chế sâu về canonical owner thay vì copy.

> **Bàn giao:** Đọc từ [SQLD output](./output/README.md). Khi cần database mechanism sâu hơn, chuyển sang [`computer_science/05_data_databases/`](../computer_science/05_data_databases/README.md); khi cần analytical pipeline/semantic correctness, chuyển sang [`data_engineering/`](../data_engineering/README.md).