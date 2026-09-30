# Sparse Retrieval và Dense Retrieval

> **Mạch đọc:** Đặt **Sparse Retrieval và Dense Retrieval** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Sparse biểu diễn (representation / 표현)** sang **Strength**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Hiện đại (modern / 현대적) retrieval các hệ thống (systems / 시스템들) thường dùng hai families chính: **sparse retrieval** dựa trên term overlap và **dense retrieval** dựa trên learned véc-tơ (vector / 벡터) representations. Hai approaches không phải generation mới thay generation cũ; chúng encode relevance theo hai các giả định (assumptions / 가정들) khác nhau.

## Sparse biểu diễn (representation / 표현)

Trong sparse retrieval, document/truy vấn (query / 쿼리) được biểu diễn trong vocabulary không gian (space / 공간) rất lớn. Hầu hết dimensions bằng 0.

Ví dụ vocabulary:

```text
[refund, cancel, account, ekyc, passport, ...]
```

Một document chỉ activate terms xuất hiện trong nó.

BM25 là sparse retrieval điển hình.

### Strength

Sparse retrieval rất mạnh khi chính xác (exact / 정확한) tokens có ý nghĩa cao:

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

Nếu không share terms, lexical score thấp dù ngữ nghĩa (semantic / 의미적) quan hệ (relation / 관계) cao.

## Dense biểu diễn (representation / 표현)

Dense retriever dùng encoder để map truy vấn (query / 쿼리)/document vào véc-tơ (vector / 벡터):

\[
q=f_q(text),\quad d=f_d(text)
\]

Similarity:

\[
s(q,d)=q^T d
\]

hoặc cosine similarity.

Mô hình (model / 모델) được train sao cho relevant pairs gần nhau hơn non-relevant pairs.

## Bi-Encoder

Truy vấn (query / 쿼리) và document encode độc lập:

```text
query → encoder → q vector
doc   → encoder → d vector
```

Document vectors precompute được, nên retrieval nhanh bằng véc-tơ (vector / 벡터) chỉ mục (index / 인덱스).

Đây là kiến trúc (architecture / 아키텍처) phổ biến của dense first-stage retrieval.

## Contrastive huấn luyện (training / 학습)

Dense retriever thường train với positive pair `(q,d+)` và negatives `d-`.

Mục tiêu (objective / 목표) kiểu softmax:

\[
P(d^+\mid q)=\frac{e^{s(q,d^+)}}{\sum_j e^{s(q,d_j)}}
\]

Mô hình (model / 모델) học hình học (geometry / 기하학) nơi relevant document có score cao.

## Negative Sampling

Negatives quyết định retriever học gì.

Random negatives quá dễ: document hoàn toàn khác topic. Hard negatives như lexical-similar nhưng wrong answer buộc mô hình (model / 모델) học distinctions fine-grained.

Nếu negative set chứa false negatives — documents thực ra relevant — huấn luyện (training / 학습) tín hiệu (signal / 신호) bị noisy.

## Cross-Encoder

Cross-encoder đưa truy vấn (query / 쿼리) và document vào cùng mô hình (model / 모델):

```text
[query ; document] → Transformer → relevance score
```

Nó cho phép token-level tương tác (interaction / 상호작용) sâu nên accuracy cao hơn bi-encoder, nhưng không thể precompute document biểu diễn (representation / 표현) độc lập. chi phí (cost / 비용) quá cao để score hàng triệu docs.

Vì vậy cross-encoder thường dùng reranker sau candidate retrieval.

## Late tương tác (interaction / 상호작용)

Các architectures như late tương tác (interaction / 상호작용) giữ multiple đơn vị từ (token / 토큰) vectors cho document/truy vấn (query / 쿼리) rồi compute finer tương tác (interaction / 상호작용) mà vẫn pre-index được phần document.

Nó nằm giữa bi-encoder và cross-encoder về chi phí (cost / 비용)/chất lượng (quality / 품질).

## Hybrid Retrieval

Hybrid kết hợp sparse và dense:

\[
score=\alpha score_{dense}+(1-\alpha)score_{sparse}
\]

Hoặc merge rankings bằng reciprocal rank fusion.

