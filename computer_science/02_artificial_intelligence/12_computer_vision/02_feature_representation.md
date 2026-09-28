# Tính năng (feature / 기능) biểu diễn (representation / 표현) trong Computer Vision

> **Mạch đọc:** Đặt **tính năng (feature / 기능) biểu diễn (representation / 표현) trong Computer Vision** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Tại sao raw pixels khó?** sang **cục bộ (local / 로컬) Features**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Trước khi deep neural networks trở thành default, Computer Vision thường tách chuỗi xử lý (pipeline / 파이프라인) thành hai phần:

```text
image → hand-designed features → classifier
```

**tính năng (feature / 기능) biểu diễn (representation / 표현)** là cách biến raw pixels thành descriptors giữ thông tin (information / 정보) quan trọng cho tác vụ (task / 작업) đồng thời bỏ bớt variation không cần thiết.

## Tại sao raw pixels khó?

Hai ảnh cùng một đối tượng (object / 객체) có thể khác mạnh ở điểm ảnh (pixel / 픽셀) không gian (space / 공간) vì:

- translation;
- quy mô (scale / 규모);
- rotation;
- lighting;
- viewpoint;
- background;
- occlusion.

Một useful biểu diễn (representation / 표현) cần stable hơn với nuisance variation nhưng vẫn sensitive với ngữ nghĩa (semantic / 의미적) differences.

## Cục bộ (local / 로컬) Features

Classical vision thường detect interest points rồi mô tả cục bộ (local / 로컬) neighborhood.

Ví dụ **SIFT (Scale-Invariant Feature Transform)** tìm keypoints qua quy mô (scale / 규모) không gian (space / 공간), estimate orientation rồi tạo descriptor từ cục bộ (local / 로컬) độ dốc (gradient / 기울기) histograms.

Mental idea:

```text
find repeatable local points
→ normalize scale/orientation
→ describe local edge pattern
```

SIFT robust hơn raw patch matching dưới quy mô (scale / 규모)/rotation changes.

## HOG

**Histogram of Oriented Gradients (HOG)** chia ảnh (image / 이미지) thành cells, tính độ dốc (gradient / 기울기) orientations rồi aggregate histograms.

Đối tượng (object / 객체) shape thường được encode tốt bởi edge directions hơn absolute điểm ảnh (pixel / 픽셀) intensity.

HOG từng rất effective cho pedestrian detection khi kết hợp tuyến tính (linear / 선형) SVM.

## Bag of Visual Words

Cục bộ (local / 로컬) descriptors có variable count. Bag-of-visual-words cluster descriptors thành visual vocabulary, rồi represent ảnh (image / 이미지) bằng histogram of “visual words”.

Analogy với NLP bag-of-words:

```text
local patch descriptors → visual tokens → frequency vector
```

Nhược điểm: mất phần lớn spatial bố cục (layout / 레이아웃).

## Tính năng (feature / 기능) Invariance vs Equivariance

**bất biến (invariant / 불변식)** biểu diễn (representation / 표현) giữ gần như giống nhau khi đầu vào (input / 입력) transform:

\[
f(Tx)\approx f(x)
\]

**Equivariant** biểu diễn (representation / 표현) transform predictable:

\[
f(Tx)=T'f(x)
\]

Classification thường muốn invariance với translation nhỏ. Detection/segmentation cần giữ spatial correspondence, nên equivariance quan trọng hơn pure invariance.

## Tính năng (feature / 기능) Pyramid

Objects có nhiều scales. Classical các hệ thống (systems / 시스템들) dùng ảnh (image / 이미지) pyramids hoặc tính năng (feature / 기능) pyramids để detect đối tượng (object / 객체) ở multiple resolutions.

Hiện đại (modern / 현대적) tính năng (feature / 기능) Pyramid Networks giữ multi-scale tính năng (feature / 기능) maps trong CNN.

## Dimensionality Reduction

Descriptors high-dimensional có thể compress bằng PCA. PCA giữ directions of largest variance nhưng không guarantee ngữ nghĩa (semantic / 의미적) importance.

Whitening có thể decorrelate dimensions nhưng đôi khi amplify low-variance noise.

## Chỉ số (metric / 지표) học tập (learning / 학습)

Nếu biểu diễn (representation / 표현) dùng cho retrieval/matching, ta muốn similar entities close và dissimilar far.

Contrastive/triplet objectives:

```text
anchor-positive distance ↓
anchor-negative distance ↑
```

Hiện đại (modern / 현대적) face recognition và ảnh (image / 이미지) retrieval dựa heavily vào learned chỉ số (metric / 지표) embeddings.

## Hand-Designed vs Learned Features

Hand-designed features encode strong prior từ human kiến thức (knowledge / 지식):

```text
edges matter
local gradients matter
scale/orientation normalization useful
```

