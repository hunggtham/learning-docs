# Trường hợp (case / 사례) Study: Autocomplete và tìm kiếm (search / 검색) Suggestions

> **Mạch đọc:** Đọc **trường hợp (case / 사례) Study: Autocomplete và tìm kiếm (search / 검색) Suggestions** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Định nghĩa tải công việc (workload / 워크로드)** sang **2. Trie cho prefix retrieval**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.

**Autocomplete & tìm kiếm (search / 검색) Suggestion thiết kế (design / 설계) / 자동완성과 검색 제안 설계**

Autocomplete nhìn bề ngoài chỉ là “gõ prefix rồi hiện vài từ gợi ý”, nhưng hệ thống thực tế phải giải đồng thời nhiều bài toán DSA: tìm theo tiền tố, xếp hạng, cập nhật độ phổ biến, giới hạn bộ nhớ, sửa lỗi chính tả, xử lý Unicode và giữ độ trễ thấp khi dữ liệu lớn.

Trường hợp (case / 사례) study này nối các chương Trie, vùng nhớ động (heap / 힙), bảng băm (hash table / 해시 테이블), Sorting, String Algorithms, Probabilistic Structures và hệ thống bộ nhớ đệm (cache / 캐시) thành một chuỗi xử lý (pipeline / 파이프라인) hoàn chỉnh.

## 1. Định nghĩa tải công việc (workload / 워크로드)

Giả sử hệ thống có:

```text
50 triệu truy vấn/từ khóa đã biết
200 nghìn QPS giờ cao điểm
Top 10 suggestions cho mỗi prefix
độ trễ mục tiêu p95 < 50 ms
ranking thay đổi theo popularity và thời gian
hỗ trợ nhiều ngôn ngữ
```

Các thao tác chính:

```text
lookup(prefix)
getTopK(prefix)
updatePopularity(term)
insertNewTerm(term)
removeOrBlock(term)
```

Ngay lập tức có hai lớp khác nhau:

```text
retrieval -> lấy tập ứng viên phù hợp prefix
ranking   -> chọn và sắp xếp ứng viên tốt nhất
```

Trie giải tốt retrieval, nhưng không tự giải ranking.

## 2. Trie cho prefix retrieval

Nếu mỗi ký tự là một cạnh, đi qua prefix `app` mất thời gian gần `O(|prefix|)` theo số ký hiệu.

```text
root
 └─ a
    └─ p
       └─ p
          ├─ apple
          ├─ apply
          └─ app store
```

Sau khi đến nút prefix, mọi hậu duệ là ứng viên.

Nhưng nếu subtree có hàng triệu từ, DFS toàn bộ rồi sort mỗi yêu cầu (request / 요청) là không khả thi.

## 3. Materialize Top-K tại nút (node / 노드)

Một chiến lược là mỗi nút (node / 노드) giữ sẵn danh sách Top-K:

```text
node "app"
  top = ["apple", "app store", "application", ...]
```

Khi truy vấn:

```text
đi theo prefix: O(|prefix|)
đọc top-K cache: gần O(K)
```

Đổi lại, khi popularity của một term thay đổi, mọi prefix của term có thể cần cập nhật siêu dữ liệu (metadata / 메타데이터).

Nếu term dài `L`, một cập nhật (update / 업데이트) có thể tác động tới `O(L)` nút (node / 노드).

Đây là sự đánh đổi điển hình:

```text
query rất nhanh
↔
update đắt hơn + nhiều bộ nhớ hơn
```

## 4. vùng nhớ động (heap / 힙) cho Top-K cập nhật cục bộ

Nếu một nút (node / 노드) có nhiều ứng viên nhưng không muốn lưu toàn bộ đã sắp xếp, có thể dùng vùng nhớ động (heap / 힙) kích thước `K` để duy trì Top-K.

Khi cập nhật score:

```text
đưa ứng viên mới/cập nhật vào heap
loại phần tử tệ nhất nếu size > K
```

Tuy nhiên nếu score của phần tử đang trong vùng nhớ động (heap / 힙) thay đổi tùy ý, cần xử lý stale entry hoặc indexed vùng nhớ động (heap / 힙). Trong hệ thống phân tán, thường đơn giản hơn khi cho phép entry cũ tồn tại và xác minh score mới khi đọc.

## 5. Ranking score

Một score thực tế có thể là:

\[
score = w_1 \cdot popularity + w_2 \cdot recency + w_3 \cdot personalization + w_4 \cdot chất lượng (quality / 품질)
\]

DSA không quyết định trọng số, nhưng nó quyết định cách lưu và cập nhật score hiệu quả.

Nếu personalization theo từng người dùng (user / 사용자), không thể materialize mọi prefix × người dùng (user / 사용자). Khi đó hệ thống thường:

```text
lấy candidate toàn cục
+
thêm feature cá nhân hóa
+
rerank Top-M thành Top-K
```

Tức là chia bài toán thành nhiều tầng để kiểm soát trạng thái (state / 상태) explosion.

