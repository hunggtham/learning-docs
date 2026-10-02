# Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mẫu (sample / 표본) đường dẫn (path / 경로) và phân phối (distribution / 분포)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Discrete-time và continuous-time** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối stochastic processes với Markov chains và time series, để trạng thái hiện tại, phụ thuộc thời gian và dự báo dùng đúng mô hình.

Xác suất (probability / 확률) cơ bản thường mô tả một random variable tại một thời điểm. Nhưng nhiều hệ thực tế thay đổi theo thời gian: giá tài sản, số yêu cầu (request / 요청) đến máy chủ (server / 서버), trạng thái người dùng (user / 사용자), packet hàng đợi (queue / 큐), nhiệt độ, tín hiệu cảm biến, gene expression hay vị trí robot. Để mô tả những hệ như vậy ta cần **stochastic tiến trình (process / 프로세스)**.

Một stochastic tiến trình (process / 프로세스) là một family các random variables được chỉ mục (index / 인덱스) bởi thời gian (time / 시간) hoặc một parameter khác:

```math
\{X_t:t\in T\}.
```

Với mỗi thời điểm `t`, `X_t` là random variable. Nhưng điều quan trọng không chỉ là phân phối (distribution / 분포) riêng lẻ của từng `X_t`; ta cần phụ thuộc (dependency / 의존성) cấu trúc (structure / 구조) giữa các thời điểm.

## Mẫu (sample / 표본) đường dẫn (path / 경로) và phân phối (distribution / 분포)

Có hai cách nhìn song song. Nếu cố định thời gian (time / 시간) `t`, `X_t` là random variable. Nếu cố định một kết quả (outcome / 결과) `ω`, ta thu được một hàm (function / 함수) theo thời gian (time / 시간)

```math
t\mapsto X_t(\omega),
```

gọi là **mẫu (sample / 표본) đường dẫn (path / 경로)**.

Một tiến trình (process / 프로세스) vì vậy vừa là collection của distributions vừa là collection của possible trajectories.

Ví dụ random walk có mẫu (sample / 표본) đường dẫn (path / 경로) đi lên xuống từng bước; Brownian motion có continuous nhưng nowhere differentiable mẫu (sample / 표본) paths.

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Mẫu (sample / 표본) đường dẫn (path / 경로) và phân phối (distribution / 분포)** xác định đầu vào; **Discrete-time và continuous-time** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mean hàm (function / 함수) và covariance hàm (function / 함수)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Discrete-time và continuous-time

Nếu

```math
T=\{0,1,2,\dots\},
```

Tiến trình (process / 프로세스) là discrete-time. thời gian (time / 시간) series và Markov chains thường nằm trong category này.

Nếu

```math
T=[0,\infty),
```

Tiến trình (process / 프로세스) là continuous-time. Poisson tiến trình (process / 프로세스), Brownian motion và nhiều queueing các mô hình (models / 모델들) là ví dụ.

Trạng thái (state / 상태) không gian (space / 공간) cũng có thể discrete hoặc continuous, độc lập với việc thời gian (time / 시간) là discrete hay continuous.

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Mean hàm (function / 함수) và covariance hàm (function / 함수)** tiếp nhận điểm tựa từ **Discrete-time và continuous-time** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Stationarity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mean hàm (function / 함수) và covariance hàm (function / 함수)

Mean của tiến trình (process / 프로세스) tại thời gian (time / 시간) `t` là

```math
m(t)=E[X_t].
```

Covariance giữa hai times là

```math
C(s,t)=\operatorname{Cov}(X_s,X_t).
```

Covariance hàm (function / 함수) mô tả mức độ tiến trình (process / 프로세스) ở hai thời điểm cùng biến thiên.

Nếu covariance giảm khi `|t-s|` lớn, states xa nhau trong thời gian có xu hướng ít liên quan hơn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Stationarity** tiếp nhận điểm tựa từ **Mean hàm (function / 함수) và covariance hàm (function / 함수)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Autocorrelation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stationarity

Một tiến trình (process / 프로세스) **strictly stationary** nếu joint phân phối (distribution / 분포) không đổi khi dịch toàn bộ thời gian (time / 시간) indices.

Trong thực tế ta thường dùng **weak stationarity**: mean constant và covariance chỉ phụ thuộc lag

```math
\tau=t-s
```

chứ không phụ thuộc absolute thời gian (time / 시간).

Khi đó

```math
C(s,t)=C(t-s).
```

