# Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable

> **Mạch đọc:** [README](./README.md) là bản đồ owner của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**; nhìn vào vị trí đó trước để biết file này đang phục vụ nhánh kiến thức nào. **Vì sao không initialize mọi weight bằng zero?** mở đối tượng chính của file và câu hỏi cần theo dõi; sau đó sang **Variance propagation** để mở rộng đối tượng sang phạm vi kế cận. Cách đi này giữ lại điểm tựa của section đầu và cho biết kết luận sẽ được dùng ở đâu, thay vì dừng ở định nghĩa đầu tiên.

Deep mạng (network / 네트워크) có thể có kiến trúc (architecture / 아키텍처) đúng nhưng huấn luyện (training / 학습) thất bại (fail / 실패) ngay từ đầu nếu activations hoặc gradients explode/vanish qua layers. **Initialization (초기화 / khởi tạo)** chọn starting phân phối (distribution / 분포) của parameters; **Normalization (정규화 / chuẩn hóa)** kiểm soát statistics của intermediate representations trong huấn luyện (training / 학습).

Hai concept này giải quyết một cốt lõi (core / 핵심) các hệ thống (systems / 시스템들) bài toán (problem / 문제): làm sao tín hiệu (signal / 신호) đi qua nhiều transformations mà vẫn ở numerical/tối ưu hóa (optimization / 최적화) quy mô (scale / 규모) hợp lý?

## Vì sao không initialize mọi weight bằng zero?

Nếu neurons cùng tầng (layer / 계층) có identical weights zero, chúng nhận cùng độ dốc (gradient / 기울기) và tiếp tục giống nhau. **Symmetry breaking** cần random initialization để units học functions khác nhau.

Độ lệch (bias / 편향) có thể initialize zero vì weights đã break symmetry.

> **Chuyển mạch:** Trong **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Variance propagation** tiếp nhận điểm tựa từ **Vì sao không initialize mọi weight bằng zero?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Xavier / Glorot Initialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Variance propagation

Giả sử:

\[
z=\sum_{i=1}^{n}w_ix_i
\]

Nếu independent, zero-mean:

\[
Var(z)\approx nVar(w)Var(x)
\]

Nếu `Var(w)` không quy mô (scale / 규모) theo fan-in `n`, activation variance tăng/giảm theo độ sâu (depth / 깊이).

Initialization tốt cố giữ forward activation variance và backward độ dốc (gradient / 기울기) variance roughly stable.

> **Chuyển mạch:** Ở chặng này của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Xavier / Glorot Initialization** tiếp nhận điểm tựa từ **Variance propagation** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **He / Kaiming Initialization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Xavier / Glorot Initialization

Phù hợp tanh/sigmoid-like symmetric activations:

\[
Var(w)\approx\frac{2}{fan_{in}+fan_{out}}
\]

Một dùng chung (common / 공통) form uniform:

\[
w\sim U\left(-\sqrt{\frac{6}{fan_{in}+fan_{out}}},
\sqrt{\frac{6}{fan_{in}+fan_{out}}}\right)
\]

Mục tiêu balance tín hiệu (signal / 신호) forward/backward.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **He / Kaiming Initialization** tiếp nhận điểm tựa từ **Xavier / Glorot Initialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Initialization không độc lập kiến trúc (architecture / 아키텍처)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## He / Kaiming Initialization

ReLU zero roughly half activations under symmetric giả định (assumption / 가정), nên use larger variance:

\[
Var(w)\approx\frac{2}{fan_{in}}
\]

Dùng chung (common / 공통) normal initialization:

\[
w\sim\mathcal N(0,2/fan_{in})
\]

Activation-specific gain matters.

> **Chuyển mạch:** Trong **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Initialization không độc lập kiến trúc (architecture / 아키텍처)** tiếp nhận điểm tựa từ **He / Kaiming Initialization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Batch Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Initialization không độc lập kiến trúc (architecture / 아키텍처)

