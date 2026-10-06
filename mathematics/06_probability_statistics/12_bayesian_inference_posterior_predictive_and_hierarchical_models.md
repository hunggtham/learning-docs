# Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)

> **Mạch đọc:** [README](../README.md) là bản đồ owner của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Prior** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Likelihood** để mở rộng đối tượng sang phạm vi kế cận. Mạch này nối Bayesian inference với posterior, predictive và hierarchical models, để bất định được cập nhật qua dữ liệu và cấu trúc nhóm.

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

> **Nối mạch:** Trong **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Likelihood** nối từ **Prior** sang **Posterior**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Posterior** nối từ **Likelihood** sang **Conjugate prior**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Conjugate prior** nối từ **Posterior** sang **MAP, MLE và posterior mean**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **MAP, MLE và posterior mean** nối từ **Conjugate prior** sang **Posterior predictive phân phối (distribution / 분포)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Posterior predictive phân phối (distribution / 분포)** nối từ **MAP, MLE và posterior mean** sang **Credible interval**, vì cơ chế trước tạo đầu vào cho bước sau.

## Posterior predictive phân phối (distribution / 분포)

Một trong những lợi ích lớn nhất của Bayesian khung phần mềm (framework / 프레임워크) là prediction tự nhiên integrate bất định (uncertainty / 불확실성) về parameters.

Với future observation `x_new`, posterior predictive là

```math
p(x_{new}\mid D)
=\int p(x_{new}\mid\theta)p(\theta\mid D)d\theta.
```

Thay vì plug-in một single `θ_hat`, ta average predictions qua all plausible parameter values weighted by posterior xác suất (probability / 확률).

Điều này thường làm bất định (uncertainty / 불확실성) calibration tốt hơn khi dữ liệu (data / 데이터) ít.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Credible interval** nối từ **Posterior predictive phân phối (distribution / 분포)** sang **Prior predictive phân phối (distribution / 분포)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Credible interval

Một Bayesian credible interval `[a,b]` có thể được chọn sao cho

```math
P(a\le\theta\le b\mid D)=0.95.
```

Interpretation trực tiếp là: conditional on mô hình (model / 모델) và observed dữ liệu (data / 데이터), posterior xác suất (probability / 확률) parameter nằm trong interval là 95%.

Điều này khác confidence interval trong frequentist statistics. Confidence interval procedure có long-run coverage 95%; sau khi interval cụ thể được tạo, classical parameter được coi fixed chứ không random.

Hai frameworks trả lời questions khác nhau và không nên diễn giải lẫn nhau.

> **Nối mạch:** Trong **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Prior predictive phân phối (distribution / 분포)** nối từ **Credible interval** sang **Posterior predictive checks**, vì cơ chế trước tạo đầu vào cho bước sau.

## Prior predictive phân phối (distribution / 분포)

Trước khi observe dữ liệu (data / 데이터), ta có thể xem mô hình (model / 모델) dự đoán dữ liệu (data / 데이터) nào:

```math
p(x)=\int p(x\mid\theta)p(\theta)d\theta.
```

Đây là **prior predictive check**. Nếu prior + likelihood tạo ra datasets phi lý, mô hình (model / 모델) đã có vấn đề trước khi fitting.

Ví dụ nếu mô hình (model / 모델) về thời gian phản hồi web thường sinh độ trễ (latency / 지연 시간) hàng nghìn năm, prior quy mô (scale / 규모) rõ ràng không phù hợp.

> **Nối mạch:** Ở chặng này của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Posterior predictive checks** nối từ **Prior predictive phân phối (distribution / 분포)** sang **Bayes factor và marginal likelihood**, vì cơ chế trước tạo đầu vào cho bước sau.

## Posterior predictive checks

Sau fitting, generate replicated dữ liệu (data / 데이터)

```math
\tilde D\sim p(\tilde D\mid D)
```

và so sánh với observed dữ liệu (data / 데이터).

Nếu mô hình (model / 모델) không reproduce important patterns của actual dữ liệu (data / 데이터), posterior parameter estimates dù “chính xác” trong mô hình (model / 모델) vẫn không cứu được mô hình (model / 모델) misspecification.

