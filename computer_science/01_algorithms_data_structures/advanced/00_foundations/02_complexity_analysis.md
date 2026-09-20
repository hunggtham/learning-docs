# Phân tích độ phức tạp
**Complexity Analysis / 복잡도 분석**

Độ phức tạp mô tả cách lượng tài nguyên cần thiết tăng theo kích thước input. Hai tài nguyên được nhắc nhiều nhất là **thời gian (Time Complexity / 시간 복잡도)** và **bộ nhớ (Space Complexity / 공간 복잡도)**, nhưng trong hệ thống thật còn có số lần I/O, cache miss, network round-trip, allocation, branch misprediction hoặc synchronization. Vì vậy complexity analysis không phải một bảng Big-O để học thuộc, mà là một **mô hình tăng trưởng** giúp ta biết design nào sẽ tiếp tục hoạt động khi dữ liệu lớn lên.

Một benchmark 2 ms hôm nay không trả lời được câu hỏi “điều gì xảy ra khi input tăng 100 lần?”. Complexity analysis cố trả lời câu hỏi đó bằng cách bỏ bớt chi tiết phần cứng và nhìn vào cấu trúc của computation.

## 1. Tại sao không chỉ đo milliseconds?

Giả sử hai implementation cùng xử lý `n = 1_000` trong thời gian tương tự. Một cái có cost gần `n`, cái còn lại gần `n²`. Ở input nhỏ, constants và cache có thể che khác biệt. Khi `n` tăng 100 lần, thuật toán tuyến tính tăng khoảng 100 lần, còn thuật toán bậc hai có thể tăng khoảng 10.000 lần.

Nếu runtime có dạng:

\[
T(n)=3n^2+5n+20
\]

thì khi `n` lớn, term `n²` chi phối. Ta nói `T(n)=O(n^2)`. Nếu bound trên và dưới cùng order, ta dùng `Θ(n²)`. Ký hiệu `Ω` diễn tả lower bound.

Các ký hiệu này không phải ba cách nói cùng một câu:

- `O(f(n))` nói cost không tăng nhanh hơn một hằng số nhân `f(n)` sau một ngưỡng nào đó;
- `Ω(f(n))` nói cost không tăng chậm hơn một hằng số nhân `f(n)`;
- `Θ(f(n))` nói growth bị kẹp hai phía cùng order.

Trong trao đổi engineering, người ta thường dùng Big-O hơi lỏng để nói “order of growth”, nhưng khi cần reasoning chặt, nên biết mình đang nói upper bound hay tight bound.

## 2. Growth rate quan trọng hơn code dài bao nhiêu

Một function 5 dòng có thể `O(n²)`; một function 100 dòng có thể `O(n)`. Complexity không đo source-code length mà đo **số operation hoặc lượng state tăng theo input**.

Các growth rate phổ biến:

| Complexity | Mental model |
|---|---|
| `O(1)` | cost không tăng theo `n` |
| `O(log n)` | mỗi bước loại hoặc gộp một tỷ lệ cố định của search space |
| `O(n)` | đi qua dữ liệu một số lần hằng số |
| `O(n log n)` | `log n` tầng, mỗi tầng làm tổng work tuyến tính |
| `O(n²)` | tương tác theo cặp hoặc nested state-space |
| `O(2^n)` | mỗi phần tử mở thêm nhánh binary decision |
| `O(n!)` | enumerate permutations |

Binary search giảm interval một nửa:

\[
n,\frac n2,\frac n4,\ldots,1
\]

Sau `k` bước:

\[
\frac{n}{2^k}=1 \Rightarrow k=\log_2 n
\]

`log n` xuất hiện vì mỗi bước co không gian còn lại theo tỷ lệ, không phải vì “binary search luôn có log”.

## 3. Input size không phải lúc nào cũng chỉ là `n`

Graph có thể cần hai biến `V` và `E`. Matrix có `R` và `C`. String algorithm có thể phụ thuộc `n + m`. Một hash table workload còn phụ thuộc load factor. Knapsack có `n` items và capacity `W`.

Ví dụ BFS adjacency list là:

\[
O(V+E)
\]

không nên rút gọn thành `O(n)` nếu điều đó làm mất thông tin quan trọng về graph density.

Một graph sparse có `E≈V`, còn graph dense có thể `E≈V²`. Cùng công thức `O(V+E)` có hành vi thực tế rất khác giữa hai regime.

