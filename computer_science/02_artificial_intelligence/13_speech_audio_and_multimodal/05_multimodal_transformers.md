# Multimodal Transformer

Transformer phù hợp với Multimodal AI vì attention cho phép token từ nhiều source tương tác trong cùng computation graph. Tuy nhiên **multimodal Transformer** không phải một architecture duy nhất; có nhiều pattern tùy cách encode, align và fuse các modality.

## Pattern 1: Separate Encoder + Late Fusion

```text
image → vision encoder → embedding
text  → text encoder   → embedding
→ similarity / classifier
```

CLIP-style dual encoder rất hiệu quả cho retrieval vì image và text embedding có thể được precompute độc lập.

Hạn chế là interaction thường coarse, chủ yếu ở mức global embedding.

## Pattern 2: Cross-Attention

Text có thể query visual key/value:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Vision encoder vẫn giữ modality-specific representation, còn cross-attention cho phép language representation lấy information từ visual token khi cần.

Nhiều cross-attention block có thể được stack để tăng interaction depth.

## Pattern 3: Unified Sequence

Tất cả modality được project về cùng hidden dimension rồi concatenate:

```text
[visual token][audio token][text token]
```

Một Transformer chung xử lý toàn sequence.

Architecture đơn giản về mặt interface, nhưng sequence length có thể tăng rất mạnh khi image hoặc video tạo nhiều token.

## Token-Type / Modality Encoding

Model cần biết token thuộc image, audio hay text.

Có thể dùng:

- modality embedding;
- token-type embedding;
- positional convention;
- learned delimiter hoặc special token.

Nếu modality identity không rõ, model phải tự suy ra từ distribution và có thể học interface kém ổn định hơn.

## Positional Structure

Các modality có geometry khác nhau:

```text
text  → 1D sequence
image → 2D spatial grid
video → time × height × width
audio → time hoặc time–frequency
```

Khi flatten thành token sequence 1D, model vẫn cần information về geometry gốc.

Relative position bias, 2D/3D positional embedding hoặc factorized positional encoding giúp preserve structure này.

## Chi phí Cross-Modal Attention

Nếu text length là `T` và visual token count là `V`, full unified self-attention có cost gần:

\[
O((T+V)^2)
\]

Với high-resolution image hoặc video, `V` thường dominate.

Do đó token compression, resampling hoặc sparse attention trở thành requirement quan trọng cho scalability.

## Perceiver / Resampler

Một fixed latent set `L` có thể attend vào visual sequence rất lớn:

\[
L\ll V
\]

Cross-attention có cost gần `O(LV)`, sau đó downstream model chỉ xử lý `L` latent.

Đây là một **information bottleneck**: latent count nhỏ giảm compute nhưng có thể làm mất fine detail.

## Q-Former Pattern

Q-Former sử dụng learnable query token để attend frozen visual encoder output rồi sinh compact visual representation cho language model.

Pattern này đặc biệt hữu ích khi muốn kết nối hai pretrained component mạnh mà không cần fine-tune toàn bộ stack.

## Modality Adapter

Thay vì joint pretraining toàn model, ta có thể dùng adapter hoặc projector nhỏ giữa modality encoder và shared backbone.

Cách này parameter-efficient và rẻ hơn, nhưng alignment capacity có thể bị giới hạn nếu adapter quá nhỏ so với domain gap.

## Joint Pretraining Objective

Multimodal Transformer có thể tối ưu đồng thời nhiều objective:

```text
contrastive alignment
image-text matching
caption generation
masked token / patch prediction
next-token prediction
grounding
instruction following
```

Objective mixture quyết định model ưu tiên broad semantic alignment hay fine-grained grounding.

## Causal Masking giữa các Modality

Trong generative model, attention mask xác định token nào có thể nhìn token nào.

Image token thường được dùng như fully visible context, trong khi text decoder vẫn causal.

Trong unified autoregressive model, thứ tự modality và mask policy quyết định generation direction và dependency structure.

