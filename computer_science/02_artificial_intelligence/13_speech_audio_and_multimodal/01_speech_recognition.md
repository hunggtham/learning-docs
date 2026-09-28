# Automatic Speech Recognition

> **Mạch đọc:** Đặt **Automatic Speech Recognition** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Classical ASR chuỗi xử lý (pipeline / 파이프라인)** sang **Alignment bài toán (problem / 문제)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


**Automatic Speech Recognition (ASR / 음성 인식)** biến acoustic tín hiệu (signal / 신호) thành văn bản (text / 텍스트)/đơn vị từ (token / 토큰) chuỗi (sequence / 시퀀스).

```text
waveform
→ acoustic representation
→ encoder
→ sequence decoding/alignment
→ text
```

ASR khó vì đầu vào (input / 입력) dài theo thời gian (time / 시간), đầu ra (output / 출력) ngắn hơn và alignment giữa audio frames với characters/words không biết trước.

## Classical ASR chuỗi xử lý (pipeline / 파이프라인)

Traditional các hệ thống (systems / 시스템들) tách nhiều modules:

```text
features (MFCC)
→ acoustic model
→ pronunciation lexicon
→ language model
→ decoder
```

Acoustic mô hình (model / 모델) estimate phonetic likelihood; lexicon map phonemes→words; ngôn ngữ (language / 언어) mô hình (model / 모델) score word sequences.

Hiện đại (modern / 현대적) end-to-end ASR học nhiều components jointly.

## Alignment bài toán (problem / 문제)

Một utterance vài giây có hundreds frames nhưng transcript có vài chục tokens. mô hình (model / 모델) cần biết frame nào correspond đơn vị từ (token / 토큰) nào mà huấn luyện (training / 학습) label thường chỉ có transcript whole chuỗi (sequence / 시퀀스).

## CTC

**Connectionist Temporal Classification (CTC)** giải alignment bằng thêm `blank` symbol và sum xác suất (probability / 확률) over all valid frame-level alignments collapsing to mục tiêu (target / 대상) chuỗi (sequence / 시퀀스).

Ví dụ paths:

```text
_ h h _ i _
h _ h i i _
```

có thể collapse thành `hi` theo CTC rules.

CTC assumes conditional independence giữa đầu ra (output / 출력) labels given encoder features mạnh hơn autoregressive decoders, giúp decoding efficient.

## Sequence-to-Sequence ASR

Encoder transforms audio; autoregressive decoder attends encoder features và generate tokens one by one.

Pros:

- ngôn ngữ (language / 언어) ngữ cảnh (context / 맥락) integrated;
- flexible đầu ra (output / 출력).

Cons:

- autoregressive độ trễ (latency / 지연 시간);
- hallucination rủi ro (risk / 위험) khi audio poor/silent;
- harder streaming.

## RNN-T / Transducer

Recurrent Neural mạng (network / 네트워크) Transducer combines acoustic encoder, prediction mạng (network / 네트워크) và joint mạng (network / 네트워크). It supports streaming better and các mô hình (models / 모델들) đầu ra (output / 출력) lịch sử (history / 이력).

Hiện đại (modern / 현대적) implementations may replace RNN with Transformer/Conformer components.

## Conformer

Conformer combines self-attention for toàn cục (global / 전역) ngữ cảnh (context / 맥락) + convolution for cục bộ (local / 로컬) acoustic patterns. This hybrid inductive độ lệch (bias / 편향) fits speech well.

## Encoder-Only Self-Supervised Speech các mô hình (models / 모델들)

Large unlabeled audio can pretrain representations using masked/contrastive objectives. Fine-tuning then needs less labeled speech.

This parallels self-supervised vision and ngôn ngữ (language / 언어) pretraining.

## Streaming ASR

Real-time transcription cannot wait full utterance. Need nhân quả (causal / 인과적)/chunked encoders and partial hypotheses.

Metrics include not only Word lỗi (error / 오류) tỷ lệ (rate / 비율) but **độ trễ (latency / 지연 시간)** and stability of partial transcripts.

## Word lỗi (error / 오류) tỷ lệ (rate / 비율)

WER:

\[
WER=\frac{S+D+I}{N}
\]

where:

- `S` substitutions;
- `D` deletions;
- `I` insertions;
- `N` tham chiếu (reference / 참조) words.

WER can exceed 100% if insertions large.

For languages without whitespace word boundaries, Character lỗi (error / 오류) tỷ lệ (rate / 비율) or language-specific tokenization may be more meaningful.

