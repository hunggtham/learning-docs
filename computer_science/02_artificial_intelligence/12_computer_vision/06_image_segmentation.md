# Ảnh (image / 이미지) Segmentation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Image segmentation**. Route đi từ pixel labels → semantic vs instance masks → encoder–decoder features → upsampling/boundaries → IoU/Dice and deployment cost, để output dense giữ được hình dạng đối tượng.

**ảnh (image / 이미지) Segmentation (이미지 분할)** gán label ở mức điểm ảnh (pixel / 픽셀) hoặc region. Nó trả lời không chỉ “có đối tượng (object / 객체) gì?” và “ở đâu?”, mà còn **điểm ảnh (pixel / 픽셀) nào thuộc đối tượng (object / 객체) nào**.

Có ba setting chính:

```text
Semantic Segmentation → mỗi pixel có class, không tách instance cùng class
Instance Segmentation → tách từng object instance + mask
Panoptic Segmentation → kết hợp semantic “stuff” + instance “things”
```

## Ngữ nghĩa (semantic / 의미적) Segmentation

Đầu vào (input / 입력):

\[
X\in\mathbb{R}^{H\times W\times C}
\]

Đầu ra (output / 출력) logits per điểm ảnh (pixel / 픽셀):

\[
Z\in\mathbb{R}^{H\times W\times K}
\]

Mỗi điểm ảnh (pixel / 픽셀) được classify vào one of `K` classes.


## Encoder–Decoder kiến trúc (architecture / 아키텍처)

Classification backbone downsample để học ngữ nghĩa (semantics / 의미론) nhưng mất spatial detail. Segmentation cần recover resolution.

Typical mẫu (pattern / 패턴):

```text
image
→ encoder: lower resolution, richer semantics
→ decoder: upsample + fuse details
→ pixel-wise prediction
```

U-Net là classic kiến trúc (architecture / 아키텍처) với skip connections nối encoder features high-resolution sang decoder.

Encoder–decoder khôi phục hình học, nhưng phần chi tiết được truyền qua skip connection mới quyết định ranh giới mask có sắc hay không.

## Why Skip Connections Matter

Deep features biết “đây là car” nhưng spatial ranh giới (boundary / 경계) coarse. Early features có edges/location chi tiết. Skip connections combine ngữ nghĩa (semantics / 의미론) + localization.

Khi đã giữ được chi tiết không gian, decoder vẫn phải phóng to feature map mà không tạo artefact.

## Upsampling

Options:

- nearest/bilinear interpolation;
- transposed convolution;
- learned upsampling.

Transposed convolution có thể tạo checkerboard artifacts nếu kernel/stride tương tác (interaction / 상호작용) không tốt.

Lựa chọn upsampling ảnh hưởng trực tiếp đến mask cuối; hàm mất mát sẽ biến sai lệch pixel và overlap thành tín hiệu để tối ưu lựa chọn đó.

## Segmentation mất mát (loss / 손실)

Pixel-wise cross-entropy:

\[
L=-\sum_{i} \log p_{i,y_i}
\]

Nhưng lớp (class / 클래스) imbalance rất severe: background có thể dominate.

Dice coefficient:

\[
Dice=\frac{2|P\cap G|}{|P|+|G|}
\]

Dice mất mát (loss / 손실) emphasizes overlap và useful medical/small-object segmentation.

IoU/Jaccard:

\[
IoU=\frac{|P\cap G|}{|P\cup G|}
\]

Các metric overlap chưa nói hết chất lượng contour, nên ranh giới cần được xem như một tiêu chí riêng.

## Ranh giới (boundary / 경계) chất lượng (quality / 품질)

Two masks có similar IoU nhưng ranh giới (boundary / 경계) hành vi (behavior / 동작) khác. Boundary-specific metrics/losses useful when contour precision matters, e.g. medical surgery or manufacturing. Khi contour đã rõ, bài toán tiếp theo là phân biệt các object cùng class thay vì gộp chúng vào một mask.


## Instance Segmentation

Mask R-CNN extends detection:

```text
region proposal
→ class + box
→ per-instance mask head
```

Need assign pixels to distinct objects even if same lớp (class / 클래스) and overlapping. Instance mask giải quyết từng object; panoptic segmentation mở rộng phạm vi sang cả vùng nền có ngữ nghĩa nhưng không có instance riêng.


## Panoptic Segmentation

“Things” = countable instances như person/car.

“Stuff” = amorphous regions như sky/road/grass.

Panoptic segmentation seeks unified scene parse. Để tạo dự đoán dày đặc cho scene parse, mạng cần giữ cấu trúc không gian trong suốt backbone thay vì nén thành một vector duy nhất.


## Fully Convolutional Networks

FCN replaces dense classifier with convolutional operations to preserve spatial prediction and accept variable ảnh (image / 이미지) sizes more naturally. FCN giữ dự đoán theo pixel; dilated convolution cho phép mở rộng vùng nhìn mà không phải giảm thêm độ phân giải.


## Atrous/Dilated Convolution

Dilated convolution expands receptive trường dữ liệu (field / 필드) without reducing resolution. DeepLab-style architectures combine dilation + multi-scale ngữ cảnh (context / 맥락). Một receptive field đơn lẻ vẫn có thể thiếu ngữ cảnh; pyramid pooling hoặc ASPP vì vậy kết hợp nhiều scale.


## Multi-Scale ngữ cảnh (context / 맥락)

Điểm ảnh (pixel / 픽셀) định danh (identity / 식별자) may depend on larger scene. A tiny gray patch could be road, wall or car based on ngữ cảnh (context / 맥락). Pyramid pooling/ASPP capture multiple receptive-field scales. Multi-scale context giúp pixel được diễn giải theo scene rộng hơn; transformer segmentation tiếp tục mô hình hóa các quan hệ toàn cục ấy.


