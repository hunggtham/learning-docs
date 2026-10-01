# Chọn cấu trúc dữ liệu phù hợp

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Chọn cấu trúc dữ liệu phù hợp**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **1. Bắt đầu từ thao tác** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **2. chính xác (exact / 정확한) Lookup hay Ordered truy vấn (query / 쿼리)?** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**cấu trúc dữ liệu (data structure / 자료구조) Selection / 자료구조 선택**

Chọn cấu trúc dữ liệu không phải là nhớ một bảng “bài này dùng cấu trúc nào”, mà là quá trình biến yêu cầu thành **khối lượng công việc (workload)** rồi chọn cách biểu diễn phù hợp nhất với khối lượng công việc đó.

Một cấu trúc chỉ “tốt” khi:

```text
các thao tác quan trọng đủ rẻ
bất biến cần thiết được duy trì đúng
bộ nhớ nằm trong ngân sách
độ trễ và thông lượng phù hợp SLA
cách triển khai đủ đơn giản để vận hành và kiểm thử
```

Không có cấu trúc “nhanh nhất” theo nghĩa tuyệt đối. Mảng, bảng băm, cây, vùng nhớ động (heap / 힙) hay trie chỉ tốt trong một mô hình truy cập cụ thể.

## 1. Bắt đầu từ thao tác

Đừng hỏi “HashMap hay TreeMap?”. Hãy viết các thao tác thật:

```text
lookup(key)
insert(key, value)
delete(key)
min()
max()
predecessor(key)
successor(key)
rangeQuery(l, r)
prefixSearch(prefix)
rank(key)
select(k)
connect(a, b)
sameComponent(a, b)
```

Sau đó đánh dấu thao tác nào chiếm phần lớn lưu lượng và thao tác nào nằm trên đường chạy nóng.

Một thao tác khởi tạo chạy một lần không cần được tối ưu giống thao tác chạy hàng triệu lần mỗi giây.

> **Chuyển mạch:** Start from operations and workload: exact lookup favors hashing, ordered/range queries favor trees, then static versus dynamic updates determines memory and maintenance cost.

## 2. chính xác (exact / 정확한) Lookup hay Ordered truy vấn (query / 쿼리)?

Nếu chỉ cần equality lookup, bảng băm (hash table / 해시 테이블) thường là ứng viên tự nhiên:

```text
get / put / contains -> expected O(1)
```

Nếu cần:

```text
min / max
floor / ceiling
predecessor / successor
range scan
ordered iteration
```

thì thứ tự là một phần của bài toán. Balanced BST hoặc B+cây (tree / 트리) thường hợp lý hơn.

Nếu dữ liệu tĩnh, sorted array có thể còn tốt hơn cây vì tìm kiếm `O(log n)`, bộ nhớ gọn và locality tốt.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **3. Static hay động (dynamic / 동적)?** tiếp nhận điểm tựa từ **2. chính xác (exact / 정확한) Lookup hay Ordered truy vấn (query / 쿼리)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **4. Read/ghi (write / 쓰기) Ratio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3. Static hay động (dynamic / 동적)?

Dữ liệu tĩnh cho phép tiền xử lý mạnh.

Ví dụ:

```text
static range sum       -> prefix sum
dynamic point update   -> Fenwick / Segment Tree
static RMQ             -> Sparse Table
dynamic ordered set    -> balanced BST
```

Một câu hỏi rất mạnh:

> Ta có thể trả một khoản chi phí xây dựng trước để làm hàng nghìn truy vấn sau rẻ hơn không?

Nếu câu trả lời là có, hãy nghĩ tới sorting, indexing, prefix structures hoặc preprocessing đồ thị (graph / 그래프)/string.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **4. Read/ghi (write / 쓰기) Ratio** tiếp nhận điểm tựa từ **3. Static hay động (dynamic / 동적)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **5. Dense hay Sparse Key không gian (space / 공간)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 4. Read/ghi (write / 쓰기) Ratio

Hai hệ thống chứa cùng dữ liệu nhưng tỷ lệ đọc/ghi khác nhau có thể cần cấu trúc khác.

Một chỉ mục (index / 인덱스) làm đọc nhanh hơn nhưng mọi ghi (write / 쓰기) phải duy trì chỉ mục (index / 인덱스). Một bộ nhớ đệm (cache / 캐시) làm đọc nhanh nhưng phải trả chi phí vô hiệu hóa (invalidation / 무효화)/freshness. Một LSM cây (tree / 트리) tối ưu đường ghi tuần tự nhưng tăng read/compaction độ phức tạp (complexity / 복잡도).

