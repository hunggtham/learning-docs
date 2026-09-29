# SQLD / SQL — kiểm toán phạm vi

> **Mạch đọc:** Đọc audit này sau [README](./README.md). `README.md` là entrypoint cấp domain, còn learning output nằm trong [`output/`](./output/README.md). Audit này trả lời: **SQLD cần sở hữu phần nào để phục vụ thi và reasoning truy vấn, còn phần nào phải bàn giao sang Database Internals hoặc Data Engineering để tránh biến `sql/` thành textbook database thứ hai?**

**Ngày rà soát:** 2026-09-29. `main` là nguồn chuẩn (source of truth / 정본) sau khi thay đổi được merge.

## 1. Phạm vi sở hữu

`sql/` sở hữu tài liệu học SQLD: mô hình dữ liệu, terminology quan hệ/cơ sở dữ liệu cần cho kỳ thi, ngữ nghĩa SQL và pattern truy vấn ở mức người học phải **giải thích được vì sao kết quả đúng**.

```text
SQLD
├── Môn 1 — 데이터 모델링의 이해
└── Môn 2 — SQL 기본 및 활용
```

`sql/output/` là learning output. `raw/`, `raw_md/` và `scripts/` là provenance/chuyển đổi hỗ trợ, không phải prose chuẩn để đọc tuần tự.

Nội tại database như optimizer, MVCC, WAL, concurrency control và recovery sâu thuộc [`computer_science/05_data_databases/`](../computer_science/05_data_databases/README.md). Pipeline, warehouse, semantic layer và analytical correctness thuộc [`data_engineering/`](../data_engineering/README.md).

## 2. Coverage hiện đã mạnh

Các vùng chính của SQLD đã có: entity/attribute/relationship/identifier/ERD; normalization; `SELECT`, filtering, grouping, ordering; join, subquery, set operator; group/window/TOP-N/pagination; hierarchical query; DML/TCL/transaction; DDL/constraint/view; DCL/role/privilege; và các pattern nâng cao như `PIVOT`, `UNPIVOT`, regex.

Điểm quan trọng là coverage không nên đo bằng số syntax. Query chỉ đáng học khi người đọc hiểu **độ hạt của dòng (row grain / 행 단위)**, **lực lượng kết hợp (join cardinality / 조인 카디널리티)**, **ngữ nghĩa NULL (NULL semantics / NULL 의미론)**, **ranh giới tổng hợp (aggregation boundary / 집계 경계)**, **ngữ nghĩa thứ tự/cửa sổ (ordering/window semantics / 정렬·윈도우 의미론)** và **ranh giới giao dịch (transaction boundary / 트랜잭션 경계)**.

Nếu chỉ nhớ mẫu câu lệnh mà không dự đoán được intermediate relation hoặc duplicate row, người học chưa thật sự hiểu SQL.

## 3. Ranh giới với Database và Data Engineering

SQLD hỏi “query này trả kết quả gì?” hoặc “mô hình dữ liệu này đúng nguyên tắc nào?”. Khi câu hỏi chuyển thành “engine chọn plan nào, khóa/log/recovery hoạt động ra sao?” thì phải bàn giao sang Computer Science Databases.

Tương tự, SQLD có thể dạy aggregation/window nhưng khi câu hỏi chuyển sang pipeline, late data, semantic metric, grain qua nhiều nguồn hoặc analytical serving, owner là Data Engineering.

Ranh giới này giữ SQLD tập trung vào exam + query reasoning mà không duplicate hệ thống dữ liệu sâu hơn.

## 4. Khoảng trống ưu tiên

### P1 — Tracing query bằng intermediate relation

Cần tăng bài tập theo kiểu:

```text
FROM/JOIN tạo tập dòng nào
→ WHERE loại dòng nào
→ GROUP BY thay grain thế nào
→ HAVING lọc group nào
→ window function nhìn partition/order nào
→ SELECT cuối cùng biểu diễn gì
```

Cách này có giá trị hơn học thuộc logical processing order vì nó buộc người học theo dõi dữ liệu thật qua từng bước.

### P1 — Edge case về cardinality, NULL và window

Các distractor khó thường sinh từ duplicate row sau join, `NULL` trong so sánh/tổng hợp, tie trong ranking hoặc window frame. Nên tăng case nhỏ nhưng có reasoning rõ, thay vì chỉ tăng số câu trắc nghiệm.

### P1 — Transaction scenario

Cần nối exam semantics với mô hình canonical: transaction boundary, commit/rollback, visibility/isolation consequence. Không đi sâu implementation MVCC/WAL ở đây; chỉ đủ để người học hiểu câu SQL thay đổi trạng thái gì và khi nào trạng thái đó trở nên durable/visible theo contract.

### P2 — Handoff sau SQLD

Nên link rõ từ SQLD sang tuyến [`query → transaction → pipeline → analytical serving`](../computer_science/90_connections/06_query_transaction_pipeline_and_analytical_serving.md) để người học thấy SQLD là nền, không phải điểm kết thúc của database/data reasoning.

## 5. Quy trình review

Khi cập nhật domain:

1. kiểm phạm vi/outline chứng chỉ hiện hành trước khi thêm nội dung exam-specific;
2. giữ [`output/README.md`](./output/README.md) là learning map chi tiết;
3. chỉ promote OCR/generated material sau khi kiểm format và meaning;
4. ví dụ SQL phải nêu row set/grain hoặc transaction effect khi đó là điểm học chính;
5. link cơ chế sâu sang canonical owner thay vì copy.

## 6. Kết luận và bàn giao

Coverage SQLD hiện **mạnh**; gap lớn nhất là tăng reasoning qua intermediate relation, edge case và transaction scenario. Không cần mở rộng `sql/` thành database textbook thứ hai.

Bắt đầu học tại [SQLD output](./output/README.md). Khi cần cơ chế database sâu hơn, chuyển sang [Computer Science Databases](../computer_science/05_data_databases/README.md); khi cần analytical pipeline và semantic correctness, chuyển sang [Data Engineering](../data_engineering/README.md).