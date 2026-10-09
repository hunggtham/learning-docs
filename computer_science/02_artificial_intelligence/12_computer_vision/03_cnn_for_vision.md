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

Convolution xử lý một vùng cục bộ, còn **Weight Sharing** khiến cùng một bộ lọc có thể tìm mẫu đó ở mọi vị trí. Hệ quả tự nhiên của cách dùng chung trọng số là **Translation Equivariance**.

## Weight Sharing

Cùng kernel được slide qua mọi location. Nếu kernel học vertical edge, nó detect edge ở left hay right bằng same weights.

Đây encode translation-related prior.

Weight sharing giải thích vì sao một detector được tái sử dụng, còn **Translation Equivariance** mô tả cách feature map dịch theo đầu vào. Phạm vi mà detector có thể nhìn thấy được quyết định bởi **Receptive trường dữ liệu (field / 필드)**.

## Translation Equivariance

Ideal convolution gần equivariant:

\[
f(T_x X)\approx T_x f(X)
\]

Translate đầu vào (input / 입력) → tính năng (feature / 기능) map translate tương ứng.

Classification sau pooling có thể trở nên more bất biến (invariant / 불변식).

Equivariance giữ tương ứng vị trí, nhưng không nói mô hình nhìn được bao nhiêu ngữ cảnh. Receptive field trả lời câu hỏi đó; **Stride** tiếp tục quyết định ngữ cảnh được đổi lấy bao nhiêu độ phân giải.

## Receptive trường dữ liệu (field / 필드)

Neuron tầng (layer / 계층) đầu thấy cục bộ (local / 로컬) patch. ngăn xếp (stack / 스택) layers làm effective receptive trường dữ liệu (field / 필드) grow.

Ví dụ nhiều 3×3 convolutions có thể cover region lớn hơn trong khi thêm nonlinearities.

Receptive trường dữ liệu (field / 필드) quyết định mô hình (model / 모델) nhìn ngữ cảnh (context / 맥락) rộng tới đâu.

Receptive field lớn giúp gom ngữ cảnh, còn stride lớn làm giảm số vị trí cần xử lý. Khi thay đổi kích thước feature map, **Padding** quyết định cách vùng biên được giữ lại.

## Stride

Stride > 1 downsample spatial resolution.

Đầu ra (output / 출력) dimension roughly:

\[
H_{out}=\left\lfloor\frac{H+2P-K}{S}\right\rfloor+1
\]

Downsampling giảm compute nhưng mất spatial detail.

Stride kiểm soát bước di chuyển của kernel, còn padding kiểm soát những gì xảy ra ở biên. Sau hai lựa chọn đó, **Pooling** là một cách khác để giảm kích thước không gian và tạo bất biến cục bộ.

## Padding

`same`-style padding giữ resolution tương đối; `valid` giảm kích thước (size / 크기). Border treatment ảnh hưởng features near edges.

Pooling giảm độ phân giải và có thể làm mất vị trí chính xác; đổi lại, nó giúp mô hình bớt nhạy với dịch chuyển nhỏ. Khi không gian đã được nén, các **Channels như Learned tính năng (feature / 기능) Types** sẽ mang những mẫu đã học.

## Pooling

Max pooling chọn cục bộ (local / 로컬) maximum; average pooling lấy mean.

Pooling giảm resolution và tăng cục bộ (local / 로컬) invariance nhưng có thể discard precise position.

Hiện đại (modern / 현대적) CNN nhiều khi dùng strided convolution thay pooling.

Mỗi channel ẩn có thể phản hồi với một họ mẫu, dù không phải lúc nào cũng diễn giải được riêng lẻ. Các channel qua nhiều tầng kết hợp thành **Hierarchical Features**.

## Channels như Learned tính năng (feature / 기능) Types

Đầu vào (input / 입력) RGB có 3 channels; hidden layers có dozens/hundreds channels. Mỗi channel không necessarily interpretable đơn giản, nhưng có thể encode families of patterns.

Hierarchy mô tả cách các mẫu cục bộ được ghép thành cấu trúc lớn hơn, nhưng mạng sâu khó tối ưu khi đường truyền dài. **Residual Connections** giải quyết một phần khó khăn đó bằng cách cung cấp đường tắt cho biểu diễn và gradient.

## Hierarchical Features

