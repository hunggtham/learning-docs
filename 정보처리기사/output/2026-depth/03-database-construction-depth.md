# Môn 3 — 데이터베이스 구축: Deep Dive 2026

> Môn 3 không nên học bằng cách thuộc lệnh SQL rời rạc. Cần hiểu toàn bộ chuỗi: **data model → key/dependency → normalization → physical storage/index → SQL → transaction/concurrency/recovery → migration**.

## 1. 데이터베이스 기본 개념

Database là tập dữ liệu có cấu trúc được quản lý để nhiều ứng dụng/user có thể truy cập nhất quán. DBMS cung cấp definition, storage, query, transaction, concurrency, recovery, security và integrity.

### 1.1 Three-Schema Architecture

External Schema — 외부 스키마 — view của từng user/application. Conceptual Schema — 개념 스키마 — mô hình logic tổng thể của toàn database. Internal Schema — 내부 스키마 — cách data được lưu vật lý.

Data independence được chia thành logical data independence và physical data independence. Physical independence nghĩa thay đổi storage/index mà application logic không phải đổi. Logical independence khó hơn: thay đổi conceptual schema nhưng external view/application ít bị ảnh hưởng.

### 1.2 Data Model

Data model gồm structure, operation và constraint. Các mô hình lịch sử như hierarchical, network, relational có cách biểu diễn relation khác nhau. Relational model biểu diễn data bằng relation/table và dựa mạnh vào relational algebra/set theory.

## 2. 논리 데이터베이스 설계 — Logical Database Design

### 2.1 Entity, Attribute, Relationship

Entity là đối tượng cần quản lý. Attribute là đặc tính. Relationship mô tả liên hệ giữa entity. Cardinality thường gặp: 1:1, 1:N, M:N. Participation có thể mandatory/optional tùy model.

M:N trong relational implementation thường cần associative/junction table để tách thành hai quan hệ 1:N.

### 2.2 Keys

Super Key — 슈퍼키 — tập attribute xác định duy nhất tuple, có thể thừa. Candidate Key — 후보키 — super key tối thiểu. Primary Key — 기본키 — candidate key được chọn chính. Alternate Key — 대체키 — candidate key còn lại. Foreign Key — 외래키 — attribute tham chiếu key của relation khác. Composite Key — 복합키 — key gồm nhiều attribute.

Hai property cốt lõi của candidate key: uniqueness và minimality.

### 2.3 Integrity Constraints

Entity Integrity: primary key không NULL. Referential Integrity: foreign key phải tham chiếu target hợp lệ hoặc NULL nếu schema cho phép. Domain Integrity: value nằm trong domain/type/range hợp lệ.

Khi delete parent row, behavior có thể RESTRICT/NO ACTION, CASCADE, SET NULL hoặc SET DEFAULT tùy DBMS/schema.

## 3. Relational Algebra

Relational algebra là nền tảng thao tác relation. Các operation cơ bản:

Selection `σ` chọn row theo predicate. Projection `π` chọn column. Union hợp relation compatible. Difference lấy tuple ở A không có trong B. Cartesian Product ghép mọi tuple A với mọi tuple B. Join kết hợp tuple liên quan theo condition. Division thường dùng cho query dạng “đối tượng thỏa **tất cả** điều kiện trong một tập”.

Bẫy: Selection liên quan **row**, Projection liên quan **column**.

## 4. Functional Dependency và Normalization

### 4.1 Functional Dependency

`X → Y` nghĩa nếu hai tuple có cùng X thì phải có cùng Y. X functionally determines Y.

Full Functional Dependency nghĩa Y phụ thuộc toàn bộ composite key, không phụ thuộc chỉ một phần. Partial Dependency là phụ thuộc vào một phần composite key. Transitive Dependency xảy ra khi key → A và A → B, khiến B phụ thuộc gián tiếp key qua non-key attribute.

### 4.2 Anomaly

Unnormalized/redundant design có thể gây:

- Insert Anomaly: không thể insert một fact nếu thiếu fact khác không liên quan.
- Update Anomaly: cùng fact lặp nhiều row, update không đồng bộ.
- Delete Anomaly: xóa một row vô tình mất fact khác.

Normalization giảm anomaly bằng decomposition có lý do.

### 4.3 1NF

1NF yêu cầu attribute value mang tính atomic theo relational design đang xét; không có repeating group/list đa trị trong một cell theo cách thiết kế chuẩn.

