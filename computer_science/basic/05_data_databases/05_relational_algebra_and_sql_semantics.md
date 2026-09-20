# Relational algebra và SQL semantics

SQL thường được học bằng syntax: `SELECT`, `JOIN`, `GROUP BY`. Nhưng database không “chạy từng dòng câu SQL từ trái sang phải”. Để hiểu đúng query, cần nhìn relational model và relational algebra (관계 대수) phía dưới: một query mô tả **quan hệ kết quả mong muốn**, còn optimizer có quyền chọn nhiều execution plans miễn chúng giữ semantics tương đương.

## Relation không chỉ là bảng giao diện

Trong relational model, relation là một tập tuples theo schema. Table implementation có row order vật lý, pages, indexes và metadata, nhưng relational semantics không cam kết order nếu không có `ORDER BY`.

Đây là lý do query trả rows “có vẻ cùng thứ tự” nhiều lần vẫn không tạo guarantee.

## Core relational operations

Selection lọc tuples theo predicate; projection chọn attributes; join kết hợp tuples theo condition; union/difference kết hợp relations; rename thay tên để tránh ambiguity.

SQL mở rộng model với duplicates, `NULL`, aggregation, ordering và procedural extensions. Vì vậy SQL không phải relational algebra thuần, nhưng algebra vẫn là mental model rất mạnh cho optimization.

## Join không phải chỉ một keyword

Một inner join về logic tạo các pairs thỏa predicate. Nhưng physical execution có thể là nested-loop join, hash join hoặc sort-merge join.

Same semantics, different mechanism. Đây là nguyên tắc cốt lõi của declarative language: user nói **what**, engine chọn **how**.

Outer joins thêm unmatched rows và `NULL` padding, làm algebraic rewrites phức tạp hơn. Predicate pushdown qua outer join không phải lúc nào cũng semantics-preserving.

## Three-valued logic của NULL

SQL predicate không chỉ TRUE/FALSE mà còn UNKNOWN khi `NULL` tham gia nhiều comparisons.

`NULL = NULL` không TRUE; nó là UNKNOWN. `WHERE` chỉ giữ rows có predicate TRUE, nên UNKNOWN bị loại.

Đây là lý do `NOT IN` có thể gây bất ngờ nếu subquery chứa NULL. `NOT EXISTS` thường biểu đạt anti-join semantics rõ hơn.

## Logical query processing order

Một mental model hữu ích cho SQL query:

```text
FROM / JOIN
WHERE
GROUP BY
HAVING
SELECT
DISTINCT
ORDER BY
LIMIT/OFFSET
```

Đây là logical semantics, không phải physical execution order. Optimizer có thể push predicates xuống index scan hoặc reorder joins nếu bảo toàn kết quả.

Hiểu distinction này giải thích tại sao alias trong `SELECT` có thể chưa usable ở một số clauses nhưng usable ở `ORDER BY`.

## Aggregation biến cardinality

`GROUP BY` partition rows thành groups rồi aggregate mỗi group. Aggregate functions có semantics riêng với NULL; `COUNT(*)` đếm rows, `COUNT(column)` bỏ NULL values.

Aggregation không chỉ “tính tổng”; nó đổi granularity của relation. Sau grouping, columns ngoài group keys phải được aggregate hoặc xác định theo rules của DBMS.

## Window functions không collapse rows

Window function tính trên một window liên quan nhưng giữ mỗi input row. `ROW_NUMBER`, `RANK`, running sum và moving average vì vậy khác `GROUP BY`.

Mental model: aggregate query thay nhiều rows bằng một row/group; window function thêm context-derived values vào từng row.

## Set semantics và bag semantics

Relational theory thường nói sets, nhưng SQL tables/query results mặc định gần bag/multiset: duplicates được giữ trừ khi dùng `DISTINCT` hoặc set operator có duplicate elimination.

Duplicate elimination cần sort/hash và có cost. `UNION ALL` tránh bước này nếu semantics cho phép.

## Functional dependencies và query reasoning

Functional dependency giúp hiểu khi một attribute được xác định bởi key. Đây là nền của normalization nhưng cũng liên quan grouping, uniqueness constraints và optimizer assumptions.

Constraint khai báo đúng không chỉ bảo vệ data; nó còn cung cấp facts để optimizer có thể loại join hoặc estimate cardinality tốt hơn trong một số engines.

## Common Misconceptions

**“SQL chạy từ SELECT xuống dưới vì ta viết như vậy.”** Logical order khác textual order và physical plan lại khác cả hai.

**“JOIN luôn tạo Cartesian product rồi filter.”** Đó là relational equivalence, không phải yêu cầu implementation.

**“NULL là một value đặc biệt.”** SQL NULL biểu diễn missing/unknown marker với three-valued logic; coi nó như ordinary value dẫn tới bugs.

## Mental Model

> SQL là declarative specification trên relations. Để reasoning đúng, tách ba tầng: relational meaning, SQL-specific semantics và physical execution plan.

## Kết nối

Đọc cùng [relational model/normalization](./01_relational_model_keys_and_normalization.md), [query execution/indexes](./03_indexes_and_query_execution.md) và [query optimization](./06_query_optimization_and_execution_plans.md).