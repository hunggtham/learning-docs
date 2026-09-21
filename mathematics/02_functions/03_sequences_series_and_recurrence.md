# Dãy, chuỗi và recurrence: toán học của trạng thái theo bước rời rạc

Dãy số (sequence / 수열) là function có domain rời rạc, thường là

```math
n=0,1,2,\ldots
```

Thay vì hỏi “output thay đổi thế nào theo real input liên tục?”, sequence hỏi “state ở step `n` là gì?”. Đây là ngôn ngữ tự nhiên của monthly balance, iteration, population generations, algorithm runtime và discrete-time systems.

Ba khái niệm cần phân biệt ngay từ đầu:

```text
sequence   → values theo từng step
recurrence → rule chuyển từ state cũ sang state mới
series     → accumulation của sequence terms
```

## 1. Sequence là function trên discrete index

Một sequence có thể viết

```math
a_0,a_1,a_2,\ldots
```

hoặc như function:

```math
a:\mathbb N\to\mathbb R.
```

Ví dụ:

```math
a_n=2n+1.
```

Các terms:

```text
1,3,5,7,...
```

Cách nhìn function giúp sequence nối tự nhiên với limits, asymptotics và algorithms.

## 2. Explicit formula và recurrence encode information khác nhau

Explicit form:

```math
a_n=2n+1
```

cho phép jump trực tiếp tới term `n`.

Recursive form:

```math
a_{n+1}=a_n+2,
\qquad a_0=1
```

nhấn mạnh transition rule.

Hai representations có thể mô tả cùng sequence nhưng phục vụ questions khác nhau.

Explicit formula phù hợp random access. Recurrence phù hợp process evolution.

Trong computing, đây gần distinction giữa:

```text
closed-form evaluation
vs
state iteration
```

## 3. Arithmetic sequence = constant additive change

Nếu difference constant `d`:

```math
a_{n+1}-a_n=d,
```

thì

```math
a_n=a_0+nd.
```

Đây là discrete counterpart của linear function.

Mental connection:

```text
constant discrete difference → linear sequence
constant derivative → linear continuous function
```

Finite difference đóng vai trò gần giống derivative trong discrete setting.

## 4. Arithmetic series và vì sao sum scale như n²

Tổng:

```math
S_n=1+2+\cdots+n.
```

Pair first + last:

```text
1+n
2+(n-1)
3+(n-2)
...
```

mỗi pair sum `n+1`.

Kết quả:

```math
S_n=\frac{n(n+1)}2.
```

Nếu term grow như `O(n)`, cumulative sum thường grow như `O(n^2)`.

Đây là intuition quan trọng trong complexity analysis: accumulation tăng order growth lên một bậc trong nhiều trường hợp polynomial.

## 5. Geometric sequence = constant multiplicative change

Nếu ratio constant `r`:

```math
a_{n+1}=ra_n,
```

thì

```math
a_n=a_0r^n.
```

Đây là discrete exponential growth/decay.

Nếu `|r|<1`, magnitude decay.

Nếu `r>1`, growth exponential.

Nếu `r<0`, signs alternate.

## 6. Derive finite geometric sum thay vì học thuộc

Cho

```math
S_n=a_0+a_0r+\cdots+a_0r^{n-1}.
```

Nhân `r`:

```math
rS_n=a_0r+a_0r^2+\cdots+a_0r^n.
```

Subtract:

```math
S_n-rS_n=a_0-a_0r^n.
```

Do đó

```math
S_n=a_0\frac{1-r^n}{1-r},
\qquad r\ne1.
```

Formula xuất hiện vì shift-by-one làm almost all terms cancel.

Đây là một proof pattern rất phổ biến: transform expression để structure cancellation lộ ra.

## 7. Infinite geometric series là limit của partial sums

Ta không “cộng xong vô hạn terms”. Ta định nghĩa

```math
\sum_{k=0}^{\infty}a_0r^k
=
\lim_{n\to\infty}S_n.
```

Nếu `|r|<1`:

```math
r^n\to0
```

nên

```math
\sum_{k=0}^{\infty}a_0r^k
=
\frac{a_0}{1-r}.
```

Condition `|r|<1` là essential assumption, không phải decoration.

## 8. Recurrence là equation của state transition

General first-order recurrence:

```math
a_{n+1}=F(a_n,n).
```

Nếu `F` không phụ thuộc explicit vào `n`:

```math
a_{n+1}=F(a_n),
```

ta có discrete dynamical system.

Fixed point `a_*` thỏa

```math
F(a_*)=a_*.
```

Stability hỏi nếu bắt đầu gần `a_*`, iterations có quay về đó không.

Đây là bridge sang numerical methods, optimization và control.

## 9. Linear first-order recurrence

Xét

```math
a_{n+1}=ra_n+b.
```

Fixed point nếu `r\ne1`:

```math
a_*=
\frac{b}{1-r}.
```

Subtract fixed point:

```math
u_n=a_n-a_*.
```

thì

```math
u_{n+1}=ru_n.
```

Do đó

```math
u_n=r^nu_0
```

và

```math
a_n=a_*+r^n(a_0-a_*).
```

Nếu `|r|<1`, state converge tới fixed point.

Nếu `|r|>1`, deviations grow.

Đây là một example quan trọng: đổi variables có thể biến recurrence có constant forcing thành geometric recurrence đơn giản.

## 10. Finance example: balance recurrence

Nếu account balance tăng rate `r` mỗi period và thêm contribution `c` cuối period:

```math
B_{n+1}=(1+r)B_n+c.
```

Đây là affine recurrence.

Repeated substitution tạo:

```math
B_n=(1+r)^nB_0
+c\sum_{k=0}^{n-1}(1+r)^k.
```

Geometric sum cho closed form.

Compound interest và annuity formulas thực chất là recurrence + geometric series.

## 11. Fibonacci: recurrence order 2

Fibonacci:

```math
F_{n+1}=F_n+F_{n-1}.
```

State ở step `n+1` cần hai previous values.

Ta gom thành vector state:

```math
\begin{bmatrix}
F_{n+1}\\
F_n
\end{bmatrix}
=
\begin{bmatrix}
1&1\\
1&0
\end{bmatrix}
\begin{bmatrix}
F_n\\
F_{n-1}
\end{bmatrix}.
```

Sau nhiều steps:

```math
x_n=A^nx_0.
```

Eigenvalues của `A` giải thích long-run growth rate.

Đây là connection sâu giữa recurrence và linear algebra.

## 12. Characteristic equation intuition

Với homogeneous recurrence:

```math
a_{n+2}=pa_{n+1}+qa_n,
```

thử solution exponential:

```math
a_n=r^n.
```

Substitute:

```math
r^{n+2}=pr^{n+1}+qr^n.
```

Nếu `r\ne0`, divide `r^n`:

```math
r^2-pr-q=0.
```

Roots của characteristic polynomial quyết định modes của solution.

Đây hoàn toàn analogous với solving linear differential equations bằng `e^{\lambda t}`.

## 13. Recurrence trong algorithm analysis

Binary search:

```math
T(n)=T(n/2)+c.
```

Mỗi step halve input, nên depth gần

```math
\log_2n.
```

Merge sort:

```math
T(n)=2T(n/2)+cn.
```

Recursion tree có `\log n` levels và mỗi level tổng work `O(n)`:

```math
T(n)=O(n\log n).
```

Runtime recurrence không phải code recursion itself; nó là mathematical model của work dependency.

## 14. Memoization thay computation graph, không thay recurrence definition

Naive Fibonacci recursion recompute same states nhiều lần.

Recurrence:

```math
F_n=F_{n-1}+F_{n-2}
```

không sai. Problem nằm ở evaluation strategy.

Memoization lưu solved states, biến computation từ exponential call tree thành roughly linear number of distinct states.

Dynamic programming = recurrence + systematic state reuse/order.

## 15. Convergence của sequence

`a_n` converge tới `L` nếu:

```math
\forall\varepsilon>0,
\exists N
\text{ sao cho }
n\ge N
\Rightarrow
|a_n-L|<\varepsilon.
```

Intuition: sau một index đủ lớn, mọi terms còn lại nằm trong bất kỳ tolerance band nào quanh `L`.

Ví dụ:

```math
a_n=\frac1n\to0.
```

Sequence convergence là foundation cho series, iterative numerical methods và stochastic limit laws.

## 16. Bounded không imply convergent

Sequence

```math
a_n=(-1)^n
```

bounded trong `[-1,1]` nhưng không converge vì oscillates giữa ±1.

Monotone bounded theorem nói nếu sequence monotone và bounded phù hợp thì converge.

Assumptions matter: boundedness alone chưa đủ.

