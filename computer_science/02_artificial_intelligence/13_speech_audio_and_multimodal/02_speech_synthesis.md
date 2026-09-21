# Speech Synthesis và Text-to-Speech

**Tổng hợp tiếng nói (Text-to-Speech — TTS / 음성 합성)** biến text thành waveform có thể nghe được. Bài toán không chỉ là đọc đúng chữ; system còn phải tạo pronunciation, timing, prosody, speaker characteristic và fine acoustic detail.

```text
text
→ linguistic representation
→ acoustic representation
→ waveform generation
```

## Classical TTS

Các system cũ thường dùng **concatenative synthesis**, tức ghép các đoạn speech đã thu sẵn, hoặc statistical parametric synthesis.

Quality bị giới hạn bởi coverage của recording unit, discontinuity tại điểm ghép và hiện tượng oversmoothing.

Modern neural TTS học mapping từ text hoặc phoneme sang acoustic feature rồi dùng neural vocoder để synthesize waveform.

## Text Normalization

Raw text có thể chứa:

```text
2026-09-20
$15.30
Dr.
CPU
1234
```

TTS phải quyết định cách đọc dựa trên language và context.

**Text normalization** chuyển các non-standard word thành dạng có thể phát âm.

Nếu normalization sai, pronunciation vẫn sai dù acoustic model rất mạnh.

## Grapheme-to-Phoneme

Written form không phải lúc nào cũng xác định pronunciation duy nhất.

**Grapheme-to-Phoneme (G2P)** map grapheme sang phoneme hoặc pronunciation unit.

English có irregular spelling nên G2P đặc biệt quan trọng. Korean Hangul gần phonemic hơn nhưng vẫn có liaison và sound-change rule. Vietnamese ghi tone và pronunciation khá trực tiếp bằng orthography nhưng vẫn có regional variation.

## Acoustic Model

Acoustic model dự đoán spectrogram hoặc mel feature từ linguistic sequence.

Attention-based sequence-to-sequence model từng được dùng nhiều để align text position với audio frame.

Vì speech alignment gần monotonic, modern architecture thường đưa duration hoặc monotonic constraint vào để giảm lỗi skip và repeat.

## Trực giác Tacotron

Tacotron-style pipeline:

```text
text encoder
→ attention alignment
→ autoregressive decoder
→ mel spectrogram
```

Điểm yếu lớn là attention failure: model có thể bỏ từ, lặp từ hoặc mất ổn định với câu dài.

## Duration-Based Non-Autoregressive TTS

Model như FastSpeech family dự đoán duration của phoneme rồi expand representation thành sequence frame.

Lợi ích:

- generation song song;
- inference nhanh hơn;
- duration control rõ hơn;
- ít attention-alignment failure hơn.

## Vocoder

**Vocoder** biến acoustic representation như mel spectrogram thành waveform.

Neural vocoder có nhiều family:

- autoregressive;
- GAN-based;
- flow-based;
- diffusion-based.

Có thể hiểu separation như sau:

```text
Acoustic model → quyết định cấu trúc speech ở mức spectrogram
Vocoder        → dựng fine waveform detail
```

## End-to-End và Codec-Token TTS

Một số system mới encode speech thành neural audio codec token rồi model token sequence trực tiếp bằng Transformer-like architecture.

Cách này làm mờ ranh giới truyền thống giữa acoustic model và vocoder, vì speech có thể được biểu diễn bằng discrete hoặc quantized token sequence ngay trong generation stack.

## Prosody

Prosody gồm:

- pitch / F0;
- duration;
- energy;
- pause;
- rhythm;
- emphasis;
- speaking style.

Text không xác định duy nhất prosody. Cùng một sentence có thể được nói như question, sarcasm hoặc excitement tùy cách delivery.

Vì vậy TTS luôn phải chọn một acoustic realization trong rất nhiều khả năng hợp lệ.

## Speaker Embedding

Multi-speaker TTS thường condition trên **speaker embedding**.

Speaker encoder có thể trích representation từ reference audio và dùng representation này để giữ voice identity trong generation.

