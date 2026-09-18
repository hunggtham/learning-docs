# Đo lường, đơn vị và ước lượng

Khi toán học chạm vào thế giới thật, number hầu như luôn đi cùng unit, uncertainty và scale. “5” một mình có rất ít nghĩa; `5 m`, `5 s`, `5%`, `5 requests/s` mô tả những loại quantity hoàn toàn khác nhau.

## Quantity và unit

Một measured quantity có thể conceptualize là

```text
numerical value × unit
```

Ví dụ `3.2 km`.

Nếu đổi sang meter:

```math
3.2\,km
\times
\frac{1000\,m}{1\,km}
=
3200\,m.
```

Conversion factor bằng 1 về physical quantity, nên quantity không đổi dù numerical representation đổi.

## Dimensional analysis

Các base dimensions phổ biến gồm length `[L]`, mass `[M]`, time `[T]`.

Velocity:

```math
[v]=LT^{-1}.
```

Acceleration:

```math
[a]=LT^{-2}.
```

Force từ `F=ma`:

```math
[F]=MLT^{-2}.
```

Nếu hai vế của equation có different dimensions, equation chắc chắn sai về physical meaning.

Ngược lại, dimensionally consistent không đảm bảo equation đúng. `s=vt` và `s=2vt` đều same dimensions; cần physics/model để chọn relationship.

## Significant figures

Chữ số có nghĩa (Significant figures / 유효숫자) truyền đạt precision của measurement.

Một length `12.3 cm` không nói rằng ta biết value tới `12.300000 cm`. Extra digits do calculator tạo ra không thêm information từ measurement ban đầu.

Trong engineering, false precision có thể gây cảm giác certainty giả.

## Absolute và relative error

Nếu true value là `x` và approximation là `\hat x`, absolute error:

```math
E_{abs}=|x-\hat x|.
```

Relative error:

```math
E_{rel}=\frac{|x-\hat x|}{|x|}
```

khi `x≠0`.

Một error `1 cm` có thể lớn nếu object dài `2 cm`, nhưng negligible nếu bridge dài `2 km`. Relative error capture scale.

## Percentage error

```math
100E_{rel}\%
```

cho percentage error.

Nhưng percentage dễ bị lạm dụng. Increase từ 10 lên 20 là `100%`; decrease từ 20 xuống 10 là `50%`. Percentage changes không symmetric vì denominator khác.

## Approximation order

Một approximation có thể phụ thuộc vào small quantity `h`. Nếu error behaves approximately như

```math
E(h)\approx Ch^p,
```

thì giảm `h` một nửa làm error giảm khoảng

```math
2^p
```

lần.

Đây là nền để hiểu numerical methods. Higher-order method không nhất thiết luôn tốt hơn thực tế vì computational cost, stability và floating-point error cũng quan trọng.

## Order of magnitude

Order of magnitude mô tả scale theo powers of ten. `3000≈3×10^3`; `0.004≈4×10^{-3}`.

Nếu hai systems khác nhau 6 orders of magnitude, difference khoảng factor `10^6`, tức một triệu lần.

Scientific notation làm scale rõ hơn và giảm lỗi đếm zero.

## Fermi estimation

Fermi estimate phân rã một question lớn thành factors có thể estimate.

Ví dụ rough estimate requests/day:

```text
users × sessions/user/day × requests/session
```

Nếu có:

```text
100,000 users
× 2 sessions/day
× 30 requests/session
```

thì khoảng

```text
6,000,000 requests/day.
```

Average requests/second:

```math
\frac{6,000,000}{86,400}\approx69.4.
```

Peak load sẽ cao hơn average, nhưng estimate đầu tiên cho scale trước khi design infrastructure.

## Ratio và dimensionless quantities

Một ratio giữa quantities cùng unit thường dimensionless.

Ví dụ efficiency:

```math
\eta=\frac{useful\ output}{input}.
```

Probability, percentage, many normalized metrics và cosine similarity đều dimensionless hoặc effectively normalized quantities.

Dimensionless values dễ compare across systems nhưng context vẫn quan trọng. Accuracy `95%` trên heavily imbalanced classification có thể misleading.

## Linear và logarithmic scales

Linear scale coi equal differences là equal spacing. Logarithmic scale coi equal ratios là equal spacing.

Trên log10 scale:

```math
1,10,100,1000
```

cách nhau đều vì mỗi step multiply by 10.

Log scales hữu ích khi range spans many orders of magnitude. Decibel, pH, earthquake magnitude và log charts dùng idea này ở các contexts khác nhau.

## Percentage point

Nếu interest rate từ `3%` lên `4%`, increase là `1 percentage point`, nhưng relative increase là

```math
\frac{4-3}{3}=33.3\%.
```

Hai cách nói trả lời hai questions khác nhau.

## Uncertainty propagation trực giác

Nếu measured quantities có uncertainty, result tính từ chúng cũng có uncertainty.

Nếu

```math
z=x+y,
```

small absolute errors ảnh hưởng theo additive scale.

Nếu

```math
z=xy,
```

relative errors thường là perspective tự nhiên hơn.

Calculus sau này formalize bằng derivatives: sensitivity của output với input quyết định error propagation.

## Mental Model

> Number trả lời “bao nhiêu”, unit cho biết number đang đo “loại gì”, error cho biết ta tin nó đến đâu, scale cho biết nên so sánh nó theo additive hay multiplicative perspective.

## Common Misconceptions

Nhiều decimal places không đồng nghĩa với accurate measurement. Percentage increase và percentage-point change không giống nhau. Unit không phải decoration có thể bỏ đi; trong scientific reasoning, unit hoạt động gần giống type information và có thể bắt được lỗi logic.
