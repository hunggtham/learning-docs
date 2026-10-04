# Columnar lưu trữ (storage / 저장소), encoding, pruning và vectorized scans

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Columnar storage, encoding, pruning và vectorized scans**. Route đi từ row/column layout → row groups/encoding → zone maps/Bloom/predicate pushdown → vectorized scan/late materialization → spill và distributed skew, để bandwidth và CPU locality dẫn dắt thiết kế.

Đọc trước [NoSQL, distributed và analytical databases](../../basic/05_data_databases/07_nosql_distributed_and_analytical_databases.md) để có khái niệm OLTP/OLAP, và [join algorithms, vectorized execution, late materialization](./06_join_algorithms_vectorized_execution_and_late_materialization.md) để nối lưu trữ (storage / 저장소) đường dẫn (path / 경로) với thực thi (execution / 실행) engine.

Chapter này tập trung vào một câu hỏi khác B+cây (tree / 트리) hay LSM: **khi tải công việc (workload / 워크로드) đọc rất nhiều rows nhưng chỉ cần một số columns và thường thực hiện aggregate/filter, vật lý (physical / 물리적) bố cục (layout / 레이아웃) nào giảm bytes phải đọc và tăng công việc (work / 작업) hữu ích trên mỗi CPU cycle?**

Mô hình tư duy (mental model / 사고 모델):

```text
logical table
→ row groups / column chunks
→ encoding + compression + metadata
→ pruning / projection
→ decode in vectors
→ predicate / aggregate / join
→ late materialization
→ result
```

## 1. Row store tối ưu locality theo bản ghi (record / 레코드); column store tối ưu locality theo attribute

Trong row-oriented bố cục (layout / 레이아웃), các fields của một row nằm gần nhau. Điều này rất hợp với điểm (point / 지점) lookup hoặc giao dịch (transaction / 트랜잭션) cần đọc/ghi phần lớn bản ghi (record / 레코드).

Trong columnar bố cục (layout / 레이아웃), values của cùng một column được đặt gần nhau. Một truy vấn (query / 쿼리) như:

```sql
SELECT region, SUM(amount)
FROM sales
WHERE event_date >= ...
GROUP BY region;
```

không cần đọc `customer_name`, `shipping_address`, `comment` hoặc nhiều columns khác. Columnar lưu trữ (storage / 저장소) giảm I/O bằng cách chỉ mang các column chunks cần thiết qua lưu trữ (storage / 저장소)/bộ nhớ (memory / 메모리) hierarchy.

Đây là bất biến (invariant / 불변식) hiệu năng (performance / 성능) đầu tiên:

> Không chuyển bytes qua disk → bộ nhớ (memory / 메모리) → bộ nhớ đệm (cache / 캐시) → CPU nếu truy vấn (query / 쿼리) không cần chúng.

> **Nối mạch:** Row store tối ưu theo record, column store theo attribute; row group cân bằng locality với parallelism, rồi encoding/compression biến layout đó thành lợi thế scan và pruning.

## 2. Row group tạo compromise giữa locality và parallelism

Column store thường không lưu “một tệp (file / 파일) cho mỗi column toàn bảng (table / 테이블)” vô hạn. Dữ liệu được chia thành **row groups**, mỗi row group chứa column chunks tương ứng cho một phạm vi (range / 범위) rows.

Row group quá nhỏ làm siêu dữ liệu (metadata / 메타데이터) và seek/object-request overhead tăng. Quá lớn làm pruning thô, bộ nhớ (memory / 메모리) working set lớn và tác vụ (task / 작업) parallelism kém linh hoạt.

Vì vậy row-group kích thước (size / 크기) là sự đánh đổi (trade-off / 트레이드오프) giữa scan efficiency, pruning granularity, compression ratio và scheduling flexibility.

> **Nối mạch:** **3. Encoding và compression không chỉ để tiết kiệm disk** nối từ **2. Row group tạo compromise giữa locality và parallelism** sang **4. Dictionary encoding đổi string comparison thành integer-domain công việc (work / 작업)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Encoding và compression không chỉ để tiết kiệm disk

