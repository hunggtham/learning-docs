# Tính năng (feature / 기능) biểu diễn (representation / 표현) trong Computer Vision

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Feature representation trong computer vision**. Route đi từ raw pixels → local edges/corners → invariant descriptors → learned features → transfer/task heads, để representation nối với biến thiên hình học và mục tiêu nhận dạng.

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

Vì raw pixels thay đổi mạnh theo góc nhìn và điều kiện chụp, ta cần tìm những mẫu ổn định trong vùng lân cận. **Cục bộ (local / 로컬) Features** là bước đầu để xây dựng các mô tả như vậy, trước khi chuyển sang **HOG**.

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

SIFT mô tả một vùng quanh keypoint để tăng độ bền với scale và rotation; **HOG** khái quát hướng gradient trên các cell để nắm hình dạng. Khi số descriptor cục bộ thay đổi theo ảnh, **Bag of Visual Words** cung cấp một cách gom chúng thành biểu diễn có kích thước cố định.

## HOG

**Histogram of Oriented Gradients (HOG)** chia ảnh (image / 이미지) thành cells, tính độ dốc (gradient / 기울기) orientations rồi aggregate histograms.

Đối tượng (object / 객체) shape thường được encode tốt bởi edge directions hơn absolute điểm ảnh (pixel / 픽셀) intensity.

HOG từng rất effective cho pedestrian detection khi kết hợp tuyến tính (linear / 선형) SVM.

HOG giữ thông tin hướng biên theo vùng, còn Bag of Visual Words biến nhiều descriptor thành histogram từ vựng thị giác. Cả hai đều phải cân bằng việc bỏ biến thiên với việc giữ cấu trúc; đó là câu hỏi của **Tính năng (feature / 기능) Invariance vs Equivariance**.

## Bag of Visual Words

Cục bộ (local / 로컬) descriptors có variable count. Bag-of-visual-words cluster descriptors thành visual vocabulary, rồi represent ảnh (image / 이미지) bằng histogram of “visual words”.

Analogy với NLP bag-of-words:

```text
local patch descriptors → visual tokens → frequency vector
```

Nhược điểm: mất phần lớn spatial bố cục (layout / 레이아웃).

Bag of Visual Words có thể bất biến với nhiều thay đổi nhưng phải trả giá bằng thông tin không gian. Việc chọn invariance hay equivariance phụ thuộc tác vụ; **Tính năng (feature / 기능) Pyramid** tiếp tục giữ thông tin ở nhiều scale để hỗ trợ lựa chọn đó.

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

Feature pyramid giữ các mức chi tiết khác nhau để một detector có thể xử lý vật thể nhỏ lẫn lớn. Vì nhiều mức có thể tạo vector lớn, bước kế tiếp là xem **Dimensionality Reduction** có thể nén chúng ra sao mà không làm mất tín hiệu cần thiết.

## Tính năng (feature / 기능) Pyramid

Objects có nhiều scales. Classical các hệ thống (systems / 시스템들) dùng ảnh (image / 이미지) pyramids hoặc tính năng (feature / 기능) pyramids để detect đối tượng (object / 객체) ở multiple resolutions.

Hiện đại (modern / 현대적) tính năng (feature / 기능) Pyramid Networks giữ multi-scale tính năng (feature / 기능) maps trong CNN.

Pyramid mở rộng biểu diễn theo scale, còn dimensionality reduction tìm một không gian gọn hơn để tính toán và quan sát. Không gian gọn có hữu ích hay không phải được đánh giá bằng **Chỉ số (metric / 지표) học tập (learning / 학습)** phù hợp với mục tiêu.

## Dimensionality Reduction

Descriptors high-dimensional có thể compress bằng PCA. PCA giữ directions of largest variance nhưng không guarantee ngữ nghĩa (semantic / 의미적) importance.

Whitening có thể decorrelate dimensions nhưng đôi khi amplify low-variance noise.

Một phép nén có thể trông tốt theo reconstruction nhưng chưa chắc tách được nhãn. Vì vậy metric phải gắn với tác vụ; đây cũng là điểm so sánh quan trọng giữa **Hand-Designed vs Learned Features**.

