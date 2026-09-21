# Modern Visual Representation

Computer Vision hiện đại ngày càng ít xoay quanh một task head riêng lẻ và ngày càng tập trung vào **biểu diễn thị giác dùng chung (general-purpose visual representation)** có thể transfer sang classification, retrieval, detection, segmentation và multimodal reasoning.

Sự chuyển đổi có thể hình dung như sau:

```text
Task-specific supervised model
        ↓
Large pretrained visual encoder
        ↓
adapt / prompt / fine-tune cho nhiều task
```

## Self-Supervised Learning

Image label đắt nhưng raw image rất dồi dào. **Self-supervised learning** tạo supervision từ chính structure của data thay vì cần human label cho mọi sample.

Hai family lớn:

```text
contrastive / alignment objective
masked / reconstruction objective
```

## Contrastive Learning

Hai augmented view của cùng image được coi là positive pair; view từ image khác đóng vai trò negative hoặc được tách gián tiếp tùy method.

Mục tiêu:

\[
sim(z_i,z_i^+) \uparrow
\]

\[
sim(z_i,z_j^-) \downarrow
\]

Representation được học để trở nên invariant với các augmentation đã chọn.

Vì vậy augmentation policy thực chất là một phần của supervision signal.

## Trực giác SimCLR

Pipeline:

```text
image
→ hai random augmentation
→ shared encoder
→ projection head
→ contrastive loss
```

Trong formulation ban đầu, batch lớn cung cấp nhiều negative sample.

## Momentum / Teacher Encoder

Các family như MoCo, BYOL hoặc DINO dùng momentum teacher, target network, queue hoặc self-distillation để ổn định representation learning.

Ý tưởng cốt lõi là learner cố khớp với một target representation thay đổi chậm thay vì học trực tiếp từ manual label.

## Tránh Representation Collapse

Nếu encoder output cùng một vector cho mọi image, alignment loss có thể rơi vào trivial solution.

Các method tránh collapse bằng nhiều cơ chế:

- negative sample;
- stop-gradient;
- predictor asymmetry;
- variance/covariance constraint;
- teacher centering hoặc sharpening.

## Masked Image Modeling

Một lượng lớn patch được che rồi model phải reconstruct phần bị thiếu:

```text
visible patch
→ encoder
→ decoder
→ dự đoán missing pixel / feature / latent target
```

MAE-style method thường dùng masking ratio khá cao vì neighboring image patch có redundancy lớn.

Target có thể là raw pixel hoặc learned feature token.

## Supervised và Self-Supervised Representation

Supervised ImageNet training đẩy feature theo taxonomy class được cung cấp.

Self-supervised objective có thể giữ broader visual information hữu ích cho task ngoài taxonomy đó.

Tuy nhiên self-supervised không tự động tốt hơn. Data scale, augmentation, architecture và objective vẫn quyết định chất lượng representation.

## Vision–Language Pretraining

CLIP-style training dùng paired `(image,text)`.

Image encoder tạo `v`, text encoder tạo `t`; contrastive objective làm matched pair gần nhau trong shared embedding space.

```text
image ↔ caption
```

Điều này tạo một **open-vocabulary semantic interface**: class mới có thể được mô tả bằng text prompt thay vì fixed classifier ID.

## Zero-Shot Classification

Ta có thể tính image embedding `v`, rồi so với text embedding của candidate prompt:

```text
"a photo of a cat"
"a photo of a dog"
...
```

Class có similarity cao nhất được chọn.

Không cần train task-specific classifier head, nhưng prompt template, domain shift và pretraining coverage vẫn ảnh hưởng mạnh chất lượng.

## Semantic Retrieval

Shared embedding space hỗ trợ:

```text
text query  → retrieve image
image query → retrieve text hoặc image
```

Đây là một dạng multimodal information retrieval.

## Open-Vocabulary Vision

Detection hoặc segmentation có thể thay fixed class head bằng text-conditioned representation.

Model khi đó có thể localize concept được mô tả bằng natural language.

Challenge là image-text pretraining thường học broad semantics tốt hơn precise localization, nên cần objective hoặc architecture bổ sung.

## Foundation Model cho Segmentation

Promptable segmentation tách **cách chỉ định target** khỏi **cách sinh mask**.

Prompt có thể là point, box hoặc mask.

