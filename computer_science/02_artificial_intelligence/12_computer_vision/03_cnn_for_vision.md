# Convolutional Neural Network trong Computer Vision

**Convolutional Neural Network (CNN / 합성곱 신경망)** đưa vào một inductive bias rất phù hợp với image: local pattern quan trọng và cùng một pattern có thể xuất hiện ở nhiều vị trí khác nhau.

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

Output tại mỗi location là weighted combination của một local patch qua toàn bộ input channel.

Số parameter không phụ thuộc trực tiếp vào image width hoặc height:

\[
\#params=k_hk_wC_{in}C_{out}+C_{out}
\]

Đây là một lý do CNN tiết kiệm parameter hơn dense network trên image.

## Weight Sharing

Cùng một kernel được trượt qua mọi location. Nếu kernel học một vertical edge detector, detector đó có thể phát hiện edge ở bên trái hoặc bên phải image bằng cùng một bộ weight.

Weight sharing encode prior rằng một pattern thị giác có ý nghĩa tương tự bất kể nó xuất hiện ở vị trí nào.

## Translation Equivariance

Convolution lý tưởng gần **equivariant với translation**:

\[
f(T_x X)\approx T_x f(X)
\]

Nếu input dịch chuyển, feature map cũng dịch chuyển tương ứng.

Classification head sau pooling có thể tạo thêm invariance đối với translation nhỏ.

## Receptive Field

Neuron ở layer đầu chỉ nhìn local patch nhỏ. Khi stack nhiều layer, **effective receptive field** tăng dần.

Nhiều convolution 3×3 liên tiếp có thể cover vùng rộng hơn đồng thời chèn thêm nonlinearity giữa các layer.

Receptive field quyết định model có thể kết hợp context ở phạm vi rộng đến đâu.

## Stride

Stride lớn hơn 1 làm downsample spatial resolution.

Output dimension gần đúng:

\[
H_{out}=\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1
\]

Downsampling giảm compute và memory nhưng cũng làm mất spatial detail.

## Padding

Padding kiểu `same` giữ spatial resolution gần như không đổi; `valid` không thêm border nên output nhỏ dần.

Cách xử lý border ảnh hưởng feature gần edge của image và có thể tạo artifact nếu không phù hợp.

## Pooling

Max pooling giữ local maximum; average pooling lấy mean của vùng.

Pooling giúp giảm resolution và tăng local invariance, nhưng cũng có thể làm mất precise location.

Nhiều modern CNN dùng strided convolution thay cho pooling ở một số stage.

## Channel như Learned Feature Type

Input RGB có ba channel. Hidden layer có thể có hàng chục hoặc hàng trăm channel.

Mỗi channel không nhất thiết có interpretation đơn giản như “edge ngang” hoặc “mắt”, vì representation thường distributed. Tuy nhiên channel có thể xem như các learned feature family hoạt động tại mỗi spatial position.

## Hierarchical Feature

Một trực giác phổ biến:

```text
pixel
→ edge / color blob
→ texture / part
→ object-level pattern
```

Thực tế representation phức tạp và distributed hơn, nhưng hierarchy này giúp hiểu vì sao depth có giá trị: layer sau có thể xây feature dựa trên composition của feature layer trước.

## Residual Connection

Deep CNN gặp optimization difficulty khi depth tăng. ResNet dùng block:

\[
y=F(x)+x
\]

Identity path giúp gradient và information đi xuyên network dễ hơn. Model học residual adjustment thay vì phải tái tạo toàn bộ mapping từ đầu ở mỗi block.

Residual connection sau này cũng trở thành pattern cốt lõi trong Transformer.

## Batch Normalization

CNN truyền thống thường dùng **Batch Normalization (BatchNorm)** để ổn định activation statistic và optimization.

Training và inference behavior khác nhau vì BatchNorm dùng batch statistic khi train và running statistic khi eval.

