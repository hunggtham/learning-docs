# Công cụ Toán học cho Data Structures & Algorithms
**Mathematical Toolkit for DSA / 알고리즘을 위한 수학 도구**

DSA không đòi hỏi toàn bộ Toán cao cấp, nhưng nó liên tục sử dụng một số ý tưởng toán học: logarithm, tổng hữu hạn, recurrence, combinatorics, modular arithmetic, probability, expectation, induction, graph/tree identities và asymptotic bounds. Mục tiêu của chapter này không phải biến DSA thành môn Toán thuần túy, mà giúp nhìn thấy **vì sao complexity và correctness có hình dạng như vậy** thay vì học thuộc kết quả.

Khi gặp một formula, hãy luôn hỏi nó mô tả hiện tượng gì trong algorithm. Nếu không nối được ký hiệu với structure của computation, formula chưa thực sự được hiểu.

## Logarithm là số lần giảm theo một tỷ lệ cố định

Nếu search space kích thước `n` và mỗi bước còn một nửa, sau `k` bước:

\[
\frac{n}{2^k}\approx 1
\]

suy ra:

\[
k\approx \log_2 n
\]

Đây là nguồn gốc của `O(log n)` trong binary search, balanced BST, heap height, binary lifting và nhiều divide-and-conquer algorithms.

Cơ số logarithm thường không quan trọng trong Big-O vì:

\[
\log_a n = \frac{\log_b n}{\log_b a}
\]

khác nhau bởi constant factor. Nhưng trong implementation, cơ số vẫn có thể ảnh hưởng constants và data layout. B-tree có `log_B n` theo fan-out lớn vì mỗi page chứa nhiều keys; đó chính là lý do nó phù hợp external memory.

Mental model:

> `log n` xuất hiện khi mỗi bước loại bỏ hoặc gom lại một **tỷ lệ cố định** của phần còn lại.

## Powers of two và binary representation

Powers of two xuất hiện khắp DSA vì computer representation và vì doubling/halving rất tự nhiên.

```text
1, 2, 4, 8, 16, ...
```

Heap index, Fenwick Tree, Sparse Table, binary lifting, bitmask và doubling techniques đều khai thác cấu trúc này.

Nếu `2^k <= n < 2^(k+1)`, thì `k = floor(log2 n)`. Sparse Table lưu blocks length `2^k`; binary lifting lưu ancestor ở distance `2^k`; Fenwick dùng least significant set bit để biểu diễn canonical block size.

Hiểu powers of two giúp nhìn thấy cùng một idea lặp lại dưới nhiều tên khác nhau.

## Tổng số học và nested loops

Tổng cơ bản:

\[
1+2+\cdots+n=\frac{n(n+1)}2=\Theta(n^2)
\]

giải thích loop:

```c
for (int i = 0; i < n; ++i)
    for (int j = 0; j <= i; ++j)
        work();
```

Tổng số lần `work()` không phải `n*n` chính xác, nhưng cùng bậc `Theta(n^2)`.

Một useful habit là biến nested loop thành summation. Nếu inner work phụ thuộc `i`, hãy viết:

\[
T(n)=\sum_{i=1}^{n} f(i)
\]

rồi nhận diện tổng thay vì đoán complexity bằng số loops.

## Geometric series

Tổng:

\[
1+2+4+\cdots+2^k = 2^{k+1}-1
\]

xuất hiện trong complete binary tree và amortized analysis.

Dynamic array tăng capacity gấp đôi. Tổng elements phải copy qua nhiều resize:

\[
1+2+4+\cdots+\frac n2 < n
\]

nên tổng copy work qua `n` appends là `O(n)`, làm append amortized `O(1)`.

Đây là ví dụ rất quan trọng: một operation riêng lẻ có thể `O(n)`, nhưng sequence operations vẫn có average amortized constant cost nhờ geometric growth.

## Harmonic series

Tổng harmonic:

\[
H_n=1+\frac12+\frac13+\cdots+\frac1n=\Theta(\log n)
\]

