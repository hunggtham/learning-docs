# Automatic Speech Recognition

**Nhận dạng tiếng nói tự động (Automatic Speech Recognition — ASR / 음성 인식)** biến acoustic signal thành text hoặc token sequence.

```text
waveform
→ acoustic representation
→ encoder
→ sequence decoding / alignment
→ text
```

ASR khó vì input rất dài theo time, output ngắn hơn nhiều và alignment giữa audio frame với character hoặc word thường không biết trước.

## Classical ASR Pipeline

Traditional ASR system thường tách thành nhiều module:

```text
feature như MFCC
→ acoustic model
→ pronunciation lexicon
→ language model
→ decoder
```

Acoustic model ước lượng likelihood của phonetic unit từ audio. Lexicon map phoneme sang word. Language model đánh giá mức hợp lý của word sequence.

Modern end-to-end ASR cố học nhiều thành phần này jointly trong một architecture thống nhất hơn.

## Bài toán Alignment

Một utterance dài vài giây có thể tạo hàng trăm frame, nhưng transcript chỉ có vài chục token.

Training label thường chỉ cung cấp toàn transcript chứ không nói chính xác frame nào tương ứng với token nào.

Do đó ASR phải đồng thời học representation và alignment.

## CTC

**Connectionist Temporal Classification (CTC)** xử lý alignment bằng cách thêm `blank` symbol rồi cộng xác suất của mọi frame-level alignment hợp lệ có thể collapse về cùng target sequence.

Ví dụ:

```text
_ h h _ i _
h _ h i i _
```

có thể collapse thành `hi` theo CTC rule.

CTC đặt conditional-independence assumption mạnh hơn autoregressive decoder, đổi lại decoding thường hiệu quả và alignment tự nhiên hơn cho streaming hoặc forced alignment.

## Sequence-to-Sequence ASR

Encoder biến audio thành hidden representation. Autoregressive decoder attend encoder feature rồi generate token từng bước.

Ưu điểm:

- language context được tích hợp mạnh;
- output format linh hoạt;
- có thể model dependency giữa token trực tiếp.

Hạn chế:

- autoregressive latency;
- khó streaming hơn;
- có thể hallucinate text khi audio rất kém hoặc silence;
- decoding cost cao hơn.

## RNN-T / Transducer

**Recurrent Neural Network Transducer (RNN-T)** kết hợp acoustic encoder, prediction network và joint network.

Kiến trúc này hỗ trợ streaming tốt hơn và vẫn model output history.

Modern implementation có thể thay RNN bằng Transformer hoặc Conformer component trong một số phần của stack.

## Conformer

**Conformer** kết hợp self-attention để nắm global context với convolution để model local acoustic pattern.

Hybrid inductive bias này phù hợp speech vì speech vừa có local spectral structure vừa có dependency dài theo thời gian.

## Self-Supervised Speech Encoder

Lượng unlabeled audio rất lớn có thể được dùng để pretrain encoder bằng masked hoặc contrastive objective.

Sau đó model chỉ cần ít labeled speech hơn để fine-tune cho ASR.

Đây là parallel trực tiếp với self-supervised learning trong Vision và pretraining trong NLP.

## Streaming ASR

Real-time transcription không thể chờ toàn utterance kết thúc.

Streaming ASR cần causal hoặc chunked encoder và phải trả partial hypothesis trong lúc user vẫn đang nói.

Ngoài Word Error Rate, cần đo thêm:

- latency;
- time-to-first-partial;
- stability của partial transcript;
- finalization delay.

## Word Error Rate

**Word Error Rate (WER)**:

\[
WER=\frac{S+D+I}{N}
\]

trong đó:

- `S`: substitution;
- `D`: deletion;
- `I`: insertion;
- `N`: số word trong reference.

WER có thể lớn hơn 100% nếu insertion rất nhiều.

Với language có word-boundary khác English, Character Error Rate hoặc language-specific tokenization có thể phản ánh chất lượng tốt hơn.

## Khác biệt giữa các Ngôn ngữ

Korean, Vietnamese và English khác nhau về phonology, writing system, morphology và word segmentation.

Evaluation pipeline phải phù hợp structure của từng language thay vì dùng một tokenizer rule chung một cách máy móc.

