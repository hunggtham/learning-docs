# Activation Functions: tại sao Neural Network cần Nonlinearity?

Activation Function (활성화 함수 / hàm kích hoạt) thường được giới thiệu như một danh sách `sigmoid`, `tanh`, `ReLU`, `GELU`. Cách học đó dễ biến thành thuộc lòng. Bản chất sâu hơn là: activation quyết định **hình dạng transformation**, **gradient flow** và **statistical behavior** của hidden representations.

Nếu bỏ activation giữa các affine layers, toàn network collapse thành một affine transformation. Vì vậy nonlinearity là điều kiện để depth tạo expressivity mới.

## Identity activation

\[
\phi(z)=z
\]

Không thêm nonlinearity. Hữu ích ở regression output hoặc một số residual/projection block, nhưng nếu mọi hidden layer đều identity thì deep stack vẫn linear.

## Sigmoid

\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]

Range `(0,1)`. Derivative:

\[
\sigma'(z)=\sigma(z)(1-\sigma(z))
\]

Maximum derivative chỉ `0.25`; khi `|z|` lớn, derivative gần zero. Đây là **saturation**, gây vanishing gradients khi stack sâu.

Sigmoid vẫn rất phù hợp ở binary probability output hoặc gates trong LSTM, nơi bounded value có semantic rõ.

## tanh

\[
tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}
\]

Range `(-1,1)`, zero-centered hơn sigmoid.

Derivative:

\[
1-tanh^2(z)
\]

vẫn saturate khi magnitude lớn.

Historically tanh tốt hơn sigmoid cho hidden layers trong nhiều early networks, nhưng ReLU-family thường easier train deep feed-forward nets.

## ReLU

\[
ReLU(z)=\max(0,z)
\]

Derivative:

\[
ReLU'(z)=
\begin{cases}
0,&z<0\\
1,&z>0
\end{cases}
\]

Tại zero derivative convention tùy implementation, nhưng single point không tạo issue lớn trong continuous training.

Ưu điểm:

- không saturate ở positive side;
- computation đơn giản;
- sparse activations;
- gradient có thể flow tốt hơn sigmoid/tanh.

## Dying ReLU

Nếu unit rơi vào region `z<0` cho hầu hết inputs, gradient qua ReLU = 0 nên unit có thể không recover. Learning rate quá lớn hoặc bad initialization làm risk tăng.

Variants:

**Leaky ReLU**:

\[
\phi(z)=\max(\alpha z,z)
\]

cho small negative slope.

**PReLU** học `α`.

**ELU/SELU** có smooth negative region với goals khác về activation statistics.

## GELU

Gaussian Error Linear Unit (GELU) phổ biến trong Transformers:

\[
GELU(x)=x\Phi(x)
\]

với `Φ` là CDF của standard normal.

Intuitively, GELU gate input smoothly theo magnitude thay vì hard zero như ReLU.

Approximation thường dùng:

\[
0.5x\left(1+tanh\left[\sqrt{2/\pi}(x+0.044715x^3)\right]\right)
\]

Transformer variants cũng dùng SiLU/SwiGLU.

## SiLU / Swish

\[
SiLU(x)=x\sigma(x)
\]

Smooth, non-monotonic nhẹ ở negative region và được dùng trong nhiều modern architectures.

## Gated Linear Units và SwiGLU

Transformer feed-forward blocks hiện đại thường dùng gated activation:

\[
SwiGLU(x)=(xW_1)\odot SiLU(xW_2)
\]

rồi projection tiếp theo.

Gating cho phép multiplicative interaction giữa learned projections, tăng expressivity so với một activation scalar đơn giản.

## Softmax không phải hidden activation thông thường

Softmax:

\[
softmax(z_i)=\frac{e^{z_i}}{\sum_j e^{z_j}}
\]

biến vector logits thành distribution sum=1. Nó thường dùng ở multiclass output và attention weights, không làm hidden activation generic như ReLU/GELU.

Softmax couples dimensions: thay một logit ảnh hưởng probabilities của mọi classes.

## Activation và gradient flow

Backprop qua chain product:

\[
\frac{\partial L}{\partial h^{(l)}}=rac{\partial L}{\partial h^{(l+1)}}\frac{\partial h^{(l+1)}}{\partial h^{(l)}}
\]

Nếu derivatives liên tục <1 mạnh, gradient shrink qua depth. Nếu Jacobian norms >1 liên tục, gradient có thể explode.

Activation choice tương tác với initialization, normalization, residual connections và architecture; không thể đánh giá riêng lẻ.

## Output activation phải match target

Regression unbounded → thường identity.

Binary classification → sigmoid probability hoặc logits + numerically stable BCE-with-logits.

Mutually exclusive multiclass → softmax.

Multi-label → independent sigmoid per label.

Positive quantity → có thể softplus/exponential tùy probabilistic model.

Variance parameter cần >0 → softplus thường useful.

Activation ở output là một modeling assumption, không chỉ implementation detail.

## Differentiability có bắt buộc tuyệt đối không?

Gradient-based training cần useful derivatives gần như mọi nơi, nhưng function không cần differentiable tại mọi single point. ReLU là example.

Discrete operations như `argmax` thường không differentiable và được đặt ngoài training path hoặc xử lý bằng relaxations/estimators.

## Activation statistics

Nếu activations liên tục có mean/variance drift qua layers, optimization khó. Initialization và normalization cố giữ scale signal hợp lý.

Self-normalizing networks từng thiết kế SELU + initialization để activation statistics converge về stable range under assumptions.

Modern Transformers thường dựa LayerNorm/RMSNorm + residual pathways.

## Why ReLU changed Deep Learning

ReLU không phải nguyên nhân duy nhất, nhưng cùng better initialization và GPUs, nó giảm saturation problem trong deep feed-forward/CNN networks, giúp training depth lớn hơn thực dụng.

Historical progress thường đến từ interaction của nhiều improvements, không single magic activation.

## Mental Model

> Activation function là “shape control” của learned transformation: nó quyết định layer có thể bend representation space thế nào và gradient đi qua transformation ra sao.

## Common Misconceptions

### “ReLU tốt nhất nên cứ dùng ReLU”

Architecture/domain matter. Transformers thường dùng GELU/SiLU/SwiGLU; RNN gates dùng sigmoid/tanh.

### “Sigmoid lỗi thời”

Không. Nó vẫn natural cho Bernoulli output và gating.

### “Softmax làm model confident hơn”

Softmax chỉ normalize logits; temperature/scale ảnh hưởng sharpness, không đảm bảo correctness/calibration.

### “Activation chỉ ảnh hưởng expressivity”

Nó còn ảnh hưởng optimization, gradient flow, activation statistics và numerical behavior.

## Knowledge Connection

Xem [Calculus](../01_mathematical_foundations/04_calculus_for_ai.md), [Numerical Computation](../01_mathematical_foundations/07_numerical_computation.md), [Initialization and Normalization](./06_initialization_and_normalization.md).

Xem tiếp: [Forward Propagation](./03_forward_propagation.md).