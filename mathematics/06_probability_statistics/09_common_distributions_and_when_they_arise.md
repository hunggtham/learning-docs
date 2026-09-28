# Các phân phối xác suất thường gặp và vì sao chúng xuất hiện

> **Mạch đọc:** Đọc **Các phân phối xác suất thường gặp và vì sao chúng xuất hiện** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. phân phối (distribution / 분포) là mô hình (model / 모델), không phải nhãn histogram** sang **2. Bernoulli: một trial, hai outcomes**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Một phân phối (distribution / 분포) không nên được học như một dòng trong bảng công thức. Cách học bền hơn là hỏi ba câu:

```text
variable sống trên support nào?
mechanism ngẫu nhiên nào sinh ra nó?
assumptions nào khiến model đó hợp lý?
```

Khi hiểu cơ chế (mechanism / 메커니즘), ta nhớ phân phối (distribution / 분포) bằng cấu trúc (structure / 구조) thay vì hình curve.

## 1. phân phối (distribution / 분포) là mô hình (model / 모델), không phải nhãn histogram

Hai datasets có histogram tương tự nhưng mechanisms khác nhau có thể cần các mô hình (models / 모델들) khác nhau. Ngược lại, cùng một cơ chế (mechanism / 메커니즘) dưới nhiều regimes có thể dẫn tới approximate distributions khác nhau.

Vì vậy lựa chọn phân phối (distribution / 분포) cần xét:

```text
support
sampling mechanism
independence / stationarity
count vs waiting time
boundedness
skew / tails
```

## 2. Bernoulli: một trial, hai outcomes

Bernoulli random variable:

```math
X\in\{0,1\}
```

với:

```math
P(X=1)=p,
\qquad
P(X=0)=1-p.
```

Mean:

```math
E[X]=p.
```

Variance:

```math
\operatorname{Var}(X)=p(1-p).
```

Bernoulli là atomic building khối (block / 블록) của nhiều count các mô hình (models / 모델들).

Examples: click/no-click, pass/thất bại (fail / 실패), default/no-default, conversion/no-conversion.

## 3. Indicator variables

Một sự kiện (event / 이벤트) `A` có indicator:

```math
I_A=
\begin{cases}
1 & A\text{ xảy ra}\\
0 & \text{ngược lại}
\end{cases}
```

Then:

```math
E[I_A]=P(A).
```

Đây là cầu nối (bridge / 브리지) quan trọng giữa events và random variables. Tổng indicators biến counting bài toán (problem / 문제) thành expectation bài toán (problem / 문제).

## 4. Binomial: số successes trong fixed trials

Nếu:

```text
n fixed trials
independent
same success probability p
```

thì:

```math
X\sim\operatorname{Binomial}(n,p)
```

với:

```math
P(X=k)=\binom nk p^k(1-p)^{n-k}.
```

Mean:

```math
np.
```

Variance:

```math
np(1-p).
```

`\binom nk` xuất hiện vì có `C(n,k)` ways đặt `k` successes vào `n` trial positions.

## 5. Khi binomial không phù hợp

Binomial có thể sai nếu:

```text
p thay đổi theo trial
trials phụ thuộc nhau
sampling without replacement từ population nhỏ
```

Trong without-replacement sampling, hypergeometric thường tự nhiên hơn.

## 6. Hypergeometric: sampling without replacement

Population `N`, trong đó `K` successes. Draw `n` without replacement. Số successes `X`:

```math
P(X=k)
=
\frac{\binom Kk\binom{N-K}{n-k}}
{\binom Nn}.
```

Khác binomial ở dependence: mỗi draw thay composition còn lại.

Khi population rất lớn relative to mẫu (sample / 표본), binomial có thể approximate hypergeometric.

## 7. Geometric: waiting tới success đầu tiên

```math
P(X=k)=(1-p)^{k-1}p,
\qquad k=1,2,\ldots
```

Mean:

```math
E[X]=\frac1p.
```

Memoryless thuộc tính (property / 속성):

```math
P(X>s+t\mid X>s)=P(X>t).
```

Thuộc tính (property / 속성) này không phải “thế giới quên quá khứ”; nó là consequence của constant independent success xác suất (probability / 확률) giả định (assumption / 가정).

## 8. Negative binomial: chờ tới nhiều successes

