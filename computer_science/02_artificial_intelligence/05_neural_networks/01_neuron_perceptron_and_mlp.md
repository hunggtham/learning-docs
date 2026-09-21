# Neuron, Perceptron và Multi-Layer Perceptron

**Neuron nhân tạo (artificial neuron)** là một khối tính toán đơn giản: nhận vector đầu vào, tính tổng có trọng số, cộng bias rồi đưa kết quả qua hàm kích hoạt. Tuy nhiên để hiểu Neural Network đúng bản chất, cần phân biệt rõ **Perceptron**, **neuron hiện đại**, **mạng một layer** và **Multi-Layer Perceptron (MLP / 다층 퍼셉트론)**.

## Neuron nhân tạo

Một unit có dạng:

\[
z=\mathbf w^T\mathbf x+b
\]

\[
a=\phi(z)
\]

Trong đó `w` quyết định hướng và độ nhạy của phép đo tuyến tính, `b` dịch ngưỡng, còn `φ` tạo tính phi tuyến.

Nếu `φ` là hàm đồng nhất, unit chỉ còn là một thành phần tuyến tính giống Linear Regression. Nếu dùng sigmoid, hành vi giống Logistic Regression. Nếu dùng ReLU, đầu ra bằng 0 với pre-activation âm và tăng tuyến tính với phần dương.

## Perceptron lịch sử

Perceptron nhị phân dùng activation dạng threshold hoặc sign:

\[
\hat y=sign(\mathbf w^T\mathbf x+b)
\]

Quy tắc học trong dạng đơn giản cập nhật khi mẫu bị phân loại sai:

\[
\mathbf w\leftarrow \mathbf w+\eta y\mathbf x
\]

với nhãn `y∈{-1,+1}`.

**Perceptron Convergence Theorem** nói rằng nếu dữ liệu có thể phân tách tuyến tính, thuật toán sẽ hội tụ sau hữu hạn số lỗi.

Tuy nhiên XOR không phân tách tuyến tính được, nên một perceptron đơn lẻ không thể giải bài toán đó. Hạn chế này là một trong những động lực dẫn tới mạng nhiều layer.

## Một layer dưới dạng ma trận

Thay vì một neuron, một layer có thể có `m` unit:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

với:

\[
W\in\mathbb R^{m\times d}
\]

Sau activation:

\[
\mathbf h=\phi(\mathbf z)
\]

Mỗi hàng của `W` là weight vector của một unit.

GPU có thể tính hàng nghìn unit song song bằng matrix multiplication, đây là một trong các lý do Neural Network phù hợp rất tốt với accelerator hiện đại.

## Multi-Layer Perceptron

MLP xếp chồng nhiều fully connected layer:

\[
h^{(1)}=\phi(W^{(1)}x+b^{(1)})
\]

\[
h^{(2)}=\phi(W^{(2)}h^{(1)}+b^{(2)})
\]

\[
\hat y=g(W^{(3)}h^{(2)}+b^{(3)})
\]

Các hidden layer không có target riêng trực tiếp. Representation bên trong được định hình bởi loss cuối thông qua backpropagation.

## Hidden unit đang học gì?

Không nên giả định mỗi hidden unit tương ứng một khái niệm rõ ràng như “mắt mèo” hay “bánh xe”.

Representation thường mang tính phân tán. Một hidden vector `h` có thể mã hóa nhiều yếu tố thông qua direction hoặc subspace, còn layer sau kết hợp chúng thành feature bậc cao hơn.

Muốn diễn giải hidden unit cần phân tích thực nghiệm; không thể suy ý nghĩa chỉ từ vị trí neuron trong layer.

## Output layer phụ thuộc task

Với binary classification, hệ thống thường dùng một logit + sigmoid hoặc hai logit + softmax.

Với multiclass classification:

\[
\mathbf p=softmax(Wh+b)
\]

Với regression, output có thể tuyến tính.

Với **multi-label classification**, mỗi label thường dùng sigmoid độc lập thay vì softmax vì nhiều label có thể đồng thời đúng.

Activation và loss ở output layer phải phù hợp với cấu trúc xác suất của target.

## Chiều batch

Trong thực tế, input thường là batch:

\[
X\in\mathbb R^{B\times d}
\]

Forward pass:

\[
Z=XW^T+b
\]

Bias được broadcast qua `B` sample.

Khả năng suy luận đúng shape của tensor là kỹ năng rất quan trọng khi implement Neural Network. Nhiều lỗi không nằm ở công thức mà nằm ở việc hiểu sai ý nghĩa của một axis.

## Đếm số tham số

