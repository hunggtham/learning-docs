# Vision Transformers

**Vision Transformer (ViT / 비전 트랜스포머)** áp dụng Transformer lên images bằng cách biến image thành sequence của patch tokens. Ý tưởng cốt lõi là thay inductive bias convolution mạnh bằng self-attention có khả năng model interactions toàn cục.

## Patch Tokenization

Với image `H×W×C`, chia thành patches `P×P`.

Số patches:

\[
N=\frac{HW}{P^2}
\]

Mỗi patch flatten thành vector size `P^2C`, sau đó linear projection:

\[
z_i = x_i W_E + b
\]

thành embedding dimension `D`.

```text
image
→ patches
→ patch embeddings
→ positional information
→ Transformer encoder
→ task head
```

## Vì sao cần Positional Information?

Self-attention nguyên bản không biết patch nào ở top-left hay bottom-right nếu không encode position.

Positional embeddings thêm spatial order. Có thể learned absolute, relative hoặc 2D variants.

## CLS Token

Original ViT thêm learnable `[CLS]` token vào sequence. Sau encoder, representation của token này dùng cho classification.

Alternatives dùng global average pooling trên patch features.

## Self-Attention trong Image

Attention:

\[
A=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)
\]

cho mỗi patch aggregate information từ mọi patch khác.

Điểm mạnh: long-range interactions accessible ngay một layer, không cần stack many local convs để receptive field lan rộng.

## Complexity

Attention memory/compute theo số tokens gần:

\[
O(N^2)
\]

Nếu patch size nhỏ hoặc high-resolution image, `N` tăng nhanh.

Ví dụ doubling both H and W → patches ~4× → attention matrix ~16×.

Do đó high-resolution ViT cần hierarchical/windowed/sparse attention variants.

## CNN vs ViT Inductive Bias

CNN hard-code:

- locality;
- translation weight sharing;
- hierarchical spatial processing.

ViT hard-code ít hơn, cho model learn relations from data. Điều này từng khiến ViT cần large-scale pretraining hơn CNN, nhưng modern training/augmentation architectures thu hẹp gap.

## Data Scale

Weaker inductive bias means model may need more data/regularization to discover useful structure. Large pretraining giúp ViT shine.

Đây là example của general ML principle:

> stronger prior → potentially better sample efficiency; weaker prior → more flexibility if data/compute abundant.

## Hierarchical Vision Transformers

Models như Swin process local windows và merge patches over stages:

```text
fine patches
→ local attention
→ patch merging
→ coarser feature hierarchy
```

Điều này recover multi-scale structure useful detection/segmentation và reduce quadratic cost.

## Windowed Attention

Attention chỉ trong local windows giảm complexity. Shifted windows allow cross-window communication across layers.

Trade-off gần CNN: locality introduced lại để gain efficiency.

## Hybrid Models

CNN stem + Transformer body hoặc convolution inside transformer block kết hợp local bias và global attention.

Modern vision architectures không còn binary CNN vs Transformer; ideas mix widely.

## Masked Image Modeling

ViT naturally supports masked-patch pretraining. Hide large fraction patches, train reconstruct pixels/features/latent targets.

This resembles masked language modeling nhưng image patches have high redundancy, nên masking ratios/objectives khác NLP.

## Distillation

Teacher model can transfer class/representation signals to ViT, improving data efficiency.

## Detection with Transformers

DETR uses CNN/ViT-like features + Transformer encoder-decoder + learned object queries. Detection becomes set prediction rather than anchor/NMS pipeline.

## Segmentation with Transformers

Patch features can be decoded into masks. Global context helps scene parsing; multi-scale/hierarchical features important boundary/detail.

## Position Resolution Transfer

Fine-tuning at different image resolution may require interpolate positional embeddings if using absolute positions.

This is an implementation consequence of learned positional table.

## Attention Maps

Visualizing attention weights can show token interaction but should not be treated as exact causal explanation. Multiple heads/layers and residual pathways contribute.

## Patch Size Trade-off

Large patch:

```text
fewer tokens
lower compute
less fine detail
```

Small patch:

```text
more tokens
higher compute
better local granularity
```

Task and hardware determine sweet spot.

## Vision Transformer và Multimodal AI

Once image becomes sequence of embeddings, architecture aligns naturally with text token processing. Multimodal models can:

- encode image separately then project into LLM space;
- concatenate visual tokens with text tokens;
- use cross-attention between modalities.

ViT therefore is a core bridge to vision-language models.

## Foundation Vision Models

Large pretrained visual encoders learn representations transferable across classification, detection, segmentation and multimodal alignment. Pretraining objectives may be supervised, contrastive, masked or multimodal.

## Mental Model

> **ViT xem image như một set/sequence patches cần học relation toàn cục; CNN xem image như một spatial signal nơi local pattern sharing được hard-code mạnh hơn.**

## Common Misconceptions

### “ViT không có spatial bias”

Patch layout, positional encoding, augmentations và architecture variants vẫn encode spatial structure.

### “Attention global nên luôn tốt hơn convolution”

Global attention expensive và không phải mọi task cần global relation ở mọi layer.

### “Transformer đã thay CNN hoàn toàn”

Modern systems sử dụng cả hai families và hybrid designs.

## Knowledge Connection

Vision Transformer reuses [Attention](../06_deep_learning_architectures/04_attention.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md) trong spatial domain.

Xem tiếp: [Modern Visual Representation](./08_modern_visual_representation.md).