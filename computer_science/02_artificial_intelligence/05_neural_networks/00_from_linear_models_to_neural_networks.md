# Từ Linear Models tới Neural Networks

Neural Network (신경망 / mạng nơ-ron) không xuất hiện vì linear/logistic regression “sai”, mà vì nhiều relationship trong thế giới không thể biểu diễn tốt bằng một global linear boundary trên raw features. Ý tưởng cốt lõi của neural network là **compose nhiều transformations và học representation trung gian**, thay vì yêu cầu con người hand-engineer toàn bộ nonlinear features.

Chapter này tạo cầu nối từ Machine Learning cổ điển sang Deep Learning. Nếu nắm được lý do composition + nonlinearity cần thiết, neural network sẽ không còn là một “hộp đen nhiều layer”.

## Một linear layer thực sự làm gì?

Linear/affine transformation:

\[
\mathbf z=W\mathbf x+\mathbf b
\]

biến vector input thành vector mới bằng rotate/scale/shear/project + shift theo geometric interpretation.

Nếu stack hai linear layers mà không có nonlinear function:

\[
\mathbf h=W_1\mathbf x+b_1
\]

\[
\mathbf y=W_2\mathbf h+b_2
\]

thì:

\[
\mathbf y=W_2W_1\mathbf x+(W_2b_1+b_2)
\]

vẫn chỉ là **một affine transformation duy nhất**.

Do đó depth chỉ có ý nghĩa expressive nếu giữa layers có nonlinearity hoặc mechanism khác không collapse thành một linear map.

## XOR: vì sao một boundary tuyến tính không đủ?

XOR có truth table:

```text
x1 x2 | y
0  0  | 0
0  1  | 1
1  0  | 1
1  1  | 0
```

Không có một đường thẳng trong 2D tách hai positive points khỏi hai negative points.

Nhưng nếu tạo hidden representation phù hợp, problem có thể trở nên linearly separable ở space mới.

Đây là essence của neural networks:

> Không nhất thiết cố tìm decision boundary phức tạp trong raw space; hãy học một transformation đưa data sang representation space nơi task trở nên đơn giản hơn.

## Hand-Engineered Features vs Learned Features

Classical ML thường có pipeline:

```text
raw input
→ domain feature engineering
→ linear/tree model
```

Ví dụ text classification từng dùng word counts, TF-IDF, n-grams.

Deep Learning chuyển nhiều burden sang model:

```text
raw-ish input
→ learned representations
→ learned representations sâu hơn
→ task output
```

Image network có thể học edges → textures → parts → object-level representations. Transformer học contextual token representations qua nhiều layers.

Điều này không có nghĩa feature engineering biến mất. Tokenization, normalization, data augmentation, architecture, position encoding và context construction đều là representation decisions.

## Function Composition

Một neural network có thể viết:

\[
f(x)=f_L(f_{L-1}(...f_2(f_1(x))))
\]

Mỗi layer thường:

\[
h^{(l)}=\phi(W^{(l)}h^{(l-1)}+b^{(l)})
\]

`φ` là activation/nonlinearity.

Depth cho phép model tái sử dụng intermediate features. Thay vì học trực tiếp raw pixels → class, network có thể xây hierarchy.

## Universal Approximation không có nghĩa “network học được mọi thứ dễ dàng”

Universal Approximation Theorem nói under conditions, một sufficiently wide network có thể approximate continuous functions trên compact domain tốt tùy ý.

Nhưng theorem **không** nói:

- gradient descent sẽ tìm được parameters đó;
- cần ít data;
- network sẽ generalize;
- representation sẽ interpretable;
- compute hữu hạn là đủ.

Expressivity, trainability và generalization là ba vấn đề khác nhau.

## Width và Depth

Width tăng số units trong layer; depth tăng số composed transformations.

Một số functions có thể represent compactly bằng deep network nhưng cần exponentially many units nếu shallow. Depth tạo compositional efficiency khi problem có hierarchical structure.

Tuy nhiên deeper không luôn better: optimization, latency, memory và overfitting/instability matter.

## Parameters và Architecture

