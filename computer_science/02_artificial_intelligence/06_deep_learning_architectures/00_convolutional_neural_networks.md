# Convolutional Neural Networks: tận dụng cấu trúc không gian

Convolutional Neural Network (CNN / 합성곱 신경망) được tạo ra vì dense MLP đối xử mọi input dimension như độc lập, trong khi image có structure rất mạnh: pixels gần nhau tạo local patterns, cùng một edge có thể xuất hiện ở nhiều vị trí, và spatial hierarchy từ edge → texture → part → object có tính compositional.

CNN encode hai inductive biases chính: **local connectivity** và **weight sharing**.

## Vì sao flatten image vào MLP là lãng phí?

Image RGB `224×224×3` có 150,528 values. Dense layer 4096 units cần hơn 600 triệu weights chỉ layer đầu.

Quan trọng hơn, flatten bỏ explicit locality. Pixel ở `(10,10)` và `(10,11)` vốn neighboring nhưng vector index không cho MLP biết relation đặc biệt đó.

CNN giữ spatial grid và dùng local kernels.

## Convolution operation

Một 2D kernel nhỏ, ví dụ `3×3`, trượt qua image. Với single channel:

\[
y_{i,j}=\sum_{u,v}K_{u,v}x_{i+u,j+v}
\]

Deep-learning frameworks thường implement cross-correlation (không flip kernel) nhưng vẫn gọi convolution.

Multi-channel input:

\[
W\in R^{C_{out}\times C_{in}\times K_h\times K_w}
\]

mỗi output channel combine local patch across all input channels.

## Weight Sharing

Cùng kernel weights được reuse mọi spatial location. Nếu kernel học vertical edge, nó detect edge ở nhiều vị trí.

Parameter count không phụ thuộc image width/height trực tiếp:

\[
C_{out}(C_{in}K_hK_w+1)
\]

Đây là huge efficiency gain so dense connection.

## Translation Equivariance

Nếu input shift, convolution feature map cũng shift tương ứng (ignoring boundaries/stride effects). Đây là **equivariance**, không phải exact invariance.

Pooling/global aggregation có thể tạo more invariant final prediction.

## Stride, Padding, Dilation

Output size 1D:

\[
O=\left\lfloor\frac{N+2P-D(K-1)-1}{S}+1\right\rfloor
\]

`S` stride, `P` padding, `D` dilation.

- stride >1 downsample;
- padding giữ spatial size/control border;
- dilation mở receptive field mà không tăng kernel parameters nhiều.

## Receptive Field

Unit ở deep layer phụ thuộc một region của original image. Stack `3×3` convolutions làm receptive field tăng.

Early layers local; deeper units integrate larger context.

**Effective receptive field** có thể nhỏ hơn theoretical vì contribution distribution không uniform.

## Pooling

Max pooling:

\[
y_{i,j}=\max_{(u,v)\in window}x_{i+u,j+v}
\]

Average pooling lấy mean.

Pooling giảm resolution, tăng effective receptive field và tạo local invariance. Modern CNN đôi khi dùng strided convolution thay pooling.

Global Average Pooling average toàn spatial map per channel, giảm dense-head parameters.

## Hierarchical Features

Một classic interpretation:

```text
pixels
→ edges/orientations
→ textures/simple shapes
→ parts
→ object-level features
```

Không phải mọi channel cleanly map concept, nhưng hierarchy intuition hữu ích vì receptive field và composition tăng qua depth.

## ResNet và Skip Connections

Very deep CNN khó optimize. ResNet block:

\[
y=x+F(x)
\]

cho identity path và easier gradient flow.

Thay vì mỗi block phải learn full mapping, nó learn residual correction `F(x)`.

Residual architecture trở thành principle chung và xuất hiện mạnh trong Transformers.

## 1×1 Convolution

Kernel `1×1` không mix neighbors spatially nhưng mix channels:

\[
y_{i,j}=W x_{i,j}
\]

Nó là per-location linear projection, useful để change channel dimension/bottleneck.

## Depthwise Separable Convolution

Standard conv mixes spatial + channel jointly. Depthwise separable conv tách:

1. depthwise spatial conv per channel;
2. pointwise `1×1` conv mix channels.

Compute giảm mạnh, used in MobileNet-like architectures.

## BatchNorm và CNN Training

CNN historically dùng Conv → BatchNorm → ReLU patterns. Modern variants thay ordering/norm/activation.

BatchNorm works well with sufficiently large image batches; small-batch detection/segmentation may prefer GroupNorm.

## CNN for more than Images

1D convolution: audio/time series/text local patterns.

3D convolution: video/medical volumes.

Graph convolutions generalize neighborhood aggregation on non-grid structures nhưng mathematical operation khác grid convolution.

## Classification, Detection, Segmentation

Image classification output one/few labels.

Object detection cần bounding boxes + classes.

Segmentation prediction per pixel.

Same CNN backbone can feed different heads. Task output structure quyết định architecture beyond feature extractor.

## CNN vs Vision Transformer

CNN hardcodes locality/translation sharing. Vision Transformer splits image into patches và learn global interactions through attention.

CNN often data-efficient due strong inductive bias; ViT scales extremely well with large pretraining. Modern vision systems frequently hybrid or use convolution-like local biases inside transformers.

Không có simple “Transformer replaced CNN” rule.

## Mental Model

> CNN says: local pattern matters, same kind of pattern can occur anywhere, and complex visual concepts can be composed hierarchically from local features.

## Common Misconceptions

### “Convolution automatically makes model translation invariant”

Convolution is mainly equivariant. Pooling/aggregation/training augmentation contribute invariance.

### “CNN kernel is hand-designed edge filter”

Classical vision used hand filters; CNN kernels are learned end-to-end.

### “Deep layer neuron always represents object part”

Representation distributed; conceptual hierarchy is approximate mental model.

### “CNN obsolete after Vision Transformer”

CNN remains strong, efficient and widely deployed; architectures converge/hybridize.

## Knowledge Connection

CNN applies [Representation Learning](../05_neural_networks/08_representation_learning.md), [Weight Sharing/Regularization](../05_neural_networks/07_regularization.md) and [Residual Connections](../05_neural_networks/04_backpropagation.md).

Computer Vision domain later expands detection, segmentation and ViT.