# Optimization cho Artificial Intelligence

Optimization (최적화 / tối ưu hóa) là quá trình tìm giá trị của variables để một objective trở nên tốt hơn. Trong Machine Learning, architecture xác định class of functions model có thể biểu diễn, data cung cấp examples, loss function định nghĩa behavior nào được coi là tốt, còn optimizer tìm parameters phù hợp objective đó.

Một misconception phổ biến là “training = gradient descent”. Chính xác hơn, training là learning process rộng hơn; optimization là mechanism tìm parameters; gradient-based methods chỉ là một family algorithms. Hơn nữa, optimize rất tốt một objective sai vẫn có thể tạo system tệ. Vì vậy Optimization phải luôn được học cùng **objective design, constraints và evaluation**.

Xem trước: [Calculus for AI](./04_calculus_for_ai.md).

## Objective function

General optimization problem:

\[
\theta^*=\arg\min_\theta J(\theta)
\]

Trong supervised learning:

\[
J(\theta)=\frac{1}{n}\sum_{i=1}^{n}L(f_\theta(x_i),y_i)+\lambda\Omega(\theta)
\]

Term đầu đo fit với data. `Ω(θ)` regularize parameters hoặc behavior. `λ` kiểm soát trade-off.

Nếu maximize reward `R`, ta có thể equivalently minimize `-R`. `argmin` và `argmax` nói về location của optimum, không phải value minimum/maximum.

## Loss, objective và metric khác nhau

**Loss function (손실 함수)** thường là differentiable quantity optimizer minimize trên examples.

**Objective** có thể gồm loss + regularization + constraints/penalties.

**Evaluation metric** là quantity ta thực sự report hoặc care about, ví dụ accuracy, F1, revenue, safety violation rate.

Metric không nhất thiết differentiable. Ta có thể optimize cross-entropy nhưng evaluate accuracy.

Đây là idea của **surrogate loss**: optimize quantity tractable có relationship với target metric.

Nếu surrogate và real objective misaligned, training loss giảm nhưng product outcome có thể không tốt hơn.

## Constraint optimization

Không phải objective chỉ là minimize một scalar unconstrained.

Ví dụ:

\[
\min_\theta L(\theta)
\]

subject to:

\[
C(\theta)\le c
\]

Constraint có thể là latency, memory, fairness bound, energy budget hoặc risk limit.

Production AI thường là multi-objective/constraint problem:

```text
quality ↑
latency ↓
cost ↓
privacy risk ↓
safety violations ↓
```

Không có một model “best” độc lập context; có Pareto trade-offs.

## Convexity

Function `f` convex nếu line segment giữa hai points trên graph nằm trên/above graph theo convexity inequality:

\[
f(\lambda x+(1-\lambda)y)
\le
\lambda f(x)+(1-\lambda)f(y)
\]

với `0≤λ≤1`.

Convex optimization hấp dẫn vì local minimum cũng là global minimum dưới suitable conditions.

Linear regression với squared loss là convex theo parameters. Logistic regression với standard convex loss cũng convex.

Deep neural networks generally non-convex vì composition và parameter interactions tạo complex landscape.

## Local minima, saddle points và flat regions

Trong non-convex landscape, gradient bằng zero có thể là:

- local minimum;
- local maximum;
- saddle point;
- flat plateau.

High-dimensional neural networks có rất nhiều saddle/flat directions. Optimization behavior không nên được tưởng tượng chỉ như “quả bóng lăn xuống một cái bát”.

Landscape phụ thuộc parameterization và symmetries. Hai parameter sets khác nhau có thể represent same function.

## Gradient descent

Full-batch gradient descent:

\[
\theta_{t+1}=\theta_t-\eta\nabla J(\theta_t)
\]

`η` là learning rate.

Nếu `η` quá nhỏ, progress chậm. Nếu quá lớn, updates có thể overshoot hoặc diverge.

Một quadratic 1D:

\[
J(w)=\frac{1}{2}aw^2
\]

có gradient:

\[
J'(w)=aw
\]

update:

\[
w_{t+1}=(1-\eta a)w_t
\]

