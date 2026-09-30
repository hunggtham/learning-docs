# Generative Adversarial Networks: học phân phối qua một trò chơi đối kháng

> **Mạch đọc:** Đặt **Generative Adversarial Networks: học phân phối qua một trò chơi đối kháng** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **Hai networks** sang **Discriminator optimum intuition**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Generative Adversarial mạng (network / 네트워크) học generative mô hình (model / 모델) bằng cách đặt **generator** và **discriminator** vào một game đối kháng. Generator tạo fake samples; discriminator cố phân biệt real/fake. Generator cải thiện để discriminator khó nhận ra hơn.

GAN quan trọng vì nó cho thấy generative học tập (learning / 학습) không nhất thiết cần tường minh (explicit / 명시적) likelihood. phân phối (distribution / 분포) có thể được học thông qua một learned critic/discriminator tín hiệu (signal / 신호).

## Hai networks

Generator:

\[
z\sim p(z),\qquad x_{fake}=G_\theta(z)
\]

Discriminator:

\[
D_\phi(x)\in(0,1)
\]

ước lượng đầu vào (input / 입력) real hay generated.

Original minimax mục tiêu (objective / 목표):

\[
\min_G\max_D
\mathbb E_{x\sim p_{dữ liệu (data / 데이터)}}[\log D(x)]
+
\mathbb E_{z\sim p(z)}[\log(1-D(G(z)))]
\]

## Discriminator optimum intuition

Với fixed generator phân phối (distribution / 분포) `p_g`, optimal discriminator:

\[
D^*(x)=\frac{p_{dữ liệu (data / 데이터)}(x)}{p_{dữ liệu (data / 데이터)}(x)+p_g(x)}
\]

Substituting into mục tiêu (objective / 목표) links GAN huấn luyện (training / 학습) to Jensen–Shannon divergence under idealized conditions.

Generator thus tries make `p_g` indistinguishable from `p_data`.

## Non-Saturating Generator mất mát (loss / 손실)

Original generator minimizing:

\[
\log(1-D(G(z)))
\]

can have weak độ dốc (gradient / 기울기) when discriminator confidently rejects fakes early.

Dùng chung (common / 공통) alternative maximize:

\[
\log D(G(z))
\]

or minimize negative log. Same equilibrium intuition, stronger early gradients.

## Why adversarial mất mát (loss / 손실) can create sharp images

Điểm ảnh (pixel / 픽셀) MSE encourages averaging when multiple plausible outputs exist, often blurry.

Discriminator learns high-dimensional criterion for “looks like real dữ liệu (data / 데이터)”, providing perceptual distribution-level tín hiệu (signal / 신호) beyond per-pixel lỗi (error / 오류).

This can yield sharp samples, but huấn luyện (training / 학습) becomes game between moving objectives.

## Chế độ (mode / 모드) Collapse

Generator may map many latent inputs to same/small set of outputs that fool discriminator.

Then samples look plausible but lack diversity.

This is **chế độ (mode / 모드) collapse**.

Detection requires diversity metrics/inspection, not only individual mẫu (sample / 표본) chất lượng (quality / 품질).

## Huấn luyện (training / 학습) Instability

GAN tối ưu hóa (optimization / 최적화) is not simple minimization of fixed mất mát (loss / 손실); both players thay đổi (change / 변경).

Possible dynamics:

- oscillation;
- discriminator too strong → weak generator gradients;
- generator exploits temporary discriminator blind spots;
- divergence.

Balance kiến trúc (architecture / 아키텍처), học tập (learning / 학습) rates, cập nhật (update / 업데이트) ratios and regularization matter.

## Wasserstein GAN

WGAN replaces discriminator xác suất (probability / 확률) interpretation with critic and uses Wasserstein-1 / Earth Mover intuition:

\[
W(p_r,p_g)=\sup_{\|f\|_L\le1}
\mathbb E_{p_r}[f(x)]-
\mathbb E_{p_g}[f(x)]
\]

Need Lipschitz ràng buộc (constraint / 제약조건). Original WGAN used weight clipping; WGAN-GP uses độ dốc (gradient / 기울기) penalty:

\[
\lambda(\|\nabla_{\hat x}D(\hat x)\|_2-1)^2
\]

providing more stable huấn luyện (training / 학습) in many regimes.

## Conditional GAN

Điều kiện (condition / 조건) generator/discriminator on label/ngữ cảnh (context / 맥락) `y`:

\[
G(z,y),\qquad D(x,y)
\]

allows class-controlled generation.

Image-to-image GANs điều kiện (condition / 조건) on nguồn (source / 소스) ảnh (image / 이미지), enabling translation like edges→photo, segmentation→ảnh (image / 이미지).

## CycleGAN

