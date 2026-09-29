# Regularization trong Neural Networks

> **Mạch đọc:** Đặt **Regularization trong Neural Networks** trong bản đồ [README](./README.md) để thấy đơn vị sở hữu (owner / 오너) và vị trí của nó. Nội dung đi từ **L2 Penalty và Weight Decay** sang **L1 Regularization**; điểm nối này chuẩn bị câu hỏi cho các mục sau thay vì dừng ở định nghĩa đầu tiên.


Regularization (규제 / 정규화라는 표현도 쓰이지만 normalization과 구분 필요 / điều chuẩn) là các mechanisms độ lệch (bias / 편향) huấn luyện (training / 학습) về những solutions có khả năng generalize tốt hơn, thay vì chỉ minimize huấn luyện (training / 학습) mất mát (loss / 손실). Trong neural networks, regularization không phải một “mẹo chống overfitting” riêng lẻ; nó xuất hiện qua mục tiêu (objective / 목표), kiến trúc (architecture / 아키텍처), dữ liệu (data / 데이터), stochasticity và tối ưu hóa (optimization / 최적화).

Cần phân biệt `regularization` với `normalization`. Normalization kiểm soát statistics/quy mô (scale / 규모); regularization kiểm soát effective độ phức tạp (complexity / 복잡도) hoặc preference among solutions.

## L2 Penalty và Weight Decay

L2-regularized mục tiêu (objective / 목표):

\[
J(\theta)=\hat R(\theta)+\lambda\|\theta\|_2^2
\]

khuyến khích parameters magnitude nhỏ.

Với vanilla SGD, L2 độ dốc (gradient / 기울기) term:

\[
2\lambda\theta
\]

tạo shrinkage tương tự weight decay. Với adaptive optimizers, decoupled weight decay (AdamW) khác naive L2 penalty.

Weight decay có thể improve generalization và stabilize quy mô (scale / 규모), nhưng optimal giá trị (value / 값) phụ thuộc học tập (learning / 학습) tỷ lệ (rate / 비율), batch kích thước (size / 크기), kiến trúc (architecture / 아키텍처) và huấn luyện (training / 학습) length.

## L1 Regularization

\[
J=\hat R+\lambda\|\theta\|_1
\]

encourage sparsity. Với large neural networks, pure L1 ít là default hơn L2/weight decay nhưng useful khi muốn sparse solution hoặc specific các ràng buộc (constraints / 제약조건들).

Structured sparsity có thể mục tiêu (target / 대상) whole channels/heads/blocks để actual hardware speedup; random individual zeros không luôn tăng speed nếu kernels không exploit sparsity.

## Dropout

Trong huấn luyện (training / 학습), dropout random mask activations:

\[
\tilde h_i=\frac{m_i}{1-p}h_i,
\qquad m_i\sim Bernoulli(1-p)
\]

`p` là drop xác suất (probability / 확률). Scaling `1/(1-p)` giữ expected activation roughly same.

Dropout ngăn units phụ thuộc quá mạnh vào chính xác (exact / 정확한) co-adaptation và tạo stochastic ensemble-like tác động (effect / 효과).

Suy luận (inference / 추론) thường disable dropout.

## Dropout không phải luôn cần

Large hiện đại (modern / 현대적) các mô hình (models / 모델들) với huge dữ liệu (data / 데이터), normalization, augmentation và weight decay có thể dùng dropout rất thấp hoặc zero trong pretraining. Fine-tuning small dữ liệu (data / 데이터) có thể lại benefit.

Regularization strength phải match dữ liệu (data / 데이터)/mô hình (model / 모델) regime.

## Early Stopping

Nếu kiểm tra hợp lệ (validation / 검증) hiệu năng (performance / 성능) bắt đầu worsen trong khi huấn luyện (training / 학습) mất mát (loss / 손실) tiếp tục giảm, stop tại checkpoint tốt nhất.

Early stopping acts như regularization vì giới hạn tối ưu hóa (optimization / 최적화) trajectory; mô hình (model / 모델) chưa có thời gian fit finer sample-specific patterns.

Nhưng nếu huấn luyện (training / 학습) schedule chưa tuned, stop sớm có thể chỉ mask bad học tập (learning / 학습) tỷ lệ (rate / 비율).

## Dữ liệu (data / 데이터) Augmentation

Augmentation tạo transformed examples mà label/ngữ nghĩa (semantics / 의미론) nên preserve:

Ảnh (image / 이미지):

```text
crop, flip, color jitter, rotation (nếu task invariant)
```

Audio:

```text
noise, time masking, frequency masking
```

Văn bản (text / 텍스트) augmentation khó hơn vì small wording thay đổi (change / 변경) có thể đổi meaning.

Augmentation encode **invariance các giả định (assumptions / 가정들)**. Horizontal flip hợp đối tượng (object / 객체) recognition nhưng có thể sai với văn bản (text / 텍스트) ảnh (image / 이미지) hoặc medical laterality.

## Mixup

Mixup tạo convex combinations:

\[
\tilde x=\lambda x_i+(1-\lambda)x_j
\]

\[
\tilde y=\lambda y_i+(1-\lambda)y_j
\]

Nó encourage smoother hành vi (behavior / 동작) giữa examples và giảm sharp memorization.

CutMix cho images paste region từ ảnh (image / 이미지) khác và mix labels proportional area.

## Label Smoothing

One-hot mục tiêu (target / 대상) thay bằng slightly softened phân phối (distribution / 분포):

\[
y'_k=(1-\epsilon)y_k+\frac{\epsilon}{K}
\]

