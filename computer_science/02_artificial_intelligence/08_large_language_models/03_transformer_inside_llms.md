# Transformer bên trong Large Language Models

Ở layer trước, Transformer đã được giải thích như một architecture gồm attention, feed-forward network, residual connection và normalization. Khi architecture đó được scale thành Large Language Model, cơ chế cơ bản không đổi, nhưng **tỷ lệ giữa các thành phần, cách tổ chức attention, positional encoding, normalization, feed-forward block, cache và parallelism** trở thành những quyết định ảnh hưởng trực tiếp tới chất lượng, tốc độ và chi phí.

Chapter này không lặp lại công thức attention từ đầu. Mục tiêu là nhìn Transformer như một **LLM computation engine**: một token đi qua model như thế nào, parameters nằm ở đâu, context được trộn ra sao, và vì sao inference behavior khác training behavior.

Xem nền: [Transformer](../06_deep_learning_architectures/05_transformer.md) và [Attention](../06_deep_learning_architectures/04_attention.md).

## Decoder-only stack

Một decoder-only LLM thường có flow:

```text
Token IDs
   ↓ embedding lookup
Token vectors + positional mechanism
   ↓
Transformer block 1
   ↓
Transformer block 2
   ↓
...
   ↓
Transformer block L
   ↓ final norm
Hidden state at each position
   ↓ output projection / unembedding
Vocabulary logits
   ↓ softmax / sampling
Next token
```

Mỗi block thường có hai computation lớn:

```text
Attention sublayer
Feed-Forward / MLP sublayer
```

và residual path chạy xuyên suốt.

## Residual stream như “shared working representation”

Với pre-norm architecture:

\[
x' = x + Attention(Norm(x))
\]

\[
x'' = x' + MLP(Norm(x'))
\]

Một cách nghĩ hữu ích là residual stream chứa representation hiện tại của mỗi token. Attention đọc representation của nhiều positions và ghi một update; MLP đọc từng position và ghi một feature transformation khác.

Đây là mental model, không phải claim rằng model có các “register” symbolic rõ ràng. Hidden information phân tán qua dimensions, layers và token positions.

## Attention trộn thông tin giữa positions

Với hidden states `X`, mỗi layer tạo:

\[
Q=XW_Q,\qquad K=XW_K,\qquad V=XW_V
\]

Causal mask đảm bảo token tại position `t` chỉ dùng positions `≤t`.

Attention output:

\[
O=softmax\left(\frac{QK^T}{\sqrt{d_h}}+M\right)V
\]

Điều quan trọng ở LLM scale không chỉ là công thức. Attention là nơi context length tạo cost theo sequence length và là nơi KV cache xuất hiện trong generation.

## Multi-Head, GQA và MQA

Classic multi-head attention dùng số Query/Key/Value heads giống nhau. Trong autoregressive serving, keys/values của mọi previous tokens phải được giữ trong KV cache.

Nếu model có:

```text
L layers
T cached tokens
Hkv KV heads
Dh head dimension
2 tensors: K and V
```

cache size roughly proportional:

\[
2LT H_{kv}D_h\times bytes\_per\_element
\]

Do đó modern LLMs thường dùng:

- **MHA**: Q heads = K/V heads;
- **MQA**: nhiều Q heads chia sẻ một K và V head;
- **GQA**: nhiều Q heads nhưng chỉ một số nhóm K/V heads.

GQA là compromise phổ biến: giảm KV memory/bandwidth trong khi giữ quality gần multi-head attention.

## Feed-Forward Network chiếm rất nhiều parameters

Một classic FFN:

\[
FFN(x)=W_2\phi(W_1x)
\]

Nếu hidden width `d` và intermediate width `d_ff≈4d`, chỉ hai matrices đã có khoảng:

\[
2d\cdot d_{ff}\approx8d^2
\]

parameters mỗi layer.

Modern LLMs thường dùng gated MLP, ví dụ SwiGLU:

\[
FFN(x)=W_3\left(SiLU(W_1x)\odot W_2x\right)
\]

Ba projections tạo multiplicative gating. Intermediate width thường điều chỉnh để parameter/FLOP budget phù hợp.

Attention thường được truyền thông nhiều vì dễ hình dung, nhưng FFN/MLP blocks chứa một phần rất lớn parameter và computation của dense LLM.

## MLP đang làm gì?

Attention chủ yếu route/mix information across token positions. MLP biến đổi representation tại từng token độc lập theo position nhưng shared weights.

Một perspective nghiên cứu xem MLP như associative/key-value-like memory cho learned features/facts, nhưng không nên literalize rằng mỗi neuron hay row là một fact. Knowledge distributed và có interaction qua many layers.

## RMSNorm và Pre-Norm

Many modern decoder LLMs dùng RMSNorm:

\[
RMS(x)=\sqrt{\frac1d\sum_i x_i^2+\epsilon}
\]

\[
RMSNorm(x)=g\odot\frac{x}{RMS(x)}
\]

Nó bỏ mean-centering của LayerNorm và giảm computation nhẹ.

Pre-norm đặt norm trước sublayer, giúp gradient đi qua residual identity path ổn định hơn trong deep stacks.

## Rotary Position Embedding (RoPE)

Transformer attention tự nó không biết token order. RoPE encode position bằng rotation của Q/K components.

Simplified pairwise rotation:

