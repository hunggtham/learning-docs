# Chuỗi vô hạn, power series và convergence

Một chuỗi vô hạn (Infinite Series / 무한급수) không phải hành động “cộng xong vô hạn số”. Nó là giới hạn của một sequence các tổng hữu hạn. Sự khác biệt này quyết định toàn bộ logic của infinite series.

## Từ sequence sang series

Cho sequence `(a_n)`. Định nghĩa partial sum:

```math
S_N=\sum_{n=1}^{N}a_n.
```

Infinite series

```math
\sum_{n=1}^{\infty}a_n
```

được gọi là hội tụ (Convergent / 수렴) tới `S` nếu

```math
\lim_{N\to\infty}S_N=S.
```

Nếu limit không tồn tại hoặc không hữu hạn, series phân kỳ (Divergent / 발산).

## Geometric series từ repeated scaling

Xét

```math
1+r+r^2+\cdots+r^N.
```

Gọi sum là `S_N`. Nhân với `r`:

```math
rS_N=r+r^2+\cdots+r^{N+1}.
```

Trừ:

```math
S_N-rS_N=1-r^{N+1}.
```

Do đó

```math
S_N=\frac{1-r^{N+1}}{1-r}.
```

Nếu `|r|<1`, `r^{N+1}\to0`, nên

```math
\sum_{n=0}^{\infty}r^n=\frac1{1-r}.
```

Nếu `|r|\ge1`, terms không decay đủ để geometric series converge theo cách này.

## Điều kiện a_n→0 chưa đủ

Nếu series converge thì necessarily

```math
a_n\to0.
```

Nhưng converse sai. Harmonic series

```math
\sum_{n=1}^{\infty}\frac1n
```

diverges dù `1/n→0`.

Một argument grouping:

```text
1 + 1/2 + (1/3+1/4) + (1/5+...+1/8) + ...
```

Mỗi block sau có `2^{k-1}` terms, mỗi term ít nhất khoảng `1/2^k`, nên mỗi block contribution ít nhất khoảng `1/2`. Accumulation không bounded.

Lesson: individual contributions tiến về zero không nói total accumulated contribution finite.

## Absolute và conditional convergence

Series absolutely convergent nếu

```math
\sum |a_n|
```

converges. Absolute convergence mạnh hơn và cho phép rearrangement an toàn hơn.

Alternating harmonic series

```math
1-\frac12+\frac13-\frac14+\cdots
```

converges nhưng không absolutely, nên gọi conditionally convergent. Rearranging conditionally convergent series có thể thay sum; infinite addition khác finite addition ở đây.

## Comparison thinking

Nhiều convergence tests chỉ formalize một mental model: compare tail behavior với series đã biết.

Nếu positive `a_n` eventually smaller than a known convergent `b_n`, `Σa_n` cũng converge. Nếu `a_n` larger than a divergent benchmark, nó diverge.

`p`-series:

```math
\sum_{n=1}^{\infty}\frac1{n^p}
```

converges iff `p>1`.

## Ratio test và exponential decay

Nếu

```math
L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|,
```

và `L<1`, terms asymptotically shrink gần geometric, nên series converges absolutely. Nếu `L>1`, terms không decay về zero thích hợp. Nếu `L=1`, test không quyết định.

Again, test dựa trên comparison với multiplicative/geometric behavior.

## Power series

Power series quanh center `a`:

```math
\sum_{n=0}^{\infty}c_n(x-a)^n.
```

Nó là một infinite polynomial-like representation. Thường tồn tại radius of convergence `R` sao cho series converges khi

```math
|x-a|<R
```

và diverges khi `|x-a|>R`; endpoints cần xét riêng.

Trong interior convergence interval, power series có thể differentiated/integrated term-by-term dưới standard conditions.

## Geometric series như generator của identities

Từ

```math
\frac1{1-x}=1+x+x^2+x^3+\cdots,
\qquad |x|<1,
```

differentiate:

```math
\frac1{(1-x)^2}
=
1+2x+3x^2+4x^3+\cdots.
```

Một simple closed form chứa information về whole infinite coefficient sequence. Generating functions trong combinatorics/algorithms phát triển idea này sâu hơn.

## Numerical truncation

Máy tính không sum infinity; nó truncate tại finite `N`. Nếu có bound cho tail

```math
R_N=\sum_{n=N+1}^{\infty}a_n,
```

ta biết approximation tốt tới mức nào.

Với geometric series `|r|<1`, tail magnitude:

```math
|R_N|
\le
\frac{|r|^{N+1}}{1-|r|}.
```

Đây là bridge từ pure convergence sang error control.

## Knowledge Connection

Series nối discrete accumulation với calculus. Taylor series represent functions bằng power series; Fourier series represent signals bằng sinusoidal modes; probability dùng sums/integrals của distributions; numerical algorithms dùng iterative series approximations.

Trong CS, amortized/geometric arguments thường dựa trên facts như

```math
1+\frac12+\frac14+\cdots=2.
```

Ví dụ dynamic arrays resize exponentially: dù một resize copy nhiều elements, tổng copy work across growth stages là geometric và vẫn linear overall.

## Mental Model

> Infinite series là limit của partial sums. Câu hỏi không phải “terms có nhỏ không?” mà là “total accumulation có settle về một finite value không?”. Convergence tests chỉ là các cách so tail với behavior đã hiểu.

## Common Misconceptions

`a_n→0` không đủ để `Σa_n` converge. Infinite sums không luôn có thể reorder như finite sums. Power series không necessarily valid cho mọi `x`; radius/interval of convergence là một phần của representation.