Deep học tập (learning / 학습) học hierarchy từ dữ liệu (data / 데이터):

```text
pixels
→ edges/textures
→ parts
→ objects/semantic patterns
```

Không nên hiểu hierarchy này quá literal, nhưng nó là mô hình tư duy (mental model / 사고 모델) hữu ích.

## Transfer học tập (learning / 학습)

A pretrained visual backbone produces generic representations. Downstream tác vụ (task / 작업) có thể:

- freeze backbone + train head;
- fine-tune all layers;
- use adapters/parameter-efficient tuning.

Biểu diễn (representation / 표현) chất lượng (quality / 품질) quyết định mẫu (sample / 표본) efficiency downstream.

## Self-Supervised Visual biểu diễn (representation / 표현)

Labels expensive. Self-supervised methods học từ ảnh (image / 이미지) augmentations/masking.

Contrastive idea:

```text
two views of same image → embeddings should align
views of different images → separated
```

Masked ảnh (image / 이미지) modeling reconstruct/predict missing patches/features.

## CLIP-Style biểu diễn (representation / 표현)

Ảnh (image / 이미지) encoder và văn bản (text / 텍스트) encoder được train để aligned image-text pairs close trong dùng chung (shared / 공유) embedding không gian (space / 공간).

Điều này tạo powerful zero-shot classification/retrieval:

```text
image embedding
vs
text embeddings of candidate labels
```

Đây là cầu nối (bridge / 브리지) trực tiếp sang multimodal AI.

## Biểu diễn (representation / 표현) Collapse

Self-supervised objectives có rủi ro (risk / 위험) mô hình (model / 모델) đầu ra (output / 출력) same véc-tơ (vector / 벡터) cho everything. Methods cần negatives, predictors, stop-gradient hoặc variance/covariance các ràng buộc (constraints / 제약조건들) để tránh trivial solution.

## Tính năng (feature / 기능) chất lượng (quality / 품질) is Task-Dependent

Embedding tốt cho ngữ nghĩa (semantic / 의미적) retrieval chưa chắc tốt cho fine-grained defect inspection. “Good biểu diễn (representation / 표현)” luôn relative to downstream cấu trúc (structure / 구조).

## Tuyến tính (linear / 선형) Probe

Một cách kiểm thử (test / 테스트) biểu diễn (representation / 표현): freeze encoder, train tuyến tính (linear / 선형) classifier. Nếu simple tuyến tính (linear / 선형) head đạt tốt, ngữ nghĩa (semantic / 의미적) classes đã tương đối linearly separable trong tính năng (feature / 기능) không gian (space / 공간).

## Visualization

t-SNE/UMAP có thể visualize high-dimensional features nhưng 2D plots distort toàn cục (global / 전역) hình học (geometry / 기하학); không nên dùng cluster đẹp làm proof chất lượng.

## Explainability Caution

Activation map/nearest neighbors giúp inspect biểu diễn (representation / 표현) nhưng không cho complete nhân quả (causal / 인과적) explanation mô hình (model / 모델) quyết định (decision / 결정).

## Mô hình tư duy (mental model / 사고 모델)

> **tính năng (feature / 기능) biểu diễn (representation / 표현) là coordinate hệ thống (system / 시스템) mới nơi distinctions quan trọng của tác vụ (task / 작업) trở nên dễ xử lý hơn.**

Deep học tập (learning / 학습) mạnh vì nó học coordinate hệ thống (system / 시스템) cùng mục tiêu (objective / 목표) thay vì chỉ dùng features cố định.

## Dùng chung (common / 공통) Misconceptions

### “Learned features luôn tốt hơn hand-crafted”

Không nếu dữ liệu (data / 데이터) nhỏ, các ràng buộc (constraints / 제약조건들) rõ hoặc tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링) encode lĩnh vực (domain / 도메인) physics mạnh.

### “Embedding distance = ngữ nghĩa (semantic / 의미적) truth”

Distance phản ánh huấn luyện (training / 학습) mục tiêu (objective / 목표) và dữ liệu (data / 데이터), không universal ngữ nghĩa (semantics / 의미론).

### “Invariance càng nhiều càng tốt”

Nếu transformation đổi label, invariance gây mất thông tin (information / 정보).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tính năng (feature / 기능) biểu diễn (representation / 표현) nối [Representation Learning](../05_neural_networks/08_representation_learning.md), dimensionality reduction và chỉ số (metric / 지표) học tập (learning / 학습). CNN là kiến trúc (architecture / 아키텍처) đưa locality/translation độ lệch (bias / 편향) trực tiếp vào biểu diễn (representation / 표현) học tập (learning / 학습).

Xem tiếp: [CNN for Vision](./03_cnn_for_vision.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 images as data](./00_images_as_data.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
