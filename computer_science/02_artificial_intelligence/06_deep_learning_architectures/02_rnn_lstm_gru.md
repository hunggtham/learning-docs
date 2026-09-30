# RNN, LSTM và GRU: học trạng thái qua thời gian

> **Mạch đọc:** Đặt **RNN, LSTM và GRU: học trạng thái qua thời gian** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Vanilla RNN** sang **Unrolling through thời gian (time / 시간)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Recurrent Neural mạng (network / 네트워크) xử lý chuỗi (sequence / 시퀀스) bằng cách reuse cùng chuyển tiếp (transition / 전이) hàm (function / 함수) qua timesteps. Thay vì mỗi position độc lập, mô hình (model / 모델) duy trì hidden trạng thái (state / 상태) mang thông tin (information / 정보) từ quá khứ.

RNN là bước lịch sử quan trọng vì nó biến variable-length chuỗi (sequence / 시퀀스) thành stateful differentiable computation. LSTM và GRU ra đời để giảm difficulty của long-term độ dốc (gradient / 기울기) luồng (flow / 흐름).

## Vanilla RNN

Cập nhật (update / 업데이트):

\[
h_t=\phi(W_{xh}x_t+W_{hh}h_{t-1}+b_h)
\]

Đầu ra (output / 출력):

\[
y_t=g(W_{hy}h_t+b_y)
\]

Same weights `W` reused mọi timestep → parameter sharing across thời gian (time / 시간).

## Unrolling through thời gian (time / 시간)

RNN có thể unroll:

```text
x1 → [cell] → h1
       ↓
x2 → [cell] → h2
       ↓
x3 → [cell] → h3
```

Mathematically đồ thị (graph / 그래프) độ sâu (depth / 깊이) proportional chuỗi (sequence / 시퀀스) length. Backpropagation phải traverse unrolled đồ thị (graph / 그래프) — **Backpropagation Through thời gian (time / 시간) (BPTT)**.

## Vanishing độ dốc (gradient / 기울기) trong RNN

Độ dốc (gradient / 기울기) qua many timesteps chứa repeated products involving recurrent Jacobian:

\[
\frac{\partial h_t}{\partial h_k}
=\prod_{i=k+1}^{t}\frac{\partial h_i}{\partial h_{i-1}}
\]

Nếu spectral effects/activation derivatives shrink, độ dốc (gradient / 기울기) vanish; nếu grow, explode.

Do đó vanilla RNN khó học long-range dependencies.

## Truncated BPTT

Long chuỗi (sequence / 시퀀스) huấn luyện (training / 학습) có thể backprop chỉ `K` timesteps thay vì toàn lịch sử (history / 이력).

Hidden trạng thái (state / 상태) vẫn carry forward, nhưng độ dốc (gradient / 기울기) đồ thị (graph / 그래프) detach periodically.

Sự đánh đổi (trade-off / 트레이드오프):

```text
lower memory/compute
↔
cannot assign credit through dependencies longer than truncation window directly
```

## LSTM: tạo bộ nhớ (memory / 메모리) đường dẫn (path / 경로) có gates

Long Short-Term bộ nhớ (memory / 메모리) có cell trạng thái (state / 상태) `c_t` và gates.

Forget gate:

\[
f_t=\sigma(W_f[x_t,h_{t-1}]+b_f)
\]

Đầu vào (input / 입력) gate:

\[
i_t=\sigma(W_i[x_t,h_{t-1}]+b_i)
\]

Candidate:

\[
\tilde c_t=\tanh(W_c[x_t,h_{t-1}]+b_c)
\]

Cell cập nhật (update / 업데이트):

\[
c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t
\]

Đầu ra (output / 출력) gate:

\[
o_t=\sigma(W_o[x_t,h_{t-1}]+b_o)
\]

Hidden:

\[
h_t=o_t\odot\tanh(c_t)
\]

## Vì sao LSTM giúp độ dốc (gradient / 기울기) luồng (flow / 흐름)?

Cell trạng thái (state / 상태) cập nhật (update / 업데이트) có additive đường dẫn (path / 경로):

\[
c_t=f_t\odot c_{t-1}+...
\]

Derivative:

\[
\frac{\partial c_t}{\partial c_{t-1}}=f_t
\]

Nếu forget gate gần `1`, thông tin (information / 정보)/độ dốc (gradient / 기울기) có thể luồng (flow / 흐름) qua nhiều steps ít bị repeated nonlinear squashing hơn vanilla RNN.

LSTM không “giải quyết hoàn toàn” long phụ thuộc (dependency / 의존성), nhưng cải thiện đáng kể.

## Gate interpretation

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

- forget gate: bao nhiêu old memory giữ lại;
- input gate: bao nhiêu new candidate viết vào memory;
- output gate: bao nhiêu cell state expose ra hidden.

Gates learned, không hand-coded ngữ nghĩa (semantic / 의미적).

