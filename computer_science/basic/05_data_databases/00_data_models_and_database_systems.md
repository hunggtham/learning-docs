# Data model và database systems

Một program nhỏ có thể giữ state trong memory hoặc file. Khi dữ liệu cần sống lâu hơn process, được truy cập đồng thời, truy vấn theo nhiều cách, recovery sau crash và enforce constraints, ta cần một data management system. Database Management System — DBMS (데이터베이스 관리 시스템) không chỉ “lưu rows”; nó quản lý representation, query, concurrency, durability và metadata dưới một contract thống nhất.

## Data model là cách nhìn dữ liệu

Data model (데이터 모델 / mô hình dữ liệu) định nghĩa structures, relationships và operations mà user nhìn thấy. Relational model biểu diễn data bằng relations/tuples/attributes và operations theo relational algebra. Document model tổ chức documents nested. Key-value model expose key→value. Graph database nhấn mạnh vertices/edges/traversal.

Model không chỉ là storage layout. Một relational table có thể physically stored row-wise, columnar, compressed hoặc distributed nhưng vẫn expose relational semantics.

## Schema và constraints

Schema mô tả structure và constraints. Type, NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY và CHECK encode invariants gần data. Khi invariant chỉ tồn tại trong application code, nhiều writers/services dễ vi phạm.

Constraint có cost khi write nhưng đổi lại integrity được centralized. Tuy nhiên business rules phức tạp không phải lúc nào phù hợp DB constraint; boundary phải được chọn có chủ đích.

## Logical vs physical data independence

Một mục tiêu lịch sử của DBMS là tách logical model khỏi physical storage. Application viết query “tìm orders của customer X”; optimizer/storage engine quyết định index scan, join order, pages.

Abstraction này cho phép thêm index mà không sửa query semantics. Nhưng performance vẫn leak: query shape, selectivity và transaction patterns ảnh hưởng plan.

## Query language và declarative execution

SQL declarative: user mô tả result set, optimizer chọn execution plan. Đây khác imperative loop qua records. Optimizer dùng statistics và cost model để estimate rows/I/O/CPU.

Same SQL có thể chọn plan khác khi data distribution, indexes hoặc parameters thay đổi. Vì vậy “SQL text giống nhau” không guarantee performance giống nhau.

## OLTP và OLAP

Online Transaction Processing thường nhiều short reads/writes, low latency, concurrency cao, normalized relational design phổ biến. Online Analytical Processing thường scan/aggregate volumes lớn; columnar storage, denormalization/star schemas và vectorized execution phù hợp hơn.

Một schema tối ưu transaction không luôn tối ưu analytics. Workload shape quyết định physical design.

## Row store vs column store

Row store đặt fields cùng record gần nhau, tốt khi transaction đọc/write nhiều columns của một row. Column store đặt cùng column gần nhau, tốt khi analytic query chỉ đọc vài columns qua nhiều rows và compression theo column hiệu quả.

Cùng logical table, storage orientation khác tạo locality khác — connection trực tiếp với [data layout](../01_algorithms_data_structures/02_memory_models_and_data_layout.md).

## In-memory, disk-backed và distributed databases

“In-memory database” không nghĩa durability không tồn tại; nó có thể dùng WAL/snapshots để recover. Disk-backed DB cache hot pages trong memory. Distributed DB partition/replicate data qua nodes và phải đối mặt network failure, consistency và consensus.

## Metadata và catalog

DBMS cần biết tables, columns, indexes, constraints, privileges và statistics. System catalog lưu metadata này. Query planner phụ thuộc statistics; stale/misleading stats có thể làm cardinality estimates sai và chọn plan tệ.

## Mental Model

> DBMS là **state machine bền vững với query engine**: data model định nghĩa logical state; constraints bảo vệ invariants; transaction điều khiển concurrent transitions; storage/recovery làm state sống qua crash.

## Common Misconceptions

**“Database chỉ là file có API.”** DBMS thêm concurrency control, query planning, transactions, constraints, recovery và security.

**“NoSQL nghĩa không có schema.”** Schema vẫn tồn tại trong data/application expectations; có thể flexible/implicit thay vì centrally enforced.

**“Relational model = SQL implementation cụ thể.”** SQL là language family và DBMS implementations có extensions; relational model là mathematical foundation rộng hơn.

## Kết nối

Tiếp theo: [relational model/normalization](./01_relational_model_keys_and_normalization.md), [transactions](./02_transactions_acid_and_concurrency_control.md), [indexes/query execution](./03_indexes_and_query_execution.md), [WAL/recovery](./04_storage_logs_recovery_and_durability.md). Phần SQL thực hành trong repo có thể đọc song song với conceptual chapters này.