Bayesian workflow vì vậy không chỉ là compute posterior; nó còn gồm mô hình (model / 모델) criticism.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Bayes factor và marginal likelihood** nối từ **Posterior predictive checks** sang **Hierarchical các mô hình (models / 모델들)**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Hierarchical các mô hình (models / 모델들)** nối từ **Bayes factor và marginal likelihood** sang **Partial pooling**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Ở chặng này của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Partial pooling** nối từ **Hierarchical các mô hình (models / 모델들)** sang **Bayesian tuyến tính (linear / 선형) regression**, vì cơ chế trước tạo đầu vào cho bước sau.

## Partial pooling

Không pooling: fit mỗi group hoàn toàn riêng, variance cao với small groups.

Complete pooling: bỏ qua group differences, độ lệch (bias / 편향) cao nếu groups thực sự khác.

Partial pooling cân bằng hai extremes bằng hierarchy.

Đây là một trong những ideas Bayesian hữu ích nhất trong sản phẩm (product / 제품) analytics, medicine, A/B testing và organizational dữ liệu (data / 데이터).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Bayesian tuyến tính (linear / 선형) regression** nối từ **Partial pooling** sang **Bayesian updating theo từng batch**, vì cơ chế trước tạo đầu vào cho bước sau.

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

> **Nối mạch:** Trong **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Bayesian updating theo từng batch** nối từ **Bayesian tuyến tính (linear / 선형) regression** sang **Computational suy luận (inference / 추론)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Bayesian updating theo từng batch

Posterior sau batch đầu có thể trở thành prior cho batch sau:

```math
p(\theta\mid D_1,D_2)
\propto p(D_2\mid\theta)p(\theta\mid D_1).
```

Điều này thể hiện consistency của sequential học tập (learning / 학습) khi các giả định (assumptions / 가정들) phù hợp.

Nó rất tự nhiên cho các hệ thống (systems / 시스템들) nhận dữ liệu (data / 데이터) liên tục.

> **Nối mạch:** Ở chặng này của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Computational suy luận (inference / 추론)** nối từ **Bayesian updating theo từng batch** sang **Calibration và bất định (uncertainty / 불확실성)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Computational suy luận (inference / 추론)

Trong simple conjugate các mô hình (models / 모델들) posterior có closed form. Với hiện đại (modern / 현대적) các mô hình (models / 모델들), integral khó tính nên cần numerical suy luận (inference / 추론).

MCMC tạo correlated samples từ posterior. Variational suy luận (inference / 추론) biến suy luận (inference / 추론) thành tối ưu hóa (optimization / 최적화) bằng cách chọn approximation `q(θ)` gần posterior thật.

Dùng chung (common / 공통) mục tiêu (objective / 목표) là minimize

```math
KL(q(\theta)\|p(\theta\mid D)).
```

hoặc maximize ELBO.

Sự đánh đổi (trade-off / 트레이드오프) thường là MCMC chính xác hơn asymptotically nhưng costly, còn variational methods nhanh hơn nhưng có approximation độ lệch (bias / 편향).

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Calibration và bất định (uncertainty / 불확실성)** nối từ **Computational suy luận (inference / 추론)** sang **Prior sensitivity**, vì cơ chế trước tạo đầu vào cho bước sau.

## Calibration và bất định (uncertainty / 불확실성)

Bayesian posterior bất định (uncertainty / 불확실성) chỉ meaningful nếu mô hình (model / 모델) cấu trúc (structure / 구조), likelihood và prior đủ hợp lý. Nếu mô hình (model / 모델) sai nghiêm trọng, posterior vẫn có thể rất concentrated nhưng quanh answer sai.

“Bayesian” không tự động đồng nghĩa “bất định (uncertainty / 불확실성) đúng”. mô hình (model / 모델) checking và sensitivity phân tích (analysis / 분석) là bắt buộc.

> **Nối mạch:** Trong **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Prior sensitivity** nối từ **Calibration và bất định (uncertainty / 불확실성)** sang **Example: tỷ lệ lỗi triển khai (deployment / 배포)**, vì cơ chế trước tạo đầu vào cho bước sau.

## Prior sensitivity

Khi dữ liệu (data / 데이터) rất lớn, reasonable priors thường ít ảnh hưởng. Khi dữ liệu (data / 데이터) ít hoặc likelihood weakly identifies parameters, prior có thể ảnh hưởng mạnh.

