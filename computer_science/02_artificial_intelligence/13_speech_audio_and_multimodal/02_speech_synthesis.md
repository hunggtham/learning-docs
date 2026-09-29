# Speech Synthesis và Text-to-Speech

> **Mạch đọc:** Đặt **Speech Synthesis và Text-to-Speech** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Classical TTS** sang **văn bản (text / 텍스트) Normalization**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Text-to-Speech (TTS / 음성 합성)** biến văn bản (text / 텍스트) thành waveform có thể nghe được. Đây không chỉ là đọc đúng chữ; hệ thống (system / 시스템) phải tạo pronunciation, timing, prosody, speaker characteristics và acoustic detail.

```text
text
→ linguistic representation
→ acoustic representation
→ waveform generation
```

## Classical TTS

Older các hệ thống (systems / 시스템들) dùng concatenative synthesis (ghép recorded units) hoặc parametric statistical synthesis. chất lượng (quality / 품질) bị giới hạn bởi coverage, joins và oversmoothing.

Hiện đại (modern / 현대적) neural TTS học ánh xạ (mapping / 매핑) từ văn bản (text / 텍스트)/phonemes tới acoustic features và dùng neural vocoder để synthesize waveform.

## Văn bản (text / 텍스트) Normalization

Raw văn bản (text / 텍스트) có:

```text
2026-09-20
$15.30
Dr.
CPU
1234
```

TTS cần quyết định cách đọc theo ngôn ngữ (language / 언어)/ngữ cảnh (context / 맥락). văn bản (text / 텍스트) normalization converts non-standard words into speakable forms.

Lỗi (error / 오류) ở normalization tạo pronunciation sai dù acoustic mô hình (model / 모델) tốt.

## Grapheme-to-Phoneme

Written form không luôn uniquely determine pronunciation. G2P maps graphemes to phonemes or pronunciation units.

English irregular spelling cần mạnh; Korean Hangul closer phonemic but liaison/sound rules still matter; Vietnamese tones/diacritics encode pronunciation more directly nhưng regional variation tồn tại.

## Acoustic mô hình (model / 모델)

Acoustic mô hình (model / 모델) predicts spectrogram/mel features from linguistic chuỗi (sequence / 시퀀스).

Attention-based seq2seq các mô hình (models / 모델들) historically align văn bản (text / 텍스트) positions with audio frames. Monotonic nature của speech alignment giúp architectures impose duration/monotonic các ràng buộc (constraints / 제약조건들).

## Tacotron Intuition

Encoder represents văn bản (text / 텍스트), attention aligns văn bản (text / 텍스트) positions to decoder thời gian (time / 시간), decoder generates mel spectrogram frames autoregressively.

Weakness: attention failures can skip/repeat words, long sentences unstable.

## Duration-Based Non-Autoregressive TTS

Các mô hình (models / 모델들) like FastSpeech family predict phoneme durations rồi expand representations across frames.

Benefits:

- parallel generation;
- faster suy luận (inference / 추론);
- tường minh (explicit / 명시적) duration điều khiển (control / 제어);
- fewer attention alignment failures.

## Vocoder

Vocoder maps acoustic biểu diễn (representation / 표현) (e.g., mel spectrogram) to waveform.

Neural vocoders include autoregressive, GAN-based, luồng (flow / 흐름)/diffusion families.

Separation:

```text
Acoustic model decides what speech should sound like at spectrogram level
Vocoder renders fine waveform detail
```

## End-to-End / Codec-Token TTS

Recent các hệ thống (systems / 시스템들) may represent speech with neural audio codec tokens and mô hình (model / 모델) đơn vị từ (token / 토큰) sequences directly with Transformer-like architectures, reducing traditional mel/vocoder ranh giới (boundary / 경계).

## Prosody

Prosody includes:

- pitch/F0;
- duration;
- năng lượng (energy / 에너지);
- pauses;
- rhythm;
- emphasis;
- speaking style.

Văn bản (text / 텍스트) underdetermines prosody. Same sentence can be question, sarcasm, excitement depending delivery.

## Speaker Embeddings

Multi-speaker TTS điều kiện (condition / 조건) on speaker embedding. Speaker encoder may derive biểu diễn (representation / 표현) from tham chiếu (reference / 참조) audio.

This enables voice cloning, but also creates impersonation/bảo mật (security / 보안) risks.

## Voice Cloning

