# Đạo hàm: tốc độ thay đổi cục bộ

Đạo hàm (Derivative / 미분계수, 도함수) trả lời một câu hỏi tưởng đơn giản nhưng algebra hữu hạn không giải trực tiếp được: một quantity đang thay đổi nhanh đến đâu tại chính một thời điểm?

## Từ average rate đến instantaneous rate

Nếu `y=f(x)`, average rate trên interval từ `x` đến `x+h` là

```math
\frac{f(x+h)-f(x)}{h}
```

Đây là slope của secant line qua hai points trên graph. Muốn slope tại một point, ta làm second point tiến gần first:

```math
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}
```

Đây là derivative from first principles.

## Derive x²

Với `f(x)=x^2`:

```math
f'(x)=\lim_{h\to0}\frac{(x+h)^2-x^2}{h}
```

Khai triển:

```math
=\lim_{h\to0}\frac{2xh+h^2}{h}
```

với `h≠0` trong quá trình limit:

```math
=\lim_{h\to0}(2x+h)=2x
```

Derivative thay đổi theo `x`: parabola càng xa origin càng steep.

## Units

Nếu `x(t)` đo meters và `t` seconds:

```math
\frac{dx}{dt}
```

có unit m/s, là velocity. Second derivative:

```math
\frac{d^2x}{dt^2}
```

có unit m/s², là acceleration.

Derivative là rate, nên unit ratio rất quan trọng.

## Local linearization

Với small `Δx`:

```math
f(x+\Delta x)\approx f(x)+f'(x)\Delta x
```

Derivative là coefficient của best local linear approximation. Đây là interpretation sâu hơn “slope tangent”. Một nonlinear function khi zoom đủ gần một differentiable point trông gần linear.

## Power rule

```math
\frac{d}{dx}x^n=nx^{n-1}
```

có thể derive từ binomial expansion trong integer case. Rule nói local sensitivity của power function scale theo power và current magnitude.

## Product rule

Nếu `y=u(x)v(x)`, small changes:

```math
(u+\Delta u)(v+\Delta v)-uv
=u\Delta v+v\Delta u+\Delta u\Delta v
```

Chia cho `Δx` rồi limit, second-order product term vanish, cho

```math
(uv)'=u'v+uv'
```

Cả hai factors thay đổi nên phải tính contribution của cả hai.

## Chain rule

Nếu

```math
y=f(g(x))
```

thì

```math
\frac{dy}{dx}=f'(g(x))g'(x)
```

Trực giác: outer sensitivity “output per unit g” nhân inner sensitivity “g per unit x” cho output per unit x. Units cũng multiply/cancel giống rates.

Backpropagation trong neural networks là repeated chain rule qua computational graph.

## Implicit differentiation

Không phải relationship nào cũng viết dễ dạng `y=f(x)`. Với circle

```math
x^2+y^2=r^2
```

differentiate theo `x`:

```math
2x+2y\frac{dy}{dx}=0
```

nên

```math
\frac{dy}{dx}=-\frac{x}{y}
```

Derivative của `y` xuất hiện vì `y` itself depends on `x`.

## Derivatives của exp, log, trig

Các identities nền:

```math
\frac{d}{dx}e^x=e^x
```

```math
\frac{d}{dx}\ln x=\frac1x
```

```math
\frac{d}{dx}\sin x=\cos x
```

```math
\frac{d}{dx}\cos x=-\sin x
```

với angles tính bằng radians.

## Non-differentiability

Function có thể không differentiable vì corner/cusp, vertical tangent hoặc discontinuity. `|x|` tại 0 có left slope `-1`, right slope `1`, nên derivative không tồn tại.

Differentiability imply continuity, nhưng continuity không imply differentiability.

## Mental Model

> Derivative là hệ số nhạy cục bộ: nếu input nhích một lượng rất nhỏ, output thay đổi xấp xỉ derivative nhân với lượng nhích đó. Nó là local linear model của một process có thể nonlinear ở scale lớn.

## Common Misconceptions

`dy/dx` có thể thao tác giống fraction trong một số derivations nhưng formal derivative không đơn giản chỉ là fraction hai infinitesimals. Derivative bằng 0 không luôn là max/min. Function continuous chưa chắc differentiable.
