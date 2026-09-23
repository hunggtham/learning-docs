# 03 — Storage, file format và analytical layout

## 1. Logical schema chưa đủ

Hai dataset có cùng column và cùng row nhưng performance có thể khác nhau hàng chục lần chỉ vì cách dữ liệu được đặt trên storage. Analytical system đọc khối lượng lớn dữ liệu, nên physical layout quyết định lượng byte phải đọc, khả năng parallel scan và hiệu quả compression.

Vì vậy Data Engineer phải reasoning cả logical model lẫn physical representation.

## 2. Row-oriented và column-oriented

Row-oriented layout đặt các field của một record gần nhau. Nó phù hợp khi workload thường đọc hoặc ghi phần lớn field của một số ít record, như OLTP.

Column-oriented layout nhóm giá trị cùng column. Analytical query như `SELECT region, SUM(amount)` có thể bỏ qua hàng chục column không dùng. Các giá trị cùng kiểu và thường tương tự nhau cũng nén tốt hơn.

Columnar không có nghĩa là từng column luôn là một file riêng. Format như Parquet tổ chức dữ liệu thành row group rồi lưu column chunk bên trong. Cấu trúc này cân bằng giữa scan theo column, metadata statistics và khả năng chia work.

## 3. Parquet như một ví dụ về predicate pushdown

Một Parquet file có metadata như min/max cho column trong từng row group. Nếu query cần `event_date = '2026-09-22'` và metadata chứng minh row group chỉ chứa ngày trước đó, engine có thể bỏ qua block mà không decode toàn bộ data.

Đây là predicate pushdown/data skipping. Lợi ích phụ thuộc distribution và statistics. Nếu column có min/max gần như bao trùm toàn domain trong mọi row group, khả năng skip thấp.

Physical ordering vì vậy có thể làm metadata trở nên hữu ích hơn, nhưng sorting cũng tốn compute và làm ingestion phức tạp hơn. Không có layout miễn phí.

## 4. Compression là trade-off CPU và I/O

Compression giảm byte trên storage và network nhưng cần CPU để encode/decode. Analytical workload thường hưởng lợi vì I/O đắt và columnar data nén tốt. Tuy nhiên codec mạnh hơn không mặc định tốt hơn nếu workload latency-sensitive hoặc CPU đã là bottleneck.

Phải đo end-to-end: compressed size, scan bytes, decode CPU, query latency và cost. Chọn codec chỉ theo compression ratio là tối ưu sai mục tiêu.

## 5. Partitioning

Partitioning chia dataset theo key để query có thể loại bỏ phần dữ liệu không liên quan. Time-series thường partition theo date vì query hay giới hạn thời gian.

Partition quá thô khiến mỗi query vẫn đọc nhiều dữ liệu. Partition quá mịn tạo rất nhiều directory/file nhỏ, tăng metadata overhead và scheduling cost. Partition theo key cardinality cực cao như `user_id` thường tạo explosion trừ khi platform có cơ chế khác phù hợp.

Partition key phải xuất phát từ access pattern, volume và lifecycle operation, không phải từ việc column đó "quan trọng".

## 6. Small-file problem

Một triệu file 10 KB và mười file 1 GB có tổng byte tương tự nhưng operational behavior hoàn toàn khác. Mỗi file cần metadata lookup, open request, task scheduling và bookkeeping. Với object storage, request overhead và listing cũng trở thành cost.

Streaming/micro-batch ingestion dễ sinh file nhỏ vì mỗi task liên tục flush output. Compaction gom các file nhỏ thành file lớn hơn là maintenance operation quan trọng của analytical storage.

Nhưng compaction cần coordination: không được làm reader nhìn thấy half-written state, không được mất concurrent writes và cần garbage-collect file cũ an toàn. Đây là một trong các lý do table format hiện đại tồn tại trên object storage.

## 7. Object storage không phải filesystem truyền thống

