# Convolutional Neural Networks cho Vision

**Convolutional Neural Network (CNN / 합성곱 신경망)** đưa một inductive bias rất phù hợp với image: local patterns quan trọng và pattern tương tự có thể xuất hiện ở nhiều vị trí.

Thay vì fully connected layer nối mọi pixel với mọi hidden unit, convolution dùng **local receptive field** và **weight sharing**.

## Convolution Layer

Input feature map:

\[
X\in\mathbb{R}^{H\times W\times C_{in}}
\]

Kernel:

\[
K\in\mathbb{R}^{k_h\times k_w\times C_{in}\times C_{out}}
\]

Output mỗi location là weighted combination của local patch qua toàn input channels.

Số parameters không depend trực tiếp vào image width/height:

\[
\#params=k_hk_wC_{in}C_{out}+C_{out}
\]

Đây là lý do CNN parameter-efficient hơn dense network trên images.

## Weight Sharing

Cùng kernel được slide qua mọi location. Nếu kernel học vertical edge, nó detect edge ở left hay right bằng same weights.

Đây encode translation-related prior.

## Translation Equivariance

Ideal convolution gần equivariant:

\[
f(T_x X)\approx T_x f(X)
\]

Translate input → feature map translate tương ứng.

Classification sau pooling có thể trở nên more invariant.

## Receptive Field

Neuron layer đầu thấy local patch. Stack layers làm effective receptive field grow.

Ví dụ nhiều 3×3 convolutions có thể cover region lớn hơn trong khi thêm nonlinearities.

Receptive field quyết định model nhìn context rộng tới đâu.

## Stride

Stride > 1 downsample spatial resolution.

Output dimension roughly:

\[
H_{out}=\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1
\]

Downsampling giảm compute nhưng mất spatial detail.

## Padding

`same`-style padding giữ resolution tương đối; `valid` giảm size. Border treatment ảnh hưởng features near edges.

## Pooling

Max pooling chọn local maximum; average pooling lấy mean.

Pooling giảm resolution và tăng local invariance nhưng có thể discard precise position.

Modern CNN nhiều khi dùng strided convolution thay pooling.

## Channels như Learned Feature Types

Input RGB có 3 channels; hidden layers có dozens/hundreds channels. Mỗi channel không necessarily interpretable đơn giản, nhưng có thể encode families of patterns.

## Hierarchical Features

Một common intuition:

```text
pixels
→ edges/color blobs
→ textures/parts
→ object-level patterns
```

Thực tế representations distributed và nonlinear, nhưng hierarchy giải thích lợi ích depth.

## Residual Connections

Deep CNN gặp optimization difficulty. ResNet block:

\[
y=F(x)+x
\]

cho gradient/representation một identity path. Network học residual adjustment thay vì reconstruct entire mapping.

Residual connection sau này là core Transformer pattern.

## Batch Normalization

CNN historically dùng BatchNorm để stabilize activation statistics và optimization. Behavior train/eval khác nhau vì running statistics.

Small batch sizes có thể làm BatchNorm unstable; alternatives GroupNorm/LayerNorm phù hợp contexts khác.

## Depthwise Separable Convolution

Standard convolution mix spatial + channels cùng lúc. Depthwise separable tách:

1. spatial conv per channel;
2. 1×1 pointwise conv mix channels.

Compute giảm mạnh, popular trong mobile architectures.

## 1×1 Convolution

Kernel 1×1 không nhìn neighbors nhưng mix channels tại mỗi position. Nó hoạt động như per-pixel linear projection và dùng để change channel dimensions/bottleneck.

## Dilated Convolution

Dilated convolution chèn gaps trong kernel sampling, tăng receptive field mà không tăng kernel size/downsample nhiều. Hữu ích segmentation/audio.

## Grouped Convolution

Channels chia groups, giảm compute và tạo structural sparsity. Depthwise là extreme case mỗi channel một group.

## Global Average Pooling

Thay flatten + huge dense layer, average mỗi channel across spatial positions:

\[
z_c=\frac1{HW}\sum_{i,j}X_{i,j,c}
\]

Giảm parameters và kết nối channel evidence tới classification head.

## CNN Compute

Convolution được implement hiệu quả bằng specialized kernels/GEMM. Memory layout, kernel fusion và accelerator libraries ảnh hưởng performance thực tế.

FLOPs không phản ánh hoàn toàn latency; memory bandwidth và hardware utilization cũng quan trọng.

## Data Augmentation và CNN Bias

Crop/flip/color jitter reinforce invariances CNN architecture alone không guarantee.

Architecture prior + augmentation prior + dataset cùng quyết định behavior.

## Transfer Learning

CNN pretrained trên large dataset có thể fine-tune downstream. Early/mid features often reusable, nhưng domain gap như natural images → medical images có thể lớn.

## CNN vs Vision Transformer

CNN:

```text
strong locality/translation prior
high data efficiency in many settings
hierarchical multi-scale maps naturally
```

ViT:

```text
weaker hard-coded locality
self-attention global interaction
scales strongly with large pretraining
```

Modern systems often combine ideas từ cả hai.

## Mental Model

> **CNN không “hiểu ảnh” vì convolution magic; nó giới hạn hypothesis space theo giả định rằng local spatial patterns và repeated detectors là useful.**

Inductive bias phù hợp giúp learning efficient.

## Common Misconceptions

### “Convolution tự tạo translation invariance hoàn toàn”

Convolution chủ yếu equivariant; padding, stride, pooling và data augmentation ảnh hưởng invariance.

### “Deeper luôn tốt hơn”

Optimization, resolution, compute và task determine useful depth.

### “CNN đã obsolete vì ViT”

CNN vẫn strong/efficient trong nhiều edge, detection và specialized vision workloads.

## Knowledge Connection

CNN là concrete example của [Inductive Bias](../04_machine_learning/01_learning_problem_and_inductive_bias.md) và [Representation Learning](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Image Classification](./04_image_classification.md).