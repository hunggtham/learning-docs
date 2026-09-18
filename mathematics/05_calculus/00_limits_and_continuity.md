# Giới hạn và tính liên tục

Giải tích cần một ngôn ngữ để nói chính xác về “tiến gần”. Không thể định nghĩa vận tốc tức thời bằng cách đặt khoảng thời gian bằng 0, vì sẽ chia cho 0. Giới hạn (Limit / 극한) giải quyết vấn đề bằng cách nghiên cứu behavior khi input tiến gần một value mà không cần chạm đúng value đó.

## Limit là gì?

Ký hiệu

```math
\lim_{x\to a}f(x)=L
```

nghĩa là khi `x` được làm đủ gần `a` nhưng không nhất thiết bằng `a`, `f(x)` có thể được làm tùy ý gần `L`.

Ví dụ

```math
f(x)=\frac{x^2-1}{x-1}
```

undefined tại `x=1`, nhưng với `x≠1`:

```math
f(x)=x+1
```

nên

```math
\lim_{x\to1}f(x)=2
```

Limit mô tả local behavior xung quanh point; function value tại point có thể là chuyện khác.

## Epsilon–delta idea

Định nghĩa formal:

```math
\lim_{x\to a}f(x)=L
```

nếu với mọi `ε>0`, tồn tại `δ>0` sao cho

```math
0<|x-a|<\delta
```

thì

```math
|f(x)-L|<\varepsilon
```

`ε` là tolerance mong muốn ở output; `δ` là mức input proximity đủ để đảm bảo tolerance đó. Definition không nói “rất gần” mơ hồ; nó cho một contract quantitative.

## One-sided limits

Left-hand limit:

```math
\lim_{x\to a^-}f(x)
```

right-hand limit:

```math
\lim_{x\to a^+}f(x)
```

Two-sided limit tồn tại khi hai one-sided limits tồn tại và bằng nhau.

Piecewise business rules, thresholds và step functions thường có jumps nơi hai sides khác nhau.

## Infinite limits và asymptotes

Nếu `f(x)` grow without bound khi `x→a`, ta viết limit là `∞` theo extended notation. `∞` không phải real number mà function “đạt tới”; nó mô tả unbounded behavior.

Ví dụ

```math
\lim_{x\to0^+}\frac1x=+\infty
```

trong khi left side là `-∞`, nên two-sided finite/infinite limit theo cùng sign không tồn tại.

## Limits at infinity

```math
\lim_{x\to\infty}f(x)=L
```

mô tả long-run behavior khi input tăng không giới hạn.

Với rational function, highest-degree terms thường dominate. Ví dụ

```math
\lim_{x\to\infty}\frac{3x^2+1}{x^2-5}=3
```

vì chia numerator/denominator cho `x^2` làm lower-order terms vanish in limit.

## Continuity

Function continuous tại `a` nếu ba điều đúng:

1. `f(a)` được xác định;
2. `lim_{x→a} f(x)` tồn tại;
3. limit bằng `f(a)`.

Trực giác “vẽ không nhấc bút” hữu ích nhưng không phải definition đầy đủ.

Continuity nói small changes in input dẫn tới arbitrarily small changes in output local quanh point, theo precise limit sense.

## Types of discontinuity

Removable discontinuity như hole ở `f(x)=(x^2-1)/(x-1)` tại 1 có finite limit nhưng function missing/wrong value.

Jump discontinuity có left/right limits hữu hạn nhưng khác nhau.

Infinite discontinuity có unbounded behavior như `1/x` quanh 0.

## Intermediate Value Theorem

Nếu `f` continuous trên `[a,b]` và một value `N` nằm giữa `f(a)` và `f(b)`, tồn tại ít nhất một `c∈[a,b]` sao cho `f(c)=N`.

Đây là existence theorem. Nó đứng sau bisection root-finding: nếu continuous function đổi dấu trên interval, có ít nhất một root ở giữa.

## Limits trong numerical computing

Máy tính không “lấy h→0” literal. Nếu chọn `h` quá lớn, finite-difference derivative có truncation error; quá nhỏ, floating-point cancellation/rounding error có thể dominate. Mathematical limit là ideal object; numerical approximation cần cân bằng finite precision.

## Mental Model

> Limit là cách biến câu “càng tiến gần thì càng giống” thành một statement chính xác về tolerance. Nó cho phép calculus nói về instantaneous change và infinite processes mà không cần thực hiện phép chia cho zero hay hoàn thành vô hạn bước.

## Common Misconceptions

Limit không bắt buộc bằng function value. `∞` không phải real number có thể thay vào algebra như bình thường. Continuous không đồng nghĩa differentiable; `|x|` continuous tại 0 nhưng không có derivative ở đó.
