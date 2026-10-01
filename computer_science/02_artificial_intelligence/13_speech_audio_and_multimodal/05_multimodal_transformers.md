# Multimodal Transformers

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Multimodal Transformers**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Mẫu (pattern / 패턴) 1: Separate Encoders + Late Fusion** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Mẫu (pattern / 패턴) 2: Cross-Attention** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Transformer kiến trúc (architecture / 아키텍처) phù hợp multimodal AI vì attention cho phép tokens từ nhiều sources tương tác trong cùng computation đồ thị (graph / 그래프). Tuy nhiên “multimodal Transformer” không phải một kiến trúc (architecture / 아키텍처) duy nhất; có nhiều patterns tùy cách encode và fuse modalities.

## Mẫu (pattern / 패턴) 1: Separate Encoders + Late Fusion

Phần này chuyển khái niệm Computer Science thành cấu trúc, ví dụ hoặc quy trình có thể kiểm tra. Hãy xác định câu hỏi mà mục trả lời rồi nối kết luận với phần kế tiếp.

```text
image → vision encoder → embedding
text → text encoder → embedding
→ similarity / classifier
```

CLIP-like dual encoder rất efficient cho retrieval vì ảnh (image / 이미지)/văn bản (text / 텍스트) embeddings có thể precompute independently.

Nhược điểm: tương tác (interaction / 상호작용) coarse, thường toàn cục (global / 전역) embedding-level.

> **Chuyển mạch:** Trong **Multimodal Transformers**, **Mẫu (pattern / 패턴) 2: Cross-Attention** tiếp nhận điểm tựa từ **Mẫu (pattern / 패턴) 1: Separate Encoders + Late Fusion** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mẫu (pattern / 패턴) 3: Unified chuỗi (sequence / 시퀀스)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) 2: Cross-Attention

Văn bản (text / 텍스트) queries visual keys/values:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Visual encoder giữ modality-specific biểu diễn (representation / 표현); cross-attention cho conditional lập luận (reasoning / 추론).

Có thể ngăn xếp (stack / 스택) repeated cross-attention blocks.

> **Chuyển mạch:** Ở chặng này của **Multimodal Transformers**, **Mẫu (pattern / 패턴) 2: Cross-Attention** xác định đầu vào; **Mẫu (pattern / 패턴) 3: Unified chuỗi (sequence / 시퀀스)** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Token-Type / Modality Encoding** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mẫu (pattern / 패턴) 3: Unified chuỗi (sequence / 시퀀스)

Dự án (project / 프로젝트) all modalities thành same hidden dimension rồi concatenate:

```text
[visual tokens][audio tokens][text tokens]
```

Một Transformer xử lý chung. Simpler conceptual kiến trúc (architecture / 아키텍처), nhưng chuỗi (sequence / 시퀀스) length lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal Transformers**, **Mẫu (pattern / 패턴) 3: Unified chuỗi (sequence / 시퀀스)** xác định đầu vào; **Token-Type / Modality Encoding** giải thích bước vận hành tạo ra kết quả kế tiếp. Từ đây, **Positional cấu trúc (structure / 구조)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Token-Type / Modality Encoding

Mô hình (model / 모델) cần biết đơn vị từ (token / 토큰) đến từ ảnh (image / 이미지)/audio/văn bản (text / 텍스트). Có thể add modality embeddings hoặc rely on positional/bố cục (layout / 레이아웃) conventions.

> **Chuyển mạch:** Trong **Multimodal Transformers**, **Positional cấu trúc (structure / 구조)** tiếp nhận điểm tựa từ **Token-Type / Modality Encoding** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cross-Modal Attention ma trận (matrix / 행렬)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Positional cấu trúc (structure / 구조)

Văn bản (text / 텍스트) 1D; ảnh (image / 이미지) 2D; video 3D (time × height × width); audio time-frequency.

Flattening thành 1D tokens cần encode original hình học (geometry / 기하학)/thời gian (time / 시간). Relative position biases hoặc factorized positional embeddings preserve cấu trúc (structure / 구조).

