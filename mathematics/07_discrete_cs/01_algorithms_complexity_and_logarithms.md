# Độ phức tạp thuật toán và ý nghĩa của logarithm: từ counting work đến scalability

Phân tích độ phức tạp (algorithmic complexity / 알고리즘 복잡도) không nhằm dự đoán chính xác chương trình chạy bao nhiêu milliseconds. Nó trả lời câu hỏi cấu trúc hơn:

> Khi input size tăng, lượng resource cần thiết tăng theo **shape** nào?

Đây là câu hỏi về scalability. Một implementation rất nhanh ở `n=100` có thể trở nên vô dụng ở `n=10^9` nếu growth rate xấu. Ngược lại, algorithm có constant overhead lớn nhưng asymptotic tốt có thể thắng ở scale lớn.

## Trước Big-O phải chọn cost model

Complexity luôn phụ thuộc điều ta đang count.

Ta có thể count:

- arithmetic operations;
- comparisons;
- memory usage;
- disk I/O;
- network round trips;
- cache misses;
- parallel depth.

Statement `O(n)` không có nghĩa universal “nhanh”. Một scan `O(n)` trên RAM và `O(n)` remote API calls có latency hoàn toàn khác.

Vì vậy analysis bắt đầu bằng input-size definition và cost model.

## Big-O là asymptotic upper bound

`f(n)=O(g(n))` nếu tồn tại constants `c>0` và `n_0` sao cho

```math
0\le f(n)\le c g(n)
```

với mọi `n\ge n_0`.

Big-O nói rằng sau một scale đủ lớn, `f` không grow nhanh hơn `g` hơn constant factor.

Tight bound dùng `\Theta`:

```math
f(n)=\Theta(g(n))
```

nếu `f` vừa upper-bounded vừa lower-bounded bởi constant multiples của `g` asymptotically.

`\Omega` biểu diễn lower asymptotic bound.

## Vì sao constants và lower-order terms thường bị bỏ?

Giả sử

```math
T(n)=3n^2+10n+500.
```

Chia cho `n^2`:

```math
\frac{T(n)}{n^2}
=
3+\frac{10}{n}+\frac{500}{n^2}.
```

Khi `n\to\infty`, lower-order terms vanish và ratio tiến về 3. Growth structure dominant là quadratic:

```math
T(n)=\Theta(n^2).
```

Nhưng constants vẫn matter trong engineering. Complexity analysis và benchmarking trả lời hai câu hỏi khác nhau:

```text
complexity: scaling shape là gì?
benchmark: implementation này nhanh bao nhiêu trên workload/hardware cụ thể?
```

## `O(1)` không nghĩa “một instruction”

Constant complexity nghĩa cost không grow với chosen input size `n`.

Hash-table lookup average-case có thể được gọi expected `O(1)` under assumptions, nhưng vẫn có hashing, memory access và collision handling.

Database indexed lookup có thể look constant ở application abstraction nhưng storage engine thực tế dùng tree/page I/O. Complexity label chỉ meaningful khi model rõ.

## Linear và quadratic growth

Linear scan:

```math
T(n)=an+b
```

scale proportionally với `n`.

All-pairs comparison thường:

```math
\binom n2
=
\frac{n(n-1)}2
=
\Theta(n^2).
```

Nếu `n` tăng 10×, linear work tăng khoảng 10×, quadratic tăng khoảng 100×.

Đây là practical meaning của growth class.

## Logarithm xuất hiện khi progress là multiplicative

Nếu mỗi step giảm problem size bởi factor `b>1`:

```math
n,
\frac nb,
\frac n{b^2},
\ldots
```

Sau `k` steps muốn còn khoảng 1:

```math
\frac n{b^k}\approx1.
```

Nên

```math
b^k\approx n,
```

và

```math
k\approx\log_b n.
```

Vì vậy logarithmic complexity không đến từ việc code gọi hàm `log`. Nó xuất hiện từ repeated multiplicative shrinkage.

## Worked example — binary search

Sorted array size `n`. Mỗi comparison loại khoảng half candidates.

Recurrence:

```math
T(n)=T(n/2)+O(1).
```

Unroll:

```math
T(n)=T(n/2^k)+kO(1).
```

Stop khi

```math
n/2^k\approx1,
```

nên

```math
k\approx\log_2n.
```

Do đó

```math
T(n)=O(\log n).
```

Log base không matter trong Big-O vì

```math
\log_a n
=
\frac{\log_b n}{\log_b a},
```

chỉ khác constant factor.

## Balanced trees và logarithmic height

Balanced binary tree với branching factor roughly 2 có number nodes tăng exponential theo depth:

```math
1+2+4+\cdots+2^h\approx2^{h+1}.
```

Do đó storing `n` nodes cần height

```math
h=O(\log n).
```

Search/update complexity xuất hiện từ same multiplicative geometry như binary search.

## Divide and conquer: vì sao `n log n` xuất hiện?

Merge sort recurrence:

```math
T(n)=2T(n/2)+O(n).
```

Recursion tree có `\log_2n` levels. Ở mỗi level, total merge work across subproblems là `O(n)`.

Do đó

```math
T(n)=O(n\log n).
```

Meaning: ta trả linear work ở mỗi logarithmic level of decomposition.

## Master theorem là pattern recognition, không phải spell

Recurrence dạng

```math
T(n)=aT(n/b)+f(n)
```

so sánh work trong recursive subproblems với nonrecursive work `f(n)`.

