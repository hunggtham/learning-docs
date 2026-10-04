# B+cây (tree / 트리) page bố cục (layout / 레이아웃), splits/merges và latch coupling

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **B+Tree page layout, splits/merges và latch coupling**. Route đi từ internal/leaf pages → buffer-pool traversal → insert split/delete merge → latch coupling và concurrent failure, để cấu trúc cây được đọc cùng chi phí I/O và contention.

B+cây (tree / 트리) thường được giới thiệu như “balanced cây (tree / 트리) có O(log n)”. Điều đó đúng nhưng chưa đủ để giải thích cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스) môi trường vận hành (production / 운영 환경). B+cây (tree / 트리) tồn tại vì nó giữ một bất biến (invariant / 불변식) rất thực tế: **mỗi traversal phải đi qua một cấu trúc page-oriented luôn hợp lệ dưới concurrent read/ghi (write / 쓰기), trong khi cây (tree / 트리) vẫn đủ nông để giảm I/O và trượt bộ nhớ đệm (cache miss / 캐시 미스).**

Hiệu năng (performance / 성능) thật không được quyết định chỉ bởi `O(log n)`, mà bởi page bố cục (layout / 레이아웃), fan-out, buffer-pool residency, split/merge giao thức (protocol / 프로토콜), latch contention, WAL và key phân phối (distribution / 분포).

## 1. Vì sao cơ sở dữ liệu (database / 데이터베이스) không dùng tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리) thông thường?

Nhị phân (binary / 이진) cây (tree / 트리) có branching factor thấp. Nếu mỗi pointer hop thành một random page truy cập (access / 접근), số I/O rất lớn. B+cây (tree / 트리) đóng hàng trăm keys/pointers vào một page để mỗi page truy cập (access / 접근) mang về nhiều routing thông tin (information / 정보).

Nếu fan-out là vài trăm, cây (tree / 트리) hàng triệu hoặc hàng tỷ records vẫn chỉ cần vài levels.

```text
root
  ↓
internal page
  ↓
internal/leaf page
```

Height nhỏ là một bất biến (invariant / 불변식) hiệu năng (performance / 성능) quan trọng vì mỗi mức (level / 수준) có thể là buffer lookup hoặc lưu trữ (storage / 저장소) truy cập (access / 접근).

> **Nối mạch:** **1. Vì sao cơ sở dữ liệu (database / 데이터베이스) không dùng tìm kiếm nhị phân (binary search / 이진 탐색) cây (tree / 트리) thông thường?** đặt vấn đề; **2. nội bộ (internal / 내부) page và leaf page có vai trò khác nhau** kiểm tra bằng chứng, rồi **3. Page thực tế không chỉ là array keys** mở rộng hệ quả.

## 2. nội bộ (internal / 내부) page và leaf page có vai trò khác nhau

Nội bộ (internal / 내부) page chứa separator keys và child page IDs. Leaf page chứa chỉ mục (index / 인덱스) entries; tùy clustered/nonclustered thiết kế (design / 설계), leaf có thể chứa full row, primary key hoặc row locator.

Leaves thường linked theo key thứ tự (order / 순서). Sau khi tìm điểm bắt đầu, phạm vi (range / 범위) scan có thể đi tuần tự qua sibling leaves thay vì quay lại gốc (root / 루트) cho từng key.

Đây là lý do một cấu trúc vừa phục vụ equality lookup vừa phục vụ ordered phạm vi (range / 범위) scan tốt.

> **Nối mạch:** **3. Page thực tế không chỉ là array keys** nối từ **2. nội bộ (internal / 내부) page và leaf page có vai trò khác nhau** sang **4. tìm kiếm (search / 검색) đi qua buffer pool trước khi đi tới lưu trữ (storage / 저장소)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 3. Page thực tế không chỉ là array keys

Một page cần header và siêu dữ liệu (metadata / 메타데이터) như page id/kiểu (type / 타입), free-space trạng thái (state / 상태), sibling links, LSN/checksum tùy engine. Variable-length records thường dùng **slot directory** để logical slot ổn định hơn dù bytes bên trong page được compact/move.

Điểm này quan trọng vì một cập nhật (update / 업데이트) `VARCHAR` dài hơn có thể làm bản ghi (record / 레코드) move trong page mà logical key không đổi. vật lý (physical / 물리적) bố cục (layout / 레이아웃) vì thế tác động trực tiếp tới ghi (write / 쓰기) amplification và fragmentation.

