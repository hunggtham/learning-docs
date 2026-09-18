# Biến ngẫu nhiên và phân phối

Biến ngẫu nhiên (Random variable / 확률변수) là function gán numerical value cho outcomes của random experiment. Tên “variable” dễ gây hiểu lầm: nó không phải một value tự nhảy lung tung; nó là mapping từ outcome space sang numbers, còn randomness nằm ở outcome chưa biết.

## Discrete random variables

Nếu possible values countable, dùng probability mass function:

```math
p_X(x)=P(X=x)
```

với

```math
\sum_xp_X(x)=1
```

Ví dụ number of heads trong 3 coin tosses nhận values 0,1,2,3.

## Continuous random variables

Continuous variable dùng probability density function `f_X(x)` với

```math
P(a\le X\le b)=\int_a^b f_X(x)dx
```

và

```math
\int_{-\infty}^{\infty}f_X(x)dx=1
```

Với continuous distribution, probability tại exact point thường 0:

```math
P(X=x)=0
```

Density có thể lớn hơn 1 ở một point; probability là area/integral, không phải density height alone.

## CDF

Cumulative distribution function:

```math
F_X(x)=P(X\le x)
```

CDF áp dụng cho cả discrete và continuous cases, monotone từ 0 đến 1. Nếu density tồn tại:

```math
F'(x)=f(x)
```

almost everywhere phù hợp conditions.

## Bernoulli và binomial

Bernoulli variable nhận 1 với probability `p`, 0 với `1-p`.

Binomial `X~Bin(n,p)` đếm successes trong `n` independent Bernoulli trials:

```math
P(X=k)=\binom nkp^k(1-p)^{n-k}
```

Combination chọn positions successes; product probabilities cho một arrangement.

## Poisson

Poisson distribution:

```math
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}
```

model count events trong interval khi assumptions về independent rare events/constant rate approximately hold. `λ` vừa mean vừa variance.

## Uniform distribution

Continuous uniform trên `[a,b]` có constant density:

```math
f(x)=\frac1{b-a}
```

vì total area phải 1.

## Normal distribution

Normal distribution:

```math
f(x)=\frac{1}{\sigma\sqrt{2\pi}}
\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
```

xuất hiện rộng vì sums/averages của nhiều small independent-ish contributions thường approximate normal dưới central limit conditions. Nhưng không phải mọi data “tự nhiên” đều normal.

## Standardization

Nếu `X` có mean `μ`, standard deviation `σ`:

```math
Z=\frac{X-\mu}{\sigma}
```

cho biết value cách mean bao nhiêu standard deviations. Với normal variable, `Z` standard normal.

## Distribution là model, không phải histogram

Histogram là sample-based visualization; distribution là probabilistic model/population law. Sample histogram thay đổi từ sample này sang sample khác.

## Mental Model

> Random variable biến outcomes thành numbers để arithmetic và calculus có thể xử lý uncertainty. Distribution mô tả cách probability mass/density được phân bổ trên những possible values đó.

## Common Misconceptions

Density không phải probability tại point. Normal distribution không phải default cho mọi measurement. “Random variable” là mapping, không phải một variable trong programming theo nghĩa thông thường.

## Worked Example: transformation của random variable

Nếu `X` là temperature Celsius và

```math
Y=1.8X+32
```

là Fahrenheit, expectation biến tuyến tính:

```math
E[Y]=1.8E[X]+32
```

variance:

```math
Var(Y)=1.8^2Var(X)
```

Shift 32 không thêm spread; scale 1.8 scale deviations.

## Joint distributions

Khi có nhiều random variables, joint distribution mô tả probability của combinations. Marginal distribution của X lấy bằng sum/integrate out Y. Conditional distribution giữ information Y đã biết.

Covariance/correlation chỉ tóm tắt một aspect của joint structure. Hai joint distributions có thể cùng means/covariance nhưng tail dependence khác nhau, quan trọng trong finance/risk.

## Distribution choice as assumption

Dùng Poisson ngầm giả định count mechanism gần independent và rate stable; dùng normal ngầm giả định shape phù hợp; dùng binomial giả định fixed n, binary trials và often constant p/independence. Distribution name là package assumptions, không chỉ formula.
