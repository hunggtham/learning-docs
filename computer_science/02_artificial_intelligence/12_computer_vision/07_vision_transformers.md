# Vision Transformers

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Vision transformers**. Route đi từ patch tokenization → positional information → self-attention over patches → pretraining/augmentation → transfer and resolution limits, để ViT nối hình ảnh với pipeline biểu diễn kiểu transformer.

**Vision Transformer (ViT / 비전 트랜스포머)** áp dụng Transformer lên images bằng cách biến ảnh (image / 이미지) thành chuỗi (sequence / 시퀀스) của patch tokens. Ý tưởng cốt lõi là thay inductive độ lệch (bias / 편향) convolution mạnh bằng self-attention có khả năng mô hình (model / 모델) interactions toàn cục.

## Patch Tokenization

Với ảnh (image / 이미지) `H×W×C`, chia thành patches `P×P`.

Số patches:

\[
N=\frac{HW}{P^2}
\]

Mỗi patch flatten thành véc-tơ (vector / 벡터) kích thước (size / 크기) `P^2C`, sau đó tuyến tính (linear / 선형) projection:

\[
z_i = x_i W_E + b
\]

thành embedding dimension `D`.

```text
image
→ patches
→ patch embeddings
→ positional information
→ Transformer encoder
→ task head
```

Patch tokenization tạo chuỗi đầu vào; để chuỗi vẫn phản ánh bố cục ảnh, ViT phải thêm thông tin vị trí trước khi attention xử lý các token.

## Vì sao cần Positional thông tin (information / 정보)?

Self-attention nguyên bản không biết patch nào ở top-left hay bottom-right nếu không encode position.

Positional embeddings thêm spatial thứ tự (order / 순서). Có thể learned absolute, relative hoặc 2D variants.

Vị trí giúp attention phân biệt các patch có nội dung giống nhau nhưng nằm ở nơi khác; `[CLS]` sau đó cung cấp một điểm gom thông tin cho classification.

## CLS đơn vị từ (token / 토큰)

Original ViT thêm learnable `[CLS]` đơn vị từ (token / 토큰) vào chuỗi (sequence / 시퀀스). Sau encoder, biểu diễn (representation / 표현) của đơn vị từ (token / 토큰) này dùng cho classification.

Alternatives dùng toàn cục (global / 전역) average pooling trên patch features.

Sau khi có token tổng hợp, self-attention mới quyết định mỗi patch trao đổi thông tin với các patch còn lại như thế nào.

## Self-Attention trong ảnh (image / 이미지)

Attention:

\[
A=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)
\]

cho mỗi patch aggregate thông tin (information / 정보) từ mọi patch khác.

Điểm mạnh: long-range interactions accessible ngay một tầng (layer / 계층), không cần ngăn xếp (stack / 스택) many cục bộ (local / 로컬) convs để receptive trường dữ liệu (field / 필드) lan rộng.

Đổi lại, attention toàn cục phải tính nhiều cặp token; chi phí này là giới hạn chính khi ảnh có độ phân giải cao.

## Độ phức tạp (complexity / 복잡도)

Attention bộ nhớ (memory / 메모리)/compute theo số tokens gần:

\[
O(N^2)
\]

Nếu patch kích thước (size / 크기) nhỏ hoặc high-resolution ảnh (image / 이미지), `N` tăng nhanh.

Ví dụ doubling both H and W → patches ~4× → attention ma trận (matrix / 행렬) ~16×.

Do đó high-resolution ViT cần hierarchical/windowed/sparse attention variants.

Giới hạn token giải thích vì sao ViT phải cân bằng giữa inductive bias của CNN và khả năng học quan hệ linh hoạt từ dữ liệu.

## CNN vs ViT Inductive độ lệch (bias / 편향)

CNN hard-code:

- locality;
- translation weight sharing;
- hierarchical spatial processing.

ViT hard-code ít hơn, cho mô hình (model / 모델) learn relations from dữ liệu (data / 데이터). Điều này từng khiến ViT cần large-scale pretraining hơn CNN, nhưng hiện đại (modern / 현대적) huấn luyện (training / 학습)/augmentation architectures thu hẹp gap.

