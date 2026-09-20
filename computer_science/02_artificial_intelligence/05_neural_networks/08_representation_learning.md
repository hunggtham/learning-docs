# Representation Learning: học cách biểu diễn dữ liệu

Representation Learning (표현 학습 / học biểu diễn) là một trong những ý tưởng trung tâm nhất của Deep Learning. Thay vì chỉ học mapping trực tiếp `input → output`, network học intermediate spaces trong đó những factors relevant cho task được sắp xếp theo geometry dễ xử lý hơn.

Một representation tốt không có nghĩa “vector nhìn đẹp”. Nó phải làm downstream computation đơn giản, robust hoặc transferable hơn.

## Representation là gì?

Raw object có thể rất phức tạp:

- image: pixels;
- text: token sequence;
- audio: waveform;
- user: interaction history;
- molecule: graph.

Encoder tạo vector/tensor:

\[
z=f_\theta(x)
\]

`z` là learned representation.

Downstream head:

\[
\hat y=g_\phi(z)
\]

Nếu `z` organize task-relevant information tốt, `g` có thể rất simple.

## Linear Probe như một test

Nếu frozen representation `z` cho phép linear classifier đạt performance cao, ta nói target information **linearly accessible**.

Linear probe không đo toàn bộ semantic richness, nhưng là useful diagnostic: feature extractor đã “untangle” task đến mức nào?

## Distributed Representation

One-hot symbol đặt mỗi category ở orthogonal axis; không encode similarity.

Dense learned embedding:

\[
z\in R^d
\]

có thể encode multiple factors distributed across dimensions/directions.

Similarity relation xuất hiện từ training objective, không từ vector format tự thân.

## Embedding Geometry

Nếu contrastive training kéo related pairs gần nhau và đẩy unrelated pairs xa:

```text
semantically related objects → nearby directions/regions
unrelated objects → farther apart
```

thì cosine/dot-product retrieval becomes meaningful.

Nhưng geometry objective-specific. Embedding tốt cho semantic search chưa chắc tốt cho sentiment clustering hoặc recommendation.

## Supervised Representation Learning

Classifier network learn hidden representation vì final task loss backprop through encoder.

Hidden layers retain information useful cho target và có thể discard nuisance factors.

Nếu target narrow, representation cũng có thể narrow và transfer kém.

## Self-Supervised Representation Learning

Self-supervision tạo learning signal từ raw data.

Examples:

- predict next token;
- reconstruct masked token/patch;
- contrast views of same image;
- predict future segment;
- reconstruct corrupted input.

Mục tiêu là exploit abundant unlabeled data để learn reusable structure.

Foundation models largely rely on self-supervised pretraining rồi adapt downstream.

## Contrastive Learning

Given positive pair `(x,x⁺)` and negatives `x⁻`, objective encourage similarity positive > negatives.

InfoNCE-style loss:

\[
L=-\log
\frac{\exp(sim(z,z^+)/\tau)}
{\sum_j\exp(sim(z,z_j)/\tau)}
\]

`τ` là temperature.

Choice positive pairs defines invariance. Image augmentations say two crops/color variants should represent same semantic object. Wrong augmentation can erase task-relevant information.

## Metric Learning

Triplet loss:

\[
L=\max(0,d(a,p)-d(a,n)+m)
\]

push anchor-positive closer than anchor-negative by margin `m`.

Hard-negative mining is critical: easy negatives produce little gradient; false negatives can damage semantic geometry.

## Autoencoder Representation

Encoder-decoder:

\[
x\to z\to\hat x
\]

Reconstruction objective forces `z` to preserve input information needed for reconstruction.

But pixel-perfect reconstruction may prioritize low-level detail not semantics. Bottleneck/denoising/variational constraints alter learned factors.

Thus objective determines what “important information” means.

## Bottleneck và Compression

A lower-dimensional `z` forces compression. Under an Information Bottleneck intuition, representation should keep information useful for target while discarding irrelevant variation.

Formal Information Bottleneck studies trade-off between `I(X;Z)` and `I(Z;Y)`, but practical deep networks do not always directly optimize this formula.

Mental idea remains useful: good representation filters nuisance while preserving predictive structure.

## Invariance và Equivariance

**Invariant** representation: transformation of input should not change representation/output.

Example image classification may want translation invariance.

**Equivariant** representation: output changes predictably with input transformation.

For segmentation/pose, spatial shift should shift output correspondingly, not erase location.

Architecture and augmentation encode these assumptions.

## Transfer Learning

Pretrained encoder learns broad representation, then downstream task uses:

- frozen features + new head;
- partial fine-tuning;
- full fine-tuning;
- adapters/LoRA.

Transfer works when pretraining representation covers factors relevant downstream.

Negative transfer occurs when source biases/objective mismatch target.

## Representation Collapse

Some self-supervised objectives risk all inputs map to same constant vector. Then similarity trivial nhưng no information.

Contrastive negatives, stop-gradient asymmetry, predictor architecture, variance/covariance regularizers or teacher-student dynamics prevent collapse in different methods.

Understanding collapse clarifies why self-supervised loss design matters.

## Disentanglement

Idealized disentangled representation assigns distinct latent factors to independent generative causes. Example rotation, lighting, identity separated.

In practice disentanglement is difficult and often not identifiable without inductive bias/supervision. Do not assume latent dimensions map cleanly to human concepts.

## Sparse vs Dense Representations

Sparse representation activates few components; dense uses many.

Sparse can improve interpretability/storage/retrieval properties. Dense embeddings are compact and differentiable.

Modern retrieval increasingly combines sparse lexical and dense semantic representations because they capture complementary structure.

## Representation Drift

When encoder is retrained, embedding geometry changes. Stored vectors in vector database generated by old encoder may become incompatible.

Production consequence:

```text
embedding model version change
→ re-embed corpus
→ rebuild/revalidate index
```

Representation versioning is an LLMOps/data-engineering concern, not just model theory.

## Probing và Interpretability

Probe classifiers can detect whether information exists in representation, but high probe accuracy does not prove base model actually uses that information causally.

Interventions/ablation are needed for stronger claims.

Representation interpretability must distinguish **decodability** from **causal use**.

## LLM Hidden States Preview

Transformer converts token embeddings through layers into contextual representations. Same token can have different hidden vector depending context.

Final hidden state feeds output projection/softmax for next-token prediction. Intermediate layers may encode syntax, semantic, factual and task structure in distributed form.

This chapter therefore directly prepares embeddings/Transformer/LLM sections.

## Mental Model

> Representation learning = học một coordinate system nơi relationships relevant cho objective trở nên dễ tính hơn.

Raw space không nhất thiết có useful geometry; training bends/reorganizes space.

## Common Misconceptions

### “Embedding gần nhau nghĩa objects giống nhau tuyệt đối”

Chúng gần theo geometry/objective/model/data cụ thể.

### “Latent dimension 42 chắc chắn đại diện một concept”

Information thường distributed/subspace-based.

### “Self-supervised model không cần labels nên objective neutral”

Pretext task, augmentation và sampling chính là inductive bias mạnh.

### “Nếu information decodable từ hidden state thì model đang dùng nó”

Decodability không chứng minh causal reliance.

## Knowledge Connection

Representation Learning nối [Dimensionality Reduction](../04_machine_learning/12_dimensionality_reduction.md), [Information Theory](../01_mathematical_foundations/05_information_theory.md), [Regularization](./07_regularization.md) và sau này [Embeddings](../08_large_language_models/02_embeddings_and_semantic_space.md), [RAG](../09_retrieval_and_rag/05_rag_fundamentals.md).