When paired examples unavailable, CycleGAN uses two mappings `G:X→Y`, `F:Y→X` and cycle consistency:

\[
F(G(x))\approx x
\]

\[
G(F(y))\approx y
\]

This imposes structural ràng buộc (constraint / 제약조건) but does not guarantee ngữ nghĩa (semantic / 의미적) tính đúng đắn (correctness / 정확성); ánh xạ (mapping / 매핑) can exploit hidden shortcuts.

## StyleGAN

StyleGAN-family redesigned generator with style modulation, ánh xạ (mapping / 매핑) mạng (network / 네트워크) and multi-scale controls, achieving high-quality controllable face/ảnh (image / 이미지) synthesis.

Its significance is architectural: latent điều khiển (control / 제어) injected across layers rather than only đầu vào (input / 입력) noise.

## GAN Evaluation

**FID (Fréchet Inception Distance)** compares means/covariances of Inception tính năng (feature / 기능) distributions:

\[
FID=\|\mu_r-\mu_g\|^2+
Tr(\Sigma_r+\Sigma_g-2(\Sigma_r\Sigma_g)^{1/2})
\]

Lower generally better.

But FID depends tính năng (feature / 기능) extractor/cỡ mẫu (sample size / 표본 크기) and can be gamed/limited. It mixes fidelity/diversity imperfectly.

Precision/Recall for generative các mô hình (models / 모델들) can separate mẫu (sample / 표본) chất lượng (quality / 품질) vs coverage.

Human evaluation may still matter.

## GAN vs tường minh (explicit / 명시적) Likelihood

GAN defines implicit generative phân phối (distribution / 분포) via sampling `z→G(z)`. Usually no tractable `p_G(x)` density.

VAE/diffusion have more tường minh (explicit / 명시적) probabilistic huấn luyện (training / 학습) formulations.

GAN excels direct fast generation: one forward pass after huấn luyện (training / 학습), unlike iterative diffusion.

## Adversarial huấn luyện (training / 학습) as Learned mất mát (loss / 손실)

A deep insight: discriminator acts as learned hàm mất mát (loss function / 손실 함수) that adapts to generator weaknesses.

Instead of hand-designing điểm ảnh (pixel / 픽셀) similarity, mô hình (model / 모델) learns criterion distinguishing real phân phối (distribution / 분포).

But adaptive mất mát (loss / 손실) makes tối ưu hóa (optimization / 최적화) nonstationary.

## GAN and Adversarial Examples are different concepts

“Adversarial” in GAN refers generator-discriminator game. **Adversarial examples** are intentionally perturbed inputs causing mô hình (model / 모델) thất bại (failure / 실패). Related game-theoretic flavor but distinct topics.

## Why Diffusion displaced GANs in many image-generation settings

Diffusion huấn luyện (training / 학습) tends to be more stable, covers modes better and scales well with conditioning, while GANs historically require delicate balancing.

GANs still useful where one-pass low-latency generation matters and in specialized domains.

Technology shifts do not make GAN conceptual kiến thức (knowledge / 지식) obsolete: adversarial objectives remain important in lĩnh vực (domain / 도메인) adaptation, biểu diễn (representation / 표현) học tập (learning / 학습) and an toàn (safety / 안전)/bảo mật (security / 보안).

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Generator: propose synthetic reality
Discriminator/Critic: learn what distinguishes proposal from data
Feedback: forces generator toward data distribution
```

The mất mát (loss / 손실) itself becomes learned through competition.

## Dùng chung (common / 공통) Misconceptions

### “GAN generator copies huấn luyện (training / 학습) images”

It learns ánh xạ (mapping / 매핑) from latent noise to samples; memorization can occur but is not cơ chế (mechanism / 메커니즘) definition.

### “If generated images look sharp, mô hình (model / 모델) phân phối (distribution / 분포) is good”

Chế độ (mode / 모드) collapse can produce sharp but low-diversity samples.

### “Discriminator accuracy should approach 100%”

At ideal equilibrium discriminator cannot distinguish and outputs ~0.5; huấn luyện (training / 학습) dynamics more complex.

### “WGAN simply changes mất mát (loss / 손실) name”

It changes divergence/distance khung phần mềm (framework / 프레임워크) and critic các ràng buộc (constraints / 제약조건들), altering độ dốc (gradient / 기울기) hành vi (behavior / 동작) fundamentally.

## Liên kết kiến thức (knowledge connection / 지식 연결)

GAN connects [Game/Adversarial Search intuition](../02_search_reasoning_and_planning/03_adversarial_search_and_games.md), [Optimization](../01_mathematical_foundations/06_optimization.md), [Probability/Distribution Learning](../01_mathematical_foundations/02_probability_for_ai.md) and [Representation Learning](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Diffusion Models](./09_diffusion_models.md).
