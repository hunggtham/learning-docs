# Multimodal Transformers

> **Mạch đọc:** Đặt **Multimodal Transformers** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **mẫu (pattern / 패턴) 1: Separate Encoders + Late Fusion** sang **mẫu (pattern / 패턴) 2: Cross-Attention**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Transformer kiến trúc (architecture / 아키텍처) phù hợp multimodal AI vì attention cho phép tokens từ nhiều sources tương tác trong cùng computation đồ thị (graph / 그래프). Tuy nhiên “multimodal Transformer” không phải một kiến trúc (architecture / 아키텍처) duy nhất; có nhiều patterns tùy cách encode và fuse modalities.

## Mẫu (pattern / 패턴) 1: Separate Encoders + Late Fusion

```text
image → vision encoder → embedding
text → text encoder → embedding
→ similarity / classifier
```

CLIP-like dual encoder rất efficient cho retrieval vì ảnh (image / 이미지)/văn bản (text / 텍스트) embeddings có thể precompute independently.

Nhược điểm: tương tác (interaction / 상호작용) coarse, thường toàn cục (global / 전역) embedding-level.

## Mẫu (pattern / 패턴) 2: Cross-Attention

Văn bản (text / 텍스트) queries visual keys/values:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Visual encoder giữ modality-specific biểu diễn (representation / 표현); cross-attention cho conditional lập luận (reasoning / 추론).

Có thể ngăn xếp (stack / 스택) repeated cross-attention blocks.

## Mẫu (pattern / 패턴) 3: Unified chuỗi (sequence / 시퀀스)

Dự án (project / 프로젝트) all modalities thành same hidden dimension rồi concatenate:

```text
[visual tokens][audio tokens][text tokens]
```

Một Transformer xử lý chung. Simpler conceptual kiến trúc (architecture / 아키텍처), nhưng chuỗi (sequence / 시퀀스) length lớn.

## Token-Type / Modality Encoding

Mô hình (model / 모델) cần biết đơn vị từ (token / 토큰) đến từ ảnh (image / 이미지)/audio/văn bản (text / 텍스트). Có thể add modality embeddings hoặc rely on positional/bố cục (layout / 레이아웃) conventions.

## Positional cấu trúc (structure / 구조)

Văn bản (text / 텍스트) 1D; ảnh (image / 이미지) 2D; video 3D (time × height × width); audio time-frequency.

Flattening thành 1D tokens cần encode original hình học (geometry / 기하학)/thời gian (time / 시간). Relative position biases hoặc factorized positional embeddings preserve cấu trúc (structure / 구조).

## Cross-Modal Attention ma trận (matrix / 행렬)

Nếu văn bản (text / 텍스트) length `T`, visual tokens `V`, full unified self-attention chi phí (cost / 비용) gần:

\[
O((T+V)^2)
\]

High-resolution vision/video làm `V` dominate. Resampling/compression trọng yếu (critical / 중요).

## Perceiver / Resampler

Introduce fixed set latent queries `L` attend huge modality chuỗi (sequence / 시퀀스):

\[
L\ll V
\]

Chi phí (cost / 비용) of cross-attention ~`O(LV)` then downstream operates on `L` latents.

This is thông tin (information / 정보) bottleneck; choosing number latent queries trades detail vs compute.

## Q-Former mẫu (pattern / 패턴)

Learnable truy vấn (query / 쿼리) tokens attend frozen visual encoder outputs and produce compact visual biểu diễn (representation / 표현) for ngôn ngữ (language / 언어) mô hình (model / 모델).

Useful when connecting frozen pretrained components.

## Modality Adapters

Instead full joint pretraining, use small adapters/projectors to cầu nối (bridge / 브리지) encoders to dùng chung (shared / 공유) backbone. Parameter-efficient but alignment sức chứa (capacity / 용량) limited.

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

Multi-objective huấn luyện (training / 학습) balances ngữ nghĩa (semantics / 의미론) and detailed grounding.

## Nhân quả (causal / 인과적) Masking Across Modalities

For generative mô hình (model / 모델), attention mask decides which tokens can see which.

