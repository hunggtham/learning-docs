# Backpropagation: Chain Rule trên đồ thị tính toán

**Backpropagation (역전파 / lan truyền ngược)** thường bị mô tả đơn giản là “thuật toán giúp Neural Network học”. Chính xác hơn, đây là một **thuật toán hiệu quả để tính gradient của một đầu ra vô hướng, thường là loss, đối với rất nhiều giá trị trung gian và tham số trong computation graph**.

Quá trình học vẫn cần optimizer sử dụng gradient để cập nhật tham số. Backpropagation chỉ trả lời câu hỏi:

> Nếu một tham số thay đổi rất nhỏ, loss sẽ thay đổi theo hướng nào và với mức độ bao nhiêu?

## Bắt đầu từ Chain Rule

Nếu:

\[
y=f(u),\qquad u=g(x)
\]

thì:

\[
\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}
\]

Neural Network chỉ là một phép hợp thành lớn hơn:

\[
L=f_L(f_{L-1}(...f_1(x)))
\]

Backpropagation áp dụng Chain Rule theo thứ tự topo ngược của computation graph.

## Một ví dụ vô hướng

Giả sử:

\[
z=wx+b
\]

\[
\hat y=\sigma(z)
\]

\[
L=\frac12(\hat y-y)^2
\]

Muốn tính gradient theo `w`:

\[
\frac{\partial L}{\partial w}
=\frac{\partial L}{\partial \hat y}
\frac{\partial \hat y}{\partial z}
\frac{\partial z}{\partial w}
\]

Từng thành phần:

\[
\frac{\partial L}{\partial \hat y}=\hat y-y
\]

\[
\frac{\partial \hat y}{\partial z}=\sigma(z)(1-\sigma(z))
\]

\[
\frac{\partial z}{\partial w}=x
\]

nên:

\[
\frac{\partial L}{\partial w}=(\hat y-y)\sigma(z)(1-\sigma(z))x
\]

Không có một cơ chế bí ẩn nào ở đây. Đây chỉ là Chain Rule được áp dụng xuyên qua các phép toán đã chạy trong forward pass.

## Reverse-Mode Automatic Differentiation

Nếu mô hình có hàng triệu tham số nhưng chỉ một scalar loss, ta cần:

\[
\frac{\partial L}{\partial \theta_1},...,
\frac{\partial L}{\partial \theta_m}
\]

**Reverse-mode Automatic Differentiation** rất hiệu quả cho cấu trúc này vì một lần duyệt backward có thể tính gradient cho toàn bộ tham số với chi phí cùng bậc với forward pass, thường chỉ vài lần chi phí forward chứ không cần `m` lần chạy riêng.

Backpropagation trong Neural Network chính là một ứng dụng đặc biệt của reverse-mode automatic differentiation.

## Gradient cục bộ và gradient từ phía sau

Mỗi operation chỉ cần biết hai thứ:

1. đạo hàm cục bộ của output theo input;
2. gradient đã được truyền tới từ downstream.

Ví dụ với:

\[
z=a+b
\]

thì:

\[
\frac{\partial z}{\partial a}=1,\qquad \frac{\partial z}{\partial b}=1
\]

Nếu gradient từ phía sau là:

\[
\bar z=\frac{\partial L}{\partial z}
\]

thì:

\[
\bar a=\bar z,
\qquad
\bar b=\bar z
\]

Với phép nhân `z=ab`:

\[
\bar a=\bar z\cdot b,
\qquad
\bar b=\bar z\cdot a
\]

Autograd framework chỉ cần ghép nối hàng nghìn quy tắc đạo hàm cục bộ kiểu này.

## Graph phân nhánh và tích lũy gradient

Nếu một tensor ảnh hưởng loss qua nhiều đường:

\[
L=f(x)+g(x)
\]

thì:

\[
\frac{dL}{dx}=f'(x)+g'(x)
\]

Backward pass phải **cộng gradient từ tất cả đường downstream**.

