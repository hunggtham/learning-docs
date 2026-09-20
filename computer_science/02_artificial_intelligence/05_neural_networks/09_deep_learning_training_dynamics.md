# Deep Learning Training Dynamics: hiểu quá trình model thực sự học

Training neural network không chỉ là lặp `forward → backward → optimizer.step()`. Một model có thể giảm loss nhưng học representation kém, diverge sau vài nghìn steps, overfit, collapse, hoặc đạt cùng final loss bằng trajectories rất khác nhau. **Training dynamics (학습 동역학 / động lực học huấn luyện)** nghiên cứu behavior của optimization process theo time.

Hiểu dynamics giúp debug system thay vì chỉ thử hyperparameters ngẫu nhiên.

## Training loop

Một loop cơ bản:

```text
for batch in data:
    prediction = model(batch.x)
    loss = objective(prediction, batch.y)
    gradients = backward(loss)
    optimizer.update(parameters, gradients)
```

Production training thêm:

```text
mixed precision
loss scaling
gradient accumulation
clipping
learning-rate schedule
logging
checkpointing
validation
distributed synchronization
```

Mỗi component có thể thay dynamics.

## Loss curve nói gì và không nói gì?

Training loss giảm nghĩa optimizer đang improve objective trên observed batches. Nó không đảm bảo:

- validation improve;
- calibration improve;
- robustness improve;
- representation semantically useful;
- deployment metric improve.

Validation curve và downstream slices vẫn cần.

Loss curve shape hữu ích:

- flat từ đầu → LR quá nhỏ, bad init, frozen params, data/label bug;
- explode → LR too high, numerical issue, bad normalization;
- oscillate mạnh → high LR/noisy batch;
- training ↓ validation ↑ → overfitting/shift;
- sudden spikes → bad batch, overflow, unstable optimizer state.

## Learning Rate Warmup

Early parameters random; LayerNorm/residual/optimizer moments chưa stable. Large LR ngay từ step 1 có thể destabilize.

Warmup increase LR gradually:

\[
\eta_t=\eta_{max}\frac{t}{T_{warmup}}
\]

sau đó decay.

Transformer training đặc biệt sensitive với warmup/batch/initialization interaction.

## Update-to-Weight Ratio

Không chỉ gradient norm; update magnitude so parameter magnitude hữu ích:

\[
ratio=\frac{\|\Delta\theta\|}{\|\theta\|}
\]

Ratio quá lớn có thể destroy learned structure; quá nhỏ model gần như không move.

Fine-tuning pretrained model thường cần update nhỏ hơn pretraining from scratch.

## Gradient Norm Tracking

Global/per-layer gradient norm cho biết signal distribution.

Nếu early layers norm ~0 còn late layers lớn → vanishing/blocked gradients.

Nếu một layer huge norm → instability/source scale issue.

Gradient clipping logs nên track fraction of steps clipped; nếu 90% steps bị clip, threshold/LR/root cause cần inspect.

## Activation Statistics

Theo dõi mean/std/max/zero fraction across layers.

Dying ReLU: zero fraction gần 100%.

Saturation sigmoid/tanh: activations near boundaries, gradients tiny.

Exploding activation: std tăng nhanh qua depth.

Norm layers mask một phần symptom nhưng không eliminate all instability.

## Data Order và Shuffling

SGD assumes batches representative enough. Nếu data sorted by label/time/domain, consecutive gradients biased và training oscillate/drift.

Shuffle improves IID approximation, nhưng time/online learning đôi khi intentionally preserves order.

Large distributed training cần deterministic sharding để avoid duplicate/missing samples.

## Curriculum Learning

Training examples theo easier→harder order có thể improve optimization trong some tasks. Nhưng defining difficulty đúng không trivial.

LLM instruction tuning sometimes mixes data sources/qualities with schedules. Data curriculum becomes optimization parameter.

## Sampling Distribution

Dataset composition quyết định gradient expectation.

Nếu source A 90% data, objective implicitly weights A mạnh. Reweight/resample sources changes what model learns even with same loss formula.

Large foundation-model training thường carefully design data mixture weights.

## Class Imbalance Dynamics

Rare class contributes few gradient updates. Model may learn majority behavior early and never recover well.

Class weighting, balanced sampling, focal loss hoặc two-stage approaches change gradient distribution.

Monitor per-class metrics, not just loss.

## Catastrophic Forgetting

Fine-tuning on narrow new data can overwrite capabilities from pretraining.

Mitigations:

- lower learning rate;
- mix old/general data;
- regularize toward base weights;
- adapters/LoRA;
- freeze layers;
- rehearsal methods.

This is a training-dynamics issue across sequential distributions.

## Fine-Tuning vs Feature Extraction

Frozen encoder + new head preserves pretrained representation but may underadapt.

Full fine-tuning gives flexibility but higher compute/forgetting/overfit risk.

Gradual unfreezing or layer-wise learning rates create middle ground.

