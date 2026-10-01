# Relational algebra và SQL ngữ nghĩa (semantics / 의미론)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Quan hệ (relation / 관계) không chỉ là bảng giao diện** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Cốt lõi (core / 핵심) relational operations** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

SQL thường được học bằng cú pháp (syntax / 문법): `SELECT`, `JOIN`, `GROUP BY`. Nhưng cơ sở dữ liệu (database / 데이터베이스) không “chạy từng dòng câu SQL từ trái sang phải”. Để hiểu đúng truy vấn (query / 쿼리), cần nhìn relational mô hình (model / 모델) và relational algebra (관계 대수) phía dưới: một truy vấn (query / 쿼리) mô tả **quan hệ kết quả mong muốn**, còn optimizer có quyền chọn nhiều thực thi (execution / 실행) plans miễn chúng giữ ngữ nghĩa (semantics / 의미론) tương đương.

## Quan hệ (relation / 관계) không chỉ là bảng giao diện

Trong relational mô hình (model / 모델), quan hệ (relation / 관계) là một tập tuples theo lược đồ (schema / 스키마). bảng (table / 테이블) hiện thực (implementation / 구현) có row thứ tự (order / 순서) vật lý, pages, indexes và siêu dữ liệu (metadata / 메타데이터), nhưng relational ngữ nghĩa (semantics / 의미론) không cam kết thứ tự (order / 순서) nếu không có `ORDER BY`.

Đây là lý do truy vấn (query / 쿼리) trả rows “có vẻ cùng thứ tự” nhiều lần vẫn không tạo guarantee.