Đây là lý do framework tích lũy gradient. Trong PyTorch, nếu gọi `.backward()` nhiều lần mà không reset gradient, các giá trị sẽ cộng dồn — đôi khi là lỗi, đôi khi lại được dùng có chủ đích cho gradient accumulation qua nhiều mini-batch.

## Cách nhìn qua Jacobian

Nếu:

\[
y=f(x)
\]

với `x` và `y` là vector, đạo hàm là Jacobian:

\[
J_{ij}=\frac{\partial y_i}{\partial x_j}
\]

Nhưng Backpropagation không cần tạo ra toàn bộ ma trận Jacobian khổng lồ.

Nó tính **vector-Jacobian product (VJP)** một cách hiệu quả.

Nếu gradient từ phía sau là:

\[
v=\frac{\partial L}{\partial y}
\]

thì backward cần:

\[
v^TJ
\]

mà không cần materialize `J` đầy đủ.

Đây là lý do reverse-mode AD khả thi về memory và compute cho mô hình lớn.

## Backprop qua Linear Layer

Với batch:

\[
Z=XW^T+b
\]

và gradient từ downstream:

\[
G_Z=\frac{\partial L}{\partial Z}
\]

thì:

\[
\frac{\partial L}{\partial W}=G_Z^TX
\]

\[
\frac{\partial L}{\partial X}=G_ZW
\]

\[
\frac{\partial L}{\partial b}=\sum_{batch}G_Z
\]

Toàn bộ đều là matrix multiplication và reduction, đây là một lý do GPU rất phù hợp cho cả forward lẫn backward.

## Backprop qua hàm kích hoạt

Với activation theo từng phần tử:

\[
h=\phi(z)
\]

thì:

\[
\frac{\partial L}{\partial z}
=rac{\partial L}{\partial h}\odot\phi'(z)
\]

Nếu `φ'(z)` thường rất gần 0, gradient sẽ co lại. Đây là kết nối trực tiếp tới vanishing gradient.

## Sigmoid + Cross-Entropy

Với sigmoid:

\[
p=\sigma(z)
\]

và Binary Cross-Entropy:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

đạo hàm rút gọn thành:

\[
\frac{\partial L}{\partial z}=p-y
\]

Softmax + Cross-Entropy cho multiclass cũng có dạng tương tự:

\[
\frac{\partial L}{\partial z_k}=p_k-y_k
\]

Sự rút gọn này làm gradient và implementation số học thuận lợi hơn so với việc xử lý từng khối một cách ngây thơ.

## Vanishing Gradient

Gradient đi qua nhiều layer là tích của nhiều Jacobian:

\[
\frac{\partial L}{\partial h^{(l)}}
=J_{l+1}^TJ_{l+2}^T...J_L^T
\frac{\partial L}{\partial h^{(L)}}
\]

Nếu norm của các Jacobian thường nhỏ hơn 1, tích này co rất nhanh theo chiều sâu. Các layer đầu nhận tín hiệu gradient cực nhỏ.

Sigmoid và tanh khi bão hòa làm vấn đề này nặng hơn.

Các hướng khắc phục trong lịch sử gồm ReLU, Xavier/He initialization, normalization, residual connection và kiến trúc có cơ chế gating.

## Exploding Gradient

Nếu norm của Jacobian liên tục lớn hơn 1, gradient có thể bùng nổ.

Dấu hiệu thường gặp gồm loss thành NaN/Inf, parameter update quá lớn hoặc training dao động mạnh.

Các biện pháp gồm initialization phù hợp, normalization, learning rate nhỏ hơn và gradient clipping.

Gradient norm clipping:

\[
g\leftarrow g\cdot\min\left(1,\frac{c}{\|g\|}\right)
\]

giới hạn norm của gradient ở mức `c`.

## Residual Connection như một đường cao tốc cho gradient

Residual block:

\[
y=x+F(x)
\]

có đạo hàm:

\[
\frac{\partial y}{\partial x}=I+\frac{\partial F}{\partial x}
\]

Thành phần identity tạo một đường gradient trực tiếp, giúp mạng rất sâu dễ huấn luyện hơn.

ResNet và Transformer đều tận dụng nguyên lý này.

