# Convolutional Neural Networks cho Vision

> **Mạch đọc:** Đặt **Convolutional Neural Networks cho Vision** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Convolution tầng (layer / 계층)** sang **Weight Sharing**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Convolutional Neural mạng (network / 네트워크)** đưa một inductive độ lệch (bias / 편향) rất phù hợp với ảnh (image / 이미지): cục bộ (local / 로컬) patterns quan trọng và mẫu (pattern / 패턴) tương tự có thể xuất hiện ở nhiều vị trí.

Thay vì fully connected tầng (layer / 계층) nối mọi điểm ảnh (pixel / 픽셀) với mọi hidden đơn vị (unit / 단위), convolution dùng **cục bộ (local / 로컬) receptive trường dữ liệu (field / 필드)** và **weight sharing**.

## Convolution tầng (layer / 계층)

Đầu vào (input / 입력) tính năng (feature / 기능) map:

\[
X\in\mathbb{R}^{H\times W\times C_{in}}
\]

Kernel:

\[
K\in\mathbb{R}^{k_h\times k_w\times C_{in}\times C_{out}}
\]

Đầu ra (output / 출력) mỗi location là weighted combination của cục bộ (local / 로컬) patch qua toàn đầu vào (input / 입력) channels.

Số parameters không depend trực tiếp vào ảnh (image / 이미지) width/height:

\[
\#params=k_hk_wC_{in}C_{out}+C_{out}
\]

Đây là lý do CNN parameter-efficient hơn dense mạng (network / 네트워크) trên images.

## Weight Sharing

Cùng kernel được slide qua mọi location. Nếu kernel học vertical edge, nó detect edge ở left hay right bằng same weights.

Đây encode translation-related prior.

## Translation Equivariance

Ideal convolution gần equivariant:

\[
f(T_x X)\approx T_x f(X)
\]

Translate đầu vào (input / 입력) → tính năng (feature / 기능) map translate tương ứng.

Classification sau pooling có thể trở nên more bất biến (invariant / 불변식).

## Receptive trường dữ liệu (field / 필드)

Neuron tầng (layer / 계층) đầu thấy cục bộ (local / 로컬) patch. ngăn xếp (stack / 스택) layers làm effective receptive trường dữ liệu (field / 필드) grow.

Ví dụ nhiều 3×3 convolutions có thể cover region lớn hơn trong khi thêm nonlinearities.

Receptive trường dữ liệu (field / 필드) quyết định mô hình (model / 모델) nhìn ngữ cảnh (context / 맥락) rộng tới đâu.

## Stride

Stride > 1 downsample spatial resolution.

Đầu ra (output / 출력) dimension roughly:

\[
H_{out}=\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1
\]

Downsampling giảm compute nhưng mất spatial detail.

## Padding

`same`-style padding giữ resolution tương đối; `valid` giảm kích thước (size / 크기). Border treatment ảnh hưởng features near edges.

## Pooling

Max pooling chọn cục bộ (local / 로컬) maximum; average pooling lấy mean.

Pooling giảm resolution và tăng cục bộ (local / 로컬) invariance nhưng có thể discard precise position.

Hiện đại (modern / 현대적) CNN nhiều khi dùng strided convolution thay pooling.

## Channels như Learned tính năng (feature / 기능) Types

Đầu vào (input / 입력) RGB có 3 channels; hidden layers có dozens/hundreds channels. Mỗi channel không necessarily interpretable đơn giản, nhưng có thể encode families of patterns.

## Hierarchical Features

Một dùng chung (common / 공통) intuition:

```text
pixels
→ edges/color blobs
→ textures/parts
→ object-level patterns
```

Thực tế representations phân tán (distributed / 분산) và nonlinear, nhưng hierarchy giải thích lợi ích độ sâu (depth / 깊이).

## Residual Connections

Deep CNN gặp tối ưu hóa (optimization / 최적화) difficulty. ResNet khối (block / 블록):

\[
y=F(x)+x
\]

cho độ dốc (gradient / 기울기)/biểu diễn (representation / 표현) một định danh (identity / 식별자) đường dẫn (path / 경로). mạng (network / 네트워크) học residual adjustment thay vì reconstruct entire ánh xạ (mapping / 매핑).