Nếu geometric chờ success thứ nhất, negative binomial generalizes tới number trials/failures trước success thứ `r`.

Nó cũng hữu ích cho overdispersed count dữ liệu (data / 데이터) trong một số parameterizations/các mô hình (models / 모델들).

Điều quan trọng là check convention vì textbooks/software có nhiều cách định nghĩa hỗ trợ (support / 지원).

## 9. Poisson: count events theo tỷ lệ (rate / 비율)

Poisson phân phối (distribution / 분포):

```math
P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!}.
```

Mean = variance:

```math
E[X]=\operatorname{Var}(X)=\lambda.
```

Poisson tự nhiên khi events xuất hiện theo tỷ lệ (rate / 비율) ổn định trong interval và increments có independence/rare-event cấu trúc (structure / 구조) phù hợp.

## 10. Poisson từ rare-event limit

Binomial với:

```text
n lớn
p nhỏ
np≈λ
```

có limit gần Poisson:

```math
\operatorname{Binomial}(n,p)
\approx
\operatorname{Poisson}(\lambda).
```

Đây là liên kết (connection / 연결) cơ chế (mechanism / 메커니즘) quan trọng: nhiều opportunities, mỗi sự kiện (event / 이벤트) hiếm, total expected count finite.

## 11. Overdispersion cảnh báo mô hình (model / 모델) sai

Poisson bắt buộc:

```math
\operatorname{Var}(X)=E[X].
```

Nếu dữ liệu (data / 데이터) count có variance lớn hơn mean rất nhiều, có thể có clustering, heterogeneous rates hoặc dependence.

Negative binomial hoặc hierarchical các mô hình (models / 모델들) có thể hợp lý hơn.

## 12. Exponential: waiting thời gian (time / 시간) trong Poisson tiến trình (process / 프로세스)

Nếu events theo homogeneous Poisson tiến trình (process / 프로세스) tỷ lệ (rate / 비율) `\lambda`, waiting thời gian (time / 시간) `T`:

```math
f(t)=\lambda e^{-\lambda t},
\qquad t\ge0.
```

Mean:

```math
E[T]=\frac1\lambda.
```

Survival hàm (function / 함수):

```math
P(T>t)=e^{-\lambda t}.
```

Exponential là continuous memoryless phân phối (distribution / 분포).

## 13. Hazard tỷ lệ (rate / 비율)

Hazard:

```math
h(t)=\frac{f(t)}{P(T>t)}.
```

Với exponential:

```math
h(t)=\lambda.
```

Constant hazard là statement mạnh. Nếu thất bại (failure / 실패) rủi ro (risk / 위험) tăng theo age, exponential có thể không phù hợp.

## 14. Gamma: sum của exponential waiting times

Nếu `T_i` exponential independent cùng tỷ lệ (rate / 비율), tổng nhiều waiting times có gamma phân phối (distribution / 분포).

Gamma hỗ trợ (support / 지원) trên positive reals và linh hoạt cho right-skewed quantities.

Special cases liên hệ exponential và chi-square.

## 15. Uniform: symmetry theo interval

Continuous uniform trên `[a,b]`:

```math
f(x)=\frac1{b-a}.
```

Equal-length subintervals có equal xác suất (probability / 확률).

Uniform không đồng nghĩa “ta không biết gì” một cách bất biến (invariant / 불변식). Uniform trong `x` không còn uniform sau nonlinear reparameterization `y=g(x)`.

Đây là caution quan trọng trong Bayesian priors.

## 16. Normal/Gaussian: additive fluctuation cấu trúc (structure / 구조)

Normal density:

```math
f(x)
=
\frac1{\sigma\sqrt{2\pi}}
\exp\left(
-\frac{(x-\mu)^2}{2\sigma^2}
\right).
```

Gaussian xuất hiện tự nhiên khi quantity là aggregate của nhiều small contributions và CLT conditions approximately hold.

Nhưng raw dữ liệu (data / 데이터) không cần normal để mẫu (sample / 표본) mean trở nên approximately Gaussian.

## 17. tiêu chuẩn (standard / 표준) normal và z-score

Nếu:

```math
X\sim N(\mu,\sigma^2),
```

thì:

```math
Z=\frac{X-\mu}{\sigma}\sim N(0,1).
```

