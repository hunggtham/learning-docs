# Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)

> **Mạch đọc:** Đặt **Variational Autoencoders: latent không gian (space / 공간) như một probabilistic mô hình (model / 모델)** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Generative mô hình (model / 모델)** sang **suy luận (inference / 추론) bài toán (problem / 문제)**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


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

## Why regularize latent toward prior?

Vanilla autoencoder maps examples to arbitrary isolated regions. Sampling random Gaussian điểm (point / 지점) may land where decoder never trained.

VAE pushes encoded distributions to occupy a smoother prior-compatible không gian (space / 공간), making:

\[
z\sim\mathcal N(0,I)
\]

then decode feasible.

Sự đánh đổi (trade-off / 트레이드오프): too much KL can reduce reconstruction detail.

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

## Closed-form KL for Gaussian

For diagonal Gaussian vs tiêu chuẩn (standard / 표준) normal:

\[
D_{KL}(q\|p)=\frac12\sum_j
(\mu_j^2+\sigma_j^2-\log\sigma_j^2-1)
\]

Thus no Monte Carlo needed for KL term in tiêu chuẩn (standard / 표준) VAE.

## Decoder likelihood determines reconstruction mất mát (loss / 손실)

If:

\[
p(x\mid z)=\mathcal N(\mu_\theta(z),\sigma^2I)
\]

negative log-likelihood corresponds roughly MSE.

For Bernoulli outputs, BCE-like likelihood.

Choosing reconstruction mất mát (loss / 손실) is choosing observation mô hình (model / 모델) các giả định (assumptions / 가정들).

## β-VAE

Modify:

\[
L=L_{recon}+\beta D_{KL}
\]

`β>1` strengthens prior pressure and sometimes improves factorized/disentangled cấu trúc (structure / 구조) at chi phí (cost / 비용) reconstruction.

But disentanglement is not guaranteed; identifiability needs các giả định (assumptions / 가정들).

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

## Latent Interpolation

Because latent prior is regularized, interpolation usually smoother than vanilla AE.

But tuyến tính (linear / 선형) interpolation in Gaussian không gian (space / 공간) not always probability-geodesic optimal; spherical interpolation sometimes used.

Smooth visualization does not prove ngữ nghĩa (semantic / 의미적) disentanglement.

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

## Variational suy luận (inference / 추론) liên kết (connection / 연결)

VAE is not only autoencoder with noise. It is amortized variational suy luận (inference / 추론): one encoder mạng (network / 네트워크) learns ánh xạ (mapping / 매핑) from any `x` to approximate posterior parameters, instead of running separate tối ưu hóa (optimization / 최적화) per datapoint.

**Amortization** shares suy luận (inference / 추론) computation across dataset.

## Mô hình tư duy (mental model / 사고 모델)

```text
Encoder: x → distribution over plausible latent causes z
Prior:   regularizes latent world to a sampleable space
Decoder: z → distribution over observations x
ELBO:    balance explaining data vs keeping latent posterior compatible with prior
```

## Dùng chung (common / 공통) Misconceptions

### “VAE encoder outputs latent véc-tơ (vector / 벡터)”

It usually outputs phân phối (distribution / 분포) parameters; latent is sampled/reparameterized.

### “KL term just prevents overfitting”

It aligns approximate posterior with prior, enabling coherent generative latent không gian (space / 공간) and controlling thông tin (information / 정보) sức chứa (capacity / 용량).

### “VAE mất mát (loss / 손실) = MSE + KL always”

Reconstruction term depends chosen likelihood; MSE is one trường hợp (case / 사례).

### “VAE guarantees disentangled human-readable latent factors”

No. Disentanglement requires stronger các giả định (assumptions / 가정들)/objectives/dữ liệu (data / 데이터).

## Liên kết kiến thức (knowledge connection / 지식 연결)

VAE combines [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [KL Divergence / Information Theory](../01_mathematical_foundations/05_information_theory.md), [Autoencoders](./06_autoencoders.md) and variational suy luận (inference / 추론).

Xem tiếp: [Generative Adversarial Networks](./08_generative_adversarial_networks.md) and [Diffusion Models](./09_diffusion_models.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 convolutional neural networks](./00_convolutional_neural_networks.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
