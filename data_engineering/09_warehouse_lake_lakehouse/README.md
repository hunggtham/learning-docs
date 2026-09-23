# 09 — Warehouse, lake và lakehouse

Warehouse, lake và lakehouse là các điểm khác nhau trên trục storage, schema, transaction, governance và compute. Không nên chọn bằng khẩu hiệu; hãy bắt đầu từ workload và invariant cần giữ.

## 1. Warehouse

Warehouse thường cung cấp catalog, SQL, workload isolation, access control và managed compute cùng các semantics phân tích tương đối chặt. Đổi lại chi phí, format và portability có thể bị gắn với platform.

Điểm cần kiểm tra là query isolation, concurrency, ingestion latency, historical correction và quyền truy cập—not chỉ benchmark scan.

## 2. Data lake

Lake lưu file linh hoạt trên object storage, phù hợp raw evidence, nhiều format và chi phí storage thấp. Nếu thiếu schema discipline, ownership, quality và catalog, lake nhanh chóng trở thành swamp: nhiều file nhưng không biết file nào đáng tin.

Object storage không cung cấp mọi semantics của filesystem. Rename có thể là copy+delete; listing có thể eventually consistent; nhiều writer có thể ghi cùng prefix. Commit protocol phải được thiết kế rõ.

## 3. Lakehouse và snapshot

Lakehouse thêm metadata layer mô tả snapshot hợp lệ của các data files. Một commit thường gồm:

```text
read current snapshot → validate conflict → write new files → publish metadata pointer
```

Reader chỉ đọc file thuộc snapshot đã commit. Time travel là khả năng chọn snapshot cũ, không phải phép màu để phục hồi mọi dữ liệu nếu file đã bị garbage-collect.

## 4. Compaction

Streaming và micro-batch tạo small files. Compaction đọc nhiều file nhỏ, rewrite thành file lớn hơn và cập nhật metadata. Compaction phải bảo đảm reader cũ vẫn đọc được snapshot của nó, reader mới thấy snapshot mới, và file cũ chỉ bị xóa sau retention an toàn.

Compaction quá thường xuyên làm tăng write amplification; quá muộn làm query metadata và task scheduling chậm. Trigger nên dựa trên file count/size, query behavior và recovery window.

## 5. Snapshot và schema evolution

Schema evolution cần tương thích với cả file cũ, reader cũ và writer mới. Add nullable field thường dễ hơn rename/type narrowing. Nếu field identity chỉ dựa trên tên, rename có thể bị hiểu như drop+add.

Migration an toàn thường dùng dual-read/dual-write hoặc versioned schema, có compatibility window và rollback path. Xóa column khỏi metadata không đồng nghĩa bytes đã biến mất; retention/privacy policy phải bao phủ cả file cũ và snapshot cũ.

## 6. Partition và layout

Partition theo ngày hỗ trợ pruning và lifecycle nhưng có thể tạo partition nhỏ khi volume thấp. Partition theo high-cardinality key tạo directory explosion. File size, row group, sort order và clustering có thể quan trọng hơn số partition.

Layout phải được đo bằng bytes scanned, files opened, task count, compaction cost và query latency trên workload thật.

## 7. Decision frame

Chọn storage bằng câu hỏi:

1. Raw evidence cần giữ và replay trong bao lâu?
2. Consumer cần SQL ad-hoc, API latency hay batch scan?
3. Snapshot/transaction semantics cần mạnh tới mức nào?
4. Schema evolution và multi-writer conflict được kiểm soát ra sao?
5. Catalog, lineage, access control, deletion và cost ownership thuộc về ai?

Đọc tiếp: [03 — Storage và formats](../03_storage_and_formats.md), [11 — Governance](../11_governance_lineage_security/README.md), [12 — Cost và capacity](../12_cost_performance_capacity/README.md).
