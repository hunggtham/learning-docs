# Xác suất (probability / 확률) cho Artificial Intelligence

> **Mạch đọc:** Đặt **xác suất (probability / 확률) cho Artificial Intelligence** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Tại sao AI cần xác suất (probability / 확률)?** sang **mẫu (sample / 표본) không gian (space / 공간), sự kiện (event / 이벤트) và random variable**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Xác suất (probability / 확률) là ngôn ngữ để lập luận (reasoning / 추론) khi thông tin không đầy đủ, kết quả (outcome / 결과) không chắc chắn hoặc tiến trình (process / 프로세스) có randomness. AI gần như luôn sống trong điều kiện như vậy: ảnh (image / 이미지) có thể ambiguous, sensor có noise, người dùng (user / 사용자) hành vi (behavior / 동작) không deterministic, dữ liệu huấn luyện (training data / 학습 데이터) chỉ là mẫu (sample / 표본) của world, và ngôn ngữ (language / 언어) mô hình (model / 모델) không biết chắc đơn vị từ (token / 토큰) tiếp theo.

Điểm cốt lõi không phải “mô hình (model / 모델) trả về 0.8 nên đúng 80%”. xác suất (probability / 확률) cần được hiểu như một hệ thống để biểu diễn belief, frequency hoặc bất định (uncertainty / 불확실성) dưới các giả định (assumptions / 가정들) cụ thể. Nếu không phân biệt những interpretation này, ta rất dễ đọc sai mô hình (model / 모델) đầu ra (output / 출력).

Xem trước: [Mathematics for AI](./00_mathematics_for_ai.md).

## Tại sao AI cần xác suất (probability / 확률)?

Giả sử camera thấy một hình mờ. Không có đủ thông tin (information / 정보) để nói chắc chắn đó là mèo hay chó. Một deterministic quy tắc (rule / 규칙) buộc hệ thống (system / 시스템) chọn ngay một label sẽ che mất bất định (uncertainty / 불확실성). xác suất (probability / 확률) phân phối (distribution / 분포) cho phép biểu diễn:

\[
P(cat\mid x)=0.65,\quad P(dog\mid x)=0.30,\quad P(other\mid x)=0.05
\]

Phân phối (distribution / 분포) giữ nhiều thông tin (information / 정보) hơn một hard label. Downstream hệ thống (system / 시스템) có thể quyết định rằng `0.65` chưa đủ để tự động hành động và cần human rà soát (review / 검토).

Xác suất (probability / 확률) vì vậy không chỉ là mathematical decoration; nó ảnh hưởng trực tiếp hệ thống (system / 시스템) thiết kế (design / 설계) và rủi ro (risk / 위험) management.

## Mẫu (sample / 표본) không gian (space / 공간), sự kiện (event / 이벤트) và random variable

Một **mẫu (sample / 표본) không gian (space / 공간)** `Ω` là tập các kết quả (outcome / 결과) có thể xảy ra.

Ví dụ tung coin:

\[
\Omega=\{H,T\}
\]

Một **sự kiện (event / 이벤트)** là subset của mẫu (sample / 표본) không gian (space / 공간).

Một **random variable (확률변수 / biến ngẫu nhiên)** map kết quả (outcome / 결과) thành một giá trị (value / 값). Nếu `X` là số lần ra head trong hai lần tung coin, `X` có thể nhận `0,1,2`.

Trong ML, label `Y`, tính năng (feature / 기능) `X`, noise `ε` hoặc đơn vị từ (token / 토큰) tiếp theo đều thường được modeling như random variables.

## Xác suất (probability / 확률) phân phối (distribution / 분포)

Với discrete random variable `X`, **xác suất (probability / 확률) mass hàm (function / 함수)**:

\[
P(X=x)
\]

gán xác suất (probability / 확률) cho từng giá trị (value / 값).

Với continuous random variable, ta dùng **xác suất (probability / 확률) density hàm (function / 함수)** `p(x)`. xác suất (probability / 확률) tại đúng một real giá trị (value / 값) có thể bằng 0; meaningful quantity là area trên interval:

\[
P(a\le X\le b)=\int_a^b p(x)dx
\]

