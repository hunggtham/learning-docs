# Likelihood, MLE, MAP và chọn mô hình từ dữ liệu

Probability thường được giới thiệu theo hướng: biết model, tính xác suất data. Statistics thường đi chiều ngược lại: đã quan sát data, ta muốn suy ra parameters hoặc so sánh models. Bridge giữa hai hướng nhìn là **likelihood / 우도**.

Giả sử model có parameter `\theta` và data `x`. Probability distribution viết

```math
p(x\mid\theta)
```

mô tả probability hoặc density của data nếu `\theta` đã biết. Khi data `x` đã fixed và ta xem expression này như function của `\theta`, ta gọi nó là likelihood:

```math
L(\theta;x)=p(x\mid\theta).
```

Cùng một biểu thức số học, nhưng câu hỏi đã đổi: parameter nào làm observed data trở nên plausible nhất dưới model?

## Ví dụ Bernoulli: từ coin flips tới estimate xác suất

Giả sử `n` independent trials, mỗi trial success với probability `p`, và ta quan sát `k` successes. Likelihood là

```math
L(p)
=
p^k(1-p)^{n-k}.
```

Ta muốn tìm `p` maximize expression này. Product dễ underflow và derivative của product phức tạp hơn, nên thường dùng **log-likelihood / 로그우도**:

```math
\ell(p)
=
k\log p+(n-k)\log(1-p).
```

Log là monotonic nên maximize `L` tương đương maximize `\ell`. Derivative:

```math
\frac{d\ell}{dp}
=
\frac{k}{p}-\frac{n-k}{1-p}.
```

Đặt bằng zero:

```math
\frac{k}{p}
=
\frac{n-k}{1-p}
```

suy ra

```math
\hat p=\frac{k}{n}.
```

Sample proportion không phải một formula rơi từ trời xuống; nó là **maximum likelihood estimator** cho Bernoulli probability dưới independence assumption.

## Maximum Likelihood Estimation

**Ước lượng hợp lý cực đại (Maximum Likelihood Estimation, MLE / 최대우도추정)** chọn

```math
\hat\theta_{MLE}
=
\arg\max_\theta L(\theta;x).
```

hoặc tương đương

```math
\hat\theta_{MLE}
=
\arg\max_\theta \log L(\theta;x).
```

MLE rất phổ biến vì general, nối trực tiếp với optimization và thường có good asymptotic properties dưới regularity assumptions. Nhưng MLE không phải “truth detector”. Nó chỉ chọn parameter tốt nhất trong model family đã giả định.

Nếu model family sai, MLE vẫn trả về một answer — chỉ là answer tốt nhất trong family sai đó.

## Negative log-likelihood và loss function trong machine learning

Machine learning thường minimize loss thay vì maximize likelihood. Hai cách nhìn nối nhau bằng

```math
\text{NLL}(\theta)
=
-\log L(\theta;x).
```

Với independent observations,

```math
L(\theta)=\prod_i p(x_i\mid\theta),
```

nên

```math
-\log L(\theta)
=
-\sum_i\log p(x_i\mid\theta).
```

Classification với categorical distribution dẫn tới cross-entropy loss. Linear regression với Gaussian noise dẫn tới squared-error objective. Vì vậy nhiều “loss functions” thực ra encode probabilistic assumptions về data noise.

Ví dụ nếu

```math
y_i=f_\theta(x_i)+\varepsilon_i,
\qquad
\varepsilon_i\sim\mathcal N(0,\sigma^2),
```

thì maximizing Gaussian likelihood tương đương minimizing

```math
\sum_i(y_i-f_\theta(x_i))^2.
```

Mean squared error do đó không chỉ là convenient metric; nó tương ứng một noise model cụ thể.

## Bayesian update và MAP

Bayes theorem cho

```math
p(\theta\mid x)
\propto
p(x\mid\theta)p(\theta).
```

Trong đó `p(\theta)` là **prior / 사전분포**, `p(x|\theta)` là likelihood và `p(\theta|x)` là **posterior / 사후분포**.

**Maximum A Posteriori (MAP / 최대사후추정)** chọn

```math
\hat\theta_{MAP}
=
\arg\max_\theta p(\theta\mid x).
```

Dùng log:

```math
\hat\theta_{MAP}
=
\arg\max_\theta
\left[
\log p(x\mid\theta)+\log p(\theta)
\right].
```

So với MLE, MAP thêm prior. Nếu data rất nhiều và likelihood dominate, MLE và MAP có thể gần nhau. Khi data ít, prior có ảnh hưởng mạnh hơn.