## Ngôn ngữ (language / 언어) Dependence

Korean, Vietnamese, English differ in phonology, writing hệ thống (system / 시스템) and word segmentation. Evaluation/tokenization must respect ngôn ngữ (language / 언어) cấu trúc (structure / 구조).

Code-switching adds challenge because ngôn ngữ (language / 언어) định danh (identity / 식별자) changes inside utterance.

## Beam tìm kiếm (search / 검색)

Decoder may keep top candidate hypotheses instead of greedy đơn vị từ (token / 토큰). bên ngoài (external / 외부)/implicit language-model scores can combine with acoustic score:

\[
Score = \log P_{ASR}(y|x)+\lambda\log P_{LM}(y)+\beta LengthPenalty
\]

Weights require tuning.

## Hallucination

End-to-end generative ASR may đầu ra (output / 출력) plausible văn bản (text / 텍스트) unsupported by audio under noise/silence. This differs from ordinary substitution errors.

Need VAD, no-speech confidence, timestamps and fallback policies.

## Timestamp Alignment

Applications need word/segment timestamps for subtitles/tìm kiếm (search / 검색). Alignment can be derived from attention/CTC or separate forced alignment mô hình (model / 모델).

Timestamp accuracy is independent chất lượng (quality / 품질) dimension from transcript tính đúng đắn (correctness / 정확성).

## Speaker Diarization

“Who spoke when?” is separate tác vụ (task / 작업). chuỗi xử lý (pipeline / 파이프라인) may:

```text
speech segments
→ speaker embeddings
→ clustering
→ speaker labels
```

ASR + diarization combine into meeting transcription.

## Punctuation and Formatting

Raw ASR may omit punctuation/casing. Post-processing mô hình (model / 모델) restores sentence boundaries, numbers and formatting. But formatting can alter meaning, especially decimal/date entities.

## Lĩnh vực (domain / 도메인) Adaptation

Medical/legal/company jargon creates out-of-vocabulary or rare-token errors. Adaptation options:

- lĩnh vực (domain / 도메인) văn bản (text / 텍스트) language-model biasing;
- vocabulary/contextual biasing;
- fine-tuning with lĩnh vực (domain / 도메인) speech;
- custom pronunciation lexicon in modular các hệ thống (systems / 시스템들).

## Contextual Biasing

Provide names/entities expected in ngữ cảnh (context / 맥락). But excessive độ lệch (bias / 편향) can force hallucinated rare terms.

## Noise Robustness

Evaluate separately by SNR, microphone, accent, speaker demographic and môi trường (environment / 환경). Average WER hides subgroup failures.

## Multilingual ASR

One mô hình (model / 모델) may share encoder across languages and use ngôn ngữ (language / 언어) tokens. Benefits transfer low-resource languages, but high-resource languages can dominate and scripts/tokenization need balance.

## Privacy

Speech contains biometric and contextual sensitive thông tin (information / 정보) beyond transcript. dữ liệu (data / 데이터) retention and encryption policies matter even if only văn bản (text / 텍스트) đầu ra (output / 출력) is needed.

## Edge ASR

On-device ASR reduces độ trễ (latency / 지연 시간)/privacy rủi ro (risk / 위험) but mô hình (model / 모델) needs quantization, streaming bộ nhớ (memory / 메모리) điều khiển (control / 제어) and hardware tối ưu hóa (optimization / 최적화).

## Mô hình tư duy (mental model / 사고 모델)

> **ASR is not “audio classification repeated over thời gian (time / 시간)”; it is chuỗi (sequence / 시퀀스) transduction with uncertain alignment, acoustic variation and linguistic các ràng buộc (constraints / 제약조건들).**

## Dùng chung (common / 공통) Misconceptions

### “Low WER means perfect meeting transcription”

Diarization, punctuation, timestamps and thực thể (entity / 엔터티) formatting can still thất bại (fail / 실패).

### “ngôn ngữ (language / 언어) mô hình (model / 모델) correction always improves ASR”

It can replace acoustically supported rare words with more dùng chung (common / 공통) but wrong phrases.

### “Speech recognition = speaker recognition”

Transcript content and speaker định danh (identity / 식별자) are distinct tasks.

## Liên kết kiến thức (knowledge connection / 지식 연결)

ASR joins chuỗi (sequence / 시퀀스) modeling, CTC/attention, self-supervised học tập (learning / 학습) and ngôn ngữ (language / 언어) modeling.

Xem tiếp: [Speech Synthesis](./02_speech_synthesis.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 audio and speech representation](./00_audio_and_speech_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