## Chỉ số (metric / 지표) học tập (learning / 학습)

Nếu biểu diễn (representation / 표현) dùng cho retrieval/matching, ta muốn similar entities close và dissimilar far.

Contrastive/triplet objectives:

```text
anchor-positive distance ↓
anchor-negative distance ↑
```

Hiện đại (modern / 현대적) face recognition và ảnh (image / 이미지) retrieval dựa heavily vào learned chỉ số (metric / 지표) embeddings.

Feature thủ công mang prior rõ ràng và dễ kiểm soát; feature học được linh hoạt hơn nhưng cần dữ liệu và mục tiêu phù hợp. Khi biểu diễn đã học từ một nguồn lớn, **Transfer học tập (learning / 학습)** là cách kiểm tra khả năng tái sử dụng của nó.

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

Transfer learning cho phép giữ lại phần biểu diễn hữu ích rồi điều chỉnh theo domain mới, nhưng domain gap vẫn có thể lớn. Một hướng giảm phụ thuộc vào nhãn là **Self-Supervised Visual biểu diễn (representation / 표현)**.

## Transfer học tập (learning / 학습)

A pretrained visual backbone produces generic representations. Downstream tác vụ (task / 작업) có thể:

- freeze backbone + train head;
- fine-tune all layers;
- use adapters/parameter-efficient tuning.

Biểu diễn (representation / 표현) chất lượng (quality / 품질) quyết định mẫu (sample / 표본) efficiency downstream.

Self-supervised learning dùng tín hiệu từ chính dữ liệu để học cấu trúc trước khi fine-tune. Khi tín hiệu đó đến từ cặp ảnh–văn bản và mục tiêu tương phản, ta có kiểu **CLIP-Style biểu diễn (representation / 표현)**.

## Self-Supervised Visual biểu diễn (representation / 표현)

Labels expensive. Self-supervised methods học từ ảnh (image / 이미지) augmentations/masking.

Contrastive idea:

```text
two views of same image → embeddings should align
views of different images → separated
```

Masked ảnh (image / 이미지) modeling reconstruct/predict missing patches/features.

CLIP-style training nối hai modality bằng không gian embedding chung, nhưng mục tiêu tương phản vẫn cần đủ đa dạng để tránh nghiệm tầm thường. Một rủi ro cần theo dõi là **Biểu diễn (representation / 표현) Collapse**.

## CLIP-Style biểu diễn (representation / 표현)

Ảnh (image / 이미지) encoder và văn bản (text / 텍스트) encoder được train để aligned image-text pairs close trong dùng chung (shared / 공유) embedding không gian (space / 공간).

Điều này tạo powerful zero-shot classification/retrieval:

```text
image embedding
vs
text embeddings of candidate labels
```

Đây là cầu nối (bridge / 브리지) trực tiếp sang multimodal AI.

Nếu mọi đầu vào bị ánh xạ gần như cùng một vector, embedding mất khả năng phân biệt dù loss có thể vẫn giảm. Vì thế, **Tính năng (feature / 기능) chất lượng (quality / 품질) is Task-Dependent** chứ không thể suy ra từ một chỉ số duy nhất.

## Biểu diễn (representation / 표현) Collapse

Self-supervised objectives có rủi ro (risk / 위험) mô hình (model / 모델) đầu ra (output / 출력) same véc-tơ (vector / 벡터) cho everything. Methods cần negatives, predictors, stop-gradient hoặc variance/covariance các ràng buộc (constraints / 제약조건들) để tránh trivial solution.

Chất lượng representation phải được hỏi trong ngữ cảnh classification, retrieval, detection hay robustness. **Tuyến tính (linear / 선형) Probe** là một phép thử đơn giản để xem thông tin của một tác vụ có còn dễ tách trong embedding hay không.

## Tính năng (feature / 기능) chất lượng (quality / 품질) is Task-Dependent

Embedding tốt cho ngữ nghĩa (semantic / 의미적) retrieval chưa chắc tốt cho fine-grained defect inspection. “Good biểu diễn (representation / 표현)” luôn relative to downstream cấu trúc (structure / 구조).

