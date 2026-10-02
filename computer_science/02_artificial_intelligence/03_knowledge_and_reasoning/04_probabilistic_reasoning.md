# Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Probabilistic reasoning trong AI**. Route đi từ uncertainty models → Bayesian update → likelihood/priors → decision/calibration → approximate inference, để niềm tin được cập nhật bằng evidence và loss.

Classical lô-gic (logic / 논리) asks whether proposition follows or not. Real AI often cannot công việc (work / 작업) with nhị phân (binary / 이진) certainty. Sensor noisy, diagnosis ambiguous, người dùng (user / 사용자) intent uncertain và kiến thức (knowledge / 지식) incomplete. **Probabilistic lập luận (reasoning / 추론)** extends lập luận (reasoning / 추론) by assigning and updating degrees of belief under a xác suất (probability / 확률) mô hình (model / 모델).

The cốt lõi (core / 핵심) question changes from:

> Is hypothesis H logically entailed?

to:

> Given bằng chứng (evidence / 증거) E, how should belief `P(H|E)` thay đổi (change / 변경)?

Xem trước: [Probability for AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Inference and Reasoning](./03_inference_and_reasoning.md).

## Bất định (uncertainty / 불확실성) is not ignorance alone

Bất định (uncertainty / 불확실성) can come from:

- inherent randomness;
- đo lường (measurement / 측정) noise;
- hidden variables;
- incomplete kiến thức (knowledge / 지식);
- limited dữ liệu (data / 데이터);
- mô hình (model / 모델) approximation.

A single xác suất (probability / 확률) number may mix several sources. Good hệ thống (system / 시스템) thiết kế (design / 설계) tries separate what can be reduced by more thông tin (information / 정보) from what is irreducible.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Bayesian cập nhật (update / 업데이트)** tiếp nhận điểm tựa từ **Bất định (uncertainty / 불확실성) is not ignorance alone** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Odds form** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bayesian cập nhật (update / 업데이트)

Bayes' quy tắc (rule / 규칙):

\[
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
\]

Interpretation:

```text
prior belief
   ×
likelihood of evidence under hypothesis
   ↓
posterior belief
```

