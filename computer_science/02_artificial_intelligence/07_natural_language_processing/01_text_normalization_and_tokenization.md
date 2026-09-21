# Text Normalization và Tokenization

Text model không nhận trực tiếp “câu”. Nó nhận một sequence discrete IDs. **Normalization (정규화)** quyết định canonical form của raw text; **tokenization (토큰화)** quyết định cách chia text thành units và map chúng vào vocabulary.

Đây là infrastructure layer cực quan trọng: tokenization ảnh hưởng sequence length, multilingual fairness, context cost, vocabulary size, OOV behavior, code handling và generation boundary.

## Unicode trước khi nói tokenization

Text là Unicode code points được encode thành bytes như UTF-8. Cùng visual character có thể có multiple Unicode compositions.

Ví dụ accented character có thể precomposed hoặc base + combining mark. Unicode normalization forms:

- NFC: canonical compose;
- NFD: canonical decompose;
- NFKC/NFKD: compatibility normalization, có thể merge distinctions.

Không nên blindly NFKC nếu distinctions matter, e.g. symbols/code/user identifiers.

## Case Folding

Lowercasing reduces vocabulary sparsity:

```text
Apple → apple
```

nhưng mất distinction:

```text
US vs us
Apple company vs apple fruit
```

Modern foundation models often preserve case and let tokenizer/model learn pattern.

## Punctuation và whitespace

Old pipelines often remove punctuation/stopwords. For LLMs this can destroy grammar, code, numbers and style information.

Modern tokenizers generally preserve much surface form, sometimes encode leading-space behavior explicitly.

Whitespace matters in Python/code and document structure.

## Word-level Tokenization

Split words then assign IDs.

Advantages: intuitive semantic units.

Problems:

- huge vocabulary;
- OOV rare/new words;
- morphology explosion;
- multilingual scripts.

Unknown words map `<UNK>`, losing internal structure.

## Character-level Tokenization

Vocabulary small and no word OOV, but sequences much longer. Model must learn morphology/word structure from many steps.

Trade-off:

```text
smaller vocabulary ↔ longer sequences
larger units       ↔ more OOV/sparsity
```

Subword methods find middle ground.

## Byte-level Tokenization

Represent UTF-8 bytes, vocabulary base ≤256 symbols plus merges/special tokens. Any string representable, no `<UNK>` needed.

But non-ASCII languages may use multiple bytes per character, increasing raw length before merges.

Byte-level BPE-like tokenizers can still learn common multi-byte sequences into larger tokens.

## Byte Pair Encoding (BPE)

Start with small symbols, repeatedly merge frequent adjacent pairs.

Toy corpus:

```text
low lower newest widest
```

Frequent pair merges create subwords.

At inference, word decomposes into known subword units.

BPE vocabulary size is design trade-off:

- larger vocab → shorter sequence, bigger embedding/output matrices;
- smaller vocab → longer sequence, finer reuse.

## WordPiece

WordPiece also builds subwords but merge/selection criterion differs from plain BPE, historically used in BERT family.

Typical visual convention:

```text
play ##ing
```

`##` indicates continuation in one implementation, not universal concept.

## Unigram Language Model Tokenization

SentencePiece Unigram starts large candidate vocabulary and removes pieces optimizing probabilistic segmentation likelihood.

A string may have multiple possible segmentations; tokenizer chooses high-probability one, and subword regularization can sample alternatives during training.

## SentencePiece

SentencePiece operates raw text independent of whitespace-token preprocessor and supports BPE/Unigram variants. Whitespace can be encoded as special visible marker such as `▁`.

Useful multilingual languages where word segmentation rules differ.

## Tokenization là learned compression scheme

Common strings become longer token pieces; rare patterns decompose smaller. Thus tokenizer allocates vocabulary capacity according to corpus frequency.

This creates distributional bias: languages underrepresented during tokenizer training may require more tokens per sentence, increasing cost/context usage.

## Multilingual Token Efficiency

Nếu English phrase 10 tokens nhưng Vietnamese/Korean equivalent 18 tokens, same semantic content consumes more context and inference compute.