## 6. Trie thuần có thể quá tốn bộ nhớ

50 triệu term × nhiều nút (node / 노드) đối tượng (object / 객체) có thể tạo overhead rất lớn.

Các lựa chọn nén gồm:

```text
Radix Tree / Patricia Trie
Double-Array Trie
LOUDS / succinct trie
Finite-State Transducer (FST)
```

Radix cây (tree / 트리) nén các chuỗi nút (node / 노드) một-con thành cạnh dài hơn. FST còn có thể hợp nhất các suffix/trạng thái (state / 상태) tương đương trong từ điển tĩnh, tiết kiệm bộ nhớ đáng kể.

Nếu dictionary gần như tĩnh, FST hoặc sorted array + prefix tìm kiếm nhị phân (binary search / 이진 탐색) có thể tốt hơn Trie object-heavy.

## 7. Sorted Array là một baseline mạnh

Nếu dữ liệu chủ yếu đọc và rebuild theo batch:

```text
sort tất cả terms theo từ điển
lower_bound(prefix)
upper_bound(prefix_range)
quét một vùng nhỏ
```

Ưu điểm:

```text
bộ nhớ gọn
cache locality tốt
serialize đơn giản
```

Nhược điểm:

```text
insert động đắt
khó duy trì metadata prefix phong phú
```

Không nên mặc định “autocomplete = Trie”. tải công việc (workload / 워크로드) tĩnh có thể làm sorted array hấp dẫn hơn.

## 8. Unicode và normalization

Một từ người dùng nhìn thấy có thể có nhiều biểu diễn Unicode khác nhau. Nếu chỉ mục (index / 인덱스) và truy vấn (query / 쿼리) không normalization nhất quán, hai chuỗi trông giống nhau có thể không match.

Chuỗi xử lý (pipeline / 파이프라인) nên xác định rõ:

```text
Unicode normalization form
case folding
locale-specific rules
accent handling
code point vs grapheme cluster
```

Ví dụ tiếng Hàn, tiếng Việt và emoji có các đặc điểm khác ASCII. Cấu trúc dữ liệu đúng nhưng đơn vị ký tự sai vẫn cho kết quả sai về sản phẩm.

## 9. Prefix không đủ cho lỗi chính tả

Nếu người dùng gõ `applr` thay vì `apple`, Trie exact-prefix không trả kết quả mong muốn.

Có thể dùng:

```text
Levenshtein distance
BK-Tree
trie + DP theo hàng edit distance
n-gram index
fuzzy automaton
```

Trie + DP có thể cắt tỉa nhiều nhánh nếu edit distance hiện tại đã vượt ngưỡng.

Ở đây DSA chuyển từ chính xác (exact / 정확한) traversal sang state-space tìm kiếm (search / 검색) trên:

```text
(node trong trie, vị trí trong query, edit budget)
```

## 10. Aho–Corasick không phải autocomplete

Aho–Corasick giải bài toán tìm nhiều mẫu (pattern / 패턴) trong một văn bản (text / 텍스트) lớn. Autocomplete hỏi prefix của truy vấn (query / 쿼리) hiện tại.

Cả hai cùng dùng Trie nhưng tải công việc (workload / 워크로드) khác nhau. Đây là ví dụ vì sao không nên chọn thuật toán chỉ vì thấy cùng cấu trúc nền.

## 11. bộ nhớ đệm (cache / 캐시) theo prefix

Một số prefix nóng như `a`, `th`, `iphone` có lưu lượng cực lớn.

Có thể bộ nhớ đệm (cache / 캐시):

```text
prefix -> Top-K result
```

Băm (hash / 해시) Map cho lookup nhanh, còn eviction có thể dùng LRU/TinyLFU tùy tải công việc (workload / 워크로드).

Bộ nhớ đệm (cache / 캐시) càng ở gần máy khách (client / 클라이언트)/người dùng (user / 사용자) càng giảm độ trễ (latency / 지연 시간), nhưng freshness của ranking giảm nếu score cập nhật liên tục.

## 12. Heavy Hitters cho truy vấn (query / 쿼리) stream

Muốn biết prefix hoặc truy vấn (query / 쿼리) nào đang nóng mà không lưu mọi tần suất chính xác, có thể dùng:

```text
Count-Min Sketch
Space-Saving
Misra–Gries
```

Các sketch giúp phát hiện xu hướng với bộ nhớ nhỏ, sau đó chỉ duy trì trạng thái (state / 상태) chính xác cho nhóm candidate nổi bật.

Đây là mô hình nhiều tầng:

```text
approximate wide monitoring
→ candidate narrowing
→ exact state for small set
```

## 13. thời gian (time / 시간) decay

Popularity cũ không nên thống trị mãi. Có thể dùng score suy giảm theo thời gian:

\[
score(t)=raw\_count \cdot e^{-\lambda \Delta t}
\]

hoặc bucket theo giờ/ngày rồi gộp có trọng số.

