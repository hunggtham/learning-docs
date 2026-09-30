# Văn bản (text / 텍스트) Normalization và Tokenization

> **Mạch đọc:** Đặt **văn bản (text / 텍스트) Normalization và Tokenization** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Unicode trước khi nói tokenization** sang **trường hợp (case / 사례) Folding**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Văn bản (text / 텍스트) mô hình (model / 모델) không nhận trực tiếp “câu”. Nó nhận một chuỗi (sequence / 시퀀스) discrete IDs. **Normalization (정규화)** quyết định chuẩn gốc (canonical / 정본) form của raw văn bản (text / 텍스트); **tokenization (토큰화)** quyết định cách chia văn bản (text / 텍스트) thành units và map chúng vào vocabulary.

Đây là hạ tầng (infrastructure / 인프라) tầng (layer / 계층) cực quan trọng: tokenization ảnh hưởng chuỗi (sequence / 시퀀스) length, multilingual fairness, ngữ cảnh (context / 맥락) chi phí (cost / 비용), vocabulary kích thước (size / 크기), OOV hành vi (behavior / 동작), mã (code / 코드) handling và generation ranh giới (boundary / 경계).

## Unicode trước khi nói tokenization

Văn bản (text / 텍스트) là Unicode mã (code / 코드) points được encode thành bytes như UTF-8. Cùng visual character có thể có multiple Unicode compositions.

Ví dụ accented character có thể precomposed hoặc cơ sở (base / 기반) + combining mark. Unicode normalization forms:

- NFC: chuẩn gốc (canonical / 정본) compose;
- NFD: chuẩn gốc (canonical / 정본) decompose;
- NFKC/NFKD: tính tương thích (compatibility / 호환성) normalization, có thể merge distinctions.

Không nên blindly NFKC nếu distinctions matter, e.g. symbols/mã (code / 코드)/người dùng (user / 사용자) identifiers.

## Trường hợp (case / 사례) Folding

Lowercasing reduces vocabulary sparsity:

```text
Apple → apple
```

nhưng mất distinction:

```text
US vs us
Apple company vs apple fruit
```

Hiện đại (modern / 현대적) foundation các mô hình (models / 모델들) often preserve trường hợp (case / 사례) and let tokenizer/mô hình (model / 모델) learn mẫu (pattern / 패턴).

## Punctuation và whitespace

Old pipelines often remove punctuation/stopwords. For LLMs this can destroy grammar, mã (code / 코드), numbers and style thông tin (information / 정보).

Hiện đại (modern / 현대적) tokenizers generally preserve much surface form, sometimes encode leading-space hành vi (behavior / 동작) explicitly.

Whitespace matters in Python/mã (code / 코드) and document cấu trúc (structure / 구조).

## Word-level Tokenization

Split words then assign IDs.

Advantages: intuitive ngữ nghĩa (semantic / 의미적) units.

Problems:

- huge vocabulary;
- OOV rare/new words;
- morphology explosion;
- multilingual scripts.

Unknown words map `<UNK>`, losing nội bộ (internal / 내부) cấu trúc (structure / 구조).

## Character-level Tokenization

Vocabulary small and no word OOV, but sequences much longer. mô hình (model / 모델) must learn morphology/word cấu trúc (structure / 구조) from many steps.

Sự đánh đổi (trade-off / 트레이드오프):

```text
smaller vocabulary ↔ longer sequences
larger units       ↔ more OOV/sparsity
```

Subword methods find middle ground.

## Byte-level Tokenization

Represent UTF-8 bytes, vocabulary cơ sở (base / 기반) ≤256 symbols plus merges/special tokens. Any string representable, no `<UNK>` needed.

But non-ASCII languages may use multiple bytes per character, increasing raw length before merges.

Byte-level BPE-like tokenizers can still learn dùng chung (common / 공통) multi-byte sequences into larger tokens.

## Byte Pair Encoding (BPE)

Start with small symbols, repeatedly merge frequent adjacent pairs.

Toy corpus:

```text
low lower newest widest
```

Frequent pair merges create subwords.

At suy luận (inference / 추론), word decomposes into known subword units.

BPE vocabulary kích thước (size / 크기) is thiết kế (design / 설계) sự đánh đổi (trade-off / 트레이드오프):

- larger vocab → shorter chuỗi (sequence / 시퀀스), bigger embedding/đầu ra (output / 출력) matrices;
- smaller vocab → longer chuỗi (sequence / 시퀀스), finer reuse.

