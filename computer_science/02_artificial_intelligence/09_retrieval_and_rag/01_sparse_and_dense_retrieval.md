# Sparse Retrieval và Dense Retrieval

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Sparse retrieval và dense retrieval**. Route đi từ lexical terms → sparse vectors/BM25 → dense embeddings → hybrid retrieval → recall/latency trade-offs, để chọn representation theo query và corpus thay vì theo nhãn mô hình.

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

Sparse retrieval giữ được tín hiệu term và identifier rõ ràng, còn dense retrieval cố nối những câu khác từ bằng hình học biểu diễn.

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

Dense vectors cho phép tìm theo ngữ nghĩa, nhưng để truy hồi nhanh cần encoder xử lý query và document một cách phù hợp; bi-encoder tách hai lần encode.

## Bi-Encoder

Truy vấn (query / 쿼리) và document encode độc lập:

```text
query → encoder → q vector
doc   → encoder → d vector
```

Document vectors precompute được, nên retrieval nhanh bằng véc-tơ (vector / 벡터) chỉ mục (index / 인덱스).

Đây là kiến trúc (architecture / 아키텍처) phổ biến của dense first-stage retrieval.

Bi-encoder precompute document vectors nên phù hợp first-stage retrieval; contrastive training quyết định hình học nào được học từ positive và negative pairs.

## Contrastive huấn luyện (training / 학습)

Dense retriever thường train với positive pair `(q,d+)` và negatives `d-`.

Mục tiêu (objective / 목표) kiểu softmax:

\[
P(d^+\mid q)=\frac{e^{s(q,d^+)}}{\sum_j e^{s(q,d_j)}}
\]

Mô hình (model / 모델) học hình học (geometry / 기하학) nơi relevant document có score cao.

Contrastive objective chỉ hiệu quả khi negative phản ánh lỗi retrieval thực tế; negative sampling vì thế quyết định model học distinction nào.

## Negative Sampling

Negatives quyết định retriever học gì.

Random negatives quá dễ: document hoàn toàn khác topic. Hard negatives như lexical-similar nhưng wrong answer buộc mô hình (model / 모델) học distinctions fine-grained.

Nếu negative set chứa false negatives — documents thực ra relevant — huấn luyện (training / 학습) tín hiệu (signal / 신호) bị noisy.

Negative set tạo áp lực học fine-grained, còn cross-encoder đánh giá từng cặp query–document với tương tác token sâu hơn.

## Cross-Encoder

Cross-encoder đưa truy vấn (query / 쿼리) và document vào cùng mô hình (model / 모델):

```text
[query ; document] → Transformer → relevance score
```

Nó cho phép token-level tương tác (interaction / 상호작용) sâu nên accuracy cao hơn bi-encoder, nhưng không thể precompute document biểu diễn (representation / 표현) độc lập. chi phí (cost / 비용) quá cao để score hàng triệu docs.

Vì vậy cross-encoder thường dùng reranker sau candidate retrieval.

Cross-encoder thường chính xác nhưng đắt khi chấm hàng triệu tài liệu; late interaction giữ thêm thông tin token mà vẫn pre-index được phần document.

## Late tương tác (interaction / 상호작용)

Các architectures như late tương tác (interaction / 상호작용) giữ multiple đơn vị từ (token / 토큰) vectors cho document/truy vấn (query / 쿼리) rồi compute finer tương tác (interaction / 상호작용) mà vẫn pre-index được phần document.

Nó nằm giữa bi-encoder và cross-encoder về chi phí (cost / 비용)/chất lượng (quality / 품질).

Late interaction đứng giữa tốc độ của bi-encoder và độ sâu của cross-encoder; hybrid retrieval lại kết hợp cả tín hiệu dense lẫn sparse.

## Hybrid Retrieval

Hybrid kết hợp sparse và dense:

\[
score=\alpha score_{dense}+(1-\alpha)score_{sparse}
\]

Hoặc merge rankings bằng reciprocal rank fusion.

Hybrid thường robust trong enterprise corpora vì ngữ nghĩa (semantic / 의미적) queries và chính xác (exact / 정확한) identifiers coexist.

Hybrid cần đưa hai nguồn tín hiệu về cách kết hợp ổn định; reciprocal rank fusion dùng vị trí trong ranking để tránh phụ thuộc raw score scales.

## Reciprocal Rank Fusion

Nếu hai retrievers có score scales khác nhau, direct weighted sum khó. RRF combine rank positions:

\[
RRF(d)=\sum_r \frac{1}{k+rank_r(d)}
\]

Nó không cần calibrate raw scores giữa retrievers.

RRF không cần calibrate điểm thô, nhưng dense và sparse vẫn có thể lệch về loại lỗi; semantic drift là trường hợp dense gần về chủ đề nhưng sai chi tiết.

## Ngữ nghĩa (semantic / 의미적) Drift

Dense retriever có thể trả document semantically related nhưng answer-specific detail sai.

Ví dụ truy vấn (query / 쿼리) hỏi `refund within 7 days`, retriever đưa chính sách (policy / 정책) `refund within 30 days` vì topic rất giống.

