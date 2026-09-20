# Generative Adversarial Networks: học phân phối qua một trò chơi đối kháng

Generative Adversarial Network (GAN / 생성적 적대 신경망) học generative model bằng cách đặt **generator** và **discriminator** vào một game đối kháng. Generator tạo fake samples; discriminator cố phân biệt real/fake. Generator cải thiện để discriminator khó nhận ra hơn.

GAN quan trọng vì nó cho thấy generative learning không nhất thiết cần explicit likelihood. Distribution có thể được học thông qua một learned critic/discriminator signal.

## Hai networks

Generator:

\[
z\sim p(z),\qquad x_{fake}=G_\theta(z)
\]

Discriminator:

\[
D_\phi(x)\in(0,1)
\]

ước lượng input real hay generated.

Original minimax objective:

\[
\min_G\max_D
\mathbb E_{x\sim p_{data}}[\log D(x)]
+
\mathbb E_{z\sim p(z)}[\log(1-D(G(z)))]
\]

## Discriminator optimum intuition

Với fixed generator distribution `p_g`, optimal discriminator:

\[
D^*(x)=\frac{p_{data}(x)}{p_{data}(x)+p_g(x)}
\]

Substituting into objective links GAN training to Jensen–Shannon divergence under idealized conditions.

Generator thus tries make `p_g` indistinguishable from `p_data`.

## Non-Saturating Generator Loss

Original generator minimizing:

\[
\log(1-D(G(z)))
\]

can have weak gradient when discriminator confidently rejects fakes early.

Common alternative maximize:

\[
\log D(G(z))
\]

or minimize negative log. Same equilibrium intuition, stronger early gradients.

## Why adversarial loss can create sharp images

Pixel MSE encourages averaging when multiple plausible outputs exist, often blurry.

Discriminator learns high-dimensional criterion for “looks like real data”, providing perceptual distribution-level signal beyond per-pixel error.

This can yield sharp samples, but training becomes game between moving objectives.

## Mode Collapse

Generator may map many latent inputs to same/small set of outputs that fool discriminator.

Then samples look plausible but lack diversity.

This is **mode collapse**.

Detection requires diversity metrics/inspection, not only individual sample quality.

## Training Instability

GAN optimization is not simple minimization of fixed loss; both players change.

Possible dynamics:

- oscillation;
- discriminator too strong → weak generator gradients;
- generator exploits temporary discriminator blind spots;
- divergence.

Balance architecture, learning rates, update ratios and regularization matter.

## Wasserstein GAN

WGAN replaces discriminator probability interpretation with critic and uses Wasserstein-1 / Earth Mover intuition:

\[
W(p_r,p_g)=\sup_{\|f\|_L\le1}
\mathbb E_{p_r}[f(x)]-
\mathbb E_{p_g}[f(x)]
\]

Need Lipschitz constraint. Original WGAN used weight clipping; WGAN-GP uses gradient penalty:

\[
\lambda(\|\nabla_{\hat x}D(\hat x)\|_2-1)^2
\]

providing more stable training in many regimes.

## Conditional GAN

Condition generator/discriminator on label/context `y`:

\[
G(z,y),\qquad D(x,y)
\]

allows class-controlled generation.

Image-to-image GANs condition on source image, enabling translation like edges→photo, segmentation→image.

## CycleGAN

When paired examples unavailable, CycleGAN uses two mappings `G:X→Y`, `F:Y→X` and cycle consistency:

\[
F(G(x))\approx x
\]

\[
G(F(y))\approx y
\]

This imposes structural constraint but does not guarantee semantic correctness; mapping can exploit hidden shortcuts.

## StyleGAN

StyleGAN-family redesigned generator with style modulation, mapping network and multi-scale controls, achieving high-quality controllable face/image synthesis.

Its significance is architectural: latent control injected across layers rather than only input noise.

## GAN Evaluation

**FID (Fréchet Inception Distance)** compares means/covariances of Inception feature distributions:

\[
FID=\|\mu_r-\mu_g\|^2+
Tr(\Sigma_r+\Sigma_g-2(\Sigma_r\Sigma_g)^{1/2})
\]

Lower generally better.

But FID depends feature extractor/sample size and can be gamed/limited. It mixes fidelity/diversity imperfectly.

Precision/Recall for generative models can separate sample quality vs coverage.

Human evaluation may still matter.

## GAN vs Explicit Likelihood

GAN defines implicit generative distribution via sampling `z→G(z)`. Usually no tractable `p_G(x)` density.

VAE/diffusion have more explicit probabilistic training formulations.

GAN excels direct fast generation: one forward pass after training, unlike iterative diffusion.

## Adversarial Training as Learned Loss

A deep insight: discriminator acts as learned loss function that adapts to generator weaknesses.

Instead of hand-designing pixel similarity, model learns criterion distinguishing real distribution.

But adaptive loss makes optimization nonstationary.

## GAN and Adversarial Examples are different concepts

“Adversarial” in GAN refers generator-discriminator game. **Adversarial examples** are intentionally perturbed inputs causing model failure. Related game-theoretic flavor but distinct topics.

## Why Diffusion displaced GANs in many image-generation settings

Diffusion training tends to be more stable, covers modes better and scales well with conditioning, while GANs historically require delicate balancing.

GANs still useful where one-pass low-latency generation matters and in specialized domains.

Technology shifts do not make GAN conceptual knowledge obsolete: adversarial objectives remain important in domain adaptation, representation learning and safety/security.

## Mental Model

```text
Generator: propose synthetic reality
Discriminator/Critic: learn what distinguishes proposal from data
Feedback: forces generator toward data distribution
```

The loss itself becomes learned through competition.

## Common Misconceptions

### “GAN generator copies training images”

It learns mapping from latent noise to samples; memorization can occur but is not mechanism definition.

### “If generated images look sharp, model distribution is good”

Mode collapse can produce sharp but low-diversity samples.

### “Discriminator accuracy should approach 100%”

At ideal equilibrium discriminator cannot distinguish and outputs ~0.5; training dynamics more complex.

### “WGAN simply changes loss name”

It changes divergence/distance framework and critic constraints, altering gradient behavior fundamentally.

## Knowledge Connection

GAN connects [Game/Adversarial Search intuition](../02_search_reasoning_and_planning/03_adversarial_search_and_games.md), [Optimization](../01_mathematical_foundations/06_optimization.md), [Probability/Distribution Learning](../01_mathematical_foundations/02_probability_for_ai.md) and [Representation Learning](../05_neural_networks/08_representation_learning.md).

Xem tiếp: [Diffusion Models](./09_diffusion_models.md).