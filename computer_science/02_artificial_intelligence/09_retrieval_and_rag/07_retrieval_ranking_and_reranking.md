# Retrieval, Ranking và Reranking

Một retrieval system tốt thường không cố dùng một model duy nhất để vừa search toàn corpus vừa đánh giá relevance rất tinh. Thay vào đó, architecture phổ biến là **multi-stage ranking**: first-stage retriever tạo candidate set nhanh, sau đó reranker đắt hơn refine order.

## Candidate Generation

First-stage objective ưu tiên **recall**:

```text
millions of chunks
→ retrieve top 50–200 candidates
```

Sparse, dense hoặc hybrid retrievers phù hợp vì search nhanh.

Nếu correct evidence không xuất hiện trong candidates, reranker phía sau không thể cứu.

## Reranking

Reranker score query và candidate với interaction sâu hơn.

Cross-encoder:

```text
[query ; chunk] → Transformer → relevance score
```

Nó đọc query và chunk cùng lúc nên hiểu fine-grained match tốt hơn bi-encoder.

Cost gần proportional số candidates × document length, vì vậy chỉ dùng sau first-stage retrieval.

## Relevance Types

Reranker cần học distinction:

```text
topical relevance
answer relevance
freshness
authority
user scope
```

Một document cùng topic nhưng old version không nên rank cao hơn current authoritative document.

Some factors tốt hơn xử lý explicit metadata/business rules thay vì learned reranker.

## Hybrid Fusion

Sparse/dense result sets có thể merge bằng RRF hoặc learned fusion.

Example:

```text
BM25 top 50
Dense top 50
→ union
→ reranker
→ top 8 context chunks
```

Union increases recall; reranker resolves conflicts.

## Query Rewriting

Before retrieval, query có thể được rewrite để:

- resolve pronouns/history;
- expand abbreviations;
- translate language;
- decompose multi-part question.

Rewrite itself must be evaluated because it can remove important qualifiers.

## Query Decomposition

Question:

```text
"So sánh phí và điều kiện hủy của gói A và B"
```

có thể decompose:

```text
A fees
A cancellation conditions
B fees
B cancellation conditions
```

Retrieve each subquery then synthesize.

Useful for multi-hop questions.

## Multi-Hop Retrieval

Some questions require evidence chain:

```text
entity A → relation → entity B → property of B
```

One-shot query may not contain terms needed for second hop. Iterative retrieval uses first evidence to formulate next query.

This begins to resemble agentic search.

## Reranker Training

Training examples need query, positive chunk và hard negatives. Hard negatives should be plausible but wrong:

```text
same product, wrong version
same policy, wrong country
same topic, missing condition
```

These cases teach fine distinctions relevant production.

## Rank vs Score Calibration

Reranker score often only meaningful for ordering within query, not absolute probability of relevance.

If using threshold to abstain, calibrate on labeled data.

## Diversification

Top results may all duplicate same paragraph. **Maximal Marginal Relevance (MMR)** balances relevance and diversity:

\[
MMR=\lambda Sim(q,d)-(1-\lambda)\max_{d'\in S}Sim(d,d')
\]

Useful when query needs multiple aspects.

But diversity can hurt if user only needs one exact fact.

## Context Selection

After rerank, do not blindly take top-k. Context builder may consider:

```text
relevance
source diversity
version/authority
token budget
redundancy
neighbor context
```

This is a constrained selection problem.

## Lost-in-the-Middle Effect

LLMs may attend unevenly to long contexts. Critical evidence placed among many distractors can be underused.

Context ordering matters. Common patterns place strongest evidence early or group by subquestion.

## Duplicate Suppression

Near-duplicate chunks waste tokens and can bias model as if repeated fact were stronger evidence.

Dedup candidate set using content hash or semantic similarity.

## Freshness Boost

For time-sensitive corpora, ranking can combine relevance with freshness:

\[
score = relevance + \alpha \cdot freshness
\]

But newest document is not always authoritative. Version status is better signal when available.

## Authority Boost

Policy hierarchy can be explicit:

```text
official regulation > internal wiki > chat note
```

Encode source authority metadata rather than hoping embedding model infer it.

## Reranking Cost

If 100 candidates × 1000 tokens each go through cross-encoder, latency may dominate. Options:

```text
reduce candidates
shorten chunks
use smaller reranker
batch scoring
late interaction
cache repeated queries
```

Quality/cost curve must be measured.

## LLM Reranking

LLM can rerank by reading candidate summaries and query. It handles nuanced criteria but is expensive and can be position-biased.

Use when candidate count small and value high, with deterministic ordering/IDs.

## Retrieval Confidence

Low top scores or flat score distribution may indicate no good evidence. System can broaden search, fallback lexical, ask clarification or abstain.

This is better than always force answer.

## Offline Evaluation

Need labeled query→relevant chunk/document pairs. Metrics:

```text
Recall@k
MRR
nDCG
Precision@k
```

Compare stages:

```text
first-stage recall
reranked nDCG
final context recall
```

## Mental Model

> Retrieval pipeline giống funnel: **wide recall first, precise relevance later, context constraints cuối**.

## Common Misconceptions

### “Reranker có thể sửa retriever bỏ sót evidence”

Không nếu evidence không vào candidate set.

### “Top-k càng lớn càng tốt”

Không. Noise và token cost tăng.

### “Newest = most correct”

Không nếu draft/newer document không authoritative.

## Knowledge Connection

Ranking connects IR metrics, cross-encoder NLP, optimization và context engineering.

Xem tiếp: [Advanced RAG](./08_advanced_rag.md).