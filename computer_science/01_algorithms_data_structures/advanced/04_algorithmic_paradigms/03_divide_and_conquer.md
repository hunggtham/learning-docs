# chia để trị
**Chia để trị / chia để trị / 분할 정복**

chia để trị là một chiến lược thiết kế thuật toán trong đó một problem lớn được tách thành các subproblems nhỏ hơn có cấu trúc tương tự, giải các phần đó, rồi ghép kết quả lại. mẫu kinh điển:

```text
Divide → Conquer → Combine
```

Điểm quan trọng không phải “dùng recursion”. Một hàm recursive chưa chắc là divide-and-conquer, và một thuật toán divide-and-conquer có thể được implement iterative. Bản chất nằm ở **decomposition**: problem được tách thành các phần nhỏ hơn sao cho mỗi phần có thể giải tương đối độc lập và phần kết hợp không phá lợi ích của việc chia nhỏ.

## 1. Ba câu hỏi trước khi dùng chia để trị

Khi nhìn một problem, hãy hỏi:

```text
Có thể chia input/state thành những phần nhỏ hơn cùng loại không?
Các phần có overlap/recompute nhiều không?
Combine result có rẻ hơn giải trực tiếp toàn problem không?
```

Nếu subproblems overlap mạnh, quy hoạch động (dynamic programming) thường tự nhiên hơn. Nếu kết hợp step đắt gần bằng brute force, việc chia không giúp nhiều. Nếu decomposition rất mất cân bằng, recursion độ sâu có thể xấu.

## 2. công thức truy hồi là ngôn ngữ tự nhiên của decomposition

Nếu mỗi bài toán kích thước `n` tạo `a` bài toán con kích thước khoảng `n/b`, và phần công việc ngoài đệ quy là `f(n)`:

\[
T(n)=aT(n/b)+f(n)
\]

sắp xếp trộn:

\[
T(n)=2T(n/2)+\Theta(n)
\]

tìm kiếm nhị phân:

\[
T(n)=T(n/2)+\Theta(1)
\]

Karatsuba:

\[
T(n)=3T(n/2)+\Theta(n)
\]

công thức truy hồi ghi lại chính **shape của computation cây**.

## 3. cây đệ quy: xem work nằm ở đâu

Với sắp xếp trộn, mỗi tầng có tổng kích thước đầu vào `n`, nên kết hợp work mỗi tầng là `Θ(n)`. Có `Θ(log n)` các tầng:

\[
T(n)=\Theta(n\log n)
\]

Với:

\[
T(n)=2T(n/2)+\Theta(1)
\]

nội bộ work mỗi nút constant, nhưng số các nút lá là `Θ(n)`, nên total `Θ(n)`.

Đừng nhìn thấy `2T(n/2)` rồi tự động kết luận `n log n`; hãy hỏi **work phân bố theo tầng thế nào**.

## 4. Định lý Master: cách rút gọn có điều kiện

Với công thức truy hồi chuẩn:

\[
T(n)=aT(n/b)+f(n)
\]

so sánh `f(n)` với:

\[
n^{\log_b a}
\]

Term này đại diện quy mô work của cây đệ quy nếu nội bộ kết hợp nhỏ.

Định lý Master rất tiện nhưng không áp dụng cho mọi công thức truy hồi. Ví dụ:

\[
T(n)=T(n/3)+T(2n/3)+\Theta(n)
\]

không đúng dạng equal-size subproblems. cây đệ quy/Akra–Bazzi reasoning phù hợp hơn.

## 5. sắp xếp trộn: kết hợp step dựa trên điều kiện trước mạnh

Hai halves đã sorted, nên merge linear bằng hai con trỏ (two pointers):

```text
left smallest vs right smallest
chọn nhỏ hơn
advance pointer tương ứng
```

bất biến (invariant):

> Prefix đầu ra luôn là các phần tử nhỏ nhất đã được quyết định đúng thứ tự từ hai halves.

Nếu halves chưa sorted, kết hợp `O(n)` này không tồn tại. Divide-and-conquer hiệu quả vì recursive work đã tạo ra **structure thuận lợi cho kết hợp**.

## 6. tìm kiếm nhị phân: chia để trị một nhánh

tìm kiếm nhị phân chia interval nhưng chỉ tiếp tục một half.

điều kiện trước là monotonic/sorted thông tin đủ mạnh để chứng minh half còn lại không thể chứa answer.

Mỗi bước giảm không gian tìm kiếm theo tỷ lệ:

\[
T(n)=T(n/2)+O(1)=O(\log n)
\]