Đây là nền của voice cloning nhưng cũng tạo impersonation và security risk.

## Voice Cloning

Few-shot hoặc zero-shot voice cloning dùng một đoạn reference audio ngắn để suy ra speaker representation rồi synthesize nội dung mới.

Quality phụ thuộc recording quality, language overlap, speaker encoder và coverage trong training data.

Consent, disclosure và anti-spoofing trở thành requirement quan trọng khi feature này được deploy.

## Emotion và Style Control

Style control có thể đến từ:

- categorical style label;
- natural-language instruction;
- reference audio;
- latent style embedding.

Thách thức là **entanglement**: speaker identity, emotion, pitch và speaking rate có thể không tách biệt sạch trong learned representation.

## Multilingual TTS

Một model có thể support nhiều language bằng shared acoustic và speaker representation.

Cần xử lý:

```text
phoneme inventory
script
accent transfer
code-switching
language-specific prosody
```

Một speaker được synthesize ở language chưa từng thấy trong reference có thể mang accent do training distribution quyết định.

## Diffusion TTS

Diffusion model có thể generate acoustic feature hoặc waveform với quality cao bằng iterative denoising.

Điểm yếu là inference có thể chậm hơn nếu cần nhiều denoising step. Distillation hoặc few-step sampler giúp giảm latency.

## Evaluation

Metric chủ quan truyền thống là **Mean Opinion Score (MOS)**, nơi listener chấm naturalness.

MOS phụ thuộc test protocol, listener population và audio condition nên không nên so sánh các study khác nhau một cách máy móc.

Các dimension khác cần đo:

- intelligibility;
- ASR WER trên generated speech;
- speaker similarity;
- prosody accuracy;
- latency;
- long-text robustness;
- pronunciation của name, number và domain term.

Không có một metric duy nhất mô tả đầy đủ TTS quality.

## Streaming TTS

Voice assistant cần bắt đầu phát speech trước khi toàn response được generate.

Streaming TTS synthesize chunk theo thời gian nhưng vẫn phải giữ prosody và continuity giữa chunk.

Trade-off quan trọng:

```text
latency khởi đầu thấp
↔
cần future text context để phrasing tự nhiên hơn
```

## Real-Time Conversational Speech

Một voice assistant dạng cascade có thể dùng:

```text
ASR / speech encoder
→ LLM
→ TTS
```

Pipeline này modular và dễ debug nhưng thêm latency, đồng thời có thể làm mất prosody information giữa các stage.

End-to-end speech-to-speech model cố giữ acoustic interaction trực tiếp hơn trong khi vẫn sử dụng language reasoning.

## Watermarking và Provenance

Synthetic audio misuse thúc đẩy research về watermark và provenance.

Watermark lý tưởng cần survive compression hoặc editing mà không tạo audible artifact lớn, nhưng không nên xem watermark là security guarantee tuyệt đối.

## TTS Safety

Các risk chính gồm:

- impersonation fraud;
- fake evidence;
- non-consensual voice cloning;
- social engineering.

Tùy use case, application control có thể cần speaker consent, rate limit, disclosure, provenance và abuse monitoring.

## Mô hình tư duy

> **TTS giải một bài toán underdetermined: text xác định linguistic content, nhưng model phải chọn một acoustic realization hợp lý trong rất nhiều voice, rhythm và emotion có thể có.**

## Những nhầm lẫn thường gặp

### “Pronunciation đúng nghĩa là TTS tốt”

Không. Naturalness, prosody, speaker consistency và timing cũng rất quan trọng.

### “Voice cloning chỉ lưu recording rồi phát lại từng đoạn”

Không. Modern system thường condition generative model trên learned speaker representation.

### “TTS càng expressive càng tốt”

Không phải trong mọi application. Business hoặc assistive use case có thể cần delivery ổn định và predictable hơn dramatic variation.

## Liên kết kiến thức

TTS nối Generative Modeling, Diffusion, GAN, Audio Codec, Sequence Alignment và Multimodal Interaction.

Xem tiếp: [Multimodal Representation](./03_multimodal_representation.md).