Residual networks, Transformers, gated blocks và normalization layers thay tín hiệu (signal / 신호) dynamics. Large-model recipes có custom scaling, residual branch initialization hoặc μ-parameterization variants.

Không có một initialization formula universal cho mọi kiến trúc (architecture / 아키텍처).

> **Chuyển mạch:** Ở chặng này của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Batch Normalization** tiếp nhận điểm tựa từ **Initialization không độc lập kiến trúc (architecture / 아키텍처)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **BatchNorm giúp gì?** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Batch Normalization

BatchNorm normalize activation per tính năng (feature / 기능)/channel dùng mini-batch statistics:

\[
\mu_B=\frac1m\sum_i x_i
\]

\[
\sigma_B^2=\frac1m\sum_i(x_i-\mu_B)^2
\]

\[
\hat x_i=\frac{x_i-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}
\]

rồi learn affine quy mô (scale / 규모)/shift:

\[
y_i=\gamma\hat x_i+\beta
\]

`γ,β` cho mô hình (model / 모델) restore useful quy mô (scale / 규모)/offset.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **BatchNorm giúp gì?** tiếp nhận điểm tựa từ **Batch Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Train vs Eval trong BatchNorm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## BatchNorm giúp gì?

Lịch sử thường giải thích bằng “reduce nội bộ (internal / 내부) covariate shift”, nhưng hiện đại (modern / 현대적) understanding rộng hơn. BatchNorm:

- stabilizes activation quy mô (scale / 규모);
- smooths tối ưu hóa (optimization / 최적화) landscape in useful ways;
- permits larger LR;
- adds batch-dependent noise/regularization;
- reduces sensitivity to initialization.

Không nên coi một single explanation là complete.

> **Chuyển mạch:** Trong **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Train vs Eval trong BatchNorm** tiếp nhận điểm tựa từ **BatchNorm giúp gì?** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tầng (layer / 계층) Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Train vs Eval trong BatchNorm

Huấn luyện (training / 학습) dùng hiện tại (current / 현재) batch stats và cập nhật (update / 업데이트) running estimates. Evaluation dùng running mean/variance.

Small batch làm estimates noisy. phân tán (distributed / 분산) huấn luyện (training / 학습) có SyncBatchNorm để aggregate stats across devices, nhưng communication chi phí (cost / 비용) tăng.

Nếu triển khai (deployment / 배포) phân phối (distribution / 분포) shift, stale running stats cũng có thể gây degradation.

> **Chuyển mạch:** Ở chặng này của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Tầng (layer / 계층) Normalization** tiếp nhận điểm tựa từ **Train vs Eval trong BatchNorm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **RMSNorm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tầng (layer / 계층) Normalization

LayerNorm normalize across tính năng (feature / 기능) dimensions của từng mẫu (sample / 표본)/đơn vị từ (token / 토큰):

\[
\mu=\frac1D\sum_{j=1}^{D}x_j
\]

\[
\sigma^2=\frac1D\sum_j(x_j-\mu)^2
\]

Không phụ thuộc batch kích thước (size / 크기), nên phù hợp chuỗi (sequence / 시퀀스) các mô hình (models / 모델들)/Transformers.

Transformer hidden trạng thái (state / 상태) `x∈R^D` được normalize per đơn vị từ (token / 토큰).

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **RMSNorm** tiếp nhận điểm tựa từ **Tầng (layer / 계층) Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **GroupNorm và InstanceNorm** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## RMSNorm

RMSNorm bỏ mean-centering, quy mô (scale / 규모) bằng gốc (root / 루트) mean square:

\[
RMS(x)=\sqrt{\frac1D\sum_jx_j^2+\epsilon}
\]

\[
y=\gamma\odot\frac{x}{RMS(x)}
\]

Đơn giản/efficient và phổ biến trong hiện đại (modern / 현대적) LLMs.

