# Transformer: Attention + Residual Computation ở quy mô lớn

Transformer (트랜스포머) không chỉ là “model dùng attention”. Nó là một architecture tổ chức computation thành repeated blocks gồm attention, feed-forward transformation, residual connections và normalization, cho phép sequence positions xử lý song song trong training và long-range interactions ngắn path hơn RNN.

Transformer là nền của BERT, GPT, T5, Vision Transformer và phần lớn modern foundation models, nên cần hiểu block ở mức tensor/mechanism chứ không chỉ hình minh họa.

## Input Representation

Token IDs được lookup embedding matrix:

\[
E\in R^{|V|\times d_{model}}
\]

Token `i`:

\[
x_i=E[token_i]
\]

Sau đó thêm/encode positional information.

Hidden tensor:

\[
X\in R^{B\times T\times d_{model}}
\]

## Core Transformer Block

Một simplified pre-norm block:

\[
H'=H+Attention(Norm(H))
\]

\[
H''=H'+FFN(Norm(H'))
\]

Lặp `L` layers.

Hai sublayers chính:

1. Attention — mix information across positions.
2. Feed-Forward Network — transform each position independently in feature dimension.

Residual stream carries representation through stack.

## Self-Attention Sub-layer

Given normalized hidden state:

\[
Q=XW_Q,
K=XW_K,
V=XW_V
\]

then:

\[
A=softmax\left(\frac{QK^T}{\sqrt{d_k}}+M\right)
\]

\[
O=AVW_O
\]

`M` is mask/bias.

Attention mixes tokens; without it each token's computation would stay local to own position in standard FFN.

## Feed-Forward Network

Classic Transformer FFN:

\[
FFN(x)=W_2\phi(W_1x+b_1)+b_2
\]

applied independently to each token position with shared weights.

Typically hidden expansion:

\[
d_{ff}\approx4d_{model}
\]

classic design, though modern gated FFNs/SwiGLU use different ratios.

Attention mixes **across sequence**; FFN mixes **across feature dimensions**.

## Residual Stream

Residual addition:

\[
x\leftarrow x+F(x)
\]

means sublayer writes an update into shared residual representation rather than replacing it completely.

This improves gradient flow and supports composition of many layers.

A useful mechanistic mental model is “residual stream as communication bus”: attention/MLP blocks read from and write transformations back into stream. Đây là abstraction hữu ích, không phải literal software bus.

## LayerNorm / RMSNorm

Pre-Norm modern pattern:

```text
x
├───────────────┐
↓ Norm          │
↓ Attention     │
└→ + residual ──┘
↓
├───────────────┐
↓ Norm          │
↓ MLP           │
└→ + residual ──┘
```

Pre-norm usually easier optimize deep stacks because identity residual path remains clean.

Many LLMs use RMSNorm instead of LayerNorm.

## Encoder Transformer

Encoder self-attention is usually bidirectional: every non-masked token can attend every other.

Good for representation/understanding tasks.

BERT-style masked-language-model pretraining uses encoder stack.

## Decoder Transformer

Decoder-only self-attention uses causal mask:

\[
M_{ij}=-\infty\quad j>i
\]

so position `i` cannot see future tokens.

GPT-style autoregressive model trains:

\[
P(x_{1:T})=\prod_tP(x_t\mid x_{<t})
\]

All positions can still be processed parallel during training because target sequence known and mask enforces causality.

## Encoder–Decoder Transformer

Encoder builds source representations bidirectionally.

Decoder block contains:

1. causal self-attention;
2. cross-attention over encoder output;
3. FFN.

Suitable translation/summarization and conditional generation.

## Multi-Head Dimensions

If:

\[
d_{model}=4096,
\quad h=32
\]

then classic head dimension:

\[
d_{head}=128
\]

Q/K/V projected then reshape:

```text
[B, T, D]
→ [B, T, H, Dh]
→ transpose to [B, H, T, Dh]
```

Shape reasoning is critical for implementation/inference systems.

## Positional Encoding

Original Transformer used sinusoidal:

\[
PE(pos,2i)=\sin(pos/10000^{2i/d})
\]

\[
PE(pos,2i+1)=\cos(pos/10000^{2i/d})
\]

Modern LLMs often use RoPE or relative mechanisms.

Position scheme influences context extension/extrapolation. Extending max context beyond training length is not trivial just changing config number.

