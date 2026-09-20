# Quy trình giải bài DSA và thiết kế thuật toán
**Problem-Solving Workflow / 문제 해결 흐름**

Giải một bài DSA tốt không bắt đầu bằng việc cố nhớ “mẫu nào giống LeetCode”, mà bắt đầu bằng **đặc tả đúng vấn đề**, xây mô hình đúng, tìm một baseline đúng, rồi loại bỏ dần những phần công việc không cần thiết.

Một lời giải đáng tin thường có bốn lớp:

```text
mô hình trạng thái đúng
cách biểu diễn đúng
bất biến / chứng minh đúng
mô hình chi phí phù hợp
```

Nếu một trong bốn lớp sai, code có thể vẫn chạy trên sample nhưng lời giải không bền vững.

## 1. Đọc đề như một specification

Trước khi code, phải xác định:

```text
input domain
output semantics
preconditions
constraints
edge cases
error behavior
```

Các từ rất giống nhau có thể tạo bài khác hoàn toàn:

```text
subarray      -> liên tiếp
subsequence   -> giữ thứ tự nhưng không cần liên tiếp
subset        -> không quan tâm vị trí
path          -> chuỗi đỉnh/cạnh hợp lệ
simple path   -> không lặp đỉnh
walk          -> có thể lặp
```

Nếu terminology chưa rõ, thuật toán chưa thể bắt đầu chắc chắn.

## 2. Viết lại bài toán bằng một câu

Một kỹ thuật đơn giản nhưng mạnh:

> “Tôi cần tìm/đếm/tối ưu **X**, sao cho **Y**, dưới các ràng buộc **Z**.”

Ví dụ:

> “Tìm chi phí nhỏ nhất để đi từ `s` tới `t`, với trọng số cạnh không âm.”

Câu này ngay lập tức làm lộ domain thích hợp cho Dijkstra.

Nếu chưa viết được bài toán bằng câu ngắn, story layer vẫn đang che mô hình thật.

## 3. Tách story khỏi computational model

“Thành phố” có thể là đỉnh. “Chuyến bay” là cạnh. “Khóa và cửa” có thể biến trạng thái thành `(position,keyMask)`. “Booking” là interval. “Undo” là stack. “Mạng lưới phụ thuộc” là DAG.

Story chỉ là tên gọi. Thuật toán làm việc trên cấu trúc toán học bên dưới.

Một thuật toán đúng trên mô hình sai vẫn giải sai vấn đề.

## 4. Ràng buộc là ngân sách complexity

Hãy chuyển constraints thành quy mô work sơ bộ.

```text
n <= 20         -> 2^n có thể khả thi
n ~ 10^3        -> n^2 có thể khả thi
n ~ 10^5        -> thường cần n log n hoặc n
n ~ 10^6        -> memory/allocation cũng thành vấn đề lớn
Q ~ 10^5        -> preprocessing/index có thể rất đáng
```

Đây chỉ là heuristic, không phải luật cứng. Runtime, constant factor và time limit vẫn quan trọng.

Nhưng constraints giúp loại nhanh những ý tưởng bất khả thi.

## 5. Đừng chỉ nhìn n; tìm mọi tham số

Graph có `V` và `E`. String matching có `n` và `m`. Top-K có `n` và `k`. Knapsack có `n` và `W`.

Một complexity như:

\[
O(n\log k)
\]

có thể tốt hơn nhiều `O(n log n)` khi `k` nhỏ.

Giữ tham số riêng giúp thấy structure mà việc ép tất cả thành một `n` sẽ che mất.

## 6. Tìm baseline đúng trước

Brute force không phải đáp án “ngu ngốc”; nó là **đặc tả có thể chạy được**.

Baseline giúp:

```text
xác nhận hiểu đề
làm oracle cho test nhỏ
cho thấy work nào đang bị lặp
```

Two Sum `O(n²)` làm lộ rằng inner loop chỉ đang hỏi “complement đã xuất hiện chưa?”, từ đó Hash Set loại quét lặp.

Range Sum brute force làm lộ rằng cùng prefix bị cộng lại nhiều lần, dẫn tới Prefix Sum.

Memoization làm lộ rằng nhiều nhánh recursion đang tính lại cùng state.

## 7. Hỏi: “Tôi đang tính lại cái gì?”

Đây là câu hỏi tối ưu hóa quan trọng nhất.

Các dạng lặp lại phổ biến:

