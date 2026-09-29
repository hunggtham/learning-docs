# Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)

> **Mạch đọc:** Đọc **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **Prior** sang **Likelihood**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Bayes' theorem thường được giới thiệu bằng một formula ngắn:

```math
P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.
```

Nhưng **Bayesian suy luận (inference / 추론)** không chỉ là một bài toán đổi conditional xác suất (probability / 확률). Nó là một khung phần mềm (framework / 프레임워크) hoàn chỉnh để cập nhật bất định (uncertainty / 불확실성) về unknown quantities khi có dữ liệu (data / 데이터) mới.

Trong statistical modeling, unknown parameter được coi như một random variable. Trước khi quan sát dữ liệu (data / 데이터) ta mô tả bất định (uncertainty / 불확실성) bằng prior. dữ liệu (data / 데이터) đi vào qua likelihood. Sau khi kết hợp hai nguồn thông tin (information / 정보), ta nhận posterior.

```math
p(\theta\mid D)
=\frac{p(D\mid\theta)p(\theta)}{p(D)}.
```

Tư duy cốt lõi là: **không chỉ estimate một parameter điểm (point / 지점) giá trị (value / 값); ta giữ cả phân phối (distribution / 분포) của bất định (uncertainty / 불확실성) về parameter đó**.

## Prior

**Prior phân phối (distribution / 분포)** mô tả beliefs hoặc kiến thức (knowledge / 지식) về parameter trước khi dùng hiện tại (current / 현재) dataset.

Ví dụ xác suất (probability / 확률) một người dùng (user / 사용자) click có thể được mô hình bằng parameter `θ∈[0,1]`. Ta có thể chọn

```math
\theta\sim\operatorname{Beta}(\alpha,\beta).
```

Nếu `α=β=1`, prior uniform. Nếu `α` và `β` lớn hơn, prior concentrated hơn.

Prior không nhất thiết phải “subjective guess”. Nó có thể encode vật lý (physical / 물리적) các ràng buộc (constraints / 제약조건들), previous studies, historical dữ liệu (data / 데이터) hoặc regularization cấu trúc (structure / 구조).

## Likelihood

Likelihood xem observed dữ liệu (data / 데이터) là cố định và parameter là variable:

```math
L(\theta)=p(D\mid\theta).
```

Nếu có Bernoulli observations `x_i∈{0,1}` độc lập conditional on `θ`, likelihood là

```math
p(D\mid\theta)=\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}.
```

Likelihood cho biết parameter values nào giải thích dữ liệu (data / 데이터) tốt hơn, nhưng tự nó chưa phải xác suất (probability / 확률) phân phối (distribution / 분포) over parameter trừ khi normalize và kết hợp prior.

## Posterior

Posterior proportional to prior times likelihood:

```math
p(\theta\mid D)\propto p(D\mid\theta)p(\theta).
```

Normalization constant

```math
p(D)=\int p(D\mid\theta)p(\theta)d\theta
```

được gọi là bằng chứng (evidence / 증거) hoặc marginal likelihood.

Trong many các mô hình (models / 모델들), denominator khó tính. Nhưng khi chỉ cần posterior up to proportionality, ta có thể làm suy luận (inference / 추론) bằng MCMC hoặc variational methods.

## Conjugate prior

Prior gọi là conjugate nếu posterior thuộc cùng family với prior.

Bernoulli likelihood với Beta prior là ví dụ kinh điển.

Nếu

```math
\theta\sim\operatorname{Beta}(\alpha,\beta)
```

và dữ liệu (data / 데이터) có `s` successes, `f` failures, thì

```math
\theta\mid D
\sim\operatorname{Beta}(\alpha+s,\beta+f).
```

Dữ liệu (data / 데이터) đơn giản cộng counts vào prior pseudo-counts.

