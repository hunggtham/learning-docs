# Tỉ số, tỉ lệ và phần trăm

Tỉ số (Ratio / 비) so sánh hai quantity bằng division. Khi nói `a:b`, ta đang nói relative scale giữa `a` và `b`, thường equivalent với fraction `a/b` khi `b≠0`.

## Ratio là multiplicative comparison

Nếu team A xử lý 200 requests và team B 100 requests, ratio A:B là

```math
\frac{200}{100}=2.
```

A xử lý gấp 2 lần B. Đây là multiplicative comparison, khác với difference `100 requests` là additive comparison.

## Proportion

Tỉ lệ thức (Proportion / 비례식) là equality giữa ratios:

```math
\frac ab=\frac cd.
```

Với denominators nonzero, cross multiplication

```math
ad=bc
```

không phải một luật bí ẩn; nó đến từ nhân hai vế với `bd`.

## Direct proportionality

Nếu `y` tỉ lệ thuận với `x`:

```math
y=kx.
```

`k` là constant of proportionality.

Graph là line qua origin. Nếu `x` gấp đôi, `y` gấp đôi.

Ví dụ với unit price cố định `p`:

```math
cost=p\times quantity.
```

## Inverse proportionality

Nếu

```math
y=\frac{k}{x},
```

`y` tỉ lệ nghịch với `x`. Tích

```math
xy=k
```

không đổi.

Nếu một job cần fixed total work và workers có productivity giống nhau hoàn hảo, completion time có thể roughly inverse với worker count. Thực tế communication overhead phá assumption, nên relation này chỉ là first model.

## Percentage

Percentage (Phần trăm / 백분율) là ratio trên scale 100.

```math
15\%=\frac{15}{100}=0.15.
```

`p% of x` là

```math
\frac p{100}x.
```

Ví dụ 20% của 300:

```math
0.2\times300=60.
```

## Percentage increase

Nếu old value là `x` và new value `y`, relative change:

```math
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

Nhưng từ 100 giảm về 80:

```math
\frac{-20}{100}=-20\%.
```

Increase 25% rồi decrease 20% quay lại original. Percentage changes asymmetric vì base thay đổi.

## Repeated percentage change

Tăng `r` mỗi period:

```math
x_{n+1}=x_n(1+r)
```

nên

```math
x_n=x_0(1+r)^n.
```

Đây là bridge trực tiếp sang exponential growth và compound interest.

Giảm 10% rồi tăng 10% không quay lại original:

```math
0.9\times1.1=0.99.
```

Net result giảm 1%.

## Rates và units

Rate như km/h, requests/s, KRW/USD là ratio của quantities khác loại.

Nếu exchange rate là

```text
1 USD = 1400 KRW
```

thì conversion dùng dimensional cancellation:

```math
100\ USD\times\frac{1400\ KRW}{1\ USD}
=140000\ KRW.
```

Đặt units trong calculation giúp biết nên nhân hay chia.

## Weighted average

Nếu groups có sizes khác nhau, average của group averages không nên lấy simple mean trừ khi weights bằng nhau.

Nếu class A 10 người average 80, class B 30 người average 90:

```math
\bar x=\frac{10(80)+30(90)}{40}=87.5.
```

Không phải `(80+90)/2=85`.

Weighted thinking xuất hiện trong finance portfolio, grade calculation, distributed metrics và statistical aggregation.

## Mental Model

> Difference hỏi “hơn bao nhiêu?”. Ratio hỏi “gấp bao nhiêu?”. Percentage chỉ là ratio được biểu diễn trên scale 100. Khi process lặp bằng percentage, bản chất là repeated multiplication nên exponential behavior xuất hiện.

## Common Misconceptions

Percentage và percentage point không giống nhau. Tăng 50% rồi giảm 50% không quay lại ban đầu. Average của averages cần weights khi group sizes khác nhau. Cross multiplication chỉ hợp lệ khi denominators liên quan không bằng zero.
