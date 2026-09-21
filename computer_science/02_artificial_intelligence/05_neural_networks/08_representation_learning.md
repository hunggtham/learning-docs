# Representation Learning: học cách biểu diễn dữ liệu

**Học biểu diễn (Representation Learning / 표현 학습)** là một trong những ý tưởng trung tâm nhất của Deep Learning. Thay vì chỉ học ánh xạ trực tiếp `input → output`, network học các không gian trung gian nơi những yếu tố liên quan tới task được sắp xếp theo một hình học dễ xử lý hơn.

Một representation tốt không có nghĩa “vector nhìn đẹp”. Nó phải làm computation phía sau đơn giản hơn, bền vững hơn hoặc dễ chuyển sang task mới hơn.

## Representation là gì?

Đối tượng thô có thể rất phức tạp:

- ảnh: pixel;
- văn bản: chuỗi token;
- âm thanh: waveform;
- người dùng: lịch sử tương tác;
- phân tử: graph.

Encoder tạo vector hoặc tensor:

\[
z=f_\theta(x)
\]

`z` là **biểu diễn học được (learned representation)**.

Downstream head:

\[
\hat y=g_\phi(z)
\]

Nếu `z` tổ chức thông tin liên quan tới task tốt, `g` có thể rất đơn giản.

## Linear Probe như một phép kiểm tra

Nếu đóng băng representation `z` rồi một linear classifier vẫn đạt performance cao, ta nói thông tin về target đã trở nên **truy cập tuyến tính (linearly accessible)**.

Linear probe không đo toàn bộ sự phong phú ngữ nghĩa, nhưng là một diagnostic hữu ích để kiểm tra feature extractor đã “gỡ rối” task tới mức nào.

## Biểu diễn phân tán

One-hot symbol đặt mỗi category trên một trục trực giao và không biểu diễn similarity.

Embedding dày đặc được học:

\[
z\in R^d
\]

có thể mã hóa nhiều yếu tố phân tán trên các dimension hoặc direction.

Quan hệ similarity xuất hiện do training objective, không phải vì bản thân định dạng vector tự mang ý nghĩa.

## Hình học của Embedding

Nếu contrastive training kéo các cặp liên quan lại gần và đẩy các cặp không liên quan ra xa:

```text
đối tượng liên quan ngữ nghĩa → vùng / hướng gần nhau
đối tượng không liên quan      → xa nhau hơn
```

thì cosine similarity hoặc dot-product retrieval trở nên có ý nghĩa.

Nhưng geometry phụ thuộc objective. Embedding tốt cho semantic search chưa chắc tốt cho sentiment clustering hay recommendation.

## Supervised Representation Learning

Trong classifier neural, hidden representation được học vì task loss cuối cùng backpropagate xuyên qua encoder.

Các hidden layer giữ lại thông tin hữu ích cho target và có thể loại bỏ variation không liên quan.

Nếu target quá hẹp, representation cũng có thể trở nên quá chuyên biệt và transfer kém.

## Self-Supervised Representation Learning

**Học tự giám sát (self-supervised learning)** tạo tín hiệu huấn luyện từ chính raw data.

Ví dụ gồm dự đoán token tiếp theo, khôi phục token hoặc patch bị che, đối chiếu hai view của cùng ảnh, dự đoán đoạn tương lai hoặc tái tạo input bị làm nhiễu.

Mục tiêu là tận dụng lượng dữ liệu chưa gán nhãn rất lớn để học cấu trúc có thể tái sử dụng.

Foundation model hiện đại chủ yếu dựa trên self-supervised pretraining rồi mới thích nghi với downstream task.

## Contrastive Learning

Với cặp positive `(x,x⁺)` và negative `x⁻`, objective khuyến khích similarity của cặp positive cao hơn negative.

Một dạng InfoNCE:

\[
L=-\log
\frac{\exp(sim(z,z^+)/\tau)}
{\sum_j\exp(sim(z,z_j)/\tau)}
\]

`τ` là temperature.

Cách chọn positive pair chính là định nghĩa invariance.

Ví dụ hai crop của cùng ảnh được xem là cùng semantic object. Nếu augmentation làm mất thông tin quan trọng cho task, representation cũng sẽ học sai invariance.

## Metric Learning

Triplet loss:

\[
L=\max(0,d(a,p)-d(a,n)+m)
\]

ép anchor–positive gần nhau hơn anchor–negative ít nhất một margin `m`.

**Hard-negative mining** rất quan trọng: negative quá dễ gần như không tạo gradient; negative giả lại có thể phá geometry ngữ nghĩa.

## Representation từ Autoencoder

Encoder–decoder:

\[
x\to z\to\hat x
\]

Reconstruction objective buộc `z` giữ thông tin cần để tái tạo input.

Tuy nhiên tái tạo pixel hoàn hảo có thể ưu tiên chi tiết cấp thấp hơn semantics.

Bottleneck, denoising hoặc variational constraint thay đổi loại factor mà latent representation phải giữ.

Objective quyết định “thông tin quan trọng” thực sự nghĩa là gì.

## Bottleneck và Compression

Một `z` có số chiều thấp hơn buộc hệ thống nén thông tin.

Theo trực giác Information Bottleneck, representation tốt nên giữ thông tin hữu ích cho target trong khi loại bỏ variation không liên quan.

Lý thuyết hình thức nghiên cứu sự đánh đổi giữa:

\[
I(X;Z)
\]

và:

\[
I(Z;Y)
\]

Nhưng Neural Network thực tế không phải lúc nào cũng tối ưu trực tiếp đúng hai đại lượng này.

Trực giác vẫn hữu ích: representation tốt lọc nuisance nhưng giữ predictive structure.

## Invariance và Equivariance

Representation **bất biến (invariant)** khi phép biến đổi đầu vào không nên đổi representation hoặc output.

Ví dụ classification ảnh thường mong muốn mức bất biến nhất định với dịch chuyển.

Representation **đồng biến (equivariant)** khi output thay đổi theo một quy luật tương ứng với transformation của input.

Segmentation hoặc pose estimation cần giữ thông tin vị trí, nên khi ảnh dịch chuyển, output cũng phải dịch chuyển theo.

Architecture và augmentation chính là nơi mã hóa những giả định này.

## Transfer Learning

Encoder pretrained học representation rộng, sau đó task mới có thể dùng bằng các cách:

- đóng băng feature rồi train head mới;
- fine-tuning một phần;
- fine-tuning toàn bộ;
- adapter hoặc LoRA.

Transfer hiệu quả khi representation từ pretraining chứa các factor liên quan tới downstream task.

Nếu source và target lệch quá nhiều, có thể xảy ra **negative transfer**.

## Representation Collapse

Một số self-supervised objective có nguy cơ ánh xạ mọi input vào gần cùng một vector hằng.

Khi đó similarity trở nên vô nghĩa vì representation không còn giữ thông tin.

Các phương pháp khác nhau ngăn collapse bằng negative sample, stop-gradient bất đối xứng, predictor riêng, regularization variance/covariance hoặc teacher–student dynamics.

Hiểu collapse giúp thấy vì sao thiết kế self-supervised objective rất quan trọng.

## Disentanglement

Representation “disentangled” lý tưởng cố tách những yếu tố sinh dữ liệu như rotation, lighting hay identity thành các factor tương đối độc lập.

Trong thực tế, disentanglement khó và thường không thể xác định duy nhất nếu thiếu inductive bias hoặc supervision bổ sung.

Không nên giả định mỗi latent dimension tự nhiên tương ứng với một khái niệm con người.

## Biểu diễn thưa và biểu diễn dày đặc

**Sparse representation** chỉ kích hoạt một số ít thành phần; **dense representation** dùng nhiều dimension cùng lúc.

Sparse representation có thể thuận lợi hơn cho interpretability hoặc retrieval kiểu lexical. Dense embedding gọn và phù hợp với gradient-based learning.

Modern retrieval thường kết hợp sparse lexical signal với dense semantic embedding vì hai loại representation bổ sung nhau.

## Representation Drift

Khi encoder được retrain, geometry của embedding thay đổi.

Các vector cũ trong vector database có thể không còn tương thích với query embedding từ model mới.

Hệ quả production:

```text
đổi phiên bản embedding model
→ tạo lại embedding cho corpus
→ rebuild / revalidate index
```

Versioning representation vì vậy là vấn đề LLMOps và Data Engineering, không chỉ lý thuyết mô hình.

## Probe và Interpretability

Probe classifier có thể cho thấy một loại thông tin có thể được giải mã từ representation.

Nhưng probe accuracy cao **không** chứng minh base model thực sự dùng thông tin đó để tạo prediction.

Muốn đưa ra kết luận mạnh hơn cần intervention hoặc ablation.

Phải phân biệt **khả năng giải mã (decodability)** với **mức sử dụng nhân quả (causal use)**.

## Preview Hidden State của LLM

Transformer biến token embedding qua nhiều layer thành contextual representation.

Cùng một token có thể có hidden vector khác nhau tùy context.

Hidden state cuối được đưa qua output projection và softmax để dự đoán token tiếp theo. Các layer trung gian có thể mã hóa cấu trúc cú pháp, ngữ nghĩa, factual pattern và task feature theo dạng phân tán.

Chương này vì vậy chuẩn bị trực tiếp cho các phần Embedding, Transformer và LLM.

## Mô hình tư duy

> Representation Learning là quá trình học một hệ tọa độ nơi những mối quan hệ quan trọng đối với objective trở nên dễ tính toán hơn.

Raw space không nhất thiết có geometry hữu ích; training tái tổ chức không gian đó.

## Các hiểu lầm thường gặp

### “Embedding gần nhau nghĩa hai đối tượng giống nhau tuyệt đối”

Không. Chúng chỉ gần nhau theo geometry được tạo bởi model, data và objective cụ thể.

### “Latent dimension 42 chắc chắn đại diện một concept”

Không. Thông tin thường phân tán trên nhiều dimension hoặc subspace.

### “Self-supervised không có label nên objective trung lập”

Không. Pretext task, augmentation và sampling chính là inductive bias rất mạnh.

### “Nếu thông tin giải mã được từ hidden state thì model đang dùng nó”

Không. Decodability không chứng minh causal reliance.

## Liên kết kiến thức

Representation Learning nối [Giảm chiều](../04_machine_learning/12_dimensionality_reduction.md), [Lý thuyết thông tin](../01_mathematical_foundations/05_information_theory.md), [Regularization](./07_regularization.md) và sau này [Embedding](../08_large_language_models/02_embeddings_and_semantic_space.md), [RAG](../09_retrieval_and_rag/05_rag_fundamentals.md).