# Contextual Embeddings: meaning thay đổi theo context

Static word embedding gán một vector duy nhất cho mỗi word/token type. Nhưng language có polysemy và contextual meaning: `bank` trong `river bank` khác `bank loan`. **Contextual Embedding (문맥 임베딩)** tính representation của token như function của cả context.

Transformer làm điều này bằng self-attention: token ban đầu có embedding lookup giống nhau, nhưng qua layers nó trao đổi information với neighboring/distant tokens và trở thành hidden state context-specific.

## Static vs Contextual

Static:

\[
e(w)=v_w
\]

Contextual:

\[
h_i=f_\theta(x_1,...,x_T,i)
\]

Cùng token ID ở position/context khác có `h_i` khác.

## ELMo: contextualization bằng bidirectional LM

ELMo là milestone trước Transformer. Nó dùng stacked bidirectional LSTMs; representation kết hợp hidden states từ multiple layers.

Insight: different layers capture different linguistic information, and context-sensitive token representation improves downstream tasks.

## BERT representations

BERT uses bidirectional Transformer encoder trained with masked-language-model objective.

Input representation combines token/subword + position + segment/type embeddings (implementation-specific).

After each Transformer layer, token vector becomes contextualized.

Final/selected layers feed classification, QA, NER etc.

## Token Representation vs Sentence Representation

Token-level tasks use per-token hidden states.

Sentence/document tasks need pooling:

- `[CLS]` representation;
- mean pooling;
- max pooling;
- attention pooling;
- dedicated sentence-embedding fine-tuning.

Raw BERT `[CLS]` is not automatically ideal semantic sentence embedding. Objective matters.

## Sentence-BERT / Contrastive Sentence Embeddings

Cross-encoder BERT jointly processes two texts and can model rich token interactions, but expensive for retrieval because every query-document pair needs forward pass.

Bi-encoder encodes separately:

\[
q=f(qtext),\quad d=g(document)
\]

score:

\[
s(q,d)=cos(q,d)
\]

allows precompute document vectors + ANN search.

Sentence-BERT-style contrastive training makes pooled embeddings suitable semantic similarity/retrieval.

## Bi-Encoder vs Cross-Encoder

**Bi-encoder**:

```text
query → vector ┐
               ├→ similarity
 doc  → vector ┘
```

Fast retrieval, information compressed into independent vectors.

**Cross-encoder**:

```text
[query ; document]
        ↓ joint Transformer
      relevance score
```

More accurate pairwise interaction but costly.

Modern retrieval often:

```text
bi-encoder retrieve top K
→ cross-encoder rerank
```

This architecture is core RAG retrieval stack.

## Contextual token geometry

A token's hidden state encodes mixture of lexical, syntactic, semantic and positional factors. Layers often show progression but not clean strict hierarchy.

Probing studies can decode linguistic attributes from hidden states, but decodability does not prove causal use.

## Layer Selection

Last layer optimized closest pretraining output objective; intermediate layers may be better for some linguistic tasks.

Some methods concatenate/learn weighted mixture across layers.

No universal “last layer always best”.

## Pooling and Length Bias

Mean pooling averages token vectors; long docs may dilute salient segments. `[CLS]` depends training objective; max pooling favors strongest feature per dimension.

For long document retrieval, chunk-level embeddings often better than one vector for entire document.

Chunking introduces segmentation/provenance trade-offs.

## Normalization

Embedding vectors often L2-normalized:

\[
\hat z=\frac{z}{\|z\|}
\]

Then dot product equals cosine similarity:

\[
\hat q^T\hat d=cos(q,d)
\]

ANN indexes may assume one metric; preprocessing must match model training/recommendation.

## Contrastive Training

Positive query-doc pairs should score higher than negatives.

InfoNCE-like loss:

\[
L_i=-\log\frac{e^{s(q_i,d_i^+)/\tau}}
{e^{s(q_i,d_i^+)/\tau}+\sum_j e^{s(q_i,d_j^-)/\tau}}
\]

In-batch negatives provide efficiency, but false negatives (actually relevant docs treated negative) hurt.

Hard negatives improve discrimination near decision boundary.

## Domain Adaptation

General embedding model may fail specialized vocabulary/relations. Fine-tuning on domain query-document pairs can improve retrieval.

However overfitting narrow domain may reduce general semantic behavior. Evaluation needs representative queries.

## Multilingual Embeddings

Multilingual encoders align sentences from multiple languages in shared vector space. Cross-lingual retrieval becomes possible:

```text
Vietnamese query
→ vector
→ retrieve Korean/English document vectors
```

Alignment quality varies languages/domains and tokenizer efficiency.

## Context Length

Embedding model max context may truncate long docs. Truncation silently loses tail information.

Production pipeline should explicitly:

```text
inspect token count
chunk / summarize / hierarchical encode
track source span
```

## Embedding Drift và Versioning

Change embedding model/version → geometry changes. Old corpus vectors should not be mixed with new query vectors unless backward compatibility empirically validated.

Re-embedding/re-indexing can be costly; model version must live in vector-store metadata.

## Semantic Similarity ≠ Relevance

Two texts can be semantically similar but irrelevant to query intent. Retrieval relevance includes task-specific utility, recency, authority, permissions and metadata constraints.

Dense embedding should combine with lexical search, filters/rerankers when appropriate.

## Mental Model

> Static embedding asks “symbol này thường liên quan gì?”; contextual embedding asks “symbol/text này trong context hiện tại đang biểu diễn gì?”.

For retrieval, sentence embedding further asks “nén toàn bộ text thành vector nào để similarity phản ánh relevance objective?”.

## Common Misconceptions

### “BERT output nào cũng dùng làm embedding search được”

Raw hidden state/pooling may not be trained for semantic similarity. Use retrieval/sentence embedding objective.

### “Cross-encoder luôn tốt hơn nên dùng cho toàn corpus”

Pairwise cost quá cao; typical use rerank small candidate set.

### “Cosine similarity 0.9 nghĩa 90% relevant”

Similarity score không calibrated probability.

### “Multilingual shared space means all languages equally good”

Training balance/tokenization/data quality lead uneven performance.

## Knowledge Connection

Contextual embeddings combine [Transformer](../06_deep_learning_architectures/05_transformer.md), [Contrastive Representation Learning](../05_neural_networks/08_representation_learning.md) and prepare [Information Retrieval](./08_search_and_information_retrieval.md), RAG and LLM embeddings.