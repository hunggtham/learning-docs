# Gradient Descent và Optimizers trong Deep Learning

Sau khi backpropagation tính gradient, optimizer quyết định **parameters sẽ thay đổi như thế nào**. Đây là distinction quan trọng: gradient chỉ là local information về slope; optimizer là policy sử dụng information đó qua time.

Deep Learning optimization khó vì objective non-convex, scale parameters lớn, gradients noisy do mini-batches và curvature khác nhau theo directions. Vì vậy simple Gradient Descent là nền để hiểu, nhưng practical training thường dùng SGD with momentum, Adam/AdamW và learning-rate schedules.

## Gradient Descent

Update cơ bản:

\[
\theta_{t+1}=\theta_t-\eta\nabla_\theta L(\theta_t)
\]

`η` là learning rate.

Gradient chỉ direction steepest increase under Euclidean norm locally; negative gradient giảm loss nhanh nhất cho infinitesimal step. Với finite step, learning rate quyết định update có còn useful hay overshoot.

## Full Batch, Stochastic và Mini-Batch

Full-batch gradient dùng toàn dataset:

\[
g=\frac1N\sum_i\nabla L_i
\]

accurate nhưng expensive.

Stochastic Gradient Descent theo nghĩa strict dùng một sample. Practical “SGD” thường dùng mini-batch:

\[
g_B=\frac1{|B|}\sum_{i\in B}\nabla L_i
\]

Mini-batch gradient là noisy estimator của full gradient. Noise không chỉ nuisance; nó có thể giúp exploration và implicit regularization.

## Learning Rate là hyperparameter critical

Quá nhỏ:

- training chậm;
- có thể stuck lâu ở flat regions.

Quá lớn:

- oscillation;
- divergence;
- NaN/Inf.

Learning rate thường quan trọng hơn nhiều optimizer-detail khác.

## Momentum

Momentum tích lũy direction qua steps:

\[
v_t=\beta v_{t-1}+g_t
\]

\[
\theta_{t+1}=\theta_t-\eta v_t
\]

Nó smooth noisy gradient và tăng tốc qua directions gradient consistently aligned, đồng thời giảm zig-zag trong ravine.

Có analogy physical momentum nhưng đây là mathematical state, không phải vật lý thật.

## Nesterov Momentum

Nesterov-style methods evaluate/look ahead theo momentum direction rồi correct. Ý tưởng là anticipate future position để update responsive hơn.

Implementation conventions khác nhau giữa frameworks; cần đọc exact formula nếu reproducibility quan trọng.

## AdaGrad

AdaGrad scale learning rate per parameter bằng accumulated squared gradients:

\[
s_t=s_{t-1}+g_t^2
\]

\[
\theta_{t+1}=\theta_t-\eta\frac{g_t}{\sqrt{s_t}+\epsilon}
\]

Parameters hiếm update có effective learning rate lớn hơn, useful cho sparse features. Nhưng accumulator chỉ tăng nên learning rate có thể decay quá mạnh.

## RMSProp

RMSProp dùng exponential moving average:

\[
s_t=\beta s_{t-1}+(1-\beta)g_t^2
\]

rồi normalize gradient.

Điều này tránh AdaGrad accumulator grow forever.

## Adam

Adam kết hợp first-moment và second-moment estimates:

\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t
\]

\[
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
\]

Bias correction:

\[
\hat m_t=\frac{m_t}{1-\beta_1^t},\qquad
\hat v_t=\frac{v_t}{1-\beta_2^t}
\]

Update:

\[
\theta_{t+1}=\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\epsilon}
\]

Adam adapts per-parameter step scale và thường easy-to-use cho Transformers.

## AdamW và Weight Decay

L2 regularization và weight decay tương đương trong vanilla SGD dưới certain formulation, nhưng không hoàn toàn equivalent với adaptive optimizers.

**AdamW** decouples weight decay from gradient-based adaptive update:

\[
\theta\leftarrow(1-\eta\lambda)\theta-\eta\cdot AdamUpdate
\]

Đây là reason AdamW trở thành default phổ biến cho Transformer training/fine-tuning.

## Learning-Rate Schedules

Constant LR hiếm là best cho long training.

### Warmup

Bắt đầu LR nhỏ rồi tăng dần. Early training parameters/optimizer moments chưa stable; warmup giảm risk unstable updates, đặc biệt Transformers/large batch.

### Step / Exponential Decay