## Transformer Segmentation

Vision transformers provide toàn cục (global / 전역) interactions. hiện đại (modern / 현대적) segmentation may use transformer encoder/decoder and mask queries, treating masks as set predictions similar DETR. Ngữ cảnh toàn cục cải thiện việc tách vùng liên quan, còn promptable segmentation cho phép người dùng chỉ rõ vùng hoặc object cần tách.


## Promptable Segmentation

Foundation segmentation các mô hình (models / 모델들) can accept points, boxes, masks or text-like prompts to specify mục tiêu (target / 대상) đối tượng (object / 객체)/region. This changes tương tác (interaction / 상호작용) from fixed taxonomy to **conditional segmentation**.

Still, mô hình (model / 모델) may thất bại (fail / 실패) on domain-specific imagery outside pretraining phân phối (distribution / 분포). Prompt làm thay đổi cách chỉ định mục tiêu, nhưng không loại bỏ chi phí tạo và kiểm tra các mask dùng cho huấn luyện.


## Annotation chi phí (cost / 비용)

Điểm ảnh (pixel / 픽셀) masks expensive. Strategies:

- polygons;
- weak labels;
- boxes/scribbles;
- pseudo-labeling;
- interactive annotation;
- foundation-model-assisted labeling.

Label chất lượng (quality / 품질) at boundaries can be subjective. Sự khác biệt về chất lượng nhãn thường rõ nhất ở lớp hiếm và vùng nhỏ, nơi mất cân bằng class dễ che khuất lỗi.


## Lớp (class / 클래스) Imbalance

Rare classes/small lesions can occupy tiny fraction. điểm ảnh (pixel / 픽셀) accuracy then misleading.

Use class-wise IoU, Dice, recall and region-level metrics. Metric theo class cho biết mô hình đang bỏ sót vùng nào; post-processing chỉ nên xử lý nhiễu hình học sau khi tín hiệu học đã được đánh giá đúng.


## Post-Processing

Morphological cleanup, connected components, CRF-like refinement or lĩnh vực (domain / 도메인) các ràng buộc (constraints / 제약조건들) can remove isolated noise.

Môi trường vận hành (production / 운영 환경) segmentation often hybrid neural + deterministic hình học (geometry / 기하학). Các quy tắc hình học này có thể áp dụng cho mask 2D; dữ liệu volume đòi hỏi tính thêm chiều sâu và ngân sách bộ nhớ.


## 3D Segmentation

Medical CT/MRI uses volumes:

\[
X\in\mathbb{R}^{D\times H\times W\times C}
\]

3D convolutions capture volumetric ngữ cảnh (context / 맥락) but bộ nhớ (memory / 메모리) chi phí (cost / 비용) huge. 2.5D approaches tiến trình (process / 프로세스) slices with neighboring ngữ cảnh (context / 맥락). Volume giữ ngữ cảnh không gian ba chiều, còn video đặt câu hỏi tương tự theo trục thời gian: mask có nhất quán giữa các frame hay không.


## Temporal Segmentation

Video segmentation should preserve consistency across frames. Independent per-frame masks flicker; temporal các mô hình (models / 모델들)/tracking help. Vì vậy đánh giá video không chỉ đo từng mask riêng lẻ mà còn xem độ ổn định của chuỗi dự đoán.


## Evaluation

Dùng chung (common / 공통) metrics:

- mIoU;
- Dice/F1;
- điểm ảnh (pixel / 픽셀) accuracy;
- ranh giới (boundary / 경계) F-score;
- panoptic chất lượng (quality / 품질).

Chỉ số (metric / 지표) choice depends ứng dụng (application / 애플리케이션). In medical imaging, missing small lesion may be much worse than slight ranh giới (boundary / 경계) mismatch. Metric phải phản ánh rủi ro của ứng dụng; confidence và uncertainty giúp tìm các dự đoán cần rà soát.


## Bất định (uncertainty / 불확실성)

Pixel-wise confidence maps can guide manual rà soát (review / 검토). But neighboring pixels correlated, so naive confidence interpretation may overstate certainty. Uncertainty không phải là bảo đảm đúng–sai tuyệt đối, nhưng là tín hiệu hữu ích để phân bổ việc kiểm tra và tạo mô hình tư duy đúng về segmentation.


## Mô hình tư duy (mental model / 사고 모델)

> **Segmentation giữ spatial cấu trúc (structure / 구조) đến mức điểm ảnh (pixel / 픽셀); encoder học “cái gì”, decoder khôi phục “ở đâu chính xác”.**

Mô hình này giúp kiểm tra các ngộ nhận về accuracy, ground truth và khả năng phục hồi chi tiết.

## Dùng chung (common / 공통) Misconceptions

### “điểm ảnh (pixel / 픽셀) accuracy cao = segmentation tốt”

Background dominance có thể làm chỉ số (metric / 지표) cao dù rare đối tượng (object / 객체) thất bại (fail / 실패).

### “Segmentation mask là ground truth tuyệt đối”

Human annotation boundaries có bất định (uncertainty / 불확실성).

### “Upsampling phục hồi detail đã mất”

Nó chỉ reconstruct từ retained features/skip connections; thông tin (information / 정보) fully discarded không magically return. Những giới hạn trên nối segmentation với xử lý ảnh, biểu diễn đa scale, detection và transformer set prediction.


## Liên kết kiến thức (knowledge connection / 지식 연결)

Segmentation connects xử lý ảnh (image processing / 이미지 처리) masks, CNN multi-scale biểu diễn (representation / 표현), detection và transformer set prediction.

Xem tiếp: [Vision Transformers](./07_vision_transformers.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
