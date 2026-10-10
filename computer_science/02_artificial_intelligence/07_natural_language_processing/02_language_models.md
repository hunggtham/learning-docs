# Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Language models**. Route đi từ sequence probability/chain rule → n-gram limits → neural next-token modeling → perplexity/context → generation and calibration, để xác suất chuỗi nối với hành vi sinh văn bản.

Ngôn ngữ (language / 언어) mô hình (model / 모델) gán xác suất (probability / 확률) cho chuỗi (sequence / 시퀀스) hoặc dự đoán đơn vị từ (token / 토큰) dựa trên ngữ cảnh (context / 맥락). Đây là cốt lõi (core / 핵심) lớp trừu tượng (abstraction / 추상화) đứng sau autocomplete, speech decoding, machine translation và Large ngôn ngữ (language / 언어) các mô hình (models / 모델들).

Điểm quan trọng: ngôn ngữ (language / 언어) mô hình (model / 모델) không trực tiếp optimize “truth” hay “lập luận (reasoning / 추론)”. mục tiêu (objective / 목표) cơ bản là mô hình (model / 모델) phân phối (distribution / 분포) của observed ngôn ngữ (language / 언어). năng lực (capability / 역량) khác xuất hiện vì để predict ngôn ngữ (language / 언어) tốt ở quy mô (scale / 규모) lớn, mô hình (model / 모델) phải learn nhiều cấu trúc (structure / 구조) về cú pháp (syntax / 문법), ngữ nghĩa (semantics / 의미론), kiến thức (knowledge / 지식) và patterns of lập luận (reasoning / 추론) — nhưng mục tiêu (objective / 목표) và năng lực (capability / 역량) không đồng nhất.

## Joint xác suất (probability / 확률) và chuỗi (chain / 사슬) quy tắc (rule / 규칙)

Với chuỗi (sequence / 시퀀스):

\[
x_{1:T}=(x_1,...,x_T)
\]

Chuỗi (chain / 사슬) quy tắc (rule / 규칙):

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Không cần Markov giả định (assumption / 가정) để factorization đúng. Difficulty là estimate each conditional phân phối (distribution / 분포).

Autoregressive ngôn ngữ (language / 언어) mô hình (model / 모델) học:

\[
P_\theta(x_t\mid x_{<t})
\]

Chain rule biến xác suất của cả chuỗi thành các điều kiện theo thời điểm; n-gram tiếp theo là một xấp xỉ hữu hạn cho các điều kiện đó.

## n-gram ngôn ngữ (language / 언어) các mô hình (models / 모델들)

Approximate ngữ cảnh (context / 맥락) limited:

\[
P(x_t\mid x_{<t})\approx P(x_t\mid x_{t-n+1:t-1})
\]

Estimate counts:

\[
P(w_t\mid h)=\frac{count(h,w_t)}{count(h)}
\]

Sparse dữ liệu (data / 데이터) causes zero probabilities for unseen n-grams.

Smoothing methods như Laplace, Good-Turing, Kneser-Ney redistribute xác suất (probability / 확률) mass. Kneser-Ney đặc biệt uses continuation statistics and remains a landmark classical LM technique.

N-gram làm rõ lợi ích và giới hạn của context hữu hạn; neural LM thay thế các context rời rạc bằng biểu diễn liên tục để chia sẻ thống kê.

## Why Neural ngôn ngữ (language / 언어) các mô hình (models / 모델들)?

n-gram treats contexts mostly discrete. `the cat sat` and `the dog sat` share little unless tường minh (explicit / 명시적) backoff.

Neural LM maps words/tokens into embeddings and represents ngữ cảnh (context / 맥락) continuously, allowing statistical sharing across similar contexts.

Early feed-forward LM:

```text
fixed previous tokens
→ embeddings
→ MLP
→ softmax next word
```

RNN removed fixed ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우). Transformer improved long-range truy cập (access / 접근) and parallel huấn luyện (training / 학습).

Neural LM học từ embedding và context liên tục; maximum likelihood formalize mục tiêu tối ưu xác suất trên corpus.

## Maximum Likelihood huấn luyện (training / 학습)

Given corpus, maximize:

\[
\sum_t\log P_\theta(x_t\mid x_{<t})
\]

Equivalent minimize negative log-likelihood / cross-entropy:

\[
L=-\frac1T\sum_t\log P_\theta(x_t\mid x_{<t})
\]

Teacher forcing gives mô hình (model / 모델) true previous tokens during huấn luyện (training / 학습).

Maximum likelihood tương đương giảm negative log-likelihood; perplexity chuyển loss này thành thước đo dễ diễn giải hơn về độ bất định.

## Perplexity

If average cross-entropy in natural log is `H`:

\[
PPL=e^H
\]

