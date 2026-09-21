# Xác suất có điều kiện và Bayes: cập nhật uncertainty khi information thay đổi

Xác suất có điều kiện (conditional probability / 조건부 확률) formalize một việc rất tự nhiên: **probability phụ thuộc vào information đang có**.

Cùng một event có thể có probability khác nhau khi context thay đổi. Vì vậy dấu `|` trong

```math
P(A\mid B)
```

không phải decoration. Nó nói:

> Hãy tính probability của `A` trong một universe đã được thu hẹp bởi information `B`.

Bayes theorem sau đó giải một bài toán sâu hơn:

> Nếu ta biết evidence có khả năng xuất hiện thế nào dưới từng hypothesis, làm sao cập nhật probability của hypothesis sau khi evidence xuất hiện?

## 1. Conditional probability là renormalization của sample space

Nếu `P(B)>0`:

```math
P(A\mid B)
=
\frac{P(A\cap B)}{P(B)}.
```

Khi biết `B` xảy ra, tất cả outcomes ngoài `B` bị loại khỏi consideration. Probability phải được renormalize để total mass trên `B` trở lại 1.

Geometric intuition:

```text
original universe: Ω
condition on B: chỉ giữ B
A|B: phần của B cũng nằm trong A
```

Do đó denominator `P(B)` không phải trick; nó rescale probability mass trên restricted universe.

## 2. Product rule đến trực tiếp từ definition

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

Product rule nói joint probability có thể factor thành:

```text
probability của context
× probability của event bên trong context
```

## 3. Chain rule cho nhiều events

Với `A_1,\ldots,A_n`:

```math
P(A_1\cap\cdots\cap A_n)
=
P(A_1)
P(A_2\mid A_1)
P(A_3\mid A_1,A_2)
\cdots.
```

Đây là foundation của probabilistic sequence models.

Ví dụ language model factorization:

```math
P(w_1,\ldots,w_n)
=
\prod_{i=1}^n
P(w_i\mid w_{<i}).
```

Modern autoregressive AI dùng đúng probability chain rule ở scale lớn.

## 4. Independence là statement về information

Events `A` và `B` independent nếu

```math
P(A\cap B)=P(A)P(B).
```

Equivalent khi probabilities phù hợp:

```math
P(A\mid B)=P(A).
```

Meaning:

> Biết `B` không thay đổi probability của `A` trong model.

Independence không nghĩa events “không liên quan về mặt câu chuyện”; nó là mathematical property của joint distribution.

## 5. Mutual exclusivity khác independence

Nếu `A` và `B` mutually exclusive:

```math
P(A\cap B)=0.
```

Nếu cả hai có positive probability, chúng **không independent**, vì occurrence của `B` làm probability của `A` thành 0.

Đây là misconception rất phổ biến:

```text
cannot happen together ≠ independent
```

## 6. Conditional independence: concept quan trọng hơn ordinary independence trong models

`A` và `B` conditionally independent given `C` nếu:

```math
P(A,B\mid C)
=
P(A\mid C)P(B\mid C).
```

Hai variables có thể dependent overall nhưng independent sau khi biết hidden/common cause.

Ví dụ:

```text
umbrella use ← rain → wet streets
```

Umbrella use và wet streets correlate. Nhưng nếu condition on actual rain state, remaining dependence có thể giảm mạnh trong simplified model.

Graphical models, Naive Bayes và causal reasoning dùng conditional independence liên tục.

## 7. Law of total probability: average qua hidden cases

Nếu `B_1,\ldots,B_k` partition sample space:

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

Weights chính là base rates `P(B_i)`.

Đây thường là denominator trong Bayes theorem.

## 8. Bayes theorem derive bằng symmetry của joint probability

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

Bayes không tạo probability từ nothing. Nó reorganize joint probability để reverse conditioning direction.

## 9. Prior, likelihood, evidence, posterior

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

Mental model:

```text
posterior ∝ likelihood × prior
```

Posterior là prior sau khi reweight bởi mức độ mỗi hypothesis giải thích evidence.

## 10. Likelihood không phải posterior

Likelihood:

```math
L(\theta;D)=p(D\mid\theta)
```

được xem như function của `\theta` khi data fixed.

Nó không cần integrate/sum thành 1 over `\theta`.

Posterior mới là probability distribution trên parameter/hypothesis khi prior được đưa vào và normalize.

Confusing likelihood with posterior dẫn tới nhiều lỗi khi đọc statistics/ML.

## 11. Medical-test example: base rate controls posterior

Giả sử:

```math
P(D)=0.01
```

sensitivity:

```math
P(+\mid D)=0.99
```

false-positive rate:

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

Positive result chỉ đưa probability disease lên khoảng 16.7%, không phải 99%.

Sensitivity trả lời:

```text
P(test+ | disease)
```

nhưng patient thường quan tâm:

```text
P(disease | test+)
```

Hai quantities đảo conditioning direction.

## 12. Natural-frequency representation thường dễ hiểu hơn percentages

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

Frequency tree làm denominator trực quan hơn và giảm base-rate neglect.

## 13. Likelihood ratio là evidence multiplier

Positive likelihood ratio:

```math
LR^+
=
\frac{P(+\mid D)}{P(+\mid D^c)}.
```

Nó đo evidence `+` favor disease hypothesis bao nhiêu lần so với non-disease.

Bayes odds form:

```math
\text{posterior odds}
=
\text{prior odds}
\times LR.
```