Thay vì che giấu điều này, nên vary plausible priors và xem conclusions thay đổi bao nhiêu.

Sensitivity phân tích (analysis / 분석) giúp phân biệt thông tin (information / 정보) đến từ dữ liệu (data / 데이터) hay các giả định (assumptions / 가정들).

> **Nối mạch:** Ở chặng này của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Prior sensitivity** nêu quy tắc; **Example: tỷ lệ lỗi triển khai (deployment / 배포)** thử quy tắc trong tình huống, rồi **Quyết định (decision / 결정) lý thuyết (theory / 이론)** mở rộng hệ quả.

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

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Example: tỷ lệ lỗi triển khai (deployment / 배포)** nêu quy tắc; **Quyết định (decision / 결정) lý thuyết (theory / 이론)** thử quy tắc trong tình huống, rồi **Mô hình tư duy (mental model / 사고 모델)** mở rộng hệ quả.

## Quyết định (decision / 결정) lý thuyết (theory / 이론)

Suy luận (inference / 추론) và quyết định (decision / 결정) là hai bước khác nhau. Posterior mô tả bất định (uncertainty / 불확실성); hành động (action / 동작) cần mất mát (loss / 손실) hoặc utility.

Optimal Bayesian hành động (action / 동작) minimize posterior expected mất mát (loss / 손실):

```math
a^*=\arg\min_a E[L(a,\theta)\mid D].
```

Trong nghiệp vụ (business / 비즈니스), same posterior có thể dẫn tới actions khác nhau nếu chi phí (cost / 비용) của false positive và false negative khác nhau.

Đây là lý do xác suất (probability / 확률) estimate không tự động quyết định threshold.

> **Nối mạch:** Trong **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** tổng hợp từ **Quyết định (decision / 결정) lý thuyết (theory / 이론)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** mở rộng hệ quả hoặc giới hạn liên quan.

## Mô hình tư duy (mental model / 사고 모델)

Bayesian suy luận (inference / 추론) là một chuỗi xử lý (pipeline / 파이프라인) của thông tin (information / 정보): prior mô tả trạng thái kiến thức (knowledge / 지식) trước dữ liệu (data / 데이터), likelihood mô tả cách dữ liệu (data / 데이터) được sinh ra nếu parameter có giá trị (value / 값) nhất định, posterior là kiến thức (knowledge / 지식) sau dữ liệu (data / 데이터), và posterior predictive biến updated kiến thức (knowledge / 지식) thành predictions. Hierarchical các mô hình (models / 모델들) cho phép thông tin (information / 정보) luồng (flow / 흐름) cả trong group lẫn giữa các groups.

> **Nối mạch:** Ở chặng này của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, **Dùng chung (common / 공통) Misconceptions** tổng hợp từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức** mở rộng hệ quả hoặc giới hạn liên quan.

## Dùng chung (common / 공통) Misconceptions

Prior không nhất thiết là opinion tùy ý và posterior cũng không “khách quan tuyệt đối”; cả mô hình (model / 모델) lẫn prior đều là các giả định (assumptions / 가정들) cần kiểm tra. MAP cũng không phải synonym của Bayesian suy luận (inference / 추론) vì nó chỉ giữ một chế độ (mode / 모드) của posterior.

Một misconception khác là credible interval và confidence interval cùng nghĩa. Con số có thể giống nhau trong một số mô hình (model / 모델) nhưng interpretation khác fundamentally.

> **Nối mạch:** Đặt trong câu hỏi lớn của **Bayesian suy luận (inference / 추론): posterior, predictive phân phối (distribution / 분포) và hierarchical các mô hình (models / 모델들)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Mục này khép mạch bằng cách nối kết quả với phạm vi của chapter.

## Liên kết kiến thức

Chapter này phát triển từ [Conditional probability and Bayes](./02_conditional_probability_and_bayes.md), [Likelihood, MLE, MAP](./10_likelihood_mle_map_and_model_selection.md) và [Stochastic processes](./11_stochastic_processes_markov_chains_and_time_series.md). Nó nối trực tiếp với regularization, probabilistic ML, Bayesian A/B testing, MCMC và quyết định (decision / 결정) lý thuyết (theory / 이론).

> **Bàn giao:** Sau **Liên kết kiến thức**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](../README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
