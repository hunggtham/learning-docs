# Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Recursion, divide-and-conquer, greedy, backtracking và dynamic programming**. Route đi từ recurrence/state → divide-and-conquer → greedy exchange arguments → backtracking search → DP subproblem/reuse, để chiến lược gắn với proof obligation.

Thay vì nhớ hàng trăm algorithms riêng, hữu ích hơn là nhận ra vài **problem-solving structures** lặp đi lặp lại. Recursion mô tả self-similarity; divide-and-conquer tách subproblems độc lập; greedy lần ghi nhận (commit / 커밋) cục bộ (local / 로컬) choice; backtracking khám phá tìm kiếm (search / 검색) không gian (space / 공간) có pruning; động (dynamic / 동적) programming tái sử dụng overlapping subproblems.

## Recursion: định nghĩa bài toán (problem / 문제) bằng phiên bản nhỏ hơn

Recursive hàm (function / 함수) cần cơ sở (base / 기반) trường hợp (case / 사례) và recursive step tiến gần cơ sở (base / 기반). Factorial chỉ là ví dụ nhỏ; cây (tree / 트리) traversal, parsing, divide-and-conquer và đồ thị (graph / 그래프) DFS đều tự nhiên recursive.

Recursion tính đúng đắn (correctness / 정확성) thường dùng induction: giả sử hàm (function / 함수) đúng cho subproblems nhỏ hơn, chứng minh combine step tạo kết quả đúng cho kích thước (size / 크기) hiện tại.

Thời gian chạy (runtime / 런타임) thường dùng ngăn xếp lời gọi (call stack / 호출 스택), nên recursion độ sâu (depth / 깊이) lớn có thể ngăn xếp (stack / 스택) overflow nếu ngôn ngữ (language / 언어)/thời gian chạy (runtime / 런타임) không có tail-call tối ưu hóa (optimization / 최적화) hoặc thuật toán (algorithm / 알고리즘) không cân bằng.

> **Chuyển mạch:** Trong **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Divide-and-conquer** tiếp nhận điểm tựa từ **Recursion: định nghĩa bài toán (problem / 문제) bằng phiên bản nhỏ hơn** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Greedy: cục bộ (local / 로컬) choice cần proof** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Divide-and-conquer

Mẫu (pattern / 패턴):

```text
divide problem
solve subproblems
combine results
```

Merge sort chia hai halves và merge. tìm kiếm nhị phân (binary search / 이진 탐색) chỉ giữ một subproblem. Fast Fourier Transform và many hình học (geometry / 기하학) algorithms cũng theo cấu trúc (structure / 구조) này.

Lợi ích đến khi subproblems nhỏ đáng kể và combine không quá đắt. Recurrence mô tả total chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Greedy: cục bộ (local / 로컬) choice cần proof** tiếp nhận điểm tựa từ **Divide-and-conquer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Backtracking: tìm kiếm (search / 검색) có quay lui (rollback / 롤백)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Greedy: cục bộ (local / 로컬) choice cần proof

Greedy thuật toán (algorithm / 알고리즘) chọn option tốt nhất hiện tại rồi không quay lại. Nó nhanh/simpler nhưng chỉ đúng khi bài toán (problem / 문제) có cấu trúc (structure / 구조) như greedy-choice thuộc tính (property / 속성) và optimal substructure.

Ví dụ interval scheduling tối đa số non-overlapping intervals: chọn interval có finish thời gian (time / 시간) sớm nhất là chiến lược (strategy / 전략) đúng. Nhưng coin thay đổi (change / 변경) chọn coin lớn nhất không đúng với mọi denomination set. Với coins {1,3,4}, amount 6: greedy 4+1+1 dùng 3 coins, optimal 3+3 dùng 2.

Counterexample là công cụ quan trọng để phá greedy intuition.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Backtracking: tìm kiếm (search / 검색) có quay lui (rollback / 롤백)** tiếp nhận điểm tựa từ **Greedy: cục bộ (local / 로컬) choice cần proof** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Động (dynamic / 동적) Programming: trạng thái (state / 상태) là bản tóm tắt quá khứ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Backtracking: tìm kiếm (search / 검색) có quay lui (rollback / 롤백)

Backtracking xây partial solution, nếu vi phạm ràng buộc (constraint / 제약조건) thì undo và thử choice khác. Sudoku, N-Queens và ràng buộc (constraint / 제약조건) problems dùng mẫu (pattern / 패턴) này.

Worst-case có thể exponential, nhưng pruning tốt giảm tìm kiếm (search / 검색) thực tế. Branch-and-bound thêm bound để loại branches không thể beat hiện tại (current / 현재) best.

> **Chuyển mạch:** Trong **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Động (dynamic / 동적) Programming: trạng thái (state / 상태) là bản tóm tắt quá khứ** tiếp nhận điểm tựa từ **Backtracking: tìm kiếm (search / 검색) có quay lui (rollback / 롤백)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Từ recurrence sang DP** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Động (dynamic / 동적) Programming: trạng thái (state / 상태) là bản tóm tắt quá khứ

