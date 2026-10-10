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

Probability không chỉ nói “chưa biết” mà mô tả phân phối belief về các khả năng. Bayesian updating biến evidence mới thành thay đổi có định lượng trong belief đó.

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

Bayesian update dễ thấy hơn ở odds: posterior odds bằng prior odds nhân likelihood ratio. Dạng này làm rõ evidence đã đẩy niềm tin về một hypothesis theo hướng nào.

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

Odds chỉ diễn tả mức tin tương đối; prior/base rate quyết định điểm xuất phát. Bỏ qua base rate có thể khiến likelihood mạnh nhưng hiếm bị diễn giải quá mức.

## Cơ sở (base / 기반) tỷ lệ (rate / 비율) matters

Rare-event detection often suffers base-rate neglect.

Even high sensitivity/specificity may yield low posterior positive xác suất (probability / 확률) when prevalence very low.

Fraud, anomaly detection and bảo mật (security / 보안) alerts require careful cơ sở (base / 기반) rates; otherwise false positives dominate.

Base rate là một phần của prior, còn nhiều bằng chứng cần được kết hợp theo cấu trúc phụ thuộc của chúng. Nếu đếm cùng một tín hiệu nhiều lần, posterior sẽ bị tự tin giả.

## Multiple bằng chứng (evidence / 증거)

If bằng chứng (evidence / 증거) `E1,E2` conditionally independent given H:

\[
P(E_1,E_2\mid H)=P(E_1\mid H)P(E_2\mid H)
\]

Then likelihoods multiply.

But naive independence các giả định (assumptions / 가정들) can double-count correlated bằng chứng (evidence / 증거).

Example two fraud signals derived from same IP reputation nguồn (source / 소스) are not independent just because represented as separate features.

Multiple evidence cần likelihood joint hoặc điều kiện độc lập được biện minh. Naive Bayes biến giả định độc lập thành một mô hình đơn giản, nhanh và dễ kiểm tra.

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

Naive Bayes tối ưu posterior theo một generative factorization cụ thể. So sánh generative và discriminative modeling giúp thấy khi nào cần mô hình hóa dữ liệu đầu vào, khi nào chỉ cần ranh giới dự đoán.

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

Generative model có thể suy ra cấu trúc sinh dữ liệu, nhưng nhiều nguyên nhân không quan sát trực tiếp. Latent variables cho phép biểu diễn các yếu tố ẩn và truyền uncertainty của chúng vào inference.

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

Latent variables thường không cần được quyết định thành một giá trị duy nhất. Marginalization cộng xác suất trên các trạng thái ẩn để giữ lại uncertainty thay vì chọn một giả thuyết sớm.

## Marginalization

To reason about observed variables while hidden variable unknown:

\[
P(X)=\sum_z P(X,Z)
\]

This “sum over possibilities” can be computationally expensive when many hidden variables.

Probabilistic suy luận (inference / 추론) độ phức tạp (complexity / 복잡도) often comes from exponential number joint assignments.

Marginalization loại bỏ biến bằng cách cộng hoặc tích phân, còn conditioning cập nhật phân phối khi đã biết evidence. Hai phép toán này là nền tảng để tách prior, likelihood và posterior.

## Conditioning

When observe bằng chứng (evidence / 증거) `E=e`, posterior restricts/renormalizes phân phối (distribution / 분포):

\[
P(X\mid E=e)
\]

In graphical các mô hình (models / 모델들), bằng chứng (evidence / 증거) can propagate belief through mạng (network / 네트워크).

Observation can make previously independent variables dependent — phenomenon called **explaining away**.

Conditioning có thể tạo explaining away: khi đã biết một nguyên nhân của effect, bằng chứng về nguyên nhân khác có thể giảm. Hiện tượng này chỉ đúng khi cấu trúc phụ thuộc trong model cho phép.

## Explaining away

Suppose burglary `B` and earthquake `E` can both cause alarm `A`:

```text
B → A ← E
```

Before observing alarm, B and E may be independent.

After observe `A=true`, học tập (learning / 학습) `B=true` reduces need to believe earthquake caused alarm, so B and E become dependent conditioned on A.