Values cùng column thường có phân phối (distribution / 분포) thuận lợi cho encoding. Ví dụ categorical string có thể dictionary encode thành integer IDs; sorted integer có thể delta encode; repeated values có thể run-length encode; small domains có thể bit-pack.

Compression đem lại một hiệu ứng quan trọng: **đọc ít bytes hơn có thể nhanh hơn dù CPU phải decode**. Nếu bottleneck nằm ở lưu trữ (storage / 저장소) hoặc bộ nhớ (memory / 메모리) bandwidth, thêm decode compute để giảm bytes có thể tăng overall thông lượng (throughput / 처리량).

Ngược lại, nếu dữ liệu (data / 데이터) đã ở bộ nhớ đệm (cache / 캐시) và decoder quá đắt, compression mạnh hơn chưa chắc nhanh hơn. hiệu năng (performance / 성능) phụ thuộc bottleneck hiện tại.

> **Nối mạch:** **4. Dictionary encoding đổi string comparison thành integer-domain công việc (work / 작업)** nối từ **3. Encoding và compression không chỉ để tiết kiệm disk** sang **5. Zone map/min-max siêu dữ liệu (metadata / 메타데이터) biến scan thành skip**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. Dictionary encoding đổi string comparison thành integer-domain công việc (work / 작업)

Giả sử column `country` chỉ có vài chục values. Thay vì lặp chuỗi dài cho hàng triệu rows, lưu trữ (storage / 저장소) lưu dictionary và chuỗi (sequence / 시퀀스) IDs.

Predicate `country = 'KR'` có thể resolve `'KR'` thành dictionary ID rồi scan integer IDs. Điều này giảm footprint và thường thân thiện hơn với SIMD/bộ nhớ đệm (cache / 캐시).

Nhưng dictionary có phạm vi (scope / 범위). Dictionary per page/row-group giúp cục bộ (local / 로컬) compression tốt nhưng complicate comparison/merge giữa chunks. toàn cục (global / 전역) dictionary dễ reuse ID nhưng khó maintain khi cardinality drift hoặc phân tán (distributed / 분산) ingest.

> **Nối mạch:** **4. Dictionary encoding đổi string comparison thành integer-domain công việc (work / 작업)** đặt vấn đề; **5. Zone map/min-max siêu dữ liệu (metadata / 메타데이터) biến scan thành skip** kiểm tra bằng chứng, rồi **6. Bloom filter giúp negative pruning nhưng không chứng minh presence** mở rộng hệ quả.

## 5. Zone map/min-max siêu dữ liệu (metadata / 메타데이터) biến scan thành skip

Nếu mỗi chunk lưu min/max, truy vấn (query / 쿼리) `event_date BETWEEN A AND B` có thể bỏ qua chunk mà phạm vi (range / 범위) không overlap.

Đây là **dữ liệu (data / 데이터) skipping**: không tăng tốc việc xử lý row; nó loại bỏ cả vùng dữ liệu trước khi đọc/decode.

Hiệu quả phụ thuộc vật lý (physical / 물리적) clustering. Nếu values ngẫu nhiên, hầu hết row group đều có min/max rất rộng và pruning yếu. Nếu dữ liệu (data / 데이터) được sort/cluster theo truy vấn (query / 쿼리) dimension, min/max trở nên sắc hơn.

Vì vậy bố cục (layout / 레이아웃) và tải công việc (workload / 워크로드) truy vấn (query / 쿼리) phải được lập luận (reasoning / 추론) cùng nhau.

> **Nối mạch:** **5. Zone map/min-max siêu dữ liệu (metadata / 메타데이터) biến scan thành skip** đặt vấn đề; **6. Bloom filter giúp negative pruning nhưng không chứng minh presence** kiểm tra bằng chứng, rồi **7. Projection pushdown quyết định columns nào đi vào chuỗi xử lý (pipeline / 파이프라인)** mở rộng hệ quả.