## Regularization như prior

Một connection quan trọng: regularization trong optimization thường tương đương MAP với một prior cụ thể.

Nếu prior Gaussian

```math
p(\theta)\propto e^{-\lambda\|\theta\|_2^2},
```

negative log posterior chứa term

```math
\lambda\|\theta\|_2^2,
```

đó là L2 regularization.

Nếu prior Laplace, ta nhận L1-like penalty. Vì vậy regularization không chỉ là trick chống overfitting; nó có thể được hiểu là preference về parameter structure.

## Bias–variance và overfitting

Một model quá simple có thể **underfit / 과소적합**: không đủ flexibility để capture structure. Model quá flexible có thể **overfit / 과적합**: fit cả noise trong training data.

Generalization error thường được conceptualize qua **bias–variance trade-off / 편향-분산 절충**. High-bias model có systematic error; high-variance model thay đổi mạnh khi training sample thay đổi.

Đây không phải law nói “model complexity luôn có một sweet spot đơn giản”. Modern high-dimensional models có behavior phức tạp hơn classical picture. Nhưng mental model vẫn hữu ích: fit training data tốt chưa đủ; ta quan tâm performance trên unseen data.

## Train, validation và test

Nếu ta dùng cùng data để fit model và evaluate model, estimate performance bị optimistic. Thực hành phổ biến tách data thành training, validation và test sets.

Training data dùng để estimate parameters. Validation data dùng để chọn hyperparameters hoặc model variants. Test data nên được dùng như final held-out evaluation; nếu ta xem test repeatedly rồi điều chỉnh model, test đã trở thành validation data về mặt thực chất.

**Cross-validation / 교차검증** chia data thành folds và luân phiên train/validate để estimate out-of-sample performance ổn định hơn, đặc biệt khi dataset không lớn.

## Information criteria: fit tốt nhưng trả giá cho complexity

Criteria như AIC và BIC cân bằng likelihood với model complexity. AIC có form điển hình

```math
AIC=2k-2\log\hat L,
```

với `k` là number of parameters và `\hat L` là maximized likelihood. Lower AIC được ưu tiên trong framework của nó.

BIC có penalty tăng theo sample size:

```math
BIC=k\log n-2\log\hat L.
```

Không nên dùng AIC/BIC như universal score cho mọi problem; assumptions và modeling goal quan trọng. Nhưng chúng minh họa principle: higher in-sample likelihood không free — complexity cần được account.

## Identifiability

Một parameter **identifiable / 식별가능** nếu different parameter values tạo distributions phân biệt được theo model. Nếu hai parameter settings tạo exactly same observable distribution, data không thể quyết định giữa chúng dù sample lớn đến đâu.

Trong neural networks, parameter symmetries khiến many weight configurations represent same function. Trong mixture models, label switching là một dạng non-identifiability. Đây là reminder rằng “tối ưu được một parameter vector” không có nghĩa parameter đó có unique interpretation.

## Knowledge Connection

Likelihood nối probability với optimization. Log-likelihood dùng logarithm để biến products thành sums. Hessian của log-likelihood liên hệ uncertainty của estimators. Bayesian posterior nối likelihood với prior. Cross-entropy trong classification, least squares trong regression và many losses trong ML đều có probabilistic interpretations.

Information theory cũng gặp likelihood qua coding: model gán high probability cho observed data tương ứng shorter ideal code length `-\log p(x)`. Vì vậy minimizing negative log-likelihood đồng thời có thể hiểu là minimizing description length dưới model.

## Mental Model

> Probability hỏi “nếu parameter là thế này, data có thể trông như thế nào?”. Likelihood quay cùng biểu thức lại và hỏi “data đã trông như thế này, parameter nào giải thích nó tốt nhất trong model family?”. MLE chọn theo data; MAP thêm prior; model selection hỏi liệu phần fit thêm có thực sự generalize hay chỉ đang mua bằng complexity.

## Common Misconceptions

Likelihood không phải probability distribution của parameter trừ khi được normalize cùng prior thành posterior trong Bayesian framework. Vì vậy không nên nói `L(\theta)` là “xác suất parameter đúng”.

MLE cũng không tự động unbiased, robust hay unique. Properties phụ thuộc model và sample size.

Cross-validation không chữa được data leakage. Nếu preprocessing sử dụng toàn dataset trước khi split — ví dụ standardization bằng global mean hoặc feature selection nhìn labels của test fold — validation estimate vẫn bị nhiễm information.
