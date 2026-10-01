# Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Self-Supervised học tập (learning / 학습)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Contrastive học tập (learning / 학습)** để soi ranh giới và điểm dễ nhầm. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Hiện đại (modern / 현대적) Computer Vision ngày càng ít xoay quanh một tác vụ (task / 작업) head riêng lẻ và ngày càng tập trung vào **general-purpose visual representations** có thể transfer sang classification, retrieval, detection, segmentation và multimodal lập luận (reasoning / 추론).

Điểm chuyển paradigm:

```text
Task-specific supervised model
        ↓
Large pretrained visual encoder
        ↓
adapt / prompt / fine-tune for many tasks
```

## Self-Supervised học tập (learning / 학습)

Ảnh (image / 이미지) labels đắt nhưng raw images abundant. Self-supervised methods tạo supervision từ chính dữ liệu (data / 데이터).

Hai family lớn:

```text
contrastive / alignment objectives
masked / reconstruction objectives
```

> **Chuyển mạch:** Self-supervised learning tạo target từ data; contrastive learning tổ chức positive/negative pairs trong representation space, và SimCLR minh họa cách augmentation định nghĩa identity.

## Contrastive học tập (learning / 학습)

Hai augmented views từ cùng ảnh (image / 이미지) được coi positive pair; views khác là negatives hoặc implicitly separated.

Goal:

\[
sim(z_i,z_i^+) \uparrow
\]

\[
sim(z_i,z_j^-) \downarrow
\]

Biểu diễn (representation / 표현) được học để bất biến (invariant / 불변식) với augmentations chosen.

Vì vậy augmentation chính sách (policy / 정책) là part of supervision.

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Contrastive học tập (learning / 학습)** đã nêu tiêu chí phân biệt, còn **SimCLR Intuition** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Momentum / Teacher Encoders** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## SimCLR Intuition

Chuỗi xử lý (pipeline / 파이프라인):

```text
image
→ two random augmentations
→ shared encoder
→ projection head
→ contrastive loss
```

Large batch cung cấp many negatives trong original formulation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Momentum / Teacher Encoders** tiếp nhận điểm tựa từ **SimCLR Intuition** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Avoiding Collapse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Momentum / Teacher Encoders

Methods như MoCo/BYOL/DINO-style families dùng mục tiêu (target / 대상)/momentum teacher, queues hoặc self-distillation để stabilize biểu diễn (representation / 표현) học tập (learning / 학습).

Điểm conceptual: learner match a slowly changing mục tiêu (target / 대상) biểu diễn (representation / 표현) thay vì labels manual.

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Avoiding Collapse** tiếp nhận điểm tựa từ **Momentum / Teacher Encoders** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Masked ảnh (image / 이미지) Modeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Avoiding Collapse

Nếu encoder đầu ra (output / 출력) same véc-tơ (vector / 벡터) cho all images, alignment mục tiêu (objective / 목표) trivial. Different methods prevent collapse bằng:

- negatives;
- stop-gradient;
- predictor asymmetry;
- variance/covariance các ràng buộc (constraints / 제약조건들);
- teacher centering/sharpening.

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Masked ảnh (image / 이미지) Modeling** tiếp nhận điểm tựa từ **Avoiding Collapse** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Supervised vs Self-Supervised biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Masked ảnh (image / 이미지) Modeling

Mask nhiều patches rồi reconstruct:

```text
visible patches → encoder → decoder → predict missing content/features
```

MAE-style methods mask high ratio vì neighboring ảnh (image / 이미지) patches redundant.

Mục tiêu (target / 대상) có thể raw pixels hoặc learned tính năng (feature / 기능) tokens.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Supervised vs Self-Supervised biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **Masked ảnh (image / 이미지) Modeling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vision–ngôn ngữ (language / 언어) Pretraining** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Supervised vs Self-Supervised biểu diễn (representation / 표현)

Supervised ImageNet huấn luyện (training / 학습) pushes features toward provided classes. Self-supervised objectives có thể preserve broader visual thông tin (information / 정보) useful tasks beyond taxonomy.

Không có guarantee self-supervised always better; mục tiêu (objective / 목표)/dữ liệu (data / 데이터) quy mô (scale / 규모) matter.

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Vision–ngôn ngữ (language / 언어) Pretraining** tiếp nhận điểm tựa từ **Supervised vs Self-Supervised biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Zero-Shot Classification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vision–ngôn ngữ (language / 언어) Pretraining

CLIP-style huấn luyện (training / 학습) uses paired `(image,text)`.

Ảnh (image / 이미지) encoder produces `v`; văn bản (text / 텍스트) encoder produces `t`. Contrastive mục tiêu (objective / 목표) makes matched pairs similar in dùng chung (shared / 공유) không gian (space / 공간).