> **Chuyển mạch:** Trong **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Cốt lõi (core / 핵심) relational operations** tiếp nhận điểm tựa từ **Quan hệ (relation / 관계) không chỉ là bảng giao diện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phép nối (join / 조인) không phải chỉ một từ khóa (keyword / 키워드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cốt lõi (core / 핵심) relational operations

Selection lọc tuples theo predicate; projection chọn attributes; phép nối (join / 조인) kết hợp tuples theo điều kiện (condition / 조건); union/difference kết hợp relations; rename thay tên để tránh ambiguity.

SQL mở rộng mô hình (model / 모델) với duplicates, `NULL`, aggregation, thứ tự (ordering / 순서) và procedural extensions. Vì vậy SQL không phải relational algebra thuần, nhưng algebra vẫn là mô hình tư duy (mental model / 사고 모델) rất mạnh cho tối ưu hóa (optimization / 최적화).

> **Chuyển mạch:** Ở chặng này của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Phép nối (join / 조인) không phải chỉ một từ khóa (keyword / 키워드)** tiếp nhận điểm tựa từ **Cốt lõi (core / 핵심) relational operations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Three-valued lô-gic (logic / 논리) của NULL** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phép nối (join / 조인) không phải chỉ một từ khóa (keyword / 키워드)

Một inner phép nối (join / 조인) về lô-gic (logic / 논리) tạo các pairs thỏa predicate. Nhưng vật lý (physical / 물리적) thực thi (execution / 실행) có thể là nested-loop phép nối (join / 조인), băm (hash / 해시) phép nối (join / 조인) hoặc sort-merge phép nối (join / 조인).

Same ngữ nghĩa (semantics / 의미론), different cơ chế (mechanism / 메커니즘). Đây là nguyên tắc cốt lõi của declarative ngôn ngữ (language / 언어): người dùng (user / 사용자) nói **what**, engine chọn **how**.

Outer joins thêm unmatched rows và `NULL` padding, làm algebraic rewrites phức tạp hơn. Predicate pushdown qua outer phép nối (join / 조인) không phải lúc nào cũng semantics-preserving.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Three-valued lô-gic (logic / 논리) của NULL** tiếp nhận điểm tựa từ **Phép nối (join / 조인) không phải chỉ một từ khóa (keyword / 키워드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Logical truy vấn (query / 쿼리) processing thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Three-valued lô-gic (logic / 논리) của NULL

SQL predicate không chỉ TRUE/FALSE mà còn UNKNOWN khi `NULL` tham gia nhiều comparisons.

`NULL = NULL` không TRUE; nó là UNKNOWN. `WHERE` chỉ giữ rows có predicate TRUE, nên UNKNOWN bị loại.

Đây là lý do `NOT IN` có thể gây bất ngờ nếu subquery chứa NULL. `NOT EXISTS` thường biểu đạt anti-join ngữ nghĩa (semantics / 의미론) rõ hơn.

> **Chuyển mạch:** Trong **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Three-valued lô-gic (logic / 논리) của NULL** xác định đầu vào; **Logical truy vấn (query / 쿼리) processing thứ tự (order / 순서)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Aggregation biến cardinality** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Logical truy vấn (query / 쿼리) processing thứ tự (order / 순서)

Một mô hình tư duy (mental model / 사고 모델) hữu ích cho SQL truy vấn (query / 쿼리):

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

Đây là logical ngữ nghĩa (semantics / 의미론), không phải vật lý (physical / 물리적) thực thi (execution / 실행) thứ tự (order / 순서). Optimizer có thể push predicates xuống chỉ mục (index / 인덱스) scan hoặc reorder joins nếu bảo toàn kết quả.

Hiểu distinction này giải thích tại sao alias trong `SELECT` có thể chưa usable ở một số clauses nhưng usable ở `ORDER BY`.

> **Chuyển mạch:** Ở chặng này của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Logical truy vấn (query / 쿼리) processing thứ tự (order / 순서)** xác định đầu vào; **Aggregation biến cardinality** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Cửa sổ (window / 윈도우) functions không collapse rows** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Aggregation biến cardinality

`GROUP BY` partition rows thành groups rồi aggregate mỗi group. Aggregate functions có ngữ nghĩa (semantics / 의미론) riêng với NULL; `COUNT(*)` đếm rows, `COUNT(column)` bỏ NULL values.

Aggregation không chỉ “tính tổng”; nó đổi granularity của quan hệ (relation / 관계). Sau grouping, columns ngoài group keys phải được aggregate hoặc xác định theo rules của DBMS.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Cửa sổ (window / 윈도우) functions không collapse rows** tiếp nhận điểm tựa từ **Aggregation biến cardinality** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Set ngữ nghĩa (semantics / 의미론) và bag ngữ nghĩa (semantics / 의미론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cửa sổ (window / 윈도우) functions không collapse rows

Hàm cửa sổ (window function / 윈도우 함수) tính trên một cửa sổ (window / 윈도우) liên quan nhưng giữ mỗi đầu vào (input / 입력) row. `ROW_NUMBER`, `RANK`, running sum và moving average vì vậy khác `GROUP BY`.

Mô hình tư duy (mental model / 사고 모델): aggregate truy vấn (query / 쿼리) thay nhiều rows bằng một row/group; hàm cửa sổ (window function / 윈도우 함수) thêm context-derived values vào từng row.

> **Chuyển mạch:** Trong **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Set ngữ nghĩa (semantics / 의미론) và bag ngữ nghĩa (semantics / 의미론)** tiếp nhận điểm tựa từ **Cửa sổ (window / 윈도우) functions không collapse rows** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Functional dependencies và truy vấn (query / 쿼리) lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Set ngữ nghĩa (semantics / 의미론) và bag ngữ nghĩa (semantics / 의미론)

Relational lý thuyết (theory / 이론) thường nói sets, nhưng SQL tables/truy vấn (query / 쿼리) results mặc định gần bag/multiset: duplicates được giữ trừ khi dùng `DISTINCT` hoặc set operator có duplicate elimination.

Duplicate elimination cần sort/băm (hash / 해시) và có chi phí (cost / 비용). `UNION ALL` tránh bước này nếu ngữ nghĩa (semantics / 의미론) cho phép.

> **Chuyển mạch:** Ở chặng này của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Functional dependencies và truy vấn (query / 쿼리) lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Set ngữ nghĩa (semantics / 의미론) và bag ngữ nghĩa (semantics / 의미론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Functional dependencies và truy vấn (query / 쿼리) lập luận (reasoning / 추론)

Functional phụ thuộc (dependency / 의존성) giúp hiểu khi một attribute được xác định bởi key. Đây là nền của normalization nhưng cũng liên quan grouping, uniqueness các ràng buộc (constraints / 제약조건들) và optimizer các giả định (assumptions / 가정들).

Ràng buộc (constraint / 제약조건) khai báo đúng không chỉ bảo vệ dữ liệu (data / 데이터); nó còn cung cấp facts để optimizer có thể loại phép nối (join / 조인) hoặc estimate cardinality tốt hơn trong một số engines.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Dùng chung (common / 공통) Misconceptions** tiếp nhận điểm tựa từ **Functional dependencies và truy vấn (query / 쿼리) lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“SQL chạy từ SELECT xuống dưới vì ta viết như vậy.”** Logical thứ tự (order / 순서) khác textual thứ tự (order / 순서) và vật lý (physical / 물리적) plan lại khác cả hai.

**“phép nối (join / 조인) luôn tạo Cartesian sản phẩm (product / 제품) rồi filter.”** Đó là relational equivalence, không phải yêu cầu hiện thực (implementation / 구현).

**“NULL là một giá trị (value / 값) đặc biệt.”** SQL NULL biểu diễn missing/unknown marker với three-valued lô-gic (logic / 논리); coi nó như ordinary giá trị (value / 값) dẫn tới bugs.

> **Chuyển mạch:** Trong **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Dùng chung (common / 공통) Misconceptions** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> SQL là declarative specification trên relations. Để lập luận (reasoning / 추론) đúng, tách ba tầng: relational meaning, SQL-specific ngữ nghĩa (semantics / 의미론) và vật lý (physical / 물리적) thực thi (execution / 실행) plan.

> **Chuyển mạch:** Ở chặng này của **Relational algebra và SQL ngữ nghĩa (semantics / 의미론)**, **Kết nối** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Đọc cùng [relational model/normalization](./01_relational_model_keys_and_normalization.md), [query execution/indexes](./03_indexes_and_query_execution.md) và [query optimization](./06_query_optimization_and_execution_plans.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
