# Audio và Speech Representation

Âm thanh là một **tín hiệu áp suất thay đổi theo thời gian (time-varying pressure signal)**. Microphone biến dao động áp suất thành tín hiệu điện, sau đó hệ thống sampling để tạo thành các giá trị số. Máy không trực tiếp nghe “giọng nói” hoặc “âm nhạc”; nó nhận một discrete waveform.

Một mono waveform có thể viết:

\[
x[n],\quad n=0,1,...,N-1
\]

## Sampling Rate

**Tần số lấy mẫu (sampling rate)** `f_s` cho biết số sample được ghi mỗi giây, ví dụ 16 kHz cho nhiều speech system hoặc 44.1 kHz cho music.

Nyquist theorem cho biết frequency cao nhất có thể biểu diễn mà không aliasing trong điều kiện lý tưởng phải thỏa:

\[
f_{max}<\frac{f_s}{2}
\]

Phần lớn information quan trọng cho speech intelligibility nằm ở dải tương đối thấp, vì vậy 16 kHz thường đủ cho nhiều ASR application.

## Bit Depth

**Bit depth** quyết định độ phân giải của phép quantization amplitude.

Bit depth cao hơn giảm quantization noise nhưng làm storage và bandwidth tăng.

Sampling rate quyết định độ phân giải theo thời gian; bit depth quyết định độ phân giải theo amplitude. Hai khái niệm này không giống nhau.

## Waveform và Frequency Domain

Raw waveform biểu diễn amplitude theo thời gian.

Fourier Transform phân rã signal thành các frequency component:

\[
X(f)=\mathcal F\{x(t)\}
\]

Nhưng speech liên tục thay đổi theo thời gian, nên Fourier Transform trên toàn signal làm mất information về frequency nào xuất hiện ở thời điểm nào.

## Short-Time Fourier Transform

**Short-Time Fourier Transform (STFT)** chia waveform thành các window chồng lấn rồi tính Fourier Transform riêng cho từng window:

\[
X(m,k)=\sum_n x[n]w[n-mH]e^{-j2\pi kn/N}
\]

Trong đó `m` là frame index, `k` là frequency bin và `H` là hop size.

Magnitude spectrogram:

\[
S(m,k)=|X(m,k)|^2
\]

biểu diễn năng lượng theo cả time và frequency.

## Trade-off của Window Size

Window dài:

```text
frequency resolution tốt hơn
nhưng time resolution kém hơn
```

Window ngắn tạo trade-off ngược lại.

Đây là một biểu hiện của **time–frequency uncertainty trade-off**: khó có resolution cực cao đồng thời ở cả hai trục.

## Mel Scale

Human perception về pitch và frequency không tuyến tính hoàn toàn theo Hz.

**Mel scale** nén vùng high frequency và giữ resolution tương đối tốt hơn ở vùng frequency thấp theo một mô hình gần với perception của con người.

Mel filterbank tổng hợp spectrum thành các perceptually motivated band. **Mel spectrogram** vì vậy là input rất phổ biến cho speech và audio model.

## Log-Mel Feature

Loudness perception cũng gần logarithmic hơn linear.

Do đó energy thường được log-transform:

\[
\log(S+\epsilon)
\]

Phép biến đổi này vừa nén dynamic range vừa giúp optimization ổn định hơn.

## MFCC

**Mel-Frequency Cepstral Coefficients (MFCC)** từng là feature rất phổ biến trong ASR truyền thống:

```text
waveform
→ STFT
→ mel filterbank
→ log
→ DCT
→ MFCC
```

MFCC nén spectral envelope liên quan tới đặc điểm vocal tract.

Modern deep model thường dùng log-mel spectrogram hoặc raw waveform trực tiếp, nhưng MFCC vẫn rất quan trọng để hiểu lịch sử và signal-processing foundation của speech recognition.

## Speech Production

Speech signal phản ánh tương tác giữa:

- nguồn dao động từ vocal folds;
- resonance của vocal tract và formant;
- articulation;
- prosody;
- acoustic channel và room.

