# Hàm kích hoạt: vì sao Neural Network cần tính phi tuyến?

**Hàm kích hoạt (Activation Function / 활성화 함수)** thường được giới thiệu như một danh sách `sigmoid`, `tanh`, `ReLU`, `GELU`. Nếu chỉ học như vậy, kiến thức rất dễ biến thành ghi nhớ tên hàm. Bản chất sâu hơn là: activation quyết định **hình dạng của phép biến đổi**, **dòng gradient (gradient flow)** và **đặc tính thống kê của hidden representation**.

Nếu bỏ activation giữa các affine layer, toàn bộ network có thể rút gọn thành một phép biến đổi affine duy nhất. Vì vậy tính phi tuyến là điều kiện để độ sâu tạo ra khả năng biểu diễn mới.

## Identity activation

\[
\phi(z)=z
\]

Hàm đồng nhất không tạo thêm tính phi tuyến.

Nó vẫn hữu ích ở output của regression hoặc trong một số residual/projection block, nhưng nếu mọi hidden layer đều dùng identity thì mạng sâu vẫn chỉ tương đương một mô hình tuyến tính.

## Sigmoid

\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]

Đầu ra nằm trong `(0,1)`.

Đạo hàm:

\[
\sigma'(z)=\sigma(z)(1-\sigma(z))
\]

Giá trị đạo hàm lớn nhất chỉ `0.25`; khi `|z|` lớn, đạo hàm tiến gần 0. Hiện tượng này gọi là **bão hòa (saturation)** và có thể gây **gradient biến mất (vanishing gradient)** khi mạng sâu.

Sigmoid vẫn rất phù hợp cho đầu ra xác suất nhị phân hoặc các cổng trong LSTM, nơi giá trị bị giới hạn trong `(0,1)` có ý nghĩa rõ ràng.

## tanh

\[
tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
\]

Đầu ra nằm trong `(-1,1)` và có tâm quanh 0 tốt hơn sigmoid.

Đạo hàm:

\[
1-tanh^2(z)
\]

Tuy nhiên tanh vẫn bão hòa khi giá trị tuyệt đối lớn.

Trong lịch sử, tanh thường dễ train hơn sigmoid ở hidden layer của nhiều mạng đời đầu, nhưng họ ReLU sau này thuận lợi hơn cho nhiều feed-forward network sâu.

## ReLU

\[
ReLU(z)=\max(0,z)
\]

Đạo hàm:

\[
ReLU'(z)=
\begin{cases}
0,&z<0\\
1,&z>0
\end{cases}
\]

Tại `z=0`, convention đạo hàm phụ thuộc implementation, nhưng một điểm đơn lẻ thường không gây vấn đề lớn trong training liên tục.

Các ưu điểm chính của ReLU gồm không bão hòa ở phía dương, tính toán đơn giản, tạo activation thưa và giúp gradient đi qua tốt hơn sigmoid/tanh trong nhiều mạng sâu.

## Dying ReLU

Nếu một unit rơi vào vùng `z<0` đối với hầu hết input, gradient qua ReLU bằng 0 và unit có thể không phục hồi được.

Hiện tượng này gọi là **Dying ReLU**.

Learning rate quá lớn hoặc initialization không phù hợp làm rủi ro tăng lên.

Một số biến thể:

**Leaky ReLU**:

\[
\phi(z)=\max(\alpha z,z)
\]

cho một slope âm nhỏ.

**PReLU** học trực tiếp `α`.

**ELU** và **SELU** dùng vùng âm mượt với các mục tiêu khác về thống kê activation.

## GELU

**Gaussian Error Linear Unit (GELU)** phổ biến trong Transformer:

\[
GELU(x)=x\Phi(x)
\]

với `Φ` là CDF của phân phối chuẩn chuẩn hóa.

Trực giác đơn giản là GELU “gating” input một cách mượt dựa trên độ lớn thay vì cắt cứng phần âm như ReLU.

Một xấp xỉ thường gặp:

\[
0.5x\left(1+tanh\left[\sqrt{2/\pi}(x+0.044715x^3)\right]\right)
\]

Nhiều Transformer hiện đại cũng dùng SiLU hoặc SwiGLU.

## SiLU / Swish

\[
SiLU(x)=x\sigma(x)
\]

SiLU là hàm mượt, có một vùng âm hơi không đơn điệu và xuất hiện trong nhiều kiến trúc hiện đại.

## Gated Linear Unit và SwiGLU

Feed-forward block của Transformer hiện đại thường sử dụng activation có cơ chế cổng:

\[
SwiGLU(x)=(xW_1)\odot SiLU(xW_2)
\]