Phân biệt mass và density giúp tránh câu “density lớn hơn 1 là impossible”. Density có thể lớn hơn 1 miễn total integral bằng 1.

## Joint, marginal và conditional xác suất (probability / 확률)

**Joint xác suất (probability / 확률)**:

\[
P(X,Y)
\]

mô tả hai variables cùng nhau.

**Marginal xác suất (probability / 확률)** lấy một variable ra bằng cách sum/integrate variable còn lại:

\[
P(X)=\sum_y P(X,Y=y)
\]

**Conditional xác suất (probability / 확률)**:

\[
P(Y\mid X)=\frac{P(X,Y)}{P(X)}
\]

mô tả phân phối (distribution / 분포) của `Y` khi đã biết `X`.

Supervised học tập (learning / 학습) thường cố approximate:

\[
P(Y\mid X=x)
\]

Ngôn ngữ (language / 언어) modeling approximate:

\[
P(x_t\mid x_1,\ldots,x_{t-1})
\]

Conditional xác suất (probability / 확률) là một trong những cầu nối (bridge / 브리지) quan trọng nhất giữa xác suất (probability / 확률) lý thuyết (theory / 이론) và ML.

## Sản phẩm (product / 제품) quy tắc (rule / 규칙) và chuỗi (chain / 사슬) quy tắc (rule / 규칙) of xác suất (probability / 확률)

Từ conditional xác suất (probability / 확률):

\[
P(X,Y)=P(X)P(Y\mid X)
\]

Với chuỗi (sequence / 시퀀스):

\[
P(x_1,\ldots,x_n)=\prod_{t=1}^{n}P(x_t\mid x_{<t})
\]

Đây là foundation của autoregressive ngôn ngữ (language / 언어) modeling. Một LLM không cần assign xác suất (probability / 확률) cho cả sentence “một lần”. Nó factorize joint xác suất (probability / 확률) thành next-token conditionals.

Ví dụ:

```text
P("I love AI")
= P("I")
× P("love" | "I")
× P("AI" | "I love")
```

Tokenization thực tế phức tạp hơn word-level example, nhưng probabilistic cơ chế (mechanism / 메커니즘) vẫn vậy.

## Independence

Hai events `A` và `B` independent nếu:

\[
P(A,B)=P(A)P(B)
\]

Tương đương:

\[
P(A\mid B)=P(A)
\]

khi xác suất (probability / 확률) defined.

**Conditional independence** mạnh hơn về utility trong AI. `X` và `Y` có thể dependent overall nhưng independent khi biết `Z`.

Bayesian networks khai thác conditional independence để factorize joint phân phối (distribution / 분포) hiệu quả.

Một lỗi dùng chung (common / 공통) là assume independence chỉ vì correlation thấp. Zero correlation không đồng nghĩa independence, ngoại trừ một số phân phối (distribution / 분포) đặc biệt như jointly Gaussian.

## Bayes' theorem

Bayes' theorem:

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
\]

Trong đó:

- `H` là hypothesis;
- `E` là bằng chứng (evidence / 증거);
- `P(H)` là prior;
- `P(E|H)` là likelihood;
- `P(H|E)` là posterior.

### Ví dụ medical-test style

Giả sử disease prevalence là 1%:

\[
P(D)=0.01
\]

Kiểm thử (test / 테스트) có sensitivity 99%:

\[
P(+\mid D)=0.99
\]

và false-positive tỷ lệ (rate / 비율) 5%:

\[
P(+\mid \neg D)=0.05
\]

Ta có:

\[
P(D\mid +)=\frac{0.99\times0.01}{0.99\times0.01+0.05\times0.99}
\]

xấp xỉ 0.167.

Một positive kiểm thử (test / 테스트) rất accurate không tự động có nghĩa patient có 99% chance mắc bệnh. cơ sở (base / 기반) tỷ lệ (rate / 비율) matters.

Trong anomaly detection, fraud detection và bảo mật (security / 보안), base-rate neglect là dạng thất bại (failure mode / 실패 모드) cực kỳ quan trọng.

## Prior, likelihood và posterior trong Machine học tập (learning / 학습)