Hybrid thường robust trong enterprise corpora vì ngữ nghĩa (semantic / 의미적) queries và chính xác (exact / 정확한) identifiers coexist.

## Reciprocal Rank Fusion

Nếu hai retrievers có score scales khác nhau, direct weighted sum khó. RRF combine rank positions:

\[
RRF(d)=\sum_r \frac{1}{k+rank_r(d)}
\]

Nó không cần calibrate raw scores giữa retrievers.

## Ngữ nghĩa (semantic / 의미적) Drift

Dense retriever có thể trả document semantically related nhưng answer-specific detail sai.

Ví dụ truy vấn (query / 쿼리) hỏi `refund within 7 days`, retriever đưa chính sách (policy / 정책) `refund within 30 days` vì topic rất giống.

Reranking/siêu dữ liệu (metadata / 메타데이터)/thời gian (time / 시간) filters cần xử lý fine distinction.

## Exact-match Blind Spot

Embedding mô hình (model / 모델) có thể smooth rare strings. lỗi (error / 오류) mã (code / 코드) `E1012` và `E1013` có thể nằm gần nhau dù khác meaning operationally.

Sparse retrieval nên giữ chính xác (exact / 정확한) đơn vị từ (token / 토큰) tín hiệu (signal / 신호).

## Multilingual Retrieval

Multilingual embedding mô hình (model / 모델) có thể map Korean/English/Vietnamese ngữ nghĩa (semantic / 의미적) equivalents gần nhau. Điều này rất hữu ích cho cross-language kiến thức (knowledge / 지식) cơ sở (base / 기반).

Nhưng chất lượng (quality / 품질) không uniform giữa languages. Enterprise eval cần kiểm thử (test / 테스트) ngôn ngữ (language / 언어) pairs thật.

## Lĩnh vực (domain / 도메인) Adaptation

General embedding mô hình (model / 모델) có thể không hiểu nội bộ (internal / 내부) abbreviations. Fine-tuning retriever hoặc augment huấn luyện (training / 학습) pairs từ lĩnh vực (domain / 도메인) queries cải thiện hình học (geometry / 기하학).

Siêu dữ liệu (metadata / 메타데이터)/lexical aliases cũng là solution simpler hơn trong nhiều cases.

## Truy vấn (query / 쿼리) vs Document Encoder

Có thể share weights hoặc dùng asymmetric encoders. truy vấn (query / 쿼리) thường ngắn, document dài; asymmetric huấn luyện (training / 학습) có thể optimize roles khác nhau.

## Candidate Count

Retrieve top `k` quá nhỏ → miss bằng chứng (evidence / 증거).

Top `k` quá lớn → reranker/generator overload.

Chọn `k` dựa retrieval recall curve và downstream ngân sách (budget / 예산), không arbitrary.

## Sparse Learned Retrieval

Có methods học sparse term weights bằng neural mô hình (model / 모델), giữ inverted-index efficiency nhưng ngữ nghĩa (semantic / 의미적) expansion tốt hơn classic BM25.

Conceptual điểm (point / 지점): sparse/dense không hoàn toàn đồng nghĩa classical/neural.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Sparse → "có cùng words/identifiers không?"
Dense  → "có cùng meaning pattern không?"
Hybrid → "dùng cả lexical evidence và semantic geometry"
```

## Dùng chung (common / 공통) Misconceptions

### “Dense luôn tốt hơn BM25”

Không, especially chính xác (exact / 정확한) technical corpora.

### “Cosine similarity có thể compare trực tiếp giữa mọi embedding các mô hình (models / 모델들)”

Không. Score phân phối (distribution / 분포) depends mô hình (model / 모델)/huấn luyện (training / 학습)/normalization.

### “Hybrid chỉ cần cộng 2 scores”

Raw score scales có thể incompatible; normalization/RRF cần xem xét.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Dense retrieval dựa trực tiếp vào [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md). Sparse retrieval dựa inverted chỉ mục (index / 인덱스)/IR. RAG tốt thường dùng multiple retrieval signals.

Xem tiếp: [Embeddings for Retrieval](./02_embeddings_for_retrieval.md).