Cấu trúc dữ liệu (data structure / 자료구조) selection luôn là bài toán **đẩy chi phí từ thao tác này sang thao tác khác**.

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **5. Dense hay Sparse Key không gian (space / 공간)?** tiếp nhận điểm tựa từ **4. Read/ghi (write / 쓰기) Ratio** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **6. Contiguous bộ nhớ (memory / 메모리) hay Node-Based cấu trúc (structure / 구조)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 5. Dense hay Sparse Key không gian (space / 공간)?

Nếu key là số nguyên dày đặc `0..n-1`, mảng thường tốt hơn HashMap:

```text
count[id]
visited[id]
dist[id]
```

Nếu key thưa, lớn hoặc là chuỗi/đối tượng (object / 객체), HashMap phù hợp hơn.

Không nên dùng cấu trúc tổng quát khi miền khóa đã cho phép direct addressing rẻ hơn.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **6. Contiguous bộ nhớ (memory / 메모리) hay Node-Based cấu trúc (structure / 구조)?** tiếp nhận điểm tựa từ **5. Dense hay Sparse Key không gian (space / 공간)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **7. Min/Max liên tục hay Full thứ tự (order / 순서)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 6. Contiguous bộ nhớ (memory / 메모리) hay Node-Based cấu trúc (structure / 구조)?

Mảng có locality tốt, ít siêu dữ liệu (metadata / 메타데이터) và traversal nhanh. Cấu trúc node-based linh hoạt hơn cho relinking nhưng phải trả giá cho pointer/tham chiếu (reference / 참조), allocation và trượt bộ nhớ đệm (cache miss / 캐시 미스).

Ví dụ Linked danh sách (list / 목록) có thể xóa nút (node / 노드) `O(1)` khi đã có nút (node / 노드), nhưng tìm vị trí vẫn `O(n)` và traversal thường chậm hơn mảng.

Big-O không mô tả đầy đủ bộ nhớ (memory / 메모리) hierarchy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **7. Min/Max liên tục hay Full thứ tự (order / 순서)?** tiếp nhận điểm tựa từ **6. Contiguous bộ nhớ (memory / 메모리) hay Node-Based cấu trúc (structure / 구조)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **8. Prefix hay Full-Key Equality?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 7. Min/Max liên tục hay Full thứ tự (order / 순서)?

Nếu chỉ cần phần tử nhỏ nhất/lớn nhất lặp lại, vùng nhớ động (heap / 힙) thường đủ:

```text
peek min O(1)
insert O(log n)
extract min O(log n)
```

Không cần trả chi phí duy trì full sorted thứ tự (order / 순서) của TreeMap.

Nếu cần cả predecessor/phạm vi (range / 범위) scan, vùng nhớ động (heap / 힙) không đủ.

Một nguyên tắc quan trọng:

> Chỉ duy trì lượng thứ tự tối thiểu đủ để trả lời truy vấn (query / 쿼리).

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **8. Prefix hay Full-Key Equality?** tiếp nhận điểm tựa từ **7. Min/Max liên tục hay Full thứ tự (order / 순서)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **9. phạm vi (range / 범위) truy vấn (query / 쿼리) yêu cầu phép toán gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 8. Prefix hay Full-Key Equality?

Nếu tải công việc (workload / 워크로드) hỏi prefix:

```text
autocomplete
routing prefix
string dictionary
```

Trie/Radix cây (tree / 트리) có thể trực tiếp mã hóa prefix cấu trúc (structure / 구조).

Nếu chỉ cần chính xác (exact / 정확한) string lookup, HashMap có thể đơn giản hơn và gọn hơn.

Cấu trúc (structure / 구조) mạnh là cấu trúc (structure / 구조) lưu đúng loại thông tin mà truy vấn (query / 쿼리) cần.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **9. phạm vi (range / 범위) truy vấn (query / 쿼리) yêu cầu phép toán gì?** tiếp nhận điểm tựa từ **8. Prefix hay Full-Key Equality?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **10. Mutable hay Persistent?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 9. phạm vi (range / 범위) truy vấn (query / 쿼리) yêu cầu phép toán gì?

