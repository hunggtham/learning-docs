# Audio và Speech Representation

Âm thanh là **time-varying pressure signal** được microphone biến thành electrical signal rồi sample thành numbers. Máy không trực tiếp nghe “giọng nói” hay “âm nhạc”; nó nhận discrete waveform.

Một mono waveform:

\[
x[n],\quad n=0,1,...,N-1
\]

## Sampling Rate

Sampling rate `f_s` cho biết số samples mỗi giây, ví dụ 16 kHz cho speech hoặc 44.1 kHz cho music.

Nyquist theorem nói frequency cao nhất có thể represent không aliasing lý tưởng là:

\[
f_{max}<\frac{f_s}{2}
\]

Vì speech intelligibility chủ yếu nằm dưới vài kHz, 16 kHz thường đủ cho ASR.

## Bit Depth

Bit depth controls quantization resolution. Higher bit depth giảm quantization noise nhưng tăng storage/bandwidth.

## Waveform vs Frequency Domain

Raw waveform cho amplitude theo time. Fourier transform decompose thành frequencies:

\[
X(f)=\mathcal F\{x(t)\}
\]

Nhưng speech changes over time, nên full-signal Fourier transform mất temporal locality.

## Short-Time Fourier Transform

STFT chia waveform thành overlapping windows rồi Fourier transform mỗi window:

\[
X(m,k)=\sum_n x[n]w[n-mH]e^{-j2\pi kn/N}
\]

`m` là frame index, `k` frequency bin, `H` hop size.

Magnitude spectrogram:

\[
S(m,k)=|X(m,k)|^2
\]

cho time–frequency representation.

## Window Size Trade-off

Long window:

```text
better frequency resolution
worse time resolution
```

Short window ngược lại. Đây là time-frequency uncertainty trade-off.

## Mel Scale

Human pitch perception không linear theo Hz. **Mel scale** compresses high frequencies. Mel filterbank aggregates spectrum into perceptually motivated bands.

Mel spectrogram là common input cho speech/audio models.

## Log-Mel Features

Human loudness roughly logarithmic, nên dùng log energy:

\[
\log(S+\epsilon)
\]

cũng compress dynamic range và stabilize training.

## MFCC

Mel-Frequency Cepstral Coefficients historically common in ASR:

```text
waveform
→ STFT
→ mel filterbank
→ log
→ DCT
→ MFCC
```

MFCC compress spectral envelope linked to vocal tract characteristics.

Modern deep models often use log-mel spectrogram or raw waveform directly.

## Speech Production

Speech signal reflects interaction của:

- vocal-source excitation;
- vocal tract resonances/formants;
- articulation;
- prosody;
- room/acoustic channel.

This source-filter view helps understand why same phoneme differs across speakers but shares spectral patterns.

## Phoneme, Grapheme, Token

Speech recognition may map audio to:

```text
phonemes
characters/graphemes
subword tokens
words
```

Output unit choice affects alignment, vocabulary and multilingual behavior.

## Prosody

Meaning is not only lexical content. Pitch `F0`, energy, duration and rhythm encode emotion, emphasis and sentence structure.

ASR may discard much prosody; TTS must recreate it.

## Silence and Voice Activity Detection

VAD determines regions containing speech. It reduces compute and avoids transcribing silence/noise, but false negatives cut real speech.

## Noise and Reverberation

Real recordings contain:

- background noise;
- echo/reverberation;
- microphone frequency response;
- clipping;
- packet compression.

Training only clean studio speech causes deployment shift.

## Beamforming

Microphone arrays exploit spatial delays to emphasize source direction and suppress noise. This is signal processing before/alongside learned models.

## Audio Augmentation

Useful transforms:

- additive noise;
- speed perturbation;
- room impulse convolution;
- gain changes;
- SpecAugment masks time/frequency regions.

Augmentations encode expected invariance but should not destroy label.

## Raw-Waveform Models

Learned convolutional encoders can directly transform waveform into latent features. This reduces handcrafted frontend but still must discover frequency/time structure from data.

## Audio Tokenization

Generative audio models may quantize continuous acoustic representations into discrete codec tokens using vector quantization.

Then audio can be modeled autoregressively like language tokens.

## Multi-Channel Audio

Stereo/microphone arrays add channel dimension and spatial cues such as interaural time/level differences.

## Mental Model

> **Audio AI là inference trên một signal vừa temporal vừa spectral. Waveform nói cái gì xảy ra theo time; spectrogram nói năng lượng nằm ở frequency nào tại từng time window.**

## Common Misconceptions

### “Spectrogram là ảnh nên xử lý như image bình thường”

Nó là 2D tensor nhưng axes có physical meaning khác; augmentations valid cho image không necessarily valid cho audio.

### “Higher sample rate luôn tốt hơn ASR”

Above task-relevant bandwidth, compute/data cost có thể tăng mà gain nhỏ.

### “Speech = text trong audio form”

Speech còn speaker identity, prosody, emotion, acoustic environment.

## Knowledge Connection

Audio connects Signal Processing, Fourier Analysis, CNN/Transformer sequence models và representation learning.

Xem tiếp: [Speech Recognition](./01_speech_recognition.md).