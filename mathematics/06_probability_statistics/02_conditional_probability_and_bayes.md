# Xác suất có điều kiện và Bayes: cập nhật bất định (uncertainty / 불확실성) khi thông tin (information / 정보) thay đổi

> **Mạch đọc:** Đọc **Xác suất có điều kiện và Bayes: cập nhật bất định (uncertainty / 불확실성) khi thông tin (information / 정보) thay đổi** như một mắt xích của lộ trình học (learning path / 학습 경로) hiện tại, không như một ghi chú tách rời. Nội dung đi từ **1. Conditional xác suất (probability / 확률) là renormalization của mẫu (sample / 표본) không gian (space / 공간)** sang **2. sản phẩm (product / 제품) quy tắc (rule / 규칙) đến trực tiếp từ definition**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Xác suất có điều kiện (conditional probability / 조건부 확률) formalize một việc rất tự nhiên: **xác suất (probability / 확률) phụ thuộc vào thông tin (information / 정보) đang có**.

Cùng một sự kiện (event / 이벤트) có thể có xác suất (probability / 확률) khác nhau khi ngữ cảnh (context / 맥락) thay đổi. Vì vậy dấu `|` trong

```math
P(A\mid B)
```

không phải decoration. Nó nói:

> Hãy tính xác suất (probability / 확률) của `A` trong một universe đã được thu hẹp bởi thông tin (information / 정보) `B`.

Bayes theorem sau đó giải một bài toán sâu hơn:

> Nếu ta biết bằng chứng (evidence / 증거) có khả năng xuất hiện thế nào dưới từng hypothesis, làm sao cập nhật xác suất (probability / 확률) của hypothesis sau khi bằng chứng (evidence / 증거) xuất hiện?

## 1. Conditional xác suất (probability / 확률) là renormalization của mẫu (sample / 표본) không gian (space / 공간)

Nếu `P(B)>0`:

```math
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)}.
```

Khi biết `B` xảy ra, tất cả outcomes ngoài `B` bị loại khỏi consideration. xác suất (probability / 확률) phải được renormalize để total mass trên `B` trở lại 1.

Geometric intuition:

```text
original universe: Ω
condition on B: chỉ giữ B
A|B: phần của B cũng nằm trong A
```

Do đó denominator `P(B)` không phải trick; nó rescale xác suất (probability / 확률) mass trên restricted universe.

## 2. sản phẩm (product / 제품) quy tắc (rule / 규칙) đến trực tiếp từ definition

Từ definition:

```math
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)},
```

suy ra:

```math
P(A\cap B)
=
P(A\mid B)P(B).
```

Tương tự:

```math
P(A\cap B)
=
P(B\mid A)P(A).
```

Sản phẩm (product / 제품) quy tắc (rule / 규칙) nói joint xác suất (probability / 확률) có thể factor thành:

```text
probability của context
× probability của event bên trong context
```

## 3. chuỗi (chain / 사슬) quy tắc (rule / 규칙) cho nhiều events

Với `A_1,\ldots,A_n`:

```math
P(A_1\cap\cdots\cap A_n)
=
P(A_1)
P(A_2\mid A_1)
P(A_3\mid A_1,A_2)
\cdots.
```

Đây là foundation của probabilistic chuỗi (sequence / 시퀀스) các mô hình (models / 모델들).

Ví dụ ngôn ngữ (language / 언어) mô hình (model / 모델) factorization:

```math
P(w_1,\ldots,w_n)
=
\prod_{i=1}^n
P(w_i\mid w_{<i}).
```

Hiện đại (modern / 현대적) autoregressive AI dùng đúng xác suất (probability / 확률) chuỗi (chain / 사슬) quy tắc (rule / 규칙) ở quy mô (scale / 규모) lớn.

## 4. Independence là statement về thông tin (information / 정보)

Events `A` và `B` independent nếu

```math
P(A\cap B)=P(A)P(B).
```

Equivalent khi probabilities phù hợp:

```math
P(A\mid B)=P(A).
```

Meaning:

> Biết `B` không thay đổi xác suất (probability / 확률) của `A` trong mô hình (model / 모델).

Independence không nghĩa events “không liên quan về mặt câu chuyện”; nó là mathematical thuộc tính (property / 속성) của joint phân phối (distribution / 분포).

## 5. Mutual exclusivity khác independence

Nếu `A` và `B` mutually exclusive:

```math
P(A\cap B)=0.
```

Nếu cả hai có positive xác suất (probability / 확률), chúng **không independent**, vì occurrence của `B` làm xác suất (probability / 확률) của `A` thành 0.

Đây là misconception rất phổ biến:

```text
cannot happen together ≠ independent
```

## 6. Conditional independence: concept quan trọng hơn ordinary independence trong các mô hình (models / 모델들)

`A` và `B` conditionally independent given `C` nếu:

```math
P(A,B\mid C)
=
P(A\mid C)P(B\mid C).
```

Hai variables có thể dependent overall nhưng independent sau khi biết hidden/dùng chung (common / 공통) cause.

Ví dụ:

```text
umbrella use ← rain → wet streets
```

Umbrella use và wet streets correlate. Nhưng nếu điều kiện (condition / 조건) on actual rain trạng thái (state / 상태), remaining dependence có thể giảm mạnh trong simplified mô hình (model / 모델).

Graphical các mô hình (models / 모델들), Naive Bayes và lập luận nhân quả (causal reasoning / 인과적 추론) dùng conditional independence liên tục.

## 7. Law of total xác suất (probability / 확률): average qua hidden cases

Nếu `B_1,\ldots,B_k` partition mẫu (sample / 표본) không gian (space / 공간):

```math
P(A)
=
\sum_i
P(A\mid B_i)P(B_i).
```

Interpretation:

```text
overall probability
= weighted average của case-specific probabilities
```

Weights chính là cơ sở (base / 기반) rates `P(B_i)`.

Đây thường là denominator trong Bayes theorem.

## 8. Bayes theorem derive bằng symmetry của joint xác suất (probability / 확률)

Ta có:

```math
P(A\cap B)
=P(B\mid A)P(A)
```

và

```math
P(A\cap B)
=P(A\mid B)P(B).
```

Equate:

```math
P(A\mid B)
=
\frac{P(B\mid A)P(A)}{P(B)}.
```

Bayes không tạo xác suất (probability / 확률) từ nothing. Nó reorganize joint xác suất (probability / 확률) để reverse conditioning direction.

## 9. Prior, likelihood, bằng chứng (evidence / 증거), posterior

Trong Bayesian notation:

```math
p(\theta\mid D)
=
\frac{p(D\mid\theta)p(\theta)}{p(D)}.
```

Các terms:

```text
p(θ)       prior
p(D|θ)     likelihood
p(D)       evidence / marginal likelihood
p(θ|D)     posterior
```

Mô hình tư duy (mental model / 사고 모델):

```text
posterior ∝ likelihood × prior
```

Posterior là prior sau khi reweight bởi mức độ mỗi hypothesis giải thích bằng chứng (evidence / 증거).

## 10. Likelihood không phải posterior

Likelihood:

```math
L(\theta;D)=p(D\mid\theta)
```

được xem như hàm (function / 함수) của `\theta` khi dữ liệu (data / 데이터) fixed.

Nó không cần integrate/sum thành 1 over `\theta`.

Posterior mới là xác suất (probability / 확률) phân phối (distribution / 분포) trên parameter/hypothesis khi prior được đưa vào và normalize.

Confusing likelihood with posterior dẫn tới nhiều lỗi khi đọc statistics/ML.

## 11. Medical-test example: cơ sở (base / 기반) tỷ lệ (rate / 비율) controls posterior

Giả sử:

```math
P(D)=0.01
```

sensitivity:

```math
P(+\mid D)=0.99
```

false-positive tỷ lệ (rate / 비율):

```math
P(+\mid D^c)=0.05.
```

Total positive:

```math
P(+)
=0.99(0.01)+0.05(0.99)
=0.0594.
```

Posterior:

```math
P(D\mid+)
=
\frac{0.99(0.01)}{0.0594}
\approx0.167.
```

Positive kết quả (result / 결과) chỉ đưa xác suất (probability / 확률) disease lên khoảng 16.7%, không phải 99%.

Sensitivity trả lời:

```text
P(test+ | disease)
```

nhưng patient thường quan tâm:

```text
P(disease | test+)
```

Hai quantities đảo conditioning direction.

## 12. Natural-frequency biểu diễn (representation / 표현) thường dễ hiểu hơn percentages

Giả sử 10,000 people.

Disease prevalence 1%:

```text
100 diseased
9,900 healthy
```

Sensitivity 99%:

```text
≈99 true positives
```

False positive 5%:

```text
≈495 false positives
```

Among positives:

```text
99 / (99+495) ≈ 16.7%
```

Frequency cây (tree / 트리) làm denominator trực quan hơn và giảm base-rate neglect.

## 13. Likelihood ratio là bằng chứng (evidence / 증거) multiplier

Positive likelihood ratio:

```math
LR^+
=
\frac{P(+\mid D)}{P(+\mid D^c)}.
```

Nó đo bằng chứng (evidence / 증거) `+` favor disease hypothesis bao nhiêu lần so với non-disease.

Bayes odds form:

```math
\text{posterior odds}
=
\text{prior odds}
\times LR.
```

Bằng chứng (evidence / 증거) cập nhật (update / 업데이트) trở thành multiplication.

## 14. Log-odds biến multiplicative bằng chứng (evidence / 증거) thành additive bằng chứng (evidence / 증거)

Odds:

```math
O(H)=\frac{P(H)}{1-P(H)}.
```

Take log:

```math
\log O(H\mid E)
=
\log O(H)
+
\log LR(E).
```

Đây là lý do log-odds/log-likelihood xuất hiện rộng trong statistics, logistic regression và bằng chứng (evidence / 증거) accumulation.

## 15. Sequential Bayesian updating

Với bằng chứng (evidence / 증거) `E_1,E_2,...`, posterior sau step trước trở thành prior cho step sau:

```text
prior
→ update with E1
→ posterior1
→ update with E2
→ posterior2
→ ...
```

Nếu evidences conditionally independent given hypothesis:

```math
p(E_1,\ldots,E_n\mid H)
=
\prod_i p(E_i\mid H).
```

Log-likelihoods add.

Nhưng nếu bằng chứng (evidence / 증거) correlated, multiplying as independent **double-counts thông tin (information / 정보)**.

## 16. Naive Bayes: intentionally strong conditional independence giả định (assumption / 가정)

Naive Bayes assumes features conditionally independent given lớp (class / 클래스):

```math
P(x_1,\ldots,x_d\mid y)
=
\prod_j P(x_j\mid y).
```

Giả định (assumption / 가정) thường không literally true, nhưng classifier vẫn có thể công việc (work / 작업) well if quyết định (decision / 결정) boundaries robust.

Important lesson:

```text
useful model ≠ literally true model
```

Hiệu năng (performance / 성능) và calibration cần empirical kiểm tra hợp lệ (validation / 검증).

## 17. Bayes denominator là mô hình (model / 모델) bằng chứng (evidence / 증거)

For hypotheses `H_i`:

```math
P(E)
=
\sum_i P(E\mid H_i)P(H_i).
```

Denominator đảm bảo posterior probabilities sum to 1.

Trong mô hình (model / 모델) comparison, marginal likelihood còn penalize parameter không gian (space / 공간) regions dự đoán dữ liệu (data / 데이터) kém, tạo Occam-like tác động (effect / 효과) under priors.

## 18. Continuous Bayes

For continuous parameter:

```math
p(\theta\mid D)
=
\frac{p(D\mid\theta)p(\theta)}
{\int p(D\mid\vartheta)p(\vartheta)d\vartheta}.
```

Denominator có thể khó compute, dẫn tới MCMC, variational suy luận (inference / 추론) và other approximate methods.

Concept Bayes simple; computation có thể hard.

