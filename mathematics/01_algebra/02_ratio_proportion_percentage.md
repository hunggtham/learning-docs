# Tỉ số, tỉ lệ, rate và phần trăm: ngôn ngữ của so sánh tương đối

Tỉ số (ratio / 비) là một trong những ideas arithmetic quan trọng nhất vì rất nhiều quantities trong đời sống không có ý nghĩa khi nhìn bằng absolute difference alone. “Hơn 10” và “gấp đôi” trả lời hai câu hỏi khác nhau.

Nếu server A xử lý 200 requests/s và server B xử lý 100 requests/s, difference là 100 requests/s nhưng ratio là

```math
\frac{200}{100}=2.
```

Difference là additive comparison; ratio là multiplicative comparison.

## Ratio là quantity không phụ thuộc scale chung

Nếu `a:b=2:3`, scale cả hai bởi cùng positive factor `k`:

```math
ka:kb=2:3.
```

Ratio không đổi. Đây là reason ratios phù hợp mô tả shape, composition và relative allocation.

Recipe 2 parts water : 1 part concentrate vẫn giữ taste nếu scale từ cups sang liters, miễn cùng ratio.

## Ratio, rate và fraction khác nhau thế nào?

Ratio có thể so quantities cùng loại hoặc khác loại.

Nếu same unit, ratio thường dimensionless:

```math
\frac{10\text{ kg}}{5\text{ kg}}=2.
```

Nếu khác units, ratio trở thành rate:

```math
\frac{120\text{ km}}{2\text{ h}}=60\text{ km/h}.
```

Rate có unit và thường mô tả “per one unit” của denominator quantity.

Fraction như `3/5` có thể represent ratio, probability, operator “divide 3 by 5” hoặc part-whole relation tùy context. Không nên đồng nhất notation với meaning.

## Proportion: equality của ratios

Tỉ lệ thức (proportion / 비례식):

```math
\frac ab=\frac cd,
```

với denominators nonzero.

Cross multiplication

```math
ad=bc
```

không phải rule riêng cần học thuộc. Multiply both sides bởi `bd`:

```math
bd\frac ab=bd\frac cd,
```

rồi cancel denominators.

Understanding này giúp tránh dùng cross multiplication trong expressions nơi denominator có thể zero hoặc equation không thực sự là equality of ratios.

## Direct proportionality: constant ratio

Nếu `y` tỷ lệ thuận với `x`:

```math
y=kx.
```

Then

```math
\frac yx=k
```

constant khi `x\neq0`.

Graph đi qua origin vì nếu input zero thì output zero trong model.

Ví dụ unit price fixed `p`:

```math
C=pq.
```

Nếu quantity double, total cost double.

Nếu graph linear nhưng có intercept:

```math
C=b+pq,
```

thì cost không proportional với quantity dù vẫn affine/linear-looking. Fixed fee `b` phá constant ratio.

## Inverse proportionality: constant product

Nếu

```math
y=\frac{k}{x},
```

thì

```math
xy=k.
```

Một variable tăng factor `c` thì other giảm factor `c`.

Ideal work model: fixed workload `W`, identical workers `n`, no coordination overhead:

```math
T=\frac W{rn}.
```

Time inverse-proportional với workers. Real teams violate assumptions vì communication, dependencies và uneven tasks. Đây là example quan trọng: proportionality is a model, not a law by notation alone.

## Percentage chỉ là ratio trên base 100

```math
15\%=\frac{15}{100}=0.15.
```

`p%` của `x`:

```math
\frac p{100}x.
```

Ví dụ:

```math
20\%\text{ of }300
=0.2\times300
=60.
```

Điểm quan trọng là luôn xác định **base**. “20% increase” nghĩa 20% của old value, không phải new value.

## Percentage change: denominator là reference state

Từ old `x` sang new `y`:

```math
\text{relative change}
=
\frac{y-x}{x}.
```

Percentage change:

```math
\frac{y-x}{x}\times100\%.
```

Từ 80 lên 100:

```math
\frac{20}{80}=25\%.
```

Từ 100 xuống 80:

```math
\frac{-20}{100}=-20\%.
```

Hai percentages khác nhau vì denominator/base khác.

## Vì sao +10% rồi -10% không cancel?

Repeated percentage changes multiply growth factors.

Increase 10%:

```math
\times1.10.
```

Decrease 10%:

```math
\times0.90.
```

Combined:

```math
1.10\times0.90=0.99.
```

Net -1%.

Percentage operations live naturally in multiplicative space, không additive space.

## Percentage point khác percentage change

Nếu interest rate tăng từ 3% lên 5%:

- increase là 2 **percentage points**;
- relative percentage increase là

```math
\frac{5-3}{3}\approx66.7\%.
```

