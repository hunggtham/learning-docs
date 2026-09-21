# Logistic Regression: từ linear score tới xác suất phân loại

Logistic Regression (로지스틱 회귀 / hồi quy logistic) có tên chứa “regression” nhưng thường được dùng cho **classification**. Ý tưởng trung tâm rất đơn giản: trước hết tính một linear score, sau đó biến score đó thành probability-like output bằng sigmoid.

Model này quan trọng vì nó tạo cây cầu trực tiếp giữa Linear Algebra, Probability, Maximum Likelihood, Cross-Entropy và Decision Boundary. Nhiều classifier hiện đại vẫn dùng cùng logic ở output layer.

## Tại sao Linear Regression không phù hợp trực tiếp cho binary classification?

Nếu target chỉ nhận `0` hoặc `1`, linear model:

\[
\hat y=\mathbf w^T\mathbf x+b
\]

có thể output `-3.2` hoặc `1.8`, không phù hợp để interpret như probability.

Ta cần một function map real line vào `(0,1)`.

Sigmoid:

\[
\sigma(z)=\frac{1}{1+e^{-z}}
\]

với:

\[
z=\mathbf w^T\mathbf x+b
\]

cho:

\[
p(y=1\mid x)=\sigma(z)
\]

Khi `z=0`, probability là `0.5`. `z` càng dương thì probability tiến về `1`; càng âm thì tiến về `0`.

## Odds và log-odds

Probability `p` có odds:

\[
\frac{p}{1-p}
\]

Log-odds hoặc **logit**:

\[
\log\frac{p}{1-p}
\]

Logistic Regression assume log-odds là linear function của input:

\[
\log\frac{p}{1-p}=\mathbf w^T\mathbf x+b
\]

Đây là interpretation chính xác hơn câu “probability tuyến tính theo feature”. Probability không tuyến tính; log-odds mới linear.

Nếu coefficient `w_j` tăng một đơn vị trong `x_j`, odds được nhân với:

\[
e^{w_j}
\]

khi giữ feature khác cố định.

## Maximum Likelihood dẫn tới Binary Cross-Entropy

Với Bernoulli target:

\[
y\sim Bernoulli(p)
\]

likelihood của một sample:

\[
P(y\mid x)=p^y(1-p)^{1-y}
\]

Log-likelihood:

\[
\log P(y\mid x)=y\log p+(1-y)\log(1-p)
\]

Maximize likelihood tương đương minimize negative log-likelihood:

\[
L=-[y\log p+(1-y)\log(1-p)]
\]

Đây chính là **binary cross-entropy**.

Vì vậy sigmoid và cross-entropy không phải hai recipe vô tình ghép với nhau. Chúng xuất phát từ một probabilistic model thống nhất.

## Decision boundary

Nếu threshold là `0.5`:

\[
\sigma(z)\ge0.5 \iff z\ge0
\]

Decision boundary:

\[
\mathbf w^T\mathbf x+b=0
\]

Trong 2D, đây là đường thẳng; trong higher dimension là hyperplane.

Logistic Regression vì vậy là linear classifier trong original feature space.

Nếu cần nonlinear boundary, có thể thêm transformed features hoặc dùng nonlinear model.

## Probability output không tự động calibrated

Logistic Regression thường có probability interpretation tốt khi model specification phù hợp, nhưng calibration vẫn phải kiểm tra.

Nếu model nói `p≈0.8` cho nhiều samples, ideally khoảng 80% trong nhóm đó positive.

Calibration có thể đánh giá bằng reliability diagram, Brier score hoặc expected calibration error.

Một classifier có AUC cao nhưng calibration kém vẫn có thể gây problem nếu downstream system dùng score như risk probability.

## Threshold không phải luôn 0.5

Prediction probability và decision action là hai tầng khác nhau.

Giả sử fraud detection: false negative có cost lớn hơn false positive. Threshold có thể chọn `0.2` thay vì `0.5` để tăng recall.

Decision rule tổng quát nên dựa vào expected cost:

\[
Choose\ action\ a=\arg\min_a \mathbb E[Cost(a,Y)\mid x]
\]

Do đó threshold phải được chọn theo operational objective, không theo convention.

