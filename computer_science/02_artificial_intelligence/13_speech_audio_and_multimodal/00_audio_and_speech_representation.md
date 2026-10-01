# Audio và Speech biểu diễn (representation / 표현)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Audio và Speech biểu diễn (representation / 표현)**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Sampling tỷ lệ (rate / 비율)** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Bit độ sâu (depth / 깊이)** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Âm thanh là **time-varying pressure tín hiệu (signal / 신호)** được microphone biến thành electrical tín hiệu (signal / 신호) rồi mẫu (sample / 표본) thành numbers. Máy không trực tiếp nghe “giọng nói” hay “âm nhạc”; nó nhận discrete waveform.

Một mono waveform:

\[
x[n],\quad n=0,1,...,N-1
\]

## Sampling tỷ lệ (rate / 비율)

Sampling tỷ lệ (rate / 비율) `f_s` cho biết số samples mỗi giây, ví dụ 16 kHz cho speech hoặc 44.1 kHz cho music.

Nyquist theorem nói frequency cao nhất có thể represent không aliasing lý tưởng là:

\[
f_{max}<\frac{f_s}{2}
\]

Vì speech intelligibility chủ yếu nằm dưới vài kHz, 16 kHz thường đủ cho ASR.

> **Chuyển mạch:** Trong **Audio và Speech biểu diễn (representation / 표현)**, **Bit độ sâu (depth / 깊이)** tiếp nhận điểm tựa từ **Sampling tỷ lệ (rate / 비율)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Waveform vs Frequency lĩnh vực (domain / 도메인)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bit độ sâu (depth / 깊이)

Bit độ sâu (depth / 깊이) controls quantization resolution. Higher bit độ sâu (depth / 깊이) giảm quantization noise nhưng tăng lưu trữ (storage / 저장소)/bandwidth.

> **Chuyển mạch:** Ở chặng này của **Audio và Speech biểu diễn (representation / 표현)**, **Waveform vs Frequency lĩnh vực (domain / 도메인)** tiếp nhận điểm tựa từ **Bit độ sâu (depth / 깊이)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Short-Time Fourier Transform** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Waveform vs Frequency lĩnh vực (domain / 도메인)

Raw waveform cho amplitude theo thời gian (time / 시간). Fourier transform decompose thành frequencies:

\[
X(f)=\mathcal F\{x(t)\}
\]

Nhưng speech changes over thời gian (time / 시간), nên full-signal Fourier transform mất temporal locality.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Audio và Speech biểu diễn (representation / 표현)**, **Short-Time Fourier Transform** tiếp nhận điểm tựa từ **Waveform vs Frequency lĩnh vực (domain / 도메인)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cửa sổ (window / 윈도우) kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Short-Time Fourier Transform

STFT chia waveform thành overlapping windows rồi Fourier transform mỗi cửa sổ (window / 윈도우):

\[
X(m,k)=\sum_n x[n]w[n-mH]e^{-j2\pi kn/N}
\]

`m` là frame chỉ mục (index / 인덱스), `k` frequency bin, `H` hop kích thước (size / 크기).

Magnitude spectrogram:

\[
S(m,k)=|X(m,k)|^2
\]

cho thời gian (time / 시간)–frequency biểu diễn (representation / 표현).

> **Chuyển mạch:** Trong **Audio và Speech biểu diễn (representation / 표현)**, **Cửa sổ (window / 윈도우) kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Short-Time Fourier Transform** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mel quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cửa sổ (window / 윈도우) kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)

Long cửa sổ (window / 윈도우):

```text
better frequency resolution
worse time resolution
```

Short cửa sổ (window / 윈도우) ngược lại. Đây là time-frequency bất định (uncertainty / 불확실성) sự đánh đổi (trade-off / 트레이드오프).

