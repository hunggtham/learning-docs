# Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Attention**. Route đi từ fixed context → dynamic relevance → query/key/value → masking/complexity → cross/self-attention, để context selection được nối với sequence modeling và cost.

Attention (어텐션 / 주의 메커니즘) giải quyết một limitation quan trọng của early sequence-to-sequence các mô hình (models / 모델들): decoder không nên bị buộc nén toàn bộ nguồn (source / 소스) chuỗi (sequence / 시퀀스) vào một fixed-size véc-tơ (vector / 벡터). Thay vào đó, tại mỗi đầu ra (output / 출력) step, mô hình (model / 모델) có thể **tính relevance giữa truy vấn (query / 쿼리) hiện tại và nhiều bộ nhớ (memory / 메모리) positions**, rồi tổng hợp thông tin (information / 정보) phù hợp.

Hiện đại (modern / 현대적) self-attention mở rộng idea này: mỗi đơn vị từ (token / 토큰) có thể truy cập các đơn vị từ (token / 토큰) khác dựa trên learned content-dependent relationships.

## Từ fixed ngữ cảnh (context / 맥락) tới động (dynamic / 동적) ngữ cảnh (context / 맥락)

RNN encoder cho states:

\[
h_1,h_2,...,h_T
\]

Thay vì chỉ đưa `h_T` cho decoder, attention tạo ngữ cảnh (context / 맥락) tại decoder step `t`:

\[
c_t=\sum_i\alpha_{t,i}h_i
\]

Weights `α` phụ thuộc decoder trạng thái (state / 상태) và encoder trạng thái (state / 상태):

\[
e_{t,i}=score(s_{t-1},h_i)
\]

\[
\alpha_{t,i}=softmax(e_{t,i})
\]

Decoder vì vậy “look back” nguồn (source / 소스) dynamically.

> **Chuyển mạch:** Trong **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Truy vấn (query / 쿼리), Key, giá trị (value / 값)** tiếp nhận điểm tựa từ **Từ fixed ngữ cảnh (context / 맥락) tới động (dynamic / 동적) ngữ cảnh (context / 맥락)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scaled Dot-Product Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Truy vấn (query / 쿼리), Key, giá trị (value / 값)

Transformer formalizes bộ nhớ (memory / 메모리) lookup bằng ba roles.

Given biểu diễn (representation / 표현) ma trận (matrix / 행렬) `X`:

\[
Q=XW_Q,
\quad K=XW_K,
\quad V=XW_V
\]

Mô hình tư duy (mental model / 사고 모델):

- **truy vấn (query / 쿼리)**: tôi đang tìm loại thông tin (information / 정보) nào?
- **Key (K / 키)**: mỗi item “advertise” nó match truy vấn (query / 쿼리) thế nào?
- **giá trị (value / 값)**: nếu item được attend, content nào được truyền?

Đây là analogy, không literal cơ sở dữ liệu (database / 데이터베이스) key-value lookup.

> **Chuyển mạch:** Ở chặng này của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Scaled Dot-Product Attention** tiếp nhận điểm tựa từ **Truy vấn (query / 쿼리), Key, giá trị (value / 값)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention không “bản sao (copy / 복사) xác suất (probability / 확률) of truth”** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scaled Dot-Product Attention

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Hãy unpack từng step.

### 1. Similarity Scores

\[
S=QK^T
\]

Nếu chuỗi (sequence / 시퀀스) length `T`, `S∈R^{T×T}` trong self-attention. Entry `S_{ij}` đo alignment giữa truy vấn (query / 쿼리) đơn vị từ (token / 토큰) `i` và key đơn vị từ (token / 토큰) `j`.

Dot sản phẩm (product / 제품) có magnitude tăng với dimension. Nếu Q/K components variance roughly 1, dot-product variance quy mô (scale / 규모) ~`d_k`.

### 2. quy mô (scale / 규모)

\[
\frac{S}{\sqrt{d_k}}
\]

keeps score quy mô (scale / 규모) more stable as dimension grows. Without scaling, softmax may become extremely peaked; gradients shrink because phân phối (distribution / 분포) saturates.

### 3. Mask

Before softmax, forbidden positions get `-∞` (large negative numerically).

Nhân quả (causal / 인과적) mask:

```text
token i can attend j only if j ≤ i
```

Padding mask excludes pad tokens.

### 4. Softmax

\[
A=softmax(S_{masked})
\]

Each truy vấn (query / 쿼리) row becomes positive weights sum 1.

### 5. Weighted Values

\[
O=AV
\]

Each đầu ra (output / 출력) biểu diễn (representation / 표현) is weighted mixture of giá trị (value / 값) vectors.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Attention không “bản sao (copy / 복사) xác suất (probability / 확률) of truth”** tiếp nhận điểm tựa từ **Scaled Dot-Product Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Self-Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention không “bản sao (copy / 복사) xác suất (probability / 확률) of truth”

Attention weights are routing coefficients learned for tác vụ (task / 작업). A weight `0.8` does not mean “80% xác suất (probability / 확률) đơn vị từ (token / 토큰) j is causally responsible” or factual confidence.

Interpretability based solely attention maps is limited because:

- values contain transformed thông tin (information / 정보);
- multiple heads/layers compose;
- residual paths bypass attention;
- alternative attention distributions may yield similar đầu ra (output / 출력).

> **Chuyển mạch:** Trong **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Self-Attention** tiếp nhận điểm tựa từ **Attention không “bản sao (copy / 복사) xác suất (probability / 확률) of truth”** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cross-Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Self-Attention

Q/K/V đều từ same chuỗi (sequence / 시퀀스) biểu diễn (representation / 표현) `X`.

Each position contextualizes itself based on others.

Example word `bank`:

```text
river bank → attends river/water context
bank loan  → attends loan/money context
```

Same initial đơn vị từ (token / 토큰) embedding becomes different contextual biểu diễn (representation / 표현).

> **Chuyển mạch:** Ở chặng này của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Cross-Attention** tiếp nhận điểm tựa từ **Self-Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Head Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cross-Attention

Queries from one chuỗi (sequence / 시퀀스)/modality, keys/values from another:

\[
Q=H_{decoder}W_Q
\]

\[
K=H_{encoder}W_K,
V=H_{encoder}W_V
\]

Used encoder-decoder translation and multimodal fusion.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Multi-Head Attention** tiếp nhận điểm tựa từ **Cross-Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Query và Grouped-Query Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Head Attention

Instead of one attention:

\[
head_i=Attention(QW_i^Q,KW_i^K,VW_i^V)
\]

Concatenate:

\[
MHA=Concat(head_1,...,head_h)W_O
\]

Different heads can learn different tương tác (interaction / 상호작용) patterns/subspaces.

Head dimension usually:

\[
d_{head}=d_{mô hình (model / 모델)}/h
\]

But hiện đại (modern / 현대적) variants may use different Q-head/KV-head counts.

> **Chuyển mạch:** Trong **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Multi-Query và Grouped-Query Attention** tiếp nhận điểm tựa từ **Multi-Head Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Positional thông tin (information / 정보)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Query và Grouped-Query Attention

Autoregressive suy luận (inference / 추론) KV bộ nhớ đệm (cache / 캐시) bộ nhớ (memory / 메모리) lớn. **Multi-Query Attention (MQA)** shares one K/V head across many truy vấn (query / 쿼리) heads. **Grouped-Query Attention (GQA)** uses fewer K/V heads than Q heads.

Sự đánh đổi (trade-off / 트레이드오프): reduce KV bộ nhớ đệm (cache / 캐시)/bộ nhớ (memory / 메모리) bandwidth while retain much multi-head chất lượng (quality / 품질). Many hiện đại (modern / 현대적) LLMs use GQA.

> **Chuyển mạch:** Ở chặng này của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Positional thông tin (information / 정보)** tiếp nhận điểm tựa từ **Multi-Query và Grouped-Query Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Positional thông tin (information / 정보)

Self-attention score without position depends content, not thứ tự (order / 순서) inherently.

Need inject/thứ tự (order / 순서) độ lệch (bias / 편향):

- sinusoidal position encoding;
- learned absolute embeddings;
- relative position độ lệch (bias / 편향);
- Rotary Position Embedding (RoPE);
- ALiBi.

### RoPE intuition

RoPE rotates Q/K véc-tơ (vector / 벡터) pairs by position-dependent angles. Dot sản phẩm (product / 제품) then naturally depends on relative position differences.