Reranking/siêu dữ liệu (metadata / 메타데이터)/thời gian (time / 시간) filters cần xử lý fine distinction.

Semantic similarity có thể bỏ qua identifier và con số quan trọng; exact-match signal cần được giữ lại, đặc biệt trong corpus kỹ thuật.

## Exact-match Blind Spot

Embedding mô hình (model / 모델) có thể smooth rare strings. lỗi (error / 오류) mã (code / 코드) `E1012` và `E1013` có thể nằm gần nhau dù khác meaning operationally.

Sparse retrieval nên giữ chính xác (exact / 정확한) đơn vị từ (token / 토큰) tín hiệu (signal / 신호).

Exact-match bảo vệ token hiếm, còn multilingual retrieval mở rộng khả năng nối cùng intent giữa các ngôn ngữ; cả hai đều cần evaluation theo ngữ cảnh sử dụng.

## Multilingual Retrieval

Multilingual embedding mô hình (model / 모델) có thể map Korean/English/Vietnamese ngữ nghĩa (semantic / 의미적) equivalents gần nhau. Điều này rất hữu ích cho cross-language kiến thức (knowledge / 지식) cơ sở (base / 기반).

Nhưng chất lượng (quality / 품질) không uniform giữa languages. Enterprise eval cần kiểm thử (test / 테스트) ngôn ngữ (language / 언어) pairs thật.

Cross-language quality không đồng đều, nên domain adaptation cần xem xét thuật ngữ nội bộ và dữ liệu truy vấn của từng lĩnh vực.

## Lĩnh vực (domain / 도메인) Adaptation

General embedding mô hình (model / 모델) có thể không hiểu nội bộ (internal / 내부) abbreviations. Fine-tuning retriever hoặc augment huấn luyện (training / 학습) pairs từ lĩnh vực (domain / 도메인) queries cải thiện hình học (geometry / 기하학).

Siêu dữ liệu (metadata / 메타데이터)/lexical aliases cũng là solution simpler hơn trong nhiều cases.

Domain adaptation cải thiện encoder bằng dữ liệu đặc thù, nhưng query và document có thể cần vai trò hoặc phân phối khác nhau; đó là lý do chọn encoder đối xứng hay bất đối xứng.

## Truy vấn (query / 쿼리) vs Document Encoder

Có thể share weights hoặc dùng asymmetric encoders. truy vấn (query / 쿼리) thường ngắn, document dài; asymmetric huấn luyện (training / 학습) có thể optimize roles khác nhau.

Khi vai trò encoder đã rõ, số lượng candidate trở thành ngân sách trực tiếp cho recall và chi phí reranking.

## Candidate Count

Retrieve top `k` quá nhỏ → miss bằng chứng (evidence / 증거).

Top `k` quá lớn → reranker/generator overload.

Chọn `k` dựa retrieval recall curve và downstream ngân sách (budget / 예산), không arbitrary.

Candidate count phải đủ lớn để không bỏ sót bằng chứng, nhưng quá lớn sẽ làm downstream quá tải; sparse learned retrieval là một điểm cân bằng khác giữa mở rộng ngữ nghĩa và hiệu quả index.

## Sparse Learned Retrieval

Có methods học sparse term weights bằng neural mô hình (model / 모델), giữ inverted-index efficiency nhưng ngữ nghĩa (semantic / 의미적) expansion tốt hơn classic BM25.

Conceptual điểm (point / 지점): sparse/dense không hoàn toàn đồng nghĩa classical/neural.

Sparse learned retrieval cho thấy sparse/dense không đồng nhất với classical/neural; mô hình tư duy dưới đây tóm tắt cách chọn representation theo corpus và query.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Sparse → "có cùng words/identifiers không?"
Dense  → "có cùng meaning pattern không?"
Hybrid → "dùng cả lexical evidence và semantic geometry"
```

Mô hình tư duy đặt sparse, dense và hybrid cạnh nhau theo loại tín hiệu chúng sử dụng; các ngộ nhận sau đây giúp kiểm tra những ranh giới đó.

## Dùng chung (common / 공통) Misconceptions

### “Dense luôn tốt hơn BM25”

Không, especially chính xác (exact / 정확한) technical corpora.

### “Cosine similarity có thể compare trực tiếp giữa mọi embedding các mô hình (models / 모델들)”

Không. Score phân phối (distribution / 분포) depends mô hình (model / 모델)/huấn luyện (training / 학습)/normalization.

### “Hybrid chỉ cần cộng 2 scores”

Raw score scales có thể incompatible; normalization/RRF cần xem xét.

Các ngộ nhận về dense, cosine và hybrid thường bỏ qua calibration, exact-match và score scale; phần liên kết kiến thức nối các lựa chọn này với embeddings và RAG.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Dense retrieval dựa trực tiếp vào [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md). Sparse retrieval dựa inverted chỉ mục (index / 인덱스)/IR. RAG tốt thường dùng multiple retrieval signals.

Xem tiếp: [Embeddings for Retrieval](./02_embeddings_for_retrieval.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