Tokenizer quality can affect multilingual performance/cost, even before model architecture.

Measure tokens per character/word/content across target languages when deploying multilingual systems.

## Korean Tokenization

Korean agglutinative forms make pure whitespace word vocabulary sparse. Subwords handle stems/endings statistically.

Morphological analyzer can explicitly segment morphemes, useful classical NLP, but large multilingual LMs often use general subword/byte tokenization to avoid language-specific pipelines.

Choice depends model/data/task.

## Vietnamese Tokenization

Vietnamese spaces separate syllables, while lexical word can contain multiple syllables:

```text
trí_tuệ
nhân_tạo
```

Classical Vietnamese NLP may word-segment first. Subword LM can learn frequent multi-syllable patterns without explicit segmentation, but efficiency/quality depends corpus.

## Numbers

Tokenizer may split:

```text
20260920
```

into arbitrary digit groups. Arithmetic semantics are not guaranteed from tokenization.

Different numbers sharing digit patterns may generalize poorly. Some models/tools use specialized numerical representations or external calculator/code execution.

## Code Tokenization

Programming language needs punctuation, indentation, identifiers and whitespace. Tokenizer trained mostly natural language may fragment code identifiers inefficiently.

Code-focused models benefit tokenizer/data distribution covering code syntax and common identifier substrings.

## Special Tokens

Examples:

```text
<BOS> beginning
<EOS> end
<PAD> padding
<MASK> masked modeling
<SEP> separator
```

Chat models add role/control tokens delimiting system/user/assistant turns.

These tokens are part model protocol. Manually formatting prompt incorrectly can change behavior because model sees different token sequence than training format.

## Vocabulary IDs are arbitrary

Token ID `50256` is not numerically “larger meaning” than token ID `42`. IDs index embedding rows.

Never feed raw token IDs as continuous scalar features.

## Tokenization and Context Window

Context limit measured tokens, not characters/words.

Document chunking must inspect actual tokenizer. “500 words” may vary token count widely by language/content.

Code/JSON tables often tokenize differently from prose.

## Tokenization and Generation

Model predicts token, not word/character directly.

A generated word may require multiple decoding steps. Probability of string is product over its tokenization sequence.

Tokenizer boundaries affect sampling behavior and log-prob analysis.

## Unknown / Invalid Byte Handling

Byte fallback guarantees arbitrary Unicode strings, but decoded partial byte sequences during intermediate token stream may temporarily be invalid UTF-8. Libraries should decode through tokenizer, not concatenate guessed token strings naïvely.

## Normalization and Security

Unicode confusables:

```text
Latin a vs Cyrillic а
```

look similar but different code points. Attackers can exploit homoglyphs, zero-width chars or normalization edge cases.

Security-sensitive text pipelines need Unicode-aware canonicalization/detection policies without destroying legitimate multilingual text.

## Tokenizer Training Leakage

Tokenizer vocabulary itself can reveal frequency patterns/corpus artifacts, though much less than model parameters. More importantly, tokenizer trained using future/test corpus can be a subtle data-processing dependency; evaluation reproducibility should version tokenizer.

## Tokenizer Version = Model Compatibility

Embedding/output matrices indexed vocabulary. Change token IDs/vocabulary without retraining breaks model semantics.

Tokenizer is part of model artifact and must version/deploy together.

## Mental Model

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

Tokenization is a lossy/structuring interface between human text and model computation, though modern byte-based schemes preserve raw content reversibly more often.

## Common Misconceptions

### “1 token ≈ 1 word”

Không. Subword/byte tokenization varies by language/string.

### “Tokenizer only affects speed, not quality”

It affects sequence length, morphology sharing, multilingual efficiency and boundaries the model predicts.

### “Lowercase/remove punctuation always cleans text”

For modern LMs it can destroy meaningful syntax/context.

### “Can swap tokenizer if vocabulary size same”

No. Token IDs/segmentations must match trained embedding/output matrices exactly.

## Knowledge Connection

Tokenization prepares [Language Models](./02_language_models.md), [Word Embeddings](./03_word_embeddings.md) and later LLM tokenization/context engineering.