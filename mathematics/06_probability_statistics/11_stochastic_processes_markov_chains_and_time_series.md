# Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian

Probability cơ bản thường mô tả một random variable tại một thời điểm. Nhưng nhiều hệ thực tế thay đổi theo thời gian: giá tài sản, số request đến server, trạng thái user, packet queue, nhiệt độ, tín hiệu cảm biến, gene expression hay vị trí robot. Để mô tả những hệ như vậy ta cần **stochastic process (확률과정)**.

Một stochastic process là một family các random variables được index bởi time hoặc một parameter khác:

```math
\{X_t:t\in T\}.
```

Với mỗi thời điểm `t`, `X_t` là random variable. Nhưng điều quan trọng không chỉ là distribution riêng lẻ của từng `X_t`; ta cần dependency structure giữa các thời điểm.

## Sample path và distribution

Có hai cách nhìn song song. Nếu cố định time `t`, `X_t` là random variable. Nếu cố định một outcome `ω`, ta thu được một function theo time

```math
t\mapsto X_t(\omega),
```

gọi là **sample path**.

Một process vì vậy vừa là collection của distributions vừa là collection của possible trajectories.

Ví dụ random walk có sample path đi lên xuống từng bước; Brownian motion có continuous nhưng nowhere differentiable sample paths.

## Discrete-time và continuous-time

Nếu

```math
T=\{0,1,2,\dots\},
```

process là discrete-time. Time series và Markov chains thường nằm trong category này.

Nếu

```math
T=[0,\infty),
```

process là continuous-time. Poisson process, Brownian motion và nhiều queueing models là ví dụ.

State space cũng có thể discrete hoặc continuous, độc lập với việc time là discrete hay continuous.

## Mean function và covariance function

Mean của process tại time `t` là

```math
m(t)=E[X_t].
```

Covariance giữa hai times là

```math
C(s,t)=\operatorname{Cov}(X_s,X_t).
```

Covariance function mô tả mức độ process ở hai thời điểm cùng biến thiên.

Nếu covariance giảm khi `|t-s|` lớn, states xa nhau trong thời gian có xu hướng ít liên quan hơn.

## Stationarity

Một process **strictly stationary** nếu joint distribution không đổi khi dịch toàn bộ time indices.

Trong thực tế ta thường dùng **weak stationarity**: mean constant và covariance chỉ phụ thuộc lag

```math
\tau=t-s
```

chứ không phụ thuộc absolute time.

Khi đó

```math
C(s,t)=C(t-s).
```

Stationarity là assumption mạnh nhưng hữu ích trong signal processing và time-series analysis vì nó biến một hệ thay đổi theo time thành structure có thể học từ repeated patterns.

## Autocorrelation

Autocorrelation đo correlation giữa process và phiên bản delayed của chính nó.

Nếu process stationary,

```math
\rho(k)=\operatorname{Corr}(X_t,X_{t+k}).
```

Autocorrelation cao ở lag `k` cho thấy observation hiện tại chứa information về observation cách `k` steps.

Điều này khác ordinary correlation giữa hai variables khác nhau; đây là self-dependence across time.

## Markov property

Một process có **Markov property (마르코프 성질)** nếu future phụ thuộc current state nhưng không cần toàn bộ past khi current state đã biết.

Trong discrete time:

```math
P(X_{t+1}=x_{t+1}\mid X_t=x_t,\dots,X_0=x_0)
=
P(X_{t+1}=x_{t+1}\mid X_t=x_t).
```

Câu này không có nghĩa “future độc lập với past” theo nghĩa tuyệt đối. Nó nói current state chứa đủ relevant information từ past cho việc dự đoán next state.

## Transition matrix

Với finite-state Markov chain, define

```math
P_{ij}=P(X_{t+1}=j\mid X_t=i).
```

Matrix `P` có mỗi row sum bằng 1.

Nếu state distribution tại time `t` là row vector `π_t`, thì

```math
\pi_{t+1}=\pi_tP.
```

Sau `n` steps,

```math
\pi_{t+n}=\pi_tP^n.
```

Như vậy Markov chain nối probability với linear algebra rất trực tiếp.

## Ví dụ trạng thái hệ thống

Giả sử một service mỗi ngày ở một trong hai states: `Healthy` hoặc `Degraded`.

Transition matrix

```math
P=
\begin{bmatrix}
0.95&0.05\\
0.40&0.60
\end{bmatrix}
```

nghĩa là nếu hôm nay Healthy thì ngày mai vẫn Healthy với probability `0.95`; nếu hôm nay Degraded thì probability recover là `0.40`.

Nhân distribution vector với `P` nhiều lần cho ta long-run behavior.

## Stationary distribution

Một distribution `π` là stationary nếu

```math
\pi=\pi P.
```

Nó là left eigenvector của `P` với eigenvalue 1, sau normalization để probabilities sum bằng 1.

Under appropriate irreducibility và aperiodicity conditions, finite Markov chain có unique stationary distribution và distribution của chain hội tụ về nó bất kể initial state.

Đây là một connection đẹp giữa probability, eigenvalues và long-run dynamics.

## Irreducibility và communicating states

Hai states communicate nếu có positive-probability path từ state này tới state kia và ngược lại.

Chain irreducible nếu mọi states communicate.

Nếu chain tách thành nhiều disconnected classes, không thể mong một unique long-run distribution independent of initial state.