It does not simply “add position number”; it modifies hình học (geometry / 기하학) of Q/K tương tác (interaction / 상호작용).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Attention độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **Positional thông tin (information / 정보)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhân quả (causal / 인과적) Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention độ phức tạp (complexity / 복잡도)

Vanilla self-attention builds `T×T` score ma trận (matrix / 행렬):

\[
O(T^2d)
\]

compute/bộ nhớ (memory / 메모리) scales quadratically with chuỗi (sequence / 시퀀스) length `T` for attention thành phần (component / 컴포넌트).

For long ngữ cảnh (context / 맥락) this becomes expensive. Techniques:

- FlashAttention: chính xác (exact / 정확한) attention with IO-aware tiling, not approximation;
- sparse/cục bộ (local / 로컬) attention;
- sliding cửa sổ (window / 윈도우);
- low-rank/kernel approximations;
- state-space/recurrent alternatives.

Important distinction: FlashAttention reduces bộ nhớ (memory / 메모리) traffic/intermediate lưu trữ (storage / 저장소) but mathematical attention kết quả (result / 결과) remains chính xác (exact / 정확한) within numerical considerations.

> **Chuyển mạch:** Trong **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Nhân quả (causal / 인과적) Attention** tiếp nhận điểm tựa từ **Attention độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **KV bộ nhớ đệm (cache / 캐시)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhân quả (causal / 인과적) Attention

For decoder-only ngôn ngữ (language / 언어) mô hình (model / 모델):

\[
A_{ij}=0\quad j>i
\]

Đơn vị từ (token / 토큰) cannot truy cập (access / 접근) future đơn vị từ (token / 토큰) during huấn luyện (training / 학습). Despite processing full chuỗi (sequence / 시퀀스) in parallel, mask preserves autoregressive factorization.

This is one key Transformer advantage over RNN: huấn luyện (training / 학습) all positions parallel while maintaining nhân quả (causal / 인과적) thông tin (information / 정보) ràng buộc (constraint / 제약조건).

> **Chuyển mạch:** Ở chặng này của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **KV bộ nhớ đệm (cache / 캐시)** tiếp nhận điểm tựa từ **Nhân quả (causal / 인과적) Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention Sink / Long ngữ cảnh (context / 맥락) Issues** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## KV bộ nhớ đệm (cache / 캐시)

During autoregressive generation, previous keys/values need not recompute each đơn vị từ (token / 토큰). Store them:

```text
step t:
compute Q/K/V for new token
reuse K/V of tokens 1...t-1
attend over cached K/V
```

KV bộ nhớ đệm (cache / 캐시) bộ nhớ (memory / 메모리) scales with layers × chuỗi (sequence / 시퀀스) length × KV heads × head dimension × dtype.

Long ngữ cảnh (context / 맥락) suy luận (inference / 추론) often becomes memory-bandwidth/bộ nhớ đệm (cache / 캐시) bài toán (problem / 문제), not just FLOPs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Attention Sink / Long ngữ cảnh (context / 맥락) Issues** tiếp nhận điểm tựa từ **KV bộ nhớ đệm (cache / 캐시)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sparse Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention Sink / Long ngữ cảnh (context / 맥락) Issues

Long ngữ cảnh (context / 맥락) does not guarantee mô hình (model / 모델) uses all tokens effectively. Position extrapolation, attention dilution, retrieval failures and lost-in-the-middle hành vi (behavior / 동작) can occur.

Context-window kích thước (size / 크기) is sức chứa (capacity / 용량) limit, not proof of uniform usable bộ nhớ (memory / 메모리).

> **Chuyển mạch:** Trong **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Sparse Attention** tiếp nhận điểm tựa từ **Attention Sink / Long ngữ cảnh (context / 맥락) Issues** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention as Differentiable Retrieval** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sparse Attention

If each truy vấn (query / 쿼리) attends subset positions, độ phức tạp (complexity / 복잡도) can reduce. cục bộ (local / 로컬) cửa sổ (window / 윈도우) works when nearby ngữ cảnh (context / 맥락) dominates; toàn cục (global / 전역) tokens/structured patterns preserve long-range truy cập (access / 접근).

Sparse mẫu (pattern / 패턴) is inductive độ lệch (bias / 편향): efficient but may khối (block / 블록) relevant liên kết (connection / 연결).