> **Chuyển mạch:** Trong **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **GroupNorm và InstanceNorm** tiếp nhận điểm tựa từ **RMSNorm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Pre-Norm vs Post-Norm Transformer** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## GroupNorm và InstanceNorm

**GroupNorm** chia channels thành groups rồi normalize trong group, không phụ thuộc batch statistics mạnh; useful khi vision batch small.

**InstanceNorm** normalize per mẫu (sample / 표본)/channel và phổ biến trong style/ảnh (image / 이미지) generation contexts.

Normalization axes là modeling choice.

> **Chuyển mạch:** Ở chặng này của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Pre-Norm vs Post-Norm Transformer** tiếp nhận điểm tựa từ **GroupNorm và InstanceNorm** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Normalization không chỉ standardize đầu vào (input / 입력)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Pre-Norm vs Post-Norm Transformer

Post-Norm classic:

\[
y=LN(x+F(x))
\]

Pre-Norm:

\[
y=x+F(LN(x))
\]

Pre-Norm tạo cleaner định danh (identity / 식별자) residual độ dốc (gradient / 기울기) đường dẫn (path / 경로) và thường train deep Transformers stable hơn, nên được dùng rộng rãi.

Kiến trúc (architecture / 아키텍처) details như norm placement ảnh hưởng tối ưu hóa (optimization / 최적화) lớn.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Normalization không chỉ standardize đầu vào (input / 입력)** tiếp nhận điểm tựa từ **Pre-Norm vs Post-Norm Transformer** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Epsilon và Numerical Stability** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Normalization không chỉ standardize đầu vào (input / 입력)

Đầu vào (input / 입력) standardization là preprocessing trên dataset. BatchNorm/LayerNorm là nội bộ (internal / 내부) differentiable modules với learned quy mô (scale / 규모)/shift, applied repeatedly inside mạng (network / 네트워크).

Hai concept related nhưng khác phạm vi (scope / 범위) và hành vi (behavior / 동작).

> **Chuyển mạch:** Trong **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Epsilon và Numerical Stability** tiếp nhận điểm tựa từ **Normalization không chỉ standardize đầu vào (input / 입력)** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Weight Normalization và Spectral Normalization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Epsilon và Numerical Stability

Denominator thêm `ε` để tránh divide-by-zero:

\[
\sqrt{\sigma^2+\epsilon}
\]

Choice epsilon có thể matter trong low precision. Normalization kernels thường accumulate stats higher precision.

> **Chuyển mạch:** Ở chặng này của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Weight Normalization và Spectral Normalization** tiếp nhận điểm tựa từ **Epsilon và Numerical Stability** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Tương tác (interaction / 상호작용) với Regularization** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Weight Normalization và Spectral Normalization

Có normalization tác động parameters thay activations.

WeightNorm reparameterize weight thành direction + magnitude.

Spectral Normalization constrain largest singular giá trị (value / 값), giúp điều khiển (control / 제어) Lipschitz hành vi (behavior / 동작) và từng được dùng mạnh trong GAN discriminators.

Normalization là family rộng, không chỉ BatchNorm.

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Tương tác (interaction / 상호작용) với Regularization** tiếp nhận điểm tựa từ **Weight Normalization và Spectral Normalization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Debugging tín hiệu (signal / 신호) statistics** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Tương tác (interaction / 상호작용) với Regularization

BatchNorm noise có implicit regularization; Dropout + BatchNorm tương tác (interaction / 상호작용) đôi khi complex. Weight decay trên norm quy mô (scale / 규모)/độ lệch (bias / 편향) thường excluded trong hiện đại (modern / 현대적) optimizer configs.

Recipes phải xem whole hệ thống (system / 시스템), không tune từng trick isolated.