```text
quét lại cùng prefix
so lại cùng pair
tính lại cùng state
sort lại dữ liệu đã có thứ tự
lookup tuyến tính lặp lại
recompute aggregate sau mỗi update
```

Structure thường xuất hiện để **materialize một summary** giúp tránh recomputation.

## 8. Thiết kế state

Một state tốt phải đủ thông tin để tương lai được xác định, nhưng không giữ lịch sử thừa.

Ví dụ grid có key/door:

```text
(row, col)              -> thiếu
(row, col, keyMask)     -> đủ hơn
```

Nếu hai lịch sử khác nhau dẫn tới cùng state và từ đó mọi action/cost tương lai tương đương, ta có thể gộp chúng.

Đây là nền tảng của memoization, DP và state-space graph.

## 9. Nhận diện state explosion

Nếu state có nhiều chiều:

```text
position × mask × time × resource
```

không gian có thể tăng theo tích các miền.

Trước khi code, ước lượng số state tối đa.

```text
n * 2^k
n * m * k
V * stops
```

Một DP transition `O(1)` vẫn vô dụng nếu số state là `10^12`.

## 10. Dense hay Sparse State?

Nếu phần lớn state có thể xuất hiện, array/table dense thường nhanh và memory predictable.

Nếu chỉ một phần rất nhỏ reachable, Hash Map/Set có thể tiết kiệm memory dù lookup đắt hơn.

Đừng chỉ hỏi “DP array hay map”; hãy hỏi density của reachable state.

## 11. Chọn representation trước thuật toán chi tiết

Graph sparse:

```text
adjacency list
```

Graph dense hoặc cần edge lookup nhanh:

```text
adjacency matrix
```

Key integer dense:

```text
array
```

Key sparse/string:

```text
Hash Map
```

Representation quyết định cost của operation tiếp theo.

## 12. Viết invariant trước loop phức tạp

Nếu không thể nói loop đang bảo vệ điều gì, code rất dễ biến thành trial-and-error.

Binary search:

> nếu answer tồn tại, nó vẫn nằm trong vùng ứng viên hiện tại.

Sliding window:

> cửa sổ hiện tại luôn thỏa constraint; left là ranh giới nhỏ nhất/lớn nhất theo invariant đã chọn.

Monotonic deque:

> deque chứa đúng candidate chưa hết hạn, theo thứ tự giá trị đơn điệu.

## 13. Invariant cần đủ mạnh

“Inorder prefix đã sorted” chưa đủ chứng minh sorting nếu không đảm bảo các phần tử không bị mất hoặc nhân đôi.

Một invariant tốt thường gồm:

```text
shape/order property
membership/conservation property
candidate completeness
```

Nó phải đủ mạnh để kết hợp với điều kiện dừng suy ra postcondition.

## 14. Tách correctness và complexity

Correctness trả lời:

```text
vì sao answer đúng?
```

Complexity trả lời:

```text
phải làm bao nhiêu work và dùng bao nhiêu memory?
```

Một thuật toán có thể đúng nhưng quá chậm; hoặc nhanh nhưng sai.

Đừng dùng “Big-O tốt” như bằng chứng đúng đắn.

## 15. Pattern chứng minh

Các pattern phổ biến:

```text
loop invariant
structural induction
strong induction
exchange argument
greedy stays-ahead
cut/cycle property
contradiction
optimal substructure
residual/certificate proof
```

Nhận diện pattern chứng minh thường quan trọng hơn nhận diện tên thuật toán.

## 16. Khi baseline O(n²), thử những câu hỏi nào?

Nếu đang xét mọi cặp:

```text
sort có tạo monotonic order không?
hash có thay inner scan bằng lookup không?
two pointers có loại cả vùng candidate không?
prefix/difference có tái sử dụng aggregate không?
sweep line có biến pair interaction thành event stream không?
```

Không có một mẹo duy nhất; mục tiêu là tìm **thông tin nào giúp loại nhiều ứng viên cùng lúc**.

## 17. Khi recursion exponential, thử gì?

```text
có overlapping states không?        -> memoization / DP
có branch vô ích nhận ra sớm không? -> pruning
có bound tốt không?                 -> branch-and-bound
có symmetry không?                  -> canonicalization
n có ~40 không?                     -> meet-in-the-middle
parameter nhỏ không?                -> FPT / bitmask DP
```

Cây tìm kiếm lớn thường được giảm bằng cách hợp nhất state hoặc loại nhánh.

## 18. Khi có nhiều query

