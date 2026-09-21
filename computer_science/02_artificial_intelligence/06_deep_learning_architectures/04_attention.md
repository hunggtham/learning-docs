# Attention: cho model truy cập thông tin theo relevance

Attention (어텐션 / 주의 메커니즘) giải quyết một limitation quan trọng của early sequence-to-sequence models: decoder không nên bị buộc nén toàn bộ source sequence vào một fixed-size vector. Thay vào đó, tại mỗi output step, model có thể **tính relevance giữa query hiện tại và nhiều memory positions**, rồi tổng hợp information phù hợp.

Modern self-attention mở rộng idea này: mỗi token có thể truy cập các token khác dựa trên learned content-dependent relationships.

## Từ fixed context tới dynamic context

RNN encoder cho states:

\[
h_1,h_2,...,h_T
\]

Thay vì chỉ đưa `h_T` cho decoder, attention tạo context tại decoder step `t`:

\[
c_t=\sum_i\alpha_{t,i}h_i
\]

Weights `α` phụ thuộc decoder state và encoder state:

\[
e_{t,i}=score(s_{t-1},h_i)
\]

\[
\alpha_{t,i}=softmax(e_{t,i})
\]

Decoder vì vậy “look back” source dynamically.

## Query, Key, Value

Transformer formalizes memory lookup bằng ba roles.

Given representation matrix `X`:

\[
Q=XW_Q,
\quad K=XW_K,
\quad V=XW_V
\]

Mental model:

- **Query (Q / 쿼리)**: tôi đang tìm loại information nào?
- **Key (K / 키)**: mỗi item “advertise” nó match query thế nào?
- **Value (V / 값)**: nếu item được attend, content nào được truyền?

Đây là analogy, không literal database key-value lookup.

## Scaled Dot-Product Attention

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

Hãy unpack từng step.

### 1. Similarity Scores

\[
S=QK^T
\]

Nếu sequence length `T`, `S∈R^{T×T}` trong self-attention. Entry `S_{ij}` đo alignment giữa query token `i` và key token `j`.

Dot product có magnitude tăng với dimension. Nếu Q/K components variance roughly 1, dot-product variance scale ~`d_k`.

### 2. Scale

\[
\frac{S}{\sqrt{d_k}}
\]

keeps score scale more stable as dimension grows. Without scaling, softmax may become extremely peaked; gradients shrink because distribution saturates.

### 3. Mask

Before softmax, forbidden positions get `-∞` (large negative numerically).

Causal mask:

```text
token i can attend j only if j ≤ i
```

Padding mask excludes pad tokens.

### 4. Softmax

\[
A=softmax(S_{masked})
\]

Each query row becomes positive weights sum 1.

### 5. Weighted Values

\[
O=AV
\]

Each output representation is weighted mixture of value vectors.

## Attention không “copy probability of truth”

Attention weights are routing coefficients learned for task. A weight `0.8` does not mean “80% probability token j is causally responsible” or factual confidence.

Interpretability based solely attention maps is limited because:

- values contain transformed information;
- multiple heads/layers compose;
- residual paths bypass attention;
- alternative attention distributions may yield similar output.

## Self-Attention

Q/K/V đều từ same sequence representation `X`.

Each position contextualizes itself based on others.

Example word `bank`:

```text
river bank → attends river/water context
bank loan  → attends loan/money context
```

Same initial token embedding becomes different contextual representation.

## Cross-Attention

Queries from one sequence/modality, keys/values from another:

\[
Q=H_{decoder}W_Q
\]

\[
K=H_{encoder}W_K,
V=H_{encoder}W_V
\]

Used encoder-decoder translation and multimodal fusion.

## Multi-Head Attention

Instead of one attention:

\[
head_i=Attention(QW_i^Q,KW_i^K,VW_i^V)
\]

Concatenate:

\[
MHA=Concat(head_1,...,head_h)W_O
\]

Different heads can learn different interaction patterns/subspaces.

Head dimension usually:

\[
d_{head}=d_{model}/h
\]

But modern variants may use different Q-head/KV-head counts.

## Multi-Query và Grouped-Query Attention

Autoregressive inference KV cache memory lớn. **Multi-Query Attention (MQA)** shares one K/V head across many query heads. **Grouped-Query Attention (GQA)** uses fewer K/V heads than Q heads.

