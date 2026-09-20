# Divide and Conquer
**Chia để trị / Divide and Conquer / 분할 정복**

Divide and Conquer là một chiến lược thiết kế thuật toán trong đó ta chia một problem lớn thành các subproblems nhỏ hơn có cấu trúc tương tự, giải chúng độc lập hoặc gần độc lập, rồi kết hợp kết quả. Ba bước thường được mô tả là:

```text
Divide → Conquer → Combine
```

Điểm quan trọng không phải là “dùng recursion”, mà là **cấu trúc decomposition**. Một hàm recursive chưa chắc là divide-and-conquer, và divide-and-conquer cũng có thể được implement iterative trong một số trường hợp.

## 1. Khi nào một bài toán có cấu trúc divide-and-conquer?

Một bài phù hợp khi problem size có thể được giảm theo một quy luật rõ ràng và các phần nhỏ có thể giải tương đối độc lập. Nếu sau khi chia, mỗi subproblem cần biết rất nhiều state từ subproblem khác, decomposition không còn hữu ích.

Merge Sort là ví dụ kinh điển: sort n phần tử bằng cách sort hai nửa rồi merge hai sorted halves. Binary Search chia search interval làm đôi nhưng chỉ tiếp tục một nửa. Closest Pair trong computational geometry chia theo tọa độ rồi giải hai bên, sau đó xử lý các candidate cross-boundary bằng một combine step có cấu trúc.

## 2. Recurrence là ngôn ngữ phân tích tự nhiên

Nếu một problem được chia thành `a` subproblems, mỗi subproblem kích thước khoảng `n/b`, và phần work ngoài recursion là `f(n)`, runtime thường có dạng:

\[
T(n)=aT(n/b)+f(n)
\]

Merge Sort:

\[
T(n)=2T(n/2)+O(n)
\]

vì có hai halves và merge tuyến tính. Kết quả:

\[
T(n)=O(n\log n)
\]

Binary Search:

\[
T(n)=T(n/2)+O(1)=O(\log n)
\]

Điểm cần nhớ là việc “chia đôi” tự nó không quyết định complexity. Số subproblems và combine cost mới quyết định tổng work.

## 3. Recursion tree cho ta intuition về total work

Với Merge Sort, level 0 có tổng work merge `n`. Level 1 có hai subproblems, nhưng tổng kích thước vẫn `n`, nên tổng combine work level đó vẫn `O(n)`. Có khoảng `log n` levels, nên total là `O(n log n)`.

Ngược lại, recurrence:

\[
T(n)=2T(n/2)+O(1)
\]

có rất ít work ở mỗi internal node nhưng số nodes tăng theo level. Cuối cùng leaves chiếm `Theta(n)` nên total là `Theta(n)`.

Recursion tree rất hữu ích để tránh việc nhìn thấy `2T(n/2)` rồi tự động kết luận `n log n`.

## 4. Master Theorem như một shortcut phân tích

Với recurrence chuẩn:

\[
T(n)=aT(n/b)+f(n)
\]

Master Theorem so sánh `f(n)` với:

\[
n^{\log_b a}
\]

Đại lượng `n^{log_b a}` đại diện roughly cho total work của leaves nếu mỗi node chỉ trả constant combine cost.

Nếu `f(n)` nhỏ hơn đáng kể so với term này, recursive leaves dominate. Nếu cùng order, mỗi level thường đóng góp tương đương và xuất hiện thêm factor `log n`. Nếu `f(n)` lớn hơn đủ rõ và regularity conditions thỏa, combine work gần root dominate.

Master Theorem không áp dụng cho mọi recurrence. Ví dụ subproblem sizes không đều như `T(n)=T(n/3)+T(2n/3)+O(n)` cần cách phân tích khác hoặc recursion tree/Akra–Bazzi style reasoning.

## 5. Merge Sort: combine step quyết định tính chất thuật toán

Merge Sort chia array thành hai halves, recursively sort mỗi half, rồi merge bằng hai pointers.

Điểm mạnh là merge step có thể thực hiện tuyến tính vì hai inputs đã sorted. Invariant trong merge là phần output đã xây luôn chứa những phần tử nhỏ nhất đã được quyết định đúng thứ tự.

Merge Sort có worst-case `O(n log n)` và có thể stable nếu tie-handling đúng. Đổi lại, implementation array thông thường cần auxiliary memory `O(n)`.

Điểm sâu hơn là preprocessing recursive đã tạo ra **structure** để combine dễ hơn. Nếu hai halves chưa sorted, merge tuyến tính không tồn tại.

## 6. Binary Search là divide-and-conquer một nhánh

Binary Search cũng chia problem space nhưng chỉ giữ một subproblem. Điều kiện cốt lõi là có monotonic/ordered property cho phép loại nửa còn lại một cách an toàn.

