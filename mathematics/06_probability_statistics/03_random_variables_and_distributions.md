# Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán

> **Mạch đọc:** Đọc **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Tại sao cần random variables?** sang **Discrete random variable và PMF**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Biến ngẫu nhiên (random variable / 확률변수) không phải là một “biến tự nhiên nhảy lung tung”. Formal definition đúng hơn: nó là một hàm (function / 함수) ánh xạ mỗi kết quả (outcome / 결과) trong mẫu (sample / 표본) không gian (space / 공간) thành một number.

```math
X:\Omega\to\mathbb R.
```

Randomness nằm ở kết quả (outcome / 결과) chưa biết; `X` chỉ là quy tắc (rule / 규칙) trích một quantity từ kết quả (outcome / 결과) đó. Cách nhìn này rất quan trọng vì nó nối xác suất (probability / 확률) với functions, measure, expectation, statistics và machine học tập (learning / 학습).

## Tại sao cần random variables?

Raw outcomes thường quá chi tiết. Trong ba coin tosses, mẫu (sample / 표본) kết quả (outcome / 결과) có thể là `HTH`, nhưng nhiều câu hỏi chỉ quan tâm **number of heads**.

Ta định nghĩa

```math
X(HTH)=2.
```

Nhiều outcomes khác nhau có thể map tới cùng giá trị (value / 값). Random variable compresses kết quả (outcome / 결과) không gian (space / 공간) thành numerical quantity relevant cho question.

## Discrete random variable và PMF

Nếu possible values countable, xác suất (probability / 확률) mass hàm (function / 함수) là

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

PMF là phân phối (distribution / 분포) of xác suất (probability / 확률) mass over possible values.

## Continuous random variable và density

Với continuous random variable, chính xác (exact / 정확한) điểm (point / 지점) thường có xác suất (probability / 확률) zero:

```math
P(X=x)=0.
```

Xác suất (probability / 확률) của interval được tính bằng density:

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

Density có đơn vị (unit / 단위) inverse của variable. Nếu `X` đo seconds, density có đơn vị (unit / 단위) `1/second`. Vì vậy density giá trị (value / 값) có thể lớn hơn 1 mà xác suất (probability / 확률) vẫn hợp lệ; xác suất (probability / 확률) là **area**, không phải height.

## CDF là biểu diễn (representation / 표현) thống nhất

Cumulative phân phối (distribution / 분포) hàm (function / 함수):

```math
F_X(x)=P(X\le x).
```

CDF tồn tại cho discrete, continuous và mixed distributions. Nó nondecreasing, right-continuous, tiến về 0 ở `-∞` và 1 ở `+∞`.

Nếu density tồn tại đủ regular:

```math
f_X(x)=F_X'(x).
```

Trong discrete trường hợp (case / 사례), CDF có jumps; jump kích thước (size / 크기) chính là điểm (point / 지점) xác suất (probability / 확률).

## Phân phối (distribution / 분포) không phải histogram

Phân phối (distribution / 분포) là population/mô hình (model / 모델) law. Histogram là một estimator/visualization từ finite mẫu (sample / 표본).

Hai samples từ cùng phân phối (distribution / 분포) cho histograms khác nhau. Một histogram mượt không chứng minh true density mượt; bin width selection ảnh hưởng appearance mạnh.

Đây là distinction giữa **mô hình (model / 모델) đối tượng (object / 객체)** và **mẫu (sample / 표본) bằng chứng (evidence / 증거)**.

## Bernoulli: đơn vị (unit / 단위) nhỏ nhất của nhị phân (binary / 이진) bất định (uncertainty / 불확실성)

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

Một nhị phân (binary / 이진) indicator sự kiện (event / 이벤트) `A` có thể viết

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

Indicator variables là cầu nối (bridge / 브리지) cực mạnh giữa xác suất (probability / 확률) và combinatorics.

## Binomial: count successes từ Bernoulli trials

Nếu

```math
X=X_1+\cdots+X_n
```

với `X_i` independent Bernoulli(`p`), thì

```math
X\sim Bin(n,p).
```

Xác suất (probability / 확률) exactly `k` successes:

```math
P(X=k)
=
\binom nkp^k(1-p)^{n-k}.
```

