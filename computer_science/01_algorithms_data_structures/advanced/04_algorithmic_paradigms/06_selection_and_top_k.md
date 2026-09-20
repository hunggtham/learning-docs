# Selection, k-th phần tử và Top-K
**Selection các thuật toán, Order thống kê & Top-K / 선택 알고리즘과 Top-K**

Bài toán chọn (selection) yêu cầu ít thông tin hơn sắp xếp: **không cần biết toàn bộ thứ tự tương đối của mọi phần tử, chỉ cần một hạng hoặc một nhóm nhỏ quanh ranh giới**. Nếu chỉ cần phần tử nhỏ thứ `k`, sắp xếp toàn bộ tạo nhiều thông tin hơn đầu ra yêu cầu.

Đây là một principle rất quan trọng của thuật toán design:

> Đừng trả chi phí để tính thông tin mà contract không cần.

## 1. thống kê thứ tự

Nếu mảng sorted tăng dần:

```text
[2, 4, 7, 9, 13]
```

- smallest = thống kê thứ tự 1;
- median = thống kê thứ tự giữa;
- percentile = thống kê thứ tự ở một rank xác định.

API phải định nghĩa `k` zero-based hay one-based. Nếu code dùng zero-based, “phần tử nhỏ thứ k” thường map thành index `k-1` theo ngôn ngữ tự nhiên. Đây là nguồn off-by-one phổ biến.

## 2. Full Sort là baseline, không phải luôn sai

Sort rồi lấy rank:

\[
O(n\log n)
\]

Nếu sau đó còn hàng nghìn các truy vấn có thứ tự, sorting một lần có thể tốt hơn selection riêng lẻ. Nếu chỉ một rank one-shot, có thể làm ít work hơn.

Selection vs sorting là sự đánh đổi (trade-off) giữa:

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

Sau partition, nếu pivot/range equal nằm đúng vùng hạng, ta đã tìm answer mà không cần sort từng phía.

Partition chính là mechanism biến một phép so sánh với pivot thành **toàn cục elimination of các ứng viên**.

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

trường hợp xấu nhất vẫn `O(n²)` nếu mỗi pivot chỉ loại một phần tử.

## 5. ngẫu nhiên hóa Quickselect

ngẫu nhiên pivot làm đầu vào cố định khó ép thuật toán liên tục chọn cực trị.

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

hàm này mutate đầu vào. Nếu API phải bất biến sau khi tạo, copy trước tạo thêm `O(n)` bộ nhớ/time.

## 6. Three-way partition cho các phần tử trùng

Nếu nhiều các giá trị bằng pivot, two-way partition có thể recurse trên vùng equal lớn một cách vô ích.

Three-way partition cho interval `[lt, gt]` chứa tất cả các giá trị bằng chốt. Nếu đích `k` nằm trong interval này, return ngay.

có nhiều phần tử trùng data là case mà three-way partition không chỉ là optimization nhỏ; nó có thể thay đổi shape recursion rõ rệt.

## 7. Median of Medians: xác định trường hợp xấu nhất O(n)

Median-of-medians chia dữ liệu thành các nhóm nhỏ, lấy trung vị của mỗi nhóm, đệ quy tìm trung vị của các trung vị rồi dùng giá trị đó làm chốt.

Analysis bảo đảm pivot loại một fraction đủ lớn ở cả hai phía:

\[
T(n) \le T(n/5)+T(7n/10)+O(n)=O(n)
\]

Ý nghĩa lý thuyết rất lớn: comparison-based selection không có cận dưới `Ω(n log n)` như full sorting.

Nhưng constant factor và cách triển khai complexity khiến ngẫu nhiên hóa Quickselect thường thực dụng hơn trong general code.

## 8. thông tin cận dưới của selection

Để tìm minimum, mọi phần tử trừ winner phải “thua” ít nhất một phép so sánh, nên cần ít nhất `n-1` các phép so sánh.

Selection của arbitrary rank cũng có linear cận dưới vì ít nhất phải inspect đủ đầu vào để không bỏ sót ứng viên.

Vì vậy kỳ vọng/trường hợp xấu nhất `O(n)` selection là asymptotically optimal.

## 9. Median và robust thống kê

Median ít nhạy với outlier hơn mean. chính xác median batch có thể dùng selection. Nếu data quá lớn/xử lý luồng, chính xác rank đòi lưu nhiều trạng thái (state); lúc đó xấp xỉ quantile sketches như KLL/t-digest family phù hợp hơn.

thuật toán selection phải xét cả statistical ngữ nghĩa (semantics) và mô hình bộ nhớ (memory model).

