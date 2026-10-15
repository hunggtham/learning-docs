# Hiện đại (modern / 현대적) Visual biểu diễn (representation / 표현)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Modern visual representation**. Route đi từ unlabeled augmentations → self-supervised objectives → contrastive/distillation learning → multimodal alignment → transfer and collapse risks, để representation học được tín hiệu dùng lại qua nhiều task.

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

Hai family này khác nhau ở nguồn tín hiệu học: contrastive giữ các view của cùng ảnh gần nhau, còn masked modeling yêu cầu khôi phục phần bị che.

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

SimCLR làm rõ pipeline contrastive bằng cách dùng hai view ngẫu nhiên, encoder dùng chung và projection head.

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

Các phương pháp dùng teacher hoặc momentum encoder thay đổi cách tạo target, giảm phụ thuộc vào batch lớn và nhãn thủ công.

## Momentum / Teacher Encoders

Methods như MoCo/BYOL/DINO-style families dùng mục tiêu (target / 대상)/momentum teacher, queues hoặc self-distillation để stabilize biểu diễn (representation / 표현) học tập (learning / 학습).

Điểm conceptual: learner match a slowly changing mục tiêu (target / 대상) biểu diễn (representation / 표현) thay vì labels manual.

Bất kể target đến từ đâu, mục tiêu vẫn phải ngăn encoder rơi vào nghiệm suy biến khi mọi ảnh nhận cùng một vector.

## Avoiding Collapse

Nếu encoder đầu ra (output / 출력) same véc-tơ (vector / 벡터) cho all images, alignment mục tiêu (objective / 목표) trivial. Different methods prevent collapse bằng:

- negatives;
- stop-gradient;
- predictor asymmetry;
- variance/covariance các ràng buộc (constraints / 제약조건들);
- teacher centering/sharpening.

Một nhánh khác tránh dựa vào negative pairs bằng cách che patch rồi học biểu diễn từ phần còn nhìn thấy.

## Masked ảnh (image / 이미지) Modeling

Mask nhiều patches rồi reconstruct:

```text
visible patches → encoder → decoder → predict missing content/features
```

MAE-style methods mask high ratio vì neighboring ảnh (image / 이미지) patches redundant.

Mục tiêu (target / 대상) có thể raw pixels hoặc learned tính năng (feature / 기능) tokens.

Supervised và self-supervised vì thế cần được so sánh theo loại thông tin mà representation giữ lại và task downstream, không chỉ theo tên objective.

## Supervised vs Self-Supervised biểu diễn (representation / 표현)

Supervised ImageNet huấn luyện (training / 학습) pushes features toward provided classes. Self-supervised objectives có thể preserve broader visual thông tin (information / 정보) useful tasks beyond taxonomy.

Không có guarantee self-supervised always better; mục tiêu (objective / 목표)/dữ liệu (data / 데이터) quy mô (scale / 규모) matter.

Khi nhãn văn bản đi kèm ảnh, cùng nguyên tắc alignment mở rộng thành pretraining vision–language.

## Vision–ngôn ngữ (language / 언어) Pretraining

CLIP-style huấn luyện (training / 학습) uses paired `(image,text)`.

Ảnh (image / 이미지) encoder produces `v`; văn bản (text / 텍스트) encoder produces `t`. Contrastive mục tiêu (objective / 목표) makes matched pairs similar in dùng chung (shared / 공유) không gian (space / 공간).

```text
image ↔ caption
```

This creates **open-vocabulary ngữ nghĩa (semantic / 의미적) giao diện (interface / 인터페이스)**: new label can be represented by văn bản (text / 텍스트) prompt rather than fixed classifier ID.

Giao diện prompt cho phép đánh giá zero-shot bằng cách so sánh embedding ảnh với nhiều mô tả lớp.

## Zero-Shot Classification

Compute ảnh (image / 이미지) embedding `v`, văn bản (text / 텍스트) embeddings for prompts:

```text
"a photo of a cat"
"a photo of a dog"
...
```

select highest similarity.

No task-specific classifier huấn luyện (training / 학습) required, though prompt templates and lĩnh vực (domain / 도메인) shift affect chất lượng (quality / 품질).