`p^k(1-p)^{n-k}` là xác suất (probability / 확률) của one particular success/thất bại (failure / 실패) arrangement. `\binom nk` đếm số arrangements tạo cùng count.

Các giả định (assumptions / 가정들) gồm fixed `n`, nhị phân (binary / 이진) trials, constant `p` và independence. Nếu xác suất (probability / 확률) changes theo thời gian (time / 시간) hoặc trials dependent, binomial mô hình (model / 모델) không còn chính xác (exact / 정확한).

## Poisson: count events trong interval

Poisson phân phối (distribution / 분포):

```math
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
```

Nó phù hợp khi events occur roughly independently, tỷ lệ (rate / 비율) approximately constant và simultaneous events negligible ở tiny intervals.

Mean và variance đều bằng `\lambda`:

```math
E[X]=Var(X)=\lambda.
```

Nếu observed variance lớn hơn mean nhiều, dữ liệu (data / 데이터) có overdispersion; simple Poisson mô hình (model / 모델) có thể miss hidden heterogeneity/dependence.

## Exponential phân phối (distribution / 분포) và memorylessness

Nếu Poisson tiến trình (process / 프로세스) có tỷ lệ (rate / 비율) `\lambda`, waiting thời gian (time / 시간) giữa events có exponential phân phối (distribution / 분포):

```math
f(t)=\lambda e^{-\lambda t},\qquad t\ge0.
```

Memoryless thuộc tính (property / 속성):

```math
P(T>s+t\mid T>s)=P(T>t).
```

Nghĩa là conditional remaining-time phân phối (distribution / 분포) không depend on elapsed thời gian (time / 시간). Đây là giả định (assumption / 가정) mạnh; human thời gian tồn tại (lifetime / 수명), hardware aging và many queues không memoryless.

## Normal phân phối (distribution / 분포) và vì sao nó xuất hiện

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

Nhưng “dữ liệu (data / 데이터) có nhiều factors” không tự động guarantee normality. Heavy tails, skewness, dependence hoặc bounds có thể làm Gaussian giả định (assumption / 가정) poor.

## Expectation là weighted average của phân phối (distribution / 분포)

Discrete:

```math
E[X]=\sum_xxP(X=x).
```

Continuous:

```math
E[X]=\int xf_X(x)\,dx.
```

Expectation là center theo xác suất (probability / 확률) weights, không nhất thiết là typical kết quả (outcome / 결과).

Linearity:

```math
E[aX+bY]=aE[X]+bE[Y]
```

không cần independence.

Đây là một trong những rules useful nhất trong xác suất (probability / 확률).

## Variance: spread quanh expectation

```math
Var(X)=E[(X-E[X])^2].
```

Equivalent:

```math
Var(X)=E[X^2]-E[X]^2.
```

Tiêu chuẩn (standard / 표준) deviation

```math
\sigma=\sqrt{Var(X)}
```

trở lại same đơn vị (unit / 단위) as `X`.

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

Shift không đổi spread; quy mô (scale / 규모) multiply deviations.

## Worked example — transform temperature bất định (uncertainty / 불확실성)

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

Translation +32 đổi location, không đổi deviations. quy mô (scale / 규모) 1.8 quy mô (scale / 규모) tiêu chuẩn (standard / 표준) deviation.

## Joint distributions: bất định (uncertainty / 불확실성) của nhiều quantities cùng lúc

Với `X,Y`, joint phân phối (distribution / 분포) mô tả pairs `(X,Y)`. Marginal phân phối (distribution / 분포) của `X` lấy bằng sum/integrate out `Y`.

Discrete:

```math
P(X=x)=\sum_yP(X=x,Y=y).
```

Conditional phân phối (distribution / 분포):

```math
P(X=x\mid Y=y)
```

cho phân phối (distribution / 분포) của `X` sau khi thông tin (information / 정보) `Y=y` được biết.

Joint → marginal → conditional là cốt lõi (core / 핵심) phụ thuộc (dependency / 의존성) cho statistics và Bayesian suy luận (inference / 추론).

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

Phân phối (distribution / 분포) của `Y` được induce từ `X`.

Với monotone differentiable `g`:

```math
f_Y(y)
=
f_X(g^{-1}(y))
\left|\frac{d}{dy}g^{-1}(y)\right|.
```