If log cơ sở (base / 기반) 2:

\[
PPL=2^{H_2}
\]

Intuition: effective branching factor under mô hình (model / 모델).

Lower perplexity on same tokenization/kiểm thử (test / 테스트) phân phối (distribution / 분포) usually better next-token modeling.

But perplexity cannot compare cleanly across different tokenizers because đơn vị (unit / 단위) differs. Lower PPL also does not guarantee better instruction following/factuality.

Perplexity đo chất lượng dự đoán trên cùng tokenizer và phân phối; masked modeling dùng mục tiêu khác để tận dụng cả hai phía của context.

## Masked ngôn ngữ (language / 언어) Modeling

BERT-like mục tiêu (objective / 목표) masks tokens and predicts them using both left/right ngữ cảnh (context / 맥락):

\[
P(x_i\mid x_{\setminus i})
\]

This is not autoregressive joint factorization in same direct way. It learns bidirectional representations excellent for encoding tasks.

Masked LM nhìn hai phía để học biểu diễn; causal LM áp đặt mask nhân quả khi cần sinh từng token theo thứ tự.

## Nhân quả (causal / 인과적) ngôn ngữ (language / 언어) Modeling

GPT-style mục tiêu (objective / 목표) predicts each đơn vị từ (token / 토큰) using only previous tokens. nhân quả (causal / 인과적) mask preserves:

\[
P(x_t\mid x_{<t})
\]

Advantage: mô hình (model / 모델) can directly generate by ancestral sampling.

Causal LM sinh bằng cách lấy mẫu từ lịch sử đã có; prefix/seq2seq mở rộng điều kiện bằng một chuỗi nguồn riêng.

## Prefix / Seq2Seq ngôn ngữ (language / 언어) Modeling

Encoder-decoder các mô hình (models / 모델들) điều kiện (condition / 조건) đầu ra (output / 출력) chuỗi (sequence / 시퀀스) on nguồn (source / 소스):

\[
P(y\mid x)=\prod_tP(y_t\mid y_{<t},x)
\]

T5 reframes many NLP tasks as text-to-text conditional generation.

Seq2seq mô hình hóa đầu ra có điều kiện trên nguồn; sampling quyết định cách biến phân phối token thành một chuỗi cụ thể.

## Sampling from ngôn ngữ (language / 언어) mô hình (model / 모델)

Given logits `z`, temperature:

\[
p_i=softmax(z_i/T)
\]

- `T<1`: sharper;
- `T>1`: flatter.

### Greedy

Pick max xác suất (probability / 확률) each step. Deterministic but can be repetitive/suboptimal sequence-level.

### Top-k

Keep k highest-probability tokens, renormalize.

### Top-p / Nucleus

Choose smallest đơn vị từ (token / 토큰) set whose cumulative xác suất (probability / 확률) ≥ `p`, then mẫu (sample / 표본). Candidate set adapts phân phối (distribution / 분포) bất định (uncertainty / 불확실성).

Sampling cấu hình (configuration / 구성) affects style/diversity, not mô hình (model / 모델) kiến thức (knowledge / 지식) itself.

Sampling thay đổi độ sắc và độ đa dạng của đầu ra nhưng không thêm kiến thức; exposure bias giải thích vì sao lỗi có thể lan khi sinh tự hồi quy.

## Exposure độ lệch (bias / 편향)

Huấn luyện (training / 학습) conditions on true lịch sử (history / 이력); generation conditions on own outputs. One lỗi (error / 오류) changes future ngữ cảnh (context / 맥락) and can cascade.

This mismatch is inherent tiêu chuẩn (standard / 표준) autoregressive maximum-likelihood huấn luyện (training / 학습).

Instruction tuning/RL-based post-training can thay đổi (change / 변경) hành vi (behavior / 동작), but does not remove autoregressive nature.

Exposure bias là chênh lệch giữa lịch sử đúng khi huấn luyện và lịch sử do model tự sinh; degeneration là một biểu hiện thường gặp của chênh lệch và decoding.

## Degeneration

Pure maximization or poor sampling can cause repetition, generic văn bản (text / 텍스트) or loops.

Reasons include phân phối (distribution / 분포) shape, huấn luyện (training / 학습) mục tiêu (objective / 목표) and decoding chiến lược (strategy / 전략). Repetition penalties can help but are heuristic and may distort phân phối (distribution / 분포).

Degeneration cho thấy đầu ra trôi vào lặp hoặc văn bản chung chung; cần phân biệt hiện tượng đó với việc model đang tra cứu một cơ sở dữ liệu.

## Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ kiến thức (knowledge / 지식) cơ sở dữ liệu (database / 데이터베이스)