Bayesian view cho parameter `θ`:

\[
p(\theta\mid D)=\frac{p(D\mid\theta)p(\theta)}{p(D)}
\]

`p(θ)` encode prior belief. `p(D|θ)` đo parameters giải thích observed dữ liệu (data / 데이터) tốt đến đâu. Posterior combine cả hai.

**Maximum Likelihood Estimation (MLE)** chọn:

\[
\theta_{MLE}=\arg\max_\theta p(D\mid\theta)
\]

**Maximum A Posteriori (MAP)** chọn:

\[
\theta_{MAP}=\arg\max_\theta p(D\mid\theta)p(\theta)
\]

Log transform biến sản phẩm (product / 제품) thành sum:

\[
\theta_{MLE}=\arg\max_\theta \log p(D\mid\theta)
\]

Đây là lý do negative log-likelihood xuất hiện tự nhiên như hàm mất mát (loss function / 손실 함수).

## Expectation

Expected giá trị (value / 값) của discrete random variable:

\[
\mathbb{E}[X]=\sum_x xP(X=x)
\]

Continuous trường hợp (case / 사례):

\[
\mathbb{E}[X]=\int xp(x)dx
\]

Expectation không nhất thiết là kết quả (outcome / 결과) có thể xảy ra. Expected dice roll là 3.5 dù không thể tung ra 3.5.

Trong ML, expected rủi ro (risk / 위험):

\[
R(\theta)=\mathbb{E}_{(X,Y)\sim P}[L(f_\theta(X),Y)]
\]

là mục tiêu (objective / 목표) lý tưởng trên true dữ liệu (data / 데이터) phân phối (distribution / 분포). huấn luyện (training / 학습) dataset chỉ cho empirical approximation.

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

đo tendency hai variables move cùng nhau theo tuyến tính (linear / 선형) sense.

Covariance ma trận (matrix / 행렬):

\[
\Sigma_{ij}=Cov(X_i,X_j)
\]

là đối tượng (object / 객체) central trong multivariate statistics, Gaussian distributions và PCA.

Correlation normalize covariance:

\[
\rho_{XY}=\frac{Cov(X,Y)}{\sigma_X\sigma_Y}
\]

Correlation không imply causation, và correlation thấp không có nghĩa không có nonlinear phụ thuộc (dependency / 의존성).

## Bernoulli và Binomial phân phối (distribution / 분포)

Bernoulli variable `X∈{0,1}` với:

\[
P(X=1)=p
\]

có expectation `p` và variance `p(1-p)`.

Nhị phân (binary / 이진) classification mục tiêu (target / 대상) thường được modeled như Bernoulli.

Nếu có `n` independent Bernoulli trials cùng parameter `p`, count successes có Binomial phân phối (distribution / 분포):

\[
P(K=k)=\binom{n}{k}p^k(1-p)^{n-k}
\]

## Categorical phân phối (distribution / 분포)

Categorical phân phối (distribution / 분포) generalize Bernoulli sang `K` classes:

\[
P(Y=k)=p_k,\quad \sum_k p_k=1
\]

Softmax đầu ra (output / 출력) thường parameterize categorical phân phối (distribution / 분포):

