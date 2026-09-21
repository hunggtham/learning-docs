# Sparse Retrieval và Dense Retrieval

Modern retrieval systems thường dùng hai families chính: **sparse retrieval** dựa trên term overlap và **dense retrieval** dựa trên learned vector representations. Hai approaches không phải generation mới thay generation cũ; chúng encode relevance theo hai assumptions khác nhau.

## Sparse Representation

Trong sparse retrieval, document/query được biểu diễn trong vocabulary space rất lớn. Hầu hết dimensions bằng 0.

Ví dụ vocabulary:

```text
[refund, cancel, account, ekyc, passport, ...]
```

Một document chỉ activate terms xuất hiện trong nó.

BM25 là sparse retrieval điển hình.

### Strength

Sparse retrieval rất mạnh khi exact tokens có ý nghĩa cao:

```text
error code EKYC_4021
product ID
legal article number
rare technical term
person/company name
```

Nó transparent hơn: ta biết term nào match.

### Weakness

Vocabulary mismatch:

```text
query: "người dùng không đăng nhập được"
doc: "authentication failure"
```

Nếu không share terms, lexical score thấp dù semantic relation cao.

## Dense Representation

Dense retriever dùng encoder để map query/document vào vector:

\[
q=f_q(text),\quad d=f_d(text)
\]

Similarity:

\[
s(q,d)=q^T d
\]

hoặc cosine similarity.

Model được train sao cho relevant pairs gần nhau hơn non-relevant pairs.

## Bi-Encoder

Query và document encode độc lập:

```text
query → encoder → q vector
doc   → encoder → d vector
```

Document vectors precompute được, nên retrieval nhanh bằng vector index.

Đây là architecture phổ biến của dense first-stage retrieval.

## Contrastive Training

Dense retriever thường train với positive pair `(q,d+)` và negatives `d-`.

Objective kiểu softmax:

\[
P(d^+\mid q)=\frac{e^{s(q,d^+)}}{\sum_j e^{s(q,d_j)}}
\]

Model học geometry nơi relevant document có score cao.

## Negative Sampling

Negatives quyết định retriever học gì.

Random negatives quá dễ: document hoàn toàn khác topic. Hard negatives như lexical-similar nhưng wrong answer buộc model học distinctions fine-grained.

Nếu negative set chứa false negatives — documents thực ra relevant — training signal bị noisy.

## Cross-Encoder

Cross-encoder đưa query và document vào cùng model:

```text
[query ; document] → Transformer → relevance score
```

Nó cho phép token-level interaction sâu nên accuracy cao hơn bi-encoder, nhưng không thể precompute document representation độc lập. Cost quá cao để score hàng triệu docs.

Vì vậy cross-encoder thường dùng reranker sau candidate retrieval.

## Late Interaction

Các architectures như late interaction giữ multiple token vectors cho document/query rồi compute finer interaction mà vẫn pre-index được phần document.

Nó nằm giữa bi-encoder và cross-encoder về cost/quality.

## Hybrid Retrieval

Hybrid kết hợp sparse và dense:

\[
score=\alpha score_{dense}+(1-\alpha)score_{sparse}
\]

Hoặc merge rankings bằng reciprocal rank fusion.

Hybrid thường robust trong enterprise corpora vì semantic queries và exact identifiers coexist.

## Reciprocal Rank Fusion

Nếu hai retrievers có score scales khác nhau, direct weighted sum khó. RRF combine rank positions:

\[
RRF(d)=\sum_r \frac{1}{k+rank_r(d)}
\]

Nó không cần calibrate raw scores giữa retrievers.

## Semantic Drift

Dense retriever có thể trả document semantically related nhưng answer-specific detail sai.

Ví dụ query hỏi `refund within 7 days`, retriever đưa policy `refund within 30 days` vì topic rất giống.

Reranking/metadata/time filters cần xử lý fine distinction.

## Exact-match Blind Spot

Embedding model có thể smooth rare strings. Error code `E1012` và `E1013` có thể nằm gần nhau dù khác meaning operationally.

Sparse retrieval nên giữ exact token signal.

## Multilingual Retrieval

Multilingual embedding model có thể map Korean/English/Vietnamese semantic equivalents gần nhau. Điều này rất hữu ích cho cross-language knowledge base.

Nhưng quality không uniform giữa languages. Enterprise eval cần test language pairs thật.

## Domain Adaptation

General embedding model có thể không hiểu internal abbreviations. Fine-tuning retriever hoặc augment training pairs từ domain queries cải thiện geometry.

Metadata/lexical aliases cũng là solution simpler hơn trong nhiều cases.

## Query vs Document Encoder

Có thể share weights hoặc dùng asymmetric encoders. Query thường ngắn, document dài; asymmetric training có thể optimize roles khác nhau.

## Candidate Count

Retrieve top `k` quá nhỏ → miss evidence.

Top `k` quá lớn → reranker/generator overload.

Chọn `k` dựa retrieval recall curve và downstream budget, không arbitrary.

## Sparse Learned Retrieval

Có methods học sparse term weights bằng neural model, giữ inverted-index efficiency nhưng semantic expansion tốt hơn classic BM25.

Conceptual point: sparse/dense không hoàn toàn đồng nghĩa classical/neural.

## Mental Model

```text
Sparse → "có cùng words/identifiers không?"
Dense  → "có cùng meaning pattern không?"
Hybrid → "dùng cả lexical evidence và semantic geometry"
```

## Common Misconceptions

### “Dense luôn tốt hơn BM25”

Không, especially exact technical corpora.

### “Cosine similarity có thể compare trực tiếp giữa mọi embedding models”

Không. Score distribution depends model/training/normalization.

### “Hybrid chỉ cần cộng 2 scores”

Raw score scales có thể incompatible; normalization/RRF cần xem xét.

## Knowledge Connection

Dense retrieval dựa trực tiếp vào [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md). Sparse retrieval dựa inverted index/IR. RAG tốt thường dùng multiple retrieval signals.

Xem tiếp: [Embeddings for Retrieval](./02_embeddings_for_retrieval.md).