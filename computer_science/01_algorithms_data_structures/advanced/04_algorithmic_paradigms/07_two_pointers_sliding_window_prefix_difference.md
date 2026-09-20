# Two Pointers, Sliding Window, Prefix Sum và Difference Techniques
**Two Pointers, Sliding Window, Prefix Sum & Difference / 투 포인터, 슬라이딩 윈도우, 누적합, 차분**

Nhóm kỹ thuật này nhìn bề ngoài gồm nhiều “pattern” khác nhau, nhưng có cùng một nguyên lý sâu: **hai trạng thái lân cận thường giống nhau rất nhiều, vì vậy đừng tính lại từ đầu**.

Two Pointers tận dụng order/monotonicity để loại cả một vùng candidates. Sliding Window reuse trạng thái của window cũ khi biên dịch chuyển. Prefix Sum precompute cumulative state để range query thành subtraction. Difference Array lưu thay đổi ở boundaries thay vì cập nhật từng phần tử.

Đây không phải bốn mẹo độc lập; chúng là bốn cách khác nhau để **reuse structure giữa các trạng thái liên tiếp**.

## 1. Two Pointers trên sorted array

Giả sử array đã sort tăng dần và cần tìm hai phần tử có tổng bằng `target`.

Đặt `L=0`, `R=n-1`.

Nếu:

\[
a[L]+a[R] < target
\]

thì tăng `L` là safe. Vì với `a[L]` hiện tại, thay `a[R]` bằng bất kỳ phần tử nhỏ hơn nào chỉ làm tổng nhỏ hơn nữa. Không có pair dùng `a[L]` với index `<=R` có thể đạt target.

Nếu tổng quá lớn, giảm `R` theo reasoning đối xứng.

Mỗi pointer chỉ di chuyển một chiều, nên total `O(n)` sau khi data đã sorted.

Điểm cốt lõi là proof từ sorted invariant, không phải việc có đúng “hai biến index”.

## 2. Sorting cost có phải được tính không?

Nếu input chưa sorted và ta sort chỉ để dùng two pointers, total complexity là:

\[
O(n\log n)+O(n)=O(n\log n)
\]

Nếu problem yêu cầu original indices, sorting còn phải giữ index metadata.

Trong Two Sum unsorted one-shot, hash map `O(n)` expected có thể phù hợp hơn. Nhưng nếu có nhiều queries trên same array, sort một lần rồi two-pointers/binary-search có thể đáng giá.

Luôn phân tích toàn pipeline, không chỉ scan phase.

## 3. Opposite-direction và same-direction pointers

“Two pointers” không chỉ là một pointer trái và một pointer phải.

**Opposite direction**: `L` từ đầu, `R` từ cuối; phổ biến ở sorted pair sum, palindrome, container/range problems.

**Same direction**: cả hai đi từ trái sang phải nhưng đại diện boundaries khác nhau; sliding window là một dạng.

**Read/write pointers**: một pointer đọc input, một pointer viết compacted output in-place.

**Fast/slow pointers**: hai pointers đi tốc độ khác nhau trên linked structure.

Điểm chung là pointers encode một invariant giúp mỗi vị trí không bị xử lý lặp vô ích.

## 4. Read/Write Pointers cho in-place compaction

Ví dụ remove duplicates khỏi sorted array:

```java
int write = 0;
for (int read = 0; read < a.length; read++) {
    if (read == 0 || a[read] != a[read - 1]) {
        a[write++] = a[read];
    }
}
```

Invariant: prefix `[0, write)` luôn chứa output hợp lệ đã compact; `read` đang khám phá input chưa xử lý.

Pattern này xuất hiện trong remove-element, filter-in-place, partition và stream compaction.

## 5. Fast/Slow Pointers trên linked list

Floyd cycle detection đặt `slow` đi 1 step, `fast` đi 2 steps. Nếu list có cycle, hai pointers cuối cùng gặp nhau trong cycle.

Nếu không cycle, `fast` chạm null.

Midpoint cũng dùng slow/fast: khi fast đi hết list, slow ở gần giữa.

Điểm quan trọng là linked list không có random access, nên pointer-speed relation thay thế arithmetic index.