## Class imbalance

Trong rare-event classification, accuracy dễ misleading.

Nếu positive rate `0.1%`, model luôn predict negative đã đạt `99.9%` accuracy.

Ta cần nhìn precision, recall, PR-AUC, calibration và expected business cost.

Class weighting có thể thay loss:

\[
L=-[w_1y\log p+w_0(1-y)\log(1-p)]
\]

nhưng weighting cũng có thể thay probability calibration. Nếu cần calibrated probability, phải đánh giá lại sau training.

## Regularization

L2-regularized logistic regression:

\[
J(\mathbf w)=\frac1n\sum_iL_i+\lambda\|\mathbf w\|_2^2
\]

L1 regularization có thể tạo sparse coefficients.

Regularization đặc biệt hữu ích khi feature dimension lớn hoặc features correlated.

## Multiclass: Softmax Regression

Với `K` classes, model tạo logits:

\[
z_k=\mathbf w_k^T\mathbf x+b_k
\]

Softmax:

\[
p(y=k\mid x)=\frac{e^{z_k}}{\sum_j e^{z_j}}
\]

Cross-entropy:

\[
L=-\log p(y_{true}\mid x)
\]

Đây còn được gọi là multinomial logistic regression hoặc softmax regression.

Neural network classifier thường chỉ thay phần feature extractor; cuối cùng vẫn có linear logits + softmax.

## Numerical stability

Tính sigmoid naive với `e^{-z}` có thể overflow khi `z` rất âm. Softmax naive cũng có overflow.

Implementation production dùng stable formulations như log-sum-exp và framework primitives (`BCEWithLogitsLoss`, `CrossEntropyLoss`) thay vì tự sigmoid rồi log.

Ví dụ mathematically:

\[
\log\sum_i e^{z_i}
\]

được tính ổn định bằng:

\[
m+\log\sum_i e^{z_i-m},\quad m=\max_i z_i
\]

Đây là connection trực tiếp tới Numerical Computation.

## Interpretability và giới hạn

Coefficients tương đối dễ inspect, nhưng “dễ đọc coefficient” không đồng nghĩa causal interpretability.

Feature correlation, omitted variables, data selection và transformations đều ảnh hưởng coefficients.

Nếu input là one-hot categories hoặc standardized features, coefficient meaning cũng phụ thuộc representation.

## Connection tới Language Models

Language model output layer tạo logits cho vocabulary, sau đó softmax tạo next-token distribution:

\[
p(token=k\mid context)=softmax(z)_k
\]

Cấu trúc mathematical này là multiclass logistic regression ở quy mô rất lớn, trong đó hidden representation `h` được Deep Neural Network/Transformer tạo ra trước:

\[
z=W_{out}h+b
\]

Vì vậy Logistic Regression không phải “algorithm cũ không liên quan LLM”; nó là building block còn hiện diện ở output distribution.

## Mental Model

```text
Features
   ↓
Linear score (logit)
   ↓
Sigmoid / Softmax
   ↓
Probability distribution
   ↓
Threshold / decision policy
```

Hãy giữ tách hai câu hỏi: model ước lượng probability gì, và system dùng probability đó để ra quyết định thế nào.

## Common Misconceptions

### “Sigmoid output 0.9 nghĩa chắc chắn 90% đúng”

Chỉ khi model calibrated trên relevant distribution.

### “Threshold phải là 0.5”

Không. Threshold phụ thuộc cost, class prevalence và operational constraints.

### “Logistic Regression không dùng được nonlinear feature”

Có thể dùng polynomial/interaction/engineered features; decision boundary chỉ linear trong transformed feature space.

### “Softmax probability là confidence tuyệt đối của model”

Softmax chỉ normalize logits. Neural network có thể overconfident, đặc biệt under distribution shift.

## Knowledge Connection

Xem lại [Loss, Objective and Risk](./04_loss_objective_and_risk.md), [Probability for AI](../01_mathematical_foundations/02_probability_for_ai.md) và [Information Theory](../01_mathematical_foundations/05_information_theory.md).

Xem tiếp: [Model Evaluation](./15_model_evaluation.md) để hiểu ROC, PR curve, calibration và threshold selection.