Parameters gồm weights/biases học từ data.

Architecture quyết định computation graph: số layer, hidden dimension, connections, activation, normalization, attention/convolution etc.

Architecture là một mạnh **inductive bias**.

CNN encode locality/weight sharing. RNN encode recurrence. Transformer encode content-dependent interactions through attention.

## Neural Network là differentiable program

Một useful mental model:

> Neural network là một parameterized differentiable program.

Forward pass chạy program để tạo output. Loss đo output. Backpropagation dùng chain rule để tính sensitivity của loss đối với parameters. Optimizer thay parameters.

```text
Input
 ↓
Differentiable computation graph fθ
 ↓
Prediction
 ↓
Loss
 ↓ backward
Gradients
 ↓ optimizer
Updated θ
```

Đây là core training loop của Deep Learning.

## Neural Network không nhất thiết mô phỏng brain

Names như neuron, synapse đến từ historical inspiration, nhưng modern neural networks không phải realistic simulation của biological brain.

Artificial neuron thường chỉ tính weighted sum + activation. Transformer càng xa neuron sinh học trực tiếp.

Biological analogy hữu ích ở mức lịch sử/intuitive inspiration, nhưng không nên dùng để suy luận technical behavior.

## Distributed Representation

Trong symbolic system, concept có thể map tới explicit symbol. Neural networks thường dùng **distributed representation**: information được encode qua pattern của nhiều dimensions/units.

Một neuron hiếm khi tương ứng đơn giản với một semantic concept duy nhất. Meaning thường nằm trong subspace/direction/activation pattern.

Điều này giúp representation compositional/generalizable nhưng làm interpretability khó.

## End-to-End Learning

End-to-end training optimize một objective qua nhiều stages jointly.

Ví dụ speech recognition trước đây có pipeline acoustic features → phoneme model → language model → decoder. End-to-end model có thể learn mapping audio → text với components jointly optimized.

Lợi ích: intermediate representation adapt task.

Risk: less modular/debuggable, cần more data/compute, và failure origin khó trace.

Production systems thường vẫn hybrid, không phải mọi thứ end-to-end.

## Neural Networks và probabilistic outputs

Network thường output logits/parameters của distribution, không phải “answer certainty” trực tiếp.

Classification:

\[
p(y\mid x)=softmax(W_outh+b)
\]

Regression có thể output mean/variance của Gaussian.

Generative models parameterize complex distributions.

Probability/calibration principles từ ML vẫn áp dụng.

## Scale: data, compute, parameters

Deep Learning thành công nhờ combination:

- large datasets;
- GPU/accelerator matrix computation;
- better initialization/activations/normalization;
- optimization methods;
- architectures matching modalities;
- distributed systems.

Không có một single “neural network breakthrough” giải thích toàn bộ.

## Mental Model

```text
Linear model:
raw representation → simple decision

Neural network:
raw representation
→ learned transform
→ learned transform
→ ...
→ representation where task is easier
→ simple output head
```

## Common Misconceptions

### “Neural Network chỉ là rất nhiều logistic regressions”

Mỗi unit có linear + nonlinear operation, nhưng composition tạo learned hierarchical representations mà một single logistic model không có.

### “Universal approximation nghĩa neural network giải được mọi problem”

Representation capacity không đảm bảo learnability, data sufficiency, robustness hay correctness.

### “Deep Learning không cần feature engineering”

Nó giảm handcraft feature extraction nhưng data/representation/architecture engineering vẫn cực quan trọng.

### “Càng nhiều layers càng intelligent”

Depth chỉ hữu ích nếu architecture/training/data support. Deeper có thể khó optimize và lãng phí compute.

## Knowledge Connection

Chapter này nối [Linear Regression](../04_machine_learning/05_linear_regression.md), [Logistic Regression](../04_machine_learning/06_logistic_regression.md), [Calculus](../01_mathematical_foundations/04_calculus_for_ai.md) và [Optimization](../01_mathematical_foundations/06_optimization.md).

Xem tiếp: [Neuron, Perceptron and MLP](./01_neuron_perceptron_and_mlp.md).