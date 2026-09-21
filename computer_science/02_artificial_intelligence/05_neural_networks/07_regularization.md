# Regularization trong Neural Network

**Regularization (điều chuẩn)** là tập hợp các cơ chế khiến quá trình training ưu tiên những nghiệm có khả năng khái quát hóa tốt hơn thay vì chỉ giảm training loss thấp nhất có thể. Trong Neural Network, regularization không phải một “mẹo chống overfitting” riêng lẻ; nó xuất hiện trong objective, architecture, dữ liệu, tính ngẫu nhiên và quá trình tối ưu.

Cần phân biệt `regularization` với `normalization`. Normalization chủ yếu kiểm soát scale và thống kê tín hiệu; regularization kiểm soát độ phức tạp hiệu dụng hoặc preference giữa nhiều nghiệm cùng fit dữ liệu.

## L2 Penalty và Weight Decay

Objective có L2:

\[
J(\theta)=\hat R(\theta)+\lambda\|\theta\|_2^2
\]

khuyến khích tham số có độ lớn nhỏ hơn.

Với vanilla SGD, gradient từ L2:

\[
2\lambda\theta
\]

tạo hiệu ứng co tham số tương tự weight decay. Với adaptive optimizer, **weight decay tách rời (decoupled weight decay)** như AdamW khác với việc thêm L2 penalty trực tiếp vào gradient.

Weight decay có thể cải thiện generalization và giúp kiểm soát scale, nhưng giá trị phù hợp phụ thuộc learning rate, batch size, architecture và thời lượng training.

## L1 Regularization

\[
J=\hat R+\lambda\|\theta\|_1
\]

khuyến khích nghiệm thưa (sparse).

Trong mạng lớn, L1 thuần túy ít là lựa chọn mặc định hơn L2 hoặc weight decay, nhưng vẫn hữu ích khi muốn sparsity hoặc ràng buộc cụ thể.

Nếu mục tiêu là tăng tốc thật trên hardware, **structured sparsity** theo channel, head hoặc block thường hữu ích hơn các số 0 rời rạc mà kernel không tận dụng được.

## Dropout

Trong training, Dropout tạo mask ngẫu nhiên trên activation:

\[
\tilde h_i=\frac{m_i}{1-p}h_i,
\qquad m_i\sim Bernoulli(1-p)
\]

`p` là xác suất drop. Hệ số `1/(1-p)` giữ expected activation gần tương đương.

Dropout làm các unit khó phụ thuộc quá mức vào một pattern đồng xuất hiện cố định và tạo hiệu ứng gần giống ensemble ngẫu nhiên.

Khi inference, Dropout thường được tắt.

## Dropout không phải luôn cần

Mô hình hiện đại rất lớn với dataset lớn, normalization, augmentation và weight decay có thể dùng Dropout rất thấp hoặc bằng 0 trong pretraining.

Ngược lại, khi fine-tuning trên dataset nhỏ, Dropout có thể hữu ích hơn.

Cường độ regularization phải phù hợp với quan hệ giữa quy mô dữ liệu, model capacity và task.

## Early Stopping

Nếu validation performance bắt đầu xấu đi trong khi training loss vẫn tiếp tục giảm, có thể dừng tại checkpoint tốt nhất.

Early stopping hoạt động như một dạng regularization vì giới hạn quỹ đạo tối ưu trước khi mô hình có thời gian fit quá sâu vào pattern đặc thù của training sample.

Tuy nhiên nếu learning-rate schedule chưa hợp lý, dừng sớm có thể chỉ đang che giấu một optimization recipe kém.

## Data Augmentation

Augmentation tạo các phiên bản biến đổi mà label hoặc semantics được giả định là giữ nguyên.

Ảnh có thể dùng crop, flip, color jitter hoặc rotation nếu task cho phép.

Âm thanh có thể thêm noise, time masking hoặc frequency masking.

Văn bản khó hơn vì chỉ một thay đổi nhỏ về từ ngữ cũng có thể đổi nghĩa.

Augmentation quan trọng không chỉ vì “tăng số mẫu”, mà vì nó mã hóa **giả định bất biến (invariance assumption)**.

Ví dụ lật ngang hợp lý cho nhận diện nhiều loại vật thể nhưng có thể sai với chữ viết hoặc ảnh y khoa có phân biệt trái/phải.

## Mixup

Mixup tạo tổ hợp lồi của hai sample:

\[
\tilde x=\lambda x_i+(1-\lambda)x_j
\]

\[
\tilde y=\lambda y_i+(1-\lambda)y_j
\]

Cách này khuyến khích mô hình thay đổi đầu ra mượt hơn giữa các sample và giảm việc ghi nhớ quá sắc các điểm riêng lẻ.

CutMix trong ảnh ghép một vùng từ ảnh khác rồi trộn label theo tỷ lệ diện tích.

## Label Smoothing

One-hot target được làm mềm:

\[
y'_k=(1-\epsilon)y_k+\frac{\epsilon}{K}
\]

hoặc một biến thể phân phối một phần probability mass cho các class sai.

