# Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Variational autoencoders**. Route đi từ probabilistic latent model → encoder/decoder → ELBO/reconstruction-KL trade-off → reparameterization → sampling and posterior limits, để generative representation nối với inference.

Variational Autoencoder (VAE / 변분 오토인코더) mở rộng autoencoder từ deterministic compression thành một **latent-variable generative mô hình (model / 모델)**. Encoder không đầu ra (output / 출력) một latent véc-tơ (vector / 벡터) duy nhất; nó approximate phân phối (distribution / 분포) của latent variable `z` conditioned on đầu vào (input / 입력) `x`. Decoder defines likelihood của dữ liệu (data / 데이터) given latent.

Mục tiêu là vừa reconstruct dữ liệu (data / 데이터) vừa làm latent phân phối (distribution / 분포) có cấu trúc (structure / 구조) gần một prior đơn giản để có thể mẫu (sample / 표본)/generate.

## Generative mô hình (model / 모델)

Assume latent prior:

\[
p(z)=\mathcal N(0,I)
\]

Decoder:

\[
p_\theta(x\mid z)
\]

Joint:

\[
p_\theta(x,z)=p(z)p_\theta(x\mid z)
\]

Dữ liệu (data / 데이터) likelihood:

\[
p_\theta(x)=\int p(z)p_\theta(x\mid z)dz
\]

Integral thường intractable với neural decoder.

> **Chuyển mạch:** Trong **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Suy luận (inference / 추론) bài toán (problem / 문제)** tiếp nhận điểm tựa từ **Generative mô hình (model / 모델)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Bằng chứng (evidence / 증거) Lower Bound (ELBO)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Suy luận (inference / 추론) bài toán (problem / 문제)

True posterior:

\[
p_\theta(z\mid x)=\frac{p(z)p_\theta(x\mid z)}{p_\theta(x)}
\]

khó compute vì denominator integral.

VAE introduce encoder phân phối (distribution / 분포):

\[
q_\phi(z\mid x)
\]

để approximate posterior. Đây là **variational suy luận (inference / 추론)**.

> **Chuyển mạch:** Ở chặng này của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Suy luận (inference / 추론) bài toán (problem / 문제)** nêu điều cần giải thích; **Bằng chứng (evidence / 증거) Lower Bound (ELBO)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Why regularize latent toward prior?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Bằng chứng (evidence / 증거) Lower Bound (ELBO)

Ta derive lower bound:

\[
\log p_\theta(x)
\ge
\mathbb E_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
-D_{KL}(q_\phi(z\mid x)\|p(z))
\]

ELBO gồm hai phần.

### Reconstruction / Likelihood Term

\[
\mathbb E_q[\log p_\theta(x\mid z)]
\]

encourage latent explain đầu vào (input / 입력) well.

### KL Regularization

\[
D_{KL}(q_\phi(z\mid x)\|p(z))
\]

encourage posterior codes stay close prior.

Mất mát (loss / 손실) often written:

\[
L_{VAE}=L_{recon}+D_{KL}(q(z\mid x)\|p(z))
\]

with sign/convention differences.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Bằng chứng (evidence / 증거) Lower Bound (ELBO)** nêu điều cần giải thích; **Why regularize latent toward prior?** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Gaussian Encoder** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Why regularize latent toward prior?

Vanilla autoencoder maps examples to arbitrary isolated regions. Sampling random Gaussian điểm (point / 지점) may land where decoder never trained.

VAE pushes encoded distributions to occupy a smoother prior-compatible không gian (space / 공간), making:

\[
z\sim\mathcal N(0,I)
\]

then decode feasible.

Sự đánh đổi (trade-off / 트레이드오프): too much KL can reduce reconstruction detail.

> **Chuyển mạch:** Trong **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Gaussian Encoder** tiếp nhận điểm tựa từ **Why regularize latent toward prior?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Reparameterization Trick** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Gaussian Encoder