sau đó mới qua projection tiếp theo.

Cơ chế gating cho phép tương tác nhân giữa nhiều projection được học, làm representation linh hoạt hơn so với chỉ dùng một activation scalar đơn giản.

## Softmax không phải hidden activation thông thường

Softmax:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

biến vector logit thành một phân phối có tổng bằng 1.

Nó thường được dùng ở output của multiclass classification hoặc để tạo attention weight, chứ không phải hidden activation tổng quát như ReLU hay GELU.

Softmax còn có tính liên kết giữa các chiều: thay một logit sẽ ảnh hưởng xác suất của tất cả class còn lại.

## Activation và dòng gradient

Backpropagation qua nhiều layer tạo tích của nhiều đạo hàm:

\[
\frac{\partial L}{\partial h^{(l)}}=
\frac{\partial L}{\partial h^{(l+1)}}
\frac{\partial h^{(l+1)}}{\partial h^{(l)}}
\]

Nếu các đạo hàm liên tục nhỏ hơn 1 đáng kể, gradient có thể co lại qua chiều sâu. Nếu norm của Jacobian liên tục lớn hơn 1, gradient có thể bùng nổ.

Vì vậy activation không thể được đánh giá riêng lẻ. Nó tương tác trực tiếp với initialization, normalization, residual connection và toàn bộ architecture.

## Output activation phải phù hợp target

Một số lựa chọn thường gặp:

```text
Regression không bị chặn        → thường dùng identity
Binary classification           → sigmoid hoặc logits + BCE-with-logits
Multiclass loại trừ lẫn nhau    → softmax
Multi-label                     → sigmoid độc lập cho từng label
Đại lượng dương                 → có thể dùng softplus / exponential
Tham số variance phải > 0       → softplus thường hữu ích
```

Activation ở output layer chính là một giả định mô hình hóa, không chỉ là chi tiết implementation.

## Có bắt buộc khả vi ở mọi điểm không?

Gradient-based training cần đạo hàm hữu ích gần như mọi nơi, nhưng hàm không cần khả vi tuyệt đối tại mọi điểm đơn lẻ. ReLU là ví dụ điển hình.

Các phép toán rời rạc như `argmax` thường không khả vi, nên thường được đặt ngoài đường training hoặc xử lý bằng relaxation hay estimator đặc biệt.

## Thống kê activation

Nếu mean và variance của activation liên tục trôi khi đi qua nhiều layer, optimization trở nên khó hơn.

Initialization và normalization cố giữ scale của tín hiệu ở mức hợp lý.

SELU từng được thiết kế để activation statistics có xu hướng hội tụ về một vùng ổn định dưới các giả định nhất định.

Transformer hiện đại thường dựa vào LayerNorm hoặc RMSNorm kết hợp residual path để kiểm soát dòng tín hiệu.

## Vì sao ReLU từng là bước tiến quan trọng?

ReLU không phải nguyên nhân duy nhất làm Deep Learning phát triển, nhưng cùng với initialization tốt hơn và GPU, nó giúp giảm vấn đề saturation trong feed-forward network và CNN sâu.

Tiến bộ lịch sử thường đến từ sự kết hợp của nhiều cải tiến, không phải một “activation thần kỳ” duy nhất.

## Mô hình tư duy

> Hàm kích hoạt là cơ chế điều khiển hình dạng của phép biến đổi được học: nó quyết định layer có thể bẻ cong representation space ra sao và gradient truyền qua phép biến đổi đó như thế nào.

## Các hiểu lầm thường gặp

### “ReLU tốt nhất nên cứ dùng ReLU”

Không. Kiến trúc và domain quyết định lựa chọn. Transformer thường dùng GELU, SiLU hoặc SwiGLU; các cổng RNN lại dùng sigmoid/tanh.

### “Sigmoid đã lỗi thời”

Không. Nó vẫn tự nhiên cho Bernoulli output và cơ chế gating.

### “Softmax làm mô hình tự tin hơn”

Không. Softmax chỉ chuẩn hóa logit; scale và temperature ảnh hưởng độ sắc của phân phối, nhưng không bảo đảm correctness hay calibration.

### “Activation chỉ ảnh hưởng expressivity”

Không. Nó còn ảnh hưởng optimization, gradient flow, activation statistics và numerical stability.

## Liên kết kiến thức

Xem [Giải tích](../01_mathematical_foundations/04_calculus_for_ai.md), [Tính toán số](../01_mathematical_foundations/07_numerical_computation.md) và [Initialization và Normalization](./06_initialization_and_normalization.md).

Xem tiếp: [Lan truyền tiến](./03_forward_propagation.md).