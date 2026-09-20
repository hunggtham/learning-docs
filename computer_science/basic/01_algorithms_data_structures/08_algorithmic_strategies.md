# Recursion, divide-and-conquer, greedy, backtracking và dynamic programming

Thay vì nhớ hàng trăm algorithms riêng, hữu ích hơn là nhận ra vài **problem-solving structures** lặp đi lặp lại. Recursion mô tả self-similarity; divide-and-conquer tách subproblems độc lập; greedy commit local choice; backtracking khám phá search space có pruning; dynamic programming tái sử dụng overlapping subproblems.

## Recursion: định nghĩa problem bằng phiên bản nhỏ hơn

Recursive function cần base case và recursive step tiến gần base. Factorial chỉ là ví dụ nhỏ; tree traversal, parsing, divide-and-conquer và graph DFS đều tự nhiên recursive.

Recursion correctness thường dùng induction: giả sử function đúng cho subproblems nhỏ hơn, chứng minh combine step tạo kết quả đúng cho size hiện tại.

Runtime thường dùng call stack, nên recursion depth lớn có thể stack overflow nếu language/runtime không có tail-call optimization hoặc algorithm không cân bằng.

## Divide-and-conquer

Pattern:

```text
divide problem
solve subproblems
combine results
```

Merge sort chia hai halves và merge. Binary search chỉ giữ một subproblem. Fast Fourier Transform và many geometry algorithms cũng theo structure này.

Lợi ích đến khi subproblems nhỏ đáng kể và combine không quá đắt. Recurrence mô tả total cost.

## Greedy: local choice cần proof

Greedy algorithm chọn option tốt nhất hiện tại rồi không quay lại. Nó nhanh/simpler nhưng chỉ đúng khi problem có structure như greedy-choice property và optimal substructure.

Ví dụ interval scheduling tối đa số non-overlapping intervals: chọn interval có finish time sớm nhất là strategy đúng. Nhưng coin change chọn coin lớn nhất không đúng với mọi denomination set. Với coins {1,3,4}, amount 6: greedy 4+1+1 dùng 3 coins, optimal 3+3 dùng 2.

Counterexample là công cụ quan trọng để phá greedy intuition.

## Backtracking: search có rollback

Backtracking xây partial solution, nếu vi phạm constraint thì undo và thử choice khác. Sudoku, N-Queens và constraint problems dùng pattern này.

Worst-case có thể exponential, nhưng pruning tốt giảm search thực tế. Branch-and-bound thêm bound để loại branches không thể beat current best.

## Dynamic Programming: state là bản tóm tắt quá khứ

DP dùng khi subproblems overlap và optimal solution có thể xây từ solutions nhỏ hơn. Điều khó nhất không phải viết loop mà chọn **state** đủ thông tin về quá khứ ảnh hưởng tương lai, nhưng không dư thừa.

Ví dụ shortest path trong DAG có state `dp[v] = shortest distance to v`. Knapsack có state theo items considered và capacity. Edit distance state `dp[i][j]` mô tả prefix lengths của hai strings.

Top-down memoization giữ recursive structure và cache results. Bottom-up tabulation xác định dependency order rồi fill table.

## Từ recurrence sang DP

Naive Fibonacci recursion:

\[
F(n)=F(n-1)+F(n-2)
\]

recomputes same subproblems exponentially. Memoization bảo đảm mỗi `F(k)` tính một lần, thành O(n). Nhưng Fibonacci chỉ minh họa overlap; DP thật sự đáng học ở state design và transition proof.

## Space optimization

Nếu `dp[i]` chỉ phụ thuộc vài previous rows/states, ta không cần giữ toàn table. Edit-distance row có thể compress từ O(mn) space xuống O(min(m,n)) nếu chỉ cần distance, nhưng nếu cần reconstruct alignment phải giữ thêm information hoặc recompute.

Đây là time-space-output-requirement trade-off.

## Greedy, DP hay graph?

Nhiều DP problems có thể nhìn như shortest path trên implicit DAG: state là nodes, transitions là edges, cost là weight. Greedy Dijkstra đúng khi edge weights non-negative; general DP trên DAG dùng topological order. Nhìn cùng problem qua graph giúp thấy connection giữa paradigms.

## Mental Model

> Strategy được chọn theo **structure của dependency/search space**: recursive self-similarity; independent subproblems → divide-and-conquer; provably safe local commitment → greedy; exhaustive choices với pruning → backtracking; repeated states → dynamic programming.

## Common Misconceptions

**“DP là dùng một table.”** Table là implementation. Essence là state + recurrence + overlapping subproblems + dependency order.

**“Greedy là chọn cái lớn nhất/nhỏ nhất.”** Greedy là irrevocable local decision theo criterion; correctness phụ thuộc proof, không phụ thuộc vẻ hợp lý.

**“Memoization luôn cải thiện.”** Nó đổi compute lấy memory; nếu subproblems hầu như không overlap hoặc cache keys lớn, overhead có thể không đáng.

## Kết nối

Strategies này dựa trên [correctness/invariants](./00_algorithmic_thinking_and_correctness.md) và [complexity](./01_complexity_and_asymptotic_analysis.md). [Graph algorithms](./06_graphs_and_graph_algorithms.md) là nơi nhiều strategies gặp nhau; [distributed/system design](../90_connections/03_cross_cutting_tradeoffs.md) cũng dùng cùng tư duy decomposition và trade-off, dù units không còn là subarray mà là services/nodes/resources.