## 17. Series là accumulation, không phải sequence

Cho sequence `a_n`, series là

```math
\sum_{n=1}^{\infty}a_n.
```

Ta define partial sums:

```math
S_N=\sum_{n=1}^{N}a_n.
```

Series converge iff sequence `S_N` converge.

Vì vậy series convergence là sequence convergence của accumulated state.

## 18. Vì sao a_n → 0 chưa đủ?

Nếu series converge, terms phải tiến về zero:

```math
a_n\to0.
```

Nhưng converse sai.

Harmonic series:

```math
\sum_{n=1}^{\infty}\frac1n
```

diverges.

Grouping:

```text
1
+ 1/2
+ (1/3+1/4)
+ (1/5+...+1/8)
+ ...
```

mỗi block sau có sum ít nhất khoảng `1/2`, nên total không bounded.

Terms giảm nhưng không đủ nhanh.

## 19. Comparison test là asymptotic reasoning

Nếu

```math
0\le a_n\le b_n
```

và

```math
\sum b_n
```

converges, thì `\sum a_n` converges.

Nếu `a_n\ge b_n\ge0` và `\sum b_n` diverges, thì `\sum a_n` diverges.

Ta không cần exact sum; chỉ cần compare accumulation rate.

## 20. Ratio test nhìn multiplicative shrink

```math
L=
\lim_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|.
```

Nếu `L<1`, terms eventually shrink gần geometric factor dưới 1, nên absolute convergence.

Nếu `L>1`, terms không thể tiến về zero phù hợp.

Nếu `L=1`, test inconclusive.

Test không phải magic rule; nó compare series với geometric behavior.

## 21. Generating-function intuition

Một sequence có thể encode thành power series:

```math
G(x)=\sum_{n=0}^{\infty}a_nx^n.
```

Recurrence relations có thể biến thành algebraic equations cho `G(x)`.

Generating functions là bridge từ discrete sequences sang algebra/complex analysis/combinatorics.

Không cần đi sâu ở chapter này; important idea là representation change có thể turn recurrence into algebra.

## 22. Difference equations và control

Continuous systems:

```math
\frac{dx}{dt}=Ax+Bu.
```

Discrete-time systems:

```math
x_{k+1}=Ax_k+Bu_k.
```

Matrix powers `A^k` quyết định state evolution.

Eigenvalues inside unit circle thường liên quan stability của discrete linear system, analogous real-part-negative eigenvalues trong continuous systems.

## 23. Worked example: iterative approximation

Newton method:

```math
x_{n+1}
=
x_n-
\frac{f(x_n)}{f'(x_n)}.
```

Đây là recurrence.

Convergence analysis hỏi error

```math
e_n=x_n-x_*
```

biến đổi thế nào từ step này sang step khác.

Nếu near root:

```math
|e_{n+1}|\approx C|e_n|^2,
```

ta nói quadratic convergence.

Numerical algorithms vì vậy là dynamical systems trên approximation state.

## 24. Common modeling patterns

Additive update:

```math
x_{n+1}=x_n+c
```

→ linear/arithmetic growth.

Multiplicative update:

```math
x_{n+1}=rx_n
```

→ exponential/geometric growth.

Feedback update:

```math
x_{n+1}=F(x_n)
```

→ nonlinear discrete dynamics.

Accumulation:

```math
S_{n+1}=S_n+a_{n+1}
```

→ series/ running totals.

Nhận ra pattern quan trọng hơn nhớ từng formula riêng.

## Knowledge Connection

Sequence/recurrence nối:

```text
functions on integers
→ finite differences
→ series accumulation
→ limits
→ algorithm recurrences
→ dynamic programming
→ matrix powers/eigenvalues
→ numerical iteration
→ finance compounding
→ discrete control
```

## Mental Model

> Sequence là state theo discrete time. Recurrence là transition law. Series là accumulated state. Khi rule additive ta thấy linear behavior; khi multiplicative ta thấy exponential behavior; khi rule feedback nonlinear, stability và fixed points trở thành câu hỏi trung tâm.

## Common Misconceptions

Recursive definition không đồng nghĩa recursive implementation là tốt nhất. `a_n\to0` không đủ để `\sum a_n` converge. Bounded sequence chưa chắc converge. Infinite series là limit của partial sums, không phải hành động “thực hiện vô hạn phép cộng”. Closed form không phải lúc nào cũng computationally superior; numerical stability và cost vẫn matter.