# Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán

Biến ngẫu nhiên (random variable / 확률변수) không phải là một “biến tự nhiên nhảy lung tung”. Formal definition đúng hơn: nó là một function ánh xạ mỗi outcome trong sample space thành một number.

```math
X:\Omega\to\mathbb R.
```

Randomness nằm ở outcome chưa biết; `X` chỉ là rule trích một quantity từ outcome đó. Cách nhìn này rất quan trọng vì nó nối probability với functions, measure, expectation, statistics và machine learning.

## Tại sao cần random variables?

Raw outcomes thường quá chi tiết. Trong ba coin tosses, sample outcome có thể là `HTH`, nhưng nhiều câu hỏi chỉ quan tâm **number of heads**.

Ta định nghĩa

```math
X(HTH)=2.
```

Nhiều outcomes khác nhau có thể map tới cùng value. Random variable compresses outcome space thành numerical quantity relevant cho question.

## Discrete random variable và PMF

Nếu possible values countable, probability mass function là

```math
p_X(x)=P(X=x).
```

Và

```math
\sum_xp_X(x)=1.
```

Ví dụ fair die:

```math
P(X=k)=\frac16,
\qquad k=1,\ldots,6.
```

PMF là distribution of probability mass over possible values.

## Continuous random variable và density

Với continuous random variable, exact point thường có probability zero:

```math
P(X=x)=0.
```

Probability của interval được tính bằng density:

```math
P(a\le X\le b)
=
\int_a^bf_X(x)\,dx.
```

Density thỏa

```math
f_X(x)\ge0,
```

```math
\int_{-\infty}^{\infty}f_X(x)\,dx=1.
```

Density có unit inverse của variable. Nếu `X` đo seconds, density có unit `1/second`. Vì vậy density value có thể lớn hơn 1 mà probability vẫn hợp lệ; probability là **area**, không phải height.

## CDF là representation thống nhất

Cumulative distribution function:

```math
F_X(x)=P(X\le x).
```

CDF tồn tại cho discrete, continuous và mixed distributions. Nó nondecreasing, right-continuous, tiến về 0 ở `-∞` và 1 ở `+∞`.

Nếu density tồn tại đủ regular:

```math
f_X(x)=F_X'(x).
```

Trong discrete case, CDF có jumps; jump size chính là point probability.

## Distribution không phải histogram

Distribution là population/model law. Histogram là một estimator/visualization từ finite sample.

Hai samples từ cùng distribution cho histograms khác nhau. Một histogram mượt không chứng minh true density mượt; bin width selection ảnh hưởng appearance mạnh.

Đây là distinction giữa **model object** và **sample evidence**.

## Bernoulli: unit nhỏ nhất của binary uncertainty

`X~Bernoulli(p)` nếu

```math
P(X=1)=p,
```

```math
P(X=0)=1-p.
```

Expectation:

```math
E[X]=p.
```

Variance:

```math
Var(X)=p(1-p).
```

Một binary indicator event `A` có thể viết

```math
I_A=
\begin{cases}
1,&A\text{ xảy ra}\\
0,&\text{otherwise}
\end{cases}.
```

Then

```math
E[I_A]=P(A).
```

Indicator variables là bridge cực mạnh giữa probability và combinatorics.

## Binomial: count successes từ Bernoulli trials

Nếu

```math
X=X_1+\cdots+X_n
```

với `X_i` independent Bernoulli(`p`), thì

```math
X\sim Bin(n,p).
```

Probability exactly `k` successes:

```math
P(X=k)
=
\binom nkp^k(1-p)^{n-k}.
```

`p^k(1-p)^{n-k}` là probability của one particular success/failure arrangement. `\binom nk` đếm số arrangements tạo cùng count.

Assumptions gồm fixed `n`, binary trials, constant `p` và independence. Nếu probability changes theo time hoặc trials dependent, binomial model không còn exact.

## Poisson: count events trong interval

Poisson distribution:

```math
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
```

Nó phù hợp khi events occur roughly independently, rate approximately constant và simultaneous events negligible ở tiny intervals.

Mean và variance đều bằng `\lambda`:

```math
E[X]=Var(X)=\lambda.
```

Nếu observed variance lớn hơn mean nhiều, data có overdispersion; simple Poisson model có thể miss hidden heterogeneity/dependence.

## Exponential distribution và memorylessness

Nếu Poisson process có rate `\lambda`, waiting time giữa events có exponential distribution:

```math
f(t)=\lambda e^{-\lambda t},\qquad t\ge0.
```

Memoryless property:

```math
P(T>s+t\mid T>s)=P(T>t).
```

Nghĩa là conditional remaining-time distribution không depend on elapsed time. Đây là assumption mạnh; human lifetime, hardware aging và many queues không memoryless.

## Normal distribution và vì sao nó xuất hiện

Normal density:

```math
f(x)
=
\frac{1}{\sigma\sqrt{2\pi}}
\exp\left(
-\frac{(x-\mu)^2}{2\sigma^2}
\right).
```

Normal xuất hiện rộng partly vì central limit theorem: sums/averages của many small contributions có thể approximately normal dưới conditions phù hợp.

Nhưng “data có nhiều factors” không tự động guarantee normality. Heavy tails, skewness, dependence hoặc bounds có thể làm Gaussian assumption poor.

