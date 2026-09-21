# RNN, LSTM và GRU: học trạng thái qua thời gian

Recurrent Neural Network (RNN / 순환 신경망) xử lý sequence bằng cách reuse cùng transition function qua timesteps. Thay vì mỗi position độc lập, model duy trì hidden state mang information từ quá khứ.

RNN là bước lịch sử quan trọng vì nó biến variable-length sequence thành stateful differentiable computation. LSTM và GRU ra đời để giảm difficulty của long-term gradient flow.

## Vanilla RNN

Update:

\[
h_t=\phi(W_{xh}x_t+W_{hh}h_{t-1}+b_h)
\]

Output:

\[
y_t=g(W_{hy}h_t+b_y)
\]

Same weights `W` reused mọi timestep → parameter sharing across time.

## Unrolling through time

RNN có thể unroll:

```text
x1 → [cell] → h1
       ↓
x2 → [cell] → h2
       ↓
x3 → [cell] → h3
```

Mathematically graph depth proportional sequence length. Backpropagation phải traverse unrolled graph — **Backpropagation Through Time (BPTT)**.

## Vanishing gradient trong RNN

Gradient qua many timesteps chứa repeated products involving recurrent Jacobian:

\[
\frac{\partial h_t}{\partial h_k}
=\prod_{i=k+1}^{t}\frac{\partial h_i}{\partial h_{i-1}}
\]

Nếu spectral effects/activation derivatives shrink, gradient vanish; nếu grow, explode.

Do đó vanilla RNN khó học long-range dependencies.

## Truncated BPTT

Long sequence training có thể backprop chỉ `K` timesteps thay vì toàn history.

Hidden state vẫn carry forward, nhưng gradient graph detach periodically.

Trade-off:

```text
lower memory/compute
↔
cannot assign credit through dependencies longer than truncation window directly
```

## LSTM: tạo memory path có gates

Long Short-Term Memory (LSTM / 장단기 메모리) có cell state `c_t` và gates.

Forget gate:

\[
f_t=\sigma(W_f[x_t,h_{t-1}]+b_f)
\]

Input gate:

\[
i_t=\sigma(W_i[x_t,h_{t-1}]+b_i)
\]

Candidate:

\[
\tilde c_t=\tanh(W_c[x_t,h_{t-1}]+b_c)
\]

Cell update:

\[
c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t
\]

Output gate:

\[
o_t=\sigma(W_o[x_t,h_{t-1}]+b_o)
\]

Hidden:

\[
h_t=o_t\odot\tanh(c_t)
\]

## Vì sao LSTM giúp gradient flow?

Cell state update có additive path:

\[
c_t=f_t\odot c_{t-1}+...
\]

Derivative:

\[
\frac{\partial c_t}{\partial c_{t-1}}=f_t
\]

Nếu forget gate gần `1`, information/gradient có thể flow qua nhiều steps ít bị repeated nonlinear squashing hơn vanilla RNN.

LSTM không “giải quyết hoàn toàn” long dependency, nhưng cải thiện đáng kể.

## Gate interpretation

- forget gate: bao nhiêu old memory giữ lại;
- input gate: bao nhiêu new candidate viết vào memory;
- output gate: bao nhiêu cell state expose ra hidden.

Gates learned, không hand-coded semantic.

## GRU

Gated Recurrent Unit (GRU / 게이트 순환 유닛) đơn giản hóa LSTM, merge memory/hidden.

Update gate:

\[
z_t=\sigma(W_z[x_t,h_{t-1}])
\]

Reset gate:

\[
r_t=\sigma(W_r[x_t,h_{t-1}])
\]

Candidate:

\[
\tilde h_t=\tanh(W_h[x_t,r_t\odot h_{t-1}])
\]

Update:

\[
h_t=(1-z_t)\odot h_{t-1}+z_t\odot\tilde h_t
\]

GRU fewer parameters/gates; performance depends task/data.

## Bidirectional RNN

Nếu task cho phép future context, run one RNN forward và one backward:

\[
h_t=[\overrightarrow h_t;\overleftarrow h_t]
\]

Useful tagging/speech encoders.

Không dùng directly cho causal generation nếu future token unavailable.

## Stacked RNN

Multiple recurrent layers:

```text
sequence
→ RNN layer 1
→ RNN layer 2
→ ...
```

Depth across time + layers makes optimization harder. Dropout/residual/norm variants help.

## Sequence bottleneck

Many-to-one model dùng final hidden state `h_T` để summarize entire input. Long sequence information phải compress vào fixed vector.

Early seq2seq translation suffered this bottleneck. Attention solves by allowing decoder access all encoder states rather than one final state.

## RNN strengths

RNN processes streaming input incrementally with constant state size per layer. Inference per new timestep can be efficient without storing all past activations (beyond state).

This is useful edge/online time-series/audio contexts.

## RNN limitations vs Transformer

Sequential dependency prevents parallel computation across timesteps during training. Transformer computes positions mostly parallel.

Long-range path length in RNN is `O(T)` recurrent steps; self-attention connects positions in one layer.

This compute/optimization advantage drove Transformer dominance in NLP.

## RNN vẫn còn giá trị

RNN/LSTM/GRU remain useful for:

- small/medium time-series datasets;
- streaming low-latency models;
- embedded devices;
- stateful sequence processing;
- domains where recurrence is natural.

Modern state-space models also revive recurrent-style efficient inference with better long-range design.

## Encoder–Decoder with RNN

Encoder processes source sequence to states. Decoder recurrently generates target, conditioned on encoder summary/states.

Adding attention was the key bridge to modern architecture.

Xem [Encoder–Decoder Models](./03_encoder_decoder_models.md) và [Attention](./04_attention.md).

## Mental Model

```text
RNN  = continuously update compressed state
LSTM = state + learned gates controlling write/keep/read
GRU  = simplified gated state update
```

## Common Misconceptions

### “LSTM remembers indefinitely”

Gates improve retention, but capacity/noise/optimization still limit long-range memory.

### “GRU always faster and therefore better”

Fewer gates/parameters often cheaper, but performance task-dependent.

### “RNN obsolete because Transformer exists”

Transformer dominates many large sequence tasks, but recurrence remains useful under streaming/compute constraints.

### “Hidden state is human-readable memory”

It is distributed learned vector state, not explicit symbolic memory.

## Knowledge Connection

RNN applies [Backpropagation](../05_neural_networks/04_backpropagation.md), [Gradient Clipping](../05_neural_networks/05_gradient_descent_and_optimizers.md) and sequence state ideas. Attention emerges specifically because fixed recurrent state becomes bottleneck.