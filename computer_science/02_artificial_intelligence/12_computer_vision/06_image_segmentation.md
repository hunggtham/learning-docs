# Image Segmentation

**Phân đoạn ảnh (Image Segmentation / 이미지 분할)** gán label ở mức pixel hoặc region. Nó không chỉ trả lời “có object gì?” và “object ở đâu?”, mà còn xác định **pixel nào thuộc object hoặc vùng nào**.

Có ba setting chính:

```text
Semantic Segmentation → mỗi pixel có class, không tách các instance cùng class
Instance Segmentation → tách từng object instance và mask riêng
Panoptic Segmentation → kết hợp semantic “stuff” và instance “things”
```

## Semantic Segmentation

Input:

\[
X\in\mathbb{R}^{H\times W\times C}
\]

Output logits cho mỗi pixel:

\[
Z\in\mathbb{R}^{H\times W\times K}
\]

Mỗi pixel được classify vào một trong `K` class.

## Encoder–Decoder Architecture

Classification backbone thường downsample để học semantic feature mạnh hơn, nhưng quá trình đó làm mất spatial detail.

Segmentation cần khôi phục resolution để dự đoán ở mức pixel.

Pattern điển hình:

```text
image
→ encoder: resolution thấp hơn, semantics mạnh hơn
→ decoder: upsample + kết hợp detail
→ pixel-wise prediction
```

U-Net là architecture kinh điển với skip connection nối high-resolution feature từ encoder sang decoder.

## Vì sao Skip Connection quan trọng?

Deep feature có thể biết “đây là car” nhưng boundary thường coarse vì spatial resolution đã giảm.

Feature ở layer sớm giữ edge và location detail tốt hơn.

Skip connection kết hợp:

```text
semantics mạnh từ layer sâu
+
localization detail từ layer sớm
```

## Upsampling

Các lựa chọn phổ biến:

- nearest hoặc bilinear interpolation;
- transposed convolution;
- learned upsampling.

Transposed convolution có thể tạo checkerboard artifact nếu interaction giữa kernel và stride không phù hợp.

Upsampling không tự tái tạo information đã bị mất hoàn toàn; nó chỉ xây lại spatial output từ feature còn giữ được.

## Segmentation Loss

Pixel-wise cross-entropy:

\[
L=-\sum_{i} \log p_{i,y_i}
\]

Nhưng class imbalance thường rất mạnh vì background có thể chiếm phần lớn pixel.

Dice coefficient:

\[
Dice=\frac{2|P\cap G|}{|P|+|G|}
\]

Dice loss tập trung vào overlap nên đặc biệt hữu ích trong medical hoặc small-object segmentation.

IoU/Jaccard:

\[
IoU=\frac{|P\cap G|}{|P\cup G|}
\]

## Chất lượng Boundary

Hai mask có IoU gần nhau nhưng boundary behavior có thể rất khác.

Nếu contour precision quan trọng, ví dụ surgical planning hoặc industrial inspection, nên dùng thêm boundary-specific loss hoặc metric.

## Instance Segmentation

Mask R-CNN mở rộng object detection:

```text
region proposal
→ class + box
→ mask head cho từng instance
```

Bài toán khó hơn semantic segmentation vì phải tách hai object cùng class nhưng nằm cạnh hoặc overlap nhau.

## Panoptic Segmentation

“Things” là object đếm được như person hoặc car.

“Stuff” là region không có instance rõ như sky, road hoặc grass.

Panoptic segmentation cố tạo một unified scene parse gồm cả hai loại.

## Fully Convolutional Network

**Fully Convolutional Network (FCN)** thay dense classifier bằng convolutional operation để giữ spatial output và hỗ trợ image size linh hoạt hơn.

Đây là bước quan trọng trong lịch sử deep segmentation.

## Atrous / Dilated Convolution

Dilated convolution tăng receptive field mà không giảm resolution mạnh.

