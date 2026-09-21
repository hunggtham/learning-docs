# Encoder–Decoder Models: tách hiểu input và tạo output

Encoder–Decoder (인코더–디코더) là architectural pattern cho tasks nơi input và output có structures/lengths khác nhau. Encoder biến input thành internal representation; decoder dùng representation đó để tạo output.

Pattern này xuất hiện trong translation, summarization, speech recognition, image captioning, autoencoders và Transformers. “Encoder” và “decoder” không phải một algorithm cụ thể; chúng là vai trò trong computation system.

## Sequence-to-Sequence Problem

Translation:

```text
English sequence → Korean sequence
```

Input length khác output length. Per-token aligned classifier không đủ.

Model factor output autoregressively:

\[
P(y_{1:T}\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x)
\]

Encoder processes `x`; decoder models conditional next-token distribution.

## Early RNN Seq2Seq

Encoder RNN:

\[
h_t^{enc}=f(x_t,h_{t-1}^{enc})
\]

Final state:

\[
c=h_T^{enc}
\]

Decoder:

\[
h_t^{dec}=g(y_{t-1},h_{t-1}^{dec},c)
\]

All source information compressed into fixed vector `c`.

For long sentences, this becomes information bottleneck.

## Context Bottleneck

Imagine source 100 tokens nhưng decoder only gets one vector. Even high-dimensional vector must preserve all details needed at every output step.

As input grows, performance degrades. This motivated attention: decoder at each step constructs context from all encoder states dynamically.

## Teacher Forcing in Decoder

Training usually conditions on ground-truth previous target:

\[
P(y_t\mid y_{<t}^{true},x)
\]

Inference conditions on generated tokens.

Mismatch creates exposure bias, but teacher forcing remains computationally effective and standard.

## Start / End Tokens

Decoder needs know when generation begins/ends.

Special tokens:

```text
<BOS> beginning of sequence
<EOS> end of sequence
```

Generation stops when EOS emitted or max length reached.

Modern LLM chat protocols use richer special/control tokens but same idea: sequence structure encoded by token conventions.

## Decoding Algorithms

At each step model outputs distribution. Choosing final sequence requires search.

### Greedy Decoding

\[
y_t=\arg\max_kP(y_t=k\mid context)
\]

Fast but locally best choice may cause poor global sequence.

### Beam Search

Keep top `B` partial hypotheses according cumulative log-probability.

```text
step 1: keep B candidates
step 2: expand each → keep best B
...
```

Beam search is heuristic search in sequence space.

Length normalization often needed because log probabilities sum negative values and may favor short sequences.

### Sampling

For open-ended generation, sample from distribution. Temperature/top-k/top-p later discussed in LLM generation.

Translation historically favors beam; creative text often sampling.

## Encoder-only Architecture

If output is label/representation, decoder unnecessary.

BERT-like models are encoder-only: bidirectional self-attention creates contextual representations for classification/extraction.

## Decoder-only Architecture

If task is autoregressive continuation conditioned on prefix, decoder-only architecture sufficient.

GPT-family uses causal self-attention:

\[
P(x_t\mid x_{<t})
\]

Input prompt itself acts conditioning prefix; no separate encoder.

## Encoder–Decoder Transformer

Models like original Transformer/T5-style:

- encoder: bidirectional self-attention over source;
- decoder: causal self-attention over generated target;
- cross-attention: decoder queries encoder representations.

This matches translation/conditional generation naturally.

## Cross-Attention

Decoder hidden state provides queries; encoder outputs provide keys/values:

\[
Attention(Q_{dec},K_{enc},V_{enc})
\]

At each target position, decoder retrieves relevant source information.

Cross-attention is learned differentiable retrieval across source positions.

## Beyond Text

Image captioning:

```text
Image encoder → visual tokens/features
        ↓ cross-attention
Text decoder → caption
```

Speech translation:

```text
audio encoder → acoustic representation
text decoder → translated text
```

Multimodal models often use encoder/projection + LLM decoder patterns.

## Latent Bottleneck Autoencoders

Autoencoder also encoder-decoder:

\[
x\xrightarrow{encoder}z\xrightarrow{decoder}\hat x
\]

Nhưng goal là reconstruct input, not conditional sequence translation. Same architecture pattern, different objective/probabilistic semantics.

## Information Flow là cách phân loại hữu ích

Thay vì nhớ model names, hỏi:

```text
Which positions can encoder see?
Which positions can decoder see?
Where can decoder access source?
Is generation causal?
What representation bottleneck exists?
```

Attention mask/connectivity defines information flow.

## Mental Model

> Encoder answers “input nên được biểu diễn như thế nào?”; decoder answers “từ representation + outputs trước đó, tạo output tiếp theo thế nào?”.

Cross-attention removes need to squeeze all source details into one fixed vector.

## Common Misconceptions

### “Encoder = embedding layer, decoder = output layer”

Không. Encoder/decoder thường là multi-layer networks with rich computation.

### “Every Transformer has encoder and decoder”

Có encoder-only, decoder-only và encoder-decoder families.

### “Beam search guarantees highest-probability sequence”

Finite beam is heuristic; exact search over huge sequence space infeasible.

### “Decoder-only LLM cannot process input because no encoder”

Prompt tokens are encoded through same causal Transformer stack; no separate encoder module required.

## Knowledge Connection

Encoder–Decoder nối [Search](../02_search_reasoning_and_planning/00_state_space_and_search.md), [Sequence Models](./01_sequence_models.md), [RNN/LSTM](./02_rnn_lstm_gru.md) và trực tiếp dẫn tới [Attention](./04_attention.md).