Normalization `P(E)` makes probabilities sum to 1.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Odds form** tiếp nhận điểm tựa từ **Bayesian cập nhật (update / 업데이트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cơ sở (base / 기반) tỷ lệ (rate / 비율) matters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Odds form

Bayes can be expressed with odds:

\[
\frac{P(H\mid E)}{P(\neg H\mid E)}
=
\frac{P(H)}{P(\neg H)}
\times
\frac{P(E\mid H)}{P(E\mid\neg H)}
\]

Likelihood ratio tells how strongly bằng chứng (evidence / 증거) shifts odds.

This is useful in medical testing and bằng chứng (evidence / 증거) accumulation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Cơ sở (base / 기반) tỷ lệ (rate / 비율) matters** tiếp nhận điểm tựa từ **Odds form** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multiple bằng chứng (evidence / 증거)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cơ sở (base / 기반) tỷ lệ (rate / 비율) matters

Rare-event detection often suffers base-rate neglect.

Even high sensitivity/specificity may yield low posterior positive xác suất (probability / 확률) when prevalence very low.

Fraud, anomaly detection and bảo mật (security / 보안) alerts require careful cơ sở (base / 기반) rates; otherwise false positives dominate.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Cơ sở (base / 기반) tỷ lệ (rate / 비율) matters** nêu điều cần giải thích; **Multiple bằng chứng (evidence / 증거)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Naive Bayes** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multiple bằng chứng (evidence / 증거)

If bằng chứng (evidence / 증거) `E1,E2` conditionally independent given H:

\[
P(E_1,E_2\mid H)=P(E_1\mid H)P(E_2\mid H)
\]

Then likelihoods multiply.

But naive independence các giả định (assumptions / 가정들) can double-count correlated bằng chứng (evidence / 증거).

Example two fraud signals derived from same IP reputation nguồn (source / 소스) are not independent just because represented as separate features.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Multiple bằng chứng (evidence / 증거)** nêu điều cần giải thích; **Naive Bayes** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Generative vs discriminative modeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Naive Bayes

Naive Bayes assumes features conditionally independent given lớp (class / 클래스):

\[
P(x_1,...,x_d\mid y)=\prod_i P(x_i\mid y)
\]

Then:

\[
P(y\mid x)\propto P(y)\prod_i P(x_i\mid y)
\]

Giả định (assumption / 가정) often false, yet classifier can công việc (work / 작업) surprisingly well because quyết định (decision / 결정) ranh giới (boundary / 경계) may still be useful and estimation easy.

This is lesson: mô hình (model / 모델) các giả định (assumptions / 가정들) can be wrong literally but useful operationally.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Generative vs discriminative modeling** tiếp nhận điểm tựa từ **Naive Bayes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Latent variables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Generative vs discriminative modeling

Generative classifier các mô hình (models / 모델들) joint cấu trúc (structure / 구조):

\[
P(X,Y)=P(Y)P(X\mid Y)
\]

Discriminative mô hình (model / 모델) directly các mô hình (models / 모델들):

\[
P(Y\mid X)
\]

Naive Bayes generative; logistic regression discriminative.

Generative mô hình (model / 모델) can mẫu (sample / 표본)/mô hình (model / 모델) đầu vào (input / 입력) conditional on lớp (class / 클래스); discriminative focuses quyết định (decision / 결정) ranh giới (boundary / 경계).

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Latent variables** tiếp nhận điểm tựa từ **Generative vs discriminative modeling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Marginalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Latent variables

A latent variable `Z` is not directly observed but helps explain observed dữ liệu (data / 데이터) `X`.

\[
P(X)=\sum_z P(X,Z)
\]

or continuous integral.

Examples:

- hidden topic causing word phân phối (distribution / 분포);
- hidden disease causing symptoms;
- hidden trạng thái (state / 상태) causing sensor observations.

Latent variables compress explanatory cấu trúc (structure / 구조) but introduce suy luận (inference / 추론) challenge.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Marginalization** tiếp nhận điểm tựa từ **Latent variables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conditioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Marginalization

To reason about observed variables while hidden variable unknown:

\[
P(X)=\sum_z P(X,Z)
\]

This “sum over possibilities” can be computationally expensive when many hidden variables.

Probabilistic suy luận (inference / 추론) độ phức tạp (complexity / 복잡도) often comes from exponential number joint assignments.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Conditioning** tiếp nhận điểm tựa từ **Marginalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Explaining away** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conditioning

When observe bằng chứng (evidence / 증거) `E=e`, posterior restricts/renormalizes phân phối (distribution / 분포):

\[
P(X\mid E=e)
\]

In graphical các mô hình (models / 모델들), bằng chứng (evidence / 증거) can propagate belief through mạng (network / 네트워크).

Observation can make previously independent variables dependent — phenomenon called **explaining away**.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Explaining away** tiếp nhận điểm tựa từ **Conditioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Conditional independence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Explaining away

Suppose burglary `B` and earthquake `E` can both cause alarm `A`:

```text
B → A ← E
```

Before observing alarm, B and E may be independent.

After observe `A=true`, học tập (learning / 학습) `B=true` reduces need to believe earthquake caused alarm, so B and E become dependent conditioned on A.

Collider cấu trúc (structure / 구조) is central in probabilistic/nhân quả (causal / 인과적) graphs.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Conditional independence** tiếp nhận điểm tựa từ **Explaining away** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Factorization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Conditional independence

Notation:

\[
X\perp Y\mid Z
\]

means X and Y independent when conditioned on Z.

Graphical các mô hình (models / 모델들) encode many conditional independence relations compactly, allowing factorization of huge joint phân phối (distribution / 분포).

Without factorization, joint bảng (table / 테이블) over `n` nhị phân (binary / 이진) variables requires:

\[
2^n
\]

entries.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Factorization** tiếp nhận điểm tựa từ **Conditional independence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chính xác (exact / 정확한) suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Factorization

Instead of full joint:

\[
P(X_1,...,X_n)
\]

use sản phẩm (product / 제품) cục bộ (local / 로컬) factors:

\[
\prod_i \phi_i(X_{S_i})
\]

Bayesian mạng (network / 네트워크) factors conditional distributions; Markov Random trường dữ liệu (field / 필드) uses undirected potentials.

Factorization is the probabilistic equivalent of exploiting cấu trúc (structure / 구조) instead of brute force enumeration.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Chính xác (exact / 정확한) suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Factorization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Variable elimination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chính xác (exact / 정확한) suy luận (inference / 추론)

Chính xác (exact / 정확한) methods compute posterior exactly under mô hình (model / 모델):

- variable elimination;
- belief propagation on trees/polytrees;
- junction cây (tree / 트리).

Độ phức tạp (complexity / 복잡도) depends đồ thị (graph / 그래프) cấu trúc (structure / 구조)/treewidth, not just number variables.

Dense dependencies can make chính xác (exact / 정확한) suy luận (inference / 추론) exponential.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Variable elimination** tiếp nhận điểm tựa từ **Chính xác (exact / 정확한) suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Approximate suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variable elimination

Suppose want:

\[
P(A\mid E=e)
\]

We multiply relevant factors and sum hidden variables in chosen thứ tự (order / 순서).

Elimination thứ tự (order / 순서) strongly affects kích thước (size / 크기) of intermediate factors.

This resembles cơ sở dữ liệu (database / 데이터베이스) join-order tối ưu hóa (optimization / 최적화): mathematically same kết quả (result / 결과), computational chi phí (cost / 비용) can vary dramatically.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Approximate suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Variable elimination** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Monte Carlo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Approximate suy luận (inference / 추론)

When chính xác (exact / 정확한) suy luận (inference / 추론) too expensive, use approximation:

- Monte Carlo sampling;
- importance sampling;
- MCMC;
- variational suy luận (inference / 추론);
- loopy belief propagation.

Approximation trades tính đúng đắn (correctness / 정확성) exactness for tractability.

Need monitor convergence/lỗi (error / 오류); “thuật toán (algorithm / 알고리즘) returned number” does not mean posterior accurate.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Monte Carlo** tiếp nhận điểm tựa từ **Approximate suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Importance sampling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Monte Carlo

Mẫu (sample / 표본) hidden configurations:

\[
z^{(1)},...,z^{(N)}\sim P
\]

estimate expectation:

\[
\mathbb{E}[f(Z)]\approx\frac1N\sum_i f(z^{(i)})
\]

Lỗi (error / 오류) typically shrinks around `O(1/√N)` under tiêu chuẩn (standard / 표준) independent sampling, making high precision expensive.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Importance sampling** tiếp nhận điểm tựa từ **Monte Carlo** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Markov chuỗi (chain / 사슬) Monte Carlo** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Importance sampling

If mục tiêu (target / 대상) phân phối (distribution / 분포) hard mẫu (sample / 표본) but proposal `q` easy:

\[
\mathbb{E}_p[f(X)]
=
\mathbb{E}_q\left[f(X)\frac{p(X)}{q(X)}\right]
\]

Importance weights explode if `q` poorly covers regions where `p` has mass, causing high variance.

This theme appears again in off-policy RL.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Importance sampling** xác định đầu vào; **Markov chuỗi (chain / 사슬) Monte Carlo** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Variational suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Markov chuỗi (chain / 사슬) Monte Carlo

MCMC constructs Markov chuỗi (chain / 사슬) whose stationary phân phối (distribution / 분포) is mục tiêu (target / 대상).

Methods include Metropolis–Hastings, Gibbs Sampling.

Samples correlated; burn-in/mixing/convergence diagnostic matter.

High-dimensional multimodal distributions can mix slowly.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Markov chuỗi (chain / 사슬) Monte Carlo** xác định đầu vào; **Variational suy luận (inference / 추론)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Maximum likelihood and Bayesian suy luận (inference / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variational suy luận (inference / 추론)

Choose tractable phân phối (distribution / 분포) family `q_φ(z)` approximate posterior `p(z|x)` by tối ưu hóa (optimization / 최적화).

Often minimize:

\[
D_{KL}(q_\phi(z)\|p(z\mid x))
\]

Equivalent maximize ELBO:

\[
\log p(x)\ge
\mathbb{E}_{q}[\log p(x,z)-\log q(z)]
\]

Variational suy luận (inference / 추론) turns suy luận (inference / 추론) into tối ưu hóa (optimization / 최적화), usually faster but introduces approximation độ lệch (bias / 편향).

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Maximum likelihood and Bayesian suy luận (inference / 추론)** tiếp nhận điểm tựa từ **Variational suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Predictive phân phối (distribution / 분포)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Maximum likelihood and Bayesian suy luận (inference / 추론)

MLE chooses điểm (point / 지점) estimate:

\[
\theta_{MLE}=\arg\max_\theta P(D\mid\theta)
\]

Bayesian suy luận (inference / 추론) keeps posterior phân phối (distribution / 분포):

\[
P(\theta\mid D)
\]

Full posterior expresses parameter bất định (uncertainty / 불확실성) but is often computationally expensive in neural networks.

Approximate Bayesian deep học tập (learning / 학습) uses ensembles, variational methods or other bất định (uncertainty / 불확실성) approximations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Predictive phân phối (distribution / 분포)** tiếp nhận điểm tựa từ **Maximum likelihood and Bayesian suy luận (inference / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Calibration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Predictive phân phối (distribution / 분포)

Bayesian prediction integrates parameters:

\[
P(y\mid x,D)=\int P(y\mid x,\theta)P(\theta\mid D)d\theta
\]

Rather than lần ghi nhận (commit / 커밋) to one `θ`, average predictions weighted by posterior plausibility.

Deep ensembles approximate mô hình (model / 모델) bất định (uncertainty / 불확실성) differently by huấn luyện (training / 학습) multiple các mô hình (models / 모델들).

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Calibration** tiếp nhận điểm tựa từ **Predictive phân phối (distribution / 분포)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bằng chứng (evidence / 증거) and likelihood are model-dependent** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Calibration

Probabilistic reasoner should not only rank correctly but probabilities should match empirical frequencies when interpretation requires.

Calibration can degrade under phân phối (distribution / 분포) shift.

A mô hình (model / 모델) calibrated on US customers may be miscalibrated on Korean customers if conditional relationships differ.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Calibration** nêu điều cần giải thích; **Bằng chứng (evidence / 증거) and likelihood are model-dependent** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Prior sensitivity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bằng chứng (evidence / 증거) and likelihood are model-dependent

Posterior is only as good as likelihood/prior các giả định (assumptions / 가정들).

Bayes theorem itself is mathematically chính xác (exact / 정확한), but wrong mô hình (model / 모델) gives wrong posterior.

This mirrors formal lô-gic (logic / 논리): valid suy luận (inference / 추론) from false premises is still formal-valid but real-world wrong.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Bằng chứng (evidence / 증거) and likelihood are model-dependent** nêu điều cần giải thích; **Prior sensitivity** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Bayesian quyết định (decision / 결정) lý thuyết (theory / 이론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prior sensitivity

With little dữ liệu (data / 데이터), prior strongly influences posterior. With abundant informative dữ liệu (data / 데이터), likelihood often dominates under regular conditions.

In high-dimensional các mô hình (models / 모델들), “uninformative prior” is not simple; parameterization matters.

Prior encodes inductive độ lệch (bias / 편향), not something to hide.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Bayesian quyết định (decision / 결정) lý thuyết (theory / 이론)** tiếp nhận điểm tựa từ **Prior sensitivity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Probabilistic graphical các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bayesian quyết định (decision / 결정) lý thuyết (theory / 이론)

Posterior alone not hành động (action / 동작). Choose hành động (action / 동작) minimize posterior expected mất mát (loss / 손실):

\[
a^*=\arg\min_a\mathbb{E}_{\theta\mid D}[L(a,\theta)]
\]

This connects probabilistic suy luận (inference / 추론) to [Decision Making Under Uncertainty](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md).

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Probabilistic graphical các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Bayesian quyết định (decision / 결정) lý thuyết (theory / 이론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **HMM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Probabilistic graphical các mô hình (models / 모델들)

Two major forms:

**Bayesian mạng (network / 네트워크)** — directed acyclic đồ thị (graph / 그래프); cục bộ (local / 로컬) conditional probabilities.

**Markov Random trường dữ liệu (field / 필드)** — undirected đồ thị (graph / 그래프); potentials/factors.

Factor đồ thị (graph / 그래프) explicitly separates variable and factor nodes.

These representations expose conditional cấu trúc (structure / 구조) for suy luận (inference / 추론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **HMM** tiếp nhận điểm tựa từ **Probabilistic graphical các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Kalman Filter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## HMM

Hidden Markov mô hình (model / 모델) has latent trạng thái (state / 상태) chuỗi (sequence / 시퀀스):

```text
Z1 → Z2 → Z3 → ...
↓    ↓    ↓
X1   X2   X3
```

Các giả định (assumptions / 가정들):

\[
P(Z_t\mid Z_{<t})=P(Z_t\mid Z_{t-1})
\]

and observations conditionally dependent on trạng thái hiện tại (current state / 현재 상태).

Algorithms:

- Forward thuật toán (algorithm / 알고리즘) → likelihood/filtering;
- Viterbi → most likely trạng thái (state / 상태) chuỗi (sequence / 시퀀스);
- Forward–Backward → posterior marginals.

HMM historically central in speech/NLP before Deep học tập (learning / 학습).

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Kalman Filter** tiếp nhận điểm tựa từ **HMM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Probabilistic programming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Kalman Filter

Linear-Gaussian state-space mô hình (model / 모델) permits chính xác (exact / 정확한) recursive Bayesian filtering with Gaussian beliefs.

It predicts next trạng thái (state / 상태) then corrects using observation.

Kalman gain balances mô hình (model / 모델) bất định (uncertainty / 불확실성) and đo lường (measurement / 측정) bất định (uncertainty / 불확실성).

This is probabilistic lập luận (reasoning / 추론) deployed in điều hướng (navigation / 내비게이션)/tracking/điều khiển (control / 제어).

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Probabilistic programming** tiếp nhận điểm tựa từ **Kalman Filter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bất định (uncertainty / 불확실성) in LLMs** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Probabilistic programming

Languages like Stan, PyMC-like ecosystems let người dùng (user / 사용자) specify generative mô hình (model / 모델) and perform suy luận (inference / 추론) via MCMC/VI.

This separates mô hình (model / 모델) specification from bộ máy suy luận (inference engine / 추론 엔진) similarly to declarative lô-gic (logic / 논리).

But suy luận (inference / 추론) chất lượng (quality / 품질)/computation still depend mô hình (model / 모델) hình học (geometry / 기하학) and thuật toán (algorithm / 알고리즘).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Bất định (uncertainty / 불확실성) in LLMs** tiếp nhận điểm tựa từ **Probabilistic programming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Self-reported confidence** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất định (uncertainty / 불확실성) in LLMs

LLM next-token probabilities are conditional chuỗi (sequence / 시퀀스) probabilities, not directly “truth probabilities”.

A đơn vị từ (token / 토큰) can have high xác suất (probability / 확률) because it is linguistically likely despite claim being false.

Therefore:

```text
P(token | context)
≠
P(statement is true | world evidence)
```

This distinction is fundamental to hallucination/grounding.

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Self-reported confidence** tiếp nhận điểm tựa từ **Bất định (uncertainty / 불확실성) in LLMs** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Probabilistic RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Self-reported confidence

Asking LLM “How confident are you?” produces văn bản (text / 텍스트) generated from same mô hình (model / 모델), not automatically calibrated posterior about tính đúng đắn (correctness / 정확성).

Confidence estimation requires tường minh (explicit / 명시적) evaluation/calibration methods, ensembles, consistency signals, bên ngoài (external / 외부) xác minh (verification / 확인) or task-specific các mô hình (models / 모델들).

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Probabilistic RAG** tiếp nhận điểm tựa từ **Self-reported confidence** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Probabilistic RAG

Retrieval introduces bất định (uncertainty / 불확실성):

```text
query intent uncertain
retriever ranking uncertain
document truth/freshness uncertain
LLM interpretation uncertain
```

Reliable RAG should treat retrieval score as ranking tín hiệu (signal / 신호), not guaranteed relevance/truth.

Reranking, citations and nguồn (source / 소스) kiểm tra hợp lệ (validation / 검증) reduce bất định (uncertainty / 불확실성) at different stages.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Probabilistic RAG** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Logic         → what must follow if premises true
Probability   → how belief is distributed under uncertainty
Bayes         → update belief with evidence
Factorization → exploit conditional structure
Inference     → compute posterior/marginals/expectations
Approximation → trade exactness for tractability
Decision      → combine posterior with utility/cost
```

> **Chuyển mạch:** Trong **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Bayesian means probabilities are always correct”

Posterior depends mô hình (model / 모델), prior, likelihood and dữ liệu (data / 데이터) chất lượng (quality / 품질).

### “LLM xác suất (probability / 확률) = factual confidence”

Next-token likelihood is not calibrated truth xác suất (probability / 확률).

### “chính xác (exact / 정확한) suy luận (inference / 추론) is always preferable”

Chính xác (exact / 정확한) may be infeasible; approximate suy luận (inference / 추론) can be only practical option.

### “Conditional independence means variables unrelated”

They can be dependent marginally but independent given a third variable.

> **Chuyển mạch:** Ở chặng này của **Probabilistic lập luận (reasoning / 추론) trong Artificial Intelligence**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Probabilistic Reasoning bridges Probability, Knowledge Representation and Decision Theory. [Bayesian Networks](./05_bayesian_networks.md) will make the conditional-dependency structure concrete, while later Machine Learning chapters will show how models estimate these distributions from data.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
