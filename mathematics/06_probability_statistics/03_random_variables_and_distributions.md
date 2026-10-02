# Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tại sao cần random variables?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Discrete random variable và PMF** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối random variables với distributions, expectation và observation, để biến kết quả ngẫu nhiên thành đối tượng đo được.

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

> **Chuyển mạch:** Trong **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Discrete random variable và PMF** tiếp nhận điểm tựa từ **Tại sao cần random variables?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Continuous random variable và density** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Continuous random variable và density** tiếp nhận điểm tựa từ **Discrete random variable và PMF** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CDF là biểu diễn (representation / 표현) thống nhất** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **CDF là biểu diễn (representation / 표현) thống nhất** tiếp nhận điểm tựa từ **Continuous random variable và density** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân phối (distribution / 분포) không phải histogram** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Phân phối (distribution / 분포) không phải histogram** tiếp nhận điểm tựa từ **CDF là biểu diễn (representation / 표현) thống nhất** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bernoulli: đơn vị (unit / 단위) nhỏ nhất của nhị phân (binary / 이진) bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) không phải histogram

Phân phối (distribution / 분포) là population/mô hình (model / 모델) law. Histogram là một estimator/visualization từ finite mẫu (sample / 표본).

Hai samples từ cùng phân phối (distribution / 분포) cho histograms khác nhau. Một histogram mượt không chứng minh true density mượt; bin width selection ảnh hưởng appearance mạnh.

Đây là distinction giữa **mô hình (model / 모델) đối tượng (object / 객체)** và **mẫu (sample / 표본) bằng chứng (evidence / 증거)**.