Object storage cung cấp namespace key/object và API thay vì POSIX filesystem semantics đầy đủ. Rename có thể không phải atomic metadata operation như local filesystem; trong một số hệ thống nó tương đương copy rồi delete.

Algorithm được thiết kế dựa trên atomic rename của HDFS/local filesystem có thể hoạt động kém hoặc không đúng khi chuyển thẳng sang object storage. Modern table formats giải quyết vấn đề này bằng metadata/manifest và commit protocol phù hợp hơn.

## 8. Warehouse, lake và lakehouse

Data warehouse truyền thống cung cấp storage + compute + catalog + transaction/query semantics trong một hệ thống được quản lý chặt. Data lake ưu tiên lưu dữ liệu linh hoạt trên storage rẻ/open format nhưng nếu thiếu metadata, quality và governance rất dễ thành data swamp.

Lakehouse cố gắng đưa table semantics như snapshot, schema evolution, transaction-like commit và time travel lên object storage/open file formats. Điểm cốt lõi không phải marketing term mà là separation giữa data files và metadata layer mô tả snapshot hợp lệ.

## 9. Schema evolution

Thêm column, đổi type hoặc rename field phải được xét ở cả writer, stored data và reader. Một reader cũ có thể không hiểu schema mới. Một rename đôi khi bị engine nhìn như drop + add nếu identity chỉ dựa vào tên.

Safe evolution cần compatibility policy và deployment order. Ví dụ producer thêm field optional trước, consumer được nâng cấp để đọc field đó, sau đó mới bắt đầu dựa vào field. Breaking change cần version hoặc migration explicit.

## 10. Cost reasoning

Trong cloud analytics, performance và cost thường cùng liên quan đến lượng data scan, shuffle và thời gian compute. Partition pruning, column pruning và compact file không chỉ là optimization kỹ thuật mà trực tiếp thay đổi hóa đơn.

Tuy nhiên tối ưu storage để giảm scan có thể tăng ingestion/maintenance cost. Một hệ thống tốt tối ưu total cost of ownership, bao gồm compute, storage, network, operational complexity và thời gian kỹ sư, thay vì chỉ tối thiểu một metric.

## 11. Layout invariants và read amplification

Physical layout nên được đánh giá bằng tỷ lệ giữa dữ liệu hữu ích và dữ liệu phải đọc:

```text
read amplification = bytes read / bytes returned or used
```

Partition pruning và column pruning giảm read amplification. Nhưng statistics không đáng tin nếu row group quá lớn, dữ liệu không được cluster hoặc predicate có selectivity thấp. File nhỏ hơn không mặc định tốt hơn nếu số request và metadata overhead tăng mạnh.

## 12. File commit và visibility

Writer không nên ghi trực tiếp vào path mà reader coi là committed. Mẫu an toàn là ghi temporary files, validate schema/row count/checksum, rồi publish manifest hoặc metadata commit. Nếu object storage không có atomic rename, metadata pointer phải là source of truth về visibility.

Khi retry, temporary files cũ phải có naming/version và garbage-collection policy. Nếu không, reader có thể double-count file hoặc compaction gom cả output chưa commit.

## 13. Compaction và delete semantics

Compaction rewrite data files nhưng không được thay đổi logical result. Cần kiểm tra số row, distinct key, min/max statistics, delete/tombstone và khả năng đọc snapshot cũ trong retention window. File cũ chỉ được xóa sau khi không còn reader cần.

Delete vật lý và delete logic khác nhau. Tombstone bị compaction bỏ qua quá sớm có thể làm record đã xóa “sống lại” khi đọc snapshot cũ hoặc replay.

## 14. Schema identity và type widening

Schema evolution nên phân biệt add field, rename, drop và type widening. `INT → BIGINT` có thể an toàn hơn `STRING → TIMESTAMP`; rename cần field identity hoặc explicit migration để reader không coi là drop+add.

Compatibility matrix phải kiểm tra writer mới/reader cũ, writer cũ/reader mới và file cũ/file mới. Chỉ test một hướng là không đủ cho rolling deployment.