Đây là một mô hình tư duy (mental model / 사고 모델) rất hữu ích: prior mang một lượng bằng chứng (evidence / 증거) trước đó, dữ liệu (data / 데이터) bổ sung bằng chứng (evidence / 증거) mới.

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

Ba quantities trả lời ba câu hỏi khác nhau. MLE tối đa likelihood. MAP tối đa posterior density. Posterior mean minimize squared-error Bayes rủi ro (risk / 위험) dưới dùng chung (common / 공통) mất mát (loss / 손실) các giả định (assumptions / 가정들).

Bayesian suy luận (inference / 추론) không bắt buộc phải collapse posterior thành một điểm (point / 지점) estimate; thường giữ full posterior là mục tiêu chính.

## Posterior predictive phân phối (distribution / 분포)

Một trong những lợi ích lớn nhất của Bayesian khung phần mềm (framework / 프레임워크) là prediction tự nhiên integrate bất định (uncertainty / 불확실성) về parameters.

Với future observation `x_new`, posterior predictive là

```math
p(x_{new}\mid D)
=\int p(x_{new}\mid\theta)p(\theta\mid D)d\theta.
```

Thay vì plug-in một single `θ_hat`, ta average predictions qua all plausible parameter values weighted by posterior xác suất (probability / 확률).

Điều này thường làm bất định (uncertainty / 불확실성) calibration tốt hơn khi dữ liệu (data / 데이터) ít.

## Credible interval

Một Bayesian credible interval `[a,b]` có thể được chọn sao cho

```math
P(a\le\theta\le b\mid D)=0.95.
```

Interpretation trực tiếp là: conditional on mô hình (model / 모델) và observed dữ liệu (data / 데이터), posterior xác suất (probability / 확률) parameter nằm trong interval là 95%.

Điều này khác confidence interval trong frequentist statistics. Confidence interval procedure có long-run coverage 95%; sau khi interval cụ thể được tạo, classical parameter được coi fixed chứ không random.

Hai frameworks trả lời questions khác nhau và không nên diễn giải lẫn nhau.

## Prior predictive phân phối (distribution / 분포)

Trước khi observe dữ liệu (data / 데이터), ta có thể xem mô hình (model / 모델) dự đoán dữ liệu (data / 데이터) nào:

```math
p(x)=\int p(x\mid\theta)p(\theta)d\theta.
```

Đây là **prior predictive check**. Nếu prior + likelihood tạo ra datasets phi lý, mô hình (model / 모델) đã có vấn đề trước khi fitting.

Ví dụ nếu mô hình (model / 모델) về thời gian phản hồi web thường sinh độ trễ (latency / 지연 시간) hàng nghìn năm, prior quy mô (scale / 규모) rõ ràng không phù hợp.

## Posterior predictive checks

Sau fitting, generate replicated dữ liệu (data / 데이터)

```math
\tilde D\sim p(\tilde D\mid D)
```

và so sánh với observed dữ liệu (data / 데이터).

Nếu mô hình (model / 모델) không reproduce important patterns của actual dữ liệu (data / 데이터), posterior parameter estimates dù “chính xác” trong mô hình (model / 모델) vẫn không cứu được mô hình (model / 모델) misspecification.

Bayesian workflow vì vậy không chỉ là compute posterior; nó còn gồm mô hình (model / 모델) criticism.

## Bayes factor và marginal likelihood

Để compare các mô hình (models / 모델들) `M_1` và `M_2`, Bayes factor là

```math
BF_{12}=\frac{p(D\mid M_1)}{p(D\mid M_2)}.
```

Marginal likelihood integrate parameter bất định (uncertainty / 불확실성):

```math
p(D\mid M)=\int p(D\mid\theta,M)p(\theta\mid M)d\theta.
```

Nó naturally penalizes các mô hình (models / 모델들) spreading prior mass over parameter regions that fit dữ liệu (data / 데이터) poorly. Tuy nhiên Bayes factors có thể nhạy với prior choice, đặc biệt diffuse priors.