> **Chuyển mạch:** Ở chặng này của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Attention as Differentiable Retrieval** tiếp nhận điểm tựa từ **Sparse Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Why Attention improved seq2seq** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention as Differentiable Retrieval

A powerful mental liên kết (connection / 연결):

```text
Query vector
→ similarity against keys
→ normalized scores
→ weighted retrieval of values
```

This resembles retrieval, but all bộ nhớ (memory / 메모리) vectors live inside hiện tại (current / 현재) neural computation and thao tác (operation / 연산) is differentiable.

RAG later performs **bên ngoài (external / 외부) retrieval** over document chỉ mục (index / 인덱스). Attention performs **nội bộ (internal / 내부) differentiable retrieval** over tokens/hidden states.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Why Attention improved seq2seq** tiếp nhận điểm tựa từ **Attention as Differentiable Retrieval** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention and đồ thị (graph / 그래프) message passing** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why Attention improved seq2seq

Đường dẫn (path / 경로) length between distant tokens in self-attention is one tầng (layer / 계층) instead of many recurrent steps. huấn luyện (training / 학습) parallelizes across chuỗi (sequence / 시퀀스) positions. động (dynamic / 동적) ngữ cảnh (context / 맥락) removes fixed bottleneck.

Sự đánh đổi (trade-off / 트레이드오프) is quadratic pairwise tương tác (interaction / 상호작용) chi phí (cost / 비용).

> **Chuyển mạch:** Trong **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Attention and đồ thị (graph / 그래프) message passing** tiếp nhận điểm tựa từ **Why Attention improved seq2seq** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Numerical Stability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention and đồ thị (graph / 그래프) message passing

Self-attention can be viewed as fully connected đồ thị (graph / 그래프) where each đơn vị từ (token / 토큰) nút (node / 노드) sends message to others with learned edge weights based on Q/K tính tương thích (compatibility / 호환성).

This connects Transformer to đồ thị (graph / 그래프) Neural mạng (network / 네트워크) intuition, though chính xác (exact / 정확한) parameterization differs.

> **Chuyển mạch:** Ở chặng này của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Numerical Stability** tiếp nhận điểm tựa từ **Attention and đồ thị (graph / 그래프) message passing** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Numerical Stability

Softmax should use max subtraction. Attention kernels also carefully handle mask `-inf`, low precision, accumulation.

FlashAttention computes softmax in blocks using online normalization to avoid materializing full ma trận (matrix / 행렬) and maintain stability.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Numerical Stability** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Attention = content-dependent routing. truy vấn (query / 쿼리) asks, keys compete for relevance, values carry thông tin (information / 정보), softmax determines routing weights.

Self-attention lets every đơn vị từ (token / 토큰) rewrite its biểu diễn (representation / 표현) using other tokens selected by learned relevance.

> **Chuyển mạch:** Trong **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Attention weight = importance/explanation”

It is routing coefficient, not guaranteed nhân quả (causal / 인과적) explanation.

### “Attention solves long-term bộ nhớ (memory / 메모리) completely”

It enables direct truy cập (access / 접근) within ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우), but long ngữ cảnh (context / 맥락) still has compute and utilization limits.

### “Multi-head means each head has a predefined role”

Roles are learned, may be redundant/phân tán (distributed / 분산) and vary layers/các mô hình (models / 모델들).

### “FlashAttention approximates attention”

No. tiêu chuẩn (standard / 표준) FlashAttention algorithms compute chính xác (exact / 정확한) attention more IO-efficiently.

### “RAG and attention are same”

Both retrieval-like, but attention routes nội bộ (internal / 내부) hidden values; RAG retrieves bên ngoài (external / 외부) documents/chunks before/around generation.

> **Chuyển mạch:** Ở chặng này của **Attention: cho mô hình (model / 모델) truy cập thông tin theo relevance**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Attention combines [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Probability-like Softmax](../01_mathematical_foundations/02_probability_for_ai.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [Encoder–Decoder](./03_encoder_decoder_models.md).

Xem tiếp: [Transformer](./05_transformer.md), nơi attention được ghép với residual stream, normalization và feed-forward blocks thành scalable kiến trúc (architecture / 아키텍처).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
