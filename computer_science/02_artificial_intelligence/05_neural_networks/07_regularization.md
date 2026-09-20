# Regularization trong Neural Networks

Regularization (규제 / 정규화라는 표현도 쓰이지만 normalization과 구분 필요 / điều chuẩn) là các mechanisms bias training về những solutions có khả năng generalize tốt hơn, thay vì chỉ minimize training loss. Trong neural networks, regularization không phải một “mẹo chống overfitting” riêng lẻ; nó xuất hiện qua objective, architecture, data, stochasticity và optimization.

Cần phân biệt `regularization` với `normalization`. Normalization kiểm soát statistics/scale; regularization kiểm soát effective complexity hoặc preference among solutions.

## L2 Penalty và Weight Decay

L2-regularized objective:

\[
J(\theta)=\hat R(\theta)+\lambda\|\theta\|_2^2
\]

khuyến khích parameters magnitude nhỏ.

Với vanilla SGD, L2 gradient term:

\[
2\lambda\theta
\]

tạo shrinkage tương tự weight decay. Với adaptive optimizers, decoupled weight decay (AdamW) khác naive L2 penalty.

Weight decay có thể improve generalization và stabilize scale, nhưng optimal value phụ thuộc learning rate, batch size, architecture và training length.

## L1 Regularization

\[
J=\hat R+\lambda\|\theta\|_1
\]

encourage sparsity. Với large neural networks, pure L1 ít là default hơn L2/weight decay nhưng useful khi muốn sparse solution hoặc specific constraints.

Structured sparsity có thể target whole channels/heads/blocks để actual hardware speedup; random individual zeros không luôn tăng speed nếu kernels không exploit sparsity.

## Dropout

Trong training, dropout random mask activations:

\[
\tilde h_i=\frac{m_i}{1-p}h_i,
\qquad m_i\sim Bernoulli(1-p)
\]

`p` là drop probability. Scaling `1/(1-p)` giữ expected activation roughly same.

Dropout ngăn units phụ thuộc quá mạnh vào exact co-adaptation và tạo stochastic ensemble-like effect.

Inference thường disable dropout.

## Dropout không phải luôn cần

Large modern models với huge data, normalization, augmentation và weight decay có thể dùng dropout rất thấp hoặc zero trong pretraining. Fine-tuning small data có thể lại benefit.

Regularization strength phải match data/model regime.

## Early Stopping

Nếu validation performance bắt đầu worsen trong khi training loss tiếp tục giảm, stop tại checkpoint tốt nhất.

Early stopping acts như regularization vì giới hạn optimization trajectory; model chưa có thời gian fit finer sample-specific patterns.

Nhưng nếu training schedule chưa tuned, stop sớm có thể chỉ mask bad learning rate.

## Data Augmentation

Augmentation tạo transformed examples mà label/semantics nên preserve:

Image:

```text
crop, flip, color jitter, rotation (nếu task invariant)
```

Audio:

```text
noise, time masking, frequency masking
```

Text augmentation khó hơn vì small wording change có thể đổi meaning.

Augmentation encode **invariance assumptions**. Horizontal flip hợp object recognition nhưng có thể sai với text image hoặc medical laterality.

## Mixup

Mixup tạo convex combinations:

\[
\tilde x=\lambda x_i+(1-\lambda)x_j
\]

\[
\tilde y=\lambda y_i+(1-\lambda)y_j
\]

Nó encourage smoother behavior giữa examples và giảm sharp memorization.

CutMix cho images paste region từ image khác và mix labels proportional area.

## Label Smoothing

One-hot target thay bằng slightly softened distribution:

\[
y'_k=(1-\epsilon)y_k+\frac{\epsilon}{K}
\]

hoặc variant distribute mass among incorrect classes.

Label smoothing giảm incentive đẩy logits tới extreme confidence, có thể improve generalization/calibration trong regimes.

Nhưng nó cũng có trade-offs, ví dụ representations cho distillation/calibration có thể thay đổi; không nên apply blindly.

## Noise Injection

Thêm noise vào inputs, activations, weights hoặc gradients có regularization effect. Dropout là một form structured multiplicative noise.

Stochastic Gradient Descent mini-batch noise cũng tạo implicit regularization.

## Architectural Regularization

Convolution weight sharing giảm degrees of freedom so với dense layer.

Bottlenecks giới hạn representation capacity.

Low-rank adapters constrain fine-tuning updates vào low-rank subspace.

Sparse attention/routing constrain interactions.

Architecture itself is regularizer through inductive bias.

## Parameter Sharing

RNN reuse same weights across timesteps; CNN reuse kernel across locations; Transformer reuse same projection matrices across token positions within layer.

Sharing reduces parameter count và encodes symmetry/invariance assumptions.

## Batch Normalization as implicit regularization

Batch statistics introduce noise depending on co-samples. This can regularize. With very large batch or synchronized stats, effect changes.

Do not treat normalization and regularization as identical, but acknowledge interactions.

## Pretraining as Regularization / Prior

Fine-tuning pretrained model starts from parameters encoding broad structure. Small task dataset only nudges solution around pretrained region.

This acts like a strong data-driven prior compared with training from random initialization.

Transfer learning therefore changes bias–variance landscape dramatically.

## Parameter-Efficient Fine-Tuning

LoRA models update:

\[
\Delta W=BA
\]

with low rank `r`:

\[
A\in R^{r\times d_{in}},
B\in R^{d_{out}\times r}
\]

Instead of full arbitrary `ΔW`, updates constrained low-rank. This reduces memory and can regularize small-data adaptation.

LoRA will return in LLM fine-tuning chapters.

## Regularization và Memorization

Neural networks can memorize random labels with enough capacity, showing architecture capacity alone doesn't force generalization.

Real generalization comes from combination of structure in natural data, optimization bias, regularization, augmentation and scale.

Memorization and generalization can coexist; model may memorize rare examples while still generalizing broadly.

## Regularization under Distribution Shift

Regularization improving IID test may not improve robustness to domain shift. Data augmentation aligned with expected shift can help more than generic weight decay.

Robustness requires evaluate on shifted/stress distributions, not infer from regularization alone.

## Mental Model

> Regularization is preference: trong rất nhiều parameter settings fit training data, ta muốn learning procedure ưu tiên những solutions đơn giản/stable/invariant hoặc gần useful prior hơn.

## Common Misconceptions

### “More regularization always means less overfitting and therefore better”

Quá mạnh gây underfitting hoặc erase useful task adaptation.

### “Dropout phải có trong mọi neural network”

Không. Need depends data scale/architecture/training regime.

### “Data augmentation chỉ tăng số lượng samples”

Nó quan trọng hơn ở việc encode invariances.

### “Weight decay làm model sparse”

L2/weight decay shrink magnitude nhưng không thường tạo exact zeros như L1/structured pruning.

### “Fine-tuning ít parameters chỉ để tiết kiệm VRAM”

Parameter constraints cũng thay inductive bias và có thể reduce overfitting.

## Knowledge Connection

Xem [Bias–Variance and Generalization](../04_machine_learning/14_bias_variance_and_generalization.md), [AdamW](./05_gradient_descent_and_optimizers.md), [Initialization and Normalization](./06_initialization_and_normalization.md), và tiếp theo [Representation Learning](./08_representation_learning.md).