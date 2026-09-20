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