> **Nối mạch:** **4. tìm kiếm (search / 검색) đi qua buffer pool trước khi đi tới lưu trữ (storage / 저장소)** nối từ **3. Page thực tế không chỉ là array keys** sang **5. tìm kiếm (search / 검색) trong page cũng có microarchitectural chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 4. tìm kiếm (search / 검색) đi qua buffer pool trước khi đi tới lưu trữ (storage / 저장소)

Logical đường dẫn (path / 경로) gốc (root / 루트) → nội bộ (internal / 내부) → leaf không đồng nghĩa mỗi mức (level / 수준) gây disk I/O. Hot gốc (root / 루트)/nội bộ (internal / 내부) pages thường ở buffer pool. Leaf truy cập (access / 접근) hoặc base-table lookup mới có thể là random I/O đáng kể.

Chi phí (cost / 비용) mô hình (model / 모델) cần tách:

```text
tree height
×
page residency/cache hit
×
storage latency
×
key/record width
```

Hai indexes cùng height có thể có hiệu năng (performance / 성능) rất khác nếu một chỉ mục (index / 인덱스) lớn hơn và ít fit bộ nhớ đệm (cache / 캐시) hơn.

> **Nối mạch:** **5. tìm kiếm (search / 검색) trong page cũng có microarchitectural chi phí (cost / 비용)** nối từ **4. tìm kiếm (search / 검색) đi qua buffer pool trước khi đi tới lưu trữ (storage / 저장소)** sang **6. Insert và page split**, vì cơ chế trước tạo đầu vào cho bước sau.

## 5. tìm kiếm (search / 검색) trong page cũng có microarchitectural chi phí (cost / 비용)

Bên trong page, engine có thể binary-search separator keys, dùng prefix compression hoặc bố cục (layout / 레이아웃) tối ưu bộ nhớ đệm (cache / 캐시)/SIMD tùy hiện thực (implementation / 구현).

Khi chỉ mục (index / 인덱스) nằm phần lớn trong bộ nhớ (memory / 메모리), branch prediction, cache-line footprint và key width có thể quan trọng gần như lưu trữ (storage / 저장소) I/O.

Đây là liên kết (connection / 연결) giữa cơ sở dữ liệu (database / 데이터베이스) internals và Computer kiến trúc (architecture / 아키텍처): asymptotic độ phức tạp (complexity / 복잡도) không mô tả toàn bộ hành vi (behavior / 동작) khi hierarchy bộ nhớ (memory / 메모리) chi phối độ trễ (latency / 지연 시간).

> **Nối mạch:** **6. Insert và page split** nối từ **5. tìm kiếm (search / 검색) trong page cũng có microarchitectural chi phí (cost / 비용)** sang **7. Fill factor là sự đánh đổi (trade-off / 트레이드오프) density với future ghi (write / 쓰기) chi phí (cost / 비용)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 6. Insert và page split

Nếu leaf còn free không gian (space / 공간), insert tương đối cục bộ (local / 로컬). Khi page đầy, engine phải split:

```text
[ A B C D E F ]
        ↓
[ A B C ] <-> [ D E F ]
        ↑
parent nhận separator
```

Nếu parent đầy, split có thể propagate lên; gốc (root / 루트) split làm cây (tree / 트리) cao thêm một mức (level / 수준).

Split không chỉ là array thao tác (operation / 연산). Nó cần structural synchronization, WAL/logging, dirty pages và khôi phục (recovery / 복구) ngữ nghĩa (semantics / 의미론).

Bất biến (invariant / 불변식) là concurrent readers/writers không được thấy cây (tree / 트리) ở trạng thái làm mất key, đi sai child hoặc tạo unreachable page.

> **Nối mạch:** **7. Fill factor là sự đánh đổi (trade-off / 트레이드오프) density với future ghi (write / 쓰기) chi phí (cost / 비용)** nối từ **6. Insert và page split** sang **8. Key phân phối (distribution / 분포) quyết định hotspot**, vì cơ chế trước tạo đầu vào cho bước sau.

## 7. Fill factor là sự đánh đổi (trade-off / 트레이드오프) density với future ghi (write / 쓰기) chi phí (cost / 비용)

Page bản dựng (build / 빌드) 100% full tối ưu density hiện tại nhưng random inserts dễ gây split sớm. Fill factor để lại free không gian (space / 공간) để hấp thụ future writes.

Đổi lại:

```text
free space nhiều
→ page count tăng
→ cache footprint tăng
→ range scan đọc nhiều pages hơn
```

Không có fill factor đúng universal. Append-heavy và random-key workloads tạo pressure khác nhau.

