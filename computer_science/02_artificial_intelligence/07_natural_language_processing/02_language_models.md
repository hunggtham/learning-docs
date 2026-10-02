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

> **Chuyển mạch:** Trong **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Joint xác suất (probability / 확률) và chuỗi (chain / 사슬) quy tắc (rule / 규칙)** xác định đầu vào; **n-gram ngôn ngữ (language / 언어) các mô hình (models / 모델들)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Why Neural ngôn ngữ (language / 언어) các mô hình (models / 모델들)?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Why Neural ngôn ngữ (language / 언어) các mô hình (models / 모델들)?** tiếp nhận điểm tựa từ **n-gram ngôn ngữ (language / 언어) các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Maximum Likelihood huấn luyện (training / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Maximum Likelihood huấn luyện (training / 학습)** tiếp nhận điểm tựa từ **Why Neural ngôn ngữ (language / 언어) các mô hình (models / 모델들)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Perplexity** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Perplexity** tiếp nhận điểm tựa từ **Maximum Likelihood huấn luyện (training / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Masked ngôn ngữ (language / 언어) Modeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Masked ngôn ngữ (language / 언어) Modeling** tiếp nhận điểm tựa từ **Perplexity** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhân quả (causal / 인과적) ngôn ngữ (language / 언어) Modeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Masked ngôn ngữ (language / 언어) Modeling

BERT-like mục tiêu (objective / 목표) masks tokens and predicts them using both left/right ngữ cảnh (context / 맥락):

\[
P(x_i\mid x_{\setminus i})
\]

This is not autoregressive joint factorization in same direct way. It learns bidirectional representations excellent for encoding tasks.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Nhân quả (causal / 인과적) ngôn ngữ (language / 언어) Modeling** tiếp nhận điểm tựa từ **Masked ngôn ngữ (language / 언어) Modeling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prefix / Seq2Seq ngôn ngữ (language / 언어) Modeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhân quả (causal / 인과적) ngôn ngữ (language / 언어) Modeling

GPT-style mục tiêu (objective / 목표) predicts each đơn vị từ (token / 토큰) using only previous tokens. nhân quả (causal / 인과적) mask preserves:

\[
P(x_t\mid x_{<t})
\]

Advantage: mô hình (model / 모델) can directly generate by ancestral sampling.

> **Chuyển mạch:** Trong **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Prefix / Seq2Seq ngôn ngữ (language / 언어) Modeling** tiếp nhận điểm tựa từ **Nhân quả (causal / 인과적) ngôn ngữ (language / 언어) Modeling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sampling from ngôn ngữ (language / 언어) mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prefix / Seq2Seq ngôn ngữ (language / 언어) Modeling

Encoder-decoder các mô hình (models / 모델들) điều kiện (condition / 조건) đầu ra (output / 출력) chuỗi (sequence / 시퀀스) on nguồn (source / 소스):

\[
P(y\mid x)=\prod_tP(y_t\mid y_{<t},x)
\]

T5 reframes many NLP tasks as text-to-text conditional generation.

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Sampling from ngôn ngữ (language / 언어) mô hình (model / 모델)** tiếp nhận điểm tựa từ **Prefix / Seq2Seq ngôn ngữ (language / 언어) Modeling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Exposure độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Exposure độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Sampling from ngôn ngữ (language / 언어) mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Degeneration** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Exposure độ lệch (bias / 편향)

Huấn luyện (training / 학습) conditions on true lịch sử (history / 이력); generation conditions on own outputs. One lỗi (error / 오류) changes future ngữ cảnh (context / 맥락) and can cascade.

This mismatch is inherent tiêu chuẩn (standard / 표준) autoregressive maximum-likelihood huấn luyện (training / 학습).

Instruction tuning/RL-based post-training can thay đổi (change / 변경) hành vi (behavior / 동작), but does not remove autoregressive nature.

> **Chuyển mạch:** Trong **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Degeneration** tiếp nhận điểm tựa từ **Exposure độ lệch (bias / 편향)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ kiến thức (knowledge / 지식) cơ sở dữ liệu (database / 데이터베이스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Degeneration

Pure maximization or poor sampling can cause repetition, generic văn bản (text / 텍스트) or loops.

Reasons include phân phối (distribution / 분포) shape, huấn luyện (training / 학습) mục tiêu (objective / 목표) and decoding chiến lược (strategy / 전략). Repetition penalties can help but are heuristic and may distort phân phối (distribution / 분포).

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Degeneration** nêu điều cần giải thích; **Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ kiến thức (knowledge / 지식) cơ sở dữ liệu (database / 데이터베이스)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ Truth mô hình (model / 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ kiến thức (knowledge / 지식) cơ sở dữ liệu (database / 데이터베이스)

Parameters encode phân tán (distributed / 분산) statistical associations. Querying a fact is not chính xác (exact / 정확한) key lookup.

Consequences:

- kiến thức (knowledge / 지식) can be approximate;
- conflicting facts coexist;
- recency limited by huấn luyện (training / 학습);
- provenance absent;
- rare facts unreliable.

Bên ngoài (external / 외부) retrieval (RAG) adds tường minh (explicit / 명시적) nguồn (source / 소스) truy cập (access / 접근).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ kiến thức (knowledge / 지식) cơ sở dữ liệu (database / 데이터베이스)** nêu điều cần giải thích; **Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ Truth mô hình (model / 모델)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Ngữ cảnh (context / 맥락) and In-Context học tập (learning / 학습) Preview** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ Truth mô hình (model / 모델)

Huấn luyện (training / 학습) corpus contains true/false fiction/speculation. Next-token likelihood rewards linguistic plausibility under corpus phân phối (distribution / 분포), not direct world xác minh (verification / 확인).

This explains hallucination rủi ro (risk / 위험) at mục tiêu (objective / 목표) mức (level / 수준).

> **Chuyển mạch:** Trong **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Ngữ cảnh (context / 맥락) and In-Context học tập (learning / 학습) Preview** tiếp nhận điểm tựa từ **Ngôn ngữ (language / 언어) mô hình (model / 모델) ≠ Truth mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Scaling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Ngữ cảnh (context / 맥락) and In-Context học tập (learning / 학습) Preview

Transformer ngôn ngữ (language / 언어) mô hình (model / 모델) conditions predictions on prompt examples/instructions without parameter cập nhật (update / 업데이트). This is **in-context học tập (learning / 학습)**.

Cơ chế (mechanism / 메커니즘) arises from learned chuỗi (sequence / 시퀀스) computation. It is not same as huấn luyện (training / 학습)/fine-tuning because weights fixed during prompt.

Detailed in LLM folder.

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Scaling** tiếp nhận điểm tựa từ **Ngữ cảnh (context / 맥락) and In-Context học tập (learning / 학습) Preview** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Compression View** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Scaling

As mô hình (model / 모델) parameters, dữ liệu (data / 데이터) and compute quy mô (scale / 규모), language-model mất mát (loss / 손실) often follows predictable power-law-like curves over regimes. Better predictive modeling unlocks emergent-looking downstream capabilities, though “emergence” can depend chỉ số (metric / 지표) thresholding.

Scaling laws later discussed in LLM tầng (layer / 계층).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Compression View** tiếp nhận điểm tựa từ **Scaling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Compression View

A good probabilistic mô hình (model / 모델) can encode chuỗi (sequence / 시퀀스) efficiently via arithmetic coding: expected mã (code / 코드) length relates negative log xác suất (probability / 확률).

Thus ngôn ngữ (language / 언어) modeling and compression connect through thông tin (information / 정보) lý thuyết (theory / 이론):

\[
mã (code / 코드)\ length\approx-\log_2P(x)
\]

Predictive cấu trúc (structure / 구조) = compressible cấu trúc (structure / 구조).

> **Chuyển mạch:** Trong **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Compression View** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Language model does not choose a sentence all at once.
It repeatedly estimates:
P(next token | all allowed context)
```

The richness comes from learned contextual biểu diễn (representation / 표현), not a different basic đầu ra (output / 출력) mục tiêu (objective / 목표).

> **Chuyển mạch:** Ở chặng này của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Perplexity 10 means mô hình (model / 모델) has 10 choices each đơn vị từ (token / 토큰) exactly”

Only effective geometric-average bất định (uncertainty / 불확실성) intuition, not literal fixed choices.

### “Next-token prediction is too simple to learn ngữ nghĩa (semantics / 의미론)”

Simple mục tiêu (objective / 목표) over massive diverse ngữ cảnh (context / 맥락) can require rich nội bộ (internal / 내부) representations; mục tiêu (objective / 목표) simplicity does not imply learned hàm (function / 함수) simplicity.

### “Low perplexity guarantees factual answers”

No. Truth is not directly optimized.

### “Temperature changes mô hình (model / 모델) intelligence”

It changes sampling phân phối (distribution / 분포) from same logits, not parameters/kiến thức (knowledge / 지식).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Ngôn ngữ (language / 언어) các mô hình (models / 모델들): học xác suất của chuỗi ngôn ngữ**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Language Models connect [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Sequence Models](../06_deep_learning_architectures/01_sequence_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) and prepare LLM pretraining.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