Stationarity là giả định (assumption / 가정) mạnh nhưng hữu ích trong tín hiệu (signal / 신호) processing và time-series phân tích (analysis / 분석) vì nó biến một hệ thay đổi theo thời gian (time / 시간) thành cấu trúc (structure / 구조) có thể học từ repeated patterns.

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Autocorrelation** tiếp nhận điểm tựa từ **Stationarity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Markov thuộc tính (property / 속성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Autocorrelation

Autocorrelation đo correlation giữa tiến trình (process / 프로세스) và phiên bản delayed của chính nó.

Nếu tiến trình (process / 프로세스) stationary,

```math
\rho(k)=\operatorname{Corr}(X_t,X_{t+k}).
```

Autocorrelation cao ở lag `k` cho thấy observation hiện tại chứa thông tin (information / 정보) về observation cách `k` steps.

Điều này khác ordinary correlation giữa hai variables khác nhau; đây là self-dependence across thời gian (time / 시간).

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Markov thuộc tính (property / 속성)** tiếp nhận điểm tựa từ **Autocorrelation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuyển tiếp (transition / 전이) ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Markov thuộc tính (property / 속성)

Một tiến trình (process / 프로세스) có **Markov thuộc tính (property / 속성)** nếu future phụ thuộc trạng thái hiện tại (current state / 현재 상태) nhưng không cần toàn bộ past khi trạng thái hiện tại (current state / 현재 상태) đã biết.

Trong discrete thời gian (time / 시간):

```math
P(X_{t+1}=x_{t+1}\mid X_t=x_t,\dots,X_0=x_0)
=
P(X_{t+1}=x_{t+1}\mid X_t=x_t).
```

Câu này không có nghĩa “future độc lập với past” theo nghĩa tuyệt đối. Nó nói trạng thái hiện tại (current state / 현재 상태) chứa đủ relevant thông tin (information / 정보) từ past cho việc dự đoán next trạng thái (state / 상태).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Chuyển tiếp (transition / 전이) ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **Markov thuộc tính (property / 속성)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ví dụ trạng thái hệ thống** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuyển tiếp (transition / 전이) ma trận (matrix / 행렬)

Với finite-state Markov chuỗi (chain / 사슬), define

```math
P_{ij}=P(X_{t+1}=j\mid X_t=i).
```

Ma trận (matrix / 행렬) `P` có mỗi row sum bằng 1.

Nếu trạng thái (state / 상태) phân phối (distribution / 분포) tại thời gian (time / 시간) `t` là row véc-tơ (vector / 벡터) `π_t`, thì

```math
\pi_{t+1}=\pi_tP.
```

Sau `n` steps,

```math
\pi_{t+n}=\pi_tP^n.
```

Như vậy Markov chuỗi (chain / 사슬) nối xác suất (probability / 확률) với tuyến tính (linear / 선형) algebra rất trực tiếp.

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Chuyển tiếp (transition / 전이) ma trận (matrix / 행렬)** cho ta quy tắc; **Ví dụ trạng thái hệ thống** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Stationary phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ví dụ trạng thái hệ thống

Giả sử một dịch vụ (service / 서비스) mỗi ngày ở một trong hai states: `Healthy` hoặc `Degraded`.

Chuyển tiếp (transition / 전이) ma trận (matrix / 행렬)

```math
P=
\begin{bmatrix}
0.95&0.05\\
0.40&0.60
\end{bmatrix}
```

nghĩa là nếu hôm nay Healthy thì ngày mai vẫn Healthy với xác suất (probability / 확률) `0.95`; nếu hôm nay Degraded thì xác suất (probability / 확률) recover là `0.40`.

Nhân phân phối (distribution / 분포) véc-tơ (vector / 벡터) với `P` nhiều lần cho ta long-run hành vi (behavior / 동작).

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Ví dụ trạng thái hệ thống** cho ta quy tắc; **Stationary phân phối (distribution / 분포)** đặt quy tắc ấy vào tình huống cụ thể để thấy nó hoạt động đến đâu. Từ đây, **Irreducibility và communicating states** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stationary phân phối (distribution / 분포)

Một phân phối (distribution / 분포) `π` là stationary nếu

```math
\pi=\pi P.
```

Nó là left eigenvector của `P` với eigenvalue 1, sau normalization để probabilities sum bằng 1.

Under appropriate irreducibility và aperiodicity conditions, finite Markov chuỗi (chain / 사슬) có unique stationary phân phối (distribution / 분포) và phân phối (distribution / 분포) của chuỗi (chain / 사슬) hội tụ về nó bất kể initial trạng thái (state / 상태).

Đây là một liên kết (connection / 연결) đẹp giữa xác suất (probability / 확률), eigenvalues và long-run dynamics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Irreducibility và communicating states** tiếp nhận điểm tựa từ **Stationary phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Periodicity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Irreducibility và communicating states

Hai states communicate nếu có positive-probability đường dẫn (path / 경로) từ trạng thái (state / 상태) này tới trạng thái (state / 상태) kia và ngược lại.

Chuỗi (chain / 사슬) irreducible nếu mọi states communicate.

Nếu chuỗi (chain / 사슬) tách thành nhiều disconnected classes, không thể mong một unique long-run phân phối (distribution / 분포) independent of initial trạng thái (state / 상태).

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Periodicity** tiếp nhận điểm tựa từ **Irreducibility và communicating states** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Absorbing states** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Periodicity

Một trạng thái (state / 상태) có period `d>1` nếu return times chỉ xảy ra ở multiples của `d`.

Ví dụ chuỗi (chain / 사슬) deterministic alternating giữa A và B có period 2. phân phối (distribution / 분포) không settle theo cách thông thường mà oscillates.

Aperiodicity loại bỏ kiểu rigid cycling này.

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Absorbing states** tiếp nhận điểm tựa từ **Periodicity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Random walk** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Absorbing states

Trạng thái (state / 상태) `i` absorbing nếu

```math
P_{ii}=1.
```

Một khi vào trạng thái (state / 상태) đó chuỗi (chain / 사슬) không rời đi.

Absorbing Markov chains dùng để mô hình churn, thất bại (failure / 실패), completion, bankruptcy hoặc termination states.

Ta có thể tính xác suất (probability / 확률) cuối cùng bị absorb ở mỗi absorbing trạng thái (state / 상태) và expected thời gian (time / 시간) tới absorption.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Random walk** tiếp nhận điểm tựa từ **Absorbing states** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Poisson tiến trình (process / 프로세스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Random walk

Simple symmetric random walk có

```math
X_{t+1}=X_t+\varepsilon_t,
```

với

```math
P(\varepsilon_t=1)=P(\varepsilon_t=-1)=\frac12.
```

Expected position sau `t` steps vẫn bằng initial position, nhưng variance tăng tuyến tính theo thời gian (time / 시간).

Random walk là mô hình (model / 모델) nền tảng cho diffusion, finance, queueing và stochastic algorithms.

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Random walk** xác định đầu vào; **Poisson tiến trình (process / 프로세스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Brownian motion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Poisson tiến trình (process / 프로세스)

Poisson tiến trình (process / 프로세스) `N(t)` mô hình số events xảy ra tới thời gian (time / 시간) `t` khi events đến độc lập với constant tỷ lệ (rate / 비율) `λ`.

Ta có

```math
N(t)\sim\operatorname{Poisson}(\lambda t).
```

Interarrival times độc lập và exponential với mean `1/λ`.

Mô hình (model / 모델) này hợp lý cho rare independent arrivals trong một số hệ, nhưng không phù hợp nếu events cluster mạnh hoặc tỷ lệ (rate / 비율) thay đổi theo thời gian (time / 시간).

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Poisson tiến trình (process / 프로세스)** xác định đầu vào; **Brownian motion** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Martingale intuition** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Brownian motion

Brownian motion `W_t` là continuous-time tiến trình (process / 프로세스) với

```math
W_0=0,
```

independent increments, và

```math
W_t-W_s\sim N(0,t-s)
```

cho `t>s`.

Mẫu (sample / 표본) paths continuous gần như chắc chắn nhưng nowhere differentiable gần như chắc chắn.

Brownian motion là building khối (block / 블록) của stochastic calculus, diffusion các mô hình (models / 모델들) và mathematical finance.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Martingale intuition** tiếp nhận điểm tựa từ **Brownian motion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Thời gian (time / 시간) series: trend, seasonality và noise** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Martingale intuition

Tiến trình (process / 프로세스) `X_t` là martingale nếu conditional expectation của future trạng thái (state / 상태) bằng trạng thái hiện tại (current state / 현재 상태):

```math
E[X_{t+1}\mid X_0,\dots,X_t]=X_t.
```

Nó formalize idea của “fair game”: với thông tin (information / 정보) hiện có, không có expected drift.

Martingale không có nghĩa values không thay đổi; bất định (uncertainty / 불확실성) có thể tăng mạnh dù conditional mean không đổi.

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Thời gian (time / 시간) series: trend, seasonality và noise** tiếp nhận điểm tựa từ **Martingale intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **AR mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Thời gian (time / 시간) series: trend, seasonality và noise

Observed thời gian (time / 시간) series thường được conceptualize thành components như trend, seasonality và residual noise.

Một tiến trình (process / 프로세스) không stationary vì trend có thể trở nên stationary sau differencing:

```math
Y_t=X_t-X_{t-1}.
```

Đây là lý do differencing xuất hiện trong classical time-series các mô hình (models / 모델들).

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **AR mô hình (model / 모델)** tiếp nhận điểm tựa từ **Thời gian (time / 시간) series: trend, seasonality và noise** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Moving-average mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## AR mô hình (model / 모델)

Autoregressive mô hình (model / 모델) bậc 1:

```math
X_t=\phi X_{t-1}+\varepsilon_t.
```

Nếu `|φ|<1`, tác động (effect / 효과) của shock giảm dần và tiến trình (process / 프로세스) có stationary solution dưới dùng chung (common / 공통) các giả định (assumptions / 가정들).

Nếu `φ≈1`, bộ nhớ (memory / 메모리) rất dài. Nếu `φ=1`, ta có random-walk-like hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Moving-average mô hình (model / 모델)** tiếp nhận điểm tựa từ **AR mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hidden Markov mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Moving-average mô hình (model / 모델)

MA(q) mô hình (model / 모델) viết

```math
X_t=\mu+\varepsilon_t+\theta_1\varepsilon_{t-1}+\cdots+\theta_q\varepsilon_{t-q}.
```

Hiện tại (current / 현재) observation phụ thuộc hiện tại (current / 현재) và recent shocks thay vì past observations trực tiếp.

AR và MA có thể combine thành ARMA; thêm differencing tạo ARIMA.

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Hidden Markov mô hình (model / 모델)** tiếp nhận điểm tựa từ **Moving-average mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Markov chuỗi (chain / 사슬) Monte Carlo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hidden Markov mô hình (model / 모델)

Trong **Hidden Markov mô hình (model / 모델) — HMM**, hidden trạng thái (state / 상태) `Z_t` tuân Markov chuỗi (chain / 사슬) nhưng ta không observe trực tiếp. Thay vào đó observe `X_t` generated conditional on `Z_t`.

Cấu trúc này phù hợp khi hệ thống (system / 시스템) có latent regimes: speech phonemes, người dùng (user / 사용자) intent states, machine operating modes hoặc thị trường (market / 시장) regimes.

Suy luận (inference / 추론) thường hỏi posterior xác suất (probability / 확률) của hidden states given observations.

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Hidden Markov mô hình (model / 모델)** xác định đầu vào; **Markov chuỗi (chain / 사슬) Monte Carlo** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Markov chuỗi (chain / 사슬) Monte Carlo

Markov chains còn được dùng như computational công cụ (tool / 도구). Trong **MCMC**, ta thiết kế chuỗi (chain / 사슬) có stationary phân phối (distribution / 분포) chính là mục tiêu (target / 대상) phân phối (distribution / 분포) khó mẫu (sample / 표본) trực tiếp.

Sau burn-in và dưới suitable conditions, samples từ chuỗi (chain / 사슬) có thể dùng xấp xỉ expectations theo mục tiêu (target / 대상) phân phối (distribution / 분포).

Điều này tạo cầu nối (bridge / 브리지) giữa Markov chains và Bayesian suy luận (inference / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Markov chuỗi (chain / 사슬) Monte Carlo** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Random variable mô tả bất định (uncertainty / 불확실성) của một quantity. Stochastic tiến trình (process / 프로세스) mô tả bất định (uncertainty / 불확실성) của cả trajectory. Markov chuỗi (chain / 사슬) thêm giả định (assumption / 가정) rằng trạng thái hiện tại (current state / 현재 상태) là sufficient summary của past cho future evolution. chuyển tiếp (transition / 전이) operator đóng vai trò giống động (dynamic / 동적) quy tắc (rule / 규칙), còn xác suất (probability / 확률) phân phối (distribution / 분포) thay thế một trajectory deterministic duy nhất.

> **Chuyển mạch:** Trong **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

Markov không có nghĩa observations liên tiếp độc lập. Ngược lại, chúng thường phụ thuộc mạnh; chỉ là dependence từ distant past được mediated qua trạng thái hiện tại (current state / 현재 상태).

Stationary cũng không có nghĩa tiến trình (process / 프로세스) đứng yên. mẫu (sample / 표본) paths vẫn dao động liên tục; chỉ statistical laws không thay đổi theo thời gian (time / 시간) shift.

Một autocorrelation cao không tự chứng minh nhân quả (causal / 인과적) quan hệ (relation / 관계). Nó chỉ cho biết temporal dependence cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Stochastic processes, Markov chains và cách mô hình hóa ngẫu nhiên theo thời gian**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức

Chapter này dựa trên [Conditional probability and Bayes](./02_conditional_probability_and_bayes.md), [Random variables and distributions](./03_random_variables_and_distributions.md), [Expectation and variance](./04_expectation_variance_and_limit_laws.md) và [Eigenvalues/eigenvectors](../04_vectors_linear_algebra/04_eigenvalues_and_eigenvectors.md). Nó dẫn tự nhiên tới Bayesian filtering, reinforcement học tập (learning / 학습), queueing lý thuyết (theory / 이론) và stochastic differential equations.

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
