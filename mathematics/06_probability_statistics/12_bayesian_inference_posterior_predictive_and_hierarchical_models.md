# Bayesian inference: posterior, predictive distribution và hierarchical models

Bayes' theorem thường được giới thiệu bằng một formula ngắn:

```math
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.
```

Nhưng **Bayesian inference (베이지안 추론)** không chỉ là một bài toán đổi conditional probability. Nó là một framework hoàn chỉnh để cập nhật uncertainty về unknown quantities khi có data mới.

Trong statistical modeling, unknown parameter được coi như một random variable. Trước khi quan sát data ta mô tả uncertainty bằng prior. Data đi vào qua likelihood. Sau khi kết hợp hai nguồn information, ta nhận posterior.

```math
p(\theta\mid D)
=\frac{p(D\mid\theta)p(\theta)}{p(D)}.
```

Tư duy cốt lõi là: **không chỉ estimate một parameter point value; ta giữ cả distribution của uncertainty về parameter đó**.

## Prior

**Prior distribution (사전분포)** mô tả beliefs hoặc knowledge về parameter trước khi dùng current dataset.

Ví dụ probability một user click có thể được mô hình bằng parameter `θ∈[0,1]`. Ta có thể chọn

```math
\theta\sim\operatorname{Beta}(\alpha,\beta).
```

Nếu `α=β=1`, prior uniform. Nếu `α` và `β` lớn hơn, prior concentrated hơn.

Prior không nhất thiết phải “subjective guess”. Nó có thể encode physical constraints, previous studies, historical data hoặc regularization structure.

## Likelihood

Likelihood xem observed data là cố định và parameter là variable:

```math
L(\theta)=p(D\mid\theta).
```

Nếu có Bernoulli observations `x_i∈{0,1}` độc lập conditional on `θ`, likelihood là

```math
p(D\mid\theta)=\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}.
```

Likelihood cho biết parameter values nào giải thích data tốt hơn, nhưng tự nó chưa phải probability distribution over parameter trừ khi normalize và kết hợp prior.

## Posterior

Posterior proportional to prior times likelihood:

```math
p(\theta\mid D)\propto p(D\mid\theta)p(\theta).
```

Normalization constant

```math
p(D)=\int p(D\mid\theta)p(\theta)d\theta
```

được gọi là evidence hoặc marginal likelihood.

Trong many models, denominator khó tính. Nhưng khi chỉ cần posterior up to proportionality, ta có thể làm inference bằng MCMC hoặc variational methods.

## Conjugate prior

Prior gọi là conjugate nếu posterior thuộc cùng family với prior.

Bernoulli likelihood với Beta prior là ví dụ kinh điển.

Nếu

```math
\theta\sim\operatorname{Beta}(\alpha,\beta)
```

và data có `s` successes, `f` failures, thì

```math
\theta\mid D
\sim\operatorname{Beta}(\alpha+s,\beta+f).
```

Data đơn giản cộng counts vào prior pseudo-counts.

Đây là một mental model rất hữu ích: prior mang một lượng evidence trước đó, data bổ sung evidence mới.

## MAP, MLE và posterior mean

MLE chọn

```math
\hat\theta_{MLE}
=\arg\max_\theta p(D\mid\theta).
```

MAP chọn

```math
\hat\theta_{MAP}
=\arg\max_\theta p(D\mid\theta)p(\theta).
```

Posterior mean là

```math
E[\theta\mid D].
```

Ba quantities trả lời ba câu hỏi khác nhau. MLE tối đa likelihood. MAP tối đa posterior density. Posterior mean minimize squared-error Bayes risk dưới common loss assumptions.

Bayesian inference không bắt buộc phải collapse posterior thành một point estimate; thường giữ full posterior là mục tiêu chính.

## Posterior predictive distribution

Một trong những lợi ích lớn nhất của Bayesian framework là prediction tự nhiên integrate uncertainty về parameters.