xuất hiện trong expected analysis của randomized algorithms, coupon-collector-like reasoning và một số probabilistic processes.

Không cần nhớ mọi theorem, nhưng nên nhận diện rằng tổng reciprocal thường tăng logarithmically chứ không hội tụ nhanh như geometric series.

## Recurrence mô tả shape của recursion

Recurrence ghi lại runtime của recursive algorithm bằng subproblems.

Merge sort:

\[
T(n)=2T(n/2)+cn
\]

Mỗi recursion level tổng combine work `cn`, có khoảng `log n` levels:

\[
T(n)=\Theta(n\log n)
\]

Binary search:

\[
T(n)=T(n/2)+c=\Theta(\log n)
\]

Worst-case quicksort với partitions `0` và `n-1`:

\[
T(n)=T(n-1)+cn=\Theta(n^2)
\]

Recurrence không phải notation trang trí; nó là bản mô tả mathematical của recursion tree.

## Master theorem — biết khi nào được dùng

Với recurrence dạng:

\[
T(n)=aT(n/b)+f(n)
\]

`a` là số subproblems, `n/b` là size mỗi subproblem và `f(n)` là divide/combine work. Ta so `f(n)` với:

\[
n^{\log_b a}
\]

để xác định phần nào chi phối.

Master theorem rất tiện cho balanced divide-and-conquer, nhưng không nên ép vào recurrence như `T(n)=T(n-1)+n`, subproblems không đều hoặc random recurrence phức tạp. Recursion tree, substitution hoặc probabilistic analysis có thể phù hợp hơn.

## Counting principle

Combinatorics giúp ước lượng search space trước khi code.

Nếu có `n` independent binary choices, số assignments là:

\[
2^n
\]

Nếu mỗi position có `k` choices:

\[
k^n
\]

Permutations của `n` distinct items:

\[
n!
\]

Combinations chọn `r` items:

\[
\binom nr = \frac{n!}{r!(n-r)!}
\]

Những số này quyết định feasibility. `2^20` khoảng một triệu; `2^40` khoảng một nghìn tỷ. `20!` đã cực lớn.

## Principle of product và sum

Nếu một process có `a` cách ở bước 1 và `b` cách độc lập tiếp theo, tổng paths là `ab`. Nếu hai groups alternatives loại trừ nhau có `a` và `b` cách, tổng là `a+b`.

Backtracking tree size thường được ước lượng bằng branching factor và depth:

\[
O(b^d)
\]

nhưng pruning có thể làm effective branching factor nhỏ hơn nhiều.

## Pigeonhole principle

Nếu nhét nhiều hơn `m` objects vào `m` buckets, ít nhất một bucket chứa từ hai objects trở lên. Đây là nền tảng trực giác cho hash collisions: key space thường lớn hơn bucket space, nên collision không thể tránh hoàn toàn.

Pigeonhole cũng xuất hiện trong cycle detection, duplicate reasoning và combinatorial proofs.

## Inclusion–exclusion

Khi đếm union của sets, cộng trực tiếp có thể double-count overlap.

Hai sets:

\[
|A\cup B|=|A|+|B|-|A\cap B|
\]

Idea này xuất hiện trong combinatorics, bitmask DP/SOS DP, probability và counting problems. Với nhiều sets, formula mở rộng theo alternating intersections.

## Prefix sums là đại số của phép trừ phần đã tích lũy

Prefix sum:

\[
P[i]=\sum_{j=0}^{i-1} a_j
\]

cho:

\[
sum(L,R)=P[R+1]-P[L]
\]

Tại sao? Vì `P[R+1]` chứa prefix đến `R`, còn `P[L]` chính là phần trước `L` cần loại.

Mental model này tổng quát sang cumulative counts, prefix XOR và difference arrays. Khi operation có inverse phù hợp, prefix aggregation rất mạnh.

## Associativity, identity, inverse và idempotence

Một số DSA structures hoạt động nhờ properties đại số.

**Associativity / 결합법칙**:

