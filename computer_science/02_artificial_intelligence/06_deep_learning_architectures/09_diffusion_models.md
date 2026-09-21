# Diffusion Models: tạo dữ liệu bằng quá trình khử nhiễu có điều kiện

Diffusion Models (확산 모델) học generative distribution bằng một idea khác GAN: thay vì generator một bước phải tạo sample hoàn chỉnh ngay, ta định nghĩa một **forward process** dần phá data thành noise, rồi train model học **reverse denoising process** từng bước để quay từ noise về data.

Điều này biến generation thành một chuỗi bài toán local denoising tương đối ổn định.

## Forward Diffusion Process

Bắt đầu data:

\[
x_0\sim p_{data}
\]

Mỗi step thêm Gaussian noise:

\[
q(x_t\mid x_{t-1})=
\mathcal N(\sqrt{1-\beta_t}x_{t-1},\beta_t I)
\]

Define:

\[
\alpha_t=1-\beta_t,
\qquad
\bar\alpha_t=\prod_{s=1}^{t}\alpha_s
\]

Ta có closed form sample trực tiếp bất kỳ timestep:

\[
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon,
\qquad \epsilon\sim\mathcal N(0,I)
\]

As `t` large, signal destroyed và `x_t` gần Gaussian noise.

## Reverse Process

Goal learn:

\[
p_\theta(x_{t-1}\mid x_t)
\]

Nếu biết noise/data score, có thể gradually denoise.

DDPM parameterization phổ biến train neural network predict added noise:

\[
\epsilon_\theta(x_t,t)
\]

Loss simplified:

\[
L=\mathbb E_{x_0,\epsilon,t}
\left[
\|\epsilon-\epsilon_\theta(x_t,t)\|^2
\right]
\]

Network receives noisy sample + timestep and learns noise component.

## Tại sao predict noise giúp generation?

From:

\[
x_t=\sqrt{\bar\alpha_t}x_0+\sqrt{1-\bar\alpha_t}\epsilon
\]

if model estimates `ε`, one can estimate clean `x_0` or reverse mean. Repeating reverse steps gradually reconstructs data structure.

Model is learning denoising vector field across noise levels, not memorizing one deterministic mapping noise→image in single jump.

## Timestep Encoding

Same noisy image at low vs high noise requires different denoising behavior. Model therefore receives timestep/noise level embedding.

Sinusoidal/Fourier-like embeddings map scalar `t` into vector processed alongside features.

## U-Net Architecture

Image diffusion historically uses U-Net:

```text
high resolution
→ downsample encoder
→ bottleneck
→ upsample decoder
```

Skip connections pass fine spatial details from down path to up path.

Modern diffusion U-Nets include residual blocks, attention/cross-attention and normalization.

Transformer-based diffusion architectures (DiT-like) increasingly replace/augment U-Net at scale.

## Conditional Diffusion

Want generate `x` conditioned on text/class `c`:

\[
\epsilon_\theta(x_t,t,c)
\]

Text encoder creates embeddings; cross-attention injects text condition into image denoiser.

Thus text-to-image is multimodal encoder + conditional generative denoising system.

## Classifier Guidance

An external classifier estimates:

\[
\nabla_{x_t}\log p(c\mid x_t)
\]

and modifies reverse score toward desired class.

This improved conditional quality but requires classifier trained on noisy data.

## Classifier-Free Guidance

Train same model sometimes with condition dropped. At inference combine conditional and unconditional predictions:

\[
\epsilon_{guided}
=\epsilon_{uncond}
+w(\epsilon_{cond}-\epsilon_{uncond})
\]

`w` guidance scale.

Higher guidance often increases prompt adherence but can reduce diversity/oversaturate artifacts. Trade-off, not “higher better”.

## Score-Based View

Score function:

\[
\nabla_x\log p_t(x)
\]

points toward directions increasing data density at noise level `t`.

Denoising-score matching and diffusion are closely connected. Continuous-time formulation uses stochastic differential equations (SDEs).

