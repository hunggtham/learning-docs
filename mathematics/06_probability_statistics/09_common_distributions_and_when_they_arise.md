# Các phân phối xác suất thường gặp và vì sao chúng xuất hiện

Một distribution không nên được học như một dòng trong bảng công thức. Cách học bền hơn là hỏi ba câu:

```text
variable sống trên support nào?
mechanism ngẫu nhiên nào sinh ra nó?
assumptions nào khiến model đó hợp lý?
```

Khi hiểu mechanism, ta nhớ distribution bằng structure thay vì hình curve.

## 1. Distribution là model, không phải nhãn histogram

Hai datasets có histogram tương tự nhưng mechanisms khác nhau có thể cần models khác nhau. Ngược lại, cùng một mechanism dưới nhiều regimes có thể dẫn tới approximate distributions khác nhau.

Vì vậy lựa chọn distribution cần xét:

```text
support
sampling mechanism
independence / stationarity
count vs waiting time
boundedness
skew / tails
```

## 2. Bernoulli: một trial, hai outcomes

Bernoulli random variable:

```math
X\in\{0,1\}
```

với:

```math
P(X=1)=p,
\qquad
P(X=0)=1-p.
```

Mean:

```math
E[X]=p.
```

Variance:

```math
\operatorname{Var}(X)=p(1-p).
```

Bernoulli là atomic building block của nhiều count models.

Examples: click/no-click, pass/fail, default/no-default, conversion/no-conversion.

## 3. Indicator variables

Một event `A` có indicator:

```math
I_A=
\begin{cases}
1 & A\text{ xảy ra}\\
0 & \text{ngược lại}
\end{cases}
```

Then:

```math
E[I_A]=P(A).
```

Đây là bridge quan trọng giữa events và random variables. Tổng indicators biến counting problem thành expectation problem.

## 4. Binomial: số successes trong fixed trials

Nếu:

```text
n fixed trials
independent
same success probability p
```

thì:

```math
X\sim\operatorname{Binomial}(n,p)
```

với:

```math
P(X=k)=\binom nk p^k(1-p)^{n-k}.
```

Mean:

```math
np.
```

Variance:

```math
np(1-p).
```

`\binom nk` xuất hiện vì có `C(n,k)` ways đặt `k` successes vào `n` trial positions.

## 5. Khi binomial không phù hợp

Binomial có thể sai nếu:

```text
p thay đổi theo trial
trials phụ thuộc nhau
sampling without replacement từ population nhỏ
```

Trong without-replacement sampling, hypergeometric thường tự nhiên hơn.

## 6. Hypergeometric: sampling without replacement

Population `N`, trong đó `K` successes. Draw `n` without replacement. Số successes `X`:

```math
P(X=k)
=
\frac{\binom Kk\binom{N-K}{n-k}}
{\binom Nn}.
```

Khác binomial ở dependence: mỗi draw thay composition còn lại.

Khi population rất lớn relative to sample, binomial có thể approximate hypergeometric.

## 7. Geometric: waiting tới success đầu tiên

```math
P(X=k)=(1-p)^{k-1}p,
\qquad k=1,2,\ldots
```

Mean:

```math
E[X]=\frac1p.
```

Memoryless property:

```math
P(X>s+t\mid X>s)=P(X>t).
```

Property này không phải “thế giới quên quá khứ”; nó là consequence của constant independent success probability assumption.

## 8. Negative binomial: chờ tới nhiều successes

Nếu geometric chờ success thứ nhất, negative binomial generalizes tới number trials/failures trước success thứ `r`.

Nó cũng hữu ích cho overdispersed count data trong một số parameterizations/models.

Điều quan trọng là check convention vì textbooks/software có nhiều cách định nghĩa support.

## 9. Poisson: count events theo rate

Poisson distribution:

```math
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
```

Mean = variance:

```math
E[X]=\operatorname{Var}(X)=\lambda.
```

Poisson tự nhiên khi events xuất hiện theo rate ổn định trong interval và increments có independence/rare-event structure phù hợp.

## 10. Poisson từ rare-event limit

Binomial với:

```text
n lớn
p nhỏ
np≈λ
```

có limit gần Poisson:

```math
\operatorname{Binomial}(n,p)
\approx
\operatorname{Poisson}(\lambda).
```