\[
(a*b)*c=a*(b*c)
\]

cho phép group ranges theo nhiều cách. Segment Tree cần combine operation associative.

**Identity / 항등원** là phần tử `e` sao cho `a*e=e*a=a`. Sum có identity `0`; min có `+infinity`.

**Inverse / 역원** cho phép “trừ” contribution. Prefix sums dùng additive inverse; prefix minimum không có inverse tương tự.

**Idempotence / 멱등성**:

\[
f(x,x)=x
\]

cho phép Sparse Table classic dùng overlapping blocks với min/max/GCD.

Hiểu các properties này giúp biết một structure có thể generalize tới operation nào.

## Modular arithmetic

Modulo xuất hiện trong hashing, combinatorial counting, cyclic buffers và number-theoretic algorithms.

Các identities cơ bản:

\[
(a+b)\bmod m = ((a\bmod m)+(b\bmod m))\bmod m
\]

\[
(ab)\bmod m = ((a\bmod m)(b\bmod m))\bmod m
\]

Nhưng division không thể thay bằng integer division modulo. Cần **modular inverse** khi inverse tồn tại.

Trong programming contests hoặc combinatorial DP, một prime modulus thường được chọn để inverse dễ xử lý bằng Fermat's little theorem dưới conditions phù hợp.

## Negative modulo semantics khác nhau theo ngôn ngữ

Mathematical modulo thường được định nghĩa non-negative, nhưng language `%` có thể là remainder với sign rules riêng. Trong Java/C/JavaScript, negative operand có thể tạo negative remainder.

Nếu cần normalized modulo:

```text
((x % m) + m) % m
```

là pattern phổ biến, nhưng vẫn phải xét overflow/range trong language cụ thể.

## GCD và Euclidean algorithm

Greatest Common Divisor xuất hiện trong fractions, modular arithmetic, number theory và range queries.

Euclid:

\[
gcd(a,b)=gcd(b,a\bmod b)
\]

mỗi bước giảm mạnh argument, cho logarithmic complexity theo magnitude.

GCD còn là associative và idempotent, nên phù hợp Sparse Table static range GCD.

## Probability: event, conditional probability và independence

Randomized algorithms cần assumption xác suất rõ ràng.

Nếu events độc lập:

\[
P(A\cap B)=P(A)P(B)
\]

Nhưng independence không nên được giả định chỉ vì hai events “trông khác nhau”. Hash functions correlated hoặc reused randomness có thể phá model.

Conditional probability:

\[
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
\]

hữu ích khi reasoning về collision, randomized sampling và Bayesian-like updates.

## Expected value và linearity of expectation

Expected value:

\[
E[X]=\sum_x xP(X=x)
\]

Một property cực mạnh:

\[
E[X+Y]=E[X]+E[Y]
\]

không cần `X` và `Y` độc lập.

Điều này cho phép phân tích tổng work bằng indicator variables. Ví dụ expected number of collisions hoặc expected successful comparisons có thể được tách thành contribution của từng event.

Linearity of expectation là một trong những tools probabilistic hữu ích nhất trong algorithm analysis.

## Indicator variables

Định nghĩa indicator:

\[
I_i=\begin{cases}
1 & \text{nếu event i xảy ra}\\
0 & \text{nếu không}
\end{cases}
\]

thì:

\[
E[I_i]=P(event_i)
\]

Nếu total count `X = \sum I_i`, thì:

\[
E[X]=\sum P(event_i)
\]

Cách này biến bài toán “đếm expected number” thành tổng probabilities, rất hữu ích cho randomized algorithms.

## Variance và concentration intuition

Expectation chỉ cho average, không nói distribution tập trung quanh average bao nhiêu. Variance đo spread:

\[
Var(X)=E[(X-E[X])^2]
\]

Trong production latency hoặc probabilistic structures, tail behavior có thể quan trọng hơn mean. Chernoff/Hoeffding bounds là các tools nâng cao để chứng minh sum of random variables tập trung quanh expectation dưới assumptions thích hợp.

