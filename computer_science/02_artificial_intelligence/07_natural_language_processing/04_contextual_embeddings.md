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

Biểu diễn tĩnh chỉ có một véc-tơ cho mỗi kiểu từ, còn contextual embedding cần một trạng thái phụ thuộc cả câu. ELMo thực hiện điều đó bằng mô hình ngôn ngữ hai chiều; BERT mở rộng ý tưởng với kiến trúc Transformer.

## ELMo: contextualization bằng bidirectional LM

ELMo là milestone trước Transformer. Nó dùng stacked bidirectional LSTMs; biểu diễn (representation / 표현) kết hợp hidden states từ multiple layers.

Insight: different layers capture different linguistic thông tin (information / 정보), and context-sensitive đơn vị từ (token / 토큰) biểu diễn (representation / 표현) improves downstream tasks.

ELMo và BERT đều tạo trạng thái theo ngữ cảnh, nhưng BERT biểu diễn từng token qua các tầng Transformer. Muốn dùng các trạng thái ấy cho truy hồi hoặc phân loại câu, cần phân biệt token representation với sentence representation.

## BERT representations

BERT uses bidirectional Transformer encoder trained with masked-language-model mục tiêu (objective / 목표).

Đầu vào (input / 입력) biểu diễn (representation / 표현) combines đơn vị từ (token / 토큰)/subword + position + segment/kiểu (type / 타입) embeddings (implementation-specific).

After each Transformer tầng (layer / 계층), đơn vị từ (token / 토큰) véc-tơ (vector / 벡터) becomes contextualized.

Final/selected layers feed classification, QA, NER etc.

Một ma trận trạng thái theo token chưa phải một véc-tơ câu tốt. Sentence-BERT dùng pooling và mục tiêu tương phản để biến các câu thành biểu diễn có thể so sánh trực tiếp.

## Đơn vị từ (token / 토큰) biểu diễn (representation / 표현) vs Sentence biểu diễn (representation / 표현)

Token-level tasks use per-token hidden states.

Sentence/document tasks need pooling:

- `[CLS]` biểu diễn (representation / 표현);
- mean pooling;
- max pooling;
- attention pooling;
- dedicated sentence-embedding fine-tuning.

Raw BERT `[CLS]` is not automatically ideal ngữ nghĩa (semantic / 의미적) sentence embedding. mục tiêu (objective / 목표) matters.

Contrastive learning làm cho sentence embedding phù hợp với similarity và retrieval, nhưng cách tính điểm vẫn là một lựa chọn kiến trúc. Bi-encoder và cross-encoder minh họa rõ đánh đổi giữa tốc độ truy hồi và khả năng tương tác sâu giữa hai câu.

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

Bi-encoder mã hóa độc lập nên nhanh và có thể lập chỉ mục; cross-encoder đọc cặp đầu vào cùng lúc nên thường chính xác hơn nhưng đắt hơn. Cả hai đều dựa trên hình học của các trạng thái contextual, vì vậy phần tiếp theo xem hình học đó nên được hiểu ra sao.

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

Khoảng cách giữa các trạng thái contextual phụ thuộc vị trí trong mạng và mục tiêu đã huấn luyện; khả năng giải mã một thuộc tính không chứng minh mô hình dùng nó theo cách nhân quả. Vì vậy, chọn tầng cần gắn với tác vụ và đánh giá thực nghiệm.

## Contextual đơn vị từ (token / 토큰) hình học (geometry / 기하학)

A đơn vị từ (token / 토큰)'s hidden trạng thái (state / 상태) encodes mixture of lexical, syntactic, ngữ nghĩa (semantic / 의미적) and positional factors. Layers often show progression but not clean strict hierarchy.

Probing studies can decode linguistic attributes from hidden states, but decodability does not prove nhân quả (causal / 인과적) use.

Các tầng giữa và cuối có thể hữu ích cho những thông tin khác nhau, nên “tầng cuối luôn tốt nhất” là một quy tắc thiếu căn cứ. Sau khi chọn tầng, bước pooling còn quyết định cách độ dài câu ảnh hưởng đến véc-tơ.

## Tầng (layer / 계층) Selection

