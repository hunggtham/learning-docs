# Ứng dụng của đạo hàm: shape, approximation và optimization

Derivative trở nên mạnh khi ta dùng sign và magnitude của nó để đọc behavior của function thay vì chỉ tính symbolic expression.

## Increasing và decreasing

Nếu `f'(x)>0` trên interval, `f` tăng ở đó; nếu `f'(x)<0`, giảm. Critical points thường nơi

```math
f'(x)=0
```

hoặc derivative undefined nhưng function defined.

Critical point chỉ là candidate cho extremum, không phải guarantee.

## Local extrema

First derivative test xem sign change. Nếu `f'` đổi `+` sang `-`, local maximum; `-` sang `+`, local minimum.

Second derivative:

```math
f''(x)>0
```

cho local concave-up behavior; nếu tại critical point và `f''>0`, thường là local minimum. Nếu `f''<0`, local maximum. Nếu `f''=0`, test inconclusive.

Ví dụ `f(x)=x^4` có `f''(0)=0` nhưng vẫn minimum.

## Concavity và inflection

`f''` đo cách slope thay đổi. Positive second derivative nghĩa slope increasing; negative nghĩa slope decreasing.

Inflection point liên quan change of concavity, không chỉ `f''=0`. Cần verify sign change hoặc structural condition.

## Optimization from first principles

Giả sử rectangle có perimeter fixed `P`. Nếu sides `x,y`:

```math
2x+2y=P
```

nên

```math
y=\frac P2-x
```

Area:

```math
A(x)=x\left(\frac P2-x\right)=\frac P2x-x^2
```

Derivative:

```math
A'(x)=\frac P2-2x
```

set zero:

```math
x=\frac P4
```

và `y=P/4`. Square maximizes area under fixed perimeter.

Điểm quan trọng là derivative chỉ bước cuối; khó khăn thực là model constraint để objective trở thành function phù hợp.

## Marginal quantities

Trong economics, nếu cost `C(q)`, marginal cost:

```math
C'(q)
```

xấp xỉ extra cost khi production tăng một unit quanh current `q`. “Marginal” chính là local rate of change.

Trong software capacity, derivative-like sensitivity có thể đo latency thay đổi thế nào khi load tăng gần operating point, dù real systems thường discrete/noisy.

## Newton's method

Muốn solve `f(x)=0`, dùng tangent line tại current estimate `x_n`:

```math
x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}
```

Derivation: tangent approximation

```math
0\approx f(x_n)+f'(x_n)(x_{n+1}-x_n)
```

solve cho next point.

Method có thể converge rất nhanh gần good root, nhưng có thể fail với poor initial guess, small derivative hoặc structure phức tạp.

## Error propagation

Nếu `y=f(x)` và input uncertainty small `Δx`, local approximation:

```math
\Delta y\approx f'(x)\Delta x
```

nên derivative đo sensitivity/error amplification. Multivariable version dùng gradient/Jacobian.

## Elasticity

Dimensionless sensitivity:

```math
E=\frac{x}{f(x)}f'(x)
```

đo approximate percentage change output cho 1% input change. Economics dùng elasticity vì unit-independent comparison.

## Mental Model

> Derivative biến graph thành bản đồ local behavior: sign nói hướng đi, magnitude nói độ nhạy, derivative thứ hai nói slope đang tự thay đổi thế nào. Optimization là tìm nơi cải thiện first-order không còn khả thi hoặc boundary chặn lại.

## Common Misconceptions

`f'(x)=0` không đủ để kết luận extremum. Local optimum không nhất thiết global. Newton method không guaranteed converge. Optimization luôn cần xét domain/boundary constraints, không chỉ solve derivative bằng zero.
