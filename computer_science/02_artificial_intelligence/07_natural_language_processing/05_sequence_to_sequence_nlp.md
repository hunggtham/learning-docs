# Sequence-to-Sequence NLP: từ Translation tới Text-to-Text Learning

Sequence-to-Sequence (Seq2Seq / 시퀀스-투-시퀀스) NLP xử lý tasks nơi input là một sequence và output là một sequence khác có thể khác length/alignment. Translation, summarization, grammatical correction, question generation và many structured-to-text tasks thuộc family này.

Architecture đã được giải thích ở [Encoder–Decoder Models](../06_deep_learning_architectures/03_encoder_decoder_models.md); chapter này tập trung vào NLP-specific training, decoding và evaluation implications.

## Conditional Language Modeling

Given source `x`, output sequence `y`:

\[
P(y\mid x)=\prod_{t=1}^{T}P(y_t\mid y_{<t},x)
\]

Training minimize conditional negative log-likelihood:

\[
L=-\sum_t\log P(y_t^{true}\mid y_{<t}^{true},x)
\]

Source condition distinguishes seq2seq from unconditional/autoregressive LM continuation.

## Neural Machine Translation

Classical statistical MT used phrase tables, alignment models and language models. Neural MT learned end-to-end conditional model.

RNN encoder-decoder first, then attention removed fixed-vector bottleneck, then Transformer became dominant.

Translation quality requires more than word substitution because word order, morphology, idioms and discourse differ languages.

## Alignment

Attention weights often correlate source-target alignment but are not guaranteed explicit linguistic alignments.

Traditional alignment asks which source word generated target word. Neural seq2seq may distribute source information across states/heads.

For explainable translation, dedicated alignment extraction/constraints may be needed.

## Copy Mechanism / Pointer Networks

Some tasks require reproduce names/numbers/entities not well generated from fixed vocabulary.

Pointer/copy mechanism mixes generation distribution with attention-based copying from source.

Concept:

\[
P(token)=p_{gen}P_{vocab}+(1-p_{gen})P_{copy}
\]

Useful summarization, data-to-text and entity-heavy tasks.

Modern subword LMs reduce OOV but exact copying still important.

## Summarization

**Extractive** summarization selects source spans/sentences.

**Abstractive** summarization generates new wording.

Abstractive models risk hallucinating facts because generation objective rewards likely summary text, not strict entailment.

Faithfulness evaluation therefore separate from fluency/coverage.

## Teacher Forcing và Exposure Bias

Training sees correct previous target. Inference sees own generated history.

Sequence-level training approaches such as minimum risk training or reinforcement learning have been explored, but token-level MLE remains foundation due stability/scalability.

## Beam Search

Beam keeps top `B` partial translations according cumulative score.

Raw log probability biases short sequences. Length normalization:

\[
score(y)=\frac{\log P(y\mid x)}{len(y)^\alpha}
\]

or other penalties balance length.

Larger beam does not always improve human quality; model probability may prefer generic/short hypotheses.

## Coverage

Seq2seq may under-translate/repeat source. Coverage mechanisms track how much attention each source position received.

Modern Transformers reduce but do not eliminate omissions/repetitions.

## Text-to-Text Unification

T5-style framing casts tasks as:

```text
input text + task prefix → output text
```

Examples:

```text
translate English to German: ...
summarize: ...
```

One conditional generation architecture handles classification, QA, translation, summarization.

This foreshadows instruction-tuned LLMs where natural language defines task.

## Denoising Seq2Seq Pretraining

Corrupt input spans and train model reconstruct original:

```text
corrupted text → encoder
               → decoder → original text
```

This lets encoder-decoder learn language from unlabeled corpora before supervised fine-tuning.

BART/T5-style objectives are examples.

## Constrained Decoding

Some applications require output format/terminology constraints.

Constrained beam search can force phrases, schema tokens or grammar.

For structured JSON generation, modern systems may constrain next-token choices by grammar/schema rather than hope prompt alone produces valid structure.

This connects language generation with classical search/constraint satisfaction.

## Multilingual Translation

One model can handle many language pairs with language tags/instructions.

Transfer helps low-resource pairs, but capacity/data imbalance can cause interference. Sampling temperature/reweighting often used so high-resource English does not dominate.

Zero-shot translation may emerge between pairs not directly trained, but quality varies.

## Evaluation: BLEU

BLEU compares n-gram precision against references with brevity penalty.

Simplified:

\[
BLEU=BP\cdot\exp\left(\sum_nw_n\log p_n\right)
\]

Useful corpus-level MT benchmark, but limitations:

- multiple valid translations;
- weak semantic/factual sensitivity;
- tokenization matters;
- sentence-level unstable.

Neural metrics like COMET/BERTScore use learned representations but introduce model bias.

Human evaluation remains important for adequacy/fluency/faithfulness.

## Sequence-Level Error

A single early decoding error changes subsequent history. Token accuracy does not capture global coherence.

Evaluation should inspect:

```text
omission
addition/hallucination
mistranslation
entity/number errors
agreement
terminology consistency
repetition
```

## Domain Adaptation

General MT may fail legal/medical/company terminology. Fine-tuning/adapters, terminology constraints and retrieval of translation memory can help.

But domain adaptation can cause catastrophic forgetting general language; mixing/general data and controlled fine-tuning matter.

## Mental Model

> Seq2Seq NLP is conditional language modeling plus a source-information access mechanism and a decoding/search procedure.

Architecture gives probability distribution; decoding turns distribution into final sequence.

## Common Misconceptions

### “Beam search tìm exact best translation”

Finite beam is heuristic and model's highest-probability sequence may not be best human translation.

### “High BLEU means factually faithful summary”

BLEU overlap cannot reliably detect hallucinated facts.

### “Seq2Seq became obsolete after decoder-only LLMs”

Encoder-decoder remains efficient/natural for conditional transformation and widely used; decoder-only unifies via prompting but not universally optimal.

## Knowledge Connection

Seq2Seq combines [Language Models](./02_language_models.md), [Encoder–Decoder](../06_deep_learning_architectures/03_encoder_decoder_models.md), [Attention](../06_deep_learning_architectures/04_attention.md), and connects classical search via decoding.