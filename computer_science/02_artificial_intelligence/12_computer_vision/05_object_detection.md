# Đối tượng (object / 객체) Detection

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Object detection**. Route đi từ object instances → bounding boxes → anchor/proposal or set prediction → IoU/NMS → precision–recall at multiple thresholds, để detection gắn classification với localization.

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

Detection phải vừa phân loại vừa định vị. Bounding boxes biến vị trí thành prediction có thể so sánh, rồi IoU đo mức overlap với ground truth.

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

Bounding boxes chuẩn hóa cách biểu diễn vị trí; IoU cung cấp tiêu chí định lượng để so khớp chúng với ground truth. Từ tiêu chí đó, ta có thể so sánh hai họ detector: two-stage và one-stage.

## Intersection over Union

**IoU (Intersection over Union / 교집합-합집합 비율)** đo overlap:

\[
IoU(A,B)=\frac{|A\cap B|}{|A\cup B|}
\]

IoU=1 perfect overlap; 0 no overlap.

IoU dùng cho matching predictions-ground truth và evaluation.

IoU đo chất lượng box nhưng không quyết định cách sinh ra box. Two-stage detectors tách proposal khỏi phân loại/tinh chỉnh; one-stage detectors đặt mục tiêu dự đoán dày đặc trong một lượt.

## Two-Stage Detectors

Family R-CNN:

```text
image → backbone features
→ region proposals
→ classify/refine each region
```

Faster R-CNN learns Region Proposal mạng (network / 네트워크). Two-stage methods historically strong accuracy, especially complex scenes.

Two-stage ưu tiên proposal có chọn lọc, còn one-stage đổi sự đơn giản và tốc độ lấy việc dự đoán dày đặc. Anchors là một cách cung cấp các hộp tham chiếu cho các dự đoán dày đặc đó.

## One-Stage Detectors

YOLO/SSD-style các mô hình (models / 모델들) predict classes/boxes densely in one pass:

```text
feature maps → dense box/class predictions
```

Thường faster and simpler triển khai (deployment / 배포).

One-stage detectors cần biểu diễn nhiều vị trí và kích thước trong feature map; anchors cung cấp các hình dạng khởi đầu để dự đoán offset. Objectness sau đó đánh giá vị trí nào có khả năng chứa vật thể.

## Anchors

Anchor-based detectors place predefined boxes of different scales/aspect ratios. mô hình (model / 모델) predicts offsets + objectness/classes relative anchors.

Anchor thiết kế (design / 설계) introduces hyperparameters and matching độ phức tạp (complexity / 복잡도).

Anchor-free detectors predict centers/corners/distances directly, reducing handcrafted anchor các giả định (assumptions / 가정들).

Anchors mô tả các ứng viên hình học, còn objectness tách câu hỏi “có vật thể hay không” khỏi câu hỏi về lớp. Trong huấn luyện, các ứng viên này phải được matching với ground-truth boxes theo một quy tắc rõ ràng.

## Objectness

Mô hình (model / 모델) often estimates xác suất (probability / 확률) location contains đối tượng (object / 객체) independent of lớp (class / 클래스). Final score may combine objectness + lớp (class / 클래스) xác suất (probability / 확률).

Objectness cho biết ứng viên nào đáng chú ý; matching quyết định ứng viên nào nhận tín hiệu positive, negative hoặc ignore. Các assignment đó dẫn trực tiếp đến mục tiêu box regression loss.

## Matching During huấn luyện (training / 학습)

Many candidate predictions must be assigned to ground-truth boxes. Assignment quy tắc (rule / 규칙) strongly affects tối ưu hóa (optimization / 최적화).

Old approaches use IoU thresholds; hiện đại (modern / 현대적) detectors may use động (dynamic / 동적) matching/cost-based assignment.

Matching xác định những cặp prediction–ground truth cần tối ưu; box regression loss đo sai lệch hình học của từng cặp. Bên cạnh sai lệch tọa độ, dense detection còn phải xử lý mất cân bằng giữa nền và vật thể.

## Box Regression mất mát (loss / 손실)

Coordinate L1/Smooth-L1 losses do not directly optimize overlap hình học (geometry / 기하학). IoU-based losses:

- IoU mất mát (loss / 손실);
- GIoU;
- DIoU;
- CIoU.

They incorporate spatial overlap/distance/aspect considerations.