Không phải cứ lấy midpoint là tìm kiếm nhị phân; phần cốt lõi là chứng minh loại được nửa các ứng viên.

## 7. Quicksort: chất lượng divide quyết định môi trường chạy (runtime)

Partition quanh pivot tạo hai subarrays. Nếu gần cân bằng:

\[
T(n)=2T(n/2)+O(n)=O(n\log n)
\]

Nếu liên tục lệch `0` và `n-1`:

\[
T(n)=T(n-1)+O(n)=O(n^2)
\]

Đây là ví dụ rõ rằng cùng khung làm việc chia để trị nhưng **chất lượng phân hoạch** thay đổi toàn bộ cây đệ quy.

ngẫu nhiên hóa pivot giúp kỳ vọng hành vi tốt hơn, nhưng trường hợp xấu nhất vẫn khác kỳ vọng-case.

## 8. Quickselect: objective quyết định số subproblems cần giải

Selection chỉ cần rank `k`, nên sau partition chỉ recurse vào side chứa `k`.

kỳ vọng công thức truy hồi gần:

\[
T(n)=T(n/2)+O(n)=O(n)
\]

Sắp xếp toàn bộ sẽ tạo nhiều thông tin thứ tự hơn mức đầu ra yêu cầu.

Lesson:

> Decomposition không có nghĩa phải solve tất cả branches. Solve đúng những subproblems mà objective thật sự cần.

## 9. Closest Pair: kết hợp được cứu bởi geometry

Cách đơn giản xét mọi cặp có độ phức tạp `O(n²)`. Cách chia để trị chia các điểm theo trục x, giải hai nửa rồi lấy khoảng cách tốt nhất `d`.

Các ứng viên đi qua đường chia chỉ cần xét trong một dải rộng `2d`. Nếu các điểm trong dải được sắp theo y, lập luận đóng gói cho thấy mỗi điểm chỉ cần so với một số hằng ứng viên tiếp theo.

kết hợp giữ `O(n)` mỗi tầng, total `O(n log n)`.

Đây là mẫu quan trọng: **domain-specific theorem làm kết hợp rẻ**.

## 10. Karatsuba: giảm hệ số phân nhánh bằng đại số

Cách đơn giản multiplication hai số split high/low cần 4 multiplications recursive. Karatsuba biến đổi để chỉ cần 3:

\[
T(n)=3T(n/2)+O(n)
\]

nên:

\[
T(n)=O(n^{\log_2 3})\approx O(n^{1.585})
\]

Optimization ở đây không giảm kích thước đầu vào nhiều hơn; nó giảm số branches `a`.

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

mẫu này xuất hiện trong modular exponentiation, matrix exponentiation và nhảy nhị phân.

## 12. Matrix Multiplication và block decomposition

Cách đơn giản matrix multiplication `O(n³)`. Divide matrix thành quadrants giúp tính cục bộ bộ nhớ đệm và mở đường cho các thuật toán giảm số recursive multiplications như Strassen.

Strassen giảm 8 recursive products xuống 7:

\[
T(n)=7T(n/2)+O(n^2)
\]

nên exponent nhỏ hơn 3.

Nhưng constants, numeric tính ổn định và bộ nhớ hành vi quyết định khi nào nó thực dụng.

## 13. chia để trị vs quy hoạch động

Fibonacci recursion chia thành `F(n-1)` và `F(n-2)` nhưng sự chồng lặp bài toán con rất mạnh. Pure divide-and-conquer recompute cùng các trạng thái nhiều lần.

DP thêm memoization/tabulation để reuse:

```text
Divide-and-conquer: branches mostly independent
Dynamic Programming: many branches converge to same state
```

Question hữu ích:

> Hai histories khác nhau có dẫn tới cùng chính xác tương lai trạng thái (state) không?

Nếu có nhiều convergence, nghĩ tới DP.

## 14. chia để trị vs quay lui (backtracking)

Quay lui cũng tạo cây đệ quy nhưng mục tiêu khác. Chia để trị chia bài toán thành các bài toán con cần giải rồi ghép kết quả; quay lui liệt kê các lựa chọn trong không gian tìm kiếm và cắt tỉa những nhánh không hợp lệ hoặc không hứa hẹn.

Quicksort recursion không phải “thử choices”; N-Queens không phải “kết hợp independent halves”.

Nhìn cùng hình cây recursion không có nghĩa cùng paradigm.

## 15. Unbalanced các công thức truy hồi

Một công thức truy hồi:

\[
T(n)=T(n/10)+T(9n/10)+O(n)
\]

vẫn có thể `O(n log n)` dù split không 50/50, vì độ sâu vẫn logarithmic theo constant ratio và total tầng work linear theo reasoning phù hợp.