Evidence update trở thành multiplication.

## 14. Log-odds biến multiplicative evidence thành additive evidence

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

Đây là lý do log-odds/log-likelihood xuất hiện rộng trong statistics, logistic regression và evidence accumulation.

## 15. Sequential Bayesian updating

Với evidence `E_1,E_2,...`, posterior sau step trước trở thành prior cho step sau:

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

Nhưng nếu evidence correlated, multiplying as independent **double-counts information**.

## 16. Naive Bayes: intentionally strong conditional independence assumption

Naive Bayes assumes features conditionally independent given class:

```math
P(x_1,\ldots,x_d\mid y)
=
\prod_j P(x_j\mid y).
```

Assumption thường không literally true, nhưng classifier vẫn có thể work well if decision boundaries robust.

Important lesson:

```text
useful model ≠ literally true model
```

Performance và calibration cần empirical validation.

## 17. Bayes denominator là model evidence

For hypotheses `H_i`:

```math
P(E)
=
\sum_i P(E\mid H_i)P(H_i).
```

Denominator đảm bảo posterior probabilities sum to 1.

Trong model comparison, marginal likelihood còn penalize parameter space regions dự đoán data kém, tạo Occam-like effect under priors.

## 18. Continuous Bayes

For continuous parameter:

```math
p(\theta\mid D)
=
\frac{p(D\mid\theta)p(\theta)}
{\int p(D\mid\vartheta)p(\vartheta)d\vartheta}.
```

Denominator có thể khó compute, dẫn tới MCMC, variational inference và other approximate methods.

Concept Bayes simple; computation có thể hard.

## 19. Conjugate example: Beta–Bernoulli intuition

Suppose Bernoulli probability `p` unknown.

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

This is a clean example of updating uncertainty, not just point estimate.

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

Posterior predictive averages future prediction over parameter uncertainty.

This distinction matters:

```text
parameter uncertainty
≠ observation noise
```

Predictive distribution combines both.

## 21. Calibration vs discrimination

A model can rank high-risk cases well but output probabilities that are miscalibrated.

If among all cases predicted `0.8`, roughly 80% actually occur over repeated comparable cases, model is calibrated at that level.

Bayesian/probabilistic reasoning cares about probability quality, not only classification accuracy.

## 22. Selection effects change conditional probabilities

Conditioning can introduce dependency.

Classic collider pattern:

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

Conditional probability is not just computational; it changes which population question is being asked.

## 24. Causal interpretation requires more than Bayes theorem

Bayes updates beliefs about hypotheses under a probability model.

Causal question asks:

```text
What happens if we intervene?
```

Conditioning:

```math
P(Y\mid X=x)
```

is not generally same as intervention distribution:

```math
P(Y\mid do(X=x)).
```

Confounding can make them differ.

Bayesian inference and causal inference can combine, but Bayes theorem alone does not establish causality.

## 25. Fraud detection example

Suppose fraud rate:

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

Posterior fraud probability:

```math
P(F\mid+)
\approx
0.0868.
```

Even a strong detector yields many false alerts under extreme class imbalance.

Operations teams need posterior precision, not only sensitivity.

## 26. Finance connection: evidence updates, regime probabilities

Suppose hypotheses represent market regimes:

```text
H1 = expansion
H2 = slowdown
```

Macro data `E` reweights regime probabilities:

```math
P(H_i\mid E)
\propto
P(E\mid H_i)P(H_i).
```

Real models require continuous variables, time dependence and model uncertainty, but conceptual structure is Bayesian updating.

Do not confuse posterior probability with guaranteed forecast.

## 27. AI connection: softmax and posterior-like normalization

Classifier logits `z_k` often converted:

```math
p_k=
\frac{e^{z_k}}
{\sum_j e^{z_j}}.
```

This creates normalized class probabilities under model interpretation.

But softmax output is not automatically calibrated posterior probability; training objective/data shift/model misspecification matter.

Probabilistic notation does not guarantee probabilistic reliability.

## 28. Information theory connection

Bayesian evidence update in log space:

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

and log-likelihood ratios measure evidence on additive information scale.

Bayes, log-loss and information theory share log-probability structure.

## 29. Worked example: two tests are not automatically independent

Suppose two medical tests use similar biomarkers.

It is tempting to write:

```math
P(T_1,T_2\mid D)
=P(T_1\mid D)P(T_2\mid D).
```

But shared measurement mechanism can make errors correlated.

If both false-positive for same biological reason, independence assumption exaggerates combined evidence.

Always ask:

```text
independent marginally?
independent conditional on hypothesis?
or not independent at all?
```

## 30. Practical Bayes checklist

When reading a probability update, identify:

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

## Knowledge Connection

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

## Mental Model

> Conditional probability changes the universe you are reasoning inside. Bayes theorem then **reweights competing hypotheses by how well they predict the evidence**, while preserving base rates. Evidence is strong only relative to alternatives, and multiple pieces of evidence can be multiplied safely only when the dependency assumptions justify it.

## Common Misconceptions

`P(A|B)` is not `P(B|A)`. Sensitivity is not positive predictive value. High classifier accuracy under class imbalance may say little about posterior precision. Likelihood is not posterior. Bayesian updating cannot rescue a bad likelihood model or unjustified prior. Conditional independence must be modeled, not assumed because features “look different”. Conditioning can create correlations through selection. Bayes theorem updates association under a model; it does not by itself prove causal effects.