Không phải mọi phạm vi (range / 범위) cấu trúc (structure / 구조) hỗ trợ mọi aggregate.

Prefix sum dựa trên khả năng “trừ phần trước”. Fenwick cây (tree / 트리) phù hợp các phép toán có cấu trúc đại số thích hợp. Segment cây (tree / 트리) chỉ cần phép combine có tính kết hợp. Sparse bảng (table / 테이블) đặc biệt mạnh với static idempotent thao tác (operation / 연산) như `min/max/gcd`.

Vì vậy trước khi chọn cấu trúc (structure / 구조) hãy hỏi:

```text
operation có associative không?
có identity không?
có inverse không?
có idempotent không?
update là point hay range?
query là prefix hay arbitrary interval?
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **10. Mutable hay Persistent?** tiếp nhận điểm tựa từ **9. phạm vi (range / 범위) truy vấn (query / 쿼리) yêu cầu phép toán gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **11. chính xác (exact / 정확한) hay Approximate?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 10. Mutable hay Persistent?

Nếu chỉ cần trạng thái hiện tại, mutable cấu trúc (structure / 구조) thường đơn giản và tiết kiệm allocation.

Nếu cần:

```text
undo/versioning
snapshot
branching histories
functional semantics
```

persistent cấu trúc (structure / 구조) với structural sharing có thể phù hợp.

Persistent không có nghĩa “lưu xuống disk”; nó có nghĩa phiên bản cũ vẫn dùng được sau cập nhật (update / 업데이트).

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **11. chính xác (exact / 정확한) hay Approximate?** tiếp nhận điểm tựa từ **10. Mutable hay Persistent?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **12. Online hay Offline?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 11. chính xác (exact / 정확한) hay Approximate?

Nếu dữ liệu quá lớn, có thể không cần lưu trạng thái chính xác cho mọi key.

```text
membership approximate     -> Bloom/Cuckoo/XOR Filter
cardinality approximate    -> HyperLogLog
frequency approximate      -> Count-Min Sketch
similarity approximate     -> MinHash
```

Nhưng approximation chỉ hợp lệ nếu nghiệp vụ chấp nhận lỗi (error / 오류) mô hình (model / 모델).

Một Bloom Filter có false positive nhưng không false negative trong mô hình chuẩn có thể rất tốt làm bộ lọc I/O, nhưng không nên là nguồn sự thật cho authorization.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **12. Online hay Offline?** tiếp nhận điểm tựa từ **11. chính xác (exact / 정확한) hay Approximate?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **13. Ordered Array hay Balanced cây (tree / 트리)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 12. Online hay Offline?

Nếu phải trả lời ngay khi dữ liệu đến, chỉ dùng thông tin quá khứ. Nếu có thể giữ toàn bộ đầu vào (input / 입력) rồi reorder, nhiều thuật toán offline mạnh hơn.

Ví dụ:

```text
sweep line
Kruskal + query sorting
Mo's algorithm
batch processing
```

Offline processing có thể đổi thứ tự sự kiện (event / 이벤트) để giảm công việc (work / 작업). Online hệ thống (system / 시스템) không có quyền đó.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **13. Ordered Array hay Balanced cây (tree / 트리)?** tiếp nhận điểm tựa từ **12. Online hay Offline?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **14. vùng nhớ động (heap / 힙) hay Sorted cấu trúc (structure / 구조) cho Top-K?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 13. Ordered Array hay Balanced cây (tree / 트리)?

Nếu dữ liệu ít thay đổi:

```text
sorted array
+ binary search
+ sequential range scan
```

có locality và bộ nhớ (memory / 메모리) footprint rất tốt.

Nếu insert/delete liên tục ở vị trí tùy ý, balanced cây (tree / 트리) tránh `O(n)` dịch phần tử.

Không nên chọn cây (tree / 트리) chỉ vì “tìm kiếm (search / 검색) O(log n)” nếu tải công việc (workload / 워크로드) thực tế gần tĩnh.

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **14. vùng nhớ động (heap / 힙) hay Sorted cấu trúc (structure / 구조) cho Top-K?** tiếp nhận điểm tựa từ **13. Ordered Array hay Balanced cây (tree / 트리)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **15. đồ thị (graph / 그래프) biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 14. vùng nhớ động (heap / 힙) hay Sorted cấu trúc (structure / 구조) cho Top-K?

Nếu cần Top-K một lần từ batch dữ liệu:

```text
Quickselect
partial sort
heap size k
full sort
```

đều có thể hợp lý tùy `k`, `n` và yêu cầu thứ tự đầu ra.

Nếu dữ liệu đến liên tục, vùng nhớ động (heap / 힙) kích thước (size / 크기) `k` tự nhiên hơn.

Nếu cần truy vấn rank động cho nhiều `k`, order-statistic cây (tree / 트리) có thể phù hợp hơn.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **15. đồ thị (graph / 그래프) biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **14. vùng nhớ động (heap / 힙) hay Sorted cấu trúc (structure / 구조) cho Top-K?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **16. DSU chỉ tốt khi bài toán đúng mô hình merge-only** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 15. đồ thị (graph / 그래프) biểu diễn (representation / 표현)

Đồ thị thưa thường dùng adjacency danh sách (list / 목록):

\[
O(V+E)
\]

Đồ thị dày có thể dùng adjacency ma trận (matrix / 행렬) nếu cần edge lookup cực nhanh và `V²` bộ nhớ (memory / 메모리) chấp nhận được.

Nếu đồ thị (graph / 그래프) tĩnh rất lớn, CSR giúp giảm overhead đối tượng (object / 객체) và tăng locality.

Biểu diễn (representation / 표현) đồ thị (graph / 그래프) quyết định cả bộ nhớ (memory / 메모리) lẫn độ phức tạp (complexity / 복잡도) của traversal.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **16. DSU chỉ tốt khi bài toán đúng mô hình merge-only** tiếp nhận điểm tựa từ **15. đồ thị (graph / 그래프) biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **17. Bounded bộ nhớ (memory / 메모리) hay Unbounded Growth?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 16. DSU chỉ tốt khi bài toán đúng mô hình merge-only

DSU hỗ trợ rất tốt:

```text
union(a,b)
find(a)
sameComponent(a,b)
```

nhưng không hỗ trợ split/delete edge tổng quát.

Nếu đồ thị (graph / 그래프) connectivity thay đổi bằng cả add và remove, cần offline reversal, quay lui (rollback / 롤백) DSU hoặc động (dynamic / 동적) connectivity cấu trúc (structure / 구조) phức tạp hơn.

Cấu trúc (structure / 구조) nhanh thường nhanh vì nó **không hỗ trợ một số thao tác khó**.

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **17. Bounded bộ nhớ (memory / 메모리) hay Unbounded Growth?** tiếp nhận điểm tựa từ **16. DSU chỉ tốt khi bài toán đúng mô hình merge-only** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **18. Worst-Case hay Expected Guarantee?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 17. Bounded bộ nhớ (memory / 메모리) hay Unbounded Growth?

Hàng đợi (queue / 큐) không giới hạn có thể che giấu overload cho tới khi hệ thống hết bộ nhớ (memory / 메모리). Ring buffer bounded bắt hệ thống chọn chính sách (policy / 정책) khi đầy:

```text
block
drop
reject
spill
backpressure
```

Cấu trúc dữ liệu (data structure / 자료구조) sức chứa (capacity / 용량) là một quyết định độ tin cậy (reliability / 신뢰성), không chỉ hiện thực (implementation / 구현) detail.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **17. Bounded bộ nhớ (memory / 메모리) hay Unbounded Growth?** cho ta quy tắc; **18. Worst-Case hay Expected Guarantee?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **19. Amortized hay Per-Operation độ trễ (latency / 지연 시간)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 18. Worst-Case hay Expected Guarantee?

Bảng băm (hash table / 해시 테이블), Skip danh sách (list / 목록) và randomized algorithms thường có expected bound tốt. Balanced cây (tree / 트리) cho deterministic `O(log n)`.

Nếu tải công việc (workload / 워크로드) có thể đối nghịch hoặc tail độ trễ (latency / 지연 시간) quan trọng, deterministic bound có thể đáng giá hơn constant factor trung bình tốt.

Nếu thông lượng (throughput / 처리량) là mục tiêu chính, expected/amortized thiết kế (design / 설계) đơn giản hơn có thể thắng.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **18. Worst-Case hay Expected Guarantee?** cho ta quy tắc; **19. Amortized hay Per-Operation độ trễ (latency / 지연 시간)?** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **20. bên ngoài (external / 외부) bộ nhớ (memory / 메모리)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 19. Amortized hay Per-Operation độ trễ (latency / 지연 시간)?

Động (dynamic / 동적) array append `O(1)` amortized nhưng một resize riêng có thể `O(n)`. bảng băm (hash table / 해시 테이블) resize tương tự.

Hệ thống real-time có thể cần:

```text
preallocation
incremental resize
deamortized structure
bounded buffer
```

Đừng xóa từ “amortized” khi mô tả SLA.

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **20. bên ngoài (external / 외부) bộ nhớ (memory / 메모리)** tiếp nhận điểm tựa từ **19. Amortized hay Per-Operation độ trễ (latency / 지연 시간)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **21. tính đồng thời (concurrency / 동시성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 20. bên ngoài (external / 외부) bộ nhớ (memory / 메모리)

Khi dữ liệu vượt RAM, số page I/O quan trọng hơn số comparison.

B+cây (tree / 트리) có fan-out lớn để giảm chiều cao. bên ngoài (external / 외부) Merge Sort dùng sequential I/O. LSM cây (tree / 트리) chuyển random ghi (write / 쓰기) thành sequential append + background compaction.

Cấu trúc dữ liệu (data structure / 자료구조) phải khớp tầng lưu trữ thực tế.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **21. tính đồng thời (concurrency / 동시성)** tiếp nhận điểm tựa từ **20. bên ngoài (external / 외부) bộ nhớ (memory / 메모리)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **22. Composition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 21. tính đồng thời (concurrency / 동시성)

Một cấu trúc (structure / 구조) tốt single-thread chưa chắc tốt multi-thread.

Cần hỏi:

```text
read-heavy hay write-heavy?
contention tập trung ở đâu?
lock granularity thế nào?
cần linearizability không?
iterator/snapshot semantics là gì?
```

ConcurrentHashMap không chỉ là HashMap “nhanh hơn”; nó có đặc tả hợp đồng (contract / 계약) đồng thời khác.

Lock-free cấu trúc (structure / 구조) thêm vấn đề ABA, bộ nhớ (memory / 메모리) reclamation và thứ tự (ordering / 순서).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **22. Composition** tiếp nhận điểm tựa từ **21. tính đồng thời (concurrency / 동시성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **23. Đừng nhân đôi nguồn sự thật nếu không cần** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 22. Composition

Hệ thống thực tế thường ghép nhiều cấu trúc (structure / 구조).

### LRU bộ nhớ đệm (cache / 캐시)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
HashMap       -> tìm node theo key
Doubly List   -> recency order
```

