# MVCC, visibility, WAL và recovery internals

Ở mức foundation, ACID và MVCC thường được mô tả như cơ chế giúp nhiều transactions cùng chạy mà ít block nhau. Ở mức advanced, cần hiểu một câu hỏi cụ thể hơn: **một reader nhìn thấy version nào, version đó được bảo vệ khỏi crash ra sao, và engine dọn versions cũ khi nào?**

## MVCC biến một row thành lịch sử versions

Multi-Version Concurrency Control (MVCC / 다중 버전 동시성 제어) không nhất thiết lưu “nhiều bản copy hoàn chỉnh” theo cùng cách ở mọi DBMS, nhưng mental model hữu ích là mỗi logical row có các versions gắn với transaction/commit metadata.

Reader không đơn giản lấy version mới nhất về thời gian vật lý. Nó lấy version **visible đối với snapshot/isolation rule** của transaction. Vì vậy hai transactions cùng query một key tại gần cùng thời điểm có thể hợp lệ khi nhìn thấy hai versions khác nhau.

## Snapshot là tập quy tắc visibility

Một snapshot thường cần biểu diễn boundary của transactions đã commit, đang active hoặc bắt đầu sau thời điểm snapshot. Engine dùng metadata của row version để quyết định:

```text
version này được tạo bởi transaction nào?
creator đã commit chưa?
commit nằm trước hay sau snapshot?
version có bị delete/update bởi transaction khác không?
```

Chi tiết khác giữa PostgreSQL, Oracle, MySQL/InnoDB hay SQL Server, nhưng abstraction chung là **visibility function(snapshot, version)**.

## Update không nhất thiết overwrite tại chỗ

Với MVCC, update thường tạo version mới hoặc record mới kèm undo information. Old version phải tiếp tục tồn tại nếu còn snapshot cũ cần đọc nó. Điều này giải thích vì sao long-running transactions có thể làm vacuum/purge chậm, giữ undo/old tuples lâu và tăng storage pressure.

Từ đây thấy một trade-off: readers ít block writers hơn, nhưng engine phải trả cost quản lý version lifecycle.

## WAL giải quyết crash durability theo write-ahead rule

Write-Ahead Logging (WAL / 선행 기록 로그) dựa trên nguyên tắc: thông tin log đủ để recover thay đổi phải được durable **trước** khi data page tương ứng được coi là durable trên disk.

Data pages có thể được flush theo thứ tự khác transaction commit. WAL cung cấp một sequential-ish durability path hiệu quả hơn việc buộc flush mọi random page mỗi commit.

Một commit thường cần đảm bảo commit record/log position đã tới durable storage theo policy. Sau crash, recovery dùng log để xác định effects nào phải redo, effects nào chưa được coi commit và cần undo hoặc bỏ qua tùy architecture.

## Steal/no-steal và force/no-force

Buffer manager policy ảnh hưởng recovery design. Nếu dirty page của uncommitted transaction được phép ghi ra disk, đó là **steal** và recovery phải có cách undo effects chưa commit. Nếu committed pages không bắt buộc flush ngay tại commit, đó là **no-force** và recovery cần redo committed changes chưa tới data file.

Nhiều high-performance engines dùng steal + no-force vì throughput tốt, đổi lại recovery/logging phức tạp hơn.

## LSN và page state

Log Sequence Number (LSN) tạo ordering logic cho log records. Data page có thể lưu pageLSN cho biết log record mới nhất đã reflected vào page. Recovery dùng quan hệ giữa pageLSN và log record LSN để tránh redo work đã có.

Concept này cho thấy durability không phải “save file xong”. Nó là protocol giữa log, buffer pool, page metadata, checkpoint và storage ordering.

## Checkpoint không đồng nghĩa mọi dirty page đã sạch

Checkpoint nhằm giới hạn recovery work, nhưng implementation không nhất thiết flush toàn bộ pages đồng thời. Fuzzy checkpoint có thể ghi metadata về active transactions/dirty pages trong khi workload vẫn chạy.

Sau crash, recovery bắt đầu từ checkpoint rồi phân tích log cần thiết thay vì scan từ đầu lịch sử database.

## MVCC và WAL giao nhau ở transaction identity

MVCC cần biết transaction nào tạo/xóa version và trạng thái commit của nó. WAL/recovery cần tái tạo hoặc xác nhận transaction state sau crash. Vì vậy transaction table, commit metadata, undo/redo và visibility không phải những subsystem hoàn toàn tách biệt.

Một crash giữa “data page đã ghi” và “commit log chưa durable” phải được xử lý sao cho transaction không đột nhiên xuất hiện như committed. Đây chính là nơi protocol ordering quyết định correctness.

## Vacuum/purge và transaction horizon

Old versions không thể xóa chỉ vì có version mới. Engine cần biết không còn snapshot hợp lệ nào có thể nhìn thấy old version. Horizon quá cũ do long transaction, replica lag hoặc idle transaction có thể giữ garbage lâu.

Trong production, bloat hoặc undo growth đôi khi không phải “DB tự dọn kém” mà là consequence của snapshot lifetime.

## Mental Model

> MVCC trả lời **ai nhìn thấy version nào**; WAL trả lời **sau crash history nào được coi là thật**; vacuum/purge trả lời **khi nào history cũ có thể bị quên**. Ba câu hỏi này cùng định nghĩa transaction lifecycle.

## Kết nối

Ôn [Transactions/ACID](../../basic/05_data_databases/02_transactions_acid_and_concurrency_control.md) và [WAL/recovery foundation](../../basic/05_data_databases/04_storage_logs_recovery_and_durability.md). Khi học distributed database, hãy nối tiếp sang consensus/replication và distributed transaction protocols.