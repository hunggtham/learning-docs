# Modern Visual Representation

Modern Computer Vision ngày càng ít xoay quanh một task head riêng lẻ và ngày càng tập trung vào **general-purpose visual representations** có thể transfer sang classification, retrieval, detection, segmentation và multimodal reasoning.

Điểm chuyển paradigm:

```text
Task-specific supervised model
        ↓
Large pretrained visual encoder
        ↓
adapt / prompt / fine-tune for many tasks
```

## Self-Supervised Learning

Image labels đắt nhưng raw images abundant. Self-supervised methods tạo supervision từ chính data.

Hai family lớn:

```text
contrastive / alignment objectives
masked / reconstruction objectives
```

## Contrastive Learning

Hai augmented views từ cùng image được coi positive pair; views khác là negatives hoặc implicitly separated.

Goal:

\[
sim(z_i,z_i^+) \uparrow
\]

\[
sim(z_i,z_j^-) \downarrow
\]

Representation được học để invariant với augmentations chosen.

Vì vậy augmentation policy là part of supervision.

## SimCLR Intuition

Pipeline:

```text
image
→ two random augmentations
→ shared encoder
→ projection head
→ contrastive loss
```

Large batch cung cấp many negatives trong original formulation.

## Momentum / Teacher Encoders

Methods như MoCo/BYOL/DINO-style families dùng target/momentum teacher, queues hoặc self-distillation để stabilize representation learning.

Điểm conceptual: learner match a slowly changing target representation thay vì labels manual.

## Avoiding Collapse

Nếu encoder output same vector cho all images, alignment objective trivial. Different methods prevent collapse bằng:

- negatives;
- stop-gradient;
- predictor asymmetry;
- variance/covariance constraints;
- teacher centering/sharpening.

## Masked Image Modeling

Mask nhiều patches rồi reconstruct:

```text
visible patches → encoder → decoder → predict missing content/features
```

MAE-style methods mask high ratio vì neighboring image patches redundant.

Target có thể raw pixels hoặc learned feature tokens.

## Supervised vs Self-Supervised Representation

Supervised ImageNet training pushes features toward provided classes. Self-supervised objectives có thể preserve broader visual information useful tasks beyond taxonomy.

Không có guarantee self-supervised always better; objective/data scale matter.

## Vision–Language Pretraining

CLIP-style training uses paired `(image,text)`.

Image encoder produces `v`; text encoder produces `t`. Contrastive objective makes matched pairs similar in shared space.

```text
image ↔ caption
```

This creates **open-vocabulary semantic interface**: new label can be represented by text prompt rather than fixed classifier ID.

## Zero-Shot Classification

Compute image embedding `v`, text embeddings for prompts:

```text
"a photo of a cat"
"a photo of a dog"
...
```

select highest similarity.

No task-specific classifier training required, though prompt templates and domain shift affect quality.

## Semantic Retrieval

Shared embedding space enables:

```text
text query → retrieve images
image query → retrieve text/images
```

This is multimodal information retrieval.

## Open-Vocabulary Vision

Detection/segmentation can replace fixed class head with text-conditioned embeddings. Model can localize concepts specified by natural language.

Challenge: text-image pretraining may learn broad semantics but weak precise localization; extra objectives/architectures needed.

## Foundation Models for Segmentation

Promptable segmentation separates target specification from mask generation. Input prompts may be points, boxes or masks.

This turns segmentation into general interactive capability rather than fixed class taxonomy.

## Visual Tokenizers

Generative image models may encode image into discrete/continuous latent tokens using VAE/VQ-style encoder. Transformer/diffusion operates in latent space instead of raw pixels.

Latent representation reduces compute while hopefully preserving perceptual semantics.

## Diffusion Representation

Diffusion models are generative, but intermediate features can also contain semantic structure useful downstream. Generative training can produce representations, though objective differs discriminative contrastive training.

## Image Embedding Geometry

Cosine similarity useful only because training aligns geometry to semantics. Embedding is not universal semantic truth.

Different encoders place concepts differently depending data/objective.

## Fine-Tuning Strategies

Pretrained visual model can adapt via:

```text
linear probe
full fine-tuning
partial unfreezing
adapters / LoRA-like methods
prompt tuning
```

Choice depends data size, compute and domain gap.

## Domain-Specific Foundation Models

Medical, satellite, industrial imagery differ strongly from web photos. Domain pretraining often required because texture, scale, sensor and label semantics differ.

## Data Curation

At foundation-model scale, data quality matters:

- duplicates;
- low-quality captions;
- NSFW/sensitive data;
- geographic/cultural imbalance;
- copyright/licensing;
- benchmark leakage.

Representation inherits dataset bias.

## Evaluation Beyond Classification

Good representation should be tested on multiple tasks:

- linear probing;
- retrieval;
- few-shot transfer;
- robustness;
- localization;
- cross-domain transfer.

A single benchmark can overfit architecture/data choices.

## Visual Reasoning

Strong visual encoder is not same as reasoning model. VLM needs connect perception features with language/reasoning layers. Failure can arise because object not perceived, relation lost, OCR weak or reasoning wrong.

## Multimodal Bridge

Common architecture:

```text
image
→ vision encoder
→ visual tokens
→ projector / cross-attention
→ language model
→ text/tool output
```

The projector aligns visual feature dimension/distribution with language model interface.

## Temporal Vision

Video adds time. A frame-only visual encoder misses motion/action relationships. Video representation uses temporal sampling, 3D conv, temporal attention or factorized space-time models.

## Spatial Grounding

Multimodal assistant that describes image globally may still fail exact coordinate grounding. Grounded vision-language models need explicit spatial training/tasks.

## Mental Model

> **Modern vision foundation models học một visual coordinate system reusable; multimodal AI nối coordinate system đó với language/action spaces.**

## Common Misconceptions

### “CLIP understands everything visually because it supports zero-shot labels”

Alignment quality limited by pretraining pairs and can miss fine spatial details/counting/OCR.

### “Foundation model eliminates domain data”

Domain validation/adaptation vẫn cần, đặc biệt medical/industrial.

### “Embedding similarity proves objects same”

Similarity reflects model objective/data, not ontological identity.

## Knowledge Connection

Modern visual representation là bridge trực tiếp sang `13_speech_audio_and_multimodal/`, nơi image tokens, audio representations và text tokens được kết hợp trong shared or connected representation spaces.