# Ảnh (image / 이미지) Segmentation

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Ảnh (image / 이미지) Segmentation**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Ngữ nghĩa (semantic / 의미적) Segmentation** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Encoder–Decoder kiến trúc (architecture / 아키텍처)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, **Encoder–Decoder kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **Ngữ nghĩa (semantic / 의미적) Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why Skip Connections Matter** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Ảnh (image / 이미지) Segmentation**, **Why Skip Connections Matter** tiếp nhận điểm tựa từ **Encoder–Decoder kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Upsampling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why Skip Connections Matter

Deep features biết “đây là car” nhưng spatial ranh giới (boundary / 경계) coarse. Early features có edges/location chi tiết. Skip connections combine ngữ nghĩa (semantics / 의미론) + localization.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ảnh (image / 이미지) Segmentation**, **Upsampling** tiếp nhận điểm tựa từ **Why Skip Connections Matter** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Segmentation mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Upsampling

Options:

- nearest/bilinear interpolation;
- transposed convolution;
- learned upsampling.

Transposed convolution có thể tạo checkerboard artifacts nếu kernel/stride tương tác (interaction / 상호작용) không tốt.

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, **Segmentation mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Upsampling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ranh giới (boundary / 경계) chất lượng (quality / 품질)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Ảnh (image / 이미지) Segmentation**, **Segmentation mất mát (loss / 손실)** đã nêu tiêu chí phân biệt, còn **Ranh giới (boundary / 경계) chất lượng (quality / 품질)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Instance Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ranh giới (boundary / 경계) chất lượng (quality / 품질)

Two masks có similar IoU nhưng ranh giới (boundary / 경계) hành vi (behavior / 동작) khác. Boundary-specific metrics/losses useful when contour precision matters, e.g. medical surgery or manufacturing.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ảnh (image / 이미지) Segmentation**, **Ranh giới (boundary / 경계) chất lượng (quality / 품질)** đã nêu tiêu chí phân biệt, còn **Instance Segmentation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Panoptic Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Instance Segmentation

Mask R-CNN extends detection:

```text
region proposal
→ class + box
→ per-instance mask head
```

Need assign pixels to distinct objects even if same lớp (class / 클래스) and overlapping.

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, **Panoptic Segmentation** tiếp nhận điểm tựa từ **Instance Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fully Convolutional Networks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Panoptic Segmentation

“Things” = countable instances như person/car.

“Stuff” = amorphous regions như sky/road/grass.

Panoptic segmentation seeks unified scene parse.

> **Chuyển mạch:** Ở chặng này của **Ảnh (image / 이미지) Segmentation**, **Fully Convolutional Networks** tiếp nhận điểm tựa từ **Panoptic Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Atrous/Dilated Convolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fully Convolutional Networks

FCN replaces dense classifier with convolutional operations to preserve spatial prediction and accept variable ảnh (image / 이미지) sizes more naturally.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ảnh (image / 이미지) Segmentation**, **Atrous/Dilated Convolution** tiếp nhận điểm tựa từ **Fully Convolutional Networks** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Scale ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Atrous/Dilated Convolution

Dilated convolution expands receptive trường dữ liệu (field / 필드) without reducing resolution. DeepLab-style architectures combine dilation + multi-scale ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, **Multi-Scale ngữ cảnh (context / 맥락)** tiếp nhận điểm tựa từ **Atrous/Dilated Convolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Transformer Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Scale ngữ cảnh (context / 맥락)

Điểm ảnh (pixel / 픽셀) định danh (identity / 식별자) may depend on larger scene. A tiny gray patch could be road, wall or car based on ngữ cảnh (context / 맥락). Pyramid pooling/ASPP capture multiple receptive-field scales.

> **Chuyển mạch:** Ở chặng này của **Ảnh (image / 이미지) Segmentation**, **Transformer Segmentation** tiếp nhận điểm tựa từ **Multi-Scale ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Promptable Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Transformer Segmentation

Vision transformers provide toàn cục (global / 전역) interactions. hiện đại (modern / 현대적) segmentation may use transformer encoder/decoder and mask queries, treating masks as set predictions similar DETR.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ảnh (image / 이미지) Segmentation**, **Promptable Segmentation** tiếp nhận điểm tựa từ **Transformer Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Annotation chi phí (cost / 비용)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Promptable Segmentation

Foundation segmentation các mô hình (models / 모델들) can accept points, boxes, masks or text-like prompts to specify mục tiêu (target / 대상) đối tượng (object / 객체)/region. This changes tương tác (interaction / 상호작용) from fixed taxonomy to **conditional segmentation**.