### Dijkstra

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
adjacency list
+ distance array/map
+ priority queue
```

### Truy vấn cơ sở dữ liệu (database query / 데이터베이스 쿼리) Engine

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
B+Tree / Hash Index
+ Buffer Pool
+ Hash Join / Sort-Merge Join
+ Heap cho Top-N
```

### Autocomplete

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Trie/Radix index
+ ranking metadata
+ heap/top-k cache
```

Điểm khó không chỉ là từng cấu trúc (structure / 구조) mà là **bất biến liên cấu trúc**.

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **22. Composition** nêu điều cần giải thích; **23. Đừng nhân đôi nguồn sự thật nếu không cần** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **24. Một quyết định (decision / 결정) ma trận (matrix / 행렬) thực dụng** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 23. Đừng nhân đôi nguồn sự thật nếu không cần

Nếu cùng một dữ liệu được lưu trong map và danh sách (list / 목록), cần bảo đảm hai biểu diễn (representation / 표현) luôn đồng bộ.

Mỗi secondary chỉ mục (index / 인덱스), bộ nhớ đệm (cache / 캐시) hoặc siêu dữ liệu (metadata / 메타데이터) tăng tốc truy vấn (query / 쿼리) nhưng đồng thời tạo thêm bất biến (invariant / 불변식) phải duy trì.

Một cấu trúc (structure / 구조) phụ chỉ đáng có nếu lợi ích truy vấn (query / 쿼리) lớn hơn chi phí (cost / 비용) cập nhật (update / 업데이트), bộ nhớ (memory / 메모리) và độ phức tạp (complexity / 복잡도) vận hành.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **23. Đừng nhân đôi nguồn sự thật nếu không cần** nêu điều cần giải thích; **24. Một quyết định (decision / 결정) ma trận (matrix / 행렬) thực dụng** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **25. Từ yêu cầu tới chi phí (cost / 비용) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 24. Một quyết định (decision / 결정) ma trận (matrix / 행렬) thực dụng

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

| Câu hỏi | Nếu “có”, hãy nghĩ tới |
|---|---|
| key dày đặc dạng integer? | array / bitset |
| equality lookup là chính? | bảng băm (hash table / 해시 테이블) |
| cần ordered/phạm vi (range / 범위) truy vấn (query / 쿼리)? | sorted array / balanced cây (tree / 트리) / B+cây (tree / 트리) |
| cần min/max liên tục? | vùng nhớ động (heap / 힙) |
| cần prefix? | trie / radix cây (tree / 트리) |
| dữ liệu tĩnh, nhiều phạm vi (range / 범위) truy vấn (query / 쿼리)? | prefix / sparse bảng (table / 테이블) |
| có cập nhật (update / 업데이트) + aggregate? | Fenwick / Segment cây (tree / 트리) |
| chỉ merge connectivity? | DSU |
| văn bản (text / 텍스트) cần substring chỉ mục (index / 인덱스)? | suffix structures / automata |
| dữ liệu vượt RAM? | B+cây (tree / 트리) / bên ngoài (external / 외부) sort / LSM concepts |
| bộ nhớ (memory / 메모리) cực hạn, chấp nhận sai số? | probabilistic structures |

Bảng chỉ là điểm khởi đầu. Quyết định cuối phải dựa trên tải công việc (workload / 워크로드).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **25. Từ yêu cầu tới chi phí (cost / 비용) mô hình (model / 모델)** tiếp nhận điểm tựa từ **24. Một quyết định (decision / 결정) ma trận (matrix / 행렬) thực dụng** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **26. di chuyển (migration / 마이그레이션) tín hiệu (signal / 신호)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 25. Từ yêu cầu tới chi phí (cost / 비용) mô hình (model / 모델)

Một cách formal hơn là viết:

\[
ExpectedCost = \sum_i p_i C_i
\]

với `p_i` là tỷ lệ thao tác và `C_i` là chi phí tương ứng.

Sau đó cộng thêm bộ nhớ (memory / 메모리) chi phí (cost / 비용), độ trễ (latency / 지연 시간) yêu cầu (requirement / 요구사항) và hiện thực (implementation / 구현) độ phức tạp (complexity / 복잡도).

Không cần luôn tính ra con số chính xác; mục tiêu là tránh tối ưu một thao tác hiếm mà bỏ qua thao tác chi phối.

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **26. di chuyển (migration / 마이그레이션) tín hiệu (signal / 신호)** tiếp nhận điểm tựa từ **25. Từ yêu cầu tới chi phí (cost / 비용) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **27. Benchmark đúng tải công việc (workload / 워크로드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 26. di chuyển (migration / 마이그레이션) tín hiệu (signal / 신호)

Cấu trúc (structure / 구조) đúng hôm nay có thể sai sau khi tải công việc (workload / 워크로드) thay đổi.

Dấu hiệu cần xem lại:

```text
n tăng 100 lần
read/write ratio đổi mạnh
range query xuất hiện nhiều hơn
GC/allocation trở thành bottleneck
p99 latency tăng do resize
memory vượt budget
concurrency contention tăng
```

Cấu trúc dữ liệu (data structure / 자료구조) selection là quyết định có thể cần tái đánh giá, không phải lựa chọn một lần mãi mãi.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **27. Benchmark đúng tải công việc (workload / 워크로드)** tiếp nhận điểm tựa từ **26. di chuyển (migration / 마이그레이션) tín hiệu (signal / 신호)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **28. Chọn cấu trúc (structure / 구조) đơn giản nhất đáp ứng yêu cầu** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 27. Benchmark đúng tải công việc (workload / 워크로드)

Không benchmark HashMap với random integer rồi suy ra hiệu năng (performance / 성능) cho key dài, expensive băm (hash / 해시) hoặc adversarial phân phối (distribution / 분포).

Không benchmark TreeMap chỉ bằng lookup nếu môi trường vận hành (production / 운영 환경) tải công việc (workload / 워크로드) có phạm vi (range / 범위) scan lớn.

Benchmark phải phản ánh:

```text
data size
key distribution
operation mix
mutation pattern
concurrency
memory pressure
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **28. Chọn cấu trúc (structure / 구조) đơn giản nhất đáp ứng yêu cầu** tiếp nhận điểm tựa từ **27. Benchmark đúng tải công việc (workload / 워크로드)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **29. Những hiểu lầm phổ biến** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 28. Chọn cấu trúc (structure / 구조) đơn giản nhất đáp ứng yêu cầu

