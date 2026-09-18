# Các phân phối xác suất thường gặp và vì sao chúng xuất hiện

Học distribution bằng một bảng tên–công thức rất dễ quên. Cách tốt hơn là hỏi **process nào sinh ra distribution đó**. Distribution không phải decoration; nó là model của mechanism ngẫu nhiên.

## Bernoulli: một trial có hai outcome

Bernoulli random variable `X` nhận `1` với probability `p` và `0` với probability `1-p`.

```math
E[X]=p,
```

```math
\operatorname{Var}(X)=p(1-p).
```

Click/no-click, success/failure, defective/non-defective là examples khi outcome được idealize thành binary.

## Binomial: đếm successes trong fixed number trials

Nếu có `n` independent Bernoulli trials cùng probability `p`, số successes `X` có binomial distribution:

```math
P(X=k)=\binom nk p^k(1-p)^{n-k}.
```

Combination factor đếm số cách chọn `k` positions success trong `n` trials.

Mean và variance:

```math
E[X]=np,
```

```math
\operatorname{Var}(X)=np(1-p).
```

Nếu independence hoặc constant `p` không hợp lý, binomial model có thể sai dù data vẫn là counts.

## Geometric: chờ tới success đầu tiên

Nếu mỗi trial independent với probability success `p`, số trials đến success đầu tiên có

```math
P(X=k)=(1-p)^{k-1}p.
```

Geometric distribution có memoryless property:

```math
P(X>s+t\mid X>s)=P(X>t).
```

Past failures không thay đổi future success probability trong model.

## Poisson: số events trong interval

Poisson distribution model count events khi events xảy ra với average rate `\lambda` và assumptions về independent increments/small interval behavior phù hợp:

```math
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
```

Mean và variance đều bằng `\lambda`.

Poisson thường là approximation của binomial khi `n` lớn, `p` nhỏ và `np\approx\lambda`.

## Exponential: waiting time trong Poisson process

Nếu events theo Poisson process rate `\lambda`, waiting time `T` tới event tiếp theo có density

```math
f(t)=\lambda e^{-\lambda t},\qquad t\ge0.
```

Mean:

```math
E[T]=\frac1\lambda.
```

Exponential cũng memoryless. Đây là continuous analog của geometric waiting time.

## Uniform: không ưu tiên vị trí nào trong interval

Continuous uniform trên `[a,b]` có density constant:

```math
f(x)=\frac1{b-a}.
```

Equal-length subintervals có equal probability. Uniform phù hợp khi mechanism thực sự symmetric theo position trong range, không phải chỉ vì “ta không biết gì”.

## Normal/Gaussian: tổng của nhiều contributions nhỏ

Normal density:

```math
f(x)=\frac{1}{\sigma\sqrt{2\pi}}
\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
```

Nó xuất hiện tự nhiên qua Central Limit Theorem: tổng/average của nhiều contributions tương đối độc lập với finite variance thường có distribution gần Gaussian sau chuẩn hóa.

Vì vậy measurement errors, aggregate variation và sample means thường gần normal hơn raw mechanisms riêng lẻ.

Normal không phải “distribution mặc định của mọi data”. Heavy tails, skewness, boundedness hoặc multimodality có thể làm Gaussian model rất sai.

## Student's t: uncertainty khi variance được estimate

Khi estimate mean của normal population nhưng `\sigma` unknown, standardized statistic dùng sample standard deviation có `t` distribution thay vì exact normal.

`t` có heavier tails, phản ánh additional uncertainty do estimate `\sigma`. Khi degrees of freedom tăng, `t` tiến gần standard normal.

## Chi-square và F

Nếu `Z_i` independent standard normal, sum of squares

```math
\sum_{i=1}^k Z_i^2
```

có chi-square distribution với `k` degrees of freedom.

Chi-square xuất hiện trong variance inference và goodness-of-fit. Ratio của scaled independent chi-square variables dẫn tới F distribution, nền của classical ANOVA và variance comparison.

## Beta: probability parameter trên [0,1]

Beta distribution có density proportional với

```math
p^{\alpha-1}(1-p)^{\beta-1},\qquad 0<p<1.
```

Nó linh hoạt cho quantities bounded trong `[0,1]` và là conjugate prior cho Bernoulli/binomial likelihood trong Bayesian inference.

Posterior update rất trực quan: successes/failures cộng vào shape parameters.

## Gamma: positive waiting/scale quantities

Gamma generalizes exponential và thường model waiting time đến nhiều events hoặc positive continuous quantities với right skew.

Nếu waiting times exponential independent, tổng của nhiều waiting times có gamma distribution.

## Chọn distribution theo mechanism, support và assumptions

Trước khi chọn distribution, hỏi:

- variable là discrete count hay continuous measurement;
- support là `0/1`, nonnegative integers, positive reals, bounded interval hay toàn real line;
- process là fixed trials, waiting time, sum of effects hay rate process;
- independence và stationarity assumptions có hợp lý không.

Distribution fitting chỉ nhìn histogram mà không xét mechanism dễ tạo model đẹp nhưng vô nghĩa.

## Knowledge Connection

Bernoulli/binomial nối combinatorics với likelihood. Poisson/exponential nối count process với waiting time. Normal nối sums với CLT. `t`, chi-square và F nối Gaussian geometry với inference. Beta/Gamma nối probability với Bayesian updating.

## Mental Model

> Một distribution là dấu vân tay của một stochastic mechanism. Thay vì nhớ tên theo hình curve, hãy nhớ câu chuyện sinh dữ liệu: đếm successes, chờ event, cộng nhiều nhiễu nhỏ, hay biểu diễn uncertainty của một probability parameter.

## Common Misconceptions

Normality không phải requirement cho mọi statistical method theo cùng mức độ. Poisson không phù hợp nếu variance khác mean quá mạnh do overdispersion. Uniform không có nghĩa “không biết gì” trong mọi parameterization. Continuous density tại một point không phải probability tại point đó; probability đến từ area/integral.