Dùng chung (common / 공통) encoder outputs:

\[
\mu_\phi(x),\qquad \log\sigma_\phi^2(x)
\]

and defines:

\[
q_\phi(z\mid x)=\mathcal N(\mu,diag(\sigma^2))
\]

Why đầu ra (output / 출력) log variance? Variance must positive; log-space unconstrained/stable and exponentiate when needed.

> **Chuyển mạch:** Ở chặng này của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Reparameterization Trick** tiếp nhận điểm tựa từ **Gaussian Encoder** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Closed-form KL for Gaussian** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Reparameterization Trick

Naively sampling:

\[
z\sim\mathcal N(\mu,\sigma^2)
\]

puts stochastic nút (node / 노드) depending on parameters, hard for pathwise độ dốc (gradient / 기울기).

Rewrite:

\[
\epsilon\sim\mathcal N(0,I)
\]

\[
z=\mu+\sigma\odot\epsilon
\]

Randomness moved to parameter-independent `ε`; `z` differentiable w.r.t. `μ,σ`.

This is **reparameterization trick**.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Closed-form KL for Gaussian** tiếp nhận điểm tựa từ **Reparameterization Trick** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Decoder likelihood determines reconstruction mất mát (loss / 손실)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Closed-form KL for Gaussian

For diagonal Gaussian vs tiêu chuẩn (standard / 표준) normal:

\[
D_{KL}(q\|p)=\frac12\sum_j
(\mu_j^2+\sigma_j^2-\log\sigma_j^2-1)
\]

Thus no Monte Carlo needed for KL term in tiêu chuẩn (standard / 표준) VAE.

> **Chuyển mạch:** Trong **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Decoder likelihood determines reconstruction mất mát (loss / 손실)** tiếp nhận điểm tựa từ **Closed-form KL for Gaussian** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **β-VAE** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Decoder likelihood determines reconstruction mất mát (loss / 손실)

If:

\[
p(x\mid z)=\mathcal N(\mu_\theta(z),\sigma^2I)
\]

negative log-likelihood corresponds roughly MSE.

For Bernoulli outputs, BCE-like likelihood.

Choosing reconstruction mất mát (loss / 손실) is choosing observation mô hình (model / 모델) các giả định (assumptions / 가정들).

> **Chuyển mạch:** Ở chặng này của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **β-VAE** tiếp nhận điểm tựa từ **Decoder likelihood determines reconstruction mất mát (loss / 손실)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Posterior Collapse** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## β-VAE

Modify:

\[
L=L_{recon}+\beta D_{KL}
\]

`β>1` strengthens prior pressure and sometimes improves factorized/disentangled cấu trúc (structure / 구조) at chi phí (cost / 비용) reconstruction.

