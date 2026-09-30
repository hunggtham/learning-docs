# Ngôn ngữ (language / 언어) as dữ liệu (data / 데이터): làm sao biến ngôn ngữ thành đối tượng tính toán?

> **Mạch đọc:** Đặt **ngôn ngữ (language / 언어) as dữ liệu (data / 데이터): làm sao biến ngôn ngữ thành đối tượng tính toán?** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **văn bản (text / 텍스트) không phải meaning** sang **Các mức (level / 수준) của linguistic cấu trúc (structure / 구조)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Natural ngôn ngữ (language / 언어) Processing (NLP / 자연어 처리 / xử lý ngôn ngữ tự nhiên) bắt đầu với một tension: ngôn ngữ (language / 언어) là symbolic, contextual, ambiguous và socially grounded, trong khi computer cần discrete codes/numbers/tensors. Bước đầu tiên không phải chọn Transformer; nó là quyết định **ta đang coi ngôn ngữ (language / 언어) là loại dữ liệu gì và giữ/mất cấu trúc (structure / 구조) nào khi biểu diễn**.

## Văn bản (text / 텍스트) không phải meaning

Một string như:

```text
bank
```

có thể nghĩa ngân hàng hoặc bờ sông. Raw characters không chứa sense tường minh (explicit / 명시적); meaning phụ thuộc ngữ cảnh (context / 맥락), world kiến thức (knowledge / 지식) và usage.

NLP hệ thống (system / 시스템) xử lý observable forms và học statistical/structured relationships để infer useful representations. “Understanding” cần được đánh giá qua capabilities, không assume từ fluency.

## Các mức (level / 수준) của linguistic cấu trúc (structure / 구조)

Ngôn ngữ (language / 언어) có nhiều tầng tương tác:

- **phonetics/phonology**: âm thanh;
- **morphology (형태론)**: cấu tạo từ/morpheme;
- **cú pháp (syntax / 문법)**: cấu trúc câu;
- **ngữ nghĩa (semantics / 의미론)**: meaning;
- **pragmatics (화용론)**: meaning trong ngữ cảnh (context / 맥락)/intention;
- **discourse**: quan hệ (relation / 관계) across sentences/document.

Hiện đại (modern / 현대적) các mô hình (models / 모델들) thường learn nhiều tầng jointly, nhưng terminology giúp diagnose tasks/failures.

## Đơn vị từ (token / 토큰), kiểu (type / 타입), Vocabulary

**đơn vị từ (token / 토큰)** là một occurrence trong văn bản (text / 텍스트) sau segmentation.

**kiểu (type / 타입)** là unique đơn vị từ (token / 토큰) category.

Vocabulary `V` là set đơn vị từ (token / 토큰) types mô hình (model / 모델) recognizes.

Nếu corpus:

```text
AI learns. AI changes.
```

`AI` xuất hiện hai tokens nhưng một kiểu (type / 타입).

Subword tokenization làm “word” không còn đơn vị cơ bản bắt buộc.

## Corpus và phân phối (distribution / 분포)

Corpus là collection texts. mô hình (model / 모델) học phân phối (distribution / 분포) trong corpus, không “ngôn ngữ (language / 언어) universal” trực tiếp.

Corpus composition ảnh hưởng:

- dialect;
- lĩnh vực (domain / 도메인);
- register;
- factual coverage;
- xã hội (social / 사회적) độ lệch (bias / 편향);
- recency;
- ngôn ngữ (language / 언어) balance.

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
- rare/OOV words dùng chung (common / 공통);
- subword tokenization useful;
- frequency imbalance affects huấn luyện (training / 학습).

## Morphology và Korean/Vietnamese/English khác nhau

English spacing khá gần word boundaries nhưng morphology vẫn có `walk`, `walked`, `walking`.

Korean is agglutinative: stem + grammatical endings/particles:

```text
먹었습니다
먹 + 었 + 습니다
```

Word-level vocabulary dễ sparse. Morphological analyzers hoặc subword tokenizers handle variants.

Vietnamese spacing separates syllables, not always ngữ nghĩa (semantic / 의미적) words:

```text
trí tuệ nhân tạo
```

contains multi-syllable lexical units. Tokenization thiết kế (design / 설계) must respect ngôn ngữ (language / 언어) properties.

Universal subword các mô hình (models / 모델들) trade linguistic purity for scalable data-driven segmentation.

## Ambiguity

### Lexical ambiguity

`bank` multiple senses.

### Syntactic ambiguity

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
I saw the man with the telescope.
```

Ai có telescope?

### Referential ambiguity

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
John told Mike that he was late.
```

`he` refers whom?

Ngôn ngữ (language / 언어) modeling needs ngữ cảnh (context / 맥락)/world priors to resolve probabilistically.

## Bag-of-Words

Early biểu diễn (representation / 표현) counts đơn vị từ (token / 토큰) occurrences:

\[
x_j=count(token_j)
\]

It ignores thứ tự (order / 순서):

```text
dog bites man
man bites dog
```

have same bag-of-words.

Despite limitation, BoW/TF-IDF remain strong interpretable baselines for many classification/tìm kiếm (search / 검색) tasks.

## n-grams

n-gram captures cục bộ (local / 로컬) thứ tự (order / 순서):

- unigram: one đơn vị từ (token / 토큰);
- bigram: two;
- trigram: three.