This provides deeper probabilistic interpretation beyond “predict noise”.

## Sampling Speed

Original DDPM uses many reverse steps (hundreds/thousands), slower than one-pass GAN.

Accelerations:

- DDIM;
- higher-order samplers;
- DPM-Solver-like methods;
- distillation/consistency models;
- fewer-step schedules.

Sampler changes numerical integration/path, often trading speed vs quality/diversity.

## DDIM

DDIM constructs non-Markovian/deterministic-like sampling paths sharing training objective, enabling fewer steps and latent interpolation behavior.

`η`-style settings can control stochasticity depending formulation.

## Latent Diffusion

Raw pixel diffusion expensive. Latent diffusion first compress image:

\[
x\xrightarrow{VAE\ encoder}z
\]

run diffusion on `z`, then:

\[
z_0\xrightarrow{VAE\ decoder}\hat x
\]

Latent spatial resolution smaller → attention/U-Net computation drastically cheaper.

This is why understanding VAE matters for text-to-image systems.

## Image-to-Image và Inpainting

Image-to-image starts from encoded input plus controlled noise then denoises under text condition. Noise strength controls how far output may deviate.

Inpainting keeps known pixels/latent regions constrained and denoises masked region using surrounding context + prompt.

Outpainting extends canvas similarly.

These are conditioning/control variations, not completely different model classes.

## ControlNet-like Conditioning

Additional structural condition such as edge map, pose, depth can feed parallel/control branch while preserving pretrained diffusion model.

This separates semantic text control from geometric/spatial control.

## Diffusion vs VAE vs GAN

| Family | Training signal | Sampling | Typical trade-off |
|---|---|---|---|
| VAE | ELBO / reconstruction + KL | one decoder pass | smooth latent, likelihood framework, sometimes softer samples |
| GAN | adversarial critic | one generator pass | sharp/fast, unstable/mode collapse risk |
| Diffusion | denoising/score objective | iterative | stable/high quality, traditionally slower |

Modern systems hybridize, so taxonomy describes mechanisms, not product boundaries.

## Diffusion for non-image data

Diffusion/score methods apply audio, video, 3D, molecule, continuous actions. Discrete diffusion variants adapt process to categorical/token spaces.

However discrete language generation remains dominated autoregressive Transformers because corruption/reverse process and decoding trade-offs differ.

## Data and Copyright/Safety Connection

Generative model behavior reflects training distribution. Memorization can occur; model may reproduce styles/concepts/biases. Dataset provenance and deduplication matter.

Safety filters can operate training data, prompt, latent/generation and output — system problem beyond diffusion math.

## Mental Model

```text
Training:
real data → add known noise level → model predicts how to remove noise

Generation:
random noise → denoise a little → denoise a little → ... → structured sample
```

At every noise level, model learns local direction toward plausible data.

## Common Misconceptions

### “Diffusion stores images then retrieves nearest one”

Generation runs learned denoising dynamics. Memorization is separate risk, not core mechanism.

### “Noise prediction is arbitrary trick”

It arises from parameterization of reverse probabilistic/score process and yields simple stable objective.

### “More diffusion steps always better”

Sampler/order/training determine trade-off; advanced samplers achieve quality with fewer steps.

### “Guidance scale controls image quality only”

It trades conditioning strength against diversity/artifacts.

### “Stable Diffusion means diffusion is done directly in pixels”

Latent diffusion operates in VAE-compressed latent space, then decodes to pixels.

## Knowledge Connection

Diffusion synthesizes [Probability](../01_mathematical_foundations/02_probability_for_ai.md), [Numerical Methods](../01_mathematical_foundations/07_numerical_computation.md), [Autoencoder/VAE](./06_autoencoders.md), [Attention](./04_attention.md) and multimodal text conditioning.

Later `13_speech_audio_and_multimodal/` will connect diffusion with text/image/audio/video foundation systems.