Ảnh (image / 이미지) tokens may be fully visible ngữ cảnh (context / 맥락); văn bản (text / 텍스트) decoder nhân quả (causal / 인과적). In unified autoregressive các mô hình (models / 모델들), modality thứ tự (ordering / 순서)/masking controls generation direction.

## Generating Images/Audio as Tokens

If ảnh (image / 이미지)/audio converted to discrete codec tokens, Transformer can mô hình (model / 모델) them autoregressively along with văn bản (text / 텍스트).

Challenges:

- much higher đơn vị từ (token / 토큰) tỷ lệ (rate / 비율);
- lỗi (error / 오류) accumulation;
- modality-specific perceptual mất mát (loss / 손실);
- long sequences.

Diffusion/luồng (flow / 흐름) các mô hình (models / 모델들) often more efficient for high-dimensional continuous generation.

## Mixture of Experts

Multimodal MoE can tuyến (route / 경로) tokens to specialized experts while sharing backbone. Routing may be modality-aware or learned dynamically.

This increases sức chứa (capacity / 용량) without dense compute proportional to all parameters.

## Modality Dropout

During huấn luyện (training / 학습) randomly remove modalities so mô hình (model / 모델) remains robust if đầu vào (input / 입력) incomplete. Otherwise hệ thống (system / 시스템) may overdepend on easiest modality.

## Cross-Modal Shortcut học tập (learning / 학습)

If captions leak label directly, mô hình (model / 모델) may ignore ảnh (image / 이미지). If visual cue strongly predicts answer, it may ignore văn bản (text / 텍스트) instruction. huấn luyện (training / 학습)/evaluation should include counterfactual cases requiring both modalities.

## Synchronization

Audio-video transformer needs aligned timestamps. Relative timing can indicate lip movements, events, speaker turns.

If streams unsynchronized, mô hình (model / 모델) may learn spurious associations.

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
- bộ nhớ (memory / 메모리) modules;
- streaming attention.

## Streaming Multimodal các mô hình (models / 모델들)

Real-time assistant receives partial audio/video over thời gian (time / 시간). Need incremental trạng thái (state / 상태)/KV bộ nhớ đệm (cache / 캐시) and chính sách (policy / 정책) for when to respond vs wait for more bằng chứng (evidence / 증거).

This resembles partially observable hệ tác nhân (agent system / 에이전트 시스템).

## Multimodal Generation

One hệ thống (system / 시스템) can accept văn bản (text / 텍스트)/ảnh (image / 이미지)/audio and đầu ra (output / 출력) multiple modalities. kiến trúc (architecture / 아키텍처) may use dùng chung (shared / 공유) ngữ nghĩa (semantic / 의미적) backbone + modality-specific decoders.

Dùng chung (shared / 공유) biểu diễn (representation / 표현) should preserve intent while decoder handles waveform/điểm ảnh (pixel / 픽셀) generation details.

## Evaluation

Kiểm thử (test / 테스트) modality-specific and cross-modal capabilities separately:

```text
vision only
audio only
text only
vision+text required
audio+vision conflict
missing modality
adversarial visual text
```

A mô hình (model / 모델) scoring high on mixed benchmark may rely primarily one modality.

## Mô hình tư duy (mental model / 사고 모델)

> **Multimodal Transformer is an information-routing hệ thống (system / 시스템): encoders create tokens, attention decides what thông tin (information / 정보) crosses modality boundaries, and compression/masking determines what can be preserved.**

## Dùng chung (common / 공통) Misconceptions

### “Unified mô hình (model / 모델) means unified understanding automatically”

Dùng chung (shared / 공유) parameters/tokens do not guarantee fine-grained cross-modal grounding.

### “More visual/audio tokens always improve chất lượng (quality / 품질)”

Compute/noise increase and mô hình (model / 모델) may not effectively use them.

### “Cross-attention explains exactly what mô hình (model / 모델) used”

Attention weights are tương tác (interaction / 상호작용) signals, not complete nhân quả (causal / 인과적) explanations.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Multimodal Transformers extend [Transformer](../06_deep_learning_architectures/05_transformer.md) across heterogeneous đơn vị từ (token / 토큰) spaces and form backbone for multimodal agents.

Xem tiếp: [Multimodal Agents](./06_multimodal_agents.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 audio and speech representation](./00_audio_and_speech_representation.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