Label smoothing làm giảm động lực đẩy logit tới độ tự tin cực đoan và có thể cải thiện generalization hoặc calibration trong một số chế độ.

Tuy nhiên nó cũng làm thay đổi representation và confidence behavior, nên không nên áp dụng máy móc.

## Noise Injection

Thêm nhiễu vào input, activation, weight hoặc gradient có thể tạo regularization.

Dropout chính là một dạng nhiễu nhân có cấu trúc.

Nhiễu từ mini-batch của SGD cũng tạo implicit regularization.

## Regularization từ kiến trúc

Convolution weight sharing giảm số bậc tự do so với dense layer.

Bottleneck giới hạn capacity của representation.

LoRA giới hạn update fine-tuning trong một low-rank subspace.

Sparse attention hoặc routing giới hạn kiểu tương tác.

Vì vậy architecture tự nó cũng là một regularizer thông qua inductive bias.

## Parameter Sharing

RNN dùng lại cùng weight qua nhiều timestep; CNN dùng cùng kernel ở nhiều vị trí; Transformer dùng cùng projection matrix cho mọi token trong một layer.

Chia sẻ tham số làm giảm số degree of freedom và mã hóa symmetry hoặc invariance cụ thể.

## BatchNorm như implicit regularization

BatchNorm dùng batch statistics nên tạo một lượng nhiễu phụ thuộc vào các sample cùng batch. Điều này có thể tạo hiệu ứng regularization.

Khi batch cực lớn hoặc dùng synchronized statistics, hiệu ứng này thay đổi.

Normalization và regularization không phải cùng một khái niệm, nhưng chúng có thể tương tác mạnh.

## Pretraining như một prior đã học

Fine-tuning mô hình pretrained bắt đầu từ tham số đã chứa cấu trúc rộng của dữ liệu trước đó.

Dataset task nhỏ chỉ điều chỉnh mô hình quanh vùng tham số đã học thay vì bắt đầu từ random initialization.

Điều này hoạt động giống một **prior học từ dữ liệu** và thay đổi mạnh bài toán bias–variance.

## Parameter-Efficient Fine-Tuning

LoRA giới hạn update:

\[
\Delta W=BA
\]

với rank nhỏ `r`:

\[
A\in R^{r\times d_{in}},
B\in R^{d_{out}\times r}
\]

Thay vì cho `ΔW` thay đổi hoàn toàn tự do, update bị giới hạn vào low-rank subspace.

Điều này giảm memory và đôi khi cũng giúp hạn chế overfitting khi dữ liệu fine-tuning nhỏ.

## Regularization và Memorization

Neural Network đủ lớn có thể ghi nhớ cả nhãn ngẫu nhiên, cho thấy model capacity tự nó không ép mô hình phải generalize.

Generalization trên dữ liệu tự nhiên đến từ sự kết hợp giữa cấu trúc dữ liệu, optimization bias, regularization, augmentation và quy mô.

Memorization và generalization cũng có thể cùng tồn tại: mô hình có thể ghi nhớ một số example hiếm nhưng vẫn khái quát hóa tốt ở phần lớn distribution.

## Regularization dưới Distribution Shift

Một kỹ thuật giúp IID test tốt hơn không nhất thiết giúp robustness khi domain thay đổi.

Augmentation được thiết kế đúng với loại shift dự kiến có thể hữu ích hơn một weight decay chung chung.

Robustness phải được đánh giá trực tiếp trên shifted hoặc stress distribution.

## Mô hình tư duy

> Regularization là một preference: trong rất nhiều cấu hình tham số có thể fit training data, ta muốn quá trình học ưu tiên những nghiệm đơn giản hơn, ổn định hơn, bất biến phù hợp hơn hoặc gần một prior hữu ích hơn.

## Các hiểu lầm thường gặp

### “Regularization càng mạnh càng ít overfit nên càng tốt”

Không. Quá mạnh sẽ gây underfitting hoặc làm mất adaptation hữu ích cho task.

### “Dropout bắt buộc phải có trong mọi Neural Network”

Không. Nhu cầu phụ thuộc dataset, architecture và chế độ training.

### “Data augmentation chỉ để tăng số sample”

Không. Vai trò quan trọng hơn là mã hóa invariance.

### “Weight decay làm model sparse”

Không theo nghĩa tạo nhiều giá trị đúng bằng 0. L2/weight decay chủ yếu thu nhỏ magnitude; L1 hoặc structured pruning phù hợp hơn nếu mục tiêu là sparsity.

### “Fine-tuning ít tham số chỉ để tiết kiệm VRAM”

Không. Việc giới hạn không gian update cũng làm thay đổi inductive bias và đôi khi giảm overfitting.

## Liên kết kiến thức

Xem [Bias–Variance và Generalization](../04_machine_learning/14_bias_variance_and_generalization.md), [AdamW](./05_gradient_descent_and_optimizers.md), [Initialization và Normalization](./06_initialization_and_normalization.md), và tiếp theo [Representation Learning](./08_representation_learning.md).