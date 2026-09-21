# Multimodal Representation

**Multimodal AI (멀티모달 AI)** xử lý và liên kết nhiều modality như text, image, audio, video và sensor data. Thách thức không chỉ là nhận nhiều loại input; model phải học **representation tương thích** để xác định information nào tương ứng, bổ sung hoặc mâu thuẫn giữa các modality.

```text
text token
image patch
audio frame
video frame
sensor value
      ↓
modality encoder
      ↓
aligned / fused representation
      ↓
reasoning / generation / action
```

## Vì sao Multimodal khó?

Mỗi modality có structure khác nhau:

- text: discrete sequence, semantic density cao;
- image: spatial grid hai chiều;
- audio: time–frequency signal;
- video: space + time;
- sensor: continuous hoặc irregular stream.

Sampling rate giữa các modality cũng khác rất lớn. Một câu kéo dài 5 giây có thể chỉ có vài chục text token, nhưng audio chứa hàng chục nghìn sample và video có hàng trăm frame.

Model vì vậy phải giải cả bài toán representation, synchronization và scale mismatch.

## Alignment

**Alignment** hỏi phần nào của modality A tương ứng với phần nào của modality B.

Ví dụ:

```text
caption ↔ toàn image
word ↔ image region
phoneme ↔ audio frame
subtitle ↔ video segment
gesture ↔ spoken phrase
```

Alignment có thể coarse ở mức toàn sample hoặc fine-grained ở mức token, region hay timestamp.

## Shared Embedding Space

Contrastive training có thể đưa paired modality tới gần nhau:

\[
sim(f_{img}(x),f_{text}(y))\uparrow
\]

Matched image-caption pair được đẩy gần, mismatched pair bị tách xa.

Shared embedding space rất hữu ích cho retrieval và zero-shot transfer, nhưng một global vector có thể làm mất fine spatial alignment hoặc temporal detail.

## Modality-Specific Encoder

Một architecture phổ biến:

```text
vision encoder → visual token
speech encoder → audio token
text tokenizer / embedding → text token
```

Sau đó projector hoặc fusion layer map các representation về hidden dimension tương thích.

Việc giữ encoder riêng giúp mỗi modality tiếp tục tận dụng inductive bias phù hợp với dữ liệu của mình.

## Early, Intermediate và Late Fusion

**Early fusion** trộn raw hoặc low-level feature rất sớm. Interaction mạnh nhưng khó vì distribution và scale giữa modality khác nhau.

**Intermediate fusion** encode từng modality trước rồi dùng cross-attention hoặc joint layer để tương tác. Đây là lựa chọn phổ biến trong modern multimodal model.

**Late fusion** kết hợp final score hoặc embedding. Cách này đơn giản và robust hơn nhưng fine-grained interaction bị hạn chế.

## Cross-Attention

Một modality có thể query modality khác:

\[
Attention(Q_{text},K_{vision},V_{vision})
\]

Text token có thể attend visual patch có liên quan. Chiều ngược lại cũng có thể thực hiện.

Cross-attention giữ representation của các modality tương đối tách biệt nhưng vẫn cho phép exchange information.

## Unified Token Space

Một hướng khác là biến mọi modality thành token rồi xử lý bằng một Transformer chung:

```text
[image token][audio token][text token]
```

Unified architecture giúp scaling và interface đơn giản hơn, nhưng token count, positional structure và statistic của từng modality vẫn phải được xử lý cẩn thận.

## Modality Projector

Vision encoder có hidden dimension `D_v`, trong khi LLM có dimension `D_l`.

Một projector có thể dùng linear mapping:

\[
h_{llm}=Wh_v+b
\]

hoặc MLP nhỏ để chuyển visual representation vào interface của LLM.

Projector đơn giản vẫn có thể hoạt động tốt nếu pretrained encoder hai phía đã đủ mạnh.

## Modality Gap

Hai representation có cùng dimension không đồng nghĩa chúng nằm trong cùng semantic geometry.

Image feature và text feature có distribution khác nhau. Alignment training dạy hệ thống cách visual structure tương ứng với language concept.

## Paired Data

Multimodal training thường dựa trên paired data:

- image-caption;
- video-subtitle;
- speech-transcript;
- image + instruction + response.

Pair quality quyết định chất lượng alignment. Web caption thường chỉ mô tả salient object chứ không cover toàn bộ visual detail.

