# Language as Data: làm sao biến ngôn ngữ thành đối tượng tính toán?

Natural Language Processing (NLP / 자연어 처리 / xử lý ngôn ngữ tự nhiên) bắt đầu với một tension: language là symbolic, contextual, ambiguous và socially grounded, trong khi computer cần discrete codes/numbers/tensors. Bước đầu tiên không phải chọn Transformer; nó là quyết định **ta đang coi language là loại dữ liệu gì và giữ/mất structure nào khi biểu diễn**.

## Text không phải meaning

Một string như:

```text
bank
```

có thể nghĩa ngân hàng hoặc bờ sông. Raw characters không chứa sense explicit; meaning phụ thuộc context, world knowledge và usage.

NLP system xử lý observable forms và học statistical/structured relationships để infer useful representations. “Understanding” cần được đánh giá qua capabilities, không assume từ fluency.

## Các level của linguistic structure

Language có nhiều tầng tương tác:

- **phonetics/phonology**: âm thanh;
- **morphology (형태론)**: cấu tạo từ/morpheme;
- **syntax (통사론)**: cấu trúc câu;
- **semantics (의미론)**: meaning;
- **pragmatics (화용론)**: meaning trong context/intention;
- **discourse**: relation across sentences/document.

Modern models thường learn nhiều tầng jointly, nhưng terminology giúp diagnose tasks/failures.

## Token, Type, Vocabulary

**Token** là một occurrence trong text sau segmentation.

**Type** là unique token category.

Vocabulary `V` là set token types model recognizes.

Nếu corpus:

```text
AI learns. AI changes.
```

`AI` xuất hiện hai tokens nhưng một type.

Subword tokenization làm “word” không còn đơn vị cơ bản bắt buộc.

## Corpus và Distribution

Corpus là collection texts. Model học distribution trong corpus, không “language universal” trực tiếp.

Corpus composition ảnh hưởng:

- dialect;
- domain;
- register;
- factual coverage;
- social bias;
- recency;
- language balance.

Dataset curation là modeling choice.

## Zipf's Law

Word frequency roughly heavy-tailed: vài words cực phổ biến, rất nhiều words hiếm.

Approx:

\[
f(r)\propto\frac1{r^s}
\]

với rank `r`.

Consequence:

- word-level vocabulary huge;
- rare/OOV words common;
- subword tokenization useful;
- frequency imbalance affects training.

## Morphology và Korean/Vietnamese/English khác nhau

English spacing khá gần word boundaries nhưng morphology vẫn có `walk`, `walked`, `walking`.

Korean is agglutinative: stem + grammatical endings/particles:

```text
먹었습니다
먹 + 었 + 습니다
```

Word-level vocabulary dễ sparse. Morphological analyzers hoặc subword tokenizers handle variants.

Vietnamese spacing separates syllables, not always semantic words:

```text
trí tuệ nhân tạo
```

contains multi-syllable lexical units. Tokenization design must respect language properties.

Universal subword models trade linguistic purity for scalable data-driven segmentation.

## Ambiguity

### Lexical ambiguity

`bank` multiple senses.

### Syntactic ambiguity

```text
I saw the man with the telescope.
```

Ai có telescope?

### Referential ambiguity

```text
John told Mike that he was late.
```

`he` refers whom?

Language modeling needs context/world priors to resolve probabilistically.

## Bag-of-Words

Early representation counts token occurrences:

\[
x_j=count(token_j)
\]

It ignores order:

```text
dog bites man
man bites dog
```

have same bag-of-words.

Despite limitation, BoW/TF-IDF remain strong interpretable baselines for many classification/search tasks.

## n-grams

n-gram captures local order:

- unigram: one token;
- bigram: two;
- trigram: three.

Classical language model:

\[
P(w_t\mid w_{<t})\approx P(w_t\mid w_{t-n+1:t-1})
\]

Markov approximation reduces complexity but sparse for large `n`.

Neural LMs replace explicit n-gram table with distributed representations and long context.

## TF-IDF

Term Frequency-Inverse Document Frequency downweights globally common terms.

Simplified:

\[
TFIDF(t,d)=TF(t,d)\cdot\log\frac{N}{DF(t)}
\]

A term frequent in one document but rare corpus-wide gets higher weight.

This is core lexical retrieval representation and remains useful alongside dense embeddings in hybrid search.

## Language as Sequence vs Graph vs Tree

Raw text is sequence, but linguistic relations can be tree/graph:

- dependency parse tree;
- constituency tree;
- coreference graph;
- semantic role graph.

Transformer does not explicitly require parse tree; attention can learn dependencies from sequence. But explicit structures still useful in constrained/explainable systems.

## Discrete Tokens → Continuous Vectors

Token IDs are arbitrary integers, not numerical magnitude. Embedding lookup maps:

\[
token\ id\rightarrow e\in R^d
\]

Now geometry can encode learned similarities. This transition from discrete symbol to continuous vector is foundational modern NLP.

## Context Window as a Data Boundary

Document may exceed model context. Chunking/truncation changes what relations model can observe.

A paragraph split away from its heading loses context; RAG chunking later inherits this issue.

Context construction is part of representation.

## Metadata

Author, timestamp, language, document title, section path and source can matter. Dropping metadata may remove useful context; injecting it carelessly may cause leakage.

NLP pipeline should distinguish content vs metadata and track provenance.

## Data Quality

Common text issues:

```text
encoding corruption
HTML boilerplate
OCR errors
duplicates
spam
auto-generated low-quality text
PII/secrets
language misclassification
```

Large language-model training quality depends heavily on filtering/deduplication, not only scale.

## Grounding

Text describes world but is not world itself. A language model learns patterns in textual observations. Factual correctness requires source quality, temporal relevance, retrieval/tools or verification.

This distinction becomes critical for hallucination.

## Mental Model

```text
World / human intent
   ↓ expressed imperfectly
Language signal
   ↓ normalization/segmentation
Tokens / structures
   ↓ vector representation
Model computation
   ↓
Prediction / generated language
```

Every arrow can lose information or introduce bias.

## Common Misconceptions

### “Words are natural atomic units”

Boundaries vary language; modern tokenization often subword/byte-based.

### “More text data always improves language model”

Quality, diversity, duplication, domain balance and contamination matter.

### “Embedding contains word meaning itself”

Embedding encodes statistical/task-dependent relations, not complete grounded meaning.

### “Transformer made classical text representations useless”

TF-IDF/BM25 remain excellent lexical retrieval/baselines and combine well with dense models.

## Knowledge Connection

Language representation connects [Sequence Models](../06_deep_learning_architectures/01_sequence_models.md), [Representation Learning](../05_neural_networks/08_representation_learning.md), Probability and Information Theory.

Xem tiếp: [Text Normalization and Tokenization](./01_text_normalization_and_tokenization.md).