# Đạo hàm: local change, sensitivity và linear approximation

Đạo hàm (derivative / 미분계수, 도함수) không nên được học như một bảng công thức differentiation. Nó xuất hiện vì ta cần mô tả **tốc độ thay đổi tại một trạng thái cụ thể**, trong khi phép chia hữu hạn chỉ cho average change trên một interval.

Nếu position của một object là `s(t)`, average velocity từ `t` đến `t+h` là

```math
\frac{s(t+h)-s(t)}{h}.
```

Nhưng câu hỏi vật lý “velocity ngay tại thời điểm `t` là bao nhiêu?” không thể được trả lời bằng cách đơn giản đặt `h=0`, vì khi đó mẫu số bằng zero. Calculus giải quyết bằng limit:

```math
s'(t)=\lim_{h\to0}\frac{s(t+h)-s(t)}{h}.
```

Ta không chia cho zero. Ta nghiên cứu behavior của average rate khi interval trở nên arbitrarily small.

## Ba cách nhìn cần giữ cùng lúc

Derivative có ba interpretation tương đương nhưng hữu ích trong các context khác nhau.

**Slope viewpoint:** derivative là slope của tangent line.

**Rate viewpoint:** derivative là output change trên một unit input change, ở local scale.

**Linearization viewpoint:** derivative là coefficient của best first-order linear approximation:

```math
f(x+\Delta x)
\approx
f(x)+f'(x)\Delta x.
```

Cách nhìn thứ ba là sâu nhất để nối sang multivariable calculus, optimization, numerical methods và machine learning.

## Derive `x^2` từ first principles

Với

```math
f(x)=x^2,
```

ta có

```math
f'(x)
=
\lim_{h\to0}\frac{(x+h)^2-x^2}{h}.
```

Khai triển:

```math
=
\lim_{h\to0}\frac{2xh+h^2}{h}.
```

Trong quá trình limit, `h\neq0`, nên có thể factor/cancel:

```math
=
\lim_{h\to0}(2x+h)=2x.
```

Formula `2x` không phải magic rule. Nó nói parabola có local slope tăng tuyến tính theo position.

## Vì sao power rule có dạng `nx^{n-1}`?

Với positive integer `n`, binomial expansion cho

```math
(x+h)^n
=
x^n+n x^{n-1}h+\text{terms chứa }h^2,h^3,\ldots
```

Difference quotient:

```math
\frac{(x+h)^n-x^n}{h}
=
nx^{n-1}+\text{terms vẫn chứa }h.
```

Khi `h\to0`, các higher-order terms vanish, còn lại

```math
\frac{d}{dx}x^n=nx^{n-1}.
```

Đây cũng preview một idea lớn: derivative giữ lại **first-order term** và bỏ những effects nhỏ hơn theo order của `h`.

## Units: derivative luôn là một rate

Nếu distance đo bằng meters và time bằng seconds:

```math
\frac{ds}{dt}
```

có unit m/s.

Nếu revenue `R(q)` đo bằng dollars và quantity `q` là units sold:

```math
R'(q)
```

có unit dollars per additional unit quanh current operating point.

Units là sanity check mạnh. Nếu derivative có unit vô lý, model hoặc manipulation có thể sai.

## Product rule: khi hai factors cùng thay đổi

Cho

```math
y=u(x)v(x).
```

Nếu cả hai thay đổi một chút:

```math
(u+\Delta u)(v+\Delta v)-uv
=u\Delta v+v\Delta u+\Delta u\Delta v.
```

Chia cho `\Delta x`. Trong limit, term cuối là second order và vanish dưới smoothness phù hợp. Ta nhận

```math
(uv)'=u'v+uv'.
```

Meaning: total first-order change là contribution từ `u` thay đổi khi `v` tạm fixed, cộng contribution từ `v` thay đổi khi `u` tạm fixed.

## Chain rule: sensitivity đi qua một pipeline

Nếu

```math
y=f(g(x)),
```

thì

```math
\frac{dy}{dx}
=
\frac{dy}{dg}\frac{dg}{dx}
=
f'(g(x))g'(x).
```

Interpretation bằng units rất tự nhiên:

```text
output per g-unit × g-unit per x-unit = output per x-unit.
```

Nếu temperature ảnh hưởng pressure, pressure ảnh hưởng sensor voltage, chain rule đo sensitivity của voltage đối với temperature bằng cách multiply local sensitivities qua pipeline.

Backpropagation trong neural networks chính là chain rule được tổ chức efficient trên computational graph.

## Worked example — sensitivity qua một composed model

Giả sử

```math
g(x)=x^2+1,
```

và

```math
f(u)=\ln u.
```

Then

```math
y=\ln(x^2+1).
```

Ta có

```math
\frac{dy}{du}=\frac1u,
\qquad
\frac{du}{dx}=2x.
```

Nên

```math
y'(x)=\frac{2x}{x^2+1}.
```

Tại `x=2`:

```math
y'(2)=\frac45.
```

Nếu `x` tăng khoảng `0.01`, output tăng xấp xỉ

```math
\Delta y\approx \frac45\cdot0.01=0.008.
```

Derivative đã trở thành local prediction tool.

## Exponential và logarithm: những derivatives có structure đặc biệt