> **Nối mạch:** **8. Key phân phối (distribution / 분포) quyết định hotspot** nối từ **7. Fill factor là sự đánh đổi (trade-off / 트레이드오프) density với future ghi (write / 쓰기) chi phí (cost / 비용)** sang **9. Delete và merge trong môi trường vận hành (production / 운영 환경) không giống textbook tuyệt đối**, vì cơ chế trước tạo đầu vào cho bước sau.

## 8. Key phân phối (distribution / 분포) quyết định hotspot

Monotonically increasing IDs tập trung insert ở rightmost leaf. Điều này có locality tốt nhưng có thể tạo latch/ghi (write / 쓰기) hotspot. Random UUID phân tán inserts rộng hơn nhưng làm page locality và fragmentation mẫu (pattern / 패턴) khác.

Khi quy mô (scale / 규모) ghi (write / 쓰기) tính đồng thời (concurrency / 동시성), câu hỏi không chỉ “chỉ mục (index / 인덱스) có selectivity tốt không?” mà còn “writes tập trung vào bao nhiêu leaves?”.

> **Nối mạch:** **9. Delete và merge trong môi trường vận hành (production / 운영 환경) không giống textbook tuyệt đối** nối từ **8. Key phân phối (distribution / 분포) quyết định hotspot** sang **10. Latch khác giao dịch (transaction / 트랜잭션) khóa (lock / 잠금)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 9. Delete và merge trong môi trường vận hành (production / 운영 환경) không giống textbook tuyệt đối

Textbook B-tree thường redistribute/merge để giữ occupancy bound chặt sau delete. cơ sở dữ liệu (database / 데이터베이스) engine thực tế có thể trì hoãn cleanup vì merge cũng tạo ghi (write / 쓰기) amplification và synchronization chi phí (cost / 비용).

Do đó sparse/fragmented pages có thể tồn tại cho tới background maintenance/rebuild/vacuum tùy engine.

Bất biến (invariant / 불변식) môi trường vận hành (production / 운영 환경) thường yếu hơn “mọi page luôn >= 50% full”, nhưng mạnh hơn ở tính đúng đắn (correctness / 정확성): tìm kiếm (search / 검색)/phạm vi (range / 범위) thứ tự (order / 순서) vẫn đúng và page đồ thị (graph / 그래프) vẫn reachable hợp lệ.

> **Nối mạch:** **10. Latch khác giao dịch (transaction / 트랜잭션) khóa (lock / 잠금)** nối từ **9. Delete và merge trong môi trường vận hành (production / 운영 환경) không giống textbook tuyệt đối** sang **11. Latch coupling / crabbing**, vì cơ chế trước tạo đầu vào cho bước sau.

## 10. Latch khác giao dịch (transaction / 트랜잭션) khóa (lock / 잠금)

**khóa (lock / 잠금)** bảo vệ logical cơ sở dữ liệu (database / 데이터베이스) trạng thái (state / 상태) giữa transactions. **Latch** bảo vệ in-memory cấu trúc dữ liệu (data structure / 자료구조) trong trọng yếu (critical / 중요) section rất ngắn.

Một row khóa (lock / 잠금) có thể sống hàng giây theo giao dịch (transaction / 트랜잭션). Page/cây (tree / 트리) latch thường chỉ sống micro/milliseconds hoặc ngắn hơn tùy hiện thực (implementation / 구현).

Vì vậy `lock wait` và `latch contention` là hai thất bại (failure / 실패) families khác nhau:

```text
transaction lock -> isolation/business concurrency
latch             -> internal structure concurrency
```

Chẩn đoán sai loại wait dẫn tới fix sai lớp trừu tượng (abstraction / 추상화) tầng (layer / 계층).