Few-shot/zero-shot cloning maps short tham chiếu (reference / 참조) audio to speaker style. chất lượng (quality / 품질) depends recording chất lượng (quality / 품질), ngôn ngữ (language / 언어) overlap and speaker biểu diễn (representation / 표현).

Consent, disclosure and anti-spoofing become important quản trị (governance / 거버넌스) concerns.

## Emotion and Style điều khiển (control / 제어)

Điều khiển (control / 제어) signals can be categorical style labels, natural-language instructions, tham chiếu (reference / 참조) audio or latent embeddings.

But entanglement bài toán (problem / 문제): speaker định danh (identity / 식별자), emotion and speaking tỷ lệ (rate / 비율) may not separate cleanly.

## Multilingual TTS

One mô hình (model / 모델) can hỗ trợ (support / 지원) many languages, sharing acoustic/speaker representations. Need handle phoneme inventories, scripts, accent transfer and code-switching.

Speaker voice in unseen ngôn ngữ (language / 언어) may inherit accent from dữ liệu huấn luyện (training data / 학습 데이터).

## Diffusion TTS

Diffusion can generate acoustic features/waveforms iteratively with high chất lượng (quality / 품질), but suy luận (inference / 추론) may be slower unless distillation/fewer steps.

## Evaluation

Traditional subjective chỉ số (metric / 지표) **MOS (Mean Opinion Score)** asks listeners tỷ lệ (rate / 비율) naturalness. But MOS depends kiểm thử (test / 테스트) giao thức (protocol / 프로토콜)/listener population.

Other dimensions:

- intelligibility / ASR WER on generated audio;
- speaker similarity;
- prosody accuracy;
- độ trễ (latency / 지연 시간);
- robustness to long văn bản (text / 텍스트);
- pronunciation of names/numbers.

No single chỉ số (metric / 지표) captures naturalness.

## Streaming TTS

Voice assistants need start speaking before entire phản hồi (response / 응답) generated. Streaming kiến trúc (architecture / 아키텍처) synthesizes chunks while preserving prosody/continuity.

Sự đánh đổi (trade-off / 트레이드오프): low initial độ trễ (latency / 지연 시간) vs needing future văn bản (text / 텍스트) ngữ cảnh (context / 맥락) for natural phrasing.

## Real-Time Conversational Speech

Chuỗi xử lý (pipeline / 파이프라인) may be:

```text
ASR / speech encoder
→ LLM
→ TTS
```

but cascaded stages add độ trễ (latency / 지연 시간) and lose prosody. End-to-end speech-to-speech các mô hình (models / 모델들) seek direct acoustic tương tác (interaction / 상호작용) while retaining ngôn ngữ (language / 언어) lập luận (reasoning / 추론).

## Watermarking and Provenance

Synthetic audio misuse motivates watermark/provenance techniques. Watermarks must survive compression/editing while minimizing audible artifacts; not foolproof bảo mật (security / 보안).

## TTS an toàn (safety / 안전)

Risks:

- impersonation fraud;
- fake bằng chứng (evidence / 증거);
- non-consensual voice cloning;
- xã hội (social / 사회적) kỹ thuật (engineering / 엔지니어링).

Ứng dụng (application / 애플리케이션) controls should include speaker consent, tỷ lệ (rate / 비율) limits, disclosure and abuse monitoring depending use trường hợp (case / 사례).

## Mô hình tư duy (mental model / 사고 모델)

> **TTS solves an underdetermined inverse bài toán (problem / 문제): văn bản (text / 텍스트) specifies linguistic content, but mô hình (model / 모델) must choose one plausible acoustic realization among many possible voices, rhythms and emotions.**

## Dùng chung (common / 공통) Misconceptions

### “Correct pronunciation means good TTS”

Naturalness/prosody/speaker consistency also matter.

### “Voice cloning stores the original recordings and plays pieces back”

Hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) typically điều kiện (condition / 조건) generative mô hình (model / 모델) on learned speaker biểu diễn (representation / 표현).

### “More expressive TTS is always better”

Nghiệp vụ (business / 비즈니스)/assistive contexts may prefer stable predictable delivery over dramatic variation.

## Liên kết kiến thức (knowledge connection / 지식 연결)

TTS connects generative modeling, diffusion/GAN/audio codecs, chuỗi (sequence / 시퀀스) alignment and multimodal tương tác (interaction / 상호작용).

Xem tiếp: [Multimodal Representation](./03_multimodal_representation.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 audio and speech representation](./00_audio_and_speech_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
