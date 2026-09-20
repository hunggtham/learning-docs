# Neural networks và representation learning

Neural network là parameterized function composition có khả năng học nonlinear representations từ data. Tên “neural” lấy cảm hứng sinh học lịch sử nhưng modern deep learning nên được hiểu bằng linear algebra, nonlinear functions, optimization và data—not như mô phỏng não đầy đủ.

## Neuron như affine transform + nonlinearity

Một unit cơ bản tính:

\[
z = w^T x + b,
\qquad a = \phi(z)
\]

Nếu chỉ stack linear layers không có nonlinear activation, toàn network vẫn collapse thành một linear transformation. Nonlinearity tạo khả năng biểu diễn functions phức tạp.

## Layers và representations

Early layers có thể học local/simple patterns; deeper layers compose thành higher-level features. Nhưng interpretation không phải luôn human-readable.

Representation learning giảm nhu cầu hand-engineer features, đổi lại cần data/compute và làm internal behavior khó giải thích hơn.

## Forward pass và loss

Input đi qua layers tạo prediction. Loss so prediction với target/objective.

Training cần gradient của loss theo mọi parameters. Backpropagation là efficient application của chain rule trên computation graph, không phải một learning rule bí ẩn độc lập khỏi calculus.

## Gradient descent

Parameters update theo hướng giảm loss:

\[
\theta \leftarrow \theta - \eta \nabla_\theta L
\]

Learning rate `η` quá lớn có thể diverge; quá nhỏ training chậm. Adaptive optimizers như Adam điều chỉnh update dựa moments của gradients.

Optimization landscape non-convex; exact global optimum không thường là requirement để generalize tốt.

## Batch và stochasticity

Full-batch gradient dùng toàn dataset mỗi step; SGD/minibatch dùng subset, giảm per-step cost và thêm noise có thể giúp exploration/generalization.

Batch size ảnh hưởng memory, throughput và optimization dynamics.

## CNN intuition

Convolutional neural networks khai thác locality và weight sharing trên grid-like data như images. Same filter dùng ở nhiều positions tạo translation-related inductive bias.

## Sequence models và attention

RNN xử lý state theo sequence nhưng khó parallelize dài và có gradient issues. Attention cho mỗi position tính weighted interaction với positions khác.

Transformer dùng self-attention + feed-forward blocks và positional information, trở thành architecture nền cho language/vision/multimodal models.

## Embeddings

Embedding map discrete symbols/items vào vectors sao cho geometry phản ánh learned relationships theo training objective.

Similarity trong embedding space là model-dependent. Cosine gần không có nghĩa entities “giống nhau mọi nghĩa”; chỉ theo representation learned.

## Capacity và scaling

Tăng parameters/data/compute có thể cải thiện performance nhưng cost energy, latency và memory tăng. Quantization, pruning, distillation và efficient architectures trade accuracy/compute.

## Common Misconceptions

**“Neural network học giống não.”** Inspiration lịch sử không đồng nghĩa biological fidelity.

**“Deep learning không cần feature engineering.”** Architecture, tokenization, preprocessing, labels và objective vẫn encode assumptions.

**“Attention là explanation.”** Attention weights không tự động là causal explanation của model decision.

## Mental Model

> Deep network là differentiable program whose internal representation được học bằng gradient-based optimization để phục vụ objective trên data.

## Kết nối

Đọc [linear algebra](../../../mathematics/04_vectors_linear_algebra/01_matrices_and_linear_systems.md), [matrix calculus/autodiff](../../../mathematics/04_vectors_linear_algebra/09_matrix_calculus_jacobian_hessian_and_autodiff.md), [gradient descent](../../../mathematics/08_optimization_numerical/01_gradient_descent_and_convexity.md) và [ML foundations](./02_machine_learning_foundations.md).