Trade-off: reduce KV cache/memory bandwidth while retain much multi-head quality. Many modern LLMs use GQA.

## Positional Information

Self-attention score without position depends content, not order inherently.

Need inject/order bias:

- sinusoidal position encoding;
- learned absolute embeddings;
- relative position bias;
- Rotary Position Embedding (RoPE);
- ALiBi.

### RoPE intuition

RoPE rotates Q/K vector pairs by position-dependent angles. Dot product then naturally depends on relative position differences.

It does not simply “add position number”; it modifies geometry of Q/K interaction.

## Attention Complexity

Vanilla self-attention builds `T×T` score matrix:

\[
O(T^2d)
\]

compute/memory scales quadratically with sequence length `T` for attention component.

For long context this becomes expensive. Techniques:

- FlashAttention: exact attention with IO-aware tiling, not approximation;
- sparse/local attention;
- sliding window;
- low-rank/kernel approximations;
- state-space/recurrent alternatives.

Important distinction: FlashAttention reduces memory traffic/intermediate storage but mathematical attention result remains exact within numerical considerations.

## Causal Attention

For decoder-only language model:

\[
A_{ij}=0\quad j>i
\]

Token cannot access future token during training. Despite processing full sequence in parallel, mask preserves autoregressive factorization.

This is one key Transformer advantage over RNN: training all positions parallel while maintaining causal information constraint.

## KV Cache

During autoregressive generation, previous keys/values need not recompute each token. Store them:

```text
step t:
compute Q/K/V for new token
reuse K/V of tokens 1...t-1
attend over cached K/V
```

KV cache memory scales with layers × sequence length × KV heads × head dimension × dtype.

Long context inference often becomes memory-bandwidth/cache problem, not just FLOPs.

## Attention Sink / Long Context Issues

Long context does not guarantee model uses all tokens effectively. Position extrapolation, attention dilution, retrieval failures and lost-in-the-middle behavior can occur.

Context-window size is capacity limit, not proof of uniform usable memory.

## Sparse Attention

If each query attends subset positions, complexity can reduce. Local window works when nearby context dominates; global tokens/structured patterns preserve long-range access.

Sparse pattern is inductive bias: efficient but may block relevant connection.

## Attention as Differentiable Retrieval

A powerful mental connection:

```text
Query vector
→ similarity against keys
→ normalized scores
→ weighted retrieval of values
```

This resembles retrieval, but all memory vectors live inside current neural computation and operation is differentiable.

RAG later performs **external retrieval** over document index. Attention performs **internal differentiable retrieval** over tokens/hidden states.

## Why Attention improved seq2seq

Path length between distant tokens in self-attention is one layer instead of many recurrent steps. Training parallelizes across sequence positions. Dynamic context removes fixed bottleneck.

Trade-off is quadratic pairwise interaction cost.

## Attention and graph message passing

Self-attention can be viewed as fully connected graph where each token node sends message to others with learned edge weights based on Q/K compatibility.

This connects Transformer to Graph Neural Network intuition, though exact parameterization differs.

## Numerical Stability

Softmax should use max subtraction. Attention kernels also carefully handle mask `-inf`, low precision, accumulation.

FlashAttention computes softmax in blocks using online normalization to avoid materializing full matrix and maintain stability.

## Mental Model

> Attention = content-dependent routing. Query asks, keys compete for relevance, values carry information, softmax determines routing weights.

Self-attention lets every token rewrite its representation using other tokens selected by learned relevance.

## Common Misconceptions

### “Attention weight = importance/explanation”

It is routing coefficient, not guaranteed causal explanation.

### “Attention solves long-term memory completely”

It enables direct access within context window, but long context still has compute and utilization limits.

### “Multi-head means each head has a predefined role”

Roles are learned, may be redundant/distributed and vary layers/models.

### “FlashAttention approximates attention”

No. Standard FlashAttention algorithms compute exact attention more IO-efficiently.

### “RAG and attention are same”

Both retrieval-like, but attention routes internal hidden values; RAG retrieves external documents/chunks before/around generation.

## Knowledge Connection

Attention combines [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), [Probability-like Softmax](../01_mathematical_foundations/02_probability_for_ai.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [Encoder–Decoder](./03_encoder_decoder_models.md).

Xem tiếp: [Transformer](./05_transformer.md), nơi attention được ghép với residual stream, normalization và feed-forward blocks thành scalable architecture.