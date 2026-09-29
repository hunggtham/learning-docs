# Convolutional Neural Networks: tận dụng cấu trúc không gian

> **Mạch đọc:** Đặt **Convolutional Neural Networks: tận dụng cấu trúc không gian** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vì sao flatten ảnh (image / 이미지) vào MLP là lãng phí?** sang **Convolution thao tác (operation / 연산)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Convolutional Neural mạng (network / 네트워크) được tạo ra vì dense MLP đối xử mọi đầu vào (input / 입력) dimension như độc lập, trong khi ảnh (image / 이미지) có cấu trúc (structure / 구조) rất mạnh: pixels gần nhau tạo cục bộ (local / 로컬) patterns, cùng một edge có thể xuất hiện ở nhiều vị trí, và spatial hierarchy từ edge → texture → part → đối tượng (object / 객체) có tính compositional.

CNN encode hai inductive biases chính: **cục bộ (local / 로컬) connectivity** và **weight sharing**.

## Vì sao flatten ảnh (image / 이미지) vào MLP là lãng phí?

Ảnh (image / 이미지) RGB `224×224×3` có 150,528 values. Dense tầng (layer / 계층) 4096 units cần hơn 600 triệu weights chỉ tầng (layer / 계층) đầu.

Quan trọng hơn, flatten bỏ tường minh (explicit / 명시적) locality. điểm ảnh (pixel / 픽셀) ở `(10,10)` và `(10,11)` vốn neighboring nhưng véc-tơ (vector / 벡터) chỉ mục (index / 인덱스) không cho MLP biết quan hệ (relation / 관계) đặc biệt đó.

CNN giữ spatial grid và dùng cục bộ (local / 로컬) kernels.

## Convolution thao tác (operation / 연산)

Một 2D kernel nhỏ, ví dụ `3×3`, trượt qua ảnh (image / 이미지). Với single channel:

\[
y_{i,j}=\sum_{u,v}K_{u,v}x_{i+u,j+v}
\]

Deep-learning frameworks thường implement cross-correlation (không flip kernel) nhưng vẫn gọi convolution.

Multi-channel đầu vào (input / 입력):

\[
W\in R^{C_{out}\times C_{in}\times K_h\times K_w}
\]

mỗi đầu ra (output / 출력) channel combine cục bộ (local / 로컬) patch across all đầu vào (input / 입력) channels.

## Weight Sharing

Cùng kernel weights được reuse mọi spatial location. Nếu kernel học vertical edge, nó detect edge ở nhiều vị trí.

Parameter count không phụ thuộc ảnh (image / 이미지) width/height trực tiếp:

\[
C_{out}(C_{in}K_hK_w+1)
\]

Đây là huge efficiency gain so dense liên kết (connection / 연결).

## Translation Equivariance

Nếu đầu vào (input / 입력) shift, convolution tính năng (feature / 기능) map cũng shift tương ứng (ignoring boundaries/stride effects). Đây là **equivariance**, không phải chính xác (exact / 정확한) invariance.

Pooling/toàn cục (global / 전역) aggregation có thể tạo more bất biến (invariant / 불변식) final prediction.

## Stride, Padding, Dilation

Đầu ra (output / 출력) kích thước (size / 크기) 1D:

\[
O=\left\lfloor\frac{N+2P-D(K-1)-1}{S}+1\right\rfloor
\]

`S` stride, `P` padding, `D` dilation.

- stride >1 downsample;
- padding giữ spatial kích thước (size / 크기)/điều khiển (control / 제어) border;
- dilation mở receptive trường dữ liệu (field / 필드) mà không tăng kernel parameters nhiều.

## Receptive trường dữ liệu (field / 필드)

Đơn vị (unit / 단위) ở deep tầng (layer / 계층) phụ thuộc một region của original ảnh (image / 이미지). ngăn xếp (stack / 스택) `3×3` convolutions làm receptive trường dữ liệu (field / 필드) tăng.

Early layers cục bộ (local / 로컬); deeper units integrate larger ngữ cảnh (context / 맥락).

**Effective receptive trường dữ liệu (field / 필드)** có thể nhỏ hơn theoretical vì contribution phân phối (distribution / 분포) không uniform.

## Pooling

Max pooling:

\[
y_{i,j}=\max_{(u,v)\in cửa sổ (window / 윈도우)}x_{i+u,j+v}
\]

Average pooling lấy mean.

Pooling giảm resolution, tăng effective receptive trường dữ liệu (field / 필드) và tạo cục bộ (local / 로컬) invariance. hiện đại (modern / 현대적) CNN đôi khi dùng strided convolution thay pooling.

Toàn cục (global / 전역) Average Pooling average toàn spatial map per channel, giảm dense-head parameters.

## Hierarchical Features