Cấu trúc (structure / 구조) phức tạp hơn tạo nhiều mã (code / 코드), nhiều trường hợp biên (edge case / 경계 사례) và nhiều bất biến (invariant / 불변식) hơn.

Nếu array + sort một lần đủ, không cần custom balanced cây (tree / 트리). Nếu `HashMap` chuẩn đủ, không cần tự viết Cuckoo Hashing. Nếu `O(n²)` với `n<=100` đã dư sức, không cần Segment cây (tree / 트리).

Độ phức tạp hiện thực (implementation / 구현) cũng là một chi phí kỹ thuật.

> **Chuyển mạch:** Trong **Chọn cấu trúc dữ liệu phù hợp**, **29. Những hiểu lầm phổ biến** tiếp nhận điểm tựa từ **28. Chọn cấu trúc (structure / 구조) đơn giản nhất đáp ứng yêu cầu** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **30. Workflow chọn cấu trúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 29. Những hiểu lầm phổ biến

“Big-O nhỏ hơn luôn nhanh hơn” — sai do constant factor, locality, allocation và tải công việc (workload / 워크로드) mix.

“Linked danh sách (list / 목록) chèn O(1) nên tốt hơn ArrayList” — bỏ qua chi phí tìm nút (node / 노드) và bộ nhớ đệm (cache / 캐시) hành vi (behavior / 동작).

