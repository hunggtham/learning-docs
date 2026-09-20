# Variational Autoencoders: latent space như một probabilistic model

Variational Autoencoder (VAE / 변분 오토인코더) mở rộng autoencoder từ deterministic compression thành một **latent-variable generative model**. Encoder không output một latent vector duy nhất; nó approximate distribution của latent variable `z` conditioned on input `x`. Decoder defines likelihood của data given latent.

Mục tiêu là vừa reconstruct data vừa làm latent distribution có structure gần một prior đơn giản để có thể sample/generate.

## Generative model

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

Data likelihood:

\[
p_\theta(x)=\int p(z)p_\theta(x\mid z)dz
\]

Integral thường intractable với neural decoder.

## Inference problem

True posterior:

\[
p_\theta(z\mid x)=\frac{p(z)p_\theta(x\mid z)}{p_\theta(x)}
\]

khó compute vì denominator integral.

VAE introduce encoder distribution:

\[
q_\phi(z\mid x)
\]

để approximate posterior. Đây là **variational inference**.

## Evidence Lower Bound (ELBO)

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

encourage latent explain input well.

### KL Regularization

\[
D_{KL}(q_\phi(z\mid x)\|p(z))
\]

encourage posterior codes stay close prior.

Loss often written:

\[
L_{VAE}=L_{recon}+D_{KL}(q(z\mid x)\|p(z))
\]

with sign/convention differences.

## Why regularize latent toward prior?

Vanilla autoencoder maps examples to arbitrary isolated regions. Sampling random Gaussian point may land where decoder never trained.

VAE pushes encoded distributions to occupy a smoother prior-compatible space, making:

\[
z\sim\mathcal N(0,I)
\]

then decode feasible.

Trade-off: too much KL can reduce reconstruction detail.

## Gaussian Encoder

Common encoder outputs:

\[
\mu_\phi(x),\qquad \log\sigma_\phi^2(x)
\]

and defines:

\[
q_\phi(z\mid x)=\mathcal N(\mu,diag(\sigma^2))
\]

Why output log variance? Variance must positive; log-space unconstrained/stable and exponentiate when needed.

## Reparameterization Trick

Naively sampling:

\[
z\sim\mathcal N(\mu,\sigma^2)
\]

puts stochastic node depending on parameters, hard for pathwise gradient.

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

For diagonal Gaussian vs standard normal:

\[
D_{KL}(q\|p)=\frac12\sum_j
(\mu_j^2+\sigma_j^2-\log\sigma_j^2-1)
\]

Thus no Monte Carlo needed for KL term in standard VAE.

## Decoder likelihood determines reconstruction loss

If:

\[
p(x\mid z)=\mathcal N(\mu_\theta(z),\sigma^2I)
\]

negative log-likelihood corresponds roughly MSE.

For Bernoulli outputs, BCE-like likelihood.

Choosing reconstruction loss is choosing observation model assumptions.

## β-VAE

Modify:

\[
L=L_{recon}+\beta D_{KL}
\]

`β>1` strengthens prior pressure and sometimes improves factorized/disentangled structure at cost reconstruction.

But disentanglement is not guaranteed; identifiability needs assumptions.

## Posterior Collapse

Powerful decoder may ignore `z`:

\[
q(z\mid x)\approx p(z)
\]

KL near zero and latent carries little information.

Common in text VAEs with autoregressive decoder because decoder can model sequence without latent.

Mitigations:

- KL annealing;
- free bits;
- weaker decoder;
- architecture/objective changes.

## Latent Interpolation

Because latent prior is regularized, interpolation usually smoother than vanilla AE.

But linear interpolation in Gaussian space not always probability-geodesic optimal; spherical interpolation sometimes used.

Smooth visualization does not prove semantic disentanglement.

## VAE vs GAN vs Diffusion

VAE:

- explicit latent probabilistic model;
- ELBO likelihood lower bound;
- stable end-to-end training;
- samples historically blurrier in pixel space depending decoder/loss.

GAN:

- adversarial implicit distribution;
- sharp samples;
- unstable training/mode collapse risk.

Diffusion:

- iterative denoising likelihood/score-based family;
- high sample quality/stable training;
- slower iterative sampling traditionally.

Modern systems combine ideas, e.g. latent diffusion uses VAE-like image autoencoder to compress images before diffusion.

## Latent Diffusion Connection

Stable-Diffusion-like pipeline often:

```text
image
→ VAE encoder
→ latent spatial representation
→ diffusion denoising in latent space
→ VAE decoder
→ image
```

VAE here reduces compute by moving diffusion from raw pixels to compressed latent.

Thus VAE remains central even when diffusion is visible generation mechanism.

## Variational Inference Connection

VAE is not only autoencoder with noise. It is amortized variational inference: one encoder network learns mapping from any `x` to approximate posterior parameters, instead of running separate optimization per datapoint.

**Amortization** shares inference computation across dataset.

## Mental Model

```text
Encoder: x → distribution over plausible latent causes z
Prior:   regularizes latent world to a sampleable space
Decoder: z → distribution over observations x
ELBO:    balance explaining data vs keeping latent posterior compatible with prior
```

## Common Misconceptions

### “VAE encoder outputs latent vector”

It usually outputs distribution parameters; latent is sampled/reparameterized.

### “KL term just prevents overfitting”

It aligns approximate posterior with prior, enabling coherent generative latent space and controlling information capacity.

### “VAE loss = MSE + KL always”

Reconstruction term depends chosen likelihood; MSE is one case.

### “VAE guarantees disentangled human-readable latent factors”

No. Disentanglement requires stronger assumptions/objectives/data.

## Knowledge Connection

VAE combines [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [KL Divergence / Information Theory](../01_mathematical_foundations/05_information_theory.md), [Autoencoders](./06_autoencoders.md) and variational inference.

Xem tiếp: [Generative Adversarial Networks](./08_generative_adversarial_networks.md) and [Diffusion Models](./09_diffusion_models.md).