## 6. Bloom filter giúp negative pruning nhưng không chứng minh presence

Một chunk-level Bloom filter có thể nói “giá trị chắc chắn không có” hoặc “có thể có”. Nó hữu ích cho equality predicate trên high-cardinality column khi min/max ít giá trị.

False positive làm truy vấn (query / 쿼리) đọc thêm chunk nhưng không gây false negative nếu hiện thực (implementation / 구현) đúng. bộ nhớ (memory / 메모리) dành cho Bloom filters và number of băm (hash / 해시) probes là sự đánh đổi (trade-off / 트레이드오프) giữa siêu dữ liệu (metadata / 메타데이터) kích thước (size / 크기) và I/O tránh được.

> **Nối mạch:** **6. Bloom filter giúp negative pruning nhưng không chứng minh presence** đặt đầu vào cho **7. Projection pushdown quyết định columns nào đi vào chuỗi xử lý (pipeline / 파이프라인)**, rồi **8. Predicate pushdown cần phân biệt siêu dữ liệu (metadata / 메타데이터) filter và row filter** mở rộng hệ quả.

## 7. Projection pushdown quyết định columns nào đi vào chuỗi xử lý (pipeline / 파이프라인)

Lưu trữ (storage / 저장소) reader cần biết truy vấn (query / 쿼리) chỉ yêu cầu columns nào. Nếu thực thi (execution / 실행) tầng (layer / 계층) materialize full row quá sớm, lợi thế columnar bị phá.

Projection pushdown đẩy kiến thức (knowledge / 지식) này xuống scan:

```text
query references A, C, F
→ storage reads only A, C, F chunks
→ unused columns never enter memory pipeline
```

Trong phân tán (distributed / 분산)/đối tượng (object / 객체) lưu trữ (storage / 저장소), tránh tải unused columns còn giảm mạng (network / 네트워크) egress và yêu cầu (request / 요청) chi phí (cost / 비용).

> **Nối mạch:** cơ chế trong **7. Projection pushdown quyết định columns nào đi vào chuỗi xử lý (pipeline / 파이프라인)** cần được kiểm chứng bằng dấu vết cụ thể; **8. Predicate pushdown cần phân biệt siêu dữ liệu (metadata / 메타데이터) filter và row filter** đưa dữ liệu và nguồn vào đúng điểm đó.; **9. Vectorized scan làm việc trên batch thay vì tuple-at-a-time** mở rộng hệ quả hoặc giới hạn của cơ chế này.

## 8. Predicate pushdown cần phân biệt siêu dữ liệu (metadata / 메타데이터) filter và row filter

Predicate có thể được dùng ở nhiều mức:

```text
partition pruning
→ file pruning
→ row-group pruning
→ page pruning
→ vector predicate
→ row-level residual filter
```

Không phải predicate nào cũng push xuống được. User-defined hàm (function / 함수) phức tạp, collation ngữ nghĩa (semantics / 의미론) hoặc expression phụ thuộc thời gian chạy (runtime / 런타임) trạng thái (state / 상태) có thể buộc engine đọc/decode rồi mới đánh giá.

Cấp cao (senior / 시니어) debugging cần biết filter đang loại dữ liệu (data / 데이터) ở tầng (layer / 계층) nào, không chỉ thấy SQL có `WHERE`.

> **Nối mạch:** **8. Predicate pushdown cần phân biệt siêu dữ liệu (metadata / 메타데이터) filter và row filter** đặt vấn đề; **9. Vectorized scan làm việc trên batch thay vì tuple-at-a-time** kiểm tra bằng chứng, rồi **10. Selection véc-tơ (vector / 벡터) giữ “row định danh (identity / 식별자)” mà không materialize cả row** mở rộng hệ quả.

## 9. Vectorized scan làm việc trên batch thay vì tuple-at-a-time