Code-switching làm bài toán khó hơn vì language identity có thể thay đổi ngay bên trong một utterance.

## Beam Search

Decoder có thể giữ nhiều candidate hypothesis thay vì chọn greedy token duy nhất.

Một external hoặc integrated language model có thể được kết hợp:

\[
Score = \log P_{ASR}(y|x)+\lambda\log P_{LM}(y)+\beta LengthPenalty
\]

Các weight cần tune trên validation data phù hợp domain.

## Hallucination trong ASR

End-to-end generative ASR có thể sinh text nghe rất hợp lý nhưng không được audio support, đặc biệt khi input là noise hoặc silence.

Đây là failure khác với substitution thông thường.

Mitigation có thể gồm:

- VAD;
- no-speech confidence;
- timestamp consistency;
- constrained decoding;
- fallback hoặc abstention policy.

## Timestamp Alignment

Subtitle, search và meeting analysis thường cần timestamp theo segment hoặc word.

Alignment có thể lấy từ CTC, attention signal hoặc một forced-alignment model riêng.

Timestamp accuracy là một quality dimension độc lập với transcript correctness.

## Speaker Diarization

Câu hỏi “ai nói vào lúc nào?” là một task khác ASR.

Một diarization pipeline có thể:

```text
speech segment
→ speaker embedding
→ clustering / assignment
→ speaker label
```

Kết hợp ASR với diarization tạo meeting transcription có cả nội dung và speaker turn.

## Punctuation và Formatting

Raw ASR transcript có thể thiếu punctuation, casing hoặc normalized number format.

Post-processing model có thể khôi phục các thành phần này, nhưng formatting sai có thể làm đổi meaning của date, decimal hoặc identifier.

## Domain Adaptation

Medical term, legal vocabulary hoặc internal company jargon thường hiếm trong general ASR data.

Các lựa chọn adaptation gồm:

- language-model biasing bằng domain text;
- contextual vocabulary biasing;
- fine-tuning bằng domain speech;
- custom pronunciation lexicon trong modular system.

## Contextual Biasing

System có thể cung cấp danh sách name, product hoặc entity dự kiến xuất hiện.

Bias vừa phải giúp recognize rare term, nhưng bias quá mạnh có thể ép decoder hallucinate entity ngay cả khi acoustic evidence yếu.

## Noise Robustness

Nên evaluate ASR theo nhiều slice:

```text
SNR
microphone type
accent
speaker subgroup
environment
room reverberation
```

Average WER có thể che failure nghiêm trọng ở một subgroup cụ thể.

## Multilingual ASR

Một model có thể dùng shared encoder cho nhiều language và language token để điều kiện hóa decoding.

Điều này giúp transfer sang low-resource language nhưng cũng có nguy cơ high-resource language dominate training mixture.

Tokenizer, script coverage và data balancing cần được thiết kế cẩn thận.

## Privacy

Speech chứa nhiều information nhạy cảm hơn transcript:

- speaker identity;
- accent;
- background conversation;
- emotion;
- environmental context.

Retention, access control và encryption vẫn quan trọng ngay cả khi application chỉ cần text output.

## Edge ASR

On-device ASR giảm network latency và privacy exposure, nhưng model cần tối ưu:

- quantization;
- streaming memory;
- accelerator usage;
- battery/power consumption.

## Mô hình tư duy

> **ASR không phải “audio classification lặp theo thời gian”; nó là sequence transduction với uncertain alignment, acoustic variation và linguistic constraint.**

## Những nhầm lẫn thường gặp

### “WER thấp nghĩa meeting transcript đã hoàn hảo”

Không. Diarization, punctuation, timestamp và entity formatting vẫn có thể fail.

### “Language model correction luôn cải thiện ASR”

Không. LM có thể thay rare word được audio support bằng một phrase phổ biến hơn nhưng sai.

### “Speech recognition và speaker recognition là một task”

Không. Transcript content và speaker identity là hai mục tiêu khác nhau.

## Liên kết kiến thức

ASR kết hợp Sequence Modeling, CTC, Attention, Self-Supervised Learning và Language Modeling.

Xem tiếp: [Speech Synthesis](./02_speech_synthesis.md).