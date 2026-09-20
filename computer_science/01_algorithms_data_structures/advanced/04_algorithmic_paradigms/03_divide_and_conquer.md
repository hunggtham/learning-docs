# Divide and Conquer
**Chia để trị / Divide and Conquer / 분할 정복**

Divide and Conquer là một chiến lược thiết kế thuật toán trong đó một problem lớn được tách thành các subproblems nhỏ hơn có cấu trúc tương tự, giải các phần đó, rồi ghép kết quả lại. Pattern kinh điển:

```text
Divide → Conquer → Combine
```

Điểm quan trọng không phải “dùng recursion”. Một function recursive chưa chắc là divide-and-conquer, và một algorithm divide-and-conquer có thể được implement iterative. Bản chất nằm ở **decomposition**: problem được tách thành các phần nhỏ hơn sao cho mỗi phần có thể giải tương đối độc lập và phần combine không phá lợi ích của việc chia nhỏ.

## 1. Ba câu hỏi trước khi dùng Divide and Conquer

Khi nhìn một problem, hãy hỏi:

```text
Có thể chia input/state thành những phần nhỏ hơn cùng loại không?
Các phần có overlap/recompute nhiều không?
Combine result có rẻ hơn giải trực tiếp toàn problem không?
```

Nếu subproblems overlap mạnh, Dynamic Programming thường tự nhiên hơn. Nếu combine step đắt gần bằng brute force, việc chia không giúp nhiều. Nếu decomposition rất mất cân bằng, recursion depth có thể xấu.

## 2. Recurrence là ngôn ngữ tự nhiên của decomposition

Nếu mỗi problem size `n` tạo `a` subproblems size khoảng `n/b`, và phần work ngoài recursion là `f(n)`:

\[
T(n)=aT(n/b)+f(n)
\]

Merge Sort:

\[
T(n)=2T(n/2)+\Theta(n)
\]

Binary Search:

\[
T(n)=T(n/2)+\Theta(1)
\]

Karatsuba:

\[
T(n)=3T(n/2)+\Theta(n)
\]

Recurrence ghi lại chính **shape của computation tree**.

## 3. Recursion Tree: xem work nằm ở đâu

Với Merge Sort, mỗi level có tổng input size `n`, nên combine work mỗi level là `Θ(n)`. Có `Θ(log n)` levels:

\[
T(n)=\Theta(n\log n)
\]

Với:

\[
T(n)=2T(n/2)+\Theta(1)
\]

internal work mỗi node constant, nhưng số leaves là `Θ(n)`, nên total `Θ(n)`.

Đừng nhìn thấy `2T(n/2)` rồi tự động kết luận `n log n`; hãy hỏi **work phân bố theo level thế nào**.

## 4. Master Theorem: shortcut có điều kiện

Với recurrence chuẩn:

\[
T(n)=aT(n/b)+f(n)
\]

so sánh `f(n)` với:

\[
n^{\log_b a}
\]

Term này đại diện quy mô work của recursion tree nếu internal combine nhỏ.

Master theorem rất tiện nhưng không áp dụng cho mọi recurrence. Ví dụ:

\[
T(n)=T(n/3)+T(2n/3)+\Theta(n)
\]

không đúng dạng equal-size subproblems. Recursion tree/Akra–Bazzi reasoning phù hợp hơn.

## 5. Merge Sort: combine step dựa trên precondition mạnh

Hai halves đã sorted, nên merge linear bằng two pointers:

```text
left smallest vs right smallest
chọn nhỏ hơn
advance pointer tương ứng
```

Invariant:

> Prefix output luôn là các phần tử nhỏ nhất đã được quyết định đúng thứ tự từ hai halves.

Nếu halves chưa sorted, combine `O(n)` này không tồn tại. Divide-and-conquer hiệu quả vì recursive work đã tạo ra **structure thuận lợi cho combine**.

## 6. Binary Search: Divide and Conquer một nhánh

Binary Search chia interval nhưng chỉ tiếp tục một half.

Precondition là monotonic/sorted information đủ mạnh để chứng minh half còn lại không thể chứa answer.

Mỗi bước giảm search space theo tỷ lệ:

\[
T(n)=T(n/2)+O(1)=O(\log n)
\]

Không phải cứ lấy midpoint là binary search; phần cốt lõi là proof loại được nửa candidates.

## 7. Quicksort: chất lượng divide quyết định runtime

Partition quanh pivot tạo hai subarrays. Nếu gần cân bằng:

\[
T(n)=2T(n/2)+O(n)=O(n\log n)
\]

Nếu liên tục lệch `0` và `n-1`:

\[
T(n)=T(n-1)+O(n)=O(n^2)
\]

Đây là ví dụ rõ rằng cùng framework Divide and Conquer nhưng **partition quality** thay đổi toàn bộ recursion tree.

Randomized pivot giúp expected behavior tốt hơn, nhưng worst-case vẫn khác expected-case.

## 8. Quickselect: objective quyết định số subproblems cần giải

Selection chỉ cần rank `k`, nên sau partition chỉ recurse vào side chứa `k`.

Expected recurrence gần:

\[
T(n)=T(n/2)+O(n)=O(n)
\]

Sorting toàn bộ sẽ tạo nhiều order information hơn output yêu cầu.

Lesson:

> Decomposition không có nghĩa phải solve tất cả branches. Solve đúng những subproblems mà objective thật sự cần.

## 9. Closest Pair: combine được cứu bởi geometry

Naive all-pairs `O(n²)`. Divide points theo x, solve hai halves, lấy best distance `d`.

Cross-boundary candidates chỉ cần xét trong strip width `2d`. Nếu points strip sorted theo y, packing argument cho thấy mỗi point chỉ cần so với số constant candidates tiếp theo.

Combine giữ `O(n)` mỗi level, total `O(n log n)`.

Đây là pattern quan trọng: **domain-specific theorem làm combine rẻ**.

## 10. Karatsuba: giảm branching factor bằng đại số

Naive multiplication hai số split high/low cần 4 multiplications recursive. Karatsuba biến đổi để chỉ cần 3:

\[
T(n)=3T(n/2)+O(n)
\]

nên:

\[
T(n)=O(n^{\log_2 3})\approx O(n^{1.585})
\]

Optimization ở đây không giảm input size nhiều hơn; nó giảm số branches `a`.

## 11. Fast Exponentiation

Tính `a^n` bằng n multiplications là `O(n)`. Nhưng:

\[
a^n=(a^{n/2})^2
\]

với n chẵn, và thêm một factor `a` nếu n lẻ.

Mỗi bước halve exponent:

\[
O(\log n)
\]

Pattern này xuất hiện trong modular exponentiation, matrix exponentiation và binary lifting.

## 12. Matrix Multiplication và block decomposition

Naive matrix multiplication `O(n³)`. Divide matrix thành quadrants giúp cache locality và mở đường cho algorithms giảm số recursive multiplications như Strassen.

Strassen giảm 8 recursive products xuống 7:

\[
T(n)=7T(n/2)+O(n^2)
\]

nên exponent nhỏ hơn 3.

Nhưng constants, numeric stability và memory behavior quyết định khi nào nó thực dụng.

## 13. Divide and Conquer vs Dynamic Programming

Fibonacci recursion chia thành `F(n-1)` và `F(n-2)` nhưng subproblem overlap rất mạnh. Pure divide-and-conquer recompute cùng states nhiều lần.

DP thêm memoization/tabulation để reuse:

```text
Divide-and-conquer: branches mostly independent
Dynamic Programming: many branches converge to same state
```

Question hữu ích:

> Hai histories khác nhau có dẫn tới cùng exact future state không?

Nếu có nhiều convergence, nghĩ tới DP.

## 14. Divide and Conquer vs Backtracking

Backtracking cũng tạo recursion tree, nhưng mục tiêu khác. Divide-and-conquer chia problem thành subproblems cần giải/ghép. Backtracking enumerate choices trong search space và prune invalid/unpromising branches.

Quicksort recursion không phải “thử choices”; N-Queens không phải “combine independent halves”.

Nhìn cùng hình cây recursion không có nghĩa cùng paradigm.

## 15. Unbalanced Recurrences

Một recurrence:

\[
T(n)=T(n/10)+T(9n/10)+O(n)
\]

