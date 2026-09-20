# Ensemble Learning: nhiều model yếu thành một hệ thống mạnh hơn

Ensemble Learning (앙상블 학습 / học tổ hợp) bắt đầu từ một observation: một model đơn lẻ có thể mắc lỗi do noise, sample variation hoặc limitation của function class. Nếu kết hợp nhiều models có lỗi không hoàn toàn giống nhau, aggregate prediction có thể ổn định và chính xác hơn.

Hai family quan trọng nhất là **bagging** và **boosting**. Cả hai đều dùng nhiều learners, nhưng mechanism gần như đối lập: bagging huấn luyện tương đối độc lập rồi average để giảm variance; boosting xây learners tuần tự, mỗi learner tập trung sửa phần ensemble hiện tại làm chưa tốt.

## Vì sao averaging có thể giảm variance?

Giả sử các estimators có cùng variance `σ²` và pairwise correlation `ρ`. Variance của average `M` models xấp xỉ:

\[
Var(\bar f)\approx \rho\sigma^2+\frac{1-\rho}{M}\sigma^2
\]

Khi `M` tăng, phần independent noise giảm. Nhưng nếu models hoàn toàn correlated (`ρ≈1`), averaging gần như không giúp.

Insight cốt lõi:

> Ensemble cần cả **strength** và **diversity**.

## Bagging

**Bootstrap Aggregating (Bagging / 배깅)** tạo nhiều bootstrap datasets bằng sampling training examples với replacement. Mỗi model train trên sample khác nhau; predictions được average/vote.

Decision Tree đặc biệt phù hợp vì tree có high variance: thay data một chút có thể thay structure mạnh. Averaging nhiều trees giúp ổn định.

## Random Forest

Random Forest thêm một source randomness nữa: tại mỗi split, tree chỉ xem một random subset features.

Điều này giảm correlation giữa trees. Nếu tất cả trees luôn dùng cùng dominant feature ở root, chúng sẽ rất giống nhau; random feature subsets tăng diversity.

Classification:

\[
\hat y=mode\{f_1(x),...,f_M(x)\}
\]

Regression:

\[
\hat y=\frac1M\sum_{m=1}^M f_m(x)
\]

Random Forest thường là strong baseline cho tabular data vì ít preprocessing, robust với nonlinear interaction và không quá nhạy hyperparameter so với boosting.

## Out-of-Bag Evaluation

Mỗi bootstrap sample không chứa khoảng 36.8% unique training examples. Những points không được dùng train một tree gọi là **out-of-bag (OOB)** cho tree đó.

Ta có thể aggregate predictions chỉ từ trees mà sample đó là OOB để ước lượng generalization performance mà không cần separate validation cho một số use case.

OOB không thay thế mọi validation design, đặc biệt time/group leakage vẫn phải xử lý đúng.

## Boosting: sửa lỗi tuần tự

Boosting xây model dạng additive:

\[
F_M(x)=\sum_{m=1}^{M}\alpha_m h_m(x)
\]

Mỗi weak learner `h_m` được thêm để cải thiện objective của ensemble hiện tại.

### AdaBoost

AdaBoost tăng trọng số các samples bị classify sai để learner sau chú ý chúng hơn.

Conceptually:

```text
Model 1 → tìm lỗi
        ↓
Tăng trọng số examples khó
        ↓
Model 2 → tập trung hơn vào lỗi
        ↓
Weighted vote
```

### Gradient Boosting

Gradient Boosting có interpretation tổng quát hơn: ở mỗi step, train learner mới để approximate negative gradient của loss theo current predictions.

Với squared-error regression, negative gradient chính là residual:

\[
r_i=y_i-F_{m-1}(x_i)
\]

Tree mới học residual, sau đó:

\[
F_m(x)=F_{m-1}(x)+\eta h_m(x)
\]

`η` là learning rate/shrinkage.

Tên “Gradient Boosting” vì procedure thực hiện gradient descent trong **function space**, không trực tiếp chỉ parameter space như neural network.

## XGBoost, LightGBM, CatBoost

Các implementation hiện đại bổ sung regularization, efficient histogram splitting, parallelization, missing-value handling và categorical strategies.

- **XGBoost** nổi tiếng với regularized objective và engineering hiệu quả.
- **LightGBM** dùng histogram/leaf-wise growth để scale tốt trên large tabular data.
- **CatBoost** có techniques mạnh cho categorical features và giảm target leakage trong target statistics.

Không nên học chúng chỉ như ba library APIs. Chúng đều nằm trong gradient-boosted decision-tree family nhưng khác optimization/system design.

## Learning rate và number of trees

Small learning rate thường cần nhiều trees hơn. Đây là trade-off giữa từng step update nhỏ và ensemble depth theo iteration.

Quá nhiều boosting rounds có thể overfit, dù tree boosting thường overfit chậm hơn single deep tree. Early stopping trên validation set là practice quan trọng.

## Bagging vs Boosting

| Aspect | Bagging | Boosting |
|---|---|---|
| Primary goal | giảm variance | giảm bias, tiếp tục sửa error |
| Training | có thể parallel | chủ yếu sequential |
| Typical model | Random Forest | GBDT/XGBoost/LightGBM |
| Noise sensitivity | thường robust hơn | có thể nhạy hơn với mislabeled/outlier |
| Core mechanism | average diverse learners | additive corrective learners |

## Stacking

**Stacking** dùng predictions của base models làm input cho meta-model.

Ví dụ:

```text
Linear model ─┐
Tree model   ─┼→ out-of-fold predictions → Meta model
Neural model ─┘
```

Critical: meta-model phải train trên **out-of-fold** predictions. Nếu dùng in-sample predictions, leakage xảy ra vì base models đã thấy targets.

## Ensemble và uncertainty

Disagreement giữa ensemble members đôi khi cung cấp signal về epistemic uncertainty. Deep ensembles dùng nhiều neural networks với initialization/data order khác nhau và thường cho uncertainty estimate thực dụng tốt.

Nhưng disagreement không tự động là calibrated uncertainty, nhất là khi all models share same blind spots.

## Tabular ML và Deep Learning

Trên nhiều structured/tabular tasks với dataset vừa phải, Gradient Boosted Trees vẫn rất competitive hoặc tốt hơn generic neural networks. Điều này cho thấy “model mới hơn” không đồng nghĩa “phù hợp hơn mọi data modality”.

Inductive bias của trees rất hợp threshold, heterogeneous scale và feature interaction trong tabular data.

## Mental Model

```text
Bagging  = nhiều góc nhìn độc lập + average → ổn định hơn
Boosting = model sau sửa lỗi model trước → function mạnh dần
Stacking = model cấp trên học cách phối hợp các model cấp dưới
```

## Common Misconceptions

### “Nhiều model luôn tốt hơn một model”

Nếu models correlated hoặc cùng bias, ensemble gain có thể nhỏ.

### “Random Forest chỉ là nhiều tree bình thường”

Random feature selection là component quan trọng để decorrelate trees.

### “Gradient Boosting train từng tree trên target gốc”

Learners sau được fit để cải thiện current objective, thường qua residual/negative gradient.

### “Stacking chỉ cần lấy prediction rồi train model mới”

Nếu không dùng out-of-fold design, leakage làm meta-model đánh giá giả.

## Knowledge Connection

Ensemble Learning là application trực tiếp của [Bias–Variance and Generalization](./14_bias_variance_and_generalization.md) và [Optimization](../01_mathematical_foundations/06_optimization.md).

Xem tiếp: [Support Vector Machines](./10_support_vector_machines.md) để chuyển sang một family có inductive bias hình học rất khác.