# Đa thức và phân tích nhân tử

Đa thức (Polynomial / 다항식) là tổng hữu hạn các powers không âm nguyên của variable với coefficients:

```math
P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0.
```

Polynomial quan trọng vì nó dễ tính, dễ đạo hàm/tích phân và có thể approximate nhiều functions locally.

## Degree

Bậc (Degree / 차수) là highest exponent có coefficient khác zero.

```math
3x^4-2x+1
```

có degree 4.

Degree phản ánh growth ở large `|x|`: leading term thường dominate.

## Roots

Root/zero là `r` sao cho

```math
P(r)=0.
```

Factor theorem nói:

```math
P(r)=0
\iff
(x-r)\text{ là factor của }P(x).
```

Ví dụ

```math
x^2-5x+6
```

có roots 2 và 3, nên

```math
x^2-5x+6=(x-2)(x-3).
```

Factorization biến problem tìm zeros thành problem tìm factors.

## Why factorization works

Nếu product bằng zero:

```math
ab=0
```

trong real/integer arithmetic, ít nhất một factor phải zero. Vì vậy

```math
(x-2)(x-3)=0
```

cho

```math
x=2\quad\text{hoặc}\quad x=3.
```

Đây là zero-product property.

## Multiplicity

Nếu

```math
P(x)=(x-r)^kQ(x)
```

và `Q(r)≠0`, root `r` có multiplicity `k`.

Even multiplicity thường làm graph chạm x-axis rồi quay lại; odd multiplicity thường cross axis. Calculus sau này giải thích điều này qua local behavior và derivatives.

## Polynomial division

Polynomial long division tương tự integer division:

```math
P(x)=D(x)Q(x)+R(x)
```

với degree của remainder nhỏ hơn degree divisor.

Nếu divisor là `(x-r)`, remainder bằng `P(r)`. Đây là remainder theorem.

## Quadratics và geometry

Quadratic

```math
f(x)=ax^2+bx+c
```

có graph parabola. Completing square:

```math
f(x)=a(x-h)^2+k
```

làm vertex `(h,k)` rõ ngay.

Representation expanded form hữu ích cho coefficients; factored form hữu ích cho roots; vertex form hữu ích cho geometry. Đây là ví dụ quan trọng rằng cùng object có nhiều representations, và chọn representation đúng có thể làm bài toán dễ hơn đáng kể.

## Polynomial approximation

Taylor polynomial approximate smooth function quanh một point:

```math
f(x)\approx
f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\cdots
```

Điều này khiến polynomial trở thành local universal language của calculus và numerical computation.

## Horner's method

Thay vì evaluate

```math
a_nx^n+\cdots+a_1x+a_0
```

bằng tính powers riêng, viết nested:

```text
(...((a_n x + a_{n-1})x+a_{n-2})x+...)+a_0
```

Horner's method giảm number of multiplications và thường numerically/computationally tốt hơn.

Ví dụ:

```math
2x^3-3x^2+4x-5
```

viết

```math
((2x-3)x+4)x-5.
```

Đây là connection trực tiếp giữa algebraic representation và algorithm efficiency.

## Mental Model

> Polynomial là object có nhiều “view”: coefficients cho algebra, factors cho roots, graph cho geometry, Taylor form cho local approximation. Factorization là đổi representation để zeros và structure trở nên nhìn thấy được.

## Common Misconceptions

Degree của sum có thể thấp hơn max degree nếu leading terms cancel. Root multiplicity ảnh hưởng local graph. Factorization không phải lúc nào cũng đẹp trên integers; có thể cần real hoặc complex numbers.
