# DSA trong cơ sở dữ liệu, mạng và hệ thống

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **DSA trong cơ sở dữ liệu, mạng và hệ thống**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. B+cây (tree / 트리) trong cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스)** gom dữ liệu hoặc nguồn để kiểm tra một nhận định cụ thể; sau đó sang **2. Clustered và Secondary chỉ mục (index / 인덱스)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**dữ liệu (data / 데이터) Structures & Algorithms in Real các hệ thống (systems / 시스템들) / 실무 시스템 속의 자료구조와 알고리즘**

DSA trong hệ thống thực tế hiếm khi xuất hiện dưới nhãn “bài mảng”, “bài vùng nhớ động (heap / 힙)” hay “bài đồ thị”. Nó ẩn trong chỉ mục (index / 인덱스) cơ sở dữ liệu, buffer pool, bộ nhớ đệm (cache / 캐시), scheduler, routing bảng (table / 테이블), filesystem, trình biên dịch (compiler / 컴파일러), tìm kiếm (search / 검색) engine, telemetry chuỗi xử lý (pipeline / 파이프라인) và thời gian chạy (runtime / 런타임).

Điểm quan trọng là hệ thống thật gần như luôn **ghép nhiều cấu trúc dữ liệu**, rồi thêm persistence, tính đồng thời (concurrency / 동시성), khôi phục (recovery / 복구) và hardware-aware tối ưu hóa (optimization / 최적화) lên trên phần lõi DSA.

Vì vậy mục tiêu của chương này không phải liệt kê “cấu trúc nào xuất hiện ở đâu”, mà là chỉ ra cách các bất biến và mô hình chi phí của DSA được chuyển thành quyết định kiến trúc.

## 1. B+cây (tree / 트리) trong cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스)

Một cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스) cần:

```text
exact lookup
ordered lookup
lower/upper bound
range scan
insert/update/delete
```

Balanced BST trong RAM có `O(log n)` nhưng mỗi nút (node / 노드) thường chứa ít key và liên kết bằng pointer. lưu trữ (storage / 저장소) engine lại làm việc theo page/khối (block / 블록), nên mục tiêu thật là giảm **số page I/O**.

B+cây (tree / 트리) đặt nhiều key trong một page, tạo fan-out lớn và chiều cao rất nhỏ:

\[
height\approx \log_B n
\]

với `B` là số nhánh trên page.

Leaf còn thường liên kết tuần tự, nên phạm vi (range / 범위) scan sau khi tìm lower bound có thể đọc nhiều page liền nhau.

