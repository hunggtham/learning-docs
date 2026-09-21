# Object Detection

**Phát hiện vật thể (Object Detection / 객체 탐지)** vừa phải nhận biết object class, vừa phải xác định vị trí của nhiều instance trong cùng image. Output thường là một set:

\[
\{(b_i,c_i,s_i)\}_{i=1}^N
\]

với bounding box `b_i`, class `c_i` và confidence score `s_i`.

## Vì sao Detection khó hơn Classification?

Classification chỉ cần quyết định class ở mức toàn image. Detection phải xử lý thêm nhiều unknown:

- có bao nhiêu object;
- object nằm ở đâu;
- kích thước như thế nào;
- object overlap hoặc occlusion ra sao;
- background có thể chiếm phần lớn image.

Do đó model phải đồng thời giải localization, classification và variable-length output.

## Bounding Box

Box có thể được biểu diễn bằng:

```text
(x_min, y_min, x_max, y_max)
```

hoặc:

```text
(center_x, center_y, width, height)
```

Khi resize hoặc crop image, label coordinate phải được transform nhất quán. Box-format mismatch là nguồn bug rất phổ biến.

## Intersection over Union

**Intersection over Union (IoU / 교집합-합집합 비율)** đo mức overlap giữa hai box:

\[
IoU(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

- `IoU = 1`: overlap hoàn hảo;
- `IoU = 0`: không overlap.

IoU được dùng cả trong matching prediction với ground truth và trong evaluation.

## Two-Stage Detector

Family R-CNN dùng pipeline:

```text
image
→ backbone feature
→ region proposal
→ classify và refine từng region
```

Faster R-CNN học **Region Proposal Network (RPN)** để sinh proposal.

Two-stage detector thường có accuracy mạnh trong scene phức tạp, đổi lại latency và implementation cost có thể cao hơn.

## One-Stage Detector

YOLO hoặc SSD-style model dự đoán box và class trực tiếp trên dense feature map trong một forward pass:

```text
feature map
→ dense box / class prediction
```

Cách này thường phù hợp hơn với real-time hoặc edge deployment.

## Anchor

Anchor-based detector đặt trước nhiều box template với scale và aspect ratio khác nhau. Model dự đoán offset và objectness/class tương đối với anchor.

Anchor design tạo thêm hyperparameter và matching complexity.

Anchor-free detector cố dự đoán center, corner hoặc distance trực tiếp, giảm một phần handcrafted assumption.

## Objectness

Nhiều detector tách câu hỏi:

```text
“vị trí này có object không?”
```

khỏi câu hỏi class cụ thể.

Objectness score có thể được kết hợp với class probability để tạo final detection score.

## Matching khi Training

Model thường tạo rất nhiều candidate prediction, trong khi ground truth chỉ có một số box.

Training phải xác định prediction nào chịu trách nhiệm cho ground-truth object nào.

Approach cổ điển dùng IoU threshold. Modern detector có thể dùng dynamic matching hoặc cost-based assignment.

Assignment rule ảnh hưởng mạnh optimization vì nó xác định positive/negative sample.

## Box Regression Loss

L1 hoặc Smooth-L1 trên coordinate không trực tiếp tối ưu overlap geometry.

IoU-based loss gồm:

- IoU loss;
- GIoU;
- DIoU;
- CIoU.

Các loss này thêm thông tin về overlap, center distance hoặc aspect ratio để box learning phù hợp geometry hơn.

## Class Imbalance

Dense detector tạo số lượng background candidate rất lớn so với positive object.

**Focal Loss** giảm weight của easy example:

\[
FL(p_t)=-(1-p_t)^\gamma\log p_t
\]

nhờ đó gradient tập trung nhiều hơn vào hard positive và hard negative.

## Non-Maximum Suppression

Dense detector có thể output nhiều box overlap cho cùng một object.

**Non-Maximum Suppression (NMS)** thường:

1. sort box theo score;
2. giữ box score cao nhất;
3. loại box score thấp có IoU quá cao với box đã giữ;
4. lặp lại.

NMS là post-processing heuristic, không phải semantic reasoning.

Soft-NMS giảm score dần thay vì xóa cứng prediction.

## Detection Transformer

DETR chuyển detection thành **set prediction**.

Transformer decoder dùng object query và bipartite matching bằng Hungarian algorithm để ghép predicted set với ground truth.

Formulation này giảm sự phụ thuộc vào anchor và NMS truyền thống, nhưng đem lại các challenge riêng về training speed, query design và small-object performance.

## Multi-Scale Feature

Small và large object cần feature ở resolution khác nhau.

Feature Pyramid Network kết hợp high-level semantic feature với feature map có spatial resolution cao hơn.

Small-object detection đặc biệt nhạy với downsampling vì object có thể chỉ còn vài cell trên feature map.

## Mean Average Precision

Detection thường dùng AP hoặc mAP.

Precision–recall được tính với một IoU criterion. COCO-style mAP average qua nhiều IoU threshold, vì vậy localization chính xác được thưởng nhiều hơn.

Một detector có thể classification rất tự tin nhưng box localization vẫn kém.

## Trade-off của NMS Threshold

Threshold quá thấp:

```text
→ dễ xóa nhầm hai object gần nhau
```

Threshold quá cao:

```text
→ nhiều duplicate detection còn lại
```

Crowded scene làm trade-off này khó hơn đáng kể.

## Small Object

Nếu object chỉ chiếm vài pixel hoặc vài feature-map cell, information gần như bị mất.

Các hướng xử lý gồm:

- input resolution cao hơn;
- feature pyramid;
- tiling image;
- data hoặc augmentation tập trung small object.

Tất cả đều có cost về memory hoặc latency.

## Occlusion

Object bị che một phần tạo evidence không đầy đủ.

Context có thể giúp infer object, nhưng cũng tạo risk model dựa quá nhiều vào background shortcut thay vì object feature.

## Data Annotation

Bounding-box annotation rẻ hơn pixel mask nhưng vẫn có ambiguity:

```text
có tính shadow không?
box có bao gồm phần object bị cắt khỏi frame không?
object bị che quá nhiều có label không?
```

Annotation guideline cần nhất quán để model không học target mâu thuẫn.

## Real-Time Detection

Latency production gồm:

```text
preprocessing
+ model inference
+ NMS/post-processing
+ memory transfer
```

Không nên chỉ nhìn FLOPs của model. Với interactive hoặc edge system, batch-size-1 latency thường quan trọng hơn throughput benchmark.

## Liên hệ với Tracking

Detection trên mỗi frame chỉ tạo object độc lập theo thời gian.

Multi-object tracking bổ sung identity consistency giữa frame bằng motion, appearance embedding hoặc assignment algorithm.

## Open-Vocabulary Detection

Vision-language pretraining cho phép detector nhận text label ngoài một fixed closed-set taxonomy.

Challenge vẫn gồm localization, calibration và khả năng generalize tới concept chưa thấy trong training.

## Mô hình tư duy

> **Object Detection = classification trên candidate region + geometry estimation + cơ chế giải quyết duplicate hoặc set prediction.**

Các detector family khác nhau chủ yếu ở cách chúng tạo candidate, biểu diễn query và gán prediction với target.

## Những nhầm lẫn thường gặp

### “mAP cao nghĩa mọi object đều được detect đáng tin”

Không. Average metric có thể che lỗi theo class, object size hoặc subgroup.

### “NMS là một phần của learning”

Traditional NMS là post-processing heuristic. Một số modern architecture dùng set prediction để giảm hoặc loại bỏ nó.

### “Tăng resolution luôn giải quyết small object”

Không. Resolution cao hơn giúp nếu sensor còn information, nhưng làm compute/memory tăng mạnh và không thể khôi phục detail đã mất từ acquisition.

## Liên kết kiến thức

Object Detection kết hợp CNN/Transformer feature, geometry, matching algorithm và set prediction. Segmentation ở chapter tiếp theo chuyển từ bounding box sang cấu trúc ở cấp pixel.

Xem tiếp: [Image Segmentation](./06_image_segmentation.md).