Segmentation vì vậy trở thành một general interactive capability thay vì bị giới hạn bởi fixed class taxonomy.

## Visual Tokenizer

Generative image model có thể encode image thành discrete hoặc continuous latent token bằng VAE hoặc VQ-style encoder.

Transformer hoặc diffusion model sau đó hoạt động trong latent space thay vì raw pixel space.

Latent representation giảm compute nếu vẫn giữ được perceptual information quan trọng.

## Representation từ Diffusion Model

Diffusion model chủ yếu được train cho generation, nhưng intermediate feature cũng có thể chứa semantic structure hữu ích cho downstream task.

Điều này cho thấy generative objective cũng có thể sinh representation mạnh, dù inductive pressure khác contrastive hoặc discriminative training.

## Geometry của Image Embedding

Cosine similarity chỉ hữu ích vì training objective đã tổ chức geometry theo một số semantic relation.

Embedding không phải universal semantic truth. Hai encoder khác nhau có thể đặt cùng concept ở geometry rất khác do data và objective khác nhau.

## Fine-Tuning Strategy

Pretrained visual model có thể được adapt bằng:

```text
linear probe
full fine-tuning
partial unfreezing
adapter / LoRA-like method
prompt tuning
```

Choice phụ thuộc data size, compute budget, deployment constraint và domain gap.

## Domain-Specific Foundation Model

Medical image, satellite image và industrial image khác web photo về texture, scale, sensor và label semantics.

Domain-specific pretraining hoặc adaptation thường cần thiết khi distribution gap lớn.

## Data Curation

Ở foundation-model scale, data quality trở thành yếu tố trọng yếu:

- duplicate;
- caption chất lượng thấp;
- sensitive hoặc NSFW data;
- geographic/cultural imbalance;
- copyright/licensing;
- benchmark leakage.

Representation kế thừa bias và coverage gap từ training corpus.

## Evaluation vượt ra ngoài Classification

Một visual representation tốt nên được kiểm tra trên nhiều task:

- linear probing;
- retrieval;
- few-shot transfer;
- robustness;
- localization;
- cross-domain transfer.

Một benchmark duy nhất có thể phản ánh quá hẹp và dễ bị overfit bởi architecture hoặc data choice.

## Visual Reasoning

Visual encoder mạnh không đồng nghĩa model reasoning tốt.

Một Vision-Language Model có thể fail vì nhiều nguyên nhân khác nhau:

```text
object không được perception đúng
spatial relation bị mất
OCR yếu
counting sai
reasoning language sai
```

Cần tách perception failure khỏi reasoning failure khi debug.

## Cầu nối Multimodal

Một architecture phổ biến:

```text
image
→ vision encoder
→ visual token
→ projector / cross-attention
→ language model
→ text hoặc tool output
```

Projector giúp align dimension và distribution của visual feature với interface mà language model có thể sử dụng.

## Temporal Vision

Video thêm dimension thời gian. Frame-only encoder không trực tiếp nắm motion hoặc action relation giữa các frame.

Video representation có thể dùng temporal sampling, 3D convolution, temporal attention hoặc factorized space–time model.

## Spatial Grounding

Một multimodal assistant mô tả image tổng quát tốt vẫn có thể kém ở exact coordinate grounding.

Grounded vision-language model cần explicit spatial supervision hoặc architecture hỗ trợ region/box/mask relation.

## Mô hình tư duy

> **Modern vision foundation model học một visual coordinate system có thể tái sử dụng; Multimodal AI nối coordinate system đó với language và action space.**

## Những nhầm lẫn thường gặp

### “CLIP hỗ trợ zero-shot nên hiểu mọi thứ trong ảnh”

Không. Image-text alignment phụ thuộc pretraining pair và thường yếu hơn ở fine spatial detail, counting hoặc OCR.

### “Foundation model loại bỏ nhu cầu domain data”

Không. Domain validation và adaptation vẫn rất quan trọng, đặc biệt trong medical và industrial system.

### “Embedding similarity chứng minh hai object giống nhau”

Không. Similarity phản ánh model objective và data, không phải ontological identity.

## Liên kết kiến thức

Modern visual representation là bridge trực tiếp sang `13_speech_audio_and_multimodal/`, nơi image token, audio representation và text token được kết nối trong shared hoặc connected representation space.