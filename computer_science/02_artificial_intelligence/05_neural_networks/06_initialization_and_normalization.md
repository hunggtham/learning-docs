# Initialization và Normalization: giữ tín hiệu và gradient ở vùng dễ huấn luyện

Một mạng sâu có thể có architecture đúng nhưng training vẫn thất bại ngay từ đầu nếu activation hoặc gradient bùng nổ hay biến mất qua nhiều layer. **Khởi tạo (Initialization / 초기화)** chọn phân phối ban đầu của tham số; **chuẩn hóa bên trong mạng (Normalization / 정규화)** kiểm soát thống kê của representation trung gian trong quá trình training.

Hai nhóm kỹ thuật này giải quyết một vấn đề hệ thống cốt lõi: làm thế nào để tín hiệu đi qua rất nhiều phép biến đổi mà vẫn nằm trong scale hợp lý cho tính toán số và tối ưu hóa?

## Vì sao không khởi tạo mọi trọng số bằng 0?

Nếu các neuron trong cùng layer bắt đầu với trọng số giống hệt nhau, chúng nhận cùng gradient và tiếp tục học giống nhau.

Ta cần **phá vỡ đối xứng (symmetry breaking)** bằng random initialization để các unit có thể học những hàm khác nhau.

Bias có thể khởi tạo bằng 0 vì chính weight ngẫu nhiên đã phá vỡ đối xứng.

## Lan truyền phương sai

Giả sử:

\[
z=\sum_{i=1}^{n}w_ix_i
\]

với các biến gần độc lập và có mean bằng 0:

\[
Var(z)\approx nVar(w)Var(x)
\]

Nếu `Var(w)` không được scale theo fan-in `n`, phương sai của activation có thể tăng hoặc giảm nhanh theo depth.

Initialization tốt cố giữ phương sai của tín hiệu forward và gradient backward tương đối ổn định qua các layer.

## Xavier / Glorot Initialization

Phù hợp hơn với activation đối xứng kiểu tanh hoặc sigmoid:

\[
Var(w)\approx\frac{2}{fan_{in}+fan_{out}}
\]

Một dạng uniform thường gặp:

\[
w\sim U\left(-\sqrt{\frac{6}{fan_{in}+fan_{out}}},
\sqrt{\frac{6}{fan_{in}+fan_{out}}}\right)
\]

Mục tiêu là cân bằng scale của tín hiệu cả ở chiều forward lẫn backward.

## He / Kaiming Initialization

Với ReLU, dưới giả định đối xứng, khoảng một nửa activation bị cắt về 0 nên thường dùng variance lớn hơn:

\[
Var(w)\approx\frac{2}{fan_{in}}
\]

Một dạng khởi tạo chuẩn:

\[
w\sim\mathcal N(0,2/fan_{in})
\]

Hệ số cụ thể cần phù hợp với activation được sử dụng.

## Initialization phụ thuộc architecture

Residual Network, Transformer, gated block và normalization layer làm thay đổi dynamics của tín hiệu.

Các recipe cho mô hình lớn có thể dùng residual scaling, initialization riêng cho từng branch hoặc các cách tham số hóa như μ-parameterization.

Vì vậy không có một công thức khởi tạo duy nhất phù hợp cho mọi architecture.

## Batch Normalization

BatchNorm chuẩn hóa activation theo feature hoặc channel bằng thống kê của mini-batch:

\[
\mu_B=\frac1m\sum_i x_i
\]

\[
\sigma_B^2=\frac1m\sum_i(x_i-\mu_B)^2
\]

\[
\hat x_i=\frac{x_i-\mu_B}{\sqrt{\sigma_B^2+\epsilon}}
\]

sau đó học scale và shift affine:

\[
y_i=\gamma\hat x_i+\beta
\]

`γ` và `β` cho phép mô hình khôi phục scale hoặc offset hữu ích thay vì bị ép cố định ở mean 0 và variance 1.

## BatchNorm giúp gì?

Giải thích lịch sử thường nhấn mạnh việc giảm “internal covariate shift”, nhưng cách hiểu hiện đại rộng hơn.

BatchNorm giúp ổn định scale activation, làm bài toán tối ưu dễ hơn trong nhiều trường hợp, cho phép learning rate lớn hơn, thêm nhiễu phụ thuộc batch như một dạng regularization và giảm độ nhạy với initialization.

Không nên coi một giải thích duy nhất là nguyên nhân đầy đủ cho toàn bộ hiệu quả của BatchNorm.

## Training và Evaluation trong BatchNorm

Khi training, BatchNorm dùng thống kê của batch hiện tại và cập nhật running estimate.

Khi evaluation, nó dùng running mean và running variance.

Batch quá nhỏ làm estimate nhiễu. SyncBatchNorm có thể tổng hợp thống kê trên nhiều thiết bị nhưng tăng chi phí communication.

Nếu deployment distribution thay đổi, running statistics cũ cũng có thể làm chất lượng giảm.

## Layer Normalization

LayerNorm chuẩn hóa theo các chiều feature của từng sample hoặc token:

\[
\mu=\frac1D\sum_{j=1}^{D}x_j
\]

\[
\sigma^2=\frac1D\sum_j(x_j-\mu)^2
\]

Nó không phụ thuộc batch size theo cách BatchNorm phụ thuộc, nên đặc biệt phù hợp với sequence model và Transformer.

Một hidden state `x∈R^D` của Transformer thường được normalize riêng cho từng token.

## RMSNorm

RMSNorm bỏ bước trừ mean, chỉ scale bằng root mean square:

\[
RMS(x)=\sqrt{\frac1D\sum_jx_j^2+\epsilon}
\]

\[
y=\gamma\odot\frac{x}{RMS(x)}
\]

Nó đơn giản, hiệu quả và được dùng rộng rãi trong nhiều LLM hiện đại.

## GroupNorm và InstanceNorm

**GroupNorm** chia channel thành nhiều nhóm rồi normalize bên trong từng nhóm. Nó ít phụ thuộc batch statistics và hữu ích khi batch ảnh nhỏ.

**InstanceNorm** chuẩn hóa theo từng sample/channel và xuất hiện nhiều trong style transfer hoặc image generation.

Việc chọn axis để normalize chính là một quyết định mô hình hóa.

## Pre-Norm và Post-Norm trong Transformer

Post-Norm cổ điển:

\[
y=LN(x+F(x))
\]

Pre-Norm:

\[
y=x+F(LN(x))
\]

Pre-Norm giữ đường residual identity rõ hơn cho gradient và thường làm Transformer sâu dễ train ổn định hơn, vì vậy được dùng rộng rãi.

Vị trí normalization trong architecture có ảnh hưởng rất lớn tới optimization.

## Normalization bên trong mạng khác chuẩn hóa input

Standardization input là bước preprocessing dựa trên thống kê dataset.

BatchNorm và LayerNorm là module khả vi nằm **bên trong** network, có tham số học được và được áp dụng lặp lại ở nhiều layer.

Hai ý tưởng có liên quan nhưng phạm vi và hành vi hoàn toàn khác nhau.

## Epsilon và ổn định số

Mẫu số thêm `ε`:

\[
\sqrt{\sigma^2+\epsilon}
\]

để tránh chia cho 0 và giữ computation ổn định khi variance rất nhỏ.

Giá trị epsilon có thể ảnh hưởng rõ trong low precision.

Normalization kernel thường tích lũy thống kê ở precision cao hơn input dtype để giảm sai số.

## Weight Normalization và Spectral Normalization

Không phải mọi normalization đều tác động lên activation.

WeightNorm tái tham số hóa weight thành direction và magnitude.

Spectral Normalization giới hạn singular value lớn nhất, giúp kiểm soát Lipschitz behavior và từng được dùng nhiều trong GAN discriminator.

Vì vậy Normalization là một họ kỹ thuật rộng, không chỉ BatchNorm.

## Tương tác với Regularization

Nhiễu từ BatchNorm có thể tạo implicit regularization. Tương tác giữa Dropout và BatchNorm đôi khi phức tạp.

Weight decay cũng thường không được áp dụng giống nhau cho bias hoặc scale của normalization layer trong optimizer config hiện đại.

Training recipe cần được xem như một hệ thống hoàn chỉnh thay vì tuning từng “mẹo” tách rời.

## Debug thống kê tín hiệu

Nên theo dõi theo từng layer:

```text
mean/std của activation
min/max của activation
tỷ lệ activation bằng 0
gradient norm
parameter norm
tỷ lệ update / parameter
```

Nếu standard deviation tăng theo cấp số nhân qua depth, tín hiệu đang bùng nổ. Nếu co dần về gần 0, có thể đang xảy ra vanishing hoặc dead unit.

## Mô hình tư duy

```text
Initialization = chọn scale khởi đầu để mạng bắt đầu trong vùng trainable
Normalization  = giữ scale/thống kê trung gian trong vùng dễ tối ưu
Residual path  = tạo đường truyền tín hiệu và gradient ổn định
```

## Các hiểu lầm thường gặp

### “Random small weights là đủ”

Không. Scale phải phụ thuộc fan-in, activation và architecture. Trọng số quá nhỏ cũng có thể gây vanishing.

### “BatchNorm và LayerNorm giống nhau, chỉ khác tên”

Không. Axis thống kê và hành vi train/eval khác nhau về bản chất.

### “Có Normalization thì không cần initialization tốt”

Không. Normalization giảm độ nhạy nhưng initialization vẫn ảnh hưởng early dynamics và độ ổn định của mô hình lớn hoặc rất sâu.

### “LayerNorm làm token mất thông tin vì mean=0, variance=1”

Không. Direction, pattern tương đối, learned affine parameter và residual stream vẫn mang thông tin.

## Liên kết kiến thức

Xem [Hàm kích hoạt](./02_activation_functions.md), [Backpropagation](./04_backpropagation.md), [Optimizer](./05_gradient_descent_and_optimizers.md) và sau này [Transformer](../06_deep_learning_architectures/05_transformer.md).