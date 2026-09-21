# Feature Representation trong Computer Vision

Trước khi deep neural networks trở thành default, Computer Vision thường tách pipeline thành hai phần:

```text
image → hand-designed features → classifier
```

**Feature representation (특징 표현 / biểu diễn đặc trưng)** là cách biến raw pixels thành descriptors giữ information quan trọng cho task đồng thời bỏ bớt variation không cần thiết.

## Tại sao raw pixels khó?

Hai ảnh cùng một object có thể khác mạnh ở pixel space vì:

- translation;
- scale;
- rotation;
- lighting;
- viewpoint;
- background;
- occlusion.

Một useful representation cần stable hơn với nuisance variation nhưng vẫn sensitive với semantic differences.

## Local Features

Classical vision thường detect interest points rồi mô tả local neighborhood.

Ví dụ **SIFT (Scale-Invariant Feature Transform)** tìm keypoints qua scale space, estimate orientation rồi tạo descriptor từ local gradient histograms.

Mental idea:

```text
find repeatable local points
→ normalize scale/orientation
→ describe local edge pattern
```

SIFT robust hơn raw patch matching dưới scale/rotation changes.

## HOG

**Histogram of Oriented Gradients (HOG)** chia image thành cells, tính gradient orientations rồi aggregate histograms.

Object shape thường được encode tốt bởi edge directions hơn absolute pixel intensity.

HOG từng rất effective cho pedestrian detection khi kết hợp linear SVM.

## Bag of Visual Words

Local descriptors có variable count. Bag-of-visual-words cluster descriptors thành visual vocabulary, rồi represent image bằng histogram of “visual words”.

Analogy với NLP bag-of-words:

```text
local patch descriptors → visual tokens → frequency vector
```

Nhược điểm: mất phần lớn spatial layout.

## Feature Invariance vs Equivariance

**Invariant** representation giữ gần như giống nhau khi input transform:

\[
f(Tx)\approx f(x)
\]

**Equivariant** representation transform predictable:

\[
f(Tx)=T'f(x)
\]

Classification thường muốn invariance với translation nhỏ. Detection/segmentation cần giữ spatial correspondence, nên equivariance quan trọng hơn pure invariance.

## Feature Pyramid

Objects có nhiều scales. Classical systems dùng image pyramids hoặc feature pyramids để detect object ở multiple resolutions.

Modern Feature Pyramid Networks giữ multi-scale feature maps trong CNN.

## Dimensionality Reduction

Descriptors high-dimensional có thể compress bằng PCA. PCA giữ directions of largest variance nhưng không guarantee semantic importance.

Whitening có thể decorrelate dimensions nhưng đôi khi amplify low-variance noise.

## Metric Learning

Nếu representation dùng cho retrieval/matching, ta muốn similar entities close và dissimilar far.

Contrastive/triplet objectives:

```text
anchor-positive distance ↓
anchor-negative distance ↑
```

Modern face recognition và image retrieval dựa heavily vào learned metric embeddings.

## Hand-Designed vs Learned Features

Hand-designed features encode strong prior từ human knowledge:

```text
edges matter
local gradients matter
scale/orientation normalization useful
```

Deep learning học hierarchy từ data:

```text
pixels
→ edges/textures
→ parts
→ objects/semantic patterns
```

Không nên hiểu hierarchy này quá literal, nhưng nó là mental model hữu ích.

## Transfer Learning

A pretrained visual backbone produces generic representations. Downstream task có thể:

- freeze backbone + train head;
- fine-tune all layers;
- use adapters/parameter-efficient tuning.

Representation quality quyết định sample efficiency downstream.

## Self-Supervised Visual Representation

Labels expensive. Self-supervised methods học từ image augmentations/masking.

Contrastive idea:

```text
two views of same image → embeddings should align
views of different images → separated
```

Masked image modeling reconstruct/predict missing patches/features.

## CLIP-Style Representation

Image encoder và text encoder được train để aligned image-text pairs close trong shared embedding space.

Điều này tạo powerful zero-shot classification/retrieval:

```text
image embedding
vs
text embeddings of candidate labels
```

Đây là bridge trực tiếp sang multimodal AI.

## Representation Collapse

Self-supervised objectives có risk model output same vector cho everything. Methods cần negatives, predictors, stop-gradient hoặc variance/covariance constraints để tránh trivial solution.

## Feature Quality is Task-Dependent

Embedding tốt cho semantic retrieval chưa chắc tốt cho fine-grained defect inspection. “Good representation” luôn relative to downstream structure.

## Linear Probe

Một cách test representation: freeze encoder, train linear classifier. Nếu simple linear head đạt tốt, semantic classes đã tương đối linearly separable trong feature space.

## Visualization

t-SNE/UMAP có thể visualize high-dimensional features nhưng 2D plots distort global geometry; không nên dùng cluster đẹp làm proof chất lượng.

## Explainability Caution

Activation map/nearest neighbors giúp inspect representation nhưng không cho complete causal explanation model decision.

## Mental Model

> **Feature representation là coordinate system mới nơi distinctions quan trọng của task trở nên dễ xử lý hơn.**

Deep learning mạnh vì nó học coordinate system cùng objective thay vì chỉ dùng features cố định.

## Common Misconceptions

### “Learned features luôn tốt hơn hand-crafted”

Không nếu data nhỏ, constraints rõ hoặc feature engineering encode domain physics mạnh.

### “Embedding distance = semantic truth”

Distance phản ánh training objective và data, không universal semantics.

### “Invariance càng nhiều càng tốt”

Nếu transformation đổi label, invariance gây mất information.

## Knowledge Connection

Feature representation nối [Representation Learning](../05_neural_networks/08_representation_learning.md), dimensionality reduction và metric learning. CNN là architecture đưa locality/translation bias trực tiếp vào representation learning.

Xem tiếp: [CNN for Vision](./03_cnn_for_vision.md).