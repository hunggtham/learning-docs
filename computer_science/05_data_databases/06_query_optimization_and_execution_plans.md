# Truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화) và thực thi (execution / 실행) plans

> **Mạch đọc:** Đặt **truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화) và thực thi (execution / 실행) plans** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Từ truy vấn (query / 쿼리) văn bản (text / 텍스트) đến vật lý (physical / 물리적) plan** sang **Cardinality estimation là trái tim của chi phí (cost / 비용) mô hình (model / 모델)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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


> **Chuyển mạch:** Từ **Từ truy vấn (query / 쿼리) văn bản (text / 텍스트) đến vật lý (physical / 물리적) plan**, ta sang **Cardinality estimation là trái tim của chi phí (cost / 비용) mô hình (model / 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Cardinality estimation là trái tim của chi phí (cost / 비용) mô hình (model / 모델)

Nếu optimizer đoán một filter trả 10 rows nhưng thực tế 10 triệu, phép nối (join / 조인) thứ tự (order / 순서) và phép nối (join / 조인) thuật toán (algorithm / 알고리즘) có thể sai hoàn toàn.

Statistics thường gồm row count, number of distinct values, histograms, null fraction và đôi khi extended/multi-column statistics.

Giả định (assumption / 가정) independence giữa columns thường sai. `city='Seoul'` và `country='KR'` có correlation mạnh; multiply selectivities độc lập có thể underestimate/overestimate.


> **Chuyển mạch:** Từ **Cardinality estimation là trái tim của chi phí (cost / 비용) mô hình (model / 모델)**, ta sang **phép nối (join / 조인) thứ tự (order / 순서) explosion** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Phép nối (join / 조인) thứ tự (order / 순서) explosion

Với nhiều tables, số possible phép nối (join / 조인) orders tăng cực nhanh. Exhaustive tìm kiếm (search / 검색) sớm trở nên infeasible, nên optimizers dùng động (dynamic / 동적) programming cho small phép nối (join / 조인) sets, heuristics hoặc restricted tìm kiếm (search / 검색) spaces.

Phép nối (join / 조인) associativity cho phép `(A join B) join C` và `A join (B join C)` tương đương với inner joins dưới conditions phù hợp, tạo tối ưu hóa (optimization / 최적화) freedom.

Outer joins, lateral dependencies và volatile functions giảm freedom này.


> **Chuyển mạch:** Từ **phép nối (join / 조인) thứ tự (order / 순서) explosion**, ta sang **vật lý (physical / 물리적) operators** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Vật lý (physical / 물리적) operators

Nested-loop phép nối (join / 조인) phù hợp khi outer nhỏ và inner có chỉ mục (index / 인덱스) selective. băm (hash / 해시) phép nối (join / 조인) tốt cho equality phép nối (join / 조인) khi bản dựng (build / 빌드) side vừa bộ nhớ (memory / 메모리). Sort-merge phép nối (join / 조인) hữu ích khi inputs đã sorted hoặc sort có giá trị cho downstream.

Sequential scan có thể nhanh hơn chỉ mục (index / 인덱스) scan khi truy vấn (query / 쿼리) cần phần lớn bảng (table / 테이블), vì random page fetch + lookup overhead vượt lợi ích chỉ mục (index / 인덱스).

Không có operator “tốt nhất”; phù hợp phụ thuộc cardinality, thứ tự (ordering / 순서), bộ nhớ (memory / 메모리) và lưu trữ (storage / 저장소).


> **Chuyển mạch:** Từ **vật lý (physical / 물리적) operators**, ta sang **SARGability** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## SARGability

Predicate search-argument-able cho phép chỉ mục (index / 인덱스) truy cập (access / 접근) hiệu quả hơn. Ví dụ `WHERE created_at >= ?` thường index-friendly hơn `WHERE function(created_at) = ?` nếu DB không có expression chỉ mục (index / 인덱스) tương ứng.

Concept quan trọng là transformation của column có thể làm chỉ mục (index / 인덱스) key thứ tự (order / 순서) không còn usable trực tiếp.


> **Chuyển mạch:** Từ **SARGability**, ta sang **Covering chỉ mục (index / 인덱스) và index-only scan** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Covering chỉ mục (index / 인덱스) và index-only scan

Nếu chỉ mục (index / 인덱스) chứa đủ columns truy vấn (query / 쿼리) cần, engine có thể tránh bảng (table / 테이블) lookup cho nhiều rows. Điều này đổi random I/O mẫu (pattern / 패턴) đáng kể.

Nhưng chỉ mục (index / 인덱스) rộng tăng lưu trữ (storage / 저장소) và ghi (write / 쓰기) amplification. Mỗi INSERT/cập nhật (update / 업데이트) phải maintain indexes, nên read tối ưu hóa (optimization / 최적화) có ghi (write / 쓰기) chi phí (cost / 비용).


> **Chuyển mạch:** Từ **Covering chỉ mục (index / 인덱스) và index-only scan**, ta sang **Sort, spill và bộ nhớ (memory / 메모리) grants** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Sort, spill và bộ nhớ (memory / 메모리) grants

Sort/băm (hash / 해시) operators cần bộ nhớ (memory / 메모리). Nếu dataset vượt allocation, engine spill ra temporary lưu trữ (storage / 저장소) và độ trễ (latency / 지연 시간) tăng mạnh.

Truy vấn (query / 쿼리) chậm đột biến khi dữ liệu (data / 데이터) kích thước (size / 크기) vượt bộ nhớ (memory / 메모리) threshold là ví dụ phase thay đổi (change / 변경): cùng plan nhưng vật lý (physical / 물리적) hành vi (behavior / 동작) khác vì tài nguyên (resource / 자원) ràng buộc (constraint / 제약조건).


> **Chuyển mạch:** Từ **Sort, spill và bộ nhớ (memory / 메모리) grants**, ta sang **EXPLAIN như bằng chứng (evidence / 증거), không phải decoration** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## EXPLAIN như bằng chứng (evidence / 증거), không phải decoration

Thực thi (execution / 실행) plan cho thấy operator cây (tree / 트리), estimated rows/chi phí (cost / 비용) và trong `ANALYZE` chế độ (mode / 모드) có thể có actual rows/thời gian (time / 시간).

Một debugging đường dẫn (path / 경로) tốt là tìm nơi estimates lệch actual lớn, xem truy cập (access / 접근) đường dẫn (path / 경로), phép nối (join / 조인) thứ tự (order / 순서), filters, sorts/spills rồi mới quyết định chỉ mục (index / 인덱스)/rewrite/statistics.

Không nên tối ưu bằng cách đoán chỉ từ SQL văn bản (text / 텍스트).


> **Chuyển mạch:** Từ **EXPLAIN như bằng chứng (evidence / 증거), không phải decoration**, ta sang **Parameter sensitivity** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Parameter sensitivity

Một prepared truy vấn (query / 쿼리) có thể nhận values có selectivity rất khác. Plan tốt cho dùng chung (common / 공통) giá trị (value / 값) có thể tệ cho rare giá trị (value / 값) hoặc ngược lại. DBMSs có mechanisms khác nhau cho parameter sniffing, generic/custom plans hoặc adaptive plans.

Điều này cho thấy “một truy vấn (query / 쿼리) = một optimal plan” không luôn đúng trên changing parameters.


> **Chuyển mạch:** Từ **Parameter sensitivity**, ta sang **dùng chung (common / 공통) Misconceptions** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Có chỉ mục (index / 인덱스) thì cơ sở dữ liệu (database / 데이터베이스) sẽ dùng.”** Optimizer có thể đúng khi không dùng nếu scan rẻ hơn.

**“chi phí (cost / 비용) trong EXPLAIN là milliseconds.”** Thường là nội bộ (internal / 내부) chi phí (cost / 비용) units, không phải wall-clock trực tiếp.

**“Rewrite SQL đẹp hơn luôn nhanh hơn.”** Optimizer có thể normalize chúng về cùng plan; phải kiểm tra actual plan.


> **Chuyển mạch:** Từ **dùng chung (common / 공통) Misconceptions**, ta sang **mô hình tư duy (mental model / 사고 모델)** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Mô hình tư duy (mental model / 사고 모델)

> truy vấn (query / 쿼리) tối ưu hóa (optimization / 최적화) là tìm kiếm (search / 검색) dưới bất định (uncertainty / 불확실성): optimizer dùng statistics để dự đoán cardinality, từ đó chọn operators có chi phí (cost / 비용) mô hình (model / 모델) phù hợp. Sai estimate thường kéo theo sai plan.


> **Chuyển mạch:** Từ **mô hình tư duy (mental model / 사고 모델)**, ta sang **Kết nối** để mở rộng cùng câu hỏi và dùng kết quả đó để khép lại mạch giải thích.

## Kết nối

Đọc cùng [SQL semantics](./05_relational_algebra_and_sql_semantics.md), [indexes/query execution](./03_indexes_and_query_execution.md), [storage hardware](../02_computer_architecture/06_storage_hardware_ssd_disks_and_persistence.md) và [software performance](../08_software_systems/02_performance_capacity_and_scalability.md).

> **Bàn giao:** Sau **Kết nối**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 data models and database systems](./00_data_models_and_database_systems.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
