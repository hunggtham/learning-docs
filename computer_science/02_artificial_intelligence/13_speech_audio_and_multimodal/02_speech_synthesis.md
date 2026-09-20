# Speech Synthesis và Text-to-Speech

**Text-to-Speech (TTS / 음성 합성)** biến text thành waveform có thể nghe được. Đây không chỉ là đọc đúng chữ; system phải tạo pronunciation, timing, prosody, speaker characteristics và acoustic detail.

```text
text
→ linguistic representation
→ acoustic representation
→ waveform generation
```

## Classical TTS

Older systems dùng concatenative synthesis (ghép recorded units) hoặc parametric statistical synthesis. Quality bị giới hạn bởi coverage, joins và oversmoothing.

Modern neural TTS học mapping từ text/phonemes tới acoustic features và dùng neural vocoder để synthesize waveform.

## Text Normalization

Raw text có:

```text
2026-09-20
$15.30
Dr.
CPU
1234
```

TTS cần quyết định cách đọc theo language/context. Text normalization converts non-standard words into speakable forms.

Error ở normalization tạo pronunciation sai dù acoustic model tốt.

## Grapheme-to-Phoneme

Written form không luôn uniquely determine pronunciation. G2P maps graphemes to phonemes or pronunciation units.

English irregular spelling cần mạnh; Korean Hangul closer phonemic but liaison/sound rules still matter; Vietnamese tones/diacritics encode pronunciation more directly nhưng regional variation tồn tại.

## Acoustic Model

Acoustic model predicts spectrogram/mel features from linguistic sequence.

Attention-based seq2seq models historically align text positions with audio frames. Monotonic nature của speech alignment giúp architectures impose duration/monotonic constraints.

## Tacotron Intuition

Encoder represents text, attention aligns text positions to decoder time, decoder generates mel spectrogram frames autoregressively.

Weakness: attention failures can skip/repeat words, long sentences unstable.

## Duration-Based Non-Autoregressive TTS

Models like FastSpeech family predict phoneme durations rồi expand representations across frames.

Benefits:

- parallel generation;
- faster inference;
- explicit duration control;
- fewer attention alignment failures.

## Vocoder

Vocoder maps acoustic representation (e.g., mel spectrogram) to waveform.

Neural vocoders include autoregressive, GAN-based, flow/diffusion families.

Separation:

```text
Acoustic model decides what speech should sound like at spectrogram level
Vocoder renders fine waveform detail
```

## End-to-End / Codec-Token TTS

Recent systems may represent speech with neural audio codec tokens and model token sequences directly with Transformer-like architectures, reducing traditional mel/vocoder boundary.

## Prosody

Prosody includes:

- pitch/F0;
- duration;
- energy;
- pauses;
- rhythm;
- emphasis;
- speaking style.

Text underdetermines prosody. Same sentence can be question, sarcasm, excitement depending delivery.

## Speaker Embeddings

Multi-speaker TTS condition on speaker embedding. Speaker encoder may derive representation from reference audio.

This enables voice cloning, but also creates impersonation/security risks.

## Voice Cloning

Few-shot/zero-shot cloning maps short reference audio to speaker style. Quality depends recording quality, language overlap and speaker representation.

Consent, disclosure and anti-spoofing become important governance concerns.

## Emotion and Style Control

Control signals can be categorical style labels, natural-language instructions, reference audio or latent embeddings.

But entanglement problem: speaker identity, emotion and speaking rate may not separate cleanly.

## Multilingual TTS

One model can support many languages, sharing acoustic/speaker representations. Need handle phoneme inventories, scripts, accent transfer and code-switching.

Speaker voice in unseen language may inherit accent from training data.

## Diffusion TTS

Diffusion can generate acoustic features/waveforms iteratively with high quality, but inference may be slower unless distillation/fewer steps.

## Evaluation

Traditional subjective metric **MOS (Mean Opinion Score)** asks listeners rate naturalness. But MOS depends test protocol/listener population.

Other dimensions:

- intelligibility / ASR WER on generated audio;
- speaker similarity;
- prosody accuracy;
- latency;
- robustness to long text;
- pronunciation of names/numbers.

No single metric captures naturalness.

## Streaming TTS

Voice assistants need start speaking before entire response generated. Streaming architecture synthesizes chunks while preserving prosody/continuity.

Trade-off: low initial latency vs needing future text context for natural phrasing.

## Real-Time Conversational Speech

Pipeline may be:

```text
ASR / speech encoder
→ LLM
→ TTS
```

but cascaded stages add latency and lose prosody. End-to-end speech-to-speech models seek direct acoustic interaction while retaining language reasoning.

## Watermarking and Provenance

Synthetic audio misuse motivates watermark/provenance techniques. Watermarks must survive compression/editing while minimizing audible artifacts; not foolproof security.

## TTS Safety

Risks:

- impersonation fraud;
- fake evidence;
- non-consensual voice cloning;
- social engineering.

Application controls should include speaker consent, rate limits, disclosure and abuse monitoring depending use case.

## Mental Model

> **TTS solves an underdetermined inverse problem: text specifies linguistic content, but model must choose one plausible acoustic realization among many possible voices, rhythms and emotions.**

## Common Misconceptions

### “Correct pronunciation means good TTS”

Naturalness/prosody/speaker consistency also matter.

### “Voice cloning stores the original recordings and plays pieces back”

Modern systems typically condition generative model on learned speaker representation.

### “More expressive TTS is always better”

Business/assistive contexts may prefer stable predictable delivery over dramatic variation.

## Knowledge Connection

TTS connects generative modeling, diffusion/GAN/audio codecs, sequence alignment and multimodal interaction.

Xem tiếp: [Multimodal Representation](./03_multimodal_representation.md).