Góc nhìn **source–filter model** giúp hiểu vì sao cùng một phoneme có thể khác nhau giữa speaker nhưng vẫn chia sẻ spectral structure nhất định.

## Phoneme, Grapheme và Token

Speech recognition có thể map audio sang nhiều output unit khác nhau:

```text
phoneme
character / grapheme
subword token
word
```

Choice của output unit ảnh hưởng alignment, vocabulary size, pronunciation handling và multilingual behavior.

## Prosody

Meaning của speech không chỉ nằm ở lexical content.

Pitch `F0`, energy, duration và rhythm còn encode emotion, emphasis, question/statement pattern và discourse structure.

ASR có thể bỏ qua nhiều prosody khi chỉ cần transcript, trong khi TTS cần tái tạo prosody để giọng nói tự nhiên và truyền đúng ý.

## Silence và Voice Activity Detection

**Voice Activity Detection (VAD)** xác định đoạn nào chứa speech.

VAD giúp giảm compute và tránh transcribe silence hoặc noise, nhưng false negative có thể cắt mất speech thật.

Trong streaming system, VAD cũng ảnh hưởng latency vì nó góp phần quyết định khi nào một utterance được xem là kết thúc.

## Noise và Reverberation

Recording thực tế có thể chứa:

- background noise;
- echo và reverberation;
- microphone frequency response;
- clipping;
- codec/compression artifact.

Nếu training chỉ dùng clean studio speech, deployment quality có thể giảm mạnh do domain shift.

## Beamforming

Microphone array có thể tận dụng delay khác nhau giữa nhiều microphone để tăng tín hiệu từ một hướng và suppress noise từ hướng khác.

**Beamforming** là ví dụ điển hình cho signal processing có thể hoạt động trước hoặc song song với learned model.

## Audio Augmentation

Các augmentation hữu ích gồm:

- additive noise;
- speed perturbation;
- convolution với room impulse response;
- gain change;
- SpecAugment che một số vùng time/frequency.

Augmentation encode assumption về variation mà model nên robust, nhưng không được làm thay đổi label semantics ngoài ý muốn.

## Raw-Waveform Model

Learned convolutional encoder có thể xử lý waveform trực tiếp và tự học frontend representation.

Điều này giảm reliance vào handcrafted feature nhưng không làm time–frequency structure biến mất; model vẫn phải học các pattern đó từ data.

## Audio Tokenization

Generative audio model có thể quantize continuous acoustic representation thành discrete **codec token** bằng vector quantization hoặc neural codec.

Khi đó audio có thể được model như một token sequence, gần hơn với cách autoregressive language model xử lý text.

## Multi-Channel Audio

Stereo hoặc microphone array thêm channel dimension và cung cấp spatial cue như interaural time difference hoặc level difference.

Thông tin spatial này hữu ích cho localization, separation và beamforming.

## Mô hình tư duy

> **Audio AI là quá trình suy luận trên một signal vừa có cấu trúc thời gian vừa có cấu trúc tần số. Waveform cho biết signal thay đổi thế nào theo time; spectrogram cho biết energy nằm ở frequency nào trong từng time window.**

## Những nhầm lẫn thường gặp

### “Spectrogram là ảnh nên có thể augmentation như image bình thường”

Không hoàn toàn. Spectrogram là tensor 2D nhưng hai axis mang physical meaning khác image spatial axis. Một transformation hợp lệ cho image chưa chắc hợp lệ cho audio.

### “Sampling rate càng cao thì ASR luôn càng tốt”

Không. Khi đã vượt task-relevant bandwidth, compute và storage có thể tăng nhiều trong khi quality gain rất nhỏ.

### “Speech chỉ là text ở dạng audio”

Không. Speech còn chứa speaker identity, prosody, emotion và acoustic environment.

## Liên kết kiến thức

Audio nối Signal Processing, Fourier Analysis, CNN/Transformer sequence model và Representation Learning.

Xem tiếp: [Speech Recognition](./01_speech_recognition.md).