> **Chuyển mạch:** Ở chặng này của **Multimodal Transformers**, **Cross-Modal Attention ma trận (matrix / 행렬)** tiếp nhận điểm tựa từ **Positional cấu trúc (structure / 구조)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Perceiver / Resampler** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cross-Modal Attention ma trận (matrix / 행렬)

Nếu văn bản (text / 텍스트) length `T`, visual tokens `V`, full unified self-attention chi phí (cost / 비용) gần:

\[
O((T+V)^2)
\]

High-resolution vision/video làm `V` dominate. Resampling/compression trọng yếu (critical / 중요).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal Transformers**, **Perceiver / Resampler** tiếp nhận điểm tựa từ **Cross-Modal Attention ma trận (matrix / 행렬)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Q-Former mẫu (pattern / 패턴)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Perceiver / Resampler

Introduce fixed set latent queries `L` attend huge modality chuỗi (sequence / 시퀀스):

\[
L\ll V
\]

Chi phí (cost / 비용) of cross-attention ~`O(LV)` then downstream operates on `L` latents.

This is thông tin (information / 정보) bottleneck; choosing number latent queries trades detail vs compute.

> **Chuyển mạch:** Trong **Multimodal Transformers**, **Q-Former mẫu (pattern / 패턴)** tiếp nhận điểm tựa từ **Perceiver / Resampler** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modality Adapters** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Q-Former mẫu (pattern / 패턴)

Learnable truy vấn (query / 쿼리) tokens attend frozen visual encoder outputs and produce compact visual biểu diễn (representation / 표현) for ngôn ngữ (language / 언어) mô hình (model / 모델).

Useful when connecting frozen pretrained components.

> **Chuyển mạch:** Ở chặng này của **Multimodal Transformers**, **Modality Adapters** tiếp nhận điểm tựa từ **Q-Former mẫu (pattern / 패턴)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Joint Pretraining Objectives** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modality Adapters

Instead full joint pretraining, use small adapters/projectors to cầu nối (bridge / 브리지) encoders to dùng chung (shared / 공유) backbone. Parameter-efficient but alignment sức chứa (capacity / 용량) limited.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal Transformers**, **Joint Pretraining Objectives** tiếp nhận điểm tựa từ **Modality Adapters** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Nhân quả (causal / 인과적) Masking Across Modalities** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Trong **Multimodal Transformers**, **Nhân quả (causal / 인과적) Masking Across Modalities** tiếp nhận điểm tựa từ **Joint Pretraining Objectives** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Generating Images/Audio as Tokens** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Nhân quả (causal / 인과적) Masking Across Modalities

For generative mô hình (model / 모델), attention mask decides which tokens can see which.

Ảnh (image / 이미지) tokens may be fully visible ngữ cảnh (context / 맥락); văn bản (text / 텍스트) decoder nhân quả (causal / 인과적). In unified autoregressive các mô hình (models / 모델들), modality thứ tự (ordering / 순서)/masking controls generation direction.

> **Chuyển mạch:** Ở chặng này của **Multimodal Transformers**, **Generating Images/Audio as Tokens** tiếp nhận điểm tựa từ **Nhân quả (causal / 인과적) Masking Across Modalities** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mixture of Experts** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Generating Images/Audio as Tokens

If ảnh (image / 이미지)/audio converted to discrete codec tokens, Transformer can mô hình (model / 모델) them autoregressively along with văn bản (text / 텍스트).

Challenges:

- much higher đơn vị từ (token / 토큰) tỷ lệ (rate / 비율);
- lỗi (error / 오류) accumulation;
- modality-specific perceptual mất mát (loss / 손실);
- long sequences.

Diffusion/luồng (flow / 흐름) các mô hình (models / 모델들) often more efficient for high-dimensional continuous generation.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal Transformers**, **Mixture of Experts** tiếp nhận điểm tựa từ **Generating Images/Audio as Tokens** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Modality Dropout** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mixture of Experts

Multimodal MoE can tuyến (route / 경로) tokens to specialized experts while sharing backbone. Routing may be modality-aware or learned dynamically.