Box loss cải thiện vị trí của các positive, nhưng số lượng background negative vẫn có thể áp đảo. Focal loss và các chiến lược cân bằng giảm ảnh hưởng đó; NMS xử lý một vấn đề khác ở đầu ra: các box trùng lặp.

## Lớp (class / 클래스) Imbalance

Dense detectors generate huge background negatives. **Focal mất mát (loss / 손실)** downweights easy examples:

\[
FL(p_t)=-(1-p_t)^\gamma\log p_t
\]

helping huấn luyện (training / 학습) focus hard positives/negatives.

Class imbalance được giải quyết trong tín hiệu huấn luyện, còn NMS là bước hậu xử lý để loại các dự đoán trùng nhau. Detection Transformers đặt lại bài toán bằng set prediction, giảm sự phụ thuộc vào các thủ tục hậu xử lý kiểu này.

## Non-Maximum Suppression

Dense detector may đầu ra (output / 출력) many overlapping boxes for same đối tượng (object / 객체). **NMS**:

1. sort boxes by score;
2. keep highest;
3. remove lower-score boxes with IoU above threshold;
4. repeat.

NMS is post-processing, not ngữ nghĩa (semantic / 의미적) lập luận (reasoning / 추론).

Soft-NMS decays scores instead of hard removal.

NMS chọn lọc các box sau dự đoán, còn DETR học trực tiếp một tập kết quả và dùng bipartite matching để phân biệt các phần tử. Dù theo cách nào, detector vẫn phải giữ thông tin ở nhiều độ phân giải để xử lý vật thể lớn và nhỏ.

## Detection Transformers

DETR reframes detection as **set prediction**. Transformer decoder uses đối tượng (object / 객체) queries and bipartite matching (Hungarian algorithm) between predicted set and ground truth.

This reduces need for anchors/NMS in cốt lõi (core / 핵심) formulation, though huấn luyện (training / 학습)/variants have their own độ phức tạp (complexity / 복잡도).

Detection Transformers giải quyết việc gán một tập prediction, nhưng chất lượng vẫn phụ thuộc vào biểu diễn không gian. Multi-scale features giữ lại độ phân giải cần thiết; mAP sau đó đánh giá đồng thời phân loại và localization.

## Multi-Scale Features

Small and large objects need different resolutions. tính năng (feature / 기능) Pyramid Networks combine high-level ngữ nghĩa (semantics / 의미론) with higher spatial resolution.

Small-object detection is especially sensitive to downsampling.

Multi-scale features hỗ trợ các kích thước vật thể khác nhau, còn mAP tổng hợp precision–recall dưới các ngưỡng IoU. Một tham số vận hành như NMS threshold có thể làm thay đổi các kết quả trước khi metric được tính.

## Mean Average Precision

Detection chỉ số (metric / 지표) usually AP/mAP. Precision-recall is computed under IoU criterion; COCO-style mAP averages over multiple IoU thresholds, rewarding localization chất lượng (quality / 품질) more strictly.

A detector can have high classification confidence but poor box localization.

MAP phản ánh cả chất lượng box và cách các dự đoán được giữ lại; NMS threshold vì thế tạo ra sự đánh đổi giữa bỏ sót và trùng lặp. Small objects là trường hợp đặc biệt dễ bị ảnh hưởng bởi các quyết định này.

## NMS Threshold sự đánh đổi (trade-off / 트레이드오프)

Threshold too low → suppress neighboring distinct objects.

Too high → duplicate detections remain.

Crowded scenes require careful handling.

NMS threshold điều chỉnh sự phân biệt giữa các box gần nhau; với small objects, vấn đề còn bắt đầu từ việc tín hiệu bị thu nhỏ qua feature map. Khi vật thể bị che khuất, ngay cả tín hiệu có độ phân giải cao cũng có thể trở nên mơ hồ.

## Small Objects

If đối tượng (object / 객체) becomes only a few feature-map cells, thông tin (information / 정보) nearly lost. Solutions:

- larger đầu vào (input / 입력) resolution;
- tính năng (feature / 기능) pyramids;
- tiling;
- small-object focused augmentation/dữ liệu (data / 데이터).

Compute chi phí (cost / 비용) rises significantly.

Small objects cần đủ chi tiết không gian để không biến mất trong downsampling; occlusion lại làm thiếu bằng chứng ngay cả khi độ phân giải còn đủ. Annotation policy phải ghi rõ cách xử lý các instance bị che để mô hình học cùng một tiêu chuẩn.

