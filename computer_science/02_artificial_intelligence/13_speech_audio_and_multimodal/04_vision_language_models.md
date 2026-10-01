# Vision-Language các mô hình (models / 모델들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Vision-Language các mô hình (models / 모델들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **VLM không chỉ là ảnh (image / 이미지) captioning** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Frozen Encoder + LLM** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

**Vision-Language mô hình (model / 모델)** kết hợp visual biểu diễn (representation / 표현) với ngôn ngữ (language / 언어) biểu diễn (representation / 표현) để xử lý tasks như ảnh (image / 이미지) captioning, visual question answering, OCR-aware lập luận (reasoning / 추론), grounded dialogue và image-text retrieval.

Một kiến trúc (architecture / 아키텍처) phổ biến:

```text
image
→ vision encoder
→ visual tokens
→ projector / resampler
→ language model
→ text/tool output
```

## VLM không chỉ là ảnh (image / 이미지) captioning

Captioning sinh mô tả toàn ảnh. VLM general hơn vì có thể nhận instruction + ảnh (image / 이미지), trả answer conditioned on both.

```text
Image + “What is the serial number?”
→ OCR/localization/reasoning
→ answer
```

Năng lực (capability / 역량) phụ thuộc encoder, visual đơn vị từ (token / 토큰) resolution, alignment huấn luyện (training / 학습) và LLM.

> **Chuyển mạch:** Trong **Vision-Language các mô hình (models / 모델들)**, **Frozen Encoder + LLM** tiếp nhận điểm tựa từ **VLM không chỉ là ảnh (image / 이미지) captioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Visual Tokens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Frozen Encoder + LLM

Một practical chiến lược (strategy / 전략):

1. dùng pretrained vision encoder;
2. dùng pretrained LLM;
3. train projector/alignment mô-đun (module / 모듈);
4. instruction-tune multimodal dữ liệu (data / 데이터).

Điều này leverage strong unimodal các mô hình (models / 모델들) và giảm huấn luyện (training / 학습) chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Vision-Language các mô hình (models / 모델들)**, **Visual Tokens** tiếp nhận điểm tựa từ **Frozen Encoder + LLM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh (image / 이미지) Resolution** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Visual Tokens

Vision encoder đầu ra (output / 출력) patch features. Projector maps chúng vào LLM hidden dimension.

Question quan trọng:

- giữ bao nhiêu tokens?
- preserve 2D positions thế nào?
- có crop/high-res views không?
- compress bằng resampler không?

Đơn vị từ (token / 토큰) ngân sách (budget / 예산) directly affects fine-detail perception.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision-Language các mô hình (models / 모델들)**, **Ảnh (image / 이미지) Resolution** tiếp nhận điểm tựa từ **Visual Tokens** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **OCR năng lực (capability / 역량)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh (image / 이미지) Resolution

Small văn bản (text / 텍스트), tables, UI screenshots cần high resolution. Nếu mô hình (model / 모델) resize 4K screenshot xuống 224×224, OCR thông tin (information / 정보) mất trước lập luận (reasoning / 추론).

Hiện đại (modern / 현대적) VLM có thể split ảnh (image / 이미지) thành tiles/crops hoặc variable-resolution tokenization.

> **Chuyển mạch:** Trong **Vision-Language các mô hình (models / 모델들)**, **OCR năng lực (capability / 역량)** tiếp nhận điểm tựa từ **Ảnh (image / 이미지) Resolution** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Visual Question Answering** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## OCR năng lực (capability / 역량)

OCR-heavy tasks cần distinguish:

```text
visual object recognition
vs
text reading in image
```

A mô hình (model / 모델) good at natural photos may still thất bại (fail / 실패) documents/screenshots if pretraining lacks high-resolution văn bản (text / 텍스트).

> **Chuyển mạch:** Ở chặng này của **Vision-Language các mô hình (models / 모델들)**, **Visual Question Answering** tiếp nhận điểm tựa từ **OCR năng lực (capability / 역량)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Grounding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Visual Question Answering

VQA requires answer questions grounded in ảnh (image / 이미지). thất bại (failure / 실패) taxonomy:

- perception miss;
- localization miss;
- OCR miss;
- quan hệ (relation / 관계) lập luận (reasoning / 추론) miss;
- ngôn ngữ (language / 언어) hallucination.

Debugging cần biết stage nào thất bại (fail / 실패).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision-Language các mô hình (models / 모델들)**, **Grounding** tiếp nhận điểm tựa từ **Visual Question Answering** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ảnh (image / 이미지) Captioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Grounding

Grounded VLM có thể đầu ra (output / 출력) boxes/points/regions linked to phrases. Text-only answer đúng nhưng điểm (point / 지점) sai cho thấy ngữ nghĩa (semantic / 의미적) recognition không equal precise spatial grounding.

> **Chuyển mạch:** Trong **Vision-Language các mô hình (models / 모델들)**, **Ảnh (image / 이미지) Captioning** tiếp nhận điểm tựa từ **Grounding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Instruction Tuning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ảnh (image / 이미지) Captioning

Caption mục tiêu (objective / 목표):

\[
P(y|image)=\prod_t P(y_t|y_{<t},v)
\]

Caption can be fluent yet omit objects. tham chiếu (reference / 참조) captions cũng incomplete, làm automatic metrics imperfect.

> **Chuyển mạch:** Ở chặng này của **Vision-Language các mô hình (models / 모델들)**, **Instruction Tuning** tiếp nhận điểm tựa từ **Ảnh (image / 이미지) Captioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Visual chuỗi (chain / 사슬) Tasks** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Instruction Tuning

Multimodal instruction dữ liệu (data / 데이터):

```text
(image, instruction, answer)
```

teaches conversation/tool-style hành vi (behavior / 동작). Synthetic dữ liệu (data / 데이터) from stronger các mô hình (models / 모델들) can quy mô (scale / 규모) dataset but may propagate hallucinations/độ lệch (bias / 편향).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision-Language các mô hình (models / 모델들)**, **Instruction Tuning** xác định đầu vào; **Visual chuỗi (chain / 사슬) Tasks** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Charts and Tables** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Visual chuỗi (chain / 사슬) Tasks

Examples:

- charts → read values → calculate;
- screenshot → identify button → plan click;
- diagram → dấu vết (trace / 추적) relations → answer.

Need perception + structured lập luận (reasoning / 추론). LLM strength cannot compensate for unreadable visual tokens.

> **Chuyển mạch:** Trong **Vision-Language các mô hình (models / 모델들)**, **Visual chuỗi (chain / 사슬) Tasks** xác định đầu vào; **Charts and Tables** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Hallucination** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Charts and Tables

Charts require axis/legend/văn bản (text / 텍스트) parsing + hình học (geometry / 기하학). Tables in images require cell cấu trúc (structure / 구조). Dedicated parsers or OCR may outperform end-to-end VLM for chính xác (exact / 정확한) extraction.

Hybrid kiến trúc (architecture / 아키텍처):

```text
VLM for semantic routing
+ OCR/table extractor for exact data
+ deterministic calculator
```

> **Chuyển mạch:** Ở chặng này của **Vision-Language các mô hình (models / 모델들)**, **Hallucination** tiếp nhận điểm tựa từ **Charts and Tables** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contrastive Pretraining vs Generative VLM** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hallucination

VLM may name visually plausible but absent objects because ngôn ngữ (language / 언어) priors dominate uncertain vision bằng chứng (evidence / 증거).

Grounded answer generation should encourage abstention/xác minh (verification / 확인) when visual bằng chứng (evidence / 증거) weak.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision-Language các mô hình (models / 모델들)**, **Hallucination** đã nêu tiêu chí phân biệt, còn **Contrastive Pretraining vs Generative VLM** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Multi-Image ngữ cảnh (context / 맥락)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contrastive Pretraining vs Generative VLM

CLIP-style dual encoder good retrieval/zero-shot similarity but cannot directly generate detailed ngôn ngữ (language / 언어). Generative VLM connects visual tokens to autoregressive ngôn ngữ (language / 언어) decoder.

These are different kiến trúc (architecture / 아키텍처)/use cases.