## 6. Fixed-size Sliding Window

Giả sử cần maximum sum của subarray length `k`.

Naive tính sum cho mỗi window `O(k)`, tổng `O(nk)`.

Nếu current window sum là `S`, khi dịch một bước:

\[
S' = S - a[L] + a[R+1]
\]

Ta chỉ bỏ một phần tử và thêm một phần tử. Sau initial `O(k)`, mỗi shift `O(1)`, total `O(n)`.

Đây là state reuse ở dạng rõ nhất.

## 7. Variable Sliding Window cần monotonic property

Giả sử array chỉ có số dương và cần longest subarray có sum `<= K`.

Khi tăng `R`, sum không giảm. Nếu sum vượt K, tăng `L` sẽ làm sum giảm hoặc giữ. Vì vậy ta có thể shrink cho đến khi invariant được khôi phục.

Pseudo:

```text
for R:
    add a[R]
    while window invalid:
        remove a[L]
        L++
    update answer
```

Mỗi element vào window một lần và ra một lần, nên total `O(n)`.

## 8. Tại sao số âm phá sliding-window sum đơn giản?

Nếu array có negative numbers, tăng `R` có thể làm sum giảm; tăng `L` có thể làm sum tăng nếu phần tử bỏ ra âm.

Monotonic relation giữa boundary movement và predicate mất đi. Khi đó “sum quá lớn thì tăng left” không còn guaranteed safe.

Một problem tương tự có thể cần prefix sums + hash map, monotonic deque, balanced tree hoặc different algorithm.

Đây là một lesson quan trọng: sliding window không được xác định bởi syntax hai pointers; nó được xác định bởi **monotonic validity under boundary movement**.

## 9. Window state không chỉ là sum

Window có thể duy trì frequency map, count distinct, number of violations, max/min hoặc other summary.

Ví dụ longest substring without repeated characters giữ frequency/last-position information. Khi thêm character làm duplicate, move left cho tới khi uniqueness invariant phục hồi.

Nếu update add/remove mỗi element `O(1)` expected, total vẫn tuyến tính vì boundaries monotonic.

## 10. Minimum Window Substring

Bài minimum window chứa đủ required character counts có hai phases lặp:

Mở rộng right cho tới khi window valid.

Sau đó shrink left tối đa trong khi vẫn valid, cập nhật minimum.

Một biến như `formed` hoặc number of satisfied requirements tránh scan toàn frequency map mỗi step.

Đây là ví dụ window invariant phức tạp hơn sum nhưng cùng state-transition pattern.

## 11. At Most K → Exactly K transformation

Một kỹ thuật đẹp với counting windows là:

\[
count(exactly\ K)=count(atMost\ K)-count(atMost\ K-1)
\]

Nếu `atMost(K)` có monotonic sliding-window solution, ta có thể derive exactly-K count.

Ví dụ subarrays với exactly K distinct values.

Đây là inclusion-exclusion ở mức simple difference giữa cumulative constraints.

## 12. Prefix Sum

Định nghĩa:

```text
P[0] = 0
P[i+1] = P[i] + a[i]
```

Khi đó sum của half-open range `[L,R)`:

\[
P[R]-P[L]
\]

hoặc inclusive `[L,R]`:

\[
P[R+1]-P[L]
\]

Preprocessing `O(n)`, mỗi range-sum query `O(1)`.

Ta trả upfront memory `O(n)` và build cost để nhiều query rẻ hơn.

## 13. Prefix Sum là representation của cumulative state

Prefix array không chỉ là một trick cộng số. Nó lưu state sau khi xử lý prefix đầu tiên `i` elements.

Range query lấy “state đến R” trừ “state trước L”. Điều này hoạt động vì sum có inverse operation subtraction.

XOR prefix cũng tương tự vì XOR tự đảo:

\[
rangeXor(L,R)=P[R+1]\oplus P[L]
\]

Không phải mọi aggregate đều hỗ trợ subtraction/inverse đơn giản. Min/max prefix không thể lấy range min bằng `prefixMin[R] - prefixMin[L]`.

## 14. Prefix Frequency

Nếu alphabet/value domain nhỏ, prefix không cần là scalar. Ta có thể lưu cumulative frequency vectors.