Từ đây thấy learning rate stability phụ thuộc curvature `a`. Một learning rate phù hợp direction flat có thể quá lớn ở direction steep.

## Stochastic Gradient Descent

Dataset lớn khiến compute full gradient expensive. SGD dùng one sample hoặc mini-batch:

\[
g_t=\frac{1}{B}\sum_{i\in\mathcal{B}_t}\nabla L_i(\theta_t)
\]

\[
\theta_{t+1}=\theta_t-\eta g_t
\]

`g_t` là noisy estimate của full gradient.

Noise không chỉ là drawback. Nó giảm compute/update, có thể giúp exploration landscape và tạo implicit regularization effects.

Modern “SGD” trong practice thường nghĩa mini-batch SGD, không phải exactly one sample.

## Batch size trade-off

Larger batch:

- gradient estimate ít noisy hơn;
- hardware utilization có thể tốt hơn;
- memory demand cao hơn;
- ít parameter updates trên mỗi epoch;
- generalization/training dynamics có thể đổi.

Small batch:

- noisy gradients hơn;
- nhiều updates hơn;
- memory nhẹ hơn;
- hardware throughput có thể kém nếu quá nhỏ.

Không có batch size universally optimal. Nó tương tác learning rate, optimizer, model, hardware và dataset scale.

## Momentum

Vanilla SGD dễ oscillate trong ravine có curvature khác nhau theo axes.

Momentum giữ velocity:

\[
v_t=\beta v_{t-1}+g_t
\]

\[
\theta_{t+1}=\theta_t-\eta v_t
\]

Mental model: gradients consistent qua nhiều steps accumulate, oscillation alternating directions partly cancel.

Momentum không phải physical momentum exact, nhưng analogy hữu ích vừa phải.

## Nesterov momentum

Nesterov-style method evaluates/look-ahead gradient relative to momentum-shifted point trong một formulation phổ biến. Nó có theoretical advantages trong convex settings và variants practical.

Framework implementations có conventions khác nhau, nên khi reproduce result cần check exact optimizer definition thay vì chỉ name.

## Adaptive learning rates

### AdaGrad

AdaGrad accumulate squared gradients:

\[
s_t=s_{t-1}+g_t^2
\]

và scale update:

\[
\theta\leftarrow\theta-\eta\frac{g_t}{\sqrt{s_t}+\epsilon}
\]

Parameters có historical large gradients nhận smaller effective learning rate.

Useful cho sparse features nhưng accumulated denominator chỉ tăng, có thể làm learning rate decay quá mạnh.

### RMSProp

RMSProp dùng exponential moving average:

\[
s_t=\beta s_{t-1}+(1-\beta)g_t^2
\]

tránh accumulation không giới hạn của AdaGrad.

### Adam

Adam combine first moment và second moment estimates:

\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
\]

\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
\]

Sau bias correction:

\[
\hat m_t=\frac{m_t}{1-\beta_1^t},\quad
\hat v_t=\frac{v_t}{1-\beta_2^t}
\]

update:

\[
\theta_{t+1}=
\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
\]

Adam phổ biến vì robust across many tasks, nhưng không automatically best mọi setting.

## AdamW và weight decay

L2 regularization và weight decay có equivalence trong simple SGD settings, nhưng với adaptive optimizer chúng không necessarily equivalent.

AdamW decouples weight decay khỏi gradient-based adaptive scaling:

\[
\theta\leftarrow (1-\eta\lambda)\theta-	ext{AdamUpdate}
\]

Đây là reason AdamW phổ biến trong Transformer training.

## Learning-rate schedule

Learning rate hiếm khi giữ constant từ đầu tới cuối large training.

Common patterns:

- warmup;
- step decay;
- exponential decay;
- cosine decay;
- one-cycle-like schedules.

**Warmup** tăng learning rate từ nhỏ lên target trong early steps. Với Transformer, early optimization có thể unstable khi moments/activations chưa settled.

Cosine schedule giảm smoothly:

\[
\eta_t=\eta_{min}+\frac{1}{2}(\eta_{max}-\eta_{min})
\left(1+\cos\frac{\pi t}{T}\right)
\]