> **Chuyển mạch:** Trong **Vision-Language các mô hình (models / 모델들)**, **Contrastive Pretraining vs Generative VLM** đã nêu tiêu chí phân biệt, còn **Multi-Image ngữ cảnh (context / 맥락)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Video Extension** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Image ngữ cảnh (context / 맥락)

Tasks may compare images, inspect before/after, analyze multiple pages. mô hình (model / 모델) needs ảnh (image / 이미지) định danh (identity / 식별자)/thứ tự (order / 순서) and ngữ cảnh (context / 맥락) ngân sách (budget / 예산) allocation.

> **Chuyển mạch:** Ở chặng này của **Vision-Language các mô hình (models / 모델들)**, **Video Extension** tiếp nhận điểm tựa từ **Multi-Image ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Video Extension

Video VLM samples frames/clips. Too sparse misses brief events; too dense explodes tokens. Temporal thứ tự (ordering / 순서) must be encoded.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision-Language các mô hình (models / 모델들)**, **Evaluation** tiếp nhận điểm tựa từ **Video Extension** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bảo mật (security / 보안)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Evaluation

Need task-specific suites:

- VQA accuracy;
- OCR/document accuracy;
- grounding IoU/điểm (point / 지점) accuracy;
- hallucination tỷ lệ (rate / 비율);
- chart/math exactness;
- robustness to resolution/crops;
- multilingual văn bản (text / 텍스트) in images.

LLM-as-judge useful for open answers but chính xác (exact / 정확한) visual facts need deterministic/human xác minh (verification / 확인).

> **Chuyển mạch:** Trong **Vision-Language các mô hình (models / 모델들)**, **Bảo mật (security / 보안)** tiếp nhận điểm tựa từ **Evaluation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Khả năng tiếp cận (accessibility / 접근성)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bảo mật (security / 보안)

Ảnh (image / 이미지) can contain văn bản (text / 텍스트) prompt injection, QR links or malicious UI instructions. VLM should treat visual văn bản (text / 텍스트) as untrusted content, not hệ thống (system / 시스템) authority.

This matters for screen/trình duyệt (browser / 브라우저) agents.

> **Chuyển mạch:** Ở chặng này của **Vision-Language các mô hình (models / 모델들)**, **Khả năng tiếp cận (accessibility / 접근성)** tiếp nhận điểm tựa từ **Bảo mật (security / 보안)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Khả năng tiếp cận (accessibility / 접근성)

VLM can describe images for blind users, but hallucination rủi ro (risk / 위험) means trọng yếu (critical / 중요) điều hướng (navigation / 내비게이션)/medical contexts need clear bất định (uncertainty / 불확실성) and xác minh (verification / 확인).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision-Language các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Khả năng tiếp cận (accessibility / 접근성)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **A VLM is a ngôn ngữ (language / 언어) reasoner connected to a visual đo lường (measurement / 측정) chuỗi xử lý (pipeline / 파이프라인). Its ceiling is bounded both by what the vision side preserves and what the ngôn ngữ (language / 언어) side can infer.**

> **Chuyển mạch:** Trong **Vision-Language các mô hình (models / 모델들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “If mô hình (model / 모델) can describe ảnh (image / 이미지), it understands chính xác (exact / 정확한) hình học (geometry / 기하학)”

Toàn cục (global / 전역) ngữ nghĩa (semantics / 의미론) and precise localization differ.

### “Bigger LLM fixes poor OCR”

If visual văn bản (text / 텍스트) lost in encoder/resizing, ngôn ngữ (language / 언어) mô hình (model / 모델) cannot reconstruct reliably.

### “Vision-language alignment means factual grounding guaranteed”

Alignment increases association, not truth guarantee.

> **Chuyển mạch:** Ở chặng này của **Vision-Language các mô hình (models / 모델들)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

VLM connects [Vision Transformers](../12_computer_vision/07_vision_transformers.md), LLMs, RAG-like grounding and multimodal ngữ cảnh (context / 맥락) kỹ thuật (engineering / 엔지니어링).

Xem tiếp: [Multimodal Transformers](./05_multimodal_transformers.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
