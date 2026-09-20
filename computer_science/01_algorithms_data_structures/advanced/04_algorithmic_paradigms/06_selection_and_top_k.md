# Selection, k-th Element và Top-K
**Selection Algorithms, Order Statistics & Top-K / 선택 알고리즘과 Top-K**

Selection hỏi một câu ít tham vọng hơn sorting: **không cần biết toàn bộ relative order của mọi phần tử, chỉ cần một rank hoặc một nhóm nhỏ quanh boundary**. Nếu chỉ cần phần tử nhỏ thứ `k`, sorting toàn bộ tạo nhiều information hơn output yêu cầu.

Đây là một principle rất quan trọng của algorithm design:

> Đừng trả chi phí để tính information mà contract không cần.

## 1. Order Statistic

Nếu array sorted tăng dần:

```text
[2, 4, 7, 9, 13]
```

- smallest = order statistic 1;
- median = order statistic giữa;
- percentile = order statistic ở một rank xác định.

API phải định nghĩa `k` zero-based hay one-based. Nếu code dùng zero-based, “k-th smallest” thường map thành index `k-1` theo ngôn ngữ tự nhiên. Đây là nguồn off-by-one phổ biến.

## 2. Full Sort là baseline, không phải luôn sai

Sort rồi lấy rank:

\[
O(n\log n)
\]

Nếu sau đó còn hàng nghìn ordered queries, sorting một lần có thể tốt hơn selection riêng lẻ. Nếu chỉ một rank one-shot, có thể làm ít work hơn.

Selection vs sorting là trade-off giữa:

```text
single query, ít information
vs
preprocess toàn order cho nhiều query
```

## 3. Partition là primitive cốt lõi

Chọn pivot và rearrange data thành regions:

```text
< pivot | pivot | >= pivot
```

hoặc three-way:

```text
< pivot | == pivot | > pivot
```

Sau partition, nếu pivot/range equal nằm đúng rank region, ta đã tìm answer mà không cần sort từng phía.

Partition chính là mechanism biến một comparison với pivot thành **global elimination of candidates**.

## 4. Quickselect

Quickselect partition như Quicksort nhưng chỉ tiếp tục side chứa rank `k`.

Nếu pivot thường đủ cân bằng:

\[
T(n)=T(n/2)+O(n)=O(n)
\]

vì:

\[
n+n/2+n/4+\cdots=O(n)
\]

Worst case vẫn `O(n²)` nếu mỗi pivot chỉ loại một phần tử.

## 5. Randomized Quickselect

Random pivot làm input cố định khó ép algorithm liên tục chọn cực trị.

```js
function quickselect(a, k) {
  let lo = 0, hi = a.length - 1;

  while (lo <= hi) {
    const p0 = lo + Math.floor(Math.random() * (hi - lo + 1));
    [a[p0], a[hi]] = [a[hi], a[p0]];
    const pivot = a[hi];

    let p = lo;
    for (let i = lo; i < hi; i++) {
      if (a[i] < pivot) {
        [a[i], a[p]] = [a[p], a[i]];
        p++;
      }
    }

    [a[p], a[hi]] = [a[hi], a[p]];

    if (p === k) return a[p];
    if (k < p) hi = p - 1;
    else lo = p + 1;
  }

  throw new RangeError("k out of range");
}
```

Function này mutate input. Nếu API phải immutable, copy trước tạo thêm `O(n)` memory/time.

## 6. Three-way partition cho duplicates

Nếu nhiều values bằng pivot, two-way partition có thể recurse trên vùng equal lớn một cách vô ích.

Three-way partition cho interval `[lt, gt]` chứa tất cả values equal pivot. Nếu target `k` nằm trong interval này, return ngay.

Duplicate-heavy data là case mà three-way partition không chỉ là optimization nhỏ; nó có thể thay đổi shape recursion rõ rệt.

## 7. Median of Medians: deterministic worst-case O(n)

Median-of-medians chia data thành groups nhỏ, lấy median mỗi group, recursively tìm median của các medians rồi dùng làm pivot.