Nhưng:

\[
T(n)=T(1)+T(n-1)+O(n)
\]

có độ sâu linear và total quadratic.

Balance không cần hoàn hảo; quan trọng là **mỗi branch giảm theo tỷ lệ đủ mạnh hay không**.

## 16. Base-case threshold và hybrid các thuật toán

các lời gọi đệ quy có overhead. Với subarray rất nhỏ, insertion sort có thể nhanh hơn quick/sắp xếp trộn.

Trong hệ thống thực tế, sort thường:

```text
large partitions -> divide-and-conquer
small partitions -> insertion-like strategy
pathological depth -> fallback heapsort/introsort
```

Hybrid thuật toán giữ asymptotic bảo đảm nhưng tối ưu constants theo regime.

## 17. Tail-recursion elimination cho Quicksort stack độ sâu

Nếu always recurse vào phân vùng nhỏ hơn trước và xử lý phân vùng lớn hơn bằng loop, ngăn xếp lời gọi độ sâu có thể giữ `O(log n)` ngay cả khi partitions không đẹp theo một phía.

mẫu:

```text
partition
recurse smaller side
loop on larger side
```

Ta đang dùng explicit control-flow phép biến đổi để giảm stack usage mà không đổi logic partitioning.

## 18. Parallel chia để trị

Nếu subproblems độc lập, có thể fork tasks song song.

sắp xếp trộn:

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

Nếu spawn task tới từng subproblem rất nhỏ, bộ lập lịch overhead có thể lớn hơn actual work.

Trong hệ thống thực tế, fork-join thường có threshold:

```text
if size <= threshold:
    solve sequentially
else:
    split and parallelize
```

Threshold là engineering parameter cần benchmark.

## 20. Work và Span

Trong parallel thuật toán analysis:

- **Work** = tổng các thao tác nếu chạy sequential;
- **Span / critical đường đi** = longest dependency chain.

Potential parallelism xấp xỉ:

\[
Work/Span
\]

Divide-and-conquer tự nhiên cho mô hình này vì cây đệ quy thể hiện dependency structure rõ ràng.

## 21. Cache-oblivious các thuật toán

Recursive decomposition thường xử lý smaller contiguous regions. Khi region đủ nhỏ để fit bộ nhớ đệm, tính cục bộ (locality) tự cải thiện dù thuật toán không biết bộ nhớ đệm size cụ thể.

Cache-oblivious matrix các thuật toán, recursive transpose/bố trí và divide-based searching tận dụng tính chất này.

Đây là bridge giữa asymptotic decomposition và phân cấp bộ nhớ.

## 22. In-place chia để trị vs extra bộ đệm

sắp xếp trộn mảng thường cần bộ đệm `O(n)`. Quicksort có thể partition in-place với bộ nhớ phụ trợ chủ yếu ngăn xếp đệ quy.

Nhưng in-place không luôn nhanh hơn: bộ đệm copy có thể sequential/thân thiện với bộ nhớ đệm hơn phức tạp swapping.

độ phức tạp bộ nhớ và bộ nhớ bandwidth phải được xét cùng nhau.

## 23. ổn định Partition khó hơn unstable partition

Quicksort-style in-place partition thường không ổn định. Nếu hợp đồng đầu ra yêu cầu tính ổn định, kết hợp/partition strategy phức tạp hơn hoặc cần extra bộ nhớ.

Một yêu cầu như “giữ order của equal các khóa” có thể thay đổi cách triển khai landscape dù asymptotic time tương tự.

## 24. CDQ chia để trị

Trong các bài toán ngoại tuyến, đệ quy có thể chia theo một chiều hoặc theo thứ tự thời gian, còn Fenwick Tree hoặc Segment Tree xử lý một chiều khác.

CDQ thường xuất hiện trong dominance counting hoặc ngoại tuyến các truy vấn. Mô hình tư duy:

```text
recursion cố định order ở dimension A
combine đếm cross-half contributions bằng data structure trên dimension B
```

Divide-and-conquer ở đây không còn là “split mảng rồi sắp xếp trộn” đơn giản, mà là khung làm việc để xử lý cross interactions có cấu trúc.

## 25. Divide-and-Conquer DP Optimization

công thức truy hồi dạng:

\[
dp[k][i]=\min_{j<i}(dp[k-1][j]+C(j,i))
\]

naive có thể `O(KN²)`.

Nếu optimal split indices có monotonicity:

\[
opt[i]\le opt[i+1]
\]

ta có thể compute midpoint `i`, tìm best `j` trong narrowed interval, rồi recurse trái/phải với ứng viên bounds tương ứng.

