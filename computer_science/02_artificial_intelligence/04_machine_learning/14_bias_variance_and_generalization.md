# Bias, Variance và Generalization

Machine Learning không được đánh giá bằng khả năng nhớ training data, mà bằng khả năng **generalize (일반화 / khái quát hóa)** sang những examples chưa thấy nhưng đến từ environment mục tiêu. Đây là điểm phân biệt learning với memorization.

Ba concept giúp reasoning về vấn đề này là **bias**, **variance** và **irreducible noise**. Chúng không phải chỉ là vocabulary để giải thích overfitting; chúng là framework để hiểu model capacity, regularization, data size và ensemble methods.

## Training error không phải mục tiêu cuối

Một model có thể đạt gần zero training loss bằng cách memorize dataset. Nếu future input khác training examples, prediction có thể thất bại.

Ta quan tâm expected risk:

\[
R(f)=\mathbb E_{(X,Y)\sim P}[L(Y,f(X))]
\]

nhưng chỉ quan sát finite sample. Validation/test design cố estimate risk này dưới assumptions về future distribution.

Generalization gap:

\[
Gap=R_{test}-R_{train}
\]

là một signal, nhưng interpretation phụ thuộc split representativeness.

## Bias trong bias–variance decomposition

Ở đây **bias** không phải social bias. Nó là systematic error do model class/learning procedure không thể hoặc không có xu hướng capture true relationship.

Với squared error regression:

\[
\mathbb E[(Y-\hat f(x))^2]
=Bias^2+Variance+Noise
\]

một decomposition simplified dưới assumptions phù hợp.

Bias cao: model consistently miss structure, ví dụ fit straight line cho relationship rất cong.

Variance cao: model thay đổi mạnh nếu training sample thay đổi nhẹ.

Noise: uncertainty không thể loại hết chỉ bằng model tốt hơn với observed features.

## Underfitting và Overfitting

**Underfitting** thường liên quan capacity quá thấp, feature representation nghèo hoặc optimization chưa đủ. Training error và validation error đều cao.

**Overfitting** xảy ra khi model học details/noise specific training sample khiến validation/generalization kém. Training error thấp nhưng validation error cao.

Tuy nhiên modern Deep Learning làm simple textbook picture phức tạp hơn: overparameterized networks có thể interpolate training data vẫn generalize tốt nhờ implicit/explicit regularization, data scale và optimization bias.

Vì vậy “parameters > samples ⇒ chắc chắn overfit” không phải rule universal.

## Model Capacity

Capacity mô tả richness của function class model có thể represent.

Examples:

- linear regression với vài features: capacity thấp;
- deep tree: capacity cao hơn;
- large neural network: rất cao.

Capacity cao giảm approximation bias nhưng mở nhiều solutions fit noise. Regularization và data constrain learning process để chọn solution có generalization tốt hơn.

## Inductive Bias

Không model nào học từ finite data mà hoàn toàn không assumption.

Linear model assume useful relationship gần linear trong representation. CNN assume locality/translation structure. Tree assume recursive feature partitions. Transformer attention assume token interactions có thể học từ content-dependent weighted mixing.

Inductive bias tốt làm sample-efficient hơn nếu phù hợp domain.

## Regularization

### Explicit Regularization

L2:

\[
J=\hat R+\lambda\|\theta\|_2^2
\]

L1, dropout, label smoothing, data augmentation và early stopping đều có regularization effects khác nhau.

### Early Stopping

Trong iterative training, validation performance có thể tốt nhất trước khi training loss minimum. Stop sớm hạn chế model tiếp tục fit sample-specific details.

### Data Augmentation

Image flips/crops, audio perturbations hoặc text transformations encode invariances: label nên không đổi dưới những transformations hợp lệ.

Augmentation không chỉ “tạo thêm data”; nó inject inductive bias.

## More Data thay đổi trade-off thế nào?

Với fixed useful model class, thêm representative data thường giảm variance và làm estimate stable hơn.

Nhưng thêm data từ wrong distribution có thể không giúp. Duplicate, low-quality hoặc biased data cũng không tương đương independent information mới.

Dataset size nên nghĩ theo **effective diversity and coverage**, không chỉ row count.