## 19. Conjugate example: Beta–Bernoulli intuition

Suppose Bernoulli xác suất (probability / 확률) `p` unknown.

Prior:

```math
p\sim Beta(\alpha,\beta).
```

Observe `s` successes và `f` failures.

Posterior:

```math
p\mid D
\sim
Beta(\alpha+s,\beta+f).
```

Prior parameters behave like pseudo-counts.

This is a clean example of updating bất định (uncertainty / 불확실성), not just điểm (point / 지점) estimate.

## 20. Posterior predictive asks about future observations

Instead of only estimate parameter:

```math
p(\tilde y\mid D)
=
\int
p(\tilde y\mid\theta)
p(\theta\mid D)
d\theta.
```

Posterior predictive averages future prediction over parameter bất định (uncertainty / 불확실성).

This distinction matters:

```text
parameter uncertainty
≠ observation noise
```

Predictive phân phối (distribution / 분포) combines both.

## 21. Calibration vs discrimination

A mô hình (model / 모델) can rank high-risk cases well but đầu ra (output / 출력) probabilities that are miscalibrated.

If among all cases predicted `0.8`, roughly 80% actually occur over repeated comparable cases, mô hình (model / 모델) is calibrated at that mức (level / 수준).

Bayesian/probabilistic lập luận (reasoning / 추론) cares about xác suất (probability / 확률) chất lượng (quality / 품질), not only classification accuracy.

## 22. Selection effects thay đổi (change / 변경) conditional probabilities

Conditioning can introduce phụ thuộc (dependency / 의존성).

Classic collider mẫu (pattern / 패턴):

```text
A → C ← B
```

Even if `A` and `B` independent marginally, conditioning on `C` can make them dependent.

This is important in hiring/admission/medical samples: selecting only observed cases can create misleading correlations.

## 23. Simpson's paradox as conditioning warning

An aggregate trend can reverse when conditioning on a third variable.

Reason: group weights differ.

Therefore:

```text
P(A|B) across subgroups
```

cannot always be understood from aggregate `P(A|B)` alone.

Conditional xác suất (probability / 확률) is not just computational; it changes which population question is being asked.

## 24. nhân quả (causal / 인과적) interpretation requires more than Bayes theorem

Bayes updates beliefs about hypotheses under a xác suất (probability / 확률) mô hình (model / 모델).

Nhân quả (causal / 인과적) question asks:

```text
What happens if we intervene?
```

Conditioning:

```math
P(Y\mid X=x)
```

is not generally same as intervention phân phối (distribution / 분포):

```math
P(Y\mid do(X=x)).
```

Confounding can make them differ.

Bayesian suy luận (inference / 추론) and nhân quả (causal / 인과적) suy luận (inference / 추론) can combine, but Bayes theorem alone does not establish causality.

## 25. Fraud detection example

Suppose fraud tỷ lệ (rate / 비율):

```math
P(F)=0.001.
```

Detector:

```math
P(+\mid F)=0.95
```

```math
P(+\mid F^c)=0.01.
```

Then:

```math
P(+)
=0.95(0.001)+0.01(0.999)
=0.01094.
```

Posterior fraud xác suất (probability / 확률):

```math
P(F\mid+)
\approx
0.0868.
```

Even a strong detector yields many false alerts under extreme lớp (class / 클래스) imbalance.

Operations teams need posterior precision, not only sensitivity.

## 26. Finance liên kết (connection / 연결): bằng chứng (evidence / 증거) updates, regime probabilities

Suppose hypotheses represent thị trường (market / 시장) regimes:

```text
H1 = expansion
H2 = slowdown
```

Macro dữ liệu (data / 데이터) `E` reweights regime probabilities:

```math
P(H_i\mid E)
\propto
P(E\mid H_i)P(H_i).
```

Real các mô hình (models / 모델들) require continuous variables, thời gian (time / 시간) dependence and mô hình (model / 모델) bất định (uncertainty / 불확실성), but conceptual cấu trúc (structure / 구조) is Bayesian updating.

