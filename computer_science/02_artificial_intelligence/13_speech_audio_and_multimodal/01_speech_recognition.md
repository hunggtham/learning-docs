# Automatic Speech Recognition

**Automatic Speech Recognition (ASR / 음성 인식)** biến acoustic signal thành text/token sequence.

```text
waveform
→ acoustic representation
→ encoder
→ sequence decoding/alignment
→ text
```

ASR khó vì input dài theo time, output ngắn hơn và alignment giữa audio frames với characters/words không biết trước.

## Classical ASR Pipeline

Traditional systems tách nhiều modules:

```text
features (MFCC)
→ acoustic model
→ pronunciation lexicon
→ language model
→ decoder
```

Acoustic model estimate phonetic likelihood; lexicon map phonemes→words; language model score word sequences.

Modern end-to-end ASR học nhiều components jointly.

## Alignment Problem

Một utterance vài giây có hundreds frames nhưng transcript có vài chục tokens. Model cần biết frame nào correspond token nào mà training label thường chỉ có transcript whole sequence.

## CTC

**Connectionist Temporal Classification (CTC)** giải alignment bằng thêm `blank` symbol và sum probability over all valid frame-level alignments collapsing to target sequence.

Ví dụ paths:

```text
_ h h _ i _
h _ h i i _
```

có thể collapse thành `hi` theo CTC rules.

CTC assumes conditional independence giữa output labels given encoder features mạnh hơn autoregressive decoders, giúp decoding efficient.

## Sequence-to-Sequence ASR

Encoder transforms audio; autoregressive decoder attends encoder features và generate tokens one by one.

Pros:

- language context integrated;
- flexible output.

Cons:

- autoregressive latency;
- hallucination risk khi audio poor/silent;
- harder streaming.

## RNN-T / Transducer

Recurrent Neural Network Transducer combines acoustic encoder, prediction network và joint network. It supports streaming better and models output history.

Modern implementations may replace RNN with Transformer/Conformer components.

## Conformer

Conformer combines self-attention for global context + convolution for local acoustic patterns. This hybrid inductive bias fits speech well.

## Encoder-Only Self-Supervised Speech Models

Large unlabeled audio can pretrain representations using masked/contrastive objectives. Fine-tuning then needs less labeled speech.

This parallels self-supervised vision and language pretraining.

## Streaming ASR

Real-time transcription cannot wait full utterance. Need causal/chunked encoders and partial hypotheses.

Metrics include not only Word Error Rate but **latency** and stability of partial transcripts.

## Word Error Rate

WER:

\[
WER=\frac{S+D+I}{N}
\]

where:

- `S` substitutions;
- `D` deletions;
- `I` insertions;
- `N` reference words.

WER can exceed 100% if insertions large.

For languages without whitespace word boundaries, Character Error Rate or language-specific tokenization may be more meaningful.

## Language Dependence

Korean, Vietnamese, English differ in phonology, writing system and word segmentation. Evaluation/tokenization must respect language structure.

Code-switching adds challenge because language identity changes inside utterance.

## Beam Search

Decoder may keep top candidate hypotheses instead of greedy token. External/implicit language-model scores can combine with acoustic score:

\[
Score = \log P_{ASR}(y|x)+\lambda\log P_{LM}(y)+\beta LengthPenalty
\]

Weights require tuning.

## Hallucination

End-to-end generative ASR may output plausible text unsupported by audio under noise/silence. This differs from ordinary substitution errors.

Need VAD, no-speech confidence, timestamps and fallback policies.

## Timestamp Alignment

Applications need word/segment timestamps for subtitles/search. Alignment can be derived from attention/CTC or separate forced alignment model.

Timestamp accuracy is independent quality dimension from transcript correctness.

## Speaker Diarization

“Who spoke when?” is separate task. Pipeline may:

```text
speech segments
→ speaker embeddings
→ clustering
→ speaker labels
```

ASR + diarization combine into meeting transcription.

## Punctuation and Formatting

Raw ASR may omit punctuation/casing. Post-processing model restores sentence boundaries, numbers and formatting. But formatting can alter meaning, especially decimal/date entities.

## Domain Adaptation

Medical/legal/company jargon creates out-of-vocabulary or rare-token errors. Adaptation options:

- domain text language-model biasing;
- vocabulary/contextual biasing;
- fine-tuning with domain speech;
- custom pronunciation lexicon in modular systems.

## Contextual Biasing

Provide names/entities expected in context. But excessive bias can force hallucinated rare terms.

## Noise Robustness

Evaluate separately by SNR, microphone, accent, speaker demographic and environment. Average WER hides subgroup failures.

## Multilingual ASR

One model may share encoder across languages and use language tokens. Benefits transfer low-resource languages, but high-resource languages can dominate and scripts/tokenization need balance.

## Privacy

Speech contains biometric and contextual sensitive information beyond transcript. Data retention and encryption policies matter even if only text output is needed.

## Edge ASR

On-device ASR reduces latency/privacy risk but model needs quantization, streaming memory control and hardware optimization.

## Mental Model

> **ASR is not “audio classification repeated over time”; it is sequence transduction with uncertain alignment, acoustic variation and linguistic constraints.**

## Common Misconceptions

### “Low WER means perfect meeting transcription”

Diarization, punctuation, timestamps and entity formatting can still fail.

### “Language model correction always improves ASR”

It can replace acoustically supported rare words with more common but wrong phrases.

### “Speech recognition = speaker recognition”

Transcript content and speaker identity are distinct tasks.

## Knowledge Connection

ASR joins sequence modeling, CTC/attention, self-supervised learning and language modeling.

Xem tiếp: [Speech Synthesis](./02_speech_synthesis.md).