Still, mô hình (model / 모델) may thất bại (fail / 실패) on domain-specific imagery outside pretraining phân phối (distribution / 분포).

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, **Annotation chi phí (cost / 비용)** tiếp nhận điểm tựa từ **Promptable Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Lớp (class / 클래스) Imbalance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Annotation chi phí (cost / 비용)

Điểm ảnh (pixel / 픽셀) masks expensive. Strategies:

- polygons;
- weak labels;
- boxes/scribbles;
- pseudo-labeling;
- interactive annotation;
- foundation-model-assisted labeling.

Label chất lượng (quality / 품질) at boundaries can be subjective.

> **Chuyển mạch:** Ở chặng này của **Ảnh (image / 이미지) Segmentation**, **Lớp (class / 클래스) Imbalance** tiếp nhận điểm tựa từ **Annotation chi phí (cost / 비용)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Post-Processing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lớp (class / 클래스) Imbalance

Rare classes/small lesions can occupy tiny fraction. điểm ảnh (pixel / 픽셀) accuracy then misleading.

Use class-wise IoU, Dice, recall and region-level metrics.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ảnh (image / 이미지) Segmentation**, **Lớp (class / 클래스) Imbalance** xác định đầu vào; **Post-Processing** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **3D Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Post-Processing

Morphological cleanup, connected components, CRF-like refinement or lĩnh vực (domain / 도메인) các ràng buộc (constraints / 제약조건들) can remove isolated noise.

Môi trường vận hành (production / 운영 환경) segmentation often hybrid neural + deterministic hình học (geometry / 기하학).

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, **Post-Processing** xác định đầu vào; **3D Segmentation** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Temporal Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## 3D Segmentation

Medical CT/MRI uses volumes:

\[
X\in\mathbb{R}^{D\times H\times W\times C}
\]

3D convolutions capture volumetric ngữ cảnh (context / 맥락) but bộ nhớ (memory / 메모리) chi phí (cost / 비용) huge. 2.5D approaches tiến trình (process / 프로세스) slices with neighboring ngữ cảnh (context / 맥락).

> **Chuyển mạch:** Ở chặng này của **Ảnh (image / 이미지) Segmentation**, **Temporal Segmentation** tiếp nhận điểm tựa từ **3D Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temporal Segmentation

Video segmentation should preserve consistency across frames. Independent per-frame masks flicker; temporal các mô hình (models / 모델들)/tracking help.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ảnh (image / 이미지) Segmentation**, **Evaluation** tiếp nhận điểm tựa từ **Temporal Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bất định (uncertainty / 불확실성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation

Dùng chung (common / 공통) metrics:

- mIoU;
- Dice/F1;
- điểm ảnh (pixel / 픽셀) accuracy;
- ranh giới (boundary / 경계) F-score;
- panoptic chất lượng (quality / 품질).

Chỉ số (metric / 지표) choice depends ứng dụng (application / 애플리케이션). In medical imaging, missing small lesion may be much worse than slight ranh giới (boundary / 경계) mismatch.

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, **Bất định (uncertainty / 불확실성)** tiếp nhận điểm tựa từ **Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bất định (uncertainty / 불확실성)

Pixel-wise confidence maps can guide manual rà soát (review / 검토). But neighboring pixels correlated, so naive confidence interpretation may overstate certainty.

> **Chuyển mạch:** Ở chặng này của **Ảnh (image / 이미지) Segmentation**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Bất định (uncertainty / 불확실성)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Segmentation giữ spatial cấu trúc (structure / 구조) đến mức điểm ảnh (pixel / 픽셀); encoder học “cái gì”, decoder khôi phục “ở đâu chính xác”.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ảnh (image / 이미지) Segmentation**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “điểm ảnh (pixel / 픽셀) accuracy cao = segmentation tốt”

Background dominance có thể làm chỉ số (metric / 지표) cao dù rare đối tượng (object / 객체) thất bại (fail / 실패).

### “Segmentation mask là ground truth tuyệt đối”

Human annotation boundaries có bất định (uncertainty / 불확실성).

### “Upsampling phục hồi detail đã mất”

Nó chỉ reconstruct từ retained features/skip connections; thông tin (information / 정보) fully discarded không magically return.

> **Chuyển mạch:** Trong **Ảnh (image / 이미지) Segmentation**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Segmentation connects xử lý ảnh (image processing / 이미지 처리) masks, CNN multi-scale biểu diễn (representation / 표현), detection và transformer set prediction.

Xem tiếp: [Vision Transformers](./07_vision_transformers.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