Collider cấu trúc (structure / 구조) is central in probabilistic/nhân quả (causal / 인과적) graphs.

Explaining away cho thấy phụ thuộc có điều kiện không giống độc lập biên. Ghi rõ conditional independence giúp biết biến nào có thể bỏ khỏi phép tính mà không đổi semantics.

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

Conditional independence cho phép factorization joint distribution thành các factor nhỏ hơn. Factorization là cây cầu từ semantics xác suất sang thuật toán inference có thể chạy được.

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

Factorization làm giảm kích thước biểu thức nhưng không bảo đảm mọi query đều rẻ. Exact inference vẫn phải xem graph structure và treewidth trước khi chọn thuật toán.

## Chính xác (exact / 정확한) suy luận (inference / 추론)

Chính xác (exact / 정확한) methods compute posterior exactly under mô hình (model / 모델):

- variable elimination;
- belief propagation on trees/polytrees;
- junction cây (tree / 트리).

Độ phức tạp (complexity / 복잡도) depends đồ thị (graph / 그래프) cấu trúc (structure / 구조)/treewidth, not just number variables.

Dense dependencies can make chính xác (exact / 정확한) suy luận (inference / 추론) exponential.

Exact inference khai thác cấu trúc nhân tử để trả lời đúng, nhưng variable elimination có thể kiểm soát thứ tự loại biến nhằm giảm intermediate factor.

## Variable elimination

Suppose want:

\[
P(A\mid E=e)
\]

We multiply relevant factors and sum hidden variables in chosen thứ tự (order / 순서).

Elimination thứ tự (order / 순서) strongly affects kích thước (size / 크기) of intermediate factors.

This resembles cơ sở dữ liệu (database / 데이터베이스) join-order tối ưu hóa (optimization / 최적화): mathematically same kết quả (result / 결과), computational chi phí (cost / 비용) can vary dramatically.

Variable elimination cho kết quả chính xác khi còn khả thi; với graph lớn hoặc liên tục, approximate inference đổi guarantee lấy chi phí và thời gian có giới hạn.

## Approximate suy luận (inference / 추론)

When chính xác (exact / 정확한) suy luận (inference / 추론) too expensive, use approximation:

- Monte Carlo sampling;
- importance sampling;
- MCMC;
- variational suy luận (inference / 추론);
- loopy belief propagation.

Approximation trades tính đúng đắn (correctness / 정확성) exactness for tractability.

Need monitor convergence/lỗi (error / 오류); “thuật toán (algorithm / 알고리즘) returned number” does not mean posterior accurate.

Approximate inference mở ra nhiều họ phương pháp; Monte Carlo dùng samples để xấp xỉ kỳ vọng hoặc phân phối mà không cần giải toàn bộ biểu thức symbolically.

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

Monte Carlo hội tụ theo số sample nhưng sample từ proposal không phù hợp sẽ lãng phí. Importance sampling reweight sample để ước lượng target từ một distribution dễ lấy mẫu hơn.

## Importance sampling

If mục tiêu (target / 대상) phân phối (distribution / 분포) hard mẫu (sample / 표본) but proposal `q` easy:

\[
\mathbb{E}_p[f(X)]
=
\mathbb{E}_q\left[f(X)\frac{p(X)}{q(X)}\right]
\]

Importance weights explode if `q` poorly covers regions where `p` has mass, causing high variance.

This theme appears again in off-policy RL.

Importance sampling nhạy với trọng số cực lớn khi proposal bỏ sót vùng quan trọng. Markov chain Monte Carlo thay cách lấy mẫu độc lập bằng chain có stationary distribution là target.

## Markov chuỗi (chain / 사슬) Monte Carlo

MCMC constructs Markov chuỗi (chain / 사슬) whose stationary phân phối (distribution / 분포) is mục tiêu (target / 대상).

Methods include Metropolis–Hastings, Gibbs Sampling.

Samples correlated; burn-in/mixing/convergence diagnostic matter.

High-dimensional multimodal distributions can mix slowly.

MCMC không cần proposal bao phủ hoàn hảo nhưng phải kiểm tra mixing, burn-in và autocorrelation. Variational inference tiếp cận khác: tối ưu một họ phân phối đơn giản để gần posterior.

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