Schedule là part của optimization algorithm, không phải cosmetic config.

## Weight initialization và optimization

Nếu weights quá lớn, activations/gradients có thể explode hoặc saturate. Quá nhỏ, signals có thể vanish.

Xavier/Glorot initialization cân variance theo fan-in/fan-out, useful với certain activations.

He/Kaiming initialization điều chỉnh cho ReLU-like activations.

Initialization không chỉ “random seed”; nó đặt starting geometry và signal scale cho optimization.

## Normalization và trainability

BatchNorm, LayerNorm và variants normalize activations theo different axes.

Ngoài regularization effects, normalization cải thiện optimization conditioning và signal scales.

Transformer thường dùng LayerNorm/RMSNorm-like mechanisms vì sequence/batch semantics khác CNN.

Normalization placement (`pre-norm` vs `post-norm`) ảnh hưởng gradient flow và deep Transformer stability.

## Conditioning

Optimization problem **ill-conditioned** khi curvature khác nhau rất mạnh theo directions.

Với quadratic Hessian eigenvalues từ `λ_min` tới `λ_max`, condition number:

\[
\kappa=\frac{\lambda_{max}}{\lambda_{min}}
\]

large `κ` khiến gradient descent zig-zag và require conservative learning rate.

Feature scaling, normalization, preconditioning và adaptive methods cố improve effective conditioning.

## Second-order methods

Newton update:

\[
\theta_{t+1}=\theta_t-H^{-1}\nabla J
\]

uses Hessian curvature.

Nếu objective locally quadratic, Newton can converge fast near optimum. Nhưng neural-network Hessian khổng lồ, storage/inversion impossible trực tiếp.

Quasi-Newton methods như BFGS/L-BFGS approximate curvature và useful ở smaller problems, nhưng large-scale stochastic Deep Learning chủ yếu dùng first-order methods.

## Gradient clipping

Global norm clipping:

\[
g\leftarrow g\cdot\min\left(1,\frac{c}{\|g\|}\right)
\]

nếu gradient norm vượt threshold `c`.

Clipping giúp prevent catastrophic huge update, đặc biệt sequence models. Nhưng nếu clipping xảy ra liên tục, có thể là symptom learning rate, normalization hoặc numerical instability khác.

## Regularization và optimization không hoàn toàn tách rời

L2 penalty thay objective.

Dropout thay stochastic training dynamics.

Early stopping dừng optimization trước khi fully fit training set.

Data augmentation thay empirical distribution optimizer sees.

Do đó generalization behavior là interaction giữa objective, data và optimization trajectory.

## Early stopping

Validation loss có thể bắt đầu tăng dù training loss tiếp tục giảm. Early stopping chọn checkpoint trước overfitting.

Đây là implicit regularization: ta giới hạn number of optimization steps.

Nhưng noisy validation metric có thể khiến stop quá sớm; practical systems dùng patience/smoothing/checkpoint strategy.

## Hyperparameters như outer optimization

Parameters `θ` được optimizer học từ training data. Hyperparameters `λ`, learning rate, architecture depth, batch size thường được chọn bằng validation process.

Có thể nhìn:

```text
inner loop: train θ
outer loop: choose hyperparameters h
```

Grid search, random search, Bayesian optimization và population-based methods là strategies cho outer problem.

Nếu tune quá nhiều trên một validation set, validation overfitting cũng xảy ra.

## Multi-objective optimization

Suppose system cần maximize quality `Q` và minimize latency `C`:

\[
\max Q(\theta),\quad \min C(\theta)
\]

Một scalarized objective:

\[
J=-Q+\lambda C
\]

encode trade-off qua `λ`, nhưng choice `λ` là value judgment/business requirement, không phải mathematics tự quyết định.

Pareto frontier chứa solutions không thể improve một objective mà không worsen objective khác.

AI deployment thường chọn point trên frontier theo product constraints.

## Constrained optimization và Lagrangian

Problem:

\[
\min_x f(x)\quad \text{s.t.}\quad g(x)\le0
\]

Lagrangian:

\[
\mathcal{L}(x,\lambda)=f(x)+\lambda g(x)
\]

