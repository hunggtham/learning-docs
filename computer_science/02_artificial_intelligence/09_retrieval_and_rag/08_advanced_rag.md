# Advanced RAG Patterns

Basic RAG uses one query, one retrieval pass and one generation step. Real workloads often need more structure: ambiguous questions, multi-hop evidence, heterogeneous data, changing documents and high reliability. **Advanced RAG** is not one algorithm; it is a collection of architectural patterns for improving retrieval, evidence selection and generation control.

## Query Rewriting

Conversational input may be underspecified:

```text
"còn phí của gói kia thì sao?"
```

A rewrite model resolves history into standalone query. Good system preserves original intent and logs both forms.

A rewrite should not silently add facts not present in conversation.

## Query Expansion

Generate synonyms/aliases or multiple semantic formulations to increase recall.

Example:

```text
"hủy hợp đồng"
→ cancellation
→ contract termination
→ 해지
```

Merge results from expanded queries. Risk is topic drift, so expansion should be constrained by domain dictionaries or reranking.

## Multi-Query Retrieval

For complex question, generate several related queries and fuse results. This is useful when one embedding cannot represent all aspects equally.

```text
user question
→ query A
→ query B
→ query C
→ retrieve each
→ fusion/rerank
```

## HyDE

**Hypothetical Document Embeddings (HyDE)** creates a hypothetical answer/document from query, embeds that generated text, then retrieves real documents close to it.

Intuition: long hypothetical text may land nearer relevant documents than short query.

Risk: hypothetical generation may inject wrong assumptions and drift retrieval.

HyDE should be evaluated, not treated as default.

## Parent-Child Retrieval

Index small child chunks for precise search, then return larger parent context for generation.

```text
small chunk finds needle
→ parent section supplies surrounding conditions
```

This is especially effective for manuals/policies.

## Multi-Vector Retrieval

One document may have multiple representations:

```text
raw chunk embedding
summary embedding
title embedding
questions-the-chunk-can-answer embeddings
```

Retrieve by any representation but return original source text.

This separates **search representation** from **evidence representation**.

## Summary Index

For very long documents, build hierarchical summaries:

```text
document summary
section summaries
leaf chunks
```

Retriever first routes to relevant document/section, then searches locally.

This reduces search space and supports broad questions.

## Hierarchical Retrieval

Corpus can be organized:

```text
organization
→ product
→ document
→ section
→ chunk
```

Query first predicts higher-level route then retrieves lower-level units.

Routing errors become new failure mode, so fallback global search is useful.

## Metadata Routing

Before semantic search, detect structured constraints:

```text
language=ko
product=eKYC
country=KR
version=current
```

Route to matching namespace/index. LLM may extract filters, but application validates allowed values.

## Multi-Hop Retrieval

Some answers require chain of sources. Example:

```text
Which policy applies to product X?
→ retrieve product definition
→ discover policy ID
→ retrieve policy clauses
```

An iterative controller can use intermediate evidence to formulate next query.

This begins to overlap agent architecture.

## Graph RAG

When relationships between entities matter, build graph or knowledge graph and combine graph traversal with text retrieval.

Useful for:

```text
organization relationships
dependency chains
regulations and clauses
entity networks
```

Graph RAG is valuable when relational structure is explicit, not because graph is automatically superior to vectors.

## SQL + RAG

Structured data should often be queried with SQL, while unstructured explanation comes from text retrieval.

Example:

```text
SQL → current transaction values
RAG → policy/explanation
LLM → synthesize
```

Do not embed tables and expect vector search to perform accurate aggregation.

## Tool-Augmented RAG

Retriever itself can be one tool among many:

```text
web search
internal docs
SQL
API
code search
```

Router chooses data source based on question.

This is more robust than one universal vector index.

## Corrective RAG

After retrieval, system evaluates whether evidence is sufficient/relevant. If not:

```text
rewrite query
broaden search
switch retriever
search web
ask clarification
abstain
```

Correction loop prevents forced answer on weak evidence.

## Self-RAG-like Patterns

Model may decide when retrieval is needed and critique whether generated statements are supported.

But self-evaluation is probabilistic; external evidence checks still valuable.

## Adaptive Retrieval

Not every query needs retrieval. Simple greetings or pure transformation tasks may skip search.

Router predicts:

```text
retrieve?
which source?
how many results?
```

This saves latency/cost but routing errors can miss necessary knowledge.

## Query Classification

Classify query into patterns:

```text
exact lookup
policy QA
comparison
multi-hop
calculation
current data
```

Each class gets specialized retrieval strategy.

## Context Compression

Reranked chunks can be compressed into query-relevant excerpts. This lowers tokens but introduces extractor risk.

Keep source references so user can inspect full context.

## Evidence Graph

For multi-source answer, create explicit mapping:

```text
claim A ← source 1
claim B ← source 2 + source 3
```

This improves citation quality and makes verification easier.

## Conflict Resolution

If two sources disagree, model should not silently average. Use metadata:

```text
version
date
authority
status
jurisdiction
```

System may present conflict rather than fabricate single answer.

## Temporal RAG

Time-sensitive corpora need effective-date filtering. Query should retrieve source valid at requested time, not simply newest.

Example:

```text
"policy as of 2025-12-01"
```

requires temporal validity intervals.

## Personalized RAG

Retrieval can consider user profile/permissions/preferences. But personalization must not leak sensitive cross-user data.

Separate personalization signal from authorization logic.

## Caching

Cache query embedding, retrieval results or final answers. Cache key must include:

```text
query
user/tenant scope
index version
source version
model/prompt version
```

Otherwise stale or cross-user leakage can occur.

## Observability

Advanced RAG needs traces:

```text
original query
rewritten queries
filters
retrieved IDs/scores
reranker scores
selected context
citations
final output
```

Without trace, debugging “LLM trả lời sai” becomes guesswork.

## Mental Model

> Advanced RAG is **retrieval orchestration under uncertainty**. Complexity should be added only when a measured failure mode justifies it.

## Common Misconceptions

### “Advanced RAG means add an agent framework”

Không. Many improvements are deterministic retrieval/ranking architecture.

### “Graph RAG always beats vector RAG”

Không. It depends on relational structure and query type.

### “More retrieval loops always improve answer”

No. More calls increase latency, drift and cost.

## Knowledge Connection

Advanced RAG is the bridge from retrieval pipeline to [Agents](../10_agents_and_ai_systems/00_from_llm_to_agent.md).

Xem tiếp: [RAG Evaluation](./09_rag_evaluation.md).