## Learning Curves

Plot training/validation performance theo training-set size giúp diagnose:

- cả hai error cao và gần nhau → possible high bias;
- training tốt, validation kém với gap lớn → high variance;
- validation tiếp tục improve rõ khi thêm data → more data likely useful.

Learning curve thực dụng hơn việc gắn label “overfit” chỉ từ một metric snapshot.

## Cross-Validation

k-fold cross-validation chia data thành `k` folds; mỗi lần train trên `k-1`, validate fold còn lại.

Nó giảm dependence vào một random split và estimate variability.

Nhưng random k-fold không hợp mọi problem:

- time series cần forward/time split;
- multiple rows cùng user cần group split;
- spatial data có autocorrelation cần spatial split.

Validation scheme phải mimic deployment boundary.

## Distribution Shift

Generalization theory thường assume train/test từ same hoặc related distribution. Production lại gặp shift.

Các dạng hữu ích:

- **covariate shift**: `P(X)` đổi;
- **label/prior shift**: `P(Y)` đổi;
- **concept shift**: relationship `P(Y|X)` đổi.

Ví dụ fraud behavior thay vì attacker adapt là concept drift.

Model có excellent IID test score vẫn có thể fail dưới shift.

## Shortcut Learning

Model có thể exploit correlation dễ nhưng không robust.

Ví dụ medical image classifier học hospital watermark thay vì pathology. Training/test random split cùng source có score cao, nhưng external hospital performance collapse.

Đây là generalization failure do representation/data design, không chỉ “overfitting” theo parameter count.

## Spurious Correlation

Nếu feature tương quan target vì historical accident, model có thể dùng nó. Khi deployment context thay, correlation mất.

Domain knowledge và stress tests cần để detect reliance vào brittle signals.

## Double Descent

Classical intuition nói test error giảm rồi tăng khi complexity vượt optimum. Modern overparameterized models đôi khi cho **double descent**: error tăng gần interpolation threshold rồi giảm lại khi model cực overparameterized.

Điều này nhắc rằng bias–variance vẫn là mental framework hữu ích nhưng simple U-shaped curve không mô tả đầy đủ Deep Learning.

## Ensemble và Variance

Bagging/Random Forest giảm variance bằng averaging partially independent models.

Boosting thường giảm bias qua additive correction nhưng cũng có regularization mechanisms như shrinkage/tree depth/subsampling.

Xem: [Ensemble Learning](./09_ensemble_learning.md).

## Generalization trong LLM

LLM pretraining không chỉ “memorize internet”; model học statistical patterns và representations cho phép generalize tới unseen combinations/tasks. Nhưng memorization vẫn tồn tại, đặc biệt rare sequences.

In-context learning, domain shift, contamination và benchmark leakage làm generalization evaluation phức tạp hơn supervised tabular ML.

Các chapter LLM sau sẽ mở rộng distinction này.

## Mental Model

```text
Observed sample
   ↓ learning algorithm + inductive bias
Chosen hypothesis
   ↓
Performance on new distribution
```

Nếu fail, hãy hỏi bốn tầng:

```text
Representation có đủ signal?
Model capacity phù hợp?
Learning/regularization chọn solution nào?
Validation có giống deployment distribution?
```

## Common Misconceptions

### “Overfitting = model quá nhiều parameters”

Parameter count chỉ là một factor; data, architecture, regularization, optimization và task matter.

### “Train và test đều tốt thì model đã robust”

Chỉ nếu test đại diện deployment. IID split có thể bỏ lỡ shift/shortcut.

### “Thêm data luôn giải quyết overfitting”

Chỉ khi data mới informative, diverse và relevant.

### “Bias–variance bias là fairness bias”

Không. Đây là statistical estimation bias; fairness bias là concept khác.

## Knowledge Connection

Generalization nối [Statistics for AI](../01_mathematical_foundations/03_statistics_for_ai.md), [Learning Problem and Inductive Bias](./01_learning_problem_and_inductive_bias.md), [Training/Validation/Testing](./03_training_validation_and_testing.md), [Ensemble Learning](./09_ensemble_learning.md) và [Model Evaluation](./15_model_evaluation.md).