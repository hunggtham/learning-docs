# Sequence Models: dữ liệu có thứ tự cần model khác gì?

Sequence data (순차 데이터) khác fixed unordered feature vector vì **thứ tự và context** mang meaning. Câu `dog bites man` khác `man bites dog`; sensor readings cùng values nhưng order khác biểu diễn dynamics khác. Vì vậy sequence model phải xử lý variable length, dependency qua positions và đôi khi causal direction.

Trước RNN và Transformer, cần hiểu sequence modeling problem itself.

## Sequence notation

Một sequence:

\[
x_{1:T}=(x_1,x_2,...,x_T)
\]

Output có thể:

- sequence → one: sentiment/classification;
- one → sequence: conditional generation;
- sequence → sequence aligned: tagging;
- sequence → sequence unaligned: translation;
- autoregressive next-step prediction.

Architecture phụ thuộc output structure.

## Markov Assumption

Simplest sequence model assume future phụ thuộc limited past.

First-order Markov:

\[
P(x_t\mid x_{1:t-1})=P(x_t\mid x_{t-1})
\]

This drastically simplifies modeling nhưng bỏ long-range dependencies.

Higher-order increases context nhưng state combinations explode.

RNN attempts learn compressed state summarizing arbitrary history.

## Autoregressive Factorization

Any joint sequence distribution can factor:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Language models use this principle. Transformer changed mechanism computing context, not this probability factorization.

Autoregressive generation repeatedly:

```text
context → predict distribution next token
sample/select token
append
repeat
```

## Sequence State

A recurrent model maintains hidden state:

\[
h_t=f(h_{t-1},x_t)
\]

`h_t` tries compress relevant history `x_{1:t}`.

This is elegant but creates information bottleneck: long history must flow through fixed-size state.

Attention later avoids forcing all source information into one vector.

## Variable Length và Padding

Batching sequences of different lengths often uses padding. Model/loss must mask padded positions.

If padding accidentally participates attention/loss, model learns artifacts and metrics wrong.

Sequence batching also uses bucketing by length to reduce wasted compute.

## Position Matters

RNN inherently processes order sequentially. Pure self-attention without positional information is permutation-equivariant: reorder tokens and same set interactions reorder correspondingly.

Transformer therefore injects positional information explicitly: sinusoidal, learned position embeddings, relative bias, RoPE, ALiBi etc.

Position encoding is not optional decoration; it tells model about sequence geometry/order.

## Causal vs Bidirectional Context

Causal model at position `t` can see only `x_{<t}`. Necessary for autoregressive generation without future leakage.

Bidirectional encoder can see left and right context, useful for understanding/classification/masked modeling.

Attention mask defines information flow.

A model architecture can be similar but masking objective changes semantics profoundly.

## Teacher Forcing

During autoregressive training, model often receives ground-truth previous token rather than its own generated prediction:

\[
P(x_t\mid x_{<t}^{true})
\]

At inference it conditions on generated history. Errors can accumulate — **exposure bias**.

Scheduled sampling was proposed to bridge gap, though modern language models largely still use teacher-forced next-token training and address behavior through scale/objectives/inference methods.

## Sequence-to-Sequence

Translation input length and output length differ. Encoder builds source representations; decoder generates target autoregressively conditioned on source.

Early seq2seq compressed source into final RNN state, creating bottleneck. Attention let decoder access all encoder states dynamically.

This historical path leads directly to Transformer.

## Temporal Dependencies

Dependencies differ timescale:

- phoneme depends nearby audio frames;
- grammar may span clauses;
- document reference spans paragraphs;
- time-series seasonality spans days/months.

Model needs receptive context matching task.

RNN theoretically carries indefinite history but practical gradient/memory decay. CNN sequence models get finite receptive field unless dilated/deep. Attention directly connects distant positions but quadratic cost in vanilla form.

## State-Space Models

Classical state-space:

\[
h_t=Ah_{t-1}+Bx_t
\]

\[
y_t=Ch_t+Dx_t
\]

Kalman filters add stochastic assumptions. Modern structured state-space neural models (S4/Mamba-like families) revisit recurrence/convolution with efficient long-sequence computation.

Sequence modeling landscape is broader than RNN vs Transformer.

## Time Series vs Language

Both are sequences nhưng assumptions differ.

Time series may have real timestamps, irregular sampling, known seasonality, exogenous variables and continuous values.

Language tokens are discrete and order-relative; future token prediction is natural objective.

Do not blindly reuse NLP architectures without modeling time semantics.

## Sequence Evaluation

Token accuracy can miss sequence quality. Translation uses BLEU/COMET-like metrics; speech uses WER; forecasting uses MAE/RMSE/probabilistic scores; generation needs human/model-based evaluation.

Error compounds across sequence, so per-step metric and sequence-level metric can differ.

## Mental Model

> Sequence modeling = represent information distributed across ordered positions, decide which past/future context each output may use, and model dependencies across appropriate timescales.

## Common Misconceptions

### “RNN remembers whole sequence”

Hidden state has finite capacity and long-range information can degrade.

### “Transformer knows order automatically because input tokens are ordered in array”

Self-attention operation needs positional signal/mask to distinguish order structurally.

### “All sequence tasks should be autoregressive”

Classification/tagging/denoising/forecasting may use different objectives/context.

### “Time series is just text with numbers”

Temporal scale, continuous values, irregular time and causal covariates create different modeling constraints.

## Knowledge Connection

Sequence models connect classical [Markov Decision/State ideas](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md), [Probabilistic Reasoning](../03_knowledge_and_reasoning/04_probabilistic_reasoning.md) and Neural Networks.

Xem tiếp: [RNN, LSTM and GRU](./02_rnn_lstm_gru.md).