Với future observation `x_new`, posterior predictive là

```math
p(x_{new}\mid D)
=\int p(x_{new}\mid\theta)p(\theta\mid D)d\theta.
```

Thay vì plug-in một single `θ_hat`, ta average predictions qua all plausible parameter values weighted by posterior probability.

Điều này thường làm uncertainty calibration tốt hơn khi data ít.

## Credible interval

Một Bayesian credible interval `[a,b]` có thể được chọn sao cho

```math
P(a\le\theta\le b\mid D)=0.95.
```

Interpretation trực tiếp là: conditional on model và observed data, posterior probability parameter nằm trong interval là 95%.

Điều này khác confidence interval trong frequentist statistics. Confidence interval procedure có long-run coverage 95%; sau khi interval cụ thể được tạo, classical parameter được coi fixed chứ không random.

Hai frameworks trả lời questions khác nhau và không nên diễn giải lẫn nhau.

## Prior predictive distribution

Trước khi observe data, ta có thể xem model dự đoán data nào:

```math
p(x)=\int p(x\mid\theta)p(\theta)d\theta.
```

Đây là **prior predictive check**. Nếu prior + likelihood tạo ra datasets phi lý, model đã có vấn đề trước khi fitting.

Ví dụ nếu model về thời gian phản hồi web thường sinh latency hàng nghìn năm, prior scale rõ ràng không phù hợp.

## Posterior predictive checks

Sau fitting, generate replicated data

```math
\tilde D\sim p(\tilde D\mid D)
```

và so sánh với observed data.

Nếu model không reproduce important patterns của actual data, posterior parameter estimates dù “chính xác” trong model vẫn không cứu được model misspecification.

Bayesian workflow vì vậy không chỉ là compute posterior; nó còn gồm model criticism.

## Bayes factor và marginal likelihood

Để compare models `M_1` và `M_2`, Bayes factor là

```math
BF_{12}=\frac{p(D\mid M_1)}{p(D\mid M_2)}.
```

Marginal likelihood integrate parameter uncertainty:

```math
p(D\mid M)=\int p(D\mid\theta,M)p(\theta\mid M)d\theta.
```

Nó naturally penalizes models spreading prior mass over parameter regions that fit data poorly. Tuy nhiên Bayes factors có thể nhạy với prior choice, đặc biệt diffuse priors.

## Hierarchical models

Nhiều datasets có group structure: users trong countries, students trong schools, requests trên servers, products trong categories.

Một hierarchical model cho group-specific parameters nhưng giả định chúng sinh từ một common population distribution.

Ví dụ

```math
\theta_j\sim N(\mu,\tau^2),
```

với observations

```math
y_{ij}\sim N(\theta_j,\sigma^2).
```

Các group estimates được **partial pooling** về global mean `μ`, mức pooling phụ thuộc data và uncertainty.

Group ít data bị shrink nhiều hơn; group nhiều data giữ estimate riêng mạnh hơn.

## Partial pooling

Không pooling: fit mỗi group hoàn toàn riêng, variance cao với small groups.

Complete pooling: bỏ qua group differences, bias cao nếu groups thực sự khác.

Partial pooling cân bằng hai extremes bằng hierarchy.

Đây là một trong những ideas Bayesian hữu ích nhất trong product analytics, medicine, A/B testing và organizational data.

## Bayesian linear regression

Classical linear regression viết

```math
y=X\beta+\varepsilon.
```

Bayesian version đặt prior lên coefficients:

```math
\beta\sim N(0,\tau^2I).
```

và likelihood Gaussian:

```math
y\mid\beta\sim N(X\beta,\sigma^2I).
```

Posterior của `β` combine data fit với prior regularization.

Gaussian prior tương ứng gần với L2 regularization/MAP. Laplace prior dẫn tới L1-like behavior.

Vì vậy regularization trong ML có thể được giải thích như prior assumptions.

## Bayesian updating theo từng batch

