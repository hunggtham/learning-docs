# Multimodal Transformers

Transformer architecture phù hợp multimodal AI vì attention cho phép tokens từ nhiều sources tương tác trong cùng computation graph. Tuy nhiên “multimodal Transformer” không phải một architecture duy nhất; có nhiều patterns tùy cách encode và fuse modalities.

## Pattern 1: Separate Encoders + Late Fusion

```text
image → vision encoder → embedding
text → text encoder → embedding
→ similarity / classifier
```

CLIP-like dual encoder rất efficient cho retrieval vì image/text embeddings có thể precompute independently.

Nhược điểm: interaction coarse, thường global embedding-level.

## Pattern 2: Cross-Attention

Text queries visual keys/values:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Visual encoder giữ modality-specific representation; cross-attention cho conditional reasoning.

Có thể stack repeated cross-attention blocks.

## Pattern 3: Unified Sequence

Project all modalities thành same hidden dimension rồi concatenate:

```text
[visual tokens][audio tokens][text tokens]
```

Một Transformer xử lý chung. Simpler conceptual architecture, nhưng sequence length lớn.

## Token-Type / Modality Encoding

Model cần biết token đến từ image/audio/text. Có thể add modality embeddings hoặc rely on positional/layout conventions.

## Positional Structure

Text 1D; image 2D; video 3D (time × height × width); audio time-frequency.

Flattening thành 1D tokens cần encode original geometry/time. Relative position biases hoặc factorized positional embeddings preserve structure.

## Cross-Modal Attention Matrix

Nếu text length `T`, visual tokens `V`, full unified self-attention cost gần:

\[
O((T+V)^2)
\]

High-resolution vision/video làm `V` dominate. Resampling/compression critical.

## Perceiver / Resampler

Introduce fixed set latent queries `L` attend huge modality sequence:

\[
L\ll V
\]

Cost of cross-attention ~`O(LV)` then downstream operates on `L` latents.

This is information bottleneck; choosing number latent queries trades detail vs compute.

## Q-Former Pattern

Learnable query tokens attend frozen visual encoder outputs and produce compact visual representation for language model.

Useful when connecting frozen pretrained components.

## Modality Adapters

Instead full joint pretraining, use small adapters/projectors to bridge encoders to shared backbone. Parameter-efficient but alignment capacity limited.

## Joint Pretraining Objectives

A multimodal transformer may optimize multiple objectives:

```text
contrastive alignment
matching classification
caption generation
masked token/patch prediction
next-token prediction
grounding
instruction following
```

Multi-objective training balances semantics and detailed grounding.

## Causal Masking Across Modalities

For generative model, attention mask decides which tokens can see which.

Image tokens may be fully visible context; text decoder causal. In unified autoregressive models, modality ordering/masking controls generation direction.

## Generating Images/Audio as Tokens

If image/audio converted to discrete codec tokens, Transformer can model them autoregressively along with text.

Challenges:

- much higher token rate;
- error accumulation;
- modality-specific perceptual loss;
- long sequences.

Diffusion/flow models often more efficient for high-dimensional continuous generation.

## Mixture of Experts

Multimodal MoE can route tokens to specialized experts while sharing backbone. Routing may be modality-aware or learned dynamically.

This increases capacity without dense compute proportional to all parameters.

## Modality Dropout

During training randomly remove modalities so model remains robust if input incomplete. Otherwise system may overdepend on easiest modality.

## Cross-Modal Shortcut Learning

If captions leak label directly, model may ignore image. If visual cue strongly predicts answer, it may ignore text instruction. Training/evaluation should include counterfactual cases requiring both modalities.

## Synchronization

Audio-video transformer needs aligned timestamps. Relative timing can indicate lip movements, events, speaker turns.

If streams unsynchronized, model may learn spurious associations.

## Long Video

Video tokens explode:

\[
N = frames \times patches/frame
\]

Techniques:

- sparse frame sampling;
- temporal pooling;
- hierarchical summaries;
- event-based retrieval;
- memory modules;
- streaming attention.

## Streaming Multimodal Models

Real-time assistant receives partial audio/video over time. Need incremental state/KV cache and policy for when to respond vs wait for more evidence.

This resembles partially observable agent system.

## Multimodal Generation

One system can accept text/image/audio and output multiple modalities. Architecture may use shared semantic backbone + modality-specific decoders.

Shared representation should preserve intent while decoder handles waveform/pixel generation details.

## Evaluation

Test modality-specific and cross-modal capabilities separately:

```text
vision only
audio only
text only
vision+text required
audio+vision conflict
missing modality
adversarial visual text
```

A model scoring high on mixed benchmark may rely primarily one modality.

## Mental Model

> **Multimodal Transformer is an information-routing system: encoders create tokens, attention decides what information crosses modality boundaries, and compression/masking determines what can be preserved.**

## Common Misconceptions

### “Unified model means unified understanding automatically”

Shared parameters/tokens do not guarantee fine-grained cross-modal grounding.

### “More visual/audio tokens always improve quality”

Compute/noise increase and model may not effectively use them.

### “Cross-attention explains exactly what model used”

Attention weights are interaction signals, not complete causal explanations.

## Knowledge Connection

Multimodal Transformers extend [Transformer](../06_deep_learning_architectures/05_transformer.md) across heterogeneous token spaces and form backbone for multimodal agents.

Xem tiếp: [Multimodal Agents](./06_multimodal_agents.md).