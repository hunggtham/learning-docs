# Language Models: học xác suất của chuỗi ngôn ngữ

Language Model (언어 모델 / mô hình ngôn ngữ) gán probability cho sequence hoặc dự đoán token dựa trên context. Đây là core abstraction đứng sau autocomplete, speech decoding, machine translation và Large Language Models.

Điểm quan trọng: language model không trực tiếp optimize “truth” hay “reasoning”. Objective cơ bản là model distribution của observed language. Capability khác xuất hiện vì để predict language tốt ở scale lớn, model phải learn nhiều structure về syntax, semantics, knowledge và patterns of reasoning — nhưng objective và capability không đồng nhất.

## Joint Probability và Chain Rule

Với sequence:

\[
x_{1:T}=(x_1,...,x_T)
\]

chain rule:

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

Không cần Markov assumption để factorization đúng. Difficulty là estimate each conditional distribution.

Autoregressive language model học:

\[
P_\theta(x_t\mid x_{<t})
\]

## n-gram Language Models

Approximate context limited:

\[
P(x_t\mid x_{<t})\approx P(x_t\mid x_{t-n+1:t-1})
\]

Estimate counts:

\[
P(w_t\mid h)=\frac{count(h,w_t)}{count(h)}
\]

Sparse data causes zero probabilities for unseen n-grams.

Smoothing methods như Laplace, Good-Turing, Kneser-Ney redistribute probability mass. Kneser-Ney đặc biệt uses continuation statistics and remains a landmark classical LM technique.

## Why Neural Language Models?

n-gram treats contexts mostly discrete. `the cat sat` and `the dog sat` share little unless explicit backoff.

Neural LM maps words/tokens into embeddings and represents context continuously, allowing statistical sharing across similar contexts.

Early feed-forward LM:

```text
fixed previous tokens
→ embeddings
→ MLP
→ softmax next word
```

RNN removed fixed context window. Transformer improved long-range access and parallel training.

## Maximum Likelihood Training

Given corpus, maximize:

\[
\sum_t\log P_\theta(x_t\mid x_{<t})
\]

Equivalent minimize negative log-likelihood / cross-entropy:

\[
L=-\frac1T\sum_t\log P_\theta(x_t\mid x_{<t})
\]

Teacher forcing gives model true previous tokens during training.

## Perplexity

If average cross-entropy in natural log is `H`:

\[
PPL=e^H
\]

If log base 2:

\[
PPL=2^{H_2}
\]

Intuition: effective branching factor under model.

Lower perplexity on same tokenization/test distribution usually better next-token modeling.

But perplexity cannot compare cleanly across different tokenizers because unit differs. Lower PPL also does not guarantee better instruction following/factuality.

## Masked Language Modeling

BERT-like objective masks tokens and predicts them using both left/right context:

\[
P(x_i\mid x_{\setminus i})
\]

This is not autoregressive joint factorization in same direct way. It learns bidirectional representations excellent for encoding tasks.

## Causal Language Modeling

GPT-style objective predicts each token using only previous tokens. Causal mask preserves:

\[
P(x_t\mid x_{<t})
\]

Advantage: model can directly generate by ancestral sampling.

## Prefix / Seq2Seq Language Modeling

Encoder-decoder models condition output sequence on source:

\[
P(y\mid x)=\prod_tP(y_t\mid y_{<t},x)
\]

T5 reframes many NLP tasks as text-to-text conditional generation.

## Sampling from Language Model

Given logits `z`, temperature:

\[
p_i=softmax(z_i/T)
\]

- `T<1`: sharper;
- `T>1`: flatter.

### Greedy

Pick max probability each step. Deterministic but can be repetitive/suboptimal sequence-level.

### Top-k

Keep k highest-probability tokens, renormalize.

### Top-p / Nucleus

Choose smallest token set whose cumulative probability ≥ `p`, then sample. Candidate set adapts distribution uncertainty.

Sampling configuration affects style/diversity, not model knowledge itself.

## Exposure Bias

Training conditions on true history; generation conditions on own outputs. One error changes future context and can cascade.

This mismatch is inherent standard autoregressive maximum-likelihood training.

Instruction tuning/RL-based post-training can change behavior, but does not remove autoregressive nature.

## Degeneration

Pure maximization or poor sampling can cause repetition, generic text or loops.

Reasons include distribution shape, training objective and decoding strategy. Repetition penalties can help but are heuristic and may distort distribution.

## Language Model ≠ Knowledge Database

Parameters encode distributed statistical associations. Querying a fact is not exact key lookup.

Consequences:

- knowledge can be approximate;
- conflicting facts coexist;
- recency limited by training;
- provenance absent;
- rare facts unreliable.

External retrieval (RAG) adds explicit source access.

## Language Model ≠ Truth Model

Training corpus contains true/false fiction/speculation. Next-token likelihood rewards linguistic plausibility under corpus distribution, not direct world verification.

This explains hallucination risk at objective level.

## Context and In-Context Learning Preview

Transformer language model conditions predictions on prompt examples/instructions without parameter update. This is **in-context learning**.

Mechanism arises from learned sequence computation. It is not same as training/fine-tuning because weights fixed during prompt.

Detailed in LLM folder.

## Scaling

As model parameters, data and compute scale, language-model loss often follows predictable power-law-like curves over regimes. Better predictive modeling unlocks emergent-looking downstream capabilities, though “emergence” can depend metric thresholding.

Scaling laws later discussed in LLM layer.

## Compression View

A good probabilistic model can encode sequence efficiently via arithmetic coding: expected code length relates negative log probability.

Thus language modeling and compression connect through Information Theory:

\[
code\ length\approx-\log_2P(x)
\]

Predictive structure = compressible structure.

## Mental Model

```text
Language model does not choose a sentence all at once.
It repeatedly estimates:
P(next token | all allowed context)
```

The richness comes from learned contextual representation, not a different basic output objective.

## Common Misconceptions

### “Perplexity 10 means model has 10 choices each token exactly”

Only effective geometric-average uncertainty intuition, not literal fixed choices.

### “Next-token prediction is too simple to learn semantics”

Simple objective over massive diverse context can require rich internal representations; objective simplicity does not imply learned function simplicity.

### “Low perplexity guarantees factual answers”

No. Truth is not directly optimized.

### “Temperature changes model intelligence”

It changes sampling distribution from same logits, not parameters/knowledge.

## Knowledge Connection

Language Models connect [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Sequence Models](../06_deep_learning_architectures/01_sequence_models.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) and prepare LLM pretraining.