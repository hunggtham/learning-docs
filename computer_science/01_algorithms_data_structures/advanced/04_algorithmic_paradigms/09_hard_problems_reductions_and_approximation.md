# Khi Exact Algorithm trở nên khó: Reductions, NP-Complete và Approximation  
**환원, NP-완전, 근사 알고리즘**

DSA không chỉ dạy cách làm nhanh; nó cũng phải dạy nhận ra khi một bài toán có vẻ chống lại mọi cố gắng polynomial-time exact.

## Polynomial vs exponential scale

`O(n^3)` có thể nặng nhưng vẫn polynomial. `O(2^n)` tăng khác hẳn: thêm một biến có thể nhân đôi search space. Với `n` vài chục, brute-force có thể đã khó.

Constraint nhỏ đôi khi cho phép exponential algorithms; constraint lớn buộc ta khai thác structure đặc biệt, approximation, parameterization hoặc heuristic.

## Decision problem và NP intuition

NP bao gồm các decision problems mà một proposed solution có thể được verify trong polynomial time. NP-complete problems vừa thuộc NP vừa đủ khó để mọi problem trong NP reduce tới chúng theo polynomial reduction.

Không cần đồng nhất “NP” với “không giải được”. Nhiều instances thực tế nhỏ/có structure vẫn giải được; nhiều special cases có polynomial algorithms.

## Reduction

Reduction là cách dùng solver của problem B để giải problem A sau transformation polynomial. Nếu A đã biết khó và A reduces to B, B ít nhất khó tương đương theo framework đó.

Trong algorithm design, reduction cũng là công cụ tích cực: biến problem mới thành shortest path, matching, flow, SAT hoặc known structure rồi tái sử dụng algorithm.

## Traveling Salesperson distinction

TSP optimization tổng quát tìm tour minimum qua mọi vertices. Held–Karp DP dùng subset state khoảng `O(n^2 2^n)`, tốt hơn factorial brute force nhưng vẫn exponential.

Metric TSP có approximation guarantees nhờ triangle inequality; general TSP không có cùng behavior. Thêm assumption domain thay đổi algorithmic possibilities.

## Approximation

Approximation algorithm trả solution có provable ratio so với optimum. Nó khác heuristic không guarantee. Ví dụ một 2-approximation nói cost không quá 2 lần optimum cho minimization dưới assumptions.

## Parameterized thinking

Một algorithm `O(f(k) n^c)` có thể thực dụng nếu parameter `k` nhỏ dù worst-case theo `k` exponential. Đây là fixed-parameter tractability mindset.

## Mental Model

> Khi search space bùng nổ, câu hỏi không còn chỉ là “data structure nào nhanh hơn?” mà là “problem có structure nào cho phép exact polynomial algorithm không; nếu không, ta chấp nhận constraint, parameter, approximation hay heuristic nào?”

## P, NP, NP-hard và NP-complete

**P** là lớp decision problems có algorithm polynomial-time đã biết trong model chuẩn.

**NP** là lớp decision problems mà một certificate “yes” có thể được verify trong polynomial time.

**NP-hard** nghĩa problem ít nhất khó bằng mọi problem trong NP theo polynomial reductions; nó không bắt buộc bản thân là decision problem hay thuộc NP.

**NP-complete** nghĩa vừa thuộc NP vừa NP-hard.

Cho tới hiện nay không có proof được cộng đồng chấp nhận rằng `P = NP` hay `P ≠ NP`. Vì vậy khi nói một problem NP-complete, kết luận thực dụng là: không biết general exact polynomial-time algorithm, và nếu tìm được một cái thì hậu quả lý thuyết rất lớn.

## Reduction phải giữ yes/no semantics

Nếu reduction biến instance `x` của A thành `f(x)` của B, ta cần:

\[
x\in A \iff f(x)\in B
\]

và transformation phải polynomial time.

Một connection đơn giản giữa Independent Set và Vertex Cover trong cùng graph là:

\[
S \text{ independent}
\iff
V\setminus S \text{ vertex cover}
\]

Do đó question “có independent set size ít nhất `k`?” tương đương “có vertex cover size nhiều nhất `|V|-k`?”. Đây là transformation structural, không phải gọi hai problems “giống nhau”.

## Exact exponential algorithms vẫn có giá trị

NP-hard không có nghĩa chỉ dùng heuristic. Nếu `n` nhỏ, exact approaches có thể gồm:

```text
backtracking + pruning
branch and bound
bitmask DP
meet-in-the-middle
integer programming / SAT solver
parameterized algorithm
```

Meet-in-the-middle là ví dụ quan trọng: split `n` items thành hai halves, enumerate khoảng `2^(n/2)` states mỗi phía thay vì `2^n` direct search, rồi combine bằng sorting/hash/binary search.

## Branch and bound

Backtracking chỉ prune branch khi infeasible. Branch-and-bound còn dùng optimistic bound về best possible future objective. Nếu bound đã không thể thắng best solution hiện tại, branch được loại.

Correctness phụ thuộc bound phải thật sự optimistic/safe; bound quá “lạc quan” chỉ prune ít, nhưng bound không hợp lệ có thể xóa optimal solution.

## Approximation ratio

Với minimization, một `α`-approximation thường bảo đảm:

\[
cost(A(I)) \le \alpha\cdot OPT(I)
\]

cho mọi instance thuộc problem class, với `α >= 1`.

Guarantee phải đi cùng assumptions. Metric TSP có triangle inequality, nhờ đó approximation strategies tồn tại mà general weighted TSP không được hưởng tương tự.

## Heuristic khác approximation

Heuristic có thể rất hiệu quả thực tế nhưng không có worst-case quality guarantee tương tự. Local search, simulated annealing, genetic methods hoặc domain-specific greedy có thể hợp production nếu objective và latency quan trọng hơn proof ratio.

Không nên dùng từ “approximation” chỉ để nói “answer gần đúng”.

## Parameterized algorithms

Nếu difficulty tập trung vào parameter `k`, runtime:

\[
f(k)\cdot n^{O(1)}
\]

có thể rất tốt khi `k` nhỏ. Ví dụ một search exponential theo solution size nhưng linear/polynomial theo graph size có thể practical hơn algorithm exponential theo toàn `n`.

## Mental Model mở rộng

> Complexity theory không nói “bỏ cuộc”. Nó giúp chọn **kiểu thỏa hiệp có nguyên tắc**: giới hạn input, khai thác special structure, parameterize, approximate, hoặc dùng heuristic — và biết guarantee nào mình đã từ bỏ.
