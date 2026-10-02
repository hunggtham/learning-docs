# Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Autoencoders**. Route đi từ encoder bottleneck → decoder reconstruction → reconstruction loss → denoising/contractive variants → latent use, để representation quality được phân biệt với mere copying.

Autoencoder (오토인코더) là kiến trúc (architecture / 아키텍처) học ánh xạ (mapping / 매핑):

\[
x\xrightarrow{Encoder}z\xrightarrow{Decoder}\hat x
\]

với mục tiêu (objective / 목표) reconstruct đầu vào (input / 입력):

\[
L=L(x,\hat x)
\]

Nó là một trong những cách trực quan nhất để hiểu biểu diễn (representation / 표현) học tập (learning / 학습) không cần human labels. Nhưng “reconstruct tốt” không tự động nghĩa latent không gian (space / 공간) semantically tốt; mọi thiết kế bottleneck/noise/mục tiêu (objective / 목표) đều quyết định thông tin (information / 정보) nào được giữ.

## Undercomplete Autoencoder

Nếu latent dimension:

\[
d_z<d_x
\]

Mạng (network / 네트워크) bị buộc compress đầu vào (input / 입력) qua bottleneck.

Tuyến tính (linear / 선형) autoencoder với squared-error và các ràng buộc (constraints / 제약조건들) phù hợp học subspace liên quan PCA. Nonlinear autoencoder có thể learn nonlinear manifold.

Nhưng nếu decoder quá powerful, latent có thể vẫn encode idiosyncratic detail thay vì useful lớp trừu tượng (abstraction / 추상화).

> **Chuyển mạch:** Trong **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Reconstruction mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Undercomplete Autoencoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Overcomplete Autoencoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reconstruction mất mát (loss / 손실)

Continuous normalized dữ liệu (data / 데이터) có thể dùng MSE:

\[
L=\|x-\hat x\|_2^2
\]

Nhị phân (binary / 이진)/Bernoulli-like pixels historically dùng BCE.

Hiện đại (modern / 현대적) ảnh (image / 이미지) reconstruction may use perceptual losses vì điểm ảnh (pixel / 픽셀) MSE penalizes small shifts strongly và often yields blurry averages.

Mất mát (loss / 손실) defines what “similar reconstruction” means.

> **Chuyển mạch:** Ở chặng này của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Overcomplete Autoencoder** tiếp nhận điểm tựa từ **Reconstruction mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Sparse Autoencoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Overcomplete Autoencoder

Nếu latent dimension lớn hơn đầu vào (input / 입력), mô hình (model / 모델) có thể learn định danh (identity / 식별자) trivially. Cần regularization hoặc corruption để force meaningful cấu trúc (structure / 구조).

Examples:

- sparse autoencoder;
- denoising autoencoder;
- contractive autoencoder.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Sparse Autoencoder** tiếp nhận điểm tựa từ **Overcomplete Autoencoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Denoising Autoencoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Sparse Autoencoder

Encourage most latent activations near zero. mục tiêu (objective / 목표):

\[
L=L_{recon}+\lambda R(z)
\]

Sparsity forces biểu diễn (representation / 표현) use limited active features per đầu vào (input / 입력).

Hiện đại (modern / 현대적) mechanistic interpretability also explores sparse autoencoders to decompose dense LLM activations into sparse learned features, though interpretation remains research bài toán (problem / 문제).

> **Chuyển mạch:** Trong **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Denoising Autoencoder** tiếp nhận điểm tựa từ **Sparse Autoencoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Contractive Autoencoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Denoising Autoencoder

Corrupt đầu vào (input / 입력):

\[
\tilde x\sim q(\tilde x\mid x)
\]

train:

\[
\tilde x\to Encoder\to z\to Decoder\to \hat x\approx x
\]

Mô hình (model / 모델) cannot simply bản sao (copy / 복사); it learns cấu trúc (structure / 구조) needed to recover clean dữ liệu (data / 데이터).

This principle connects directly to masked ngôn ngữ (language / 언어) modeling and diffusion denoising: corrupt dữ liệu (data / 데이터) then learn khôi phục (recovery / 복구).

> **Chuyển mạch:** Ở chặng này của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Contractive Autoencoder** tiếp nhận điểm tựa từ **Denoising Autoencoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Autoencoder for Anomaly Detection** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Contractive Autoencoder

Penalize sensitivity of latent biểu diễn (representation / 표현) to small đầu vào (input / 입력) changes, e.g. encoder Jacobian norm:

\[
\|\partial f(x)/\partial x\|_F^2
\]

encouraging locally stable biểu diễn (representation / 표현).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Autoencoder for Anomaly Detection** tiếp nhận điểm tựa từ **Contractive Autoencoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Latent Interpolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Autoencoder for Anomaly Detection

Train mostly normal dữ liệu (data / 데이터). If normal patterns reconstruct well, anomaly may have high reconstruction lỗi (error / 오류):

\[
s(x)=\|x-\hat x\|
\]

But high-capacity autoencoder can reconstruct anomalies too, and some normal rare patterns reconstruct poorly. Score needs kiểm tra hợp lệ (validation / 검증)/thresholding.

> **Chuyển mạch:** Trong **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Latent Interpolation** tiếp nhận điểm tựa từ **Autoencoder for Anomaly Detection** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Chuỗi (sequence / 시퀀스) Autoencoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Latent Interpolation

If latent không gian (space / 공간) is smooth, interpolate:

\[
z(\alpha)=(1-\alpha)z_1+\alpha z_2
\]