\[
\begin{bmatrix}
x'_{2i}\\x'_{2i+1}
\end{bmatrix}
=
\begin{bmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix}
x_{2i}\\x_{2i+1}
\end{bmatrix}
\]

Angle depends position and frequency.

Key benefit: dot products after rotation encode relative positional differences naturally.

Context extension methods may rescale/interpolate RoPE frequencies, but simply increasing context config can degrade position behavior nếu model chưa được trained/adapted appropriately.

## Output projection và weight tying

Final hidden state `h_t` maps to vocabulary logits:

\[
z_t=W_Uh_t+b
\]

với:

\[
W_U\in R^{|V|\times d}
\]

Then:

\[
P(token=k\mid context)=softmax(z_t)_k
\]

Một số models tie input embedding và output matrix:

\[
W_U=E
\]

hoặc transpose tùy convention.

Weight tying reduces parameters and creates shared lexical geometry, nhưng không phải requirement universal.

## Prefill và Decode là hai workload khác nhau

### Prefill

Model nhận toàn prompt dài `T` và computes representations cho tất cả positions. Matrix multiplications lớn, parallelism cao; workload thường compute-heavy.

### Decode

Sau đó mỗi step chỉ thêm một token. K/V cũ cache lại; model tính query/new K/V cho token mới rồi attend toàn cache.

Decode thường memory-bandwidth/latency-sensitive vì mỗi token cần đọc large weights + KV cache nhưng batch/sequence compute nhỏ hơn.

Do đó optimization inference phải tách:

```text
prefill throughput
vs
decode latency / tokens per second
```

## KV Cache không phải model memory dài hạn

KV cache là cached intermediate attention state của current context/request. Nó biến mất khi session/request kết thúc trừ khi serving system giữ/reuse.

Nó không update weights, không phải semantic memory database.

Application “memory” cần persist text/structured state externally rồi đưa lại context/retrieval.

## Context length và attention cost

Training full attention có score matrix roughly `T×T`. Longer context làm attention compute/memory tăng quadratic trong vanilla form.

Inference with KV cache avoids recomputing previous states, nhưng per-new-token attention vẫn grows roughly linearly với cached context length, và cache memory grows linearly.

Long-context model vì vậy có real systems cost even if API exposes huge context window.

## FlashAttention

Naive implementation materializes large attention matrix in high-bandwidth memory. FlashAttention reorganizes computation thành blocks để reduce memory IO and store fewer intermediates, while computing mathematically exact attention up to floating-point behavior.

Core lesson:

> Algorithmic complexity chưa đủ để predict speed; memory hierarchy và kernel design matter.

This is a direct bridge from AI mathematics to GPU systems engineering.

## Mixture of Experts (MoE) preview

Not every LLM is dense. MoE block has multiple expert FFNs and router sends each token to subset experts.

Conceptually:

\[
y=\sum_{e\in TopK(router(x))}p_e(x)Expert_e(x)
\]

Total parameters can be huge while only few experts active per token, reducing active compute relative dense model of same total parameter count.

Challenges:

- load balancing;
- routing instability;
- expert parallel communication;
- memory footprint;
- serving complexity.

MoE belongs to architecture/compute specialization and will return in infrastructure discussions.

## Parameter count vs active parameters

For dense model, nearly all layer parameters participate every token.

For MoE, total parameters ≠ active parameters per token. Therefore comparing “model size” only by total billions can mislead compute comparisons.

Need ask:

```text
total parameters?
active parameters/token?
training tokens?
architecture?
context?
precision?
```

## Quantization and architecture interaction

Inference may store weights INT8/INT4 while compute/dequantize into higher precision. Some layers/outliers more sensitive.

Architecture determines quantization behavior: normalization, activation outliers, KV cache dtype and expert routing can all matter.

Quantization does not conceptually change Transformer function target, but approximates numeric execution to save memory/bandwidth.

## Transformer block as repeated learned program

Even though layer structure repeated, weights usually differ per layer. Each layer can refine representation through:

```text
retrieve relevant context via attention
→ transform features via MLP
→ accumulate through residual stream
```

After many layers, final representation has undergone iterative contextual computation.

This is why next-token prediction can involve substantial internal computation before one token is emitted.

## Common Misconceptions

### “LLM parameters chủ yếu nằm trong attention”

MLP/FFN projections often contain larger share of dense block parameters.

### “Context window càng lớn thì model nhớ tốt hơn proportionally”

Window only provides addressable input capacity; actual utilization can degrade with distance/noise.

### “KV cache là persistent memory của LLM”

It is request/context-specific cached attention state, not learned or durable memory.

### “Quantization làm model trở thành architecture khác”

Usually same architecture/function family executed approximately at lower precision; quality loss depends method.

### “MoE 1T parameters compute như dense 1T model”

Only subset experts active each token, though memory/communication still substantial.

## Mental Model

```text
Residual stream = evolving token state
Attention       = context routing/mixing
MLP/Experts     = feature transformation / nonlinear computation
Norm            = stabilize scale
Position        = encode order/relative distance
Output head     = turn final state into next-token logits
KV cache        = reuse current-context attention states during decode
```

## Knowledge Connection

This chapter ties [Transformer](../06_deep_learning_architectures/05_transformer.md), [Attention](../06_deep_learning_architectures/04_attention.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md) and later [AI Compute & Infrastructure](../17_ai_compute_and_infrastructure/).

Xem tiếp: [Pretraining](./04_pretraining.md).