## GRU

Gated Recurrent đơn vị (unit / 단위) đơn giản hóa LSTM, merge bộ nhớ (memory / 메모리)/hidden.

Cập nhật (update / 업데이트) gate:

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

Cập nhật (update / 업데이트):

\[
h_t=(1-z_t)\odot h_{t-1}+z_t\odot\tilde h_t
\]

GRU fewer parameters/gates; hiệu năng (performance / 성능) depends tác vụ (task / 작업)/dữ liệu (data / 데이터).

## Bidirectional RNN

Nếu tác vụ (task / 작업) cho phép future ngữ cảnh (context / 맥락), run one RNN forward và one backward:

\[
h_t=[\overrightarrow h_t;\overleftarrow h_t]
\]

Useful tagging/speech encoders.

Không dùng directly cho nhân quả (causal / 인과적) generation nếu future đơn vị từ (token / 토큰) unavailable.

## Stacked RNN

Multiple recurrent layers:

```text
sequence
→ RNN layer 1
→ RNN layer 2
→ ...
```

Độ sâu (depth / 깊이) across thời gian (time / 시간) + layers makes tối ưu hóa (optimization / 최적화) harder. Dropout/residual/norm variants help.

## Chuỗi (sequence / 시퀀스) bottleneck

Many-to-one mô hình (model / 모델) dùng final hidden trạng thái (state / 상태) `h_T` để summarize entire đầu vào (input / 입력). Long chuỗi (sequence / 시퀀스) thông tin (information / 정보) phải compress vào fixed véc-tơ (vector / 벡터).

Early seq2seq translation suffered this bottleneck. Attention solves by allowing decoder truy cập (access / 접근) all encoder states rather than one final trạng thái (state / 상태).

## RNN strengths

RNN processes streaming đầu vào (input / 입력) incrementally with constant trạng thái (state / 상태) kích thước (size / 크기) per tầng (layer / 계층). suy luận (inference / 추론) per new timestep can be efficient without storing all past activations (beyond state).

This is useful edge/online time-series/audio contexts.

## RNN limitations vs Transformer

Sequential phụ thuộc (dependency / 의존성) prevents parallel computation across timesteps during huấn luyện (training / 학습). Transformer computes positions mostly parallel.

Long-range đường dẫn (path / 경로) length in RNN is `O(T)` recurrent steps; self-attention connects positions in one tầng (layer / 계층).

This compute/tối ưu hóa (optimization / 최적화) advantage drove Transformer dominance in NLP.

## RNN vẫn còn giá trị

RNN/LSTM/GRU remain useful for:

- small/medium time-series datasets;
- streaming low-latency các mô hình (models / 모델들);
- embedded devices;
- stateful chuỗi (sequence / 시퀀스) processing;
- domains where recurrence is natural.

Hiện đại (modern / 현대적) state-space các mô hình (models / 모델들) also revive recurrent-style efficient suy luận (inference / 추론) with better long-range thiết kế (design / 설계).

## Encoder–Decoder with RNN

Encoder processes nguồn (source / 소스) chuỗi (sequence / 시퀀스) to states. Decoder recurrently generates mục tiêu (target / 대상), conditioned on encoder summary/states.

Adding attention was the key cầu nối (bridge / 브리지) to hiện đại (modern / 현대적) kiến trúc (architecture / 아키텍처).

Xem [Encoder–Decoder Models](./03_encoder_decoder_models.md) và [Attention](./04_attention.md).

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
RNN  = continuously update compressed state
LSTM = state + learned gates controlling write/keep/read
GRU  = simplified gated state update
```

## Dùng chung (common / 공통) Misconceptions

### “LSTM remembers indefinitely”

Gates improve retention, but sức chứa (capacity / 용량)/noise/tối ưu hóa (optimization / 최적화) still limit long-range bộ nhớ (memory / 메모리).

### “GRU always faster and therefore better”

Fewer gates/parameters often cheaper, but hiệu năng (performance / 성능) task-dependent.

### “RNN obsolete because Transformer exists”

Transformer dominates many large chuỗi (sequence / 시퀀스) tasks, but recurrence remains useful under streaming/compute các ràng buộc (constraints / 제약조건들).

### “Hidden trạng thái (state / 상태) is human-readable bộ nhớ (memory / 메모리)”

It is phân tán (distributed / 분산) learned véc-tơ (vector / 벡터) trạng thái (state / 상태), not tường minh (explicit / 명시적) symbolic bộ nhớ (memory / 메모리).

## Liên kết kiến thức (knowledge connection / 지식 연결)

RNN applies [Backpropagation](../05_neural_networks/04_backpropagation.md), [Gradient Clipping](../05_neural_networks/05_gradient_descent_and_optimizers.md) and sequence state ideas. Attention emerges specifically because fixed recurrent state becomes bottleneck.
