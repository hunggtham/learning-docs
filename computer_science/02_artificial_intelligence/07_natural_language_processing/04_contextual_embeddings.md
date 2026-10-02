# Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Contextual embeddings**. Route đi từ static/contextual distinction → bidirectional context → ELMo-style representations → transformer contextual states → polysemy/transfer limits, để meaning được nối với vị trí trong sequence.

Static word embedding gán một véc-tơ (vector / 벡터) duy nhất cho mỗi word/đơn vị từ (token / 토큰) kiểu (type / 타입). Nhưng ngôn ngữ (language / 언어) có polysemy và contextual meaning: `bank` trong `river bank` khác `bank loan`. **Contextual Embedding (문맥 임베딩)** tính biểu diễn (representation / 표현) của đơn vị từ (token / 토큰) như hàm (function / 함수) của cả ngữ cảnh (context / 맥락).

Transformer làm điều này bằng self-attention: đơn vị từ (token / 토큰) ban đầu có embedding lookup giống nhau, nhưng qua layers nó trao đổi thông tin (information / 정보) với neighboring/distant tokens và trở thành hidden trạng thái (state / 상태) context-specific.

## Static vs Contextual

Static:

\[
e(w)=v_w
\]

Contextual:

\[
h_i=f_\theta(x_1,...,x_T,i)
\]

Cùng đơn vị từ (token / 토큰) ID ở position/ngữ cảnh (context / 맥락) khác có `h_i` khác.

> **Chuyển mạch:** Trong **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **ELMo: contextualization bằng bidirectional LM** tiếp nhận điểm tựa từ **Static vs Contextual** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BERT representations** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## ELMo: contextualization bằng bidirectional LM

ELMo là milestone trước Transformer. Nó dùng stacked bidirectional LSTMs; biểu diễn (representation / 표현) kết hợp hidden states từ multiple layers.

Insight: different layers capture different linguistic thông tin (information / 정보), and context-sensitive đơn vị từ (token / 토큰) biểu diễn (representation / 표현) improves downstream tasks.

> **Chuyển mạch:** Ở chặng này của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **BERT representations** tiếp nhận điểm tựa từ **ELMo: contextualization bằng bidirectional LM** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Đơn vị từ (token / 토큰) biểu diễn (representation / 표현) vs Sentence biểu diễn (representation / 표현)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BERT representations

BERT uses bidirectional Transformer encoder trained with masked-language-model mục tiêu (objective / 목표).

Đầu vào (input / 입력) biểu diễn (representation / 표현) combines đơn vị từ (token / 토큰)/subword + position + segment/kiểu (type / 타입) embeddings (implementation-specific).

After each Transformer tầng (layer / 계층), đơn vị từ (token / 토큰) véc-tơ (vector / 벡터) becomes contextualized.

Final/selected layers feed classification, QA, NER etc.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Đơn vị từ (token / 토큰) biểu diễn (representation / 표현) vs Sentence biểu diễn (representation / 표현)** tiếp nhận điểm tựa từ **BERT representations** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sentence-BERT / Contrastive Sentence Embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Đơn vị từ (token / 토큰) biểu diễn (representation / 표현) vs Sentence biểu diễn (representation / 표현)

Token-level tasks use per-token hidden states.

Sentence/document tasks need pooling:

- `[CLS]` biểu diễn (representation / 표현);
- mean pooling;
- max pooling;
- attention pooling;
- dedicated sentence-embedding fine-tuning.

Raw BERT `[CLS]` is not automatically ideal ngữ nghĩa (semantic / 의미적) sentence embedding. mục tiêu (objective / 목표) matters.

> **Chuyển mạch:** Trong **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Đơn vị từ (token / 토큰) biểu diễn (representation / 표현) vs Sentence biểu diễn (representation / 표현)** đã nêu tiêu chí phân biệt, còn **Sentence-BERT / Contrastive Sentence Embeddings** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Bi-Encoder vs Cross-Encoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sentence-BERT / Contrastive Sentence Embeddings

Cross-encoder BERT jointly processes two texts and can mô hình (model / 모델) rich đơn vị từ (token / 토큰) interactions, but expensive for retrieval because every query-document pair needs forward pass.

Bi-encoder encodes separately:

\[
q=f(qtext),\quad d=g(document)
\]

score:

\[
s(q,d)=cos(q,d)
\]

allows precompute document vectors + ANN tìm kiếm (search / 검색).

Sentence-BERT-style contrastive huấn luyện (training / 학습) makes pooled embeddings suitable ngữ nghĩa (semantic / 의미적) similarity/retrieval.

