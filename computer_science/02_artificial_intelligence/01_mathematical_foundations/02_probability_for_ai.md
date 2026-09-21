# Probability cho Artificial Intelligence

Probability (확률 / xác suất) là ngôn ngữ để reasoning khi thông tin không đầy đủ, outcome không chắc chắn hoặc process có randomness. AI gần như luôn sống trong điều kiện như vậy: image có thể ambiguous, sensor có noise, user behavior không deterministic, training data chỉ là sample của world, và language model không biết chắc token tiếp theo.

Điểm cốt lõi không phải “model trả về 0.8 nên đúng 80%”. Probability cần được hiểu như một hệ thống để biểu diễn belief, frequency hoặc uncertainty dưới assumptions cụ thể. Nếu không phân biệt những interpretation này, ta rất dễ đọc sai model output.

Xem trước: [Mathematics for AI](./00_mathematics_for_ai.md).

## Tại sao AI cần probability?

Giả sử camera thấy một hình mờ. Không có đủ information để nói chắc chắn đó là mèo hay chó. Một deterministic rule buộc system chọn ngay một label sẽ che mất uncertainty. Probability distribution cho phép biểu diễn:

\[
P(cat\mid x)=0.65,\quad P(dog\mid x)=0.30,\quad P(other\mid x)=0.05
\]

Distribution giữ nhiều information hơn một hard label. Downstream system có thể quyết định rằng `0.65` chưa đủ để tự động hành động và cần human review.

Probability vì vậy không chỉ là mathematical decoration; nó ảnh hưởng trực tiếp system design và risk management.

## Sample space, event và random variable

Một **sample space (표본공간)** `Ω` là tập các outcome có thể xảy ra.

Ví dụ tung coin:

\[
\Omega=\{H,T\}
\]

Một **event (사건)** là subset của sample space.

Một **random variable (확률변수 / biến ngẫu nhiên)** map outcome thành một value. Nếu `X` là số lần ra head trong hai lần tung coin, `X` có thể nhận `0,1,2`.

Trong ML, label `Y`, feature `X`, noise `ε` hoặc token tiếp theo đều thường được modeling như random variables.

## Probability distribution

Với discrete random variable `X`, **probability mass function**:

\[
P(X=x)
\]

gán probability cho từng value.

Với continuous random variable, ta dùng **probability density function** `p(x)`. Probability tại đúng một real value có thể bằng 0; meaningful quantity là area trên interval:

\[
P(a\le X\le b)=\int_a^b p(x)dx
\]

Phân biệt mass và density giúp tránh câu “density lớn hơn 1 là impossible”. Density có thể lớn hơn 1 miễn total integral bằng 1.

## Joint, marginal và conditional probability

**Joint probability**:

\[
P(X,Y)
\]

mô tả hai variables cùng nhau.

**Marginal probability** lấy một variable ra bằng cách sum/integrate variable còn lại:

\[
P(X)=\sum_y P(X,Y=y)
\]

**Conditional probability**:

\[
P(Y\mid X)=\frac{P(X,Y)}{P(X)}
\]

mô tả distribution của `Y` khi đã biết `X`.

Supervised learning thường cố approximate:

\[
P(Y\mid X=x)
\]

Language modeling approximate:

\[
P(x_t\mid x_1,\ldots,x_{t-1})
\]

Conditional probability là một trong những bridge quan trọng nhất giữa probability theory và ML.

## Product rule và chain rule of probability

Từ conditional probability:

\[
P(X,Y)=P(X)P(Y\mid X)
\]

Với sequence:

\[
P(x_1,\ldots,x_n)=\prod_{t=1}^{n}P(x_t\mid x_{<t})
\]

Đây là foundation của autoregressive language modeling. Một LLM không cần assign probability cho cả sentence “một lần”. Nó factorize joint probability thành next-token conditionals.

Ví dụ:

```text
P("I love AI")
= P("I")
× P("love" | "I")
× P("AI" | "I love")
```

Tokenization thực tế phức tạp hơn word-level example, nhưng probabilistic mechanism vẫn vậy.

## Independence

Hai events `A` và `B` independent nếu:

\[
P(A,B)=P(A)P(B)
\]

Tương đương:

\[
P(A\mid B)=P(A)
\]

khi probability defined.

**Conditional independence** mạnh hơn về utility trong AI. `X` và `Y` có thể dependent overall nhưng independent khi biết `Z`.

Bayesian networks khai thác conditional independence để factorize joint distribution hiệu quả.

Một lỗi common là assume independence chỉ vì correlation thấp. Zero correlation không đồng nghĩa independence, ngoại trừ một số distribution đặc biệt như jointly Gaussian.

## Bayes' theorem

Bayes' theorem:

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
\]

Trong đó:

- `H` là hypothesis;
- `E` là evidence;
- `P(H)` là prior;
- `P(E|H)` là likelihood;
- `P(H|E)` là posterior.