Jacobian factor xuất hiện vì xác suất (probability / 확률) mass phải được bảo toàn khi coordinates stretch/compress.

Đây là cùng change-of-variables cấu trúc (structure / 구조) trong multivariable tích hợp (integration / 통합) và normalizing flows.

## Quantiles: đôi khi center/spread chưa đủ

Quantile `q_p` thỏa roughly

```math
P(X\le q_p)=p.
```

Median là 50th percentile. Tail metrics như 95th/99th percentile rất quan trọng cho độ trễ (latency / 지연 시간), rủi ro (risk / 위험) và độ tin cậy (reliability / 신뢰성).

Hai distributions cùng mean/variance vẫn có tails khác mạnh, nên high-percentile hành vi (behavior / 동작) có thể hoàn toàn khác.

## Finance liên kết (connection / 연결) — returns và tail dependence

Asset returns rarely fully described by Gaussian mean/covariance. Skewness, heavy tails và correlated crashes matter.

Joint phân phối (distribution / 분포) determines portfolio rủi ro (risk / 위험). Correlation estimated trong normal periods có thể underestimate dependence during stress.

Phân phối (distribution / 분포) choice therefore encodes rủi ro (risk / 위험) các giả định (assumptions / 가정들), not just curve-fitting convenience.

## AI liên kết (connection / 연결) — đầu ra (output / 출력) distributions

Classification mô hình (model / 모델) often estimates categorical probabilities; regression mô hình (model / 모델) có thể predict mean only hoặc full conditional phân phối (distribution / 분포).

Negative log-likelihood huấn luyện (training / 학습) depends on assumed đầu ra (output / 출력) phân phối (distribution / 분포). Squared lỗi (error / 오류) corresponds to Gaussian-noise các giả định (assumptions / 가정들) under dùng chung (common / 공통) setup; cross-entropy corresponds to categorical/Bernoulli likelihood structures.

Hàm mất mát (loss function / 손실 함수) và xác suất (probability / 확률) mô hình (model / 모델) are linked.

## Phân phối (distribution / 분포) choice là giả định (assumption / 가정) gói (package / 패키지)

- Binomial: fixed trials, nhị phân (binary / 이진) kết quả (outcome / 결과), often independence/constant `p`.
- Poisson: event-count cơ chế (mechanism / 메커니즘) with approximately stable independent increments.
- Normal: symmetric light-tailed continuous variation.
- Exponential: memoryless waiting times.
- Heavy-tailed các mô hình (models / 모델들): larger extreme-event probabilities.

Tên phân phối (distribution / 분포) không chỉ chọn formula; nó chọn a story about cơ chế (mechanism / 메커니즘).

## Mô hình tư duy (mental model / 사고 모델)

> Random variable is a đo lường (measurement / 측정) hàm (function / 함수) on uncertain outcomes. phân phối (distribution / 분포) tells how xác suất (probability / 확률) is pushed onto the numerical quy mô (scale / 규모) created by that hàm (function / 함수). PMF/density/CDF are different representations of the same probabilistic law; expectation, variance and quantiles are summaries; joint distributions preserve dependence cấu trúc (structure / 구조) that one-dimensional summaries lose.

## Dùng chung (common / 공통) Misconceptions

**“Density tại `x` là xác suất (probability / 확률) của `x`.”** Không trong continuous trường hợp (case / 사례); xác suất (probability / 확률) là area.

**“Normal là default phân phối (distribution / 분포) cho mọi đo lường (measurement / 측정).”** Không. cơ chế (mechanism / 메커니즘), hỗ trợ (support / 지원) và tails phải phù hợp.

**“Mean và tiêu chuẩn (standard / 표준) deviation mô tả hết phân phối (distribution / 분포).”** Chỉ với restricted families như Gaussian mới gần như vậy; generally tails/skew/dependence còn rất nhiều thông tin (information / 정보).

**“Zero correlation nghĩa independent.”** Sai trong general trường hợp (case / 사례).

**“Chọn Poisson/binomial chỉ là chọn formula.”** Mỗi phân phối (distribution / 분포) kéo theo các giả định (assumptions / 가정들) về data-generating tiến trình (process / 프로세스).

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 counting and combinatorics](./00_counting_and_combinatorics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