> **Chuyển mạch:** Ở chặng này của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Sentence-BERT / Contrastive Sentence Embeddings** đã nêu tiêu chí phân biệt, còn **Bi-Encoder vs Cross-Encoder** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Contextual đơn vị từ (token / 토큰) hình học (geometry / 기하학)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bi-Encoder vs Cross-Encoder

**Bi-encoder**:

```text
query → vector ┐
               ├→ similarity
 doc  → vector ┘
```

Fast retrieval, thông tin (information / 정보) compressed into independent vectors.

**Cross-encoder**:

```text
[query ; document]
        ↓ joint Transformer
      relevance score
```

More accurate pairwise tương tác (interaction / 상호작용) but costly.

Hiện đại (modern / 현대적) retrieval often:

```text
bi-encoder retrieve top K
→ cross-encoder rerank
```

This kiến trúc (architecture / 아키텍처) is cốt lõi (core / 핵심) RAG retrieval ngăn xếp (stack / 스택).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Contextual đơn vị từ (token / 토큰) hình học (geometry / 기하학)** tiếp nhận điểm tựa từ **Bi-Encoder vs Cross-Encoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tầng (layer / 계층) Selection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contextual đơn vị từ (token / 토큰) hình học (geometry / 기하학)

A đơn vị từ (token / 토큰)'s hidden trạng thái (state / 상태) encodes mixture of lexical, syntactic, ngữ nghĩa (semantic / 의미적) and positional factors. Layers often show progression but not clean strict hierarchy.

Probing studies can decode linguistic attributes from hidden states, but decodability does not prove nhân quả (causal / 인과적) use.

> **Chuyển mạch:** Trong **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Tầng (layer / 계층) Selection** tiếp nhận điểm tựa từ **Contextual đơn vị từ (token / 토큰) hình học (geometry / 기하학)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pooling and Length độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tầng (layer / 계층) Selection

Last tầng (layer / 계층) optimized closest pretraining đầu ra (output / 출력) mục tiêu (objective / 목표); intermediate layers may be better for some linguistic tasks.

Some methods concatenate/learn weighted mixture across layers.

No universal “last tầng (layer / 계층) always best”.

> **Chuyển mạch:** Ở chặng này của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Pooling and Length độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Tầng (layer / 계층) Selection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pooling and Length độ lệch (bias / 편향)

Mean pooling averages đơn vị từ (token / 토큰) vectors; long docs may dilute salient segments. `[CLS]` depends huấn luyện (training / 학습) mục tiêu (objective / 목표); max pooling favors strongest tính năng (feature / 기능) per dimension.

For long document retrieval, chunk-level embeddings often better than one véc-tơ (vector / 벡터) for entire document.

Chunking introduces segmentation/provenance trade-offs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Normalization** tiếp nhận điểm tựa từ **Pooling and Length độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contrastive huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normalization

Embedding vectors often L2-normalized:

\[
\hat z=\frac{z}{\|z\|}
\]

Then dot sản phẩm (product / 제품) equals cosine similarity:

\[
\hat q^T\hat d=cos(q,d)
\]

ANN indexes may assume one chỉ số (metric / 지표); preprocessing must match mô hình (model / 모델) huấn luyện (training / 학습)/recommendation.

> **Chuyển mạch:** Trong **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Normalization** đã nêu tiêu chí phân biệt, còn **Contrastive huấn luyện (training / 학습)** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Lĩnh vực (domain / 도메인) Adaptation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contrastive huấn luyện (training / 학습)

Positive query-doc pairs should score higher than negatives.

InfoNCE-like mất mát (loss / 손실):

\[
L_i=-\log\frac{e^{s(q_i,d_i^+)/\tau}}
{e^{s(q_i,d_i^+)/\tau}+\sum_j e^{s(q_i,d_j^-)/\tau}}
\]

In-batch negatives provide efficiency, but false negatives (actually relevant docs treated negative) hurt.

Hard negatives improve discrimination near quyết định (decision / 결정) ranh giới (boundary / 경계).

> **Chuyển mạch:** Ở chặng này của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Contrastive huấn luyện (training / 학습)** đã nêu tiêu chí phân biệt, còn **Lĩnh vực (domain / 도메인) Adaptation** dùng tiêu chí đó để soi ranh giới và điểm dễ nhầm. Từ đây, **Multilingual Embeddings** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Lĩnh vực (domain / 도메인) Adaptation

General embedding mô hình (model / 모델) may thất bại (fail / 실패) specialized vocabulary/relations. Fine-tuning on lĩnh vực (domain / 도메인) query-document pairs can improve retrieval.