## 10. Top-K largest bằng đống nhỏ nhất size k

Duy trì đống nhỏ nhất chứa hiện tại `k` largest:

```text
heap size < k -> push
x <= heap.min -> bỏ
x > heap.min -> replace root
```

Complexity:

\[
O(n\log k)
\]

bộ nhớ:

\[
O(k)
\]

Nếu `k << n`, đây là lựa chọn rất mạnh cho xử lý luồng.

## 11. Vì sao đống nhỏ nhất cho k largest?

Trong nhóm hiện tại Top-K, phần tử quan trọng nhất để quyết định ứng viên mới là **phần tử nhỏ nhất đang giữ**. Nếu ứng viên không thắng ranh giới này, nó không thể vào Top-K.

Do đó đống nhỏ nhất đặt đúng ranh giới phần tử ở nút gốc.

Tương tự k smallest dùng đống lớn nhất size k.

## 12. Quickselect cho batch Top-K

Quickselect partition đầu vào để `k` largest/smallest nằm cùng một phía kỳ vọng `O(n)`.

Nếu đầu ra không cần có thứ tự, ta có thể dừng ở đó. Nếu cần Top-K đã được sắp xếp:

\[
O(n)+O(k\log k)
\]

sort riêng selected region.

Heap và Quickselect giải cùng hợp đồng đầu ra dưới khối lượng công việc khác:

```text
stream/bounded memory -> heap
batch/in-memory       -> quickselect
```

## 13. Heapify toàn bộ rồi pop k lần

xây dựng đống lớn nhất `O(n)`, pop k lần:

\[
O(n+k\log n)
\]

Giữ toàn dataset `O(n)` nhưng hợp nếu heap còn dùng sau đó hoặc k tương đối lớn.

Không có một strategy Top-K duy nhất tốt cho mọi `k/n`.

## 14. sắp xếp một phần

Nếu cần prefix Top-K **đã sorted**, sắp xếp một phần có thể phù hợp hơn full sort.

Conceptual distinction:

```text
nth-element: chỉ cần đúng boundary rank
selection: một rank
unordered top-k: đúng membership
sorted top-k: membership + order trong top-k
full sort: order toàn bộ n
```

Mỗi contract chứa lượng thông tin khác nhau.

## 15. Multi-selection: cần nhiều ranks nhưng chưa cần full sort

Nếu cần quartiles hoặc một tập ranks `k1,k2,...`, ta có thể reuse partition cây thay vì chạy Quickselect độc lập cho từng rank.

Một partition chia set ranks thành nhóm trái/phải; recurse chỉ nơi có các hạng cần tìm.

Đây là middle ground giữa one-rank selection và full sorting.

## 16. K-way Merge

Có `m` các danh sách đã sắp xếp và cần k smallest tổng thể. đống nhỏ nhất chứa hiện tại head mỗi list:

1. pop toàn cục smallest;
2. đưa phần tử tiếp theo từ cùng danh sách vào heap;
3. lặp k lần.

Complexity:

\[
O(k\log m)
\]

Không cần merge toàn bộ data.

mẫu này xuất hiện trong bên ngoài sort, cơ sở dữ liệu merge, search shards và time-series streams.

## 17. Top-K frequent các phần tử

Bài này gồm hai phases:

```text
frequency counting
selection theo frequency
```

Bảng băm tạo bảng tần suất trong thời gian kỳ vọng `O(n)`. Sau đó dùng heap kích thước k trên `u` giá trị phân biệt:

\[
O(n+u\log k)
\]

Nếu các tần suất bounded `0..n`, bucket-by-frequency có thể đạt near-linear.

“Top-K” không tự động đồng nghĩa heap; khóa domain có thể mở alternative.

## 18. xử lý luồng các phần tử xuất hiện dày đặc khác chính xác Top-K các giá trị

Nếu muốn items có tần suất cao nhất trong stream khổng lồ, chính xác map có thể cần bộ nhớ theo số distinct các khóa.

bản phác đếm tối thiểu + ứng viên tracking, Space-Saving hoặc Misra–Gries giảm bộ nhớ đổi lấy bảo đảm khác.

Phân biệt:

```text
top-k by raw score per item
vs
top-k frequent over stream
```

chúng là problem khác nhau dù tên giống.

## 19. Quantile trong các hệ thống phân tán

chính xác percentile toàn distributed dataset có thể cần shuffle/sort lớn. xấp xỉ sketches cho phép mỗi shard giữ dữ liệu tóm lược rồi merge.

Nếu chính xác, một strategy có thể dùng distributed selection/partition rounds, nhưng mạng communication trở thành chi phí chính.