Tuple-at-a-time trình thông dịch (interpreter / 인터프리터) thường lặp qua row và virtual/hàm (function / 함수) dispatch cho từng operator. Vectorized thực thi (execution / 실행) xử lý batch values, giảm branch/dispatch overhead và tạo cơ hội SIMD.

Ví dụ scan một véc-tơ (vector / 벡터) 1024 integers, so sánh với threshold rồi sinh selection véc-tơ (vector / 벡터). Aggregate chỉ xử lý positions còn sống thay vì materialize đối tượng (object / 객체) cho từng row.

Mô hình tư duy (mental model / 사고 모델):

```text
encoded column chunk
→ decode batch
→ SIMD/vector predicate
→ selection vector
→ aggregate/join
```

> **Nối mạch:** **10. Selection véc-tơ (vector / 벡터) giữ “row định danh (identity / 식별자)” mà không materialize cả row** nối từ **9. Vectorized scan làm việc trên batch thay vì tuple-at-a-time** sang **11. Late materialization trì hoãn reconstruction của row**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Selection véc-tơ (vector / 벡터) giữ “row định danh (identity / 식별자)” mà không materialize cả row

Sau filter, engine có thể giữ danh sách offsets/bitmask của rows hợp lệ. Các operators sau dùng selection véc-tơ (vector / 벡터) để chỉ đụng dữ liệu cần thiết.

Điều này giảm copying nhưng có chi phí (cost / 비용) khi selectivity cao/thấp khác nhau. Với gần 100% rows survive, maintaining sparse chỉ mục (index / 인덱스) có thể không lợi. Engine thường có multiple mã (code / 코드) paths tùy density.

> **Nối mạch:** **11. Late materialization trì hoãn reconstruction của row** nối từ **10. Selection véc-tơ (vector / 벡터) giữ “row định danh (identity / 식별자)” mà không materialize cả row** sang **12. Null biểu diễn (representation / 표현) là một vật lý (physical / 물리적) thiết kế (design / 설계) concern**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Late materialization trì hoãn reconstruction của row

Nếu truy vấn (query / 쿼리) filter mạnh, ta nên filter bằng columns rẻ trước rồi chỉ fetch/materialize columns đầu ra (output / 출력) cho surviving rows.

Ví dụ:

```text
scan event_date + status
→ filter 100M rows xuống 200K
→ fetch expensive description column chỉ cho 200K rows
```

Late materialization giảm bộ nhớ (memory / 메모리) traffic nhưng cần giữ ánh xạ (mapping / 매핑) từ logical row position sang column values. phép nối (join / 조인)/reorder có thể làm ánh xạ (mapping / 매핑) phức tạp hơn.

> **Nối mạch:** **12. Null biểu diễn (representation / 표현) là một vật lý (physical / 물리적) thiết kế (design / 설계) concern** nối từ **11. Late materialization trì hoãn reconstruction của row** sang **13. Nested dữ liệu (data / 데이터) cần thêm cấu trúc (structure / 구조) ngoài flat column**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Null biểu diễn (representation / 표현) là một vật lý (physical / 물리적) thiết kế (design / 설계) concern

Nullable column thường có validity bitmap riêng. Engine có thể tiến trình (process / 프로세스) values và null mask theo véc-tơ (vector / 벡터) operations thay vì branch mỗi row.

Nhưng SQL three-valued lô-gic (logic / 논리) vẫn phải được giữ. tối ưu hóa (optimization / 최적화) không được đổi ngữ nghĩa (semantics / 의미론) của `NULL`, especially trong predicate, phép nối (join / 조인) và aggregate.

Vật lý (physical / 물리적) biểu diễn (representation / 표현) được phép thay; logical bất biến (invariant / 불변식) không được thay.

