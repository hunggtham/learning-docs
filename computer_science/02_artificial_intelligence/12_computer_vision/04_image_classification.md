# Image Classification

**Phân loại ảnh (image classification / 이미지 분류)** gán một hoặc nhiều label cho toàn bộ image. Đây là task đơn giản hơn object detection hoặc segmentation vì output không cần chỉ ra vị trí chính xác của object.

```text
image
→ encoder / backbone
→ global representation
→ classification head
→ xác suất class
```

## Single-Label Classification

Mỗi image thuộc đúng một class trong `K` class. Model output logits:

\[
z\in\mathbb{R}^K
\]

Softmax:

\[
p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Training thường dùng cross-entropy:

\[
L=-\log p_y
\]

trong đó `y` là class đúng.

## Multi-Label Classification

Một image có thể có nhiều label đồng thời, ví dụ `dog`, `outdoor`, `grass`.

Không dùng softmax competition giữa các class. Thay vào đó mỗi class thường có sigmoid riêng:

\[
p_k=\sigma(z_k)
\]

và binary cross-entropy được tính cho từng label.

## Class Probability không phải Truth Probability

Softmax score có thể rất tự tin dù prediction sai, đặc biệt khi distribution deployment khác training data.

Calibration cần được evaluate riêng. Một score `0.99` chỉ có interpretation xác suất tốt khi model được calibration phù hợp trên target distribution.

## Data Split

Random image split có thể làm rò rỉ near-duplicate frame từ cùng video, cùng patient hoặc cùng product vào cả train và test.

Khi các sample có quan hệ nhóm, nên split theo group như:

```text
patient
device
scene
video
product instance
```

để đo generalization thực tế hơn.

## Class Imbalance

Nếu rare defect chỉ chiếm 0.1%, accuracy tổng thể gần như vô nghĩa.

Metric phù hợp hơn có thể gồm:

- precision và recall;
- PR-AUC;
- per-class F1;
- macro average;
- expected business cost.

Class weighting hoặc focal loss có thể thay đổi emphasis của training, nhưng không thay thế data coverage đại diện cho class hiếm.

## Top-k Accuracy

Top-1 yêu cầu correct class có score cao nhất.

Top-5 được tính đúng nếu label thật nằm trong 5 class score cao nhất.

Top-k hữu ích với taxonomy rất lớn, nhưng có thể không liên quan trực tiếp tới production decision nếu hệ thống buộc phải chọn một action duy nhất.

## Confusion Matrix

Confusion matrix cho biết model thường nhầm class nào với class nào.

Aggregate accuracy có thể che systematic failure giữa các category gần nhau.

Ví dụ nếu model luôn nhầm defect A thành defect B, đó là signal quan trọng hơn một con số accuracy tổng quát.

## Transfer Learning Pipeline

Một flow thực tế:

```text
pretrained backbone
→ thay classifier head
→ train head
→ tùy nhu cầu unfreeze và fine-tune backbone
```

Learning rate cho pretrained layer thường nhỏ hơn layer mới khởi tạo để tránh phá representation quá nhanh.

## Freeze và Fine-Tune

Freeze backbone phù hợp khi:

- labeled data ít;
- compute hạn chế;
- domain mới gần domain pretraining.

Fine-tune nhiều layer hơn khi domain shift đáng kể và có đủ data.

Full fine-tuning có thể gây overfit hoặc catastrophic forgetting. Adapter hoặc parameter-efficient tuning là lựa chọn ở một số setting.

## Augmentation

Các transformation phổ biến:

- random crop/resize;
- horizontal flip;
- color jitter;
- Mixup;
- CutMix;
- random erasing.

Mixup tạo sample nội suy:

\[
\tilde x=\lambda x_i+(1-\lambda)x_j
\]

\[
\tilde y=\lambda y_i+(1-\lambda)y_j
\]

nhằm khuyến khích decision boundary mượt hơn.

CutMix thay một vùng image bằng patch từ image khác rồi mix label theo area. Nó giữ local visual statistic tự nhiên hơn pure pixel interpolation trong nhiều case.

## Label Smoothing

Label smoothing thay one-hot target bằng một distribution hơi mềm hơn.

Kỹ thuật này có thể giảm overconfidence và regularize training, nhưng cũng ảnh hưởng calibration hoặc learning của rare class nếu dùng không phù hợp.

## Fine-Grained Classification

Phân biệt bird species, product variant hoặc defect subtype thường cần feature rất nhỏ và tinh tế.

Khi đó high-resolution crop, localization, attention và domain-specific data trở nên quan trọng hơn.

## Hierarchical Taxonomy

Label có thể nằm trong hierarchy:

```text
animal → bird → eagle
```

Flat classifier bỏ qua relationship này.

Hierarchical loss hoặc routing có thể tận dụng taxonomy, và evaluation cũng nên phân biệt lỗi “eagle → hawk” với lỗi “eagle → car”.

## Open-Set Recognition

Standard classifier giả định mọi input thuộc một class đã biết.

Trong real world, input có thể thuộc unknown category. **Open-set recognition** hoặc out-of-distribution detection cố nhận biết những example như vậy.

High softmax confidence không chứng minh input nằm trong training distribution.

## Zero-Shot Classification

Vision-language model có thể so image embedding với text embedding của candidate label để classification mà không cần train classifier head riêng cho từng class.

Quality phụ thuộc:

```text
prompt wording
class semantics
pretraining coverage
image-text alignment
```

Zero-shot không đồng nghĩa zero-error.

## Data-Centric Error Analysis

Khi phân tích error cluster, nên hỏi:

- label có sai không?
- image có mơ hồ không?
- resolution có quá thấp không?
- model có dựa vào background shortcut không?
- subgroup hiếm có thiếu trong training không?
- camera deployment có khác training không?

Thay model chỉ là một trong nhiều lever.

## Shortcut Learning

Model có thể học class “cow” từ green pasture background thay vì từ shape của animal.

Nếu deployment background thay đổi, performance có thể collapse.

Counterfactual data hoặc background-balanced data giúp phát hiện và giảm shortcut reliance.

## Saliency và CAM

Class Activation Map có thể highlight region ảnh hưởng mạnh tới class score.

Nó hữu ích để debug, nhưng không phải causal explanation hoàn chỉnh.

Nếu model liên tục tập trung vào watermark hoặc corner artifact, đó có thể là dấu hiệu dataset leakage.

## Robustness tự nhiên và Adversarial

Blur, noise, brightness change, compression hoặc viewpoint shift đều có thể làm performance giảm.

Robust evaluation nên bao gồm corruption phản ánh deployment condition, không chỉ clean benchmark image.

## Confidence Threshold và Abstention

System có thể chuyển sample sang manual review khi confidence dưới threshold.

Điều này tạo trade-off giữa coverage và risk:

```text
threshold cao hơn
→ ít prediction tự động hơn
→ có thể tăng precision trên phần được tự động xử lý
```

Threshold phải được calibration bằng target distribution và business cost.

## Mô hình tư duy

> **Classification nén toàn bộ image thành một quyết định global. Vì vậy nó có thể trả lời “ảnh chứa gì” nhưng không nhất thiết biết “object nằm ở đâu”.**

Detection và segmentation bổ sung spatial output.

## Những nhầm lẫn thường gặp

### “99% accuracy nghĩa là production-ready”

Không. Cần đánh giá subgroup, distribution shift, calibration, latency và failure cost.

### “Softmax 0.99 nghĩa chắc chắn đúng 99%”

Không trừ khi model được calibration phù hợp trên distribution tương ứng.

### “Augmentation càng nhiều càng tốt”

Không. Augmentation làm đổi semantics của label có thể làm model học sai.

## Liên kết kiến thức

Image classification là supervised vision head cơ bản và là nền cho transfer learning. Object detection mở rộng bài toán sang nhiều object có location cụ thể.

Xem tiếp: [Object Detection](./05_object_detection.md).