vẫn có thể `O(n log n)` dù split không 50/50, vì depth vẫn logarithmic theo constant ratio và total level work linear theo reasoning phù hợp.

Nhưng:

\[
T(n)=T(1)+T(n-1)+O(n)
\]

có depth linear và total quadratic.

Balance không cần hoàn hảo; quan trọng là **mỗi branch giảm theo tỷ lệ đủ mạnh hay không**.

## 16. Base-case threshold và hybrid algorithms

Recursive calls có overhead. Với subarray rất nhỏ, insertion sort có thể nhanh hơn quick/merge sort.

Production sort thường:

```text
large partitions -> divide-and-conquer
small partitions -> insertion-like strategy
pathological depth -> fallback heapsort/introsort
```

Hybrid algorithm giữ asymptotic guarantee nhưng tối ưu constants theo regime.

## 17. Tail-recursion elimination cho Quicksort stack depth

Nếu always recurse vào smaller partition trước và xử lý larger partition bằng loop, call stack depth có thể giữ `O(log n)` ngay cả khi partitions không đẹp theo một phía.

Pattern:

```text
partition
recurse smaller side
loop on larger side
```

Ta đang dùng explicit control-flow transformation để giảm stack usage mà không đổi logical partitioning.

## 18. Parallel Divide and Conquer

Nếu subproblems độc lập, có thể fork tasks song song.

Merge Sort:

```text
sort left  || sort right
then merge
```

Nhưng parallel speedup bị giới hạn bởi:

```text
task creation overhead
synchronization
memory bandwidth
combine bottleneck
load imbalance
```

Amdahl's Law nhắc rằng phần serial còn lại giới hạn speedup tổng thể.

## 19. Grain Size trong parallel recursion

Nếu spawn task tới từng subproblem rất nhỏ, scheduler overhead có thể lớn hơn actual work.

Production fork-join thường có threshold:

```text
if size <= threshold:
    solve sequentially
else:
    split and parallelize
```

Threshold là engineering parameter cần benchmark.

## 20. Work và Span

Trong parallel algorithm analysis:

- **Work** = tổng operations nếu chạy sequential;
- **Span / critical path** = longest dependency chain.

Potential parallelism xấp xỉ:

\[
Work/Span
\]

Divide-and-conquer tự nhiên cho model này vì recursion tree thể hiện dependency structure rõ ràng.

## 21. Cache-oblivious algorithms

Recursive decomposition thường xử lý smaller contiguous regions. Khi region đủ nhỏ để fit cache, locality tự cải thiện dù algorithm không biết cache size cụ thể.

Cache-oblivious matrix algorithms, recursive transpose/layout và divide-based searching tận dụng property này.

Đây là bridge giữa asymptotic decomposition và memory hierarchy.

## 22. In-place Divide and Conquer vs extra buffer

Merge Sort array thường cần buffer `O(n)`. Quicksort có thể partition in-place với auxiliary memory chủ yếu recursion stack.

Nhưng in-place không luôn nhanh hơn: buffer copy có thể sequential/cache-friendly hơn complex swapping.

Space complexity và memory bandwidth phải được xét cùng nhau.

## 23. Stable Partition khó hơn unstable partition

Quicksort-style in-place partition thường không stable. Nếu output contract yêu cầu stability, combine/partition strategy phức tạp hơn hoặc cần extra memory.

Một requirement như “giữ order của equal keys” có thể thay đổi implementation landscape dù asymptotic time tương tự.

## 24. CDQ Divide and Conquer

Trong offline problems, recursion có thể chia theo một dimension/time order, còn Fenwick/segment structure xử lý dimension khác.

CDQ thường xuất hiện trong dominance counting hoặc offline queries. Mental model:

```text
recursion cố định order ở dimension A
combine đếm cross-half contributions bằng data structure trên dimension B
```

Divide-and-conquer ở đây không còn là “split array rồi merge sort” đơn giản, mà là framework để xử lý cross interactions có cấu trúc.

## 25. Divide-and-Conquer DP Optimization

Recurrence dạng:

\[
dp[k][i]=\min_{j<i}(dp[k-1][j]+C(j,i))
\]

naive có thể `O(KN²)`.

