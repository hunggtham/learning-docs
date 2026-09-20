# Neuron, Perceptron và Multi-Layer Perceptron

Artificial neuron là building block đơn giản: nhận vector input, tính weighted sum, thêm bias rồi qua activation. Nhưng để hiểu vì sao neural network hoạt động, cần phân biệt rõ **perceptron**, **neuron hiện đại**, **single-layer network** và **Multi-Layer Perceptron (MLP / 다층 퍼셉트론)**.

## Artificial neuron

Một unit:

\[
z=\mathbf w^T\mathbf x+b
\]

\[
a=\phi(z)
\]

`w` xác định direction/sensitivity, `b` dịch decision threshold, `φ` tạo nonlinearity.

Nếu `φ` là identity, unit chỉ là linear regression component. Nếu sigmoid, có logistic behavior. Nếu ReLU, output zero cho negative preactivation và linear cho positive.

## Perceptron lịch sử

Perceptron binary dùng threshold/sign activation:

\[
\hat y=sign(\mathbf w^T\mathbf x+b)
\]

Learning rule update khi misclassified:

\[
\mathbf w\leftarrow \mathbf w+\eta y\mathbf x
\]

cho labels `y∈{-1,+1}` trong simplified form.

Perceptron Convergence Theorem nói nếu data linearly separable, algorithm hội tụ sau hữu hạn mistakes.

Nhưng XOR không linearly separable, nên single perceptron không solve được. Limitation này thúc đẩy multi-layer networks.

## Layer dưới dạng matrix

Thay vì một neuron, layer có `m` units:

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

Mỗi row của `W` là weight vector của một unit. GPU có thể tính hàng nghìn units song song bằng matrix multiplication.

## Multi-Layer Perceptron

MLP stack fully-connected layers:

\[
h^{(1)}=\phi(W^{(1)}x+b^{(1)})
\]

\[
h^{(2)}=\phi(W^{(2)}h^{(1)}+b^{(2)})
\]

\[
\hat y=g(W^{(3)}h^{(2)}+b^{(3)})
\]

Hidden layers không có target trực tiếp. Chúng được shaped bởi final loss thông qua backpropagation.

## Hidden units đang học gì?

Không nên assume mỗi hidden unit tương ứng một concept rõ như “mắt mèo”. Representation thường distributed.

Một hidden vector `h` có thể encode multiple factors qua directions/subspaces. Layer sau combine chúng thành higher-order features.

Interpretability cần empirical analysis, không thể suy meaning chỉ từ unit index.

## Output layer phụ thuộc task

Binary classification thường dùng one logit + sigmoid hoặc two logits + softmax.

Multiclass:

\[
\mathbf p=softmax(Wh+b)
\]

Regression có thể dùng linear output.

Multi-label classification thường dùng independent sigmoid per label, không softmax, vì labels không mutually exclusive.

Output activation/loss phải match probabilistic structure của target.

## Batch dimension

Thực tế input batch:

\[
X\in\mathbb R^{B\times d}
\]

Forward:

\[
Z=XW^T+b
\]

Broadcast bias trên `B` samples.

Tensor-shape reasoning là skill critical khi implement neural networks.

## Parameter count

Fully connected layer từ `d_in` tới `d_out` có:

\[
d_{in}d_{out}+d_{out}
\]

parameters.

Nếu image 224×224×3 flatten trực tiếp (~150k features) rồi connect 4096 hidden units, parameters >600M chỉ layer đầu. Đây là lý do CNN dùng locality/weight sharing thay dense MLP cho images.

Architecture phản ánh structural assumptions của modality.

## MLP cho tabular data

MLP có thể dùng tabular data, nhưng Gradient Boosted Trees thường rất competitive khi data size vừa và heterogeneous. Neural models có lợi khi:

- dataset lớn;
- learned embeddings/categories;
- multimodal inputs;
- end-to-end representation learning;
- transfer/pretraining.

Không nên chọn MLP chỉ vì “deep learning hiện đại hơn”.

## Decision regions

ReLU MLP tạo piecewise-linear function. Mỗi pattern ReLU active/inactive xác định một local linear region.

Depth có thể tạo rất nhiều regions, cho decision boundary phức tạp dù mỗi primitive operation đơn giản.

## Bias term là gì?

Bias `b` không phải statistical/social bias. Nó giống intercept: cho phép activation threshold dịch khỏi origin.

Không có bias, mọi hyperplane `Wx=0` đi qua origin, hạn chế expressivity.

## Dense connection và sparsity

Standard MLP fully connected: mỗi output unit nhận toàn bộ previous hidden vector. Nhưng architectures khác có sparse/local/recurrent/attention connections.

Neural Network không đồng nghĩa fully connected network.

## Perceptron vs Logistic Neuron

Perceptron hard threshold không differentiable tại boundary và gradient zero/undefined theo cách không thuận lợi cho backprop.

Sigmoid/ReLU/GELU cung cấp differentiable hoặc almost-everywhere differentiable behavior phù hợp gradient-based training.

Modern network vì vậy không train bằng classic perceptron rule trong đa số cases.

## Example: XOR bằng hidden representation

Một MLP có thể học hidden units đại diện regions khác nhau rồi output combine chúng.

Conceptually:

```text
(x1, x2)
  ↓ hidden nonlinear features
[feature: x1 OR x2,
 feature: x1 AND x2]
  ↓ combine
XOR
```

Không cần hand-code exact logical features; training có thể discover useful intermediate features.

## Mental Model

```text
Neuron = linear measurement + nonlinear response
Layer  = many measurements learned together
MLP    = repeated representation transformation
```

Hidden layers không phải “các bước reasoning” theo nghĩa symbolic; chúng là learned numerical transformations.

## Common Misconceptions

### “Mỗi neuron là một feature có nghĩa rõ ràng”

Có thể có specialized units, nhưng information thường distributed.

### “Perceptron và modern neural network là cùng một algorithm”

Perceptron là historical linear-threshold learner. Modern nets use multilayer differentiable computation + backprop/optimizers.

### “Bias neuron gây model bias”

Bias term chỉ là affine offset, không liên quan trực tiếp fairness bias.

### “MLP đủ universal nên không cần CNN/Transformer”

Theoretical expressivity không thay efficiency/inductive bias. Specialized architectures learn relevant structure hiệu quả hơn.

## Knowledge Connection

Xem lại [Linear Algebra](../01_mathematical_foundations/01_linear_algebra_for_ai.md) và [From Linear Models to Neural Networks](./00_from_linear_models_to_neural_networks.md).

Xem tiếp: [Activation Functions](./02_activation_functions.md), phần quyết định layer composition có thực sự nonlinear và trainable hay không.