Analysis bảo đảm pivot loại một fraction đủ lớn ở cả hai phía:

\[
T(n) \le T(n/5)+T(7n/10)+O(n)=O(n)
\]

Ý nghĩa lý thuyết rất lớn: comparison-based selection không có lower bound `Ω(n log n)` như full sorting.

Nhưng constant factor và implementation complexity khiến randomized Quickselect thường thực dụng hơn trong general code.

## 8. Information lower bound của selection

Để tìm minimum, mọi element trừ winner phải “thua” ít nhất một comparison, nên cần ít nhất `n-1` comparisons.

Selection của arbitrary rank cũng có linear lower bound vì ít nhất phải inspect đủ input để không bỏ sót candidate.

Vì vậy expected/worst-case `O(n)` selection là asymptotically optimal.

## 9. Median và robust statistics

Median ít nhạy với outlier hơn mean. Exact median batch có thể dùng selection. Nếu data quá lớn/streaming, exact rank đòi lưu nhiều state; lúc đó approximate quantile sketches như KLL/t-digest family phù hợp hơn.

Algorithm selection phải xét cả statistical semantics và memory model.

## 10. Top-K largest bằng min-heap size k

Duy trì min-heap chứa current `k` largest:

```text
heap size < k -> push
x <= heap.min -> bỏ
x > heap.min -> replace root
```

Complexity:

\[
O(n\log k)
\]

Memory:

\[
O(k)
\]

Nếu `k << n`, đây là lựa chọn rất mạnh cho streaming.

## 11. Vì sao min-heap cho k largest?

Trong nhóm current top-k, phần tử quan trọng nhất để quyết định candidate mới là **phần tử nhỏ nhất đang giữ**. Nếu candidate không thắng boundary này, nó không thể vào top-k.

Do đó min-heap đặt đúng boundary element ở root.

Tương tự k smallest dùng max-heap size k.

## 12. Quickselect cho batch Top-K

Quickselect partition input để `k` largest/smallest nằm cùng một phía expected `O(n)`.

Nếu output không cần sorted, ta dừng ở đó. Nếu cần sorted top-k:

\[
O(n)+O(k\log k)
\]

sort riêng selected region.

Heap và Quickselect giải cùng output contract dưới workload khác:

```text
stream/bounded memory -> heap
batch/in-memory       -> quickselect
```

## 13. Heapify toàn bộ rồi pop k lần

Build max-heap `O(n)`, pop k lần:

\[
O(n+k\log n)
\]

Giữ toàn dataset `O(n)` nhưng hợp nếu heap còn dùng sau đó hoặc k tương đối lớn.

Không có một strategy Top-K duy nhất tốt cho mọi `k/n`.

## 14. Partial Sort

Nếu cần prefix top-k **đã sorted**, partial sort có thể phù hợp hơn full sort.

Conceptual distinction:

```text
nth-element: chỉ cần đúng boundary rank
selection: một rank
unordered top-k: đúng membership
sorted top-k: membership + order trong top-k
full sort: order toàn bộ n
```

Mỗi contract chứa lượng information khác nhau.

## 15. Multi-selection: cần nhiều ranks nhưng chưa cần full sort

Nếu cần quartiles hoặc một tập ranks `k1,k2,...`, ta có thể reuse partition tree thay vì chạy Quickselect độc lập cho từng rank.

Một partition chia set ranks thành nhóm trái/phải; recurse chỉ nơi có requested ranks.

Đây là middle ground giữa one-rank selection và full sorting.

## 16. K-way Merge

Có `m` sorted lists và cần k smallest tổng thể. Min-heap chứa current head mỗi list:

1. pop global smallest;
2. push next từ same list;
3. lặp k lần.

Complexity:

\[
O(k\log m)
\]

Không cần merge toàn bộ data.

Pattern này xuất hiện trong external sort, database merge, search shards và time-series streams.

## 17. Top-K frequent elements

Bài này gồm hai phases:

```text
frequency counting
selection theo frequency
```

Hash map tạo counts `O(n)` expected. Sau đó heap size k trên `u` unique values:

\[
O(n+u\log k)
\]

Nếu frequencies bounded `0..n`, bucket-by-frequency có thể đạt near-linear.

“Top-K” không tự động đồng nghĩa heap; key domain có thể mở alternative.

## 18. Streaming heavy hitters khác exact Top-K values

Nếu muốn items có frequency cao nhất trong stream khổng lồ, exact map có thể cần memory theo số distinct keys.

Count-Min Sketch + candidate tracking, Space-Saving hoặc Misra–Gries giảm memory đổi lấy guarantee khác.

Phân biệt:

```text
top-k by raw score per item
vs
top-k frequent over stream
```

chúng là problem khác nhau dù tên giống.

## 19. Quantile trong distributed systems

Exact percentile toàn distributed dataset có thể cần shuffle/sort lớn. Approximate sketches cho phép mỗi shard giữ summary rồi merge.

Nếu exact, một strategy có thể dùng distributed selection/partition rounds, nhưng network communication trở thành cost chính.

Ở scale lớn, communication complexity có thể quan trọng hơn CPU `O(n)` vs `O(n log n)`.

## 20. Distributed Top-K: local reduction rồi global merge

Nếu score mỗi item độc lập và mỗi shard chứa partition disjoint, local top-k của mỗi shard là candidate superset đủ cho global top-k: item không nằm local top-k không thể vượt k items cùng shard đã cao hơn nó.

Coordinator chỉ cần merge tối đa `shards * k` candidates.

Đây là một reduction rất mạnh:

```text
huge distributed dataset
-> local top-k
-> much smaller candidate union
-> global top-k
```

Nếu scoring phụ thuộc global normalization/interaction, property này có thể không còn đúng.

## 21. Threshold Algorithms cho sorted access

Trong information-retrieval/database settings, nếu nhiều attribute lists sorted theo partial scores, threshold algorithms có thể dừng sớm khi current top-k score đã vượt upper bound của unseen candidates.

Đây là một generalization của boundary reasoning: maintain lower bound của winners và upper bound của unknowns.

Không cần full materialization nếu có stopping certificate.

## 22. External-memory selection

Nếu data không fit RAM, in-place Quickselect trên toàn dataset không còn straightforward. Ta có thể partition data thành files/buckets theo pivot, count sizes, rồi chỉ recurse bucket chứa rank.

Goal chuyển từ comparison count sang giảm I/O passes và bytes read/write.

Một algorithm `O(n)` CPU nhưng nhiều random I/O có thể thua external strategy sequential scans.

## 23. Selection trên linked data

Quickselect cần efficient partition traversal nhưng không nhất thiết random access. Tuy nhiên pointer-heavy list có cache cost và partition relinking phức tạp.

Nếu data là linked structure nhưng có thể materialize array rẻ, chuyển representation đôi khi thực tế hơn cố implement specialized list selection.

## 24. Selection Trees và Tournament Trees

Tournament tree lưu kết quả pairwise winners. Tìm minimum cần `n-1` comparisons. Nếu muốn second minimum, chỉ cần xem những elements đã trực tiếp thua minimum trên path, khoảng `log n` candidates trong balanced tournament.

Đây là insight information reuse: comparison history chứa thêm structure cho order statistics tiếp theo.

Tournament/loser trees cũng dùng trong k-way external merge.

## 25. Online Median bằng hai heaps

Giữ:

```text
max-heap lower half
min-heap upper half
```

Invariant:

```text
size difference <= 1
max(lower) <= min(upper)
```

Insert `O(log n)`, median `O(1)`.

Đây không phải classic one-shot selection mà là dynamic order statistic cho insertion-only stream.

Nếu cần delete arbitrary items, two heaps cần lazy deletion/indexing phức tạp hơn hoặc balanced order-stat tree.

## 26. Top-K với updates/deletes

Static heap size k giả định each item xét một lần. Nếu scores thay đổi sau insertion, heap không tự reorder khi object field mutate.

Java `PriorityQueue` không hỗ trợ arbitrary priority update. Options:

```text
push new version + skip stale
indexed heap
balanced tree keyed by score
periodic rebuild
```

Output contract động làm data structure choice thay đổi.

## 27. Tie-breaking và determinism

Nếu nhiều items cùng score, cần secondary order:

```text
score desc
then timestamp asc
then id asc
```

Comparator phải encode rule. Nếu không, heap/partition có thể trả arbitrary ordering giữa ties, làm tests flaky và distributed results nondeterministic.

Top-k **set membership** và top-k **stable ordered list** là hai contracts khác nhau.

## 28. Floating-point scores

Ranking với `NaN`, `-0`, infinities hoặc floating rounding cần semantics rõ. Comparator không nên giả định total order nếu domain có NaN behavior đặc biệt.

Nếu score được tính từ nhiều floating components, near-tie results có thể nhạy với evaluation order. Production ranking thường cần deterministic normalization/tie-break key.

## 29. Java/C/JavaScript comparator caveats

Java/C comparator dùng subtraction có thể overflow:

```java
return a.score - b.score;
```

nên dùng `Integer.compare`/`Long.compare`.

JavaScript comparator Number phải trả negative/zero/positive. Với BigInt, không nên trộn arithmetic result BigInt trực tiếp theo cách API không chấp nhận; dùng relational branches.

Comparator correctness là prerequisite của heap/sort/ordered selection.

## 30. Mutation contract

Quickselect thường mutate array. Heap streaming không cần reorder input. Full sort có thể mutate tùy API.

Nếu caller cần original order, copy có cost `O(n)` memory/time. Đây là engineering trade-off thật, không chỉ style.

## 31. Testing Quickselect

Reference oracle:

```text
copy input
sort copy
expected = copy[k]
```

Random small arrays cho differential testing rất hiệu quả.

Cases:

```text
all equal
many duplicates
sorted
reverse sorted
single element
k = 0
k = n-1
negative/large values
```

Nếu randomized, log seed để reproduce failure.

## 32. Property của k-th statistic

Nếu answer `x` cho zero-based rank `k`, phải có đủ số elements `< x` và `<= x` phù hợp duplicate semantics để rank `k` nằm trong equal block của `x`.

Property này giúp verify result mà không cần exact pivot history.

## 33. Testing Top-K

So multiset output với first k của fully sorted reference. Nếu output contract sorted, compare sequence. Nếu unordered, compare frequency map/multiset.

Tie-breaking phải được test riêng nếu API deterministic.

## 34. Adversarial input và pivot strategy

Quickselect deterministic pivot đầu/cuối dễ bị sorted/adversarial input phá `O(n²)`.

Random pivot, median-of-three hoặc introspective fallback giúp giảm risk. Public APIs phải cân nhắc adversarial callers nếu latency/security quan trọng.

## 35. Strategy matrix theo workload

Một rank, batch, mutation allowed:

```text
Quickselect
```

Một rank, deterministic worst-case bound bắt buộc:

```text
Median of Medians / deterministic selection
```

Top-k streaming, k nhỏ:

```text
bounded heap
```

Top-k batch unsorted:

```text
Quickselect
```

Top-k sorted:

```text
selection + sort k
heap
partial sort
```

Nhiều rank queries:

```text
sort once
order-stat tree
multi-selection
```

Streaming percentile approximate:

```text
quantile sketch
```

## Mental Model

> Selection algorithms khai thác việc output chỉ yêu cầu **một boundary trong order**, không cần toàn bộ order. Quickselect loại regions; heap duy trì boundary; tournament tree reuse comparison history; distributed top-k giảm candidate set trước khi merge.

Trước khi chọn algorithm, hãy viết chính xác output contract: một rank, unordered top-k, sorted top-k, dynamic rank, frequency heavy hitters hay approximate percentile. Chỉ một từ “Top-K” chưa đủ xác định bài toán.

Xem thêm: [Heap](../02_trees/03_heaps.md), [Sorting](./01_sorting.md), [Probabilistic Structures](../05_specialized/06_probabilistic_data_structures.md), [Complexity](../00_foundations/02_complexity_analysis.md).