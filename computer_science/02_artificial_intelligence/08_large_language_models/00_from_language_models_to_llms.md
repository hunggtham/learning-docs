# Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **“Large” không có một threshold cố định** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델)** tiếp nhận điểm tựa từ **“Large” không có một threshold cố định** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Foundation mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Foundation mô hình (model / 모델)** tiếp nhận điểm tựa từ **Pretraining tạo cơ sở (base / 기반) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Post-Training** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Foundation mô hình (model / 모델)

Foundation mô hình (model / 모델) là pretrained broad mô hình (model / 모델) có thể adapt nhiều downstream tasks.

LLM thường là văn bản (text / 텍스트)/code-centered foundation mô hình (model / 모델). Multimodal foundation mô hình (model / 모델) adds vision/audio etc.

Foundation status comes from reusable biểu diễn (representation / 표현)/năng lực (capability / 역량), not only kích thước (size / 크기).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Post-Training** tiếp nhận điểm tựa từ **Foundation mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Năng lực (capability / 역량) vs hành vi (behavior / 동작)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Năng lực (capability / 역량) vs hành vi (behavior / 동작)** tiếp nhận điểm tựa từ **Post-Training** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **In-Context học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Năng lực (capability / 역량) vs hành vi (behavior / 동작)

Cơ sở (base / 기반) mô hình (model / 모델) may possess năng lực (capability / 역량) to answer question but not default choose useful phản hồi (response / 응답) format. Instruction tuning teaches hành vi (behavior / 동작) to expose/use capabilities.

Conversely post-training cannot reliably create deep kiến thức (knowledge / 지식) absent from biểu diễn (representation / 표현)/dữ liệu (data / 데이터) with tiny dataset.

Useful distinction:

```text
pretraining → broad representations/knowledge/capabilities
post-training → how/when to express and prioritize behaviors
```

not absolute, but good mô hình tư duy (mental model / 사고 모델).

> **Chuyển mạch:** Ở chặng này của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **In-Context học tập (learning / 학습)** tiếp nhận điểm tựa từ **Năng lực (capability / 역량) vs hành vi (behavior / 동작)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Emergent Capabilities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Emergent Capabilities** tiếp nhận điểm tựa từ **In-Context học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM kiến thức (knowledge / 지식) in Parameters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Emergent Capabilities

Some capabilities appear sharply as quy mô (scale / 규모) increases under discrete metrics. But apparent “emergence” can partly kết quả (result / 결과) thresholded đo lường (measurement / 측정); underlying mất mát (loss / 손실)/năng lực (capability / 역량) may improve smoothly.

Avoid mystical interpretation. Scaling can create qualitative practical changes when smooth improvements cross tác vụ (task / 작업) viability thresholds.

> **Chuyển mạch:** Trong **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **LLM kiến thức (knowledge / 지식) in Parameters** tiếp nhận điểm tựa từ **Emergent Capabilities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) as Temporary Working đầu vào (input / 입력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM kiến thức (knowledge / 지식) in Parameters

Pretraining compresses statistical cấu trúc (structure / 구조) into weights. Facts are phân tán (distributed / 분산), not records with tường minh (explicit / 명시적) provenance.

Consequences:

- recall probabilistic;
- nguồn (source / 소스) not inherently stored/retrievable;
- updates require retraining/editing/retrieval;
- conflicts/rare facts unreliable;
- temporal cutoff/staleness.

RAG externalizes updateable kiến thức (knowledge / 지식).

> **Chuyển mạch:** Ở chặng này của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Ngữ cảnh (context / 맥락) as Temporary Working đầu vào (input / 입력)** tiếp nhận điểm tựa từ **LLM kiến thức (knowledge / 지식) in Parameters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM không tự động là tác nhân (agent / 에이전트)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) as Temporary Working đầu vào (input / 입력)

Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) holds prompt, documents, conversation, công cụ (tool / 도구) outputs. It acts like temporary thông tin (information / 정보) accessible by attention, distinct parameterized long-term learned trạng thái (state / 상태).

Useful hệ thống (system / 시스템) distinction:

```text
Weights  → persistent learned statistical knowledge/behavior
Context  → request-specific working information
Retrieval/tool → external dynamic knowledge/state
Memory system → persisted application-level user/task state
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **LLM không tự động là tác nhân (agent / 에이전트)** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) as Temporary Working đầu vào (input / 입력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **LLM không tự động là RAG** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **LLM không tự động là RAG** tiếp nhận điểm tựa từ **LLM không tự động là tác nhân (agent / 에이전트)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decoder-Only Dominance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM không tự động là RAG

RAG adds bên ngoài (external / 외부) retrieval before/during generation. A plain LLM answering from parameters is not RAG.

RAG chất lượng (quality / 품질) depends retriever/chunking/reranking/ngữ cảnh (context / 맥락) usage, not only mô hình (model / 모델).

> **Chuyển mạch:** Ở chặng này của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Decoder-Only Dominance** tiếp nhận điểm tựa từ **LLM không tự động là RAG** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chat mô hình (model / 모델) là giao thức (protocol / 프로토콜) trên đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Decoder-Only Dominance** xác định đầu vào; **Chat mô hình (model / 모델) là giao thức (protocol / 프로토콜) trên đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **LLM ngăn xếp (stack / 스택) như một hệ thống (system / 시스템)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chat mô hình (model / 모델) là giao thức (protocol / 프로토콜) trên đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스)

Conversation usually serialized with special tokens/template:

```text
<system> ...
<user> ...
<assistant> ...
```

Mô hình (model / 모델) still sees one đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스). Roles matter because post-training teaches hành vi (behavior / 동작) conditional on those markers.

Changing chat template can materially affect chất lượng (quality / 품질)/an toàn (safety / 안전).

> **Chuyển mạch:** Trong **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Chat mô hình (model / 모델) là giao thức (protocol / 프로토콜) trên đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스)** xác định đầu vào; **LLM ngăn xếp (stack / 스택) như một hệ thống (system / 시스템)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## LLM ngăn xếp (stack / 스택) như một hệ thống (system / 시스템)

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

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

> **Chuyển mạch:** Ở chặng này của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **LLM ngăn xếp (stack / 스택) như một hệ thống (system / 시스템)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> LLM = large-scale pretrained chuỗi (sequence / 시퀀스) predictor whose learned representations are broad enough to be reused/adapted for many ngôn ngữ (language / 언어)/mã (code / 코드) tasks; assistant hành vi (behavior / 동작) is a post-trained hệ thống (system / 시스템) built on top.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “LLM khác ngôn ngữ (language / 언어) mô hình (model / 모델) vì nó lập luận (reasoning / 추론) thay vì predict đơn vị từ (token / 토큰)”

Suy luận (inference / 추론) vẫn implemented through đơn vị từ (token / 토큰) prediction; richer computation inside Transformer can hỗ trợ (support / 지원) reasoning-like hành vi (behavior / 동작).

### “More parameters means more kiến thức (knowledge / 지식) linearly”

Năng lực (capability / 역량) depends dữ liệu (data / 데이터)/huấn luyện (training / 학습)/kiến trúc (architecture / 아키텍처); parameter count alone not kiến thức (knowledge / 지식) count.

### “ChatGPT-like mô hình (model / 모델) is just pretrained LM”

Useful chat hành vi (behavior / 동작) requires post-training, prompting/giao thức (protocol / 프로토콜), an toàn (safety / 안전) and hệ thống (system / 시스템) tích hợp (integration / 통합).

### “LLM bộ nhớ (memory / 메모리) is its ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우)”

Ngữ cảnh (context / 맥락) is temporary đầu vào (input / 입력); persistent ứng dụng (application / 애플리케이션) bộ nhớ (memory / 메모리) is separate hệ thống (system / 시스템).

> **Chuyển mạch:** Trong **Từ ngôn ngữ (language / 언어) các mô hình (models / 모델들) tới Large ngôn ngữ (language / 언어) các mô hình (models / 모델들)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Prerequisites: [Language Models](../07_natural_language_processing/02_language_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md), [NLP tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md).

Xem tiếp: [LLM Tokenization](./01_llm_tokenization.md), then embeddings/Transformer internals, pretraining and post-training.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
