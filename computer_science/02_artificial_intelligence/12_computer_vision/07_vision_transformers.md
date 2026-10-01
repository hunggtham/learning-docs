# Vision Transformers

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Vision Transformers**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Patch Tokenization** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Vì sao cần Positional thông tin (information / 정보)?** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

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

> **Chuyển mạch:** Trong **Vision Transformers**, **Vì sao cần Positional thông tin (information / 정보)?** tiếp nhận điểm tựa từ **Patch Tokenization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CLS đơn vị từ (token / 토큰)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vì sao cần Positional thông tin (information / 정보)?

Self-attention nguyên bản không biết patch nào ở top-left hay bottom-right nếu không encode position.

Positional embeddings thêm spatial thứ tự (order / 순서). Có thể learned absolute, relative hoặc 2D variants.

> **Chuyển mạch:** Ở chặng này của **Vision Transformers**, **CLS đơn vị từ (token / 토큰)** tiếp nhận điểm tựa từ **Vì sao cần Positional thông tin (information / 정보)?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Self-Attention trong ảnh (image / 이미지)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CLS đơn vị từ (token / 토큰)

Original ViT thêm learnable `[CLS]` đơn vị từ (token / 토큰) vào chuỗi (sequence / 시퀀스). Sau encoder, biểu diễn (representation / 표현) của đơn vị từ (token / 토큰) này dùng cho classification.

Alternatives dùng toàn cục (global / 전역) average pooling trên patch features.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision Transformers**, **Self-Attention trong ảnh (image / 이미지)** tiếp nhận điểm tựa từ **CLS đơn vị từ (token / 토큰)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Độ phức tạp (complexity / 복잡도)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Self-Attention trong ảnh (image / 이미지)

Attention:

\[
A=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)
\]

cho mỗi patch aggregate thông tin (information / 정보) từ mọi patch khác.

Điểm mạnh: long-range interactions accessible ngay một tầng (layer / 계층), không cần ngăn xếp (stack / 스택) many cục bộ (local / 로컬) convs để receptive trường dữ liệu (field / 필드) lan rộng.

> **Chuyển mạch:** Trong **Vision Transformers**, **Độ phức tạp (complexity / 복잡도)** tiếp nhận điểm tựa từ **Self-Attention trong ảnh (image / 이미지)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **CNN vs ViT Inductive độ lệch (bias / 편향)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Độ phức tạp (complexity / 복잡도)

Attention bộ nhớ (memory / 메모리)/compute theo số tokens gần:

\[
O(N^2)
\]

Nếu patch kích thước (size / 크기) nhỏ hoặc high-resolution ảnh (image / 이미지), `N` tăng nhanh.

Ví dụ doubling both H and W → patches ~4× → attention ma trận (matrix / 행렬) ~16×.

Do đó high-resolution ViT cần hierarchical/windowed/sparse attention variants.

> **Chuyển mạch:** Ở chặng này của **Vision Transformers**, **CNN vs ViT Inductive độ lệch (bias / 편향)** tiếp nhận điểm tựa từ **Độ phức tạp (complexity / 복잡도)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Dữ liệu (data / 데이터) quy mô (scale / 규모)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## CNN vs ViT Inductive độ lệch (bias / 편향)

CNN hard-code:

- locality;
- translation weight sharing;
- hierarchical spatial processing.

ViT hard-code ít hơn, cho mô hình (model / 모델) learn relations from dữ liệu (data / 데이터). Điều này từng khiến ViT cần large-scale pretraining hơn CNN, nhưng hiện đại (modern / 현대적) huấn luyện (training / 학습)/augmentation architectures thu hẹp gap.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision Transformers**, **CNN vs ViT Inductive độ lệch (bias / 편향)** nêu điều cần giải thích; **Dữ liệu (data / 데이터) quy mô (scale / 규모)** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Hierarchical Vision Transformers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dữ liệu (data / 데이터) quy mô (scale / 규모)