### 4.4 2NF

2NF = 1NF + không có partial dependency của non-prime attribute lên một phần candidate key.

2NF đặc biệt đáng chú ý khi key là composite. Nếu primary/candidate key chỉ một attribute thì partial dependency theo key đó không xảy ra.

### 4.5 3NF

3NF loại transitive dependency không phù hợp giữa key và non-key attribute. Một formulation chính xác hơn với FD `X → A`: relation ở 3NF nếu X là superkey hoặc A là prime attribute, sau khi đã ở mức normalization phù hợp.

### 4.6 BCNF

BCNF mạnh hơn 3NF: với mọi non-trivial FD `X → Y`, X phải là superkey.

Một relation có thể đạt 3NF nhưng chưa BCNF khi determinant không phải superkey nhưng dependent là prime attribute.

### 4.7 4NF và 5NF

4NF xử lý non-trivial multivalued dependency khi determinant không phải superkey. 5NF xử lý join dependency phức tạp. Chúng ít xuất hiện hơn nhưng cần biết category để không nhầm với FD thông thường.

### 4.8 Lossless Join và Dependency Preservation

Decomposition tốt cần ưu tiên lossless join — join các relation con phải tái tạo đúng relation gốc, không sinh tuple giả. Dependency preservation nghĩa các dependency quan trọng có thể enforce mà không phải join relation phức tạp.

## 5. 물리 데이터베이스 설계 — Physical Database Design

Logical design nói **data có ý nghĩa và quan hệ gì**; physical design nói **lưu và truy cập thế nào**.

### 5.1 Index

Index tăng tốc lookup nhưng tốn storage và tăng cost khi insert/update/delete.

B-Tree giữ key/data pointer theo cấu trúc balanced tree. B+Tree thường lưu record/data pointer ở leaf, internal node chủ yếu giữ search key; leaf thường linked giúp range scan hiệu quả.

Hash index rất tốt cho equality lookup nhưng không tự nhiên cho range query vì hash phá ordering.

### 5.2 Clustered vs Non-clustered

Khái niệm cụ thể phụ thuộc DBMS, nhưng ý chung: clustered organization/index ảnh hưởng cách row được sắp/bố trí gần theo key; non-clustered index là structure riêng trỏ tới row. Một table thường không thể có nhiều physical clustering order độc lập.

### 5.3 Partitioning

Horizontal Partitioning chia row. Vertical Partitioning chia column. Range, Hash, List và Composite Partitioning là các chiến lược phổ biến.

Partitioning có thể tăng manageability/performance nhưng không thay normalization; đây là physical/logical scaling decision khác loại.

### 5.4 Denormalization

Denormalization cố ý thêm redundancy để tối ưu read/performance sau khi hiểu rõ consistency cost. Nó không phải “thiết kế sai” nếu được kiểm soát, nhưng làm tăng burden đồng bộ dữ liệu.

## 6. SQL 기본 — DDL, DML, DCL, TCL

### 6.1 DDL

CREATE, ALTER, DROP thường thuộc Data Definition Language. Constraint như PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, NOT NULL giúp enforce integrity.

### 6.2 DML

SELECT, INSERT, UPDATE, DELETE thao tác data. Một số classification gọi SELECT riêng là DQL, nhưng trong nhiều giáo trình vẫn nhóm trong DML/query language; đọc đúng taxonomy của đề.

### 6.3 DCL/TCL

GRANT, REVOKE liên quan privilege và thường xếp DCL. COMMIT, ROLLBACK, SAVEPOINT liên quan transaction control.

## 7. SQL Query Reasoning

### 7.1 WHERE vs HAVING

WHERE lọc row trước grouping. HAVING lọc group sau GROUP BY/aggregation.

Ví dụ: muốn department có AVG(salary) > 5000 thì condition aggregate đặt ở HAVING.

### 7.2 JOIN

INNER JOIN chỉ giữ match. LEFT OUTER JOIN giữ mọi row bên trái và NULL phía phải nếu không match. RIGHT OUTER JOIN tương tự phía phải. FULL OUTER JOIN giữ mọi row hai bên nếu DBMS hỗ trợ.

CROSS JOIN tạo Cartesian product. SELF JOIN là table join với chính nó qua alias.

### 7.3 NULL

NULL không bằng 0 và không bằng empty string. So sánh với NULL dùng `IS NULL` / `IS NOT NULL`, không dùng `= NULL`.

