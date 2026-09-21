# Chuỗi vô hạn, power series và convergence: khi accumulation có một giới hạn hữu hạn

Một chuỗi vô hạn (infinite series / 무한급수) không phải “cộng xong vô hạn số”. Nó là một statement về **limit của các tổng hữu hạn**.

Nếu

```math
S_N=\sum_{n=1}^{N}a_n,
```

thì

```math
\sum_{n=1}^{\infty}a_n=S
```

nghĩa là

```math
\lim_{N\to\infty}S_N=S.
```

Do đó mọi reasoning về infinite series cuối cùng đều quay về ba câu hỏi:

```text
partial sums có bị bounded không?
partial sums có settle về một limit không?
tail còn lại sau N terms có nhỏ đến đâu?
```

## 1. Sequence và series khác nhau ở object đang hội tụ

Sequence:

```math
a_1,a_2,a_3,\ldots
```

Series:

```math
a_1+a_2+a_3+\cdots
```

Series convergence thực chất là convergence của sequence partial sums:

```math
S_1,S_2,S_3,\ldots
```

Đây là reason condition

```math
a_n\to0
```

chỉ là necessary, không sufficient.

Terms nhỏ dần không guarantee cumulative sum bounded.

## 2. Geometric series là prototype của convergence

Cho

```math
S_N=1+r+r^2+\cdots+r^N.
```

Nhân `r`:

```math
rS_N=r+r^2+\cdots+r^{N+1}.
```

Subtract:

```math
(1-r)S_N=1-r^{N+1}.
```

Do đó

```math
S_N=\frac{1-r^{N+1}}{1-r}.
```

Nếu `|r|<1`:

```math
r^{N+1}\to0,
```

nên

```math
\sum_{n=0}^{\infty}r^n
=\frac1{1-r}.
```

Nếu `|r|\ge1`, terms không decay phù hợp và series không converge theo ordinary sense.

Geometric series là benchmark vì nhiều convergence tests hỏi: tail có behave giống geometric decay không?

## 3. Infinite series là approximation + error budget

Trong computation ta chỉ dùng finite `N`:

```math
S_N=\sum_{n=0}^{N}a_n.
```

True infinite sum nếu tồn tại:

```math
S=S_N+R_N
```

với remainder/tail:

```math
R_N=\sum_{n=N+1}^{\infty}a_n.
```

Một convergence theorem hữu ích không chỉ nói “converges”, mà nên giúp bound `R_N`.

Với geometric series:

```math
|R_N|
\le
\frac{|r|^{N+1}}{1-|r|}.
```

Convergence vì vậy nối pure analysis với numerical error control.

## 4. Vì sao a_n → 0 chưa đủ?

Harmonic series:

```math
\sum_{n=1}^{\infty}\frac1n
```

diverges dù

```math
\frac1n\to0.
```

Grouping proof:

```text
1
+ 1/2
+ (1/3+1/4)
+ (1/5+...+1/8)
+ ...
```

Mỗi block sau block đầu có sum ít nhất `1/2`.

Vì partial sums tăng thêm ít nhất một amount cố định qua infinitely many blocks, chúng không bounded.

Key lesson:

> local smallness của term không quyết định global accumulation.

## 5. p-series cho benchmark polynomial decay

Series

```math
\sum_{n=1}^{\infty}\frac1{n^p}
```

converges iff

```math
p>1.
```

Nếu `p=1`, harmonic series diverges.

Nếu `p>1`, decay đủ nhanh.

Nếu `p<1`, decay còn chậm hơn harmonic.

p-series là benchmark cho algebraic/polynomial tail, giống geometric series là benchmark cho exponential tail.

## 6. Integral test nối discrete sum với continuous area

Nếu `f(x)` positive, continuous, decreasing và

```math
a_n=f(n),
```

thì behavior của

```math
\sum_{n=1}^{\infty}a_n
```

liên hệ với

```math
\int_1^{\infty}f(x)\,dx.
```

Intuition: rectangles dưới/trên curve bound lẫn nhau.

Với

```math
f(x)=x^{-p},
```

integral converges iff `p>1`, cho p-series criterion.

Đây là một example quan trọng về knowledge connection:

```text
discrete accumulation ↔ continuous accumulation
```

## 7. Comparison test là asymptotic domination

Nếu eventually

```math
0\le a_n\le b_n
```

và

```math
\sum b_n
```

converges, thì

```math
\sum a_n
```

converges.

Ngược lại nếu

```math
a_n\ge b_n\ge0
```