and decode intermediate samples.

Vanilla autoencoder does not guarantee latent regions between huấn luyện (training / 학습) codes decode realistically. This motivates probabilistic regularization in VAE.

> **Chuyển mạch:** Ở chặng này của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Latent Interpolation** xác định đầu vào; **Chuỗi (sequence / 시퀀스) Autoencoder** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Convolutional Autoencoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Chuỗi (sequence / 시퀀스) Autoencoder

Encoder can be RNN/Transformer; decoder reconstructs chuỗi (sequence / 시퀀스). Latent bottleneck may summarize chuỗi (sequence / 시퀀스).

But đơn vị từ (token / 토큰) reconstruction with powerful autoregressive decoder risks **posterior/latent ignoring**: decoder can predict from ngữ cảnh (context / 맥락) without using latent much.

Mục tiêu (objective / 목표)/kiến trúc (architecture / 아키텍처) must ensure latent matters.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Chuỗi (sequence / 시퀀스) Autoencoder** xác định đầu vào; **Convolutional Autoencoder** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Autoencoder vs PCA** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Convolutional Autoencoder

Images often use CNN encoder/downsampling and decoder/upsampling. Decoder may use transposed convolution or resize+conv.

Transposed conv can produce checkerboard artifacts if stride/kernel interplay poor.

> **Chuyển mạch:** Trong **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Autoencoder vs PCA** tiếp nhận điểm tựa từ **Convolutional Autoencoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Autoencoder vs Compression Codec** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Autoencoder vs PCA

PCA:

- tuyến tính (linear / 선형);
- closed-form/SVD;
- globally optimal for tuyến tính (linear / 선형) squared reconstruction;
- components orthogonal.

Autoencoder:

- nonlinear;
- trained iteratively;
- flexible kiến trúc (architecture / 아키텍처)/mất mát (loss / 손실);
- latent dimensions not necessarily identifiable/orthogonal.

Use PCA when tuyến tính (linear / 선형) cấu trúc (structure / 구조) sufficient and interpretability/stability matter; autoencoder when nonlinear biểu diễn (representation / 표현) justified by dữ liệu (data / 데이터)/quy mô (scale / 규모).

> **Chuyển mạch:** Ở chặng này của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Autoencoder vs Compression Codec** tiếp nhận điểm tựa từ **Autoencoder vs PCA** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bottleneck is not only dimensional** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Autoencoder vs Compression Codec

A learned autoencoder can act compression hệ thống (system / 시스템), but practical compression also requires quantization and entropy coding.

Continuous latent floats are not automatically compressed bitstream. Rate-distortion mục tiêu (objective / 목표) adds bitrate term:

\[
L=Distortion+\lambda tỷ lệ (rate / 비율)
\]

This connects biểu diễn (representation / 표현) học tập (learning / 학습) with thông tin (information / 정보) lý thuyết (theory / 이론).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Bottleneck is not only dimensional** tiếp nhận điểm tựa từ **Autoencoder vs Compression Codec** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Autoencoders and Foundation các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bottleneck is not only dimensional

Even if latent dimension large, các ràng buộc (constraints / 제약조건들) can create thông tin (information / 정보) bottleneck:

- sparsity;
- noise;
- quantization;
- low precision;
- limited channel sức chứa (capacity / 용량);
- probabilistic prior.

VAE uses phân phối (distribution / 분포) regularization rather than only dimension.

> **Chuyển mạch:** Trong **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Autoencoders and Foundation các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Bottleneck is not only dimensional** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Autoencoders and Foundation các mô hình (models / 모델들)

Masked autoencoders reconstruct missing ảnh (image / 이미지) patches. BERT-style masking reconstructs masked tokens/distributions. Denoising seq2seq corrupts văn bản (text / 텍스트) and reconstructs original.

These are not identical to classic autoencoder, but share principle: **self-supervised học tập (learning / 학습) through thông tin (information / 정보) removal/corruption and reconstruction**.

> **Chuyển mạch:** Ở chặng này của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Autoencoders and Foundation các mô hình (models / 모델들)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> Autoencoder asks: “Nếu buộc dữ liệu đi qua một constrained channel, biểu diễn (representation / 표현) nào giữ đủ cấu trúc (structure / 구조) để reconstruct?”

Ràng buộc (constraint / 제약조건) defines what lớp trừu tượng (abstraction / 추상화) emerges.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Latent smaller means biểu diễn (representation / 표현) meaningful”

Compression alone không guarantee ngữ nghĩa (semantics / 의미론).

### “Low reconstruction lỗi (error / 오류) means good downstream features”

Mô hình (model / 모델) may preserve nuisance detail irrelevant tác vụ (task / 작업).

### “Autoencoder generates new realistic samples automatically”

Vanilla latent phân phối (distribution / 분포) is irregular; arbitrary sampled `z` may decode nonsense.

### “Autoencoder compression = tệp (file / 파일) compression”

Need quantization/entropy coding and tỷ lệ (rate / 비율) mô hình (model / 모델) for actual bit-efficient codec.

> **Chuyển mạch:** Trong **Autoencoders: học biểu diễn (representation / 표현) bằng reconstruction**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Autoencoder extends [Representation Learning](../05_neural_networks/08_representation_learning.md) and [Dimensionality Reduction](../04_machine_learning/12_dimensionality_reduction.md).

Xem tiếp: [Variational Autoencoders](./07_variational_autoencoders.md), where latent không gian (space / 공간) becomes probabilistic and sampleable.

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
