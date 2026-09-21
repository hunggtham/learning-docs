# Multimodal Representation

**Multimodal AI (멀티모달 AI)** xử lý và liên kết nhiều modality như text, image, audio, video, sensor data. Thách thức không chỉ là có nhiều input; model phải học **representation tương thích** để biết thông tin nào tương ứng, bổ sung hay mâu thuẫn giữa modalities.

```text
text tokens
image patches
speech frames
video frames
sensor values
      ↓
modality encoders
      ↓
aligned / fused representations
      ↓
reasoning / generation / action
```

## Vì sao multimodal khó?

Mỗi modality có structure khác:

- text: discrete sequence, semantic dense;
- image: 2D spatial grid;
- audio: time-frequency signal;
- video: space + time;
- sensor: continuous irregular streams.

Sampling rates khác nhau rất lớn. Một câu 5 giây có vài chục text tokens nhưng audio có hàng chục nghìn samples và video có hàng trăm frames.

## Alignment

Alignment hỏi: phần nào của modality A tương ứng phần nào của modality B?

Examples:

```text
caption ↔ whole image
word ↔ image region
phoneme ↔ audio frames
subtitle ↔ video segment
gesture ↔ spoken phrase
```

Alignment có thể coarse hoặc fine-grained.

## Shared Embedding Space

Contrastive training đặt paired modalities gần nhau:

\[
sim(f_{img}(x),f_{text}(y))\uparrow
\]

Matched image-caption pair close, mismatched far.

Shared space useful retrieval/zero-shot transfer nhưng global embedding có thể lose detailed spatial alignment.

## Modality-Specific Encoders

Common architecture:

```text
vision encoder → visual tokens
speech encoder → audio tokens
text tokenizer/embedding → text tokens
```

Sau đó fusion layer/projector maps tokens vào compatible hidden dimension.

Encoders preserve modality inductive biases.

## Early, Intermediate, Late Fusion

**Early fusion** combine raw/low-level features early. Có high interaction nhưng khó vì scales/statistics khác.

**Intermediate fusion** encode each modality first then cross-attention/joint layers. Common in modern systems.

**Late fusion** combine final scores/embeddings. Simple/robust nhưng limited fine interaction.

## Cross-Attention

One modality queries another:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Text token có thể attend visual patches. Reverse direction cũng possible.

Cross-attention preserves modality separation while enabling interaction.

## Unified Token Space

Another approach converts modalities into tokens then process one Transformer:

```text
[image tokens][audio tokens][text tokens]
```

Unified architecture simplifies scaling but token counts and modality statistics require careful design.

## Modality Projector

Vision encoder dimension `D_v` và LLM hidden `D_l` khác. Projector:

\[
h_{llm}=Wh_v+b
\]

or small MLP maps representation. Simple projector can work surprisingly well if pretrained encoders already strong.

## Modality Gap

Even after same dimension, image/text feature distributions differ. Alignment training teaches language model how visual features correspond language concepts.

## Paired Data

Multimodal learning often relies paired data:

- image-caption;
- video-subtitle;
- speech-transcript;
- instruction + image + response.

Pair quality determines alignment. Web captions may describe only salient object, not every visual detail.

## Missing Modalities

Real systems may lack one modality. Architecture should handle:

```text
text only
image + text
image only
speech + text
```

Training only always-complete pairs may make model brittle.

## Complementary vs Redundant Information

Audio and video may both reveal speech; image and text may repeat same fact. Fusion should exploit complementarity without double-counting noisy correlated evidence.

## Conflicting Modalities

Image says red light, text metadata says green. Which source trusted? Model needs reliability/authority priors and application may need explicit source policy.

## Grounding

**Grounding (그라운딩 / neo nghĩa vào dữ liệu nguồn)** means connect language claim to specific perceptual evidence.

Examples:

- phrase “red cup” ↔ pixels/box;
- word timestamp ↔ audio frames;
- action “person opens door” ↔ video segment.

Global semantic alignment is not enough for precise grounding.

## Temporal Alignment

Video/audio interaction requires sync. Millisecond/second shifts can break lip-reading or event understanding.

Timestamp normalization and sampling pipeline become part of model quality.

## Multimodal Token Budget

Images/video can create thousands tokens. Context budget trade-off:

```text
higher visual resolution / more frames
→ more detail
→ more compute/context usage
```

Adaptive token selection/compression is important.

## Modality Compression

Perceiver/resampler modules compress many visual/audio tokens into smaller latent set before LLM. Compression must preserve task-relevant information.

## Representation Bottleneck

If projector compresses image into few tokens, OCR/small-detail info may disappear. Bigger LLM cannot recover information never passed through bottleneck.

## Pretraining Objectives

Possible objectives:

- contrastive alignment;
- image-text matching;
- caption generation;
- masked multimodal modeling;
- next-token prediction conditioned on visual/audio tokens;
- instruction following.

Objective shapes capability.

## Multimodal Hallucination

Model may generate object not present because language prior overwhelms visual evidence. Evaluation needs distinguish perception failure vs reasoning/generation failure.

## Mental Model

> **Multimodal representation is the problem of building interfaces between different measurement spaces so that corresponding information can interact without erasing modality-specific structure.**

## Common Misconceptions

### “Put image embedding into LLM = true multimodal understanding”

It enables interface, but grounding/detail capability depends alignment data, projector and training.

### “Shared embedding means all modalities have same meaning geometry”

Only to extent training objective aligns them.

### “More modalities always improve result”

Noisy/conflicting modalities can degrade output.

## Knowledge Connection

Multimodal representation connects [Modern Visual Representation](../12_computer_vision/08_modern_visual_representation.md), speech encoders, embeddings and attention.

Xem tiếp: [Vision-Language Models](./04_vision_language_models.md).