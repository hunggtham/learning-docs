# Vision-Language Models

**Vision-Language Model (VLM / 비전-언어 모델)** kết hợp visual representation với language representation để xử lý tasks như image captioning, visual question answering, OCR-aware reasoning, grounded dialogue và image-text retrieval.

Một architecture phổ biến:

```text
image
→ vision encoder
→ visual tokens
→ projector / resampler
→ language model
→ text/tool output
```

## VLM không chỉ là image captioning

Captioning sinh mô tả toàn ảnh. VLM general hơn vì có thể nhận instruction + image, trả answer conditioned on both.

```text
Image + “What is the serial number?”
→ OCR/localization/reasoning
→ answer
```

Capability phụ thuộc encoder, visual token resolution, alignment training và LLM.

## Frozen Encoder + LLM

Một practical strategy:

1. dùng pretrained vision encoder;
2. dùng pretrained LLM;
3. train projector/alignment module;
4. instruction-tune multimodal data.

Điều này leverage strong unimodal models và giảm training cost.

## Visual Tokens

Vision encoder output patch features. Projector maps chúng vào LLM hidden dimension.

Question quan trọng:

- giữ bao nhiêu tokens?
- preserve 2D positions thế nào?
- có crop/high-res views không?
- compress bằng resampler không?

Token budget directly affects fine-detail perception.

## Image Resolution

Small text, tables, UI screenshots cần high resolution. Nếu model resize 4K screenshot xuống 224×224, OCR information mất trước reasoning.

Modern VLM có thể split image thành tiles/crops hoặc variable-resolution tokenization.

## OCR Capability

OCR-heavy tasks cần distinguish:

```text
visual object recognition
vs
text reading in image
```

A model good at natural photos may still fail documents/screenshots if pretraining lacks high-resolution text.

## Visual Question Answering

VQA requires answer questions grounded in image. Failure taxonomy:

- perception miss;
- localization miss;
- OCR miss;
- relation reasoning miss;
- language hallucination.

Debugging cần biết stage nào fail.

## Grounding

Grounded VLM có thể output boxes/points/regions linked to phrases. Text-only answer đúng nhưng point sai cho thấy semantic recognition không equal precise spatial grounding.

## Image Captioning

Caption objective:

\[
P(y|image)=\prod_t P(y_t|y_{<t},v)
\]

Caption can be fluent yet omit objects. Reference captions cũng incomplete, làm automatic metrics imperfect.

## Instruction Tuning

Multimodal instruction data:

```text
(image, instruction, answer)
```

teaches conversation/tool-style behavior. Synthetic data from stronger models can scale dataset but may propagate hallucinations/bias.

## Visual Chain Tasks

Examples:

- charts → read values → calculate;
- screenshot → identify button → plan click;
- diagram → trace relations → answer.

Need perception + structured reasoning. LLM strength cannot compensate for unreadable visual tokens.

## Charts and Tables

Charts require axis/legend/text parsing + geometry. Tables in images require cell structure. Dedicated parsers or OCR may outperform end-to-end VLM for exact extraction.

Hybrid architecture:

```text
VLM for semantic routing
+ OCR/table extractor for exact data
+ deterministic calculator
```

## Hallucination

VLM may name visually plausible but absent objects because language priors dominate uncertain vision evidence.

Grounded answer generation should encourage abstention/verification when visual evidence weak.

## Contrastive Pretraining vs Generative VLM

CLIP-style dual encoder good retrieval/zero-shot similarity but cannot directly generate detailed language. Generative VLM connects visual tokens to autoregressive language decoder.

These are different architecture/use cases.

## Multi-Image Context

Tasks may compare images, inspect before/after, analyze multiple pages. Model needs image identity/order and context budget allocation.

## Video Extension

Video VLM samples frames/clips. Too sparse misses brief events; too dense explodes tokens. Temporal ordering must be encoded.

## Evaluation

Need task-specific suites:

- VQA accuracy;
- OCR/document accuracy;
- grounding IoU/point accuracy;
- hallucination rate;
- chart/math exactness;
- robustness to resolution/crops;
- multilingual text in images.

LLM-as-judge useful for open answers but exact visual facts need deterministic/human verification.

## Security

Image can contain text prompt injection, QR links or malicious UI instructions. VLM should treat visual text as untrusted content, not system authority.

This matters for screen/browser agents.

## Accessibility

VLM can describe images for blind users, but hallucination risk means critical navigation/medical contexts need clear uncertainty and verification.

## Mental Model

> **A VLM is a language reasoner connected to a visual measurement pipeline. Its ceiling is bounded both by what the vision side preserves and what the language side can infer.**

## Common Misconceptions

### “If model can describe image, it understands exact geometry”

Global semantics and precise localization differ.

### “Bigger LLM fixes poor OCR”

If visual text lost in encoder/resizing, language model cannot reconstruct reliably.

### “Vision-language alignment means factual grounding guaranteed”

Alignment increases association, not truth guarantee.

## Knowledge Connection

VLM connects [Vision Transformers](../12_computer_vision/07_vision_transformers.md), LLMs, RAG-like grounding and multimodal context engineering.

Xem tiếp: [Multimodal Transformers](./05_multimodal_transformers.md).