Một classic interpretation:

```text
pixels
→ edges/orientations
→ textures/simple shapes
→ parts
→ object-level features
```

Không phải mọi channel cleanly map concept, nhưng hierarchy intuition hữu ích vì receptive trường dữ liệu (field / 필드) và composition tăng qua độ sâu (depth / 깊이).

## ResNet và Skip Connections

Very deep CNN khó optimize. ResNet khối (block / 블록):

\[
y=x+F(x)
\]

cho định danh (identity / 식별자) đường dẫn (path / 경로) và easier độ dốc (gradient / 기울기) luồng (flow / 흐름).

Thay vì mỗi khối (block / 블록) phải learn full ánh xạ (mapping / 매핑), nó learn residual correction `F(x)`.

Residual kiến trúc (architecture / 아키텍처) trở thành principle chung và xuất hiện mạnh trong Transformers.

## 1×1 Convolution

Kernel `1×1` không mix neighbors spatially nhưng mix channels:

\[
y_{i,j}=W x_{i,j}
\]

Nó là per-location tuyến tính (linear / 선형) projection, useful để thay đổi (change / 변경) channel dimension/bottleneck.

## Depthwise Separable Convolution

Tiêu chuẩn (standard / 표준) conv mixes spatial + channel jointly. Depthwise separable conv tách:

1. depthwise spatial conv per channel;
2. pointwise `1×1` conv mix channels.

Compute giảm mạnh, used in MobileNet-like architectures.

## BatchNorm và CNN huấn luyện (training / 학습)

CNN historically dùng Conv → BatchNorm → ReLU patterns. hiện đại (modern / 현대적) variants thay thứ tự (ordering / 순서)/norm/activation.

BatchNorm works well with sufficiently large ảnh (image / 이미지) batches; small-batch detection/segmentation may prefer GroupNorm.

## CNN for more than Images

1D convolution: audio/thời gian (time / 시간) series/văn bản (text / 텍스트) cục bộ (local / 로컬) patterns.

3D convolution: video/medical volumes.

Đồ thị (graph / 그래프) convolutions generalize neighborhood aggregation on non-grid structures nhưng mathematical thao tác (operation / 연산) khác grid convolution.

## Classification, Detection, Segmentation

Ảnh (image / 이미지) classification đầu ra (output / 출력) one/few labels.

Đối tượng (object / 객체) detection cần bounding boxes + classes.

Segmentation prediction per điểm ảnh (pixel / 픽셀).

Same CNN backbone can feed different heads. tác vụ (task / 작업) đầu ra (output / 출력) cấu trúc (structure / 구조) quyết định kiến trúc (architecture / 아키텍처) beyond tính năng (feature / 기능) extractor.

## CNN vs Vision Transformer

CNN hardcodes locality/translation sharing. Vision Transformer splits ảnh (image / 이미지) into patches và learn toàn cục (global / 전역) interactions through attention.

CNN often data-efficient due strong inductive độ lệch (bias / 편향); ViT scales extremely well with large pretraining. hiện đại (modern / 현대적) vision các hệ thống (systems / 시스템들) frequently hybrid or use convolution-like cục bộ (local / 로컬) biases inside transformers.

Không có simple “Transformer replaced CNN” quy tắc (rule / 규칙).

## Mô hình tư duy (mental model / 사고 모델)

> CNN says: cục bộ (local / 로컬) mẫu (pattern / 패턴) matters, same kind of mẫu (pattern / 패턴) can occur anywhere, and complex visual concepts can be composed hierarchically from cục bộ (local / 로컬) features.

## Dùng chung (common / 공통) Misconceptions

### “Convolution automatically makes mô hình (model / 모델) translation bất biến (invariant / 불변식)”

Convolution is mainly equivariant. Pooling/aggregation/huấn luyện (training / 학습) augmentation contribute invariance.

### “CNN kernel is hand-designed edge filter”

Classical vision used hand filters; CNN kernels are learned end-to-end.

### “Deep tầng (layer / 계층) neuron always represents đối tượng (object / 객체) part”

Biểu diễn (representation / 표현) phân tán (distributed / 분산); conceptual hierarchy is approximate mô hình tư duy (mental model / 사고 모델).

### “CNN obsolete after Vision Transformer”

CNN remains strong, efficient and widely deployed; architectures converge/hybridize.

## Liên kết kiến thức (knowledge connection / 지식 연결)

CNN applies [Representation Learning](../05_neural_networks/08_representation_learning.md), [Weight Sharing/Regularization](../05_neural_networks/07_regularization.md) and [Residual Connections](../05_neural_networks/04_backpropagation.md).

Computer Vision lĩnh vực (domain / 도메인) later expands detection, segmentation and ViT.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 sequence models](./01_sequence_models.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