Variational inference thường nhanh và có objective rõ, nhưng approximation family có thể bỏ sót uncertainty. So sánh với maximum likelihood và Bayesian inference giúp tách point estimate khỏi posterior.

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

Maximum likelihood chọn tham số làm dữ liệu quan sát có khả năng nhất, còn Bayesian inference giữ prior và posterior trên tham số. Predictive distribution tích hợp bất định đó khi dự đoán dữ liệu mới.

## Predictive phân phối (distribution / 분포)

Bayesian prediction integrates parameters:

\[
P(y\mid x,D)=\int P(y\mid x,\theta)P(\theta\mid D)d\theta
\]

Rather than lần ghi nhận (commit / 커밋) to one `θ`, average predictions weighted by posterior plausibility.

Deep ensembles approximate mô hình (model / 모델) bất định (uncertainty / 불확실성) differently by huấn luyện (training / 학습) multiple các mô hình (models / 모델들).

Predictive distribution trả lời không chỉ “giá trị nào có khả năng nhất” mà còn “độ tin cậy phân bố ra sao”. Calibration kiểm tra liệu xác suất dự báo có khớp tần suất thực tế hay không.

## Calibration

Probabilistic reasoner should not only rank correctly but probabilities should match empirical frequencies when interpretation requires.

Calibration can degrade under phân phối (distribution / 분포) shift.

A mô hình (model / 모델) calibrated on US customers may be miscalibrated on Korean customers if conditional relationships differ.

Calibration phụ thuộc vào target và dữ liệu đánh giá; likelihood hay evidence không tự có nghĩa nếu model và sample space chưa rõ. Vì thế evidence luôn phải được đọc cùng với assumptions của model.

## Bằng chứng (evidence / 증거) and likelihood are model-dependent

Posterior is only as good as likelihood/prior các giả định (assumptions / 가정들).

Bayes theorem itself is mathematically chính xác (exact / 정확한), but wrong mô hình (model / 모델) gives wrong posterior.

This mirrors formal lô-gic (logic / 논리): valid suy luận (inference / 추론) from false premises is still formal-valid but real-world wrong.

Evidence model-dependent làm prior trở thành một phần minh bạch của posterior, không phải chi tiết có thể giấu. Prior sensitivity kiểm tra kết luận thay đổi bao nhiêu khi lựa chọn prior hợp lý thay đổi.

## Prior sensitivity

With little dữ liệu (data / 데이터), prior strongly influences posterior. With abundant informative dữ liệu (data / 데이터), likelihood often dominates under regular conditions.

In high-dimensional các mô hình (models / 모델들), “uninformative prior” is not simple; parameterization matters.

Prior encodes inductive độ lệch (bias / 편향), not something to hide.

Prior sensitivity tells us whether posterior conclusions are robust enough to support action. Bayesian decision theory adds utility and loss so uncertainty can be turned into a decision boundary.

## Bayesian quyết định (decision / 결정) lý thuyết (theory / 이론)

Posterior alone not hành động (action / 동작). Choose hành động (action / 동작) minimize posterior expected mất mát (loss / 손실):

\[
a^*=\arg\min_a\mathbb{E}_{\theta\mid D}[L(a,\theta)]
\]

This connects probabilistic suy luận (inference / 추론) to [Decision Making Under Uncertainty](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md).

Bayesian decision theory separates belief about outcomes from the cost of actions. Probabilistic graphical models provide a compact structure for representing the dependencies needed to compute those beliefs.

## Probabilistic graphical các mô hình (models / 모델들)

Two major forms:

**Bayesian mạng (network / 네트워크)** — directed acyclic đồ thị (graph / 그래프); cục bộ (local / 로컬) conditional probabilities.

**Markov Random trường dữ liệu (field / 필드)** — undirected đồ thị (graph / 그래프); potentials/factors.

Factor đồ thị (graph / 그래프) explicitly separates variable and factor nodes.

These representations expose conditional cấu trúc (structure / 구조) for suy luận (inference / 추론).