Nếu cập nhật (update / 업데이트) mọi term theo mỗi tick thời gian sẽ quá đắt. Thay vào đó thường tính decay lazily khi đọc hoặc giữ thống kê theo bucket.

Đây là ví dụ tránh “cập nhật (update / 업데이트) toàn bộ trạng thái (state / 상태)” bằng cách thay đổi cách biểu diễn.

## 14. Sharding

Nếu dictionary quá lớn cho một máy, có thể shard theo:

```text
hash(term)
range/prefix
ngôn ngữ
thị trường
```

Băm (hash / 해시) sharding cân bằng tốt nhưng một prefix có thể nằm trên nhiều shard, khiến truy vấn (query / 쿼리) phải fan-out. Prefix/phạm vi (range / 범위) sharding giữ locality của truy vấn nhưng dễ lệch tải khi một vùng từ vựng quá nóng.

Một hệ thống thực có thể dùng nhiều tầng partitioning để cân bằng hai mục tiêu.

## 15. Fan-out và phân tán (distributed / 분산) Top-K

Giả sử truy vấn (query / 쿼리) gửi tới `p` shard, mỗi shard trả Top-M cục bộ. Coordinator cần merge thành Top-K toàn cục.

Có thể dùng vùng nhớ động (heap / 힙) `p` chiều hoặc gom `pM` candidate rồi chọn Top-K.

Nếu M quá nhỏ, có thể bỏ sót ứng viên toàn cục. Nếu M quá lớn, tăng bandwidth và CPU. Đây là một bài toán sự đánh đổi (trade-off / 트레이드오프) giữa tính đúng đắn (correctness / 정확성) guarantee và communication chi phí (cost / 비용).

## 16. Stale kết quả (result / 결과) và consistency

Ranking không phải dữ liệu giao dịch tài chính. Nhiều hệ thống chấp nhận eventual consistency:

```text
term mới có thể xuất hiện sau vài giây
popularity có thể trễ một ít
cache có TTL
```

Cho phép stale nhẹ giúp batching cập nhật (update / 업데이트) và rebuild chỉ mục (index / 인덱스) hiệu quả hơn nhiều.

Ngược lại, blocklist hoặc nội dung nguy hiểm có thể cần propagation nhanh hơn ranking score. Không phải mọi trường dữ liệu đều có cùng consistency yêu cầu (requirement / 요구사항).

## 17. chuỗi xử lý (pipeline / 파이프라인) hoàn chỉnh

Một kiến trúc khái niệm:

```text
User input
   ↓ normalize
Prefix lookup
   ↓
Trie / FST / Sorted Index
   ↓
Candidate Top-M
   ↓
Global features + personalization
   ↓
Heap / partial sort
   ↓
Top-K
   ↓
Cache
```

Offline/streaming side:

```text
query events
   ↓
Count-Min Sketch / exact counters
   ↓
popularity aggregation
   ↓
index metadata rebuild/update
```

## 18. Testing

Cần kiểm tra:

```text
mọi kết quả thực sự có prefix sau normalization
Top-K đúng theo comparator và tie-break
update popularity không làm mất candidate
Unicode equivalent forms cho cùng semantics
fuzzy search không vượt edit threshold
shard merge không bỏ sót kết quả theo guarantee thiết kế
```

Differential kiểm thử (test / 테스트) có thể so Trie với sorted-array baseline trên tập nhỏ.

## 19. Benchmark

Benchmark phải phân biệt:

```text
prefix ngắn vs dài
prefix phổ biến vs hiếm
cache hit vs miss
cold vs warm index
update rate
Unicode/script khác nhau
Top-K size
shard fan-out
```

Một benchmark chỉ với từ ASCII ngẫu nhiên sẽ không đại diện tải công việc (workload / 워크로드) thật.

## 20. Khi nào chọn cấu trúc nào?

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
Dictionary tĩnh, bộ nhớ quan trọng:
    Sorted Array / FST

Update động nhiều, prefix query nhiều:
    Trie / Radix Tree

Longest-prefix trên bit key:
    Patricia / Radix Trie

Fuzzy query:
    Trie + edit-DP / BK-Tree / n-gram index

Popularity stream quy mô lớn:
    sketch + exact Top-K candidates
```

## Mô hình tư duy

> Autocomplete không phải “bài Trie”. Nó là một hệ thống **retrieval + ranking + caching + streaming statistics**. Trie chỉ materialize quan hệ prefix; vùng nhớ động (heap / 힙) hỗ trợ Top-K; băm (hash / 해시) Map hỗ trợ bộ nhớ đệm (cache / 캐시)/counter; sketch giảm trạng thái (state / 상태); sorting/FST tối ưu dữ liệu tĩnh; Unicode và phân tán (distributed / 분산) partitioning quyết định tính đúng đắn ở cấp sản phẩm.

Xem thêm: [Trie](../02_trees/04_tries.md), [String Algorithms](../05_specialized/00_string_algorithms.md), [Selection & Top-K](../04_algorithmic_paradigms/06_selection_and_top_k.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md), [Hash Tables](../01_linear_structures/04_hash_tables.md).
