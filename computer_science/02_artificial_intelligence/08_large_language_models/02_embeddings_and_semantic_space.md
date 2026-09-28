# Embeddings và ngữ nghĩa (semantic / 의미적) không gian (space / 공간) trong LLM các hệ thống (systems / 시스템들)

> **Mạch đọc:** Đặt **Embeddings và ngữ nghĩa (semantic / 의미적) không gian (space / 공간) trong LLM các hệ thống (systems / 시스템들)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **đầu vào (input / 입력) đơn vị từ (token / 토큰) Embedding** sang **Contextual Hidden trạng thái (state / 상태)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


“Embedding” trong LLM ngữ cảnh (context / 맥락) có ít nhất ba meanings cần tách: **đầu vào (input / 입력) đơn vị từ (token / 토큰) embedding**, **nội bộ (internal / 내부) contextual hidden states**, và **bên ngoài (external / 외부) embedding mô hình (model / 모델) đầu ra (output / 출력) dùng cho retrieval/similarity**. Chúng đều là vectors nhưng mục tiêu (objective / 목표)/use khác nhau.

Nếu trộn ba loại, dễ nghĩ véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) đang lưu “LLM thoughts” hoặc đơn vị từ (token / 토큰) embedding là ngữ nghĩa (semantic / 의미적) sentence embedding. Không đúng.

## Đầu vào (input / 입력) đơn vị từ (token / 토큰) Embedding

Tokenizer ID maps row:

\[
x_t=E[token_t]
\]

`E∈R^{V×d_model}` trained jointly with ngôn ngữ (language / 언어) mô hình (model / 모델).

This véc-tơ (vector / 벡터) is context-independent initial biểu diễn (representation / 표현). Contextualization happens through Transformer layers.

## Contextual Hidden trạng thái (state / 상태)

After tầng (layer / 계층) `l`:

\[
h_t^{(l)}=TransformerLayer_l(...)
\]

depends other allowed tokens. Same đơn vị từ (token / 토큰) has different hidden trạng thái (state / 상태) based ngữ cảnh (context / 맥락).

Nội bộ (internal / 내부) hidden states optimized for next-token mục tiêu (objective / 목표), not necessarily cosine sentence tìm kiếm (search / 검색).

## Đầu ra (output / 출력) / Unembedding

Final hidden trạng thái (state / 상태) maps to vocabulary logits:

\[
z=W_Uh_t
\]

Often `W_U=E^T` through weight tying, but not universal.

Dot sản phẩm (product / 제품) hidden trạng thái (state / 상태) with đơn vị từ (token / 토큰) đầu ra (output / 출력) vectors yields đơn vị từ (token / 토큰) tính tương thích (compatibility / 호환성) logits.

This creates interesting geometric quan hệ (relation / 관계) between hidden không gian (space / 공간) and vocabulary, but softmax hành vi (behavior / 동작) is contextual/composed through layers.

## Bên ngoài (external / 외부) Embedding mô hình (model / 모델)

Retrieval mô hình (model / 모델) maps whole truy vấn (query / 쿼리)/document/chunk:

\[
f(text)\rightarrow z\in R^d
\]

trained with contrastive/retrieval mục tiêu (objective / 목표) so véc-tơ (vector / 벡터) similarity corresponds relevance/ngữ nghĩa (semantic / 의미적) quan hệ (relation / 관계).

A chat LLM's last hidden trạng thái (state / 상태) is not automatically good retrieval embedding. Dedicated embedding mô hình (model / 모델) usually better/cheaper.

## Ngữ nghĩa (semantic / 의미적) không gian (space / 공간) không phải dictionary of concepts

A véc-tơ (vector / 벡터) has no meaning independent mô hình (model / 모델)/mục tiêu (objective / 목표). Rotating entire embedding không gian (space / 공간) while preserving dot products can leave hành vi (behavior / 동작) unchanged; individual coordinate therefore not chuẩn gốc (canonical / 정본) ngữ nghĩa (semantic / 의미적) axis.

Meaning lies relationships/subspaces and downstream computation.

## Cosine vs Dot sản phẩm (product / 제품)

If vectors normalized:

\[
q^Td=cos(q,d)
\]

If not normalized, dot-product includes magnitude. Some embedding các mô hình (models / 모델들) use véc-tơ (vector / 벡터) norm to encode confidence/frequency; follow recommended similarity.

Véc-tơ (vector / 벡터) DB chỉ số (metric / 지표) must match huấn luyện (training / 학습) mục tiêu (objective / 목표).

## Matryoshka / Truncatable Embeddings

Some các mô hình (models / 모델들) train embedding so prefix dimensions retain useful thông tin (information / 정보); véc-tơ (vector / 벡터) can truncate from e.g. 1024 to 256 dimensions with graceful degradation.

Benefit lưu trữ (storage / 저장소)/ANN speed. This thuộc tính (property / 속성) must be trained/validated; arbitrary truncating generic embedding may destroy chất lượng (quality / 품질).

## Embedding Dimension sự đánh đổi (trade-off / 트레이드오프)

Higher dimension increases sức chứa (capacity / 용량) but also:

- lưu trữ (storage / 저장소);
- bộ nhớ (memory / 메모리) bandwidth;
- ANN chỉ mục (index / 인덱스) kích thước (size / 크기);
- retrieval độ trễ (latency / 지연 시간);
- mẫu (sample / 표본)/overfit độ phức tạp (complexity / 복잡도).