Đây là ví dụ kinh điển cho việc cùng Big-O nhưng **mô hình chi phí I/O** làm thay đổi lựa chọn cấu trúc.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **1. B+cây (tree / 트리) trong cơ sở dữ liệu (database / 데이터베이스) chỉ mục (index / 인덱스)** nêu điều cần giải thích; **2. Clustered và Secondary chỉ mục (index / 인덱스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **3. Composite chỉ mục (index / 인덱스) và Lexicographic thứ tự (order / 순서)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 2. Clustered và Secondary chỉ mục (index / 인덱스)

Nếu dữ liệu bản ghi được lưu gần theo thứ tự chỉ mục (index / 인덱스), phạm vi (range / 범위) scan có locality tốt hơn. Secondary chỉ mục (index / 인덱스) có thể chỉ lưu key + row identifier rồi phải truy cập bảng chính để lấy bản ghi đầy đủ.

Một truy vấn (query / 쿼리) trả nhiều row có thể trở nên đắt vì nhiều random lookup tới dữ liệu chính.

Do đó chi phí (cost / 비용) mô hình (model / 모델) không chỉ có “chỉ mục (index / 인덱스) lookup `O(log n)`” mà còn gồm:

```text
số page của index
số row lookup
locality của table access
selectivity
covering index hay không
```

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **3. Composite chỉ mục (index / 인덱스) và Lexicographic thứ tự (order / 순서)** tiếp nhận điểm tựa từ **2. Clustered và Secondary chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. băm (hash / 해시) chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Composite chỉ mục (index / 인덱스) và Lexicographic thứ tự (order / 순서)

Chỉ mục (index / 인덱스) `(a,b,c)` thường dùng thứ tự từ điển:

```text
so a trước
nếu a bằng nhau -> so b
nếu b bằng nhau -> so c
```

Điều này giải thích vì sao biết prefix trái của key làm vùng tìm kiếm liên tục hơn.

Không nên học “leftmost prefix quy tắc (rule / 규칙)” như mẹo riêng của SQL; nó xuất phát trực tiếp từ thứ tự (ordering / 순서) bất biến (invariant / 불변식) của tuple key.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **4. băm (hash / 해시) chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **3. Composite chỉ mục (index / 인덱스) và Lexicographic thứ tự (order / 순서)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. băm (hash / 해시) phép nối (join / 조인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. băm (hash / 해시) chỉ mục (index / 인덱스)

Băm (hash / 해시) chỉ mục (index / 인덱스) phù hợp chính xác (exact / 정확한) equality lookup nhưng không tự hỗ trợ phạm vi (range / 범위) scan hoặc ordered iteration.

```sql
WHERE id = ?
```

là tải công việc (workload / 워크로드) tự nhiên cho hashing.

```sql
WHERE price BETWEEN ? AND ?
ORDER BY price
```

cần thứ tự (order / 순서) ngữ nghĩa (semantics / 의미론), nên B+cây (tree / 트리) thường phù hợp hơn.

Một chỉ mục (index / 인덱스) chỉ có giá trị nếu bất biến (invariant / 불변식) của nó khớp predicate của truy vấn (query / 쿼리).

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **5. băm (hash / 해시) phép nối (join / 조인)** tiếp nhận điểm tựa từ **4. băm (hash / 해시) chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Sort-Merge phép nối (join / 조인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. băm (hash / 해시) phép nối (join / 조인)

Băm (hash / 해시) phép nối (join / 조인) thường:

1. bản dựng (build / 빌드) bảng băm (hash table / 해시 테이블) trên đầu vào (input / 입력) nhỏ hơn;
2. probe đầu vào (input / 입력) còn lại bằng phép nối (join / 조인) key.

Expected độ phức tạp (complexity / 복잡도) gần:

\[
O(n+m)
\]

nếu băm (hash / 해시) tốt và dữ liệu đủ nằm trong bộ nhớ (memory / 메모리).

Nếu bản dựng (build / 빌드) side vượt bộ nhớ (memory / 메모리), engine có thể partition dữ liệu và thực hiện nhiều pass qua disk. Khi đó external-memory chi phí (cost / 비용) trở thành phần quan trọng hơn Big-O RAM mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **6. Sort-Merge phép nối (join / 조인)** tiếp nhận điểm tựa từ **5. băm (hash / 해시) phép nối (join / 조인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Nested-Loop phép nối (join / 조인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Sort-Merge phép nối (join / 조인)

Nếu hai đầu vào (input / 입력) đã được sắp theo phép nối (join / 조인) key, có thể merge bằng hai con trỏ.

Nếu chưa có thứ tự, cần sorting trước.

Sort-Merge phép nối (join / 조인) phù hợp khi:

```text
input đã ordered
join/range semantics phù hợp
external sorting có thể tận dụng sequential I/O
```

Một chỉ mục (index / 인덱스) có thứ tự có thể đồng thời phục vụ tìm kiếm (search / 검색), order-by và merge phép nối (join / 조인). Đây là ví dụ một bất biến (invariant / 불변식) được tái sử dụng cho nhiều operator.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **7. Nested-Loop phép nối (join / 조인)** tiếp nhận điểm tựa từ **6. Sort-Merge phép nối (join / 조인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm (search / 검색)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Nested-Loop phép nối (join / 조인)

Naive nested vòng lặp (loop / 루프) có thể `O(nm)`, nhưng nếu phía ngoài nhỏ và phía trong có chỉ mục (index / 인덱스) lookup rẻ:

```text
for each outer row:
    index lookup inner
```

thì chi phí thực có thể rất tốt.

Do đó tên “hai vòng lặp” không đủ để suy độ phức tạp (complexity / 복잡도); phải nhìn chi phí (cost / 비용) của inner thao tác (operation / 연산).

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **8. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm (search / 검색)** tiếp nhận điểm tựa từ **7. Nested-Loop phép nối (join / 조인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. Cardinality Estimation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm (search / 검색)

Một SQL truy vấn (query / 쿼리) có nhiều:

```text
join order
access path
join algorithm
aggregation strategy
sort placement
```

Không gian plan có thể tăng rất nhanh.

Optimizer dùng động (dynamic / 동적) programming, memoization, pruning và chi phí (cost / 비용) estimation để tìm plan tốt mà không enumerate toàn bộ không gian.

Truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리) tối ưu hóa (optimization / 최적화) là DSA/tìm kiếm (search / 검색) ở cấp hệ thống, không chỉ là rule-based rewriting.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **9. Cardinality Estimation** tiếp nhận điểm tựa từ **8. truy vấn (query / 쿼리) Optimizer là bài toán tìm kiếm (search / 검색)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Buffer Pool** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. Cardinality Estimation

Chi phí (cost / 비용) mô hình (model / 모델) phụ thuộc ước lượng số row trung gian. Nếu estimate sai lớn, optimizer có thể chọn băm (hash / 해시) phép nối (join / 조인) thay vì Nested vòng lặp (loop / 루프) hoặc ngược lại theo cách rất tệ.

Histogram, samples và sketches là các cấu trúc tóm lược để ước lượng phân phối dữ liệu.

Đây là kết nối giữa probabilistic structures và truy vấn (query / 쿼리) planning.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **10. Buffer Pool** tiếp nhận điểm tựa từ **9. Cardinality Estimation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. LRU, LFU và Admission chính sách (policy / 정책)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Buffer Pool

Cơ sở dữ liệu (database / 데이터베이스) giữ page trong RAM để tránh I/O lặp lại.

Buffer manager cần:

```text
pageId -> frame lookup
replacement policy
pin/unpin
Dirty-page tracking
```

Chính xác (exact / 정확한) lookup thường dùng bảng băm (hash table / 해시 테이블). Replacement có thể dùng Clock, LRU-like hoặc chính sách workload-aware.

Một buffer pool là composition giữa **định danh (identity / 식별자) lookup** và **replacement thứ tự (ordering / 순서)/approximation**.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **11. LRU, LFU và Admission chính sách (policy / 정책)** tiếp nhận điểm tựa từ **10. Buffer Pool** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. TTL và Expiration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. LRU, LFU và Admission chính sách (policy / 정책)

LRU chỉ quan tâm recency. LFU quan tâm frequency. Real bộ nhớ đệm (cache / 캐시) thường cần cả hai và còn phải đối phó với scan pollution.

TinyLFU-style designs có thể dùng frequency sketch để quyết định đối tượng (object / 객체) mới có đáng được nhận vào bộ nhớ đệm (cache / 캐시) không.

Một lesson quan trọng:

> eviction và admission là hai quyết định khác nhau.

Không phải mọi đối tượng (object / 객체) vừa được đọc đều đáng đẩy đối tượng (object / 객체) đang hot ra khỏi bộ nhớ đệm (cache / 캐시).

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **12. TTL và Expiration** tiếp nhận điểm tựa từ **11. LRU, LFU và Admission chính sách (policy / 정책)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Write-Ahead Log** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. TTL và Expiration

Bộ nhớ đệm (cache / 캐시) có TTL cần biết item nào hết hạn tiếp theo.

Một vùng nhớ động (heap / 힙) theo expiration thời gian (time / 시간) là cách tự nhiên nhưng delete/cập nhật (update / 업데이트) tùy ý có thể tạo stale entry. Timer wheel hiệu quả hơn khi có rất nhiều timer và độ phân giải thời gian hữu hạn.

Cấu trúc (structure / 구조) phù hợp phụ thuộc:

```text
số timer
độ chính xác thời gian
update/cancel frequency
latency requirement
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **13. Write-Ahead Log** tiếp nhận điểm tựa từ **12. TTL và Expiration** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. LSM cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Write-Ahead Log

WAL là append-oriented cấu trúc (structure / 구조): ghi log trước, sau đó cập nhật page/cấu trúc dữ liệu (data structure / 자료구조).

Append tuần tự thường rẻ hơn random page cập nhật (update / 업데이트) và cung cấp nền tảng khôi phục (recovery / 복구).

Ở đây DSA không thể tách khỏi durability: biểu diễn (representation / 표현) phải cho phép replay/redo sau crash.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **14. LSM cây (tree / 트리)** tiếp nhận điểm tựa từ **13. Write-Ahead Log** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. Bloom Filter trong LSM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. LSM cây (tree / 트리)

LSM cây (tree / 트리) tối ưu ghi (write / 쓰기) đường dẫn (path / 경로) bằng:

```text
WAL
mutable memtable
immutable sorted files
background compaction
```

Memtable có thể là Skip danh sách (list / 목록) hoặc cây (tree / 트리) có thứ tự. SSTable là immutable sorted run. Compaction là repeated multi-way merge.

Sự đánh đổi (trade-off / 트레이드오프):

```text
write nhanh và sequential hơn
đổi lại read amplification + compaction cost
```

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **15. Bloom Filter trong LSM** tiếp nhận điểm tựa từ **14. LSM cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. Compaction và Merge** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. Bloom Filter trong LSM

Mỗi SSTable có thể kèm Bloom Filter.

Nếu filter nói “chắc chắn không có”, engine bỏ qua tệp (file / 파일). False positive chỉ tạo thêm một lần đọc; false negative sẽ phá tính đúng đắn (correctness / 정확성) nên không được phép trong mô hình chuẩn.

Đây là ví dụ rất đẹp của approximate cấu trúc dữ liệu (data structure / 자료구조) được đặt trước chính xác (exact / 정확한) lưu trữ (storage / 저장소) để tối ưu I/O mà không làm sai kết quả cuối.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **16. Compaction và Merge** tiếp nhận điểm tựa từ **15. Bloom Filter trong LSM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. MVCC và Versioned trạng thái (state / 상태)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. Compaction và Merge

Compaction đọc nhiều sorted runs rồi merge thành run mới.

Đây chính là bên ngoài (external / 외부) merge ở quy mô lưu trữ (storage / 저장소) engine, nhưng còn thêm:

```text
tombstone
version
sequence number
snapshot visibility
```

Comparator không chỉ sắp người dùng (user / 사용자) key mà có thể còn sắp theo phiên bản (version / 버전) nội bộ.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **17. MVCC và Versioned trạng thái (state / 상태)** tiếp nhận điểm tựa từ **16. Compaction và Merge** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Filesystem Directory và B-Tree/băm (hash / 해시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. MVCC và Versioned trạng thái (state / 상태)

MVCC giữ nhiều phiên bản (version / 버전) để reader thấy snapshot nhất quán trong khi writer tiếp tục cập nhật.

Conceptually đây là một dạng versioned/persistent trạng thái (state / 상태). lưu trữ (storage / 저장소) engine cần cấu trúc để tìm “phiên bản (version / 버전) mới nhất nhìn thấy được theo snapshot”.

Bài toán không còn chỉ `key -> value`; key lô-gic (logic / 논리) có thêm chiều thời gian/phiên bản (version / 버전).

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **18. Filesystem Directory và B-Tree/băm (hash / 해시)** tiếp nhận điểm tựa từ **17. MVCC và Versioned trạng thái (state / 상태)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **19. Free-Space Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Filesystem Directory và B-Tree/băm (hash / 해시)

Filesystem phải ánh xạ tên tệp (file / 파일) tới inode/siêu dữ liệu (metadata / 메타데이터). Với directory lớn, tuyến tính (linear / 선형) danh sách (list / 목록) quá đắt; hiện thực (implementation / 구현) có thể dùng hashing hoặc tree-indexed structures.

Extent cây (tree / 트리) biểu diễn các vùng khối (block / 블록) liên tiếp thay vì một entry cho từng khối (block / 블록), nén biểu diễn (representation / 표현) bằng cách khai thác tính liên tục.

Đây là ví dụ của **run-length-like structural compression** trong lưu trữ (storage / 저장소) siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **19. Free-Space Management** tiếp nhận điểm tựa từ **18. Filesystem Directory và B-Tree/băm (hash / 해시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **20. Buddy Allocator** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Free-Space Management

Allocator/filesystem cần theo dõi vùng trống.

Có thể dùng:

```text
bitmap
free list
buddy allocator
extent tree
size-segregated lists
```

Lựa chọn phụ thuộc loại truy vấn (query / 쿼리): tìm khối (block / 블록) bất kỳ, khối (block / 블록) đủ lớn, contiguous phạm vi (range / 범위), alignment, merge khi free.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **20. Buddy Allocator** tiếp nhận điểm tựa từ **19. Free-Space Management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. Networking: Routing là đồ thị (graph / 그래프) bài toán (problem / 문제)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. Buddy Allocator

Buddy hệ thống (system / 시스템) chia khối (block / 블록) theo lũy thừa của hai. Khi free hai khối (block / 블록) “buddy” cùng kích thước (size / 크기), có thể merge thành khối (block / 블록) lớn hơn.

Tìm buddy thường dùng XOR theo địa chỉ/chỉ mục (index / 인덱스).

Sự đánh đổi (trade-off / 트레이드오프) là quản lý nhanh nhưng có nội bộ (internal / 내부) fragmentation do làm tròn kích thước (size / 크기).

Đây là một ứng dụng rất thực của power-of-two decomposition.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **21. Networking: Routing là đồ thị (graph / 그래프) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **20. Buddy Allocator** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Longest-Prefix Match** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. Networking: Routing là đồ thị (graph / 그래프) bài toán (problem / 문제)

Topology mạng là đồ thị (graph / 그래프). Link-state giao thức (protocol / 프로토콜) xây bản đồ topology và chạy shortest đường dẫn (path / 경로) kiểu Dijkstra. Distance-vector family có tinh thần Bellman–Ford relaxation giữa hàng xóm.

Nhưng giao thức (protocol / 프로토콜) thật còn có:

```text
policy
convergence
hierarchy
failure recovery
loop prevention
```

Shortest-path thuật toán (algorithm / 알고리즘) chỉ là thành phần nguyên thủy (primitive / 기본 요소) toán học bên dưới.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **22. Longest-Prefix Match** tiếp nhận điểm tựa từ **21. Networking: Routing là đồ thị (graph / 그래프) bài toán (problem / 문제)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Packet Classification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Longest-Prefix Match

Router không chỉ hỏi chính xác (exact / 정확한) key. Nó chọn tuyến (route / 경로) có prefix dài nhất khớp destination address.

Trie, Radix cây (tree / 트리) hoặc Patricia Trie mã hóa prefix relationship trực tiếp.

Hardware có thể dùng TCAM hoặc specialized cấu trúc (structure / 구조), nhưng yêu cầu (requirement / 요구사항) vẫn là prefix tìm kiếm (search / 검색).

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **23. Packet Classification** tiếp nhận điểm tựa từ **22. Longest-Prefix Match** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **24. Packet hàng đợi (queue / 큐) và Scheduling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Packet Classification

Firewall/router có thể phân loại theo nhiều trường:

```text
source/destination prefix
port range
protocol
```

Đây không còn là một trie một chiều đơn giản. Có thể cần cây quyết định (decision tree / 의사결정 트리), multi-dimensional indexing hoặc hardware-specific lookup.

Bài toán cho thấy khi key có nhiều chiều, một chỉ mục (index / 인덱스) đơn chiều có thể không còn đủ.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **24. Packet hàng đợi (queue / 큐) và Scheduling** tiếp nhận điểm tựa từ **23. Packet Classification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **25. Backpressure** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Packet hàng đợi (queue / 큐) và Scheduling

FIFO là baseline. QoS có thể cần priority hàng đợi (queue / 큐), weighted fair scheduling hoặc nhiều hàng đợi (queue / 큐) theo lớp (class / 클래스).

Nếu luôn phục vụ priority cao nhất, traffic thấp priority có thể starvation. Scheduler phải duy trì thêm fairness trạng thái (state / 상태).

Cấu trúc dữ liệu (data structure / 자료구조) chọn “phần tử tiếp theo” chính là chính sách hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **25. Backpressure** tiếp nhận điểm tựa từ **24. Packet hàng đợi (queue / 큐) và Scheduling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. Consistent Hashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Backpressure

Nếu producer nhanh hơn bên tiêu thụ (consumer / 소비자) trong thời gian dài, unbounded hàng đợi (queue / 큐) chỉ trì hoãn sự cố bằng cách tăng bộ nhớ (memory / 메모리) và độ trễ (latency / 지연 시간).

Bounded hàng đợi (queue / 큐) buộc hệ thống chọn:

```text
block
reject
drop
spill
scale consumer
```

Hàng đợi (queue / 큐) sức chứa (capacity / 용량) là một phần của độ tin cậy (reliability / 신뢰성) chính sách (policy / 정책).

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **26. Consistent Hashing** tiếp nhận điểm tựa từ **25. Backpressure** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Rendezvous Hashing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. Consistent Hashing

Nếu ánh xạ (mapping / 매핑) dùng `hash(key) mod N`, thay đổi `N` remap rất nhiều key.

Consistent hashing đặt nút (node / 노드)/key trên một vòng băm (hash / 해시). Khi nút (node / 노드) thêm/bớt, chỉ một vùng keyspace gần vị trí thay đổi cần remap.

Virtual nodes giúp phân phối tải (load / 로드) đều hơn.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **27. Rendezvous Hashing** tiếp nhận điểm tựa từ **26. Consistent Hashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. tải (load / 로드) Balancing và Power of Two Choices** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Rendezvous Hashing

Một lựa chọn khác là tính score cho mỗi `(key,node)` rồi chọn nút (node / 노드) score cao nhất.

Ưu điểm là không cần duy trì vòng; khi nút (node / 노드) set thay đổi, chỉ key có winner thay đổi mới remap.

Consistent hashing và rendezvous hashing đều giải bài **stable partitioning dưới membership thay đổi (change / 변경)** nhưng bằng biểu diễn (representation / 표현) khác nhau.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **28. tải (load / 로드) Balancing và Power of Two Choices** tiếp nhận điểm tựa từ **27. Rendezvous Hashing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. tỷ lệ (rate / 비율) Limiter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. tải (load / 로드) Balancing và Power of Two Choices

Nếu chọn một máy chủ (server / 서버) hoàn toàn ngẫu nhiên, tải (load / 로드) có thể lệch. Một kỹ thuật nổi tiếng là lấy hai candidate ngẫu nhiên rồi chọn máy chủ (server / 서버) nhẹ hơn.

Một thay đổi nhỏ trong selection chính sách (policy / 정책) có thể cải thiện mạnh tail tải (load / 로드) phân phối (distribution / 분포).

Đây là ví dụ randomized thuật toán (algorithm / 알고리즘) xuất hiện trực tiếp trong hệ thống phân tán.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **28. tải (load / 로드) Balancing và Power of Two Choices** đã nêu tiêu chí phân biệt, còn **29. tỷ lệ (rate / 비율) Limiter** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **30. Scheduler của OS** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. tỷ lệ (rate / 비율) Limiter

Đơn vị từ (token / 토큰) Bucket có thể được xem như trạng thái (state / 상태) nhỏ gồm số đơn vị từ (token / 토큰) và timestamp cập nhật cuối. Sliding-window chính xác (exact / 정확한) limiter có thể cần hàng đợi (queue / 큐) timestamp; approximate limiter có thể dùng fixed buckets.

Cùng yêu cầu (requirement / 요구사항) “giới hạn yêu cầu (request / 요청)” có nhiều biểu diễn (representation / 표현) với sự đánh đổi (trade-off / 트레이드오프) precision/bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **29. tỷ lệ (rate / 비율) Limiter** đã nêu tiêu chí phân biệt, còn **30. Scheduler của OS** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **31. Timer Management** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Scheduler của OS

Ready tasks có thể được tổ chức bằng hàng đợi (queue / 큐), priority hàng đợi (queue / 큐), cây (tree / 트리) theo virtual thời gian chạy (runtime / 런타임) hoặc nhiều hàng đợi (queue / 큐) theo priority.

Một scheduler tốt không chỉ tìm tác vụ (task / 작업) priority cao nhất; nó còn phải cân bằng fairness, starvation, locality và preemption chi phí (cost / 비용).

Cấu trúc dữ liệu (data structure / 자료구조) encode chính sách (policy / 정책) chọn tác vụ (task / 작업) tiếp theo.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **31. Timer Management** tiếp nhận điểm tựa từ **30. Scheduler của OS** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **32. Git là DAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 31. Timer Management

Hệ điều hành/thời gian chạy (runtime / 런타임) có hàng nghìn hoặc hàng triệu timer.

Min-heap cho timer sắp hết hạn nhưng cập nhật (update / 업데이트)/cancel có chi phí (cost / 비용) `O(log n)`. Hierarchical timing wheel tận dụng thời gian (time / 시간) buckets để đạt chi phí (cost / 비용) gần hằng số với độ phân giải cố định.

Đây là ví dụ tải công việc (workload / 워크로드) đặc biệt cho phép cấu trúc (structure / 구조) chuyên biệt vượt generic priority hàng đợi (queue / 큐).

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **32. Git là DAG** tiếp nhận điểm tựa từ **31. Timer Management** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **33. hệ thống dựng (build system / 빌드 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 32. Git là DAG

Lần ghi nhận (commit / 커밋) đồ thị (graph / 그래프) của Git là DAG. Merge lần ghi nhận (commit / 커밋) có nhiều parent.

Các thao tác:

```text
ancestor check
merge-base
history traversal
reachability
```

đều là đồ thị (graph / 그래프) queries.

Generation number và commit-graph chỉ mục (index / 인덱스) giúp prune traversal. Bloom-filter-like siêu dữ liệu (metadata / 메타데이터) có thể giảm kiểm tra đường dẫn (path / 경로) lịch sử (history / 이력) trong một số workflow.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **33. hệ thống dựng (build system / 빌드 시스템)** tiếp nhận điểm tựa từ **32. Git là DAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **34. trình biên dịch (compiler / 컴파일러): AST, Symbol bảng (table / 테이블) và CFG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 33. hệ thống dựng (build system / 빌드 시스템)

Phụ thuộc (dependency / 의존성) đồ thị (graph / 그래프) phải acyclic nếu muốn một topological schedule hợp lệ.

Các mục tiêu (target / 대상) có phụ thuộc (dependency / 의존성) đã hoàn tất có thể được đưa vào ready hàng đợi (queue / 큐) và chạy song song.

Hệ thống dựng (build system / 빌드 시스템) thực tế còn bộ nhớ đệm (cache / 캐시) sản phẩm tạo ra (artifact / 산출물) theo content băm (hash / 해시) để tránh rebuild phần không thay đổi.

Ở đây DAG + hashing + memoization kết hợp thành incremental bản dựng (build / 빌드) engine.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **34. trình biên dịch (compiler / 컴파일러): AST, Symbol bảng (table / 테이블) và CFG** tiếp nhận điểm tựa từ **33. hệ thống dựng (build system / 빌드 시스템)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **35. Garbage Collector** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 34. trình biên dịch (compiler / 컴파일러): AST, Symbol bảng (table / 테이블) và CFG

Parser tạo AST — một cây (tree / 트리). Symbol bảng (table / 테이블) dùng băm (hash / 해시) Map hoặc phạm vi (scope / 범위) ngăn xếp (stack / 스택). điều khiển (control / 제어) luồng (flow / 흐름) đồ thị (graph / 그래프) là đồ thị (graph / 그래프). Dominator cây (tree / 트리) và data-flow phân tích (analysis / 분석) dùng các thuật toán đồ thị (graph / 그래프)/bitset/fixpoint.

Trình biên dịch (compiler / 컴파일러) là ví dụ nơi gần như toàn bộ DSA cốt lõi (core / 핵심) xuất hiện trong cùng một chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **35. Garbage Collector** tiếp nhận điểm tựa từ **34. trình biên dịch (compiler / 컴파일러): AST, Symbol bảng (table / 테이블) và CFG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **36. tìm kiếm (search / 검색) Engine Inverted chỉ mục (index / 인덱스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 35. Garbage Collector

Tracing GC bắt đầu từ roots rồi đánh dấu mọi đối tượng (object / 객체) reachable — bản chất là đồ thị (graph / 그래프) traversal.

Generational GC khai thác giả thuyết rằng đối tượng (object / 객체) trẻ thường chết sớm, giảm vùng cần scan thường xuyên.

Remembered set/card bảng (table / 테이블) là cấu trúc phụ để không phải scan toàn vùng nhớ động (heap / 힙) khi tìm tham chiếu (reference / 참조) giữa các thế hệ.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **36. tìm kiếm (search / 검색) Engine Inverted chỉ mục (index / 인덱스)** tiếp nhận điểm tựa từ **35. Garbage Collector** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **37. Full-Text chỉ mục (index / 인덱스) và Suffix/FM Structures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 36. tìm kiếm (search / 검색) Engine Inverted chỉ mục (index / 인덱스)

Thay vì map document -> words, inverted chỉ mục (index / 인덱스) map term -> posting danh sách (list / 목록) document IDs.

Posting danh sách (list / 목록) được sắp xếp, cho phép giao nhiều danh sách bằng merge/two pointers hoặc skip dữ liệu (data / 데이터).

Dictionary term có thể dùng trie/FST. Ranking dùng vùng nhớ động (heap / 힙) cho Top-K. bộ nhớ đệm (cache / 캐시) và compression lại thêm các lớp cấu trúc (structure / 구조) khác.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **37. Full-Text chỉ mục (index / 인덱스) và Suffix/FM Structures** tiếp nhận điểm tựa từ **36. tìm kiếm (search / 검색) Engine Inverted chỉ mục (index / 인덱스)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **38. khả năng quan sát (observability / 관측 가능성) và Sketches** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 37. Full-Text chỉ mục (index / 인덱스) và Suffix/FM Structures

Suffix Array, FM-index hoặc inverted chỉ mục (index / 인덱스) phù hợp các kiểu tìm kiếm (search / 검색) khác nhau.

Inverted chỉ mục (index / 인덱스) mạnh cho đơn vị từ (token / 토큰)/term queries. Suffix structures phù hợp substring/order-based queries. FM-index hỗ trợ compressed substring tìm kiếm (search / 검색).

Chỉ mục (index / 인덱스) phải khớp truy vấn (query / 쿼리) ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **38. khả năng quan sát (observability / 관측 가능성) và Sketches** tiếp nhận điểm tựa từ **37. Full-Text chỉ mục (index / 인덱스) và Suffix/FM Structures** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **39. Top-K trong Streaming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 38. khả năng quan sát (observability / 관측 가능성) và Sketches

Telemetry có cardinality cực lớn. Không thể luôn giữ chính xác (exact / 정확한) set/counter cho mọi key.

HyperLogLog, Count-Min Sketch và heavy-hitter algorithms giúp giữ summary nhỏ.

Sketch có thể merge giữa worker nên rất phù hợp phân tán (distributed / 분산) aggregation.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **39. Top-K trong Streaming** tiếp nhận điểm tựa từ **38. khả năng quan sát (observability / 관측 가능성) và Sketches** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **40. bộ nhớ (memory / 메모리) Allocator và Free danh sách (list / 목록)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 39. Top-K trong Streaming

Nếu muốn giữ các chỉ số (metric / 지표) lớn nhất liên tục, có thể dùng min-heap kích thước (size / 크기) `k`. Nếu keyspace quá lớn và muốn heavy hitters approximate, Count-Min Sketch + candidate vùng nhớ động (heap / 힙) là composition phổ biến.

Chính xác (exact / 정확한) và approximate cấu trúc (structure / 구조) có thể phối hợp nhiều tầng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **40. bộ nhớ (memory / 메모리) Allocator và Free danh sách (list / 목록)** tiếp nhận điểm tựa từ **39. Top-K trong Streaming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **41. Lock-Free Structures** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 40. bộ nhớ (memory / 메모리) Allocator và Free danh sách (list / 목록)

Allocator có thể dùng kích thước (size / 크기) classes, bins, cây (tree / 트리) hoặc bitmap để tìm khối (block / 블록) phù hợp.

Một allocator tốt phải cân bằng:

```text
allocation latency
fragmentation
concurrency
cache locality
metadata overhead
```

Đây là data-structure selection dưới ràng buộc cực thấp cấp.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **41. Lock-Free Structures** tiếp nhận điểm tựa từ **40. bộ nhớ (memory / 메모리) Allocator và Free danh sách (list / 목록)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **42. Crash Consistency** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 41. Lock-Free Structures

Lock-free ngăn xếp (stack / 스택)/hàng đợi (queue / 큐) thường dùng atomic CAS. Nhưng tính đúng đắn (correctness / 정확성) không chỉ nằm ở shape của ngăn xếp (stack / 스택)/hàng đợi (queue / 큐) mà còn ở:

```text
memory ordering
ABA
safe reclamation
linearization point
```

Hazard pointer hoặc epoch reclamation là cấu trúc/phương thức quản lý thời gian tồn tại (lifetime / 수명) đi kèm.

DSA concurrent là DSA + bộ nhớ (memory / 메모리) mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **42. Crash Consistency** tiếp nhận điểm tựa từ **41. Lock-Free Structures** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **43. Merkle cây (tree / 트리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 42. Crash Consistency

Persistent cấu trúc dữ liệu (data structure / 자료구조) phải sống qua tiến trình (process / 프로세스) crash, không chỉ qua hàm (function / 함수) lời gọi (call / 호출).

Một cập nhật (update / 업데이트) nhiều bước có thể để lưu trữ (storage / 저장소) ở trạng thái nửa cũ nửa mới. WAL, sao chép khi ghi (copy-on-write / 쓰기 시 복사) hoặc shadow paging tạo giao thức (protocol / 프로토콜) để có một lần ghi nhận (commit / 커밋) điểm (point / 지점) rõ ràng.

Đây là phiên bản persistence của transactional cập nhật (update / 업데이트) bất biến (invariant / 불변식).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **43. Merkle cây (tree / 트리)** tiếp nhận điểm tựa từ **42. Crash Consistency** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **44. Bloom Filter, Merkle cây (tree / 트리) và chỉ mục (index / 인덱스) giải các câu hỏi khác nhau** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 43. Merkle cây (tree / 트리)

Merkle cây (tree / 트리) băm (hash / 해시) mỗi nút (node / 노드) từ băm (hash / 해시) của các con. gốc (root / 루트) băm (hash / 해시) cam kết toàn bộ nội dung cây.

Ứng dụng:

```text
content verification
replication comparison
blockchain structures
versioned storage
```

Proof đường dẫn (path / 경로) chỉ cần `O(log n)` băm (hash / 해시) để chứng minh một leaf thuộc cây (tree / 트리) cân bằng.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **44. Bloom Filter, Merkle cây (tree / 트리) và chỉ mục (index / 인덱스) giải các câu hỏi khác nhau** tiếp nhận điểm tựa từ **43. Merkle cây (tree / 트리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **45. Hệ thống thực tế tối ưu dữ liệu (data / 데이터) movement** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 44. Bloom Filter, Merkle cây (tree / 트리) và chỉ mục (index / 인덱스) giải các câu hỏi khác nhau

Bloom Filter: “chắc chắn không có hay có thể có?”.

Merkle cây (tree / 트리): “hai tập dữ liệu có cùng nội dung/nhánh này có thuộc snapshot không?”.

B+cây (tree / 트리): “key này nằm ở đâu, phạm vi (range / 범위) này gồm gì?”.

Cả ba đều là siêu dữ liệu (metadata / 메타데이터) structures nhưng phục vụ ngữ nghĩa (semantic / 의미적) hoàn toàn khác.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **44. Bloom Filter, Merkle cây (tree / 트리) và chỉ mục (index / 인덱스) giải các câu hỏi khác nhau** nêu điều cần giải thích; **45. Hệ thống thực tế tối ưu dữ liệu (data / 데이터) movement** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **46. Một trường hợp (case / 사례) study: Read đường dẫn (path / 경로) của Key-Value Store** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 45. Hệ thống thực tế tối ưu dữ liệu (data / 데이터) movement

CPU thao tác (operation / 연산) thường rẻ hơn trượt bộ nhớ đệm (cache miss / 캐시 미스), page I/O hoặc mạng (network / 네트워크) round trip nhiều bậc độ lớn.

Vì vậy cấu trúc dữ liệu (data structure / 자료구조) hiệu năng (performance / 성능) trong môi trường vận hành (production / 운영 환경) thường bị chi phối bởi:

```text
bytes moved
cache lines touched
pages read
RPCs sent
allocations created
locks contended
```

Không nên dừng phân tích ở số comparison.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **45. Hệ thống thực tế tối ưu dữ liệu (data / 데이터) movement** cho ta quy tắc; **46. Một trường hợp (case / 사례) study: Read đường dẫn (path / 경로) của Key-Value Store** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **47. Một trường hợp (case / 사례) study: Scheduler** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 46. Một trường hợp (case / 사례) study: Read đường dẫn (path / 경로) của Key-Value Store

Có thể hình dung:

```text
request
 -> routing hash
 -> in-memory cache
 -> Bloom filters
 -> memtable / index lookup
 -> SSTable page read
 -> decompression
 -> value return
```

Mỗi tầng dùng cấu trúc (structure / 구조) khác để giảm chi phí tầng tiếp theo.

Câu hỏi kiến trúc là: **lọc càng sớm càng tốt bằng siêu dữ liệu (metadata / 메타데이터) rẻ hơn có đáng không?**

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **46. Một trường hợp (case / 사례) study: Read đường dẫn (path / 경로) của Key-Value Store** cho ta quy tắc; **47. Một trường hợp (case / 사례) study: Scheduler** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **48. Từ DSA sang hệ thống (system / 시스템) thiết kế (design / 설계)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 47. Một trường hợp (case / 사례) study: Scheduler

Scheduler có:

```text
ready set
priority/fairness metadata
timer queue
CPU affinity state
```

Một vùng nhớ động (heap / 힙) duy nhất hiếm khi đủ. Có thể cần cây (tree / 트리) theo virtual thời gian chạy (runtime / 런타임), hàng đợi (queue / 큐) theo lớp (class / 클래스), bitmap để tìm priority có tác vụ (task / 작업) và timer wheel cho wake-up.

Môi trường vận hành (production / 운영 환경) DSA thường là composition theo nhiều truy vấn (query / 쿼리) cùng lúc.

> **Chuyển mạch:** Ở chặng này của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **47. Một trường hợp (case / 사례) study: Scheduler** cho ta quy tắc; **48. Từ DSA sang hệ thống (system / 시스템) thiết kế (design / 설계)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **49. Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 48. Từ DSA sang hệ thống (system / 시스템) thiết kế (design / 설계)

Khi nhìn một subsystem, hãy hỏi:

```text
state nào được giữ?
query nào hot nhất?
metadata nào đang được materialize?
update phải duy trì invariant nào?
chi phí thật là CPU, memory, I/O hay network?
điều gì xảy ra khi crash/concurrent update?
```

Đây là cùng workflow của DSA nhưng mở rộng sang hệ thống.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **49. Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **48. Từ DSA sang hệ thống (system / 시스템) thiết kế (design / 설계)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 49. Những hiểu lầm phổ biến

“cơ sở dữ liệu (database / 데이터베이스) dùng B+cây (tree / 트리) chỉ vì `O(log n)`” — bỏ qua page I/O và fan-out.

“bộ nhớ đệm (cache / 캐시) chỉ cần HashMap” — còn eviction, admission, TTL và tính đồng thời (concurrency / 동시성).

“Routing chỉ là Dijkstra” — giao thức (protocol / 프로토콜) còn chính sách (policy / 정책)/convergence/thất bại (failure / 실패) handling.

“GC tự quản bộ nhớ nên không liên quan DSA” — tracing chính là đồ thị (graph / 그래프) reachability.

“hệ thống phân tán (distributed system / 분산 시스템) không còn liên quan cấu trúc dữ liệu” — partitioning, queues, sketches, logs và indexes đều là DSA ở quy mô khác.

> **Chuyển mạch:** Trong **DSA trong cơ sở dữ liệu, mạng và hệ thống**, **Mô hình tư duy** gom các mảnh từ **49. Những hiểu lầm phổ biến** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Trong hệ thống thực tế, DSA là cách **materialize đúng siêu dữ liệu (metadata / 메타데이터) để tránh công việc đắt hơn ở tầng dưới**.

B+cây (tree / 트리) giữ thứ tự (order / 순서) để tránh nhiều page I/O. Bloom Filter giữ dấu vết membership để tránh đọc tệp (file / 파일). bộ nhớ đệm (cache / 캐시) giữ dữ liệu hot để tránh backend truy cập (access / 접근). băm (hash / 해시) ring giữ partition siêu dữ liệu (metadata / 메타데이터) để hạn chế remapping. Timer wheel giữ bucket thời gian để tránh vùng nhớ động (heap / 힙) thao tác (operation / 연산) cho hàng triệu timer.

Khi gặp một subsystem, đừng chỉ hỏi “nó dùng cấu trúc dữ liệu (data structure / 자료구조) gì?”. Hãy hỏi: **truy vấn (query / 쿼리) nào đang được tăng tốc, bất biến (invariant / 불변식) nào phải trả giá để duy trì, và tầng tài nguyên đắt nhất đang được tránh là CPU, trượt bộ nhớ đệm (cache miss / 캐시 미스), disk I/O hay mạng (network / 네트워크) round-trip?**

Xem thêm: [Choose the Right Data Structure](./00_choose_the_right_data_structure.md), [B/B+Tree](../02_trees/05_b_trees_and_external_memory.md), [Hash Tables](../01_linear_structures/04_hash_tables.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Graph Algorithms](../03_graphs/_index.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
