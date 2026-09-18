# Dãy, chuỗi và recurrence

Dãy số (Sequence / 수열) là function có domain thường là integers `n=0,1,2,...`. Điều này nối functions liên tục với discrete processes như monthly balance, algorithm iteration và population generation.

## Explicit và recursive definitions

Dãy có thể explicit:

```math
a_n=2n+1
```

hoặc recursive:

```math
a_{n+1}=a_n+2,\qquad a_0=1.
```

Hai definitions mô tả cùng arithmetic sequence.

Recursive form nhấn mạnh transition từ state hiện tại sang state tiếp theo, rất gần loop/recursion trong computing.

## Arithmetic sequence

Nếu difference constant `d`:

```math
a_n=a_0+nd.
```

Sum của first `n` terms có quadratic scaling vì ta cộng sequence tăng linear.

Với `1+2+...+n`:

```math
S_n=\frac{n(n+1)}2.
```

Growth order `n^2` phản ánh accumulated linear growth.

## Geometric sequence

Nếu ratio constant `r`:

```math
a_n=a_0r^n.
```

Finite geometric sum:

```math
S_n=a_0\frac{1-r^n}{1-r},\qquad r\ne1.
```

Derivation: đặt

```math
S=a_0+a_0r+\cdots+a_0r^{n-1}.
```

Nhân `r`:

```math
rS=a_0r+\cdots+a_0r^n.
```

Trừ:

```math
S-rS=a_0-a_0r^n
```

nên formula trên.

## Infinite geometric series

Nếu `|r|<1`, thì `r^n→0`, nên

```math
\sum_{k=0}^\infty a_0r^k=\frac{a_0}{1-r}.
```

“Infinite sum” được định nghĩa qua limit của partial sums, không phải thực hiện vô hạn additions trong finite time.

## Recurrence trong algorithms

Merge sort runtime thường model:

```math
T(n)=2T(n/2)+cn.
```

Hai subproblems size `n/2`, cộng linear merge work. Recurrence tree cho mỗi level total work roughly `cn`; có `log_2n` levels, nên

```math
T(n)=O(n\log n).
```

Sequence/recurrence vì thế là cầu giữa school mathematics và algorithm complexity.

## Fibonacci

```math
F_{n+1}=F_n+F_{n-1}
```

cho state phụ thuộc hai previous states. Có thể represent bằng matrix:

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
\end{bmatrix}
```

Repeated recurrence trở thành matrix powers, nối discrete sequences với linear algebra và eigenvalues.

## Convergence

Sequence `a_n` converge tới `L` nếu terms có thể được làm tùy ý gần `L` khi `n` đủ lớn.

Ví dụ

```math
a_n=\frac1n\to0.
```

Convergence là nền của limits, infinite series và iterative algorithms.

## Mental Model

> Sequence là function theo discrete step; recurrence mô tả transition rule; series là accumulation của sequence. Linear step tạo arithmetic behavior, multiplicative step tạo exponential behavior, và recursive decomposition thường tạo complexity laws.

## Common Misconceptions

Dãy có terms tiến về 0 chưa đảm bảo infinite series converge; harmonic series `Σ1/n` diverges. Recursive definition không nhất thiết computationally efficient nếu implement naive. Infinite series là limit của partial sums, không phải một “phép cộng xong vô hạn số”.

## Convergence tests: vì sao cần nhiều test?

Điều kiện `a_n\to0` là necessary nhưng không sufficient cho

```math
\sum a_n
```

converge. Harmonic series

```math
\sum_{n=1}^{\infty}\frac1n
```

diverges dù terms tiến về zero. Intuition: terms nhỏ dần nhưng không nhỏ đủ nhanh để total accumulation bị bounded.

Với positive terms, comparison test hỏi series có bị chặn bởi một known convergent series hay dominate một known divergent series không. Ratio test xem asymptotic multiplicative shrink:

```math
L=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|.
```

Nếu `L<1`, terms eventually shrink gần geometric nên series converge absolutely. Nếu `L>1`, terms không shrink đủ. Nếu `L=1`, test không quyết định. Mỗi test là một cách so behavior với structure đã hiểu, không phải collection phép thuật.