Bias yếu hơn làm tăng nhu cầu về dữ liệu và regularization; quy mô pretraining là biến quyết định khả năng học cấu trúc hữu ích.

## Dữ liệu (data / 데이터) quy mô (scale / 규모)

Weaker inductive độ lệch (bias / 편향) means mô hình (model / 모델) may need more dữ liệu (data / 데이터)/regularization to discover useful cấu trúc (structure / 구조). Large pretraining giúp ViT shine.

Đây là example của general ML principle:

> stronger prior → potentially better mẫu (sample / 표본) efficiency; weaker prior → more flexibility if dữ liệu (data / 데이터)/compute abundant.

Để giảm chi phí attention mà vẫn giữ biểu diễn nhiều độ phân giải, các kiến trúc hierarchical chia quá trình xử lý thành nhiều stage.

## Hierarchical Vision Transformers

Các mô hình (models / 모델들) như Swin tiến trình (process / 프로세스) cục bộ (local / 로컬) windows và merge patches over stages:

```text
fine patches
→ local attention
→ patch merging
→ coarser feature hierarchy
```

Điều này recover multi-scale cấu trúc (structure / 구조) useful detection/segmentation và reduce quadratic chi phí (cost / 비용).

Windowed attention là cơ chế cụ thể để giới hạn các cặp tương tác trong mỗi stage; shifted windows giúp thông tin vẫn đi qua ranh giới cửa sổ.

## Windowed Attention

Attention chỉ trong cục bộ (local / 로컬) windows giảm độ phức tạp (complexity / 복잡도). Shifted windows allow cross-window communication across layers.

Sự đánh đổi (trade-off / 트레이드오프) gần CNN: locality introduced lại để gain efficiency.

Locality giúp tính toán hiệu quả, nhưng các mô hình hybrid cho phép kết hợp lợi thế đó với quan hệ toàn cục của transformer.

## Hybrid các mô hình (models / 모델들)

CNN stem + Transformer body hoặc convolution inside transformer khối (block / 블록) kết hợp cục bộ (local / 로컬) độ lệch (bias / 편향) và toàn cục (global / 전역) attention.

Hiện đại (modern / 현대적) vision architectures không còn nhị phân (binary / 이진) CNN vs Transformer; ideas mix widely.

Một hướng tận dụng backbone transformer là pretraining bằng cách che patch và yêu cầu mô hình khôi phục phần bị ẩn.

## Masked ảnh (image / 이미지) Modeling

ViT naturally supports masked-patch pretraining. Hide large fraction patches, train reconstruct pixels/features/latent targets.

This resembles masked ngôn ngữ (language / 언어) modeling nhưng ảnh (image / 이미지) patches have high redundancy, nên masking ratios/objectives khác NLP.

Masked modeling học từ tín hiệu tự tạo; distillation bổ sung tín hiệu từ một teacher để định hướng biểu diễn và cải thiện hiệu quả dữ liệu.

## Distillation

Teacher mô hình (model / 모델) can transfer lớp (class / 클래스)/biểu diễn (representation / 표현) signals to ViT, improving dữ liệu (data / 데이터) efficiency.

Các biểu diễn đã học có thể phục vụ cả detection, nơi transformer thay chuỗi anchor/NMS bằng dự đoán một tập object.

## Detection with Transformers

DETR uses CNN/ViT-like features + Transformer encoder-decoder + learned đối tượng (object / 객체) queries. Detection becomes set prediction rather than anchor/NMS chuỗi xử lý (pipeline / 파이프라인).

Với segmentation, các token cũng có thể được giải mã thành mask; bài toán này đòi hỏi giữ lại chi tiết ở nhiều độ phân giải.

## Segmentation with Transformers

Patch features can be decoded into masks. toàn cục (global / 전역) ngữ cảnh (context / 맥락) helps scene parsing; multi-scale/hierarchical features important ranh giới (boundary / 경계)/detail.

Khi đổi độ phân giải lúc fine-tune, positional embeddings phải được nội suy phù hợp để bố cục mới không phá vỡ biểu diễn đã học.