và `\sum b_n` diverges, thì `\sum a_n` diverges.

Comparison không cần exact sum. Nó chỉ cần relative tail size.

## 8. Limit comparison tập trung vào asymptotic ratio

Nếu

```math
\lim_{n\to\infty}\frac{a_n}{b_n}=c,
\qquad 0<c<\infty,
```

với positive terms, thì hai series có cùng convergence behavior.

Reason: eventually chúng chỉ khác nhau bởi constant factors.

Đây là series version của asymptotic equivalence.

## 9. Ratio test nhìn geometric shrink rate

Cho

```math
L=
\lim_{n\to\infty}
\left|
\frac{a_{n+1}}{a_n}
\right|.
```

Nếu `L<1`, tail behaves roughly geometric → absolute convergence.

Nếu `L>1`, terms không tiến về zero đúng cách → divergence.

Nếu `L=1`, test inconclusive.

Ratio test đặc biệt mạnh khi factorial/exponential terms xuất hiện.

## 10. Root test nhìn exponential scale trực tiếp

Cho

```math
L=
\limsup_{n\to\infty}|a_n|^{1/n}.
```

Nếu `L<1`, absolute convergence.

Nếu `L>1`, divergence.

Root test hữu ích khi term có structure `(... )^n`.

Ratio và root tests đều hỏi cùng một deep question:

> asymptotic multiplicative decay có factor dưới 1 không?

## 11. Alternating series và cancellation

Series alternating:

```math
\sum_{n=1}^{\infty}(-1)^{n+1}b_n,
\qquad b_n\ge0.
```

Nếu `b_n` decrease về 0, alternating series test cho convergence.

Reason trực giác: partial sums overshoot/undershoot limit với oscillation ngày càng nhỏ.

Remainder bound:

```math
|R_N|\le b_{N+1}.
```

Đây là một trong những error bounds rất practical.

## 12. Absolute vs conditional convergence

Absolute convergence:

```math
\sum|a_n|<\infty.
```

Thì `\sum a_n` converge.

Conditional convergence xảy ra khi `\sum a_n` converge nhưng `\sum|a_n|` diverges.

Alternating harmonic:

```math
1-\frac12+\frac13-\frac14+\cdots
```

là example.

Absolute convergence mạnh hơn vì rearrangement behavior ổn định hơn.

## 13. Rearrangement cho thấy infinite sums khác finite sums

Finite addition commutative/associative không gây vấn đề.

Nhưng với conditionally convergent series, rearranging terms có thể đổi sum hoặc làm diverge (Riemann rearrangement phenomenon).

Điều này không “phá” arithmetic; nó cho thấy limit process thêm assumptions vào phép cộng vô hạn.

## 14. Cauchy criterion nhìn tail thay vì unknown limit

Series converge iff:

```math
\forall\varepsilon>0,
\exists N
```

sao cho với mọi `m>n\ge N`:

```math
\left|
\sum_{k=n+1}^{m}a_k
\right|<\varepsilon.
```

Interpretation:

> sufficiently far out, every finite chunk của tail phải có total contribution arbitrarily small.

Cauchy criterion rất quan trọng vì không cần biết limit `S` trước.

## 15. Power series là polynomial với infinitely many degrees

Power series quanh center `a`:

```math
\sum_{n=0}^{\infty}c_n(x-a)^n.
```

Nó không chỉ là một series number; convergence phụ thuộc `x`.

Thường tồn tại radius `R` sao cho:

```text
|x-a| < R  → absolute convergence
|x-a| > R  → divergence
|x-a| = R  → phải xét riêng
```

## 16. Radius of convergence đến từ coefficient growth

Cauchy–Hadamard formula:

```math
\frac1R
=
\limsup_{n\to\infty}|c_n|^{1/n}.
```

Trong many textbook cases, ratio test cho:

```math
R=
\lim_{n\to\infty}
\left|
\frac{c_n}{c_{n+1}}
\right|
```

nếu limit phù hợp tồn tại.

Radius encode competition giữa coefficient growth và power `(x-a)^n`.

## 17. Endpoint behavior cần check riêng

Ví dụ power series có `R=1`.

Tại `x=1`, series có thể converge.

Tại `x=-1`, có thể diverge hoặc converge conditionally.

Radius chỉ quyết định inside/outside; boundary thường cần test riêng.

Đây là common exam trap nhưng sâu hơn là boundary thường có qualitatively different cancellation.

## 18. Term-by-term differentiation/integration

Inside radius of convergence, power series behave rất tốt.