> **Chuyển mạch:** Ở chặng này của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Bernoulli: đơn vị (unit / 단위) nhỏ nhất của nhị phân (binary / 이진) bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **Phân phối (distribution / 분포) không phải histogram** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Binomial: count successes từ Bernoulli trials** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Binomial: count successes từ Bernoulli trials** tiếp nhận điểm tựa từ **Bernoulli: đơn vị (unit / 단위) nhỏ nhất của nhị phân (binary / 이진) bất định (uncertainty / 불확실성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Poisson: count events trong interval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Poisson: count events trong interval** tiếp nhận điểm tựa từ **Binomial: count successes từ Bernoulli trials** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exponential phân phối (distribution / 분포) và memorylessness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Exponential phân phối (distribution / 분포) và memorylessness** tiếp nhận điểm tựa từ **Poisson: count events trong interval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Normal phân phối (distribution / 분포) và vì sao nó xuất hiện** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Normal phân phối (distribution / 분포) và vì sao nó xuất hiện** tiếp nhận điểm tựa từ **Exponential phân phối (distribution / 분포) và memorylessness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Expectation là weighted average của phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Expectation là weighted average của phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **Normal phân phối (distribution / 분포) và vì sao nó xuất hiện** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Variance: spread quanh expectation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Variance: spread quanh expectation** tiếp nhận điểm tựa từ **Expectation là weighted average của phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Worked example — transform temperature bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variance: spread quanh expectation

Variance đo độ phân tán quanh expectation bằng bình phương độ lệch. Nó nhấn mạnh các giá trị xa trung tâm và là nền cho standard deviation, risk và uncertainty propagation.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Variance: spread quanh expectation** cho ta quy tắc; **Worked example — transform temperature bất định (uncertainty / 불확실성)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Joint distributions: bất định (uncertainty / 불확실성) của nhiều quantities cùng lúc** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Worked example — transform temperature bất định (uncertainty / 불확실성)** cho ta quy tắc; **Joint distributions: bất định (uncertainty / 불확실성) của nhiều quantities cùng lúc** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Covariance và correlation chỉ tóm tắt một phần dependence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Covariance và correlation chỉ tóm tắt một phần dependence** tiếp nhận điểm tựa từ **Joint distributions: bất định (uncertainty / 불확실성) của nhiều quantities cùng lúc** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transformation của random variable và Jacobian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Covariance và correlation chỉ tóm tắt một phần dependence

Covariance và correlation nén quan hệ hai biến thành một con số, nhưng không mô tả hết phi tuyến, tail dependence hay causality. Hãy đọc chúng cùng scatterplot và mô hình sinh dữ liệu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Transformation của random variable và Jacobian** tiếp nhận điểm tựa từ **Covariance và correlation chỉ tóm tắt một phần dependence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Quantiles: đôi khi center/spread chưa đủ** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Quantiles: đôi khi center/spread chưa đủ** tiếp nhận điểm tựa từ **Transformation của random variable và Jacobian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Finance liên kết (connection / 연결) — returns và tail dependence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Quantiles: đôi khi center/spread chưa đủ

Quantile `q_p` thỏa roughly

```math
P(X\le q_p)=p.
```

Median là 50th percentile. Tail metrics như 95th/99th percentile rất quan trọng cho độ trễ (latency / 지연 시간), rủi ro (risk / 위험) và độ tin cậy (reliability / 신뢰성).

Hai distributions cùng mean/variance vẫn có tails khác mạnh, nên high-percentile hành vi (behavior / 동작) có thể hoàn toàn khác.

> **Chuyển mạch:** Ở chặng này của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, sau nội dung của **Quantiles: đôi khi center/spread chưa đủ**, **Finance liên kết (connection / 연결) — returns và tail dependence** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **AI liên kết (connection / 연결) — đầu ra (output / 출력) distributions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Finance liên kết (connection / 연결) — returns và tail dependence

Asset returns rarely fully described by Gaussian mean/covariance. Skewness, heavy tails và correlated crashes matter.

Joint phân phối (distribution / 분포) determines portfolio rủi ro (risk / 위험). Correlation estimated trong normal periods có thể underestimate dependence during stress.

Phân phối (distribution / 분포) choice therefore encodes rủi ro (risk / 위험) các giả định (assumptions / 가정들), not just curve-fitting convenience.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **AI liên kết (connection / 연결) — đầu ra (output / 출력) distributions** tiếp nhận điểm tựa từ **Finance liên kết (connection / 연결) — returns và tail dependence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phân phối (distribution / 분포) choice là giả định (assumption / 가정) gói (package / 패키지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AI liên kết (connection / 연결) — đầu ra (output / 출력) distributions

Classification mô hình (model / 모델) often estimates categorical probabilities; regression mô hình (model / 모델) có thể predict mean only hoặc full conditional phân phối (distribution / 분포).

Negative log-likelihood huấn luyện (training / 학습) depends on assumed đầu ra (output / 출력) phân phối (distribution / 분포). Squared lỗi (error / 오류) corresponds to Gaussian-noise các giả định (assumptions / 가정들) under dùng chung (common / 공통) setup; cross-entropy corresponds to categorical/Bernoulli likelihood structures.

Hàm mất mát (loss function / 손실 함수) và xác suất (probability / 확률) mô hình (model / 모델) are linked.

> **Chuyển mạch:** Trong **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Phân phối (distribution / 분포) choice là giả định (assumption / 가정) gói (package / 패키지)** tiếp nhận điểm tựa từ **AI liên kết (connection / 연결) — đầu ra (output / 출력) distributions** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phân phối (distribution / 분포) choice là giả định (assumption / 가정) gói (package / 패키지)

Chọn distribution đồng nghĩa chọn một gói giả định về support, tail, symmetry và dependence. Vì vậy cần kiểm tra dữ liệu và mục đích suy luận trước khi chọn tên phân phối quen thuộc.

- Binomial: fixed trials, binary outcome, often independence/constant `p`.
- Poisson: event-count mechanism with approximately stable independent increments.
- Normal: symmetric light-tailed continuous variation.
- Exponential: memoryless waiting times.
- Heavy-tailed các mô hình (models / 모델들): larger extreme-event probabilities.

Tên phân phối (distribution / 분포) không chỉ chọn formula; nó chọn a story about cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Ở chặng này của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Phân phối (distribution / 분포) choice là giả định (assumption / 가정) gói (package / 패키지)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Random variable is a đo lường (measurement / 측정) hàm (function / 함수) on uncertain outcomes. phân phối (distribution / 분포) tells how xác suất (probability / 확률) is pushed onto the numerical quy mô (scale / 규모) created by that hàm (function / 함수). PMF/density/CDF are different representations of the same probabilistic law; expectation, variance and quantiles are summaries; joint distributions preserve dependence cấu trúc (structure / 구조) that one-dimensional summaries lose.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Biến ngẫu nhiên và phân phối: biến outcomes thành quantities có thể tính toán**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Dùng chung (common / 공통) Misconceptions

**“Density tại `x` là xác suất (probability / 확률) của `x`.”** Không trong continuous trường hợp (case / 사례); xác suất (probability / 확률) là area.

**“Normal là default phân phối (distribution / 분포) cho mọi đo lường (measurement / 측정).”** Không. cơ chế (mechanism / 메커니즘), hỗ trợ (support / 지원) và tails phải phù hợp.

**“Mean và tiêu chuẩn (standard / 표준) deviation mô tả hết phân phối (distribution / 분포).”** Chỉ với restricted families như Gaussian mới gần như vậy; generally tails/skew/dependence còn rất nhiều thông tin (information / 정보).

**“Zero correlation nghĩa independent.”** Sai trong general trường hợp (case / 사례).

**“Chọn Poisson/binomial chỉ là chọn formula.”** Mỗi distribution kéo theo assumptions về data-generating process.

> **Bàn giao:** Sau **Dùng chung (common / 공통) Misconceptions**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