## Position Resolution Transfer

Fine-tuning at different ảnh (image / 이미지) resolution may require interpolate positional embeddings if using absolute positions.

This is an hiện thực (implementation / 구현) consequence of learned positional bảng (table / 테이블).

Attention map có thể giúp quan sát tương tác giữa patch, nhưng việc quan sát đó không tự động trở thành lời giải thích nhân quả.

## Attention Maps

Visualizing attention weights can show đơn vị từ (token / 토큰) tương tác (interaction / 상호작용) but should not be treated as chính xác (exact / 정확한) nhân quả (causal / 인과적) explanation. Multiple heads/layers and residual pathways contribute.

Kích thước patch vì thế là một lựa chọn triển khai: patch nhỏ giữ chi tiết hơn nhưng làm số token và chi phí tăng.

## Patch kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)

Large patch:

```text
fewer tokens
lower compute
less fine detail
```

Small patch:

```text
more tokens
higher compute
better local granularity
```

Tác vụ (task / 작업) and hardware determine sweet spot.

Khi patch đã trở thành token, cùng một giao diện có thể nối encoder ảnh với token văn bản trong các hệ thống multimodal.

## Vision Transformer và Multimodal AI

Once ảnh (image / 이미지) becomes chuỗi (sequence / 시퀀스) of embeddings, kiến trúc (architecture / 아키텍처) aligns naturally with văn bản (text / 텍스트) đơn vị từ (token / 토큰) processing. Multimodal các mô hình (models / 모델들) can:

- encode ảnh (image / 이미지) separately then dự án (project / 프로젝트) into LLM không gian (space / 공간);
- concatenate visual tokens with văn bản (text / 텍스트) tokens;
- use cross-attention between modalities.

ViT therefore is a cốt lõi (core / 핵심) cầu nối (bridge / 브리지) to vision-language các mô hình (models / 모델들).

Các encoder thị giác được pretrain ở quy mô lớn vì vậy trở thành foundation model có thể chuyển sang nhiều task và mục tiêu khác nhau.

## Foundation Vision các mô hình (models / 모델들)

Large pretrained visual encoders learn representations transferable across classification, detection, segmentation and multimodal alignment. Pretraining objectives may be supervised, contrastive, masked or multimodal.

Mô hình tư duy sau đây tóm tắt sự đánh đổi cốt lõi giữa patch sequence của ViT và locality được mã hóa sẵn của CNN.

## Mô hình tư duy (mental model / 사고 모델)

> **ViT xem ảnh (image / 이미지) như một set/chuỗi (sequence / 시퀀스) patches cần học quan hệ (relation / 관계) toàn cục; CNN xem ảnh (image / 이미지) như một spatial tín hiệu (signal / 신호) nơi cục bộ (local / 로컬) mẫu (pattern / 패턴) sharing được hard-code mạnh hơn.**

Từ mô hình này, có thể kiểm tra ba ngộ nhận về spatial bias, attention toàn cục và quan hệ giữa transformer với CNN.

## Dùng chung (common / 공통) Misconceptions

### “ViT không có spatial độ lệch (bias / 편향)”

Patch bố cục (layout / 레이아웃), positional encoding, augmentations và kiến trúc (architecture / 아키텍처) variants vẫn encode spatial cấu trúc (structure / 구조).

### “Attention toàn cục (global / 전역) nên luôn tốt hơn convolution”

Toàn cục (global / 전역) attention expensive và không phải mọi tác vụ (task / 작업) cần toàn cục (global / 전역) quan hệ (relation / 관계) ở mọi tầng (layer / 계층).

### “Transformer đã thay CNN hoàn toàn”

Hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) sử dụng cả hai families và hybrid designs.

Các giới hạn đó nối ViT với attention và transformer tổng quát, đồng thời mở sang biểu diễn thị giác hiện đại.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Vision Transformer reuses [Attention](../06_deep_learning_architectures/04_attention.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md) trong spatial lĩnh vực (domain / 도메인).

Xem tiếp: [Modern Visual Representation](./08_modern_visual_representation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