DeepLab-style architecture kết hợp dilation với multi-scale context để vừa giữ detail vừa nhìn region rộng.

## Multi-Scale Context

Identity của một pixel có thể phụ thuộc scene rộng hơn.

Một gray patch nhỏ có thể là road, wall hoặc car tùy surrounding context.

Pyramid pooling hoặc ASPP thu thập feature ở nhiều receptive-field scale để giải bài toán này.

## Transformer Segmentation

Vision Transformer cho phép global interaction giữa patch.

Modern segmentation system có thể dùng transformer encoder/decoder và mask query, biến segmentation thành một dạng set prediction tương tự DETR.

## Promptable Segmentation

Foundation segmentation model có thể nhận point, box, mask hoặc text-like prompt để chỉ định region cần segment.

Điều này chuyển bài toán từ fixed taxonomy sang **conditional segmentation**.

Tuy nhiên model vẫn có thể fail khi domain image khác xa pretraining distribution, ví dụ industrial hoặc medical imagery đặc thù.

## Annotation Cost

Pixel mask rất tốn công annotate. Các strategy giảm chi phí gồm:

- polygon;
- weak label;
- box hoặc scribble;
- pseudo-labeling;
- interactive annotation;
- foundation-model-assisted labeling.

Boundary label cũng có thể mang tính chủ quan giữa annotator.

## Class Imbalance

Rare class hoặc small lesion có thể chỉ chiếm phần rất nhỏ image.

Pixel accuracy lúc đó dễ gây hiểu nhầm vì chỉ cần predict background tốt cũng đạt score cao.

Nên xem class-wise IoU, Dice, recall và region-level metric.

## Post-Processing

Morphological cleanup, connected component, CRF-like refinement hoặc domain constraint có thể loại isolated noise và enforce geometry hợp lý.

Production segmentation thường là hybrid giữa neural prediction và deterministic post-processing.

## 3D Segmentation

Medical CT/MRI dùng volume:

\[
X\in\mathbb{R}^{D\times H\times W\times C}
\]

3D convolution capture volumetric context nhưng memory cost rất lớn.

2.5D approach dùng slice hiện tại cùng một số neighboring slice để giảm cost nhưng vẫn giữ thêm context theo depth.

## Temporal Segmentation

Video segmentation cần consistency qua frame.

Nếu infer từng frame độc lập, mask có thể flicker. Temporal model, optical flow hoặc tracking giúp giữ identity và shape ổn định hơn.

## Evaluation

Metric phổ biến:

- mIoU;
- Dice/F1;
- pixel accuracy;
- boundary F-score;
- panoptic quality.

Metric phải phù hợp failure cost. Trong medical imaging, bỏ sót một lesion nhỏ có thể nghiêm trọng hơn boundary lệch vài pixel.

## Uncertainty

Pixel-wise confidence map có thể giúp chọn region cần manual review.

Tuy nhiên pixel lân cận có correlation cao, nên không nên hiểu confidence từng pixel như các independent probability.

## Mô hình tư duy

> **Segmentation giữ spatial structure tới cấp pixel; encoder học “cái gì”, decoder khôi phục “ở đâu chính xác”.**

## Những nhầm lẫn thường gặp

### “Pixel accuracy cao nghĩa segmentation tốt”

Không. Background dominance có thể làm metric cao dù rare object gần như luôn bị bỏ sót.

### “Segmentation mask là ground truth tuyệt đối”

Không. Human annotation boundary có uncertainty và guideline khác nhau có thể tạo mask khác nhau.

### “Upsampling phục hồi detail đã mất”

Không hoàn toàn. Nó chỉ reconstruct từ feature còn giữ được hoặc skip connection; information đã bị discard hoàn toàn không tự quay lại.

## Liên kết kiến thức

Segmentation nối image-processing mask, CNN multi-scale representation, object detection và Transformer set prediction.

Xem tiếp: [Vision Transformer](./07_vision_transformers.md).