Một fully connected layer từ `d_in` tới `d_out` có:

\[
d_{in}d_{out}+d_{out}
\]

tham số.

Nếu ảnh `224×224×3` được flatten trực tiếp thành khoảng 150 nghìn feature rồi nối với 4.096 hidden unit, chỉ layer đầu đã cần hơn 600 triệu tham số.

Đây là lý do CNN dùng locality và weight sharing thay vì dense MLP cho ảnh.

Kiến trúc phải phản ánh cấu trúc của modality.

## MLP cho dữ liệu bảng

MLP có thể xử lý tabular data, nhưng Gradient Boosted Tree vẫn rất cạnh tranh khi dataset có quy mô vừa và feature dị thể.

Neural model thường có lợi thế hơn khi dữ liệu rất lớn, cần embedding học được cho category, input đa phương thức, cần end-to-end representation learning hoặc tận dụng transfer/pretraining.

Không nên chọn MLP chỉ vì “Deep Learning hiện đại hơn”.

## Vùng quyết định

ReLU MLP tạo hàm dạng **tuyến tính từng đoạn (piecewise-linear)**.

Mỗi pattern ReLU bật/tắt xác định một vùng cục bộ nơi toàn mạng hoạt động như một phép biến đổi tuyến tính.

Khi depth tăng, số vùng tuyến tính có thể tăng rất lớn, giúp mạng biểu diễn ranh giới quyết định phức tạp dù từng phép toán cơ bản rất đơn giản.

## Bias term là gì?

Bias `b` không phải statistical bias hay social bias. Nó tương tự intercept: cho phép ngưỡng activation dịch khỏi gốc tọa độ.

Nếu không có bias, các hyperplane kiểu `Wx=0` đều buộc đi qua origin, làm giảm khả năng biểu diễn.

## Kết nối dày đặc và kết nối thưa

MLP chuẩn là **fully connected**: mỗi output unit nhận toàn bộ hidden vector của layer trước.

Nhưng nhiều kiến trúc khác dùng kết nối cục bộ, thưa, hồi quy hoặc attention.

Neural Network không đồng nghĩa với fully connected network.

## Perceptron và Logistic Neuron

Perceptron dùng hard threshold, không khả vi tại boundary và không cung cấp gradient thuận lợi cho backpropagation.

Sigmoid, ReLU và GELU cung cấp hàm khả vi hoặc khả vi gần như mọi nơi, phù hợp với gradient-based training.

Vì vậy mạng hiện đại hầu như không được train bằng perceptron rule cổ điển.

## Ví dụ XOR qua hidden representation

Một MLP có thể học các hidden feature đại diện cho những vùng khác nhau, sau đó layer cuối kết hợp chúng.

Về mặt khái niệm:

```text
(x1, x2)
  ↓ feature phi tuyến được học
[feature gần giống x1 OR x2,
 feature gần giống x1 AND x2]
  ↓ kết hợp
XOR
```

Không cần tự viết chính xác các feature logic; quá trình training có thể tìm representation trung gian hữu ích.

## Mô hình tư duy

```text
Neuron = phép đo tuyến tính + phản ứng phi tuyến
Layer  = nhiều phép đo được học đồng thời
MLP    = chuỗi phép biến đổi representation
```

Hidden layer không phải “các bước reasoning” theo nghĩa symbolic; chúng là những phép biến đổi số được học.

## Các hiểu lầm thường gặp

### “Mỗi neuron là một feature có ý nghĩa rõ ràng”

Không nhất thiết. Có thể tồn tại unit chuyên biệt, nhưng thông tin thường được phân tán trên nhiều dimension.

### “Perceptron và Neural Network hiện đại là cùng một thuật toán”

Không. Perceptron là learner tuyến tính với threshold lịch sử; mạng hiện đại dùng nhiều layer khả vi, backpropagation và optimizer.

### “Bias neuron gây model bias”

Không. Bias term chỉ là affine offset và không trực tiếp liên quan fairness bias.

### “MLP là universal nên không cần CNN hay Transformer”

Khả năng biểu diễn về lý thuyết không thay thế hiệu quả dữ liệu, compute và inductive bias. Kiến trúc chuyên biệt học cấu trúc phù hợp nhanh và tiết kiệm hơn.

## Liên kết kiến thức

Xem lại [Đại số tuyến tính](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [Từ mô hình tuyến tính tới Neural Network](./00_from_linear_models_to_neural_networks.md).

Xem tiếp: [Hàm kích hoạt](./02_activation_functions.md), phần quyết định việc hợp thành nhiều layer có thật sự tạo tính phi tuyến và dễ huấn luyện hay không.