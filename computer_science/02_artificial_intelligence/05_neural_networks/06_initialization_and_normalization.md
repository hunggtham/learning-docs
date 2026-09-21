# Initialization và Normalization: giữ Signal và Gradient ở Scale Trainable

Deep network có thể có architecture đúng nhưng training fail ngay từ đầu nếu activations hoặc gradients explode/vanish qua layers. **Initialization (초기화 / khởi tạo)** chọn starting distribution của parameters; **Normalization (정규화 / chuẩn hóa)** kiểm soát statistics của intermediate representations trong training.

Hai concept này giải quyết một core systems problem: làm sao signal đi qua nhiều transformations mà vẫn ở numerical/optimization scale hợp lý?

## Vì sao không initialize mọi weight bằng zero?

Nếu neurons cùng layer có identical weights zero, chúng nhận cùng gradient và tiếp tục giống nhau. **Symmetry breaking** cần random initialization để units học functions khác nhau.

Bias có thể initialize zero vì weights đã break symmetry.

## Variance propagation

Giả sử:

\[
z=\sum_{i=1}^{n}w_ix_i
\]

Nếu independent, zero-mean:

\[
Var(z)\approx nVar(w)Var(x)
\]

Nếu `Var(w)` không scale theo fan-in `n`, activation variance tăng/giảm theo depth.

Initialization tốt cố giữ forward activation variance và backward gradient variance roughly stable.

## Xavier / Glorot Initialization

Phù hợp tanh/sigmoid-like symmetric activations:

\[
Var(w)\approx\frac{2}{fan_{in}+fan_{out}}
\]

Một common form uniform:

\[
w\sim U\left(-\sqrt{\frac{6}{fan_{in}+fan_{out}}},
\sqrt{\frac{6}{fan_{in}+fan_{out}}}\right)
\]

Mục tiêu balance signal forward/backward.

## He / Kaiming Initialization

ReLU zero roughly half activations under symmetric assumption, nên use larger variance:

\[
Var(w)\approx\frac{2}{fan_{in}}
\]

Common normal initialization:

\[
w\sim\mathcal N(0,2/fan_{in})
\]

Activation-specific gain matters.

## Initialization không độc lập architecture

Residual networks, Transformers, gated blocks và normalization layers thay signal dynamics. Large-model recipes có custom scaling, residual branch initialization hoặc μ-parameterization variants.

Không có một initialization formula universal cho mọi architecture.

## Batch Normalization

BatchNorm normalize activation per feature/channel dùng mini-batch statistics:

\[
\mu_B=\frac1m\sum_i x_i
\]

\[
\sigma_B^2=\frac1m\sum_i(x_i-\mu_B)^2
\]

\[
\hat x_i=\frac{x_i-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}
\]

rồi learn affine scale/shift:

\[
y_i=\gamma\hat x_i+\beta
\]

`γ,β` cho model restore useful scale/offset.

## BatchNorm giúp gì?

Lịch sử thường giải thích bằng “reduce internal covariate shift”, nhưng modern understanding rộng hơn. BatchNorm:

- stabilizes activation scale;
- smooths optimization landscape in useful ways;
- permits larger LR;
- adds batch-dependent noise/regularization;
- reduces sensitivity to initialization.

Không nên coi một single explanation là complete.

## Train vs Eval trong BatchNorm

Training dùng current batch stats và update running estimates. Evaluation dùng running mean/variance.

Small batch làm estimates noisy. Distributed training có SyncBatchNorm để aggregate stats across devices, nhưng communication cost tăng.

Nếu deployment distribution shift, stale running stats cũng có thể gây degradation.

## Layer Normalization

LayerNorm normalize across feature dimensions của từng sample/token:

\[
\mu=\frac1D\sum_{j=1}^{D}x_j
\]

\[
\sigma^2=\frac1D\sum_j(x_j-\mu)^2
\]

Không phụ thuộc batch size, nên phù hợp sequence models/Transformers.

Transformer hidden state `x∈R^D` được normalize per token.

## RMSNorm

RMSNorm bỏ mean-centering, scale bằng root mean square:

\[
RMS(x)=\sqrt{\frac1D\sum_jx_j^2+\epsilon}
\]

\[
y=\gamma\odot\frac{x}{RMS(x)}
\]

Đơn giản/efficient và phổ biến trong modern LLMs.

## GroupNorm và InstanceNorm

**GroupNorm** chia channels thành groups rồi normalize trong group, không phụ thuộc batch statistics mạnh; useful khi vision batch small.

**InstanceNorm** normalize per sample/channel và phổ biến trong style/image generation contexts.

Normalization axes là modeling choice.

## Pre-Norm vs Post-Norm Transformer

Post-Norm classic:

\[
y=LN(x+F(x))
\]

Pre-Norm:

\[
y=x+F(LN(x))
\]

Pre-Norm tạo cleaner identity residual gradient path và thường train deep Transformers stable hơn, nên được dùng rộng rãi.

Architecture details như norm placement ảnh hưởng optimization lớn.

## Normalization không chỉ standardize input

Input standardization là preprocessing trên dataset. BatchNorm/LayerNorm là internal differentiable modules với learned scale/shift, applied repeatedly inside network.

Hai concept related nhưng khác scope và behavior.

## Epsilon và Numerical Stability

Denominator thêm `ε` để tránh divide-by-zero:

\[
\sqrt{\sigma^2+\epsilon}
\]

Choice epsilon có thể matter trong low precision. Normalization kernels thường accumulate stats higher precision.

## Weight Normalization và Spectral Normalization

Có normalization tác động parameters thay activations.

WeightNorm reparameterize weight thành direction + magnitude.

Spectral Normalization constrain largest singular value, giúp control Lipschitz behavior và từng được dùng mạnh trong GAN discriminators.

Normalization là family rộng, không chỉ BatchNorm.

## Interaction với Regularization

BatchNorm noise có implicit regularization; Dropout + BatchNorm interaction đôi khi complex. Weight decay trên norm scale/bias thường excluded trong modern optimizer configs.

Recipes phải xem whole system, không tune từng trick isolated.

## Debugging signal statistics

Theo dõi per-layer:

```text
activation mean/std
activation max/min
zero fraction
gradient norm
parameter norm
update/parameter ratio
```

Nếu std tăng exponential qua depth → exploding signal. Nếu collapse gần zero → vanishing/dead units.

## Mental Model

```text
Initialization = chọn starting scale để network bắt đầu ở vùng trainable
Normalization  = liên tục giữ intermediate scale/statistics trong vùng dễ optimize
Residual paths = tạo đường truyền signal/gradient ổn định
```

## Common Misconceptions

### “Random small weights là đủ”

Scale phải depend fan-in/activation/architecture; quá nhỏ cũng gây vanishing.

### “BatchNorm và LayerNorm giống nhau, chỉ tên khác”

Axes/statistics và train/eval behavior khác fundamentally.

### “Normalization loại bỏ need for good initialization”

Nó giảm sensitivity nhưng initialization vẫn ảnh hưởng early dynamics và large/deep architecture stability.

### “LayerNorm làm token vector mất information vì mean=0 variance=1”

Learned affine parameters và direction/relative pattern vẫn carry information; residual stream architecture cũng giữ pathways khác.

## Knowledge Connection

Xem [Activation Functions](./02_activation_functions.md), [Backpropagation](./04_backpropagation.md), [Optimizers](./05_gradient_descent_and_optimizers.md) và sau này [Transformer](../06_deep_learning_architectures/05_transformer.md).