Không nhất thiết phải thuộc công thức ngay, nhưng nên nhớ: “expected good” chưa đồng nghĩa “bad case cực hiếm” nếu chưa có concentration argument.

## Randomized vs probabilistic output

Một randomized algorithm có thể luôn trả exact answer nhưng runtime random, ví dụ randomized quicksort.

Một probabilistic data structure có thể trả approximate answer với bounded error, ví dụ Bloom Filter hoặc HyperLogLog.

Hai khái niệm này khác nhau: randomness có thể ảnh hưởng performance, correctness probability hoặc cả hai.

## Structural induction

Tree, linked structure và recursive grammar thường được chứng minh bằng structural induction.

Base: empty/leaf structure đúng.

Step: giả sử substructures đúng, chứng minh combine node hiện tại đúng.

Đây là mathematical version của recursive contract.

## Strong induction và DP

Dynamic Programming state `i` có thể phụ thuộc nhiều states nhỏ hơn. Strong induction giả sử theorem đúng cho mọi state nhỏ hơn rồi chứng minh state hiện tại.

Bottom-up DP thực chất là thực thi proof order này: tính prerequisites trước để transition hiện tại dựa trên values đã đúng.

## Graph identities

Một undirected tree connected với `n` vertices có:

\[
|E|=n-1
\]

Ngược lại, một connected undirected graph có `n-1` edges thì nó là tree. Nếu graph acyclic với `n-1` edges thì cũng connected.

Các identities này giúp reasoning và validation.

Handshaking lemma:

\[
\sum_{v\in V} degree(v)=2|E|
\]

vì mỗi undirected edge đóng góp 1 degree cho hai endpoints. Suy ra số vertices odd degree luôn chẵn — nền tảng cho Euler trail conditions.

Với directed graph:

\[
\sum indegree(v)=\sum outdegree(v)=|E|
\]

## Tree height và node count

Perfect binary tree height `h` có:

\[
1+2+\cdots+2^h=2^{h+1}-1
\]

nên nếu balanced tree có `n` nodes, height logarithmic. Đây là mathematical link giữa branching factor và search depth.

B-tree dùng branching factor lớn `B`, nên height gần `log_B n`, giảm page accesses.

## Amortized analysis: aggregate method

Aggregate method nhìn cả sequence. Nếu `n` operations tổng cost `T(n)`, amortized cost là:

\[
\frac{T(n)}n
\]

Dynamic array doubling là example kinh điển. Một vài resize đắt nhưng tổng copy work tuyến tính.

Amortized không phải average-case probability. Nó cho guarantee trên mọi sequence thuộc model, chỉ phân phối cost không đều giữa operations.

## Accounting method

Ta có thể “charge” operation rẻ nhiều hơn actual cost và dùng credit trả cho operation đắt sau này.

Ví dụ mỗi append trả một số constant credits; credits tích lũy đủ để cover future array copy. Đây là cách trực giác để chứng minh amortized `O(1)` mà không cần summation chi tiết mỗi lần.

## Potential method

Potential method định nghĩa một function `Φ(state)` biểu diễn prepaid work/độ “căng” của structure.

Amortized cost:

\[
\hat c_i=c_i+\Phi(D_i)-\Phi(D_{i-1})
\]

Nếu potential tăng ở operation rẻ, ta tích credit; nếu operation đắt làm potential giảm, stored potential trả cost.

Potential method rất mạnh cho dynamic arrays, stack sequences, splay-like analysis và nhiều dynamic structures.

## Information-theoretic lower bounds

Comparison sorting phải phân biệt `n!` possible permutations. Một comparison nhị phân cung cấp tối đa khoảng một bit information. Decision tree cần ít nhất:

\[
\log_2(n!)=\Omega(n\log n)
\]

height trong worst case.

Stirling approximation cho intuition:

\[
\log(n!)=\Theta(n\log n)
\]

Điều này giải thích vì sao general comparison sort không thể có worst-case `O(n)`.