> **Chuyển mạch:** Trong **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Debugging tín hiệu (signal / 신호) statistics** tiếp nhận điểm tựa từ **Tương tác (interaction / 상호작용) với Regularization** nhưng đổi góc nhìn sang câu hỏi của chính nó; đọc liền hai mục để thấy mối quan hệ đó. Từ đây, **Mô hình tư duy (mental model / 사고 모델)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Debugging tín hiệu (signal / 신호) statistics

Theo dõi per-layer:

```text
activation mean/std
activation max/min
zero fraction
gradient norm
parameter norm
update/parameter ratio
```

Nếu std tăng exponential qua độ sâu (depth / 깊이) → exploding tín hiệu (signal / 신호). Nếu collapse gần zero → vanishing/dead units.

> **Chuyển mạch:** Ở chặng này của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Mô hình tư duy (mental model / 사고 모델)** gom các mảnh từ **Debugging tín hiệu (signal / 신호) statistics** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Dùng chung (common / 공통) Misconceptions** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Mô hình tư duy (mental model / 사고 모델)

Phần này chốt mental model thành một chuỗi có thể dùng lại: bối cảnh → cơ chế → quan sát → giới hạn → quyết định. Hãy đọc sơ đồ như công cụ suy luận, không như một khẩu hiệu tách khỏi chapter.

```text
Initialization = chọn starting scale để network bắt đầu ở vùng trainable
Normalization  = liên tục giữ intermediate scale/statistics trong vùng dễ optimize
Residual paths = tạo đường truyền signal/gradient ổn định
```

> **Chuyển mạch:** Đặt trong câu hỏi lớn của **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, **Dùng chung (common / 공통) Misconceptions** gom các mảnh từ **Mô hình tư duy (mental model / 사고 모델)** thành một kết luận có thể mang sang phần kế tiếp. Từ đây, **Liên kết kiến thức (knowledge connection / 지식 연결)** sẽ cho biết hệ quả hoặc giới hạn ấy hiện ra ở đâu.

## Dùng chung (common / 공통) Misconceptions

### “Random small weights là đủ”

Quy mô (scale / 규모) phải depend fan-in/activation/kiến trúc (architecture / 아키텍처); quá nhỏ cũng gây vanishing.

### “BatchNorm và LayerNorm giống nhau, chỉ tên khác”

Axes/statistics và train/eval hành vi (behavior / 동작) khác fundamentally.

### “Normalization loại bỏ need for good initialization”

Nó giảm sensitivity nhưng initialization vẫn ảnh hưởng early dynamics và large/deep kiến trúc (architecture / 아키텍처) stability.

### “LayerNorm làm đơn vị từ (token / 토큰) véc-tơ (vector / 벡터) mất thông tin (information / 정보) vì mean=0 variance=1”

Learned affine parameters và direction/relative mẫu (pattern / 패턴) vẫn carry thông tin (information / 정보); residual stream kiến trúc (architecture / 아키텍처) cũng giữ pathways khác.

> **Chuyển mạch:** Trong **Initialization và Normalization: giữ tín hiệu (signal / 신호) và độ dốc (gradient / 기울기) ở quy mô (scale / 규모) Trainable**, sau nội dung của **Dùng chung (common / 공통) Misconceptions**, **Liên kết kiến thức (knowledge connection / 지식 연결)** chỉ rõ tài liệu chuẩn và vị trí sở hữu để người học biết phần nào cần quay lại khi muốn đào sâu. Phần còn lại của file dùng kết quả này để khép lại mạch giải thích.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Activation Functions](./02_activation_functions.md), [Backpropagation](./04_backpropagation.md), [Optimizers](./05_gradient_descent_and_optimizers.md) và sau này [Transformer](../06_deep_learning_architectures/05_transformer.md).

> **Bàn giao:** Sau **Liên kết kiến thức (knowledge connection / 지식 연결)**, hãy giữ lại kết luận và ranh giới của mục này; quay về [README](./README.md) khi cần định vị owner hoặc chọn nhánh học tiếp theo.