Ở scale lớn, độ phức tạp truyền thông có thể quan trọng hơn CPU `O(n)` vs `O(n log n)`.

## 20. Distributed Top-K: cục bộ reduction rồi toàn cục merge

Nếu score mỗi item độc lập và mỗi shard chứa partition disjoint, cục bộ Top-K của mỗi shard là ứng viên superset đủ cho toàn cục Top-K: item không nằm cục bộ Top-K không thể vượt k items cùng shard đã cao hơn nó.

Coordinator chỉ cần merge tối đa `shards * k` các ứng viên.

Đây là một reduction rất mạnh:

```text
huge distributed dataset
-> local top-k
-> much smaller candidate union
-> global top-k
```

Nếu scoring phụ thuộc toàn cục normalization/interaction, tính chất này có thể không còn đúng.

## 21. Threshold các thuật toán cho sorted access

Trong information-retrieval/cơ sở dữ liệu settings, nếu nhiều attribute lists sorted theo partial scores, threshold các thuật toán có thể dừng sớm khi hiện tại Top-K score đã vượt cận trên (upper bound) của unseen các ứng viên.

Đây là một generalization của ranh giới reasoning: maintain cận dưới của winners và cận trên của unknowns.

Không cần full materialization nếu có stopping certificate.

## 22. lựa chọn trên bộ nhớ ngoài

Nếu dữ liệu không vừa RAM, Quickselect tại chỗ trên toàn bộ tập dữ liệu không còn là cách triển khai trực tiếp. Ta có thể partition data thành files/các ngăn băm theo pivot, count sizes, rồi chỉ recurse ngăn băm chứa rank.

Mục tiêu chuyển từ phép so sánh count sang giảm các lượt I/O và byte read/write.

Một thuật toán `O(n)` CPU nhưng nhiều ngẫu nhiên I/O có thể thua bên ngoài strategy sequential các lần quét.

## 23. Selection trên linked data

Quickselect cần efficient partition traversal nhưng không nhất thiết truy cập ngẫu nhiên. Tuy nhiên pointer-heavy list có bộ nhớ đệm chi phí và partition relinking phức tạp.

Nếu data là linked structure nhưng có thể materialize mảng rẻ, chuyển cách biểu diễn (representation) đôi khi thực tế hơn cố implement chuyên biệt list selection.

## 24. Selection các cây và Tournament các cây

Tournament Tree lưu kết quả của các cặp so sánh. Tìm phần tử nhỏ nhất cần `n-1` phép so sánh. Nếu muốn phần tử nhỏ thứ hai, chỉ cần xét những phần tử đã trực tiếp thua phần tử nhỏ nhất trên đường đi, khoảng `log n` ứng viên trong cây giải đấu cân bằng.

Đây là insight thông tin reuse: phép so sánh lịch sử chứa thêm structure cho order thống kê tiếp theo.

Tournament/loser các cây cũng dùng trong k-way bên ngoài merge.

## 25. trực tuyến Median bằng hai heaps

Giữ:

```text
max-heap lower half
min-heap upper half
```

bất biến (invariant):

```text
size difference <= 1
max(lower) <= min(upper)
```

Insert `O(log n)`, median `O(1)`.

Đây không phải bài chọn một lần kinh điển mà là thống kê thứ tự động cho luồng chỉ có thao tác chèn.

Nếu cần xóa phần tử tùy ý, mô hình hai heap cần xóa lười hoặc lập chỉ mục phức tạp hơn; một cây cân bằng có thống kê thứ tự có thể phù hợp hơn.

## 26. Top-K với các cập nhật/deletes

Heap kích thước k trong trường hợp tĩnh giả định mỗi phần tử chỉ được xét một lần. Nếu điểm số thay đổi sau khi chèn, heap không tự sắp xếp lại chỉ vì trường của đối tượng bị thay đổi.

Java `PriorityQueue` không hỗ trợ arbitrary độ ưu tiên cập nhật. Options:

```text
push new version + skip stale
indexed heap
balanced tree keyed by score
periodic rebuild
```

hợp đồng đầu ra động làm cấu trúc dữ liệu choice thay đổi.

## 27. quy tắc phân xử khi bằng nhau và determinism

Nếu nhiều items cùng score, cần secondary order:

```text
score desc
then timestamp asc
then id asc
```

Bộ so sánh phải mã hóa đầy đủ quy tắc phân xử. Nếu không, heap hoặc phép phân hoạch có thể trả thứ tự tùy ý giữa các phần tử hòa nhau, khiến kiểm thử không ổn định và kết quả phân tán không xác định.

