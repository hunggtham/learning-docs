# Relational model, keys và normalization

Relational model do Edgar F. Codd đề xuất tách logical data relationships khỏi pointer/navigation physical storage. Ý tưởng cốt lõi: dữ liệu được mô tả bằng relations và queries dựa values/relations thay vì application phải biết record nằm ở block hay nối bằng pointer nào.

## Relation, tuple và attribute

Trong model lý tưởng, relation là tập tuples cùng attributes. SQL table gần relation nhưng có differences: SQL thường là bag/multiset trừ khi DISTINCT; NULL thêm three-valued logic; row ordering không được guarantee nếu thiếu ORDER BY.

Attribute có domain — tập giá trị hợp lệ. Schema đặt types và constraints để approximate domain.

## Keys từ identity và functional dependency

Superkey là tập attributes xác định duy nhất tuple. Candidate key là superkey tối thiểu. Primary key là candidate key được chọn làm identifier chính trong schema; alternate keys vẫn có thể UNIQUE.

Surrogate key như generated ID không làm natural uniqueness biến mất. Nếu business nói email+tenant phải unique, vẫn cần constraint phù hợp dù có numeric primary key.

Functional dependency `X → Y` nghĩa nếu hai tuples có cùng X thì phải cùng Y. Đây là foundation của normalization.

## Foreign key

Foreign key encode referential integrity: child value phải reference existing parent candidate/primary key theo rules, hoặc NULL nếu allowed. Delete/update policy có RESTRICT, CASCADE, SET NULL... tùy semantics.

Cascade tiện nhưng có thể tạo large implicit effects; cần hiểu graph relationships và transaction scope.

## Tại sao normalization tồn tại?

Giả sử một table lặp customer address trên mỗi order. Update address phải sửa nhiều rows; bỏ order cuối có thể mất customer info; thêm customer chưa có order khó biểu diễn. Đây là update/delete/insert anomalies.

Normalization decomposition tách facts theo dependencies để mỗi fact có một home rõ, giảm redundancy gây inconsistency.

## 1NF, 2NF, 3NF và BCNF bằng bản chất

1NF trong practical SQL teaching thường yêu cầu attributes atomic theo chosen relational representation, không repeating groups. “Atomic” phụ thuộc domain; JSON document có thể là một scalar value trong DB nhưng relational decomposition khác.

2NF loại partial dependency của non-key attribute trên một phần composite candidate key. Nó chỉ relevant khi candidate key composite.

3NF loại certain transitive dependencies của non-key attributes qua non-key determinants, nhằm để non-key facts phụ thuộc key đúng place.

BCNF mạnh hơn: với mọi non-trivial FD `X→Y`, X phải là superkey. Một số schemas đạt 3NF nhưng không BCNF để preserve dependencies hoặc vì practical trade-off.

Normalization không phải ritual đếm forms; nó là reasoning “fact này phụ thuộc identifier nào?”.

## Denormalization

Denormalization intentional duplicate/precompute để giảm joins hoặc support analytics. Nó không “ngược quy tắc” nếu trade-off explicit và consistency mechanism tồn tại.

Materialized view, cache, search index đều là derived/duplicated state. Câu hỏi là source of truth và refresh consistency.

## NULL và three-valued logic

SQL NULL thường biểu diễn unknown/missing/not applicable tùy design, nhưng semantics tạo UNKNOWN trong comparisons. `NULL = NULL` không TRUE; dùng `IS NULL`. `WHERE` giữ rows predicate TRUE, loại FALSE và UNKNOWN.

`NOT IN` với subquery chứa NULL có thể gây kết quả bất ngờ vì UNKNOWN propagation. Đây là chỗ logical model và SQL semantics cần phân biệt.

## Relational algebra intuition

Selection lọc rows; projection chọn attributes; join kết hợp tuples theo predicate; union/difference/set operations compose relations. SQL optimizer có thể reorder equivalent operations khi semantics cho phép, như push predicate trước join để giảm intermediate data.

## Mental Model

> Relational design là **phân bố facts theo dependencies**. Key trả lời “fact thuộc entity/identity nào”; normalization giảm việc cùng một fact phải được cập nhật ở nhiều nơi.

## Common Misconceptions

**“Primary key phải là auto-increment integer.”** Đây chỉ là implementation/design choice; key concept rộng hơn.

**“3NF luôn là schema tối ưu.”** Workload, constraints và read models có thể justify denormalization; integrity trade-off phải explicit.

**“NULL là empty string/zero.”** Không; NULL có special semantics và three-valued logic.

## Kết nối

[Logic/invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md) giúp hiểu constraints. [Indexes](./03_indexes_and_query_execution.md) là physical acceleration không thay logical normalization. [Transactions](./02_transactions_acid_and_concurrency_control.md) giữ multiple related writes atomic.
