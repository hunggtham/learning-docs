# Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들): dữ liệu có thứ tự cần mô hình (model / 모델) khác gì?

> **Mạch đọc:** Đặt **chuỗi (sequence / 시퀀스) các mô hình (models / 모델들): dữ liệu có thứ tự cần mô hình (model / 모델) khác gì?** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **chuỗi (sequence / 시퀀스) notation** sang **Markov giả định (assumption / 가정)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Chuỗi (sequence / 시퀀스) dữ liệu (data / 데이터) khác fixed unordered tính năng (feature / 기능) véc-tơ (vector / 벡터) vì **thứ tự và ngữ cảnh (context / 맥락)** mang meaning. Câu `dog bites man` khác `man bites dog`; sensor readings cùng values nhưng thứ tự (order / 순서) khác biểu diễn dynamics khác. Vì vậy chuỗi (sequence / 시퀀스) mô hình (model / 모델) phải xử lý variable length, phụ thuộc (dependency / 의존성) qua positions và đôi khi nhân quả (causal / 인과적) direction.

Trước RNN và Transformer, cần hiểu chuỗi (sequence / 시퀀스) modeling bài toán (problem / 문제) itself.

## Chuỗi (sequence / 시퀀스) notation

Một chuỗi (sequence / 시퀀스):

\[
x_{1:T}=(x_1,x_2,...,x_T)
\]

Đầu ra (output / 출력) có thể:

- chuỗi (sequence / 시퀀스) → one: sentiment/classification;
- one → chuỗi (sequence / 시퀀스): conditional generation;
- chuỗi (sequence / 시퀀스) → chuỗi (sequence / 시퀀스) aligned: tagging;
- chuỗi (sequence / 시퀀스) → chuỗi (sequence / 시퀀스) unaligned: translation;
- autoregressive next-step prediction.

Kiến trúc (architecture / 아키텍처) phụ thuộc đầu ra (output / 출력) cấu trúc (structure / 구조).

## Markov giả định (assumption / 가정)

Simplest chuỗi (sequence / 시퀀스) mô hình (model / 모델) assume future phụ thuộc limited past.

First-order Markov:

\[
P(x_t\mid x_{1:t-1})=P(x_t\mid x_{t-1})
\]

This drastically simplifies modeling nhưng bỏ long-range dependencies.

Higher-order increases ngữ cảnh (context / 맥락) nhưng trạng thái (state / 상태) combinations explode.

RNN attempts learn compressed trạng thái (state / 상태) summarizing arbitrary lịch sử (history / 이력).

## Autoregressive Factorization

Any joint chuỗi (sequence / 시퀀스) phân phối (distribution / 분포) can factor:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Ngôn ngữ (language / 언어) các mô hình (models / 모델들) use this principle. Transformer changed cơ chế (mechanism / 메커니즘) computing ngữ cảnh (context / 맥락), not this xác suất (probability / 확률) factorization.

Autoregressive generation repeatedly:

```text
context → predict distribution next token
sample/select token
append
repeat
```

## Chuỗi (sequence / 시퀀스) trạng thái (state / 상태)

A recurrent mô hình (model / 모델) maintains hidden trạng thái (state / 상태):

\[
h_t=f(h_{t-1},x_t)
\]

`h_t` tries compress relevant lịch sử (history / 이력) `x_{1:t}`.

This is elegant but creates thông tin (information / 정보) bottleneck: long lịch sử (history / 이력) must luồng (flow / 흐름) through fixed-size trạng thái (state / 상태).

Attention later avoids forcing all nguồn (source / 소스) thông tin (information / 정보) into one véc-tơ (vector / 벡터).

## Variable Length và Padding

Batching sequences of different lengths often uses padding. mô hình (model / 모델)/mất mát (loss / 손실) must mask padded positions.

If padding accidentally participates attention/mất mát (loss / 손실), mô hình (model / 모델) learns artifacts and metrics wrong.

Chuỗi (sequence / 시퀀스) batching also uses bucketing by length to reduce wasted compute.

## Position Matters

RNN inherently processes thứ tự (order / 순서) sequentially. Pure self-attention without positional thông tin (information / 정보) is permutation-equivariant: reorder tokens and same set interactions reorder correspondingly.

Transformer therefore injects positional thông tin (information / 정보) explicitly: sinusoidal, learned position embeddings, relative độ lệch (bias / 편향), RoPE, ALiBi etc.

Position encoding is not optional decoration; it tells mô hình (model / 모델) about chuỗi (sequence / 시퀀스) hình học (geometry / 기하학)/thứ tự (order / 순서).

## Nhân quả (causal / 인과적) vs Bidirectional ngữ cảnh (context / 맥락)

Nhân quả (causal / 인과적) mô hình (model / 모델) at position `t` can see only `x_{<t}`. Necessary for autoregressive generation without future leakage.

Bidirectional encoder can see left and right ngữ cảnh (context / 맥락), useful for understanding/classification/masked modeling.

Attention mask defines thông tin (information / 정보) luồng (flow / 흐름).

A mô hình (model / 모델) kiến trúc (architecture / 아키텍처) can be similar but masking mục tiêu (objective / 목표) changes ngữ nghĩa (semantics / 의미론) profoundly.

## Teacher Forcing

