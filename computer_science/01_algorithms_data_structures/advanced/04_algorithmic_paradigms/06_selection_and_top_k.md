# Selection, k-th Element và Top-K
**Selection Algorithms, Order Statistics & Top-K / 선택 알고리즘과 Top-K**

Nếu chỉ cần phần tử nhỏ thứ `k`, sorting toàn bộ thường tạo nhiều information hơn yêu cầu. Sorting xác định relative order của mọi phần tử; selection chỉ cần biết một **order statistic** cụ thể hoặc một nhóm nhỏ quanh boundary.

Đây là một ví dụ quan trọng của algorithm design: đừng trả chi phí để tính thông tin mà output không cần.

## 1. Order Statistic là gì?

Với array sau khi sort tăng dần:

```text
[2, 4, 7, 9, 13]
```

phần tử nhỏ thứ nhất là 2, phần tử nhỏ thứ ba là 7, median là một order statistic ở giữa.

Tùy API, `k` có thể zero-based hoặc one-based. Nếu code dùng zero-based index, “k-th smallest” thường map thành index `k-1`. Off-by-one là lỗi rất thường gặp, nên semantics phải ghi rõ ngay từ đầu.

## 2. Sort toàn bộ là baseline hợp lý nhưng không luôn tối ưu

Cách đơn giản là sort rồi lấy `a[k]`:

\[
O(n\log n)
\]

Nếu array sau đó còn được dùng cho nhiều ordered queries, sorting có thể hoàn toàn hợp lý. Nhưng nếu chỉ cần một rank duy nhất, ta có thể làm tốt hơn về expected time.

Đây là khác biệt giữa **batch preprocessing** và **single selection query**.

## 3. Partition là primitive cốt lõi

Quickselect dựa trên cùng partition primitive với Quicksort.

Chọn một pivot. Sau partition, ta đưa array về trạng thái sao cho phần tử nhỏ hơn pivot nằm một phía, lớn hơn pivot nằm phía kia theo convention cụ thể. Nếu pivot kết thúc ở index `p`, ta biết pivot đã ở đúng final rank của nó.

Nếu `k == p`, answer đã tìm thấy. Nếu `k < p`, chỉ cần xử lý bên trái. Nếu `k > p`, chỉ cần xử lý bên phải.

Điểm khác Quicksort là Quickselect **không recurse cả hai phía**.

## 4. Tại sao expected complexity là O(n)?

Nếu pivot thường chia tương đối cân bằng, recurrence gần:

\[
T(n)=T(n/2)+O(n)
\]

Level đầu scan `n`, level sau scan khoảng `n/2`, rồi `n/4`, ... Tổng geometric series:

\[
n+n/2+n/4+\cdots = O(n)
\]

Ngay cả khi partition không luôn chính giữa, randomized pivot vẫn cho expected linear time dưới analysis chuẩn.

Worst case vẫn `O(n^2)` nếu pivot liên tục cực xấu, ví dụ mỗi lần chỉ loại được một phần tử.

## 5. Randomized Quickselect

Random pivot làm input cố định khó ép algorithm liên tục chọn pivot xấu nếu random source không bị kiểm soát bởi adversary.

JavaScript implementation iterative:

```js
function quickselect(a, k) {
  let lo = 0;
  let hi = a.length - 1;

  while (lo <= hi) {
    const pivotIndex = lo + Math.floor(Math.random() * (hi - lo + 1));
    [a[pivotIndex], a[hi]] = [a[hi], a[pivotIndex]];
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

Function này mutate input. API production phải document mutation hoặc copy array trước, đổi lại thêm `O(n)` memory/time copy.

## 6. Duplicate values và three-way partition

Nếu array có rất nhiều duplicates, partition hai vùng có thể xử lý kém hoặc tạo nhiều recursion không cần thiết.

Three-way partition chia thành:

```text
< pivot
== pivot
> pivot
```

Nếu target rank nằm trong vùng `== pivot`, ta trả ngay. Với duplicate-heavy data, cách này có thể cải thiện đáng kể.

Đây cũng là same idea với Dutch National Flag partition.

## 7. Median of Medians: worst-case linear selection

Có thể chọn pivot deterministically để bảo đảm một fraction đủ lớn của elements bị loại mỗi bước.

Median-of-medians thường chia elements thành groups nhỏ, lấy median mỗi group, recursively tìm median của các medians rồi dùng nó làm pivot.

Proof cho thấy pivot không thể quá lệch, tạo recurrence kiểu:

\[
T(n) \le T(n/5)+T(7n/10)+O(n)
\]

và dẫn tới worst-case `O(n)`.

Algorithm này quan trọng về lý thuyết vì chứng minh selection không có lower bound `Omega(n log n)` như comparison sorting. Nhưng constant factor và implementation phức tạp khiến randomized Quickselect thường thực dụng hơn.

## 8. Median và percentile

Median là k-th statistic ở khoảng giữa. Percentiles như p95, p99 cũng là order statistics trên dữ liệu batch.

Nếu dataset vừa memory và query one-shot, selection algorithm có thể đủ. Nếu streaming vô hạn hoặc distributed scale, exact percentile trở nên tốn memory; khi đó quantile sketches như t-digest/KLL family trở thành approximate structures phù hợp hơn.

Selection theory vì vậy nối trực tiếp sang observability systems.

## 9. Top-K lớn nhất bằng min-heap size k

Nếu có stream `n` items và cần `k` largest, ta không cần giữ toàn bộ data.

Duy trì min-heap size tối đa `k`:

```text
heap chưa đủ k -> push
x <= heap.min -> bỏ qua
x > heap.min -> pop min rồi push x
```

Root heap luôn là phần tử nhỏ nhất trong current Top-K. Sau khi stream kết thúc, heap chứa `k` phần tử lớn nhất.

Complexity:

\[
O(n\log k)
\]

Memory:

\[
O(k)
\]

Nếu `k << n`, đây là trade-off rất tốt.

## 10. Tại sao min-heap cho k largest?

Nghe hơi ngược: muốn largest nhưng lại dùng min-heap.

Lý do là ta cần biết phần tử **yếu nhất trong nhóm đang giữ** để quyết định candidate mới có thay thế được không. Với k largest, yếu nhất là smallest among current top-k, nên min-heap đặt đúng boundary cần kiểm tra ở root.

Ngược lại, muốn k smallest thì giữ max-heap size k.

Đây là data-structure selection từ operation boundary, không phải thuộc mẹo.

## 11. Top-K bằng Quickselect

Nếu dữ liệu batch nằm sẵn trong memory, Quickselect có thể partition để đưa k largest hoặc k smallest về một phía trong expected `O(n)`.

Nếu output cần sorted, sau selection vẫn phải sort k selected elements:

\[
O(n)+O(k\log k)
\]

Nếu `k` rất nhỏ và stream data đến dần, heap thuận lợi hơn. Nếu batch lớn và chỉ cần unsorted top-k, Quickselect có thể tốt hơn.

## 12. Heapify toàn bộ rồi pop k lần

Một strategy khác là build max-heap `O(n)` rồi pop `k` lần:

\[
O(n+k\log n)
\]

Cách này phù hợp nếu heap còn được dùng tiếp hoặc nếu k không quá nhỏ. Nhưng memory `O(n)` vì giữ toàn bộ dataset.

So sánh các strategy phải dựa vào batch/streaming, `k/n`, memory budget và whether input mutation allowed.

## 13. Partial sort

Một số standard libraries cung cấp partial sort hoặc nth-element-like primitive. Ý tưởng là chỉ đảm bảo prefix/top portion sorted thay vì toàn array.

Nếu cần top-k **và sorted**, partial sort có thể hợp lý hơn việc full sort.

Trong C++, `nth_element` thường cung cấp expected linear partition semantics, còn `partial_sort` dùng strategy khác cho sorted prefix. Dù library khác nhau, conceptual distinction vẫn là: exact rank, unordered top-k hay sorted top-k là ba output contracts khác nhau.

## 14. K-way merge và Top-K trên sorted lists

Nếu có nhiều sorted lists và cần k smallest tổng thể, ta có thể dùng heap chứa current head của mỗi list.

Mỗi lần pop smallest, push phần tử tiếp theo từ cùng list. Nếu có `m` lists:

\[
O(k\log m)
\]

thay vì merge toàn bộ dữ liệu.

Pattern này xuất hiện trong external sorting, search shards và database merge operators.

## 15. Top-K frequent elements

Nếu objective là k values có frequency cao nhất, trước tiên cần frequency map. Sau đó có thể dùng min-heap size k trên `(frequency, value)`:

\[
O(n)+O(u\log k)
\]

với `u` là số unique values.

Nếu frequencies bounded bởi `n`, bucket sort theo frequency có thể đạt linear-ish `O(n+u)` memory/time trong một số settings.

Bài này cho thấy “Top-K” không tự động đồng nghĩa heap; distribution và key domain có thể mở strategy khác.

## 16. Top-K trong streaming và bounded memory

Heap size k không cần giữ toàn bộ stream, nên rất phù hợp log processing, recommendation candidate filtering hoặc telemetry.

Nhưng nếu stream cực lớn và objective là heavy hitters theo frequency, exact frequency map có thể vẫn quá lớn. Khi đó Count-Min Sketch/Space-Saving-like structures có thể approximate frequencies với bounded memory.

Top-K selection và probabilistic streaming structures gặp nhau tại đây.

## 17. Distributed Top-K

Nếu dữ liệu chia trên nhiều shards, mỗi shard có thể tính local top-k candidates rồi coordinator merge candidates.

Với monotonic score đơn giản, global top-k phải nằm trong union của đủ local candidates theo điều kiện phù hợp. Heap có thể merge lists/candidates hiệu quả.

Trong search systems thực tế, ranking/pruning phức tạp hơn, nhưng mental model “local candidate reduction → global merge” rất quan trọng.

## 18. Stability và tie-breaking

Nếu nhiều items có cùng score, API phải xác định tie-breaking: original order, secondary key hay arbitrary.

Heap comparator phải encode rule đó. Nếu comparator chỉ dựa score nhưng output yêu cầu deterministic tie order, results có thể thay đổi giữa runs.

Trong Java, comparator subtraction có thể overflow; nên dùng `Integer.compare`/`Long.compare`. Trong JavaScript, comparator phải trả negative/zero/positive đúng semantics.

## 19. Memory và mutation trade-off

Quickselect thường in-place và mutate array, memory auxiliary nhỏ. Heap streaming dùng `O(k)` extra memory nhưng giữ input order/source immutable.

Full sort có thể mutate hoặc copy tùy API. Trong production, mutation contract có thể quan trọng ngang complexity vì callers có thể còn cần original ordering.

## 20. Testing selection algorithms

Một property test đơn giản cho k-th result `x` là có ít nhất `k` elements `<= x` và đủ elements `< x` theo duplicate/rank semantics tương ứng.

Cách đáng tin hơn cho random small arrays là copy array, sort reference, rồi so `quickselect(a,k)` với `sorted[k]`.

Với Top-K heap, sort toàn input descending làm oracle và so multiset của first k elements.

Duplicate-heavy, already sorted, reverse sorted, all equal và `k=0`, `k=n-1` là các cases quan trọng.

## 21. Chọn strategy theo workload

Nếu chỉ một exact rank trên batch array: Quickselect.

Nếu cần deterministic worst-case bound: Median of Medians hoặc specialized deterministic strategy khi thật sự cần.

Nếu streaming và `k` nhỏ: bounded heap.

Nếu cần nhiều ordered queries về sau: sort một lần có thể tốt hơn.

Nếu cần sorted Top-K: heap + sort k results, partial sort hoặc selection + sort selected region.

Nếu dữ liệu distributed/streaming quá lớn để exact: approximate heavy-hitter/quantile structures.

## Mental Model

> Selection algorithms tận dụng việc output cần **ít order information hơn sorting**. Top-K algorithms duy trì chỉ phần boundary có khả năng ảnh hưởng answer.

Hãy luôn hỏi output contract chính xác là gì: một rank, k phần tử unordered, k phần tử sorted, frequency top-k hay approximate percentile. Câu trả lời đó quyết định liệu nên partition, heap, sort, bucket hay dùng sketch.

Xem thêm: [Heap](../02_trees/03_heaps.md), [Sorting](./01_sorting.md), [Probabilistic Data Structures](../05_specialized/06_probabilistic_data_structures.md).