Ví dụ string lowercase:

```text
pref[i][c] = số lần char c trong prefix length i
```

Frequency của char c trong `[L,R)`:

```text
pref[R][c] - pref[L][c]
```

Memory `O(nσ)` với alphabet size `σ`, đổi lại range histogram query nhanh.

## 15. Prefix Sum + Hash Map cho subarray sum

Nếu cần đếm subarrays có sum `K`, kể cả có số âm:

Subarray `(j,i]` có sum K khi:

\[
P[i]-P[j]=K
\]

hay:

\[
P[j]=P[i]-K
\]

Khi scan prefix `P[i]`, ta chỉ cần biết có bao nhiêu previous prefixes bằng `P[i]-K` trong hash map.

Total expected `O(n)`.

Đây là ví dụ rất quan trọng nơi prefix sum biến subarray problem thành pair relation giữa cumulative states.

## 16. Prefix Minimum/Maximum kết hợp chứ không trừ

Dù min không invertible, prefix min vẫn hữu ích cho problems khác.

Ví dụ maximum subarray sum ending at current prefix có thể reason qua minimum previous prefix:

\[
P[i]-\min_{j<i}P[j]
\]

Ta không hỏi arbitrary range min; ta hỏi best prior boundary. Do đó cumulative summary vẫn hữu ích.

## 17. 2D Prefix Sum

Với matrix, define cumulative rectangle từ `(0,0)` tới trước `(r,c)` theo half-open convention.

Sum rectangle `[r1,r2) × [c1,c2)` dùng inclusion-exclusion:

\[
P[r2][c2]-P[r1][c2]-P[r2][c1]+P[r1][c1]
\]

Subtract hai vùng thừa rồi add lại overlap đã bị subtract hai lần.

Đây là geometric form của inclusion-exclusion.

## 18. Difference Array

Prefix representation lưu cumulative value. Difference representation lưu change giữa neighbors.

Với initial zero array, muốn add `x` vào inclusive range `[L,R]`:

```text
diff[L] += x
diff[R+1] -= x
```

Sau tất cả updates, prefix sum của `diff` reconstruct final values.

Mỗi range update `O(1)`, final materialization `O(n)`.

## 19. Difference Array chỉ phù hợp khi queries có thể deferred

Nếu sau mỗi range update phải query exact current point/range online, simple difference array chưa đủ vì chưa materialize prefix.

Khi operations interleave online, Fenwick Tree hoặc Segment Tree có thể cần thiết.

Difference array mạnh khi updates batch/offline và final output/query đến sau.

Again, workload timing quyết định structure.

## 20. 2D Difference

Rectangle add trên matrix có thể update bốn corners của 2D difference array với inclusion-exclusion signs, rồi prefix accumulate theo hai dimensions để recover final matrix.

Pattern giống 1D nhưng boundaries trở thành rectangle corners.

Đây là technique mạnh cho batch area updates.

## 21. Monotonic Stack và amortized O(n)

Dù tên không phải sliding window, monotonic stack cùng triết lý loại candidates vĩnh viễn.

Next Greater Element: khi current value lớn hơn stack top, top đã tìm được next greater và bị pop. Mỗi index push một lần, pop một lần.

Nested `while` nhìn có vẻ `O(n^2)` nhưng total operations `O(n)` theo amortized analysis.

## 22. Monotonic Deque cho Sliding Window Maximum

Recompute max mỗi window size k là `O(nk)`.

Deque giữ indices với values giảm dần.

Khi thêm `a[r]`, pop tail indices có value `<= a[r]`. Chúng không thể trở thành maximum trong một future window chứa `a[r]` vì `a[r]` vừa mới hơn vừa không nhỏ hơn.

Pop front nếu index đã ra khỏi window.

Front luôn là maximum current window.

Mỗi index enter/leave deque tối đa một lần → `O(n)`.

## 23. Monotonic Queue cho prefix optimization

Một số DP/prefix problems cần minimum/maximum prefix trong moving range. Monotonic deque duy trì optimum candidate khi range boundaries dịch chuyển.

Ví dụ shortest subarray with sum at least K khi có negative numbers có thể dùng prefix sums + monotonic deque, thay vì simple sliding window.