## 4. Best-case, average-case, expected-case và worst-case

Các từ này thường bị trộn lẫn nhưng có semantics khác nhau.

Linear search có best-case `O(1)` nếu target ở đầu, worst-case `O(n)` nếu target ở cuối hoặc không tồn tại. Average-case chỉ có nghĩa nếu ta định nghĩa distribution của target/input.

**Expected complexity** thường xuất hiện khi algorithm hoặc data structure tự dùng randomness. Randomized Quickselect có expected linear time với random pivot dưới analysis chuẩn. Hash table expected lookup gần `O(1)` khi hashing phân phối đủ tốt.

Expected không có nghĩa “đa số case đều đúng bằng expected”. Một distribution có thể có mean tốt nhưng tail rất xấu. Trong hệ thống latency-sensitive, p95/p99 và worst-case spikes có thể quan trọng hơn expectation.

## 5. Amortized không phải average

Dynamic array append thường được gọi amortized `O(1)`. Điều đó không dựa vào random input. Nó nói rằng trên **mọi sequence đủ dài** theo growth policy, tổng cost của sequence bị bound tuyến tính.

Nếu capacity tăng gấp đôi:

```text
1 -> 2 -> 4 -> 8 -> ...
```

các lần resize copy tổng cộng:

\[
1+2+4+\cdots+\frac n2 < n
\]

nên `n` appends có total `O(n)`, amortized `O(1)` mỗi append.

Một append riêng lẻ vẫn có thể `O(n)` khi resize. Đây là khác biệt rất quan trọng trong real-time systems: amortized throughput tốt không đảm bảo tail latency thấp.

## 6. Ba cách nhìn amortized analysis

Có ba framework kinh điển.

**Aggregate method** tính tổng cost của cả sequence rồi chia cho số operations.

**Accounting method** gán “giá” cao hơn cho operation rẻ để tích credit trả cho operation đắt sau này.

**Potential method** định nghĩa một hàm potential `Φ(state)` đại diện work đã “tích trữ” trong cấu trúc. Amortized cost thường viết:

\[
\hat c_i = c_i + \Phi(D_i)-\Phi(D_{i-1})
\]

Dynamic array, stack multipop, splay tree và một số union-find reasoning đều hưởng lợi từ góc nhìn này.

## 7. Phân tích loop từ update rule, không từ số tầng indentation

Nested loops không tự động `O(n²)`.

```java
for (int i = 0; i < n; i++) {
    for (int j = 1; j < n; j *= 2) {
        consume(i, j);
    }
}
```

Loop ngoài `n`, loop trong `log n`, tổng:

\[
\Theta(n\log n)
\]

Ngược lại một loop đơn cũng có thể chứa operation ẩn `O(n)`, ví dụ remove đầu dynamic array, string concatenation kiểu copy toàn prefix, hoặc `LinkedList.get(i)` lặp đi lặp lại.

Nguyên tắc đúng là: **phân tích cost của mỗi primitive/API được gọi, rồi cộng hoặc nhân theo control flow**.

## 8. Summation là công cụ phân tích quan trọng

Loop:

```c
for (int i = 0; i < n; ++i)
    for (int j = 0; j <= i; ++j)
        work();
```

thực hiện:

\[
1+2+\cdots+n=\frac{n(n+1)}2=\Theta(n^2)
\]

Một pattern khác:

\[
1+2+4+8+\cdots+n=\Theta(n)
\]

là lý do nhiều algorithm có inner loop tăng theo powers of two nhưng tổng work vẫn tuyến tính ở một số construction.

Phân tích complexity thường là việc nhận ra sequence/tổng nào đang ẩn trong code.

## 9. Recurrence cho recursive algorithms

Merge sort:

\[
T(n)=2T(n/2)+\Theta(n)
\]

Mỗi level có tổng work `Θ(n)`, có `Θ(log n)` levels, nên:

\[
T(n)=\Theta(n\log n)
\]

Binary search:

\[
T(n)=T(n/2)+\Theta(1)=\Theta(\log n)
\]

Quicksort worst case:

\[
T(n)=T(n-1)+\Theta(n)=\Theta(n^2)
\]

Master Theorem là shortcut cho một family recurrence, nhưng recursion tree hoặc substitution thường cho intuition rõ hơn khi sizes không đều.