However overfitting narrow lĩnh vực (domain / 도메인) may reduce general ngữ nghĩa (semantic / 의미적) hành vi (behavior / 동작). Evaluation needs representative queries.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Multilingual Embeddings** tiếp nhận điểm tựa từ **Lĩnh vực (domain / 도메인) Adaptation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ cảnh (context / 맥락) Length** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multilingual Embeddings

Multilingual encoders align sentences from multiple languages in dùng chung (shared / 공유) véc-tơ (vector / 벡터) không gian (space / 공간). Cross-lingual retrieval becomes possible:

```text
Vietnamese query
→ vector
→ retrieve Korean/English document vectors
```

Alignment chất lượng (quality / 품질) varies languages/domains and tokenizer efficiency.

> **Chuyển mạch:** Trong **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Ngữ cảnh (context / 맥락) Length** tiếp nhận điểm tựa từ **Multilingual Embeddings** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Embedding Drift và Versioning** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) Length

Embedding mô hình (model / 모델) max ngữ cảnh (context / 맥락) may truncate long docs. Truncation silently loses tail thông tin (information / 정보).

Môi trường vận hành (production / 운영 환경) chuỗi xử lý (pipeline / 파이프라인) should explicitly:

```text
inspect token count
chunk / summarize / hierarchical encode
track source span
```

> **Chuyển mạch:** Ở chặng này của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Embedding Drift và Versioning** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) Length** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngữ nghĩa (semantic / 의미적) Similarity ≠ Relevance** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Embedding Drift và Versioning

Thay đổi (change / 변경) embedding mô hình (model / 모델)/phiên bản (version / 버전) → hình học (geometry / 기하학) changes. Old corpus vectors should not be mixed with new truy vấn (query / 쿼리) vectors unless backward tính tương thích (compatibility / 호환성) empirically validated.

Re-embedding/re-indexing can be costly; mô hình (model / 모델) phiên bản (version / 버전) must live in vector-store siêu dữ liệu (metadata / 메타데이터).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Ngữ nghĩa (semantic / 의미적) Similarity ≠ Relevance** tiếp nhận điểm tựa từ **Embedding Drift và Versioning** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ nghĩa (semantic / 의미적) Similarity ≠ Relevance

Two texts can be semantically similar but irrelevant to truy vấn (query / 쿼리) intent. Retrieval relevance includes task-specific utility, recency, authority, permissions and siêu dữ liệu (metadata / 메타데이터) các ràng buộc (constraints / 제약조건들).

Dense embedding should combine with lexical tìm kiếm (search / 검색), filters/rerankers when appropriate.

> **Chuyển mạch:** Trong **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Ngữ nghĩa (semantic / 의미적) Similarity ≠ Relevance** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Static embedding asks “symbol này thường liên quan gì?”; contextual embedding asks “symbol/văn bản (text / 텍스트) này trong ngữ cảnh (context / 맥락) hiện tại đang biểu diễn gì?”.

For retrieval, sentence embedding further asks “nén toàn bộ văn bản (text / 텍스트) thành véc-tơ (vector / 벡터) nào để similarity phản ánh relevance mục tiêu (objective / 목표)?”.

> **Chuyển mạch:** Ở chặng này của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “BERT đầu ra (output / 출력) nào cũng dùng làm embedding tìm kiếm (search / 검색) được”

Raw hidden trạng thái (state / 상태)/pooling may not be trained for ngữ nghĩa (semantic / 의미적) similarity. Use retrieval/sentence embedding mục tiêu (objective / 목표).

### “Cross-encoder luôn tốt hơn nên dùng cho toàn corpus”

Pairwise chi phí (cost / 비용) quá cao; typical use rerank small candidate set.

### “Cosine similarity 0.9 nghĩa 90% relevant”

Similarity score không calibrated xác suất (probability / 확률).

### “Multilingual dùng chung (shared / 공유) không gian (space / 공간) means all languages equally good”

Huấn luyện (training / 학습) balance/tokenization/dữ liệu (data / 데이터) chất lượng (quality / 품질) lead uneven hiệu năng (performance / 성능).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Contextual Embeddings: meaning thay đổi theo ngữ cảnh (context / 맥락)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Contextual embeddings combine [Transformer](../06_deep_learning_architectures/05_transformer.md), [Contrastive Representation Learning](../05_neural_networks/08_representation_learning.md) and prepare [Information Retrieval](./08_search_and_information_retrieval.md), RAG and LLM embeddings.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