Parameters encode phân tán (distributed / 분산) statistical associations. Querying a fact is not chính xác (exact / 정확한) key lookup.

Consequences:

- kiến thức (knowledge / 지식) can be approximate;
- conflicting facts coexist;
- recency limited by huấn luyện (training / 학습);
- provenance absent;
- rare facts unreliable.

Bên ngoài (external / 외부) retrieval (RAG) adds tường minh (explicit / 명시적) nguồn (source / 소스) truy cập (access / 접근).

Language model lưu các liên hệ thống kê phân tán, không phải bảng tra cứu có provenance; giới hạn này dẫn trực tiếp tới phân biệt model với truth.

## Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ Truth mô hình (model / 모델)

Huấn luyện (training / 학습) corpus contains true/false fiction/speculation. Next-token likelihood rewards linguistic plausibility under corpus phân phối (distribution / 분포), not direct world xác minh (verification / 확인).

This explains hallucination rủi ro (risk / 위험) at mục tiêu (objective / 목표) mức (level / 수준).

Khả năng nói trôi chảy không bảo đảm mệnh đề đúng; in-context learning cho phép điều kiện hóa theo ví dụ trong prompt mà không cập nhật trọng số.

## Ngữ cảnh (context / 맥락) and In-Context học tập (learning / 학습) Preview

Transformer ngôn ngữ (language / 언어) mô hình (model / 모델) conditions predictions on prompt examples/instructions without parameter cập nhật (update / 업데이트). This is **in-context học tập (learning / 학습)**.

Cơ chế (mechanism / 메커니즘) arises from learned chuỗi (sequence / 시퀀스) computation. It is not same as huấn luyện (training / 학습)/fine-tuning because weights fixed during prompt.

Detailed in LLM folder.

In-context learning dùng context như bộ nhớ tạm, khác với fine-tuning; scaling đặt hiện tượng đó trong quan hệ giữa dữ liệu, tham số và compute.

## Scaling

As mô hình (model / 모델) parameters, dữ liệu (data / 데이터) and compute quy mô (scale / 규모), language-model mất mát (loss / 손실) often follows predictable power-law-like curves over regimes. Better predictive modeling unlocks emergent-looking downstream capabilities, though “emergence” can depend chỉ số (metric / 지표) thresholding.

Scaling laws later discussed in LLM tầng (layer / 계층).

Scaling thường cải thiện loss theo các regime nhất định nhưng không tự bảo đảm hành vi; compression view cung cấp trực giác thông tin cho việc học phân phối.

## Compression View

A good probabilistic mô hình (model / 모델) can encode chuỗi (sequence / 시퀀스) efficiently via arithmetic coding: expected mã (code / 코드) length relates negative log xác suất (probability / 확률).

Thus ngôn ngữ (language / 언어) modeling and compression connect through thông tin (information / 정보) lý thuyết (theory / 이론):

\[
mã (code / 코드)\ length\approx-\log_2P(x)
\]

Predictive cấu trúc (structure / 구조) = compressible cấu trúc (structure / 구조).

Nhìn từ compression, xác suất cao tương ứng mã ngắn hơn; mental model tiếp theo nối xác suất, sinh chuỗi, context và đánh giá.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Language model does not choose a sentence all at once.
It repeatedly estimates:
P(next token | all allowed context)
```

The richness comes from learned contextual biểu diễn (representation / 표현), not a different basic đầu ra (output / 출력) mục tiêu (objective / 목표).

Mental model này nhấn mạnh model tối ưu phân phối token, không trực tiếp tối ưu truth; phần misconceptions kiểm tra các suy luận sai từ mục tiêu đó.

## Dùng chung (common / 공통) Misconceptions

### “Perplexity 10 means mô hình (model / 모델) has 10 choices each đơn vị từ (token / 토큰) exactly”

Only effective geometric-average bất định (uncertainty / 불확실성) intuition, not literal fixed choices.

### “Next-token prediction is too simple to learn ngữ nghĩa (semantics / 의미론)”

Simple mục tiêu (objective / 목표) over massive diverse ngữ cảnh (context / 맥락) can require rich nội bộ (internal / 내부) representations; mục tiêu (objective / 목표) simplicity does not imply learned hàm (function / 함수) simplicity.

### “Low perplexity guarantees factual answers”

No. Truth is not directly optimized.

### “Temperature changes mô hình (model / 모델) intelligence”

It changes sampling phân phối (distribution / 분포) from same logits, not parameters/kiến thức (knowledge / 지식).

Sau khi sửa các ngộ nhận, phần liên kết kiến thức chỉ ra tài liệu về tokenization, Transformer và LLM để tiếp tục theo owner.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Language Models connect [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Sequence Models](../06_deep_learning_architectures/01_sequence_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) and prepare LLM pretraining.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
