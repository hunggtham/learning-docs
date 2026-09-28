# Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** Đặt **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **“Large” không có một threshold cố định** sang **Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Large ngôn ngữ (language / 언어) mô hình (model / 모델) không phải một loại xác suất (probability / 확률) mô hình (model / 모델) hoàn toàn mới. cốt lõi (core / 핵심) vẫn là ngôn ngữ (language / 언어) modeling: estimate phân phối (distribution / 분포) của đơn vị từ (token / 토큰) dựa trên ngữ cảnh (context / 맥락). Điều thay đổi là **quy mô (scale / 규모) của mô hình (model / 모델), dữ liệu (data / 데이터), compute và post-training**, khiến mô hình (model / 모델) học reusable representations và capabilities rộng hơn nhiều tác vụ (task / 작업) cụ thể.

Một decoder-only LLM thường vẫn tối ưu:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

với Transformer. Nhưng quy mô (scale / 규모) làm pretrained mô hình (model / 모델) trở thành **foundation mô hình (model / 모델)** có thể adapt qua prompt, examples, fine-tuning, preference tối ưu hóa (optimization / 최적화) và tools.

## “Large” không có một threshold cố định

Không có parameter count chính thức nơi ngôn ngữ (language / 언어) mô hình (model / 모델) đột nhiên thành LLM. Term phản ánh practical regime: mô hình (model / 모델) đủ lớn, trained đủ broad để hỗ trợ (support / 지원) many downstream tasks/capabilities.

Parameter count alone không đủ. dữ liệu (data / 데이터) chất lượng (quality / 품질), tokens trained, kiến trúc (architecture / 아키텍처), ngữ cảnh (context / 맥락) length và post-training quyết định năng lực (capability / 역량).

Một smaller well-trained mô hình (model / 모델) có thể outperform larger poorly trained mô hình (model / 모델) trên mục tiêu (target / 대상) lĩnh vực (domain / 도메인).

## Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델)

Pretraining corpus rất lớn:

```text
web
books
code
papers
forums
multilingual text
synthetic/curated data
```

Mô hình (model / 모델) train next-token prediction/self-supervised mục tiêu (objective / 목표).

Kết quả (result / 결과) **cơ sở (base / 기반) mô hình (model / 모델)** giỏi continuation nhưng chưa chắc follow người dùng (user / 사용자) instructions reliably.

Cơ sở (base / 기반) mô hình (model / 모델) sees many styles/tasks embedded in văn bản (text / 텍스트) and may learn latent capabilities, nhưng giao diện (interface / 인터페이스) default vẫn “continue likely văn bản (text / 텍스트)”.

## Foundation mô hình (model / 모델)

Foundation mô hình (model / 모델) là pretrained broad mô hình (model / 모델) có thể adapt nhiều downstream tasks.

LLM thường là văn bản (text / 텍스트)/code-centered foundation mô hình (model / 모델). Multimodal foundation mô hình (model / 모델) adds vision/audio etc.

Foundation status comes from reusable biểu diễn (representation / 표현)/năng lực (capability / 역량), not only kích thước (size / 크기).

## Post-Training

Hiện đại (modern / 현대적) assistant hành vi (behavior / 동작) thường đến từ post-training:

```text
Pretrained base model
→ supervised/instruction fine-tuning
→ preference optimization / RLHF / DPO-like stages
→ safety/domain tuning
→ tool-use training
```

Post-training changes hành vi (behavior / 동작) phân phối (distribution / 분포) without necessarily adding broad world kiến thức (knowledge / 지식) comparable pretraining quy mô (scale / 규모).

## Năng lực (capability / 역량) vs hành vi (behavior / 동작)

Cơ sở (base / 기반) mô hình (model / 모델) may possess năng lực (capability / 역량) to answer question but not default choose useful phản hồi (response / 응답) format. Instruction tuning teaches hành vi (behavior / 동작) to expose/use capabilities.

Conversely post-training cannot reliably create deep kiến thức (knowledge / 지식) absent from biểu diễn (representation / 표현)/dữ liệu (data / 데이터) with tiny dataset.

Useful distinction:

```text
pretraining → broad representations/knowledge/capabilities
post-training → how/when to express and prioritize behaviors
```

not absolute, but good mô hình tư duy (mental model / 사고 모델).

## In-Context học tập (learning / 학습)

At suy luận (inference / 추론), prompt includes tác vụ (task / 작업) description/examples. Weights remain fixed, yet hành vi (behavior / 동작) changes based on ngữ cảnh (context / 맥락).

```text
Examples in prompt
→ Transformer processes pattern
→ continuation follows inferred task
```

This differs fine-tuning:

- in-context: temporary, context-bound, no weight cập nhật (update / 업데이트);
- fine-tuning: parameter changes persist.

## Emergent Capabilities

Some capabilities appear sharply as quy mô (scale / 규모) increases under discrete metrics. But apparent “emergence” can partly kết quả (result / 결과) thresholded đo lường (measurement / 측정); underlying mất mát (loss / 손실)/năng lực (capability / 역량) may improve smoothly.

Avoid mystical interpretation. Scaling can create qualitative practical changes when smooth improvements cross tác vụ (task / 작업) viability thresholds.

## LLM kiến thức (knowledge / 지식) in Parameters

