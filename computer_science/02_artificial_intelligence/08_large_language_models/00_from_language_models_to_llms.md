# Từ Language Models tới Large Language Models

Large Language Model (LLM / 대규모 언어 모델) không phải một loại probability model hoàn toàn mới. Core vẫn là language modeling: estimate distribution của token dựa trên context. Điều thay đổi là **scale của model, data, compute và post-training**, khiến model học reusable representations và capabilities rộng hơn nhiều task cụ thể.

Một decoder-only LLM thường vẫn tối ưu:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

với Transformer. Nhưng scale làm pretrained model trở thành **foundation model** có thể adapt qua prompt, examples, fine-tuning, preference optimization và tools.

## “Large” không có một threshold cố định

Không có parameter count chính thức nơi language model đột nhiên thành LLM. Term phản ánh practical regime: model đủ lớn, trained đủ broad để support many downstream tasks/capabilities.

Parameter count alone không đủ. Data quality, tokens trained, architecture, context length và post-training quyết định capability.

Một smaller well-trained model có thể outperform larger poorly trained model trên target domain.

## Pretraining tạo base model

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

Model train next-token prediction/self-supervised objective.

Result **base model** giỏi continuation nhưng chưa chắc follow user instructions reliably.

Base model sees many styles/tasks embedded in text and may learn latent capabilities, nhưng interface default vẫn “continue likely text”.

## Foundation Model

Foundation model là pretrained broad model có thể adapt nhiều downstream tasks.

LLM thường là text/code-centered foundation model. Multimodal foundation model adds vision/audio etc.

Foundation status comes from reusable representation/capability, not only size.

## Post-Training

Modern assistant behavior thường đến từ post-training:

```text
Pretrained base model
→ supervised/instruction fine-tuning
→ preference optimization / RLHF / DPO-like stages
→ safety/domain tuning
→ tool-use training
```

Post-training changes behavior distribution without necessarily adding broad world knowledge comparable pretraining scale.

## Capability vs Behavior

Base model may possess capability to answer question but not default choose useful response format. Instruction tuning teaches behavior to expose/use capabilities.

Conversely post-training cannot reliably create deep knowledge absent from representation/data with tiny dataset.

Useful distinction:

```text
pretraining → broad representations/knowledge/capabilities
post-training → how/when to express and prioritize behaviors
```

not absolute, but good mental model.

## In-Context Learning

At inference, prompt includes task description/examples. Weights remain fixed, yet behavior changes based on context.

```text
Examples in prompt
→ Transformer processes pattern
→ continuation follows inferred task
```

This differs fine-tuning:

- in-context: temporary, context-bound, no weight update;
- fine-tuning: parameter changes persist.

## Emergent Capabilities

Some capabilities appear sharply as scale increases under discrete metrics. But apparent “emergence” can partly result thresholded measurement; underlying loss/capability may improve smoothly.

Avoid mystical interpretation. Scaling can create qualitative practical changes when smooth improvements cross task viability thresholds.

## LLM Knowledge in Parameters

Pretraining compresses statistical structure into weights. Facts are distributed, not records with explicit provenance.

Consequences:

- recall probabilistic;
- source not inherently stored/retrievable;
- updates require retraining/editing/retrieval;
- conflicts/rare facts unreliable;
- temporal cutoff/staleness.

RAG externalizes updateable knowledge.

## Context as Temporary Working Input

Context window holds prompt, documents, conversation, tool outputs. It acts like temporary information accessible by attention, distinct parameterized long-term learned state.

Useful system distinction:

```text
Weights  → persistent learned statistical knowledge/behavior
Context  → request-specific working information
Retrieval/tool → external dynamic knowledge/state
Memory system → persisted application-level user/task state
```

## LLM không tự động là Agent

LLM maps context to tokens/tool-call representation. Agent adds loop:

```text
goal
→ model decision
→ tool/action
→ environment result
→ updated state
→ repeat
```

LLM can be reasoning/planning component but agent requires system orchestration.

## LLM không tự động là RAG

RAG adds external retrieval before/during generation. A plain LLM answering from parameters is not RAG.

RAG quality depends retriever/chunking/reranking/context usage, not only model.

## Decoder-Only Dominance

Decoder-only architecture became common general assistant model because one causal interface handles:

```text
completion
chat
classification-as-generation
code
structured output
tool calls
few-shot tasks
```

Encoder/encoder-decoder models remain more efficient for many specialized tasks.

## Chat Model là protocol trên token sequence

Conversation usually serialized with special tokens/template:

```text
<system> ...
<user> ...
<assistant> ...
```

Model still sees one token sequence. Roles matter because post-training teaches behavior conditional on those markers.

Changing chat template can materially affect quality/safety.

## LLM stack như một system

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

Production quality often limited by context construction, tool errors, permissions, latency and evaluation — not model alone.

## Mental Model

> LLM = large-scale pretrained sequence predictor whose learned representations are broad enough to be reused/adapted for many language/code tasks; assistant behavior is a post-trained system built on top.

## Common Misconceptions

### “LLM khác language model vì nó reasoning thay vì predict token”

Inference vẫn implemented through token prediction; richer computation inside Transformer can support reasoning-like behavior.

### “More parameters means more knowledge linearly”

Capability depends data/training/architecture; parameter count alone not knowledge count.

### “ChatGPT-like model is just pretrained LM”

Useful chat behavior requires post-training, prompting/protocol, safety and system integration.

### “LLM memory is its context window”

Context is temporary input; persistent application memory is separate system.

## Knowledge Connection

Prerequisites: [Language Models](../07_natural_language_processing/02_language_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md), [NLP tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md).

Xem tiếp: [LLM Tokenization](./01_llm_tokenization.md), then embeddings/Transformer internals, pretraining and post-training.