Trong SQL three-valued logic, expression với NULL có thể cho UNKNOWN; điều này ảnh hưởng WHERE filtering.

### 7.4 Aggregate

COUNT(*) đếm row. COUNT(column) bỏ NULL ở column đó. SUM/AVG thường bỏ NULL input. GROUP BY nhóm row theo key.

### 7.5 Subquery

Scalar subquery trả một value. Single-row/multi-row subquery cần operator phù hợp. `IN`, `EXISTS`, `ANY/SOME`, `ALL` có semantics khác nhau.

EXISTS kiểm tra sự tồn tại row từ subquery, thường không quan tâm value cụ thể trong SELECT list.

### 7.6 Set Operations

UNION loại duplicate. UNION ALL giữ duplicate. INTERSECT lấy phần giao. EXCEPT/MINUS lấy difference tùy DBMS.

## 8. View, Index, Procedure, Trigger

View là virtual relation dựa query; có thể dùng abstraction/security nhưng updateability phụ thuộc definition/DBMS.

Stored Procedure đóng gói procedural logic chạy trong DB server. Trigger tự động chạy khi event được định nghĩa xảy ra. Trigger tiện cho audit/integrity nhưng quá nhiều hidden behavior có thể khó maintain.

Index là access structure, không phải copy logical table đầy đủ theo nghĩa view/materialization.

## 9. Transaction

### 9.1 ACID

Atomicity: all-or-nothing. Consistency: transaction đưa DB từ state hợp lệ sang state hợp lệ theo constraint. Isolation: concurrent transaction không gây interference vượt mức isolation cho phép. Durability: committed data survive failure phù hợp guarantee của system.

### 9.2 Concurrency anomalies

Dirty Read: đọc data chưa commit từ transaction khác. Non-repeatable Read: cùng row đọc hai lần thấy value khác do transaction khác commit update. Phantom Read: cùng predicate query hai lần thấy tập row thay đổi do insert/delete phù hợp predicate.

Lost Update: hai transaction update cùng data và một update bị overwrite theo race pattern.

### 9.3 Isolation Levels

Theo mô hình SQL kinh điển:

- Read Uncommitted cho phép nhiều anomaly nhất.
- Read Committed ngăn dirty read.
- Repeatable Read ngăn dirty read và non-repeatable read; phantom behavior phụ thuộc implementation/standard interpretation.
- Serializable mạnh nhất về semantics tuần tự.

Đừng biến bảng này thành tuyệt đối cho mọi DBMS; engine có MVCC/locking implementation khác nhau. Trong đề lý thuyết, bám semantics chuẩn.

## 10. Locking và Serializability

Shared Lock cho read, Exclusive Lock cho write trong mô hình lock cơ bản. Nhiều shared lock có thể cùng tồn tại; exclusive lock xung đột với lock khác tùy matrix.

Two-Phase Locking — 2PL — có growing phase chỉ acquire lock và shrinking phase release lock, giúp conflict serializability trong mô hình kinh điển.

Strict 2PL thường giữ exclusive lock tới commit/abort để tránh cascading rollback và tăng recoverability.

### 10.1 Deadlock

Deadlock có thể xảy ra khi transaction chờ vòng tròn resource/lock. Điều kiện Coffman quen thuộc: mutual exclusion, hold and wait, no preemption, circular wait.

Giải pháp có thể prevention, avoidance, detection + recovery, timeout. Wait-for graph dùng để detect cycle trong lock wait relation.

## 11. Recovery

### 11.1 Log và WAL

Write-Ahead Logging — WAL — yêu cầu log record cần thiết được ghi persistent trước khi data page tương ứng được ghi theo protocol. Log cho phép REDO/UNDO sau failure.

### 11.2 Checkpoint

Checkpoint giảm lượng log phải scan/reprocess khi recovery bằng cách ghi mốc trạng thái cần thiết. Nó không có nghĩa xóa mọi log trước checkpoint trong mọi system.

### 11.3 Undo / Redo

UNDO đảo thay đổi của transaction chưa commit. REDO áp lại thay đổi committed chưa phản ánh đầy đủ trên disk. Cần hiểu relation với buffer policy như steal/no-steal và force/no-force ở mức khái niệm.

## 12. 데이터 전환 — Data Migration / Conversion

