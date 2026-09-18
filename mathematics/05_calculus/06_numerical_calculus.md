# Numerical calculus: khi máy tính xấp xỉ đạo hàm và tích phân

Mathematical derivative/integral dùng limits ideal. Máy tính có finite precision và finite samples, nên numerical calculus phải xây approximations và quản lý error.

## Forward difference

Taylor expansion:

```math
f(x+h)=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+\cdots
```

rearrange:

```math
f'(x)=\frac{f(x+h)-f(x)}{h}+O(h)
```

Forward difference có first-order truncation error.

## Central difference

Dùng expansions tại `x+h` và `x-h`, subtract:

```math
f'(x)\approx\frac{f(x+h)-f(x-h)}{2h}
```

error thường `O(h^2)`, tốt hơn với comparable step nếu function smooth.

## Step size paradox

Ta tưởng càng nhỏ `h` càng tốt. Nhưng floating-point subtraction `f(x+h)-f(x)` giữa hai nearly equal numbers gây catastrophic cancellation. Khi `h` quá nhỏ, rounding error tăng.

Total error thường có tradeoff giữa truncation và rounding.

## Trapezoidal rule

Approximate `f` linear trên each interval. Một interval `[a,b]`:

```math
\int_a^b f(x)dx\approx\frac{b-a}{2}[f(a)+f(b)]
```

Composite version cộng nhiều trapezoids.

## Simpson's rule

Approximate bằng quadratic qua three samples:

```math
\int_a^b f(x)dx
\approx
\frac{b-a}{6}
\left[f(a)+4f\left(\frac{a+b}{2}\right)+f(b)\right]
```

cho một panel. Higher order với smooth functions.

## Automatic differentiation

Automatic differentiation (AD) khác symbolic differentiation và finite differences. Nó decomposes program thành primitive operations và apply chain rule exactly theo machine arithmetic.

Forward mode propagate derivatives cùng values; reverse mode propagate sensitivities backward. Backprop là reverse-mode AD specialized cho scalar loss/computational graphs.

AD tránh step-size truncation của finite differences nhưng vẫn chịu floating-point và nondifferentiability issues của computation.

## Gradient checking

ML implementations đôi khi compare AD gradient với finite-difference approximation để debug. Vì numerical difference chỉ approximate, compare tolerance chứ không expect bitwise equality.

## Mental Model

> Numerical calculus thay limit ideal bằng finite probes. Accuracy không chỉ phụ thuộc formula mà còn step size, floating-point, smoothness và stability. Automatic differentiation thay approximation bằng systematic chain-rule bookkeeping.

## Common Misconceptions

`h` nhỏ nhất không phải tốt nhất. Finite difference không phải automatic differentiation. Symbolic derivative đẹp không đảm bảo numerical evaluation stable.