Hai statements khác nhau mạnh. Reports về polls, rates, margins và market share thường bị hiểu sai vì trộn hai concepts này.

## Repeated rates dẫn tới exponential growth

Nếu quantity tăng fixed rate `r` mỗi period:

```math
x_{n+1}=x_n(1+r).
```

Repeated substitution:

```math
x_n=x_0(1+r)^n.
```

Compound interest, population growth, inflation compounding và depreciation đều dùng same multiplicative structure.

Arithmetic percentage vì vậy là prerequisite trực tiếp cho exponential functions và finance.

## Annualized return và geometric mean

Nếu returns nhiều periods là `r_1,...,r_n`, wealth multiplier là

```math
\prod_{i=1}^n(1+r_i).
```

Average arithmetic return

```math
\frac1n\sum r_i
```

không reproduce final wealth generally.

Geometric average growth rate `g` thỏa

```math
(1+g)^n
=
\prod_{i=1}^n(1+r_i).
```

Đây là reason finance phân biệt arithmetic average và compound growth.

### Worked example

Year 1 +50%, year 2 -50%:

```math
1.5\times0.5=0.75.
```

Total wealth giảm 25%, dù arithmetic average return là 0%.

Multiplicative process cần multiplicative aggregation.

## Weighted average: denominator tells what is being averaged

Class A: 10 students average 80. Class B: 30 students average 90.

Overall average:

```math
\frac{10(80)+30(90)}{40}=87.5.
```

Không phải 85.

Each group mean represents different number of observations. Weighted average reconstructs total numerator divided total denominator.

General:

```math
\bar x_w
=
\frac{\sum_iw_ix_i}{\sum_iw_i}.
```

Portfolio return, CPI baskets, grades, distributed metrics và expected values đều dùng weighted structure.

## Simpson's paradox: aggregated ratios có thể đảo conclusion

Nếu success rates được aggregate across groups có different sizes/difficulty, overall ratio có thể reverse within-group trends.

Reason: weighted composition differs between groups. Ratio comparison without conditioning can hide confounding.

Đây là bridge từ elementary percentages sang statistics và causal reasoning.

## Rates và dimensional analysis

Speed:

```math
60\frac{\text{km}}{\text{h}}.
```

Travel 2.5 h:

```math
60\frac{\text{km}}{\text{h}}
\times2.5\text{ h}
=150\text{ km}.
```

Units cancel như algebraic factors.

Currency exchange:

```math
100\text{ USD}
\times
\frac{1400\text{ KRW}}{1\text{ USD}}
=140000\text{ KRW}.
```

Writing units makes multiply/divide direction explicit.

## Scaling law và ratio reasoning

Nếu similar shapes scale length by `k`, corresponding side ratios constant. Area scales `k^2`, volume `k^3`.

Thus elementary proportion becomes geometric scaling and dimensional analysis.

## AI and data connection — normalization and rates

Metrics like precision, recall, conversion rate, error rate đều ratios. Their denominator defines meaning.

For example:

```math
precision
=
\frac{TP}{TP+FP},
```

```math
recall
=
\frac{TP}{TP+FN}.
```

Same numerator `TP`, different denominators → different questions.

Never compare percentages without checking denominator population.

## Finance connection — nominal vs real change

If nominal wealth grows by `r_n` and prices by inflation `\pi`, exact real growth factor is

```math
\frac{1+r_n}{1+\pi}.
```

So real return:

```math
r_{real}
=
\frac{1+r_n}{1+\pi}-1.
```

Approximation

```math
r_{real}\approx r_n-\pi
```

works only for small rates.

This is another example where multiplicative ratios are fundamental and additive shortcuts are approximations.

## Assumptions và failure modes

Ratios become unstable when denominator near zero. Percentage changes from very small bases can look huge. A 100% increase from 1 to 2 may be operationally tiny; context and absolute magnitude still matter.

Average of ratios may differ from ratio of totals. Weighted aggregation must match desired denominator.

## Mental Model

> Ratio answers “how many times relative to a reference?” Rate adds units to that comparison. Percentage simply expresses a ratio on a base-100 scale. Repeated percentages multiply, weighted averages reconstruct numerator/denominator structure, and many statistical or financial errors come from forgetting which denominator defines the question.

## Common Misconceptions

**“+10% and -10% cancel.”** They apply to different bases and combine multiplicatively.

**“2 percentage points = 2% increase.”** Not generally; percentage points measure absolute difference between percentages.

**“Average of averages is fine.”** Only when weights/groups are equal or specifically appropriate.

**“A huge percentage change always means a huge practical change.”** Small denominators can create huge percentages.

**“Any straight line means direct proportionality.”** `y=kx+b` is proportional only when `b=0`.