Top-K theo **tập phần tử thuộc kết quả** và Top-K theo **danh sách có thứ tự ổn định** là hai hợp đồng khác nhau.

## 28. Floating-point scores

Ranking với `NaN`, `-0`, infinities hoặc floating rounding cần ngữ nghĩa rõ. Comparator không nên giả định thứ tự toàn phần nếu domain có NaN hành vi đặc biệt.

Nếu score được tính từ nhiều floating các thành phần, near-tie các kết quả có thể nhạy với evaluation order. Trong hệ thống thực tế, ranking thường cần xác định normalization/tie-break khóa.

## 29. Java/C/JavaScript comparator caveats

Java/C comparator dùng subtraction có thể tràn số:

```java
return a.score - b.score;
```

nên dùng `Integer.compare`/`Long.compare`.

Bộ so sánh cho `Number` trong JavaScript phải trả giá trị âm, 0 hoặc dương. Với `BigInt`, không nên trả trực tiếp kết quả số học BigInt nếu API mong dấu dạng Number; hãy dùng các nhánh so sánh quan hệ.

Comparator tính đúng đắn là prerequisite của heap/sort/ordered selection.

## 30. sự thay đổi dữ liệu contract

Quickselect thường mutate mảng. Heap xử lý luồng không cần reorder đầu vào. Full sort có thể mutate tùy API.

Nếu bên gọi cần giữ nguyên thứ tự ban đầu, việc sao chép tốn `O(n)` thời gian và bộ nhớ. Đây là một đánh đổi kỹ thuật thực sự, không chỉ là vấn đề phong cách mã.

## 31. kiểm thử Quickselect

tham chiếu oracle:

```text
copy input
sort copy
expected = copy[k]
```

ngẫu nhiên small các mảng cho differential kiểm thử rất hiệu quả.

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

Nếu ngẫu nhiên hóa, log seed để reproduce failure.

## 32. tính chất của k-th statistic

Nếu answer `x` cho zero-based rank `k`, phải có đủ số các phần tử `< x` và `<= x` phù hợp phần tử trùng ngữ nghĩa để rank `k` nằm trong equal block của `x`.

tính chất này giúp verify kết quả mà không cần chính xác pivot lịch sử.

## 33. kiểm thử Top-K

So sánh đa tập đầu ra với k phần tử đầu của kết quả tham chiếu đã sắp xếp hoàn toàn. Nếu hợp đồng đầu ra yêu cầu có thứ tự, so sánh dãy; nếu không yêu cầu thứ tự, so sánh bảng tần suất hoặc đa tập.

quy tắc phân xử khi bằng nhau phải được test riêng nếu API xác định.

## 34. đối kháng đầu vào và pivot strategy

Quickselect xác định pivot đầu/cuối dễ bị sorted/đối kháng đầu vào phá `O(n²)`.

ngẫu nhiên pivot, median-of-three hoặc introspective fallback giúp giảm risk. Public APIs phải cân nhắc đối kháng callers nếu độ trễ (latency)/security quan trọng.

## 35. Strategy matrix theo khối lượng công việc

Một rank, batch, sự thay đổi dữ liệu allowed:

```text
Quickselect
```

Một rank, xác định trường hợp xấu nhất bound bắt buộc:

```text
Median of Medians / deterministic selection
```

Top-K xử lý luồng, k nhỏ:

```text
bounded heap
```

Top-K batch unsorted:

```text
Quickselect
```

Top-K sorted:

```text
selection + sort k
heap
partial sort
```

Nhiều rank các truy vấn:

```text
sort once
order-stat tree
multi-selection
```

xử lý luồng percentile xấp xỉ:

```text
quantile sketch
```

## Mô hình tư duy

> Các thuật toán chọn khai thác việc đầu ra chỉ yêu cầu **một ranh giới trong thứ tự**, không cần toàn bộ thứ tự. Quickselect loại bỏ từng vùng; heap duy trì ranh giới; Tournament Tree tái sử dụng lịch sử so sánh; Top-K phân tán giảm tập ứng viên trước khi gộp.

Trước khi chọn thuật toán, hãy viết chính xác hợp đồng đầu ra: một rank, unordered Top-K, sorted Top-K, động rank, tần suất các phần tử xuất hiện dày đặc hay xấp xỉ percentile. Chỉ một từ “Top-K” chưa đủ xác định bài toán.

Xem thêm: [Heap](../02_trees/03_heaps.md), [Sorting](./01_sorting.md), [Probabilistic Structures](../05_specialized/06_probabilistic_data_structures.md), [Complexity](../00_foundations/02_complexity_analysis.md).