Linear probe đo khả năng dùng lại embedding với một head đơn giản, nhưng không phải bằng chứng đầy đủ về mọi năng lực. **Visualization** bổ sung một góc nhìn trực quan để kiểm tra các cụm và biến thiên trong không gian đó.

## Tuyến tính (linear / 선형) Probe

Một cách kiểm thử (test / 테스트) biểu diễn (representation / 표현): freeze encoder, train tuyến tính (linear / 선형) classifier. Nếu simple tuyến tính (linear / 선형) head đạt tốt, ngữ nghĩa (semantic / 의미적) classes đã tương đối linearly separable trong tính năng (feature / 기능) không gian (space / 공간).

Visualization giúp phát hiện pattern và outlier, nhưng phép chiếu xuống hai hoặc ba chiều cũng có thể tạo ảo giác. Vì vậy cần giữ **Explainability Caution** khi diễn giải embedding hay activation.

## Visualization

t-SNE/UMAP có thể visualize high-dimensional features nhưng 2D plots distort toàn cục (global / 전역) hình học (geometry / 기하학); không nên dùng cluster đẹp làm proof chất lượng.

Một biểu đồ đẹp không chứng minh rằng feature có ý nghĩa nhân quả hoặc ổn định ngoài dữ liệu đã xem. **Mô hình tư duy (mental model / 사고 모델)** giúp đặt mọi phép đo representation vào đúng vai trò.

## Explainability Caution

Activation map/nearest neighbors giúp inspect biểu diễn (representation / 표현) nhưng không cho complete nhân quả (causal / 인과적) explanation mô hình (model / 모델) quyết định (decision / 결정).

Representation là một hệ tọa độ được học hoặc thiết kế để làm rõ những khác biệt quan trọng cho một mục tiêu. Trước khi kết luận, hãy đối chiếu mô hình này với các **Dùng chung (common / 공통) Misconceptions**.

## Mô hình tư duy (mental model / 사고 모델)

> **tính năng (feature / 기능) biểu diễn (representation / 표현) là coordinate hệ thống (system / 시스템) mới nơi distinctions quan trọng của tác vụ (task / 작업) trở nên dễ xử lý hơn.**

Deep học tập (learning / 학습) mạnh vì nó học coordinate hệ thống (system / 시스템) cùng mục tiêu (objective / 목표) thay vì chỉ dùng features cố định.

Các ngộ nhận sau nhắc rằng representation luôn phụ thuộc dữ liệu, objective và tác vụ. **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ nối các ý này với những chương liên quan.

## Dùng chung (common / 공통) Misconceptions

### “Learned features luôn tốt hơn hand-crafted”

Không nếu dữ liệu (data / 데이터) nhỏ, các ràng buộc (constraints / 제약조건들) rõ hoặc tính năng (feature / 기능) kỹ thuật (engineering / 엔지니어링) encode lĩnh vực (domain / 도메인) physics mạnh.

### “Embedding distance = ngữ nghĩa (semantic / 의미적) truth”

Distance phản ánh huấn luyện (training / 학습) mục tiêu (objective / 목표) và dữ liệu (data / 데이터), không universal ngữ nghĩa (semantics / 의미론).

### “Invariance càng nhiều càng tốt”

Nếu transformation đổi label, invariance gây mất thông tin (information / 정보).

Các liên kết cuối file chỉ ra nơi đào sâu về representation learning, dimensionality reduction và metric learning. Kết luận cần giữ là: một feature tốt là feature phục vụ đúng nhiệm vụ, không phải một vector “đúng” cho mọi ngữ cảnh.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tính năng (feature / 기능) biểu diễn (representation / 표현) nối [Representation Learning](../05_neural_networks/08_representation_learning.md), dimensionality reduction và chỉ số (metric / 지표) học tập (learning / 학습). CNN là kiến trúc (architecture / 아키텍처) đưa locality/translation độ lệch (bias / 편향) trực tiếp vào biểu diễn (representation / 표현) học tập (learning / 학습).

Xem tiếp: [CNN for Vision](./03_cnn_for_vision.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
