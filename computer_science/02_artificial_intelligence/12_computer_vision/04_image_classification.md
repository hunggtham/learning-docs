# Image Classification

**Image classification (이미지 분류)** gán một hoặc nhiều labels cho toàn image. Đây là task đơn giản hơn detection/segmentation vì output không cần vị trí chính xác của object.

```text
image → encoder/backbone → global representation → classification head → class probabilities
```

## Single-Label Classification

Mỗi image có đúng một class trong `K` classes. Model output logits:

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

## Multi-Label Classification

Một image có nhiều labels đồng thời, ví dụ `dog`, `outdoor`, `grass`.

Không dùng softmax competition. Mỗi class thường có sigmoid independent:

\[
p_k=\sigma(z_k)
\]

và binary cross-entropy per label.

## Class Probability không phải Truth Probability

Softmax score có thể overconfident, đặc biệt under distribution shift. Calibration cần evaluate riêng.

## Data Splitting

Random image split có thể leak near-duplicate frames từ cùng video/person/product vào train/test. Grouped split theo patient/device/scene thường cần để estimate generalization đúng.

## Class Imbalance

Nếu rare defect 0.1%, accuracy vô nghĩa. Metrics phù hợp:

- precision/recall;
- PR-AUC;
- per-class F1;
- macro average;
- expected cost.

Class weighting/focal loss có thể đổi training emphasis nhưng không substitute representative data.

## Top-k Accuracy

Top-1 yêu cầu correct class highest score. Top-5 tính đúng nếu label nằm trong 5 classes score cao nhất. Top-k hữu ích large-taxonomy tasks nhưng có thể irrelevant cho production action.

## Confusion Matrix

Cho biết class nào model nhầm với class nào. Aggregate accuracy không reveal systematic failure between similar categories.

## Transfer Learning Pipeline

Practical flow:

```text
pretrained backbone
→ replace classifier head
→ train head
→ optionally unfreeze/fine-tune backbone
```

Learning rate cho pretrained layers thường nhỏ hơn newly initialized head.

## Freeze vs Fine-Tune

Freeze khi data ít/compute hạn chế/domain close. Fine-tune khi enough data và domain shift meaningful.

Full fine-tuning có risk catastrophic forgetting/overfit. Parameter-efficient approaches có thể useful.

## Augmentation

Common transformations:

- random crop/resize;
- horizontal flip;
- color jitter;
- mixup;
- CutMix;
- random erasing.

Mixup creates interpolation:

\[
\tilde x=\lambda x_i+(1-\lambda)x_j
\]

\[
\tilde y=\lambda y_i+(1-\lambda)y_j
\]

encouraging smoother decision boundaries.

CutMix replaces region from another image and mixes labels proportional area, preserving local visual statistics better than pure pixel interpolation.

## Label Smoothing

Replace one-hot target with slightly softened distribution. Can reduce overconfidence but may affect calibration/rare-class learning.

## Fine-Grained Classification

Distinguishing bird species/product variants requires subtle local features. High-resolution crops, attention/localization and domain-specific data become important.

## Hierarchical Taxonomy

Labels may have hierarchy:

```text
animal → bird → eagle
```

Flat classifier ignores semantic structure. Hierarchical losses/routing can exploit taxonomy, but evaluation must handle parent/child errors meaningfully.

## Open-Set Recognition

Standard classifier assumes input belongs to known classes. Real world may contain unknown category. Out-of-distribution/open-set detection attempts identify unfamiliar examples.

High softmax confidence does not guarantee in-distribution.

## Zero-Shot Classification

Vision-language models can compare image embedding with text label descriptions, enabling classes not explicitly trained as classifier head.

But performance depends prompt wording, class semantics and pretraining coverage.

## Data-Centric Error Analysis

For each error cluster ask:

- label wrong?
- image ambiguous?
- resolution too low?
- background shortcut?
- rare subgroup missing?
- deployment camera mismatch?

Model change is only one lever.

## Shortcut Learning

Model may classify “cow” from green pasture background rather than animal shape. If deployment background changes, accuracy collapses.

Counterfactual/background-balanced data helps detect shortcut reliance.

## Saliency and CAM

Class Activation Maps highlight regions contributing to class score. Useful debugging, not definitive causal explanation.

If model consistently focuses watermark/corner, dataset leakage likely.

## Adversarial / Natural Robustness

Small perturbation or common corruptions can degrade model. Robust evaluation should include blur, noise, brightness, compression and viewpoint changes relevant deployment.

## Confidence Threshold and Abstention

System can abstain/manual-review when max confidence below threshold. This converts model into decision system with coverage–risk trade-off.

Selective risk:

```text
higher threshold → fewer automated predictions, potentially higher precision
```

## Mental Model

> **Classification compresses entire image into a global decision. Vì vậy nó có thể biết “có gì” nhưng không nhất thiết biết “ở đâu”.**

Detection/segmentation add spatial outputs.

## Common Misconceptions

### “99% accuracy nghĩa model production-ready”

Need subgroup, shift, calibration, latency and failure cost evaluation.

### “Softmax 0.99 nghĩa 99% chắc chắn đúng”

Only if calibrated on target distribution.

### “More augmentation always improves”

Invalid augmentations can destroy label semantics.

## Knowledge Connection

Classification is the simplest supervised vision head and a foundation for transfer learning. Detection extends the task to multiple localized objects.

Xem tiếp: [Object Detection](./05_object_detection.md).