Ta cần tìm previous prefix nhỏ nhất phù hợp và loại dominated prefixes.

Đây là một bước nâng cao nối prefix representation với monotonic candidate structure.

## 24. Two Pointers trên hai arrays

Merge two sorted arrays dùng pointers `i,j`, mỗi step consume phần tử nhỏ hơn. Intersection/union of sorted lists cũng tương tự.

Nếu lengths `n,m`, total `O(n+m)` vì mỗi pointer chỉ tăng.

Search engines intersect sorted postings lists theo mental model này, có thể thêm skip/galloping optimization nếu sizes chênh nhiều.

## 25. Three Sum và sorting reduction

Three Sum có thể sort array rồi fix một index `i`, sau đó two-pointers tìm pair cho target `-a[i]`.

Total:

\[
O(n^2)
\]

after sorting, thay vì naive `O(n^3)`.

Duplicates cần skip cẩn thận để tránh output lặp.

Pattern cho thấy two-pointers thường xuất hiện sau khi một dimension được fixed hoặc data được sorted.

## 26. Partition và Two Pointers

Quicksort partition có thể dùng pointers quét inward/outward; Dutch National Flag dùng boundaries cho `< pivot`, `== pivot`, `> pivot`.

Các pointers không phải chỉ “search pair” mà có thể đại diện boundaries của regions với invariants khác nhau.

Một cách học tốt là annotate mỗi region:

```text
[processed less][processed equal][unknown][processed greater]
```

và chứng minh mỗi pointer move làm unknown region nhỏ lại.

## 27. Circular Window

Với circular array, một cách là index modulo `n` hoặc conceptually duplicate data. Nhưng duplicate thật làm memory `O(n)` thêm; modulo giữ compact hơn.

Cần tránh window length vượt semantics allowed và tránh infinite pointer loops.

## 28. Overflow

Prefix sums có thể vượt `int` ngay cả khi individual values vừa `int`.

Java nên dùng `long` nếu `n * maxValue` có thể vượt 32-bit. C chọn integer width phù hợp. JavaScript `Number` phải nằm trong safe integer range nếu cần exactness.

Prefix structures tích lũy values nên overflow risk lớn hơn nhìn từng element.

## 29. Online vs Offline là câu hỏi quyết định

Prefix Sum và Difference Array mạnh vì cho phép preprocessing hoặc deferred materialization.

Nếu queries/update interleave online, Fenwick/Segment Tree có thể cần. Nếu data static và query nhiều, prefix có thể đơn giản hơn nhiều.

Không nên dùng Segment Tree chỉ vì range query nghe “nâng cao” nếu Prefix Sum `O(1)` query đã đủ.

## 30. Một cách nhận diện kỹ thuật

Nếu brute force tính lại gần như cùng state cho windows/ranges kế tiếp, hãy hỏi phần nào có thể reuse.

Nếu pointers có thể chỉ đi một chiều nhờ sorted/monotonic invariant, two pointers có thể loại repeated search.

Nếu query là aggregate trên static ranges, prefix may fit.

Nếu update là batch range-add, difference representation may fit.

Nếu optimum candidate trong moving range cần được giữ và dominated candidates có thể loại vĩnh viễn, monotonic deque/stack có thể fit.

## Mental Model

> Những kỹ thuật này đều thắng bằng cách xác định **phần nào của trạng thái cũ vẫn còn đúng khi boundary thay đổi**, rồi chỉ cập nhật phần chênh lệch.

Two Pointers reuse ordering để không quay lại candidates đã loại. Sliding Window reuse current window state. Prefix Sum reuse cumulative prefixes. Difference Array defer work vào boundaries. Monotonic structures loại dominated candidates vĩnh viễn.

Nếu bạn hiểu invariant làm cho pointer chỉ đi một chiều hoặc state update chỉ `O(1)`, bạn không cần học thuộc hàng chục “patterns” riêng lẻ.

Xem thêm: [Searching](./00_searching.md), [Intervals & Sweep Line](./08_intervals_and_sweep_line.md), [Range Queries](../05_specialized/01_range_queries_fenwick_segment_tree.md), [Amortized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md).