# Feature Representation trong Computer Vision

Trước khi deep neural network trở thành lựa chọn mặc định, Computer Vision thường tách pipeline thành hai phần:

```text
image → hand-designed feature → classifier
```

**Biểu diễn đặc trưng (feature representation / 특징 표현)** là cách biến raw pixel thành descriptor giữ lại information quan trọng cho task đồng thời loại bớt variation không cần thiết.

## Vì sao Raw Pixel khó dùng trực tiếp?

Hai ảnh của cùng một object có thể khác rất mạnh trong pixel space chỉ vì:

- translation;
- scale;
- rotation;
- lighting;
- viewpoint;
- background;
- occlusion.

Một representation hữu ích cần ổn định hơn trước các **nuisance variation** nhưng vẫn nhạy với semantic difference thật sự.

## Local Feature

Classical vision thường tìm interest point rồi mô tả local neighborhood quanh điểm đó.

Ví dụ **SIFT (Scale-Invariant Feature Transform)** tìm keypoint qua nhiều scale, ước lượng orientation rồi tạo descriptor từ local gradient histogram.

Mental model:

```text
tìm local point có thể lặp lại ổn định
→ chuẩn hóa scale và orientation
→ mô tả local edge pattern
```

Nhờ vậy SIFT ổn định hơn raw patch matching khi object bị scale hoặc rotate.

## HOG

**Histogram of Oriented Gradients (HOG)** chia image thành cell, tính gradient orientation rồi aggregate thành histogram.

Shape của object thường được encode tốt hơn bằng hướng edge so với absolute pixel intensity.

HOG từng rất hiệu quả cho pedestrian detection khi kết hợp với linear SVM.

## Bag of Visual Words

Local descriptor có số lượng thay đổi theo image. **Bag of Visual Words** cluster descriptor thành một visual vocabulary, sau đó biểu diễn mỗi image bằng histogram tần suất của các “visual word”.

Có thể liên hệ với NLP bag-of-words:

```text
local patch descriptor
→ visual token
→ frequency vector
```

Nhược điểm lớn là spatial layout bị mất phần lớn.

## Invariance và Equivariance

Một representation **invariant** gần như không đổi khi input chịu transformation:

\[
f(Tx)\approx f(x)
\]

Một representation **equivariant** thay đổi theo cách có thể dự đoán:

\[
f(Tx)=T'f(x)
\]

Classification thường muốn invariance với translation nhỏ. Detection và segmentation lại cần giữ spatial correspondence, nên equivariance thường quan trọng hơn pure invariance.

## Feature Pyramid

Object có thể xuất hiện ở nhiều scale khác nhau. Classical system dùng image pyramid hoặc feature pyramid để detect object ở nhiều resolution.

Modern CNN tiếp tục ý tưởng này bằng **Feature Pyramid Network (FPN)**, nơi representation ở nhiều spatial resolution được kết hợp.

## Dimensionality Reduction

Descriptor high-dimensional có thể được compress bằng PCA.

PCA giữ direction có variance lớn nhất nhưng không bảo đảm direction đó là semantic feature quan trọng nhất cho downstream task.

Whitening có thể decorrelate dimension, nhưng cũng có thể amplify low-variance noise.

## Metric Learning

Nếu representation dùng cho matching hoặc retrieval, ta muốn entity liên quan nằm gần nhau và entity khác nằm xa nhau.

Contrastive hoặc triplet objective theo trực giác:

```text
anchor-positive distance ↓
anchor-negative distance ↑
```

Face recognition và image retrieval hiện đại phụ thuộc mạnh vào learned metric embedding.

## Hand-Designed và Learned Feature

Hand-designed feature encode prior từ kiến thức con người, ví dụ:

```text
edge quan trọng
local gradient quan trọng
scale/orientation normalization hữu ích
```

Deep Learning thay vào đó học feature hierarchy từ data:

```text
pixel
→ edge / texture
→ part-level pattern
→ object / semantic pattern
```

Không nên hiểu hierarchy này như một mapping cứng theo layer, nhưng nó là mental model hữu ích.

## Transfer Learning

Một pretrained visual backbone có thể tạo representation dùng chung cho nhiều task.

Downstream task có thể:

- freeze backbone và chỉ train head;
- fine-tune toàn bộ network;
- dùng adapter hoặc parameter-efficient tuning.

Representation càng tốt thì downstream task thường cần càng ít labeled data hơn.

## Self-Supervised Visual Representation

Annotation image rất đắt. Self-supervised method học từ augmentation, masking hoặc relation giữa các view của cùng image.

Contrastive idea:

```text
hai view của cùng image → embedding nên gần nhau
view của image khác     → embedding nên xa hơn
```

Masked image modeling lại che patch rồi yêu cầu model reconstruct hoặc predict representation của phần bị che.

## CLIP-Style Representation

Image encoder và text encoder có thể được train để image-text pair đúng nằm gần nhau trong shared embedding space.

Điều này cho phép zero-shot classification hoặc retrieval:

```text
image embedding
so với
text embedding của candidate label
```

Đây là cầu trực tiếp từ Computer Vision sang Multimodal AI.

## Representation Collapse

Self-supervised objective có nguy cơ model output cùng một vector cho mọi input — hiện tượng **representation collapse**.

Các method khác nhau dùng negative sample, predictor, stop-gradient hoặc variance/covariance constraint để tránh trivial solution này.

## Feature Quality phụ thuộc Task

Embedding tốt cho semantic image retrieval chưa chắc tốt cho fine-grained defect inspection.

“Good representation” luôn phải được hiểu tương đối với downstream objective và loại variation cần giữ hoặc bỏ.

## Linear Probe

Một cách đơn giản để đánh giá representation là freeze encoder rồi train linear classifier trên top.

Nếu linear head đạt kết quả tốt, class structure đã tương đối linearly separable trong learned feature space.

## Visualization

t-SNE hoặc UMAP có thể project high-dimensional feature xuống 2D để inspect.

Nhưng projection làm méo geometry. Cluster nhìn đẹp trong 2D không phải bằng chứng đủ rằng representation tốt cho task thực tế.

## Cẩn trọng với Explainability

Activation map, nearest neighbor hoặc feature visualization giúp inspect model, nhưng không cung cấp complete causal explanation cho quyết định của network.

## Mô hình tư duy

> **Feature representation là một coordinate system mới nơi những distinction quan trọng cho task trở nên dễ xử lý hơn.**

Deep Learning mạnh vì nó học coordinate system cùng với objective thay vì cố định feature từ trước.

## Những nhầm lẫn thường gặp

### “Learned feature luôn tốt hơn hand-crafted feature”

Không. Khi data ít hoặc domain physics rõ, hand-crafted feature có thể rất hiệu quả và dễ kiểm soát.

### “Embedding distance là semantic truth”

Không. Distance phản ánh training objective và data distribution.

### “Invariance càng nhiều càng tốt”

Không. Nếu một transformation làm đổi label, ép invariance sẽ làm mất information cần thiết.

## Liên kết kiến thức

Feature representation nối [Representation Learning](../05_neural_networks/08_representation_learning.md), dimensionality reduction và metric learning. CNN đưa locality và translation bias trực tiếp vào quá trình representation learning.

Xem tiếp: [CNN trong Computer Vision](./03_cnn_for_vision.md).