Master theorem useful khi structure match, nhưng không thay thế việc hiểu recursion tree. Nếu recurrence không đúng form hoặc subproblem sizes irregular, theorem có thể không áp dụng.

## Exponential explosion: khi micro-optimization không cứu được model

Enumerate all subsets:

```math
2^n.
```

Enumerate all permutations:

```math
n!.
```

Ví dụ

```math
2^{100}\approx1.27\times10^{30}.
```

Dù xử lý one billion states mỗi second, exhaustive enumeration vẫn infeasible.

Khi growth class exponential/factorial, solution thường cần **algorithmic insight**: dynamic programming, pruning, approximation, relaxations hoặc exploit problem structure.

## Worst-case, average-case và expected complexity

Complexity statement phải nói case nào.

Quicksort có average/expected `O(n\log n)` under common pivot assumptions nhưng worst-case `O(n^2)`.

Hash tables often expected `O(1)` lookup, nhưng adversarial collisions có thể degrade.

Worst-case useful cho guarantees; expected/average useful khi probabilistic workload assumptions justified.

## Amortized analysis: expensive operation nhưng cheap sequence

Dynamic array append thường `O(1)`, nhưng occasionally resize costs `O(n)`.

Nếu capacity doubles, total copied elements over many appends is geometric series:

```math
1+2+4+\cdots+n<2n.
```

Across `n` appends, total resize work `O(n)`, nên amortized cost per append là `O(1)`.

Amortized không phải probabilistic average; nó là deterministic accounting over operation sequence.

## Space complexity và time-space trade-off

Memoization lưu previous results để tránh recomputation. Dynamic programming thường đổi extra memory lấy lower time.

BFS giữ frontier có thể lớn; DFS dùng stack depth khác. External-memory algorithms optimize I/O vì disk access dominates arithmetic.

Algorithm design luôn là multi-resource problem, không chỉ time.

## Lower bounds: có những giới hạn không thể vượt bằng clever coding

Comparison sorting có lower bound

```math
\Omega(n\log n)
```

trong comparison model.

Proof idea: `n!` possible input orders cần được distinguish. Decision tree với binary comparisons depth `h` có tối đa `2^h` leaves, nên

```math
2^h\ge n!,
```

suy ra

```math
h\ge\log_2(n!)=\Omega(n\log n).
```

Meaning: merge sort/heapsort are asymptotically optimal among comparison-based sorts. Muốn beat bound phải change model/assumptions, như counting sort exploiting bounded integer keys.

## Complexity classes và tractability intuition

Polynomial-time algorithms thường được xem là tractable baseline trong theoretical CS, nhưng degree/constant vẫn matter. `O(n^{100})` không practical; `O(2^n)` có thể practical nếu `n=20`.

Complexity theory nói asymptotic structure, engineering feasibility cần actual scale.

## Dynamic programming: reduce state explosion bằng overlapping structure

Naive Fibonacci recursion:

```math
F(n)=F(n-1)+F(n-2)
```

recomputes same subproblems exponentially nhiều lần.

Memoization stores each `F(k)` once, reducing time to `O(n)`.

DP không làm mọi exponential problem polynomial. It works when state space nhỏ enough và subproblems overlap with optimal substructure.

## Graph algorithms: complexity phụ thuộc representation

BFS/DFS với adjacency list:

```math
O(|V|+|E|).
```

Adjacency matrix traversal có thể cost `O(|V|^2)` even when graph sparse.

Same algorithm idea có complexity khác theo data representation. Complexity analysis phải include representation choice.

## AI connection — training complexity

Training cost depends on samples, model dimension, sequence length, batch size và hardware parallelism. Một operation theoretically `O(n^2)` như full attention becomes major bottleneck khi sequence length tăng.

Nhưng FLOP complexity alone chưa đủ: memory bandwidth, communication và kernel utilization có thể dominate wall-clock.

## Finance connection — Monte Carlo và scenario explosion

Risk engines may simulate `N` scenarios across `M` instruments, roughly `O(NM)` valuation work if no sharing. Path-dependent derivatives add time steps. Variance reduction can reduce scenarios needed for same accuracy, effectively improving cost-to-error relation even if per-scenario complexity same.

## Assumptions và failure modes

Asymptotic analysis can mislead when `n` small, constants huge, memory hierarchy dominates hoặc network latency matters.

Input-size definition itself can be subtle. Integer arithmetic on very large numbers is not constant-time if bit length grows.

Parallel speedup limited by serial fractions and communication; work complexity và span/depth both matter.

## Mental Model

> Complexity analysis is growth accounting. Ask what state shrinks or expands each step, what resource is counted, and how many structurally distinct steps are needed as input scale grows. Logarithms appear when progress is multiplicative; polynomial/exponential distinctions tell when optimization should target code constants versus algorithmic structure.

## Common Misconceptions

**“Big-O is exact runtime.”** Không; nó là asymptotic bound under a cost model.

**“`O(1)` means instant.”** Không; constant with respect to `n` can still be expensive.

**“Nested loops always mean `O(n^2)`.”** Need analyze iteration ranges and state changes.

**“`O(log n)` means code computes logarithm.”** Log often comes from repeated halving or multiplicative branching.

**“Asymptotically better always faster.”** Not at every practical input size; constants, cache and hardware matter.

**“Optimization can rescue `2^n` by making code 10× faster.”** Growth-rate problems often require changing algorithmic structure.