Đây là connection mechanism quan trọng: nhiều opportunities, mỗi event hiếm, total expected count finite.

## 11. Overdispersion cảnh báo model sai

Poisson bắt buộc:

```math
\operatorname{Var}(X)=E[X].
```

Nếu data count có variance lớn hơn mean rất nhiều, có thể có clustering, heterogeneous rates hoặc dependence.

Negative binomial hoặc hierarchical models có thể hợp lý hơn.

## 12. Exponential: waiting time trong Poisson process

Nếu events theo homogeneous Poisson process rate `\lambda`, waiting time `T`:

```math
f(t)=\lambda e^{-\lambda t},
\qquad t\ge0.
```

Mean:

```math
E[T]=\frac1\lambda.
```

Survival function:

```math
P(T>t)=e^{-\lambda t}.
```

Exponential là continuous memoryless distribution.

## 13. Hazard rate

Hazard:

```math
h(t)=\frac{f(t)}{P(T>t)}.
```

Với exponential:

```math
h(t)=\lambda.
```

Constant hazard là statement mạnh. Nếu failure risk tăng theo age, exponential có thể không phù hợp.

## 14. Gamma: sum của exponential waiting times

Nếu `T_i` exponential independent cùng rate, tổng nhiều waiting times có gamma distribution.

Gamma support trên positive reals và linh hoạt cho right-skewed quantities.

Special cases liên hệ exponential và chi-square.

## 15. Uniform: symmetry theo interval

Continuous uniform trên `[a,b]`:

```math
f(x)=\frac1{b-a}.
```

Equal-length subintervals có equal probability.

Uniform không đồng nghĩa “ta không biết gì” một cách invariant. Uniform trong `x` không còn uniform sau nonlinear reparameterization `y=g(x)`.

Đây là caution quan trọng trong Bayesian priors.

## 16. Normal/Gaussian: additive fluctuation structure

Normal density:

```math
f(x)
=
\frac1{\sigma\sqrt{2\pi}}
\exp\left(
-\frac{(x-\mu)^2}{2\sigma^2}
\right).
```

Gaussian xuất hiện tự nhiên khi quantity là aggregate của nhiều small contributions và CLT conditions approximately hold.

Nhưng raw data không cần normal để sample mean trở nên approximately Gaussian.

## 17. Standard normal và z-score

Nếu:

```math
X\sim N(\mu,\sigma^2),
```

thì:

```math
Z=\frac{X-\mu}{\sigma}\sim N(0,1).
```

Standardization chuyển location/scale về reference distribution.

Nhưng z-score chỉ có interpretation “bao nhiêu standard deviations” và không tự biến heavy-tailed data thành Gaussian.

## 18. Gaussian stability dưới linear combinations

Nếu Gaussian variables jointly Gaussian, linear combination vẫn Gaussian.

Đây là một reason Gaussian models tractable trong signal processing, Kalman filters và analytical statistics.

## 19. Student's t: extra uncertainty từ estimate scale

Khi mean inference dùng unknown population variance và sample standard deviation, statistic có heavier-tailed `t` distribution dưới standard normal-sampling assumptions.

`t` tails phản ánh uncertainty thêm do estimate `\sigma`.

Khi degrees of freedom tăng:

```text
t → normal
```

vì scale estimate stabilizes.

## 20. Chi-square: sum of squared standard normals

Nếu:

```math
Z_i\sim N(0,1)
```

independent, then:

```math
\sum_{i=1}^k Z_i^2
\sim \chi_k^2.
```

Chi-square naturally appears in variance inference và quadratic Gaussian geometry.

Mean:

```math
k.
```

Variance:

```math
2k.
```

## 21. F distribution

Ratio of scaled independent chi-square variables:

```math
F=
\frac{U_1/d_1}{U_2/d_2}
```

có F distribution.

Nó xuất hiện trong variance comparisons, ANOVA và regression model comparisons trong classical framework.

## 22. Beta: uncertainty trên probability/proportion

Beta density proportional to:

```math
p^{\alpha-1}(1-p)^{\beta-1},
\qquad 0<p<1.
```

Support `[0,1]` làm nó natural cho probability parameter.

Bernoulli/binomial likelihood + beta prior tạo beta posterior:

```text
prior pseudo-counts
+ observed successes/failures
→ posterior parameters
```

## 23. Dirichlet: multivariate beta

Nếu probability vector:

```math
(p_1,\ldots,p_K),
\qquad \sum_i p_i=1,
```

Dirichlet distribution là common model trên simplex và conjugate prior cho categorical/multinomial probabilities.

Đây là bridge tới topic modeling, categorical Bayesian models và compositional probabilities.

## 24. Multinomial: counts across multiple categories

Generalizes binomial. Với `n` independent categorical trials, probabilities `p_1,...,p_K`, counts `X_i` thỏa:

```math
\sum_iX_i=n.
```

Probability:

```math
P(X_1=x_1,\ldots,X_K=x_K)
=
\frac{n!}{\prod_i x_i!}
\prod_i p_i^{x_i}.
```

Multinomial coefficient đếm arrangements của category labels.

## 25. Log-normal: multiplicative mechanisms

Nếu:

```math
\log X\sim N(\mu,\sigma^2),
```

thì `X` log-normal.

Nó thường arise khi quantity là product của many positive random factors hơn là sum.

Income, size-like quantities hoặc multiplicative growth đôi khi có log-normal-like behavior, nhưng empirical validation vẫn cần.

## 26. Power-law và heavy-tail caution

Không phải mọi heavy-tailed histogram là power law.

Power-law-like model:

```math
P(X>x)\propto x^{-\alpha}
```

trên suitable tail region.

Estimating tail exponent và cutoff cần statistical care; log-log straight line bằng mắt không đủ.

## 27. Distribution families và maximum entropy intuition

Một số distributions có thể được characterized bởi constraints + maximum entropy.

Ví dụ Gaussian maximizes differential entropy among distributions with fixed mean/variance under suitable conditions.

This perspective links distribution choice với information theory, nhưng không có nghĩa Gaussian là correct model chỉ vì ta biết mean/variance.

## 28. Approximation relationships

Một useful map:

```text
Binomial(n,p), n large p small → Poisson(np)
Binomial with np,n(1-p) large → Normal approximation
Poisson λ large → approximately Normal
Student t, df large → Normal
```

Approximation cần regime conditions và continuity corrections đôi khi matter.

## 29. Worked example: choose a model

Question: số failed requests trong 10 minutes.

Nếu requests independent rare failures với approximately constant rate, Poisson count model có thể là starting point.

Nếu total requests fixed `n` và mỗi request failure probability roughly same `p`, binomial may be more natural.

Nếu failures cluster theo outages, neither simple model may fit; dependence/mixture/hierarchical model cần được xét.

Mechanism quyết định model family.

## 30. Support là sanity check đầu tiên

Examples:

```text
Bernoulli → {0,1}
Binomial → {0,...,n}
Poisson → nonnegative integers
Exponential/Gamma → positive reals
Beta → [0,1]
Normal → all real numbers
```

Nếu model assign nontrivial probability outside physically possible range, phải giải thích approximation hoặc chọn family khác.

## 31. Finance connection

Asset returns often show heavier tails and volatility clustering than iid Gaussian assumption. Gaussian vẫn useful analytical baseline, nhưng risk estimates có thể understated nếu model tails sai.

Positive quantities như prices không nên modeled naïvely bằng unbounded normal levels nếu negative support vô nghĩa; log-return models thường được dùng vì multiplicative structure.

## 32. AI connection

Common mappings:

```text
Bernoulli → binary labels
Categorical → multiclass labels
Gaussian → continuous noise / latent variables
Dirichlet → uncertainty over categorical probabilities
Poisson → count outputs
```

Loss functions often correspond to negative log-likelihoods of assumed distributions. Chọn loss nghĩa là ngầm chọn error model.

## Mental Model

> Distribution là compressed description của một stochastic mechanism. Support cho biết values nào có thể tồn tại; parameters cho biết scale/rate/shape; assumptions cho biết khi nào model có quyền được dùng.

## Common Misconceptions

Histogram giống bell shape không chứng minh Gaussian. Poisson không phù hợp chỉ vì data là counts. Uniform prior không invariant dưới reparameterization. Continuous density value không phải point probability. A good-fitting distribution không tự chứng minh mechanism causal đúng.