Classical ngôn ngữ (language / 언어) mô hình (model / 모델):

\[
P(w_t\mid w_{<t})\approx P(w_t\mid w_{t-n+1:t-1})
\]

Markov approximation reduces độ phức tạp (complexity / 복잡도) but sparse for large `n`.

Neural LMs replace tường minh (explicit / 명시적) n-gram bảng (table / 테이블) with phân tán (distributed / 분산) representations and long ngữ cảnh (context / 맥락).

## TF-IDF

Term Frequency-Inverse Document Frequency downweights globally dùng chung (common / 공통) terms.

Simplified:

\[
TFIDF(t,d)=TF(t,d)\cdot\log\frac{N}{DF(t)}
\]

A term frequent in one document but rare corpus-wide gets higher weight.

This is cốt lõi (core / 핵심) lexical retrieval biểu diễn (representation / 표현) and remains useful alongside dense embeddings in hybrid tìm kiếm (search / 검색).

## Ngôn ngữ (language / 언어) as chuỗi (sequence / 시퀀스) vs đồ thị (graph / 그래프) vs cây (tree / 트리)

Raw văn bản (text / 텍스트) is chuỗi (sequence / 시퀀스), but linguistic relations can be cây (tree / 트리)/đồ thị (graph / 그래프):

- phụ thuộc (dependency / 의존성) parse cây (tree / 트리);
- constituency cây (tree / 트리);
- coreference đồ thị (graph / 그래프);
- ngữ nghĩa (semantic / 의미적) role đồ thị (graph / 그래프).

Transformer does not explicitly require parse cây (tree / 트리); attention can learn dependencies from chuỗi (sequence / 시퀀스). But tường minh (explicit / 명시적) structures still useful in constrained/explainable các hệ thống (systems / 시스템들).

## Discrete Tokens → Continuous Vectors

Đơn vị từ (token / 토큰) IDs are arbitrary integers, not numerical magnitude. Embedding lookup maps:

\[
đơn vị từ (token / 토큰)\ id\rightarrow e\in R^d
\]

Now hình học (geometry / 기하학) can encode learned similarities. This chuyển tiếp (transition / 전이) from discrete symbol to continuous véc-tơ (vector / 벡터) is foundational hiện đại (modern / 현대적) NLP.

## Ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우) as a dữ liệu (data / 데이터) ranh giới (boundary / 경계)

Document may exceed mô hình (model / 모델) ngữ cảnh (context / 맥락). Chunking/truncation changes what relations mô hình (model / 모델) can observe.

A paragraph split away from its heading loses ngữ cảnh (context / 맥락); RAG chunking later inherits this issue.

Ngữ cảnh (context / 맥락) construction is part of biểu diễn (representation / 표현).

## Siêu dữ liệu (metadata / 메타데이터)

Author, timestamp, ngôn ngữ (language / 언어), document title, section đường dẫn (path / 경로) and nguồn (source / 소스) can matter. Dropping siêu dữ liệu (metadata / 메타데이터) may remove useful ngữ cảnh (context / 맥락); injecting it carelessly may cause leakage.

NLP chuỗi xử lý (pipeline / 파이프라인) should distinguish content vs siêu dữ liệu (metadata / 메타데이터) and nhánh học (track / 트랙) provenance.

## Dữ liệu (data / 데이터) chất lượng (quality / 품질)

Dùng chung (common / 공통) văn bản (text / 텍스트) issues:

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

Large language-model huấn luyện (training / 학습) chất lượng (quality / 품질) depends heavily on filtering/deduplication, not only quy mô (scale / 규모).

## Grounding

Văn bản (text / 텍스트) describes world but is not world itself. A ngôn ngữ (language / 언어) mô hình (model / 모델) learns patterns in textual observations. Factual tính đúng đắn (correctness / 정확성) requires nguồn (source / 소스) chất lượng (quality / 품질), temporal relevance, retrieval/tools or xác minh (verification / 확인).

This distinction becomes trọng yếu (critical / 중요) for hallucination.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

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

Every arrow can lose thông tin (information / 정보) or introduce độ lệch (bias / 편향).

## Dùng chung (common / 공통) Misconceptions

### “Words are natural atomic units”

Boundaries vary ngôn ngữ (language / 언어); hiện đại (modern / 현대적) tokenization often subword/byte-based.

### “More văn bản (text / 텍스트) dữ liệu (data / 데이터) always improves ngôn ngữ (language / 언어) mô hình (model / 모델)”

Chất lượng (quality / 품질), diversity, duplication, lĩnh vực (domain / 도메인) balance and contamination matter.

### “Embedding contains word meaning itself”

Embedding encodes statistical/task-dependent relations, not complete grounded meaning.

### “Transformer made classical văn bản (text / 텍스트) representations useless”

TF-IDF/BM25 remain excellent lexical retrieval/baselines and combine well with dense các mô hình (models / 모델들).

## Liên kết kiến thức (knowledge connection / 지식 연결)

Ngôn ngữ (language / 언어) biểu diễn (representation / 표현) connects [Sequence Models](../06_deep_learning_architectures/01_sequence_models.md), [Representation Learning](../05_neural_networks/08_representation_learning.md), xác suất (probability / 확률) and thông tin (information / 정보) lý thuyết (theory / 이론).

Xem tiếp: [Text Normalization and Tokenization](./01_text_normalization_and_tokenization.md).
