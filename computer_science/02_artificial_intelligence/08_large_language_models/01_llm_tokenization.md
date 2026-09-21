# LLM Tokenization: sequence length, vocabulary và model economics

LLM tokenization dùng cùng subword/byte principles của NLP, nhưng ở large-scale model nó trở thành vấn đề **compute, context economics, multilingual fairness và protocol compatibility**. Một tokenizer không chỉ chia text; nó quyết định model phải thực hiện bao nhiêu autoregressive steps để biểu diễn/generate cùng content.

Xem nền: [Text Normalization and Tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md). Chapter này tập trung LLM-specific consequences.

## Token là đơn vị compute của LLM

Training/inference cost thường scale theo token count. Một câu tokenize 20 tokens thay vì 10 roughly doubles sequence positions for many operations.

Autoregressive output latency cũng proportional generated tokens because generation serial.

Therefore tokenizer efficiency affects:

```text
training FLOPs
context usage
KV cache
inference latency
API/token cost
multilingual UX
```

## Vocabulary Size Trade-off

Large vocabulary:

- shorter sequences;
- larger embedding/output matrix;
- more rare token parameters;
- softmax/output compute/memory bigger.

Small vocabulary:

- more subword reuse;
- longer sequences;
- smaller token matrices.

Optimal depends model size/data/languages.

## Byte-Level BPE

Many GPT-like tokenizers start bytes then merge frequent sequences. Any Unicode text can represent, avoiding `<UNK>`.

But scripts using multi-byte UTF-8 may need more base units before merges. Underrepresented language gets fewer efficient merges.

## Token Fertility

**Fertility** = average number tokens per word/character/content unit.

Higher fertility language consumes more context and compute for same semantic message.

For multilingual deployment, measure fertility separately Korean, Vietnamese, English and domain code/data.

## Korean/Vietnamese practical effect

Korean endings create many forms; good subword merges can reuse stem/morpheme patterns but corpus balance matters.

Vietnamese words may span syllables separated spaces; tokenizer may or may not merge common multi-syllable expressions.

Do not assume 4 characters/token English heuristic across languages.

## Chat Templates

Instruction/chat models are trained with exact serialization scheme. Example abstractly:

```text
<|system|>...
<|user|>...
<|assistant|>...
```

Special tokens delimit roles/turns.

If application manually builds prompt with wrong template, model sees distribution unlike post-training and may leak role text/behave poorly.

Always use official tokenizer/chat-template implementation when possible.

## BOS/EOS and Stop Conditions

Beginning/end tokens affect generation boundaries. Chat turn may use special end-of-turn token distinct document EOS.

Inference server stop logic must align tokens/strings. Stopping by substring can truncate legitimate text or fail with token boundary differences.

## Token Healing / Boundary Effects

Prompt ending inside a tokenizable word or with awkward whitespace can create tokenization distribution unlike training. Some systems implement token healing/re-tokenization around boundary.

This matters autocomplete/code completion more than normal chat.

## Tokenization and Numbers

Numbers split into digit chunks unpredictably. This partly explains weak exact arithmetic/counting: model operates statistical token patterns rather than native numeric datatype.

Tools/code/calculators should handle exact arithmetic when reliability required.

## Structured Data

JSON/XML/code punctuation can consume many tokens. Minified format saves tokens but may reduce readability/model reliability; pretty format uses more context.

Schema design can optimize both validity and token cost. Repeated long field names increase output tokens.

## Tokenizer and Embedding Matrix Compatibility

Model checkpoint assumes exact mapping:

\[
token\ string\leftrightarrow token\ id\leftrightarrow embedding\ row
\]

Swap tokenizer destroys semantics even if vocab size same.

Adding new tokens requires resize embedding/output matrices and training those rows; naive addition does not teach meaning.

## Special Tokens as Attack Surface

If untrusted text can inject role delimiters/special-control strings and application serializes poorly, instruction hierarchy may be confused.

Robust chat APIs should separate roles structurally and escape/encode user data according protocol rather than concatenate raw pseudo-role markup.

Tokenizer/protocol security connects prompt injection.

## Context Budget Planning

For context window `C`:

```text
system instructions
+ conversation history
+ retrieved documents
+ tool results
+ user input
+ reserved output
≤ C tokens
```

If budget exceeded, system needs truncate/summarize/retrieve selectively. Silent truncation may remove system instruction or crucial evidence depending implementation.

## Prompt Caching

Repeated prefix tokens can be cached by inference providers/servers, reducing prefill compute. Cache usually depends exact token prefix, so tiny text/template change invalidates hit.

Stable system prompt/schema organization can improve economics.

## Input vs Output Token Cost

Transformer **prefill** processes input tokens parallel-ish; **decode** generates output one by one. Same token count has different latency characteristics.

Long input increases prefill and KV cache; long output increases serial decode latency strongly.

System optimization distinguishes both.

## Mental Model

> Tokenizer is the ABI between human strings and LLM tensor computation. It defines sequence granularity, cost and protocol boundaries; changing it is closer to changing model interface than changing a text preprocessing option.

## Common Misconceptions

### “Token count is roughly word count”

Varies language/content/tokenizer dramatically.

### “Tokenizer quality only changes cost”

It affects sequence length, morphology sharing and model learning/generation difficulty.

### “Chat roles are just text labels”

They are serialized through model-specific special token/template learned during post-training.

### “Add a token and model immediately understands it”

New embedding must be trained; ID alone has no semantic meaning.

## Knowledge Connection

Xem [NLP Tokenization](../07_natural_language_processing/01_text_normalization_and_tokenization.md), [Transformer](../06_deep_learning_architectures/05_transformer.md) và later [Context Engineering](./11_prompting_and_context_engineering.md).