## Hierarchical các mô hình (models / 모델들)

Nhiều datasets có group cấu trúc (structure / 구조): users trong countries, students trong schools, requests trên servers, products trong categories.

Một hierarchical mô hình (model / 모델) cho group-specific parameters nhưng giả định chúng sinh từ một dùng chung (common / 공통) population phân phối (distribution / 분포).

Ví dụ

```math
\theta_j\sim N(\mu,\tau^2),
```

với observations

```math
y_{ij}\sim N(\theta_j,\sigma^2).
```

Các group estimates được **partial pooling** về toàn cục (global / 전역) mean `μ`, mức pooling phụ thuộc dữ liệu (data / 데이터) và bất định (uncertainty / 불확실성).

Group ít dữ liệu (data / 데이터) bị shrink nhiều hơn; group nhiều dữ liệu (data / 데이터) giữ estimate riêng mạnh hơn.

## Partial pooling

Không pooling: fit mỗi group hoàn toàn riêng, variance cao với small groups.

Complete pooling: bỏ qua group differences, độ lệch (bias / 편향) cao nếu groups thực sự khác.

Partial pooling cân bằng hai extremes bằng hierarchy.

Đây là một trong những ideas Bayesian hữu ích nhất trong sản phẩm (product / 제품) analytics, medicine, A/B testing và organizational dữ liệu (data / 데이터).

## Bayesian tuyến tính (linear / 선형) regression

Classical tuyến tính (linear / 선형) regression viết

```math
y=X\beta+\varepsilon.
```

Bayesian phiên bản (version / 버전) đặt prior lên coefficients:

```math
\beta\sim N(0,\tau^2I).
```

và likelihood Gaussian:

```math
y\mid\beta\sim N(X\beta,\sigma^2I).
```

Posterior của `β` combine dữ liệu (data / 데이터) fit với prior regularization.

Gaussian prior tương ứng gần với L2 regularization/MAP. Laplace prior dẫn tới L1-like hành vi (behavior / 동작).

Vì vậy regularization trong ML có thể được giải thích như prior các giả định (assumptions / 가정들).

## Bayesian updating theo từng batch

Posterior sau batch đầu có thể trở thành prior cho batch sau:

```math
p(\theta\mid D_1,D_2)
\propto p(D_2\mid\theta)p(\theta\mid D_1).
```

Điều này thể hiện consistency của sequential học tập (learning / 학습) khi các giả định (assumptions / 가정들) phù hợp.

Nó rất tự nhiên cho các hệ thống (systems / 시스템들) nhận dữ liệu (data / 데이터) liên tục.

## Computational suy luận (inference / 추론)

Trong simple conjugate các mô hình (models / 모델들) posterior có closed form. Với hiện đại (modern / 현대적) các mô hình (models / 모델들), integral khó tính nên cần numerical suy luận (inference / 추론).

MCMC tạo correlated samples từ posterior. Variational suy luận (inference / 추론) biến suy luận (inference / 추론) thành tối ưu hóa (optimization / 최적화) bằng cách chọn approximation `q(θ)` gần posterior thật.

Dùng chung (common / 공통) mục tiêu (objective / 목표) là minimize

```math
KL(q(\theta)\|p(\theta\mid D)).
```

hoặc maximize ELBO.

Sự đánh đổi (trade-off / 트레이드오프) thường là MCMC chính xác hơn asymptotically nhưng costly, còn variational methods nhanh hơn nhưng có approximation độ lệch (bias / 편향).

## Calibration và bất định (uncertainty / 불확실성)

Bayesian posterior bất định (uncertainty / 불확실성) chỉ meaningful nếu mô hình (model / 모델) cấu trúc (structure / 구조), likelihood và prior đủ hợp lý. Nếu mô hình (model / 모델) sai nghiêm trọng, posterior vẫn có thể rất concentrated nhưng quanh answer sai.

