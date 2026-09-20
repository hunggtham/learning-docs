# Image Segmentation

**Image Segmentation (이미지 분할)** gán label ở mức pixel hoặc region. Nó trả lời không chỉ “có object gì?” và “ở đâu?”, mà còn **pixel nào thuộc object nào**.

Có ba setting chính:

```text
Semantic Segmentation → mỗi pixel có class, không tách instance cùng class
Instance Segmentation → tách từng object instance + mask
Panoptic Segmentation → kết hợp semantic “stuff” + instance “things”
```

## Semantic Segmentation

Input:

\[
X\in\mathbb{R}^{H\times W\times C}
\]

Output logits per pixel:

\[
Z\in\mathbb{R}^{H\times W\times K}
\]

Mỗi pixel được classify vào one of `K` classes.

## Encoder–Decoder Architecture

Classification backbone downsample để học semantics nhưng mất spatial detail. Segmentation cần recover resolution.

Typical pattern:

```text
image
→ encoder: lower resolution, richer semantics
→ decoder: upsample + fuse details
→ pixel-wise prediction
```

U-Net là classic architecture với skip connections nối encoder features high-resolution sang decoder.

## Why Skip Connections Matter

Deep features biết “đây là car” nhưng spatial boundary coarse. Early features có edges/location chi tiết. Skip connections combine semantics + localization.

## Upsampling

Options:

- nearest/bilinear interpolation;
- transposed convolution;
- learned upsampling.

Transposed convolution có thể tạo checkerboard artifacts nếu kernel/stride interaction không tốt.

## Segmentation Loss

Pixel-wise cross-entropy:

\[
L=-\sum_{i} \log p_{i,y_i}
\]

Nhưng class imbalance rất severe: background có thể dominate.

Dice coefficient:

\[
Dice=\frac{2|P\cap G|}{|P|+|G|}
\]

Dice loss emphasizes overlap và useful medical/small-object segmentation.

IoU/Jaccard:

\[
IoU=\frac{|P\cap G|}{|P\cup G|}
\]

## Boundary Quality

Two masks có similar IoU nhưng boundary behavior khác. Boundary-specific metrics/losses useful when contour precision matters, e.g. medical surgery or manufacturing.

## Instance Segmentation

Mask R-CNN extends detection:

```text
region proposal
→ class + box
→ per-instance mask head
```

Need assign pixels to distinct objects even if same class and overlapping.

## Panoptic Segmentation

“Things” = countable instances như person/car.

“Stuff” = amorphous regions như sky/road/grass.

Panoptic segmentation seeks unified scene parse.

## Fully Convolutional Networks

FCN replaces dense classifier with convolutional operations to preserve spatial prediction and accept variable image sizes more naturally.

## Atrous/Dilated Convolution

Dilated convolution expands receptive field without reducing resolution. DeepLab-style architectures combine dilation + multi-scale context.

## Multi-Scale Context

Pixel identity may depend on larger scene. A tiny gray patch could be road, wall or car based on context. Pyramid pooling/ASPP capture multiple receptive-field scales.

## Transformer Segmentation

Vision transformers provide global interactions. Modern segmentation may use transformer encoder/decoder and mask queries, treating masks as set predictions similar DETR.

## Promptable Segmentation

Foundation segmentation models can accept points, boxes, masks or text-like prompts to specify target object/region. This changes interaction from fixed taxonomy to **conditional segmentation**.

Still, model may fail on domain-specific imagery outside pretraining distribution.

## Annotation Cost

Pixel masks expensive. Strategies:

- polygons;
- weak labels;
- boxes/scribbles;
- pseudo-labeling;
- interactive annotation;
- foundation-model-assisted labeling.

Label quality at boundaries can be subjective.

## Class Imbalance

Rare classes/small lesions can occupy tiny fraction. Pixel accuracy then misleading.

Use class-wise IoU, Dice, recall and region-level metrics.

## Post-Processing

Morphological cleanup, connected components, CRF-like refinement or domain constraints can remove isolated noise.

Production segmentation often hybrid neural + deterministic geometry.

## 3D Segmentation

Medical CT/MRI uses volumes:

\[
X\in\mathbb{R}^{D\times H\times W\times C}
\]

3D convolutions capture volumetric context but memory cost huge. 2.5D approaches process slices with neighboring context.

## Temporal Segmentation

Video segmentation should preserve consistency across frames. Independent per-frame masks flicker; temporal models/tracking help.

## Evaluation

Common metrics:

- mIoU;
- Dice/F1;
- pixel accuracy;
- boundary F-score;
- panoptic quality.

Metric choice depends application. In medical imaging, missing small lesion may be much worse than slight boundary mismatch.

## Uncertainty

Pixel-wise confidence maps can guide manual review. But neighboring pixels correlated, so naive confidence interpretation may overstate certainty.

## Mental Model

> **Segmentation giữ spatial structure đến mức pixel; encoder học “cái gì”, decoder khôi phục “ở đâu chính xác”.**

## Common Misconceptions

### “Pixel accuracy cao = segmentation tốt”

Background dominance có thể làm metric cao dù rare object fail.

### “Segmentation mask là ground truth tuyệt đối”

Human annotation boundaries có uncertainty.

### “Upsampling phục hồi detail đã mất”

Nó chỉ reconstruct từ retained features/skip connections; information fully discarded không magically return.

## Knowledge Connection

Segmentation connects image processing masks, CNN multi-scale representation, detection và transformer set prediction.

Xem tiếp: [Vision Transformers](./07_vision_transformers.md).