Graphical models express nodes and conditional dependencies; HMM specializes them to a latent state sequence with observations over time. Kalman Filter is the linear-Gaussian continuous-state case of that broader family.

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

HMM and Kalman Filter both separate hidden state from observation, but their assumptions differ: discrete states versus linear-Gaussian dynamics. Probabilistic programming lets users express such models and delegate inference.

## Kalman Filter

Linear-Gaussian state-space mô hình (model / 모델) permits chính xác (exact / 정확한) recursive Bayesian filtering with Gaussian beliefs.

It predicts next trạng thái (state / 상태) then corrects using observation.

Kalman gain balances mô hình (model / 모델) bất định (uncertainty / 불확실성) and đo lường (measurement / 측정) bất định (uncertainty / 불확실성).

This is probabilistic lập luận (reasoning / 추론) deployed in điều hướng (navigation / 내비게이션)/tracking/điều khiển (control / 제어).

Probabilistic programming makes model structure explicit while hiding much of the inference plumbing. Its guarantees still depend on the chosen model, which matters when representing uncertainty in LLM outputs.

## Probabilistic programming

Languages like Stan, PyMC-like ecosystems let người dùng (user / 사용자) specify generative mô hình (model / 모델) and perform suy luận (inference / 추론) via MCMC/VI.

This separates mô hình (model / 모델) specification from bộ máy suy luận (inference engine / 추론 엔진) similarly to declarative lô-gic (logic / 논리).

But suy luận (inference / 추론) chất lượng (quality / 품질)/computation still depend mô hình (model / 모델) hình học (geometry / 기하학) and thuật toán (algorithm / 알고리즘).

LLM uncertainty is not only sampling randomness; it can reflect missing knowledge, distribution shift or ambiguity in the prompt. Self-reported confidence must therefore be tested against outcomes rather than accepted as calibrated probability.

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

A model’s verbal confidence is a claim about its own reliability, not automatically a posterior probability. Probabilistic RAG can ground generation with retrieved evidence and expose uncertainty over sources and answers.

## Self-reported confidence

Asking LLM “How confident are you?” produces văn bản (text / 텍스트) generated from same mô hình (model / 모델), not automatically calibrated posterior about tính đúng đắn (correctness / 정확성).

Confidence estimation requires tường minh (explicit / 명시적) evaluation/calibration methods, ensembles, consistency signals, bên ngoài (external / 외부) xác minh (verification / 확인) or task-specific các mô hình (models / 모델들).

Probabilistic RAG should propagate retrieval scores, source quality and answer uncertainty instead of presenting one deterministic citation. Mental model cuối chương gom belief, evidence, calibration và action boundary.

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

Mental model hữu ích là đi từ prior và evidence qua posterior, calibration đến quyết định có utility rõ. Chuỗi này giúp nhận ra các misconception về xác suất và tránh overconfidence.

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

Những misconception phổ biến gồm nhầm probability với confidence, coi calibration là accuracy, hoặc bỏ qua base rate và model dependence. Sửa chúng giúp nối probabilistic reasoning với các phần AI kế tiếp.

## Dùng chung (common / 공통) Misconceptions

### “Bayesian means probabilities are always correct”

Posterior depends mô hình (model / 모델), prior, likelihood and dữ liệu (data / 데이터) chất lượng (quality / 품질).

### “LLM xác suất (probability / 확률) = factual confidence”

Next-token likelihood is not calibrated truth xác suất (probability / 확률).

### “chính xác (exact / 정확한) suy luận (inference / 추론) is always preferable”

Chính xác (exact / 정확한) may be infeasible; approximate suy luận (inference / 추론) can be only practical option.

### “Conditional independence means variables unrelated”

They can be dependent marginally but independent given a third variable.

Probabilistic reasoning nối Bayesian inference, graphical models, calibration và RAG thành một workflow: biểu diễn uncertainty, cập nhật bằng evidence, kiểm tra dự báo rồi quyết định trong ranh giới an toàn.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Probabilistic Reasoning bridges Probability, Knowledge Representation and Decision Theory. [Bayesian Networks](./05_bayesian_networks.md) will make the conditional-dependency structure concrete, while later Machine Learning chapters will show how models estimate these distributions from data.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