```text
image ↔ caption
```

This creates **open-vocabulary ngữ nghĩa (semantic / 의미적) giao diện (interface / 인터페이스)**: new label can be represented by văn bản (text / 텍스트) prompt rather than fixed classifier ID.

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Zero-Shot Classification** tiếp nhận điểm tựa từ **Vision–ngôn ngữ (language / 언어) Pretraining** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ nghĩa (semantic / 의미적) Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Zero-Shot Classification

Compute ảnh (image / 이미지) embedding `v`, văn bản (text / 텍스트) embeddings for prompts:

```text
"a photo of a cat"
"a photo of a dog"
...
```

select highest similarity.

No task-specific classifier huấn luyện (training / 학습) required, though prompt templates and lĩnh vực (domain / 도메인) shift affect chất lượng (quality / 품질).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Ngữ nghĩa (semantic / 의미적) Retrieval** tiếp nhận điểm tựa từ **Zero-Shot Classification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Open-Vocabulary Vision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ nghĩa (semantic / 의미적) Retrieval

Dùng chung (shared / 공유) embedding không gian (space / 공간) enables:

```text
text query → retrieve images
image query → retrieve text/images
```

This is multimodal thông tin (information / 정보) retrieval.

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Open-Vocabulary Vision** tiếp nhận điểm tựa từ **Ngữ nghĩa (semantic / 의미적) Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Foundation các mô hình (models / 모델들) for Segmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Open-Vocabulary Vision

Detection/segmentation can replace fixed lớp (class / 클래스) head with text-conditioned embeddings. mô hình (model / 모델) can localize concepts specified by natural ngôn ngữ (language / 언어).

Challenge: text-image pretraining may learn broad ngữ nghĩa (semantics / 의미론) but weak precise localization; extra objectives/architectures needed.

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Foundation các mô hình (models / 모델들) for Segmentation** tiếp nhận điểm tựa từ **Open-Vocabulary Vision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Visual Tokenizers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Foundation các mô hình (models / 모델들) for Segmentation

Promptable segmentation separates mục tiêu (target / 대상) specification from mask generation. đầu vào (input / 입력) prompts may be points, boxes or masks.

This turns segmentation into general interactive năng lực (capability / 역량) rather than fixed lớp (class / 클래스) taxonomy.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Visual Tokenizers** tiếp nhận điểm tựa từ **Foundation các mô hình (models / 모델들) for Segmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Diffusion biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Visual Tokenizers

Generative ảnh (image / 이미지) các mô hình (models / 모델들) may encode ảnh (image / 이미지) into discrete/continuous latent tokens using VAE/VQ-style encoder. Transformer/diffusion operates in latent không gian (space / 공간) instead of raw pixels.

Latent biểu diễn (representation / 표현) reduces compute while hopefully preserving perceptual ngữ nghĩa (semantics / 의미론).

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Diffusion biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **Visual Tokenizers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh (image / 이미지) Embedding hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Diffusion biểu diễn (representation / 표현)

Diffusion các mô hình (models / 모델들) are generative, but intermediate features can also contain ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조) useful downstream. Generative huấn luyện (training / 학습) can produce representations, though mục tiêu (objective / 목표) differs discriminative contrastive huấn luyện (training / 학습).

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Ảnh (image / 이미지) Embedding hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **Diffusion biểu diễn (representation / 표현)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Fine-Tuning Strategies** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh (image / 이미지) Embedding hình học (geometry / 기하학)

Cosine similarity useful only because huấn luyện (training / 학습) aligns hình học (geometry / 기하학) to ngữ nghĩa (semantics / 의미론). Embedding is not universal ngữ nghĩa (semantic / 의미적) truth.

Different encoders place concepts differently depending dữ liệu (data / 데이터)/mục tiêu (objective / 목표).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Fine-Tuning Strategies** tiếp nhận điểm tựa từ **Ảnh (image / 이미지) Embedding hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Domain-Specific Foundation các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Fine-Tuning Strategies

Pretrained visual mô hình (model / 모델) can adapt via:

```text
linear probe
full fine-tuning
partial unfreezing
adapters / LoRA-like methods
prompt tuning
```

Choice depends dữ liệu (data / 데이터) kích thước (size / 크기), compute and lĩnh vực (domain / 도메인) gap.

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Domain-Specific Foundation các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Fine-Tuning Strategies** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) Curation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Domain-Specific Foundation các mô hình (models / 모델들)