## Occlusion

Partial đối tượng (object / 객체) bằng chứng (evidence / 증거) can be ambiguous. ngữ cảnh (context / 맥락) may help, but mô hình (model / 모델) can over-rely on background/ngữ cảnh (context / 맥락) shortcuts.

Occlusion làm ranh giới box và sự tồn tại của instance trở nên không chắc chắn; annotation cần biến những quyết định đó thành quy tắc nhất quán. Khi quy tắc đã rõ, real-time detection còn phải cân cả chất lượng với độ trễ toàn pipeline.

## Dữ liệu (data / 데이터) Annotation

Box labels cheaper than điểm ảnh (pixel / 픽셀) masks but still subjective: should box include shadow? truncated đối tượng (object / 객체)? heavily occluded instance? Annotation chính sách (policy / 정책) must be consistent.

Annotation quyết định target mà detector học, còn real-time detection quyết định target đó có được đáp ứng trong thời gian cho phép hay không. Khi xử lý từng frame, tracking liên kết các detection qua thời gian để giữ identity ổn định.

## Real-Time Detection

Độ trễ (latency / 지연 시간) includes preprocessing + mô hình (model / 모델) + NMS + transfer, not mô hình (model / 모델) FLOPs alone. Batch kích thước (size / 크기) 1 độ trễ (latency / 지연 시간) matters edge/interactive các hệ thống (systems / 시스템들).

Real-time detection tối ưu quyết định trên từng frame, còn tracking dùng chuyển động và appearance để nối chúng thành một chuỗi identity. Open-vocabulary detection mở rộng không gian lớp mà detector có thể nhận từ đầu vào văn bản.

## Tracking liên kết (connection / 연결)

Detection per frame gives objects independently. Multi-object tracking adds định danh (identity / 식별자) consistency across thời gian (time / 시간) using motion/appearance association.

Tracking bổ sung identity theo thời gian nhưng không tự mở rộng taxonomy; open-vocabulary detection dùng biểu diễn ảnh–văn bản để tìm các khái niệm ngoài bộ lớp cố định. Mô hình tư duy tiếp theo gom detection thành ba phần: lớp, hình học và giải quyết trùng lặp.

## Open-Vocabulary Detection

Vision-language pretrained các mô hình (models / 모델들) enable detection conditioned on văn bản (text / 텍스트) labels beyond fixed closed-set taxonomy. Challenge remains localization and calibration for unseen concepts.

Open-vocabulary detection cho thấy classifier head không phải ranh giới duy nhất của detector; query, hình học và dữ liệu cũng quyết định khả năng nhận biết. Phần ngộ nhận chung sẽ kiểm tra những giới hạn này trong các tuyên bố thường gặp.

## Mô hình tư duy (mental model / 사고 모델)

> **đối tượng (object / 객체) Detection = classification over candidate regions + hình học (geometry / 기하학) estimation + duplicate/set resolution.**

Different detector families mainly differ in how they generate candidates, represent queries and assign predictions.

Mô hình tư duy tách việc nhận lớp, ước lượng hình học và xử lý tập kết quả; các ngộ nhận sau đây cho thấy vì sao không nên thay một phần bằng một chỉ số duy nhất. Phần liên kết kiến thức sẽ nối các thành phần ấy sang segmentation.

## Dùng chung (common / 공통) Misconceptions

### “High mAP means every đối tượng (object / 객체) reliably detected”

Average chỉ số (metric / 지표) hides lớp (class / 클래스)/kích thước (size / 크기)/subgroup failures.

### “NMS is part of học tập (learning / 학습)”

Traditional NMS is post-processing heuristic, though some hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) learn/set-predict to avoid it.

### “Higher đầu vào (input / 입력) resolution always solves small objects”

It helps but increases compute/bộ nhớ (memory / 메모리); sensor detail may already be absent.

Các ngộ nhận đã làm rõ rằng mAP, NMS và input resolution đều chỉ trả lời một phần của bài toán. Phần liên kết kiến thức đặt detection cạnh segmentation để tiếp tục từ box-level sang pixel-level structure.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Detection combines CNN/Transformer features, hình học (geometry / 기하학), matching algorithms and set prediction. Segmentation moves from boxes to pixel-level cấu trúc (structure / 구조).

Xem tiếp: [Image Segmentation](./06_image_segmentation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