Weaker inductive độ lệch (bias / 편향) means mô hình (model / 모델) may need more dữ liệu (data / 데이터)/regularization to discover useful cấu trúc (structure / 구조). Large pretraining giúp ViT shine.

Đây là example của general ML principle:

> stronger prior → potentially better mẫu (sample / 표본) efficiency; weaker prior → more flexibility if dữ liệu (data / 데이터)/compute abundant.

> **Chuyển mạch:** Trong **Vision Transformers**, **Dữ liệu (data / 데이터) quy mô (scale / 규모)** nêu điều cần giải thích; **Hierarchical Vision Transformers** đối chiếu nó với bằng chứng hoặc nguồn kiểm chứng. Từ đây, **Windowed Attention** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hierarchical Vision Transformers

Các mô hình (models / 모델들) như Swin tiến trình (process / 프로세스) cục bộ (local / 로컬) windows và merge patches over stages:

```text
fine patches
→ local attention
→ patch merging
→ coarser feature hierarchy
```

Điều này recover multi-scale cấu trúc (structure / 구조) useful detection/segmentation và reduce quadratic chi phí (cost / 비용).

> **Chuyển mạch:** Ở chặng này của **Vision Transformers**, **Windowed Attention** tiếp nhận điểm tựa từ **Hierarchical Vision Transformers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Hybrid các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Windowed Attention

Attention chỉ trong cục bộ (local / 로컬) windows giảm độ phức tạp (complexity / 복잡도). Shifted windows allow cross-window communication across layers.

Sự đánh đổi (trade-off / 트레이드오프) gần CNN: locality introduced lại để gain efficiency.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision Transformers**, **Hybrid các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Windowed Attention** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Masked ảnh (image / 이미지) Modeling** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Hybrid các mô hình (models / 모델들)

CNN stem + Transformer body hoặc convolution inside transformer khối (block / 블록) kết hợp cục bộ (local / 로컬) độ lệch (bias / 편향) và toàn cục (global / 전역) attention.

Hiện đại (modern / 현대적) vision architectures không còn nhị phân (binary / 이진) CNN vs Transformer; ideas mix widely.

> **Chuyển mạch:** Trong **Vision Transformers**, **Masked ảnh (image / 이미지) Modeling** tiếp nhận điểm tựa từ **Hybrid các mô hình (models / 모델들)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Distillation** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Masked ảnh (image / 이미지) Modeling

ViT naturally supports masked-patch pretraining. Hide large fraction patches, train reconstruct pixels/features/latent targets.

This resembles masked ngôn ngữ (language / 언어) modeling nhưng ảnh (image / 이미지) patches have high redundancy, nên masking ratios/objectives khác NLP.

> **Chuyển mạch:** Ở chặng này của **Vision Transformers**, **Distillation** tiếp nhận điểm tựa từ **Masked ảnh (image / 이미지) Modeling** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Detection with Transformers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Distillation

Teacher mô hình (model / 모델) can transfer lớp (class / 클래스)/biểu diễn (representation / 표현) signals to ViT, improving dữ liệu (data / 데이터) efficiency.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision Transformers**, **Detection with Transformers** tiếp nhận điểm tựa từ **Distillation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Segmentation with Transformers** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Detection with Transformers

DETR uses CNN/ViT-like features + Transformer encoder-decoder + learned đối tượng (object / 객체) queries. Detection becomes set prediction rather than anchor/NMS chuỗi xử lý (pipeline / 파이프라인).

> **Chuyển mạch:** Trong **Vision Transformers**, **Segmentation with Transformers** tiếp nhận điểm tựa từ **Detection with Transformers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Position Resolution Transfer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Segmentation with Transformers

Patch features can be decoded into masks. toàn cục (global / 전역) ngữ cảnh (context / 맥락) helps scene parsing; multi-scale/hierarchical features important ranh giới (boundary / 경계)/detail.