\[
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Trong ngôn ngữ (language / 언어) mô hình (model / 모델), vocabulary có thể có hàng chục nghìn đơn vị từ (token / 토큰); mỗi generation step tạo categorical phân phối (distribution / 분포) trên vocabulary.

## Gaussian phân phối (distribution / 분포)

Normal/Gaussian phân phối (distribution / 분포):

\[
p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
\]

xuất hiện nhiều vì mathematical convenience và Central Limit Theorem, nhưng không nên assume mọi real-world quantity là Gaussian.

Multivariate Gaussian:

\[
\mathbf{x}\sim\mathcal{N}(\boldsymbol\mu,\Sigma)
\]

được xác định bởi mean véc-tơ (vector / 벡터) và covariance ma trận (matrix / 행렬).

Gaussian các giả định (assumptions / 가정들) xuất hiện trong tuyến tính (linear / 선형) các mô hình (models / 모델들), Kalman filters, probabilistic modeling và latent-variable methods.

## Softmax không phải magic xác suất (probability / 확률) converter

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

với `T<1` làm phân phối (distribution / 분포) sharper, `T>1` làm flatter.

Trong LLM generation, temperature thay đổi sampling phân phối (distribution / 분포), không “làm mô hình (model / 모델) thông minh hơn” hoặc trực tiếp tăng factual accuracy.

## Odds và log-odds

Với xác suất (probability / 확률) `p`, odds là:

\[
\frac{p}{1-p}
\]

Log-odds hoặc logit:

\[
\log\frac{p}{1-p}
\]

Logistic regression modeling log-odds như tuyến tính (linear / 선형) hàm (function / 함수):

\[
\log\frac{p}{1-p}=\mathbf{w}^T\mathbf{x}+b
\]

Invert bằng sigmoid:

\[
p=\sigma(z)=\frac{1}{1+e^{-z}}
\]

Điều này giải thích sigmoid không phải arbitrary activation trong logistic regression; nó phát sinh từ modeling log-odds.

## Conditional expectation và quyết định (decision / 결정) making

Nếu hành động (action / 동작) `a` có utility `U(a,Y)`, rational quyết định (decision / 결정) under bất định (uncertainty / 불확실성) có thể chọn hành động (action / 동작) maximize expected utility:

\[
a^*=\arg\max_a \mathbb{E}[U(a,Y)\mid X]
\]

Một classifier và một nghiệp vụ (business / 비즈니스) quyết định (decision / 결정) không giống nhau. mô hình (model / 모델) có thể estimate xác suất (probability / 확률) fraud, còn hệ thống (system / 시스템) phải quyết định khối (block / 블록) giao dịch (transaction / 트랜잭션) hay yêu cầu (request / 요청) xác minh (verification / 확인) dựa trên chi phí (cost / 비용) false positive/negative.

Xác suất (probability / 확률) mô hình (model / 모델) và quyết định (decision / 결정) chính sách (policy / 정책) cần được tách rõ.

## Aleatoric và epistemic bất định (uncertainty / 불확실성)

**Aleatoric bất định (uncertainty / 불확실성)** đến từ intrinsic randomness/noise của tiến trình (process / 프로세스). Ví dụ cùng ngữ cảnh (context / 맥락), người dùng (user / 사용자) vẫn có thể chọn nhiều hành động (action / 동작) khác nhau.

**Epistemic bất định (uncertainty / 불확실성)** đến từ thiếu kiến thức (knowledge / 지식)/dữ liệu (data / 데이터) về mô hình (model / 모델) hoặc môi trường (environment / 환경) và có thể giảm khi có thêm informative dữ liệu (data / 데이터).

Trong practice hai loại này không luôn tách cleanly, nhưng distinction hữu ích để lập luận (reasoning / 추론) về thất bại (failure / 실패).

Một mô hình (model / 모델) có đầu ra (output / 출력) entropy cao có thể vì đầu vào (input / 입력) thực sự ambiguous hoặc vì mô hình (model / 모델) chưa từng thấy lĩnh vực (domain / 도메인) đó. Hai trường hợp cần phản hồi (response / 응답) khác nhau.

## Calibration

Nếu mô hình (model / 모델) dự đoán xác suất (probability / 확률) 0.8 cho 1,000 cases tương tự, một calibrated mô hình (model / 모델) lý tưởng sẽ đúng khoảng 80% trong nhóm đó.

Calibration khác discrimination. Một mô hình (model / 모델) có ranking/AUC tốt vẫn có thể xác suất (probability / 확률) estimates kém calibrated.

Các công cụ (tool / 도구) như độ tin cậy (reliability / 신뢰성) diagram, Expected Calibration lỗi (error / 오류) và calibration methods như temperature scaling giúp evaluate/fix vấn đề này.

Trong high-stakes AI, xác suất (probability / 확률) không calibrated dễ dẫn đến quyết định (decision / 결정) threshold sai.

## Sampling

Nếu phân phối (distribution / 분포) là `p(x)`, **sampling** tạo random kết quả (outcome / 결과) theo phân phối (distribution / 분포) đó.

LLM generation thường không đơn giản chọn đơn vị từ (token / 토큰) xác suất (probability / 확률) cao nhất. Có thể dùng:

- greedy decoding;
- temperature sampling;
- top-k sampling;
- top-p/nucleus sampling.

Sampling chiến lược (strategy / 전략) thay đổi diversity và hành vi khi thất bại (failure behavior / 실패 동작) mà không thay mô hình (model / 모델) parameters.

Greedy decoding là deterministic nhưng không nhất thiết tạo globally most probable chuỗi (sequence / 시퀀스) vì cục bộ (local / 로컬) best choice không guarantee toàn cục (global / 전역) optimum.

## Monte Carlo idea

Khi expectation khó tính analytically:

\[
\mathbb{E}[f(X)]
\]

ta có thể mẫu (sample / 표본):

\[
X_1,\ldots,X_N\sim p(x)
\]

và approximate:

\[
\mathbb{E}[f(X)]\approx\frac{1}{N}\sum_{i=1}^{N}f(X_i)
\]

Monte Carlo methods xuất hiện trong Bayesian suy luận (inference / 추론), Reinforcement học tập (learning / 학습), bất định (uncertainty / 불확실성) estimation và simulation.

## Xác suất (probability / 확률) trong generative modeling

Generative mô hình (model / 모델) cố modeling dữ liệu (data / 데이터) phân phối (distribution / 분포) hoặc một conditional phân phối (distribution / 분포).

Autoregressive mô hình (model / 모델):

\[
p(x)=\prod_t p(x_t\mid x_{<t})
\]

Variational các mô hình (models / 모델들) dùng latent variable:

\[
p(x)=\int p(x\mid z)p(z)dz
\]

Diffusion các mô hình (models / 모델들) học cách reverse một stochastic noising tiến trình (process / 프로세스).

Dù mechanisms khác nhau, xác suất (probability / 확률) là ngôn ngữ (language / 언어) chung để mô tả generation.

## Mô hình tư duy (mental model / 사고 모델)

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

## Dùng chung (common / 공통) Misconceptions

### “xác suất (probability / 확률) 0.9 nghĩa là mô hình (model / 모델) chắc chắn 90% đúng”

Chỉ có interpretation như vậy khi đầu ra (output / 출력) được calibrated và sự kiện (event / 이벤트) definition phù hợp. Neural mạng (network / 네트워크) softmax score có thể overconfident.

### “Nếu hai variables không correlated thì independent”

Không đúng nói chung. Correlation chỉ đo tuyến tính (linear / 선형) quan hệ (relation / 관계); nonlinear phụ thuộc (dependency / 의존성) vẫn có thể tồn tại.

### “Bayesian = subjective, frequentist = mục tiêu (objective / 목표)”

Đây là oversimplification. Hai frameworks khác nhau về cách modeling bất định (uncertainty / 불확실성) và suy luận (inference / 추론); cả hai vẫn cần các giả định (assumptions / 가정들) và modeling choices.

### “Sampling làm mô hình (model / 모델) bịa”

Hallucination không chỉ do sampling. Greedy decoding cũng có thể sinh factual lỗi (error / 오류) vì learned phân phối (distribution / 분포) hoặc ngữ cảnh (context / 맥락) không grounded vào truth.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xác suất (probability / 확률) là prerequisite trực tiếp cho [Statistics for AI](./03_statistics_for_ai.md) và [Information Theory](./05_information_theory.md). Nó cũng quay lại trong classification, generative các mô hình (models / 모델들), Bayesian networks, Reinforcement học tập (learning / 학습), ngôn ngữ (language / 언어) modeling, calibration và uncertainty-aware các hệ thống (systems / 시스템들).

Khi gặp một xác suất (probability / 확률) trong AI, hãy hỏi: random variable là gì, phân phối (distribution / 분포) conditional trên thông tin nào, xác suất (probability / 확률) này là mô hình (model / 모델) estimate hay observed frequency, và downstream quyết định (decision / 결정) sẽ dùng nó thế nào.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 mathematics for ai](./00_mathematics_for_ai.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
