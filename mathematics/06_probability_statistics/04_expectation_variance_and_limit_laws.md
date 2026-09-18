# Kỳ vọng, phương sai và các luật giới hạn

Kỳ vọng (Expectation / 기댓값) tóm tắt center theo weighted average; phương sai (Variance / 분산) đo spread quanh mean. Nhưng chúng không fully determine distribution nói chung.

## Expectation

Discrete:

```math
E[X]=\sum_x xP(X=x)
```

Continuous:

```math
E[X]=\int x f_X(x)dx
```

Expectation không nhất thiết là value có thể xảy ra. Fair die có expected value 3.5 dù không roll 3.5.

## Linearity of expectation

Một property cực mạnh:

```math
E[aX+bY+c]=aE[X]+bE[Y]+c
```

không cần X và Y independent.

Điều này giúp analyze total counts. Nếu `X_i` indicator item i được selected, total `S=ΣX_i`, thì

```math
E[S]=\sum_iP(X_i=1)
```

ngay cả khi indicators phụ thuộc nhau.

## Variance

```math
\operatorname{Var}(X)=E[(X-\mu)^2]
```

với `μ=E[X]`.

Equivalent:

```math
\operatorname{Var}(X)=E[X^2]-E[X]^2
```

Standard deviation:

```math
\sigma=\sqrt{\operatorname{Var}(X)}
```

trở về same unit với X.

## Scaling variance

```math
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)
```

Shift không đổi spread; scale by `a` scale deviations by `a`, squared deviations by `a^2`.

## Covariance

```math
\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]
```

positive khi variables thường deviate cùng direction, negative opposite. Correlation normalize covariance:

```math
\rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}
```

nằm [-1,1] khi variances nonzero.

Zero covariance không nói chung imply independence, ngoại trừ special families như joint normal under suitable conditions.

## Law of Large Numbers

Với iid variables có finite expectation trong standard theorem conditions, sample mean

```math
\bar X_n=\frac1n\sum_{i=1}^nX_i
```

converges toward true mean as `n` grows.

LLN giải thích vì sao aggregate averages ổn định hơn single outcomes. Nó không nói fluctuations biến mất hoàn toàn ở finite n.

## Central Limit Theorem

Under common conditions, standardized sum/mean của nhiều iid variables có distribution approach normal:

```math
\frac{\bar X-\mu}{\sigma/\sqrt n}\Rightarrow N(0,1)
```

khi `n` lớn.

CLT nói distribution của properly normalized sample mean gần normal, không nói raw underlying data phải normal.

## Standard error

Standard deviation của sampling distribution của sample mean:

```math
SE(\bar X)=\frac{\sigma}{\sqrt n}
```

nếu population σ known/ideal iid setting. Doubling sample size không halve error; cần quadruple n để halve `1/√n` scale.

## Mental Model

> Expectation là center của probabilistic mass; variance là average squared distance khỏi center. LLN nói averaging stabilizes; CLT nói shape của normalized aggregate thường trở nên approximately normal dưới broad conditions.

## Common Misconceptions

Expected value không phải guaranteed outcome. LLN không nói short random streak phải tự sửa ngay. CLT không biến mọi raw dataset thành normal distribution. Correlation zero không luôn nghĩa independence.

## Worked Example: variance của average

Nếu `X_1,...,X_n` independent với same variance `σ²`, sample mean

```math
\bar X=\frac1n\sum_iX_i
```

có variance

```math
Var(\bar X)
=\frac1{n^2}\sum_iVar(X_i)
=\frac{n\sigma^2}{n^2}
=\frac{\sigma^2}{n}
```

nên standard deviation của mean:

```math
\frac\sigma{\sqrt n}
```

Đây là nguồn của square-root law trong sampling error. Muốn giảm uncertainty factor 10 cần roughly 100× independent sample size, nếu assumptions giữ.

## Dependence thay đổi averaging benefit

Nếu observations correlated, covariance terms xuất hiện:

```math
Var\left(\sum_iX_i\right)
=\sum_iVar(X_i)+2\sum_{i<j}Cov(X_i,X_j)
```

Strong positive correlation khiến averaging giảm variance ít hơn. Time-series observations gần nhau thường không equivalent với cùng số independent samples.

## Mean không đủ để mô tả risk

Hai distributions có cùng expectation nhưng variance hoặc tail behavior hoàn toàn khác. Vì vậy expected return, expected latency hay expected loss chỉ là một projection của distribution. Khi downside bất đối xứng hoặc catastrophic tail quan trọng, cần thêm quantiles, variance/tail metrics và domain-specific loss.
