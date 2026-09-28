# Vision-Language các mô hình (models / 모델들)

> **Mạch đọc:** Đặt **Vision-Language các mô hình (models / 모델들)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **VLM không chỉ là ảnh (image / 이미지) captioning** sang **Frozen Encoder + LLM**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Frozen Encoder + LLM

Một practical chiến lược (strategy / 전략):

1. dùng pretrained vision encoder;
2. dùng pretrained LLM;
3. train projector/alignment mô-đun (module / 모듈);
4. instruction-tune multimodal dữ liệu (data / 데이터).

Điều này leverage strong unimodal các mô hình (models / 모델들) và giảm huấn luyện (training / 학습) chi phí (cost / 비용).

## Visual Tokens

Vision encoder đầu ra (output / 출력) patch features. Projector maps chúng vào LLM hidden dimension.

Question quan trọng:

- giữ bao nhiêu tokens?
- preserve 2D positions thế nào?
- có crop/high-res views không?
- compress bằng resampler không?

Đơn vị từ (token / 토큰) ngân sách (budget / 예산) directly affects fine-detail perception.

## Ảnh (image / 이미지) Resolution

Small văn bản (text / 텍스트), tables, UI screenshots cần high resolution. Nếu mô hình (model / 모델) resize 4K screenshot xuống 224×224, OCR thông tin (information / 정보) mất trước lập luận (reasoning / 추론).

Hiện đại (modern / 현대적) VLM có thể split ảnh (image / 이미지) thành tiles/crops hoặc variable-resolution tokenization.

## OCR năng lực (capability / 역량)

OCR-heavy tasks cần distinguish:

```text
visual object recognition
vs
text reading in image
```

A mô hình (model / 모델) good at natural photos may still thất bại (fail / 실패) documents/screenshots if pretraining lacks high-resolution văn bản (text / 텍스트).

## Visual Question Answering

VQA requires answer questions grounded in ảnh (image / 이미지). thất bại (failure / 실패) taxonomy:

- perception miss;
- localization miss;
- OCR miss;
- quan hệ (relation / 관계) lập luận (reasoning / 추론) miss;
- ngôn ngữ (language / 언어) hallucination.

Debugging cần biết stage nào thất bại (fail / 실패).

## Grounding

Grounded VLM có thể đầu ra (output / 출력) boxes/points/regions linked to phrases. Text-only answer đúng nhưng điểm (point / 지점) sai cho thấy ngữ nghĩa (semantic / 의미적) recognition không equal precise spatial grounding.

## Ảnh (image / 이미지) Captioning

Caption mục tiêu (objective / 목표):

\[
P(y|image)=\prod_t P(y_t|y_{<t},v)
\]

Caption can be fluent yet omit objects. tham chiếu (reference / 참조) captions cũng incomplete, làm automatic metrics imperfect.

## Instruction Tuning

Multimodal instruction dữ liệu (data / 데이터):

```text
(image, instruction, answer)
```

teaches conversation/tool-style hành vi (behavior / 동작). Synthetic dữ liệu (data / 데이터) from stronger các mô hình (models / 모델들) can quy mô (scale / 규모) dataset but may propagate hallucinations/độ lệch (bias / 편향).

## Visual chuỗi (chain / 사슬) Tasks

Examples:

- charts → read values → calculate;
- screenshot → identify button → plan click;
- diagram → dấu vết (trace / 추적) relations → answer.

Need perception + structured lập luận (reasoning / 추론). LLM strength cannot compensate for unreadable visual tokens.

## Charts and Tables

Charts require axis/legend/văn bản (text / 텍스트) parsing + hình học (geometry / 기하학). Tables in images require cell cấu trúc (structure / 구조). Dedicated parsers or OCR may outperform end-to-end VLM for chính xác (exact / 정확한) extraction.

Hybrid kiến trúc (architecture / 아키텍처):

```text
VLM for semantic routing
+ OCR/table extractor for exact data
+ deterministic calculator
```

## Hallucination

VLM may name visually plausible but absent objects because ngôn ngữ (language / 언어) priors dominate uncertain vision bằng chứng (evidence / 증거).

Grounded answer generation should encourage abstention/xác minh (verification / 확인) when visual bằng chứng (evidence / 증거) weak.

## Contrastive Pretraining vs Generative VLM

CLIP-style dual encoder good retrieval/zero-shot similarity but cannot directly generate detailed ngôn ngữ (language / 언어). Generative VLM connects visual tokens to autoregressive ngôn ngữ (language / 언어) decoder.

These are different kiến trúc (architecture / 아키텍처)/use cases.

## Multi-Image ngữ cảnh (context / 맥락)

Tasks may compare images, inspect before/after, analyze multiple pages. mô hình (model / 모델) needs ảnh (image / 이미지) định danh (identity / 식별자)/thứ tự (order / 순서) and ngữ cảnh (context / 맥락) ngân sách (budget / 예산) allocation.

## Video Extension

Video VLM samples frames/clips. Too sparse misses brief events; too dense explodes tokens. Temporal thứ tự (ordering / 순서) must be encoded.

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

## Bảo mật (security / 보안)

Ảnh (image / 이미지) can contain văn bản (text / 텍스트) prompt injection, QR links or malicious UI instructions. VLM should treat visual văn bản (text / 텍스트) as untrusted content, not hệ thống (system / 시스템) authority.

This matters for screen/trình duyệt (browser / 브라우저) agents.

## Khả năng tiếp cận (accessibility / 접근성)

VLM can describe images for blind users, but hallucination rủi ro (risk / 위험) means trọng yếu (critical / 중요) điều hướng (navigation / 내비게이션)/medical contexts need clear bất định (uncertainty / 불확실성) and xác minh (verification / 확인).

## Mô hình tư duy (mental model / 사고 모델)

> **A VLM is a ngôn ngữ (language / 언어) reasoner connected to a visual đo lường (measurement / 측정) chuỗi xử lý (pipeline / 파이프라인). Its ceiling is bounded both by what the vision side preserves and what the ngôn ngữ (language / 언어) side can infer.**

## Dùng chung (common / 공통) Misconceptions

### “If mô hình (model / 모델) can describe ảnh (image / 이미지), it understands chính xác (exact / 정확한) hình học (geometry / 기하학)”

Toàn cục (global / 전역) ngữ nghĩa (semantics / 의미론) and precise localization differ.

### “Bigger LLM fixes poor OCR”

If visual văn bản (text / 텍스트) lost in encoder/resizing, ngôn ngữ (language / 언어) mô hình (model / 모델) cannot reconstruct reliably.

### “Vision-language alignment means factual grounding guaranteed”

Alignment increases association, not truth guarantee.

## Liên kết kiến thức (knowledge connection / 지식 연결)

VLM connects [Vision Transformers](../12_computer_vision/07_vision_transformers.md), LLMs, RAG-like grounding and multimodal ngữ cảnh (context / 맥락) kỹ thuật (engineering / 엔지니어링).

Xem tiếp: [Multimodal Transformers](./05_multimodal_transformers.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 audio and speech representation](./00_audio_and_speech_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
