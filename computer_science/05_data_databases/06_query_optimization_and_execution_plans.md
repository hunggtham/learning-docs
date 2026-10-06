# Truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화) và thực thi (execution / 실행) plans

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Query optimization và execution plans**. Route đi từ logical query → cardinality/statistics → join order/operators → SARGability/index-only scan → EXPLAIN và parameter sensitivity, để plan được kiểm chứng bằng chi phí thực tế.

Hai SQL queries có thể trả cùng kết quả nhưng thời gian chạy (runtime / 런타임) chênh hàng nghìn lần. cơ sở dữ liệu (database / 데이터베이스) optimizer (옵티마이저) giải bài toán tìm vật lý (physical / 물리적) plan có estimated chi phí (cost / 비용) thấp trong không gian plans rất lớn. Đây là nơi algorithms, statistics, lưu trữ (storage / 저장소), CPU bộ nhớ đệm (cache / 캐시) và relational algebra gặp nhau.

## Từ truy vấn (query / 쿼리) văn bản (text / 텍스트) đến vật lý (physical / 물리적) plan

Chuỗi xử lý (pipeline / 파이프라인) khái quát:

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

Optimizer không “hiểu nghiệp vụ (business / 비즈니스) meaning”; nó dựa vào lược đồ (schema / 스키마), các ràng buộc (constraints / 제약조건들), statistics và chi phí (cost / 비용) mô hình (model / 모델).

> **Nối mạch:** Optimizer biến query text thành physical plan; cardinality estimation cung cấp cost signal, còn join-order explosion buộc hệ thống dùng search/pruning thay vì thử mọi khả năng.

## Cardinality estimation là trái tim của chi phí (cost / 비용) mô hình (model / 모델)

Nếu optimizer đoán một filter trả 10 rows nhưng thực tế 10 triệu, phép nối (join / 조인) thứ tự (order / 순서) và phép nối (join / 조인) thuật toán (algorithm / 알고리즘) có thể sai hoàn toàn.

Statistics thường gồm row count, number of distinct values, histograms, null fraction và đôi khi extended/multi-column statistics.

Giả định (assumption / 가정) independence giữa columns thường sai. `city='Seoul'` và `country='KR'` có correlation mạnh; multiply selectivities độc lập có thể underestimate/overestimate.

> **Nối mạch:** **Phép nối (join / 조인) thứ tự (order / 순서) explosion** nối từ **Cardinality estimation là trái tim của chi phí (cost / 비용) mô hình (model / 모델)** sang **Vật lý (physical / 물리적) operators**, vì cơ chế trước tạo đầu vào cho bước sau.

## Phép nối (join / 조인) thứ tự (order / 순서) explosion

Với nhiều tables, số possible phép nối (join / 조인) orders tăng cực nhanh. Exhaustive tìm kiếm (search / 검색) sớm trở nên infeasible, nên optimizers dùng động (dynamic / 동적) programming cho small phép nối (join / 조인) sets, heuristics hoặc restricted tìm kiếm (search / 검색) spaces.

Phép nối (join / 조인) associativity cho phép `(A join B) join C` và `A join (B join C)` tương đương với inner joins dưới conditions phù hợp, tạo tối ưu hóa (optimization / 최적화) freedom.

Outer joins, lateral dependencies và volatile functions giảm freedom này.

> **Nối mạch:** **Vật lý (physical / 물리적) operators** nối từ **Phép nối (join / 조인) thứ tự (order / 순서) explosion** sang **SARGability**, vì cơ chế trước tạo đầu vào cho bước sau.

## Vật lý (physical / 물리적) operators

Nested-loop phép nối (join / 조인) phù hợp khi outer nhỏ và inner có chỉ mục (index / 인덱스) selective. băm (hash / 해시) phép nối (join / 조인) tốt cho equality phép nối (join / 조인) khi bản dựng (build / 빌드) side vừa bộ nhớ (memory / 메모리). Sort-merge phép nối (join / 조인) hữu ích khi inputs đã sorted hoặc sort có giá trị cho downstream.

Sequential scan có thể nhanh hơn chỉ mục (index / 인덱스) scan khi truy vấn (query / 쿼리) cần phần lớn bảng (table / 테이블), vì random page fetch + lookup overhead vượt lợi ích chỉ mục (index / 인덱스).

Không có operator “tốt nhất”; phù hợp phụ thuộc cardinality, thứ tự (ordering / 순서), bộ nhớ (memory / 메모리) và lưu trữ (storage / 저장소).

> **Nối mạch:** **SARGability** nối từ **Vật lý (physical / 물리적) operators** sang **Covering chỉ mục (index / 인덱스) và index-only scan**, vì cơ chế trước tạo đầu vào cho bước sau.

## SARGability

Predicate search-argument-able cho phép chỉ mục (index / 인덱스) truy cập (access / 접근) hiệu quả hơn. Ví dụ `WHERE created_at >= ?` thường index-friendly hơn `WHERE function(created_at) = ?` nếu DB không có expression chỉ mục (index / 인덱스) tương ứng.

Concept quan trọng là transformation của column có thể làm chỉ mục (index / 인덱스) key thứ tự (order / 순서) không còn usable trực tiếp.