But disentanglement is not guaranteed; identifiability needs các giả định (assumptions / 가정들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Posterior Collapse** tiếp nhận điểm tựa từ **β-VAE** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Latent Interpolation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Posterior Collapse

Powerful decoder may ignore `z`:

\[
q(z\mid x)\approx p(z)
\]

KL near zero and latent carries little thông tin (information / 정보).

Dùng chung (common / 공통) in văn bản (text / 텍스트) VAEs with autoregressive decoder because decoder can mô hình (model / 모델) chuỗi (sequence / 시퀀스) without latent.

Mitigations:

- KL annealing;
- free bits;
- weaker decoder;
- kiến trúc (architecture / 아키텍처)/mục tiêu (objective / 목표) changes.

> **Chuyển mạch:** Trong **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Latent Interpolation** tiếp nhận điểm tựa từ **Posterior Collapse** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **VAE vs GAN vs Diffusion** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Latent Interpolation

Because latent prior is regularized, interpolation usually smoother than vanilla AE.

But tuyến tính (linear / 선형) interpolation in Gaussian không gian (space / 공간) not always probability-geodesic optimal; spherical interpolation sometimes used.

Smooth visualization does not prove ngữ nghĩa (semantic / 의미적) disentanglement.

> **Chuyển mạch:** Ở chặng này của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **VAE vs GAN vs Diffusion** tiếp nhận điểm tựa từ **Latent Interpolation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Latent Diffusion liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## VAE vs GAN vs Diffusion

VAE:

- tường minh (explicit / 명시적) latent probabilistic mô hình (model / 모델);
- ELBO likelihood lower bound;
- stable end-to-end huấn luyện (training / 학습);
- samples historically blurrier in điểm ảnh (pixel / 픽셀) không gian (space / 공간) depending decoder/mất mát (loss / 손실).

GAN:

- adversarial implicit phân phối (distribution / 분포);
- sharp samples;
- unstable huấn luyện (training / 학습)/chế độ (mode / 모드) collapse rủi ro (risk / 위험).

Diffusion:

- iterative denoising likelihood/score-based family;
- high mẫu (sample / 표본) chất lượng (quality / 품질)/stable huấn luyện (training / 학습);
- slower iterative sampling traditionally.

Hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) combine ideas, e.g. latent diffusion uses VAE-like ảnh (image / 이미지) autoencoder to compress images before diffusion.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, sau nội dung của **VAE vs GAN vs Diffusion**, **Latent Diffusion liên kết (connection / 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Từ đây, **Variational suy luận (inference / 추론) liên kết (connection / 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Latent Diffusion liên kết (connection / 연결)

Stable-Diffusion-like chuỗi xử lý (pipeline / 파이프라인) often:

```text
image
→ VAE encoder
→ latent spatial representation
→ diffusion denoising in latent space
→ VAE decoder
→ image
```

VAE here reduces compute by moving diffusion from raw pixels to compressed latent.

Thus VAE remains central even when diffusion is visible generation cơ chế (mechanism / 메커니즘).

> **Chuyển mạch:** Trong **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Variational suy luận (inference / 추론) liên kết (connection / 연결)** tiếp nhận điểm tựa từ **Latent Diffusion liên kết (connection / 연결)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variational suy luận (inference / 추론) liên kết (connection / 연결)

VAE is not only autoencoder with noise. It is amortized variational suy luận (inference / 추론): one encoder mạng (network / 네트워크) learns ánh xạ (mapping / 매핑) from any `x` to approximate posterior parameters, instead of running separate tối ưu hóa (optimization / 최적화) per datapoint.

**Amortization** shares suy luận (inference / 추론) computation across dataset.

> **Chuyển mạch:** Ở chặng này của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Variational suy luận (inference / 추론) liên kết (connection / 연결)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Encoder: x → distribution over plausible latent causes z
Prior:   regularizes latent world to a sampleable space
Decoder: z → distribution over observations x
ELBO:    balance explaining data vs keeping latent posterior compatible with prior
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “VAE encoder outputs latent véc-tơ (vector / 벡터)”

It usually outputs phân phối (distribution / 분포) parameters; latent is sampled/reparameterized.

### “KL term just prevents overfitting”

It aligns approximate posterior with prior, enabling coherent generative latent không gian (space / 공간) and controlling thông tin (information / 정보) sức chứa (capacity / 용량).

### “VAE mất mát (loss / 손실) = MSE + KL always”

Reconstruction term depends chosen likelihood; MSE is one trường hợp (case / 사례).

### “VAE guarantees disentangled human-readable latent factors”

No. Disentanglement requires stronger các giả định (assumptions / 가정들)/objectives/dữ liệu (data / 데이터).

> **Chuyển mạch:** Trong **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

VAE combines [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [KL Divergence / Information Theory](../01_mathematical_foundations/05_information_theory.md), [Autoencoders](./06_autoencoders.md) and variational suy luận (inference / 추론).

Xem tiếp: [Generative Adversarial Networks](./08_generative_adversarial_networks.md) and [Diffusion Models](./09_diffusion_models.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