Do not confuse posterior xác suất (probability / 확률) with guaranteed forecast.

## 27. AI liên kết (connection / 연결): softmax and posterior-like normalization

Classifier logits `z_k` often converted:

```math
p_k=
\frac{e^{z_k}}
{\sum_j e^{z_j}}.
```

This creates normalized lớp (class / 클래스) probabilities under mô hình (model / 모델) interpretation.

But softmax đầu ra (output / 출력) is not automatically calibrated posterior xác suất (probability / 확률); huấn luyện (training / 학습) mục tiêu (objective / 목표)/dữ liệu (data / 데이터) shift/mô hình (model / 모델) misspecification matter.

Probabilistic notation does not guarantee probabilistic độ tin cậy (reliability / 신뢰성).

## 28. thông tin (information / 정보) lý thuyết (theory / 이론) liên kết (connection / 연결)

Bayesian bằng chứng (evidence / 증거) cập nhật (update / 업데이트) in log không gian (space / 공간):

```math
\log p(H\mid E)
=
\log p(E\mid H)
+
\log p(H)
-
\log p(E).
```

Surprisal:

```math
-\log p(E)
```

and log-likelihood ratios measure bằng chứng (evidence / 증거) on additive thông tin (information / 정보) quy mô (scale / 규모).

Bayes, log-loss and thông tin (information / 정보) lý thuyết (theory / 이론) share log-probability cấu trúc (structure / 구조).

## 29. Worked example: two tests are not automatically independent

Suppose two medical tests use similar biomarkers.

It is tempting to ghi (write / 쓰기):

```math
P(T_1,T_2\mid D)
=P(T_1\mid D)P(T_2\mid D).
```

But dùng chung (shared / 공유) đo lường (measurement / 측정) cơ chế (mechanism / 메커니즘) can make errors correlated.

If both false-positive for same biological reason, independence giả định (assumption / 가정) exaggerates combined bằng chứng (evidence / 증거).

Always ask:

```text
independent marginally?
independent conditional on hypothesis?
or not independent at all?
```

## 30. Practical Bayes checklist

When reading a xác suất (probability / 확률) cập nhật (update / 업데이트), identify:

```text
Hypothesis/event of interest?
Evidence?
Prior/base rate?
Likelihood under hypothesis?
Likelihood under alternatives?
Denominator / competing explanations?
Independence assumptions?
Selection mechanism?
Calibration evidence?
Causal or only associational claim?
```

## Liên kết kiến thức (knowledge connection / 지식 연결)

```text
conditional probability
→ product/chain rule
→ independence / conditional independence
→ total probability
→ Bayes theorem
→ odds / likelihood ratios
→ log-likelihood
→ Bayesian inference
→ graphical models
→ classification calibration
→ causal-conditioning distinction
```

## Mô hình tư duy (mental model / 사고 모델)

> Conditional xác suất (probability / 확률) changes the universe you are lập luận (reasoning / 추론) inside. Bayes theorem then **reweights competing hypotheses by how well they predict the bằng chứng (evidence / 증거)**, while preserving cơ sở (base / 기반) rates. bằng chứng (evidence / 증거) is strong only relative to alternatives, and multiple pieces of bằng chứng (evidence / 증거) can be multiplied safely only when the phụ thuộc (dependency / 의존성) các giả định (assumptions / 가정들) justify it.

## Dùng chung (common / 공통) Misconceptions

`P(A|B)` is not `P(B|A)`. Sensitivity is not positive predictive giá trị (value / 값). High classifier accuracy under lớp (class / 클래스) imbalance may say little about posterior precision. Likelihood is not posterior. Bayesian updating cannot rescue a bad likelihood mô hình (model / 모델) or unjustified prior. Conditional independence must be modeled, not assumed because features “look different”. Conditioning can create correlations through selection. Bayes theorem updates association under a mô hình (model / 모델); it does not by itself prove nhân quả (causal / 인과적) effects.

> **Bàn giao:** Sau **dùng chung (common / 공통) Misconceptions**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 counting and combinatorics](./00_counting_and_combinatorics.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
