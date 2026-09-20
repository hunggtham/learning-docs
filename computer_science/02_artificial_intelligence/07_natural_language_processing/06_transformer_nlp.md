# Transformer NLP: Encoder, Decoder và Task Adaptation

Transformer architecture là general mechanism; NLP biến mechanism đó thành các model families khác nhau bằng **masking, pretraining objective, pooling/head và fine-tuning strategy**. BERT, GPT và T5 không chỉ khác tên — chúng encode information flow khác nhau.

## Encoder-Only NLP

Encoder self-attention thường bidirectional. Mỗi token có thể attend left/right context.

BERT-style pretraining dùng Masked Language Modeling (MLM): chọn một số tokens, corrupt/mask, predict originals.

Representation tốt cho:

- text classification;
- token classification/NER;
- extractive QA;
- sentence-pair scoring;
- embeddings sau task-specific training.

Encoder-only không naturally generate long autoregressive text, vì training/information flow không causal.

## Decoder-Only NLP

Causal mask:

\[
P(x_t\mid x_{<t})
\]

Một architecture có thể handle many tasks by expressing input/task as prefix and generating output continuation.

This flexibility scales naturally into LLM/instruction following.

For pure classification, decoder model may be compute-inefficient compared with smaller encoder but unified deployment can justify it.

## Encoder–Decoder NLP

Encoder reads full source bidirectionally; decoder generates target causally with cross-attention.

Natural for:

- translation;
- summarization;
- structured transformation;
- conditional generation.

T5/BART families show strong text-to-text paradigm.

## Pretraining Objective Shapes Capability

Same architecture under different objectives learns different behavior.

Causal LM rewards continuation.

Masked LM rewards reconstruct hidden tokens using both sides.

Denoising seq2seq rewards reconstruct entire text from corrupted input.

Contrastive objectives reward similarity geometry.

Do not infer capability solely from architecture.

## Fine-Tuning for Classification

Encoder output can pool `[CLS]` or mean hidden states:

\[
h_{pool}=Pool(H)
\]

Classifier:

\[
p(y\mid x)=softmax(Wh_{pool}+b)
\]

Fine-tuning updates all/partial encoder + head.

Small dataset risks overfit/catastrophic forgetting; lower LR, regularization, adapters can help.

## Token Classification

NER/POS tagging uses per-token hidden state:

\[
p(y_i\mid x)=softmax(Wh_i+b)
\]

Subword complication: one word may split multiple pieces. Labeling strategy must decide first-piece/all-piece aggregation.

Metrics should reconstruct word/entity spans correctly.

## Extractive Question Answering

Given `[question ; context]`, encoder outputs token states. Two heads predict start/end positions:

\[
P(start=i),\qquad P(end=j)
\]

Answer constrained to span in context, reducing free-form hallucination but cannot answer if answer absent unless no-answer modeled.

## Natural Language Inference

Input premise+hypothesis, classify entailment/contradiction/neutral.

NLI datasets useful for semantic reasoning but models may exploit annotation artifacts. High benchmark score does not prove robust logical inference.

## Sentence Pair Cross-Encoding

For relevance/paraphrase:

```text
[CLS] query [SEP] document
```

joint self-attention lets every token pair interact, giving accurate scoring but O(number of candidate pairs) inference cost.

Bi-encoder vs cross-encoder trade-off becomes central retrieval architecture.

## Prompt-Based Fine-Tuning

Instead of classification head, reformulate task as language prediction:

```text
Review: ... Sentiment: [MASK]
```

or generation.

Prompting aligns downstream task with pretraining objective, useful few-shot regimes. Verbalizer choice can bias results.

## Parameter-Efficient Fine-Tuning

Rather than update all weights:

- adapters insert small trainable modules;
- LoRA learns low-rank updates;
- prefix/prompt tuning learns virtual token-like vectors;
- bias-only methods update subset.

Benefits: memory/storage, multi-tenant specialization and reduced forgetting. Trade-off can be lower ceiling/task-specific quirks.

## Long Documents

Vanilla Transformer context finite/quadratic. Strategies:

- truncate;
- sliding windows;
- hierarchical encode chunks then aggregate;
- sparse/long attention;
- retrieval before encoding.

Task determines whether local chunking loses discourse relation.

## Domain-Specific NLP Models

Biomedical/legal/financial corpora contain vocabulary/style/entities not well represented general models. Continued pretraining on domain corpus then task fine-tuning can improve.

But domain pretraining needs quality/copyright/privacy controls and can shift general capability.

## Multilingual Transformer

Shared tokenizer + parameters across languages enables transfer. High-resource languages may dominate capacity; scripts/token efficiency and corpus balance matter.

Cross-lingual transfer works because shared representations align statistical structures, but performance uneven. Evaluate each language, especially Korean/Vietnamese target use.

## Distillation

Teacher Transformer transfers behavior to smaller student using soft targets/hidden-state losses.

Goal reduce latency/memory while retain performance. Student architecture can be fewer layers/smaller hidden dimension.

Distillation will reappear in deployment/inference layer.

## Quantization-aware NLP Preview

Inference can quantize weights/activations. Some NLP models tolerate INT8/4-bit well; sensitive layers/outliers may require mixed precision/calibration.

Model compression is system constraint, not separate from NLP deployment.

## Mental Model

```text
Transformer mechanism
+ attention mask / information flow
+ pretraining objective
+ task head / prompting
+ adaptation method
= NLP model behavior
```

## Common Misconceptions

### “BERT và GPT chỉ khác training data”

Architecture direction/mask and objective differ fundamentally.

### “Encoder model không generate nên kém hơn”

For classification/retrieval/reranking, encoder can be much more efficient and accurate per compute.

### “Fine-tuning all weights always best”

Small data/multi-task/serving constraints may favor PEFT.

### “Multilingual model means language-independent representation hoàn hảo”

Cross-lingual alignment is imperfect and data-dependent.

## Knowledge Connection

Xem [Transformer architecture](../06_deep_learning_architectures/05_transformer.md), [Seq2Seq NLP](./05_sequence_to_sequence_nlp.md), and next [Information Extraction](./07_information_extraction.md).