DP dùng khi subproblems overlap và optimal solution có thể xây từ solutions nhỏ hơn. Điều khó nhất không phải viết vòng lặp (loop / 루프) mà chọn **trạng thái (state / 상태)** đủ thông tin về quá khứ ảnh hưởng tương lai, nhưng không dư thừa.

Ví dụ shortest đường dẫn (path / 경로) trong DAG có trạng thái (state / 상태) `dp[v] = shortest distance to v`. Knapsack có trạng thái (state / 상태) theo items considered và sức chứa (capacity / 용량). Edit distance trạng thái (state / 상태) `dp[i][j]` mô tả prefix lengths của hai strings.

Top-down memoization giữ recursive cấu trúc (structure / 구조) và bộ nhớ đệm (cache / 캐시) results. Bottom-up tabulation xác định phụ thuộc (dependency / 의존성) thứ tự (order / 순서) rồi fill bảng (table / 테이블).

> **Chuyển mạch:** Ở chặng này của **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Từ recurrence sang DP** tiếp nhận điểm tựa từ **Động (dynamic / 동적) Programming: trạng thái (state / 상태) là bản tóm tắt quá khứ** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Không gian (space / 공간) tối ưu hóa (optimization / 최적화)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Từ recurrence sang DP

Naive Fibonacci recursion:

\[
F(n)=F(n-1)+F(n-2)
\]

recomputes same subproblems exponentially. Memoization bảo đảm mỗi `F(k)` tính một lần, thành O(n). Nhưng Fibonacci chỉ minh họa overlap; DP thật sự đáng học ở trạng thái (state / 상태) thiết kế (design / 설계) và chuyển tiếp (transition / 전이) proof.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Không gian (space / 공간) tối ưu hóa (optimization / 최적화)** tiếp nhận điểm tựa từ **Từ recurrence sang DP** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Greedy, DP hay đồ thị (graph / 그래프)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Không gian (space / 공간) tối ưu hóa (optimization / 최적화)

Nếu `dp[i]` chỉ phụ thuộc vài previous rows/states, ta không cần giữ toàn bảng (table / 테이블). Edit-distance row có thể compress từ O(mn) không gian (space / 공간) xuống O(min(m,n)) nếu chỉ cần distance, nhưng nếu cần reconstruct alignment phải giữ thêm thông tin (information / 정보) hoặc recompute.

Đây là time-space-output-requirement sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Trong **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Greedy, DP hay đồ thị (graph / 그래프)?** tiếp nhận điểm tựa từ **Không gian (space / 공간) tối ưu hóa (optimization / 최적화)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Greedy, DP hay đồ thị (graph / 그래프)?

Nhiều DP problems có thể nhìn như shortest đường dẫn (path / 경로) trên implicit DAG: trạng thái (state / 상태) là nodes, transitions là edges, chi phí (cost / 비용) là weight. Greedy Dijkstra đúng khi edge weights non-negative; general DP trên DAG dùng topological thứ tự (order / 순서). Nhìn cùng bài toán (problem / 문제) qua đồ thị (graph / 그래프) giúp thấy liên kết (connection / 연결) giữa paradigms.

> **Chuyển mạch:** Ở chặng này của **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Greedy, DP hay đồ thị (graph / 그래프)?** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> chiến lược (strategy / 전략) được chọn theo **cấu trúc (structure / 구조) của phụ thuộc (dependency / 의존성)/tìm kiếm (search / 검색) không gian (space / 공간)**: recursive self-similarity; independent subproblems → divide-and-conquer; provably safe cục bộ (local / 로컬) commitment → greedy; exhaustive choices với pruning → backtracking; repeated states → động (dynamic / 동적) programming.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Kết nối** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

**“DP là dùng một bảng (table / 테이블).”** bảng (table / 테이블) là hiện thực (implementation / 구현). Essence là trạng thái (state / 상태) + recurrence + overlapping subproblems + phụ thuộc (dependency / 의존성) thứ tự (order / 순서).

**“Greedy là chọn cái lớn nhất/nhỏ nhất.”** Greedy là irrevocable cục bộ (local / 로컬) quyết định (decision / 결정) theo criterion; tính đúng đắn (correctness / 정확성) phụ thuộc proof, không phụ thuộc vẻ hợp lý.

**“Memoization luôn cải thiện.”** Nó đổi compute lấy bộ nhớ (memory / 메모리); nếu subproblems hầu như không overlap hoặc bộ nhớ đệm (cache / 캐시) keys lớn, overhead có thể không đáng.

> **Chuyển mạch:** Trong **Recursion, divide-and-conquer, greedy, backtracking và động (dynamic / 동적) programming**, **Kết nối** tiếp nhận điểm tựa từ **Dùng chung (common / 공통) Misconceptions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Kết nối

Strategies này dựa trên [correctness/invariants](./00_algorithmic_thinking_and_correctness.md) và [complexity](./01_complexity_and_asymptotic_analysis.md). [Graph algorithms](./06_graphs_and_graph_algorithms.md) là nơi nhiều strategies gặp nhau; [distributed/system design](../90_connections/03_cross_cutting_tradeoffs.md) cũng dùng cùng tư duy decomposition và sự đánh đổi (trade-off / 트레이드오프), dù units không còn là subarray mà là services/nodes/resources.

> **Bàn giao:** Sau **Kết nối**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