> **Nối mạch:** **12. Null biểu diễn (representation / 표현) là một vật lý (physical / 물리적) thiết kế (design / 설계) concern** đặt vấn đề; **13. Nested dữ liệu (data / 데이터) cần thêm cấu trúc (structure / 구조) ngoài flat column** kiểm tra bằng chứng, rồi **14. Updates và deletes là điểm khó của immutable columnar bố cục (layout / 레이아웃)** mở rộng hệ quả.

## 13. Nested dữ liệu (data / 데이터) cần thêm cấu trúc (structure / 구조) ngoài flat column

Array/đối tượng (object / 객체) nested không thể chỉ “tách mỗi trường dữ liệu (field / 필드) thành một flat véc-tơ (vector / 벡터)” nếu muốn reconstruct hierarchy. Columnar formats thường cần offsets, definition/repetition style siêu dữ liệu (metadata / 메타데이터) hoặc equivalent cấu trúc (structure / 구조) để biểu diễn missing/nesting boundaries.

Điều này tăng độ phức tạp (complexity / 복잡도) của scan và predicate pushdown. truy vấn (query / 쿼리) vào nested dữ liệu (data / 데이터) có thể vẫn đọc ít fields, nhưng engine phải giữ structural alignment.

> **Nối mạch:** **13. Nested dữ liệu (data / 데이터) cần thêm cấu trúc (structure / 구조) ngoài flat column** đặt vấn đề; **14. Updates và deletes là điểm khó của immutable columnar bố cục (layout / 레이아웃)** kiểm tra bằng chứng, rồi **15. Compaction/reclustering đổi ghi (write / 쓰기) chi phí (cost / 비용) để mua pruning chất lượng (quality / 품질)** mở rộng hệ quả.

## 14. Updates và deletes là điểm khó của immutable columnar bố cục (layout / 레이아웃)

Columnar chunks tối ưu scan thường gần immutable. Random in-place cập nhật (update / 업데이트) phá compression, clustering và large sequential bố cục (layout / 레이아웃).

Nhiều analytical các hệ thống (systems / 시스템들) dùng delta structures, delete vectors, append-new-version hoặc background rewrite/compaction.

Chuỗi xử lý (pipeline / 파이프라인) có thể trở thành:

```text
base immutable segment
+ delta/update/delete metadata
→ query merges visibility
→ background compaction rewrites clean segment
```

Điều này giống một dạng debt: foreground cập nhật (update / 업데이트) nhanh hơn nhưng read đường dẫn (path / 경로) và background maintenance phải trả chi phí sau.

> **Nối mạch:** **15. Compaction/reclustering đổi ghi (write / 쓰기) chi phí (cost / 비용) để mua pruning chất lượng (quality / 품질)** nối từ **14. Updates và deletes là điểm khó của immutable columnar bố cục (layout / 레이아웃)** sang **16. bộ nhớ (memory / 메모리) bandwidth thường là bottleneck trước ALU**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. Compaction/reclustering đổi ghi (write / 쓰기) chi phí (cost / 비용) để mua pruning chất lượng (quality / 품질)

Khi ingest làm dữ liệu mất sort thứ tự (order / 순서), zone map và compression có thể kém dần. Reclustering/compaction sắp xếp lại dữ liệu (data / 데이터) để phục hồi locality.

Nhưng rewrite terabytes dữ liệu cạnh tranh I/O/mạng (network / 네트워크)/CPU với queries. Hệ thống cần throttle maintenance và chọn lúc lợi ích pruning lớn hơn rewrite chi phí (cost / 비용).

Không có trạng thái “columnar bảng (table / 테이블) đã optimize xong vĩnh viễn”. tải công việc (workload / 워크로드) và dữ liệu (data / 데이터) phân phối (distribution / 분포) thay đổi theo thời gian.

> **Nối mạch:** **16. bộ nhớ (memory / 메모리) bandwidth thường là bottleneck trước ALU** nối từ **15. Compaction/reclustering đổi ghi (write / 쓰기) chi phí (cost / 비용) để mua pruning chất lượng (quality / 품질)** sang **17. Spill là phase thay đổi (change / 변경) của thực thi (execution / 실행)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 16. bộ nhớ (memory / 메모리) bandwidth thường là bottleneck trước ALU