Mỗi bước giảm search interval gần một nửa, nên depth khoảng `log_2 n`.

Không phải cứ “chia đôi array” là binary search. Phải có proof rằng một nửa chắc chắn không chứa answer.

## 7. Quicksort: decomposition phụ thuộc pivot

Quicksort partition array quanh pivot rồi recursively sort hai partitions. Nếu partition cân bằng, recurrence gần:

\[
T(n)=2T(n/2)+O(n)=O(n\log n)
\]

Nhưng nếu pivot liên tục tạo một bên size `n-1`, một bên size `0`:

\[
T(n)=T(n-1)+O(n)=O(n^2)
\]

Vì vậy Quicksort cho thấy divide-and-conquer performance không chỉ phụ thuộc framework mà còn phụ thuộc chất lượng partition.

Randomized pivot hoặc median-of-three giảm xác suất pattern xấu trong thực tế, nhưng expected complexity và worst-case complexity vẫn là hai khái niệm riêng.

## 8. Quickselect: chỉ recurse vào phần cần thiết

Nếu mục tiêu là tìm phần tử nhỏ thứ `k`, sort toàn bộ là làm nhiều work hơn cần thiết.

Quickselect partition như Quicksort nhưng chỉ recurse vào side chứa rank `k`. Expected recurrence gần:

\[
T(n)=T(n/2)+O(n)=O(n)
\]

với pivot “đủ tốt” trung bình.

Worst-case vẫn `O(n^2)` nếu partition liên tục xấu. Deterministic linear-time selection tồn tại bằng Median of Medians, nhưng constants và implementation phức tạp hơn.

Insight ở đây là: **actual objective quyết định số subproblems cần giải**. Không phải vì ta biết cách chia thành hai phần mà luôn phải xử lý cả hai.

## 9. Closest Pair: combine step dùng geometric bound

Bài Closest Pair of Points naive là `O(n^2)`. Divide-and-conquer sort points theo x, chia thành hai halves, recursively tìm minimum distance `d` ở hai bên.

Vấn đề còn lại là một closest pair có thể nằm ở hai phía khác nhau. Nhưng chỉ những điểm trong strip rộng khoảng `2d` quanh đường chia mới có khả năng tạo pair tốt hơn.

Nếu strip được xét theo y-order, geometry cho thấy mỗi point chỉ cần so với một số constant điểm kế tiếp. Vì vậy combine step có thể giữ `O(n)` mỗi level, cho total `O(n log n)`.

Điểm đáng học không phải con số constant cụ thể, mà là pattern: một proof domain-specific có thể giảm cross-boundary candidates từ quadratic xuống linear.

## 10. Karatsuba: giảm số subproblems bằng algebra

Nhân hai số lớn nếu split thành high/low halves theo cách naive cần bốn phép nhân recursive. Karatsuba dùng biến đổi đại số để chỉ cần ba.

Nếu mỗi multiplication size `n/2`, recurrence trở thành:

\[
T(n)=3T(n/2)+O(n)
\]

nên:

\[
T(n)=O(n^{\log_2 3})\approx O(n^{1.585})
\]

Đây là một insight rất quan trọng: optimization có thể đến từ **giảm branching factor `a`**, không chỉ giảm subproblem size `n/b`.

## 11. Fast exponentiation: giảm problem bằng half exponent

Tính `a^n` bằng nhân `a` n lần là `O(n)`. Nhưng:

\[
a^n = (a^{n/2})^2
\]

với n chẵn, và:

\[
a^n = a(a^{\lfloor n/2\rfloor})^2
\]

với n lẻ.

Mỗi bước giảm exponent gần một nửa, nên `O(log n)` multiplications.

Pattern này xuất hiện trong matrix exponentiation, modular exponentiation và binary lifting-like reasoning.

## 12. Divide-and-conquer và Dynamic Programming khác nhau ở overlap

Hai paradigm đều chia bài thành subproblems, nhưng quan hệ giữa các subproblems khác nhau.

Divide-and-conquer hiệu quả khi subproblems tương đối độc lập. Nếu nhiều branches liên tục giải lại cùng state, pure recursion lặp work. Khi đó memoization hoặc bottom-up DP lưu kết quả để reuse.

Fibonacci naive recursion chia thành `F(n-1)` và `F(n-2)`, nhưng hai cây subproblem overlap rất mạnh; gọi nó divide-and-conquer theo hình thức recursion không giúp complexity. DP mới giải quyết repeated states.

Một câu hỏi thực dụng là: “các nhánh có thể đi đến cùng exact state không?”. Nếu có nhiều overlap, hãy nghĩ DP/memoization.

## 13. Divide-and-conquer optimization trong DP

Tên “divide and conquer” còn xuất hiện trong một kỹ thuật tối ưu DP khi vị trí optimal transition có monotonic property.

Ví dụ một recurrence dạng:

\[
dp[k][i] = \min_{j < i} (dp[k-1][j] + C(j,i))
\]

naive có thể `O(KN^2)`. Nếu optimal split points `opt[k][i]` monotonic theo `i`, ta có thể compute một row bằng recursive divide-and-conquer và thu hẹp candidate interval.

Đây là chủ đề advanced hơn và không phải cùng pattern với Merge Sort theo nghĩa đơn giản, nhưng cùng ý tưởng dùng midpoint để giảm search range.

## 14. Offline divide-and-conquer

Một số bài query/update có thể reorder hoặc xử lý offline. Ta chia time/query range, giải contribution từ hai phía hoặc dùng CDQ divide-and-conquer để xử lý dominance/counting problems.

Trong CDQ, order của một dimension được fixed bởi recursion, còn data structure như Fenwick Tree xử lý dimension khác. Đây là ví dụ cho thấy divide-and-conquer không chỉ dành cho array sorting.

## 15. Parallelism tự nhiên

Nếu subproblems độc lập, chúng có thể chạy song song theo fork-join model. Merge Sort có thể sort hai halves đồng thời; image processing hoặc spatial decomposition cũng thường có cấu trúc tương tự.

Tuy nhiên speedup không tự động bằng số cores. Combine step, synchronization, memory bandwidth và task overhead có thể trở thành bottleneck.

Theo Amdahl's Law, phần không parallelizable vẫn giới hạn speedup tổng thể. Vì vậy decomposition tốt cho theory chưa chắc cho parallel runtime tốt nếu subproblems quá nhỏ hoặc combine quá đắt.

## 16. Cache-oblivious intuition

Một số divide-and-conquer algorithms có locality tốt vì chúng recursively làm việc trên smaller regions cho tới khi chúng vừa cache, dù algorithm không biết explicit cache size.

Cache-oblivious matrix algorithms và recursive layouts khai thác property này. Đây là connection giữa algorithmic decomposition và hardware hierarchy.

## 17. Stack depth và implementation concerns

Recursion depth `O(log n)` thường an toàn hơn depth `O(n)`, nhưng language/runtime vẫn quan trọng.

Quicksort với bad partitions có thể tạo recursion depth `O(n)` và gây stack overflow. Một implementation production có thể recurse vào smaller partition trước rồi dùng loop cho larger partition để giới hạn stack depth gần `O(log n)`.

Java và JavaScript thường có recursion stack limit đáng chú ý. C có thể overflow native stack nếu recursion quá sâu. Algorithmic complexity và call-stack engineering phải được xét cùng nhau.

## 18. Base case và threshold optimization

Recursive divide-and-conquer có overhead function calls và bookkeeping. Với subarray rất nhỏ, insertion sort có thể nhanh hơn Merge Sort/Quicksort recursive.

Nhiều production sort implementations dùng hybrid strategy: divide-and-conquer ở scale lớn, specialized small-array algorithm ở scale nhỏ.

Điều này không thay đổi asymptotic complexity nhưng cải thiện constants.

## 19. Khi divide-and-conquer không phù hợp

Nếu subproblems overlap mạnh, DP tốt hơn. Nếu combine step `O(n^2)` ở mỗi level, chia nhỏ có thể không cứu được total complexity. Nếu decomposition tạo partitions rất mất cân bằng, depth tăng mạnh.

Nếu bài có một global constraint không decomposable, mỗi subproblem có thể cần quá nhiều context từ bên ngoài. Khi đó một graph/state-space model khác có thể phù hợp hơn.

Quan trọng nhất là không chọn paradigm từ syntax recursion. Hãy viết recurrence hoặc mô tả work per level để xem decomposition thật sự giúp gì.

## 20. Một checklist reasoning

Khi cân nhắc divide-and-conquer, hãy tự hỏi:

Subproblem có cùng dạng với original problem không? Chúng có độc lập đủ không? Mỗi lần size giảm bao nhiêu? Có bao nhiêu subproblems? Combine cost là gì? Cross-boundary interactions có thể xử lý rẻ hơn brute force không? Partition có thể mất cân bằng không? Có repeated states khiến DP phù hợp hơn không?

Nếu trả lời được các câu này, recurrence gần như tự xuất hiện.

## Mental Model

> Divide-and-conquer không phải “chia nhỏ để dễ code”, mà là **thiết kế decomposition sao cho tổng work qua các levels có thể kiểm soát**.

Một improvement có thể đến từ giảm số subproblems, giảm size nhanh hơn, làm combine rẻ hơn, hoặc chứng minh cross-boundary candidates rất ít. Recurrence là bản tóm tắt định lượng của những lựa chọn đó.

Xem thêm: [Recursion & Backtracking](./02_recursion_and_backtracking.md), [Dynamic Programming](./05_dynamic_programming.md), [Complexity Analysis](../00_foundations/02_complexity_analysis.md).