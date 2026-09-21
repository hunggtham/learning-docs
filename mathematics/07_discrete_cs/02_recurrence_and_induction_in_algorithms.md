# Recurrence, induction và recursion: một structure chung của algorithmic reasoning

Đệ quy (recursion / 재귀), quan hệ truy hồi (recurrence / 점화식) và quy nạp (induction / 수학적 귀납법) thường được học ở ba nơi khác nhau: programming, discrete mathematics và proof. Nhưng chúng là ba mặt của cùng một idea:

> một object/problem lớn được xây từ versions nhỏ hơn của chính nó.

Recursion mô tả **computation**. Recurrence mô tả **quantity thay đổi theo size/state**. Induction mô tả **proof rằng structure đó đúng ở mọi size**.

Khi nhìn chúng cùng nhau, divide-and-conquer, dynamic programming, tree algorithms và loop invariants trở nên thống nhất hơn rất nhiều.

## 1. Recursion cần một well-founded descent

Một recursive definition phải có:

```text
base case
+
rule giảm problem về case nhỏ hơn
```

Ví dụ factorial:

```math
n!=n(n-1)!,
```

với

```math
0!=1.
```

Code tương ứng:

```text
factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

Base case không chỉ để tránh stack overflow. Nó neo cả definition và correctness proof vào một state đã biết.

## 2. Vì sao recursive call phải tiến về base case?

Ta cần một measure `m(state)` giảm theo một well-founded order.

Với factorial:

```math
m(n)=n.
```

Mỗi call giảm `n` một đơn vị và natural numbers không thể giảm vô hạn dưới 0.

Đây là termination proof.

Nếu recursive function gọi chính nó với cùng hoặc larger measure, termination không được guarantee.

## 3. Mathematical induction mirror recursive construction

Muốn prove property `P(n)` cho mọi natural number:

### Base case

Prove `P(0)` hoặc starting case.

### Inductive step

Assume

```math
P(n)
```

và prove

```math
P(n+1).
```

Logic là: nếu property được truyền từ mỗi state sang next state, và chain bắt đầu đúng, thì toàn chain đúng.

Induction vì vậy không phải một proof trick kỳ lạ; nó là proof form matching recursive structure của natural numbers.

## 4. Strong induction cho divide-and-conquer

Strong induction assume property đúng cho **mọi** smaller sizes:

```math
P(0),P(1),\ldots,P(n-1)
```

để prove `P(n)`.

Điều này natural khi algorithm chia input size `n` thành subproblems như `n/2`, `n/3`, hoặc varying sizes.

Ví dụ merge sort correctness có thể assume recursive calls sort correctly mọi smaller arrays, rồi prove merge step tạo sorted result size `n`.

## 5. Recurrence mô tả cost, count hoặc state relation

Nếu runtime của algorithm size `n` phụ thuộc runtime smaller inputs, ta viết recurrence.

Binary search:

```math
T(n)=T(n/2)+c.
```

Merge sort:

```math
T(n)=2T(n/2)+cn.
```

Fibonacci:

```math
F_n=F_{n-1}+F_{n-2}.
```

Cùng notation “current quantity từ smaller quantities”, nhưng semantics khác nhau: runtime, sequence value hoặc number of configurations.

## 6. Solve recurrence bằng unrolling

Binary search:

```math
T(n)=T(n/2)+c.
```

Substitute repeatedly:

```math
T(n)=T(n/4)+2c
```

```math
=T(n/8)+3c
```

sau `k` levels:

```math
T(n)=T(n/2^k)+kc.
```

Base khi

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

Logarithm xuất hiện từ recursion depth của repeated halving.

## 7. Recursion tree cho merge sort

Merge sort:

```math
T(n)=2T(n/2)+cn.
```

Level 0 work outside recursion: `cn`.

Level 1 có 2 subproblems size `n/2`; total merge work:

```math
2\cdot c(n/2)=cn.
```

Level 2:

```math
4\cdot c(n/4)=cn.
```

Có roughly `\log_2n` levels, mỗi level `O(n)`, nên

```math
T(n)=O(n\log n).
```

Recursion tree là geometric visualization của recurrence.

## 8. Master Theorem là compressed pattern recognition

Recurrences dạng

```math
T(n)=aT(n/b)+f(n)
```

so sánh:

- number subproblems `a`;
- shrink factor `b`;
- combine work `f(n)`.

Quantity

```math
n^{\log_b a}
```

mô tả total leaf-growth scale của recursion tree.

Master Theorem chỉ đóng gói comparison giữa recursive expansion và per-level combine work. Học recursion tree trước giúp theorem không trở thành bảng cases phải thuộc.

## 9. Substitution method: guess rồi prove bằng induction

Giả sử recurrence

```math
T(n)=2T(n/2)+n
```

và ta đoán

```math
T(n)=O(n\log n).
```

Ta có thể assume inductively

```math
T(n/2)\le c\frac n2\log(n/2)
```

rồi substitute để bound `T(n)`.

Đây là connection trực tiếp recurrence ↔ induction: solve asymptotic recurrence bằng proof trên input size.

## 10. Naive Fibonacci và overlapping subproblems

Recurrence mathematical:

```math
F_n=F_{n-1}+F_{n-2}.
```

Naive recursive implementation recomputes same states many times.

Call tree của `F_n` chứa repeated `F_{n-2}`, `F_{n-3}`, ...

Runtime recurrence roughly:

```math
T(n)=T(n-1)+T(n-2)+O(1),
```

leading to exponential growth.

Memoization changes computation graph: mỗi distinct state solved once.

Then number states `O(n)`, so time can become `O(n)`.

Same mathematical recurrence, radically different algorithmic execution.

## 11. Dynamic programming = recurrence + state design + reuse

Dynamic programming không chỉ là “recursion có cache”. Nó cần:

1. define state;
2. derive recurrence/transition;
3. identify base states;
4. choose evaluation order or memoization;
5. sometimes reconstruct choices.

For shortest path in DAG:

```math
D(v)=\min_{u\to v}[D(u)+w(u,v)].
```

Recurrence expresses Bellman optimality: best solution to state uses best solutions to predecessor states.

## 12. State definition quyết định complexity

Một DP có thể chậm không phải vì recurrence sai mà vì state space quá lớn.

If state uses `(i,j,k)`, number states may scale

```math
O(nmk).
```

If a dimension is redundant and can be removed, complexity drops dramatically.

Mathematics of recurrence và modeling of state must be analyzed together.

## 13. Loop invariants là induction trên time

Loop:

```text
for k = 0,1,2,...
```

can be proved with invariant `I(k)`.

### Initialization

Invariant true before first iteration.

### Maintenance

If invariant true before iteration, executing body preserves it.

### Termination

Invariant + loop exit condition imply postcondition.

This is induction on iteration count disguised as program proof.

## 14. Worked proof: binary search correctness

Invariant:

> nếu target tồn tại, nó nằm trong current interval `[low, high]`.

Initialization: interval starts as entire sorted array.

Maintenance: if `a[mid]<target`, sorted order proves positions `≤mid` cannot contain target, so setting

```text
low = mid + 1
```

preserves invariant.

Symmetric case for `a[mid]>target`.

Termination: if `low>high`, interval empty. Invariant implies target does not exist.

Runtime `O(log n)` proof và correctness proof are different arguments.

## 15. Structural induction cho recursive data structures

Trees are not naturally indexed only by integer size. Structural induction mirrors constructors.

For binary tree:

- base: empty/leaf tree;
- inductive step: assume property for left and right subtrees, prove for parent tree.

Use cases:

- AST evaluation;
- compiler transformations;
- JSON/XML trees;
- expression simplification;
- recursive type correctness.

## 16. Induction trên graph DAG order

DAG permits topological order. Many proofs/algorithms can proceed according to that order:

```text
all predecessors solved
→ solve current node
```

This is generalized induction over a partial order rather than simple integer sequence.

Dynamic programming on DAGs follows exactly this structure.

## 17. Termination via ranking functions

To prove loop/recursion terminates, define ranking function into a well-founded set.

Euclidean algorithm:

```math
\gcd(a,b)=\gcd(b,a\bmod b).
```

For `b>0`:

```math
0\le a\bmod b<b.
```

Second argument strictly decreases among nonnegative integers, so algorithm must reach zero.

Termination is a mathematical property, not just “seems to get smaller”.

## 18. Mutual recursion

Functions can recurse through each other:

```text
A → B → A
```

Termination/correctness may need a shared measure across combined states.

Parsers for grammar nonterminals often use mutual recursion.

This illustrates why call graph structure matters beyond single-function view.

## 19. Tail recursion và stack semantics

Tail-recursive call is final operation of function. Languages/runtimes with tail-call optimization can reuse stack frame.

But not every runtime guarantees optimization.

Therefore algorithmic space analysis should consider actual language implementation, not mathematical recurrence alone.

## 20. Recurrence relation as linear dynamical system

Some recurrences can be written matrix form.

Fibonacci:

```math
\begin{bmatrix}
F_{n+1}\\F_n
\end{bmatrix}
=
\begin{bmatrix}
1&1\\1&0
\end{bmatrix}
\begin{bmatrix}
F_n\\F_{n-1}
\end{bmatrix}.
```

Then

```math
v_n=A^nv_0.
```

Eigenvalues explain growth rate; fast exponentiation computes `A^n` in `O(log n)` matrix multiplications.

This connects discrete recurrence to linear algebra and dynamic systems.

## 21. Generating-function viewpoint

Sequence recurrence can be encoded into power series

```math
G(x)=\sum_{n\ge0}a_nx^n.
```

Recurrence relations become algebraic equations on `G(x)`.

This transforms a discrete recursive relation into function algebra — another example of changing representation to solve structure.

Full generating-function theory is optional in current scope, but the connection explains why recurrence analysis touches algebra and complex analysis.

## 22. Physics connection: discrete time evolution

A recurrence like

```math
x_{k+1}=Ax_k
```

is a discrete dynamical system.

Stability depends on eigenvalues of `A`:

```math
|\lambda|<1
```

for modes that decay.

Numerical ODE solvers also create recurrences from continuous equations. Thus recursion/recurrence is not only CS; it is a language for discrete dynamics.

## 23. Finance connection

Compound growth:

```math
V_{t+1}=(1+r_t)V_t+C_t
```

is recurrence.

Loan amortization, portfolio wealth updates and dynamic programming for investment decisions all use state transitions over time.

Bellman equations generalize recurrence to optimal sequential decision-making.

## 24. Common failure modes

### Missing base case

Definition/computation has no anchor.

### Base exists but measure does not decrease

Still may not terminate.

### Correct recurrence, inefficient evaluation

Naive Fibonacci demonstrates exponential recomputation.

### Correct asymptotic recurrence, wrong correctness reasoning

Runtime analysis does not prove returned answer is correct.

### State too large

Dynamic programming can still be infeasible due to curse of dimensionality.

## Mental Model

> Recursion decomposes computation, recurrence records the dependency between sizes/states, and induction proves that dependency is valid everywhere. Dynamic programming adds one more idea: if many paths reach the same state, solve that state once and reuse it.

## Common Misconceptions

**Recursive code is inherently slow.** No; repeated work and stack/runtime behavior determine cost.

**Memoization changes the mathematical recurrence.** Usually no; it changes evaluation strategy and computation graph.

**Base case is only a programming detail.** It is also the logical anchor of definition/proof.

**Finding a recurrence automatically gives complexity.** No; recurrence still needs solution/bounds and actual cost model.