> **Chuyển mạch:** Ở chặng này của **Vision Transformers**, **Position Resolution Transfer** tiếp nhận điểm tựa từ **Segmentation with Transformers** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Attention Maps** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Position Resolution Transfer

Fine-tuning at different ảnh (image / 이미지) resolution may require interpolate positional embeddings if using absolute positions.

This is an hiện thực (implementation / 구현) consequence of learned positional bảng (table / 테이블).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision Transformers**, **Attention Maps** tiếp nhận điểm tựa từ **Position Resolution Transfer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Patch kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Attention Maps

Visualizing attention weights can show đơn vị từ (token / 토큰) tương tác (interaction / 상호작용) but should not be treated as chính xác (exact / 정확한) nhân quả (causal / 인과적) explanation. Multiple heads/layers and residual pathways contribute.

> **Chuyển mạch:** Trong **Vision Transformers**, **Patch kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)** tiếp nhận điểm tựa từ **Attention Maps** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Vision Transformer và Multimodal AI** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

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

> **Chuyển mạch:** Ở chặng này của **Vision Transformers**, **Vision Transformer và Multimodal AI** tiếp nhận điểm tựa từ **Patch kích thước (size / 크기) sự đánh đổi (trade-off / 트레이드오프)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Foundation Vision các mô hình (models / 모델들)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Vision Transformer và Multimodal AI

Once ảnh (image / 이미지) becomes chuỗi (sequence / 시퀀스) of embeddings, kiến trúc (architecture / 아키텍처) aligns naturally with văn bản (text / 텍스트) đơn vị từ (token / 토큰) processing. Multimodal các mô hình (models / 모델들) can:

- encode ảnh (image / 이미지) separately then dự án (project / 프로젝트) into LLM không gian (space / 공간);
- concatenate visual tokens with văn bản (text / 텍스트) tokens;
- use cross-attention between modalities.

ViT therefore is a cốt lõi (core / 핵심) cầu nối (bridge / 브리지) to vision-language các mô hình (models / 모델들).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision Transformers**, **Foundation Vision các mô hình (models / 모델들)** tiếp nhận điểm tựa từ **Vision Transformer và Multimodal AI** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Foundation Vision các mô hình (models / 모델들)

Large pretrained visual encoders learn representations transferable across classification, detection, segmentation and multimodal alignment. Pretraining objectives may be supervised, contrastive, masked or multimodal.

> **Chuyển mạch:** Trong **Vision Transformers**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Foundation Vision các mô hình (models / 모델들)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

> **ViT xem ảnh (image / 이미지) như một set/chuỗi (sequence / 시퀀스) patches cần học quan hệ (relation / 관계) toàn cục; CNN xem ảnh (image / 이미지) như một spatial tín hiệu (signal / 신호) nơi cục bộ (local / 로컬) mẫu (pattern / 패턴) sharing được hard-code mạnh hơn.**

> **Chuyển mạch:** Ở chặng này của **Vision Transformers**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “ViT không có spatial độ lệch (bias / 편향)”

Patch bố cục (layout / 레이아웃), positional encoding, augmentations và kiến trúc (architecture / 아키텍처) variants vẫn encode spatial cấu trúc (structure / 구조).

### “Attention toàn cục (global / 전역) nên luôn tốt hơn convolution”

Toàn cục (global / 전역) attention expensive và không phải mọi tác vụ (task / 작업) cần toàn cục (global / 전역) quan hệ (relation / 관계) ở mọi tầng (layer / 계층).

### “Transformer đã thay CNN hoàn toàn”

Hiện đại (modern / 현대적) các hệ thống (systems / 시스템들) sử dụng cả hai families và hybrid designs.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Vision Transformers**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Vision Transformer reuses [Attention](../06_deep_learning_architectures/04_attention.md) và [Transformer](../06_deep_learning_architectures/05_transformer.md) trong spatial lĩnh vực (domain / 도메인).

Xem tiếp: [Modern Visual Representation](./08_modern_visual_representation.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