## Periodicity

Một state có period `d>1` nếu return times chỉ xảy ra ở multiples của `d`.

Ví dụ chain deterministic alternating giữa A và B có period 2. Distribution không settle theo cách thông thường mà oscillates.

Aperiodicity loại bỏ kiểu rigid cycling này.

## Absorbing states

State `i` absorbing nếu

```math
P_{ii}=1.
```

Một khi vào state đó chain không rời đi.

Absorbing Markov chains dùng để mô hình churn, failure, completion, bankruptcy hoặc termination states.

Ta có thể tính probability cuối cùng bị absorb ở mỗi absorbing state và expected time tới absorption.

## Random walk

Simple symmetric random walk có

```math
X_{t+1}=X_t+\varepsilon_t,
```

với

```math
P(\varepsilon_t=1)=P(\varepsilon_t=-1)=\frac12.
```

Expected position sau `t` steps vẫn bằng initial position, nhưng variance tăng tuyến tính theo time.

Random walk là model nền tảng cho diffusion, finance, queueing và stochastic algorithms.

## Poisson process

Poisson process `N(t)` mô hình số events xảy ra tới time `t` khi events đến độc lập với constant rate `λ`.

Ta có

```math
N(t)\sim\operatorname{Poisson}(\lambda t).
```

Interarrival times độc lập và exponential với mean `1/λ`.

Model này hợp lý cho rare independent arrivals trong một số hệ, nhưng không phù hợp nếu events cluster mạnh hoặc rate thay đổi theo time.

## Brownian motion

Brownian motion `W_t` là continuous-time process với

```math
W_0=0,
```

independent increments, và

```math
W_t-W_s\sim N(0,t-s)
```

cho `t>s`.

Sample paths continuous gần như chắc chắn nhưng nowhere differentiable gần như chắc chắn.

Brownian motion là building block của stochastic calculus, diffusion models và mathematical finance.

## Martingale intuition

Process `X_t` là martingale nếu conditional expectation của future state bằng current state:

```math
E[X_{t+1}\mid X_0,\dots,X_t]=X_t.
```

Nó formalize idea của “fair game”: với information hiện có, không có expected drift.

Martingale không có nghĩa values không thay đổi; uncertainty có thể tăng mạnh dù conditional mean không đổi.

## Time series: trend, seasonality và noise

Observed time series thường được conceptualize thành components như trend, seasonality và residual noise.

Một process không stationary vì trend có thể trở nên stationary sau differencing:

```math
Y_t=X_t-X_{t-1}.
```

Đây là lý do differencing xuất hiện trong classical time-series models.

## AR model

Autoregressive model bậc 1:

```math
X_t=\phi X_{t-1}+\varepsilon_t.
```

Nếu `|φ|<1`, effect của shock giảm dần và process có stationary solution dưới common assumptions.

Nếu `φ≈1`, memory rất dài. Nếu `φ=1`, ta có random-walk-like behavior.

## Moving-average model

MA(q) model viết

```math
X_t=\mu+\varepsilon_t+\theta_1\varepsilon_{t-1}+\cdots+\theta_q\varepsilon_{t-q}.
```

Current observation phụ thuộc current và recent shocks thay vì past observations trực tiếp.

AR và MA có thể combine thành ARMA; thêm differencing tạo ARIMA.

## Hidden Markov Model

Trong **Hidden Markov Model — HMM**, hidden state `Z_t` tuân Markov chain nhưng ta không observe trực tiếp. Thay vào đó observe `X_t` generated conditional on `Z_t`.

Cấu trúc này phù hợp khi system có latent regimes: speech phonemes, user intent states, machine operating modes hoặc market regimes.

Inference thường hỏi posterior probability của hidden states given observations.

## Markov Chain Monte Carlo

Markov chains còn được dùng như computational tool. Trong **MCMC**, ta thiết kế chain có stationary distribution chính là target distribution khó sample trực tiếp.

Sau burn-in và dưới suitable conditions, samples từ chain có thể dùng xấp xỉ expectations theo target distribution.

Điều này tạo bridge giữa Markov chains và Bayesian inference.

## Mental Model

Random variable mô tả uncertainty của một quantity. Stochastic process mô tả uncertainty của cả trajectory. Markov chain thêm assumption rằng current state là sufficient summary của past cho future evolution. Transition operator đóng vai trò giống dynamic rule, còn probability distribution thay thế một trajectory deterministic duy nhất.

## Common Misconceptions

Markov không có nghĩa observations liên tiếp độc lập. Ngược lại, chúng thường phụ thuộc mạnh; chỉ là dependence từ distant past được mediated qua current state.

Stationary cũng không có nghĩa process đứng yên. Sample paths vẫn dao động liên tục; chỉ statistical laws không thay đổi theo time shift.

Một autocorrelation cao không tự chứng minh causal relation. Nó chỉ cho biết temporal dependence structure.

## Liên kết kiến thức

Chapter này dựa trên [Conditional probability and Bayes](./02_conditional_probability_and_bayes.md), [Random variables and distributions](./03_random_variables_and_distributions.md), [Expectation and variance](./04_expectation_variance_and_limit_laws.md) và [Eigenvalues/eigenvectors](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md). Nó dẫn tự nhiên tới Bayesian filtering, reinforcement learning, queueing theory và stochastic differential equations.