Một query duy nhất có thể quét thẳng. `10^5` query trên cùng data thường đáng để preprocess.

```text
sorting
prefix sum
index
Sparse Table
binary lifting
suffix array
```

Hãy so:

\[
C_{build}+Q\cdot C_{query}
\]

với cách không tiền xử lý.

## 19. Khi vừa update vừa query

Nếu prefix sum bị phá bởi update, chuyển sang structure động như Fenwick/Segment Tree.

Nếu sorted array bị phá bởi insert/delete thường xuyên, chuyển sang balanced tree hoặc structure khác.

Update/query trade-off chính là lý do nhiều data structures tồn tại.

## 20. Chú ý objective thay đổi thuật toán

Cùng dữ liệu interval:

```text
max số interval không overlap   -> greedy
tối đa tổng trọng số            -> DP
minimum rooms                   -> sweep/heap
union length                    -> merge/sweep
```

Đừng nhận diện thuật toán chỉ từ “dữ liệu là interval”. Objective quyết định structure reasoning.

## 21. Edge Case phải sinh từ assumption

Nếu Dijkstra yêu cầu non-negative weight, test cạnh âm.

Nếu binary search yêu cầu sorted array, test duplicates/boundaries.

Nếu comparator yêu cầu transitive, test equal/tie cases.

Nếu recursion depth có thể `n`, test skewed tree/path graph.

Edge cases tốt nhất xuất phát từ **điều kiện mà proof sử dụng**.

## 22. Integer Overflow

Một thuật toán đúng trên số nguyên toán học có thể sai trong machine integer.

```java
mid = (lo + hi) / 2
```

có thể overflow với integer hữu hạn; mẫu an toàn hơn:

```java
mid = lo + (hi - lo) / 2
```

Distance, prefix sum, count và multiplication phải được bound trước khi chọn kiểu số.

## 23. Floating Point

Nếu comparator dùng epsilon thiếu nhất quán, có thể phá transitivity và làm sort/tree sai.

Geometry predicate gần 0 có thể đổi dấu do rounding.

Numeric semantics là một phần của specification.

## 24. Language-Specific Review

### C

```text
bounds
ownership
allocation failure
integer overflow
undefined behavior
pointer invalidation
```

### Java

```text
boxing
equals/hashCode
Comparator
mutable key
StackOverflowError
GC/allocation
```

### JavaScript

```text
Number safe integer
bitwise 32-bit coercion
Array.shift cost
Map object identity
sort comparator
UTF-16 semantics
```

Một thuật toán trừu tượng đúng vẫn cần implementation phù hợp ngôn ngữ.

## 25. Dry-Run như một state trace

Đừng chỉ đọc code bằng mắt. Tạo input nhỏ nhưng khó chịu và ghi:

```text
lo/hi/mid
stack/queue content
heap
visited
DP states
parent links
window boundaries
```

Mỗi transition phải giải thích được bằng invariant.

Nếu một biến cập nhật mà không biết nó bảo vệ tính chất nào, đó là dấu hiệu thiết kế chưa rõ.

## 26. Test Oracle

Với input nhỏ, dùng giải pháp chậm nhưng rõ ràng làm oracle.

```text
Dijkstra       vs Floyd-Warshall
Segment Tree   vs array scan
Top-K          vs full sort
MST            vs brute force nhỏ
custom map     vs standard map
```

Differential testing bắt implementation bug rất hiệu quả.

## 27. Property-Based Testing

Thay vì chỉ test output cụ thể, test tính chất:

```text
sort output ordered + same multiset
heap pop sequence nondecreasing
DSU union(a,b) => find(a)==find(b)
BFS dist[v] <= dist[u]+1 trên edge tree phù hợp
```

Tính chất thường gần proof hơn example test.

## 28. Adversarial Test

Random input không thay thế input bệnh lý.

```text
sorted/reverse/all equal
long collision chain
skewed tree
line graph
complete graph
large duplicate set
many equal event times
maximum recursion depth
```

Adversarial test kiểm tra đúng nơi asymptotic hoặc invariant dễ vỡ nhất.

## 29. Complexity Review toàn pipeline

Nếu preprocessing `O(n log n)` và mỗi query `O(log n)`, với `Q` query:

\[
O(n\log n + Q\log n)
\]

Nếu helper bên trong loop là `O(n)`, phải tính nó vào tổng.

Nếu `sort()` được gọi trong mỗi iteration, complexity có thể lớn hơn trực giác rất nhiều.