Analytical scan có thể thực hiện arithmetic rất đơn giản trên lượng dữ liệu (data / 데이터) lớn. CPU utilization cao không có nghĩa ALU là bottleneck; cores có thể chờ bộ nhớ (memory / 메모리).

Compression, vectorization, prefetch và dữ liệu (data / 데이터) bố cục (layout / 레이아웃) cùng mục tiêu tăng **useful công việc (work / 작업) per byte moved**. Đây là liên kết (connection / 연결) trực tiếp với operational intensity/roofline lập luận (reasoning / 추론) trong [capacity planning](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

> **Nối mạch:** **17. Spill là phase thay đổi (change / 변경) của thực thi (execution / 실행)** nối từ **16. bộ nhớ (memory / 메모리) bandwidth thường là bottleneck trước ALU** sang **18. phân tán (distributed / 분산) analytical scan thêm mạng (network / 네트워크) và skew**, vì cơ chế trước tạo đầu vào cho bước sau.

## 17. Spill là phase thay đổi (change / 변경) của thực thi (execution / 실행)

Băm (hash / 해시) aggregate/phép nối (join / 조인)/sort có thể chạy in-memory tới một threshold. Khi bộ nhớ (memory / 메모리) ngân sách (budget / 예산) vượt giới hạn, engine partition và spill ra disk/đối tượng (object / 객체) lưu trữ (storage / 저장소).

Độ trễ (latency / 지연 시간) lúc này không tăng tuyến tính; thực thi (execution / 실행) chế độ (mode / 모드) đổi phase:

```text
in-memory
→ memory pressure
→ spill
→ extra serialization + I/O + merge passes
```

Một truy vấn (query / 쿼리) chậm 10× có thể không phải “dữ liệu (data / 데이터) tăng 10×” mà vì vừa vượt bộ nhớ (memory / 메모리) threshold.

> **Nối mạch:** **18. phân tán (distributed / 분산) analytical scan thêm mạng (network / 네트워크) và skew** nối từ **17. Spill là phase thay đổi (change / 변경) của thực thi (execution / 실행)** sang **19. thất bại (failure / 실패) modes và tính đúng đắn (correctness / 정확성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 18. phân tán (distributed / 분산) analytical scan thêm mạng (network / 네트워크) và skew

Khi row groups phân tán, scheduler cố gắng đẩy scan gần dữ liệu (data / 데이터) hoặc phân chia ranges song song. Partition skew làm một số workers xong sớm còn một worker giữ tail độ trễ (latency / 지연 시간).

Pruning tốt giảm cả lưu trữ (storage / 저장소) I/O lẫn mạng (network / 네트워크) shuffle. Nhưng phép nối (join / 조인)/group-by có thể vẫn tạo shuffle mới sau scan. Vì vậy cần phân biệt **bytes read from lưu trữ (storage / 저장소)** và **bytes exchanged between workers**.

> **Nối mạch:** **19. thất bại (failure / 실패) modes và tính đúng đắn (correctness / 정확성)** nối từ **18. phân tán (distributed / 분산) analytical scan thêm mạng (network / 네트워크) và skew** sang **20. bằng chứng vận hành (production evidence / 운영 증거)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 19. thất bại (failure / 실패) modes và tính đúng đắn (correctness / 정확성)

Corrupt page/chunk cần checksum hoặc integrity bằng chứng (evidence / 증거). siêu dữ liệu (metadata / 메타데이터) min/max sai có thể nguy hiểm hơn slow truy vấn (query / 쿼리) vì engine có thể prune nhầm dữ liệu (data / 데이터) hợp lệ. Dictionary/encoding decoder bug có thể tạo silent corruption nếu kiểm tra hợp lệ (validation / 검증) yếu.

Tối ưu hóa (optimization / 최적화) siêu dữ liệu (metadata / 메타데이터) được phép gây false-positive công việc (work / 작업), nhưng không được gây false-negative kết quả (result / 결과) trừ khi ngữ nghĩa (semantics / 의미론) explicitly approximate.

Đây là một bất biến (invariant / 불변식) đáng nhớ:

> Pruning siêu dữ liệu (metadata / 메타데이터) có thể bỏ lỡ cơ hội skip; không được skip dữ liệu có thể chứa kết quả đúng.

> **Nối mạch:** **19. thất bại (failure / 실패) modes và tính đúng đắn (correctness / 정확성)** đặt vấn đề; **20. bằng chứng vận hành (production evidence / 운영 증거)** kiểm tra bằng chứng, rồi **21. Worked example: dashboard aggregate** mở rộng hệ quả.

## 20. bằng chứng vận hành (production evidence / 운영 증거)

Khi truy vấn (query / 쿼리) chậm, nên tách bằng chứng (evidence / 증거) theo chuỗi xử lý (pipeline / 파이프라인):

```text
partitions/files considered
→ row groups pruned
→ bytes read
→ compressed vs decoded bytes
→ rows scanned / rows selected
→ vector batch efficiency
→ spill bytes / passes
→ shuffle bytes
→ CPU vs memory-bandwidth vs I/O wait
```

Thực thi (execution / 실행) plan chỉ cho biết intended operators; thời gian chạy (runtime / 런타임) counters mới cho thấy selectivity/cardinality thực tế và phase thay đổi (change / 변경).

> **Nối mạch:** **20. bằng chứng vận hành (production evidence / 운영 증거)** nêu quy tắc; **21. Worked example: dashboard aggregate** thử quy tắc trong tình huống, rồi **22. Kết nối sang các chapter khác** mở rộng hệ quả.

## 21. Worked example: dashboard aggregate

Một dashboard đọc 2 năm dữ liệu nhưng chỉ hiển thị 7 ngày gần nhất. Nếu bảng (table / 테이블) partition/cluster theo date, partition + row-group pruning có thể giảm scan từ terabytes xuống gigabytes trước khi decode.

Sau đó chỉ `region`, `amount` và `date` được dự án (project / 프로젝트). `date` filter sinh selection véc-tơ (vector / 벡터); `region`/`amount` chỉ được xử lý cho surviving rows. Aggregate chạy vectorized. Nếu group cardinality quá lớn và bộ nhớ (memory / 메모리) ngân sách (budget / 예산) thiếu, băm (hash / 해시) aggregate spill và độ trễ (latency / 지연 시간) đổi hẳn.

Cùng SQL văn bản (text / 텍스트) có thể rất nhanh hoặc rất chậm tùy vật lý (physical / 물리적) clustering, stats, pruning tỷ lệ (rate / 비율) và bộ nhớ (memory / 메모리) threshold.

> **Nối mạch:** **21. Worked example: dashboard aggregate** nêu quy tắc; **22. Kết nối sang các chapter khác** thử quy tắc trong tình huống, rồi mục sau khép mạch bằng giới hạn và ứng dụng.

## 22. Kết nối sang các chapter khác

Columnar lưu trữ (storage / 저장소) nối với [cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md), [join/vectorized execution](./06_join_algorithms_vectorized_execution_and_late_materialization.md), [LSM/compaction](./03_lsm_tree_compaction_bloom_filters_and_write_amplification.md) về maintenance debt, và [capacity/whole-system profiling](../../08_software_systems/advanced/01_capacity_planning_utilization_knee_and_admission_control.md).

Mô hình tư duy (mental model / 사고 모델) cuối cùng: **analytical hiệu năng (performance / 성능) đến từ việc loại công việc (work / 작업) càng sớm càng tốt, giữ biểu diễn (representation / 표현) compact càng lâu càng tốt, và chỉ materialize bytes/rows thật sự cần cho kết quả.**

> **Bàn giao:** Sau **22. Kết nối sang các chapter khác**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