Một dùng chung (common / 공통) intuition:

```text
pixels
→ edges/color blobs
→ textures/parts
→ object-level patterns
```

Thực tế representations phân tán (distributed / 분산) và nonlinear, nhưng hierarchy giải thích lợi ích độ sâu (depth / 깊이).

Residual block để mạng học phần điều chỉnh so với identity, thay vì phải tái tạo toàn bộ ánh xạ. Trong quá trình huấn luyện sâu, **Batch Normalization** là một kỹ thuật khác giúp kiểm soát thống kê activation.

## Residual Connections

Deep CNN gặp tối ưu hóa (optimization / 최적화) difficulty. ResNet khối (block / 블록):

\[
y=F(x)+x
\]

cho độ dốc (gradient / 기울기)/biểu diễn (representation / 표현) một định danh (identity / 식별자) đường dẫn (path / 경로). mạng (network / 네트워크) học residual adjustment thay vì reconstruct entire ánh xạ (mapping / 매핑).

Residual liên kết (connection / 연결) sau này là cốt lõi (core / 핵심) Transformer mẫu (pattern / 패턴).

BatchNorm có thể ổn định tối ưu hóa nhưng phụ thuộc vào kích thước batch và chế độ train/eval. Khi mục tiêu chuyển sang giảm chi phí phép tính, **Depthwise Separable Convolution** tách phép trộn không gian khỏi phép trộn kênh.

## Batch Normalization

CNN historically dùng BatchNorm để stabilize activation statistics và tối ưu hóa (optimization / 최적화). hành vi (behavior / 동작) train/eval khác nhau vì running statistics.

Small batch sizes có thể làm BatchNorm unstable; alternatives GroupNorm/LayerNorm phù hợp contexts khác.

Depthwise convolution giảm phép tính bằng cách xử lý từng kênh riêng, rồi pointwise convolution trộn các kênh lại. Chính phép trộn theo vị trí này là vai trò của **1×1 Convolution**.

## Depthwise Separable Convolution

Tiêu chuẩn (standard / 표준) convolution mix spatial + channels cùng lúc. Depthwise separable tách:

1. spatial conv per channel;
2. 1×1 pointwise conv mix channels.

Compute giảm mạnh, popular trong mobile architectures.

Kernel 1×1 không mở rộng vùng lân cận, nhưng có thể đổi số kênh và tạo bottleneck hiệu quả. Ngược lại, **Dilated Convolution** mở rộng vùng nhìn mà không cần tăng kernel dày hoặc downsample quá sớm.

## 1×1 Convolution

Kernel 1×1 không nhìn neighbors nhưng mix channels tại mỗi position. Nó hoạt động như per-pixel tuyến tính (linear / 선형) projection và dùng để thay đổi (change / 변경) channel dimensions/bottleneck.

Dilated convolution thưa hóa các vị trí lấy mẫu để tăng receptive field, đặc biệt hữu ích khi cần giữ độ phân giải. **Grouped Convolution** dùng một ý tưởng khác: chia các kênh thành nhóm để giảm phép trộn.

## Dilated Convolution

Dilated convolution chèn gaps trong kernel sampling, tăng receptive trường dữ liệu (field / 필드) mà không tăng kernel kích thước (size / 크기)/downsample nhiều. Hữu ích segmentation/audio.

Grouped convolution tạo sparsity có cấu trúc; depthwise convolution là trường hợp cực hạn khi mỗi kênh thành một nhóm. Ở đầu ra, **Toàn cục (global / 전역) Average Pooling** có thể tóm tắt mỗi kênh trên toàn không gian.

## Grouped Convolution

Channels chia groups, giảm compute và tạo structural sparsity. Depthwise là extreme trường hợp (case / 사례) mỗi channel một group.

Global average pooling thay flatten và dense layer lớn bằng một thống kê gọn cho từng kênh. Thiết kế gọn đó vẫn phải được đánh giá bằng **CNN Compute**, vì FLOPs không tự nói lên độ trễ thực tế.

## Toàn cục (global / 전역) Average Pooling

Thay flatten + huge dense tầng (layer / 계층), average mỗi channel across spatial positions:

\[
z_c=\frac1{HW}\sum_{i,j}X_{i,j,c}
\]

Giảm parameters và kết nối channel bằng chứng (evidence / 증거) tới classification head.