Không chỉ phân tích “core loop”.

## 30. Space Review

Tính cả:

```text
input copy
aux arrays
hash-table slack
object overhead
recursion stack
memo table
adjacency edges
```

`O(n)` memory có thể vẫn vượt limit vì hệ số lớn.

## 31. Output Size Lower Bound

Nếu phải xuất `k` kết quả, complexity ít nhất `Ω(k)`.

Không thể yêu cầu liệt kê một triệu occurrence trong `O(log n)` chỉ vì index search nhanh.

Luôn tách:

```text
cost tìm vùng kết quả
cost materialize output
```

## 32. Stop Optimization khi đủ

Nếu constraint cho phép `O(n²)` an toàn và solution đơn giản, đôi khi đó là lựa chọn tốt hơn một structure rất phức tạp.

Độ phức tạp code tạo bug và maintenance cost.

Mục tiêu là **đủ tốt với proof rõ**, không phải luôn dùng thuật toán mạnh nhất biết được.

## 33. Profile trước Micro-Optimization

Sau khi asymptotic đã phù hợp, profiling mới trả lời bottleneck thật nằm ở:

```text
allocation
hashing
comparator
cache miss
GC
I/O
network
```

Đừng thay HashMap bằng custom structure chỉ từ trực giác nếu path đó chỉ chiếm 1% runtime.

## 34. Từ Interview Solution tới Production

Một solution algorithmic đúng còn cần:

```text
input validation
resource limits
observability
error handling
concurrency semantics
serialization/versioning
backpressure
failure recovery
```

Production hardening không thay đổi proof lõi nhưng mở rộng contract của hệ thống.

## 35. Viết Solution Note sau khi giải

Một ghi chú tốt nên trả lời:

```text
mô hình bài toán
baseline
bottleneck của baseline
insight tối ưu
invariant/proof
complexity
edge cases
implementation caveats
alternative approaches
```

Cách này biến một bài giải đơn lẻ thành kiến thức tái sử dụng.

## 36. Postmortem khi sai

Không chỉ sửa dòng code. Hãy phân loại lỗi:

```text
mô hình sai
state thiếu
invariant sai
boundary sai
complexity sai
integer/precision sai
representation sai
implementation bug
```

Phân loại đúng giúp tránh lặp lại cùng kiểu lỗi ở bài khác.

## 37. Một quy trình 12 bước

```text
1. Viết lại specification.
2. Xác định mọi constraint và parameter.
3. Bỏ story, dựng computational model.
4. Viết baseline đúng.
5. Xác định work bị lặp hoặc candidate thừa.
6. Thiết kế state tối thiểu đủ thông tin.
7. Chọn representation phù hợp.
8. Viết invariant/proof sketch.
9. Tính time + space toàn pipeline.
10. Test bằng oracle + adversarial cases.
11. Profile nếu cần tối ưu thực tế.
12. Ghi lại insight, không chỉ code.
```

## 38. Checklist trước khi nộp hoặc merge

```text
Output semantics có đúng mọi case không?
Có dùng giả định nào đề không bảo đảm không?
Invariant có được giữ sau mọi update không?
Termination có chắc chắn không?
Complexity có tính helper/API ẩn không?
Kiểu số có đủ không?
Recursion depth an toàn không?
Có mutation/invalidation ngoài ý muốn không?
Test adversarial đã có chưa?
Có cách oracle nhỏ để đối chiếu không?
```

## Mô hình tư duy

> Giải DSA là quá trình **giảm không gian bất định**: specification xác định câu hỏi, model xác định state, invariant loại bỏ trạng thái sai, data structure lưu thông tin hữu ích, còn thuật toán quyết định thứ tự khai thác thông tin đó.

Khi bí, đừng hỏi “mẫu này dùng thuật toán gì?”. Hãy quay lại hỏi: **baseline đang làm thừa công việc nào, state nào thực sự ảnh hưởng tương lai, invariant nào cho phép bỏ candidate, và structure nào materialize thông tin đó rẻ nhất?**

Xem thêm: [Problem Modeling](../00_foundations/00_dsa_as_problem_modeling.md), [Correctness & Invariants](../00_foundations/01_algorithm_correctness_and_invariants.md), [Complexity](../00_foundations/02_complexity_analysis.md), [Choose the Right Data Structure](./00_choose_the_right_data_structure.md), [Cross-Language Testing](../80_language_implementations/03_cross_language_testing_and_benchmarking.md).