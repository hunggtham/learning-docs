# Word Embeddings: từ discrete words tới continuous ngữ nghĩa (semantic / 의미적) hình học (geometry / 기하학)

> **Mạch đọc:** Đặt **Word Embeddings: từ discrete words tới continuous ngữ nghĩa (semantic / 의미적) hình học (geometry / 기하학)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **One-Hot Limitation** sang **Distributional Hypothesis**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Word Embedding (단어 임베딩 / nhúng từ) maps discrete lexical units thành dense vectors. Trước embeddings, one-hot biểu diễn (representation / 표현) coi mọi words equally unrelated. Embeddings cho mô hình (model / 모델) học hình học (geometry / 기하학) nơi words xuất hiện trong similar contexts có vectors liên quan.

Đây là bước lịch sử quan trọng từ symbolic sparse NLP sang phân tán (distributed / 분산) biểu diễn (representation / 표현), và là nền trực tiếp của đơn vị từ (token / 토큰) embeddings trong LLM.

## One-Hot Limitation

Vocabulary kích thước (size / 크기) `V`. Word `i` one-hot:

\[
e_i\in R^V
\]

với một `1`, còn lại `0`.

Dot sản phẩm (product / 제품) giữa hai different words luôn zero. `cat` không gần `dog` hơn `database` về hình học (geometry / 기하학).

Dense embedding:

\[
v_w\in R^d,\quad d\ll V
\]

cho phép learned similarities.

## Distributional Hypothesis

> “You shall know a word by the company it keeps.”

Words xuất hiện trong similar contexts thường có related meaning/hàm (function / 함수).

Embedding methods operationalize principle này từ co-occurrence/prediction.

Nhưng distributional similarity không equal ngữ nghĩa (semantic / 의미적) định danh (identity / 식별자): antonyms như `hot` và `cold` xuất hiện contexts giống nhau nên vectors có thể gần.

## Word2Vec: Skip-Gram

Given center word `w`, predict ngữ cảnh (context / 맥락) words `c`:

\[
P(c\mid w)=\frac{\exp(v_c'^Tv_w)}{\sum_{j\in V}\exp(v_j'^Tv_w)}
\]

Full softmax expensive vocabulary lớn.

Skip-gram learns word véc-tơ (vector / 벡터) useful để predict neighbors.

## CBOW

Continuous Bag-of-Words predicts center word from surrounding ngữ cảnh (context / 맥락) embeddings.

Conceptually:

```text
context words → aggregate embeddings → predict center
```

CBOW often faster; Skip-Gram historically strong rare-word representations.

## Negative Sampling

Thay full vocabulary softmax, train nhị phân (binary / 이진) discrimination real `(word,context)` vs sampled negatives.

Mục tiêu (objective / 목표) roughly:

\[
\log\sigma(v_c'^Tv_w)
+
\sum_{k=1}^{K}\log\sigma(-v_{n_k}'^Tv_w)
\]

This drastically reduces compute.

Negative sampling is not merely approximation detail; negative phân phối (distribution / 분포) influences learned hình học (geometry / 기하학).

## PMI liên kết (connection / 연결)

Skip-gram negative sampling has theoretical liên kết (connection / 연결) to factorizing shifted Pointwise Mutual thông tin (information / 정보) ma trận (matrix / 행렬).

PMI:

\[
PMI(w,c)=\log\frac{P(w,c)}{P(w)P(c)}
\]

measures how much more often pair co-occurs than independence expectation.

This links predictive embeddings to classical count-based ma trận (matrix / 행렬) factorization.

## GloVe

GloVe (Global Vectors) directly uses toàn cục (global / 전역) co-occurrence counts. It learns vectors such that dot products relate log co-occurrence ratios/statistics.

Word2Vec emphasizes cục bộ (local / 로컬) predictive mục tiêu (objective / 목표); GloVe toàn cục (global / 전역) count cấu trúc (structure / 구조). Both produce static word vectors.

## Cosine Similarity

\[
cos(a,b)=\frac{a^Tb}{\|a\|\|b\|}
\]

often used because direction captures quan hệ (relation / 관계) independent magnitude.

But whether cosine is best depends huấn luyện (training / 학습) mục tiêu (objective / 목표). hiện đại (modern / 현대적) embedding các mô hình (models / 모델들) may be optimized specifically for dot sản phẩm (product / 제품)/cosine.

## Véc-tơ (vector / 벡터) Analogies

Famous:

\[
king-man+woman\approx queen
\]

shows some relations encoded as approximately tuyến tính (linear / 선형) directions.

Không nên overgeneralize: analogy hành vi (behavior / 동작) varies corpus/preprocessing and many ngữ nghĩa (semantic / 의미적) relations are not simple toàn cục (global / 전역) véc-tơ (vector / 벡터) offsets.

## Static Embedding Limitation: Polysemy

`bank` has one Word2Vec véc-tơ (vector / 벡터) regardless ngữ cảnh (context / 맥락):

```text
bank loan
river bank
```

Static véc-tơ (vector / 벡터) averages senses.

Contextual embeddings solve by compute biểu diễn (representation / 표현) conditioned on sentence.

## Subword Embeddings: fastText

fastText represents word using character n-grams, helping rare/morphological words.

Example Korean/Vietnamese/inflected words can share subword components.

It can form vectors for unseen words from n-grams, unlike fixed whole-word lookup.

## Embedding ma trận (matrix / 행렬) in Neural Networks

Learnable embedding tầng (layer / 계층):

\[
E\in R^{V\times d}
\]

Đơn vị từ (token / 토큰) ID selects row:

\[
x_t=E[token_t]
\]

This is mathematically equivalent one-hot multiply:

\[
e_t^TE
\]

but lookup efficient.

During huấn luyện (training / 학습), gradients cập nhật (update / 업데이트) rows corresponding tokens (and through tied/shared mechanisms).

## Frequency Effects

Frequent words get many updates; rare words few. Embedding norms/directions can correlate frequency.

Subsampling very frequent words in Word2Vec reduces dominance of stopword-like contexts.

Độ lệch (bias / 편향) in corpus also appears hình học (geometry / 기하학): gender/profession/xã hội (social / 사회적) associations can be encoded.

## Debiasing Limitations

Removing one “gender direction” can reduce a measured association but not erase phân tán (distributed / 분산) xã hội (social / 사회적) độ lệch (bias / 편향). độ lệch (bias / 편향) is multi-dimensional and downstream hành vi (behavior / 동작) depends mô hình (model / 모델)/ngữ cảnh (context / 맥락).

Embedding fairness requires evaluation, not simple projection fix.

## Embeddings for Documents

Average word vectors is simple document biểu diễn (representation / 표현) but loses thứ tự (order / 순서)/ngữ cảnh (context / 맥락).

Doc2Vec historically extended phân tán (distributed / 분산) biểu diễn (representation / 표현). hiện đại (modern / 현대적) sentence/document encoders use contextual Transformers + pooling/contrastive huấn luyện (training / 학습).

## Embeddings and tìm kiếm (search / 검색)

If truy vấn (query / 쿼리)/document represented in same không gian (space / 공간):

\[
score(q,d)=q^Td
\]

nearest-neighbor tìm kiếm (search / 검색) retrieves semantically related docs.

Static word embeddings alone usually insufficient hiện đại (modern / 현대적) retrieval; sentence embedding các mô hình (models / 모델들) train at query-document mức (level / 수준).

Still, cốt lõi (core / 핵심) hình học (geometry / 기하학) principle begins here.

## Mô hình tư duy (mental model / 사고 모델)

> Embedding turns “định danh (identity / 식별자) of symbol” into “location/direction in learned quan hệ (relation / 관계) không gian (space / 공간)”. hình học (geometry / 기하학) gets meaning only because huấn luyện (training / 학습) mục tiêu (objective / 목표) + dữ liệu (data / 데이터) shape it.

## Dùng chung (common / 공통) Misconceptions

### “Each dimension corresponds a human-readable ngữ nghĩa (semantic / 의미적) attribute”

Usually biểu diễn (representation / 표현) phân tán (distributed / 분산); axes arbitrary up to transformations.

### “Cosine near 1 means synonyms”

It means vectors aligned under learned hình học (geometry / 기하학); antonyms/contextually similar words can also align.

### “Word2Vec understands ngữ cảnh (context / 맥락)”

Huấn luyện (training / 학습) uses ngữ cảnh (context / 맥락), but final word véc-tơ (vector / 벡터) is static across usages.

### “Embeddings are mục tiêu (objective / 목표) ngữ nghĩa (semantic / 의미적) truth”

They encode corpus/mục tiêu (objective / 목표) biases and omissions.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Word embeddings connect [Representation Learning](../05_neural_networks/08_representation_learning.md), [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md), and lead to [Contextual Embeddings](./04_contextual_embeddings.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 language as data](./00_language_as_data.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