## WordPiece

WordPiece also builds subwords but merge/selection criterion differs from plain BPE, historically used in BERT family.

Typical visual convention:

```text
play ##ing
```

`##` indicates continuation in one hiện thực (implementation / 구현), not universal concept.

## Unigram ngôn ngữ (language / 언어) mô hình (model / 모델) Tokenization

SentencePiece Unigram starts large candidate vocabulary and removes pieces optimizing probabilistic segmentation likelihood.

A string may have multiple possible segmentations; tokenizer chooses high-probability one, and subword regularization can mẫu (sample / 표본) alternatives during huấn luyện (training / 학습).

## SentencePiece

SentencePiece operates raw văn bản (text / 텍스트) independent of whitespace-token preprocessor and supports BPE/Unigram variants. Whitespace can be encoded as special visible marker such as `▁`.

Useful multilingual languages where word segmentation rules differ.

## Tokenization là learned compression scheme

Dùng chung (common / 공통) strings become longer đơn vị từ (token / 토큰) pieces; rare patterns decompose smaller. Thus tokenizer allocates vocabulary sức chứa (capacity / 용량) according to corpus frequency.

This creates distributional độ lệch (bias / 편향): languages underrepresented during tokenizer huấn luyện (training / 학습) may require more tokens per sentence, increasing chi phí (cost / 비용)/ngữ cảnh (context / 맥락) usage.

## Multilingual đơn vị từ (token / 토큰) Efficiency

Nếu English phrase 10 tokens nhưng Vietnamese/Korean equivalent 18 tokens, same ngữ nghĩa (semantic / 의미적) content consumes more ngữ cảnh (context / 맥락) and suy luận (inference / 추론) compute.

Tokenizer chất lượng (quality / 품질) can affect multilingual hiệu năng (performance / 성능)/chi phí (cost / 비용), even before mô hình (model / 모델) kiến trúc (architecture / 아키텍처).

Measure tokens per character/word/content across mục tiêu (target / 대상) languages when deploying multilingual các hệ thống (systems / 시스템들).

## Korean Tokenization

Korean agglutinative forms make pure whitespace word vocabulary sparse. Subwords handle stems/endings statistically.

Morphological analyzer can explicitly segment morphemes, useful classical NLP, but large multilingual LMs often use general subword/byte tokenization to avoid language-specific pipelines.

Choice depends mô hình (model / 모델)/dữ liệu (data / 데이터)/tác vụ (task / 작업).

## Vietnamese Tokenization

Vietnamese spaces separate syllables, while lexical word can contain multiple syllables:

```text
trí_tuệ
nhân_tạo
```

Classical Vietnamese NLP may word-segment first. Subword LM can learn frequent multi-syllable patterns without tường minh (explicit / 명시적) segmentation, but efficiency/chất lượng (quality / 품질) depends corpus.

## Numbers

Tokenizer may split:

```text
20260920
```

into arbitrary digit groups. Arithmetic ngữ nghĩa (semantics / 의미론) are not guaranteed from tokenization.

Different numbers sharing digit patterns may generalize poorly. Some các mô hình (models / 모델들)/tools use specialized numerical representations or bên ngoài (external / 외부) calculator/mã (code / 코드) thực thi (execution / 실행).

## Mã (code / 코드) Tokenization

Programming ngôn ngữ (language / 언어) needs punctuation, indentation, identifiers and whitespace. Tokenizer trained mostly natural ngôn ngữ (language / 언어) may fragment mã (code / 코드) identifiers inefficiently.

Code-focused các mô hình (models / 모델들) benefit tokenizer/dữ liệu (data / 데이터) phân phối (distribution / 분포) covering mã (code / 코드) cú pháp (syntax / 문법) and dùng chung (common / 공통) identifier substrings.

## Special Tokens

Examples:

```text
<BOS> beginning
<EOS> end
<PAD> padding
<MASK> masked modeling
<SEP> separator
```

Chat các mô hình (models / 모델들) add role/điều khiển (control / 제어) tokens delimiting hệ thống (system / 시스템)/người dùng (user / 사용자)/assistant turns.

These tokens are part mô hình (model / 모델) giao thức (protocol / 프로토콜). Manually formatting prompt incorrectly can thay đổi (change / 변경) hành vi (behavior / 동작) because mô hình (model / 모델) sees different đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스) than huấn luyện (training / 학습) format.

