# Autoencoders: học representation bằng reconstruction

Autoencoder (오토인코더) là architecture học mapping:

\[
x\xrightarrow{Encoder}z\xrightarrow{Decoder}\hat x
\]

với objective reconstruct input:

\[
L=L(x,\hat x)
\]

Nó là một trong những cách trực quan nhất để hiểu representation learning không cần human labels. Nhưng “reconstruct tốt” không tự động nghĩa latent space semantically tốt; mọi thiết kế bottleneck/noise/objective đều quyết định information nào được giữ.

## Undercomplete Autoencoder

Nếu latent dimension:

\[
d_z<d_x
\]

network bị buộc compress input qua bottleneck.

Linear autoencoder với squared-error và constraints phù hợp học subspace liên quan PCA. Nonlinear autoencoder có thể learn nonlinear manifold.

Nhưng nếu decoder quá powerful, latent có thể vẫn encode idiosyncratic detail thay vì useful abstraction.

## Reconstruction Loss

Continuous normalized data có thể dùng MSE:

\[
L=\|x-\hat x\|_2^2
\]

Binary/Bernoulli-like pixels historically dùng BCE.

Modern image reconstruction may use perceptual losses vì pixel MSE penalizes small shifts strongly và often yields blurry averages.

Loss defines what “similar reconstruction” means.

## Overcomplete Autoencoder

Nếu latent dimension lớn hơn input, model có thể learn identity trivially. Cần regularization hoặc corruption để force meaningful structure.

Examples:

- sparse autoencoder;
- denoising autoencoder;
- contractive autoencoder.

## Sparse Autoencoder

Encourage most latent activations near zero. Objective:

\[
L=L_{recon}+\lambda R(z)
\]

Sparsity forces representation use limited active features per input.

Modern mechanistic interpretability also explores sparse autoencoders to decompose dense LLM activations into sparse learned features, though interpretation remains research problem.

## Denoising Autoencoder

Corrupt input:

\[
\tilde x\sim q(\tilde x\mid x)
\]

train:

\[
\tilde x\to Encoder\to z\to Decoder\to \hat x\approx x
\]

Model cannot simply copy; it learns structure needed to recover clean data.

This principle connects directly to masked language modeling and diffusion denoising: corrupt data then learn recovery.

## Contractive Autoencoder

Penalize sensitivity of latent representation to small input changes, e.g. encoder Jacobian norm:

\[
\|\partial f(x)/\partial x\|_F^2
\]

encouraging locally stable representation.

## Autoencoder for Anomaly Detection

Train mostly normal data. If normal patterns reconstruct well, anomaly may have high reconstruction error:

\[
s(x)=\|x-\hat x\|
\]

But high-capacity autoencoder can reconstruct anomalies too, and some normal rare patterns reconstruct poorly. Score needs validation/thresholding.

## Latent Interpolation

If latent space is smooth, interpolate:

\[
z(\alpha)=(1-\alpha)z_1+\alpha z_2
\]

and decode intermediate samples.

Vanilla autoencoder does not guarantee latent regions between training codes decode realistically. This motivates probabilistic regularization in VAE.

## Sequence Autoencoder

Encoder can be RNN/Transformer; decoder reconstructs sequence. Latent bottleneck may summarize sequence.

But token reconstruction with powerful autoregressive decoder risks **posterior/latent ignoring**: decoder can predict from context without using latent much.

Objective/architecture must ensure latent matters.

## Convolutional Autoencoder

Images often use CNN encoder/downsampling and decoder/upsampling. Decoder may use transposed convolution or resize+conv.

Transposed conv can produce checkerboard artifacts if stride/kernel interplay poor.

## Autoencoder vs PCA

PCA:

- linear;
- closed-form/SVD;
- globally optimal for linear squared reconstruction;
- components orthogonal.

Autoencoder:

- nonlinear;
- trained iteratively;
- flexible architecture/loss;
- latent dimensions not necessarily identifiable/orthogonal.

Use PCA when linear structure sufficient and interpretability/stability matter; autoencoder when nonlinear representation justified by data/scale.

## Autoencoder vs Compression Codec

A learned autoencoder can act compression system, but practical compression also requires quantization and entropy coding.

Continuous latent floats are not automatically compressed bitstream. Rate-distortion objective adds bitrate term:

\[
L=Distortion+\lambda Rate
\]

This connects representation learning with Information Theory.

## Bottleneck is not only dimensional

Even if latent dimension large, constraints can create information bottleneck:

- sparsity;
- noise;
- quantization;
- low precision;
- limited channel capacity;
- probabilistic prior.

VAE uses distribution regularization rather than only dimension.

## Autoencoders and Foundation Models

Masked autoencoders reconstruct missing image patches. BERT-style masking reconstructs masked tokens/distributions. Denoising seq2seq corrupts text and reconstructs original.

These are not identical to classic autoencoder, but share principle: **self-supervised learning through information removal/corruption and reconstruction**.

## Mental Model

> Autoencoder asks: “Nếu buộc dữ liệu đi qua một constrained channel, representation nào giữ đủ structure để reconstruct?”

Constraint defines what abstraction emerges.

## Common Misconceptions

### “Latent smaller means representation meaningful”

Compression alone không guarantee semantics.

### “Low reconstruction error means good downstream features”

Model may preserve nuisance detail irrelevant task.

### “Autoencoder generates new realistic samples automatically”

Vanilla latent distribution is irregular; arbitrary sampled `z` may decode nonsense.

### “Autoencoder compression = file compression”

Need quantization/entropy coding and rate model for actual bit-efficient codec.

## Knowledge Connection

Autoencoder extends [Representation Learning](../05_neural_networks/08_representation_learning.md) and [Dimensionality Reduction](../04_machine_learning/12_dimensionality_reduction.md).

Xem tiếp: [Variational Autoencoders](./07_variational_autoencoders.md), where latent space becomes probabilistic and sampleable.