## Expectation là weighted average của distribution

Discrete:

```math
E[X]=\sum_xxP(X=x).
```

Continuous:

```math
E[X]=\int xf_X(x)\,dx.
```

Expectation là center theo probability weights, không nhất thiết là typical outcome.

Linearity:

```math
E[aX+bY]=aE[X]+bE[Y]
```

không cần independence.

Đây là một trong những rules useful nhất trong probability.

## Variance: spread quanh expectation

```math
Var(X)=E[(X-E[X])^2].
```

Equivalent:

```math
Var(X)=E[X^2]-E[X]^2.
```

Standard deviation

```math
\sigma=\sqrt{Var(X)}
```

trở lại same unit as `X`.

Nếu

```math
Y=aX+b,
```

then

```math
E[Y]=aE[X]+b,
```

```math
Var(Y)=a^2Var(X).
```

Shift không đổi spread; scale multiply deviations.

## Worked example — transform temperature uncertainty

Nếu Celsius temperature `X` có

```math
E[X]=20,
\qquad SD(X)=5,
```

và Fahrenheit

```math
Y=1.8X+32,
```

then

```math
E[Y]=1.8(20)+32=68,
```

```math
SD(Y)=1.8(5)=9.
```

Translation +32 đổi location, không đổi deviations. Scale 1.8 scale standard deviation.

## Joint distributions: uncertainty của nhiều quantities cùng lúc

Với `X,Y`, joint distribution mô tả pairs `(X,Y)`. Marginal distribution của `X` lấy bằng sum/integrate out `Y`.

Discrete:

```math
P(X=x)=\sum_yP(X=x,Y=y).
```

Conditional distribution:

```math
P(X=x\mid Y=y)
```

cho distribution của `X` sau khi information `Y=y` được biết.

Joint → marginal → conditional là core dependency cho statistics và Bayesian inference.

## Covariance và correlation chỉ tóm tắt một phần dependence

```math
Cov(X,Y)
=
E[(X-E[X])(Y-E[Y])].
```

Correlation normalize covariance:

```math
\rho
=
\frac{Cov(X,Y)}{\sigma_X\sigma_Y}.
```

Zero correlation không imply independence generally. Nonlinear dependence có thể tồn tại với covariance zero.

Ví dụ nếu `X` symmetric quanh zero và `Y=X^2`, then `X,Y` strongly dependent nhưng covariance có thể bằng zero.

## Transformation của random variable và Jacobian

Nếu

```math
Y=g(X),
```

distribution của `Y` được induce từ `X`.

Với monotone differentiable `g`:

```math
f_Y(y)
=
f_X(g^{-1}(y))
\left|\frac{d}{dy}g^{-1}(y)\right|.
```

Jacobian factor xuất hiện vì probability mass phải được bảo toàn khi coordinates stretch/compress.

Đây là cùng change-of-variables structure trong multivariable integration và normalizing flows.

## Quantiles: đôi khi center/spread chưa đủ

Quantile `q_p` thỏa roughly

```math
P(X\le q_p)=p.
```

Median là 50th percentile. Tail metrics như 95th/99th percentile rất quan trọng cho latency, risk và reliability.

Hai distributions cùng mean/variance vẫn có tails khác mạnh, nên high-percentile behavior có thể hoàn toàn khác.

## Finance connection — returns và tail dependence

Asset returns rarely fully described by Gaussian mean/covariance. Skewness, heavy tails và correlated crashes matter.

Joint distribution determines portfolio risk. Correlation estimated trong normal periods có thể underestimate dependence during stress.

Distribution choice therefore encodes risk assumptions, not just curve-fitting convenience.

## AI connection — output distributions

Classification model often estimates categorical probabilities; regression model có thể predict mean only hoặc full conditional distribution.

Negative log-likelihood training depends on assumed output distribution. Squared error corresponds to Gaussian-noise assumptions under common setup; cross-entropy corresponds to categorical/Bernoulli likelihood structures.

Loss function và probability model are linked.

## Distribution choice là assumption package

- Binomial: fixed trials, binary outcome, often independence/constant `p`.
- Poisson: event-count mechanism with approximately stable independent increments.
- Normal: symmetric light-tailed continuous variation.
- Exponential: memoryless waiting times.
- Heavy-tailed models: larger extreme-event probabilities.

Tên distribution không chỉ chọn formula; nó chọn a story about mechanism.

## Mental Model

> Random variable is a measurement function on uncertain outcomes. Distribution tells how probability is pushed onto the numerical scale created by that function. PMF/density/CDF are different representations of the same probabilistic law; expectation, variance and quantiles are summaries; joint distributions preserve dependence structure that one-dimensional summaries lose.

## Common Misconceptions

**“Density tại `x` là probability của `x`.”** Không trong continuous case; probability là area.

**“Normal là default distribution cho mọi measurement.”** Không. Mechanism, support và tails phải phù hợp.

**“Mean và standard deviation mô tả hết distribution.”** Chỉ với restricted families như Gaussian mới gần như vậy; generally tails/skew/dependence còn rất nhiều information.

**“Zero correlation nghĩa independent.”** Sai trong general case.

**“Chọn Poisson/binomial chỉ là chọn formula.”** Mỗi distribution kéo theo assumptions về data-generating process.