## 10. Space complexity: live memory khác total allocation

Một algorithm có thể allocate tổng cộng rất nhiều bytes theo thời gian nhưng peak live memory nhỏ nếu memory được reclaim dần. Khi nói auxiliary space `O(n)`, thường ta quan tâm **simultaneously live extra memory** chứ không phải tổng bytes từng xin từ allocator.

Recursive DFS tree height `h` dùng call stack `O(h)`. Merge sort array thường dùng auxiliary buffer `O(n)`. Quicksort in-place có data auxiliary nhỏ nhưng recursion stack expected `O(log n)`, worst `O(n)`.

Trong GC runtime, object allocation rate và retained memory là hai metric khác nhau. Nhiều temporary objects có thể gây GC pressure dù peak logical structure không lớn.

## 11. Output-sensitive complexity

Nếu output tự nó có `k` items, một algorithm phải tốn ít nhất `Ω(k)` chỉ để emit chúng. Vì vậy range query hay geometry algorithm thường có complexity dạng:

\[
O(f(n)+k)
\]

Balanced BST range query có thể `O(log n + k)`; graph traversal liệt kê mọi edge phải ít nhất `Ω(E)`.

Đây là cách tránh đặt mục tiêu bất khả thi như “liệt kê một triệu kết quả trong O(log n)”.

## 12. Input-sensitive và adaptive complexity

Một số algorithm chạy nhanh hơn trên input có cấu trúc thuận lợi. Insertion sort gần `O(n)` trên nearly-sorted data. Timsort khai thác existing runs. Union-find performance phụ thuộc sequence operations nhưng có amortized bound rất mạnh.

Khi một algorithm có performance phụ thuộc “disorder”, “number of inversions”, “tree height”, “number of distinct keys”, nên giữ parameter đó thay vì ép mọi thứ về chỉ `n`.

## 13. Pseudopolynomial complexity và bit-length

Knapsack DP `O(nW)` với capacity `W` nhìn giống polynomial, nhưng input cần chỉ `O(log W)` bits để biểu diễn `W`. Vì vậy theo bit-length, `O(nW)` có thể exponential. Ta gọi đây là **pseudopolynomial / 의사 다항 시간**.

Distinction này quan trọng khi đi từ algorithm design sang complexity theory: “polynomial theo numeric value” không đồng nghĩa “polynomial theo độ dài input encoding”.

## 14. Comparison model và lower bound

Comparison sorting phải phân biệt `n!` permutations. Một comparison có hữu hạn outcomes, nên decision tree cần depth ít nhất:

\[
\Omega(\log(n!))=\Omega(n\log n)
\]

Đây là lý do không thể có general comparison sort `o(n log n)` trong worst case.

Counting sort/radix sort không vi phạm bound vì chúng dùng thông tin khác ngoài pairwise comparison — chúng khai thác key representation/range.

Lower bound giúp ta biết khi nào cần đổi problem model thay vì cố “tối ưu code” thêm.

## 15. Complexity contract của API

Library abstraction không xóa cost model.

Java `ArrayList.get(i)` gần `O(1)`; `LinkedList.get(i)` `O(n)`. JavaScript `Array.shift()` có thể kéo theo reindex/compaction cost; `push/pop` cuối thường phù hợp hơn cho stack. HashMap expected lookup khác TreeMap `O(log n)` nhưng TreeMap giữ order.

Một refactor đổi implementation collection có thể làm toàn function đổi bậc complexity dù business logic không đổi dòng nào.

Vì vậy complexity nên được xem như một phần của **API contract engineering**.

## 16. Cache complexity và memory hierarchy

Hai algorithms cùng `O(n)` có thể chênh rất lớn nếu một cái quét contiguous memory còn cái kia pointer-chasing.

```text
array scan       -> spatial locality, prefetch-friendly
linked traversal -> random-ish addresses, cache-miss prone
```

Trong external-memory model, ta đôi khi đếm block transfers thay vì CPU operations. B-Tree tối ưu chiều cao theo page fan-out vì disk/page I/O đắt hơn comparison.

Asymptotic RAM model vẫn cực hữu ích, nhưng production reasoning nên có tầng thứ hai về locality và data movement.

## 17. CPU, branch prediction và vectorization

