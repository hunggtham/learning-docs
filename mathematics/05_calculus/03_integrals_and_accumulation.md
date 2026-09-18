# Tích phân: accumulation từ vô số phần nhỏ

Tích phân (Integral / 적분) giải quyết bài toán ngược với local rate: nếu biết density/rate ở từng point, tổng effect trên một interval là bao nhiêu?

## Riemann sum

Chia interval `[a,b]` thành subintervals width `Δx`. Approximate accumulated quantity:

```math
\sum_i f(x_i^*)\Delta x
```

Khi partition được làm ngày càng fine và limit tồn tại:

```math
\int_a^b f(x)\,dx
```

Đây là definite integral.

Nếu `f≥0`, geometric interpretation là area under curve; nhưng integral rộng hơn area: nó là signed accumulation.

## Units

Nếu velocity `v(t)` m/s, thì

```math
\int v(t)dt
```

có unit meters và cho displacement.

Nếu power kW integrate theo hours, result kWh là energy. Unit multiplication giúp hiểu integral đang tích lũy gì.

## Signed area

Region dưới x-axis đóng contribution negative. Vì vậy definite integral không luôn bằng geometric area. Muốn total area cần integrate absolute value hoặc split intervals theo sign.

## Fundamental Theorem of Calculus

Định nghĩa accumulation function:

```math
F(x)=\int_a^x f(t)dt
```

thì dưới conditions phù hợp:

```math
F'(x)=f(x)
```

Tức rate của accumulated amount tại endpoint bằng current density/rate.

Chiều còn lại: nếu `F'=f`,

```math
\int_a^b f(x)dx=F(b)-F(a)
```

Differentiation và integration là inverse operations theo nghĩa sâu này.

## Derive position from velocity

Nếu

```math
v(t)=\frac{dx}{dt}
```

thì

```math
x(t)-x(t_0)=\int_{t_0}^t v(s)ds
```

Position change là accumulated velocity. Acceleration integrate cho velocity change.

## Average value

Average function value trên `[a,b]`:

```math
f_{avg}=\frac{1}{b-a}\int_a^b f(x)dx
```

Integral cho total accumulation; chia interval length cho average density.

## Probability density

Continuous random variable với density `p(x)`:

```math
P(a\le X\le b)=\int_a^b p(x)dx
```

Density value có thể lớn hơn 1; probability là area/integral và total density integrates to 1.

## Numerical integration

Nếu antiderivative khó hoặc data discrete, approximate. Trapezoidal rule dùng linear interpolation giữa samples; Simpson dùng quadratic approximation. Accuracy phụ thuộc smoothness, step size và method order.

## Mental Model

> Integral là một accumulator: chia process thành contributions rất nhỏ, cộng chúng, rồi lấy limit khi partition trở nên vô cùng fine. Fundamental theorem nói local rate và global accumulation là hai mặt inverse của cùng process.

## Common Misconceptions

Integral không chỉ là area. `∫f(x)dx` indefinite cần constant `C` vì antiderivatives khác nhau bởi constants. Density không phải probability tại một exact point với continuous variable.