Medical, satellite, industrial imagery differ strongly from web photos. lĩnh vực (domain / 도메인) pretraining often required because texture, quy mô (scale / 규모), sensor and label ngữ nghĩa (semantics / 의미론) differ.

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Domain-Specific Foundation các mô hình (models / 모델들)** nêu điều cần giải thích; **Dữ liệu (data / 데이터) Curation** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Evaluation Beyond Classification** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) Curation

At foundation-model quy mô (scale / 규모), dữ liệu (data / 데이터) chất lượng (quality / 품질) matters:

- duplicates;
- low-quality captions;
- NSFW/sensitive dữ liệu (data / 데이터);
- geographic/cultural imbalance;
- copyright/licensing;
- benchmark leakage.

Biểu diễn (representation / 표현) inherits dataset độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Dữ liệu (data / 데이터) Curation** nêu điều cần giải thích; **Evaluation Beyond Classification** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Visual lập luận (reasoning / 추론)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation Beyond Classification

Good biểu diễn (representation / 표현) should be tested on multiple tasks:

- tuyến tính (linear / 선형) probing;
- retrieval;
- few-shot transfer;
- robustness;
- localization;
- cross-domain transfer.

A single benchmark can overfit kiến trúc (architecture / 아키텍처)/dữ liệu (data / 데이터) choices.

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Visual lập luận (reasoning / 추론)** tiếp nhận điểm tựa từ **Evaluation Beyond Classification** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multimodal cầu nối (bridge / 브리지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Visual lập luận (reasoning / 추론)

Strong visual encoder is not same as lập luận (reasoning / 추론) mô hình (model / 모델). VLM needs connect perception features with ngôn ngữ (language / 언어)/lập luận (reasoning / 추론) layers. thất bại (failure / 실패) can arise because đối tượng (object / 객체) not perceived, quan hệ (relation / 관계) lost, OCR weak or lập luận (reasoning / 추론) wrong.

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Multimodal cầu nối (bridge / 브리지)** tiếp nhận điểm tựa từ **Visual lập luận (reasoning / 추론)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Temporal Vision** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multimodal cầu nối (bridge / 브리지)

Dùng chung (common / 공통) kiến trúc (architecture / 아키텍처):

```text
image
→ vision encoder
→ visual tokens
→ projector / cross-attention
→ language model
→ text/tool output
```

The projector aligns visual tính năng (feature / 기능) dimension/phân phối (distribution / 분포) with ngôn ngữ (language / 언어) mô hình (model / 모델) giao diện (interface / 인터페이스).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Temporal Vision** tiếp nhận điểm tựa từ **Multimodal cầu nối (bridge / 브리지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Spatial Grounding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Temporal Vision

Video adds thời gian (time / 시간). A frame-only visual encoder misses motion/hành động (action / 동작) relationships. Video biểu diễn (representation / 표현) uses temporal sampling, 3D conv, temporal attention or factorized space-time các mô hình (models / 모델들).

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Spatial Grounding** tiếp nhận điểm tựa từ **Temporal Vision** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Spatial Grounding

Multimodal assistant that describes ảnh (image / 이미지) globally may still thất bại (fail / 실패) chính xác (exact / 정확한) coordinate grounding. Grounded vision-language các mô hình (models / 모델들) need tường minh (explicit / 명시적) spatial huấn luyện (training / 학습)/tasks.

> **Chuyển mạch:** Ở chặng này của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Spatial Grounding** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **hiện đại (modern / 현대적) vision foundation các mô hình (models / 모델들) học một visual coordinate hệ thống (system / 시스템) reusable; multimodal AI nối coordinate hệ thống (system / 시스템) đó với ngôn ngữ (language / 언어)/hành động (action / 동작) spaces.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “CLIP understands everything visually because it supports zero-shot labels”

Alignment chất lượng (quality / 품질) limited by pretraining pairs and can miss fine spatial details/counting/OCR.

### “Foundation mô hình (model / 모델) eliminates lĩnh vực (domain / 도메인) dữ liệu (data / 데이터)”

Lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증)/adaptation vẫn cần, đặc biệt medical/industrial.

### “Embedding similarity proves objects same”

Similarity reflects mô hình (model / 모델) mục tiêu (objective / 목표)/dữ liệu (data / 데이터), not ontological định danh (identity / 식별자).

> **Chuyển mạch:** Trong **Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Hiện đại (modern / 현대적) visual biểu diễn (representation / 표현) là cầu nối (bridge / 브리지) trực tiếp sang `13_speech_audio_and_multimodal/`, nơi ảnh (image / 이미지) tokens, audio representations và văn bản (text / 텍스트) tokens được kết hợp trong dùng chung (shared / 공유) or connected biểu diễn (representation / 표현) spaces.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