Một algorithm có nhiều branches data-dependent khó dự đoán có thể chậm hơn một scan tuyến tính đơn giản dù operation count tương tự. Contiguous numeric arrays còn có khả năng vectorization/SIMD.

Điều này giải thích vì sao binary search với ít comparisons chưa chắc nhanh hơn linear scan cho array rất nhỏ: branch/cache overhead có thể chi phối constant factors.

Big-O trả lời scale; microarchitecture trả lời constants.

## 18. Tail latency và deterministic bounds

Trong batch processing, average throughput thường quan trọng. Trong scheduler, trading, audio hoặc request-serving systems, một spike đơn lẻ có thể gây deadline miss.

Dynamic array append amortized `O(1)` nhưng resize event `O(n)`. Hash table incremental resize có thể được dùng để phân tán cost thay vì một lần rehash lớn. Real-time queue có thể ưu tiên fixed-capacity ring buffer để tránh allocation spikes.

Khi requirement là worst-case latency, hãy phân biệt:

```text
expected bound
amortized bound
worst-case bound
high-probability bound
```

chúng không thay thế lẫn nhau.

## 19. Concurrency làm cost model thay đổi

Một concurrent map không chỉ có `get/put` cost theo số elements. Contention, cache-line bouncing, lock convoy, retries hoặc memory fences có thể trở thành bottleneck.

Một theoretically `O(1)` atomic loop có thể chậm khi nhiều threads tranh cùng state. Vì vậy complexity của sequential algorithm là baseline, không phải toàn bộ performance model concurrent.

## 20. Distributed complexity

Trong distributed systems, network round-trip có thể đắt hơn hàng triệu CPU instructions. Một algorithm `O(log n)` nhưng cần nhiều sequential RPCs có thể chậm hơn một batch `O(n)` xử lý local.

Vì thế đôi khi cost nên viết theo dimensions:

```text
CPU work
memory
number of disk I/Os
number of network rounds
bytes transferred
```

MapReduce, distributed sorting, database query planning và graph processing thường tối ưu communication complexity không kém CPU complexity.

## 21. Benchmark để kiểm chứng, không thay proof

Một quy trình tốt:

1. phân tích asymptotic growth;
2. xác định hidden parameters và assumptions;
3. đo nhiều input sizes;
4. kiểm tra memory/allocation/locality;
5. profile hot path;
6. benchmark workload gần production.

Nếu runtime curve không giống theory, hãy kiểm tra constants, JIT/GC, cache, compiler optimization, input regime hoặc bug trong benchmark trước khi kết luận complexity analysis sai.

## 22. Ví dụ: chọn structure cho lookup service

Giả sử 10 triệu records, workload:

```text
95% exact lookup by id
4% insert/update
1% range scan
```

Hash table có expected lookup tốt nhưng range scan không ordered. Balanced tree có `O(log n)` lookup nhưng range operations tốt. Có thể solution thật là hash table cho hot exact lookup + ordered index riêng cho range, hoặc database index quản lý hai access paths.

Complexity không chọn structure thay ta; nó giúp định lượng trade-off theo workload.

## 23. Checklist phân tích complexity

Khi nhìn một algorithm, hãy hỏi:

```text
Input size được đo bằng biến nào?
Operation primitive nào thật sự tốn cost?
Loop update theo +1, *2 hay phụ thuộc data?
Recursive subproblems có size/số lượng ra sao?
Output size có phải lower bound không?
Có amortized/expected/randomized guarantee không?
Peak memory hay allocation rate quan trọng hơn?
Representation có làm locality khác đi không?
API/library call có hidden traversal/copy không?
Production cần average throughput hay worst-case latency?
```

## Mental Model

> Complexity analysis là nghệ thuật xây **cost model đủ đơn giản để suy luận, nhưng đủ đúng để hướng dẫn design**.

Big-O cho ta hình dạng tăng trưởng. Amortized/expected/worst-case cho ta loại guarantee. Cache, allocation, I/O và contention cho ta cost model thực tế hơn. Benchmark cuối cùng xác nhận implementation trên workload thật.

Xem thêm: [Mathematical Toolkit](./04_mathematical_toolkit_for_dsa.md), [Memory Models](./03_memory_models_c_java_javascript.md), [Testing & Benchmarking](../80_language_implementations/03_cross_language_testing_and_benchmarking.md).