Lower bound không nói counting/radix sort bất khả thi vì chúng dùng information khác ngoài pairwise comparison.

## Search lower-bound intuition

Unsorted array không có structure giúp loại vùng candidates, nên exact membership trong comparison model có thể cần xem mọi element: `Omega(n)` worst case.

Sorted order cho phép mỗi comparison loại khoảng nửa candidates, dẫn tới logarithmic search.

Lower bounds thường đến từ câu hỏi: **mỗi observation cung cấp bao nhiêu information?**

## Asymptotic notation chính xác hơn

`O(g(n))` là upper bound asymptotic.

`Ω(g(n))` là lower bound.

`Θ(g(n))` là tight bound — vừa upper vừa lower cùng bậc.

Một algorithm `Θ(n)` cũng thuộc `O(n^2)`, nhưng nói `O(n^2)` là bound lỏng và ít informative hơn.

Worst-case, average-case, expected và amortized là dimensions khác với `O/Θ/Ω`; không nên trộn chúng.

## Numeric growth và overflow

Mathematical formula có thể đúng nhưng implementation overflow.

`n(n+1)/2` có thể overflow trước division dù result cuối fit. `mid=(lo+hi)/2` có thể overflow integer, nên binary search thường dùng:

```text
lo + (hi - lo) / 2
```

Combinatorial counts như `n!`, Fibonacci hoặc number of paths tăng rất nhanh; cần `BigInteger`, `BigInt`, modulo arithmetic hoặc saturation tùy requirement.

## Floating point và error

Real-number formulas khi chạy trên IEEE-754 có rounding. Summation order có thể đổi error. Equality comparisons có thể không ổn định. Binary search trên real values cần stopping criterion theo iterations hoặc tolerance.

Numerical correctness là một layer khác của mathematical reasoning.

## Feasibility estimation trước khi code

Một kỹ năng thực dụng là ước lượng rough operation budget.

Nếu `n = 10^5`, `O(n^2)` thường quá lớn trong latency thông thường. `O(n log n)` thường khả thi. `2^n` chỉ hợp khi `n` nhỏ. Nhưng constants, language/runtime, cache và operation complexity vẫn quan trọng.

Không nên biến rough budget thành luật cứng; mục tiêu là loại sớm những algorithm scale sai rõ ràng.

## Common misconceptions

`log n` không xuất hiện chỉ vì có recursion; nó xuất hiện khi state size giảm multiplicatively.

Expected `O(1)` không phải deterministic `O(1)`.

Amortized `O(1)` không phải “trung bình trên random input”.

Modulo không cho phép chia như arithmetic bình thường nếu inverse không tồn tại.

Associative không đồng nghĩa idempotent; vì thế Segment Tree và Sparse Table classic có requirements khác.

`O(n)` không luôn nhanh hơn `O(n log n)` ở input nhỏ; asymptotic notation mô tả growth, không constants.

## Mental Model

> Toán học trong DSA là ngôn ngữ để trả lời bốn câu hỏi: search space lớn bao nhiêu, mỗi bước loại được bao nhiêu, work được lặp lại theo cấu trúc nào, và guarantee đúng/nhanh mạnh tới đâu.

Khi thấy một complexity hoặc theorem, hãy nối nó về structure: `log n` vì halving/doubling, `n log n` vì `log n` levels mỗi level `n` work, `2^n` vì binary choices, amortized constant vì geometric total work, expected bound vì random variables và assumptions, lower bound vì information cần phân biệt nhiều possible answers.

Xem tiếp: [Complexity Analysis](./02_complexity_analysis.md), [Correctness & Invariants](./01_algorithm_correctness_and_invariants.md), [Divide and Conquer](../04_algorithmic_paradigms/03_divide_and_conquer.md), [Dynamic Programming](../04_algorithmic_paradigms/05_dynamic_programming.md), [Amortized & Randomized Thinking](../05_specialized/03_amortized_randomized_and_probabilistic_thinking.md) và [Bit Manipulation](../05_specialized/02_bit_manipulation_and_bitsets.md).
