# Embeddings và Semantic Space trong LLM Systems

“Embedding” trong LLM context có ít nhất ba meanings cần tách: **input token embedding**, **internal contextual hidden states**, và **external embedding model output dùng cho retrieval/similarity**. Chúng đều là vectors nhưng objective/use khác nhau.

Nếu trộn ba loại, dễ nghĩ vector database đang lưu “LLM thoughts” hoặc token embedding là semantic sentence embedding. Không đúng.

## Input Token Embedding

Tokenizer ID maps row:

\[
x_t=E[token_t]
\]

`E∈R^{V×d_model}` trained jointly with language model.

This vector is context-independent initial representation. Contextualization happens through Transformer layers.

## Contextual Hidden State

After layer `l`:

\[
h_t^{(l)}=TransformerLayer_l(...)
\]

depends other allowed tokens. Same token has different hidden state based context.

Internal hidden states optimized for next-token objective, not necessarily cosine sentence search.

## Output / Unembedding

Final hidden state maps to vocabulary logits:

\[
z=W_Uh_t
\]

Often `W_U=E^T` through weight tying, but not universal.

Dot product hidden state with token output vectors yields token compatibility logits.

This creates interesting geometric relation between hidden space and vocabulary, but softmax behavior is contextual/composed through layers.

## External Embedding Model

Retrieval model maps whole query/document/chunk:

\[
f(text)\rightarrow z\in R^d
\]

trained with contrastive/retrieval objective so vector similarity corresponds relevance/semantic relation.

A chat LLM's last hidden state is not automatically good retrieval embedding. Dedicated embedding model usually better/cheaper.

## Semantic Space không phải dictionary of concepts

A vector has no meaning independent model/objective. Rotating entire embedding space while preserving dot products can leave behavior unchanged; individual coordinate therefore not canonical semantic axis.

Meaning lies relationships/subspaces and downstream computation.

## Cosine vs Dot Product

If vectors normalized:

\[
q^Td=cos(q,d)
\]

If not normalized, dot-product includes magnitude. Some embedding models use vector norm to encode confidence/frequency; follow recommended similarity.

Vector DB metric must match training objective.

## Matryoshka / Truncatable Embeddings

Some models train embedding so prefix dimensions retain useful information; vector can truncate from e.g. 1024 to 256 dimensions with graceful degradation.

Benefit storage/ANN speed. This property must be trained/validated; arbitrary truncating generic embedding may destroy quality.

## Embedding Dimension Trade-off

Higher dimension increases capacity but also:

- storage;
- memory bandwidth;
- ANN index size;
- retrieval latency;
- sample/overfit complexity.

Beyond a point, quality gain may small. Evaluate target corpus.

## Embedding Normalization và Quantization

Large vector corpora can store FP16/int8/product-quantized codes. Compression saves memory at recall cost.

Quantization of embeddings/index is separate from LLM weight quantization, though principles numerical approximation related.

## Semantic Search Pipeline

```text
Document
→ chunk
→ embed
→ index vector + metadata

Query
→ embed same compatible model
→ ANN search
→ filter/rerank
```

Mix embedding model versions corrupts geometry.

## Asymmetric Retrieval

Query and document roles differ. Some models use task prefixes:

```text
query: ...
passage: ...
```

or separate encoders/projections. Ignoring required prefixes lowers quality.

## Hybrid Search

Dense embeddings struggle exact IDs/names/numbers sometimes. BM25 lexical retriever catches exact terms.

Hybrid retrieval fuses sparse + dense signals, especially enterprise code/product/legal docs.

## Embedding Fine-Tuning

Domain positives/negatives can adapt geometry.

Hard negative example:

```text
query: reset corporate card PIN
negative: reset personal bank password
```

Semantically close but task-irrelevant, forcing model learn fine distinctions.

False negatives must be controlled.

## Embeddings and Privacy

Vectors are not guaranteed anonymous. Embeddings can leak attributes/membership/content under attacks; sensitive source permissions still apply.

Do not expose vector store assuming “only numbers”. Access control and encryption remain needed.

## Embedding Inversion

Research can sometimes reconstruct or infer source text/attributes from embeddings. Exact feasibility depends model/access, but principle: embedding is derived sensitive data.

## LLM Memory vs Vector Memory

Application may store past notes as embeddings and retrieve relevant memories. The vector database is external memory system; LLM weights do not update when inserting memory.

Architecture:

```text
conversation/event
→ text record
→ embedding/index
future query
→ retrieve record
→ context
→ LLM
```

This distinction prevents anthropomorphic “LLM remembered permanently” confusion.

## Knowledge Graph + Embedding

Knowledge graph stores explicit entities/relations; embeddings support fuzzy semantic lookup. Hybrid GraphRAG-like systems may retrieve graph neighborhoods + vector passages.

Explicit relation and dense similarity complement each other.

## Mental Model

```text
Token embedding      = initial learned code for token identity
Contextual hidden    = token representation after context computation
Retrieval embedding  = compressed text representation trained so distance is useful
```

All are vectors, but vector purpose comes from objective.

## Common Misconceptions

### “Any LLM hidden state can go into vector DB for semantic search”

Possible but not necessarily effective; dedicated retrieval objective matters.

### “Vector distance gives probability relevance”

No. Score needs empirical calibration if probability required.

### “Embedding removes sensitive text”

No. Treat embeddings derived from sensitive data as sensitive.

### “Bigger embedding dimension always improves RAG”

Quality/storage/ANN trade-off; retrieval errors often dominated chunking/data/reranking rather than dimension.

## Knowledge Connection

Xem [Contextual Embeddings](../07_natural_language_processing/04_contextual_embeddings.md), [Information Retrieval](../07_natural_language_processing/08_search_and_information_retrieval.md), and later `09_retrieval_and_rag/`.