Beyond a điểm (point / 지점), chất lượng (quality / 품질) gain may small. Evaluate mục tiêu (target / 대상) corpus.

## Embedding Normalization và Quantization

Large véc-tơ (vector / 벡터) corpora can store FP16/int8/product-quantized codes. Compression saves bộ nhớ (memory / 메모리) at recall chi phí (cost / 비용).

Quantization of embeddings/chỉ mục (index / 인덱스) is separate from LLM weight quantization, though principles numerical approximation related.

## Ngữ nghĩa (semantic / 의미적) tìm kiếm (search / 검색) chuỗi xử lý (pipeline / 파이프라인)

```text
Document
→ chunk
→ embed
→ index vector + metadata

Query
→ embed same compatible model
→ ANN search
→ filter/rerank
```

Mix embedding mô hình (model / 모델) versions corrupts hình học (geometry / 기하학).

## Asymmetric Retrieval

Truy vấn (query / 쿼리) and document roles differ. Some các mô hình (models / 모델들) use tác vụ (task / 작업) prefixes:

```text
query: ...
passage: ...
```

or separate encoders/projections. Ignoring required prefixes lowers chất lượng (quality / 품질).

## Hybrid tìm kiếm (search / 검색)

Dense embeddings struggle chính xác (exact / 정확한) IDs/names/numbers sometimes. BM25 lexical retriever catches chính xác (exact / 정확한) terms.

Hybrid retrieval fuses sparse + dense signals, especially enterprise mã (code / 코드)/sản phẩm (product / 제품)/legal docs.

## Embedding Fine-Tuning

Lĩnh vực (domain / 도메인) positives/negatives can adapt hình học (geometry / 기하학).

Hard negative example:

```text
query: reset corporate card PIN
negative: reset personal bank password
```

Semantically close but task-irrelevant, forcing mô hình (model / 모델) learn fine distinctions.

False negatives must be controlled.

## Embeddings and Privacy

Vectors are not guaranteed anonymous. Embeddings can leak attributes/membership/content under attacks; sensitive nguồn (source / 소스) permissions still apply.

Do not expose véc-tơ (vector / 벡터) store assuming “only numbers”. kiểm soát truy cập (access control / 접근 제어) and encryption remain needed.

## Embedding Inversion

Research can sometimes reconstruct or infer nguồn (source / 소스) văn bản (text / 텍스트)/attributes from embeddings. chính xác (exact / 정확한) feasibility depends mô hình (model / 모델)/truy cập (access / 접근), but principle: embedding is derived sensitive dữ liệu (data / 데이터).

## LLM bộ nhớ (memory / 메모리) vs véc-tơ (vector / 벡터) bộ nhớ (memory / 메모리)

Ứng dụng (application / 애플리케이션) may store past notes as embeddings and retrieve relevant memories. The véc-tơ (vector / 벡터) cơ sở dữ liệu (database / 데이터베이스) is bên ngoài (external / 외부) bộ nhớ (memory / 메모리) hệ thống (system / 시스템); LLM weights do not cập nhật (update / 업데이트) when inserting bộ nhớ (memory / 메모리).

Kiến trúc (architecture / 아키텍처):

```text
conversation/event
→ text record
→ embedding/index
future query
→ retrieve record
→ context
→ LLM
```

This distinction prevents anthropomorphic “LLM remembered permanently” confusion.

## Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) + Embedding

Kiến thức (knowledge / 지식) đồ thị (graph / 그래프) stores tường minh (explicit / 명시적) entities/relations; embeddings hỗ trợ (support / 지원) fuzzy ngữ nghĩa (semantic / 의미적) lookup. Hybrid GraphRAG-like các hệ thống (systems / 시스템들) may retrieve đồ thị (graph / 그래프) neighborhoods + véc-tơ (vector / 벡터) passages.

Tường minh (explicit / 명시적) quan hệ (relation / 관계) and dense similarity complement each other.

## Mô hình tư duy (mental model / 사고 모델)

```text
Token embedding      = initial learned code for token identity
Contextual hidden    = token representation after context computation
Retrieval embedding  = compressed text representation trained so distance is useful
```

All are vectors, but véc-tơ (vector / 벡터) purpose comes from mục tiêu (objective / 목표).

## Dùng chung (common / 공통) Misconceptions

### “Any LLM hidden trạng thái (state / 상태) can go into véc-tơ (vector / 벡터) DB for ngữ nghĩa (semantic / 의미적) tìm kiếm (search / 검색)”

Possible but not necessarily effective; dedicated retrieval mục tiêu (objective / 목표) matters.

### “véc-tơ (vector / 벡터) distance gives xác suất (probability / 확률) relevance”

No. Score needs empirical calibration if xác suất (probability / 확률) required.

### “Embedding removes sensitive văn bản (text / 텍스트)”

No. Treat embeddings derived from sensitive dữ liệu (data / 데이터) as sensitive.

### “Bigger embedding dimension always improves RAG”

Chất lượng (quality / 품질)/lưu trữ (storage / 저장소)/ANN sự đánh đổi (trade-off / 트레이드오프); retrieval errors often dominated chunking/dữ liệu (data / 데이터)/reranking rather than dimension.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Contextual Embeddings](../07_natural_language_processing/04_contextual_embeddings.md), [Information Retrieval](../07_natural_language_processing/08_search_and_information_retrieval.md), and later `09_retrieval_and_rag/`.

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from language models to llms](./00_from_language_models_to_llms.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