> **Nối mạch:** **11. Latch coupling / crabbing** nối từ **10. Latch khác giao dịch (transaction / 트랜잭션) khóa (lock / 잠금)** sang **12. Optimistic traversal và B-link style lập luận (reasoning / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 11. Latch coupling / crabbing

Trong traversal concurrent, luồng thực thi (thread / 스레드) có thể giữ latch parent, acquire latch child rồi bản phát hành (release / 릴리스) parent khi child được xem là safe cho thao tác (operation / 연산).

Insert/delete phức tạp hơn read vì child có thể split/merge. giao thức (protocol / 프로토콜) phải giữ bất biến (invariant / 불변식) rằng cấu trúc (structure / 구조) không bị thay đổi dưới chân traversal theo cách làm pointer/tìm kiếm (search / 검색) đường dẫn (path / 경로) mất validity.

Nếu latch toàn cây (tree / 트리) để đơn giản tính đúng đắn (correctness / 정확성), tính đồng thời (concurrency / 동시성) sẽ collapse. Vì vậy B+cây (tree / 트리) thiết kế (design / 설계) luôn trade proof độ phức tạp (complexity / 복잡도) lấy parallelism.

> **Nối mạch:** **12. Optimistic traversal và B-link style lập luận (reasoning / 추론)** nối từ **11. Latch coupling / crabbing** sang **13. Covering chỉ mục (index / 인덱스): ít lookup hơn nhưng page lớn hơn**, vì cơ chế trước tạo đầu vào cho bước sau.

## 12. Optimistic traversal và B-link style lập luận (reasoning / 추론)

Read-heavy indexes có thể dùng phiên bản (version / 버전) checks, sibling links hoặc optimistic techniques: traverse nhẹ, validate trạng thái (state / 상태), thử lại (retry / 재시도) khi detect concurrent structural thay đổi (change / 변경).

Mô hình tư duy (mental model / 사고 모델) giống optimistic tính đồng thời (concurrency / 동시성) điều khiển (control / 제어):

```text
đọc nhanh dưới assumption
→ validate invariant
→ retry nếu conflict
```

Mục tiêu là tránh exclusive/dùng chung (shared / 공유) latch ở hot ancestors nhiều hơn mức cần thiết.

> **Nối mạch:** **13. Covering chỉ mục (index / 인덱스): ít lookup hơn nhưng page lớn hơn** nối từ **12. Optimistic traversal và B-link style lập luận (reasoning / 추론)** sang **14. Composite key và leftmost-prefix từ vật lý (physical / 물리적) thứ tự (ordering / 순서)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 13. Covering chỉ mục (index / 인덱스): ít lookup hơn nhưng page lớn hơn

Nếu chỉ mục (index / 인덱스) chứa đủ columns để trả truy vấn (query / 쿼리), engine có thể tránh base-table lookup. Nhưng leaf entry lớn hơn làm:

```text
fan-out giảm
page count tăng
cache footprint tăng
write amplification tăng
```

Chỉ mục (index / 인덱스) thiết kế (design / 설계) là sự đánh đổi (trade-off / 트레이드오프) read-path reduction với bộ nhớ (memory / 메모리)/lưu trữ (storage / 저장소)/ghi (write / 쓰기) pressure, không chỉ “truy vấn (query / 쿼리) có dùng chỉ mục (index / 인덱스) hay không”.

> **Nối mạch:** **14. Composite key và leftmost-prefix từ vật lý (physical / 물리적) thứ tự (ordering / 순서)** nối từ **13. Covering chỉ mục (index / 인덱스): ít lookup hơn nhưng page lớn hơn** sang **15. dạng thất bại (failure mode / 실패 모드) dưới tính đồng thời (concurrency / 동시성) và pressure**, vì cơ chế trước tạo đầu vào cho bước sau.

## 14. Composite key và leftmost-prefix từ vật lý (physical / 물리적) thứ tự (ordering / 순서)

Chỉ mục (index / 인덱스) `(a, b)` được sắp lexicographically. truy vấn (query / 쿼리) theo `a` hoặc `(a,b)` thường map thành contiguous phạm vi (range / 범위) tốt; truy vấn (query / 쿼리) chỉ theo `b` không có cùng thuộc tính (property / 속성) vì values của `b` bị xen giữa các groups `a`.

“Leftmost prefix” không phải mẹo để học thuộc. Nó xuất phát từ thứ tự (ordering / 순서) vật lý của leaf keys.

> **Nối mạch:** **15. dạng thất bại (failure mode / 실패 모드) dưới tính đồng thời (concurrency / 동시성) và pressure** nối từ **14. Composite key và leftmost-prefix từ vật lý (physical / 물리적) thứ tự (ordering / 순서)** sang **16. bằng chứng vận hành (production evidence / 운영 증거)**, vì cơ chế trước tạo đầu vào cho bước sau.

## 15. dạng thất bại (failure mode / 실패 모드) dưới tính đồng thời (concurrency / 동시성) và pressure

Các symptom điển hình:

```text
hot leaf/root latch contention
page-split burst khi write spike
index bloat/fragmentation
cache miss tăng vì index quá rộng
range scan chậm vì page density thấp
WAL/write pressure tăng do structural changes
```

Một kế hoạch truy vấn (query plan / 쿼리 계획) vẫn “dùng đúng chỉ mục (index / 인덱스)” nhưng độ trễ (latency / 지연 시간) có thể xấu vì internals above.

> **Nối mạch:** **15. dạng thất bại (failure mode / 실패 모드) dưới tính đồng thời (concurrency / 동시성) và pressure** đặt vấn đề; **16. bằng chứng vận hành (production evidence / 운영 증거)** kiểm tra bằng chứng, rồi **17. Lower tầng (layer / 계층) nào quyết định hành vi (behavior / 동작)?** mở rộng hệ quả.

## 16. bằng chứng vận hành (production evidence / 운영 증거)

Bằng chứng (evidence / 증거) cần nối logical SQL với vật lý (physical / 물리적) chỉ mục (index / 인덱스) hành vi (behavior / 동작):

```text
execution plan + actual rows/pages
buffer/cache hit ratio phù hợp ngữ cảnh
index/page size và depth
page split/maintenance statistics nếu engine expose
latch/internal wait events
WAL/log volume
I/O latency và random-read pressure
key distribution/hot partition evidence
```

Tên view/wait sự kiện (event / 이벤트) khác theo PostgreSQL, Oracle, MySQL/InnoDB, SQL máy chủ (server / 서버). mô hình tư duy (mental model / 사고 모델) không phụ thuộc vendor: **đo traversal chi phí (cost / 비용), residency, structural ghi (write / 쓰기) và contention**.

> **Nối mạch:** **16. bằng chứng vận hành (production evidence / 운영 증거)** đặt vấn đề; **17. Lower tầng (layer / 계층) nào quyết định hành vi (behavior / 동작)?** kiểm tra bằng chứng, rồi **18. Mô hình tư duy** mở rộng hệ quả.

## 17. Lower tầng (layer / 계층) nào quyết định hành vi (behavior / 동작)?

Nếu điểm (point / 지점) lookup chậm vì leaf miss, buffer pool/lưu trữ (storage / 저장소) quyết định chi phí (cost / 비용). Nếu ghi (write / 쓰기) tính đồng thời (concurrency / 동시성) không quy mô (scale / 규모), page/latch hotspot có thể quyết định. Nếu wide covering chỉ mục (index / 인덱스) làm bộ nhớ đệm (cache / 캐시) pressure, dữ liệu (data / 데이터) bố cục (layout / 레이아웃) quyết định. Nếu split burst làm lần ghi nhận (commit / 커밋) độ trễ (latency / 지연 시간) tăng, WAL/filesystem đường dẫn (path / 경로) có thể trở thành bottleneck bên dưới.

B+cây (tree / 트리) là một lớp trừu tượng (abstraction / 추상화) giao nhau giữa thuật toán (algorithm / 알고리즘), cơ sở dữ liệu (database / 데이터베이스) tính đồng thời (concurrency / 동시성), OS I/O và hardware bộ nhớ đệm (cache / 캐시).

> **Nối mạch:** **18. Mô hình tư duy** tổng hợp từ **17. Lower tầng (layer / 계층) nào quyết định hành vi (behavior / 동작)?**; **Kết nối** mở rộng mạch bằng hệ quả hoặc giới hạn liên quan.

## 18. Mô hình tư duy

> B+cây (tree / 트리) môi trường vận hành (production / 운영 환경) là **một hierarchy fixed-size pages giữ ordered-search bất biến (invariant / 불변식) dưới tính đồng thời (concurrency / 동시성)**. Fan-out giữ cây (tree / 트리) nông; buffer pool quyết định bao nhiêu hop thành I/O; split/merge là structural writes; latch giữ cấu trúc (structure / 구조) ngắn hạn; giao dịch (transaction / 트랜잭션) khóa (lock / 잠금) giữ isolation lô-gic (logic / 논리); key/bố cục (layout / 레이아웃) quyết định hotspot và bộ nhớ đệm (cache / 캐시) footprint.

> **Nối mạch:** **Kết nối** tổng hợp từ **18. Mô hình tư duy**; mục sau khép mạch bằng giới hạn và ứng dụng.

## Kết nối

Đọc tiếp [LSM Tree](./03_lsm_tree_compaction_bloom_filters_and_write_amplification.md), [Buffer pool](./04_buffer_pool_replacement_and_dirty_page_management.md), [Cost-based optimizer](./05_cost_based_optimizer_cardinality_estimation_and_statistics.md), [Memory/cache hierarchy](../../02_computer_architecture/advanced/03_advanced_cache_hierarchy_prefetching_and_replacement.md) và [Durability path](../../90_connections/advanced/03_durability_path_application_commit_wal_filesystem_device.md).

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