## Parameter Count Roughly Comes From Where?

For decoder layer ignoring biases/norm:

Attention projections roughly:

\[
4d^2
\]

(Q,K,V,O; less with GQA/MQA for K/V).

FFN often roughly:

\[
2d\,d_{ff}
\]

or three matrices for gated FFN.

In many LLMs FFN parameters exceed attention parameters.

Embeddings/output head also significant, possibly weight-tied.

## Weight Tying

Input embedding and output unembedding matrix may share parameters:

\[
W_{out}=E^T
\]

This reduces parameter count and connects input/output token geometry.

Not universal but common.

## Computational Complexity

Self-attention roughly:

\[
O(T^2d)
\]

FFN:

\[
O(Td^2)
\]

Depending `T` vs `d`, different component dominates.

For long context, attention quadratic becomes major. For short context and huge `d`, MLP/projections may dominate FLOPs.

## Training Parallelism vs Generation Seriality

Training: entire sequence positions processed parallel under causal mask.

Generation: token `t+1` cannot compute until token `t` selected. This sequential dependency limits latency.

KV cache avoids recompute past attention K/V, nhưng generation remains autoregressive serial at token level.

Speculative decoding tries generate candidate tokens with smaller model then verify in batches, improving throughput without changing target distribution under proper algorithm.

## Context Window

Context window limits tokens model can process in one request/training segment.

Longer context increases:

- attention/cache memory;
- latency;
- data requirements to learn use long-range positions.

“Supports 1M tokens” does not imply model reasons equally well across 1M tokens. Effective context utilization requires evaluation.

## Transformer as Set/Graph-like Interaction

Ignoring positions, self-attention is permutation-equivariant and resembles message passing on fully connected graph.

Position encoding gives sequence structure. This explains why Transformer adapts to images (patch tokens), audio, proteins, molecules and multimodal tokens.

Architecture only needs items represented as tokens/elements plus relational/positional information.

## Why Transformer Scales Well

Several factors align:

- matrix multiplications map well to GPU/TPU;
- training sequence positions parallel;
- residual/norm stable deep stacking;
- attention handles flexible context;
- same architecture works across modalities/tasks;
- self-supervised objectives provide huge data.

Transformer success is architecture + data + compute + optimization + systems co-design.

## Limitations

- quadratic attention at long sequences;
- autoregressive decoding latency;
- huge memory/compute requirements;
- learned statistical behavior without built-in factual verification;
- finite context and retrieval limitations;
- opaque distributed representations.

These motivate efficient attention, state-space models, RAG, tools and system-level verification.

## Transformer vs RNN

| Property | RNN/LSTM | Transformer |
|---|---|---|
| Training position parallelism | thấp | cao |
| Long-range path | nhiều recurrent steps | direct attention path |
| State at inference | compact recurrent state | KV cache grows with context |
| Vanilla long-context compute | linear per recurrent step | quadratic full attention training |
| Streaming naturalness | cao | needs caching/chunking |

Không model universally superior under every deployment constraint.

## Transformer vs CNN

CNN hardcodes locality/translation structure. Transformer can learn global pairwise relations but weaker prior, often needs larger data/pretraining.

Vision architectures increasingly mix both ideas.

## Mental Model

```text
Residual stream holds token representations
Attention  → tokens exchange information
MLP        → each token transforms features internally
Norm       → stabilize scale
Residual   → preserve/accumulate information & gradients
Repeat many layers
```

## Common Misconceptions

### “Transformer = Attention”

Attention critical but MLP, residual, normalization, positions and training objective equally necessary architecture components.

### “Attention lets model see infinite history”

Only within context/cache window and compute constraints.

### “Decoder-only model has no encoder so it cannot understand input”

Same causal stack transforms prompt tokens into contextual representations before predicting continuation.

### “More context always improves answer”

Irrelevant/noisy context can degrade performance; retrieval/context engineering matters.

## Knowledge Connection

Transformer synthesizes [Attention](./04_attention.md), [Residual/Backprop](../05_neural_networks/04_backpropagation.md), [RMSNorm](../05_neural_networks/06_initialization_and_normalization.md), [Representation Learning](../05_neural_networks/08_representation_learning.md).

NLP and LLM folders will build tokenization, pretraining, scaling, instruction tuning and generation on top of this mechanism.