Nếu

```math
f(x)=\sum_{n=0}^{\infty}c_n(x-a)^n,
```

thì trong interior:

```math
f'(x)=
\sum_{n=1}^{\infty}
nc_n(x-a)^{n-1}
```

và

```math
\int f(x)dx
=
C+
\sum_{n=0}^{\infty}
\frac{c_n}{n+1}(x-a)^{n+1}.
```

Radius remains the same, though endpoints may change behavior.

## 19. Geometric series như generator

Identity:

```math
\frac1{1-x}
=
1+x+x^2+x^3+\cdots,
\qquad |x|<1.
```

Differentiate:

```math
\frac1{(1-x)^2}
=
1+2x+3x^2+\cdots.
```

Integrate:

```math
-\ln(1-x)
=
x+\frac{x^2}{2}+\frac{x^3}{3}+\cdots.
```

Một simple series identity có thể generate cả family identities.

## 20. Series solution của differential equations

Nếu closed-form solution khó, assume

```math
y(x)=\sum_{n=0}^{\infty}a_nx^n.
```

Substitute vào ODE để derive recurrence cho coefficients `a_n`.

Đây là bridge:

```text
differential equation
→ power series
→ coefficient recurrence
```

Special functions thường xuất hiện theo cách này.

## 21. Series trong numerical computing

Máy tính luôn truncate:

```math
f(x)\approx\sum_{n=0}^{N}a_n.
```

Practical accuracy phụ thuộc:

- truncation error;
- rounding error;
- cancellation;
- evaluation order;
- distance tới convergence boundary.

Một mathematically convergent series có thể là numerically poor algorithm nếu convergence quá chậm.

## 22. Slow convergence vs acceleration

Harmonic-like tails hoặc `r` gần 1 làm convergence rất chậm.

Nếu geometric ratio `r=0.999`, cần rất nhiều terms.

Production numerical methods thường dùng transformed approximations, rational approximants hoặc convergence acceleration thay vì raw summation.

Mathematical convergence không đồng nghĩa computational efficiency.

## 23. Probability connection

Expected value của discrete random variable là series:

```math
E[X]=\sum_x xP(X=x).
```

Interchanging sums/limits/expectations cần convergence conditions.

Absolute convergence/integrability giúp justify manipulations mà finite sums cho phép tự do hơn.

## 24. Finance connection: present value as geometric-like series

Perpetuity payment `C` với discount rate `r>0`:

```math
PV
=
\sum_{n=1}^{\infty}
\frac{C}{(1+r)^n}.
```

Đây là geometric series với ratio

```math
\frac1{1+r}<1.
```

Do đó

```math
PV=\frac Cr.
```

Formula finance nổi tiếng chỉ là geometric-series convergence dưới assumptions constant payment/rate.

## 25. CS connection: geometric work bounds

Dynamic array doubling costs:

```text
1 + 2 + 4 + ... + n
```

là finite geometric sum `O(n)`.

Reverse-looking shrink processes:

```text
n + n/2 + n/4 + ...
```

cũng bounded bởi `2n`.

Geometric series là foundation của many amortized/divide-and-conquer arguments.

## 26. Worked example: error target

Approximate

```math
\frac1{1-r}
```

bằng first `N+1` geometric terms.

Tail:

```math
|R_N|
=
\frac{|r|^{N+1}}{1-|r|}.
```

Muốn error < `\varepsilon`:

```math
\frac{|r|^{N+1}}{1-|r|}<\varepsilon.
```

Taking logs cho minimum `N`.

Series convergence biến thành engineering question: bao nhiêu terms đủ?

## Knowledge Connection

```text
sequence limits
→ partial sums
→ convergence tests
→ error bounds
→ power series
→ Taylor series
→ ODE series solutions
→ numerical approximation
→ probability expectations
→ finance discounting
→ algorithmic geometric bounds
```

## Mental Model

> Infinite series là một **accumulation process controlled by a limit**. Convergence không hỏi từng term có nhỏ không; nó hỏi **remaining tail có thể làm arbitrarily small không**. Power series thêm một variable vào process này, biến convergence thành một property của region quanh center.

## Common Misconceptions

`a_n\to0` không đủ cho series convergence. “Convergent” không nghĩa fast enough for computation. Absolute và conditional convergence không interchangeable. Power series không automatically valid cho mọi `x`. Endpoints phải được check riêng. Rearrangement của conditionally convergent series có thể đổi result. Một theorem cho convergence mà không có useful error bound đôi khi chưa đủ cho numerical use.