Nếu optimal split indices có monotonicity:

\[
opt[i]\le opt[i+1]
\]

ta có thể compute midpoint `i`, tìm best `j` trong narrowed interval, rồi recurse trái/phải với candidate bounds tương ứng.

Kỹ thuật này dùng divide-and-conquer để giảm **search range của transition**, không phải để split original problem thành independent halves.

## 26. Parallel prefix và scan connection

Một số prefix operations có thể được xây bằng upsweep/downsweep tree, nhìn như divide-and-conquer reduction rồi distribute results.

Associativity của operation cho phép combine partial aggregates. Đây là connection giữa algebraic property và parallel decomposition.

## 27. Tree contraction và recursive separators

Graph/tree algorithms nâng cao đôi khi dùng separators: loại một small separator chia problem thành regions nhỏ hơn, solve regions rồi combine.

Centroid decomposition trên tree là ví dụ: chọn centroid chia tree thành components không lớn hơn n/2, recurse từng component. Depth `O(log n)` nhờ size giảm theo tỷ lệ.

Đây là Divide and Conquer trên topology thay vì array interval.

## 28. Geometry và spatial partitioning

KD-tree construction, quadtree/octree và BSP cũng mang tinh thần divide-and-conquer: chia không gian thành regions, recurse theo region.

Hiệu quả phụ thuộc partition balance và query geometry. Một “midpoint” tốt trong coordinate space không nhất thiết tạo equal number of points.

## 29. Failure mode: combine quá đắt

Nếu có 2 halves nhưng combine `O(n²)` mỗi level:

\[
T(n)=2T(n/2)+O(n^2)=O(n^2)
\]

Divide không tự cứu complexity. Đôi khi combine term dominate hoàn toàn.

Khi thiết kế, hãy tính combine ngay từ đầu thay vì chỉ vui vì “đã chia problem làm đôi”.

## 30. Failure mode: hidden overlap

Hai subproblems nhìn khác input index nhưng thực chất tính lại cùng state nội bộ. Nếu overlap lớn, recursion tree phình exponential.

Memoization có thể biến tree thành DAG computation.

Đây là lý do phân biệt **subproblem identity** chứ không chỉ argument syntax.

## 31. Failure mode: bad partition adversarially

Quicksort pivot đầu tiên trên already-sorted array có thể tạo worst-case nếu không có randomization/hybrid fallback.

Production algorithm phải xét adversarial input nếu API public. Randomization, median sampling hoặc introspective fallback giúp kiểm soát tail.

## 32. Testing Divide and Conquer

Các test nên nhắm vào boundaries nơi recursion chia:

```text
n = 0,1,2
odd/even lengths
power-of-two và không power-of-two
all equal
already sorted/reverse
extreme imbalance
large duplicate groups
```

Differential testing với brute force/reference algorithm trên small input rất hiệu quả cho closest pair, selection hoặc recursive transforms.

## 33. Correctness proof pattern

Một proof điển hình dùng strong induction theo input size:

1. base case đúng;
2. assume algorithm đúng cho mọi size nhỏ hơn `n`;
3. prove divide tạo valid subproblems nhỏ hơn;
4. recursive results đúng theo induction hypothesis;
5. prove combine biến correct subresults thành correct whole result.

Phần khó nhất thường là step 5 — combine invariant/theorem.

## 34. Production checklist

Khi dùng Divide and Conquer, hãy hỏi:

```text
split có balanced đủ không?
subproblems có overlap không?
combine cost bao nhiêu?
recursion depth bao nhiêu?
input mutation có cho phép không?
stability có cần không?
parallelization có đủ coarse-grained không?
cache locality tốt hay xấu?
pathological input có fallback không?
```

## Mental Model

> Divide and Conquer biến một global problem thành một **recursion tree of smaller obligations**. Performance được quyết định bởi ba thứ: branching factor, tốc độ giảm size và combine cost.

Nếu subproblems độc lập, decomposition mở đường cho recursion, parallelism và cache locality. Nếu overlap mạnh, nghĩ DP. Nếu combine hoặc partition xấu, framework không tự mang lại speedup.

Xem thêm: [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Selection/Top-K](./06_selection_and_top_k.md).