This increases sức chứa (capacity / 용량) without dense compute proportional to all parameters.

> **Chuyển mạch:** Trong **Multimodal Transformers**, **Modality Dropout** tiếp nhận điểm tựa từ **Mixture of Experts** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Cross-Modal Shortcut học tập (learning / 학습)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Modality Dropout

During huấn luyện (training / 학습) randomly remove modalities so mô hình (model / 모델) remains robust if đầu vào (input / 입력) incomplete. Otherwise hệ thống (system / 시스템) may overdepend on easiest modality.

> **Chuyển mạch:** Ở chặng này của **Multimodal Transformers**, **Cross-Modal Shortcut học tập (learning / 학습)** tiếp nhận điểm tựa từ **Modality Dropout** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Synchronization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Cross-Modal Shortcut học tập (learning / 학습)

If captions leak label directly, mô hình (model / 모델) may ignore ảnh (image / 이미지). If visual cue strongly predicts answer, it may ignore văn bản (text / 텍스트) instruction. huấn luyện (training / 학습)/evaluation should include counterfactual cases requiring both modalities.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal Transformers**, **Synchronization** tiếp nhận điểm tựa từ **Cross-Modal Shortcut học tập (learning / 학습)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Long Video** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Synchronization

Audio-video transformer needs aligned timestamps. Relative timing can indicate lip movements, events, speaker turns.

If streams unsynchronized, mô hình (model / 모델) may learn spurious associations.

> **Chuyển mạch:** Trong **Multimodal Transformers**, **Long Video** tiếp nhận điểm tựa từ **Synchronization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Streaming Multimodal các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Multimodal Transformers**, **Streaming Multimodal các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Long Video** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Multimodal Generation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Streaming Multimodal các mô hình (models / 모델들)

Real-time assistant receives partial audio/video over thời gian (time / 시간). Need incremental trạng thái (state / 상태)/KV bộ nhớ đệm (cache / 캐시) and chính sách (policy / 정책) for when to respond vs wait for more bằng chứng (evidence / 증거).

This resembles partially observable hệ tác nhân (agent system / 에이전트 시스템).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal Transformers**, **Multimodal Generation** tiếp nhận điểm tựa từ **Streaming Multimodal các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Evaluation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Multimodal Generation

One hệ thống (system / 시스템) can accept văn bản (text / 텍스트)/ảnh (image / 이미지)/audio and đầu ra (output / 출력) multiple modalities. kiến trúc (architecture / 아키텍처) may use dùng chung (shared / 공유) ngữ nghĩa (semantic / 의미적) backbone + modality-specific decoders.

Dùng chung (shared / 공유) biểu diễn (representation / 표현) should preserve intent while decoder handles waveform/điểm ảnh (pixel / 픽셀) generation details.

> **Chuyển mạch:** Trong **Multimodal Transformers**, **Evaluation** tiếp nhận điểm tựa từ **Multimodal Generation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Multimodal Transformers**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Evaluation** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **Multimodal Transformer is an information-routing hệ thống (system / 시스템): encoders create tokens, attention decides what thông tin (information / 정보) crosses modality boundaries, and compression/masking determines what can be preserved.**

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Multimodal Transformers**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Unified mô hình (model / 모델) means unified understanding automatically”

Dùng chung (shared / 공유) parameters/tokens do not guarantee fine-grained cross-modal grounding.

### “More visual/audio tokens always improve chất lượng (quality / 품질)”

Compute/noise increase and mô hình (model / 모델) may not effectively use them.

### “Cross-attention explains exactly what mô hình (model / 모델) used”

Attention weights are tương tác (interaction / 상호작용) signals, not complete nhân quả (causal / 인과적) explanations.

> **Chuyển mạch:** Trong **Multimodal Transformers**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Multimodal Transformers extend [Transformer](../06_deep_learning_architectures/05_transformer.md) across heterogeneous đơn vị từ (token / 토큰) spaces and form backbone for multimodal agents.

Xem tiếp: [Multimodal Agents](./06_multimodal_agents.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