hoặc variant distribute mass among incorrect classes.

Label smoothing giảm incentive đẩy logits tới extreme confidence, có thể improve generalization/calibration trong regimes.

Nhưng nó cũng có trade-offs, ví dụ representations cho distillation/calibration có thể thay đổi; không nên apply blindly.

## Noise Injection

Thêm noise vào inputs, activations, weights hoặc gradients có regularization tác động (effect / 효과). Dropout là một form structured multiplicative noise.

Stochastic độ dốc (gradient / 기울기) Descent mini-batch noise cũng tạo implicit regularization.

## Architectural Regularization

Convolution weight sharing giảm degrees of freedom so với dense tầng (layer / 계층).

Bottlenecks giới hạn biểu diễn (representation / 표현) sức chứa (capacity / 용량).

Low-rank adapters constrain fine-tuning updates vào low-rank subspace.

Sparse attention/routing constrain interactions.

Kiến trúc (architecture / 아키텍처) itself is regularizer through inductive độ lệch (bias / 편향).

## Parameter Sharing

RNN reuse same weights across timesteps; CNN reuse kernel across locations; Transformer reuse same projection matrices across đơn vị từ (token / 토큰) positions within tầng (layer / 계층).

Sharing reduces parameter count và encodes symmetry/invariance các giả định (assumptions / 가정들).

## Batch Normalization as implicit regularization

Batch statistics introduce noise depending on co-samples. This can regularize. With very large batch or synchronized stats, tác động (effect / 효과) changes.

Do not treat normalization and regularization as identical, but acknowledge interactions.

## Pretraining as Regularization / Prior

Fine-tuning pretrained mô hình (model / 모델) starts from parameters encoding broad cấu trúc (structure / 구조). Small tác vụ (task / 작업) dataset only nudges solution around pretrained region.

This acts like a strong data-driven prior compared with huấn luyện (training / 학습) from random initialization.

Transfer học tập (learning / 학습) therefore changes độ lệch (bias / 편향)–variance landscape dramatically.

## Parameter-Efficient Fine-Tuning

LoRA các mô hình (models / 모델들) cập nhật (update / 업데이트):

\[
\Delta W=BA
\]

with low rank `r`:

\[
A\in R^{r\times d_{in}},
B\in R^{d_{out}\times r}
\]

Instead of full arbitrary `ΔW`, updates constrained low-rank. This reduces bộ nhớ (memory / 메모리) and can regularize small-data adaptation.

LoRA will return in LLM fine-tuning chapters.

## Regularization và Memorization

Neural networks can memorize random labels with enough sức chứa (capacity / 용량), showing kiến trúc (architecture / 아키텍처) sức chứa (capacity / 용량) alone doesn't force generalization.

Real generalization comes from combination of cấu trúc (structure / 구조) in natural dữ liệu (data / 데이터), tối ưu hóa (optimization / 최적화) độ lệch (bias / 편향), regularization, augmentation and quy mô (scale / 규모).

Memorization and generalization can coexist; mô hình (model / 모델) may memorize rare examples while still generalizing broadly.

## Regularization under phân phối (distribution / 분포) Shift

Regularization improving IID kiểm thử (test / 테스트) may not improve robustness to lĩnh vực (domain / 도메인) shift. dữ liệu (data / 데이터) augmentation aligned with expected shift can help more than generic weight decay.

Robustness requires evaluate on shifted/stress distributions, not infer from regularization alone.

## Mô hình tư duy (mental model / 사고 모델)

> Regularization is preference: trong rất nhiều parameter settings fit dữ liệu huấn luyện (training data / 학습 데이터), ta muốn học tập (learning / 학습) procedure ưu tiên những solutions đơn giản/stable/bất biến (invariant / 불변식) hoặc gần useful prior hơn.

## Dùng chung (common / 공통) Misconceptions

### “More regularization always means less overfitting and therefore better”

Quá mạnh gây underfitting hoặc erase useful tác vụ (task / 작업) adaptation.

### “Dropout phải có trong mọi neural mạng (network / 네트워크)”

Không. Need depends dữ liệu (data / 데이터) quy mô (scale / 규모)/kiến trúc (architecture / 아키텍처)/huấn luyện (training / 학습) regime.

### “dữ liệu (data / 데이터) augmentation chỉ tăng số lượng samples”

Nó quan trọng hơn ở việc encode invariances.

### “Weight decay làm mô hình (model / 모델) sparse”

L2/weight decay shrink magnitude nhưng không thường tạo chính xác (exact / 정확한) zeros như L1/structured pruning.

### “Fine-tuning ít parameters chỉ để tiết kiệm VRAM”

Parameter các ràng buộc (constraints / 제약조건들) cũng thay inductive độ lệch (bias / 편향) và có thể reduce overfitting.

## Liên kết kiến thức (knowledge connection / 지식 연결)

Xem [Bias–Variance and Generalization](../04_machine_learning/14_bias_variance_and_generalization.md), [AdamW](./05_gradient_descent_and_optimizers.md), [Initialization and Normalization](./06_initialization_and_normalization.md), và tiếp theo [Representation Learning](./08_representation_learning.md).

> **Bàn giao:** Sau **liên kết kiến thức (knowledge connection / 지식 연결)**, hãy chốt bất biến (invariant / 불변식) và giới hạn của mục này trước khi nối sang kiến thức kế tiếp. Có thể đọc tiếp [00 from linear models to neural networks](./00_from_linear_models_to_neural_networks.md) để đối chiếu ranh giới (boundary / 경계) gần nhất.