## Layer-Wise Learning Rates

Earlier pretrained layers may need smaller updates, task head larger.

Discriminative LR:

```text
embedding / early layers → small LR
middle layers            → medium LR
new task head            → larger LR
```

Not universal but useful concept: parameters have different adaptation needs.

## Loss Scale across Objectives

Multi-task loss:

\[
L=\sum_k\lambda_kL_k
\]

Raw loss magnitudes/gradient norms differ. `λ_k` determines training influence, not just displayed number.

One task may dominate shared representation if gradients much larger.

Methods can dynamically balance tasks by uncertainty, gradient norms or conflict handling.

## Gradient Conflict in Multi-Task Learning

Two task gradients may point opposing directions:

\[
g_1^Tg_2<0
\]

Shared update helps one task, hurts other. This is representation/objective trade-off, not optimizer bug.

Understanding gradient geometry helps design task weights or separate adapters.

## Sharp Loss Spikes

Large-model training sometimes sees transient spikes due to rare batches, optimizer state, precision or data anomalies.

Operational response:

- log offending batch/source;
- inspect gradient/activation norms;
- checkpoint frequently;
- skip/recover if non-finite;
- consider clipping/lower LR/data cleaning.

Blind restart without diagnosis wastes compute.

## Checkpointing

Checkpoint should include more than model weights if resume exact training:

```text
model parameters
optimizer states
scheduler state
random generator states
data-loader position / sampler state
scaler state for mixed precision
training step / config
```

Load only weights with fresh optimizer is **fine-tuning/restart-like**, not exact resume.

## Exponential Moving Average of Weights

Maintain:

\[
\theta_{EMA}\leftarrow\beta\theta_{EMA}+(1-\beta)\theta
\]

EMA weights smooth trajectory and often improve evaluation in vision/generative training.

Stochastic Weight Averaging similarly average checkpoints/weights in later training to seek wider solution region.

## Validation Frequency

Validate too often → overhead; too rarely → miss overfitting/divergence and waste compute.

Frequency should tie to dataset size, training cost và expected change rate.

For massive pretraining, proxy metrics and periodic full eval suites coexist.

## Reproducibility

Exact reproducibility difficult due to:

- random seeds;
- data order;
- GPU nondeterministic kernels;
- distributed reduction order;
- library/compiler versions;
- low-precision rounding.

Scientific/production reproducibility often targets metric-level consistency rather than bitwise equality.

Log all configs and code/data versions.

## Distributed Training Dynamics

Data parallelism averages gradients across workers. Effective global batch:

\[
B_{global}=B_{device}\times N_{devices}\times accumulation
\]

Changing device count can change batch/LR dynamics if not adjusted.

Communication precision/order may affect numerical result.

Large-scale optimization is algorithm + distributed system jointly.

## Scaling Laws Preview

As model/data/compute scale, loss often follows approximate power-law relationships over regimes. This informs resource allocation but does not guarantee downstream capability/safety.

Scaling laws will be detailed in LLM chapter.

## A systematic debugging order

Khi training fail, đừng ngay lập tức đổi optimizer. Check từ simple to complex:

1. Data/labels correct?
2. Can tiny subset overfit? Nếu không, implementation/model bug likely.
3. Forward outputs finite and reasonable?
4. Loss implementation correct?
5. Gradients nonzero/finite?
6. LR/update magnitude reasonable?
7. Activation/gradient stats stable?
8. Validation split correct/no leakage?
9. Capacity/regularization adequate?
10. Distributed/mixed-precision issues?

**Overfit a tiny batch** là diagnostic cực mạnh: model đủ expressive nên phải memorize vài examples. Nếu không, pipeline/training bug.

## Mental Model

> Training là một dynamical system trong parameter space, được điều khiển bởi data sequence, objective, optimizer, schedule, numerical precision và architecture.

Không chỉ final hyperparameters mà cả trajectory quan trọng.

## Common Misconceptions

### “Loss đang giảm nên training bình thường”

Có thể validation degrade, model exploit shortcut hoặc data leakage.

### “Same seed nghĩa exact same run”

Distributed GPU operations có thể nondeterministic.

### “Checkpoint chỉ cần weights”

Exact resume cần optimizer/scheduler/RNG/data position.

### “Training instability luôn do learning rate”

LR common cause nhưng data anomalies, precision, normalization, initialization, gradient explosion cũng có thể.

## Knowledge Connection

Chapter này tổng hợp [Forward](./03_forward_propagation.md), [Backpropagation](./04_backpropagation.md), [Optimizers](./05_gradient_descent_and_optimizers.md), [Initialization/Normalization](./06_initialization_and_normalization.md), [Regularization](./07_regularization.md) và [Model Evaluation](../04_machine_learning/15_model_evaluation.md).

Nó là cầu sang `06_deep_learning_architectures/`, nơi architecture cụ thể thay computation graph và training dynamics.