Standardization chuyển location/quy mô (scale / 규모) về tham chiếu (reference / 참조) phân phối (distribution / 분포).

Nhưng z-score chỉ có interpretation “bao nhiêu tiêu chuẩn (standard / 표준) deviations” và không tự biến heavy-tailed dữ liệu (data / 데이터) thành Gaussian.

## 18. Gaussian stability dưới tuyến tính (linear / 선형) combinations

Nếu Gaussian variables jointly Gaussian, tuyến tính (linear / 선형) combination vẫn Gaussian.

Đây là một reason Gaussian các mô hình (models / 모델들) tractable trong tín hiệu (signal / 신호) processing, Kalman filters và analytical statistics.

## 19. Student's t: extra bất định (uncertainty / 불확실성) từ estimate quy mô (scale / 규모)

Khi mean suy luận (inference / 추론) dùng unknown population variance và mẫu (sample / 표본) tiêu chuẩn (standard / 표준) deviation, statistic có heavier-tailed `t` phân phối (distribution / 분포) dưới tiêu chuẩn (standard / 표준) normal-sampling các giả định (assumptions / 가정들).

`t` tails phản ánh bất định (uncertainty / 불확실성) thêm do estimate `\sigma`.

Khi degrees of freedom tăng:

```text
t → normal
```

vì quy mô (scale / 규모) estimate stabilizes.

## 20. Chi-square: sum of squared tiêu chuẩn (standard / 표준) normals

Nếu:

```math
Z_i\sim N(0,1)
```

independent, then:

```math
\sum_{i=1}^k Z_i^2
\sim \chi_k^2.
```

Chi-square naturally appears in variance suy luận (inference / 추론) và quadratic Gaussian hình học (geometry / 기하학).

Mean:

```math
k.
```

Variance:

```math
2k.
```

## 21. F phân phối (distribution / 분포)

Ratio of scaled independent chi-square variables:

```math
F=
\frac{U_1/d_1}{U_2/d_2}
```

có F phân phối (distribution / 분포).

Nó xuất hiện trong variance comparisons, ANOVA và regression mô hình (model / 모델) comparisons trong classical khung phần mềm (framework / 프레임워크).

## 22. Beta: bất định (uncertainty / 불확실성) trên xác suất (probability / 확률)/proportion

Beta density proportional to:

```math
p^{\alpha-1}(1-p)^{\beta-1},
\qquad 0<p<1.
```

Hỗ trợ (support / 지원) `[0,1]` làm nó natural cho xác suất (probability / 확률) parameter.

Bernoulli/binomial likelihood + beta prior tạo beta posterior:

```text
prior pseudo-counts
+ observed successes/failures
→ posterior parameters
```

## 23. Dirichlet: multivariate beta

Nếu xác suất (probability / 확률) véc-tơ (vector / 벡터):

```math
(p_1,\ldots,p_K),
\qquad \sum_i p_i=1,
```

Dirichlet phân phối (distribution / 분포) là dùng chung (common / 공통) mô hình (model / 모델) trên simplex và conjugate prior cho categorical/multinomial probabilities.

Đây là cầu nối (bridge / 브리지) tới topic modeling, categorical Bayesian các mô hình (models / 모델들) và compositional probabilities.

## 24. Multinomial: counts across multiple categories

Generalizes binomial. Với `n` independent categorical trials, probabilities `p_1,...,p_K`, counts `X_i` thỏa:

```math
\sum_iX_i=n.
```

Xác suất (probability / 확률):

```math
P(X_1=x_1,\ldots,X_K=x_K)
=
\frac{n!}{\prod_i x_i!}
\prod_i p_i^{x_i}.
```

Multinomial coefficient đếm arrangements của category labels.

## 25. Log-normal: multiplicative mechanisms

Nếu:

```math
\log X\sim N(\mu,\sigma^2),
```

thì `X` log-normal.

Nó thường arise khi quantity là sản phẩm (product / 제품) của many positive random factors hơn là sum.

Income, size-like quantities hoặc multiplicative growth đôi khi có log-normal-like hành vi (behavior / 동작), nhưng empirical kiểm tra hợp lệ (validation / 검증) vẫn cần.

## 26. Power-law và heavy-tail caution

Không phải mọi heavy-tailed histogram là power law.

Power-law-like mô hình (model / 모델):