Khi truy vấn không còn là danh sách lớp mà là mô tả tự do, embedding chung có thể dùng cho semantic retrieval.

## Ngữ nghĩa (semantic / 의미적) Retrieval

Dùng chung (shared / 공유) embedding không gian (space / 공간) enables:

```text
text query → retrieve images
image query → retrieve text/images
```

This is multimodal thông tin (information / 정보) retrieval.

Retrieval và zero-shot đều phụ thuộc alignment; open-vocabulary vision đưa alignment đó vào detection và segmentation cần localization chính xác hơn.

## Open-Vocabulary Vision

Detection/segmentation can replace fixed lớp (class / 클래스) head with text-conditioned embeddings. mô hình (model / 모델) can localize concepts specified by natural ngôn ngữ (language / 언어).

Challenge: text-image pretraining may learn broad ngữ nghĩa (semantics / 의미론) but weak precise localization; extra objectives/architectures needed.

Promptable segmentation tách việc chỉ định mục tiêu khỏi việc sinh mask, nhờ đó mở rộng cách tương tác với mô hình.

## Foundation các mô hình (models / 모델들) for Segmentation

Promptable segmentation separates mục tiêu (target / 대상) specification from mask generation. đầu vào (input / 입력) prompts may be points, boxes or masks.

This turns segmentation into general interactive năng lực (capability / 역량) rather than fixed lớp (class / 클래스) taxonomy.

Các hệ thống sinh ảnh cũng làm việc với token, nhưng thường nén pixel vào latent space trước khi transformer hoặc diffusion xử lý.

## Visual Tokenizers

Generative ảnh (image / 이미지) các mô hình (models / 모델들) may encode ảnh (image / 이미지) into discrete/continuous latent tokens using VAE/VQ-style encoder. Transformer/diffusion operates in latent không gian (space / 공간) instead of raw pixels.

Latent biểu diễn (representation / 표현) reduces compute while hopefully preserving perceptual ngữ nghĩa (semantics / 의미론).

Latent giữ lại cấu trúc hữu ích cho sinh ảnh; các tầng trung gian của diffusion đôi khi cũng cung cấp biểu diễn cho task downstream.

## Diffusion biểu diễn (representation / 표현)

Diffusion các mô hình (models / 모델들) are generative, but intermediate features can also contain ngữ nghĩa (semantic / 의미적) cấu trúc (structure / 구조) useful downstream. Generative huấn luyện (training / 학습) can produce representations, though mục tiêu (objective / 목표) differs discriminative contrastive huấn luyện (training / 학습).

Để sử dụng embedding đúng cách, cần nhớ hình học của không gian được tạo bởi objective và dữ liệu, không phải bởi một ý nghĩa phổ quát có sẵn.

## Ảnh (image / 이미지) Embedding hình học (geometry / 기하학)

Cosine similarity useful only because huấn luyện (training / 학습) aligns hình học (geometry / 기하학) to ngữ nghĩa (semantics / 의미론). Embedding is not universal ngữ nghĩa (semantic / 의미적) truth.

Different encoders place concepts differently depending dữ liệu (data / 데이터)/mục tiêu (objective / 목표).

Fine-tuning chọn mức can thiệp vào encoder dựa trên dữ liệu, compute và khoảng cách giữa domain pretraining với domain đích.

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

Khi ảnh đích khác xa web photos, một foundation model theo domain có thể cung cấp prior phù hợp hơn.

## Domain-Specific Foundation các mô hình (models / 모델들)

Medical, satellite, industrial imagery differ strongly from web photos. lĩnh vực (domain / 도메인) pretraining often required because texture, quy mô (scale / 규모), sensor and label ngữ nghĩa (semantics / 의미론) differ.

Prior theo domain chỉ hữu ích khi dữ liệu được tuyển chọn có chủ đích và không làm rò rỉ benchmark hoặc khuếch đại bias.

## Dữ liệu (data / 데이터) Curation

At foundation-model quy mô (scale / 규모), dữ liệu (data / 데이터) chất lượng (quality / 품질) matters:

- duplicates;
- low-quality captions;
- NSFW/sensitive dữ liệu (data / 데이터);
- geographic/cultural imbalance;
- copyright/licensing;
- benchmark leakage.

Biểu diễn (representation / 표현) inherits dataset độ lệch (bias / 편향).

Vì representation phục vụ nhiều task, đánh giá cũng phải vượt ra ngoài một benchmark classification đơn lẻ.

## Evaluation Beyond Classification

Good biểu diễn (representation / 표현) should be tested on multiple tasks:

- tuyến tính (linear / 선형) probing;
- retrieval;
- few-shot transfer;
- robustness;
- localization;
- cross-domain transfer.

A single benchmark can overfit kiến trúc (architecture / 아키텍처)/dữ liệu (data / 데이터) choices.

Một encoder tốt không đồng nghĩa hệ thống đã reasoning tốt; multimodal model còn phải nối perception với ngôn ngữ và hành động.

## Visual lập luận (reasoning / 추론)

Strong visual encoder is not same as lập luận (reasoning / 추론) mô hình (model / 모델). VLM needs connect perception features with ngôn ngữ (language / 언어)/lập luận (reasoning / 추론) layers. thất bại (failure / 실패) can arise because đối tượng (object / 객체) not perceived, quan hệ (relation / 관계) lost, OCR weak or lập luận (reasoning / 추론) wrong.


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

Với video, pipeline này cần thêm trục thời gian để biểu diễn chuyển động và quan hệ giữa các frame.

## Temporal Vision

Video adds thời gian (time / 시간). A frame-only visual encoder misses motion/hành động (action / 동작) relationships. Video biểu diễn (representation / 표현) uses temporal sampling, 3D conv, temporal attention or factorized space-time các mô hình (models / 모델들).

Ngay cả khi hiểu thời gian, hệ thống vẫn có thể mô tả đúng cảnh nhưng không chỉ đúng tọa độ; đó là vấn đề spatial grounding.

## Spatial Grounding

Multimodal assistant that describes ảnh (image / 이미지) globally may still thất bại (fail / 실패) chính xác (exact / 정확한) coordinate grounding. Grounded vision-language các mô hình (models / 모델들) need tường minh (explicit / 명시적) spatial huấn luyện (training / 학습)/tasks.

Các giới hạn này được tóm tắt trong một mental model trước khi kiểm tra những ngộ nhận phổ biến.

## Mô hình tư duy (mental model / 사고 모델)

> **hiện đại (modern / 현대적) vision foundation các mô hình (models / 모델들) học một visual coordinate hệ thống (system / 시스템) reusable; multimodal AI nối coordinate hệ thống (system / 시스템) đó với ngôn ngữ (language / 언어)/hành động (action / 동작) spaces.**

Mental model này nhắc rằng biểu diễn reusable vẫn bị giới hạn bởi objective, dữ liệu và năng lực grounding.

## Dùng chung (common / 공통) Misconceptions

### “CLIP understands everything visually because it supports zero-shot labels”

Alignment chất lượng (quality / 품질) limited by pretraining pairs and can miss fine spatial details/counting/OCR.

### “Foundation mô hình (model / 모델) eliminates lĩnh vực (domain / 도메인) dữ liệu (data / 데이터)”

Lĩnh vực (domain / 도메인) kiểm tra hợp lệ (validation / 검증)/adaptation vẫn cần, đặc biệt medical/industrial.

### “Embedding similarity proves objects same”

Similarity reflects mô hình (model / 모델) mục tiêu (objective / 목표)/dữ liệu (data / 데이터), not ontological định danh (identity / 식별자).

Những ranh giới này nối visual representation với speech, audio và multimodal pipeline ở phần kế tiếp.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Hiện đại (modern / 현대적) visual biểu diễn (representation / 표현) là cầu nối (bridge / 브리지) trực tiếp sang `13_speech_audio_and_multimodal/`, nơi ảnh (image / 이미지) tokens, audio representations và văn bản (text / 텍스트) tokens được kết hợp trong dùng chung (shared / 공유) or connected biểu diễn (representation / 표현) spaces.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