Data conversion gồm analysis nguồn/đích, mapping, cleansing, transformation, extraction/load, validation và reconciliation.

Một migration thành công không chỉ là “copy đủ row”. Phải kiểm tra datatype, encoding, key relation, nullability, business rule, duplicate, referential integrity và aggregate/control total.

ETL: Extract → Transform → Load. ELT: Extract → Load → Transform, phổ biến khi target platform có compute mạnh. Trong kỳ thi truyền thống ETL thường gặp hơn, nhưng hiểu cả hai giúp không nhầm.

## 13. Cặp dễ nhầm

| Cặp | Điểm tách |
|---|---|
| External/Conceptual/Internal Schema | user view / global logical / physical storage |
| Super Key vs Candidate Key | unique có thể thừa / minimal unique |
| Selection vs Projection | row / column |
| Partial vs Transitive Dependency | một phần composite key / qua non-key intermediate |
| 3NF vs BCNF | cho phép một số FD với prime attribute / determinant phải superkey |
| B+Tree vs Hash Index | range/order tốt / equality tốt |
| WHERE vs HAVING | row trước grouping / group sau aggregation |
| COUNT(*) vs COUNT(col) | mọi row / bỏ NULL col |
| Dirty vs Non-repeatable vs Phantom | uncommitted value / changed row / changed row set |
| Shared vs Exclusive Lock | read sharing / write exclusive |
| UNDO vs REDO | rollback uncommitted / reapply committed |
| Normalization vs Partitioning | logical redundancy / physical distribution |

## 14. Procedural drills

### Drill 1 — Key

Relation `ENROLL(StudentId, CourseId, StudentName, CourseName, Grade)` có key `(StudentId, CourseId)`. Xác định partial dependency và đề xuất decomposition tới 2NF.

### Drill 2 — 3NF

Nếu `EmployeeId → DeptId` và `DeptId → DeptName`, vì sao `DeptName` tạo transitive dependency trong relation Employee?

### Drill 3 — Relational Algebra

Muốn lấy chỉ `name` của employee có salary > 5000, operation nào phải xảy ra về mặt logic: Selection và Projection theo thứ tự nào?

### Drill 4 — SQL

Viết query tìm department có ít nhất 5 employee và average salary > 5000. Giải thích condition nào nằm WHERE và condition nào nằm HAVING nếu thêm `status='ACTIVE'`.

### Drill 5 — NULL

Giải thích vì sao `WHERE bonus = NULL` không tìm được row như mong đợi và phải sửa thành gì.

### Drill 6 — Isolation

T1 đọc balance=100. T2 update balance=120 và commit. T1 đọc lại cùng row thấy 120. Đây là anomaly nào?

### Drill 7 — Phantom

T1 query `salary > 5000` thấy 10 row. T2 insert một employee salary 6000 và commit. T1 chạy lại thấy 11 row. Đây là gì?

### Drill 8 — Deadlock

T1 giữ lock A chờ B; T2 giữ B chờ A. Vẽ wait-for graph và xác định cycle.

### Drill 9 — Index

Query chủ yếu là `WHERE created_at BETWEEN ...` và ORDER BY created_at. Tại sao B+Tree thường tự nhiên hơn hash index?

### Drill 10 — Migration

Source có 100.000 row, target cũng 100.000 row nhưng 2% foreign key invalid. Vì sao row count match chưa đủ để xác nhận migration?

## 15. 과락 방지 checklist — Môn 3

Phải tự làm được:

- phân biệt 3 schema và data independence;
- tìm candidate/primary/foreign/composite key;
- giải Selection, Projection, Join, Division ở mức ý nghĩa;
- nhận diện functional, partial, transitive dependency;
- normalize scenario tới ít nhất 3NF/BCNF ở mức bài cơ bản;
- phân biệt B/B+Tree, hash, partitioning, denormalization;
- viết/đọc SELECT, JOIN, GROUP BY, HAVING, subquery, set operation;
- giải NULL semantics và aggregate;
- phân loại DDL/DML/DCL/TCL;
- phân biệt view/index/procedure/trigger;
- giải ACID, anomaly và isolation;
- phân biệt shared/exclusive lock, 2PL, deadlock;
- hiểu WAL, checkpoint, UNDO/REDO;
- mô tả flow data migration và validation.

Nếu normalization, SQL và transaction chỉ “nhìn quen” nhưng không tự suy luận được, Môn 3 vẫn còn rủi ro cao.