## Gradient Checkpointing

Backward pass cần activation từ forward. Với mô hình lớn, lưu tất cả activation rất tốn memory.

Checkpointing chỉ giữ lại một số mốc, còn các đoạn thiếu sẽ được tính lại khi backward cần.

Sự đánh đổi:

```text
ít memory hơn
↔
nhiều compute hơn
```

Đây là hệ quả hệ thống trực tiếp từ dependency của Backpropagation.

## Stop Gradient / Detach

Đôi khi ta muốn một giá trị tham gia forward pass nhưng không nhận gradient.

`detach` hoặc stop-gradient tạo một ranh giới trong computation graph.

Các trường hợp sử dụng gồm target network, contrastive learning, teacher–student setup hoặc ngăn một nhóm parameter bị update ngoài ý muốn.

Dùng sai `detach` có thể làm learning bị ngắt mà không tạo lỗi rõ ràng.

## Gradient bậc cao

Backpropagation thường tính gradient bậc nhất.

Một số thuật toán cần gradient của gradient, Hessian-vector product hoặc derivative trong meta-learning.

Framework có thể tạo graph cho chính backward computation khi được cấu hình, nhưng chi phí memory và compute tăng mạnh.

## Backpropagation không phải mô hình sinh học của não

Backpropagation là thuật toán tối ưu tính toán, không phải mô hình đã được chứng minh về cách não sinh học học.

Có các nghiên cứu về cơ chế gần sinh học hơn, nhưng thành công engineering của Backpropagation không chứng minh não người dùng cùng cơ chế.

## Gradient không phải lời giải thích nhân quả cho prediction

Gradient `∂output/∂input` có thể dùng trong saliency map, nhưng nó chỉ mô tả độ nhạy cục bộ.

Gradient lớn không tự động là bằng chứng một feature “gây ra” prediction hoặc là toàn bộ reasoning trace của mô hình.

## Debug gradient

Các tín hiệu hữu ích gồm:

- gradient norm theo từng layer;
- norm của parameter và tỷ lệ update;
- tỷ lệ gradient bằng 0;
- NaN/Inf;
- dấu hiệu gradient biến mất hoặc bùng nổ theo depth.

Với mạng nhỏ, có thể kiểm tra đạo hàm bằng finite difference:

\[
\frac{\partial L}{\partial \theta}
\approx
\frac{L(\theta+\epsilon)-L(\theta-\epsilon)}{2\epsilon}
\]

Cách này hữu ích để kiểm chứng custom backward implementation, nhưng không dùng cho large-scale training vì quá đắt và nhạy với sai số số học.

## Mô hình tư duy

```text
Forward:
tham số → giá trị trung gian → loss

Backward:
độ nhạy của loss
← đạo hàm cục bộ
← đạo hàm cục bộ
← ...
→ gradient cho mọi tham số
```

Backpropagation không “hiểu” ngữ nghĩa của lỗi. Nó chỉ phân phối tín hiệu trách nhiệm định lượng do loss và computation graph xác định.

## Các hiểu lầm thường gặp

### “Backpropagation = Gradient Descent”

Không. Backpropagation tính gradient; Gradient Descent, Adam hoặc optimizer khác dùng gradient đó để update.

### “Có autograd thì không cần hiểu đạo hàm”

Không. Nếu không hiểu gradient flow sẽ rất khó debug saturation, detach, exploding gradient, custom operation hoặc training instability.

### “Gradient lớn nghĩa feature quan trọng”

Không. Gradient là độ nhạy cục bộ và phụ thuộc scale, điểm đang xét và chính mô hình.

### “Backward pass lưu toàn bộ Jacobian”

Không. Reverse-mode AD dùng VJP và các quy tắc cục bộ để tránh materialize Jacobian đầy đủ.

## Liên kết kiến thức

Xem [Giải tích cho AI](../01_mathematical_foundations/04_calculus_for_ai.md), [Lan truyền tiến](./03_forward_propagation.md) và tiếp theo [Gradient Descent và Optimizer](./05_gradient_descent_and_optimizers.md).