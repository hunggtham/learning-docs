# Convolutional Neural Networks cho Vision

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Convolutional neural networks cho vision**. Route đi từ receptive fields → convolution/weight sharing → pooling/stride → hierarchical features → classification/detection heads, để CNN giải thích được cả inductive bias lẫn chi phí tính toán.

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

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, **Weight Sharing** tiếp nhận điểm tựa từ **Convolution tầng (layer / 계층)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Translation Equivariance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weight Sharing

Cùng kernel được slide qua mọi location. Nếu kernel học vertical edge, nó detect edge ở left hay right bằng same weights.

Đây encode translation-related prior.

> **Chuyển mạch:** Ở chặng này của **Convolutional Neural Networks cho Vision**, **Translation Equivariance** tiếp nhận điểm tựa từ **Weight Sharing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Receptive trường dữ liệu (field / 필드)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Translation Equivariance

Ideal convolution gần equivariant:

\[
f(T_x X)\approx T_x f(X)
\]

Translate đầu vào (input / 입력) → tính năng (feature / 기능) map translate tương ứng.

Classification sau pooling có thể trở nên more bất biến (invariant / 불변식).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Convolutional Neural Networks cho Vision**, **Translation Equivariance** nêu điều cần giải thích; **Receptive trường dữ liệu (field / 필드)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Stride** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Receptive trường dữ liệu (field / 필드)

Neuron tầng (layer / 계층) đầu thấy cục bộ (local / 로컬) patch. ngăn xếp (stack / 스택) layers làm effective receptive trường dữ liệu (field / 필드) grow.

Ví dụ nhiều 3×3 convolutions có thể cover region lớn hơn trong khi thêm nonlinearities.

Receptive trường dữ liệu (field / 필드) quyết định mô hình (model / 모델) nhìn ngữ cảnh (context / 맥락) rộng tới đâu.

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, **Receptive trường dữ liệu (field / 필드)** nêu điều cần giải thích; **Stride** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Padding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Stride

Stride > 1 downsample spatial resolution.

Đầu ra (output / 출력) dimension roughly:

\[
H_{out}=\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1
\]

Downsampling giảm compute nhưng mất spatial detail.

> **Chuyển mạch:** Ở chặng này của **Convolutional Neural Networks cho Vision**, **Padding** tiếp nhận điểm tựa từ **Stride** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pooling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Padding

`same`-style padding giữ resolution tương đối; `valid` giảm kích thước (size / 크기). Border treatment ảnh hưởng features near edges.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Convolutional Neural Networks cho Vision**, **Pooling** tiếp nhận điểm tựa từ **Padding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Channels như Learned tính năng (feature / 기능) Types** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pooling

Max pooling chọn cục bộ (local / 로컬) maximum; average pooling lấy mean.

Pooling giảm resolution và tăng cục bộ (local / 로컬) invariance nhưng có thể discard precise position.

Hiện đại (modern / 현대적) CNN nhiều khi dùng strided convolution thay pooling.

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, **Channels như Learned tính năng (feature / 기능) Types** tiếp nhận điểm tựa từ **Pooling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hierarchical Features** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Channels như Learned tính năng (feature / 기능) Types

Đầu vào (input / 입력) RGB có 3 channels; hidden layers có dozens/hundreds channels. Mỗi channel không necessarily interpretable đơn giản, nhưng có thể encode families of patterns.

> **Chuyển mạch:** Ở chặng này của **Convolutional Neural Networks cho Vision**, **Hierarchical Features** tiếp nhận điểm tựa từ **Channels như Learned tính năng (feature / 기능) Types** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Residual Connections** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hierarchical Features

Một dùng chung (common / 공통) intuition:

```text
pixels
→ edges/color blobs
→ textures/parts
→ object-level patterns
```

Thực tế representations phân tán (distributed / 분산) và nonlinear, nhưng hierarchy giải thích lợi ích độ sâu (depth / 깊이).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Convolutional Neural Networks cho Vision**, **Residual Connections** tiếp nhận điểm tựa từ **Hierarchical Features** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Residual Connections

Deep CNN gặp tối ưu hóa (optimization / 최적화) difficulty. ResNet khối (block / 블록):

\[
y=F(x)+x
\]

cho độ dốc (gradient / 기울기)/biểu diễn (representation / 표현) một định danh (identity / 식별자) đường dẫn (path / 경로). mạng (network / 네트워크) học residual adjustment thay vì reconstruct entire ánh xạ (mapping / 매핑).

Residual liên kết (connection / 연결) sau này là cốt lõi (core / 핵심) Transformer mẫu (pattern / 패턴).

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, **Batch Normalization** tiếp nhận điểm tựa từ **Residual Connections** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Depthwise Separable Convolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch Normalization

CNN historically dùng BatchNorm để stabilize activation statistics và tối ưu hóa (optimization / 최적화). hành vi (behavior / 동작) train/eval khác nhau vì running statistics.

Small batch sizes có thể làm BatchNorm unstable; alternatives GroupNorm/LayerNorm phù hợp contexts khác.