“Bayesian” không tự động đồng nghĩa “bất định (uncertainty / 불확실성) đúng”. mô hình (model / 모델) checking và sensitivity phân tích (analysis / 분석) là bắt buộc.

## Prior sensitivity

Khi dữ liệu (data / 데이터) rất lớn, reasonable priors thường ít ảnh hưởng. Khi dữ liệu (data / 데이터) ít hoặc likelihood weakly identifies parameters, prior có thể ảnh hưởng mạnh.

Thay vì che giấu điều này, nên vary plausible priors và xem conclusions thay đổi bao nhiêu.

Sensitivity phân tích (analysis / 분석) giúp phân biệt thông tin (information / 정보) đến từ dữ liệu (data / 데이터) hay các giả định (assumptions / 가정들).

## Example: tỷ lệ lỗi triển khai (deployment / 배포)

Giả sử prior thất bại (failure / 실패) xác suất (probability / 확률)

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

Observed thất bại (failure / 실패) tỷ lệ (rate / 비율) là `4/20=0.20`, nhưng posterior estimate được shrink về prior vì mẫu (sample / 표본) vẫn nhỏ.

Nếu thêm hàng nghìn deployments, dữ liệu (data / 데이터) sẽ dominate prior mạnh hơn.

## Quyết định (decision / 결정) lý thuyết (theory / 이론)

Suy luận (inference / 추론) và quyết định (decision / 결정) là hai bước khác nhau. Posterior mô tả bất định (uncertainty / 불확실성); hành động (action / 동작) cần mất mát (loss / 손실) hoặc utility.

Optimal Bayesian hành động (action / 동작) minimize posterior expected mất mát (loss / 손실):

```math
a^*=\arg\min_a E[L(a,\theta)\mid D].
```

Trong nghiệp vụ (business / 비즈니스), same posterior có thể dẫn tới actions khác nhau nếu chi phí (cost / 비용) của false positive và false negative khác nhau.

Đây là lý do xác suất (probability / 확률) estimate không tự động quyết định threshold.

## Mô hình tư duy (mental model / 사고 모델)

Bayesian suy luận (inference / 추론) là một chuỗi xử lý (pipeline / 파이프라인) của thông tin (information / 정보): prior mô tả trạng thái kiến thức (knowledge / 지식) trước dữ liệu (data / 데이터), likelihood mô tả cách dữ liệu (data / 데이터) được sinh ra nếu parameter có giá trị (value / 값) nhất định, posterior là kiến thức (knowledge / 지식) sau dữ liệu (data / 데이터), và posterior predictive biến updated kiến thức (knowledge / 지식) thành predictions. Hierarchical các mô hình (models / 모델들) cho phép thông tin (information / 정보) luồng (flow / 흐름) cả trong group lẫn giữa các groups.

## Dùng chung (common / 공통) Misconceptions

Prior không nhất thiết là opinion tùy ý và posterior cũng không “khách quan tuyệt đối”; cả mô hình (model / 모델) lẫn prior đều là các giả định (assumptions / 가정들) cần kiểm tra. MAP cũng không phải synonym của Bayesian suy luận (inference / 추론) vì nó chỉ giữ một chế độ (mode / 모드) của posterior.

Một misconception khác là credible interval và confidence interval cùng nghĩa. Con số có thể giống nhau trong một số mô hình (model / 모델) nhưng interpretation khác fundamentally.

## Liên kết kiến thức

Chapter này phát triển từ [Conditional probability and Bayes](./02_conditional_probability_and_bayes.md), [Likelihood, MLE, MAP](./10_likelihood_mle_map_and_model_selection.md) và [Stochastic processes](./11_stochastic_processes_markov_chains_and_time_series.md). Nó nối trực tiếp với regularization, probabilistic ML, Bayesian A/B testing, MCMC và quyết định (decision / 결정) lý thuyết (theory / 이론).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 counting and combinatorics](./00_counting_and_combinatorics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