### Ví dụ medical-test style

Giả sử disease prevalence là 1%:

\[
P(D)=0.01
\]

Test có sensitivity 99%:

\[
P(+\mid D)=0.99
\]

và false-positive rate 5%:

\[
P(+\mid \neg D)=0.05
\]

Ta có:

\[
P(D\mid +)=\frac{0.99\times0.01}{0.99\times0.01+0.05\times0.99}
\]

xấp xỉ 0.167.

Một positive test rất accurate không tự động có nghĩa patient có 99% chance mắc bệnh. Base rate matters.

Trong anomaly detection, fraud detection và security, base-rate neglect là failure mode cực kỳ quan trọng.

## Prior, likelihood và posterior trong Machine Learning

Bayesian view cho parameter `θ`:

\[
p(\theta\mid D)=\frac{p(D\mid\theta)p(\theta)}{p(D)}
\]

`p(θ)` encode prior belief. `p(D|θ)` đo parameters giải thích observed data tốt đến đâu. Posterior combine cả hai.

**Maximum Likelihood Estimation (MLE)** chọn:

\[
\theta_{MLE}=\arg\max_\theta p(D\mid\theta)
\]

**Maximum A Posteriori (MAP)** chọn:

\[
\theta_{MAP}=\arg\max_\theta p(D\mid\theta)p(\theta)
\]

Log transform biến product thành sum:

\[
\theta_{MLE}=\arg\max_\theta \log p(D\mid\theta)
\]

Đây là lý do negative log-likelihood xuất hiện tự nhiên như loss function.

## Expectation

Expected value của discrete random variable:

\[
\mathbb{E}[X]=\sum_x xP(X=x)
\]

Continuous case:

\[
\mathbb{E}[X]=\int xp(x)dx
\]

Expectation không nhất thiết là outcome có thể xảy ra. Expected dice roll là 3.5 dù không thể tung ra 3.5.

Trong ML, expected risk:

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P}[L(f_\theta(X),Y)]
\]

là objective lý tưởng trên true data distribution. Training dataset chỉ cho empirical approximation.

## Variance và covariance

Variance:

\[
Var(X)=\mathbb{E}[(X-\mathbb{E}[X])^2]
\]

đo spread quanh mean.

Covariance:

\[
Cov(X,Y)=\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]
\]

đo tendency hai variables move cùng nhau theo linear sense.

Covariance matrix:

\[
\Sigma_{ij}=Cov(X_i,X_j)
\]

là object central trong multivariate statistics, Gaussian distributions và PCA.

Correlation normalize covariance:

\[
\rho_{XY}=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
\]

Correlation không imply causation, và correlation thấp không có nghĩa không có nonlinear dependency.

## Bernoulli và Binomial distribution

Bernoulli variable `X∈{0,1}` với:

\[
P(X=1)=p
\]

có expectation `p` và variance `p(1-p)`.

Binary classification target thường được modeled như Bernoulli.

Nếu có `n` independent Bernoulli trials cùng parameter `p`, count successes có Binomial distribution:

\[
P(K=k)=\binom{n}{k}p^k(1-p)^{n-k}
\]

## Categorical distribution

Categorical distribution generalize Bernoulli sang `K` classes:

\[
P(Y=k)=p_k,\quad \sum_k p_k=1
\]

Softmax output thường parameterize categorical distribution:

\[
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Trong language model, vocabulary có thể có hàng chục nghìn token; mỗi generation step tạo categorical distribution trên vocabulary.

## Gaussian distribution

Normal/Gaussian distribution:

\[
p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
\]

xuất hiện nhiều vì mathematical convenience và Central Limit Theorem, nhưng không nên assume mọi real-world quantity là Gaussian.

Multivariate Gaussian:

\[
\mathbf{x}\sim\mathcal{N}(\boldsymbol\mu,\Sigma)
\]

được xác định bởi mean vector và covariance matrix.

Gaussian assumptions xuất hiện trong linear models, Kalman filters, probabilistic modeling và latent-variable methods.

## Softmax không phải magic probability converter

Softmax map logits thành positive normalized values:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

Nếu cộng cùng constant `c` vào mọi logit:

\[
softmax(z_i+c)=softmax(z_i)
\]

nên softmax phụ thuộc relative logits.

Temperature `T`:

\[
p_i=softmax\left(\frac{z_i}{T}\right)
\]

với `T<1` làm distribution sharper, `T>1` làm flatter.

Trong LLM generation, temperature thay đổi sampling distribution, không “làm model thông minh hơn” hoặc trực tiếp tăng factual accuracy.

## Odds và log-odds

Với probability `p`, odds là:

\[
\frac{p}{1-p}
\]

Log-odds hoặc logit:

\[
\log\frac{p}{1-p}
\]

Logistic regression modeling log-odds như linear function:

\[
\log\frac{p}{1-p}=\mathbf{w}^T\mathbf{x}+b
\]

Invert bằng sigmoid:

\[
p=\sigma(z)=\frac{1}{1+e^{-z}}
\]

Điều này giải thích sigmoid không phải arbitrary activation trong logistic regression; nó phát sinh từ modeling log-odds.

## Conditional expectation và decision making

Nếu action `a` có utility `U(a,Y)`, rational decision under uncertainty có thể chọn action maximize expected utility:

\[
a^*=\arg\max_a \mathbb{E}[U(a,Y)\mid X]
\]

Một classifier và một business decision không giống nhau. Model có thể estimate probability fraud, còn system phải quyết định block transaction hay request verification dựa trên cost false positive/negative.

Probability model và decision policy cần được tách rõ.

## Aleatoric và epistemic uncertainty

**Aleatoric uncertainty** đến từ intrinsic randomness/noise của process. Ví dụ cùng context, user vẫn có thể chọn nhiều action khác nhau.

**Epistemic uncertainty** đến từ thiếu knowledge/data về model hoặc environment và có thể giảm khi có thêm informative data.

Trong practice hai loại này không luôn tách cleanly, nhưng distinction hữu ích để reasoning về failure.

Một model có output entropy cao có thể vì input thực sự ambiguous hoặc vì model chưa từng thấy domain đó. Hai trường hợp cần response khác nhau.

## Calibration

Nếu model dự đoán probability 0.8 cho 1,000 cases tương tự, một calibrated model lý tưởng sẽ đúng khoảng 80% trong nhóm đó.

Calibration khác discrimination. Một model có ranking/AUC tốt vẫn có thể probability estimates kém calibrated.

Các tool như reliability diagram, Expected Calibration Error và calibration methods như temperature scaling giúp evaluate/fix vấn đề này.

Trong high-stakes AI, probability không calibrated dễ dẫn đến decision threshold sai.

## Sampling

Nếu distribution là `p(x)`, **sampling** tạo random outcome theo distribution đó.

LLM generation thường không đơn giản chọn token probability cao nhất. Có thể dùng:

- greedy decoding;
- temperature sampling;
- top-k sampling;
- top-p/nucleus sampling.

Sampling strategy thay đổi diversity và failure behavior mà không thay model parameters.

Greedy decoding là deterministic nhưng không nhất thiết tạo globally most probable sequence vì local best choice không guarantee global optimum.

## Monte Carlo idea

Khi expectation khó tính analytically:

\[
\mathbb{E}[f(X)]
\]

ta có thể sample:

\[
X_1,\ldots,X_N\sim p(x)
\]

và approximate:

\[
\mathbb{E}[f(X)]\approx\frac{1}{N}\sum_{i=1}^{N}f(X_i)
\]

Monte Carlo methods xuất hiện trong Bayesian inference, Reinforcement Learning, uncertainty estimation và simulation.

## Probability trong generative modeling

Generative model cố modeling data distribution hoặc một conditional distribution.

Autoregressive model:

\[
p(x)=\prod_t p(x_t\mid x_{<t})
\]

Variational models dùng latent variable:

\[
p(x)=\int p(x\mid z)p(z)dz
\]

Diffusion models học cách reverse một stochastic noising process.

Dù mechanisms khác nhau, probability là language chung để mô tả generation.

## Mental Model

```text
Distribution      = những outcome nào có thể xảy ra và mức belief tương đối
Conditional P     = belief sau khi biết context
Bayes             = update belief bằng evidence
Expectation       = average quantity dưới distribution
Variance          = mức spread / uncertainty
Likelihood        = data phù hợp parameters đến đâu
Sampling          = biến distribution thành một outcome cụ thể
Calibration       = probability output có khớp observed frequency không
```

## Common Misconceptions

### “Probability 0.9 nghĩa là model chắc chắn 90% đúng”

Chỉ có interpretation như vậy khi output được calibrated và event definition phù hợp. Neural network softmax score có thể overconfident.

### “Nếu hai variables không correlated thì independent”

Không đúng nói chung. Correlation chỉ đo linear relation; nonlinear dependency vẫn có thể tồn tại.

### “Bayesian = subjective, frequentist = objective”

Đây là oversimplification. Hai frameworks khác nhau về cách modeling uncertainty và inference; cả hai vẫn cần assumptions và modeling choices.

### “Sampling làm model bịa”

Hallucination không chỉ do sampling. Greedy decoding cũng có thể sinh factual error vì learned distribution hoặc context không grounded vào truth.

## Knowledge Connection

Probability là prerequisite trực tiếp cho [Statistics for AI](./03_statistics_for_ai.md) và [Information Theory](./05_information_theory.md). Nó cũng quay lại trong classification, generative models, Bayesian networks, Reinforcement Learning, language modeling, calibration và uncertainty-aware systems.

Khi gặp một probability trong AI, hãy hỏi: random variable là gì, distribution conditional trên thông tin nào, probability này là model estimate hay observed frequency, và downstream decision sẽ dùng nó thế nào.