Last tầng (layer / 계층) optimized closest pretraining đầu ra (output / 출력) mục tiêu (objective / 목표); intermediate layers may be better for some linguistic tasks.

Some methods concatenate/learn weighted mixture across layers.

No universal “last tầng (layer / 계층) always best”.

Mean pooling, attention pooling và các chiến lược theo đoạn tạo ra các phân bố độ dài khác nhau. Normalization là bước tiếp theo để kiểm soát ảnh hưởng về độ lớn trước khi so sánh hoặc lập chỉ mục.

## Pooling and Length độ lệch (bias / 편향)

Mean pooling averages đơn vị từ (token / 토큰) vectors; long docs may dilute salient segments. `[CLS]` depends huấn luyện (training / 학습) mục tiêu (objective / 목표); max pooling favors strongest tính năng (feature / 기능) per dimension.

For long document retrieval, chunk-level embeddings often better than one véc-tơ (vector / 벡터) for entire document.

Chunking introduces segmentation/provenance trade-offs.

Normalization không thể sửa một biểu diễn đã học sai mục tiêu; nó chỉ thay đổi cách các véc-tơ được so sánh. Muốn hình học phản ánh quan hệ cần dùng, contrastive training phải cung cấp cặp dương, cặp âm và tín hiệu đánh giá phù hợp.

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

Contrastive objective kéo các cặp được xem là tương tự lại gần và đẩy các cặp âm ra xa; hard negative giúp kiểm tra ranh giới khó. Khi dữ liệu huấn luyện thay đổi theo lĩnh vực, cần đánh giá nguy cơ chuyên biệt hóa quá mức.

## Contrastive huấn luyện (training / 학습)

Positive query-doc pairs should score higher than negatives.

InfoNCE-like mất mát (loss / 손실):

\[
L_i=-\log\frac{e^{s(q_i,d_i^+)/\tau}}
{e^{s(q_i,d_i^+)/\tau}+\sum_j e^{s(q_i,d_j^-)/\tau}}
\]

In-batch negatives provide efficiency, but false negatives (actually relevant docs treated negative) hurt.

Hard negatives improve discrimination near quyết định (decision / 결정) ranh giới (boundary / 경계).

Domain adaptation có thể tăng recall trong một lĩnh vực nhưng làm giảm khả năng khái quát. Khi mở rộng sang nhiều ngôn ngữ, sự khác biệt tokenizer, dữ liệu và mức độ căn chỉnh tạo thêm một lớp đánh đổi.

## Lĩnh vực (domain / 도메인) Adaptation

General embedding mô hình (model / 모델) may thất bại (fail / 실패) specialized vocabulary/relations. Fine-tuning on lĩnh vực (domain / 도메인) query-document pairs can improve retrieval.

However overfitting narrow lĩnh vực (domain / 도메인) may reduce general ngữ nghĩa (semantic / 의미적) hành vi (behavior / 동작). Evaluation needs representative queries.

Multilingual embedding có thể chia sẻ không gian giữa các ngôn ngữ, nhưng chất lượng không đồng đều và không bảo đảm chuyển giao cho mọi cặp ngôn ngữ. Giới hạn độ dài ngữ cảnh tiếp tục quyết định phần thông tin nào còn hiện diện khi mã hóa.

## Multilingual Embeddings

Multilingual encoders align sentences from multiple languages in dùng chung (shared / 공유) véc-tơ (vector / 벡터) không gian (space / 공간). Cross-lingual retrieval becomes possible:

```text
Vietnamese query
→ vector
→ retrieve Korean/English document vectors
```

Alignment chất lượng (quality / 품질) varies languages/domains and tokenizer efficiency.

Context window dài hơn không tự động tạo hiểu biết tốt hơn: cắt đoạn có thể làm mất liên kết, còn giữ toàn bộ văn bản làm tăng chi phí. Khi mô hình hoặc cách cắt thay đổi, index đã tạo cũng có thể không còn tương thích.

## Ngữ cảnh (context / 맥락) Length

Embedding mô hình (model / 모델) max ngữ cảnh (context / 맥락) may truncate long docs. Truncation silently loses tail thông tin (information / 정보).

Môi trường vận hành (production / 운영 환경) chuỗi xử lý (pipeline / 파이프라인) should explicitly:

```text
inspect token count
chunk / summarize / hierarchical encode
track source span
```

Embedding drift là lý do cần lưu phiên bản mô hình, tokenizer, preprocessing và thời điểm lập index. Ngay cả khi véc-tơ ổn định, similarity vẫn chỉ là tín hiệu ngữ nghĩa; relevance còn phụ thuộc nhu cầu truy vấn và ràng buộc nghiệp vụ.

## Embedding Drift và Versioning

Thay đổi (change / 변경) embedding mô hình (model / 모델)/phiên bản (version / 버전) → hình học (geometry / 기하학) changes. Old corpus vectors should not be mixed with new truy vấn (query / 쿼리) vectors unless backward tính tương thích (compatibility / 호환성) empirically validated.

Re-embedding/re-indexing can be costly; mô hình (model / 모델) phiên bản (version / 버전) must live in vector-store siêu dữ liệu (metadata / 메타데이터).

Similarity đo gần nhau trong không gian biểu diễn, còn relevance là phán đoán theo nhiệm vụ. Vì thế hệ thống truy hồi thường kết hợp dense embedding với lexical search, bộ lọc hoặc reranker. Mô hình tư duy sau đây tóm tắt chuỗi quyết định đó.

## Ngữ nghĩa (semantic / 의미적) Similarity ≠ Relevance

Two texts can be semantically similar but irrelevant to truy vấn (query / 쿼리) intent. Retrieval relevance includes task-specific utility, recency, authority, permissions and siêu dữ liệu (metadata / 메타데이터) các ràng buộc (constraints / 제약조건들).

Dense embedding should combine with lexical tìm kiếm (search / 검색), filters/rerankers when appropriate.

Mô hình tư duy nối từ trạng thái theo ngữ cảnh đến pooling, similarity và đánh giá theo nhiệm vụ. Các ngộ nhận cuối bài kiểm tra những điểm thường bị bỏ qua trong chuỗi này.

## Mô hình tư duy (mental model / 사고 모델)

> Static embedding asks “symbol này thường liên quan gì?”; contextual embedding asks “symbol/văn bản (text / 텍스트) này trong ngữ cảnh (context / 맥락) hiện tại đang biểu diễn gì?”.

For retrieval, sentence embedding further asks “nén toàn bộ văn bản (text / 텍스트) thành véc-tơ (vector / 벡터) nào để similarity phản ánh relevance mục tiêu (objective / 목표)?”.

Các ngộ nhận cho thấy contextual không đồng nghĩa với “hiểu đúng” và similarity không đồng nghĩa với relevance. Liên kết kiến thức cuối bài chỉ ra nơi quay lại để kiểm tra từng giả định.

## Dùng chung (common / 공통) Misconceptions

### “BERT đầu ra (output / 출력) nào cũng dùng làm embedding tìm kiếm (search / 검색) được”

Raw hidden trạng thái (state / 상태)/pooling may not be trained for ngữ nghĩa (semantic / 의미적) similarity. Use retrieval/sentence embedding mục tiêu (objective / 목표).

### “Cross-encoder luôn tốt hơn nên dùng cho toàn corpus”

Pairwise chi phí (cost / 비용) quá cao; typical use rerank small candidate set.

### “Cosine similarity 0.9 nghĩa 90% relevant”

Similarity score không calibrated xác suất (probability / 확률).

### “Multilingual dùng chung (shared / 공유) không gian (space / 공간) means all languages equally good”

Huấn luyện (training / 학습) balance/tokenization/dữ liệu (data / 데이터) chất lượng (quality / 품질) lead uneven hiệu năng (performance / 성능).

Các liên kết dưới đây nối contextual embeddings với các bài về biểu diễn, retrieval và sequence models; hãy dùng chúng để chọn nhánh học tiếp theo thay vì xem một phép đo đơn lẻ là kết luận cuối cùng.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Contextual embeddings combine [Transformer](../06_deep_learning_architectures/05_transformer.md), [Contrastive Representation Learning](../05_neural_networks/08_representation_learning.md) and prepare [Information Retrieval](./08_search_and_information_retrieval.md), RAG and LLM embeddings.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