```math
P(X>x)\propto x^{-\alpha}
```

trên suitable tail region.

Estimating tail exponent và cutoff cần statistical care; log-log straight line bằng mắt không đủ.

## 27. phân phối (distribution / 분포) families và maximum entropy intuition

Một số distributions có thể được characterized bởi các ràng buộc (constraints / 제약조건들) + maximum entropy.

Ví dụ Gaussian maximizes differential entropy among distributions with fixed mean/variance under suitable conditions.

This perspective links phân phối (distribution / 분포) choice với thông tin (information / 정보) lý thuyết (theory / 이론), nhưng không có nghĩa Gaussian là correct mô hình (model / 모델) chỉ vì ta biết mean/variance.

## 28. Approximation relationships

Một useful map:

```text
Binomial(n,p), n large p small → Poisson(np)
Binomial with np,n(1-p) large → Normal approximation
Poisson λ large → approximately Normal
Student t, df large → Normal
```

Approximation cần regime conditions và continuity corrections đôi khi matter.

## 29. Worked example: choose a mô hình (model / 모델)

Question: số failed requests trong 10 minutes.

Nếu requests independent rare failures với approximately constant tỷ lệ (rate / 비율), Poisson count mô hình (model / 모델) có thể là starting điểm (point / 지점).

Nếu total requests fixed `n` và mỗi yêu cầu (request / 요청) thất bại (failure / 실패) xác suất (probability / 확률) roughly same `p`, binomial may be more natural.

Nếu failures cluster theo outages, neither simple mô hình (model / 모델) may fit; dependence/mixture/hierarchical mô hình (model / 모델) cần được xét.

Cơ chế (mechanism / 메커니즘) quyết định mô hình (model / 모델) family.

## 30. hỗ trợ (support / 지원) là sanity check đầu tiên

Examples:

```text
Bernoulli → {0,1}
Binomial → {0,...,n}
Poisson → nonnegative integers
Exponential/Gamma → positive reals
Beta → [0,1]
Normal → all real numbers
```

Nếu mô hình (model / 모델) assign nontrivial xác suất (probability / 확률) outside physically possible phạm vi (range / 범위), phải giải thích approximation hoặc chọn family khác.

## 31. Finance liên kết (connection / 연결)

Asset returns often show heavier tails and volatility clustering than iid Gaussian giả định (assumption / 가정). Gaussian vẫn useful analytical baseline, nhưng rủi ro (risk / 위험) estimates có thể understated nếu mô hình (model / 모델) tails sai.

Positive quantities như prices không nên modeled naïvely bằng unbounded normal levels nếu negative hỗ trợ (support / 지원) vô nghĩa; log-return các mô hình (models / 모델들) thường được dùng vì multiplicative cấu trúc (structure / 구조).

## 32. AI liên kết (connection / 연결)

Dùng chung (common / 공통) mappings:

```text
Bernoulli → binary labels
Categorical → multiclass labels
Gaussian → continuous noise / latent variables
Dirichlet → uncertainty over categorical probabilities
Poisson → count outputs
```

Mất mát (loss / 손실) functions often correspond to negative log-likelihoods of assumed distributions. Chọn mất mát (loss / 손실) nghĩa là ngầm chọn lỗi (error / 오류) mô hình (model / 모델).

## Mô hình tư duy (mental model / 사고 모델)

> phân phối (distribution / 분포) là compressed description của một stochastic cơ chế (mechanism / 메커니즘). hỗ trợ (support / 지원) cho biết values nào có thể tồn tại; parameters cho biết quy mô (scale / 규모)/tỷ lệ (rate / 비율)/shape; các giả định (assumptions / 가정들) cho biết khi nào mô hình (model / 모델) có quyền được dùng.

## Dùng chung (common / 공통) Misconceptions

Histogram giống bell shape không chứng minh Gaussian. Poisson không phù hợp chỉ vì dữ liệu (data / 데이터) là counts. Uniform prior không bất biến (invariant / 불변식) dưới reparameterization. Continuous density giá trị (value / 값) không phải điểm (point / 지점) xác suất (probability / 확률). A good-fitting phân phối (distribution / 분포) không tự chứng minh cơ chế (mechanism / 메커니즘) nhân quả (causal / 인과적) đúng.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 counting and combinatorics](./00_counting_and_combinatorics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