Kỹ thuật này dùng chia để trị để giảm **miền tìm kiếm của bước chuyển**, không phải để tách bài toán gốc thành hai nửa độc lập.

## 26. Parallel prefix và quét connection

Một số prefix các thao tác có thể được xây bằng upsweep/downsweep cây, nhìn như divide-and-conquer reduction rồi distribute các kết quả.

Tính kết hợp của phép toán cho phép ghép các kết quả tổng hợp từng phần. Đây là mối liên hệ giữa tính chất đại số và khả năng phân rã để xử lý song song.

## 27. cây contraction và recursive separators

đồ thị/cây các thuật toán nâng cao đôi khi dùng separators: loại một small separator chia problem thành regions nhỏ hơn, solve regions rồi kết hợp.

Centroid decomposition trên cây là ví dụ: chọn centroid chia cây thành các thành phần không lớn hơn n/2, recurse từng thành phần. độ sâu `O(log n)` nhờ size giảm theo tỷ lệ.

Đây là chia để trị trên topology thay vì mảng interval.

## 28. Geometry và spatial partitioning

Việc xây dựng KD-tree, quadtree/octree và BSP cũng mang tinh thần chia để trị: chia không gian thành các vùng rồi đệ quy theo từng vùng.

Hiệu quả phụ thuộc vào mức cân bằng của phép phân hoạch và hình học của truy vấn. Một “điểm giữa” tốt trong không gian tọa độ không nhất thiết chia các điểm thành hai nhóm có số lượng bằng nhau.

## 29. dạng lỗi: kết hợp quá đắt

Nếu có 2 halves nhưng kết hợp `O(n²)` mỗi tầng:

\[
T(n)=2T(n/2)+O(n^2)=O(n^2)
\]

Divide không tự cứu complexity. Đôi khi kết hợp term dominate hoàn toàn.

Khi thiết kế, hãy tính kết hợp ngay từ đầu thay vì chỉ vui vì “đã chia problem làm đôi”.

## 30. dạng lỗi: hidden overlap

Hai subproblems nhìn khác đầu vào index nhưng thực chất tính lại cùng trạng thái nội bộ. Nếu overlap lớn, cây đệ quy phình exponential.

Memoization có thể biến cây thành DAG computation.

Đây là lý do phân biệt **subproblem identity** chứ không chỉ argument syntax.

## 31. dạng lỗi: bad partition adversarially

Quicksort pivot đầu tiên trên already-mảng đã sắp xếp có thể tạo trường hợp xấu nhất nếu không có randomization/hybrid fallback.

Trong hệ thống thực tế, thuật toán phải xét đối kháng đầu vào nếu API public. Randomization, median sampling hoặc introspective fallback giúp kiểm soát tail.

## 32. kiểm thử chia để trị

Các test nên nhắm vào các ranh giới nơi recursion chia:

```text
n = 0,1,2
odd/even lengths
power-of-two và không power-of-two
all equal
already sorted/reverse
extreme imbalance
large duplicate groups
```

Kiểm thử vi sai (kiểm thử vi sai) với thuật toán vét cạn hoặc thuật toán tham chiếu trên đầu vào nhỏ rất hiệu quả cho closest pair, selection hoặc recursive transforms.

## 33. tính đúng đắn chứng minh mẫu

Một chứng minh điển hình dùng quy nạp mạnh theo kích thước đầu vào:

1. trường hợp cơ sở đúng;
2. assume thuật toán đúng cho mọi size nhỏ hơn `n`;
3. prove divide tạo hợp lệ subproblems nhỏ hơn;
4. recursive các kết quả đúng theo quy nạp hypothesis;
5. prove kết hợp biến correct subresults thành correct whole kết quả.

Phần khó nhất thường là step 5 — kết hợp bất biến/theorem.

## 34. Trong hệ thống thực tế, checklist

Khi dùng chia để trị, hãy hỏi:

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

## Mô hình tư duy

> chia để trị biến một toàn cục problem thành một **cây đệ quy of smaller obligations**. hiệu năng được quyết định bởi ba thứ: hệ số phân nhánh, tốc độ giảm size và kết hợp chi phí.

Nếu subproblems độc lập, decomposition mở đường cho recursion, parallelism và tính cục bộ bộ nhớ đệm. Nếu overlap mạnh, nghĩ DP. Nếu kết hợp hoặc partition xấu, khung làm việc không tự mang lại speedup.

Xem thêm: [Complexity Analysis](../00_foundations/02_complexity_analysis.md), [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Selection/Top-K](./06_selection_and_top_k.md).