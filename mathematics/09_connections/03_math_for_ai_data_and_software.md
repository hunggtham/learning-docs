# Knowledge Connection — Toán trong AI, Data và Software Engineering

Toán trong software không phải một chapter riêng lẻ; nó là network concepts xuất hiện tùy problem. Nhìn theo dependencies giúp tránh học “toán cho AI” như list công thức.

## Data representation → vectors and matrices

Một sample với features trở thành vector `x`. Batch samples thành matrix `X`. Linear layer:

```math
z=Wx+b
```

là affine transformation. Nếu không có nonlinear activation, stacking nhiều layers vẫn collapse thành one affine map.

## Prediction → functions

Model là function parameterized bởi `θ`:

```math
\hat y=f_\theta(x)
```

Training là chọn parameters để objective nhỏ. Function concepts như domain, composition, inverse và sensitivity đều trực tiếp relevant.

## Error → distance/loss

Regression có thể dùng squared loss:

```math
L=\frac1n\sum_i(y_i-\hat y_i)^2
```

Classification có thể dùng cross-entropy. Loss định nghĩa geometry/priorities của training; chọn wrong loss có thể optimize wrong behavior.

## Learning → calculus and optimization

Gradient:

```math
\nabla_\theta L
```

đo local sensitivity của loss với parameters. Chain rule propagate derivatives qua composition. Gradient descent updates parameters.

Hessian/curvature giúp hiểu conditioning và second-order methods.

## Uncertainty → probability/statistics

Predicted probability cần calibration và conditional interpretation. Train/test evaluation là statistical estimation từ finite samples. Confidence intervals, variance, sampling bias và hypothesis testing matter khi so models.

## Similarity → geometry

Embedding search dùng vector metrics như cosine/L2. Nearest-neighbor behavior phụ thuộc dimension, scaling và learned representation.

## Graphs → dependencies and networks

Package dependencies, build order, route planning, social networks và knowledge graphs dùng graph theory. Topological sort, shortest path và connectivity không phải AI-specific; chúng là discrete mathematics.

## Complexity → feasibility

Một mathematically elegant algorithm có thể infeasible do `O(2^n)` search. Big-O cho boundary giữa “có thể code” và “có thể chạy ở scale”. Numerical complexity, memory và communication costs cũng matter.

## Floating point → numerical mathematics

ML uses fp32/fp16/bfloat16. Finite precision affects summation, gradients, overflow/underflow. Log-sum-exp trick rewrite:

```math
\log\sum_i e^{x_i}
=m+\log\sum_i e^{x_i-m}
```

với `m=max x_i` để tránh overflow, một ví dụ numerical stability thay vì thay mathematics.

## Mental Model

> AI/software không “dùng một môn toán”. Representation gọi linear algebra; change gọi calculus; uncertainty gọi probability; evidence gọi statistics; search structure gọi discrete math; training gọi optimization; actual machine execution gọi numerical analysis.

## Một forward pass nhìn bằng nhiều môn toán

Với layer

```math
z=Wx+b,
\qquad a=\sigma(z)
```

linear algebra giải thích `Wx`; function composition giải thích activation; calculus/Jacobian giải thích sensitivity; probability có thể interpret softmax output; optimization chọn `W,b`; numerical analysis quyết định computation fp16/fp32 có stable không.

Cùng một dòng code nằm ở intersection của nhiều structures. Học theo connections giúp tránh cảm giác “mỗi môn toán là một thế giới riêng”.

## Database và discrete mathematics

Relational model dùng sets/relations; joins gần relational algebra; query plans là optimization; indexes dùng trees/hash; dependency graphs dùng DAGs; cardinality estimation dùng statistics. Ngay cả công việc backend không làm ML vẫn dùng mathematical abstractions liên tục, dù frameworks che phần formal notation.

## Common Misconceptions

AI không “chỉ là matrix multiplication”; linear algebra là representation layer nhưng probability, optimization, calculus và numerical stability đều quyết định behavior. Big-O không dự đoán exact runtime. Một model có low training loss không tự động generalize; statistical assumptions và data-generating process vẫn quan trọng.