## Missing Modality

Real application có thể nhận nhiều combination:

```text
text only
image + text
image only
speech + text
```

Architecture cần xử lý trường hợp một modality vắng mặt. Nếu training luôn có complete pair, model có thể trở nên brittle khi deployment thiếu input.

## Complementary và Redundant Information

Hai modality có thể bổ sung nhau hoặc lặp lại cùng information.

Ví dụ audio và video đều chứa cue về speech. Image và metadata có thể cùng mô tả object.

Fusion tốt phải tận dụng complementarity nhưng tránh double-count noisy correlated evidence.

## Conflicting Modality

Image có thể cho thấy đèn đỏ trong khi text metadata ghi “green”.

Khi source mâu thuẫn, model cần signal về reliability, timestamp hoặc authority. Trong high-stakes application, conflict resolution nên có explicit application policy thay vì để model tự đoán hoàn toàn.

## Grounding

**Grounding (그라운딩 / neo nghĩa vào evidence)** là việc nối language claim với perceptual evidence cụ thể.

Ví dụ:

- phrase `red cup` ↔ box hoặc pixel region;
- word timestamp ↔ audio frame;
- action `person opens door` ↔ video segment.

Global semantic alignment chưa đủ để tạo precise grounding.

## Temporal Alignment

Audio và video cần synchronization chính xác.

Lệch vài trăm millisecond có thể làm lip-reading, speaker association hoặc event understanding giảm đáng kể.

Timestamp normalization, frame sampling và clock synchronization vì vậy là một phần của model quality chứ không chỉ data plumbing.

## Multimodal Token Budget

Một image hoặc video có thể tạo hàng nghìn token.

Trade-off:

```text
resolution cao hơn / nhiều frame hơn
→ detail nhiều hơn
→ context và compute lớn hơn
```

Adaptive token selection, patch merging và compression trở nên quan trọng trong long-context multimodal system.

## Modality Compression

Perceiver hoặc resampler module có thể compress nhiều visual/audio token thành một latent set nhỏ hơn trước khi đưa vào LLM.

Compression phải giữ task-relevant information. Nếu quá mạnh, fine detail sẽ mất trước khi language model có cơ hội reasoning.

## Representation Bottleneck

Nếu projector nén cả image thành quá ít token, OCR, small object hoặc precise spatial relation có thể biến mất.

Một LLM lớn hơn không thể khôi phục information chưa bao giờ đi qua bottleneck.

Đây là nguyên tắc hệ thống quan trọng:

> Downstream intelligence không thể bù hoàn toàn cho upstream information loss.

## Pretraining Objective

Multimodal model có thể dùng nhiều objective:

- contrastive alignment;
- image-text matching;
- caption generation;
- masked multimodal modeling;
- next-token prediction conditioned on visual/audio token;
- instruction following.

Objective khác nhau tạo pressure học representation khác nhau, vì vậy capability downstream cũng khác.

## Multimodal Hallucination

Language prior có thể lấn át perceptual evidence và làm model nói tới object không tồn tại trong image hoặc event không có trong audio/video.

Evaluation cần tách:

```text
perception failure
vs
alignment failure
vs
reasoning / generation failure
```

Nếu không tách layer, việc sửa model rất dễ nhắm sai nguyên nhân.

## Mô hình tư duy

> **Multimodal representation là bài toán xây interface giữa nhiều measurement space khác nhau để information tương ứng có thể tương tác mà không làm mất structure riêng của từng modality.**

## Những nhầm lẫn thường gặp

### “Đưa image embedding vào LLM là đã có multimodal understanding hoàn chỉnh”

Không. Projector chỉ tạo interface. Grounding, detail và spatial capability còn phụ thuộc alignment data, tokenization và training objective.

### “Shared embedding nghĩa mọi modality có cùng semantic geometry hoàn hảo”

Không. Geometry chỉ aligned trong phạm vi objective và data đã train.

### “Thêm nhiều modality luôn cải thiện kết quả”

Không. Modality noisy, stale hoặc conflict có thể làm output tệ hơn.

## Liên kết kiến thức

Multimodal representation nối [Modern Visual Representation](../12_computer_vision/08_modern_visual_representation.md), speech encoder, Embedding và Attention.

Xem tiếp: [Vision-Language Model](./04_vision_language_models.md).