## Sinh Image hoặc Audio dưới dạng Token

Nếu image/audio được encode thành discrete codec token, Transformer có thể model các modality đó autoregressively giống text.

Thách thức:

- token rate rất cao;
- sequence dài;
- error accumulation;
- perceptual quality không tương đương token-level accuracy;
- decoding latency.

Diffusion hoặc flow model thường hiệu quả hơn cho high-dimensional continuous generation trong nhiều use case.

## Mixture of Experts

Multimodal MoE có thể route token tới specialized expert trong khi vẫn chia sẻ backbone.

Router có thể học specialization theo modality hoặc theo semantic function.

Cách này tăng total capacity mà không bắt mọi token chạy qua toàn bộ parameter.

## Modality Dropout

Trong training, có thể ngẫu nhiên bỏ một modality để model học cách hoạt động khi input không đầy đủ.

Nếu training luôn có đủ modality, model có thể overdepend vào modality dễ nhất và fail khi deployment thiếu source đó.

## Cross-Modal Shortcut Learning

Nếu caption trực tiếp tiết lộ label, model có thể bỏ qua image.

Ngược lại nếu visual cue quá mạnh, model có thể bỏ qua text instruction.

Eval nên có counterfactual case buộc model thật sự sử dụng cả hai modality để phát hiện shortcut learning.

## Synchronization

Audio-video model cần timestamp aligned.

Lip movement, speaker turn hoặc event relation đều phụ thuộc relative timing.

Nếu stream lệch thời gian, model có thể học association sai dù từng modality riêng lẻ vẫn chính xác.

## Long Video

Video token count tăng theo:

\[
N = frames \times patches/frame
\]

Để xử lý video dài có thể dùng:

- sparse frame sampling;
- temporal pooling;
- hierarchical summary;
- event-based retrieval;
- memory module;
- streaming attention.

Không có chiến lược sampling nào tốt cho mọi task: event ngắn cần dense temporal coverage, còn scene understanding dài hạn cần broader context.

## Streaming Multimodal Model

Real-time assistant nhận audio/video từng phần theo thời gian.

System cần incremental state, KV cache và policy quyết định:

```text
đã đủ evidence để trả lời chưa?
chờ thêm input?
gọi tool?
cập nhật hypothesis?
```

Điều này gần với partially observable agent system hơn là một static classification task.

## Multimodal Generation

Một system có thể nhận text/image/audio và output nhiều modality.

Architecture thường tách:

```text
shared semantic backbone
+
modality-specific decoder
```

Shared representation giữ intent và semantic relation, còn decoder riêng xử lý chi tiết waveform hoặc pixel generation.

## Evaluation

Cần tách capability theo modality và cross-modal dependency:

```text
vision only
audio only
text only
vision + text bắt buộc
audio + vision conflict
missing modality
adversarial visual text
```

Nếu chỉ nhìn mixed benchmark score, model có thể đạt cao bằng cách dựa chủ yếu vào một modality dễ nhất.

## Mô hình tư duy

> **Multimodal Transformer là một hệ thống định tuyến information: encoder tạo token, attention quyết định information nào đi qua modality boundary, còn compression và masking quyết định information nào được giữ lại.**

## Những nhầm lẫn thường gặp

### “Unified model nghĩa là unified understanding tự động xuất hiện”

Không. Shared parameter hoặc shared token space không bảo đảm fine-grained grounding.

### “Càng nhiều visual/audio token càng tốt”

Không. Compute và noise tăng, trong khi model có thể không sử dụng hiệu quả toàn bộ token.

### “Cross-attention map cho biết chính xác model đã dùng gì”

Không. Attention weight là interaction signal chứ không phải causal explanation hoàn chỉnh.

## Liên kết kiến thức

Multimodal Transformer mở rộng [Transformer](../06_deep_learning_architectures/05_transformer.md) sang heterogeneous token space và là backbone quan trọng cho multimodal agent.

Xem tiếp: [Multimodal Agent](./06_multimodal_agents.md).