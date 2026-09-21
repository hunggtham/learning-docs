# Vision Transformer

**Vision Transformer (ViT / 비전 트랜스포머)** áp dụng Transformer lên image bằng cách biến ảnh thành một sequence các **patch token**. Ý tưởng cốt lõi là giảm bớt inductive bias mạnh của convolution và dùng self-attention để học relation giữa các vùng ảnh ở phạm vi toàn cục.

## Patch Tokenization

Với image kích thước `H×W×C`, chia ảnh thành các patch `P×P`.

Số patch:

\[
N=\frac{HW}{P^2}
\]

Mỗi patch được flatten thành vector kích thước `P^2C`, sau đó đi qua linear projection:

\[
z_i = x_i W_E + b
\]

để tạo embedding dimension `D`.

```text
image
→ patch
→ patch embedding
→ positional information
→ Transformer encoder
→ task head
```

## Vì sao cần Positional Information?

Self-attention nguyên bản không tự biết patch nào nằm ở góc trên trái, giữa ảnh hay góc dưới phải nếu không có thông tin vị trí.

**Positional embedding** bổ sung spatial order cho sequence patch. Có thể dùng learned absolute position, relative position hoặc các biến thể 2D.

## CLS Token

ViT nguyên bản thêm một learnable `[CLS]` token vào đầu sequence. Sau Transformer encoder, representation của token này được dùng cho classification.

Một số architecture khác không dùng `[CLS]` mà dùng global average pooling trên patch feature.

## Self-Attention trong Image

Attention:

\[
A=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)
\]

cho phép mỗi patch tổng hợp information từ các patch khác.

Điểm mạnh là long-range interaction có thể xuất hiện ngay trong một layer, thay vì cần stack nhiều local convolution để receptive field dần mở rộng.

## Complexity

Memory và compute của full attention tăng gần theo:

\[
O(N^2)
\]

với `N` là số token.

Nếu patch nhỏ hoặc image resolution cao, `N` tăng rất nhanh.

Ví dụ khi tăng gấp đôi cả `H` và `W`, số patch tăng khoảng 4 lần, còn attention matrix có thể tăng khoảng 16 lần.

Do đó high-resolution ViT thường cần hierarchical, windowed hoặc sparse-attention variant.

## Inductive Bias của CNN và ViT

CNN hard-code nhiều prior hơn:

- locality;
- translation weight sharing;
- hierarchical spatial processing.

ViT hard-code ít hơn và để model học relation từ data nhiều hơn. Điều này từng khiến ViT cần large-scale pretraining để cạnh tranh với CNN khi data hạn chế.

Modern training recipe, augmentation và hybrid architecture đã thu hẹp khoảng cách này.

## Data Scale

Inductive bias yếu hơn đồng nghĩa model có thể cần nhiều data và regularization hơn để tự khám phá structure hữu ích.

Đây là một nguyên lý ML tổng quát:

> Prior mạnh thường giúp sample efficiency tốt hơn; prior yếu hơn có thể linh hoạt hơn khi data và compute đủ lớn.

## Hierarchical Vision Transformer

Model như Swin Transformer xử lý local window rồi merge patch qua nhiều stage:

```text
patch chi tiết
→ local attention
→ patch merging
→ feature hierarchy thô hơn
```

Cách này khôi phục multi-scale structure hữu ích cho detection và segmentation, đồng thời giảm quadratic cost của global attention.

## Windowed Attention

Thay vì cho mọi token attend mọi token khác, attention chỉ hoạt động trong local window.

**Shifted window** thay đổi vị trí window qua layer để thông tin có thể truyền giữa các vùng.

Đây là một trade-off gần với CNN: locality được đưa trở lại để tăng efficiency.

## Hybrid Model

Một architecture có thể dùng:

```text
CNN stem + Transformer body
```

hoặc thêm convolution bên trong Transformer block.

Mục tiêu là kết hợp local bias của convolution với global interaction của attention.

Modern vision architecture không còn đơn giản là “CNN hoặc Transformer”; nhiều hệ thống kết hợp cả hai.

## Masked Image Modeling

ViT rất phù hợp với masked-patch pretraining.

Pipeline có thể:

```text
che một phần lớn patch
→ encode phần còn lại
→ dự đoán pixel / feature / latent target bị che
```

Ý tưởng có nét giống masked language modeling, nhưng image có spatial redundancy lớn nên masking ratio và reconstruction objective thường khác NLP.

## Distillation

Teacher model có thể truyền class prediction hoặc representation signal sang ViT student.

Distillation giúp cải thiện data efficiency và đôi khi giúp model nhỏ giữ được phần capability của model lớn hơn.

## Detection với Transformer

DETR kết hợp visual feature với Transformer encoder–decoder và learned object query.

Detection được formulation thành **set prediction** thay vì pipeline dựa mạnh vào anchor và NMS truyền thống.

## Segmentation với Transformer

Patch feature có thể được decode thành mask.

Global context hỗ trợ scene parsing, trong khi multi-scale hoặc hierarchical feature vẫn cần thiết để giữ boundary và fine detail.

## Transfer sang Resolution khác

Nếu model dùng learned absolute positional embedding, fine-tuning ở image resolution khác có thể cần interpolate positional table.

Đây là một consequence trực tiếp của việc position được lưu bằng learned lookup thay vì công thức có thể extrapolate tùy ý.

## Attention Map

Visualization attention weight có thể cho thấy token nào tương tác mạnh với token nào.

Tuy nhiên attention map không phải causal explanation hoàn chỉnh. Prediction còn phụ thuộc nhiều head, nhiều layer, MLP và residual pathway.

## Trade-off của Patch Size

Patch lớn:

```text
ít token hơn
compute thấp hơn
fine detail kém hơn
```

Patch nhỏ:

```text
nhiều token hơn
compute cao hơn
local granularity tốt hơn
```

Patch size phù hợp phụ thuộc task, input resolution và hardware budget.

## Vision Transformer và Multimodal AI

Khi image được biến thành sequence embedding, representation của vision trở nên dễ kết nối với text token processing hơn.

Multimodal model có thể:

- encode image riêng rồi project visual feature vào LLM space;
- concatenate visual token với text token;
- dùng cross-attention giữa các modality.

ViT vì vậy là một bridge quan trọng giữa Computer Vision và vision-language model.

## Foundation Vision Model

Large pretrained visual encoder có thể học representation tái sử dụng cho classification, detection, segmentation và multimodal alignment.

Pretraining objective có thể là:

- supervised classification;
- contrastive learning;
- masked image modeling;
- image-text alignment;
- multimodal objective.

## Mô hình tư duy

> **ViT xem image như một sequence patch cần học relation ở nhiều khoảng cách; CNN xem image như spatial signal nơi locality và weight sharing được encode mạnh ngay trong architecture.**

## Những nhầm lẫn thường gặp

### “ViT không có spatial bias”

Không đúng. Patch layout, positional encoding, augmentation và architecture variant vẫn encode spatial structure.

### “Global attention luôn tốt hơn convolution”

Không. Global attention đắt và không phải task nào cũng cần mọi token tương tác toàn cục ở mọi layer.

### “Transformer đã thay thế CNN hoàn toàn”

Không. Modern vision system vẫn dùng CNN, Transformer và nhiều hybrid design.

## Liên kết kiến thức

Vision Transformer tái sử dụng [Attention](../06_deep_learning_architectures/04_attention.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md) trong spatial domain.

Xem tiếp: [Modern Visual Representation](./08_modern_visual_representation.md).