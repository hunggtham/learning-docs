# Algorithmic thinking, specification và correctness

Algorithm (thuật toán / 알고리즘) không phải một đoạn code có vẻ chạy được. Nó là một procedure hữu hạn, rõ nghĩa, biến input thành output theo một specification. Tư duy thuật toán bắt đầu trước code: xác định state nào quan trọng, operation nào được phép, invariant nào phải giữ, và bằng chứng nào cho thấy procedure thực sự giải đúng bài toán.

## Từ problem statement tới specification

Một câu như “tìm phần tử lớn nhất” còn thiếu nhiều điều. Input có thể rỗng không? Có duplicate không? Dữ liệu so sánh được bằng ordering nào? Ta trả value hay index? Nếu comparator không transitive thì chuyện gì xảy ra?

Specification (명세 / đặc tả) làm những assumptions này explicit. Với array không rỗng `A[0..n-1]`, specification của `max` có thể là: output `m` thuộc array và với mọi `i`, `m >= A[i]`.

Một implementation đơn giản:

```text
m = A[0]
for i = 1 .. n-1:
    if A[i] > m:
        m = A[i]
return m
```

Điểm đáng học không phải syntax mà là reasoning. Sau khi đã xử lý prefix `A[0..i]`, invariant là `m` bằng maximum của prefix đó. Ban đầu invariant đúng với prefix một phần tử. Mỗi iteration hoặc giữ `m`, hoặc thay bằng phần tử lớn hơn, nên invariant được bảo toàn. Khi loop kết thúc, prefix chính là toàn array; specification được thỏa.

## Partial correctness và termination

Một algorithm có thể “nếu kết thúc thì đúng” nhưng không bảo đảm kết thúc. Partial correctness nói output đúng nếu computation terminates. Total correctness cần cả partial correctness lẫn termination.

Với loop, termination thường chứng minh bằng một **variant** giảm theo well-founded order. Binary search làm interval giảm; Euclidean algorithm làm remainder giảm; recursion cần tiến gần base case.

Trong production, termination còn có nghĩa thực dụng hơn: network call cần timeout; retry cần bound/backoff; queue consumer phải tránh poison message loop. Lý thuyết termination gặp trực tiếp reliability engineering.

## Decomposition và subproblem

Algorithmic thinking thường tìm cách biến problem thành subproblems dễ hơn. Merge sort chia array thành hai halves, sort từng nửa rồi merge. Dynamic programming nhận ra overlapping subproblems và lưu kết quả. Graph search biến câu hỏi “đi tới đâu được?” thành việc lặp lại expand frontier.

Điểm quan trọng là decomposition phải preserve structure. Chia bừa một problem không tự động tạo algorithm tốt. Với divide-and-conquer, ta cần xác định cách combine; với greedy, phải chứng minh local choice không phá global optimum; với DP, cần state đủ để mô tả phần quá khứ ảnh hưởng tương lai.

## Correctness proof không phải hình thức xa rời code

Formal proof có thể nặng, nhưng tư duy proof mang lại câu hỏi thiết thực:

- Precondition nào đang bị assumption ngầm?
- Loop invariant là gì?
- Data structure invariant nào method phải bảo toàn?
- Nếu duplicate/empty/overflow xảy ra thì proof còn đúng không?
- Nếu comparator không nhất quán thì ordering assumptions có vỡ không?

Property-based testing cũng xuất phát từ tinh thần tương tự: thay vì chỉ kiểm tra vài expected outputs, encode properties như “sort output là ordered và là permutation của input”. Testing không thay proof, nhưng property thinking nâng chất lượng test.

## Deterministic, randomized và nondeterministic behavior

Deterministic algorithm với cùng state/input cho cùng transition/output. Randomized algorithm dùng random choices, nên correctness/performance có thể được mô tả theo probability. QuickSort chọn random pivot có expected `O(n log n)` dù worst case vẫn `O(n²)`.

Concurrency tạo behavior có vẻ nondeterministic vì scheduling khác nhau, dù mỗi thread có code deterministic. Đây là lý do correctness concurrent systems cần reasoning về interleavings hoặc higher-level memory models.

## Online và offline algorithms

Offline algorithm thấy toàn input trước khi xử lý. Online algorithm nhận input dần và phải quyết định khi chưa biết tương lai. Cache replacement, streaming, scheduling và rate limiting thường có tính online.

Sự khác biệt này thay đổi specification và benchmark. Một algorithm optimal khi biết toàn future có thể không implementable trong real-time system.

## Exact, approximation và heuristic

Không phải problem nào cũng cần exact optimum. Approximation algorithm có guarantee về độ gần optimal; heuristic ưu tiên hiệu quả thực nghiệm nhưng thường không có guarantee mạnh. Search engine ranking, compiler optimization và route planning có thể dùng heuristics vì state space khổng lồ.

Điều quan trọng là đừng gọi heuristic là “algorithm sai”. Nếu specification chấp nhận approximate solution, nó vẫn có thể đúng theo contract. Sai là khi guarantees bị hiểu quá mức.

## Mental Model

> Một algorithm tốt không bắt đầu từ code. Hãy xác định **Input domain → State → Allowed transitions → Invariant → Termination → Output property → Resource cost**. Code chỉ là một representation của chuỗi reasoning đó.

## Common Misconceptions

**“Chạy qua test cases là chứng minh đúng.”** Test chỉ cover sampled executions. Nó có thể cho confidence nhưng không chứng minh universal property trừ khi domain hữu hạn và được exhaust.

**“Nếu complexity tốt thì algorithm tốt.”** Algorithm sai specification với `O(1)` vẫn vô dụng. Correctness, constraints và maintainability đến trước micro-optimization.

**“Recursion luôn chậm.”** Recursion là cách mô tả decomposition. Performance phụ thuộc call overhead, optimization, data access và algorithmic structure; iterative form không tự động đổi complexity class.

## Kết nối

Correctness dựa trên [logic, state và invariants](../00_computation_information/03_logic_state_abstraction_and_invariants.md). Sau khi biết procedure đúng, bước tiếp theo là hỏi [nó tốn bao nhiêu time/space](./01_complexity_and_asymptotic_analysis.md), rồi cách [data layout](./02_memory_models_and_data_layout.md) làm chi phí lý thuyết gặp hardware thật.