During autoregressive huấn luyện (training / 학습), mô hình (model / 모델) often receives ground-truth previous đơn vị từ (token / 토큰) rather than its own generated prediction:

\[
P(x_t\mid x_{<t}^{true})
\]

At suy luận (inference / 추론) it conditions on generated lịch sử (history / 이력). Errors can accumulate — **exposure độ lệch (bias / 편향)**.

Scheduled sampling was proposed to cầu nối (bridge / 브리지) gap, though hiện đại (modern / 현대적) ngôn ngữ (language / 언어) các mô hình (models / 모델들) largely still use teacher-forced next-token huấn luyện (training / 학습) and address hành vi (behavior / 동작) through quy mô (scale / 규모)/objectives/suy luận (inference / 추론) methods.

## Sequence-to-Sequence

Translation đầu vào (input / 입력) length and đầu ra (output / 출력) length differ. Encoder builds nguồn (source / 소스) representations; decoder generates mục tiêu (target / 대상) autoregressively conditioned on nguồn (source / 소스).

Early seq2seq compressed nguồn (source / 소스) into final RNN trạng thái (state / 상태), creating bottleneck. Attention let decoder truy cập (access / 접근) all encoder states dynamically.

This historical đường dẫn (path / 경로) leads directly to Transformer.

## Temporal Dependencies

Dependencies differ timescale:

- phoneme depends nearby audio frames;
- grammar may span clauses;
- document tham chiếu (reference / 참조) spans paragraphs;
- time-series seasonality spans days/months.

Mô hình (model / 모델) needs receptive ngữ cảnh (context / 맥락) matching tác vụ (task / 작업).

RNN theoretically carries indefinite lịch sử (history / 이력) but practical độ dốc (gradient / 기울기)/bộ nhớ (memory / 메모리) decay. CNN chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) get finite receptive trường dữ liệu (field / 필드) unless dilated/deep. Attention directly connects distant positions but quadratic chi phí (cost / 비용) in vanilla form.

## State-Space các mô hình (models / 모델들)

Classical state-space:

\[
h_t=Ah_{t-1}+Bx_t
\]

\[
y_t=Ch_t+Dx_t
\]

Kalman filters add stochastic các giả định (assumptions / 가정들). hiện đại (modern / 현대적) structured state-space neural các mô hình (models / 모델들) revisit recurrence/convolution with efficient long-sequence computation.

Chuỗi (sequence / 시퀀스) modeling landscape is broader than RNN vs Transformer.

## Thời gian (time / 시간) Series vs ngôn ngữ (language / 언어)

Both are sequences nhưng các giả định (assumptions / 가정들) differ.

Thời gian (time / 시간) series may have real timestamps, irregular sampling, known seasonality, exogenous variables and continuous values.

Ngôn ngữ (language / 언어) tokens are discrete and order-relative; future đơn vị từ (token / 토큰) prediction is natural mục tiêu (objective / 목표).

Do not blindly reuse NLP architectures without modeling thời gian (time / 시간) ngữ nghĩa (semantics / 의미론).

## Chuỗi (sequence / 시퀀스) Evaluation

Đơn vị từ (token / 토큰) accuracy can miss chuỗi (sequence / 시퀀스) chất lượng (quality / 품질). Translation uses BLEU/COMET-like metrics; speech uses WER; forecasting uses MAE/RMSE/probabilistic scores; generation needs human/model-based evaluation.

Lỗi (error / 오류) compounds across chuỗi (sequence / 시퀀스), so per-step chỉ số (metric / 지표) and sequence-level chỉ số (metric / 지표) can differ.

## Mô hình tư duy (mental model / 사고 모델)

> chuỗi (sequence / 시퀀스) modeling = represent thông tin (information / 정보) phân tán (distributed / 분산) across ordered positions, decide which past/future ngữ cảnh (context / 맥락) each đầu ra (output / 출력) may use, and mô hình (model / 모델) dependencies across appropriate timescales.

## Dùng chung (common / 공통) Misconceptions

### “RNN remembers whole chuỗi (sequence / 시퀀스)”

Hidden trạng thái (state / 상태) has finite sức chứa (capacity / 용량) and long-range thông tin (information / 정보) can degrade.

### “Transformer knows thứ tự (order / 순서) automatically because đầu vào (input / 입력) tokens are ordered in array”

Self-attention thao tác (operation / 연산) needs positional tín hiệu (signal / 신호)/mask to distinguish thứ tự (order / 순서) structurally.

### “All chuỗi (sequence / 시퀀스) tasks should be autoregressive”

Classification/tagging/denoising/forecasting may use different objectives/ngữ cảnh (context / 맥락).

### “thời gian (time / 시간) series is just văn bản (text / 텍스트) with numbers”

Temporal quy mô (scale / 규모), continuous values, irregular thời gian (time / 시간) and nhân quả (causal / 인과적) covariates create different modeling các ràng buộc (constraints / 제약조건들).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) connect classical [Markov Decision/State ideas](../02_search_reasoning_and_planning/06_decision_making_under_uncertainty.md), [Probabilistic Reasoning](../03_knowledge_and_reasoning/04_probabilistic_reasoning.md) and Neural Networks.

Xem tiếp: [RNN, LSTM and GRU](./02_rnn_lstm_gru.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 convolutional neural networks](./00_convolutional_neural_networks.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
