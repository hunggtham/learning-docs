# RAG Evaluation

RAG là multi-stage system nên một final-answer score không đủ để biết failure nằm ở đâu. Evaluation tốt phải tách **ingestion → retrieval → reranking → context selection → generation → citation**.

## Evaluation Layers

```text
1. corpus/index quality
2. retrieval quality
3. reranking/context quality
4. generation groundedness
5. end-to-end task success
6. latency/cost/reliability
```

Nếu final answer sai, trace qua từng layer để tìm root cause.

## Build a Query–Evidence Test Set

Mỗi eval item nên chứa:

```text
query
gold relevant document/chunk IDs
expected answer hoặc key facts
metadata constraints
optional forbidden/stale sources
```

Gold evidence rất valuable vì cho phép evaluate retrieval independent generator.

## Retrieval Recall@k

Quan trọng nhất: correct evidence có trong top-k không?

\[
Recall@k=\frac{queries\ with\ relevant\ evidence\ in\ top\ k}{all\ queries}
\]

Nếu Recall@10 thấp, improve retriever/chunking before prompt tuning.

## Precision@k

Đo noise trong candidates/context. High recall với quá nhiều distractors có thể hurt generator.

## MRR và nDCG

MRR reward first relevant result rank cao. nDCG supports graded relevance và multiple relevant docs.

Use metric phù hợp query: multi-source question needs more than first-hit metric.

## Chunk-Level vs Document-Level Recall

Document relevant nhưng retrieved chunk không chứa answer vẫn có thể fail generation.

Track both:

```text
document recall
answer-bearing chunk recall
```

## Reranker Lift

Compare ranking before và after reranker:

```text
MRR_before → MRR_after
nDCG_before → nDCG_after
```

Nếu reranker không lift, cost may not be justified.

## Context Recall

Even if candidate set contains evidence, context selector may drop it. Evaluate selected final context separately.

This catches token-budget/dedup bugs.

## Answer Correctness

Final answer can be exact-match, rubric-scored, human-judged or LLM-judged depending task.

For policy QA, rubric can check required clauses individually rather than one holistic score.

## Faithfulness / Groundedness

Break answer into claims and ask whether each claim is entailed by retrieved sources.

Conceptually:

\[
Groundedness=\frac{supported\ claims}{all\ factual\ claims}
\]

This is different from correctness relative to external world.

## Citation Precision

For cited claims, citation should actually support claim.

```text
citation precision = supported cited claims / cited claims
```

## Citation Recall

How many factual claims that need support actually have citation?

Useful in research/legal applications.

## Answer Relevance

Grounded answer can still fail user intent. Measure whether answer addresses query and follows requested format.

## Answerability

Dataset should include questions **not answerable from corpus**. Good RAG should abstain or state insufficient evidence rather than hallucinate.

Track:

```text
correct abstention rate
false abstention rate
unsupported answer rate
```

## Staleness Evaluation

Include old/new document versions. Verify retriever selects current/effective source and excludes archived docs when appropriate.

This catches version-filter bugs.

## Permission Evaluation

Security tests should confirm users cannot retrieve documents outside ACL/tenant.

This is pass/fail security property, not soft relevance metric.

## Multilingual Evaluation

If users query Korean/Vietnamese/English, create slices per language and cross-language retrieval.

Average score can hide one weak language.

## Table/Numeric Evaluation

Test exact numeric values, units and table row relationships. OCR/parser errors often surface here.

## Robustness

Paraphrase queries, add typo, use aliases, abbreviations and long conversational references. Retrieval should not collapse on superficial wording.

## Hard Negatives

Eval corpus should contain near-identical wrong documents:

```text
wrong version
wrong product
wrong country
similar policy title
```

Easy benchmark inflates retrieval quality.

## End-to-End Latency

Break latency:

```text
query rewrite
embedding
retrieval
rerank
LLM generation
```

p95/p99 matter more than average for UX.

## Cost Evaluation

Measure per request:

```text
embedding tokens
reranker compute
LLM input/output tokens
search infrastructure
```

Advanced pipeline may improve quality 1% but double cost; decide based value.

## Online Metrics

After deployment:

```text
user correction rate
citation clicks
escalation rate
zero-result rate
abstention rate
retrieval latency
feedback
```

Online metrics are noisy and influenced by UX, but reveal real traffic shift.

## Failure Attribution

A useful taxonomy:

```text
PARSE_FAILURE
CHUNK_MISS
RETRIEVAL_MISS
RERANK_ERROR
CONTEXT_DROP
GENERATION_UNSUPPORTED
CITATION_ERROR
STALE_SOURCE
ACL_ERROR
```

Every production incident should map to layer where possible.

## Eval-Driven Improvement Loop

```text
observe failure
→ label root cause
→ add eval case
→ modify one layer
→ rerun suite
→ compare quality/cost
→ deploy
```

This avoids random prompt tweaking.

## Human Evaluation

Experts are needed when domain nuance matters. Use clear rubric và sample representative cases. Inter-annotator disagreement can reveal ambiguous policy or insufficient source data.

## LLM-as-Judge

LLM judges scale evaluation, especially relevance/faithfulness, but require calibration against humans. Provide source evidence to judge and randomize response order to reduce bias.

## Golden Set Leakage

If engineers repeatedly tune on same golden set, it becomes development set. Maintain hidden holdout/fresh evals.

## Mental Model

> RAG evaluation phải trả lời hai câu độc lập: **Did we retrieve the right evidence? Did we use it correctly?**

## Common Misconceptions

### “Final answer đúng nên retrieval cũng tốt”

Model may answer from parametric memory by chance.

### “Retrieval recall cao là đủ”

Context noise/generation faithfulness still matter.

### “LLM judge score là ground truth”

Không. Judge itself needs evaluation.

## Knowledge Connection

RAG evaluation extends [LLM Evaluation](../08_large_language_models/14_llm_evaluation.md) and becomes prerequisite for Agent/AI Engineering observability.