> **Chuyển mạch:** Ở chặng này của **Audio và Speech biểu diễn (representation / 표현)**, **Mel quy mô (scale / 규모)** tiếp nhận điểm tựa từ **Cửa sổ (window / 윈도우) kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Log-Mel Features** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mel quy mô (scale / 규모)

Human pitch perception không tuyến tính (linear / 선형) theo Hz. **Mel quy mô (scale / 규모)** compresses high frequencies. Mel filterbank aggregates spectrum into perceptually motivated bands.

Mel spectrogram là dùng chung (common / 공통) đầu vào (input / 입력) cho speech/audio các mô hình (models / 모델들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Audio và Speech biểu diễn (representation / 표현)**, **Log-Mel Features** tiếp nhận điểm tựa từ **Mel quy mô (scale / 규모)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **MFCC** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Log-Mel Features

Human loudness roughly logarithmic, nên dùng log năng lượng (energy / 에너지):

\[
\log(S+\epsilon)
\]

cũng compress động (dynamic / 동적) phạm vi (range / 범위) và stabilize huấn luyện (training / 학습).

> **Chuyển mạch:** Trong **Audio và Speech biểu diễn (representation / 표현)**, **MFCC** tiếp nhận điểm tựa từ **Log-Mel Features** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Speech môi trường vận hành (production / 운영 환경)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## MFCC

Mel-Frequency Cepstral Coefficients historically dùng chung (common / 공통) in ASR:

```text
waveform
→ STFT
→ mel filterbank
→ log
→ DCT
→ MFCC
```

MFCC compress spectral envelope linked to vocal tract characteristics.

Hiện đại (modern / 현대적) deep các mô hình (models / 모델들) often use log-mel spectrogram or raw waveform directly.

> **Chuyển mạch:** Ở chặng này của **Audio và Speech biểu diễn (representation / 표현)**, **Speech môi trường vận hành (production / 운영 환경)** tiếp nhận điểm tựa từ **MFCC** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Phoneme, Grapheme, đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Speech môi trường vận hành (production / 운영 환경)

Speech tín hiệu (signal / 신호) reflects tương tác (interaction / 상호작용) của:

- vocal-source excitation;
- vocal tract resonances/formants;
- articulation;
- prosody;
- room/acoustic channel.

This source-filter view helps understand why same phoneme differs across speakers but shares spectral patterns.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Audio và Speech biểu diễn (representation / 표현)**, **Phoneme, Grapheme, đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **Speech môi trường vận hành (production / 운영 환경)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Prosody** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Phoneme, Grapheme, đơn vị từ (token / 토큰)

Speech recognition may map audio to:

```text
phonemes
characters/graphemes
subword tokens
words
```

Đầu ra (output / 출력) đơn vị (unit / 단위) choice affects alignment, vocabulary and multilingual hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Audio và Speech biểu diễn (representation / 표현)**, **Prosody** tiếp nhận điểm tựa từ **Phoneme, Grapheme, đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Silence and Voice Activity Detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Prosody

Meaning is not only lexical content. Pitch `F0`, năng lượng (energy / 에너지), duration and rhythm encode emotion, emphasis and sentence cấu trúc (structure / 구조).

ASR may discard much prosody; TTS must recreate it.

> **Chuyển mạch:** Ở chặng này của **Audio và Speech biểu diễn (representation / 표현)**, **Silence and Voice Activity Detection** tiếp nhận điểm tựa từ **Prosody** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Noise and Reverberation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Silence and Voice Activity Detection

VAD determines regions containing speech. It reduces compute and avoids transcribing silence/noise, but false negatives cut real speech.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Audio và Speech biểu diễn (representation / 표현)**, **Noise and Reverberation** tiếp nhận điểm tựa từ **Silence and Voice Activity Detection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Beamforming** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Noise and Reverberation

Real recordings contain:

- background noise;
- echo/reverberation;
- microphone frequency phản hồi (response / 응답);
- clipping;
- packet compression.

Huấn luyện (training / 학습) only clean studio speech causes triển khai (deployment / 배포) shift.

> **Chuyển mạch:** Trong **Audio và Speech biểu diễn (representation / 표현)**, **Beamforming** tiếp nhận điểm tựa từ **Noise and Reverberation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Audio Augmentation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Beamforming

Microphone arrays exploit spatial delays to emphasize nguồn (source / 소스) direction and suppress noise. This is tín hiệu (signal / 신호) processing before/alongside learned các mô hình (models / 모델들).

> **Chuyển mạch:** Ở chặng này của **Audio và Speech biểu diễn (representation / 표현)**, **Audio Augmentation** tiếp nhận điểm tựa từ **Beamforming** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Raw-Waveform các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Audio Augmentation

Useful transforms:

- additive noise;
- speed perturbation;
- room impulse convolution;
- gain changes;
- SpecAugment masks thời gian (time / 시간)/frequency regions.

Augmentations encode expected invariance but should not destroy label.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Audio và Speech biểu diễn (representation / 표현)**, **Raw-Waveform các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Audio Augmentation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Audio Tokenization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Raw-Waveform các mô hình (models / 모델들)

Learned convolutional encoders can directly transform waveform into latent features. This reduces handcrafted frontend but still must discover frequency/thời gian (time / 시간) cấu trúc (structure / 구조) from dữ liệu (data / 데이터).

> **Chuyển mạch:** Trong **Audio và Speech biểu diễn (representation / 표현)**, **Audio Tokenization** tiếp nhận điểm tựa từ **Raw-Waveform các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multi-Channel Audio** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Audio Tokenization

Generative audio các mô hình (models / 모델들) may quantize continuous acoustic representations into discrete codec tokens using véc-tơ (vector / 벡터) quantization.

Then audio can be modeled autoregressively like ngôn ngữ (language / 언어) tokens.

> **Chuyển mạch:** Ở chặng này của **Audio và Speech biểu diễn (representation / 표현)**, **Multi-Channel Audio** tiếp nhận điểm tựa từ **Audio Tokenization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multi-Channel Audio

Stereo/microphone arrays add channel dimension and spatial cues such as interaural thời gian (time / 시간)/mức (level / 수준) differences.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Audio và Speech biểu diễn (representation / 표현)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Multi-Channel Audio** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Audio AI là suy luận (inference / 추론) trên một tín hiệu (signal / 신호) vừa temporal vừa spectral. Waveform nói cái gì xảy ra theo thời gian (time / 시간); spectrogram nói năng lượng nằm ở frequency nào tại từng thời gian (time / 시간) cửa sổ (window / 윈도우).**

> **Chuyển mạch:** Trong **Audio và Speech biểu diễn (representation / 표현)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Spectrogram là ảnh nên xử lý như ảnh (image / 이미지) bình thường”

Nó là 2D tensor nhưng axes có vật lý (physical / 물리적) meaning khác; augmentations valid cho ảnh (image / 이미지) không necessarily valid cho audio.

### “Higher mẫu (sample / 표본) tỷ lệ (rate / 비율) luôn tốt hơn ASR”

Above task-relevant bandwidth, compute/dữ liệu (data / 데이터) chi phí (cost / 비용) có thể tăng mà gain nhỏ.

### “Speech = văn bản (text / 텍스트) trong audio form”

Speech còn speaker định danh (identity / 식별자), prosody, emotion, acoustic môi trường (environment / 환경).

> **Chuyển mạch:** Ở chặng này của **Audio và Speech biểu diễn (representation / 표현)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Audio connects tín hiệu (signal / 신호) Processing, Fourier phân tích (analysis / 분석), CNN/Transformer chuỗi (sequence / 시퀀스) các mô hình (models / 모델들) và biểu diễn (representation / 표현) học tập (learning / 학습).

Xem tiếp: [Speech Recognition](./01_speech_recognition.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