Giảm LR theo milestones hoặc exponential schedule.

### Cosine Decay

\[
\eta_t=\eta_{min}+\frac12(\eta_{max}-\eta_{min})
\left(1+\cos\frac{\pi t}{T}\right)
\]

smoothly giảm tới low LR.

### One-Cycle

LR tăng rồi giảm theo cycle, often combined momentum schedule.

Schedule là part của optimization algorithm, không decorative config.

## Weight Decay và parameters không decay

Modern training thường không apply weight decay cho mọi parameter như bias hoặc normalization scale. Exact parameter groups matter.

Fine-tuning recipe reproduce không được nếu chỉ ghi “AdamW lr=1e-4” mà bỏ weight-decay groups, warmup, batch size và schedule.

## Gradient Clipping

Global norm clipping:

\[
g\leftarrow g\cdot\min(1,c/\|g\|)
\]

phòng rare exploding update. RNN/Transformer training thường dùng.

Clipping không chữa root cause nếu gradient luôn explode; nó là safety mechanism.

## Batch Size và Learning Rate

Larger batch giảm gradient noise và tăng hardware utilization nhưng dùng memory nhiều. Effective optimization behavior đổi theo batch size.

Linear scaling rule (`lr ∝ batch`) là heuristic under regimes, không universal law.

**Gradient accumulation** mô phỏng larger effective batch bằng nhiều micro-batches trước optimizer step.

Nếu loss averaging/scaling sai, accumulated gradient magnitude cũng sai.

## Gradient Noise và Generalization

Small batches tạo noise có thể bias optimizer toward flatter/wider regions và đôi khi improve generalization. Nhưng theory complex; không nên biến thành rule “small batch luôn generalize tốt hơn”.

Hardware throughput và normalization also matter.

## Non-Convex Landscape

Deep network objective có saddle points, flat directions, symmetries và many equivalent minima.

Goal practical không phải tìm global minimum mathematically; ta cần solution low loss + good generalization under budget.

Parameter symmetries làm nhiều minima functionally equivalent.

## Sharpness và Flatness

Intuition: solution robust với small parameter perturbations có thể generalize better. Nhưng raw sharpness phụ thuộc parameterization/scale, nên interpretation cần cẩn thận.

Methods like SAM optimize neighborhood-aware objective, nhưng no single flatness metric explains generalization universally.

## Mixed Precision và Loss Scaling

FP16 gradients nhỏ có thể underflow. **Loss scaling** multiply loss trước backward:

\[
L'=sL
\]

compute gradients scaled, rồi divide before update. Dynamic loss scaling adjust `s` nếu overflow.

BF16 có exponent range lớn hơn nên less underflow-sensitive, dù precision mantissa thấp.

## Optimizer State Memory

Adam stores parameters + gradients + first moment + second moment, thường nhiều lần parameter memory. Với huge LLM, optimizer state cực lớn.

Distributed training dùng sharding (ZeRO/FSDP-style) để split states across devices.

Optimization vì vậy nối trực tiếp với infrastructure.

## Choosing Optimizer

Không có universal winner.

- SGD+momentum: strong in vision/classical deep nets, memory lower.
- AdamW: common Transformer/default fine-tuning.
- Adafactor/8-bit optimizer: reduce state memory in large models.
- Specialized optimizers có trade-offs khác.

Recipe phải evaluate cùng architecture/data/schedule.

## Mental Model

```text
Backprop = measure slope now
Optimizer = remember history + scale/update policy
Scheduler = change step policy over training time
```

## Common Misconceptions

### “Adam luôn hội tụ nhanh hơn nên tốt hơn SGD”

Convergence speed, final generalization và task differ. Không universal.

### “Learning rate càng nhỏ càng an toàn”

Quá nhỏ có thể training impractically slow hoặc converge poor under fixed budget.

### “Weight decay chỉ là L2 regularization đổi tên”

Với adaptive optimizer, decoupled weight decay khác naive L2 gradient penalty.

### “Optimizer tự xử lý exploding gradients”

Adaptive scaling không đảm bảo; clipping/architecture/normalization vẫn cần.

## Knowledge Connection

Xem [Optimization](../01_mathematical_foundations/06_optimization.md), [Backpropagation](./04_backpropagation.md), [Initialization and Normalization](./06_initialization_and_normalization.md) và [Training Dynamics](./09_deep_learning_training_dynamics.md).