Posterior sau batch đầu có thể trở thành prior cho batch sau:

```math
p(\theta\mid D_1,D_2)
\propto p(D_2\mid\theta)p(\theta\mid D_1).
```

Điều này thể hiện consistency của sequential learning khi assumptions phù hợp.

Nó rất tự nhiên cho systems nhận data liên tục.

## Computational inference

Trong simple conjugate models posterior có closed form. Với modern models, integral khó tính nên cần numerical inference.

MCMC tạo correlated samples từ posterior. Variational inference biến inference thành optimization bằng cách chọn approximation `q(θ)` gần posterior thật.

Common objective là minimize

```math
KL(q(\theta)\|p(\theta\mid D)).
```

hoặc maximize ELBO.

Trade-off thường là MCMC chính xác hơn asymptotically nhưng costly, còn variational methods nhanh hơn nhưng có approximation bias.

## Calibration và uncertainty

Bayesian posterior uncertainty chỉ meaningful nếu model structure, likelihood và prior đủ hợp lý. Nếu model sai nghiêm trọng, posterior vẫn có thể rất concentrated nhưng quanh answer sai.

“Bayesian” không tự động đồng nghĩa “uncertainty đúng”. Model checking và sensitivity analysis là bắt buộc.

## Prior sensitivity

Khi data rất lớn, reasonable priors thường ít ảnh hưởng. Khi data ít hoặc likelihood weakly identifies parameters, prior có thể ảnh hưởng mạnh.

Thay vì che giấu điều này, nên vary plausible priors và xem conclusions thay đổi bao nhiêu.

Sensitivity analysis giúp phân biệt information đến từ data hay assumptions.

## Example: tỷ lệ lỗi deployment

Giả sử prior failure probability

```math
\theta\sim\operatorname{Beta}(2,18),
```

mean prior là `0.1`.

Sau 20 deployments có 4 failures và 16 successes. Posterior là

```math
\operatorname{Beta}(6,34).
```

Posterior mean là

```math
\frac6{40}=0.15.
```

Observed failure rate là `4/20=0.20`, nhưng posterior estimate được shrink về prior vì sample vẫn nhỏ.

Nếu thêm hàng nghìn deployments, data sẽ dominate prior mạnh hơn.

## Decision theory

Inference và decision là hai bước khác nhau. Posterior mô tả uncertainty; action cần loss hoặc utility.

Optimal Bayesian action minimize posterior expected loss:

```math
a^*=\arg\min_a E[L(a,\theta)\mid D].
```

Trong business, same posterior có thể dẫn tới actions khác nhau nếu cost của false positive và false negative khác nhau.

Đây là lý do probability estimate không tự động quyết định threshold.

## Mental Model

Bayesian inference là một pipeline của information: prior mô tả trạng thái knowledge trước data, likelihood mô tả cách data được sinh ra nếu parameter có value nhất định, posterior là knowledge sau data, và posterior predictive biến updated knowledge thành predictions. Hierarchical models cho phép information flow cả trong group lẫn giữa các groups.

## Common Misconceptions

Prior không nhất thiết là opinion tùy ý và posterior cũng không “khách quan tuyệt đối”; cả model lẫn prior đều là assumptions cần kiểm tra. MAP cũng không phải synonym của Bayesian inference vì nó chỉ giữ một mode của posterior.

Một misconception khác là credible interval và confidence interval cùng nghĩa. Con số có thể giống nhau trong một số model nhưng interpretation khác fundamentally.

## Liên kết kiến thức

Chapter này phát triển từ [Conditional probability and Bayes](./02_conditional_probability_and_bayes.md), [Likelihood, MLE, MAP](./10_likelihood_mle_map_and_model_selection.md) và [Stochastic processes](./11_stochastic_processes_markov_chains_and_time_series.md). Nó nối trực tiếp với regularization, probabilistic ML, Bayesian A/B testing, MCMC và decision theory.