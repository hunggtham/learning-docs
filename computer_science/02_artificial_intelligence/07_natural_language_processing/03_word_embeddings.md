# Word Embeddings: từ discrete words tới continuous semantic geometry

Word Embedding (단어 임베딩 / nhúng từ) maps discrete lexical units thành dense vectors. Trước embeddings, one-hot representation coi mọi words equally unrelated. Embeddings cho model học geometry nơi words xuất hiện trong similar contexts có vectors liên quan.

Đây là bước lịch sử quan trọng từ symbolic sparse NLP sang distributed representation, và là nền trực tiếp của token embeddings trong LLM.

## One-Hot Limitation

Vocabulary size `V`. Word `i` one-hot:

\[
e_i\in R^V
\]

với một `1`, còn lại `0`.

Dot product giữa hai different words luôn zero. `cat` không gần `dog` hơn `database` về geometry.

Dense embedding:

\[
v_w\in R^d,\quad d\ll V
\]

cho phép learned similarities.

## Distributional Hypothesis

> “You shall know a word by the company it keeps.”

Words xuất hiện trong similar contexts thường có related meaning/function.

Embedding methods operationalize principle này từ co-occurrence/prediction.

Nhưng distributional similarity không equal semantic identity: antonyms như `hot` và `cold` xuất hiện contexts giống nhau nên vectors có thể gần.

## Word2Vec: Skip-Gram

Given center word `w`, predict context words `c`:

\[
P(c\mid w)=\frac{\exp(v_c'^Tv_w)}{\sum_{j\in V}\exp(v_j'^Tv_w)}
\]

Full softmax expensive vocabulary lớn.

Skip-gram learns word vector useful để predict neighbors.

## CBOW

Continuous Bag-of-Words predicts center word from surrounding context embeddings.

Conceptually:

```text
context words → aggregate embeddings → predict center
```

CBOW often faster; Skip-Gram historically strong rare-word representations.

## Negative Sampling

Thay full vocabulary softmax, train binary discrimination real `(word,context)` vs sampled negatives.

Objective roughly:

\[
\log\sigma(v_c'^Tv_w)
+
\sum_{k=1}^{K}\log\sigma(-v_{n_k}'^Tv_w)
\]

This drastically reduces compute.

Negative sampling is not merely approximation detail; negative distribution influences learned geometry.

## PMI Connection

Skip-gram negative sampling has theoretical connection to factorizing shifted Pointwise Mutual Information matrix.

PMI:

\[
PMI(w,c)=\log\frac{P(w,c)}{P(w)P(c)}
\]

measures how much more often pair co-occurs than independence expectation.

This links predictive embeddings to classical count-based matrix factorization.

## GloVe

GloVe (Global Vectors) directly uses global co-occurrence counts. It learns vectors such that dot products relate log co-occurrence ratios/statistics.

Word2Vec emphasizes local predictive objective; GloVe global count structure. Both produce static word vectors.

## Cosine Similarity

\[
cos(a,b)=\frac{a^Tb}{\|a\|\|b\|}
\]

often used because direction captures relation independent magnitude.

But whether cosine is best depends training objective. Modern embedding models may be optimized specifically for dot product/cosine.

## Vector Analogies

Famous:

\[
king-man+woman\approx queen
\]

shows some relations encoded as approximately linear directions.

Không nên overgeneralize: analogy behavior varies corpus/preprocessing and many semantic relations are not simple global vector offsets.

## Static Embedding Limitation: Polysemy

`bank` has one Word2Vec vector regardless context:

```text
bank loan
river bank
```

Static vector averages senses.

Contextual embeddings solve by compute representation conditioned on sentence.

## Subword Embeddings: fastText

fastText represents word using character n-grams, helping rare/morphological words.

Example Korean/Vietnamese/inflected words can share subword components.

It can form vectors for unseen words from n-grams, unlike fixed whole-word lookup.

## Embedding Matrix in Neural Networks

Learnable embedding layer:

\[
E\in R^{V\times d}
\]

Token ID selects row:

\[
x_t=E[token_t]
\]

This is mathematically equivalent one-hot multiply:

\[
e_t^TE
\]

but lookup efficient.

During training, gradients update rows corresponding tokens (and through tied/shared mechanisms).

## Frequency Effects

Frequent words get many updates; rare words few. Embedding norms/directions can correlate frequency.

Subsampling very frequent words in Word2Vec reduces dominance of stopword-like contexts.

Bias in corpus also appears geometry: gender/profession/social associations can be encoded.

## Debiasing Limitations

Removing one “gender direction” can reduce a measured association but not erase distributed social bias. Bias is multi-dimensional and downstream behavior depends model/context.

Embedding fairness requires evaluation, not simple projection fix.

## Embeddings for Documents

Average word vectors is simple document representation but loses order/context.

Doc2Vec historically extended distributed representation. Modern sentence/document encoders use contextual Transformers + pooling/contrastive training.

## Embeddings and Search

If query/document represented in same space:

\[
score(q,d)=q^Td
\]

nearest-neighbor search retrieves semantically related docs.

Static word embeddings alone usually insufficient modern retrieval; sentence embedding models train at query-document level.

Still, core geometry principle begins here.

## Mental Model

> Embedding turns “identity of symbol” into “location/direction in learned relation space”. Geometry gets meaning only because training objective + data shape it.

## Common Misconceptions

### “Each dimension corresponds a human-readable semantic attribute”

Usually representation distributed; axes arbitrary up to transformations.

### “Cosine near 1 means synonyms”

It means vectors aligned under learned geometry; antonyms/contextually similar words can also align.

### “Word2Vec understands context”

Training uses context, but final word vector is static across usages.

### “Embeddings are objective semantic truth”

They encode corpus/objective biases and omissions.

## Knowledge Connection

Word embeddings connect [Representation Learning](../05_neural_networks/08_representation_learning.md), [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), and lead to [Contextual Embeddings](./04_contextual_embeddings.md).