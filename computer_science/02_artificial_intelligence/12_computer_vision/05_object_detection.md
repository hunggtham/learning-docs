# Đối tượng (object / 객체) Detection

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Đối tượng (object / 객체) Detection**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Tại sao detection khó hơn classification?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bounding Boxes** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**đối tượng (object / 객체) Detection (객체 탐지)** vừa phải nhận biết đối tượng (object / 객체) lớp (class / 클래스), vừa phải localize nhiều instances trong cùng ảnh (image / 이미지). đầu ra (output / 출력) thường là set:

\[
\{(b_i,c_i,s_i)\}_{i=1}^N
\]

với bounding box `b_i`, lớp (class / 클래스) `c_i`, confidence `s_i`.

## Tại sao detection khó hơn classification?

Classification biết toàn ảnh (image / 이미지) thuộc lớp (class / 클래스) nào. Detection không biết trước:

- có bao nhiêu đối tượng (object / 객체);
- đối tượng (object / 객체) ở đâu;
- kích thước ra sao;
- overlaps/occlusion;
- background chiếm phần lớn ảnh (image / 이미지).

Do đó mô hình (model / 모델) phải solve localization + classification + variable-length đầu ra (output / 출력).

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, **Bounding Boxes** tiếp nhận điểm tựa từ **Tại sao detection khó hơn classification?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Intersection over Union** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bounding Boxes

Box có thể represent:

```text
(x_min, y_min, x_max, y_max)
```

hoặc:

```text
(center_x, center_y, width, height)
```

Coordinate normalization và ảnh (image / 이미지) resizing phải transform labels nhất quán.

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, **Intersection over Union** tiếp nhận điểm tựa từ **Bounding Boxes** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Two-Stage Detectors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Intersection over Union

**IoU (Intersection over Union / 교집합-합집합 비율)** đo overlap:

\[
IoU(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

IoU=1 perfect overlap; 0 no overlap.

IoU dùng cho matching predictions-ground truth và evaluation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối tượng (object / 객체) Detection**, **Two-Stage Detectors** tiếp nhận điểm tựa từ **Intersection over Union** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **One-Stage Detectors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Two-Stage Detectors

Family R-CNN:

```text
image → backbone features
→ region proposals
→ classify/refine each region
```

Faster R-CNN learns Region Proposal mạng (network / 네트워크). Two-stage methods historically strong accuracy, especially complex scenes.

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, **One-Stage Detectors** tiếp nhận điểm tựa từ **Two-Stage Detectors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Anchors** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## One-Stage Detectors

YOLO/SSD-style các mô hình (models / 모델들) predict classes/boxes densely in one pass:

```text
feature maps → dense box/class predictions
```

Thường faster and simpler triển khai (deployment / 배포).

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, **Anchors** tiếp nhận điểm tựa từ **One-Stage Detectors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Objectness** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Anchors

Anchor-based detectors place predefined boxes of different scales/aspect ratios. mô hình (model / 모델) predicts offsets + objectness/classes relative anchors.

Anchor thiết kế (design / 설계) introduces hyperparameters and matching độ phức tạp (complexity / 복잡도).

Anchor-free detectors predict centers/corners/distances directly, reducing handcrafted anchor các giả định (assumptions / 가정들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối tượng (object / 객체) Detection**, **Objectness** tiếp nhận điểm tựa từ **Anchors** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Matching During huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Objectness

Mô hình (model / 모델) often estimates xác suất (probability / 확률) location contains đối tượng (object / 객체) independent of lớp (class / 클래스). Final score may combine objectness + lớp (class / 클래스) xác suất (probability / 확률).

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, **Matching During huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Objectness** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Box Regression mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Matching During huấn luyện (training / 학습)

Many candidate predictions must be assigned to ground-truth boxes. Assignment quy tắc (rule / 규칙) strongly affects tối ưu hóa (optimization / 최적화).

Old approaches use IoU thresholds; hiện đại (modern / 현대적) detectors may use động (dynamic / 동적) matching/cost-based assignment.

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, **Box Regression mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Matching During huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lớp (class / 클래스) Imbalance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Box Regression mất mát (loss / 손실)

Coordinate L1/Smooth-L1 losses do not directly optimize overlap hình học (geometry / 기하학). IoU-based losses:

- IoU mất mát (loss / 손실);
- GIoU;
- DIoU;
- CIoU.

They incorporate spatial overlap/distance/aspect considerations.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối tượng (object / 객체) Detection**, **Lớp (class / 클래스) Imbalance** tiếp nhận điểm tựa từ **Box Regression mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Non-Maximum Suppression** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lớp (class / 클래스) Imbalance

Dense detectors generate huge background negatives. **Focal mất mát (loss / 손실)** downweights easy examples:

\[
FL(p_t)=-(1-p_t)^\gamma\log p_t
\]

helping huấn luyện (training / 학습) focus hard positives/negatives.

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, **Non-Maximum Suppression** tiếp nhận điểm tựa từ **Lớp (class / 클래스) Imbalance** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Detection Transformers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Non-Maximum Suppression

Dense detector may đầu ra (output / 출력) many overlapping boxes for same đối tượng (object / 객체). **NMS**:

1. sort boxes by score;
2. keep highest;
3. remove lower-score boxes with IoU above threshold;
4. repeat.

NMS is post-processing, not ngữ nghĩa (semantic / 의미적) lập luận (reasoning / 추론).

Soft-NMS decays scores instead of hard removal.

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, **Detection Transformers** tiếp nhận điểm tựa từ **Non-Maximum Suppression** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Scale Features** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Detection Transformers

DETR reframes detection as **set prediction**. Transformer decoder uses đối tượng (object / 객체) queries and bipartite matching (Hungarian algorithm) between predicted set and ground truth.

This reduces need for anchors/NMS in cốt lõi (core / 핵심) formulation, though huấn luyện (training / 학습)/variants have their own độ phức tạp (complexity / 복잡도).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối tượng (object / 객체) Detection**, **Multi-Scale Features** tiếp nhận điểm tựa từ **Detection Transformers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mean Average Precision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Scale Features

Small and large objects need different resolutions. tính năng (feature / 기능) Pyramid Networks combine high-level ngữ nghĩa (semantics / 의미론) with higher spatial resolution.

Small-object detection is especially sensitive to downsampling.

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, **Mean Average Precision** tiếp nhận điểm tựa từ **Multi-Scale Features** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **NMS Threshold sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mean Average Precision

Detection chỉ số (metric / 지표) usually AP/mAP. Precision-recall is computed under IoU criterion; COCO-style mAP averages over multiple IoU thresholds, rewarding localization chất lượng (quality / 품질) more strictly.

A detector can have high classification confidence but poor box localization.

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, **NMS Threshold sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Mean Average Precision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Small Objects** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## NMS Threshold sự đánh đổi (trade-off / 트레이드오프)

Threshold too low → suppress neighboring distinct objects.

Too high → duplicate detections remain.

Crowded scenes require careful handling.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối tượng (object / 객체) Detection**, **Small Objects** tiếp nhận điểm tựa từ **NMS Threshold sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Occlusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Small Objects

If đối tượng (object / 객체) becomes only a few feature-map cells, thông tin (information / 정보) nearly lost. Solutions:

- larger đầu vào (input / 입력) resolution;
- tính năng (feature / 기능) pyramids;
- tiling;
- small-object focused augmentation/dữ liệu (data / 데이터).

Compute chi phí (cost / 비용) rises significantly.

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, **Occlusion** tiếp nhận điểm tựa từ **Small Objects** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Annotation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Occlusion

Partial đối tượng (object / 객체) bằng chứng (evidence / 증거) can be ambiguous. ngữ cảnh (context / 맥락) may help, but mô hình (model / 모델) can over-rely on background/ngữ cảnh (context / 맥락) shortcuts.

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, **Occlusion** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Annotation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Real-Time Detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Annotation

Box labels cheaper than điểm ảnh (pixel / 픽셀) masks but still subjective: should box include shadow? truncated đối tượng (object / 객체)? heavily occluded instance? Annotation chính sách (policy / 정책) must be consistent.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối tượng (object / 객체) Detection**, **Dữ liệu (data / 데이터) Annotation** nêu điều cần giải thích; **Real-Time Detection** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Tracking liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Real-Time Detection

Độ trễ (latency / 지연 시간) includes preprocessing + mô hình (model / 모델) + NMS + transfer, not mô hình (model / 모델) FLOPs alone. Batch kích thước (size / 크기) 1 độ trễ (latency / 지연 시간) matters edge/interactive các hệ thống (systems / 시스템들).

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, sau nội dung của **Real-Time Detection**, **Tracking liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Open-Vocabulary Detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tracking liên kết (connection / 연결)

Detection per frame gives objects independently. Multi-object tracking adds định danh (identity / 식별자) consistency across thời gian (time / 시간) using motion/appearance association.

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, **Open-Vocabulary Detection** tiếp nhận điểm tựa từ **Tracking liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Open-Vocabulary Detection

Vision-language pretrained các mô hình (models / 모델들) enable detection conditioned on văn bản (text / 텍스트) labels beyond fixed closed-set taxonomy. Challenge remains localization and calibration for unseen concepts.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Đối tượng (object / 객체) Detection**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Open-Vocabulary Detection** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **đối tượng (object / 객체) Detection = classification over candidate regions + hình học (geometry / 기하학) estimation + duplicate/set resolution.**

Different detector families mainly differ in how they generate candidates, represent queries and assign predictions.

> **Chuyển mạch:** Trong **Đối tượng (object / 객체) Detection**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “High mAP means every đối tượng (object / 객체) reliably detected”

Average chỉ số (metric / 지표) hides lớp (class / 클래스)/kích thước (size / 크기)/subgroup failures.

### “NMS is part of học tập (learning / 학습)”

Traditional NMS is post-processing heuristic, though some hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) learn/set-predict to avoid it.

### “Higher đầu vào (input / 입력) resolution always solves small objects”

It helps but increases compute/bộ nhớ (memory / 메모리); sensor detail may already be absent.

> **Chuyển mạch:** Ở chặng này của **Đối tượng (object / 객체) Detection**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Detection combines CNN/Transformer features, hình học (geometry / 기하학), matching algorithms and set prediction. Segmentation moves from boxes to pixel-level cấu trúc (structure / 구조).

Xem tiếp: [Image Segmentation](./06_image_segmentation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