Global pooling giảm tham số, còn hiệu năng toàn hệ thống phụ thuộc cả memory bandwidth và hardware utilization. Ngoài kiến trúc, **Dữ liệu (data / 데이터) Augmentation và CNN độ lệch (bias / 편향)** cũng định hình hành vi mà mô hình học được.

## CNN Compute

Convolution được implement hiệu quả bằng specialized kernels/GEMM. bộ nhớ (memory / 메모리) bố cục (layout / 레이아웃), kernel fusion và accelerator libraries ảnh hưởng hiệu năng (performance / 성능) thực tế.

FLOPs không phản ánh hoàn toàn độ trễ (latency / 지연 시간); bộ nhớ (memory / 메모리) bandwidth và hardware utilization cũng quan trọng.

Độ trễ và chi phí tính toán là một phần của thiết kế, nhưng augmentation và dataset mới quyết định nhiều biến thiên nào được coi là hợp lệ. Khi dữ liệu gốc hạn chế, **Transfer học tập (learning / 학습)** cho phép tận dụng biểu diễn đã được huấn luyện.

## Dữ liệu (data / 데이터) Augmentation và CNN độ lệch (bias / 편향)

Crop/flip/color jitter reinforce invariances CNN kiến trúc (architecture / 아키텍처) alone không guarantee.

Kiến trúc (architecture / 아키텍처) prior + augmentation prior + dataset cùng quyết định hành vi (behavior / 동작).

Augmentation bổ sung prior cho kiến trúc, còn transfer learning bổ sung prior từ dữ liệu lớn. Đặt CNN cạnh **CNN vs Vision Transformer** sẽ làm rõ trade-off giữa locality, data efficiency và global interaction.

## Transfer học tập (learning / 학습)

CNN pretrained trên large dataset có thể fine-tune downstream. Early/mid features often reusable, nhưng lĩnh vực (domain / 도메인) gap như natural images → medical images có thể lớn.

Transfer learning giúp cả CNN và ViT khai thác pretraining, nhưng inductive bias của hai kiến trúc khác nhau. **Mô hình tư duy (mental model / 사고 모델)** dưới đây tóm tắt điều CNN giả định và điều nó không đảm bảo.

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

So sánh CNN và ViT cho thấy không có kiến trúc nào tự động thắng trong mọi bối cảnh; hiệu quả phụ thuộc prior, dữ liệu và phần cứng. Hãy dùng các **Dùng chung (common / 공통) Misconceptions** sau để kiểm tra trực giác đó.

## Mô hình tư duy (mental model / 사고 모델)

> **CNN không “hiểu ảnh” vì convolution magic; nó giới hạn hypothesis không gian (space / 공간) theo giả định rằng cục bộ (local / 로컬) spatial patterns và repeated detectors là useful.**

Inductive độ lệch (bias / 편향) phù hợp giúp học tập (learning / 학습) efficient.

Các ngộ nhận này đều nhắc rằng convolution tạo ra một inductive bias hữu ích chứ không thay thế việc chọn stride, dữ liệu và mục tiêu. **Liên kết kiến thức (knowledge connection / 지식 연결)** đặt CNN vào mạch học rộng hơn.

## Dùng chung (common / 공통) Misconceptions

### “Convolution tự tạo translation invariance hoàn toàn”

Convolution chủ yếu equivariant; padding, stride, pooling và dữ liệu (data / 데이터) augmentation ảnh hưởng invariance.

### “Deeper luôn tốt hơn”

Tối ưu hóa (optimization / 최적화), resolution, compute và tác vụ (task / 작업) determine useful độ sâu (depth / 깊이).

### “CNN đã obsolete vì ViT”

CNN vẫn strong/efficient trong nhiều edge, detection và specialized vision workloads.

Từ đây, hãy quay lại các khái niệm inductive bias và representation learning khi cần đào sâu. Ranh giới cần giữ là: CNN khai thác locality và weight sharing để học hiệu quả, nhưng hành vi cuối cùng vẫn do kiến trúc, dữ liệu và điều kiện triển khai cùng quyết định.

## Liên kết kiến thức (knowledge connection / 지식 연결)

CNN là concrete example của [Inductive Bias](../04_machine_learning/01_learning_problem_and_inductive_bias.md) và [Representation Learning](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Image Classification](./04_image_classification.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