Batch rất nhỏ có thể làm statistic không ổn định; GroupNorm hoặc LayerNorm phù hợp hơn trong một số setting.

## Depthwise Separable Convolution

Standard convolution đồng thời xử lý spatial dimension và trộn channel.

Depthwise separable convolution tách thành:

1. spatial convolution riêng trên từng channel;
2. 1×1 pointwise convolution để trộn các channel.

Cách này giảm compute đáng kể và phổ biến trong mobile architecture.

## 1×1 Convolution

Kernel 1×1 không nhìn neighbor spatial nhưng trộn channel tại mỗi position.

Có thể xem nó như một linear projection áp dụng độc lập ở từng pixel/position. Nó thường dùng để đổi channel dimension hoặc tạo bottleneck.

## Dilated Convolution

Dilated convolution chèn khoảng trống giữa các điểm sample của kernel, làm receptive field tăng mà không cần kernel lớn hoặc downsample mạnh.

Nó hữu ích khi cần giữ resolution cao, chẳng hạn segmentation.

## Grouped Convolution

Grouped convolution chia channel thành nhiều group và chỉ convolution trong từng group.

Điều này giảm compute và tạo structural sparsity. Depthwise convolution là extreme case nơi mỗi input channel là một group riêng.

## Global Average Pooling

Thay vì flatten toàn feature map rồi dùng dense layer rất lớn, có thể average từng channel theo spatial dimension:

\[
z_c=\frac1{HW}\sum_{i,j}X_{i,j,c}
\]

Global average pooling giảm parameter và tạo vector feature gọn cho classification head.

## Compute của CNN

Convolution thường được implement bằng specialized kernel hoặc GEMM trên accelerator.

FLOPs không phản ánh hoàn toàn latency thực tế. Memory layout, bandwidth, cache behavior, kernel fusion và hardware utilization đều ảnh hưởng performance.

## Data Augmentation và CNN Bias

Crop, flip, color jitter hoặc scale augmentation giúp reinforce các invariance mà architecture một mình không đảm bảo.

Behavior cuối cùng đến từ tổ hợp:

```text
architecture prior
+ augmentation prior
+ dataset distribution
+ training objective
```

## Transfer Learning

CNN pretrained trên dataset lớn có thể fine-tune cho downstream task.

Feature ở layer đầu hoặc giữa thường tái sử dụng được tốt, nhưng domain gap lớn như natural image → medical image có thể yêu cầu adaptation mạnh hơn.

## CNN và Vision Transformer

CNN có đặc điểm:

```text
strong locality / translation prior
tốt về data efficiency trong nhiều setting
multi-scale feature map tự nhiên
```

Vision Transformer có đặc điểm:

```text
ít hard-code locality hơn
self-attention hỗ trợ global interaction
scale mạnh khi pretraining lớn
```

Modern vision system thường kết hợp ý tưởng từ cả hai family thay vì coi chúng hoàn toàn loại trừ nhau.

## Mô hình tư duy

> **CNN mạnh không phải vì convolution là “phép thuật”, mà vì architecture giới hạn hypothesis space theo giả định rằng local spatial pattern và repeated detector rất quan trọng trong image.**

Inductive bias phù hợp giúp learning hiệu quả hơn.

## Những nhầm lẫn thường gặp

### “Convolution tự tạo translation invariance hoàn toàn”

Không. Convolution chủ yếu tạo equivariance; padding, stride, pooling và augmentation mới quyết định mức invariance cuối cùng.

### “Network càng sâu luôn càng tốt”

Không. Optimization, resolution, compute budget và task quyết định depth hữu ích.

### “CNN đã lỗi thời vì Vision Transformer”

Không. CNN vẫn rất mạnh và hiệu quả cho nhiều edge, detection và specialized vision workload.

## Liên kết kiến thức

CNN là ví dụ cụ thể của [Inductive Bias](../04_machine_learning/01_learning_problem_and_inductive_bias.md) và [Representation Learning](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Image Classification](./04_image_classification.md).