> **Chuyển mạch:** Ở chặng này của **Convolutional Neural Networks cho Vision**, **Depthwise Separable Convolution** tiếp nhận điểm tựa từ **Batch Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **1×1 Convolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Depthwise Separable Convolution

Tiêu chuẩn (standard / 표준) convolution mix spatial + channels cùng lúc. Depthwise separable tách:

1. spatial conv per channel;
2. 1×1 pointwise conv mix channels.

Compute giảm mạnh, popular trong mobile architectures.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Convolutional Neural Networks cho Vision**, **1×1 Convolution** tiếp nhận điểm tựa từ **Depthwise Separable Convolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dilated Convolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 1×1 Convolution

Kernel 1×1 không nhìn neighbors nhưng mix channels tại mỗi position. Nó hoạt động như per-pixel tuyến tính (linear / 선형) projection và dùng để thay đổi (change / 변경) channel dimensions/bottleneck.

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, **Dilated Convolution** tiếp nhận điểm tựa từ **1×1 Convolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Grouped Convolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dilated Convolution

Dilated convolution chèn gaps trong kernel sampling, tăng receptive trường dữ liệu (field / 필드) mà không tăng kernel kích thước (size / 크기)/downsample nhiều. Hữu ích segmentation/audio.

> **Chuyển mạch:** Ở chặng này của **Convolutional Neural Networks cho Vision**, **Grouped Convolution** tiếp nhận điểm tựa từ **Dilated Convolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Toàn cục (global / 전역) Average Pooling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Grouped Convolution

Channels chia groups, giảm compute và tạo structural sparsity. Depthwise là extreme trường hợp (case / 사례) mỗi channel một group.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Convolutional Neural Networks cho Vision**, **Toàn cục (global / 전역) Average Pooling** tiếp nhận điểm tựa từ **Grouped Convolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CNN Compute** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Toàn cục (global / 전역) Average Pooling

Thay flatten + huge dense tầng (layer / 계층), average mỗi channel across spatial positions:

\[
z_c=\frac1{HW}\sum_{i,j}X_{i,j,c}
\]

Giảm parameters và kết nối channel bằng chứng (evidence / 증거) tới classification head.

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, **CNN Compute** tiếp nhận điểm tựa từ **Toàn cục (global / 전역) Average Pooling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Augmentation và CNN độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CNN Compute

Convolution được implement hiệu quả bằng specialized kernels/GEMM. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃), kernel fusion và accelerator libraries ảnh hưởng hiệu năng (performance / 성능) thực tế.

FLOPs không phản ánh hoàn toàn độ trễ (latency / 지연 시간); bộ nhớ (memory / 메모리) bandwidth và hardware utilization cũng quan trọng.

> **Chuyển mạch:** Ở chặng này của **Convolutional Neural Networks cho Vision**, **CNN Compute** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Augmentation và CNN độ lệch (bias / 편향)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Transfer học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Augmentation và CNN độ lệch (bias / 편향)

Crop/flip/color jitter reinforce invariances CNN kiến trúc (architecture / 아키텍처) alone không guarantee.

Kiến trúc (architecture / 아키텍처) prior + augmentation prior + dataset cùng quyết định hành vi (behavior / 동작).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Convolutional Neural Networks cho Vision**, **Dữ liệu (data / 데이터) Augmentation và CNN độ lệch (bias / 편향)** nêu điều cần giải thích; **Transfer học tập (learning / 학습)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **CNN vs Vision Transformer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transfer học tập (learning / 학습)

CNN pretrained trên large dataset có thể fine-tune downstream. Early/mid features often reusable, nhưng lĩnh vực (domain / 도메인) gap như natural images → medical images có thể lớn.

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, **CNN vs Vision Transformer** tiếp nhận điểm tựa từ **Transfer học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Convolutional Neural Networks cho Vision**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **CNN vs Vision Transformer** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **CNN không “hiểu ảnh” vì convolution magic; nó giới hạn hypothesis không gian (space / 공간) theo giả định rằng cục bộ (local / 로컬) spatial patterns và repeated detectors là useful.**

Inductive độ lệch (bias / 편향) phù hợp giúp học tập (learning / 학습) efficient.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Convolutional Neural Networks cho Vision**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Convolution tự tạo translation invariance hoàn toàn”

Convolution chủ yếu equivariant; padding, stride, pooling và dữ liệu (data / 데이터) augmentation ảnh hưởng invariance.

### “Deeper luôn tốt hơn”

Tối ưu hóa (optimization / 최적화), resolution, compute và tác vụ (task / 작업) determine useful độ sâu (depth / 깊이).

### “CNN đã obsolete vì ViT”

CNN vẫn strong/efficient trong nhiều edge, detection và specialized vision workloads.

> **Chuyển mạch:** Trong **Convolutional Neural Networks cho Vision**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

CNN là concrete example của [Inductive Bias](../04_machine_learning/01_learning_problem_and_inductive_bias.md) và [Representation Learning](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Image Classification](./04_image_classification.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