## Vocabulary IDs are arbitrary

Đơn vị từ (token / 토큰) ID `50256` is not numerically “larger meaning” than đơn vị từ (token / 토큰) ID `42`. IDs chỉ mục (index / 인덱스) embedding rows.

Never feed raw đơn vị từ (token / 토큰) IDs as continuous scalar features.

## Tokenization and ngữ cảnh (context / 맥락) cửa sổ (window / 윈도우)

Ngữ cảnh (context / 맥락) limit measured tokens, not characters/words.

Document chunking must inspect actual tokenizer. “500 words” may vary đơn vị từ (token / 토큰) count widely by ngôn ngữ (language / 언어)/content.

Mã (code / 코드)/JSON tables often tokenize differently from prose.

## Tokenization and Generation

Mô hình (model / 모델) predicts đơn vị từ (token / 토큰), not word/character directly.

A generated word may require multiple decoding steps. xác suất (probability / 확률) of string is sản phẩm (product / 제품) over its tokenization chuỗi (sequence / 시퀀스).

Tokenizer boundaries affect sampling hành vi (behavior / 동작) and log-prob phân tích (analysis / 분석).

## Unknown / Invalid Byte Handling

Byte fallback guarantees arbitrary Unicode strings, but decoded partial byte sequences during intermediate đơn vị từ (token / 토큰) stream may temporarily be invalid UTF-8. Libraries should decode through tokenizer, not concatenate guessed đơn vị từ (token / 토큰) strings naïvely.

## Normalization and bảo mật (security / 보안)

Unicode confusables:

```text
Latin a vs Cyrillic а
```

look similar but different mã (code / 코드) points. Attackers can exploit homoglyphs, zero-width chars or normalization edge cases.

Security-sensitive văn bản (text / 텍스트) pipelines need Unicode-aware canonicalization/detection policies without destroying legitimate multilingual văn bản (text / 텍스트).

## Tokenizer huấn luyện (training / 학습) Leakage

Tokenizer vocabulary itself can reveal frequency patterns/corpus artifacts, though much less than mô hình (model / 모델) parameters. More importantly, tokenizer trained using future/kiểm thử (test / 테스트) corpus can be a subtle data-processing phụ thuộc (dependency / 의존성); evaluation reproducibility should phiên bản (version / 버전) tokenizer.

## Tokenizer phiên bản (version / 버전) = mô hình (model / 모델) tính tương thích (compatibility / 호환성)

Embedding/đầu ra (output / 출력) matrices indexed vocabulary. thay đổi (change / 변경) đơn vị từ (token / 토큰) IDs/vocabulary without retraining breaks mô hình (model / 모델) ngữ nghĩa (semantics / 의미론).

Tokenizer is part of mô hình (model / 모델) sản phẩm tạo ra (artifact / 산출물) and must phiên bản (version / 버전)/deploy together.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Raw bytes / Unicode
   ↓ normalization policy
Canonical-ish text
   ↓ segmentation algorithm + learned vocabulary
Token pieces
   ↓ IDs
Embedding lookup
   ↓
Neural representations
```

Tokenization is a lossy/structuring giao diện (interface / 인터페이스) between human văn bản (text / 텍스트) and mô hình (model / 모델) computation, though hiện đại (modern / 현대적) byte-based schemes preserve raw content reversibly more often.

## Dùng chung (common / 공통) Misconceptions

### “1 đơn vị từ (token / 토큰) ≈ 1 word”

Không. Subword/byte tokenization varies by ngôn ngữ (language / 언어)/string.

### “Tokenizer only affects speed, not chất lượng (quality / 품질)”

It affects chuỗi (sequence / 시퀀스) length, morphology sharing, multilingual efficiency and boundaries the mô hình (model / 모델) predicts.

### “Lowercase/remove punctuation always cleans văn bản (text / 텍스트)”

For hiện đại (modern / 현대적) LMs it can destroy meaningful cú pháp (syntax / 문법)/ngữ cảnh (context / 맥락).

### “Can swap tokenizer if vocabulary kích thước (size / 크기) same”

No. đơn vị từ (token / 토큰) IDs/segmentations must match trained embedding/đầu ra (output / 출력) matrices exactly.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Tokenization prepares [Language Models](./02_language_models.md), [Word Embeddings](./03_word_embeddings.md) and later LLM tokenization/context engineering.