với `λ≥0` trong inequality setting.

Lagrange multipliers có interpretation shadow price: cost marginal của constraint.

Idea này xuất hiện trong fairness constraints, resource allocation và Reinforcement Learning constrained objectives.

## Optimization trong Reinforcement Learning

RL tối ưu expected cumulative reward:

\[
J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]
\]

Gradient khó hơn supervised learning vì action sampling influence future states và reward.

Policy gradient theorem cho gradient estimator dựa trên log-policy:

\[
\nabla_\theta J
=\mathbb{E}[R\nabla_\theta\log\pi_\theta(a\mid s)]
\]

Noise/variance rất lớn, dẫn tới baselines, actor-critic và advanced optimization methods.

## Optimization trong LLM pretraining

LLM pretraining objective thường next-token cross-entropy trên huge token corpus.

Scale tạo challenges:

- distributed gradient aggregation;
- memory bandwidth;
- mixed precision;
- optimizer state memory;
- learning-rate schedule;
- gradient clipping;
- checkpointing;
- data ordering.

Optimization không chỉ là equation; nó là distributed systems problem ở large scale.

## Optimization trong alignment

Instruction tuning vẫn supervised optimization trên curated responses.

Preference optimization dùng human/model preference data. RLHF, PPO-style objectives, DPO-like methods encode different optimization formulations.

Quan trọng: optimizer không biết “helpful” hay “safe” theo human sense. Nó chỉ thấy mathematical objective constructed from data/rewards/preferences.

> An optimizer is powerful at finding what the objective rewards, not what the designer vaguely intended.

Connection này là core của specification gaming và alignment.

## Reward hacking / specification gaming

Nếu objective proxy không exactly match desired outcome, agent/model có thể exploit loophole.

Ví dụ simple agent rewarded “number of items picked” có thể repeatedly pick/drop same item nếu environment allows và reward definition không prevent.

Trong ML product, optimizing click-through rate alone có thể encourage sensational content dù long-term user satisfaction giảm.

Optimization amplifies metric design mistakes.

## No Free Lunch intuition

Không optimizer hoặc model universally best trên mọi possible problem. Performance dựa vào structural assumptions/inductive biases về class of tasks.

Adam mạnh trong nhiều Deep Learning tasks, nhưng không có theorem “Adam always best”. Hyperparameter defaults cũng là domain priors, không universal constants.

## Mental Model

```text
Model architecture → những functions nào có thể represent
Loss/objective      → behavior nào được rewarded
Gradient            → local direction signal
Optimizer           → rule biến signal thành parameter updates
Schedule            → update scale thay đổi theo thời gian
Regularization      → preference ngoài pure training fit
Constraints         → boundaries system không được vượt
Evaluation          → objective có thực sự map tới desired outcome không
```

## Common Misconceptions

### “Loss càng thấp thì model càng tốt”

Chỉ trên objective/dataset đang optimize. Generalization, calibration, safety và product metrics có thể khác.

### “Adam luôn tốt hơn SGD vì hiện đại hơn”

Optimizer choice phụ thuộc task, tuning và goal. SGD với momentum vẫn mạnh trong nhiều vision settings; Adam/AdamW phổ biến cho Transformers.

### “Global minimum luôn cần thiết”

Trong Deep Learning, solution có good generalization quan trọng hơn mathematical global minimum của training loss. Nhiều parameter solutions có near-zero loss.

### “Optimization tự tìm đúng behavior nếu model đủ mạnh”

Không. Optimizer faithfully follows provided signal; mis-specified objectives tạo misaligned behavior.

## Knowledge Connection

Optimization nối [Calculus](./04_calculus_for_ai.md) với Machine Learning training và nối trực tiếp tới AI Safety qua objective specification. Sau này SGD/AdamW sẽ quay lại trong Neural Networks; constrained and policy optimization quay lại trong Reinforcement Learning; preference objectives quay lại trong LLM Alignment.

Khi training fails, đừng chỉ đổi optimizer. Hãy kiểm tra objective, data scale, normalization, gradient statistics, learning-rate schedule, batch size, initialization và numerical precision như một coupled system.