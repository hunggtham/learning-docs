# Vision-Language Model

**Vision-Language Model (VLM / 비전-언어 모델)** kết hợp visual representation với language representation để xử lý các task như image captioning, visual question answering, OCR-aware reasoning, grounded dialogue và image-text retrieval.

Một architecture phổ biến:

```text
image
→ vision encoder
→ visual token
→ projector / resampler
→ language model
→ text hoặc tool output
```

## VLM không chỉ là Image Captioning

Image captioning chủ yếu sinh mô tả tổng quát cho toàn ảnh.

VLM rộng hơn vì có thể nhận đồng thời instruction và image rồi tạo answer phụ thuộc vào cả hai.

```text
Image + “What is the serial number?”
→ OCR / localization / reasoning
→ answer
```

Capability cuối cùng phụ thuộc vision encoder, visual-token resolution, alignment training và language model.

## Frozen Encoder + LLM

Một strategy thực tế:

1. dùng pretrained vision encoder;
2. dùng pretrained LLM;
3. train projector hoặc alignment module;
4. instruction-tune bằng multimodal data.

Cách này tận dụng capability đã có của hai unimodal model và giảm training cost so với train toàn stack từ đầu.

## Visual Token

Vision encoder output patch feature. Projector map chúng vào hidden dimension mà LLM có thể xử lý.

Các design question quan trọng:

- giữ bao nhiêu visual token;
- preserve 2D position như thế nào;
- có dùng crop hoặc high-resolution view không;
- có compress bằng resampler không.

Token budget ảnh hưởng trực tiếp khả năng đọc fine detail.

## Image Resolution

Small text, table và UI screenshot cần resolution cao.

Nếu một screenshot 4K bị resize xuống 224×224, nhiều OCR information đã mất trước khi language reasoning bắt đầu.

Modern VLM có thể dùng image tiling, crop nhiều scale hoặc variable-resolution tokenization để giữ detail tốt hơn.

## OCR Capability

Task chứa text trong image cần phân biệt:

```text
visual object recognition
vs
đọc text trong image
```

Một model rất tốt trên natural photo vẫn có thể yếu với document hoặc screenshot nếu pretraining không có đủ high-resolution text image.

## Visual Question Answering

**Visual Question Answering (VQA)** yêu cầu trả lời câu hỏi dựa trên image evidence.

Failure có thể đến từ nhiều layer:

- perception miss;
- localization miss;
- OCR miss;
- relation-reasoning miss;
- language hallucination.

Debugging cần xác định đúng layer thay vì chỉ xem final answer sai.

## Grounding

Grounded VLM có thể output box, point hoặc region gắn với phrase.

Một text answer đúng nhưng point hoặc box sai cho thấy global semantic recognition không đồng nghĩa precise spatial grounding.

## Image Captioning

Caption objective có thể viết:

\[
P(y|image)=\prod_t P(y_t|y_{<t},v)
\]

Caption có thể fluent nhưng bỏ sót object hoặc detail.

Reference caption của human cũng thường không mô tả mọi thứ trong image, vì vậy automatic metric cho caption không hoàn hảo.

## Multimodal Instruction Tuning

Multimodal instruction data thường có dạng:

```text
(image, instruction, answer)
```

Data này dạy VLM cách tương tác theo conversational hoặc tool-oriented format.

Synthetic data từ stronger model giúp scale nhanh nhưng cũng có thể propagate hallucination, bias và formatting artifact của teacher.

## Visual Chain Task

Một số task cần nhiều bước:

- chart → đọc value → tính toán;
- screenshot → xác định button → lập kế hoạch click;
- diagram → trace relation → trả lời.

Chúng cần cả perception và structured reasoning.

LLM mạnh không thể bù cho visual token quá mờ hoặc text không được encoder giữ lại.

## Chart và Table

Chart yêu cầu đọc axis, legend, text và geometry. Table trong image cần giữ row-column structure.

Dedicated OCR, table parser hoặc chart parser có thể đáng tin hơn end-to-end VLM cho exact extraction.

Một hybrid architecture mạnh:

```text
VLM → semantic routing
OCR / table extractor → exact data
calculator / code → deterministic computation
```

## Hallucination

VLM có thể nêu object hợp lý về mặt ngôn ngữ nhưng không tồn tại trong image vì language prior lấn át visual evidence không chắc chắn.

Grounded system nên cho phép abstention hoặc verification khi evidence yếu thay vì buộc model luôn trả lời.

## Contrastive Pretraining và Generative VLM

CLIP-style dual encoder mạnh về retrieval và zero-shot similarity nhưng không trực tiếp generate detailed language.

Generative VLM nối visual token với autoregressive language decoder để sinh answer hoặc dialogue.

Hai family có objective và use case khác nhau.

## Multi-Image Context

Một task có thể cần so sánh nhiều image, phân tích before/after hoặc đọc nhiều page.

Model phải giữ image identity, ordering và phân bổ context budget hợp lý giữa các image.

Nếu tất cả image bị compress quá mạnh, comparison detail có thể mất.

## Video Extension

Video VLM thường sample frame hoặc clip.

Sample quá thưa có thể bỏ mất event ngắn; sample quá dày làm token count bùng nổ.

Temporal order phải được encode để model phân biệt “trước” và “sau”.

## Evaluation

Cần task-specific eval suite, ví dụ:

- VQA accuracy;
- OCR/document accuracy;
- grounding IoU hoặc point accuracy;
- hallucination rate;
- chart/math exactness;
- robustness theo resolution/crop;
- multilingual text-in-image performance.

LLM-as-judge hữu ích cho open-ended response, nhưng exact visual fact nên có deterministic hoặc human verification khi khả thi.

## Security

Image có thể chứa text prompt injection, QR link hoặc malicious UI instruction.

Visual text phải được xem là **untrusted content**, không phải system authority.

Điều này đặc biệt quan trọng với browser agent hoặc screen-control agent.

## Accessibility

VLM có thể tạo image description cho người khiếm thị, nhưng hallucination vẫn là risk.

Trong navigation, medical hoặc safety-sensitive context, cần biểu đạt uncertainty rõ và có verification phù hợp.

## Mô hình tư duy

> **VLM là một language reasoner được nối với visual measurement pipeline. Capability bị giới hạn đồng thời bởi information mà vision side giữ được và khả năng inference của language side.**

## Những nhầm lẫn thường gặp

### “Model mô tả ảnh tốt nghĩa là hiểu chính xác geometry”

Không. Global semantics và precise localization là hai capability khác nhau.

### “LLM lớn hơn sẽ sửa OCR kém”

Không nếu visual text đã mất ở bước resize hoặc encoder bottleneck.

### “Vision-language alignment bảo đảm factual grounding”

Không. Alignment tăng association giữa modality, không tạo truth guarantee.

## Liên kết kiến thức

VLM nối [Vision Transformer](../12_computer_vision/07_vision_transformers.md), LLM, RAG-style grounding và Multimodal Context Engineering.

Xem tiếp: [Multimodal Transformer](./05_multimodal_transformers.md).