> **Nối mạch:** **Covering chỉ mục (index / 인덱스) và index-only scan** nối từ **SARGability** sang **Sort, spill và bộ nhớ (memory / 메모리) grants**, vì cơ chế trước tạo đầu vào cho bước sau.

## Covering chỉ mục (index / 인덱스) và index-only scan

Nếu chỉ mục (index / 인덱스) chứa đủ columns truy vấn (query / 쿼리) cần, engine có thể tránh bảng (table / 테이블) lookup cho nhiều rows. Điều này đổi random I/O mẫu (pattern / 패턴) đáng kể.

Nhưng chỉ mục (index / 인덱스) rộng tăng lưu trữ (storage / 저장소) và ghi (write / 쓰기) amplification. Mỗi INSERT/cập nhật (update / 업데이트) phải maintain indexes, nên read tối ưu hóa (optimization / 최적화) có ghi (write / 쓰기) chi phí (cost / 비용).

> **Nối mạch:** **Sort, spill và bộ nhớ (memory / 메모리) grants** nối từ **Covering chỉ mục (index / 인덱스) và index-only scan** sang **EXPLAIN như bằng chứng (evidence / 증거), không phải decoration**, vì cơ chế trước tạo đầu vào cho bước sau.

## Sort, spill và bộ nhớ (memory / 메모리) grants

Sort/băm (hash / 해시) operators cần bộ nhớ (memory / 메모리). Nếu dataset vượt allocation, engine spill ra temporary lưu trữ (storage / 저장소) và độ trễ (latency / 지연 시간) tăng mạnh.

Truy vấn (query / 쿼리) chậm đột biến khi dữ liệu (data / 데이터) kích thước (size / 크기) vượt bộ nhớ (memory / 메모리) threshold là ví dụ phase thay đổi (change / 변경): cùng plan nhưng vật lý (physical / 물리적) hành vi (behavior / 동작) khác vì tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건).

> **Nối mạch:** **Sort, spill và bộ nhớ (memory / 메모리) grants** đặt vấn đề; **EXPLAIN như bằng chứng (evidence / 증거), không phải decoration** kiểm tra bằng chứng, rồi **Parameter sensitivity** mở rộng hệ quả.

## EXPLAIN như bằng chứng (evidence / 증거), không phải decoration

Thực thi (execution / 실행) plan cho thấy operator cây (tree / 트리), estimated rows/chi phí (cost / 비용) và trong `ANALYZE` chế độ (mode / 모드) có thể có actual rows/thời gian (time / 시간).

Một debugging đường dẫn (path / 경로) tốt là tìm nơi estimates lệch actual lớn, xem truy cập (access / 접근) đường dẫn (path / 경로), phép nối (join / 조인) thứ tự (order / 순서), filters, sorts/spills rồi mới quyết định chỉ mục (index / 인덱스)/rewrite/statistics.

Không nên tối ưu bằng cách đoán chỉ từ SQL văn bản (text / 텍스트).

> **Nối mạch:** **EXPLAIN như bằng chứng (evidence / 증거), không phải decoration** đặt vấn đề; **Parameter sensitivity** kiểm tra bằng chứng, rồi **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả.

## Parameter sensitivity

Một prepared truy vấn (query / 쿼리) có thể nhận values có selectivity rất khác. Plan tốt cho dùng chung (common / 공통) giá trị (value / 값) có thể tệ cho rare giá trị (value / 값) hoặc ngược lại. DBMSs có mechanisms khác nhau cho parameter sniffing, generic/custom plans hoặc adaptive plans.

Điều này cho thấy “một truy vấn (query / 쿼리) = một optimal plan” không luôn đúng trên changing parameters.

> **Nối mạch:** **Dùng chung (common / 공통) Misconceptions** nối từ **Parameter sensitivity** sang **Mô hình tư duy (mental model / 사고 모델)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Dùng chung (common / 공통) Misconceptions

**“Có chỉ mục (index / 인덱스) thì cơ sở dữ liệu (database / 데이터베이스) sẽ dùng.”** Optimizer có thể đúng khi không dùng nếu scan rẻ hơn.

**“chi phí (cost / 비용) trong EXPLAIN là milliseconds.”** Thường là nội bộ (internal / 내부) chi phí (cost / 비용) units, không phải wall-clock trực tiếp.

**“Rewrite SQL đẹp hơn luôn nhanh hơn.”** Optimizer có thể normalize chúng về cùng plan; phải kiểm tra actual plan.

> **Nối mạch:** **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Dùng chung (common / 공통) Misconceptions**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

> truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화) là tìm kiếm (search / 검색) dưới bất định (uncertainty / 불확실성): optimizer dùng statistics để dự đoán cardinality, từ đó chọn operators có chi phí (cost / 비용) mô hình (model / 모델) phù hợp. Sai estimate thường kéo theo sai plan.

> **Nối mạch:** **Kết nối** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc cùng [SQL semantics](./05_relational_algebra_and_sql_semantics.md), [indexes/query execution](./03_indexes_and_query_execution.md), [storage hardware](../02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) và [software performance](../08_software_systems/02_performance_capacity_and_scalability.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
