# Query optimization và execution plans

Hai SQL queries có thể trả cùng kết quả nhưng runtime chênh hàng nghìn lần. Database optimizer (옵티마이저) giải bài toán tìm physical plan có estimated cost thấp trong không gian plans rất lớn. Đây là nơi algorithms, statistics, storage, CPU cache và relational algebra gặp nhau.

## Từ query text đến physical plan

Pipeline khái quát:

```text
parse SQL
→ bind names/types
→ build logical plan
→ rewrite logical expressions
→ enumerate physical alternatives
→ estimate cost
→ choose plan
→ execute operators
```

Optimizer không “hiểu business meaning”; nó dựa vào schema, constraints, statistics và cost model.

## Cardinality estimation là trái tim của cost model

Nếu optimizer đoán một filter trả 10 rows nhưng thực tế 10 triệu, join order và join algorithm có thể sai hoàn toàn.

Statistics thường gồm row count, number of distinct values, histograms, null fraction và đôi khi extended/multi-column statistics.

Assumption independence giữa columns thường sai. `city='Seoul'` và `country='KR'` có correlation mạnh; multiply selectivities độc lập có thể underestimate/overestimate.

## Join order explosion

Với nhiều tables, số possible join orders tăng cực nhanh. Exhaustive search sớm trở nên infeasible, nên optimizers dùng dynamic programming cho small join sets, heuristics hoặc restricted search spaces.

Join associativity cho phép `(A join B) join C` và `A join (B join C)` tương đương với inner joins dưới conditions phù hợp, tạo optimization freedom.

Outer joins, lateral dependencies và volatile functions giảm freedom này.

## Physical operators

Nested-loop join phù hợp khi outer nhỏ và inner có index selective. Hash join tốt cho equality join khi build side vừa memory. Sort-merge join hữu ích khi inputs đã sorted hoặc sort có giá trị cho downstream.

Sequential scan có thể nhanh hơn index scan khi query cần phần lớn table, vì random page fetch + lookup overhead vượt lợi ích index.

Không có operator “tốt nhất”; phù hợp phụ thuộc cardinality, ordering, memory và storage.

## SARGability

Predicate search-argument-able cho phép index access hiệu quả hơn. Ví dụ `WHERE created_at >= ?` thường index-friendly hơn `WHERE function(created_at) = ?` nếu DB không có expression index tương ứng.

Concept quan trọng là transformation của column có thể làm index key order không còn usable trực tiếp.

## Covering index và index-only scan

Nếu index chứa đủ columns query cần, engine có thể tránh table lookup cho nhiều rows. Điều này đổi random I/O pattern đáng kể.

Nhưng index rộng tăng storage và write amplification. Mỗi INSERT/UPDATE phải maintain indexes, nên read optimization có write cost.

## Sort, spill và memory grants

Sort/hash operators cần memory. Nếu dataset vượt allocation, engine spill ra temporary storage và latency tăng mạnh.

Query chậm đột biến khi data size vượt memory threshold là ví dụ phase change: cùng plan nhưng physical behavior khác vì resource constraint.

## EXPLAIN như evidence, không phải decoration

Execution plan cho thấy operator tree, estimated rows/cost và trong `ANALYZE` mode có thể có actual rows/time.

Một debugging path tốt là tìm nơi estimates lệch actual lớn, xem access path, join order, filters, sorts/spills rồi mới quyết định index/rewrite/statistics.

Không nên tối ưu bằng cách đoán chỉ từ SQL text.

## Parameter sensitivity

Một prepared query có thể nhận values có selectivity rất khác. Plan tốt cho common value có thể tệ cho rare value hoặc ngược lại. DBMSs có mechanisms khác nhau cho parameter sniffing, generic/custom plans hoặc adaptive plans.

Điều này cho thấy “một query = một optimal plan” không luôn đúng trên changing parameters.

## Common Misconceptions

**“Có index thì database sẽ dùng.”** Optimizer có thể đúng khi không dùng nếu scan rẻ hơn.

**“Cost trong EXPLAIN là milliseconds.”** Thường là internal cost units, không phải wall-clock trực tiếp.

**“Rewrite SQL đẹp hơn luôn nhanh hơn.”** Optimizer có thể normalize chúng về cùng plan; phải kiểm tra actual plan.

## Mental Model

> Query optimization là search dưới uncertainty: optimizer dùng statistics để dự đoán cardinality, từ đó chọn operators có cost model phù hợp. Sai estimate thường kéo theo sai plan.

## Kết nối

Đọc cùng [SQL semantics](./05_relational_algebra_and_sql_semantics.md), [indexes/query execution](./03_indexes_and_query_execution.md), [storage hardware](../02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) và [software performance](../08_software_systems/02_performance_capacity_and_scalability.md).