Residual liên kết (connection / 연결) sau này là cốt lõi (core / 핵심) Transformer mẫu (pattern / 패턴).

## Batch Normalization

CNN historically dùng BatchNorm để stabilize activation statistics và tối ưu hóa (optimization / 최적화). hành vi (behavior / 동작) train/eval khác nhau vì running statistics.

Small batch sizes có thể làm BatchNorm unstable; alternatives GroupNorm/LayerNorm phù hợp contexts khác.

## Depthwise Separable Convolution

Tiêu chuẩn (standard / 표준) convolution mix spatial + channels cùng lúc. Depthwise separable tách:

1. spatial conv per channel;
2. 1×1 pointwise conv mix channels.

Compute giảm mạnh, popular trong mobile architectures.

## 1×1 Convolution

Kernel 1×1 không nhìn neighbors nhưng mix channels tại mỗi position. Nó hoạt động như per-pixel tuyến tính (linear / 선형) projection và dùng để thay đổi (change / 변경) channel dimensions/bottleneck.

## Dilated Convolution

Dilated convolution chèn gaps trong kernel sampling, tăng receptive trường dữ liệu (field / 필드) mà không tăng kernel kích thước (size / 크기)/downsample nhiều. Hữu ích segmentation/audio.

## Grouped Convolution

Channels chia groups, giảm compute và tạo structural sparsity. Depthwise là extreme trường hợp (case / 사례) mỗi channel một group.

## Toàn cục (global / 전역) Average Pooling

Thay flatten + huge dense tầng (layer / 계층), average mỗi channel across spatial positions:

\[
z_c=\frac1{HW}\sum_{i,j}X_{i,j,c}
\]

Giảm parameters và kết nối channel bằng chứng (evidence / 증거) tới classification head.

## CNN Compute

Convolution được implement hiệu quả bằng specialized kernels/GEMM. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃), kernel fusion và accelerator libraries ảnh hưởng hiệu năng (performance / 성능) thực tế.

FLOPs không phản ánh hoàn toàn độ trễ (latency / 지연 시간); bộ nhớ (memory / 메모리) bandwidth và hardware utilization cũng quan trọng.

## Dữ liệu (data / 데이터) Augmentation và CNN độ lệch (bias / 편향)

Crop/flip/color jitter reinforce invariances CNN kiến trúc (architecture / 아키텍처) alone không guarantee.

Kiến trúc (architecture / 아키텍처) prior + augmentation prior + dataset cùng quyết định hành vi (behavior / 동작).

## Transfer học tập (learning / 학습)

CNN pretrained trên large dataset có thể fine-tune downstream. Early/mid features often reusable, nhưng lĩnh vực (domain / 도메인) gap như natural images → medical images có thể lớn.

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

Hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) often combine ideas từ cả hai.

## Mô hình tư duy (mental model / 사고 모델)

> **CNN không “hiểu ảnh” vì convolution magic; nó giới hạn hypothesis không gian (space / 공간) theo giả định rằng cục bộ (local / 로컬) spatial patterns và repeated detectors là useful.**

Inductive độ lệch (bias / 편향) phù hợp giúp học tập (learning / 학습) efficient.

## Dùng chung (common / 공통) Misconceptions

### “Convolution tự tạo translation invariance hoàn toàn”

Convolution chủ yếu equivariant; padding, stride, pooling và dữ liệu (data / 데이터) augmentation ảnh hưởng invariance.

### “Deeper luôn tốt hơn”

Tối ưu hóa (optimization / 최적화), resolution, compute và tác vụ (task / 작업) determine useful độ sâu (depth / 깊이).

### “CNN đã obsolete vì ViT”

CNN vẫn strong/efficient trong nhiều edge, detection và specialized vision workloads.

## Liên kết kiến thức (knowledge connection / 지식 연결)

CNN là concrete example của [Inductive Bias](../04_machine_learning/01_learning_problem_and_inductive_bias.md) và [Representation Learning](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Image Classification](./04_image_classification.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 images as data](./00_images_as_data.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