Function `e^x` thỏa

```math
\frac{d}{dx}e^x=e^x.
```

Nó là eigenfunction của differentiation operator: derivative không đổi shape, chỉ scale factor bằng 1. Đây là lý do exponential xuất hiện tự nhiên trong systems nơi growth rate proportional current state.

Logarithm có

```math
\frac{d}{dx}\ln x=\frac1x,
```

nên equal relative changes có structure đơn giản trong log coordinates.

## Trigonometric derivatives và vì sao radians quan trọng

Với radians:

```math
\frac{d}{dx}\sin x=\cos x,
```

```math
\frac{d}{dx}\cos x=-\sin x.
```

Nếu đo bằng degrees, extra conversion factor xuất hiện. Radian không chỉ là convention; nó làm angle bằng arc-length/radius, khiến local geometry của circle phù hợp tự nhiên với calculus.

## Implicit differentiation: relationship không cần solve explicit trước

Circle

```math
x^2+y^2=r^2
```

không phải global function `y=f(x)` nếu giữ cả hai halves, nhưng locally ta vẫn tìm slope.

Differentiate theo `x`:

```math
2x+2y\frac{dy}{dx}=0,
```

nên

```math
\frac{dy}{dx}=-\frac{x}{y}.
```

Term `dy/dx` xuất hiện vì `y` itself changes with `x` along the constraint curve.

## Derivative như error propagation

Nếu measurement `x` có small error `\Delta x`, thì

```math
\Delta y
\approx
f'(x)\Delta x.
```

Derivative magnitude cho local error amplification.

Ví dụ `y=x^2`, tại `x=100`, derivative là 200. Error `0.01` trong `x` tạo khoảng `2` units error trong `y`. Same input error ở `x=1` chỉ tạo khoảng `0.02`.

Sensitivity phụ thuộc operating point.

## Relative sensitivity và elasticity

Absolute derivative phụ thuộc units. Dimensionless sensitivity thường dùng elasticity:

```math
E(x)=\frac{x}{f(x)}f'(x).
```

Nó xấp xỉ percentage output change trên percentage input change.

Nếu

```math
f(x)=x^k,
```

thì

```math
E(x)=k.
```

Power-law exponent chính là elasticity constant.

## Differentiability mạnh hơn continuity

Nếu function differentiable tại `a`, nó continuous tại `a`. Nhưng converse sai.

`|x|` continuous tại 0 nhưng left derivative là `-1`, right derivative là `1`; không có single local linear approximation nên derivative không tồn tại.

Điều này cho thấy derivative không chỉ hỏi “graph có đứt không?” mà hỏi “zoom đủ gần có thấy một line duy nhất không?”.

## Khi derivative không tồn tại

Các common reasons:

- jump/discontinuity;
- corner như `|x|`;
- cusp;
- vertical tangent;
- highly oscillatory behavior.

Không nên force symbolic rules ở point nơi assumptions của differentiability fail.

## Numerical differentiation khác symbolic derivative

Máy tính có thể approximate

```math
f'(x)\approx \frac{f(x+h)-f(x)}{h}.
```

Nhưng `h` quá lớn gây truncation error; `h` quá nhỏ gây cancellation/rounding error. Mathematical derivative là limit ideal; finite-difference implementation là numerical approximation.

Automatic differentiation lại khác cả hai: nó áp dụng chain rule chính xác ở machine arithmetic lên computation graph, không xấp xỉ derivative bằng finite differences.

## Physics, AI và Finance connections

Trong physics, derivative tạo velocity, acceleration, force laws và field gradients. Trong AI, gradients đo local sensitivity của loss đối với parameters. Trong finance, delta của option là derivative của price theo underlying; duration/convexity là related sensitivity concepts. Trong software systems, derivative-like reasoning giúp hiểu local capacity sensitivity dù measurements thường noisy và discrete.

Điểm chung là cùng một mathematical structure: **local response to perturbation**.

## Assumptions và failure modes

Derivative là local object. Extrapolate một tangent line quá xa có thể sai mạnh nếu curvature lớn.

Small derivative không luôn nghĩa input “không quan trọng” globally; effect có thể nonlinear hoặc derivative bằng zero đúng tại một special point.

A derivative computed from a model reflects model sensitivity, not automatically real-world causal sensitivity.

## Mental Model

> Đạo hàm là local gain của một system. Ta perturb input một lượng rất nhỏ và hỏi output phản ứng first-order ra sao. Slope, velocity, marginal cost, gradient và backpropagation đều là các biểu hiện của cùng idea: local linear response.

## Common Misconceptions

**“Derivative là slope của graph nên chỉ dùng cho geometry.”** Slope là một representation; derivative tổng quát là local sensitivity.

**“`dy/dx` chỉ là fraction.”** Notation có nhiều manipulations giống fraction vì chain rule/differentials, nhưng derivative được định nghĩa bằng limit/local linear map.

**“Derivative bằng 0 nghĩa function không thay đổi.”** Chỉ nói first-order change bằng zero tại point đó; higher-order change vẫn có thể lớn.

**“Có formula differentiable thì áp dụng ở mọi point.”** Domain, corners, discontinuities và denominator restrictions vẫn phải kiểm tra.