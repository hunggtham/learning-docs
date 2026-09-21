# Object Detection

**Object Detection (객체 탐지)** vừa phải nhận biết object class, vừa phải localize nhiều instances trong cùng image. Output thường là set:

\[
\{(b_i,c_i,s_i)\}_{i=1}^N
\]

với bounding box `b_i`, class `c_i`, confidence `s_i`.

## Tại sao detection khó hơn classification?

Classification biết toàn image thuộc class nào. Detection không biết trước:

- có bao nhiêu object;
- object ở đâu;
- kích thước ra sao;
- overlaps/occlusion;
- background chiếm phần lớn image.

Do đó model phải solve localization + classification + variable-length output.

## Bounding Boxes

Box có thể represent:

```text
(x_min, y_min, x_max, y_max)
```

hoặc:

```text
(center_x, center_y, width, height)
```

Coordinate normalization và image resizing phải transform labels nhất quán.

## Intersection over Union

**IoU (Intersection over Union / 교집합-합집합 비율)** đo overlap:

\[
IoU(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

IoU=1 perfect overlap; 0 no overlap.

IoU dùng cho matching predictions-ground truth và evaluation.

## Two-Stage Detectors

Family R-CNN:

```text
image → backbone features
→ region proposals
→ classify/refine each region
```

Faster R-CNN learns Region Proposal Network. Two-stage methods historically strong accuracy, especially complex scenes.

## One-Stage Detectors

YOLO/SSD-style models predict classes/boxes densely in one pass:

```text
feature maps → dense box/class predictions
```

Thường faster and simpler deployment.

## Anchors

Anchor-based detectors place predefined boxes of different scales/aspect ratios. Model predicts offsets + objectness/classes relative anchors.

Anchor design introduces hyperparameters and matching complexity.

Anchor-free detectors predict centers/corners/distances directly, reducing handcrafted anchor assumptions.

## Objectness

Model often estimates probability location contains object independent of class. Final score may combine objectness + class probability.

## Matching During Training

Many candidate predictions must be assigned to ground-truth boxes. Assignment rule strongly affects optimization.

Old approaches use IoU thresholds; modern detectors may use dynamic matching/cost-based assignment.

## Box Regression Loss

Coordinate L1/Smooth-L1 losses do not directly optimize overlap geometry. IoU-based losses:

- IoU loss;
- GIoU;
- DIoU;
- CIoU.

They incorporate spatial overlap/distance/aspect considerations.

## Class Imbalance

Dense detectors generate huge background negatives. **Focal Loss** downweights easy examples:

\[
FL(p_t)=-(1-p_t)^\gamma\log p_t
\]

helping training focus hard positives/negatives.

## Non-Maximum Suppression

Dense detector may output many overlapping boxes for same object. **NMS**:

1. sort boxes by score;
2. keep highest;
3. remove lower-score boxes with IoU above threshold;
4. repeat.

NMS is post-processing, not semantic reasoning.

Soft-NMS decays scores instead of hard removal.

## Detection Transformers

DETR reframes detection as **set prediction**. Transformer decoder uses object queries and bipartite matching (Hungarian algorithm) between predicted set and ground truth.

This reduces need for anchors/NMS in core formulation, though training/variants have their own complexity.

## Multi-Scale Features

Small and large objects need different resolutions. Feature Pyramid Networks combine high-level semantics with higher spatial resolution.

Small-object detection is especially sensitive to downsampling.

## Mean Average Precision

Detection metric usually AP/mAP. Precision-recall is computed under IoU criterion; COCO-style mAP averages over multiple IoU thresholds, rewarding localization quality more strictly.

A detector can have high classification confidence but poor box localization.

## NMS Threshold Trade-off

Threshold too low → suppress neighboring distinct objects.

Too high → duplicate detections remain.

Crowded scenes require careful handling.

## Small Objects

If object becomes only a few feature-map cells, information nearly lost. Solutions:

- larger input resolution;
- feature pyramids;
- tiling;
- small-object focused augmentation/data.

Compute cost rises significantly.

## Occlusion

Partial object evidence can be ambiguous. Context may help, but model can over-rely on background/context shortcuts.

## Data Annotation

Box labels cheaper than pixel masks but still subjective: should box include shadow? truncated object? heavily occluded instance? Annotation policy must be consistent.

## Real-Time Detection

Latency includes preprocessing + model + NMS + transfer, not model FLOPs alone. Batch size 1 latency matters edge/interactive systems.

## Tracking Connection

Detection per frame gives objects independently. Multi-object tracking adds identity consistency across time using motion/appearance association.

## Open-Vocabulary Detection

Vision-language pretrained models enable detection conditioned on text labels beyond fixed closed-set taxonomy. Challenge remains localization and calibration for unseen concepts.

## Mental Model

> **Object Detection = classification over candidate regions + geometry estimation + duplicate/set resolution.**

Different detector families mainly differ in how they generate candidates, represent queries and assign predictions.

## Common Misconceptions

### “High mAP means every object reliably detected”

Average metric hides class/size/subgroup failures.

### “NMS is part of learning”

Traditional NMS is post-processing heuristic, though some modern systems learn/set-predict to avoid it.

### “Higher input resolution always solves small objects”

It helps but increases compute/memory; sensor detail may already be absent.

## Knowledge Connection

Detection combines CNN/Transformer features, geometry, matching algorithms and set prediction. Segmentation moves from boxes to pixel-level structure.

Xem tiếp: [Image Segmentation](./06_image_segmentation.md).