Pretraining compresses statistical cấu trúc (structure / 구조) into weights. Facts are phân tán (distributed / 분산), not records with tường minh (explicit / 명시적) provenance.

Consequences:

- recall probabilistic;
- nguồn (source / 소스) not inherently stored/retrievable;
- updates require retraining/editing/retrieval;
- conflicts/rare facts unreliable;
- temporal cutoff/staleness.

RAG externalizes updateable kiến thức (knowledge / 지식).

## Ngữ cảnh (context / 맥락) as Temporary Working đầu vào (input / 입력)

Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) holds prompt, documents, conversation, công cụ (tool / 도구) outputs. It acts like temporary thông tin (information / 정보) accessible by attention, distinct parameterized long-term learned trạng thái (state / 상태).

Useful hệ thống (system / 시스템) distinction:

```text
Weights  → persistent learned statistical knowledge/behavior
Context  → request-specific working information
Retrieval/tool → external dynamic knowledge/state
Memory system → persisted application-level user/task state
```

## LLM không tự động là tác nhân (agent / 에이전트)

LLM maps ngữ cảnh (context / 맥락) to tokens/tool-call biểu diễn (representation / 표현). tác nhân (agent / 에이전트) adds vòng lặp (loop / 루프):

```text
goal
→ model decision
→ tool/action
→ environment result
→ updated state
→ repeat
```

LLM can be lập luận (reasoning / 추론)/planning thành phần (component / 컴포넌트) but tác nhân (agent / 에이전트) requires hệ thống (system / 시스템) orchestration.

## LLM không tự động là RAG

RAG adds bên ngoài (external / 외부) retrieval before/during generation. A plain LLM answering from parameters is not RAG.

RAG chất lượng (quality / 품질) depends retriever/chunking/reranking/ngữ cảnh (context / 맥락) usage, not only mô hình (model / 모델).

## Decoder-Only Dominance

Decoder-only kiến trúc (architecture / 아키텍처) became dùng chung (common / 공통) general assistant mô hình (model / 모델) because one nhân quả (causal / 인과적) giao diện (interface / 인터페이스) handles:

```text
completion
chat
classification-as-generation
code
structured output
tool calls
few-shot tasks
```

Encoder/encoder-decoder các mô hình (models / 모델들) remain more efficient for many specialized tasks.

## Chat mô hình (model / 모델) là giao thức (protocol / 프로토콜) trên đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스)

Conversation usually serialized with special tokens/template:

```text
<system> ...
<user> ...
<assistant> ...
```

Mô hình (model / 모델) still sees one đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스). Roles matter because post-training teaches hành vi (behavior / 동작) conditional on those markers.

Changing chat template can materially affect chất lượng (quality / 품질)/an toàn (safety / 안전).

## LLM ngăn xếp (stack / 스택) như một hệ thống (system / 시스템)

```text
User/Application
↓
Prompt / context builder
↓
Tokenizer
↓
Transformer inference
↓
Logits / sampling / structured decoding
↓
Optional tools/retrieval/validation
↓
Output
```

Môi trường vận hành (production / 운영 환경) chất lượng (quality / 품질) often limited by ngữ cảnh (context / 맥락) construction, công cụ (tool / 도구) errors, permissions, độ trễ (latency / 지연 시간) and evaluation — not mô hình (model / 모델) alone.

## Mô hình tư duy (mental model / 사고 모델)

> LLM = large-scale pretrained chuỗi (sequence / 시퀀스) predictor whose learned representations are broad enough to be reused/adapted for many ngôn ngữ (language / 언어)/mã (code / 코드) tasks; assistant hành vi (behavior / 동작) is a post-trained hệ thống (system / 시스템) built on top.

## Dùng chung (common / 공통) Misconceptions

### “LLM khác ngôn ngữ (language / 언어) mô hình (model / 모델) vì nó lập luận (reasoning / 추론) thay vì predict đơn vị từ (token / 토큰)”

Suy luận (inference / 추론) vẫn implemented through đơn vị từ (token / 토큰) prediction; richer computation inside Transformer can hỗ trợ (support / 지원) reasoning-like hành vi (behavior / 동작).

### “More parameters means more kiến thức (knowledge / 지식) linearly”

Năng lực (capability / 역량) depends dữ liệu (data / 데이터)/huấn luyện (training / 학습)/kiến trúc (architecture / 아키텍처); parameter count alone not kiến thức (knowledge / 지식) count.

### “ChatGPT-like mô hình (model / 모델) is just pretrained LM”

Useful chat hành vi (behavior / 동작) requires post-training, prompting/giao thức (protocol / 프로토콜), an toàn (safety / 안전) and hệ thống (system / 시스템) tích hợp (integration / 통합).

### “LLM bộ nhớ (memory / 메모리) is its ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우)”

Ngữ cảnh (context / 맥락) is temporary đầu vào (input / 입력); persistent ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리) is separate hệ thống (system / 시스템).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Prerequisites: [Language Models](../07_natural_language_processing/02_language_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md), [NLP tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md).

Xem tiếp: [LLM Tokenization](./01_llm_tokenization.md), then embeddings/Transformer internals, pretraining and post-training.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [01 llm tokenization](./01_llm_tokenization.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