“HashMap luôn tốt hơn TreeMap vì O(1)” — sai nếu cần thứ tự hoặc worst-case deterministic guarantee.

“Segment cây (tree / 트리) tốt hơn prefix sum vì mạnh hơn” — sai nếu dữ liệu tĩnh; sức mạnh dư thừa phải trả bằng bộ nhớ (memory / 메모리)/mã (code / 코드)/truy vấn (query / 쿼리) chi phí (cost / 비용).

“Chỉ cần chọn một cấu trúc dữ liệu (data structure / 자료구조) cho cả hệ thống” — hệ thống thật thường là composition.

> **Chuyển mạch:** Ở chặng này của **Chọn cấu trúc dữ liệu phù hợp**, **29. Những hiểu lầm phổ biến** xác định đầu vào; **30. Workflow chọn cấu trúc** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 30. Workflow chọn cấu trúc

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
1. Viết chính xác operation set.
2. Ghi tần suất và đường chạy nóng.
3. Xác định static/dynamic, online/offline.
4. Xác định ordered/equality/range/prefix semantics.
5. Xác định dense/sparse và quy mô n.
6. Xác định memory/cache/I/O model.
7. Chọn invariant tối thiểu hỗ trợ query.
8. So các candidate bằng total cost, không chỉ một operation.
9. Kiểm tra correctness + edge cases.
10. Benchmark workload đại diện.
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Chọn cấu trúc dữ liệu phù hợp**, **Mô hình tư duy** gom các mảnh từ **30. Workflow chọn cấu trúc** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Mô hình tư duy

> Chọn cấu trúc dữ liệu là chọn **thông tin nào đáng được lưu sẵn** và **chi phí nào đáng trả khi cập nhật** để những truy vấn (query / 쿼리) quan trọng trở nên rẻ.

Khi phân vân giữa hai cấu trúc, đừng hỏi “cái nào nhanh hơn?”. Hãy hỏi: **tải công việc (workload / 워크로드) của tôi là gì, bất biến (invariant / 불변식) nào thật sự cần, guarantee nào bắt buộc, bộ nhớ (memory / 메모리) hierarchy ra sao, và liệu một cấu trúc (structure / 구조) đơn giản hơn đã đủ chưa?**

Xem thêm: [Problem Modeling](../00_foundations/00_dsa_as_problem_modeling.md), [Complexity](../00_foundations/02_complexity_analysis.md), [Memory Models](../00_foundations/03_memory_models_c_java_javascript.md), [Problem-Solving Workflow](./02_problem_solving_workflow.md).

> **Bàn giao:** Sau **Mô hình tư duy**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
